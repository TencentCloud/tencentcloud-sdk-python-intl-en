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

from tencentcloud.common.abstract_model import AbstractModel


class ContactItem(AbstractModel):
    """Contact description.

    """

    def __init__(self):
        """
        :param Id: Contact ID.
        :type Id: int
        :param Name: Contact name.
        :type Name: str
        :param Mail: The email address of the contact.
        :type Mail: str
        """
        self.Id = None
        self.Name = None
        self.Mail = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Mail = params.get("Mail")


class CreateDBDiagReportTaskRequest(AbstractModel):
    """CreateDBDiagReportTask request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param StartTime: Start time, such as `2020-11-08T14:00:00+08:00`.
        :type StartTime: str
        :param EndTime: End time, such as `2020-11-09T14:00:00+08:00`.
        :type EndTime: str
        :param SendMailFlag: Whether to send an email. Valid values: 0 - Yes, 1 - No.
        :type SendMailFlag: int
        :param ContactPerson: An array of contact IDs to receive the email.
        :type ContactPerson: list of int
        :param ContactGroup: An array of contact group IDs to receive the email.
        :type ContactGroup: list of int
        :param Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.SendMailFlag = None
        self.ContactPerson = None
        self.ContactGroup = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SendMailFlag = params.get("SendMailFlag")
        self.ContactPerson = params.get("ContactPerson")
        self.ContactGroup = params.get("ContactGroup")
        self.Product = params.get("Product")


class CreateDBDiagReportTaskResponse(AbstractModel):
    """CreateDBDiagReportTask response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: ID of an async task request, which can be used to query the execution result of an async task.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AsyncRequestId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateMailProfileRequest(AbstractModel):
    """CreateMailProfile request structure.

    """

    def __init__(self):
        """
        :param ProfileInfo: Email configurations
        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20191016.models.ProfileInfo`
        :param ProfileLevel: Configuration level. Valid values: "User" (user-level), "Instance" (instance-level). For database inspection report, it should be `User`; and for scheduled task reports, it should be `Instance`.
        :type ProfileLevel: str
        :param ProfileName: Configuration name, which needs to be unique. For database inspection reports, this name can be customize as needed. For scheduled task reports, the name should be in the format of "scheduler_" + {instanceId}, such as "schduler_cdb-test".
        :type ProfileName: str
        :param ProfileType: Configuration type. Valid values: "dbScan_mail_configuration" (email configuration of database inspection report), "scheduler_mail_configuration" (email configuration of scheduled task report).
        :type ProfileType: str
        :param Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)).
        :type Product: str
        :param BindInstanceIds: Instance ID bound to the configuration, which is required when the configuration level is `Instance`.
        :type BindInstanceIds: list of str
        """
        self.ProfileInfo = None
        self.ProfileLevel = None
        self.ProfileName = None
        self.ProfileType = None
        self.Product = None
        self.BindInstanceIds = None


    def _deserialize(self, params):
        if params.get("ProfileInfo") is not None:
            self.ProfileInfo = ProfileInfo()
            self.ProfileInfo._deserialize(params.get("ProfileInfo"))
        self.ProfileLevel = params.get("ProfileLevel")
        self.ProfileName = params.get("ProfileName")
        self.ProfileType = params.get("ProfileType")
        self.Product = params.get("Product")
        self.BindInstanceIds = params.get("BindInstanceIds")


class CreateMailProfileResponse(AbstractModel):
    """CreateMailProfile response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAllUserContactRequest(AbstractModel):
    """DescribeAllUserContact request structure.

    """

    def __init__(self):
        """
        :param Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)).
        :type Product: str
        :param Names: An array of contact name. Fuzzy search is supported.
        :type Names: list of str
        """
        self.Product = None
        self.Names = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.Names = params.get("Names")


class DescribeAllUserContactResponse(AbstractModel):
    """DescribeAllUserContact response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of contacts.
        :type TotalCount: int
        :param Contacts: Contact information.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Contacts: list of ContactItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Contacts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Contacts") is not None:
            self.Contacts = []
            for item in params.get("Contacts"):
                obj = ContactItem()
                obj._deserialize(item)
                self.Contacts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAllUserGroupRequest(AbstractModel):
    """DescribeAllUserGroup request structure.

    """

    def __init__(self):
        """
        :param Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)).
        :type Product: str
        :param Names: An array of contact group name. Fuzzy search is supported.
        :type Names: list of str
        """
        self.Product = None
        self.Names = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.Names = params.get("Names")


class DescribeAllUserGroupResponse(AbstractModel):
    """DescribeAllUserGroup response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of contact groups.
        :type TotalCount: int
        :param Groups: Contact group information.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Groups: list of GroupItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Groups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = GroupItem()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBDiagEventRequest(AbstractModel):
    """DescribeDBDiagEvent request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param EventId: Event ID, which can be obtained through the `DescribeDBDiagHistory` API.
        :type EventId: int
        :param Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self.InstanceId = None
        self.EventId = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EventId = params.get("EventId")
        self.Product = params.get("Product")


class DescribeDBDiagEventResponse(AbstractModel):
    """DescribeDBDiagEvent response structure.

    """

    def __init__(self):
        """
        :param DiagItem: Diagnosis item.
        :type DiagItem: str
        :param DiagType: Diagnosis type.
        :type DiagType: str
        :param EventId: Event ID.
        :type EventId: int
        :param Explanation: Event details.
        :type Explanation: str
        :param Outline: Summary.
        :type Outline: str
        :param Problem: Problem found.
        :type Problem: str
        :param Severity: Severity, which can be divided into 5 levels: 1: fatal, 2: severe, 3: warning, 4: notice, 5: healthy.
        :type Severity: int
        :param StartTime: Start time
        :type StartTime: str
        :param Suggestions: Suggestion.
        :type Suggestions: str
        :param Metric: Reserved field.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Metric: str
        :param EndTime: End time.
        :type EndTime: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DiagItem = None
        self.DiagType = None
        self.EventId = None
        self.Explanation = None
        self.Outline = None
        self.Problem = None
        self.Severity = None
        self.StartTime = None
        self.Suggestions = None
        self.Metric = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DiagItem = params.get("DiagItem")
        self.DiagType = params.get("DiagType")
        self.EventId = params.get("EventId")
        self.Explanation = params.get("Explanation")
        self.Outline = params.get("Outline")
        self.Problem = params.get("Problem")
        self.Severity = params.get("Severity")
        self.StartTime = params.get("StartTime")
        self.Suggestions = params.get("Suggestions")
        self.Metric = params.get("Metric")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class DescribeDBDiagHistoryRequest(AbstractModel):
    """DescribeDBDiagHistory request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param StartTime: Start time, such as "2019-09-10 12:13:14".
        :type StartTime: str
        :param EndTime: End time, such as "2019-09-11 12:13:14". The interval between the end time and the start time can be up to 2 days.
        :type EndTime: str
        :param Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Product = params.get("Product")


class DescribeDBDiagHistoryResponse(AbstractModel):
    """DescribeDBDiagHistory response structure.

    """

    def __init__(self):
        """
        :param Events: Event description.
        :type Events: list of DiagHistoryEventItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Events = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = DiagHistoryEventItem()
                obj._deserialize(item)
                self.Events.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBSpaceStatusRequest(AbstractModel):
    """DescribeDBSpaceStatus request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param RangeDays: Query period in days. The end date is the current date and the query period is 7 days by default.
        :type RangeDays: int
        :param Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self.InstanceId = None
        self.RangeDays = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RangeDays = params.get("RangeDays")
        self.Product = params.get("Product")


class DescribeDBSpaceStatusResponse(AbstractModel):
    """DescribeDBSpaceStatus response structure.

    """

    def __init__(self):
        """
        :param Growth: Disk usage growth in MB.
        :type Growth: int
        :param Remain: Available disk space in MB.
        :type Remain: int
        :param Total: Total disk space in MB.
        :type Total: int
        :param AvailableDays: Estimated number of available days.
        :type AvailableDays: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Growth = None
        self.Remain = None
        self.Total = None
        self.AvailableDays = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Growth = params.get("Growth")
        self.Remain = params.get("Remain")
        self.Total = params.get("Total")
        self.AvailableDays = params.get("AvailableDays")
        self.RequestId = params.get("RequestId")


class DescribeSlowLogTimeSeriesStatsRequest(AbstractModel):
    """DescribeSlowLogTimeSeriesStats request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param StartTime: Start time, such as "2019-09-10 12:13:14".
        :type StartTime: str
        :param EndTime: End time, such as "2019-09-10 12:13:14". The interval between the end time and the start time can be up to 7 days.
        :type EndTime: str
        :param Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Product = params.get("Product")


class DescribeSlowLogTimeSeriesStatsResponse(AbstractModel):
    """DescribeSlowLogTimeSeriesStats response structure.

    """

    def __init__(self):
        """
        :param Period: Time range in seconds in histogram.
        :type Period: int
        :param TimeSeries: Number of slow logs in specified time range.
        :type TimeSeries: list of TimeSlice
        :param SeriesData: Instance CPU utilization monitoring data in specified time range.
        :type SeriesData: :class:`tencentcloud.dbbrain.v20191016.models.MonitorMetricSeriesData`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Period = None
        self.TimeSeries = None
        self.SeriesData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        if params.get("TimeSeries") is not None:
            self.TimeSeries = []
            for item in params.get("TimeSeries"):
                obj = TimeSlice()
                obj._deserialize(item)
                self.TimeSeries.append(obj)
        if params.get("SeriesData") is not None:
            self.SeriesData = MonitorMetricSeriesData()
            self.SeriesData._deserialize(params.get("SeriesData"))
        self.RequestId = params.get("RequestId")


class DescribeSlowLogTopSqlsRequest(AbstractModel):
    """DescribeSlowLogTopSqls request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param StartTime: Start time, such as "2019-09-10 12:13:14".
        :type StartTime: str
        :param EndTime: End time, such as "2019-09-10 12:13:14". The interval between the end time and the start time can be up to 7 days.
        :type EndTime: str
        :param SortBy: Sorting key. Valid values: QueryTime, ExecTimes, RowsSent, LockTime, RowsExamined.
        :type SortBy: str
        :param OrderBy: Sorting order. Valid values: ASC (ascending), DESC (descending).
        :type OrderBy: str
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param SchemaList: Database name array.
        :type SchemaList: list of SchemaItem
        :param Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.SortBy = None
        self.OrderBy = None
        self.Limit = None
        self.Offset = None
        self.SchemaList = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SortBy = params.get("SortBy")
        self.OrderBy = params.get("OrderBy")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("SchemaList") is not None:
            self.SchemaList = []
            for item in params.get("SchemaList"):
                obj = SchemaItem()
                obj._deserialize(item)
                self.SchemaList.append(obj)
        self.Product = params.get("Product")


class DescribeSlowLogTopSqlsResponse(AbstractModel):
    """DescribeSlowLogTopSqls response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param Rows: List of top slow SQL statements
        :type Rows: list of SlowLogTopSqlItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = SlowLogTopSqlItem()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopSpaceTableTimeSeriesRequest(AbstractModel):
    """DescribeTopSpaceTableTimeSeries request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param Limit: Number of returned top tables. Default value: 20. Maximum value: 20.
        :type Limit: int
        :param SortBy: Field used to sort top tables. Valid values: DataLength, IndexLength, TotalLength, DataFree, FragRatio, TableRows, PhysicalFileSize. Default value: PhysicalFileSize.
        :type SortBy: str
        :param StartDate: Start date. It can be as early as 29 days before the current date, and defaults to 6 days before the end date.
        :type StartDate: str
        :param EndDate: End date. It can be as early as 29 days before the current date, and defaults to the current date.
        :type EndDate: str
        :param Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self.InstanceId = None
        self.Limit = None
        self.SortBy = None
        self.StartDate = None
        self.EndDate = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Product = params.get("Product")


class DescribeTopSpaceTableTimeSeriesResponse(AbstractModel):
    """DescribeTopSpaceTableTimeSeries response structure.

    """

    def __init__(self):
        """
        :param TopSpaceTableTimeSeries: Time series list of the returned space statistics of top tables.
        :type TopSpaceTableTimeSeries: list of TableSpaceTimeSeries
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TopSpaceTableTimeSeries = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopSpaceTableTimeSeries") is not None:
            self.TopSpaceTableTimeSeries = []
            for item in params.get("TopSpaceTableTimeSeries"):
                obj = TableSpaceTimeSeries()
                obj._deserialize(item)
                self.TopSpaceTableTimeSeries.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopSpaceTablesRequest(AbstractModel):
    """DescribeTopSpaceTables request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param Limit: Number of returned top tables. Default value: 20. Maximum value: 20.
        :type Limit: int
        :param SortBy: Field used to sort top tables. Valid values: DataLength, IndexLength, TotalLength, DataFree, FragRatio, TableRows, PhysicalFileSize. Default value: PhysicalFileSize.
        :type SortBy: str
        :param Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self.InstanceId = None
        self.Limit = None
        self.SortBy = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")
        self.Product = params.get("Product")


class DescribeTopSpaceTablesResponse(AbstractModel):
    """DescribeTopSpaceTables response structure.

    """

    def __init__(self):
        """
        :param TopSpaceTables: List of the returned space statistics of top tables.
        :type TopSpaceTables: list of TableSpaceData
        :param Timestamp: Timestamp (in seconds) of tablespace data collect points
        :type Timestamp: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TopSpaceTables = None
        self.Timestamp = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopSpaceTables") is not None:
            self.TopSpaceTables = []
            for item in params.get("TopSpaceTables"):
                obj = TableSpaceData()
                obj._deserialize(item)
                self.TopSpaceTables.append(obj)
        self.Timestamp = params.get("Timestamp")
        self.RequestId = params.get("RequestId")


class DiagHistoryEventItem(AbstractModel):
    """Instance diagnosis event

    """

    def __init__(self):
        """
        :param DiagType: Diagnosis type.
        :type DiagType: str
        :param EndTime: End time.
        :type EndTime: str
        :param StartTime: Start time.
        :type StartTime: str
        :param EventId: Event ID.
        :type EventId: int
        :param Severity: Severity, which can be divided into 5 levels: 1: fatal, 2: severe, 3: warning, 4: notice, 5: healthy.
        :type Severity: int
        :param Outline: Summary.
        :type Outline: str
        :param DiagItem: Diagnosis item.
        :type DiagItem: str
        :param InstanceId: Instance ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param Metric: Reserved field
Note: this field may return null, indicating that no valid values can be obtained.
        :type Metric: str
        :param Region: Region
Note: this field may return null, indicating that no valid values can be obtained.
        :type Region: str
        """
        self.DiagType = None
        self.EndTime = None
        self.StartTime = None
        self.EventId = None
        self.Severity = None
        self.Outline = None
        self.DiagItem = None
        self.InstanceId = None
        self.Metric = None
        self.Region = None


    def _deserialize(self, params):
        self.DiagType = params.get("DiagType")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.EventId = params.get("EventId")
        self.Severity = params.get("Severity")
        self.Outline = params.get("Outline")
        self.DiagItem = params.get("DiagItem")
        self.InstanceId = params.get("InstanceId")
        self.Metric = params.get("Metric")
        self.Region = params.get("Region")


class GroupItem(AbstractModel):
    """Describe the group information.

    """

    def __init__(self):
        """
        :param Id: Group ID.
        :type Id: int
        :param Name: Group name.
        :type Name: str
        :param MemberCount: Number of group members.
        :type MemberCount: int
        """
        self.Id = None
        self.Name = None
        self.MemberCount = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.MemberCount = params.get("MemberCount")


class InstanceConfs(AbstractModel):
    """Instance configuration.

    """

    def __init__(self):
        """
        :param DailyInspection: Whether to enable database inspection. Valid values: Yes/No.
        :type DailyInspection: str
        """
        self.DailyInspection = None


    def _deserialize(self, params):
        self.DailyInspection = params.get("DailyInspection")


class MailConfiguration(AbstractModel):
    """Email sending configuration.

    """

    def __init__(self):
        """
        :param SendMail: Whether to enable email sending. Valid values: 0 (No), 1 (Yes).
        :type SendMail: int
        :param Region: Region configuration, such as "ap-guangzhou", "ap-shanghai".
        :type Region: list of str
        :param HealthStatus: Sending a report with the specified health level, such as "HEALTH", "SUB_HEALTH", "RISK", "HIGH_RISK".
        :type HealthStatus: list of str
        :param ContactPerson: Contact ID. Either `ContactGroup` or `ContactID` should be passed in.
        :type ContactPerson: list of int
        :param ContactGroup: Contact group ID. Either `ContactGroup` or `ContactID` should be passed in.
        :type ContactGroup: list of int
        """
        self.SendMail = None
        self.Region = None
        self.HealthStatus = None
        self.ContactPerson = None
        self.ContactGroup = None


    def _deserialize(self, params):
        self.SendMail = params.get("SendMail")
        self.Region = params.get("Region")
        self.HealthStatus = params.get("HealthStatus")
        self.ContactPerson = params.get("ContactPerson")
        self.ContactGroup = params.get("ContactGroup")


class ModifyDiagDBInstanceConfRequest(AbstractModel):
    """ModifyDiagDBInstanceConf request structure.

    """

    def __init__(self):
        """
        :param InstanceConfs: Whether to enable inspection
        :type InstanceConfs: :class:`tencentcloud.dbbrain.v20191016.models.InstanceConfs`
        :param Regions: Target regions of the request. If the value is `All`, it is applied to all regions.
        :type Regions: str
        :param Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)).
        :type Product: str
        :param InstanceIds: ID of the instance to modify.
        :type InstanceIds: list of str
        """
        self.InstanceConfs = None
        self.Regions = None
        self.Product = None
        self.InstanceIds = None


    def _deserialize(self, params):
        if params.get("InstanceConfs") is not None:
            self.InstanceConfs = InstanceConfs()
            self.InstanceConfs._deserialize(params.get("InstanceConfs"))
        self.Regions = params.get("Regions")
        self.Product = params.get("Product")
        self.InstanceIds = params.get("InstanceIds")


class ModifyDiagDBInstanceConfResponse(AbstractModel):
    """ModifyDiagDBInstanceConf response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MonitorFloatMetric(AbstractModel):
    """Monitoring data in float type

    """

    def __init__(self):
        """
        :param Metric: Metric name.
        :type Metric: str
        :param Unit: Metric unit.
        :type Unit: str
        :param Values: Metric value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Values: list of float
        """
        self.Metric = None
        self.Unit = None
        self.Values = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        self.Unit = params.get("Unit")
        self.Values = params.get("Values")


class MonitorFloatMetricSeriesData(AbstractModel):
    """Monitoring metric value in float type in a unit of time interval

    """

    def __init__(self):
        """
        :param Series: Monitoring metric.
        :type Series: list of MonitorFloatMetric
        :param Timestamp: Timestamp corresponding to monitoring metric.
        :type Timestamp: list of int
        """
        self.Series = None
        self.Timestamp = None


    def _deserialize(self, params):
        if params.get("Series") is not None:
            self.Series = []
            for item in params.get("Series"):
                obj = MonitorFloatMetric()
                obj._deserialize(item)
                self.Series.append(obj)
        self.Timestamp = params.get("Timestamp")


class MonitorMetric(AbstractModel):
    """Monitoring data

    """

    def __init__(self):
        """
        :param Metric: Metric name.
        :type Metric: str
        :param Unit: Metric unit.
        :type Unit: str
        :param Values: Metric value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Values: list of int
        """
        self.Metric = None
        self.Unit = None
        self.Values = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        self.Unit = params.get("Unit")
        self.Values = params.get("Values")


class MonitorMetricSeriesData(AbstractModel):
    """Monitoring metric data in specified time range

    """

    def __init__(self):
        """
        :param Series: Monitoring metric.
        :type Series: list of MonitorMetric
        :param Timestamp: Timestamp corresponding to monitoring metric.
        :type Timestamp: list of int
        """
        self.Series = None
        self.Timestamp = None


    def _deserialize(self, params):
        if params.get("Series") is not None:
            self.Series = []
            for item in params.get("Series"):
                obj = MonitorMetric()
                obj._deserialize(item)
                self.Series.append(obj)
        self.Timestamp = params.get("Timestamp")


class ProfileInfo(AbstractModel):
    """Information configured by user.

    """

    def __init__(self):
        """
        :param Language: Language of the email, such as `en`.
        :type Language: str
        :param MailConfiguration: The content of email template.
        :type MailConfiguration: :class:`tencentcloud.dbbrain.v20191016.models.MailConfiguration`
        """
        self.Language = None
        self.MailConfiguration = None


    def _deserialize(self, params):
        self.Language = params.get("Language")
        if params.get("MailConfiguration") is not None:
            self.MailConfiguration = MailConfiguration()
            self.MailConfiguration._deserialize(params.get("MailConfiguration"))


class SchemaItem(AbstractModel):
    """`SchemaItem` array

    """

    def __init__(self):
        """
        :param Schema: Database name
        :type Schema: str
        """
        self.Schema = None


    def _deserialize(self, params):
        self.Schema = params.get("Schema")


class SlowLogTopSqlItem(AbstractModel):
    """Top slow SQL statements

    """

    def __init__(self):
        """
        :param LockTime: Total SQL lock wait time
        :type LockTime: float
        :param LockTimeMax: Maximum lock wait time
        :type LockTimeMax: float
        :param LockTimeMin: Minimum lock wait time
        :type LockTimeMin: float
        :param RowsExamined: Total number of scanned rows
        :type RowsExamined: int
        :param RowsExaminedMax: Maximum number of scanned rows
        :type RowsExaminedMax: int
        :param RowsExaminedMin: Minimum number of scanned rows
        :type RowsExaminedMin: int
        :param QueryTime: Total duration
        :type QueryTime: float
        :param QueryTimeMax: Maximum execution time
        :type QueryTimeMax: float
        :param QueryTimeMin: Minimum execution time
        :type QueryTimeMin: float
        :param RowsSent: Total number of returned rows
        :type RowsSent: int
        :param RowsSentMax: Maximum number of returned rows
        :type RowsSentMax: int
        :param RowsSentMin: Minimum number of returned rows
        :type RowsSentMin: int
        :param ExecTimes: Number of executions
        :type ExecTimes: int
        :param SqlTemplate: SQL template
        :type SqlTemplate: str
        :param SqlText: SQL with parameter (random)
        :type SqlText: str
        :param Schema: Database name
        :type Schema: str
        :param QueryTimeRatio: Ratio of total duration
        :type QueryTimeRatio: float
        :param LockTimeRatio: Ratio of total SQL lock wait time
        :type LockTimeRatio: float
        :param RowsExaminedRatio: Ratio of total number of scanned rows
        :type RowsExaminedRatio: float
        :param RowsSentRatio: Ratio of total number of returned rows
        :type RowsSentRatio: float
        """
        self.LockTime = None
        self.LockTimeMax = None
        self.LockTimeMin = None
        self.RowsExamined = None
        self.RowsExaminedMax = None
        self.RowsExaminedMin = None
        self.QueryTime = None
        self.QueryTimeMax = None
        self.QueryTimeMin = None
        self.RowsSent = None
        self.RowsSentMax = None
        self.RowsSentMin = None
        self.ExecTimes = None
        self.SqlTemplate = None
        self.SqlText = None
        self.Schema = None
        self.QueryTimeRatio = None
        self.LockTimeRatio = None
        self.RowsExaminedRatio = None
        self.RowsSentRatio = None


    def _deserialize(self, params):
        self.LockTime = params.get("LockTime")
        self.LockTimeMax = params.get("LockTimeMax")
        self.LockTimeMin = params.get("LockTimeMin")
        self.RowsExamined = params.get("RowsExamined")
        self.RowsExaminedMax = params.get("RowsExaminedMax")
        self.RowsExaminedMin = params.get("RowsExaminedMin")
        self.QueryTime = params.get("QueryTime")
        self.QueryTimeMax = params.get("QueryTimeMax")
        self.QueryTimeMin = params.get("QueryTimeMin")
        self.RowsSent = params.get("RowsSent")
        self.RowsSentMax = params.get("RowsSentMax")
        self.RowsSentMin = params.get("RowsSentMin")
        self.ExecTimes = params.get("ExecTimes")
        self.SqlTemplate = params.get("SqlTemplate")
        self.SqlText = params.get("SqlText")
        self.Schema = params.get("Schema")
        self.QueryTimeRatio = params.get("QueryTimeRatio")
        self.LockTimeRatio = params.get("LockTimeRatio")
        self.RowsExaminedRatio = params.get("RowsExaminedRatio")
        self.RowsSentRatio = params.get("RowsSentRatio")


class TableSpaceData(AbstractModel):
    """Database table space statistics.

    """

    def __init__(self):
        """
        :param TableName: Table name.
        :type TableName: str
        :param TableSchema: Database name.
        :type TableSchema: str
        :param Engine: Database table storage engine.
        :type Engine: str
        :param DataLength: Data space in MB.
        :type DataLength: float
        :param IndexLength: Index space in MB.
        :type IndexLength: float
        :param DataFree: Fragmented space in MB.
        :type DataFree: float
        :param TotalLength: Total space usage in MB.
        :type TotalLength: float
        :param FragRatio: Fragmented rate (%).
        :type FragRatio: float
        :param TableRows: Number of rows.
        :type TableRows: int
        :param PhysicalFileSize: Size in MB of the physical file exclusive to a table.
        :type PhysicalFileSize: float
        """
        self.TableName = None
        self.TableSchema = None
        self.Engine = None
        self.DataLength = None
        self.IndexLength = None
        self.DataFree = None
        self.TotalLength = None
        self.FragRatio = None
        self.TableRows = None
        self.PhysicalFileSize = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.TableSchema = params.get("TableSchema")
        self.Engine = params.get("Engine")
        self.DataLength = params.get("DataLength")
        self.IndexLength = params.get("IndexLength")
        self.DataFree = params.get("DataFree")
        self.TotalLength = params.get("TotalLength")
        self.FragRatio = params.get("FragRatio")
        self.TableRows = params.get("TableRows")
        self.PhysicalFileSize = params.get("PhysicalFileSize")


class TableSpaceTimeSeries(AbstractModel):
    """Time series of database table space data

    """

    def __init__(self):
        """
        :param TableName: Table name.
        :type TableName: str
        :param TableSchema: Database name.
        :type TableSchema: str
        :param Engine: Database table storage engine.
        :type Engine: str
        :param SeriesData: Monitoring metric data in a unit of time interval.
        :type SeriesData: :class:`tencentcloud.dbbrain.v20191016.models.MonitorFloatMetricSeriesData`
        """
        self.TableName = None
        self.TableSchema = None
        self.Engine = None
        self.SeriesData = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.TableSchema = params.get("TableSchema")
        self.Engine = params.get("Engine")
        if params.get("SeriesData") is not None:
            self.SeriesData = MonitorFloatMetricSeriesData()
            self.SeriesData._deserialize(params.get("SeriesData"))


class TimeSlice(AbstractModel):
    """Slow log statistics in specified time range

    """

    def __init__(self):
        """
        :param Count: Total number
        :type Count: int
        :param Timestamp: Statistics start time
        :type Timestamp: int
        """
        self.Count = None
        self.Timestamp = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Timestamp = params.get("Timestamp")