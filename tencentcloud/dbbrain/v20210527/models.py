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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AddUserContactRequest(AbstractModel):
    """AddUserContact request structure.

    """

    def __init__(self):
        """
        :param Name: Contact name, which must be unique, can contain 2–60 letters, digits, and underscores, and cannot start with an underscore.\n        :type Name: str\n        :param ContactInfo: Email address, which can contain letters, digits, and underscores and cannot start with an underscore.\n        :type ContactInfo: str\n        :param Product: Service type, which is fixed to `mysql`.\n        :type Product: str\n        """
        self.Name = None
        self.ContactInfo = None
        self.Product = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ContactInfo = params.get("ContactInfo")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserContactResponse(AbstractModel):
    """AddUserContact response structure.

    """

    def __init__(self):
        """
        :param Id: ID of successfully added contact.\n        :type Id: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class ContactItem(AbstractModel):
    """Contact description.

    """

    def __init__(self):
        """
        :param Id: Contact ID.\n        :type Id: int\n        :param Name: Contact name.\n        :type Name: str\n        :param Mail: Contact email.\n        :type Mail: str\n        """
        self.Id = None
        self.Name = None
        self.Mail = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Mail = params.get("Mail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBDiagReportTaskRequest(AbstractModel):
    """CreateDBDiagReportTask request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param StartTime: Start time, such as "2020-11-08T14:00:00+08:00".\n        :type StartTime: str\n        :param EndTime: End time, such as "2020-11-09T14:00:00+08:00".\n        :type EndTime: str\n        :param SendMailFlag: Whether to send an email. Valid values: 0 (yes), 1 (no).\n        :type SendMailFlag: int\n        :param ContactPerson: Array of contact IDs to receive email.\n        :type ContactPerson: list of int\n        :param ContactGroup: Array of contact group IDs to receive email.\n        :type ContactGroup: list of int\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBDiagReportTaskResponse(AbstractModel):
    """CreateDBDiagReportTask response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AsyncRequestId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateDBDiagReportUrlRequest(AbstractModel):
    """CreateDBDiagReportUrl request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param AsyncRequestId: Health report task ID, which can be queried through `DescribeDBDiagReportTasks`.\n        :type AsyncRequestId: int\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        """
        self.InstanceId = None
        self.AsyncRequestId = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBDiagReportUrlResponse(AbstractModel):
    """CreateDBDiagReportUrl response structure.

    """

    def __init__(self):
        """
        :param ReportUrl: Health report URL.\n        :type ReportUrl: str\n        :param ExpireTime: Expiration timestamp of health report URL (in seconds).\n        :type ExpireTime: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ReportUrl = None
        self.ExpireTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReportUrl = params.get("ReportUrl")
        self.ExpireTime = params.get("ExpireTime")
        self.RequestId = params.get("RequestId")


class CreateMailProfileRequest(AbstractModel):
    """CreateMailProfile request structure.

    """

    def __init__(self):
        """
        :param ProfileInfo: Email configuration.\n        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20210527.models.ProfileInfo`\n        :param ProfileLevel: Configuration level. Valid values: User (user-level), Instance (instance-level). For database inspection emails, it should be `User`. For scheduled task emails, it should be `Instance`.\n        :type ProfileLevel: str\n        :param ProfileName: Configuration name, which needs to be unique. For database inspection emails, this name can be customized as needed. For scheduled task emails, the name should be in the format of "scheduler_" + {instanceId}, such as "schduler_cdb-test".\n        :type ProfileName: str\n        :param ProfileType: Configuration type. Valid values: "dbScan_mail_configuration" (email configuration of database inspection report), "scheduler_mail_configuration" (email configuration of scheduled task report).\n        :type ProfileType: str\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL).\n        :type Product: str\n        :param BindInstanceIds: Instance ID bound with the configuration, which is set when the configuration level is `Instance`. Only one instance can be bound at a time. When the configuration level is `User`, leave this parameter empty.\n        :type BindInstanceIds: list of str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMailProfileResponse(AbstractModel):
    """CreateMailProfile response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSchedulerMailProfileRequest(AbstractModel):
    """CreateSchedulerMailProfile request structure.

    """

    def __init__(self):
        """
        :param WeekConfiguration: Value range: 1–7, representing Monday to Sunday respectively.\n        :type WeekConfiguration: list of int\n        :param ProfileInfo: Email configuration.\n        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20210527.models.ProfileInfo`\n        :param ProfileName: Configuration name, which needs to be unique. For scheduled task emails, the name should be in the format of "scheduler_" + {instanceId}, such as "schduler_cdb-test".\n        :type ProfileName: str\n        :param BindInstanceId: ID of the instance for which to configure subscription.\n        :type BindInstanceId: str\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        """
        self.WeekConfiguration = None
        self.ProfileInfo = None
        self.ProfileName = None
        self.BindInstanceId = None
        self.Product = None


    def _deserialize(self, params):
        self.WeekConfiguration = params.get("WeekConfiguration")
        if params.get("ProfileInfo") is not None:
            self.ProfileInfo = ProfileInfo()
            self.ProfileInfo._deserialize(params.get("ProfileInfo"))
        self.ProfileName = params.get("ProfileName")
        self.BindInstanceId = params.get("BindInstanceId")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSchedulerMailProfileResponse(AbstractModel):
    """CreateSchedulerMailProfile response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSecurityAuditLogExportTaskRequest(AbstractModel):
    """CreateSecurityAuditLogExportTask request structure.

    """

    def __init__(self):
        """
        :param SecAuditGroupId: Security audit group ID.\n        :type SecAuditGroupId: str\n        :param StartTime: Exported log start time, such as 2020-12-28 00:00:00.\n        :type StartTime: str\n        :param EndTime: Exported log end time, such as 2020-12-28 01:00:00.\n        :type EndTime: str\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL).\n        :type Product: str\n        :param DangerLevels: Log risk level list. Valid values: 0 (no risk), 1 (low risk), 2 (medium risk), 3 (high risk).\n        :type DangerLevels: list of int\n        """
        self.SecAuditGroupId = None
        self.StartTime = None
        self.EndTime = None
        self.Product = None
        self.DangerLevels = None


    def _deserialize(self, params):
        self.SecAuditGroupId = params.get("SecAuditGroupId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Product = params.get("Product")
        self.DangerLevels = params.get("DangerLevels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityAuditLogExportTaskResponse(AbstractModel):
    """CreateSecurityAuditLogExportTask response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Log export task Id.\n        :type AsyncRequestId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class DeleteSecurityAuditLogExportTasksRequest(AbstractModel):
    """DeleteSecurityAuditLogExportTasks request structure.

    """

    def __init__(self):
        """
        :param SecAuditGroupId: Security audit group ID.\n        :type SecAuditGroupId: str\n        :param AsyncRequestIds: Log export task ID list. This API will ignore task IDs that do not exist or have been deleted.\n        :type AsyncRequestIds: list of int non-negative\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL).\n        :type Product: str\n        """
        self.SecAuditGroupId = None
        self.AsyncRequestIds = None
        self.Product = None


    def _deserialize(self, params):
        self.SecAuditGroupId = params.get("SecAuditGroupId")
        self.AsyncRequestIds = params.get("AsyncRequestIds")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityAuditLogExportTasksResponse(AbstractModel):
    """DeleteSecurityAuditLogExportTasks response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAllUserContactRequest(AbstractModel):
    """DescribeAllUserContact request structure.

    """

    def __init__(self):
        """
        :param Product: Service type, which is fixed to `mysql`.\n        :type Product: str\n        :param Names: Array of contact names. Fuzzy search is supported.\n        :type Names: list of str\n        """
        self.Product = None
        self.Names = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllUserContactResponse(AbstractModel):
    """DescribeAllUserContact response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of contacts.\n        :type TotalCount: int\n        :param Contacts: Contact information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Contacts: list of ContactItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Product: Service type, which is fixed to `mysql`.\n        :type Product: str\n        :param Names: Array of contact group names. Fuzzy search is supported.\n        :type Names: list of str\n        """
        self.Product = None
        self.Names = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllUserGroupResponse(AbstractModel):
    """DescribeAllUserGroup response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of groups.\n        :type TotalCount: int\n        :param Groups: Group information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Groups: list of GroupItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param EventId: Event ID, which can be obtained through the `DescribeDBDiagHistory` API.\n        :type EventId: int\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        """
        self.InstanceId = None
        self.EventId = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EventId = params.get("EventId")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagEventResponse(AbstractModel):
    """DescribeDBDiagEvent response structure.

    """

    def __init__(self):
        """
        :param DiagItem: Diagnosis item.\n        :type DiagItem: str\n        :param DiagType: Diagnosis type.\n        :type DiagType: str\n        :param EventId: Event ID.\n        :type EventId: int\n        :param Explanation: Event details.\n        :type Explanation: str\n        :param Outline: Summary.\n        :type Outline: str\n        :param Problem: Found problem.\n        :type Problem: str\n        :param Severity: Severity, which can be divided into 5 levels: 1: fatal, 2: severe, 3: warning, 4: notice, 5: healthy.\n        :type Severity: int\n        :param StartTime: Start time\n        :type StartTime: str\n        :param Suggestions: Suggestion.\n        :type Suggestions: str\n        :param Metric: Reserved field.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Metric: str\n        :param EndTime: End time.\n        :type EndTime: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param StartTime: Start time, such as "2019-09-10 12:13:14".\n        :type StartTime: str\n        :param EndTime: End time, such as "2019-09-11 12:13:14". The interval between the end time and the start time can be up to 2 days.\n        :type EndTime: str\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagHistoryResponse(AbstractModel):
    """DescribeDBDiagHistory response structure.

    """

    def __init__(self):
        """
        :param Events: Event description.\n        :type Events: list of DiagHistoryEventItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeDBDiagReportTasksRequest(AbstractModel):
    """DescribeDBDiagReportTasks request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start time of the first task in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14. It is used for queries by time range.\n        :type StartTime: str\n        :param EndTime: End time of the last task in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14. It is used for queries by time range.\n        :type EndTime: str\n        :param InstanceIds: Array of instance IDs, which is used to filter the task list of a specified instance.\n        :type InstanceIds: list of str\n        :param Sources: Source that triggers the task. Valid values: `DAILY_INSPECTION` (instance inspection), `SCHEDULED` (scheduled task), and `MANUAL` (manual trigger).\n        :type Sources: list of str\n        :param HealthLevels: Health level. Valid values: `HEALTH` (healthy), `SUB_HEALTH` (suboptimal), `RISK` (risky), and `HIGH_RISK` (critical).\n        :type HealthLevels: str\n        :param TaskStatuses: Task status. Valid values: `created` (created), `chosen` (to be executed), `running` (being executed), `failed` (failed), and `finished` (completed).\n        :type TaskStatuses: str\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        """
        self.StartTime = None
        self.EndTime = None
        self.InstanceIds = None
        self.Sources = None
        self.HealthLevels = None
        self.TaskStatuses = None
        self.Offset = None
        self.Limit = None
        self.Product = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InstanceIds = params.get("InstanceIds")
        self.Sources = params.get("Sources")
        self.HealthLevels = params.get("HealthLevels")
        self.TaskStatuses = params.get("TaskStatuses")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagReportTasksResponse(AbstractModel):
    """DescribeDBDiagReportTasks response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of tasks.\n        :type TotalCount: int\n        :param Tasks: Task list.\n        :type Tasks: list of HealthReportTask\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = HealthReportTask()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBSpaceStatusRequest(AbstractModel):
    """DescribeDBSpaceStatus request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param RangeDays: Query period in days. The end date is the current date, and the query period is 7 days by default.\n        :type RangeDays: int\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        """
        self.InstanceId = None
        self.RangeDays = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RangeDays = params.get("RangeDays")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSpaceStatusResponse(AbstractModel):
    """DescribeDBSpaceStatus response structure.

    """

    def __init__(self):
        """
        :param Growth: Disk usage growth in MB.\n        :type Growth: int\n        :param Remain: Available disk space in MB.\n        :type Remain: int\n        :param Total: Total disk space in MB.\n        :type Total: int\n        :param AvailableDays: Estimated number of available days.\n        :type AvailableDays: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeDiagDBInstancesRequest(AbstractModel):
    """DescribeDiagDBInstances request structure.

    """

    def __init__(self):
        """
        :param IsSupported: Whether it is an instance supported by DBbrain. It is fixed to `true`.\n        :type IsSupported: bool\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        :param Offset: Pagination parameter indicating the offset.\n        :type Offset: int\n        :param Limit: Pagination parameter. Maximum value: 100.\n        :type Limit: int\n        :param InstanceNames: Query by instance name.\n        :type InstanceNames: list of str\n        :param InstanceIds: Query by instance ID.\n        :type InstanceIds: list of str\n        :param Regions: Query by region.\n        :type Regions: list of str\n        """
        self.IsSupported = None
        self.Product = None
        self.Offset = None
        self.Limit = None
        self.InstanceNames = None
        self.InstanceIds = None
        self.Regions = None


    def _deserialize(self, params):
        self.IsSupported = params.get("IsSupported")
        self.Product = params.get("Product")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceNames = params.get("InstanceNames")
        self.InstanceIds = params.get("InstanceIds")
        self.Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiagDBInstancesResponse(AbstractModel):
    """DescribeDiagDBInstances response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of instances.\n        :type TotalCount: int\n        :param DbScanStatus: Status of all instance inspection. 0: all instance inspection enabled, 1: all instance inspection disabled.\n        :type DbScanStatus: int\n        :param Items: Instance information.\n        :type Items: list of InstanceInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.DbScanStatus = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.DbScanStatus = params.get("DbScanStatus")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHealthScoreRequest(AbstractModel):
    """DescribeHealthScore request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID for which to get the health score.\n        :type InstanceId: str\n        :param Time: Time to get the health score.\n        :type Time: str\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        """
        self.InstanceId = None
        self.Time = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Time = params.get("Time")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHealthScoreResponse(AbstractModel):
    """DescribeHealthScore response structure.

    """

    def __init__(self):
        """
        :param Data: Health score and deduction for exceptions.\n        :type Data: :class:`tencentcloud.dbbrain.v20210527.models.HealthScoreInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = HealthScoreInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeMailProfileRequest(AbstractModel):
    """DescribeMailProfile request structure.

    """

    def __init__(self):
        """
        :param ProfileType: Configuration type. Valid values: "dbScan_mail_configuration" (email configuration of database inspection report), "scheduler_mail_configuration" (email configuration of scheduled task report).\n        :type ProfileType: str\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        :param Offset: Pagination offset.\n        :type Offset: int\n        :param Limit: Number of results per page in paginated queries. Maximum value: 50.\n        :type Limit: int\n        :param ProfileName: Query by email configuration name. The name of the scheduled task email configuration should be in the format of "scheduler_"+{instanceId}.\n        :type ProfileName: str\n        """
        self.ProfileType = None
        self.Product = None
        self.Offset = None
        self.Limit = None
        self.ProfileName = None


    def _deserialize(self, params):
        self.ProfileType = params.get("ProfileType")
        self.Product = params.get("Product")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProfileName = params.get("ProfileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMailProfileResponse(AbstractModel):
    """DescribeMailProfile response structure.

    """

    def __init__(self):
        """
        :param ProfileList: Email configuration details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProfileList: list of UserProfile\n        :param TotalCount: Total number of email templates.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ProfileList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProfileList") is not None:
            self.ProfileList = []
            for item in params.get("ProfileList"):
                obj = UserProfile()
                obj._deserialize(item)
                self.ProfileList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMySqlProcessListRequest(AbstractModel):
    """DescribeMySqlProcessList request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param ID: Thread ID, which is used to filter the thread list.\n        :type ID: int\n        :param User: Thread operation account name, which is used to filter the thread list.\n        :type User: str\n        :param Host: Thread operation host address, which is used to filter the thread list.\n        :type Host: str\n        :param DB: Thread operation database, which is used to filter the thread list.\n        :type DB: str\n        :param State: Thread operation status, which is used to filter the thread list.\n        :type State: str\n        :param Command: Thread execution type, which is used to filter the thread list.\n        :type Command: str\n        :param Time: Minimum operation duration of the thread in seconds, which is used to filter the list of threads whose operation duration is greater than this value.\n        :type Time: int\n        :param Info: Thread operation statement, which is used to filter the thread list.\n        :type Info: str\n        :param Limit: Number of returned results. Default value: 20.\n        :type Limit: int\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        """
        self.InstanceId = None
        self.ID = None
        self.User = None
        self.Host = None
        self.DB = None
        self.State = None
        self.Command = None
        self.Time = None
        self.Info = None
        self.Limit = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ID = params.get("ID")
        self.User = params.get("User")
        self.Host = params.get("Host")
        self.DB = params.get("DB")
        self.State = params.get("State")
        self.Command = params.get("Command")
        self.Time = params.get("Time")
        self.Info = params.get("Info")
        self.Limit = params.get("Limit")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMySqlProcessListResponse(AbstractModel):
    """DescribeMySqlProcessList response structure.

    """

    def __init__(self):
        """
        :param ProcessList: List of real-time threads.\n        :type ProcessList: list of MySqlProcess\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ProcessList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProcessList") is not None:
            self.ProcessList = []
            for item in params.get("ProcessList"):
                obj = MySqlProcess()
                obj._deserialize(item)
                self.ProcessList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityAuditLogDownloadUrlsRequest(AbstractModel):
    """DescribeSecurityAuditLogDownloadUrls request structure.

    """

    def __init__(self):
        """
        :param SecAuditGroupId: Security audit group ID.\n        :type SecAuditGroupId: str\n        :param AsyncRequestId: Async task Id.\n        :type AsyncRequestId: int\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL).\n        :type Product: str\n        """
        self.SecAuditGroupId = None
        self.AsyncRequestId = None
        self.Product = None


    def _deserialize(self, params):
        self.SecAuditGroupId = params.get("SecAuditGroupId")
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityAuditLogDownloadUrlsResponse(AbstractModel):
    """DescribeSecurityAuditLogDownloadUrls response structure.

    """

    def __init__(self):
        """
        :param Urls: List of COS URLs of the export results. If the result set is large, it may be divided into multiple URLs for download.\n        :type Urls: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Urls = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.RequestId = params.get("RequestId")


class DescribeSecurityAuditLogExportTasksRequest(AbstractModel):
    """DescribeSecurityAuditLogExportTasks request structure.

    """

    def __init__(self):
        """
        :param SecAuditGroupId: Security audit group ID.\n        :type SecAuditGroupId: str\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL).\n        :type Product: str\n        :param AsyncRequestIds: List of log export task IDs.\n        :type AsyncRequestIds: list of int non-negative\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        """
        self.SecAuditGroupId = None
        self.Product = None
        self.AsyncRequestIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SecAuditGroupId = params.get("SecAuditGroupId")
        self.Product = params.get("Product")
        self.AsyncRequestIds = params.get("AsyncRequestIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityAuditLogExportTasksResponse(AbstractModel):
    """DescribeSecurityAuditLogExportTasks response structure.

    """

    def __init__(self):
        """
        :param Tasks: List of security audit log export tasks.\n        :type Tasks: list of SecLogExportTaskInfo\n        :param TotalCount: Total numbers of security audit log export tasks.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Tasks = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = SecLogExportTaskInfo()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSlowLogTimeSeriesStatsRequest(AbstractModel):
    """DescribeSlowLogTimeSeriesStats request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param StartTime: Start time, such as "2019-09-10 12:13:14".\n        :type StartTime: str\n        :param EndTime: End time, such as "2019-09-10 12:13:14". The interval between the end time and the start time can be up to 7 days.\n        :type EndTime: str\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogTimeSeriesStatsResponse(AbstractModel):
    """DescribeSlowLogTimeSeriesStats response structure.

    """

    def __init__(self):
        """
        :param Period: Time range in seconds in histogram.\n        :type Period: int\n        :param TimeSeries: Number of slow logs in specified time range.\n        :type TimeSeries: list of TimeSlice\n        :param SeriesData: Instance CPU utilization monitoring data in specified time range.\n        :type SeriesData: :class:`tencentcloud.dbbrain.v20210527.models.MonitorMetricSeriesData`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param StartTime: Start time, such as "2019-09-10 12:13:14".\n        :type StartTime: str\n        :param EndTime: End time, such as "2019-09-10 12:13:14". The interval between the end time and the start time can be up to 7 days.\n        :type EndTime: str\n        :param SortBy: Sorting key. Valid values: QueryTime, ExecTimes, RowsSent, LockTime, RowsExamined. Default value: QueryTime.\n        :type SortBy: str\n        :param OrderBy: Sorting order. Valid values: ASC (ascending), DESC (descending). Default value: DESC.\n        :type OrderBy: str\n        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param SchemaList: Database name array.\n        :type SchemaList: list of SchemaItem\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogTopSqlsResponse(AbstractModel):
    """DescribeSlowLogTopSqls response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param Rows: List of top slow SQL statements\n        :type Rows: list of SlowLogTopSqlItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeSlowLogUserHostStatsRequest(AbstractModel):
    """DescribeSlowLogUserHostStats request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param StartTime: Start time of the time range in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14.\n        :type StartTime: str\n        :param EndTime: End time of the time range in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14.\n        :type EndTime: str\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogUserHostStatsResponse(AbstractModel):
    """DescribeSlowLogUserHostStats response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of source addresses.\n        :type TotalCount: int\n        :param Items: Detailed list of the proportion of slow logs from each source address.\n        :type Items: list of SlowLogHost\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = SlowLogHost()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopSpaceSchemaTimeSeriesRequest(AbstractModel):
    """DescribeTopSpaceSchemaTimeSeries request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param Limit: Number of returned top databases. Maximum value: 100. Default value: 20.\n        :type Limit: int\n        :param SortBy: Field used to sort top databases. Valid values: DataLength, IndexLength, TotalLength, DataFree, FragRatio, TableRows, PhysicalFileSize (supported only by TencentDB for MySQL instances). For TencentDB for MySQL instances, the default value is `PhysicalFileSize`. For other database instances, the default value is `TotalLength`.\n        :type SortBy: str\n        :param StartDate: Start date, such as "2021-01-01". It can be as early as 29 days before the current date and is 6 days before the end date by default.\n        :type StartDate: str\n        :param EndDate: End date, such as "2021-01-01". It can be as early as 29 days before the current date and is the current date by default.\n        :type EndDate: str\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceSchemaTimeSeriesResponse(AbstractModel):
    """DescribeTopSpaceSchemaTimeSeries response structure.

    """

    def __init__(self):
        """
        :param TopSpaceSchemaTimeSeries: Time series list of the returned space statistics of top databases.\n        :type TopSpaceSchemaTimeSeries: list of SchemaSpaceTimeSeries\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TopSpaceSchemaTimeSeries = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopSpaceSchemaTimeSeries") is not None:
            self.TopSpaceSchemaTimeSeries = []
            for item in params.get("TopSpaceSchemaTimeSeries"):
                obj = SchemaSpaceTimeSeries()
                obj._deserialize(item)
                self.TopSpaceSchemaTimeSeries.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopSpaceSchemasRequest(AbstractModel):
    """DescribeTopSpaceSchemas request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param Limit: Number of returned top databases. Maximum value: 100. Default value: 20.\n        :type Limit: int\n        :param SortBy: Field used to sort top databases. Valid values: DataLength, IndexLength, TotalLength, DataFree, FragRatio, TableRows, PhysicalFileSize (supported only by TencentDB for MySQL instances). For TencentDB for MySQL instances, the default value is `PhysicalFileSize`. For other database instances, the default value is `TotalLength`.\n        :type SortBy: str\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        """
        self.InstanceId = None
        self.Limit = None
        self.SortBy = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceSchemasResponse(AbstractModel):
    """DescribeTopSpaceSchemas response structure.

    """

    def __init__(self):
        """
        :param TopSpaceSchemas: List of the returned space statistics of top databases.\n        :type TopSpaceSchemas: list of SchemaSpaceData\n        :param Timestamp: Timestamp (in seconds) of database space data collection points\n        :type Timestamp: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TopSpaceSchemas = None
        self.Timestamp = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopSpaceSchemas") is not None:
            self.TopSpaceSchemas = []
            for item in params.get("TopSpaceSchemas"):
                obj = SchemaSpaceData()
                obj._deserialize(item)
                self.TopSpaceSchemas.append(obj)
        self.Timestamp = params.get("Timestamp")
        self.RequestId = params.get("RequestId")


class DescribeTopSpaceTableTimeSeriesRequest(AbstractModel):
    """DescribeTopSpaceTableTimeSeries request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param Limit: Number of returned top tables. Maximum value: 100. Default value: 20.\n        :type Limit: int\n        :param SortBy: Field used to sort top tables. Valid values: DataLength, IndexLength, TotalLength, DataFree, FragRatio, TableRows, PhysicalFileSize. Default value: PhysicalFileSize.\n        :type SortBy: str\n        :param StartDate: Start date, such as "2021-01-01". It can be as early as 29 days before the current date and is 6 days before the end date by default.\n        :type StartDate: str\n        :param EndDate: End date, such as "2021-01-01". It can be as early as 29 days before the current date and is the current date by default.\n        :type EndDate: str\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceTableTimeSeriesResponse(AbstractModel):
    """DescribeTopSpaceTableTimeSeries response structure.

    """

    def __init__(self):
        """
        :param TopSpaceTableTimeSeries: Time series list of the returned space statistics of top tables.\n        :type TopSpaceTableTimeSeries: list of TableSpaceTimeSeries\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param Limit: Number of returned top tables. Maximum value: 100. Default value: 20.\n        :type Limit: int\n        :param SortBy: Field used to sort top tables. Valid values: DataLength, IndexLength, TotalLength, DataFree, FragRatio, TableRows, PhysicalFileSize (only supported for TencentDB for MySQL instances). For TencentDB for MySQL instances, the default value is `PhysicalFileSize`. For other database instances, the default value is `TotalLength`.\n        :type SortBy: str\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.\n        :type Product: str\n        """
        self.InstanceId = None
        self.Limit = None
        self.SortBy = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceTablesResponse(AbstractModel):
    """DescribeTopSpaceTables response structure.

    """

    def __init__(self):
        """
        :param TopSpaceTables: List of the returned space statistics of top tables.\n        :type TopSpaceTables: list of TableSpaceData\n        :param Timestamp: Timestamp (in seconds) of tablespace data collection points\n        :type Timestamp: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeUserSqlAdviceRequest(AbstractModel):
    """DescribeUserSqlAdvice request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param SqlText: SQL statement.\n        :type SqlText: str\n        :param Schema: Database name.\n        :type Schema: str\n        """
        self.InstanceId = None
        self.SqlText = None
        self.Schema = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SqlText = params.get("SqlText")
        self.Schema = params.get("Schema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserSqlAdviceResponse(AbstractModel):
    """DescribeUserSqlAdvice response structure.

    """

    def __init__(self):
        """
        :param Advices: SQL statement optimization suggestions, which can be parsed into JSON arrays.\n        :type Advices: str\n        :param Comments: Notes of SQL statement optimization suggestions, which can be parsed into String arrays.\n        :type Comments: str\n        :param SqlText: SQL statement.\n        :type SqlText: str\n        :param Schema: Database name.\n        :type Schema: str\n        :param Tables: DDL information of related tables, which can be parsed into JSON arrays.\n        :type Tables: str\n        :param SqlPlan: SQL execution plan, which can be parsed into JSON.\n        :type SqlPlan: str\n        :param Cost: Cost saving details after SQL statement optimization, which can be parsed into JSON.\n        :type Cost: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Advices = None
        self.Comments = None
        self.SqlText = None
        self.Schema = None
        self.Tables = None
        self.SqlPlan = None
        self.Cost = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Advices = params.get("Advices")
        self.Comments = params.get("Comments")
        self.SqlText = params.get("SqlText")
        self.Schema = params.get("Schema")
        self.Tables = params.get("Tables")
        self.SqlPlan = params.get("SqlPlan")
        self.Cost = params.get("Cost")
        self.RequestId = params.get("RequestId")


class DiagHistoryEventItem(AbstractModel):
    """Instance diagnosis event

    """

    def __init__(self):
        """
        :param DiagType: Diagnosis type.\n        :type DiagType: str\n        :param EndTime: End time.\n        :type EndTime: str\n        :param StartTime: Start time.\n        :type StartTime: str\n        :param EventId: Event ID.\n        :type EventId: int\n        :param Severity: Severity, which can be divided into 5 levels: 1: fatal, 2: severe, 3: warning, 4: notice, 5: healthy.\n        :type Severity: int\n        :param Outline: Summary.\n        :type Outline: str\n        :param DiagItem: Diagnosis item.\n        :type DiagItem: str\n        :param InstanceId: Instance ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InstanceId: str\n        :param Metric: Reserved field
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Metric: str\n        :param Region: Region
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Region: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventInfo(AbstractModel):
    """Exception information.

    """

    def __init__(self):
        """
        :param EventId: Event ID.\n        :type EventId: int\n        :param DiagType: Diagnosis type.\n        :type DiagType: str\n        :param StartTime: Start time.\n        :type StartTime: str\n        :param EndTime: End time.\n        :type EndTime: str\n        :param Outline: Summary.\n        :type Outline: str\n        :param Severity: Severity, which can be divided into 5 levels: 1: fatal, 2: severe, 3: warning, 4: notice, 5: healthy.\n        :type Severity: int\n        :param ScoreLost: Deduction.\n        :type ScoreLost: int\n        :param Metric: Reserved field.\n        :type Metric: str\n        :param Count: Number of alarms.\n        :type Count: int\n        """
        self.EventId = None
        self.DiagType = None
        self.StartTime = None
        self.EndTime = None
        self.Outline = None
        self.Severity = None
        self.ScoreLost = None
        self.Metric = None
        self.Count = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.DiagType = params.get("DiagType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Outline = params.get("Outline")
        self.Severity = params.get("Severity")
        self.ScoreLost = params.get("ScoreLost")
        self.Metric = params.get("Metric")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupItem(AbstractModel):
    """Describes the group information.

    """

    def __init__(self):
        """
        :param Id: Group ID.\n        :type Id: int\n        :param Name: Group name.\n        :type Name: str\n        :param MemberCount: Number of group members.\n        :type MemberCount: int\n        """
        self.Id = None
        self.Name = None
        self.MemberCount = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.MemberCount = params.get("MemberCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthReportTask(AbstractModel):
    """Details of health report task.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID.\n        :type AsyncRequestId: int\n        :param Source: Source that triggers the task. Valid values: `DAILY_INSPECTION` (instance inspection), `SCHEDULED` (scheduled task), and `MANUAL` (manual trigger).\n        :type Source: str\n        :param Progress: Task progress in %.\n        :type Progress: int\n        :param CreateTime: Task creation time.\n        :type CreateTime: str\n        :param StartTime: Task start time.\n        :type StartTime: str\n        :param EndTime: Task end time.\n        :type EndTime: str\n        :param InstanceInfo: Basic information of the instance to which the task belongs.\n        :type InstanceInfo: :class:`tencentcloud.dbbrain.v20210527.models.InstanceBasicInfo`\n        :param HealthStatus: Health information in health report.\n        :type HealthStatus: :class:`tencentcloud.dbbrain.v20210527.models.HealthStatus`\n        """
        self.AsyncRequestId = None
        self.Source = None
        self.Progress = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.InstanceInfo = None
        self.HealthStatus = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.Source = params.get("Source")
        self.Progress = params.get("Progress")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("InstanceInfo") is not None:
            self.InstanceInfo = InstanceBasicInfo()
            self.InstanceInfo._deserialize(params.get("InstanceInfo"))
        if params.get("HealthStatus") is not None:
            self.HealthStatus = HealthStatus()
            self.HealthStatus._deserialize(params.get("HealthStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthScoreInfo(AbstractModel):
    """Details of the obtained health score.

    """

    def __init__(self):
        """
        :param IssueTypes: Exception details.\n        :type IssueTypes: list of IssueTypeInfo\n        :param EventsTotalCount: Total number of exceptions.\n        :type EventsTotalCount: int\n        :param HealthScore: Health score.\n        :type HealthScore: int\n        :param HealthLevel: Health level, such as "HEALTH", "SUB_HEALTH", "RISK", and "HIGH_RISK".\n        :type HealthLevel: str\n        """
        self.IssueTypes = None
        self.EventsTotalCount = None
        self.HealthScore = None
        self.HealthLevel = None


    def _deserialize(self, params):
        if params.get("IssueTypes") is not None:
            self.IssueTypes = []
            for item in params.get("IssueTypes"):
                obj = IssueTypeInfo()
                obj._deserialize(item)
                self.IssueTypes.append(obj)
        self.EventsTotalCount = params.get("EventsTotalCount")
        self.HealthScore = params.get("HealthScore")
        self.HealthLevel = params.get("HealthLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthStatus(AbstractModel):
    """Instance health status.

    """

    def __init__(self):
        """
        :param HealthScore: Health score out of 100 points.\n        :type HealthScore: int\n        :param HealthLevel: Health level. Valid values: `HEALTH` (healthy), `SUB_HEALTH` (suboptimal), `RISK` (risky), and `HIGH_RISK` (critical).\n        :type HealthLevel: str\n        :param ScoreLost: Total deducted scores.\n        :type ScoreLost: int\n        :param ScoreDetails: Deduction details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ScoreDetails: list of ScoreDetail\n        """
        self.HealthScore = None
        self.HealthLevel = None
        self.ScoreLost = None
        self.ScoreDetails = None


    def _deserialize(self, params):
        self.HealthScore = params.get("HealthScore")
        self.HealthLevel = params.get("HealthLevel")
        self.ScoreLost = params.get("ScoreLost")
        if params.get("ScoreDetails") is not None:
            self.ScoreDetails = []
            for item in params.get("ScoreDetails"):
                obj = ScoreDetail()
                obj._deserialize(item)
                self.ScoreDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceBasicInfo(AbstractModel):
    """Basic instance information.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param InstanceName: Instance name.\n        :type InstanceName: str\n        :param Vip: Private IP of instance.\n        :type Vip: str\n        :param Vport: Private port of instance.\n        :type Vport: int\n        :param Product: Instance service.\n        :type Product: str\n        :param EngineVersion: Instance engine version.\n        :type EngineVersion: str\n        """
        self.InstanceId = None
        self.InstanceName = None
        self.Vip = None
        self.Vport = None
        self.Product = None
        self.EngineVersion = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.Product = params.get("Product")
        self.EngineVersion = params.get("EngineVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfs(AbstractModel):
    """Instance configuration.

    """

    def __init__(self):
        """
        :param DailyInspection: Whether to enable database inspection. Valid values: Yes, No.\n        :type DailyInspection: str\n        :param OverviewDisplay: Whether to enable instance overview. Valid values: Yes, No.\n        :type OverviewDisplay: str\n        """
        self.DailyInspection = None
        self.OverviewDisplay = None


    def _deserialize(self, params):
        self.DailyInspection = params.get("DailyInspection")
        self.OverviewDisplay = params.get("OverviewDisplay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """Queries the list of instances and returns their information.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param InstanceName: Instance name.\n        :type InstanceName: str\n        :param Region: Instance region.\n        :type Region: str\n        :param HealthScore: Health score.\n        :type HealthScore: int\n        :param Product: Service.\n        :type Product: str\n        :param EventCount: Number of exceptions.\n        :type EventCount: int\n        :param InstanceType: Instance type. Valid values: 1 (MASTER), 2 (DR), 3 (RO), 4 (SDR)\n        :type InstanceType: int\n        :param Cpu: Number of cores.\n        :type Cpu: int\n        :param Memory: Memory in MB.\n        :type Memory: int\n        :param Volume: Disk storage in GB.\n        :type Volume: int\n        :param EngineVersion: Database version.\n        :type EngineVersion: str\n        :param Vip: Private network address.\n        :type Vip: str\n        :param Vport: Private network port.\n        :type Vport: int\n        :param Source: Access source.\n        :type Source: str\n        :param GroupId: Group ID.\n        :type GroupId: str\n        :param GroupName: Group name.\n        :type GroupName: str\n        :param Status: Instance status. Valid values: 0 (delivering), 1 (running), 4 (terminating), 5 (isolated)\n        :type Status: int\n        :param UniqSubnetId: Unified subnet ID.\n        :type UniqSubnetId: str\n        :param DeployMode: TencentDB instance type.\n        :type DeployMode: str\n        :param InitFlag: TencentDB instance initialization flag. Valid values: 0 (not initialized), 1 (initialized).\n        :type InitFlag: int\n        :param TaskStatus: Task status.\n        :type TaskStatus: int\n        :param UniqVpcId: Unified VPC ID.\n        :type UniqVpcId: str\n        :param InstanceConf: Instance inspection/overview status.\n        :type InstanceConf: :class:`tencentcloud.dbbrain.v20210527.models.InstanceConfs`\n        :param DeadlineTime: Resource expiration time.\n        :type DeadlineTime: str\n        :param IsSupported: Whether it is an instance supported by DBbrain.\n        :type IsSupported: bool\n        :param SecAuditStatus: Status of instance security audit log. Valid values: ON (enabled), OFF (disabled).\n        :type SecAuditStatus: str\n        :param AuditPolicyStatus: Status of instance audit log. Valid values: ALL_AUDIT (full audit is enabled), RULE_AUDIT (rule audit is enabled), UNBOUND (audit is disabled).\n        :type AuditPolicyStatus: str\n        :param AuditRunningStatus: Running status of instance audit log. Valid values: normal (running), paused (suspension due to overdue payment).\n        :type AuditRunningStatus: str\n        """
        self.InstanceId = None
        self.InstanceName = None
        self.Region = None
        self.HealthScore = None
        self.Product = None
        self.EventCount = None
        self.InstanceType = None
        self.Cpu = None
        self.Memory = None
        self.Volume = None
        self.EngineVersion = None
        self.Vip = None
        self.Vport = None
        self.Source = None
        self.GroupId = None
        self.GroupName = None
        self.Status = None
        self.UniqSubnetId = None
        self.DeployMode = None
        self.InitFlag = None
        self.TaskStatus = None
        self.UniqVpcId = None
        self.InstanceConf = None
        self.DeadlineTime = None
        self.IsSupported = None
        self.SecAuditStatus = None
        self.AuditPolicyStatus = None
        self.AuditRunningStatus = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Region = params.get("Region")
        self.HealthScore = params.get("HealthScore")
        self.Product = params.get("Product")
        self.EventCount = params.get("EventCount")
        self.InstanceType = params.get("InstanceType")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.EngineVersion = params.get("EngineVersion")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.Source = params.get("Source")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.Status = params.get("Status")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.DeployMode = params.get("DeployMode")
        self.InitFlag = params.get("InitFlag")
        self.TaskStatus = params.get("TaskStatus")
        self.UniqVpcId = params.get("UniqVpcId")
        if params.get("InstanceConf") is not None:
            self.InstanceConf = InstanceConfs()
            self.InstanceConf._deserialize(params.get("InstanceConf"))
        self.DeadlineTime = params.get("DeadlineTime")
        self.IsSupported = params.get("IsSupported")
        self.SecAuditStatus = params.get("SecAuditStatus")
        self.AuditPolicyStatus = params.get("AuditPolicyStatus")
        self.AuditRunningStatus = params.get("AuditRunningStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IssueTypeInfo(AbstractModel):
    """Metric information.

    """

    def __init__(self):
        """
        :param IssueType: Metric categories: AVAILABILITY, MAINTAINABILITY, PERFORMANCE, and RELIABILITY\n        :type IssueType: str\n        :param Events: Exception.\n        :type Events: list of EventInfo\n        :param TotalCount: Total number of exceptions.\n        :type TotalCount: int\n        """
        self.IssueType = None
        self.Events = None
        self.TotalCount = None


    def _deserialize(self, params):
        self.IssueType = params.get("IssueType")
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = EventInfo()
                obj._deserialize(item)
                self.Events.append(obj)
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MailConfiguration(AbstractModel):
    """Email sending configuration

    """

    def __init__(self):
        """
        :param SendMail: Whether to enable email sending. Valid values: 0 (no), 1 (yes).\n        :type SendMail: int\n        :param Region: Region configuration, such as "ap-guangzhou" and "ap-shanghai". For the inspection email sending template, configure the region where you need to send the inspection email. For the subscription email sending template, configure the region where the current subscribed instance resides.\n        :type Region: list of str\n        :param HealthStatus: Sends a report with the specified health level, such as "HEALTH", "SUB_HEALTH", "RISK", and "HIGH_RISK".\n        :type HealthStatus: list of str\n        :param ContactPerson: Contact ID. Either `ContactPerson` or `ContactGroup` should be passed in.\n        :type ContactPerson: list of int\n        :param ContactGroup: Contact group ID. Either `ContactPerson` or `ContactGroup` should be passed in.\n        :type ContactGroup: list of int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiagDBInstanceConfRequest(AbstractModel):
    """ModifyDiagDBInstanceConf request structure.

    """

    def __init__(self):
        """
        :param InstanceConfs: Instance configuration, including inspection and overview switch.\n        :type InstanceConfs: :class:`tencentcloud.dbbrain.v20210527.models.InstanceConfs`\n        :param Regions: Target regions of the request. If the value is `All`, it is applied to all regions.\n        :type Regions: str\n        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL).\n        :type Product: str\n        :param InstanceIds: ID of the instance to modify.\n        :type InstanceIds: list of str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiagDBInstanceConfResponse(AbstractModel):
    """ModifyDiagDBInstanceConf response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MonitorFloatMetric(AbstractModel):
    """Monitoring data in float type

    """

    def __init__(self):
        """
        :param Metric: Metric name.\n        :type Metric: str\n        :param Unit: Metric unit.\n        :type Unit: str\n        :param Values: Metric value.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Values: list of float\n        """
        self.Metric = None
        self.Unit = None
        self.Values = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        self.Unit = params.get("Unit")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorFloatMetricSeriesData(AbstractModel):
    """Monitoring metric value in float type in a unit of time interval

    """

    def __init__(self):
        """
        :param Series: Monitoring metric.\n        :type Series: list of MonitorFloatMetric\n        :param Timestamp: Timestamp corresponding to monitoring metric.\n        :type Timestamp: list of int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorMetric(AbstractModel):
    """Monitoring data

    """

    def __init__(self):
        """
        :param Metric: Metric name.\n        :type Metric: str\n        :param Unit: Metric unit.\n        :type Unit: str\n        :param Values: Metric value.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Values: list of float\n        """
        self.Metric = None
        self.Unit = None
        self.Values = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        self.Unit = params.get("Unit")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorMetricSeriesData(AbstractModel):
    """Monitoring metric value in a unit of time interval

    """

    def __init__(self):
        """
        :param Series: Monitoring metric.\n        :type Series: list of MonitorMetric\n        :param Timestamp: Timestamp corresponding to monitoring metric.\n        :type Timestamp: list of int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MySqlProcess(AbstractModel):
    """Relational database thread

    """

    def __init__(self):
        """
        :param ID: Thread ID.\n        :type ID: str\n        :param User: Thread operation account name.\n        :type User: str\n        :param Host: Thread operation host address.\n        :type Host: str\n        :param DB: Thread operation database.\n        :type DB: str\n        :param State: Thread operation status.\n        :type State: str\n        :param Command: Thread execution type.\n        :type Command: str\n        :param Time: Thread operation duration in seconds.\n        :type Time: str\n        :param Info: Thread operation statement.\n        :type Info: str\n        """
        self.ID = None
        self.User = None
        self.Host = None
        self.DB = None
        self.State = None
        self.Command = None
        self.Time = None
        self.Info = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.User = params.get("User")
        self.Host = params.get("Host")
        self.DB = params.get("DB")
        self.State = params.get("State")
        self.Command = params.get("Command")
        self.Time = params.get("Time")
        self.Info = params.get("Info")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProfileInfo(AbstractModel):
    """Information configured by user.

    """

    def __init__(self):
        """
        :param Language: Email language, such as `en`.\n        :type Language: str\n        :param MailConfiguration: Email template content.\n        :type MailConfiguration: :class:`tencentcloud.dbbrain.v20210527.models.MailConfiguration`\n        """
        self.Language = None
        self.MailConfiguration = None


    def _deserialize(self, params):
        self.Language = params.get("Language")
        if params.get("MailConfiguration") is not None:
            self.MailConfiguration = MailConfiguration()
            self.MailConfiguration._deserialize(params.get("MailConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaItem(AbstractModel):
    """`SchemaItem` array

    """

    def __init__(self):
        """
        :param Schema: Database name\n        :type Schema: str\n        """
        self.Schema = None


    def _deserialize(self, params):
        self.Schema = params.get("Schema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaSpaceData(AbstractModel):
    """Database space statistics.

    """

    def __init__(self):
        """
        :param TableSchema: Database name.\n        :type TableSchema: str\n        :param DataLength: Data space in MB.\n        :type DataLength: float\n        :param IndexLength: Index space in MB.\n        :type IndexLength: float\n        :param DataFree: Fragmented space in MB.\n        :type DataFree: float\n        :param TotalLength: Total space usage in MB.\n        :type TotalLength: float\n        :param FragRatio: Fragmentation rate in %.\n        :type FragRatio: float\n        :param TableRows: Number of rows.\n        :type TableRows: int\n        :param PhysicalFileSize: Total size in MB of physical files exclusive to all tables in the database.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PhysicalFileSize: float\n        """
        self.TableSchema = None
        self.DataLength = None
        self.IndexLength = None
        self.DataFree = None
        self.TotalLength = None
        self.FragRatio = None
        self.TableRows = None
        self.PhysicalFileSize = None


    def _deserialize(self, params):
        self.TableSchema = params.get("TableSchema")
        self.DataLength = params.get("DataLength")
        self.IndexLength = params.get("IndexLength")
        self.DataFree = params.get("DataFree")
        self.TotalLength = params.get("TotalLength")
        self.FragRatio = params.get("FragRatio")
        self.TableRows = params.get("TableRows")
        self.PhysicalFileSize = params.get("PhysicalFileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaSpaceTimeSeries(AbstractModel):
    """Time series of database space data

    """

    def __init__(self):
        """
        :param TableSchema: Database name\n        :type TableSchema: str\n        :param SeriesData: Space metric value in a unit of time interval\n        :type SeriesData: :class:`tencentcloud.dbbrain.v20210527.models.MonitorMetricSeriesData`\n        """
        self.TableSchema = None
        self.SeriesData = None


    def _deserialize(self, params):
        self.TableSchema = params.get("TableSchema")
        if params.get("SeriesData") is not None:
            self.SeriesData = MonitorMetricSeriesData()
            self.SeriesData._deserialize(params.get("SeriesData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreDetail(AbstractModel):
    """Deduction details.

    """

    def __init__(self):
        """
        :param IssueType: Deduction item type. Valid values: availability, maintainability, performance, and reliability.\n        :type IssueType: str\n        :param ScoreLost: Total deducted scores.\n        :type ScoreLost: int\n        :param ScoreLostMax: Upper limit of the deducted scores.\n        :type ScoreLostMax: int\n        :param Items: Deduction item list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Items: list of ScoreItem\n        """
        self.IssueType = None
        self.ScoreLost = None
        self.ScoreLostMax = None
        self.Items = None


    def _deserialize(self, params):
        self.IssueType = params.get("IssueType")
        self.ScoreLost = params.get("ScoreLost")
        self.ScoreLostMax = params.get("ScoreLostMax")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ScoreItem()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreItem(AbstractModel):
    """Diagnosis deduction item.

    """

    def __init__(self):
        """
        :param DiagItem: Exception diagnosis item name.\n        :type DiagItem: str\n        :param IssueType: Diagnosis item type. Valid values: availability, maintainability, performance, and reliability.\n        :type IssueType: str\n        :param TopSeverity: Health level. Valid values: information, reminder, alarm, serious, fatal.\n        :type TopSeverity: str\n        :param Count: Number of occurrences of this exception diagnosis item.\n        :type Count: int\n        :param ScoreLost: Deducted scores.\n        :type ScoreLost: int\n        """
        self.DiagItem = None
        self.IssueType = None
        self.TopSeverity = None
        self.Count = None
        self.ScoreLost = None


    def _deserialize(self, params):
        self.DiagItem = params.get("DiagItem")
        self.IssueType = params.get("IssueType")
        self.TopSeverity = params.get("TopSeverity")
        self.Count = params.get("Count")
        self.ScoreLost = params.get("ScoreLost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecLogExportTaskInfo(AbstractModel):
    """Security audit log export task information.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task Id.\n        :type AsyncRequestId: int\n        :param StartTime: Task start time.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StartTime: str\n        :param EndTime: Task end time.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EndTime: str\n        :param CreateTime: Task creation time.\n        :type CreateTime: str\n        :param Status: Task status.\n        :type Status: str\n        :param Progress: Task progress.\n        :type Progress: int\n        :param LogStartTime: Exported log start time.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type LogStartTime: str\n        :param LogEndTime: Exported log end time.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type LogEndTime: str\n        :param TotalSize: Total size of log files in KB.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalSize: int\n        :param DangerLevels: List of risk levels. 0: no risk; 1: low risk; 2: medium risk; 3 high risk.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DangerLevels: list of int non-negative\n        """
        self.AsyncRequestId = None
        self.StartTime = None
        self.EndTime = None
        self.CreateTime = None
        self.Status = None
        self.Progress = None
        self.LogStartTime = None
        self.LogEndTime = None
        self.TotalSize = None
        self.DangerLevels = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.LogStartTime = params.get("LogStartTime")
        self.LogEndTime = params.get("LogEndTime")
        self.TotalSize = params.get("TotalSize")
        self.DangerLevels = params.get("DangerLevels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogHost(AbstractModel):
    """Details of slow log source addresses.

    """

    def __init__(self):
        """
        :param UserHost: Source addresses.\n        :type UserHost: str\n        :param Ratio: Proportion (in %) of slow logs from this source address to the total number of slow logs.\n        :type Ratio: float\n        :param Count: Number of slow logs from this source address.\n        :type Count: int\n        """
        self.UserHost = None
        self.Ratio = None
        self.Count = None


    def _deserialize(self, params):
        self.UserHost = params.get("UserHost")
        self.Ratio = params.get("Ratio")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogTopSqlItem(AbstractModel):
    """Top slow SQL statements

    """

    def __init__(self):
        """
        :param LockTime: Total SQL lock wait time in seconds.\n        :type LockTime: float\n        :param LockTimeMax: Maximum lock wait time in seconds\n        :type LockTimeMax: float\n        :param LockTimeMin: Minimum lock wait time in seconds\n        :type LockTimeMin: float\n        :param RowsExamined: Total number of scanned rows\n        :type RowsExamined: int\n        :param RowsExaminedMax: Maximum number of scanned rows\n        :type RowsExaminedMax: int\n        :param RowsExaminedMin: Minimum number of scanned rows\n        :type RowsExaminedMin: int\n        :param QueryTime: Total duration in seconds\n        :type QueryTime: float\n        :param QueryTimeMax: Maximum execution time in seconds\n        :type QueryTimeMax: float\n        :param QueryTimeMin: Minimum execution time in seconds\n        :type QueryTimeMin: float\n        :param RowsSent: Total number of returned rows\n        :type RowsSent: int\n        :param RowsSentMax: Maximum number of returned rows\n        :type RowsSentMax: int\n        :param RowsSentMin: Minimum number of returned rows\n        :type RowsSentMin: int\n        :param ExecTimes: Number of executions\n        :type ExecTimes: int\n        :param SqlTemplate: SQL template\n        :type SqlTemplate: str\n        :param SqlText: SQL statements with parameter (random)\n        :type SqlText: str\n        :param Schema: Database name\n        :type Schema: str\n        :param QueryTimeRatio: Ratio of total duration in %\n        :type QueryTimeRatio: float\n        :param LockTimeRatio: Ratio of total SQL lock wait time in %\n        :type LockTimeRatio: float\n        :param RowsExaminedRatio: Ratio of total number of scanned rows in %\n        :type RowsExaminedRatio: float\n        :param RowsSentRatio: Ratio of total number of returned rows in %\n        :type RowsSentRatio: float\n        :param QueryTimeAvg: Average execution time in seconds\n        :type QueryTimeAvg: float\n        :param RowsSentAvg: Average number of returned rows\n        :type RowsSentAvg: float\n        :param LockTimeAvg: Average lock wait time in seconds\n        :type LockTimeAvg: float\n        :param RowsExaminedAvg: Average number of scanned rows\n        :type RowsExaminedAvg: float\n        """
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
        self.QueryTimeAvg = None
        self.RowsSentAvg = None
        self.LockTimeAvg = None
        self.RowsExaminedAvg = None


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
        self.QueryTimeAvg = params.get("QueryTimeAvg")
        self.RowsSentAvg = params.get("RowsSentAvg")
        self.LockTimeAvg = params.get("LockTimeAvg")
        self.RowsExaminedAvg = params.get("RowsExaminedAvg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableSpaceData(AbstractModel):
    """Database tablespace statistics.

    """

    def __init__(self):
        """
        :param TableName: Table name.\n        :type TableName: str\n        :param TableSchema: Database name.\n        :type TableSchema: str\n        :param Engine: Database table storage engine.\n        :type Engine: str\n        :param DataLength: Data space in MB.\n        :type DataLength: float\n        :param IndexLength: Index space in MB.\n        :type IndexLength: float\n        :param DataFree: Fragmented space in MB.\n        :type DataFree: float\n        :param TotalLength: Total space usage in MB.\n        :type TotalLength: float\n        :param FragRatio: Fragmentation rate in %.\n        :type FragRatio: float\n        :param TableRows: Number of rows.\n        :type TableRows: int\n        :param PhysicalFileSize: Size in MB of the physical file exclusive to a table.\n        :type PhysicalFileSize: float\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableSpaceTimeSeries(AbstractModel):
    """Time series of database tablespace data

    """

    def __init__(self):
        """
        :param TableName: Table name.\n        :type TableName: str\n        :param TableSchema: Database name.\n        :type TableSchema: str\n        :param Engine: Database table storage engine.\n        :type Engine: str\n        :param SeriesData: Space metric value in a unit of time interval\n        :type SeriesData: :class:`tencentcloud.dbbrain.v20210527.models.MonitorFloatMetricSeriesData`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeSlice(AbstractModel):
    """Slow log statistics in specified time range

    """

    def __init__(self):
        """
        :param Count: Total number\n        :type Count: int\n        :param Timestamp: Statistics start time\n        :type Timestamp: int\n        """
        self.Count = None
        self.Timestamp = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserProfile(AbstractModel):
    """Information configured by user, including email configuration.

    """

    def __init__(self):
        """
        :param ProfileId: Configured ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProfileId: str\n        :param ProfileType: Configuration type.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProfileType: str\n        :param ProfileLevel: Configuration level. Valid values: User, Instance.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProfileLevel: str\n        :param ProfileName: Configuration name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProfileName: str\n        :param ProfileInfo: Configuration details.\n        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20210527.models.ProfileInfo`\n        """
        self.ProfileId = None
        self.ProfileType = None
        self.ProfileLevel = None
        self.ProfileName = None
        self.ProfileInfo = None


    def _deserialize(self, params):
        self.ProfileId = params.get("ProfileId")
        self.ProfileType = params.get("ProfileType")
        self.ProfileLevel = params.get("ProfileLevel")
        self.ProfileName = params.get("ProfileName")
        if params.get("ProfileInfo") is not None:
            self.ProfileInfo = ProfileInfo()
            self.ProfileInfo._deserialize(params.get("ProfileInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        