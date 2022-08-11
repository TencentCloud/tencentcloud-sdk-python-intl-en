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


class CreateApiImportUserJobRequest(AbstractModel):
    """CreateApiImportUserJob request structure.

    """

    def __init__(self):
        r"""
        :param UserStoreId: User directory ID
        :type UserStoreId: str
        :param DataFlowUserCreateList: Imported user data
        :type DataFlowUserCreateList: list of ImportUser
        """
        self.UserStoreId = None
        self.DataFlowUserCreateList = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        if params.get("DataFlowUserCreateList") is not None:
            self.DataFlowUserCreateList = []
            for item in params.get("DataFlowUserCreateList"):
                obj = ImportUser()
                obj._deserialize(item)
                self.DataFlowUserCreateList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiImportUserJobResponse(AbstractModel):
    """CreateApiImportUserJob response structure.

    """

    def __init__(self):
        r"""
        :param Job: Data flow task
        :type Job: :class:`tencentcloud.ciam.v20220331.models.Job`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Job = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        self.RequestId = params.get("RequestId")


class CreateFileExportUserJobRequest(AbstractModel):
    """CreateFileExportUserJob request structure.

    """

    def __init__(self):
        r"""
        :param UserStoreId: User directory ID
        :type UserStoreId: str
        :param Format: Exported data type

<li> **JSON** </li>  JSON
<li> **NDJSON** </li>  New-line Delimited JSON
<li> **CSV** </li>  Comma-Separated Values
        :type Format: str
        :param Filters: Valid values of `Key`: `condition`, `userGroupId`.

<li> **condition** </li>	Values = Query condition, which can be user ID, username, mobile number, or email address.
<li> **userGroupId** </li>	Values = User group ID
        :type Filters: list of Filter
        :param ExportPropertyMaps: Attributes and mapping names included in the exported user information. If this parameter is empty, all attributes will be included.
        :type ExportPropertyMaps: list of ExportPropertyMap
        """
        self.UserStoreId = None
        self.Format = None
        self.Filters = None
        self.ExportPropertyMaps = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        self.Format = params.get("Format")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("ExportPropertyMaps") is not None:
            self.ExportPropertyMaps = []
            for item in params.get("ExportPropertyMaps"):
                obj = ExportPropertyMap()
                obj._deserialize(item)
                self.ExportPropertyMaps.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFileExportUserJobResponse(AbstractModel):
    """CreateFileExportUserJob response structure.

    """

    def __init__(self):
        r"""
        :param Job: Data flow task
        :type Job: :class:`tencentcloud.ciam.v20220331.models.Job`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Job = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        self.RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser request structure.

    """

    def __init__(self):
        r"""
        :param UserStoreId: User directory ID
        :type UserStoreId: str
        :param PhoneNumber: Mobile number
        :type PhoneNumber: str
        :param Email: Email address
        :type Email: str
        :param Password: Password
        :type Password: str
        :param UserName: Username
        :type UserName: str
        :param Nickname: Nickname
        :type Nickname: str
        :param Address: Address
        :type Address: str
        :param UserGroup: User group ID
        :type UserGroup: list of str
        :param Birthdate: Date of birth
        :type Birthdate: int
        :param CustomizationAttributes: Custom attribute
        :type CustomizationAttributes: list of MemberMap
        """
        self.UserStoreId = None
        self.PhoneNumber = None
        self.Email = None
        self.Password = None
        self.UserName = None
        self.Nickname = None
        self.Address = None
        self.UserGroup = None
        self.Birthdate = None
        self.CustomizationAttributes = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Email = params.get("Email")
        self.Password = params.get("Password")
        self.UserName = params.get("UserName")
        self.Nickname = params.get("Nickname")
        self.Address = params.get("Address")
        self.UserGroup = params.get("UserGroup")
        self.Birthdate = params.get("Birthdate")
        if params.get("CustomizationAttributes") is not None:
            self.CustomizationAttributes = []
            for item in params.get("CustomizationAttributes"):
                obj = MemberMap()
                obj._deserialize(item)
                self.CustomizationAttributes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    """CreateUser response structure.

    """

    def __init__(self):
        r"""
        :param User: Information of the created user
Note: This field may return null, indicating that no valid values can be obtained.
        :type User: :class:`tencentcloud.ciam.v20220331.models.User`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.User = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("User") is not None:
            self.User = User()
            self.User._deserialize(params.get("User"))
        self.RequestId = params.get("RequestId")


class DeleteUsersRequest(AbstractModel):
    """DeleteUsers request structure.

    """

    def __init__(self):
        r"""
        :param UserStoreId: User directory ID
        :type UserStoreId: str
        :param UserIds: Array of user IDs
        :type UserIds: list of str
        """
        self.UserStoreId = None
        self.UserIds = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        self.UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsersResponse(AbstractModel):
    """DeleteUsers response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeUserByIdRequest(AbstractModel):
    """DescribeUserById request structure.

    """

    def __init__(self):
        r"""
        :param UserStoreId: User directory ID
        :type UserStoreId: str
        :param UserId: User ID
        :type UserId: str
        :param Original: 
        :type Original: bool
        """
        self.UserStoreId = None
        self.UserId = None
        self.Original = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        self.UserId = params.get("UserId")
        self.Original = params.get("Original")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserByIdResponse(AbstractModel):
    """DescribeUserById response structure.

    """

    def __init__(self):
        r"""
        :param User: User information
Note: This field may return null, indicating that no valid values can be obtained.
        :type User: :class:`tencentcloud.ciam.v20220331.models.User`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.User = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("User") is not None:
            self.User = User()
            self.User._deserialize(params.get("User"))
        self.RequestId = params.get("RequestId")


class ErrorDetails(AbstractModel):
    """Failure details

    """

    def __init__(self):
        r"""
        :param UserId: User information
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param Error: Failure cause
        :type Error: str
        """
        self.UserId = None
        self.Error = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportPropertyMap(AbstractModel):
    """Exported attribute mapping

    """

    def __init__(self):
        r"""
        :param UserPropertyCode: User attribute code
        :type UserPropertyCode: str
        :param ColumnName: User attribute mapping name
        :type ColumnName: str
        """
        self.UserPropertyCode = None
        self.ColumnName = None


    def _deserialize(self, params):
        self.UserPropertyCode = params.get("UserPropertyCode")
        self.ColumnName = params.get("ColumnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FailedUsers(AbstractModel):
    """Failed user

    """

    def __init__(self):
        r"""
        :param FailedUserIdentification: ID of the failed user
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailedUserIdentification: str
        :param FailedReason: Failure cause for user import
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailedReason: str
        """
        self.FailedUserIdentification = None
        self.FailedReason = None


    def _deserialize(self, params):
        self.FailedUserIdentification = params.get("FailedUserIdentification")
        self.FailedReason = params.get("FailedReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Query condition

    """

    def __init__(self):
        r"""
        :param Key: Key value
        :type Key: str
        :param Values: Value
        :type Values: list of str
        :param Logic: Logical value
        :type Logic: bool
        """
        self.Key = None
        self.Values = None
        self.Logic = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Values = params.get("Values")
        self.Logic = params.get("Logic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportUser(AbstractModel):
    """Imported user information
    1. One of the eight attributes of `UserName`, `PhoneNumber`, `Email`, `WechatOpenId`, `WechatUnionId`, `AlipayUserId`, `QqOpenId`, and `QqUnionId` must be included during import and comply with the regular expression rules for initializing custom attributes. The regular expressions for `UserName`, `PhoneNumber`, and `Email` can be queried in the custom attributes in the console.
    2. For password import, the imported password supports plaintext import, MD5 ciphertext import, SHA1 ciphertext import, and BCRYPT ciphertext import. This needs to be specified in the `PasswordEncryptTypeEnum` field.
    3. `IdentityVerified` and `IdentityVerificationMethod` can be imported.
    If `IdentityVerified` is `true`, `IdentityVerificationMethod` is required.
    If `IdentityVerificationMethod` is `nameAndIdCard`, `Name` and `ResidentIdentityCard` are required.
    If `IdentityVerificationMethod` is `nameIdCardAndPhone`, `Name`, `PhoneNumber`, and `ResidentIdentityCard` are required.

    """

    def __init__(self):
        r"""
        :param UserName: Username
        :type UserName: str
        :param PhoneNumber: Mobile number
        :type PhoneNumber: str
        :param Email: Email address
        :type Email: str
        :param ResidentIdentityCard: ID card number
        :type ResidentIdentityCard: str
        :param Nickname: Nickname
        :type Nickname: str
        :param Address: Address
        :type Address: str
        :param UserGroup: User group ID
        :type UserGroup: list of str
        :param QqOpenId: `qqOpenId` on QQ
        :type QqOpenId: str
        :param QqUnionId: `qqUnionId` on QQ
        :type QqUnionId: str
        :param WechatOpenId: `wechatOpenId` on WeChat
        :type WechatOpenId: str
        :param WechatUnionId: `wechatUnionId` on WeChat
        :type WechatUnionId: str
        :param AlipayUserId: `alipayUserId` on Alipay
        :type AlipayUserId: str
        :param Description: Description
        :type Description: str
        :param Birthdate: Date of birth
        :type Birthdate: str
        :param Name: Name
        :type Name: str
        :param Locale: Coordinate
        :type Locale: str
        :param Gender: Gender. Valid values: `MALE`, `FEMALE`, `UNKNOWN`.
        :type Gender: str
        :param IdentityVerificationMethod: Identity verification method
        :type IdentityVerificationMethod: str
        :param IdentityVerified: Whether the identity is verified
        :type IdentityVerified: bool
        :param Job: Job
        :type Job: str
        :param Nationality: Country/Region
        :type Nationality: str
        :param Zone: Time zone
        :type Zone: str
        :param Password: Password ciphertext
        :type Password: str
        :param CustomizationAttributes: Custom attribute
        :type CustomizationAttributes: list of MemberMap
        :param Salt: Password salt
        :type Salt: :class:`tencentcloud.ciam.v20220331.models.Salt`
        :param PasswordEncryptTypeEnum: Password encryption method. Valid values: `SHA1`, `BCRYPT`.
        :type PasswordEncryptTypeEnum: str
        """
        self.UserName = None
        self.PhoneNumber = None
        self.Email = None
        self.ResidentIdentityCard = None
        self.Nickname = None
        self.Address = None
        self.UserGroup = None
        self.QqOpenId = None
        self.QqUnionId = None
        self.WechatOpenId = None
        self.WechatUnionId = None
        self.AlipayUserId = None
        self.Description = None
        self.Birthdate = None
        self.Name = None
        self.Locale = None
        self.Gender = None
        self.IdentityVerificationMethod = None
        self.IdentityVerified = None
        self.Job = None
        self.Nationality = None
        self.Zone = None
        self.Password = None
        self.CustomizationAttributes = None
        self.Salt = None
        self.PasswordEncryptTypeEnum = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Email = params.get("Email")
        self.ResidentIdentityCard = params.get("ResidentIdentityCard")
        self.Nickname = params.get("Nickname")
        self.Address = params.get("Address")
        self.UserGroup = params.get("UserGroup")
        self.QqOpenId = params.get("QqOpenId")
        self.QqUnionId = params.get("QqUnionId")
        self.WechatOpenId = params.get("WechatOpenId")
        self.WechatUnionId = params.get("WechatUnionId")
        self.AlipayUserId = params.get("AlipayUserId")
        self.Description = params.get("Description")
        self.Birthdate = params.get("Birthdate")
        self.Name = params.get("Name")
        self.Locale = params.get("Locale")
        self.Gender = params.get("Gender")
        self.IdentityVerificationMethod = params.get("IdentityVerificationMethod")
        self.IdentityVerified = params.get("IdentityVerified")
        self.Job = params.get("Job")
        self.Nationality = params.get("Nationality")
        self.Zone = params.get("Zone")
        self.Password = params.get("Password")
        if params.get("CustomizationAttributes") is not None:
            self.CustomizationAttributes = []
            for item in params.get("CustomizationAttributes"):
                obj = MemberMap()
                obj._deserialize(item)
                self.CustomizationAttributes.append(obj)
        if params.get("Salt") is not None:
            self.Salt = Salt()
            self.Salt._deserialize(params.get("Salt"))
        self.PasswordEncryptTypeEnum = params.get("PasswordEncryptTypeEnum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Job(AbstractModel):
    """Task details

    """

    def __init__(self):
        r"""
        :param Id: Task ID
        :type Id: str
        :param Status: Task status

<li> **PENDING** </li>  Pending
<li> **PROCESSING** </li>  Executing
<li> **COMPLETED** </li>  Completed
<li> **FAILED** </li>  Failed
        :type Status: str
        :param Type: Task type

<li> **IMPORT_USER** </li>  User import
<li> **EXPORT_USER** </li>  User export
        :type Type: str
        :param CreatedDate: Task creation time
        :type CreatedDate: int
        :param Format: Data type of the task

<li> **JSON** </li>  JSON
<li> **NDJSON** </li>  New-line Delimited JSON
<li> **CSV** </li>  Comma-Separated Values
Note: This field may return null, indicating that no valid values can be obtained.
        :type Format: str
        :param Location: Task result download address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Location: str
        :param ErrorDetails: Failure details
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorDetails: list of ErrorDetails
        :param FailedUsers: Failed user
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailedUsers: list of FailedUsers
        """
        self.Id = None
        self.Status = None
        self.Type = None
        self.CreatedDate = None
        self.Format = None
        self.Location = None
        self.ErrorDetails = None
        self.FailedUsers = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.CreatedDate = params.get("CreatedDate")
        self.Format = params.get("Format")
        self.Location = params.get("Location")
        if params.get("ErrorDetails") is not None:
            self.ErrorDetails = []
            for item in params.get("ErrorDetails"):
                obj = ErrorDetails()
                obj._deserialize(item)
                self.ErrorDetails.append(obj)
        if params.get("FailedUsers") is not None:
            self.FailedUsers = []
            for item in params.get("FailedUsers"):
                obj = FailedUsers()
                obj._deserialize(item)
                self.FailedUsers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkAccountRequest(AbstractModel):
    """LinkAccount request structure.

    """

    def __init__(self):
        r"""
        :param UserStoreId: User directory ID
        :type UserStoreId: str
        :param PrimaryUserId: Primary user ID
        :type PrimaryUserId: str
        :param SecondaryUserId: Secondary user ID
        :type SecondaryUserId: str
        :param UserLinkedOnAttribute: Fusion attribute

<li> **PHONENUMBER** </li>	  Mobile number
<li> **EMAIL** </li>  Email
        :type UserLinkedOnAttribute: str
        """
        self.UserStoreId = None
        self.PrimaryUserId = None
        self.SecondaryUserId = None
        self.UserLinkedOnAttribute = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        self.PrimaryUserId = params.get("PrimaryUserId")
        self.SecondaryUserId = params.get("SecondaryUserId")
        self.UserLinkedOnAttribute = params.get("UserLinkedOnAttribute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkAccountResponse(AbstractModel):
    """LinkAccount response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ListJobsRequest(AbstractModel):
    """ListJobs request structure.

    """

    def __init__(self):
        r"""
        :param UserStoreId: User directory ID
        :type UserStoreId: str
        :param JobIds: List of task IDs. If this parameter is empty, all tasks will be returned.
        :type JobIds: list of str
        """
        self.UserStoreId = None
        self.JobIds = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        self.JobIds = params.get("JobIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListJobsResponse(AbstractModel):
    """ListJobs response structure.

    """

    def __init__(self):
        r"""
        :param JobSet: List of tasks
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobSet: list of Job
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("JobSet") is not None:
            self.JobSet = []
            for item in params.get("JobSet"):
                obj = Job()
                obj._deserialize(item)
                self.JobSet.append(obj)
        self.RequestId = params.get("RequestId")


class ListLogMessageByConditionRequest(AbstractModel):
    """ListLogMessageByCondition request structure.

    """

    def __init__(self):
        r"""
        :param UserStoreId: User pool ID
        :type UserStoreId: str
        :param Pageable: Pagination data
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param StartTime: Start timestamp accurate to the millisecond
        :type StartTime: int
        :param Filters: Valid values of `Key`: `events`.

<li> **events** </li>	Values can be one or multiple items in ["SIGNUP", "USER_UPDATE", "USER_DELETE", "USER_CREATE", "ACCOUNT_LINKING"].
        :type Filters: list of Filter
        """
        self.UserStoreId = None
        self.Pageable = None
        self.StartTime = None
        self.Filters = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        if params.get("Pageable") is not None:
            self.Pageable = Pageable()
            self.Pageable._deserialize(params.get("Pageable"))
        self.StartTime = params.get("StartTime")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListLogMessageByConditionResponse(AbstractModel):
    """ListLogMessageByCondition response structure.

    """

    def __init__(self):
        r"""
        :param Total: Total number
        :type Total: int
        :param Pageable: Pagination object
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param Content: List of logs
Note: This field may return null, indicating that no valid values can be obtained.
        :type Content: list of LogMessage
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.Pageable = None
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Pageable") is not None:
            self.Pageable = Pageable()
            self.Pageable._deserialize(params.get("Pageable"))
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = LogMessage()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RequestId = params.get("RequestId")


class ListUserByPropertyRequest(AbstractModel):
    """ListUserByProperty request structure.

    """

    def __init__(self):
        r"""
        :param UserStoreId: User directory ID
        :type UserStoreId: str
        :param PropertyCode: Query attribute

<li> **phoneNumber** </li>	  Mobile number
<li> **email** </li>  Email
        :type PropertyCode: str
        :param PropertyValue: Attribute value
        :type PropertyValue: str
        :param Original: 
        :type Original: bool
        """
        self.UserStoreId = None
        self.PropertyCode = None
        self.PropertyValue = None
        self.Original = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        self.PropertyCode = params.get("PropertyCode")
        self.PropertyValue = params.get("PropertyValue")
        self.Original = params.get("Original")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserByPropertyResponse(AbstractModel):
    """ListUserByProperty response structure.

    """

    def __init__(self):
        r"""
        :param Users: List of users
Note: This field may return null, indicating that no valid values can be obtained.
        :type Users: list of User
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Users = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = User()
                obj._deserialize(item)
                self.Users.append(obj)
        self.RequestId = params.get("RequestId")


class ListUserRequest(AbstractModel):
    """ListUser request structure.

    """

    def __init__(self):
        r"""
        :param UserStoreId: User directory ID
        :type UserStoreId: str
        :param Pageable: Pagination data
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param Filters: Valid values of `Key`: `condition`, `userGroupId`.

<li> **condition** </li>	Values = Query condition, which can be user ID, username, mobile number, or email address.
<li> **userGroupId** </li>	Values = User group ID
        :type Filters: list of Filter
        :param Original: 
        :type Original: bool
        """
        self.UserStoreId = None
        self.Pageable = None
        self.Filters = None
        self.Original = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        if params.get("Pageable") is not None:
            self.Pageable = Pageable()
            self.Pageable._deserialize(params.get("Pageable"))
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Original = params.get("Original")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserResponse(AbstractModel):
    """ListUser response structure.

    """

    def __init__(self):
        r"""
        :param Total: Total number
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param Pageable: Pagination object
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param Content: List of users
Note: This field may return null, indicating that no valid values can be obtained.
        :type Content: list of User
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.Pageable = None
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Pageable") is not None:
            self.Pageable = Pageable()
            self.Pageable._deserialize(params.get("Pageable"))
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = User()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RequestId = params.get("RequestId")


class LogMessage(AbstractModel):
    """Log details

    """

    def __init__(self):
        r"""
        :param LogId: Log ID
        :type LogId: str
        :param TenantId: Tenant ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TenantId: str
        :param UserStoreId: User pool ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserStoreId: str
        :param EventCode: Event code
Note: This field may return null, indicating that no valid values can be obtained.
        :type EventCode: str
        :param EventDate: Event timestamp in milliseconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type EventDate: int
        :param Description: Description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param Participant: Event participant

<li> **TENANT** </li>  Tenant
<li> **USER** </li>  User
Note: This field may return null, indicating that no valid values can be obtained.
        :type Participant: str
        :param ApplicationClientId: Application `clientId`
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationClientId: str
        :param ApplicationName: Application name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param AuthSourceId: Authentication source ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuthSourceId: str
        :param AuthSourceName: Authentication source name
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuthSourceName: str
        :param AuthSourceType: Authentication source type
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuthSourceType: str
        :param AuthSourceCategory: Authentication source category
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuthSourceCategory: str
        :param Ip: IP address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ip: str
        :param UserAgent: User agent
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserAgent: str
        :param UserId: User ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param Detail: Details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Detail: str
        """
        self.LogId = None
        self.TenantId = None
        self.UserStoreId = None
        self.EventCode = None
        self.EventDate = None
        self.Description = None
        self.Participant = None
        self.ApplicationClientId = None
        self.ApplicationName = None
        self.AuthSourceId = None
        self.AuthSourceName = None
        self.AuthSourceType = None
        self.AuthSourceCategory = None
        self.Ip = None
        self.UserAgent = None
        self.UserId = None
        self.Detail = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.TenantId = params.get("TenantId")
        self.UserStoreId = params.get("UserStoreId")
        self.EventCode = params.get("EventCode")
        self.EventDate = params.get("EventDate")
        self.Description = params.get("Description")
        self.Participant = params.get("Participant")
        self.ApplicationClientId = params.get("ApplicationClientId")
        self.ApplicationName = params.get("ApplicationName")
        self.AuthSourceId = params.get("AuthSourceId")
        self.AuthSourceName = params.get("AuthSourceName")
        self.AuthSourceType = params.get("AuthSourceType")
        self.AuthSourceCategory = params.get("AuthSourceCategory")
        self.Ip = params.get("Ip")
        self.UserAgent = params.get("UserAgent")
        self.UserId = params.get("UserId")
        self.Detail = params.get("Detail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MemberMap(AbstractModel):
    """Map data type

    """

    def __init__(self):
        r"""
        :param Name: Key
        :type Name: str
        :param Value: Value
        :type Value: str
        :param Type: Type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        """
        self.Name = None
        self.Value = None
        self.Type = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Pageable(AbstractModel):
    """Pagination object

    """

    def __init__(self):
        r"""
        :param PageSize: Number of entries per page
        :type PageSize: int
        :param PageNumber: Current page number
        :type PageNumber: int
        """
        self.PageSize = None
        self.PageNumber = None


    def _deserialize(self, params):
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordRequest(AbstractModel):
    """ResetPassword request structure.

    """

    def __init__(self):
        r"""
        :param UserId: User ID
        :type UserId: str
        :param UserStoreId: User directory ID
        :type UserStoreId: str
        """
        self.UserId = None
        self.UserStoreId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserStoreId = params.get("UserStoreId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordResponse(AbstractModel):
    """ResetPassword response structure.

    """

    def __init__(self):
        r"""
        :param Password: User password after reset
        :type Password: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Password = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.RequestId = params.get("RequestId")


class Salt(AbstractModel):
    """Password salt

    """

    def __init__(self):
        r"""
        :param SaltValue: Salt value
        :type SaltValue: str
        :param SaltLocation: Salt value location
        :type SaltLocation: :class:`tencentcloud.ciam.v20220331.models.SaltLocation`
        """
        self.SaltValue = None
        self.SaltLocation = None


    def _deserialize(self, params):
        self.SaltValue = params.get("SaltValue")
        if params.get("SaltLocation") is not None:
            self.SaltLocation = SaltLocation()
            self.SaltLocation._deserialize(params.get("SaltLocation"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaltLocation(AbstractModel):
    """Salt location

    """

    def __init__(self):
        r"""
        :param SaltLocationTypeEnum: Password salt type. Valid values: `HEAD`, `TAIL`, `OTHER`.
        :type SaltLocationTypeEnum: str
        :param SaltLocationRule: Salting rule
        :type SaltLocationRule: :class:`tencentcloud.ciam.v20220331.models.SaltLocationRule`
        """
        self.SaltLocationTypeEnum = None
        self.SaltLocationRule = None


    def _deserialize(self, params):
        self.SaltLocationTypeEnum = params.get("SaltLocationTypeEnum")
        if params.get("SaltLocationRule") is not None:
            self.SaltLocationRule = SaltLocationRule()
            self.SaltLocationRule._deserialize(params.get("SaltLocationRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaltLocationRule(AbstractModel):
    """Salt location rule

    """

    def __init__(self):
        r"""
        :param Regex: Expression
        :type Regex: str
        """
        self.Regex = None


    def _deserialize(self, params):
        self.Regex = params.get("Regex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPasswordRequest(AbstractModel):
    """SetPassword request structure.

    """

    def __init__(self):
        r"""
        :param UserStoreId: User directory ID
        :type UserStoreId: str
        :param UserId: User ID
        :type UserId: str
        :param Password: Password
        :type Password: str
        """
        self.UserStoreId = None
        self.UserId = None
        self.Password = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        self.UserId = params.get("UserId")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPasswordResponse(AbstractModel):
    """SetPassword response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateUserRequest(AbstractModel):
    """UpdateUser request structure.

    """

    def __init__(self):
        r"""
        :param UserId: User ID
        :type UserId: str
        :param UserStoreId: User directory ID
        :type UserStoreId: str
        :param UserName: Username
        :type UserName: str
        :param PhoneNumber: Mobile number
        :type PhoneNumber: str
        :param Email: Email address
        :type Email: str
        :param Nickname: Nickname
        :type Nickname: str
        :param Address: Address
        :type Address: str
        :param UserGroup: User group
        :type UserGroup: list of str
        :param Birthdate: Date of birth
        :type Birthdate: int
        :param CustomizationAttributes: Custom attribute
        :type CustomizationAttributes: list of MemberMap
        """
        self.UserId = None
        self.UserStoreId = None
        self.UserName = None
        self.PhoneNumber = None
        self.Email = None
        self.Nickname = None
        self.Address = None
        self.UserGroup = None
        self.Birthdate = None
        self.CustomizationAttributes = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserStoreId = params.get("UserStoreId")
        self.UserName = params.get("UserName")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Email = params.get("Email")
        self.Nickname = params.get("Nickname")
        self.Address = params.get("Address")
        self.UserGroup = params.get("UserGroup")
        self.Birthdate = params.get("Birthdate")
        if params.get("CustomizationAttributes") is not None:
            self.CustomizationAttributes = []
            for item in params.get("CustomizationAttributes"):
                obj = MemberMap()
                obj._deserialize(item)
                self.CustomizationAttributes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserResponse(AbstractModel):
    """UpdateUser response structure.

    """

    def __init__(self):
        r"""
        :param User: User information after update
Note: This field may return null, indicating that no valid values can be obtained.
        :type User: :class:`tencentcloud.ciam.v20220331.models.User`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.User = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("User") is not None:
            self.User = User()
            self.User._deserialize(params.get("User"))
        self.RequestId = params.get("RequestId")


class UpdateUserStatusRequest(AbstractModel):
    """UpdateUserStatus request structure.

    """

    def __init__(self):
        r"""
        :param UserStoreId: User directory ID
        :type UserStoreId: str
        :param UserId: User ID
        :type UserId: str
        :param Status: User status

<li> **NORMAL** </li>	  Normal
<li> **LOCK** </li>  Locked
<li> **FREEZE** </li>	  Frozen
        :type Status: str
        """
        self.UserStoreId = None
        self.UserId = None
        self.Status = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        self.UserId = params.get("UserId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserStatusResponse(AbstractModel):
    """UpdateUserStatus response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class User(AbstractModel):
    """User information

    """

    def __init__(self):
        r"""
        :param UserId: User ID
        :type UserId: str
        :param UserName: Username
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param PhoneNumber: Mobile number
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhoneNumber: str
        :param Email: Email address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Email: str
        :param LastSignOn: Last login time
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastSignOn: int
        :param CreatedDate: Creation time
        :type CreatedDate: int
        :param Status: Status
        :type Status: str
        :param UserDataSourceEnum: User source
        :type UserDataSourceEnum: str
        :param Nickname: Nickname
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nickname: str
        :param Address: Address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: str
        :param Birthdate: Date of birth
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthdate: int
        :param UserGroups: User group ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserGroups: list of str
        :param LastModifiedDate: Last modified time
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastModifiedDate: int
        :param CustomAttributes: Custom attribute
Note: This field may return null, indicating that no valid values can be obtained.
        :type CustomAttributes: list of MemberMap
        :param ResidentIdentityCard: ID card number
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResidentIdentityCard: str
        :param QqOpenId: `OpenId` on QQ
Note: This field may return null, indicating that no valid values can be obtained.
        :type QqOpenId: str
        :param QqUnionId: `UnionId` on QQ
Note: This field may return null, indicating that no valid values can be obtained.
        :type QqUnionId: str
        :param WechatOpenId: `WechatOpenId` on WeChat
Note: This field may return null, indicating that no valid values can be obtained.
        :type WechatOpenId: str
        :param WechatUnionId: `WechatUnionId` on WeChat
Note: This field may return null, indicating that no valid values can be obtained.
        :type WechatUnionId: str
        :param AlipayUserId: `AlipayUserId` on Alipay
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlipayUserId: str
        :param Description: Description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param Name: Name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param Locale: Coordinate
Note: This field may return null, indicating that no valid values can be obtained.
        :type Locale: str
        :param Gender: Gender
Note: This field may return null, indicating that no valid values can be obtained.
        :type Gender: str
        :param IdentityVerificationMethod: Identity verification method
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityVerificationMethod: str
        :param IdentityVerified: Whether the identity is verified
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityVerified: bool
        :param Job: Job
Note: This field may return null, indicating that no valid values can be obtained.
        :type Job: str
        :param Nationality: Country/Region
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nationality: str
        :param Primary: Whether the account is the primary account (after account merge, this parameter is `true` for primary accounts and `false` for secondary account).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Primary: bool
        :param Zone: Time zone
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param AlreadyFirstLogin: Whether the account has ever logged in.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlreadyFirstLogin: bool
        :param TenantId: Tenant ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TenantId: str
        :param UserStoreId: User directory ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserStoreId: str
        :param Version: Version
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: int
        :param LockType: Lock type (locked by admin or locked by login policy)
Note: This field may return null, indicating that no valid values can be obtained.
        :type LockType: str
        :param LockTime: Lock time
Note: This field may return null, indicating that no valid values can be obtained.
        :type LockTime: int
        """
        self.UserId = None
        self.UserName = None
        self.PhoneNumber = None
        self.Email = None
        self.LastSignOn = None
        self.CreatedDate = None
        self.Status = None
        self.UserDataSourceEnum = None
        self.Nickname = None
        self.Address = None
        self.Birthdate = None
        self.UserGroups = None
        self.LastModifiedDate = None
        self.CustomAttributes = None
        self.ResidentIdentityCard = None
        self.QqOpenId = None
        self.QqUnionId = None
        self.WechatOpenId = None
        self.WechatUnionId = None
        self.AlipayUserId = None
        self.Description = None
        self.Name = None
        self.Locale = None
        self.Gender = None
        self.IdentityVerificationMethod = None
        self.IdentityVerified = None
        self.Job = None
        self.Nationality = None
        self.Primary = None
        self.Zone = None
        self.AlreadyFirstLogin = None
        self.TenantId = None
        self.UserStoreId = None
        self.Version = None
        self.LockType = None
        self.LockTime = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserName = params.get("UserName")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Email = params.get("Email")
        self.LastSignOn = params.get("LastSignOn")
        self.CreatedDate = params.get("CreatedDate")
        self.Status = params.get("Status")
        self.UserDataSourceEnum = params.get("UserDataSourceEnum")
        self.Nickname = params.get("Nickname")
        self.Address = params.get("Address")
        self.Birthdate = params.get("Birthdate")
        self.UserGroups = params.get("UserGroups")
        self.LastModifiedDate = params.get("LastModifiedDate")
        if params.get("CustomAttributes") is not None:
            self.CustomAttributes = []
            for item in params.get("CustomAttributes"):
                obj = MemberMap()
                obj._deserialize(item)
                self.CustomAttributes.append(obj)
        self.ResidentIdentityCard = params.get("ResidentIdentityCard")
        self.QqOpenId = params.get("QqOpenId")
        self.QqUnionId = params.get("QqUnionId")
        self.WechatOpenId = params.get("WechatOpenId")
        self.WechatUnionId = params.get("WechatUnionId")
        self.AlipayUserId = params.get("AlipayUserId")
        self.Description = params.get("Description")
        self.Name = params.get("Name")
        self.Locale = params.get("Locale")
        self.Gender = params.get("Gender")
        self.IdentityVerificationMethod = params.get("IdentityVerificationMethod")
        self.IdentityVerified = params.get("IdentityVerified")
        self.Job = params.get("Job")
        self.Nationality = params.get("Nationality")
        self.Primary = params.get("Primary")
        self.Zone = params.get("Zone")
        self.AlreadyFirstLogin = params.get("AlreadyFirstLogin")
        self.TenantId = params.get("TenantId")
        self.UserStoreId = params.get("UserStoreId")
        self.Version = params.get("Version")
        self.LockType = params.get("LockType")
        self.LockTime = params.get("LockTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        