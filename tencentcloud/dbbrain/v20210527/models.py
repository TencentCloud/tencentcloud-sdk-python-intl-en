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
        r"""
        :param _Name: Recipient name, which can contain up to 20 letters, digits, spaces, and symbols `!@#$%^&*()_+-=()` and cannot begin with an underscore.
        :type Name: str
        :param _ContactInfo: Email address, which can contain letters, digits, underscores, and the @ symbol, cannot begin with an underscore, and must be unique.
        :type ContactInfo: str
        :param _Product: Service type, which is fixed to `mysql`.
        :type Product: str
        """
        self._Name = None
        self._ContactInfo = None
        self._Product = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ContactInfo(self):
        return self._ContactInfo

    @ContactInfo.setter
    def ContactInfo(self, ContactInfo):
        self._ContactInfo = ContactInfo

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ContactInfo = params.get("ContactInfo")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserContactResponse(AbstractModel):
    """AddUserContact response structure.

    """

    def __init__(self):
        r"""
        :param _Id: ID of the successfully added recipient.
        :type Id: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class ContactItem(AbstractModel):
    """Recipient description.

    """

    def __init__(self):
        r"""
        :param _Id: Recipient ID.
        :type Id: int
        :param _Name: Recipient name.
        :type Name: str
        :param _Mail: Recipient email.
        :type Mail: str
        """
        self._Id = None
        self._Name = None
        self._Mail = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mail(self):
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Mail = params.get("Mail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBDiagReportTaskRequest(AbstractModel):
    """CreateDBDiagReportTask request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _StartTime: Start time, such as "2020-11-08T14:00:00+08:00".
        :type StartTime: str
        :param _EndTime: End time, such as "2020-11-09T14:00:00+08:00".
        :type EndTime: str
        :param _SendMailFlag: Whether to send an email. Valid values: `0` (yes), `1` (no).
        :type SendMailFlag: int
        :param _ContactPerson: Array of the IDs of recipients to receive email.
        :type ContactPerson: list of int
        :param _ContactGroup: Array of IDs of recipient groups to receive email.
        :type ContactGroup: list of int
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._SendMailFlag = None
        self._ContactPerson = None
        self._ContactGroup = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SendMailFlag(self):
        return self._SendMailFlag

    @SendMailFlag.setter
    def SendMailFlag(self, SendMailFlag):
        self._SendMailFlag = SendMailFlag

    @property
    def ContactPerson(self):
        return self._ContactPerson

    @ContactPerson.setter
    def ContactPerson(self, ContactPerson):
        self._ContactPerson = ContactPerson

    @property
    def ContactGroup(self):
        return self._ContactGroup

    @ContactGroup.setter
    def ContactGroup(self, ContactGroup):
        self._ContactGroup = ContactGroup

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SendMailFlag = params.get("SendMailFlag")
        self._ContactPerson = params.get("ContactPerson")
        self._ContactGroup = params.get("ContactGroup")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBDiagReportTaskResponse(AbstractModel):
    """CreateDBDiagReportTask response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AsyncRequestId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class CreateDBDiagReportUrlRequest(AbstractModel):
    """CreateDBDiagReportUrl request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _AsyncRequestId: Health report task ID, which can be queried through `DescribeDBDiagReportTasks`.
        :type AsyncRequestId: int
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._AsyncRequestId = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBDiagReportUrlResponse(AbstractModel):
    """CreateDBDiagReportUrl response structure.

    """

    def __init__(self):
        r"""
        :param _ReportUrl: Health report URL.
        :type ReportUrl: str
        :param _ExpireTime: Expiration timestamp of the health report URL (in seconds).
        :type ExpireTime: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReportUrl = None
        self._ExpireTime = None
        self._RequestId = None

    @property
    def ReportUrl(self):
        return self._ReportUrl

    @ReportUrl.setter
    def ReportUrl(self, ReportUrl):
        self._ReportUrl = ReportUrl

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReportUrl = params.get("ReportUrl")
        self._ExpireTime = params.get("ExpireTime")
        self._RequestId = params.get("RequestId")


class CreateKillTaskRequest(AbstractModel):
    """CreateKillTask request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the instance associated with the session killing task.
        :type InstanceId: str
        :param _Duration: Task duration in seconds. Pass in `-1` to stop the task manually.
        :type Duration: int
        :param _Host: Client IP, which is a task filter.
        :type Host: str
        :param _DB: Database name, which is a task filter. Multiple database names are separated by comma.
        :type DB: str
        :param _Command: Related command, which is a task filter. Multiple commands are separated by comma.
        :type Command: str
        :param _Info: Task filter. Filtering by single filter prefix is supported.
        :type Info: str
        :param _User: User type, which is a task filter.
        :type User: str
        :param _Time: Session duration in seconds, which is a task filter.
        :type Time: int
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._Duration = None
        self._Host = None
        self._DB = None
        self._Command = None
        self._Info = None
        self._User = None
        self._Time = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def DB(self):
        return self._DB

    @DB.setter
    def DB(self, DB):
        self._DB = DB

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Duration = params.get("Duration")
        self._Host = params.get("Host")
        self._DB = params.get("DB")
        self._Command = params.get("Command")
        self._Info = params.get("Info")
        self._User = params.get("User")
        self._Time = params.get("Time")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKillTaskResponse(AbstractModel):
    """CreateKillTask response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status. `1` is returned if the session killing task is successfully created.
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CreateMailProfileRequest(AbstractModel):
    """CreateMailProfile request structure.

    """

    def __init__(self):
        r"""
        :param _ProfileInfo: Email configuration.
        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20210527.models.ProfileInfo`
        :param _ProfileLevel: Configuration level. Valid values: `User` (user-level), `Instance` (instance-level). For database inspection emails, it should be `User`. For scheduled task emails, it should be `Instance`.
        :type ProfileLevel: str
        :param _ProfileName: Configuration name, which needs to be unique. For database inspection emails, this name can be customized as needed. For scheduled task emails, the name should be in the format of "scheduler_" + {instanceId}, such as "schduler_cdb-test".
        :type ProfileName: str
        :param _ProfileType: Configuration type. Valid values: `dbScan_mail_configuration` (email configuration of the database inspection report), `scheduler_mail_configuration` (email configuration of the scheduled task report).
        :type ProfileType: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL).
        :type Product: str
        :param _BindInstanceIds: Instance ID bound with the configuration, which is set when the configuration level is `Instance`. Only one instance can be bound at a time. When the configuration level is `User`, leave this parameter empty.
        :type BindInstanceIds: list of str
        """
        self._ProfileInfo = None
        self._ProfileLevel = None
        self._ProfileName = None
        self._ProfileType = None
        self._Product = None
        self._BindInstanceIds = None

    @property
    def ProfileInfo(self):
        return self._ProfileInfo

    @ProfileInfo.setter
    def ProfileInfo(self, ProfileInfo):
        self._ProfileInfo = ProfileInfo

    @property
    def ProfileLevel(self):
        return self._ProfileLevel

    @ProfileLevel.setter
    def ProfileLevel(self, ProfileLevel):
        self._ProfileLevel = ProfileLevel

    @property
    def ProfileName(self):
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, ProfileName):
        self._ProfileName = ProfileName

    @property
    def ProfileType(self):
        return self._ProfileType

    @ProfileType.setter
    def ProfileType(self, ProfileType):
        self._ProfileType = ProfileType

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def BindInstanceIds(self):
        return self._BindInstanceIds

    @BindInstanceIds.setter
    def BindInstanceIds(self, BindInstanceIds):
        self._BindInstanceIds = BindInstanceIds


    def _deserialize(self, params):
        if params.get("ProfileInfo") is not None:
            self._ProfileInfo = ProfileInfo()
            self._ProfileInfo._deserialize(params.get("ProfileInfo"))
        self._ProfileLevel = params.get("ProfileLevel")
        self._ProfileName = params.get("ProfileName")
        self._ProfileType = params.get("ProfileType")
        self._Product = params.get("Product")
        self._BindInstanceIds = params.get("BindInstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMailProfileResponse(AbstractModel):
    """CreateMailProfile response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateProxySessionKillTaskRequest(AbstractModel):
    """CreateProxySessionKillTask request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Product: Service type. Valid value: `redis` (TencentDB for Redis).
        :type Product: str
        """
        self._InstanceId = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProxySessionKillTaskResponse(AbstractModel):
    """CreateProxySessionKillTask response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task ID that is returned after the session killing task is created.
        :type AsyncRequestId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class CreateSchedulerMailProfileRequest(AbstractModel):
    """CreateSchedulerMailProfile request structure.

    """

    def __init__(self):
        r"""
        :param _WeekConfiguration: Value range: 1-7, representing Monday to Sunday respectively.
        :type WeekConfiguration: list of int
        :param _ProfileInfo: Email configuration.
        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20210527.models.ProfileInfo`
        :param _ProfileName: Configuration name, which needs to be unique. For scheduled task emails, the name should be in the format of "scheduler_" + {instanceId}, such as "schduler_cdb-test".
        :type ProfileName: str
        :param _BindInstanceId: ID of the instance for which to configure subscription.
        :type BindInstanceId: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._WeekConfiguration = None
        self._ProfileInfo = None
        self._ProfileName = None
        self._BindInstanceId = None
        self._Product = None

    @property
    def WeekConfiguration(self):
        return self._WeekConfiguration

    @WeekConfiguration.setter
    def WeekConfiguration(self, WeekConfiguration):
        self._WeekConfiguration = WeekConfiguration

    @property
    def ProfileInfo(self):
        return self._ProfileInfo

    @ProfileInfo.setter
    def ProfileInfo(self, ProfileInfo):
        self._ProfileInfo = ProfileInfo

    @property
    def ProfileName(self):
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, ProfileName):
        self._ProfileName = ProfileName

    @property
    def BindInstanceId(self):
        return self._BindInstanceId

    @BindInstanceId.setter
    def BindInstanceId(self, BindInstanceId):
        self._BindInstanceId = BindInstanceId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._WeekConfiguration = params.get("WeekConfiguration")
        if params.get("ProfileInfo") is not None:
            self._ProfileInfo = ProfileInfo()
            self._ProfileInfo._deserialize(params.get("ProfileInfo"))
        self._ProfileName = params.get("ProfileName")
        self._BindInstanceId = params.get("BindInstanceId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSchedulerMailProfileResponse(AbstractModel):
    """CreateSchedulerMailProfile response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateSecurityAuditLogExportTaskRequest(AbstractModel):
    """CreateSecurityAuditLogExportTask request structure.

    """

    def __init__(self):
        r"""
        :param _SecAuditGroupId: Security audit group ID.
        :type SecAuditGroupId: str
        :param _StartTime: Exported log start time, such as 2020-12-28 00:00:00.
        :type StartTime: str
        :param _EndTime: Exported log end time, such as 2020-12-28 01:00:00.
        :type EndTime: str
        :param _Product: Service type. Valid value: `mysql` (TencentDB for MySQL).
        :type Product: str
        :param _DangerLevels: List of log risk levels. Valid values: `0` (no risk), `1` (low risk), `2` (medium risk), `3` (high risk).
        :type DangerLevels: list of int
        """
        self._SecAuditGroupId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None
        self._DangerLevels = None

    @property
    def SecAuditGroupId(self):
        return self._SecAuditGroupId

    @SecAuditGroupId.setter
    def SecAuditGroupId(self, SecAuditGroupId):
        self._SecAuditGroupId = SecAuditGroupId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def DangerLevels(self):
        return self._DangerLevels

    @DangerLevels.setter
    def DangerLevels(self, DangerLevels):
        self._DangerLevels = DangerLevels


    def _deserialize(self, params):
        self._SecAuditGroupId = params.get("SecAuditGroupId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        self._DangerLevels = params.get("DangerLevels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityAuditLogExportTaskResponse(AbstractModel):
    """CreateSecurityAuditLogExportTask response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Log export task Id.
        :type AsyncRequestId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class DeleteDBDiagReportTasksRequest(AbstractModel):
    """DeleteDBDiagReportTasks request structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestIds: List of IDs of tasks to be deleted
        :type AsyncRequestIds: list of int
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._AsyncRequestIds = None
        self._InstanceId = None
        self._Product = None

    @property
    def AsyncRequestIds(self):
        return self._AsyncRequestIds

    @AsyncRequestIds.setter
    def AsyncRequestIds(self, AsyncRequestIds):
        self._AsyncRequestIds = AsyncRequestIds

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._AsyncRequestIds = params.get("AsyncRequestIds")
        self._InstanceId = params.get("InstanceId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDBDiagReportTasksResponse(AbstractModel):
    """DeleteDBDiagReportTasks response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task deletion status (`0`: Successful)
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DeleteSecurityAuditLogExportTasksRequest(AbstractModel):
    """DeleteSecurityAuditLogExportTasks request structure.

    """

    def __init__(self):
        r"""
        :param _SecAuditGroupId: Security audit group ID.
        :type SecAuditGroupId: str
        :param _AsyncRequestIds: List of log export task IDs. This API will ignore task IDs that do not exist or have been deleted.
        :type AsyncRequestIds: list of int non-negative
        :param _Product: Service type. Valid value: `mysql` (TencentDB for MySQL).
        :type Product: str
        """
        self._SecAuditGroupId = None
        self._AsyncRequestIds = None
        self._Product = None

    @property
    def SecAuditGroupId(self):
        return self._SecAuditGroupId

    @SecAuditGroupId.setter
    def SecAuditGroupId(self, SecAuditGroupId):
        self._SecAuditGroupId = SecAuditGroupId

    @property
    def AsyncRequestIds(self):
        return self._AsyncRequestIds

    @AsyncRequestIds.setter
    def AsyncRequestIds(self, AsyncRequestIds):
        self._AsyncRequestIds = AsyncRequestIds

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._SecAuditGroupId = params.get("SecAuditGroupId")
        self._AsyncRequestIds = params.get("AsyncRequestIds")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityAuditLogExportTasksResponse(AbstractModel):
    """DeleteSecurityAuditLogExportTasks response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAllUserContactRequest(AbstractModel):
    """DescribeAllUserContact request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Service type, which is fixed to `mysql`.
        :type Product: str
        :param _Names: Array of recipient names. Fuzzy search is supported.
        :type Names: list of str
        """
        self._Product = None
        self._Names = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllUserContactResponse(AbstractModel):
    """DescribeAllUserContact response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of recipients.
        :type TotalCount: int
        :param _Contacts: Recipient information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Contacts: list of ContactItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Contacts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Contacts(self):
        return self._Contacts

    @Contacts.setter
    def Contacts(self, Contacts):
        self._Contacts = Contacts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Contacts") is not None:
            self._Contacts = []
            for item in params.get("Contacts"):
                obj = ContactItem()
                obj._deserialize(item)
                self._Contacts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllUserGroupRequest(AbstractModel):
    """DescribeAllUserGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Service type, which is fixed to `mysql`.
        :type Product: str
        :param _Names: Array of recipient group names. Fuzzy search is supported.
        :type Names: list of str
        """
        self._Product = None
        self._Names = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllUserGroupResponse(AbstractModel):
    """DescribeAllUserGroup response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of groups.
        :type TotalCount: int
        :param _Groups: Group information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Groups: list of GroupItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Groups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = GroupItem()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBDiagEventRequest(AbstractModel):
    """DescribeDBDiagEvent request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _EventId: Event ID, which can be obtained through the `DescribeDBDiagHistory` API.
        :type EventId: int
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._EventId = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EventId = params.get("EventId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagEventResponse(AbstractModel):
    """DescribeDBDiagEvent response structure.

    """

    def __init__(self):
        r"""
        :param _DiagItem: Diagnosis item.
        :type DiagItem: str
        :param _DiagType: Diagnosis type.
        :type DiagType: str
        :param _EventId: Event ID.
        :type EventId: int
        :param _Explanation: Diagnosis event details. If there is no additional explanation information, the output will be empty.
        :type Explanation: str
        :param _Outline: Diagnosis summary.
        :type Outline: str
        :param _Problem: Found problem.
        :type Problem: str
        :param _Severity: Severity, which can be divided into 5 levels: `1` (Critical), `2` (Severe), `3` (Alarm), `4` (Reminder), `5` (healthy).
        :type Severity: int
        :param _StartTime: Start time
        :type StartTime: str
        :param _Suggestions: Suggestions. If there are no suggestions, the output will be empty.
        :type Suggestions: str
        :param _Metric: Reserved field.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Metric: str
        :param _EndTime: End time.
        :type EndTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiagItem = None
        self._DiagType = None
        self._EventId = None
        self._Explanation = None
        self._Outline = None
        self._Problem = None
        self._Severity = None
        self._StartTime = None
        self._Suggestions = None
        self._Metric = None
        self._EndTime = None
        self._RequestId = None

    @property
    def DiagItem(self):
        return self._DiagItem

    @DiagItem.setter
    def DiagItem(self, DiagItem):
        self._DiagItem = DiagItem

    @property
    def DiagType(self):
        return self._DiagType

    @DiagType.setter
    def DiagType(self, DiagType):
        self._DiagType = DiagType

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Explanation(self):
        return self._Explanation

    @Explanation.setter
    def Explanation(self, Explanation):
        self._Explanation = Explanation

    @property
    def Outline(self):
        return self._Outline

    @Outline.setter
    def Outline(self, Outline):
        self._Outline = Outline

    @property
    def Problem(self):
        return self._Problem

    @Problem.setter
    def Problem(self, Problem):
        self._Problem = Problem

    @property
    def Severity(self):
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Suggestions(self):
        return self._Suggestions

    @Suggestions.setter
    def Suggestions(self, Suggestions):
        self._Suggestions = Suggestions

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DiagItem = params.get("DiagItem")
        self._DiagType = params.get("DiagType")
        self._EventId = params.get("EventId")
        self._Explanation = params.get("Explanation")
        self._Outline = params.get("Outline")
        self._Problem = params.get("Problem")
        self._Severity = params.get("Severity")
        self._StartTime = params.get("StartTime")
        self._Suggestions = params.get("Suggestions")
        self._Metric = params.get("Metric")
        self._EndTime = params.get("EndTime")
        self._RequestId = params.get("RequestId")


class DescribeDBDiagEventsRequest(AbstractModel):
    """DescribeDBDiagEvents request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time in the format of “2021-05-27 00:00:00”. The earliest time that can be queried is 30 days before the current time.
        :type StartTime: str
        :param _EndTime: End time in the format of "2021-05-27 01:00:00". The interval between the end time and the start time can be up to 7 days.
        :type EndTime: str
        :param _Severities: Risk level list. Valid values in descending order of severity: `1` (critical), `2` (serious), `3` (alarm), `4` (warning), `5` (healthy).
        :type Severities: list of int
        :param _InstanceIds: Instance ID list.
        :type InstanceIds: list of str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 50.
        :type Limit: int
        """
        self._StartTime = None
        self._EndTime = None
        self._Severities = None
        self._InstanceIds = None
        self._Offset = None
        self._Limit = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Severities(self):
        return self._Severities

    @Severities.setter
    def Severities(self, Severities):
        self._Severities = Severities

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Severities = params.get("Severities")
        self._InstanceIds = params.get("InstanceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagEventsResponse(AbstractModel):
    """DescribeDBDiagEvents response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of diagnosis events.
        :type TotalCount: int
        :param _Items: Diagnosis event list.
        :type Items: list of DiagHistoryEventItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DiagHistoryEventItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBDiagHistoryRequest(AbstractModel):
    """DescribeDBDiagHistory request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _StartTime: Start time, such as "2019-09-10 12:13:14".
        :type StartTime: str
        :param _EndTime: End time, such as "2019-09-11 12:13:14". The interval between the end time and the start time can be up to 2 days.
        :type EndTime: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagHistoryResponse(AbstractModel):
    """DescribeDBDiagHistory response structure.

    """

    def __init__(self):
        r"""
        :param _Events: Event description.
        :type Events: list of DiagHistoryEventItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Events = None
        self._RequestId = None

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = DiagHistoryEventItem()
                obj._deserialize(item)
                self._Events.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBDiagReportTasksRequest(AbstractModel):
    """DescribeDBDiagReportTasks request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time of the first task in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14. It is used for queries by time range.
        :type StartTime: str
        :param _EndTime: End time of the last task in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14. It is used for queries by time range.
        :type EndTime: str
        :param _InstanceIds: Array of instance IDs, which is used to filter the task list of the specified instance.
        :type InstanceIds: list of str
        :param _Sources: Source that triggers the task. Valid values: `DAILY_INSPECTION` (instance inspection), `SCHEDULED` (scheduled task), and `MANUAL` (manual trigger).
        :type Sources: list of str
        :param _HealthLevels: Health level. Valid values: `HEALTH` (healthy), `SUB_HEALTH` (suboptimal), `RISK` (risky), and `HIGH_RISK` (critical).
        :type HealthLevels: str
        :param _TaskStatuses: Task status. Valid values: `created` (created), `chosen` (to be executed), `running` (being executed), `failed` (failed), and `finished` (completed).
        :type TaskStatuses: str
        :param _Offset: Offset. Default value: `0`.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: `20`. Maximum value: `100`.
        :type Limit: int
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._StartTime = None
        self._EndTime = None
        self._InstanceIds = None
        self._Sources = None
        self._HealthLevels = None
        self._TaskStatuses = None
        self._Offset = None
        self._Limit = None
        self._Product = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Sources(self):
        return self._Sources

    @Sources.setter
    def Sources(self, Sources):
        self._Sources = Sources

    @property
    def HealthLevels(self):
        return self._HealthLevels

    @HealthLevels.setter
    def HealthLevels(self, HealthLevels):
        self._HealthLevels = HealthLevels

    @property
    def TaskStatuses(self):
        return self._TaskStatuses

    @TaskStatuses.setter
    def TaskStatuses(self, TaskStatuses):
        self._TaskStatuses = TaskStatuses

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._InstanceIds = params.get("InstanceIds")
        self._Sources = params.get("Sources")
        self._HealthLevels = params.get("HealthLevels")
        self._TaskStatuses = params.get("TaskStatuses")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagReportTasksResponse(AbstractModel):
    """DescribeDBDiagReportTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of tasks.
        :type TotalCount: int
        :param _Tasks: List of tasks.
        :type Tasks: list of HealthReportTask
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = HealthReportTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSpaceStatusRequest(AbstractModel):
    """DescribeDBSpaceStatus request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _RangeDays: Query period in days. The end date is the current date, and the query period is 7 days by default.
        :type RangeDays: int
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._RangeDays = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RangeDays(self):
        return self._RangeDays

    @RangeDays.setter
    def RangeDays(self, RangeDays):
        self._RangeDays = RangeDays

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RangeDays = params.get("RangeDays")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSpaceStatusResponse(AbstractModel):
    """DescribeDBSpaceStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Growth: Disk usage growth in MB.
        :type Growth: int
        :param _Remain: Available disk space in MB.
        :type Remain: int
        :param _Total: Total disk space in MB.
        :type Total: int
        :param _AvailableDays: Estimated number of available days.
        :type AvailableDays: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Growth = None
        self._Remain = None
        self._Total = None
        self._AvailableDays = None
        self._RequestId = None

    @property
    def Growth(self):
        return self._Growth

    @Growth.setter
    def Growth(self, Growth):
        self._Growth = Growth

    @property
    def Remain(self):
        return self._Remain

    @Remain.setter
    def Remain(self, Remain):
        self._Remain = Remain

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AvailableDays(self):
        return self._AvailableDays

    @AvailableDays.setter
    def AvailableDays(self, AvailableDays):
        self._AvailableDays = AvailableDays

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Growth = params.get("Growth")
        self._Remain = params.get("Remain")
        self._Total = params.get("Total")
        self._AvailableDays = params.get("AvailableDays")
        self._RequestId = params.get("RequestId")


class DescribeDiagDBInstancesRequest(AbstractModel):
    """DescribeDiagDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _IsSupported: Whether it is an instance supported by DBbrain. It is fixed to `true`.
        :type IsSupported: bool
        :param _Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.
        :type Product: str
        :param _Offset: Pagination parameter indicating the offset.
        :type Offset: int
        :param _Limit: Pagination parameter. Maximum value: 100.
        :type Limit: int
        :param _InstanceNames: Query by instance name.
        :type InstanceNames: list of str
        :param _InstanceIds: Query by instance ID.
        :type InstanceIds: list of str
        :param _Regions: Query by region.
        :type Regions: list of str
        """
        self._IsSupported = None
        self._Product = None
        self._Offset = None
        self._Limit = None
        self._InstanceNames = None
        self._InstanceIds = None
        self._Regions = None

    @property
    def IsSupported(self):
        return self._IsSupported

    @IsSupported.setter
    def IsSupported(self, IsSupported):
        self._IsSupported = IsSupported

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceNames(self):
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        self._IsSupported = params.get("IsSupported")
        self._Product = params.get("Product")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceNames = params.get("InstanceNames")
        self._InstanceIds = params.get("InstanceIds")
        self._Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiagDBInstancesResponse(AbstractModel):
    """DescribeDiagDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of instances.
        :type TotalCount: int
        :param _DbScanStatus: Status of all instance inspection. 0: all instance inspection enabled, 1: all instance inspection disabled.
        :type DbScanStatus: int
        :param _Items: Instance information.
        :type Items: list of InstanceInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DbScanStatus = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DbScanStatus(self):
        return self._DbScanStatus

    @DbScanStatus.setter
    def DbScanStatus(self, DbScanStatus):
        self._DbScanStatus = DbScanStatus

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._DbScanStatus = params.get("DbScanStatus")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHealthScoreRequest(AbstractModel):
    """DescribeHealthScore request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID for which to get the health score.
        :type InstanceId: str
        :param _Time: Time to get the health score in the format of `2019-09-10 12:13:14`.
        :type Time: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._Time = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Time = params.get("Time")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHealthScoreResponse(AbstractModel):
    """DescribeHealthScore response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Health score and deduction for exceptions.
        :type Data: :class:`tencentcloud.dbbrain.v20210527.models.HealthScoreInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = HealthScoreInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMailProfileRequest(AbstractModel):
    """DescribeMailProfile request structure.

    """

    def __init__(self):
        r"""
        :param _ProfileType: Configuration type. Valid values: `dbScan_mail_configuration` (email configuration of the database inspection report), `scheduler_mail_configuration` (email configuration of the scheduled task report).
        :type ProfileType: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        :param _Offset: Pagination offset.
        :type Offset: int
        :param _Limit: Number of results per page in paginated queries. Maximum value: `50`.
        :type Limit: int
        :param _ProfileName: Query by email configuration name. The name of the scheduled task email configuration should be in the format of "scheduler_"+{instanceId}.
        :type ProfileName: str
        """
        self._ProfileType = None
        self._Product = None
        self._Offset = None
        self._Limit = None
        self._ProfileName = None

    @property
    def ProfileType(self):
        return self._ProfileType

    @ProfileType.setter
    def ProfileType(self, ProfileType):
        self._ProfileType = ProfileType

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ProfileName(self):
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, ProfileName):
        self._ProfileName = ProfileName


    def _deserialize(self, params):
        self._ProfileType = params.get("ProfileType")
        self._Product = params.get("Product")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProfileName = params.get("ProfileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMailProfileResponse(AbstractModel):
    """DescribeMailProfile response structure.

    """

    def __init__(self):
        r"""
        :param _ProfileList: Email configuration details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProfileList: list of UserProfile
        :param _TotalCount: Total number of the configured emails.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProfileList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ProfileList(self):
        return self._ProfileList

    @ProfileList.setter
    def ProfileList(self, ProfileList):
        self._ProfileList = ProfileList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProfileList") is not None:
            self._ProfileList = []
            for item in params.get("ProfileList"):
                obj = UserProfile()
                obj._deserialize(item)
                self._ProfileList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeMySqlProcessListRequest(AbstractModel):
    """DescribeMySqlProcessList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _ID: Thread ID, which is used to filter the thread list.
        :type ID: int
        :param _User: Thread operation account name, which is used to filter the thread list.
        :type User: str
        :param _Host: Thread operation host address, which is used to filter the thread list.
        :type Host: str
        :param _DB: Thread operation database, which is used to filter the thread list.
        :type DB: str
        :param _State: Thread operation status, which is used to filter the thread list.
        :type State: str
        :param _Command: Thread execution type, which is used to filter the thread list.
        :type Command: str
        :param _Time: Minimum operation duration of the thread in seconds, which is used to filter the list of threads whose operation duration is greater than this value.
        :type Time: int
        :param _Info: Thread operation statement, which is used to filter the thread list.
        :type Info: str
        :param _Limit: Number of returned results. Default value: 20.
        :type Limit: int
        :param _Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.
        :type Product: str
        """
        self._InstanceId = None
        self._ID = None
        self._User = None
        self._Host = None
        self._DB = None
        self._State = None
        self._Command = None
        self._Time = None
        self._Info = None
        self._Limit = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def DB(self):
        return self._DB

    @DB.setter
    def DB(self, DB):
        self._DB = DB

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ID = params.get("ID")
        self._User = params.get("User")
        self._Host = params.get("Host")
        self._DB = params.get("DB")
        self._State = params.get("State")
        self._Command = params.get("Command")
        self._Time = params.get("Time")
        self._Info = params.get("Info")
        self._Limit = params.get("Limit")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMySqlProcessListResponse(AbstractModel):
    """DescribeMySqlProcessList response structure.

    """

    def __init__(self):
        r"""
        :param _ProcessList: List of real-time threads.
        :type ProcessList: list of MySqlProcess
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProcessList = None
        self._RequestId = None

    @property
    def ProcessList(self):
        return self._ProcessList

    @ProcessList.setter
    def ProcessList(self, ProcessList):
        self._ProcessList = ProcessList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProcessList") is not None:
            self._ProcessList = []
            for item in params.get("ProcessList"):
                obj = MySqlProcess()
                obj._deserialize(item)
                self._ProcessList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProxyProcessStatisticsRequest(AbstractModel):
    """DescribeProxyProcessStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _InstanceProxyId: The proxy ID you want to query under the instance
        :type InstanceProxyId: str
        :param _Limit: Number of returned results.
        :type Limit: int
        :param _Product: Service type. Valid value: `redis` (TencentDB for Redis).
        :type Product: str
        :param _Offset: Offset. Default value: `0`.
        :type Offset: int
        :param _SortBy: Sort by field. Valid values: `AllConn`, `ActiveConn`, `Ip`.
        :type SortBy: str
        :param _OrderDirection: Sorting order. Valid values: `DESC`, `ASC`.
        :type OrderDirection: str
        """
        self._InstanceId = None
        self._InstanceProxyId = None
        self._Limit = None
        self._Product = None
        self._Offset = None
        self._SortBy = None
        self._OrderDirection = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceProxyId(self):
        return self._InstanceProxyId

    @InstanceProxyId.setter
    def InstanceProxyId(self, InstanceProxyId):
        self._InstanceProxyId = InstanceProxyId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceProxyId = params.get("InstanceProxyId")
        self._Limit = params.get("Limit")
        self._Product = params.get("Product")
        self._Offset = params.get("Offset")
        self._SortBy = params.get("SortBy")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyProcessStatisticsResponse(AbstractModel):
    """DescribeProxyProcessStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _ProcessStatistics: Real-time session statistics.
        :type ProcessStatistics: :class:`tencentcloud.dbbrain.v20210527.models.ProcessStatistic`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProcessStatistics = None
        self._RequestId = None

    @property
    def ProcessStatistics(self):
        return self._ProcessStatistics

    @ProcessStatistics.setter
    def ProcessStatistics(self, ProcessStatistics):
        self._ProcessStatistics = ProcessStatistics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProcessStatistics") is not None:
            self._ProcessStatistics = ProcessStatistic()
            self._ProcessStatistics._deserialize(params.get("ProcessStatistics"))
        self._RequestId = params.get("RequestId")


class DescribeProxySessionKillTasksRequest(AbstractModel):
    """DescribeProxySessionKillTasks request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _AsyncRequestIds: The async session killing task ID, which is obtained after the API `CreateProxySessionKillTask` is successfully called.
        :type AsyncRequestIds: list of int
        :param _Product: Service type. Valid value: `redis` (TencentDB for Redis).
        :type Product: str
        """
        self._InstanceId = None
        self._AsyncRequestIds = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AsyncRequestIds(self):
        return self._AsyncRequestIds

    @AsyncRequestIds.setter
    def AsyncRequestIds(self, AsyncRequestIds):
        self._AsyncRequestIds = AsyncRequestIds

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AsyncRequestIds = params.get("AsyncRequestIds")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxySessionKillTasksResponse(AbstractModel):
    """DescribeProxySessionKillTasks response structure.

    """

    def __init__(self):
        r"""
        :param _Tasks: Session killing task details.
        :type Tasks: list of TaskInfo
        :param _TotalCount: Total number of tasks.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Tasks = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRedisTopKeyPrefixListRequest(AbstractModel):
    """DescribeRedisTopKeyPrefixList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Date: Date for query, such as `2021-05-27`. You can select a date as early as in the last 30 days for query.
        :type Date: str
        :param _Product: Service type. Valid value: `redis` (TencentDB for Redis).
        :type Product: str
        :param _Limit: The number of queried items. Default value: `20`. Max value: `100`.
        :type Limit: int
        """
        self._InstanceId = None
        self._Date = None
        self._Product = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Date = params.get("Date")
        self._Product = params.get("Product")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRedisTopKeyPrefixListResponse(AbstractModel):
    """DescribeRedisTopKeyPrefixList response structure.

    """

    def __init__(self):
        r"""
        :param _Items: List of top key prefixes
        :type Items: list of RedisPreKeySpaceData
        :param _Timestamp: Data collection timestamp in seconds
        :type Timestamp: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._Timestamp = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = RedisPreKeySpaceData()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Timestamp = params.get("Timestamp")
        self._RequestId = params.get("RequestId")


class DescribeSecurityAuditLogDownloadUrlsRequest(AbstractModel):
    """DescribeSecurityAuditLogDownloadUrls request structure.

    """

    def __init__(self):
        r"""
        :param _SecAuditGroupId: Security audit group ID.
        :type SecAuditGroupId: str
        :param _AsyncRequestId: Async task Id.
        :type AsyncRequestId: int
        :param _Product: Service type. Valid value: `mysql` (TencentDB for MySQL).
        :type Product: str
        """
        self._SecAuditGroupId = None
        self._AsyncRequestId = None
        self._Product = None

    @property
    def SecAuditGroupId(self):
        return self._SecAuditGroupId

    @SecAuditGroupId.setter
    def SecAuditGroupId(self, SecAuditGroupId):
        self._SecAuditGroupId = SecAuditGroupId

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._SecAuditGroupId = params.get("SecAuditGroupId")
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityAuditLogDownloadUrlsResponse(AbstractModel):
    """DescribeSecurityAuditLogDownloadUrls response structure.

    """

    def __init__(self):
        r"""
        :param _Urls: List of COS URLs of the export results. If the result set is large, it may be divided into multiple URLs for download.
        :type Urls: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Urls = None
        self._RequestId = None

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Urls = params.get("Urls")
        self._RequestId = params.get("RequestId")


class DescribeSecurityAuditLogExportTasksRequest(AbstractModel):
    """DescribeSecurityAuditLogExportTasks request structure.

    """

    def __init__(self):
        r"""
        :param _SecAuditGroupId: Security audit group ID.
        :type SecAuditGroupId: str
        :param _Product: Service type. Valid value: `mysql` (TencentDB for MySQL).
        :type Product: str
        :param _AsyncRequestIds: List of log export task IDs.
        :type AsyncRequestIds: list of int non-negative
        :param _Offset: Offset. Default value: `0`.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: `20`. Maximum value: `100`.
        :type Limit: int
        """
        self._SecAuditGroupId = None
        self._Product = None
        self._AsyncRequestIds = None
        self._Offset = None
        self._Limit = None

    @property
    def SecAuditGroupId(self):
        return self._SecAuditGroupId

    @SecAuditGroupId.setter
    def SecAuditGroupId(self, SecAuditGroupId):
        self._SecAuditGroupId = SecAuditGroupId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def AsyncRequestIds(self):
        return self._AsyncRequestIds

    @AsyncRequestIds.setter
    def AsyncRequestIds(self, AsyncRequestIds):
        self._AsyncRequestIds = AsyncRequestIds

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SecAuditGroupId = params.get("SecAuditGroupId")
        self._Product = params.get("Product")
        self._AsyncRequestIds = params.get("AsyncRequestIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityAuditLogExportTasksResponse(AbstractModel):
    """DescribeSecurityAuditLogExportTasks response structure.

    """

    def __init__(self):
        r"""
        :param _Tasks: List of security audit log export tasks.
        :type Tasks: list of SecLogExportTaskInfo
        :param _TotalCount: Total numbers of security audit log export tasks.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Tasks = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = SecLogExportTaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSlowLogTimeSeriesStatsRequest(AbstractModel):
    """DescribeSlowLogTimeSeriesStats request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _StartTime: Start time, such as "2019-09-10 12:13:14".
        :type StartTime: str
        :param _EndTime: End time, such as "2019-09-10 12:13:14". The interval between the end time and the start time can be up to 7 days.
        :type EndTime: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogTimeSeriesStatsResponse(AbstractModel):
    """DescribeSlowLogTimeSeriesStats response structure.

    """

    def __init__(self):
        r"""
        :param _Period: Time range in seconds in histogram.
        :type Period: int
        :param _TimeSeries: Number of slow logs in the specified time range.
        :type TimeSeries: list of TimeSlice
        :param _SeriesData: Instance CPU utilization monitoring data in the specified time range.
        :type SeriesData: :class:`tencentcloud.dbbrain.v20210527.models.MonitorMetricSeriesData`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Period = None
        self._TimeSeries = None
        self._SeriesData = None
        self._RequestId = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def TimeSeries(self):
        return self._TimeSeries

    @TimeSeries.setter
    def TimeSeries(self, TimeSeries):
        self._TimeSeries = TimeSeries

    @property
    def SeriesData(self):
        return self._SeriesData

    @SeriesData.setter
    def SeriesData(self, SeriesData):
        self._SeriesData = SeriesData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Period = params.get("Period")
        if params.get("TimeSeries") is not None:
            self._TimeSeries = []
            for item in params.get("TimeSeries"):
                obj = TimeSlice()
                obj._deserialize(item)
                self._TimeSeries.append(obj)
        if params.get("SeriesData") is not None:
            self._SeriesData = MonitorMetricSeriesData()
            self._SeriesData._deserialize(params.get("SeriesData"))
        self._RequestId = params.get("RequestId")


class DescribeSlowLogTopSqlsRequest(AbstractModel):
    """DescribeSlowLogTopSqls request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _StartTime: Start time, such as "2019-09-10 12:13:14".
        :type StartTime: str
        :param _EndTime: End time in the format of "2019-09-11 10:13:14". The interval between the end time and the start time can be up to 7 days.
        :type EndTime: str
        :param _SortBy: Sorting key. Valid values: `QueryTime`, `ExecTimes`, `RowsSent`, `LockTime`, `RowsExamined`. Default value: `QueryTime`.
        :type SortBy: str
        :param _OrderBy: Sorting order. Valid values: `ASC` (ascending), `DESC` (descending). Default value: `DESC`.
        :type OrderBy: str
        :param _Limit: Number of returned results. Default value: `20`. Maximum value: `100`.
        :type Limit: int
        :param _Offset: Offset. Default value: `0`.
        :type Offset: int
        :param _SchemaList: Database name array.
        :type SchemaList: list of SchemaItem
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._SortBy = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None
        self._SchemaList = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SchemaList(self):
        return self._SchemaList

    @SchemaList.setter
    def SchemaList(self, SchemaList):
        self._SchemaList = SchemaList

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SortBy = params.get("SortBy")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("SchemaList") is not None:
            self._SchemaList = []
            for item in params.get("SchemaList"):
                obj = SchemaItem()
                obj._deserialize(item)
                self._SchemaList.append(obj)
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogTopSqlsResponse(AbstractModel):
    """DescribeSlowLogTopSqls response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param _Rows: List of top slow SQL statements
        :type Rows: list of SlowLogTopSqlItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Rows(self):
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = SlowLogTopSqlItem()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowLogUserHostStatsRequest(AbstractModel):
    """DescribeSlowLogUserHostStats request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _StartTime: Start time of the time range in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14.
        :type StartTime: str
        :param _EndTime: End time of the time range in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14.
        :type EndTime: str
        :param _Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.
        :type Product: str
        :param _Md5: MD5 value of SOL template
        :type Md5: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None
        self._Md5 = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Md5(self):
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        self._Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogUserHostStatsResponse(AbstractModel):
    """DescribeSlowLogUserHostStats response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of source addresses.
        :type TotalCount: int
        :param _Items: Detailed list of the proportion of slow logs from each source address.
        :type Items: list of SlowLogHost
        :param _UserNameItems: Detailed list of the percentages of slow logs from different source usernames
        :type UserNameItems: list of SlowLogUser
        :param _UserTotalCount: The number of source users
        :type UserTotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._UserNameItems = None
        self._UserTotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def UserNameItems(self):
        return self._UserNameItems

    @UserNameItems.setter
    def UserNameItems(self, UserNameItems):
        self._UserNameItems = UserNameItems

    @property
    def UserTotalCount(self):
        return self._UserTotalCount

    @UserTotalCount.setter
    def UserTotalCount(self, UserTotalCount):
        self._UserTotalCount = UserTotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SlowLogHost()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("UserNameItems") is not None:
            self._UserNameItems = []
            for item in params.get("UserNameItems"):
                obj = SlowLogUser()
                obj._deserialize(item)
                self._UserNameItems.append(obj)
        self._UserTotalCount = params.get("UserTotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSlowLogsRequest(AbstractModel):
    """DescribeSlowLogs request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Md5: MD5 value of a SQL template
        :type Md5: str
        :param _StartTime: Start time in the format of "2019-09-10 12:13:14".
        :type StartTime: str
        :param _EndTime: End time in the format of "2019-09-11 10:13:14". The interval between the end time and the start time can be up to 7 days.
        :type EndTime: str
        :param _Offset: The offset. Default value: `0`.
        :type Offset: int
        :param _Limit: The number of queried items. Default value: `20`. Max value: `100`.
        :type Limit: int
        :param _DB: Database list
        :type DB: list of str
        :param _Key: Keyword
        :type Key: list of str
        :param _User: User
        :type User: list of str
        :param _Ip: IP
        :type Ip: list of str
        :param _Time: Duration range. The left and right borders of the range are the zeroth and first element of the array, respectively.
        :type Time: list of int
        """
        self._Product = None
        self._InstanceId = None
        self._Md5 = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._DB = None
        self._Key = None
        self._User = None
        self._Ip = None
        self._Time = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Md5(self):
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DB(self):
        return self._DB

    @DB.setter
    def DB(self, DB):
        self._DB = DB

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        self._Md5 = params.get("Md5")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DB = params.get("DB")
        self._Key = params.get("Key")
        self._User = params.get("User")
        self._Ip = params.get("Ip")
        self._Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogsResponse(AbstractModel):
    """DescribeSlowLogs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param _Rows: Slow log details
        :type Rows: list of SlowLogInfoItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Rows(self):
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = SlowLogInfoItem()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopSpaceSchemaTimeSeriesRequest(AbstractModel):
    """DescribeTopSpaceSchemaTimeSeries request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Limit: Number of returned top databases. Maximum value: `100`. Default value: `20`.
        :type Limit: int
        :param _SortBy: Field used to sort top databases. Valid values: `DataLength`, `IndexLength`, `TotalLength`, `DataFree`, `FragRatio`, `TableRows`, `PhysicalFileSize` (supported only by TencentDB for MySQL instances). For TencentDB for MySQL instances, the default value is `PhysicalFileSize`. For other database instances, the default value is `TotalLength`.
        :type SortBy: str
        :param _StartDate: Start date, such as "2021-01-01". It can be as early as 29 days before the current date and is 6 days before the end date by default.
        :type StartDate: str
        :param _EndDate: End date, such as "2021-01-01". It can be as early as 29 days before the current date and is the current date by default.
        :type EndDate: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._Limit = None
        self._SortBy = None
        self._StartDate = None
        self._EndDate = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceSchemaTimeSeriesResponse(AbstractModel):
    """DescribeTopSpaceSchemaTimeSeries response structure.

    """

    def __init__(self):
        r"""
        :param _TopSpaceSchemaTimeSeries: Time series list of the returned space statistics of top databases.
        :type TopSpaceSchemaTimeSeries: list of SchemaSpaceTimeSeries
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopSpaceSchemaTimeSeries = None
        self._RequestId = None

    @property
    def TopSpaceSchemaTimeSeries(self):
        return self._TopSpaceSchemaTimeSeries

    @TopSpaceSchemaTimeSeries.setter
    def TopSpaceSchemaTimeSeries(self, TopSpaceSchemaTimeSeries):
        self._TopSpaceSchemaTimeSeries = TopSpaceSchemaTimeSeries

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopSpaceSchemaTimeSeries") is not None:
            self._TopSpaceSchemaTimeSeries = []
            for item in params.get("TopSpaceSchemaTimeSeries"):
                obj = SchemaSpaceTimeSeries()
                obj._deserialize(item)
                self._TopSpaceSchemaTimeSeries.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopSpaceSchemasRequest(AbstractModel):
    """DescribeTopSpaceSchemas request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Limit: Number of returned top databases. Maximum value: 100. Default value: 20.
        :type Limit: int
        :param _SortBy: Field used to sort top databases. Valid values: DataLength, IndexLength, TotalLength, DataFree, FragRatio, TableRows, PhysicalFileSize (supported only by TencentDB for MySQL instances). For TencentDB for MySQL instances, the default value is `PhysicalFileSize`. For other database instances, the default value is `TotalLength`.
        :type SortBy: str
        :param _Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.
        :type Product: str
        """
        self._InstanceId = None
        self._Limit = None
        self._SortBy = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceSchemasResponse(AbstractModel):
    """DescribeTopSpaceSchemas response structure.

    """

    def __init__(self):
        r"""
        :param _TopSpaceSchemas: List of the returned space statistics of top databases.
        :type TopSpaceSchemas: list of SchemaSpaceData
        :param _Timestamp: Timestamp (in seconds) of database space data collection points
        :type Timestamp: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopSpaceSchemas = None
        self._Timestamp = None
        self._RequestId = None

    @property
    def TopSpaceSchemas(self):
        return self._TopSpaceSchemas

    @TopSpaceSchemas.setter
    def TopSpaceSchemas(self, TopSpaceSchemas):
        self._TopSpaceSchemas = TopSpaceSchemas

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopSpaceSchemas") is not None:
            self._TopSpaceSchemas = []
            for item in params.get("TopSpaceSchemas"):
                obj = SchemaSpaceData()
                obj._deserialize(item)
                self._TopSpaceSchemas.append(obj)
        self._Timestamp = params.get("Timestamp")
        self._RequestId = params.get("RequestId")


class DescribeTopSpaceTableTimeSeriesRequest(AbstractModel):
    """DescribeTopSpaceTableTimeSeries request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Limit: Number of returned top tables. Maximum value: `100`. Default value: `20`.
        :type Limit: int
        :param _SortBy: Field used to sort top tables. Valid values: `DataLength`, `IndexLength`, `TotalLength`, `DataFree`, `FragRatio`, `TableRows`, `PhysicalFileSize`. Default value: `PhysicalFileSize`.
        :type SortBy: str
        :param _StartDate: Start date, such as "2021-01-01". It can be as early as 29 days before the current date and is 6 days before the end date by default.
        :type StartDate: str
        :param _EndDate: End date, such as "2021-01-01". It can be as early as 29 days before the current date and is the current date by default.
        :type EndDate: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._Limit = None
        self._SortBy = None
        self._StartDate = None
        self._EndDate = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceTableTimeSeriesResponse(AbstractModel):
    """DescribeTopSpaceTableTimeSeries response structure.

    """

    def __init__(self):
        r"""
        :param _TopSpaceTableTimeSeries: Time series list of the returned space statistics of top tables.
        :type TopSpaceTableTimeSeries: list of TableSpaceTimeSeries
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopSpaceTableTimeSeries = None
        self._RequestId = None

    @property
    def TopSpaceTableTimeSeries(self):
        return self._TopSpaceTableTimeSeries

    @TopSpaceTableTimeSeries.setter
    def TopSpaceTableTimeSeries(self, TopSpaceTableTimeSeries):
        self._TopSpaceTableTimeSeries = TopSpaceTableTimeSeries

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopSpaceTableTimeSeries") is not None:
            self._TopSpaceTableTimeSeries = []
            for item in params.get("TopSpaceTableTimeSeries"):
                obj = TableSpaceTimeSeries()
                obj._deserialize(item)
                self._TopSpaceTableTimeSeries.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopSpaceTablesRequest(AbstractModel):
    """DescribeTopSpaceTables request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Limit: Number of returned top tables. Maximum value: `100`. Default value: `20`.
        :type Limit: int
        :param _SortBy: Field used to sort top tables. Valid values: `DataLength`, `IndexLength`, `TotalLength`, `DataFree`, `FragRatio`, `TableRows`, `PhysicalFileSize` (only supported for TencentDB for MySQL instances). For TencentDB for MySQL instances, the default value is `PhysicalFileSize`. For other database instances, the default value is `TotalLength`.
        :type SortBy: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._Limit = None
        self._SortBy = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceTablesResponse(AbstractModel):
    """DescribeTopSpaceTables response structure.

    """

    def __init__(self):
        r"""
        :param _TopSpaceTables: List of the returned space statistics of top tables.
        :type TopSpaceTables: list of TableSpaceData
        :param _Timestamp: Timestamp (in seconds) of tablespace data collection points
        :type Timestamp: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopSpaceTables = None
        self._Timestamp = None
        self._RequestId = None

    @property
    def TopSpaceTables(self):
        return self._TopSpaceTables

    @TopSpaceTables.setter
    def TopSpaceTables(self, TopSpaceTables):
        self._TopSpaceTables = TopSpaceTables

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopSpaceTables") is not None:
            self._TopSpaceTables = []
            for item in params.get("TopSpaceTables"):
                obj = TableSpaceData()
                obj._deserialize(item)
                self._TopSpaceTables.append(obj)
        self._Timestamp = params.get("Timestamp")
        self._RequestId = params.get("RequestId")


class DescribeUserSqlAdviceRequest(AbstractModel):
    """DescribeUserSqlAdvice request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _SqlText: SQL statement.
        :type SqlText: str
        :param _Schema: Database name.
        :type Schema: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL), `dbbrain-mysql` (self-built MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._SqlText = None
        self._Schema = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SqlText(self):
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def Schema(self):
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SqlText = params.get("SqlText")
        self._Schema = params.get("Schema")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserSqlAdviceResponse(AbstractModel):
    """DescribeUserSqlAdvice response structure.

    """

    def __init__(self):
        r"""
        :param _Advices: SQL statement optimization suggestions, which can be parsed into JSON arrays. If there is no need for optimization, the output will be empty.
        :type Advices: str
        :param _Comments: Notes of SQL statement optimization suggestions, which can be parsed into String arrays. If there is no need for optimization, the output will be empty.
        :type Comments: str
        :param _SqlText: SQL statement.
        :type SqlText: str
        :param _Schema: Database name.
        :type Schema: str
        :param _Tables: DDL information of related tables, which can be parsed into JSON arrays.
        :type Tables: str
        :param _SqlPlan: SQL execution plan, which can be parsed into JSON arrays. If there is no need for optimization, the output will be empty.
        :type SqlPlan: str
        :param _Cost: Cost saving details after SQL statement optimization, which can be parsed into JSON arrays. If there is no need for optimization, the output will be empty.
        :type Cost: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Advices = None
        self._Comments = None
        self._SqlText = None
        self._Schema = None
        self._Tables = None
        self._SqlPlan = None
        self._Cost = None
        self._RequestId = None

    @property
    def Advices(self):
        return self._Advices

    @Advices.setter
    def Advices(self, Advices):
        self._Advices = Advices

    @property
    def Comments(self):
        return self._Comments

    @Comments.setter
    def Comments(self, Comments):
        self._Comments = Comments

    @property
    def SqlText(self):
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def Schema(self):
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def Tables(self):
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def SqlPlan(self):
        return self._SqlPlan

    @SqlPlan.setter
    def SqlPlan(self, SqlPlan):
        self._SqlPlan = SqlPlan

    @property
    def Cost(self):
        return self._Cost

    @Cost.setter
    def Cost(self, Cost):
        self._Cost = Cost

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Advices = params.get("Advices")
        self._Comments = params.get("Comments")
        self._SqlText = params.get("SqlText")
        self._Schema = params.get("Schema")
        self._Tables = params.get("Tables")
        self._SqlPlan = params.get("SqlPlan")
        self._Cost = params.get("Cost")
        self._RequestId = params.get("RequestId")


class DiagHistoryEventItem(AbstractModel):
    """Instance diagnosis event

    """

    def __init__(self):
        r"""
        :param _DiagType: Diagnosis type.
        :type DiagType: str
        :param _EndTime: End time.
        :type EndTime: str
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EventId: Unique event ID.
        :type EventId: int
        :param _Severity: Severity, which can be divided into 5 levels: 1: fatal, 2: severe, 3: warning, 4: notice, 5: healthy.
        :type Severity: int
        :param _Outline: Diagnosis summary.
        :type Outline: str
        :param _DiagItem: Diagnosis item description.
        :type DiagItem: str
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Metric: Reserved field.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Metric: str
        :param _Region: Region.
        :type Region: str
        """
        self._DiagType = None
        self._EndTime = None
        self._StartTime = None
        self._EventId = None
        self._Severity = None
        self._Outline = None
        self._DiagItem = None
        self._InstanceId = None
        self._Metric = None
        self._Region = None

    @property
    def DiagType(self):
        return self._DiagType

    @DiagType.setter
    def DiagType(self, DiagType):
        self._DiagType = DiagType

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Severity(self):
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def Outline(self):
        return self._Outline

    @Outline.setter
    def Outline(self, Outline):
        self._Outline = Outline

    @property
    def DiagItem(self):
        return self._DiagItem

    @DiagItem.setter
    def DiagItem(self, DiagItem):
        self._DiagItem = DiagItem

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._DiagType = params.get("DiagType")
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        self._EventId = params.get("EventId")
        self._Severity = params.get("Severity")
        self._Outline = params.get("Outline")
        self._DiagItem = params.get("DiagItem")
        self._InstanceId = params.get("InstanceId")
        self._Metric = params.get("Metric")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventInfo(AbstractModel):
    """Exception information.

    """

    def __init__(self):
        r"""
        :param _EventId: Event ID.
        :type EventId: int
        :param _DiagType: Diagnosis type.
        :type DiagType: str
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EndTime: End time.
        :type EndTime: str
        :param _Outline: Summary.
        :type Outline: str
        :param _Severity: Severity, which can be divided into 5 levels: `1` (Critical), `2` (Severe), `3` (Alarm), `4` (Reminder), `5` (Healthy).
        :type Severity: int
        :param _ScoreLost: Deduction.
        :type ScoreLost: int
        :param _Metric: Reserved field.
        :type Metric: str
        :param _Count: Number of alarms.
        :type Count: int
        """
        self._EventId = None
        self._DiagType = None
        self._StartTime = None
        self._EndTime = None
        self._Outline = None
        self._Severity = None
        self._ScoreLost = None
        self._Metric = None
        self._Count = None

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def DiagType(self):
        return self._DiagType

    @DiagType.setter
    def DiagType(self, DiagType):
        self._DiagType = DiagType

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Outline(self):
        return self._Outline

    @Outline.setter
    def Outline(self, Outline):
        self._Outline = Outline

    @property
    def Severity(self):
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def ScoreLost(self):
        return self._ScoreLost

    @ScoreLost.setter
    def ScoreLost(self, ScoreLost):
        self._ScoreLost = ScoreLost

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._DiagType = params.get("DiagType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Outline = params.get("Outline")
        self._Severity = params.get("Severity")
        self._ScoreLost = params.get("ScoreLost")
        self._Metric = params.get("Metric")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupItem(AbstractModel):
    """Describes the group information.

    """

    def __init__(self):
        r"""
        :param _Id: Group ID.
        :type Id: int
        :param _Name: Group name.
        :type Name: str
        :param _MemberCount: Number of group members.
        :type MemberCount: int
        """
        self._Id = None
        self._Name = None
        self._MemberCount = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MemberCount(self):
        return self._MemberCount

    @MemberCount.setter
    def MemberCount(self, MemberCount):
        self._MemberCount = MemberCount


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._MemberCount = params.get("MemberCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthReportTask(AbstractModel):
    """Details of the health report task.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID.
        :type AsyncRequestId: int
        :param _Source: Source that triggers the task. Valid values: `DAILY_INSPECTION` (instance inspection), `SCHEDULED` (scheduled task), and `MANUAL` (manual trigger).
        :type Source: str
        :param _Progress: Task progress in %.
        :type Progress: int
        :param _CreateTime: Task creation time.
        :type CreateTime: str
        :param _StartTime: Task start time.
        :type StartTime: str
        :param _EndTime: Task end time.
        :type EndTime: str
        :param _InstanceInfo: Basic information of the instance to which the task belongs.
        :type InstanceInfo: :class:`tencentcloud.dbbrain.v20210527.models.InstanceBasicInfo`
        :param _HealthStatus: Health information in health report.
        :type HealthStatus: :class:`tencentcloud.dbbrain.v20210527.models.HealthStatus`
        """
        self._AsyncRequestId = None
        self._Source = None
        self._Progress = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._InstanceInfo = None
        self._HealthStatus = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InstanceInfo(self):
        return self._InstanceInfo

    @InstanceInfo.setter
    def InstanceInfo(self, InstanceInfo):
        self._InstanceInfo = InstanceInfo

    @property
    def HealthStatus(self):
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._Source = params.get("Source")
        self._Progress = params.get("Progress")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("InstanceInfo") is not None:
            self._InstanceInfo = InstanceBasicInfo()
            self._InstanceInfo._deserialize(params.get("InstanceInfo"))
        if params.get("HealthStatus") is not None:
            self._HealthStatus = HealthStatus()
            self._HealthStatus._deserialize(params.get("HealthStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthScoreInfo(AbstractModel):
    """Details of the obtained health score.

    """

    def __init__(self):
        r"""
        :param _IssueTypes: Exception details.
        :type IssueTypes: list of IssueTypeInfo
        :param _EventsTotalCount: Total number of exceptions.
        :type EventsTotalCount: int
        :param _HealthScore: Health score.
        :type HealthScore: int
        :param _HealthLevel: Health level, such as `HEALTH`, `SUB_HEALTH`, `RISK`, and `HIGH_RISK`.
        :type HealthLevel: str
        """
        self._IssueTypes = None
        self._EventsTotalCount = None
        self._HealthScore = None
        self._HealthLevel = None

    @property
    def IssueTypes(self):
        return self._IssueTypes

    @IssueTypes.setter
    def IssueTypes(self, IssueTypes):
        self._IssueTypes = IssueTypes

    @property
    def EventsTotalCount(self):
        return self._EventsTotalCount

    @EventsTotalCount.setter
    def EventsTotalCount(self, EventsTotalCount):
        self._EventsTotalCount = EventsTotalCount

    @property
    def HealthScore(self):
        return self._HealthScore

    @HealthScore.setter
    def HealthScore(self, HealthScore):
        self._HealthScore = HealthScore

    @property
    def HealthLevel(self):
        return self._HealthLevel

    @HealthLevel.setter
    def HealthLevel(self, HealthLevel):
        self._HealthLevel = HealthLevel


    def _deserialize(self, params):
        if params.get("IssueTypes") is not None:
            self._IssueTypes = []
            for item in params.get("IssueTypes"):
                obj = IssueTypeInfo()
                obj._deserialize(item)
                self._IssueTypes.append(obj)
        self._EventsTotalCount = params.get("EventsTotalCount")
        self._HealthScore = params.get("HealthScore")
        self._HealthLevel = params.get("HealthLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthStatus(AbstractModel):
    """Instance health status.

    """

    def __init__(self):
        r"""
        :param _HealthScore: Health score out of 100 points.
        :type HealthScore: int
        :param _HealthLevel: Health level. Valid values: `HEALTH` (healthy), `SUB_HEALTH` (sub-healthy), `RISK` (dangerous), and `HIGH_RISK` (high-risk).
        :type HealthLevel: str
        :param _ScoreLost: Total deducted scores.
        :type ScoreLost: int
        :param _ScoreDetails: Deduction details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ScoreDetails: list of ScoreDetail
        """
        self._HealthScore = None
        self._HealthLevel = None
        self._ScoreLost = None
        self._ScoreDetails = None

    @property
    def HealthScore(self):
        return self._HealthScore

    @HealthScore.setter
    def HealthScore(self, HealthScore):
        self._HealthScore = HealthScore

    @property
    def HealthLevel(self):
        return self._HealthLevel

    @HealthLevel.setter
    def HealthLevel(self, HealthLevel):
        self._HealthLevel = HealthLevel

    @property
    def ScoreLost(self):
        return self._ScoreLost

    @ScoreLost.setter
    def ScoreLost(self, ScoreLost):
        self._ScoreLost = ScoreLost

    @property
    def ScoreDetails(self):
        return self._ScoreDetails

    @ScoreDetails.setter
    def ScoreDetails(self, ScoreDetails):
        self._ScoreDetails = ScoreDetails


    def _deserialize(self, params):
        self._HealthScore = params.get("HealthScore")
        self._HealthLevel = params.get("HealthLevel")
        self._ScoreLost = params.get("ScoreLost")
        if params.get("ScoreDetails") is not None:
            self._ScoreDetails = []
            for item in params.get("ScoreDetails"):
                obj = ScoreDetail()
                obj._deserialize(item)
                self._ScoreDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceBasicInfo(AbstractModel):
    """Basic instance information.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _InstanceName: Instance name.
        :type InstanceName: str
        :param _Vip: Private IP of the instance.
        :type Vip: str
        :param _Vport: Private port of the instance.
        :type Vport: int
        :param _Product: Instance service.
        :type Product: str
        :param _EngineVersion: Instance engine version.
        :type EngineVersion: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Vip = None
        self._Vport = None
        self._Product = None
        self._EngineVersion = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._Product = params.get("Product")
        self._EngineVersion = params.get("EngineVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfs(AbstractModel):
    """Instance configuration.

    """

    def __init__(self):
        r"""
        :param _DailyInspection: Whether to enable database inspection. Valid values: Yes, No.
        :type DailyInspection: str
        :param _OverviewDisplay: Whether to enable instance overview. Valid values: Yes, No.
        :type OverviewDisplay: str
        :param _KeyDelimiters: Custom big key analysis separator for Redis only
Note: This field may return null, indicating that no valid values can be obtained.
        :type KeyDelimiters: list of str
        """
        self._DailyInspection = None
        self._OverviewDisplay = None
        self._KeyDelimiters = None

    @property
    def DailyInspection(self):
        return self._DailyInspection

    @DailyInspection.setter
    def DailyInspection(self, DailyInspection):
        self._DailyInspection = DailyInspection

    @property
    def OverviewDisplay(self):
        return self._OverviewDisplay

    @OverviewDisplay.setter
    def OverviewDisplay(self, OverviewDisplay):
        self._OverviewDisplay = OverviewDisplay

    @property
    def KeyDelimiters(self):
        return self._KeyDelimiters

    @KeyDelimiters.setter
    def KeyDelimiters(self, KeyDelimiters):
        self._KeyDelimiters = KeyDelimiters


    def _deserialize(self, params):
        self._DailyInspection = params.get("DailyInspection")
        self._OverviewDisplay = params.get("OverviewDisplay")
        self._KeyDelimiters = params.get("KeyDelimiters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """Queries the list of instances and returns their information.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _InstanceName: Instance name.
        :type InstanceName: str
        :param _Region: Instance region.
        :type Region: str
        :param _HealthScore: Health score.
        :type HealthScore: int
        :param _Product: Service.
        :type Product: str
        :param _EventCount: Number of exceptions.
        :type EventCount: int
        :param _InstanceType: Instance type. Valid values: 1 (MASTER), 2 (DR), 3 (RO), 4 (SDR)
        :type InstanceType: int
        :param _Cpu: Number of cores.
        :type Cpu: int
        :param _Memory: Memory in MB.
        :type Memory: int
        :param _Volume: Disk storage in GB.
        :type Volume: int
        :param _EngineVersion: Database version.
        :type EngineVersion: str
        :param _Vip: Private network address.
        :type Vip: str
        :param _Vport: Private network port.
        :type Vport: int
        :param _Source: Access source.
        :type Source: str
        :param _GroupId: Group ID.
        :type GroupId: str
        :param _GroupName: Group name.
        :type GroupName: str
        :param _Status: Instance status. Valid values: 0 (delivering), 1 (running), 4 (terminating), 5 (isolated)
        :type Status: int
        :param _UniqSubnetId: Unified subnet ID.
        :type UniqSubnetId: str
        :param _DeployMode: TencentDB instance type.
        :type DeployMode: str
        :param _InitFlag: TencentDB instance initialization flag. Valid values: 0 (not initialized), 1 (initialized).
        :type InitFlag: int
        :param _TaskStatus: Task status.
        :type TaskStatus: int
        :param _UniqVpcId: Unified VPC ID.
        :type UniqVpcId: str
        :param _InstanceConf: Instance inspection/overview status.
        :type InstanceConf: :class:`tencentcloud.dbbrain.v20210527.models.InstanceConfs`
        :param _DeadlineTime: Resource expiration time.
        :type DeadlineTime: str
        :param _IsSupported: Whether it is an instance supported by DBbrain.
        :type IsSupported: bool
        :param _SecAuditStatus: Status of instance security audit log. Valid values: ON (enabled), OFF (disabled).
        :type SecAuditStatus: str
        :param _AuditPolicyStatus: Status of instance audit log. Valid values: ALL_AUDIT (full audit is enabled), RULE_AUDIT (rule audit is enabled), UNBOUND (audit is disabled).
        :type AuditPolicyStatus: str
        :param _AuditRunningStatus: Running status of instance audit log. Valid values: normal (running), paused (suspension due to overdue payment).
        :type AuditRunningStatus: str
        :param _InternalVip: Private VIP 
Note: This field may return null, indicating that no valid values can be obtained.
        :type InternalVip: str
        :param _InternalVport: Private network port 
Note: This field may return null, indicating that no valid values can be obtained.
        :type InternalVport: int
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _ClusterId: Cluster ID. This field is only required for cluster database products like TDSQL-C. 
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param _ClusterName: Cluster name. This field is only required for cluster database products like TDSQL-C. 
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterName: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None
        self._HealthScore = None
        self._Product = None
        self._EventCount = None
        self._InstanceType = None
        self._Cpu = None
        self._Memory = None
        self._Volume = None
        self._EngineVersion = None
        self._Vip = None
        self._Vport = None
        self._Source = None
        self._GroupId = None
        self._GroupName = None
        self._Status = None
        self._UniqSubnetId = None
        self._DeployMode = None
        self._InitFlag = None
        self._TaskStatus = None
        self._UniqVpcId = None
        self._InstanceConf = None
        self._DeadlineTime = None
        self._IsSupported = None
        self._SecAuditStatus = None
        self._AuditPolicyStatus = None
        self._AuditRunningStatus = None
        self._InternalVip = None
        self._InternalVport = None
        self._CreateTime = None
        self._ClusterId = None
        self._ClusterName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def HealthScore(self):
        return self._HealthScore

    @HealthScore.setter
    def HealthScore(self, HealthScore):
        self._HealthScore = HealthScore

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def EventCount(self):
        return self._EventCount

    @EventCount.setter
    def EventCount(self, EventCount):
        self._EventCount = EventCount

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def InitFlag(self):
        return self._InitFlag

    @InitFlag.setter
    def InitFlag(self, InitFlag):
        self._InitFlag = InitFlag

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def InstanceConf(self):
        return self._InstanceConf

    @InstanceConf.setter
    def InstanceConf(self, InstanceConf):
        self._InstanceConf = InstanceConf

    @property
    def DeadlineTime(self):
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def IsSupported(self):
        return self._IsSupported

    @IsSupported.setter
    def IsSupported(self, IsSupported):
        self._IsSupported = IsSupported

    @property
    def SecAuditStatus(self):
        return self._SecAuditStatus

    @SecAuditStatus.setter
    def SecAuditStatus(self, SecAuditStatus):
        self._SecAuditStatus = SecAuditStatus

    @property
    def AuditPolicyStatus(self):
        return self._AuditPolicyStatus

    @AuditPolicyStatus.setter
    def AuditPolicyStatus(self, AuditPolicyStatus):
        self._AuditPolicyStatus = AuditPolicyStatus

    @property
    def AuditRunningStatus(self):
        return self._AuditRunningStatus

    @AuditRunningStatus.setter
    def AuditRunningStatus(self, AuditRunningStatus):
        self._AuditRunningStatus = AuditRunningStatus

    @property
    def InternalVip(self):
        return self._InternalVip

    @InternalVip.setter
    def InternalVip(self, InternalVip):
        self._InternalVip = InternalVip

    @property
    def InternalVport(self):
        return self._InternalVport

    @InternalVport.setter
    def InternalVport(self, InternalVport):
        self._InternalVport = InternalVport

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        self._HealthScore = params.get("HealthScore")
        self._Product = params.get("Product")
        self._EventCount = params.get("EventCount")
        self._InstanceType = params.get("InstanceType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._EngineVersion = params.get("EngineVersion")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._Source = params.get("Source")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Status = params.get("Status")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._DeployMode = params.get("DeployMode")
        self._InitFlag = params.get("InitFlag")
        self._TaskStatus = params.get("TaskStatus")
        self._UniqVpcId = params.get("UniqVpcId")
        if params.get("InstanceConf") is not None:
            self._InstanceConf = InstanceConfs()
            self._InstanceConf._deserialize(params.get("InstanceConf"))
        self._DeadlineTime = params.get("DeadlineTime")
        self._IsSupported = params.get("IsSupported")
        self._SecAuditStatus = params.get("SecAuditStatus")
        self._AuditPolicyStatus = params.get("AuditPolicyStatus")
        self._AuditRunningStatus = params.get("AuditRunningStatus")
        self._InternalVip = params.get("InternalVip")
        self._InternalVport = params.get("InternalVport")
        self._CreateTime = params.get("CreateTime")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IssueTypeInfo(AbstractModel):
    """Metric information.

    """

    def __init__(self):
        r"""
        :param _IssueType: Metric categories. Valid values: `AVAILABILITY`, `MAINTAINABILITY`, `PERFORMANCE`, and `RELIABILITY`.
        :type IssueType: str
        :param _Events: Exception.
        :type Events: list of EventInfo
        :param _TotalCount: Total number of exceptions.
        :type TotalCount: int
        """
        self._IssueType = None
        self._Events = None
        self._TotalCount = None

    @property
    def IssueType(self):
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._IssueType = params.get("IssueType")
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = EventInfo()
                obj._deserialize(item)
                self._Events.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillMySqlThreadsRequest(AbstractModel):
    """KillMySqlThreads request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Stage: The stage of a session killing task. Valid values: `Prepare` (preparation stage), `Commit` (commit stage).
        :type Stage: str
        :param _Threads: List of IDs of the MySQL sessions to be killed. This parameter is used in the `Prepare` stage.
        :type Threads: list of int
        :param _SqlExecId: Execution ID. This parameter is used in the `Commit` stage.
        :type SqlExecId: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        :param _RecordHistory: Whether to record the thread killing history. The default value is `true`, indicating “yes”. You can set it to `false` (“no”) to speed up the killing process.
        :type RecordHistory: bool
        """
        self._InstanceId = None
        self._Stage = None
        self._Threads = None
        self._SqlExecId = None
        self._Product = None
        self._RecordHistory = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Stage(self):
        return self._Stage

    @Stage.setter
    def Stage(self, Stage):
        self._Stage = Stage

    @property
    def Threads(self):
        return self._Threads

    @Threads.setter
    def Threads(self, Threads):
        self._Threads = Threads

    @property
    def SqlExecId(self):
        return self._SqlExecId

    @SqlExecId.setter
    def SqlExecId(self, SqlExecId):
        self._SqlExecId = SqlExecId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def RecordHistory(self):
        return self._RecordHistory

    @RecordHistory.setter
    def RecordHistory(self, RecordHistory):
        self._RecordHistory = RecordHistory


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Stage = params.get("Stage")
        self._Threads = params.get("Threads")
        self._SqlExecId = params.get("SqlExecId")
        self._Product = params.get("Product")
        self._RecordHistory = params.get("RecordHistory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillMySqlThreadsResponse(AbstractModel):
    """KillMySqlThreads response structure.

    """

    def __init__(self):
        r"""
        :param _Threads: List of IDs of the MySQL sessions that have been killed.
        :type Threads: list of int
        :param _SqlExecId: Execution ID, which is output in the `Prepare` stage and used to specify the ID of the session to be killed in the `Commit` stage.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SqlExecId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Threads = None
        self._SqlExecId = None
        self._RequestId = None

    @property
    def Threads(self):
        return self._Threads

    @Threads.setter
    def Threads(self, Threads):
        self._Threads = Threads

    @property
    def SqlExecId(self):
        return self._SqlExecId

    @SqlExecId.setter
    def SqlExecId(self, SqlExecId):
        self._SqlExecId = SqlExecId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Threads = params.get("Threads")
        self._SqlExecId = params.get("SqlExecId")
        self._RequestId = params.get("RequestId")


class MailConfiguration(AbstractModel):
    """Email sending configuration

    """

    def __init__(self):
        r"""
        :param _SendMail: Whether to enable email sending. Valid values: `0` (no), `1` (yes).
        :type SendMail: int
        :param _Region: Region configuration, such as "ap-guangzhou" and "ap-shanghai". For the inspection email sending template, configure the region where you need to send the inspection email. For the subscription email sending template, configure the region where the current subscribed instance resides.
        :type Region: list of str
        :param _HealthStatus: Sends a report with the specified health level, such as `HEALTH`, `SUB_HEALTH`, `RISK`, and `HIGH_RISK`.
        :type HealthStatus: list of str
        :param _ContactPerson: Recipient ID. Either `ContactPerson` or `ContactGroup` should be passed in.
        :type ContactPerson: list of int
        :param _ContactGroup: Recipient group ID. Either `ContactPerson` or `ContactGroup` should be passed in.
        :type ContactGroup: list of int
        """
        self._SendMail = None
        self._Region = None
        self._HealthStatus = None
        self._ContactPerson = None
        self._ContactGroup = None

    @property
    def SendMail(self):
        return self._SendMail

    @SendMail.setter
    def SendMail(self, SendMail):
        self._SendMail = SendMail

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def HealthStatus(self):
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def ContactPerson(self):
        return self._ContactPerson

    @ContactPerson.setter
    def ContactPerson(self, ContactPerson):
        self._ContactPerson = ContactPerson

    @property
    def ContactGroup(self):
        return self._ContactGroup

    @ContactGroup.setter
    def ContactGroup(self, ContactGroup):
        self._ContactGroup = ContactGroup


    def _deserialize(self, params):
        self._SendMail = params.get("SendMail")
        self._Region = params.get("Region")
        self._HealthStatus = params.get("HealthStatus")
        self._ContactPerson = params.get("ContactPerson")
        self._ContactGroup = params.get("ContactGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiagDBInstanceConfRequest(AbstractModel):
    """ModifyDiagDBInstanceConf request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceConfs: Instance configuration, including inspection and overview switch.
        :type InstanceConfs: :class:`tencentcloud.dbbrain.v20210527.models.InstanceConfs`
        :param _Regions: Target regions of the request. If the value is `All`, it is applied to all regions.
        :type Regions: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL).
        :type Product: str
        :param _InstanceIds: ID of the instance to modify.
        :type InstanceIds: list of str
        """
        self._InstanceConfs = None
        self._Regions = None
        self._Product = None
        self._InstanceIds = None

    @property
    def InstanceConfs(self):
        return self._InstanceConfs

    @InstanceConfs.setter
    def InstanceConfs(self, InstanceConfs):
        self._InstanceConfs = InstanceConfs

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        if params.get("InstanceConfs") is not None:
            self._InstanceConfs = InstanceConfs()
            self._InstanceConfs._deserialize(params.get("InstanceConfs"))
        self._Regions = params.get("Regions")
        self._Product = params.get("Product")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiagDBInstanceConfResponse(AbstractModel):
    """ModifyDiagDBInstanceConf response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MonitorFloatMetric(AbstractModel):
    """Monitoring data in float type

    """

    def __init__(self):
        r"""
        :param _Metric: Metric name.
        :type Metric: str
        :param _Unit: Metric unit.
        :type Unit: str
        :param _Values: Metric value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Values: list of float
        """
        self._Metric = None
        self._Unit = None
        self._Values = None

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        self._Unit = params.get("Unit")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorFloatMetricSeriesData(AbstractModel):
    """Monitoring metric value in float type in a unit of time interval

    """

    def __init__(self):
        r"""
        :param _Series: Monitoring metric.
        :type Series: list of MonitorFloatMetric
        :param _Timestamp: Timestamp corresponding to monitoring metric.
        :type Timestamp: list of int
        """
        self._Series = None
        self._Timestamp = None

    @property
    def Series(self):
        return self._Series

    @Series.setter
    def Series(self, Series):
        self._Series = Series

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        if params.get("Series") is not None:
            self._Series = []
            for item in params.get("Series"):
                obj = MonitorFloatMetric()
                obj._deserialize(item)
                self._Series.append(obj)
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorMetric(AbstractModel):
    """Monitoring data

    """

    def __init__(self):
        r"""
        :param _Metric: Metric name.
        :type Metric: str
        :param _Unit: Metric unit.
        :type Unit: str
        :param _Values: Metric value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Values: list of float
        """
        self._Metric = None
        self._Unit = None
        self._Values = None

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        self._Unit = params.get("Unit")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorMetricSeriesData(AbstractModel):
    """Monitoring metric value in a unit of time interval

    """

    def __init__(self):
        r"""
        :param _Series: Monitoring metric.
        :type Series: list of MonitorMetric
        :param _Timestamp: Timestamp corresponding to monitoring metric.
        :type Timestamp: list of int
        """
        self._Series = None
        self._Timestamp = None

    @property
    def Series(self):
        return self._Series

    @Series.setter
    def Series(self, Series):
        self._Series = Series

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        if params.get("Series") is not None:
            self._Series = []
            for item in params.get("Series"):
                obj = MonitorMetric()
                obj._deserialize(item)
                self._Series.append(obj)
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MySqlProcess(AbstractModel):
    """Relational database thread

    """

    def __init__(self):
        r"""
        :param _ID: Thread ID.
        :type ID: str
        :param _User: Thread operation account name.
        :type User: str
        :param _Host: Thread operation host address.
        :type Host: str
        :param _DB: Thread operation database.
        :type DB: str
        :param _State: Thread operation status.
        :type State: str
        :param _Command: Thread execution type.
        :type Command: str
        :param _Time: Thread operation duration in seconds.
        :type Time: str
        :param _Info: Thread operation statement.
        :type Info: str
        """
        self._ID = None
        self._User = None
        self._Host = None
        self._DB = None
        self._State = None
        self._Command = None
        self._Time = None
        self._Info = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def DB(self):
        return self._DB

    @DB.setter
    def DB(self, DB):
        self._DB = DB

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._User = params.get("User")
        self._Host = params.get("Host")
        self._DB = params.get("DB")
        self._State = params.get("State")
        self._Command = params.get("Command")
        self._Time = params.get("Time")
        self._Info = params.get("Info")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessStatistic(AbstractModel):
    """Real-time session statistics.

    """

    def __init__(self):
        r"""
        :param _Items: Array of session details
        :type Items: list of SessionItem
        :param _AllConnSum: The total number of connections
        :type AllConnSum: int
        :param _ActiveConnSum: The total number of active connections
        :type ActiveConnSum: int
        """
        self._Items = None
        self._AllConnSum = None
        self._ActiveConnSum = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def AllConnSum(self):
        return self._AllConnSum

    @AllConnSum.setter
    def AllConnSum(self, AllConnSum):
        self._AllConnSum = AllConnSum

    @property
    def ActiveConnSum(self):
        return self._ActiveConnSum

    @ActiveConnSum.setter
    def ActiveConnSum(self, ActiveConnSum):
        self._ActiveConnSum = ActiveConnSum


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SessionItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._AllConnSum = params.get("AllConnSum")
        self._ActiveConnSum = params.get("ActiveConnSum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProfileInfo(AbstractModel):
    """Information configured by the user.

    """

    def __init__(self):
        r"""
        :param _Language: Email language, such as `en`.
        :type Language: str
        :param _MailConfiguration: Email template content.
        :type MailConfiguration: :class:`tencentcloud.dbbrain.v20210527.models.MailConfiguration`
        """
        self._Language = None
        self._MailConfiguration = None

    @property
    def Language(self):
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def MailConfiguration(self):
        return self._MailConfiguration

    @MailConfiguration.setter
    def MailConfiguration(self, MailConfiguration):
        self._MailConfiguration = MailConfiguration


    def _deserialize(self, params):
        self._Language = params.get("Language")
        if params.get("MailConfiguration") is not None:
            self._MailConfiguration = MailConfiguration()
            self._MailConfiguration._deserialize(params.get("MailConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisPreKeySpaceData(AbstractModel):
    """Space information of Redis key prefixes

    """

    def __init__(self):
        r"""
        :param _AveElementSize: Average element length
        :type AveElementSize: int
        :param _Length: Total memory usage in bytes
        :type Length: int
        :param _KeyPreIndex: Key prefix
        :type KeyPreIndex: str
        :param _ItemCount: The number of elements
        :type ItemCount: int
        :param _Count: The number of keys
        :type Count: int
        :param _MaxElementSize: The max element length
        :type MaxElementSize: int
        """
        self._AveElementSize = None
        self._Length = None
        self._KeyPreIndex = None
        self._ItemCount = None
        self._Count = None
        self._MaxElementSize = None

    @property
    def AveElementSize(self):
        return self._AveElementSize

    @AveElementSize.setter
    def AveElementSize(self, AveElementSize):
        self._AveElementSize = AveElementSize

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def KeyPreIndex(self):
        return self._KeyPreIndex

    @KeyPreIndex.setter
    def KeyPreIndex(self, KeyPreIndex):
        self._KeyPreIndex = KeyPreIndex

    @property
    def ItemCount(self):
        return self._ItemCount

    @ItemCount.setter
    def ItemCount(self, ItemCount):
        self._ItemCount = ItemCount

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def MaxElementSize(self):
        return self._MaxElementSize

    @MaxElementSize.setter
    def MaxElementSize(self, MaxElementSize):
        self._MaxElementSize = MaxElementSize


    def _deserialize(self, params):
        self._AveElementSize = params.get("AveElementSize")
        self._Length = params.get("Length")
        self._KeyPreIndex = params.get("KeyPreIndex")
        self._ItemCount = params.get("ItemCount")
        self._Count = params.get("Count")
        self._MaxElementSize = params.get("MaxElementSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaItem(AbstractModel):
    """`SchemaItem` array

    """

    def __init__(self):
        r"""
        :param _Schema: Database name
        :type Schema: str
        """
        self._Schema = None

    @property
    def Schema(self):
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema


    def _deserialize(self, params):
        self._Schema = params.get("Schema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaSpaceData(AbstractModel):
    """Database space statistics.

    """

    def __init__(self):
        r"""
        :param _TableSchema: Database name.
        :type TableSchema: str
        :param _DataLength: Data space in MB.
        :type DataLength: float
        :param _IndexLength: Index space in MB.
        :type IndexLength: float
        :param _DataFree: Fragmented space in MB.
        :type DataFree: float
        :param _TotalLength: Total space usage in MB.
        :type TotalLength: float
        :param _FragRatio: Fragmentation rate in %.
        :type FragRatio: float
        :param _TableRows: Number of rows.
        :type TableRows: int
        :param _PhysicalFileSize: Total size in MB of physical files exclusive to all tables in the database.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PhysicalFileSize: float
        """
        self._TableSchema = None
        self._DataLength = None
        self._IndexLength = None
        self._DataFree = None
        self._TotalLength = None
        self._FragRatio = None
        self._TableRows = None
        self._PhysicalFileSize = None

    @property
    def TableSchema(self):
        return self._TableSchema

    @TableSchema.setter
    def TableSchema(self, TableSchema):
        self._TableSchema = TableSchema

    @property
    def DataLength(self):
        return self._DataLength

    @DataLength.setter
    def DataLength(self, DataLength):
        self._DataLength = DataLength

    @property
    def IndexLength(self):
        return self._IndexLength

    @IndexLength.setter
    def IndexLength(self, IndexLength):
        self._IndexLength = IndexLength

    @property
    def DataFree(self):
        return self._DataFree

    @DataFree.setter
    def DataFree(self, DataFree):
        self._DataFree = DataFree

    @property
    def TotalLength(self):
        return self._TotalLength

    @TotalLength.setter
    def TotalLength(self, TotalLength):
        self._TotalLength = TotalLength

    @property
    def FragRatio(self):
        return self._FragRatio

    @FragRatio.setter
    def FragRatio(self, FragRatio):
        self._FragRatio = FragRatio

    @property
    def TableRows(self):
        return self._TableRows

    @TableRows.setter
    def TableRows(self, TableRows):
        self._TableRows = TableRows

    @property
    def PhysicalFileSize(self):
        return self._PhysicalFileSize

    @PhysicalFileSize.setter
    def PhysicalFileSize(self, PhysicalFileSize):
        self._PhysicalFileSize = PhysicalFileSize


    def _deserialize(self, params):
        self._TableSchema = params.get("TableSchema")
        self._DataLength = params.get("DataLength")
        self._IndexLength = params.get("IndexLength")
        self._DataFree = params.get("DataFree")
        self._TotalLength = params.get("TotalLength")
        self._FragRatio = params.get("FragRatio")
        self._TableRows = params.get("TableRows")
        self._PhysicalFileSize = params.get("PhysicalFileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaSpaceTimeSeries(AbstractModel):
    """Time series of database space data

    """

    def __init__(self):
        r"""
        :param _TableSchema: Database name
        :type TableSchema: str
        :param _SeriesData: Space metric value in a unit of time interval
        :type SeriesData: :class:`tencentcloud.dbbrain.v20210527.models.MonitorMetricSeriesData`
        """
        self._TableSchema = None
        self._SeriesData = None

    @property
    def TableSchema(self):
        return self._TableSchema

    @TableSchema.setter
    def TableSchema(self, TableSchema):
        self._TableSchema = TableSchema

    @property
    def SeriesData(self):
        return self._SeriesData

    @SeriesData.setter
    def SeriesData(self, SeriesData):
        self._SeriesData = SeriesData


    def _deserialize(self, params):
        self._TableSchema = params.get("TableSchema")
        if params.get("SeriesData") is not None:
            self._SeriesData = MonitorMetricSeriesData()
            self._SeriesData._deserialize(params.get("SeriesData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreDetail(AbstractModel):
    """Deduction details.

    """

    def __init__(self):
        r"""
        :param _IssueType: Deduction item type. Valid values: `Availability`, `Maintainability`, `Performance`, `Reliability`.
        :type IssueType: str
        :param _ScoreLost: Total deducted scores.
        :type ScoreLost: int
        :param _ScoreLostMax: Upper limit of the deducted scores.
        :type ScoreLostMax: int
        :param _Items: List of deduction items.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of ScoreItem
        """
        self._IssueType = None
        self._ScoreLost = None
        self._ScoreLostMax = None
        self._Items = None

    @property
    def IssueType(self):
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def ScoreLost(self):
        return self._ScoreLost

    @ScoreLost.setter
    def ScoreLost(self, ScoreLost):
        self._ScoreLost = ScoreLost

    @property
    def ScoreLostMax(self):
        return self._ScoreLostMax

    @ScoreLostMax.setter
    def ScoreLostMax(self, ScoreLostMax):
        self._ScoreLostMax = ScoreLostMax

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._IssueType = params.get("IssueType")
        self._ScoreLost = params.get("ScoreLost")
        self._ScoreLostMax = params.get("ScoreLostMax")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ScoreItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreItem(AbstractModel):
    """Diagnosis deduction item.

    """

    def __init__(self):
        r"""
        :param _DiagItem: Exception diagnosis item name.
        :type DiagItem: str
        :param _IssueType: Diagnosis item type. Valid values: `Availability`, `Maintainability`, `Performance`, `Reliability`.
        :type IssueType: str
        :param _TopSeverity: Health level. Valid values: `Healthy`, `Reminder`, `Alarm`, `Severe`, `Critical`.
        :type TopSeverity: str
        :param _Count: Number of occurrences of this exception diagnosis item.
        :type Count: int
        :param _ScoreLost: Deducted scores.
        :type ScoreLost: int
        """
        self._DiagItem = None
        self._IssueType = None
        self._TopSeverity = None
        self._Count = None
        self._ScoreLost = None

    @property
    def DiagItem(self):
        return self._DiagItem

    @DiagItem.setter
    def DiagItem(self, DiagItem):
        self._DiagItem = DiagItem

    @property
    def IssueType(self):
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def TopSeverity(self):
        return self._TopSeverity

    @TopSeverity.setter
    def TopSeverity(self, TopSeverity):
        self._TopSeverity = TopSeverity

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ScoreLost(self):
        return self._ScoreLost

    @ScoreLost.setter
    def ScoreLost(self, ScoreLost):
        self._ScoreLost = ScoreLost


    def _deserialize(self, params):
        self._DiagItem = params.get("DiagItem")
        self._IssueType = params.get("IssueType")
        self._TopSeverity = params.get("TopSeverity")
        self._Count = params.get("Count")
        self._ScoreLost = params.get("ScoreLost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecLogExportTaskInfo(AbstractModel):
    """Security audit log export task information.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task Id.
        :type AsyncRequestId: int
        :param _StartTime: Task start time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _EndTime: Task end time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _CreateTime: Task creation time.
        :type CreateTime: str
        :param _Status: Task status.
        :type Status: str
        :param _Progress: Task progress.
        :type Progress: int
        :param _LogStartTime: Exported log start time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogStartTime: str
        :param _LogEndTime: Exported log end time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogEndTime: str
        :param _TotalSize: Total size of log files in KB.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        :param _DangerLevels: List of risk levels. Valid values: `0` (no risk), `1` (low risk), `2` (medium risk), `3` (high risk).
Note: This field may return null, indicating that no valid values can be obtained.
        :type DangerLevels: list of int non-negative
        """
        self._AsyncRequestId = None
        self._StartTime = None
        self._EndTime = None
        self._CreateTime = None
        self._Status = None
        self._Progress = None
        self._LogStartTime = None
        self._LogEndTime = None
        self._TotalSize = None
        self._DangerLevels = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def LogStartTime(self):
        return self._LogStartTime

    @LogStartTime.setter
    def LogStartTime(self, LogStartTime):
        self._LogStartTime = LogStartTime

    @property
    def LogEndTime(self):
        return self._LogEndTime

    @LogEndTime.setter
    def LogEndTime(self, LogEndTime):
        self._LogEndTime = LogEndTime

    @property
    def TotalSize(self):
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def DangerLevels(self):
        return self._DangerLevels

    @DangerLevels.setter
    def DangerLevels(self, DangerLevels):
        self._DangerLevels = DangerLevels


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._LogStartTime = params.get("LogStartTime")
        self._LogEndTime = params.get("LogEndTime")
        self._TotalSize = params.get("TotalSize")
        self._DangerLevels = params.get("DangerLevels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionItem(AbstractModel):
    """Access source details of the real-time session

    """

    def __init__(self):
        r"""
        :param _Ip: Access source
        :type Ip: str
        :param _ActiveConn: The number of active connections from the current access source
        :type ActiveConn: str
        :param _AllConn: The total number of connections from the current access source
        :type AllConn: int
        """
        self._Ip = None
        self._ActiveConn = None
        self._AllConn = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def ActiveConn(self):
        return self._ActiveConn

    @ActiveConn.setter
    def ActiveConn(self, ActiveConn):
        self._ActiveConn = ActiveConn

    @property
    def AllConn(self):
        return self._AllConn

    @AllConn.setter
    def AllConn(self, AllConn):
        self._AllConn = AllConn


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._ActiveConn = params.get("ActiveConn")
        self._AllConn = params.get("AllConn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogHost(AbstractModel):
    """Details of slow log source addresses.

    """

    def __init__(self):
        r"""
        :param _UserHost: Source addresses.
        :type UserHost: str
        :param _Ratio: Proportion (in %) of slow logs from this source address to the total number of slow logs.
        :type Ratio: float
        :param _Count: Number of slow logs from this source address.
        :type Count: int
        """
        self._UserHost = None
        self._Ratio = None
        self._Count = None

    @property
    def UserHost(self):
        return self._UserHost

    @UserHost.setter
    def UserHost(self, UserHost):
        self._UserHost = UserHost

    @property
    def Ratio(self):
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._UserHost = params.get("UserHost")
        self._Ratio = params.get("Ratio")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogInfoItem(AbstractModel):
    """Slow log details

    """

    def __init__(self):
        r"""
        :param _Timestamp: Slow log start time
        :type Timestamp: str
        :param _SqlText: SQL statement
        :type SqlText: str
        :param _Database: Database
        :type Database: str
        :param _UserName: User source
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _UserHost: IP source
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserHost: str
        :param _QueryTime: Execution time in seconds
        :type QueryTime: int
        :param _LockTime: Lock time in seconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type LockTime: int
        :param _RowsExamined: Number of scanned rows
Note: This field may return null, indicating that no valid values can be obtained.
        :type RowsExamined: int
        :param _RowsSent: Number of returned rows
Note: This field may return null, indicating that no valid values can be obtained.
        :type RowsSent: int
        """
        self._Timestamp = None
        self._SqlText = None
        self._Database = None
        self._UserName = None
        self._UserHost = None
        self._QueryTime = None
        self._LockTime = None
        self._RowsExamined = None
        self._RowsSent = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def SqlText(self):
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserHost(self):
        return self._UserHost

    @UserHost.setter
    def UserHost(self, UserHost):
        self._UserHost = UserHost

    @property
    def QueryTime(self):
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def LockTime(self):
        return self._LockTime

    @LockTime.setter
    def LockTime(self, LockTime):
        self._LockTime = LockTime

    @property
    def RowsExamined(self):
        return self._RowsExamined

    @RowsExamined.setter
    def RowsExamined(self, RowsExamined):
        self._RowsExamined = RowsExamined

    @property
    def RowsSent(self):
        return self._RowsSent

    @RowsSent.setter
    def RowsSent(self, RowsSent):
        self._RowsSent = RowsSent


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._SqlText = params.get("SqlText")
        self._Database = params.get("Database")
        self._UserName = params.get("UserName")
        self._UserHost = params.get("UserHost")
        self._QueryTime = params.get("QueryTime")
        self._LockTime = params.get("LockTime")
        self._RowsExamined = params.get("RowsExamined")
        self._RowsSent = params.get("RowsSent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogTopSqlItem(AbstractModel):
    """Top slow SQL statements

    """

    def __init__(self):
        r"""
        :param _LockTime: Total SQL lock wait time in seconds.
        :type LockTime: float
        :param _LockTimeMax: Maximum lock wait time in seconds
        :type LockTimeMax: float
        :param _LockTimeMin: Minimum lock wait time in seconds
        :type LockTimeMin: float
        :param _RowsExamined: Total number of scanned rows
        :type RowsExamined: int
        :param _RowsExaminedMax: Maximum number of scanned rows
        :type RowsExaminedMax: int
        :param _RowsExaminedMin: Minimum number of scanned rows
        :type RowsExaminedMin: int
        :param _QueryTime: Total duration in seconds
        :type QueryTime: float
        :param _QueryTimeMax: Maximum execution time in seconds
        :type QueryTimeMax: float
        :param _QueryTimeMin: Minimum execution time in seconds
        :type QueryTimeMin: float
        :param _RowsSent: Total number of returned rows
        :type RowsSent: int
        :param _RowsSentMax: Maximum number of returned rows
        :type RowsSentMax: int
        :param _RowsSentMin: Minimum number of returned rows
        :type RowsSentMin: int
        :param _ExecTimes: Number of executions
        :type ExecTimes: int
        :param _SqlTemplate: SQL template
        :type SqlTemplate: str
        :param _SqlText: SQL statements with parameter (random)
        :type SqlText: str
        :param _Schema: Database name
        :type Schema: str
        :param _QueryTimeRatio: Ratio of the total duration in %
        :type QueryTimeRatio: float
        :param _LockTimeRatio: Ratio of the total SQL lock wait time in %
        :type LockTimeRatio: float
        :param _RowsExaminedRatio: Ratio of total number of scanned rows in %
        :type RowsExaminedRatio: float
        :param _RowsSentRatio: Ratio of total number of returned rows in %
        :type RowsSentRatio: float
        :param _QueryTimeAvg: Average execution time in seconds
        :type QueryTimeAvg: float
        :param _RowsSentAvg: Average number of returned rows
        :type RowsSentAvg: float
        :param _LockTimeAvg: Average lock wait time in seconds
        :type LockTimeAvg: float
        :param _RowsExaminedAvg: Average number of scanned rows
        :type RowsExaminedAvg: float
        :param _Md5: MD5 value of the SQL template
        :type Md5: str
        """
        self._LockTime = None
        self._LockTimeMax = None
        self._LockTimeMin = None
        self._RowsExamined = None
        self._RowsExaminedMax = None
        self._RowsExaminedMin = None
        self._QueryTime = None
        self._QueryTimeMax = None
        self._QueryTimeMin = None
        self._RowsSent = None
        self._RowsSentMax = None
        self._RowsSentMin = None
        self._ExecTimes = None
        self._SqlTemplate = None
        self._SqlText = None
        self._Schema = None
        self._QueryTimeRatio = None
        self._LockTimeRatio = None
        self._RowsExaminedRatio = None
        self._RowsSentRatio = None
        self._QueryTimeAvg = None
        self._RowsSentAvg = None
        self._LockTimeAvg = None
        self._RowsExaminedAvg = None
        self._Md5 = None

    @property
    def LockTime(self):
        return self._LockTime

    @LockTime.setter
    def LockTime(self, LockTime):
        self._LockTime = LockTime

    @property
    def LockTimeMax(self):
        return self._LockTimeMax

    @LockTimeMax.setter
    def LockTimeMax(self, LockTimeMax):
        self._LockTimeMax = LockTimeMax

    @property
    def LockTimeMin(self):
        return self._LockTimeMin

    @LockTimeMin.setter
    def LockTimeMin(self, LockTimeMin):
        self._LockTimeMin = LockTimeMin

    @property
    def RowsExamined(self):
        return self._RowsExamined

    @RowsExamined.setter
    def RowsExamined(self, RowsExamined):
        self._RowsExamined = RowsExamined

    @property
    def RowsExaminedMax(self):
        return self._RowsExaminedMax

    @RowsExaminedMax.setter
    def RowsExaminedMax(self, RowsExaminedMax):
        self._RowsExaminedMax = RowsExaminedMax

    @property
    def RowsExaminedMin(self):
        return self._RowsExaminedMin

    @RowsExaminedMin.setter
    def RowsExaminedMin(self, RowsExaminedMin):
        self._RowsExaminedMin = RowsExaminedMin

    @property
    def QueryTime(self):
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def QueryTimeMax(self):
        return self._QueryTimeMax

    @QueryTimeMax.setter
    def QueryTimeMax(self, QueryTimeMax):
        self._QueryTimeMax = QueryTimeMax

    @property
    def QueryTimeMin(self):
        return self._QueryTimeMin

    @QueryTimeMin.setter
    def QueryTimeMin(self, QueryTimeMin):
        self._QueryTimeMin = QueryTimeMin

    @property
    def RowsSent(self):
        return self._RowsSent

    @RowsSent.setter
    def RowsSent(self, RowsSent):
        self._RowsSent = RowsSent

    @property
    def RowsSentMax(self):
        return self._RowsSentMax

    @RowsSentMax.setter
    def RowsSentMax(self, RowsSentMax):
        self._RowsSentMax = RowsSentMax

    @property
    def RowsSentMin(self):
        return self._RowsSentMin

    @RowsSentMin.setter
    def RowsSentMin(self, RowsSentMin):
        self._RowsSentMin = RowsSentMin

    @property
    def ExecTimes(self):
        return self._ExecTimes

    @ExecTimes.setter
    def ExecTimes(self, ExecTimes):
        self._ExecTimes = ExecTimes

    @property
    def SqlTemplate(self):
        return self._SqlTemplate

    @SqlTemplate.setter
    def SqlTemplate(self, SqlTemplate):
        self._SqlTemplate = SqlTemplate

    @property
    def SqlText(self):
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def Schema(self):
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def QueryTimeRatio(self):
        return self._QueryTimeRatio

    @QueryTimeRatio.setter
    def QueryTimeRatio(self, QueryTimeRatio):
        self._QueryTimeRatio = QueryTimeRatio

    @property
    def LockTimeRatio(self):
        return self._LockTimeRatio

    @LockTimeRatio.setter
    def LockTimeRatio(self, LockTimeRatio):
        self._LockTimeRatio = LockTimeRatio

    @property
    def RowsExaminedRatio(self):
        return self._RowsExaminedRatio

    @RowsExaminedRatio.setter
    def RowsExaminedRatio(self, RowsExaminedRatio):
        self._RowsExaminedRatio = RowsExaminedRatio

    @property
    def RowsSentRatio(self):
        return self._RowsSentRatio

    @RowsSentRatio.setter
    def RowsSentRatio(self, RowsSentRatio):
        self._RowsSentRatio = RowsSentRatio

    @property
    def QueryTimeAvg(self):
        return self._QueryTimeAvg

    @QueryTimeAvg.setter
    def QueryTimeAvg(self, QueryTimeAvg):
        self._QueryTimeAvg = QueryTimeAvg

    @property
    def RowsSentAvg(self):
        return self._RowsSentAvg

    @RowsSentAvg.setter
    def RowsSentAvg(self, RowsSentAvg):
        self._RowsSentAvg = RowsSentAvg

    @property
    def LockTimeAvg(self):
        return self._LockTimeAvg

    @LockTimeAvg.setter
    def LockTimeAvg(self, LockTimeAvg):
        self._LockTimeAvg = LockTimeAvg

    @property
    def RowsExaminedAvg(self):
        return self._RowsExaminedAvg

    @RowsExaminedAvg.setter
    def RowsExaminedAvg(self, RowsExaminedAvg):
        self._RowsExaminedAvg = RowsExaminedAvg

    @property
    def Md5(self):
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5


    def _deserialize(self, params):
        self._LockTime = params.get("LockTime")
        self._LockTimeMax = params.get("LockTimeMax")
        self._LockTimeMin = params.get("LockTimeMin")
        self._RowsExamined = params.get("RowsExamined")
        self._RowsExaminedMax = params.get("RowsExaminedMax")
        self._RowsExaminedMin = params.get("RowsExaminedMin")
        self._QueryTime = params.get("QueryTime")
        self._QueryTimeMax = params.get("QueryTimeMax")
        self._QueryTimeMin = params.get("QueryTimeMin")
        self._RowsSent = params.get("RowsSent")
        self._RowsSentMax = params.get("RowsSentMax")
        self._RowsSentMin = params.get("RowsSentMin")
        self._ExecTimes = params.get("ExecTimes")
        self._SqlTemplate = params.get("SqlTemplate")
        self._SqlText = params.get("SqlText")
        self._Schema = params.get("Schema")
        self._QueryTimeRatio = params.get("QueryTimeRatio")
        self._LockTimeRatio = params.get("LockTimeRatio")
        self._RowsExaminedRatio = params.get("RowsExaminedRatio")
        self._RowsSentRatio = params.get("RowsSentRatio")
        self._QueryTimeAvg = params.get("QueryTimeAvg")
        self._RowsSentAvg = params.get("RowsSentAvg")
        self._LockTimeAvg = params.get("LockTimeAvg")
        self._RowsExaminedAvg = params.get("RowsExaminedAvg")
        self._Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogUser(AbstractModel):
    """Details of the source users of slow logs

    """

    def __init__(self):
        r"""
        :param _UserName: Source username
        :type UserName: str
        :param _Ratio: Percentage of the number of slow logs from this source username to the total number of slow logs
        :type Ratio: float
        :param _Count: Number of slow logs from this source username
        :type Count: int
        """
        self._UserName = None
        self._Ratio = None
        self._Count = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Ratio(self):
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Ratio = params.get("Ratio")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableSpaceData(AbstractModel):
    """Database tablespace statistics.

    """

    def __init__(self):
        r"""
        :param _TableName: Table name.
        :type TableName: str
        :param _TableSchema: Database name.
        :type TableSchema: str
        :param _Engine: Database table storage engine.
        :type Engine: str
        :param _DataLength: Data space in MB.
        :type DataLength: float
        :param _IndexLength: Index space in MB.
        :type IndexLength: float
        :param _DataFree: Fragmented space in MB.
        :type DataFree: float
        :param _TotalLength: Total space usage in MB.
        :type TotalLength: float
        :param _FragRatio: Fragmentation rate in %.
        :type FragRatio: float
        :param _TableRows: Number of rows.
        :type TableRows: int
        :param _PhysicalFileSize: Size in MB of the physical file exclusive to a table.
        :type PhysicalFileSize: float
        """
        self._TableName = None
        self._TableSchema = None
        self._Engine = None
        self._DataLength = None
        self._IndexLength = None
        self._DataFree = None
        self._TotalLength = None
        self._FragRatio = None
        self._TableRows = None
        self._PhysicalFileSize = None

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableSchema(self):
        return self._TableSchema

    @TableSchema.setter
    def TableSchema(self, TableSchema):
        self._TableSchema = TableSchema

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def DataLength(self):
        return self._DataLength

    @DataLength.setter
    def DataLength(self, DataLength):
        self._DataLength = DataLength

    @property
    def IndexLength(self):
        return self._IndexLength

    @IndexLength.setter
    def IndexLength(self, IndexLength):
        self._IndexLength = IndexLength

    @property
    def DataFree(self):
        return self._DataFree

    @DataFree.setter
    def DataFree(self, DataFree):
        self._DataFree = DataFree

    @property
    def TotalLength(self):
        return self._TotalLength

    @TotalLength.setter
    def TotalLength(self, TotalLength):
        self._TotalLength = TotalLength

    @property
    def FragRatio(self):
        return self._FragRatio

    @FragRatio.setter
    def FragRatio(self, FragRatio):
        self._FragRatio = FragRatio

    @property
    def TableRows(self):
        return self._TableRows

    @TableRows.setter
    def TableRows(self, TableRows):
        self._TableRows = TableRows

    @property
    def PhysicalFileSize(self):
        return self._PhysicalFileSize

    @PhysicalFileSize.setter
    def PhysicalFileSize(self, PhysicalFileSize):
        self._PhysicalFileSize = PhysicalFileSize


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._TableSchema = params.get("TableSchema")
        self._Engine = params.get("Engine")
        self._DataLength = params.get("DataLength")
        self._IndexLength = params.get("IndexLength")
        self._DataFree = params.get("DataFree")
        self._TotalLength = params.get("TotalLength")
        self._FragRatio = params.get("FragRatio")
        self._TableRows = params.get("TableRows")
        self._PhysicalFileSize = params.get("PhysicalFileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableSpaceTimeSeries(AbstractModel):
    """Time series of database tablespace data

    """

    def __init__(self):
        r"""
        :param _TableName: Table name.
        :type TableName: str
        :param _TableSchema: Database name.
        :type TableSchema: str
        :param _Engine: Database table storage engine.
        :type Engine: str
        :param _SeriesData: Space metric value in a unit of time interval
        :type SeriesData: :class:`tencentcloud.dbbrain.v20210527.models.MonitorFloatMetricSeriesData`
        """
        self._TableName = None
        self._TableSchema = None
        self._Engine = None
        self._SeriesData = None

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableSchema(self):
        return self._TableSchema

    @TableSchema.setter
    def TableSchema(self, TableSchema):
        self._TableSchema = TableSchema

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def SeriesData(self):
        return self._SeriesData

    @SeriesData.setter
    def SeriesData(self, SeriesData):
        self._SeriesData = SeriesData


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._TableSchema = params.get("TableSchema")
        self._Engine = params.get("Engine")
        if params.get("SeriesData") is not None:
            self._SeriesData = MonitorFloatMetricSeriesData()
            self._SeriesData._deserialize(params.get("SeriesData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInfo(AbstractModel):
    """Information about Redis session killing task status

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task ID.
        :type AsyncRequestId: int
        :param _InstProxyList: List of all proxies of the current instance.
        :type InstProxyList: list of str
        :param _InstProxyCount: Total number of proxies of the current instance.
        :type InstProxyCount: int
        :param _CreateTime: Task creation time.
        :type CreateTime: str
        :param _StartTime: Task start time.
        :type StartTime: str
        :param _TaskStatus: Task status. Valid values: `created` (create), `chosen` (to be executed), `running` (being executed), `failed` (failed), and `finished` (completed).
        :type TaskStatus: str
        :param _FinishedProxyList: IDs of the proxies that have completed the session killing tasks.
        :type FinishedProxyList: list of str
        :param _FailedProxyList: IDs of the proxies that failed to execute the session killing tasks.
        :type FailedProxyList: list of str
        :param _EndTime: Task end time.
        :type EndTime: str
        :param _Progress: Task progress.
        :type Progress: int
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        """
        self._AsyncRequestId = None
        self._InstProxyList = None
        self._InstProxyCount = None
        self._CreateTime = None
        self._StartTime = None
        self._TaskStatus = None
        self._FinishedProxyList = None
        self._FailedProxyList = None
        self._EndTime = None
        self._Progress = None
        self._InstanceId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def InstProxyList(self):
        return self._InstProxyList

    @InstProxyList.setter
    def InstProxyList(self, InstProxyList):
        self._InstProxyList = InstProxyList

    @property
    def InstProxyCount(self):
        return self._InstProxyCount

    @InstProxyCount.setter
    def InstProxyCount(self, InstProxyCount):
        self._InstProxyCount = InstProxyCount

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def FinishedProxyList(self):
        return self._FinishedProxyList

    @FinishedProxyList.setter
    def FinishedProxyList(self, FinishedProxyList):
        self._FinishedProxyList = FinishedProxyList

    @property
    def FailedProxyList(self):
        return self._FailedProxyList

    @FailedProxyList.setter
    def FailedProxyList(self, FailedProxyList):
        self._FailedProxyList = FailedProxyList

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._InstProxyList = params.get("InstProxyList")
        self._InstProxyCount = params.get("InstProxyCount")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._TaskStatus = params.get("TaskStatus")
        self._FinishedProxyList = params.get("FinishedProxyList")
        self._FailedProxyList = params.get("FailedProxyList")
        self._EndTime = params.get("EndTime")
        self._Progress = params.get("Progress")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeSlice(AbstractModel):
    """Slow log statistics in the specified time range

    """

    def __init__(self):
        r"""
        :param _Count: Total number
        :type Count: int
        :param _Timestamp: Statistics start time
        :type Timestamp: int
        """
        self._Count = None
        self._Timestamp = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserProfile(AbstractModel):
    """Information configured by user, including email configuration.

    """

    def __init__(self):
        r"""
        :param _ProfileId: Configured ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProfileId: str
        :param _ProfileType: Configuration type. Valid values: `dbScan_mail_configuration` (email configuration of the database inspection report), `scheduler_mail_configuration` (email configuration of the scheduled task report).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProfileType: str
        :param _ProfileLevel: Configuration level. Valid values: `User` (user-level), `Instance` (instance-level). For database inspection emails, it should be `User`. For scheduled task emails, it should be `Instance`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProfileLevel: str
        :param _ProfileName: Configuration name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProfileName: str
        :param _ProfileInfo: Configuration details.
        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20210527.models.ProfileInfo`
        """
        self._ProfileId = None
        self._ProfileType = None
        self._ProfileLevel = None
        self._ProfileName = None
        self._ProfileInfo = None

    @property
    def ProfileId(self):
        return self._ProfileId

    @ProfileId.setter
    def ProfileId(self, ProfileId):
        self._ProfileId = ProfileId

    @property
    def ProfileType(self):
        return self._ProfileType

    @ProfileType.setter
    def ProfileType(self, ProfileType):
        self._ProfileType = ProfileType

    @property
    def ProfileLevel(self):
        return self._ProfileLevel

    @ProfileLevel.setter
    def ProfileLevel(self, ProfileLevel):
        self._ProfileLevel = ProfileLevel

    @property
    def ProfileName(self):
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, ProfileName):
        self._ProfileName = ProfileName

    @property
    def ProfileInfo(self):
        return self._ProfileInfo

    @ProfileInfo.setter
    def ProfileInfo(self, ProfileInfo):
        self._ProfileInfo = ProfileInfo


    def _deserialize(self, params):
        self._ProfileId = params.get("ProfileId")
        self._ProfileType = params.get("ProfileType")
        self._ProfileLevel = params.get("ProfileLevel")
        self._ProfileName = params.get("ProfileName")
        if params.get("ProfileInfo") is not None:
            self._ProfileInfo = ProfileInfo()
            self._ProfileInfo._deserialize(params.get("ProfileInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        