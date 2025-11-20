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
from tencentcloud.dbbrain.v20210527 import models
from typing import Dict


class DbbrainClient(AbstractClient):
    _apiVersion = '2021-05-27'
    _endpoint = 'dbbrain.intl.tencentcloudapi.com'
    _service = 'dbbrain'

    async def AddUserContact(
            self,
            request: models.AddUserContactRequest,
            opts: Dict = None,
    ) -> models.AddUserContactResponse:
        """
        This API is used to add the recipient name and email. The returned value is the ID of the successfully added recipient.
        """
        
        kwargs = {}
        kwargs["action"] = "AddUserContact"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUserContactResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseAuditService(
            self,
            request: models.CloseAuditServiceRequest,
            opts: Dict = None,
    ) -> models.CloseAuditServiceResponse:
        """
        This API is used to disable database audit as needed.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBDiagReportTask(
            self,
            request: models.CreateDBDiagReportTaskRequest,
            opts: Dict = None,
    ) -> models.CreateDBDiagReportTaskResponse:
        """
        This API is used to create a health report and send it via email as configured.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBDiagReportTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBDiagReportTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBDiagReportUrl(
            self,
            request: models.CreateDBDiagReportUrlRequest,
            opts: Dict = None,
    ) -> models.CreateDBDiagReportUrlResponse:
        """
        This API is used to create a URL for a health report.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBDiagReportUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBDiagReportUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateKillTask(
            self,
            request: models.CreateKillTaskRequest,
            opts: Dict = None,
    ) -> models.CreateKillTaskResponse:
        """
        This API is used to create a session killing task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateKillTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateKillTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMailProfile(
            self,
            request: models.CreateMailProfileRequest,
            opts: Dict = None,
    ) -> models.CreateMailProfileResponse:
        """
        This API is used to create the email configuration. The input parameter `ProfileType` represents the type of the email configuration. Valid values: `dbScan_mail_configuration` (email configuration of database inspection report) and `scheduler_mail_configuration` (email sending configuration of scheduled task health report). Always select Guangzhou for `Region`, regardless of the region where the instance resides.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMailProfile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMailProfileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProxySessionKillTask(
            self,
            request: models.CreateProxySessionKillTaskRequest,
            opts: Dict = None,
    ) -> models.CreateProxySessionKillTaskResponse:
        """
        This API is used to create an async task of killing all proxy node connection sessions and is currently supported only for Redis. The async task ID is the returned value, which can be passed to the API `DescribeProxySessionKillTasks` as a parameter to query the execution status of the session killing task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProxySessionKillTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProxySessionKillTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRedisBigKeyAnalysisTask(
            self,
            request: models.CreateRedisBigKeyAnalysisTaskRequest,
            opts: Dict = None,
    ) -> models.CreateRedisBigKeyAnalysisTaskResponse:
        """
        This API is used to create an ad hoc big key analysis task for Redis instances. By default, there can only be up to five running ad hoc analysis tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRedisBigKeyAnalysisTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRedisBigKeyAnalysisTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSchedulerMailProfile(
            self,
            request: models.CreateSchedulerMailProfileRequest,
            opts: Dict = None,
    ) -> models.CreateSchedulerMailProfileResponse:
        """
        This API is used to create the regular generation time of health reports and the regular email sending configuration. Pass in the regular generation time of health reports as a parameter (Monday to Sunday) to set the regular generation time, and save the corresponding regular email sending configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSchedulerMailProfile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSchedulerMailProfileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityAuditLogExportTask(
            self,
            request: models.CreateSecurityAuditLogExportTaskRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityAuditLogExportTaskResponse:
        """
        This API is used to create a security audit log export task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityAuditLogExportTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityAuditLogExportTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDBDiagReportTasks(
            self,
            request: models.DeleteDBDiagReportTasksRequest,
            opts: Dict = None,
    ) -> models.DeleteDBDiagReportTasksResponse:
        """
        This API is used to delete health report generation tasks by task ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDBDiagReportTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDBDiagReportTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityAuditLogExportTasks(
            self,
            request: models.DeleteSecurityAuditLogExportTasksRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityAuditLogExportTasksResponse:
        """
        This API is used to delete a security audit log export task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityAuditLogExportTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityAuditLogExportTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllUserContact(
            self,
            request: models.DescribeAllUserContactRequest,
            opts: Dict = None,
    ) -> models.DescribeAllUserContactResponse:
        """
        This API is used to get the information of the recipient in the email.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllUserContact"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllUserContactResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllUserGroup(
            self,
            request: models.DescribeAllUserGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeAllUserGroupResponse:
        """
        This API is used to get the information of the recipient group in the email.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditInstanceList(
            self,
            request: models.DescribeAuditInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditInstanceListResponse:
        """
        This API is used to query the instance list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBDiagEvent(
            self,
            request: models.DescribeDBDiagEventRequest,
            opts: Dict = None,
    ) -> models.DescribeDBDiagEventResponse:
        """
        This API is used to get the details of an instance exception diagnosis event.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBDiagEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBDiagEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBDiagEvents(
            self,
            request: models.DescribeDBDiagEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBDiagEventsResponse:
        """
        This API is used to obtain the diagnosis event list in a specified time period by risk level, instance ID, etc.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBDiagEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBDiagEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBDiagHistory(
            self,
            request: models.DescribeDBDiagHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeDBDiagHistoryResponse:
        """
        This API is used to get the list of instance diagnosis events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBDiagHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBDiagHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBDiagReportTasks(
            self,
            request: models.DescribeDBDiagReportTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeDBDiagReportTasksResponse:
        """
        This API is used to query the list of health report generation tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBDiagReportTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBDiagReportTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSpaceStatus(
            self,
            request: models.DescribeDBSpaceStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSpaceStatusResponse:
        """
        This API is used to query the overview of instance space usage during a specified time period, including disk usage growth (MB), available disk space (MB), total disk space (MB), and estimated number of available days.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSpaceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSpaceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDiagDBInstances(
            self,
            request: models.DescribeDiagDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDiagDBInstancesResponse:
        """
        This API is used to get the instance information list. Please always select Guangzhou for `Region`.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDiagDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDiagDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHealthScore(
            self,
            request: models.DescribeHealthScoreRequest,
            opts: Dict = None,
    ) -> models.DescribeHealthScoreResponse:
        """
        This API is used to get the health score and deduction for exceptions in the specified time period (30 minutes) based on the instance ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHealthScore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHealthScoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMailProfile(
            self,
            request: models.DescribeMailProfileRequest,
            opts: Dict = None,
    ) -> models.DescribeMailProfileResponse:
        """
        This API is used to get the email sending configuration, including the email configuration for database inspection and the email sending configuration for scheduled task health reports.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMailProfile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMailProfileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMySqlProcessList(
            self,
            request: models.DescribeMySqlProcessListRequest,
            opts: Dict = None,
    ) -> models.DescribeMySqlProcessListResponse:
        """
        This API is used to query the real-time thread list of a relational database.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMySqlProcessList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMySqlProcessListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxyProcessStatistics(
            self,
            request: models.DescribeProxyProcessStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyProcessStatisticsResponse:
        """
        This API is used to get the session statistics of a single proxy under the current instance, and can only be called in particular environments.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyProcessStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyProcessStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxySessionKillTasks(
            self,
            request: models.DescribeProxySessionKillTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeProxySessionKillTasksResponse:
        """
        This API is used to query the result of the session killing task executed by the Redis proxy node. The async task ID (an input parameter) is obtained after the API `CreateProxySessionKillTask` is successfully called. Currently, the only valid value of `product` is `redis`.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxySessionKillTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxySessionKillTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRedisTopKeyPrefixList(
            self,
            request: models.DescribeRedisTopKeyPrefixListRequest,
            opts: Dict = None,
    ) -> models.DescribeRedisTopKeyPrefixListResponse:
        """
        This API is used to query the list of top key prefixes for Redis instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRedisTopKeyPrefixList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRedisTopKeyPrefixListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityAuditLogDownloadUrls(
            self,
            request: models.DescribeSecurityAuditLogDownloadUrlsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityAuditLogDownloadUrlsResponse:
        """
        This API is used to query the download link of a security audit log export file. Currently, log file download only provides a Tencent Cloud private network address. Download it by using a CVM instance in the Guangzhou region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityAuditLogDownloadUrls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityAuditLogDownloadUrlsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityAuditLogExportTasks(
            self,
            request: models.DescribeSecurityAuditLogExportTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityAuditLogExportTasksResponse:
        """
        This API is used to query the list of security audit log export tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityAuditLogExportTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityAuditLogExportTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogTimeSeriesStats(
            self,
            request: models.DescribeSlowLogTimeSeriesStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogTimeSeriesStatsResponse:
        """
        This API is used to get the slow log statistics histogram.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogTimeSeriesStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogTimeSeriesStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogTopSqls(
            self,
            request: models.DescribeSlowLogTopSqlsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogTopSqlsResponse:
        """
        This API is used to get and sort the top slow SQL statements in a specified time period by the aggregation mode of SQL template plus schema.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogTopSqls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogTopSqlsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogUserHostStats(
            self,
            request: models.DescribeSlowLogUserHostStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogUserHostStatsResponse:
        """
        This API is used to get the statistical distribution chart of slow log source addresses.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogUserHostStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogUserHostStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogs(
            self,
            request: models.DescribeSlowLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogsResponse:
        """
        This API is used to obtain the slow log details of a SQL template in a specified time period.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopSpaceSchemaTimeSeries(
            self,
            request: models.DescribeTopSpaceSchemaTimeSeriesRequest,
            opts: Dict = None,
    ) -> models.DescribeTopSpaceSchemaTimeSeriesResponse:
        """
        This API is used to get the daily space data of top databases consuming the most instance space. The data is daily collected by DBbrain during a specified time period. The returned results are sorted by size by default.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopSpaceSchemaTimeSeries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopSpaceSchemaTimeSeriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopSpaceSchemas(
            self,
            request: models.DescribeTopSpaceSchemasRequest,
            opts: Dict = None,
    ) -> models.DescribeTopSpaceSchemasResponse:
        """
        This API is used to get the real-time space statistics of top databases of an instance. The returned results are sorted by size by default.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopSpaceSchemas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopSpaceSchemasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopSpaceTableTimeSeries(
            self,
            request: models.DescribeTopSpaceTableTimeSeriesRequest,
            opts: Dict = None,
    ) -> models.DescribeTopSpaceTableTimeSeriesResponse:
        """
        This API is used to get the daily space data of top tables consuming the most instance space. The data is daily collected by DBbrain during a specified time period. The returned results are sorted by size by default.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopSpaceTableTimeSeries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopSpaceTableTimeSeriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopSpaceTables(
            self,
            request: models.DescribeTopSpaceTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeTopSpaceTablesResponse:
        """
        This API is used to get the real-time space statistics of top tables of an instance. The returned results are sorted by size by default.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopSpaceTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopSpaceTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserSqlAdvice(
            self,
            request: models.DescribeUserSqlAdviceRequest,
            opts: Dict = None,
    ) -> models.DescribeUserSqlAdviceResponse:
        """
        This API is used to get SQL statement optimization suggestions. It is free of charge for a limited time and will be charged after DBbrain is commercialized.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserSqlAdvice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserSqlAdviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KillMySqlThreads(
            self,
            request: models.KillMySqlThreadsRequest,
            opts: Dict = None,
    ) -> models.KillMySqlThreadsResponse:
        """
        This API is used to interrupt the current session by session ID. It needs to be called twice to commit the session interruption task in two stages. In the pre-commit stage, the stage value is `Prepare`, and the returned value is `SqlExecId`. In the commit stage, the stage value is `Commit`, and `SqlExecId` will be passed in as a parameter. Then, the session process will be terminated.
        """
        
        kwargs = {}
        kwargs["action"] = "KillMySqlThreads"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KillMySqlThreadsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuditService(
            self,
            request: models.ModifyAuditServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyAuditServiceResponse:
        """
        u200cThis API is used to modify audit configurations such as the frequent access storage period.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDiagDBInstanceConf(
            self,
            request: models.ModifyDiagDBInstanceConfRequest,
            opts: Dict = None,
    ) -> models.ModifyDiagDBInstanceConfResponse:
        """
        This API is used to enable/disable instance inspection.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDiagDBInstanceConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDiagDBInstanceConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenAuditService(
            self,
            request: models.OpenAuditServiceRequest,
            opts: Dict = None,
    ) -> models.OpenAuditServiceResponse:
        """
        This API is used to enable database audit.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)