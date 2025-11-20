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
from tencentcloud.dbbrain.v20191016 import models
from typing import Dict


class DbbrainClient(AbstractClient):
    _apiVersion = '2019-10-16'
    _endpoint = 'dbbrain.intl.tencentcloudapi.com'
    _service = 'dbbrain'

    async def AddUserContact(
            self,
            request: models.AddUserContactRequest,
            opts: Dict = None,
    ) -> models.AddUserContactResponse:
        """
        This API is used to add the contact name and email.. The return value is the successfully added contact ID. Select Guangzhou for Region.
        """
        
        kwargs = {}
        kwargs["action"] = "AddUserContact"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUserContactResponse
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
        
    async def CreateMailProfile(
            self,
            request: models.CreateMailProfileRequest,
            opts: Dict = None,
    ) -> models.CreateMailProfileResponse:
        """
        This API is used to create the email configuration. The input parameter `ProfileType` represents the type of the email configuration. Valid values: `dbScan_mail_configuration` (email configuration of database inspection report) and `scheduler_mail_configuration` (email sending configuration of regularly generated health report). Select Guangzhou for Region, regardless of the region where the instance belongs.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMailProfile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMailProfileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSchedulerMailProfile(
            self,
            request: models.CreateSchedulerMailProfileRequest,
            opts: Dict = None,
    ) -> models.CreateSchedulerMailProfileResponse:
        """
        This API is used to create the regular generation time of the health reports and the regular email sending configuration. Pass in the regular generation time of the health reports as a parameter (Monday to Sunday) to set the regular generation time of the health reports, and save the corresponding regular email sending configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSchedulerMailProfile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSchedulerMailProfileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllUserContact(
            self,
            request: models.DescribeAllUserContactRequest,
            opts: Dict = None,
    ) -> models.DescribeAllUserContactResponse:
        """
        This API is used to obtain the information of the contact in the email.
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
        This API is used to obtain the information of the contact group in the email.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllUserGroupResponse
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
        This API is used to obtain the instance information list. Select Guangzhou for Region.
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
        This API is used to obtain the health score and deduction for exceptions in the specified time period (30 minutes) based on the instance ID.
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
        This API is used to obtain the email sending configurations, including the email configuration for database inspection and the email sending configuration for regularly generated health reports. Select Guangzhou for Region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMailProfile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMailProfileResponse
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
        This API is used to obtain the statistical distribution chart of slow log source addresses.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogUserHostStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogUserHostStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopSpaceSchemaTimeSeries(
            self,
            request: models.DescribeTopSpaceSchemaTimeSeriesRequest,
            opts: Dict = None,
    ) -> models.DescribeTopSpaceSchemaTimeSeriesResponse:
        """
        This API is used to query the daily space data of top databases consuming the most instance space. The data is daily collected by DBbrain during a specified time period. The return results are sorted by size by default.
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
        This API is used to query real-time space statistics of top databases. The return results are sorted by size by default.
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
        This API is used to query the daily space data of top tables consuming the most instance space. The data is daily collected by DBbrain during a specified time period. The return results are sorted by size by default.
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
        This API is used to query real-time space statistics of top tables of an instance. The return results are sorted by size by default.
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
        This API is used to obtain SQL statement optimization suggestions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserSqlAdvice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserSqlAdviceResponse
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