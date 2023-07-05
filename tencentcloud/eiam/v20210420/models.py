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


class AccountGroupInfo(AbstractModel):
    """List of queried account group information.

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: Account group ID.
        :type AccountGroupId: str
        :param _GroupName: Account group name.
        :type GroupName: str
        :param _Description: Remarks.
        :type Description: str
        :param _CreatedDate: Creation time.
        :type CreatedDate: str
        """
        self._AccountGroupId = None
        self._GroupName = None
        self._Description = None
        self._CreatedDate = None

    @property
    def AccountGroupId(self):
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate


    def _deserialize(self, params):
        self._AccountGroupId = params.get("AccountGroupId")
        self._GroupName = params.get("GroupName")
        self._Description = params.get("Description")
        self._CreatedDate = params.get("CreatedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountGroupSearchCriteria(AbstractModel):
    """Account group query parameters

    """

    def __init__(self):
        r"""
        :param _Keyword: Keyword
        :type Keyword: str
        """
        self._Keyword = None

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAccountToAccountGroupRequest(AbstractModel):
    """AddAccountToAccountGroup request structure.

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: Account group ID
        :type AccountGroupId: str
        :param _AccountIds: List of IDs of the accounts to be added to the account group.
        :type AccountIds: list of str
        """
        self._AccountGroupId = None
        self._AccountIds = None

    @property
    def AccountGroupId(self):
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def AccountIds(self):
        return self._AccountIds

    @AccountIds.setter
    def AccountIds(self, AccountIds):
        self._AccountIds = AccountIds


    def _deserialize(self, params):
        self._AccountGroupId = params.get("AccountGroupId")
        self._AccountIds = params.get("AccountIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAccountToAccountGroupResponse(AbstractModel):
    """AddAccountToAccountGroup response structure.

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


class AddUserToUserGroupRequest(AbstractModel):
    """AddUserToUserGroup request structure.

    """

    def __init__(self):
        r"""
        :param _UserIds: List of IDs of the users to be added to the user group.
        :type UserIds: list of str
        :param _UserGroupId: User group ID, which is globally unique.
        :type UserGroupId: str
        """
        self._UserIds = None
        self._UserGroupId = None

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId


    def _deserialize(self, params):
        self._UserIds = params.get("UserIds")
        self._UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserToUserGroupResponse(AbstractModel):
    """AddUserToUserGroup response structure.

    """

    def __init__(self):
        r"""
        :param _FailedItems: List of IDs of the users failed to be added to the user group.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FailedItems: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FailedItems = None
        self._RequestId = None

    @property
    def FailedItems(self):
        return self._FailedItems

    @FailedItems.setter
    def FailedItems(self, FailedItems):
        self._FailedItems = FailedItems

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailedItems = params.get("FailedItems")
        self._RequestId = params.get("RequestId")


class AppAccountInfo(AbstractModel):
    """List of queried account information.

    """

    def __init__(self):
        r"""
        :param _AccountId: Account ID.
        :type AccountId: str
        :param _AccountName: Account name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccountName: str
        :param _UserList: User information list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserList: list of LinkUserInfo
        :param _Description: Description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _CreatedDate: Creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedDate: str
        """
        self._AccountId = None
        self._AccountName = None
        self._UserList = None
        self._Description = None
        self._CreatedDate = None

    @property
    def AccountId(self):
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def UserList(self):
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate


    def _deserialize(self, params):
        self._AccountId = params.get("AccountId")
        self._AccountName = params.get("AccountName")
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = LinkUserInfo()
                obj._deserialize(item)
                self._UserList.append(obj)
        self._Description = params.get("Description")
        self._CreatedDate = params.get("CreatedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppAccountSearchCriteria(AbstractModel):
    """Account query parameters

    """

    def __init__(self):
        r"""
        :param _Keyword: Keyword
        :type Keyword: str
        """
        self._Keyword = None

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationAuthorizationInfo(AbstractModel):
    """Application information list.

    """

    def __init__(self):
        r"""
        :param _ApplicationAccounts: List of the user's accounts under authorized applications
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationAccounts: list of str
        :param _ApplicationId: Application ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param _InheritedForm: List of IDs of the user's user groups and organization nodes that have access to the application.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InheritedForm: :class:`tencentcloud.eiam.v20210420.models.InheritedForm`
        :param _ApplicationName: Application name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param _CreatedDate: Application creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedDate: str
        """
        self._ApplicationAccounts = None
        self._ApplicationId = None
        self._InheritedForm = None
        self._ApplicationName = None
        self._CreatedDate = None

    @property
    def ApplicationAccounts(self):
        return self._ApplicationAccounts

    @ApplicationAccounts.setter
    def ApplicationAccounts(self, ApplicationAccounts):
        self._ApplicationAccounts = ApplicationAccounts

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def InheritedForm(self):
        return self._InheritedForm

    @InheritedForm.setter
    def InheritedForm(self, InheritedForm):
        self._InheritedForm = InheritedForm

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate


    def _deserialize(self, params):
        self._ApplicationAccounts = params.get("ApplicationAccounts")
        self._ApplicationId = params.get("ApplicationId")
        if params.get("InheritedForm") is not None:
            self._InheritedForm = InheritedForm()
            self._InheritedForm._deserialize(params.get("InheritedForm"))
        self._ApplicationName = params.get("ApplicationName")
        self._CreatedDate = params.get("CreatedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationInfoSearchCriteria(AbstractModel):
    """Application attribute search criteria.

    """

    def __init__(self):
        r"""
        :param _Keyword: Application search keyword, which can be application name or ID.
        :type Keyword: str
        :param _ApplicationType: Application type. Valid values: OAUTH2, JWT, CAS, SAML2, FORM, OIDC, APIGW
        :type ApplicationType: str
        """
        self._Keyword = None
        self._ApplicationType = None

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def ApplicationType(self):
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        self._ApplicationType = params.get("ApplicationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationInformation(AbstractModel):
    """Application information list.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID, which is globally unique.
        :type ApplicationId: str
        :param _DisplayName: Displayed application name, which can contain up to 64 characters and is the same as the application name by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param _CreatedDate: Application creation time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedDate: str
        :param _LastModifiedDate: Last update time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifiedDate: str
        :param _AppStatus: Application status.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AppStatus: bool
        :param _Icon: Application icon.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Icon: str
        :param _ApplicationType: Application type.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationType: str
        :param _ClientId: Client ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClientId: str
        """
        self._ApplicationId = None
        self._DisplayName = None
        self._CreatedDate = None
        self._LastModifiedDate = None
        self._AppStatus = None
        self._Icon = None
        self._ApplicationType = None
        self._ClientId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate

    @property
    def LastModifiedDate(self):
        return self._LastModifiedDate

    @LastModifiedDate.setter
    def LastModifiedDate(self, LastModifiedDate):
        self._LastModifiedDate = LastModifiedDate

    @property
    def AppStatus(self):
        return self._AppStatus

    @AppStatus.setter
    def AppStatus(self, AppStatus):
        self._AppStatus = AppStatus

    @property
    def Icon(self):
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def ApplicationType(self):
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._DisplayName = params.get("DisplayName")
        self._CreatedDate = params.get("CreatedDate")
        self._LastModifiedDate = params.get("LastModifiedDate")
        self._AppStatus = params.get("AppStatus")
        self._Icon = params.get("Icon")
        self._ApplicationType = params.get("ApplicationType")
        self._ClientId = params.get("ClientId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizationInfo(AbstractModel):
    """Returned authorization information.

    """

    def __init__(self):
        r"""
        :param _AppId: Unique application ID.
        :type AppId: str
        :param _AppName: Application name.
        :type AppName: str
        :param _EntityName: Type name.
        :type EntityName: str
        :param _EntityId: Unique type ID.
        :type EntityId: str
        :param _LastModifiedDate: Last update time in ISO 8601 format.
        :type LastModifiedDate: str
        :param _AuthorizationId: Unique authorization type ID.
        :type AuthorizationId: str
        """
        self._AppId = None
        self._AppName = None
        self._EntityName = None
        self._EntityId = None
        self._LastModifiedDate = None
        self._AuthorizationId = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def EntityName(self):
        return self._EntityName

    @EntityName.setter
    def EntityName(self, EntityName):
        self._EntityName = EntityName

    @property
    def EntityId(self):
        return self._EntityId

    @EntityId.setter
    def EntityId(self, EntityId):
        self._EntityId = EntityId

    @property
    def LastModifiedDate(self):
        return self._LastModifiedDate

    @LastModifiedDate.setter
    def LastModifiedDate(self, LastModifiedDate):
        self._LastModifiedDate = LastModifiedDate

    @property
    def AuthorizationId(self):
        return self._AuthorizationId

    @AuthorizationId.setter
    def AuthorizationId(self, AuthorizationId):
        self._AuthorizationId = AuthorizationId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._AppName = params.get("AppName")
        self._EntityName = params.get("EntityName")
        self._EntityId = params.get("EntityId")
        self._LastModifiedDate = params.get("LastModifiedDate")
        self._AuthorizationId = params.get("AuthorizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizationInfoSearchCriteria(AbstractModel):
    """User attribute search criteria.

    """

    def __init__(self):
        r"""
        :param _Keyword: Search by name. When the query type is user, the match criteria include username and application name. When the query type is user group, the match criteria include user group name and application name. When the query type is organization, the match criteria include organization name and application name.
        :type Keyword: str
        """
        self._Keyword = None

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizationUserResouceInfo(AbstractModel):
    """Returned list of eligible user data

    """

    def __init__(self):
        r"""
        :param _ResourceId: Resource ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceId: str
        :param _ResourceType: Resource type
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceType: str
        :param _Resource: Authorized resource
Note: this field may return null, indicating that no valid values can be obtained.
        :type Resource: str
        :param _InheritedForm: Inheritance relationship
Note: this field may return null, indicating that no valid values can be obtained.
        :type InheritedForm: :class:`tencentcloud.eiam.v20210420.models.InheritedForm`
        :param _ApplicationAccounts: Application account
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationAccounts: list of str
        :param _ResourceName: Resource name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceName: str
        """
        self._ResourceId = None
        self._ResourceType = None
        self._Resource = None
        self._InheritedForm = None
        self._ApplicationAccounts = None
        self._ResourceName = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def InheritedForm(self):
        return self._InheritedForm

    @InheritedForm.setter
    def InheritedForm(self, InheritedForm):
        self._InheritedForm = InheritedForm

    @property
    def ApplicationAccounts(self):
        return self._ApplicationAccounts

    @ApplicationAccounts.setter
    def ApplicationAccounts(self, ApplicationAccounts):
        self._ApplicationAccounts = ApplicationAccounts

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        self._Resource = params.get("Resource")
        if params.get("InheritedForm") is not None:
            self._InheritedForm = InheritedForm()
            self._InheritedForm._deserialize(params.get("InheritedForm"))
        self._ApplicationAccounts = params.get("ApplicationAccounts")
        self._ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountGroupRequest(AbstractModel):
    """CreateAccountGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _GroupName: Account group name.
        :type GroupName: str
        :param _Description: Description.
        :type Description: str
        """
        self._ApplicationId = None
        self._GroupName = None
        self._Description = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._GroupName = params.get("GroupName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountGroupResponse(AbstractModel):
    """CreateAccountGroup response structure.

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: Account group ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccountGroupId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccountGroupId = None
        self._RequestId = None

    @property
    def AccountGroupId(self):
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AccountGroupId = params.get("AccountGroupId")
        self._RequestId = params.get("RequestId")


class CreateAppAccountRequest(AbstractModel):
    """CreateAppAccount request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _AccountName: Account name
        :type AccountName: str
        :param _Password: Account password
        :type Password: str
        :param _Description: Description
        :type Description: str
        """
        self._ApplicationId = None
        self._AccountName = None
        self._Password = None
        self._Description = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._AccountName = params.get("AccountName")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppAccountResponse(AbstractModel):
    """CreateAppAccount response structure.

    """

    def __init__(self):
        r"""
        :param _AccountId: Account ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccountId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccountId = None
        self._RequestId = None

    @property
    def AccountId(self):
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AccountId = params.get("AccountId")
        self._RequestId = params.get("RequestId")


class CreateOrgNodeRequest(AbstractModel):
    """CreateOrgNode request structure.

    """

    def __init__(self):
        r"""
        :param _DisplayName: Organization node name, which can contain up to 64 characters.
        :type DisplayName: str
        :param _ParentOrgNodeId: Parent organization node ID. If this parameter is left empty, the organization will be created under the root organization node by default.
        :type ParentOrgNodeId: str
        :param _Description: Organization node description.
        :type Description: str
        :param _CustomizedOrgNodeId: External ID of the organization node, which is optional and customizable. If this parameter is specified, its uniqueness will be verified.
        :type CustomizedOrgNodeId: str
        """
        self._DisplayName = None
        self._ParentOrgNodeId = None
        self._Description = None
        self._CustomizedOrgNodeId = None

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def ParentOrgNodeId(self):
        return self._ParentOrgNodeId

    @ParentOrgNodeId.setter
    def ParentOrgNodeId(self, ParentOrgNodeId):
        self._ParentOrgNodeId = ParentOrgNodeId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CustomizedOrgNodeId(self):
        return self._CustomizedOrgNodeId

    @CustomizedOrgNodeId.setter
    def CustomizedOrgNodeId(self, CustomizedOrgNodeId):
        self._CustomizedOrgNodeId = CustomizedOrgNodeId


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._ParentOrgNodeId = params.get("ParentOrgNodeId")
        self._Description = params.get("Description")
        self._CustomizedOrgNodeId = params.get("CustomizedOrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrgNodeResponse(AbstractModel):
    """CreateOrgNode response structure.

    """

    def __init__(self):
        r"""
        :param _OrgNodeId: Organization node ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OrgNodeId = None
        self._RequestId = None

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OrgNodeId = params.get("OrgNodeId")
        self._RequestId = params.get("RequestId")


class CreateUserGroupRequest(AbstractModel):
    """CreateUserGroup request structure.

    """

    def __init__(self):
        r"""
        :param _DisplayName: User group nickname, which is unique and can contain up to 64 characters.
        :type DisplayName: str
        :param _Description: User group remarks, which can contain up to 512 characters.
        :type Description: str
        """
        self._DisplayName = None
        self._Description = None

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserGroupResponse(AbstractModel):
    """CreateUserGroup response structure.

    """

    def __init__(self):
        r"""
        :param _UserGroupId: User group ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UserGroupId = None
        self._RequestId = None

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        self._RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser request structure.

    """

    def __init__(self):
        r"""
        :param _UserName: Username, which can contain up to 64 characters.
        :type UserName: str
        :param _Password: User password, which needs to be configured according to the password policy.
        :type Password: str
        :param _DisplayName: Nickname, which can contain up to 64 characters and is the same as the username by default.
        :type DisplayName: str
        :param _Description: User remarks, which can contain up to 512 characters.
        :type Description: str
        :param _UserGroupIds: List of IDs of the user's user groups.
        :type UserGroupIds: list of str
        :param _Phone: User's mobile number, such as `+86-1xxxxxxxxxx`.
        :type Phone: str
        :param _OrgNodeId: Unique ID of the user's primary organization. If this parameter is left empty, the user will be created under the root node by default.
        :type OrgNodeId: str
        :param _ExpirationTime: User expiration time in ISO 8601 format.
        :type ExpirationTime: str
        :param _Email: User's email address.
        :type Email: str
        :param _PwdNeedReset: Whether the password needs to be reset. Default value: false (no).
        :type PwdNeedReset: bool
        :param _SecondaryOrgNodeIdList: List of IDs of the user's secondary organizations.
        :type SecondaryOrgNodeIdList: list of str
        """
        self._UserName = None
        self._Password = None
        self._DisplayName = None
        self._Description = None
        self._UserGroupIds = None
        self._Phone = None
        self._OrgNodeId = None
        self._ExpirationTime = None
        self._Email = None
        self._PwdNeedReset = None
        self._SecondaryOrgNodeIdList = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UserGroupIds(self):
        return self._UserGroupIds

    @UserGroupIds.setter
    def UserGroupIds(self, UserGroupIds):
        self._UserGroupIds = UserGroupIds

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def ExpirationTime(self):
        return self._ExpirationTime

    @ExpirationTime.setter
    def ExpirationTime(self, ExpirationTime):
        self._ExpirationTime = ExpirationTime

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def PwdNeedReset(self):
        return self._PwdNeedReset

    @PwdNeedReset.setter
    def PwdNeedReset(self, PwdNeedReset):
        self._PwdNeedReset = PwdNeedReset

    @property
    def SecondaryOrgNodeIdList(self):
        return self._SecondaryOrgNodeIdList

    @SecondaryOrgNodeIdList.setter
    def SecondaryOrgNodeIdList(self, SecondaryOrgNodeIdList):
        self._SecondaryOrgNodeIdList = SecondaryOrgNodeIdList


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._UserGroupIds = params.get("UserGroupIds")
        self._Phone = params.get("Phone")
        self._OrgNodeId = params.get("OrgNodeId")
        self._ExpirationTime = params.get("ExpirationTime")
        self._Email = params.get("Email")
        self._PwdNeedReset = params.get("PwdNeedReset")
        self._SecondaryOrgNodeIdList = params.get("SecondaryOrgNodeIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    """CreateUser response structure.

    """

    def __init__(self):
        r"""
        :param _UserId: Returned ID of the newly created user, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UserId = None
        self._RequestId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._RequestId = params.get("RequestId")


class DeleteAccountGroupRequest(AbstractModel):
    """DeleteAccountGroup request structure.

    """

    def __init__(self):
        r"""
        :param _AccountGroupIdList: Array of account group IDs.
        :type AccountGroupIdList: list of str
        """
        self._AccountGroupIdList = None

    @property
    def AccountGroupIdList(self):
        return self._AccountGroupIdList

    @AccountGroupIdList.setter
    def AccountGroupIdList(self, AccountGroupIdList):
        self._AccountGroupIdList = AccountGroupIdList


    def _deserialize(self, params):
        self._AccountGroupIdList = params.get("AccountGroupIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountGroupResponse(AbstractModel):
    """DeleteAccountGroup response structure.

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


class DeleteAppAccountRequest(AbstractModel):
    """DeleteAppAccount request structure.

    """

    def __init__(self):
        r"""
        :param _AccountIdList: Array of account IDs .
        :type AccountIdList: list of str
        """
        self._AccountIdList = None

    @property
    def AccountIdList(self):
        return self._AccountIdList

    @AccountIdList.setter
    def AccountIdList(self, AccountIdList):
        self._AccountIdList = AccountIdList


    def _deserialize(self, params):
        self._AccountIdList = params.get("AccountIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAppAccountResponse(AbstractModel):
    """DeleteAppAccount response structure.

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


class DeleteOrgNodeRequest(AbstractModel):
    """DeleteOrgNode request structure.

    """

    def __init__(self):
        r"""
        :param _OrgNodeId: Organization node ID, which is globally unique.
        :type OrgNodeId: str
        """
        self._OrgNodeId = None

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId


    def _deserialize(self, params):
        self._OrgNodeId = params.get("OrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrgNodeResponse(AbstractModel):
    """DeleteOrgNode response structure.

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


class DeleteUserGroupRequest(AbstractModel):
    """DeleteUserGroup request structure.

    """

    def __init__(self):
        r"""
        :param _UserGroupId: User group ID, which is globally unique.
        :type UserGroupId: str
        """
        self._UserGroupId = None

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserGroupResponse(AbstractModel):
    """DeleteUserGroup response structure.

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


class DeleteUserRequest(AbstractModel):
    """DeleteUser request structure.

    """

    def __init__(self):
        r"""
        :param _UserName: Username, which can contain up to 32 characters. You need to select either `UserName` or `UserId` as the search criterion; if both are selected, `UserName` will be used by default.
        :type UserName: str
        :param _UserId: User ID. You need to select either `UserName` or `UserId` as the search criterion. If both are selected, `UserName` will be used by default.
        :type UserId: str
        """
        self._UserName = None
        self._UserId = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    """DeleteUser response structure.

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


class DeleteUsersRequest(AbstractModel):
    """DeleteUsers request structure.

    """

    def __init__(self):
        r"""
        :param _DeleteIdList: List of IDs of the users to be deleted. You need to specify at least `DeleteIdList` or `DeleteNameList`. If both are specified, `DeleteNameList` will be used first.
        :type DeleteIdList: list of str
        :param _DeleteNameList: List of usernames of the users to be deleted. You need to specify at least `DeleteIdList` or `DeleteNameList`. If both are specified, `DeleteNameList` will be used first.
        :type DeleteNameList: list of str
        """
        self._DeleteIdList = None
        self._DeleteNameList = None

    @property
    def DeleteIdList(self):
        return self._DeleteIdList

    @DeleteIdList.setter
    def DeleteIdList(self, DeleteIdList):
        self._DeleteIdList = DeleteIdList

    @property
    def DeleteNameList(self):
        return self._DeleteNameList

    @DeleteNameList.setter
    def DeleteNameList(self, DeleteNameList):
        self._DeleteNameList = DeleteNameList


    def _deserialize(self, params):
        self._DeleteIdList = params.get("DeleteIdList")
        self._DeleteNameList = params.get("DeleteNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsersResponse(AbstractModel):
    """DeleteUsers response structure.

    """

    def __init__(self):
        r"""
        :param _FailedItems: Information of the users failed to be deleted. When the business parameter is `DeleteIdList`, this field will return the list of IDs of the users failed to be deleted. When the business parameter is `DeleteNameList`, this field will return the list of usernames of the users failed to be deleted.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FailedItems: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FailedItems = None
        self._RequestId = None

    @property
    def FailedItems(self):
        return self._FailedItems

    @FailedItems.setter
    def FailedItems(self, FailedItems):
        self._FailedItems = FailedItems

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailedItems = params.get("FailedItems")
        self._RequestId = params.get("RequestId")


class DescribeAccountGroupRequest(AbstractModel):
    """DescribeAccountGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _SearchCondition: Search criterion. You can combine multiple search criteria and search in multiple data ranges. In addition, multiple query methods such as full match, partial match, and range match are supported. Specifically, double quotation marks ("") indicate full match, an asterisk (*) at the end of the field indicates partial match, and an empty field indicates to query the full table by default.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.AccountGroupSearchCriteria`
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._ApplicationId = None
        self._SearchCondition = None
        self._Offset = None
        self._Limit = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

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
        self._ApplicationId = params.get("ApplicationId")
        if params.get("SearchCondition") is not None:
            self._SearchCondition = AccountGroupSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountGroupResponse(AbstractModel):
    """DescribeAccountGroup response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records returned for the query.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _ApplicationId: Application ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param _AccountGroupList: Returned list of eligible data.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccountGroupList: list of AccountGroupInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ApplicationId = None
        self._AccountGroupList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def AccountGroupList(self):
        return self._AccountGroupList

    @AccountGroupList.setter
    def AccountGroupList(self, AccountGroupList):
        self._AccountGroupList = AccountGroupList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._ApplicationId = params.get("ApplicationId")
        if params.get("AccountGroupList") is not None:
            self._AccountGroupList = []
            for item in params.get("AccountGroupList"):
                obj = AccountGroupInfo()
                obj._deserialize(item)
                self._AccountGroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAppAccountRequest(AbstractModel):
    """DescribeAppAccount request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _SearchCondition: Search criterion. You can combine multiple search criteria and search in multiple data ranges. In addition, multiple query methods such as full match, partial match, and range match are supported. Specifically, double quotation marks ("") indicate full match, an asterisk (*) at the end of the field indicates partial match, and an empty field indicates to query the full table by default.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.AppAccountSearchCriteria`
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._ApplicationId = None
        self._SearchCondition = None
        self._Offset = None
        self._Limit = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

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
        self._ApplicationId = params.get("ApplicationId")
        if params.get("SearchCondition") is not None:
            self._SearchCondition = AppAccountSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppAccountResponse(AbstractModel):
    """DescribeAppAccount response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records returned for the query.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _ApplicationId: Application ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param _AppAccountList: Returned list of eligible data.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AppAccountList: list of AppAccountInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ApplicationId = None
        self._AppAccountList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def AppAccountList(self):
        return self._AppAccountList

    @AppAccountList.setter
    def AppAccountList(self, AppAccountList):
        self._AppAccountList = AppAccountList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._ApplicationId = params.get("ApplicationId")
        if params.get("AppAccountList") is not None:
            self._AppAccountList = []
            for item in params.get("AppAccountList"):
                obj = AppAccountInfo()
                obj._deserialize(item)
                self._AppAccountList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeApplicationRequest(AbstractModel):
    """DescribeApplication request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID, which is globally unique. You must specify at least this parameter or `ClientId`.
        :type ApplicationId: str
        :param _ClientId: Client ID. You must specify at least this parameter or `ApplicationId`.
        :type ClientId: str
        """
        self._ApplicationId = None
        self._ClientId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ClientId = params.get("ClientId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationResponse(AbstractModel):
    """DescribeApplication response structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Key ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyId: str
        :param _DisplayName: Displayed application name, which can contain up to 64 characters and is the same as the application name by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param _LastModifiedDate: Last modification time of the application in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifiedDate: str
        :param _ClientId: Client ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClientId: str
        :param _ApplicationType: Application type, i.e., the application template type selected during application creation.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationType: str
        :param _CreatedDate: Application creation time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedDate: str
        :param _ApplicationId: Application ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param _TokenExpired: Token validity period in seconds.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TokenExpired: int
        :param _ClientSecret: Client secret.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClientSecret: str
        :param _PublicKey: Public key information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicKey: str
        :param _AuthorizeUrl: Authorization address.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthorizeUrl: str
        :param _IconUrl: Access address of the application icon image.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IconUrl: str
        :param _SecureLevel: Security level.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecureLevel: str
        :param _AppStatus: Application status.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AppStatus: bool
        :param _Description: Description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyId = None
        self._DisplayName = None
        self._LastModifiedDate = None
        self._ClientId = None
        self._ApplicationType = None
        self._CreatedDate = None
        self._ApplicationId = None
        self._TokenExpired = None
        self._ClientSecret = None
        self._PublicKey = None
        self._AuthorizeUrl = None
        self._IconUrl = None
        self._SecureLevel = None
        self._AppStatus = None
        self._Description = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def LastModifiedDate(self):
        return self._LastModifiedDate

    @LastModifiedDate.setter
    def LastModifiedDate(self, LastModifiedDate):
        self._LastModifiedDate = LastModifiedDate

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ApplicationType(self):
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def TokenExpired(self):
        return self._TokenExpired

    @TokenExpired.setter
    def TokenExpired(self, TokenExpired):
        self._TokenExpired = TokenExpired

    @property
    def ClientSecret(self):
        return self._ClientSecret

    @ClientSecret.setter
    def ClientSecret(self, ClientSecret):
        self._ClientSecret = ClientSecret

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def AuthorizeUrl(self):
        return self._AuthorizeUrl

    @AuthorizeUrl.setter
    def AuthorizeUrl(self, AuthorizeUrl):
        self._AuthorizeUrl = AuthorizeUrl

    @property
    def IconUrl(self):
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def SecureLevel(self):
        return self._SecureLevel

    @SecureLevel.setter
    def SecureLevel(self, SecureLevel):
        self._SecureLevel = SecureLevel

    @property
    def AppStatus(self):
        return self._AppStatus

    @AppStatus.setter
    def AppStatus(self, AppStatus):
        self._AppStatus = AppStatus

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._DisplayName = params.get("DisplayName")
        self._LastModifiedDate = params.get("LastModifiedDate")
        self._ClientId = params.get("ClientId")
        self._ApplicationType = params.get("ApplicationType")
        self._CreatedDate = params.get("CreatedDate")
        self._ApplicationId = params.get("ApplicationId")
        self._TokenExpired = params.get("TokenExpired")
        self._ClientSecret = params.get("ClientSecret")
        self._PublicKey = params.get("PublicKey")
        self._AuthorizeUrl = params.get("AuthorizeUrl")
        self._IconUrl = params.get("IconUrl")
        self._SecureLevel = params.get("SecureLevel")
        self._AppStatus = params.get("AppStatus")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class DescribeOrgNodeRequest(AbstractModel):
    """DescribeOrgNode request structure.

    """

    def __init__(self):
        r"""
        :param _OrgNodeId: Organization node ID, which is globally unique and can contain up to 64 characters. If this parameter is left empty, the information of the root organization node will be read by default.
        :type OrgNodeId: str
        :param _IncludeOrgNodeChildInfo: Whether to read the information of its sub-nodes. When this parameter is left empty or specified as `false`, only the information of the current organization node will be read by default. When it is specified as `true`, the information of the current organization node and its level-1 sub-nodes will be read.
        :type IncludeOrgNodeChildInfo: bool
        """
        self._OrgNodeId = None
        self._IncludeOrgNodeChildInfo = None

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def IncludeOrgNodeChildInfo(self):
        return self._IncludeOrgNodeChildInfo

    @IncludeOrgNodeChildInfo.setter
    def IncludeOrgNodeChildInfo(self, IncludeOrgNodeChildInfo):
        self._IncludeOrgNodeChildInfo = IncludeOrgNodeChildInfo


    def _deserialize(self, params):
        self._OrgNodeId = params.get("OrgNodeId")
        self._IncludeOrgNodeChildInfo = params.get("IncludeOrgNodeChildInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrgNodeResponse(AbstractModel):
    """DescribeOrgNode response structure.

    """

    def __init__(self):
        r"""
        :param _DisplayName: Displayed organization node name, which can contain up to 64 characters and is the same as the organization name by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param _LastModifiedDate: Last modification time of the organization node in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifiedDate: str
        :param _CustomizedOrgNodeId: External ID of the organization node.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CustomizedOrgNodeId: str
        :param _ParentOrgNodeId: Parent node ID of the current organization node.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ParentOrgNodeId: str
        :param _OrgNodeId: Organization node ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeId: str
        :param _DataSource: Data source.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DataSource: str
        :param _CreatedDate: Organization node creation time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedDate: str
        :param _OrgNodeChildInfo: List of sub-nodes under the current organization node.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeChildInfo: list of OrgNodeChildInfo
        :param _Description: Organization node description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DisplayName = None
        self._LastModifiedDate = None
        self._CustomizedOrgNodeId = None
        self._ParentOrgNodeId = None
        self._OrgNodeId = None
        self._DataSource = None
        self._CreatedDate = None
        self._OrgNodeChildInfo = None
        self._Description = None
        self._RequestId = None

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def LastModifiedDate(self):
        return self._LastModifiedDate

    @LastModifiedDate.setter
    def LastModifiedDate(self, LastModifiedDate):
        self._LastModifiedDate = LastModifiedDate

    @property
    def CustomizedOrgNodeId(self):
        return self._CustomizedOrgNodeId

    @CustomizedOrgNodeId.setter
    def CustomizedOrgNodeId(self, CustomizedOrgNodeId):
        self._CustomizedOrgNodeId = CustomizedOrgNodeId

    @property
    def ParentOrgNodeId(self):
        return self._ParentOrgNodeId

    @ParentOrgNodeId.setter
    def ParentOrgNodeId(self, ParentOrgNodeId):
        self._ParentOrgNodeId = ParentOrgNodeId

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate

    @property
    def OrgNodeChildInfo(self):
        return self._OrgNodeChildInfo

    @OrgNodeChildInfo.setter
    def OrgNodeChildInfo(self, OrgNodeChildInfo):
        self._OrgNodeChildInfo = OrgNodeChildInfo

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._LastModifiedDate = params.get("LastModifiedDate")
        self._CustomizedOrgNodeId = params.get("CustomizedOrgNodeId")
        self._ParentOrgNodeId = params.get("ParentOrgNodeId")
        self._OrgNodeId = params.get("OrgNodeId")
        self._DataSource = params.get("DataSource")
        self._CreatedDate = params.get("CreatedDate")
        if params.get("OrgNodeChildInfo") is not None:
            self._OrgNodeChildInfo = []
            for item in params.get("OrgNodeChildInfo"):
                obj = OrgNodeChildInfo()
                obj._deserialize(item)
                self._OrgNodeChildInfo.append(obj)
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class DescribePublicKeyRequest(AbstractModel):
    """DescribePublicKey request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID, which is globally unique.
        :type ApplicationId: str
        """
        self._ApplicationId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicKeyResponse(AbstractModel):
    """DescribePublicKey response structure.

    """

    def __init__(self):
        r"""
        :param _PublicKey: Public key information used for JWT signature verification.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicKey: str
        :param _KeyId: JWT key ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyId: str
        :param _ApplicationId: Application ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PublicKey = None
        self._KeyId = None
        self._ApplicationId = None
        self._RequestId = None

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PublicKey = params.get("PublicKey")
        self._KeyId = params.get("KeyId")
        self._ApplicationId = params.get("ApplicationId")
        self._RequestId = params.get("RequestId")


class DescribeUserGroupRequest(AbstractModel):
    """DescribeUserGroup request structure.

    """

    def __init__(self):
        r"""
        :param _UserGroupId: User group ID, which is globally unique.
        :type UserGroupId: str
        """
        self._UserGroupId = None

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserGroupResponse(AbstractModel):
    """DescribeUserGroup response structure.

    """

    def __init__(self):
        r"""
        :param _DisplayName: User group nickname, which is not unique and can contain up to 64 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param _Description: User group remarks, which can contain up to 512 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _UserGroupId: User group ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DisplayName = None
        self._Description = None
        self._UserGroupId = None
        self._RequestId = None

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._UserGroupId = params.get("UserGroupId")
        self._RequestId = params.get("RequestId")


class DescribeUserInfoRequest(AbstractModel):
    """DescribeUserInfo request structure.

    """

    def __init__(self):
        r"""
        :param _UserName: Username, which can contain up to 64 characters. You need to specify at least `UserName` or `UserId`. If both are specified, `UserName` will be used first.
        :type UserName: str
        :param _UserId: User ID, which can contain up to 64 characters. You need to specify at least `UserName` or `UserId`. If both are specified, `UserName` will be used first.
        :type UserId: str
        """
        self._UserName = None
        self._UserId = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserInfoResponse(AbstractModel):
    """DescribeUserInfo response structure.

    """

    def __init__(self):
        r"""
        :param _UserName: Username.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _Status: User status. Valid values: NORMAL: normal; FREEZE: frozen; LOCKED: locked; NOT_ENABLED: disabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _DisplayName: Nickname
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param _Description: User remarks.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _UserGroupIds: List of IDs of the user's user groups.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupIds: list of str
        :param _UserId: User ID, which can contain up to 64 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param _Email: User's email address.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Email: str
        :param _Phone: User's mobile number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Phone: str
        :param _OrgNodeId: Unique ID of the user's primary organization.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeId: str
        :param _DataSource: Data source
Note: this field may return null, indicating that no valid values can be obtained.
        :type DataSource: str
        :param _ExpirationTime: User expiration time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpirationTime: str
        :param _ActivationTime: User activation time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ActivationTime: str
        :param _PwdNeedReset: Whether the password of the current user needs to be reset. `false` indicates no.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PwdNeedReset: bool
        :param _SecondaryOrgNodeIdList: List of IDs of the user's secondary organizations.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecondaryOrgNodeIdList: list of str
        :param _AdminFlag: Whether the user is an admin. Valid values: 0: no; 1: yes.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AdminFlag: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UserName = None
        self._Status = None
        self._DisplayName = None
        self._Description = None
        self._UserGroupIds = None
        self._UserId = None
        self._Email = None
        self._Phone = None
        self._OrgNodeId = None
        self._DataSource = None
        self._ExpirationTime = None
        self._ActivationTime = None
        self._PwdNeedReset = None
        self._SecondaryOrgNodeIdList = None
        self._AdminFlag = None
        self._RequestId = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UserGroupIds(self):
        return self._UserGroupIds

    @UserGroupIds.setter
    def UserGroupIds(self, UserGroupIds):
        self._UserGroupIds = UserGroupIds

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def ExpirationTime(self):
        return self._ExpirationTime

    @ExpirationTime.setter
    def ExpirationTime(self, ExpirationTime):
        self._ExpirationTime = ExpirationTime

    @property
    def ActivationTime(self):
        return self._ActivationTime

    @ActivationTime.setter
    def ActivationTime(self, ActivationTime):
        self._ActivationTime = ActivationTime

    @property
    def PwdNeedReset(self):
        return self._PwdNeedReset

    @PwdNeedReset.setter
    def PwdNeedReset(self, PwdNeedReset):
        self._PwdNeedReset = PwdNeedReset

    @property
    def SecondaryOrgNodeIdList(self):
        return self._SecondaryOrgNodeIdList

    @SecondaryOrgNodeIdList.setter
    def SecondaryOrgNodeIdList(self, SecondaryOrgNodeIdList):
        self._SecondaryOrgNodeIdList = SecondaryOrgNodeIdList

    @property
    def AdminFlag(self):
        return self._AdminFlag

    @AdminFlag.setter
    def AdminFlag(self, AdminFlag):
        self._AdminFlag = AdminFlag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Status = params.get("Status")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._UserGroupIds = params.get("UserGroupIds")
        self._UserId = params.get("UserId")
        self._Email = params.get("Email")
        self._Phone = params.get("Phone")
        self._OrgNodeId = params.get("OrgNodeId")
        self._DataSource = params.get("DataSource")
        self._ExpirationTime = params.get("ExpirationTime")
        self._ActivationTime = params.get("ActivationTime")
        self._PwdNeedReset = params.get("PwdNeedReset")
        self._SecondaryOrgNodeIdList = params.get("SecondaryOrgNodeIdList")
        self._AdminFlag = params.get("AdminFlag")
        self._RequestId = params.get("RequestId")


class DescribeUserResourcesAuthorizationRequest(AbstractModel):
    """DescribeUserResourcesAuthorization request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _UserId: User ID. You need to specify at least `UserName` or `UserId`. If both are specified, `UserName` will be used first.
        :type UserId: str
        :param _UserName: Username. You need to specify at least `UserName` or `UserId`. If both are specified, `UserName` will be used first.
        :type UserName: str
        :param _IncludeInheritedAuthorizations: Whether the query scope includes the application access of the user groups and organizations associated with the user. Valid values: false: no; true: yes. Default value: false.
        :type IncludeInheritedAuthorizations: bool
        """
        self._ApplicationId = None
        self._UserId = None
        self._UserName = None
        self._IncludeInheritedAuthorizations = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def IncludeInheritedAuthorizations(self):
        return self._IncludeInheritedAuthorizations

    @IncludeInheritedAuthorizations.setter
    def IncludeInheritedAuthorizations(self, IncludeInheritedAuthorizations):
        self._IncludeInheritedAuthorizations = IncludeInheritedAuthorizations


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._IncludeInheritedAuthorizations = params.get("IncludeInheritedAuthorizations")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserResourcesAuthorizationResponse(AbstractModel):
    """DescribeUserResourcesAuthorization response structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Unique application ID.
        :type ApplicationId: str
        :param _ApplicationAccounts: Application account.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationAccounts: list of str
        :param _UserId: Unique ID of the authorized user.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param _UserName: Username of the authorized user.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _AuthorizationUserResourceList: Returned resource list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthorizationUserResourceList: list of AuthorizationUserResouceInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApplicationId = None
        self._ApplicationAccounts = None
        self._UserId = None
        self._UserName = None
        self._AuthorizationUserResourceList = None
        self._RequestId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationAccounts(self):
        return self._ApplicationAccounts

    @ApplicationAccounts.setter
    def ApplicationAccounts(self, ApplicationAccounts):
        self._ApplicationAccounts = ApplicationAccounts

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def AuthorizationUserResourceList(self):
        return self._AuthorizationUserResourceList

    @AuthorizationUserResourceList.setter
    def AuthorizationUserResourceList(self, AuthorizationUserResourceList):
        self._AuthorizationUserResourceList = AuthorizationUserResourceList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationAccounts = params.get("ApplicationAccounts")
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        if params.get("AuthorizationUserResourceList") is not None:
            self._AuthorizationUserResourceList = []
            for item in params.get("AuthorizationUserResourceList"):
                obj = AuthorizationUserResouceInfo()
                obj._deserialize(item)
                self._AuthorizationUserResourceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserThirdPartyAccountInfoRequest(AbstractModel):
    """DescribeUserThirdPartyAccountInfo request structure.

    """

    def __init__(self):
        r"""
        :param _UserName: Username. You need to specify at least `Username` or `UserId`. If both are specified, `Username` will be used first.
        :type UserName: str
        :param _UserId: User ID. You need to specify at least `Username` or `UserId`. If both are specified, `Username` will be used first.
        :type UserId: str
        """
        self._UserName = None
        self._UserId = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserThirdPartyAccountInfoResponse(AbstractModel):
    """DescribeUserThirdPartyAccountInfo response structure.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID.
        :type UserId: str
        :param _UserName: Username.
        :type UserName: str
        :param _ThirdPartyAccounts: Third-Party account binding information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ThirdPartyAccounts: list of ThirdPartyAccountInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UserId = None
        self._UserName = None
        self._ThirdPartyAccounts = None
        self._RequestId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def ThirdPartyAccounts(self):
        return self._ThirdPartyAccounts

    @ThirdPartyAccounts.setter
    def ThirdPartyAccounts(self, ThirdPartyAccounts):
        self._ThirdPartyAccounts = ThirdPartyAccounts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        if params.get("ThirdPartyAccounts") is not None:
            self._ThirdPartyAccounts = []
            for item in params.get("ThirdPartyAccounts"):
                obj = ThirdPartyAccountInfo()
                obj._deserialize(item)
                self._ThirdPartyAccounts.append(obj)
        self._RequestId = params.get("RequestId")


class InheritedForm(AbstractModel):
    """Application information list.

    """

    def __init__(self):
        r"""
        :param _UserGroupIds: List of IDs of the user's user groups.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupIds: list of str
        :param _OrgNodeIds: List of IDs of the user's organization nodes.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeIds: list of str
        """
        self._UserGroupIds = None
        self._OrgNodeIds = None

    @property
    def UserGroupIds(self):
        return self._UserGroupIds

    @UserGroupIds.setter
    def UserGroupIds(self, UserGroupIds):
        self._UserGroupIds = UserGroupIds

    @property
    def OrgNodeIds(self):
        return self._OrgNodeIds

    @OrgNodeIds.setter
    def OrgNodeIds(self, OrgNodeIds):
        self._OrgNodeIds = OrgNodeIds


    def _deserialize(self, params):
        self._UserGroupIds = params.get("UserGroupIds")
        self._OrgNodeIds = params.get("OrgNodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkUserInfo(AbstractModel):
    """User information associated with the account

    """

    def __init__(self):
        r"""
        :param _UserId: User ID, which is globally unique and can contain up to 64 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param _UserName: Username.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        """
        self._UserId = None
        self._UserName = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccountInAccountGroupRequest(AbstractModel):
    """ListAccountInAccountGroup request structure.

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: Account group ID.
        :type AccountGroupId: str
        :param _SearchCondition: Search criterion. You can combine multiple search criteria and search in multiple data ranges.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.AccountGroupSearchCriteria`
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._AccountGroupId = None
        self._SearchCondition = None
        self._Offset = None
        self._Limit = None

    @property
    def AccountGroupId(self):
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

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
        self._AccountGroupId = params.get("AccountGroupId")
        if params.get("SearchCondition") is not None:
            self._SearchCondition = AccountGroupSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccountInAccountGroupResponse(AbstractModel):
    """ListAccountInAccountGroup response structure.

    """

    def __init__(self):
        r"""
        :param _AccountList: List of accounts returned for the query.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccountList: list of AppAccountInfo
        :param _TotalCount: Total number of accounts returned for the query.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _AccountGroupId: Account group ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccountGroupId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccountList = None
        self._TotalCount = None
        self._AccountGroupId = None
        self._RequestId = None

    @property
    def AccountList(self):
        return self._AccountList

    @AccountList.setter
    def AccountList(self, AccountList):
        self._AccountList = AccountList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccountGroupId(self):
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccountList") is not None:
            self._AccountList = []
            for item in params.get("AccountList"):
                obj = AppAccountInfo()
                obj._deserialize(item)
                self._AccountList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._AccountGroupId = params.get("AccountGroupId")
        self._RequestId = params.get("RequestId")


class ListApplicationAuthorizationsRequest(AbstractModel):
    """ListApplicationAuthorizations request structure.

    """

    def __init__(self):
        r"""
        :param _EntityType: Query type. Valid values: User: user; UserGroup: user group; OrgNode: organization.
        :type EntityType: str
        :param _SearchCondition: Search criterion. You can combine multiple search criteria and search in multiple data ranges. In addition, multiple query methods such as full match, partial match, and range match are supported. Specifically, double quotation marks ("") indicate full match, an asterisk (*) at the end of the field indicates partial match, and an empty field indicates to query the full table by default.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.AuthorizationInfoSearchCriteria`
        :param _Sort: Set of sort criteria. You can sort the results by last modification time (lastModifiedDate). If this field is left empty, the results will be sorted in alphabetical order by application name.
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param _Offset: Pagination offset. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated.
        :type Offset: int
        :param _Limit: Number of results read per page. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated.
        :type Limit: int
        """
        self._EntityType = None
        self._SearchCondition = None
        self._Sort = None
        self._Offset = None
        self._Limit = None

    @property
    def EntityType(self):
        return self._EntityType

    @EntityType.setter
    def EntityType(self, EntityType):
        self._EntityType = EntityType

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

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
        self._EntityType = params.get("EntityType")
        if params.get("SearchCondition") is not None:
            self._SearchCondition = AuthorizationInfoSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self._Sort = SortCondition()
            self._Sort._deserialize(params.get("Sort"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListApplicationAuthorizationsResponse(AbstractModel):
    """ListApplicationAuthorizations response structure.

    """

    def __init__(self):
        r"""
        :param _AuthorizationInfoList: Returned list of application authorization information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthorizationInfoList: list of AuthorizationInfo
        :param _TotalCount: Total number of returned application information items.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AuthorizationInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AuthorizationInfoList(self):
        return self._AuthorizationInfoList

    @AuthorizationInfoList.setter
    def AuthorizationInfoList(self, AuthorizationInfoList):
        self._AuthorizationInfoList = AuthorizationInfoList

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
        if params.get("AuthorizationInfoList") is not None:
            self._AuthorizationInfoList = []
            for item in params.get("AuthorizationInfoList"):
                obj = AuthorizationInfo()
                obj._deserialize(item)
                self._AuthorizationInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListApplicationsRequest(AbstractModel):
    """ListApplications request structure.

    """

    def __init__(self):
        r"""
        :param _SearchCondition: Fuzzy match search criterion. You can combine multiple search criteria and search in multiple data ranges. In addition, multiple query methods such as full match, partial match, and range match are supported. Specifically, double quotation marks ("") indicate full match, and an asterisk (*) at the end of the field indicates partial match. The fuzzy match search feature and the exact match query feature will not take effect at the same time. If both `SearchCondition` and `ApplicationIdList` are specified, `ApplicationIdList` will take effect by default for exact match query; otherwise, the information of all applications will be returned by default.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.ApplicationInfoSearchCriteria`
        :param _Sort: Set of sort criteria. Valid values: DisplayName: application name; CreatedDate: creation time; LastModifiedDate: last modification time. If this field is left empty, the results will be sorted in alphabetical order by application name.
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param _Offset: Set of sort criteria. Valid values: DisplayName: application name; CreatedDate: creation time; LastModifiedDate: last modification time. If this field is left empty, the results will be sorted in alphabetical order by application name.
        :type Offset: int
        :param _Limit: Number of results read per page. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated.
        :type Limit: int
        :param _ApplicationIdList: Application ID list, through which the corresponding application information will be matched exactly. The fuzzy match search feature and the exact match query feature will not take effect at the same time. If both `SearchCondition` and `ApplicationIdList` are specified, `ApplicationIdList` will take effect by default for exact match query; otherwise, the information of all applications will be returned by default.
        :type ApplicationIdList: list of str
        """
        self._SearchCondition = None
        self._Sort = None
        self._Offset = None
        self._Limit = None
        self._ApplicationIdList = None

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

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
    def ApplicationIdList(self):
        return self._ApplicationIdList

    @ApplicationIdList.setter
    def ApplicationIdList(self, ApplicationIdList):
        self._ApplicationIdList = ApplicationIdList


    def _deserialize(self, params):
        if params.get("SearchCondition") is not None:
            self._SearchCondition = ApplicationInfoSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self._Sort = SortCondition()
            self._Sort._deserialize(params.get("Sort"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ApplicationIdList = params.get("ApplicationIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListApplicationsResponse(AbstractModel):
    """ListApplications response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of returned application information items.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _ApplicationInfoList: Returned application information list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationInfoList: list of ApplicationInformation
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ApplicationInfoList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApplicationInfoList(self):
        return self._ApplicationInfoList

    @ApplicationInfoList.setter
    def ApplicationInfoList(self, ApplicationInfoList):
        self._ApplicationInfoList = ApplicationInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApplicationInfoList") is not None:
            self._ApplicationInfoList = []
            for item in params.get("ApplicationInfoList"):
                obj = ApplicationInformation()
                obj._deserialize(item)
                self._ApplicationInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class ListAuthorizedApplicationsToOrgNodeRequest(AbstractModel):
    """ListAuthorizedApplicationsToOrgNode request structure.

    """

    def __init__(self):
        r"""
        :param _OrgNodeId: Organization node ID.
        :type OrgNodeId: str
        """
        self._OrgNodeId = None

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId


    def _deserialize(self, params):
        self._OrgNodeId = params.get("OrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAuthorizedApplicationsToOrgNodeResponse(AbstractModel):
    """ListAuthorizedApplicationsToOrgNode response structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationIds: List of IDs of the applications accessible to the organization node.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApplicationIds = None
        self._RequestId = None

    @property
    def ApplicationIds(self):
        return self._ApplicationIds

    @ApplicationIds.setter
    def ApplicationIds(self, ApplicationIds):
        self._ApplicationIds = ApplicationIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ApplicationIds = params.get("ApplicationIds")
        self._RequestId = params.get("RequestId")


class ListAuthorizedApplicationsToUserGroupRequest(AbstractModel):
    """ListAuthorizedApplicationsToUserGroup request structure.

    """

    def __init__(self):
        r"""
        :param _UserGroupId: User group ID.
        :type UserGroupId: str
        """
        self._UserGroupId = None

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAuthorizedApplicationsToUserGroupResponse(AbstractModel):
    """ListAuthorizedApplicationsToUserGroup response structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationIds: List of IDs of the applications accessible to the user group.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApplicationIds = None
        self._RequestId = None

    @property
    def ApplicationIds(self):
        return self._ApplicationIds

    @ApplicationIds.setter
    def ApplicationIds(self, ApplicationIds):
        self._ApplicationIds = ApplicationIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ApplicationIds = params.get("ApplicationIds")
        self._RequestId = params.get("RequestId")


class ListAuthorizedApplicationsToUserRequest(AbstractModel):
    """ListAuthorizedApplicationsToUser request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID.
        :type UserId: str
        :param _IncludeInheritedAuthorizations: Whether the query scope includes the application access of the user groups and organizations associated with the user. Valid values: false: no; true: yes. Default value: false.
        :type IncludeInheritedAuthorizations: bool
        """
        self._UserId = None
        self._IncludeInheritedAuthorizations = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def IncludeInheritedAuthorizations(self):
        return self._IncludeInheritedAuthorizations

    @IncludeInheritedAuthorizations.setter
    def IncludeInheritedAuthorizations(self, IncludeInheritedAuthorizations):
        self._IncludeInheritedAuthorizations = IncludeInheritedAuthorizations


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._IncludeInheritedAuthorizations = params.get("IncludeInheritedAuthorizations")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAuthorizedApplicationsToUserResponse(AbstractModel):
    """ListAuthorizedApplicationsToUser response structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationAuthorizationInfo: List of information of the applications accessible to the user.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationAuthorizationInfo: list of ApplicationAuthorizationInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApplicationAuthorizationInfo = None
        self._RequestId = None

    @property
    def ApplicationAuthorizationInfo(self):
        return self._ApplicationAuthorizationInfo

    @ApplicationAuthorizationInfo.setter
    def ApplicationAuthorizationInfo(self, ApplicationAuthorizationInfo):
        self._ApplicationAuthorizationInfo = ApplicationAuthorizationInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ApplicationAuthorizationInfo") is not None:
            self._ApplicationAuthorizationInfo = []
            for item in params.get("ApplicationAuthorizationInfo"):
                obj = ApplicationAuthorizationInfo()
                obj._deserialize(item)
                self._ApplicationAuthorizationInfo.append(obj)
        self._RequestId = params.get("RequestId")


class ListUserGroupsOfUserRequest(AbstractModel):
    """ListUserGroupsOfUser request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID, which is globally unique.
        :type UserId: str
        :param _SearchCondition: Fuzzy search criterion. You can search by user group name (DisplayName). If this field is left empty, all of the user's user groups will be displayed by default.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.UserGroupInformationSearchCriteria`
        :param _Sort: Set of sort criteria. Valid values: DisplayName: user group name; UserGroupId: user group ID; CreatedDate: creation time. If this field is left empty, the results will be sorted in alphabetical order by user group name.
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param _Offset: Pagination offset. Default value: 0. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated, and up to 50 user groups will be returned.
        :type Offset: int
        :param _Limit: Number of results read per page. Default value: 50. Maximum value: 100. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated, and up to 50 user groups will be returned.
        :type Limit: int
        """
        self._UserId = None
        self._SearchCondition = None
        self._Sort = None
        self._Offset = None
        self._Limit = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

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
        self._UserId = params.get("UserId")
        if params.get("SearchCondition") is not None:
            self._SearchCondition = UserGroupInformationSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self._Sort = SortCondition()
            self._Sort._deserialize(params.get("Sort"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserGroupsOfUserResponse(AbstractModel):
    """ListUserGroupsOfUser response structure.

    """

    def __init__(self):
        r"""
        :param _UserGroupIds: List of IDs of the user's user groups.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupIds: list of str
        :param _UserId: User ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param _UserGroupInfoList: List of information of the user's user groups.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupInfoList: list of UserGroupInfo
        :param _TotalCount: Total number of returned user group information items.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UserGroupIds = None
        self._UserId = None
        self._UserGroupInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def UserGroupIds(self):
        return self._UserGroupIds

    @UserGroupIds.setter
    def UserGroupIds(self, UserGroupIds):
        self._UserGroupIds = UserGroupIds

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserGroupInfoList(self):
        return self._UserGroupInfoList

    @UserGroupInfoList.setter
    def UserGroupInfoList(self, UserGroupInfoList):
        self._UserGroupInfoList = UserGroupInfoList

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
        self._UserGroupIds = params.get("UserGroupIds")
        self._UserId = params.get("UserId")
        if params.get("UserGroupInfoList") is not None:
            self._UserGroupInfoList = []
            for item in params.get("UserGroupInfoList"):
                obj = UserGroupInfo()
                obj._deserialize(item)
                self._UserGroupInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListUserGroupsRequest(AbstractModel):
    """ListUserGroups request structure.

    """

    def __init__(self):
        r"""
        :param _SearchCondition: Search criterion. You can combine multiple search criteria and search in multiple data ranges. In addition, multiple query methods such as full match, partial match, and range match are supported. Specifically, double quotation marks ("") indicate full match, an asterisk (*) at the end of the field indicates partial match, and an empty field indicates to query the full table by default.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.UserGroupInfoSearchCriteria`
        :param _Sort: Set of sort criteria. The supported attributes for sorting include user group name (DisplayName), user group ID (UserGroupId), and last modification time (LastModifiedDate). If this field is left empty, the results will be sorted in alphabetical order by user group name.
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param _Offset: Pagination offset. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated.
        :type Offset: int
        :param _Limit: Number of results read per page. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated.
        :type Limit: int
        """
        self._SearchCondition = None
        self._Sort = None
        self._Offset = None
        self._Limit = None

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

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
        if params.get("SearchCondition") is not None:
            self._SearchCondition = UserGroupInfoSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self._Sort = SortCondition()
            self._Sort._deserialize(params.get("Sort"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserGroupsResponse(AbstractModel):
    """ListUserGroups response structure.

    """

    def __init__(self):
        r"""
        :param _UserGroupList: Returned user group list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupList: list of UserGroupInformation
        :param _TotalCount: Total number of returned user group information items.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UserGroupList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def UserGroupList(self):
        return self._UserGroupList

    @UserGroupList.setter
    def UserGroupList(self, UserGroupList):
        self._UserGroupList = UserGroupList

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
        if params.get("UserGroupList") is not None:
            self._UserGroupList = []
            for item in params.get("UserGroupList"):
                obj = UserGroupInformation()
                obj._deserialize(item)
                self._UserGroupList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListUsersInOrgNodeRequest(AbstractModel):
    """ListUsersInOrgNode request structure.

    """

    def __init__(self):
        r"""
        :param _OrgNodeId: Organization node ID, which is globally unique and can contain up to 64 characters. If this parameter is left empty, the user information under the root organization node will be read by default.
        :type OrgNodeId: str
        :param _IncludeOrgNodeChildInfo: Whether to read the information of its sub-nodes. When this parameter is left empty or specified as `false`, only the information of the current organization node will be read by default. When it is specified as `true`, the information of the current organization node and its level-1 sub-nodes will be read.
        :type IncludeOrgNodeChildInfo: bool
        :param _SearchCondition: User attribute search criterion. The supported search criteria include username, mobile number, email address, user locking status, user freezing status, creation time, and last modification time, which can also be combined. In addition, multiple query methods such as full match, partial match, and range match are supported. Specifically, double quotation marks ("") indicate full match, an asterisk (*) at the end of the field indicates partial match, brackets separated by a comma ([Min,Max]) indicate query within a closed interval, braces separated by a comma ({Min,Max}) indicate query within an open interval, and a bracket and a brace can be used together (for example, {Min,Max] indicates that the minimum value is excluded and the maximum value is included in the query). Range query supports using an asterisk (for example, {20,*] indicates an interval including all data greater than 20) and querying by time period. The supported attributes include creation time (CreationTime) and last modification time (LastUpdateTime) in ISO 8601 format, such as `2021-01-13T09:44:07.182+0000`.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.ListUsersInOrgNodeSearchCriteria`
        :param _Sort: Set of sort criteria. The supported attributes for sorting include username (UserName), mobile number (Phone), email address (Email), user status (Status), creation time (CreatedDate), and last modification time (LastModifiedDate). If this field is left empty, the results will be sorted in alphabetical order by nickname (DisplayName).
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param _Offset: Pagination offset. Default value: 0. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated, and up to 50 users will be returned.
        :type Offset: int
        :param _Limit: Number of results read per page. Default value: 50. Maximum value: 100. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated, and up to 50 users will be returned.
        :type Limit: int
        """
        self._OrgNodeId = None
        self._IncludeOrgNodeChildInfo = None
        self._SearchCondition = None
        self._Sort = None
        self._Offset = None
        self._Limit = None

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def IncludeOrgNodeChildInfo(self):
        return self._IncludeOrgNodeChildInfo

    @IncludeOrgNodeChildInfo.setter
    def IncludeOrgNodeChildInfo(self, IncludeOrgNodeChildInfo):
        self._IncludeOrgNodeChildInfo = IncludeOrgNodeChildInfo

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

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
        self._OrgNodeId = params.get("OrgNodeId")
        self._IncludeOrgNodeChildInfo = params.get("IncludeOrgNodeChildInfo")
        if params.get("SearchCondition") is not None:
            self._SearchCondition = ListUsersInOrgNodeSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self._Sort = SortCondition()
            self._Sort._deserialize(params.get("Sort"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersInOrgNodeResponse(AbstractModel):
    """ListUsersInOrgNode response structure.

    """

    def __init__(self):
        r"""
        :param _OrgNodeChildUserInfo: User information list under the organization sub-node.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeChildUserInfo: list of OrgNodeChildUserInfo
        :param _OrgNodeId: Organization node ID, which is globally unique and can contain up to 64 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeId: str
        :param _UserInfo: User information list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserInfo: list of UserInfo
        :param _TotalUserNum: Total number of users under the current organization node.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalUserNum: int
        :param _OrgNodeIdPath: Organization ID path.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeIdPath: str
        :param _OrgNodeNamePath: Organization name path.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeNamePath: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OrgNodeChildUserInfo = None
        self._OrgNodeId = None
        self._UserInfo = None
        self._TotalUserNum = None
        self._OrgNodeIdPath = None
        self._OrgNodeNamePath = None
        self._RequestId = None

    @property
    def OrgNodeChildUserInfo(self):
        return self._OrgNodeChildUserInfo

    @OrgNodeChildUserInfo.setter
    def OrgNodeChildUserInfo(self, OrgNodeChildUserInfo):
        self._OrgNodeChildUserInfo = OrgNodeChildUserInfo

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def TotalUserNum(self):
        return self._TotalUserNum

    @TotalUserNum.setter
    def TotalUserNum(self, TotalUserNum):
        self._TotalUserNum = TotalUserNum

    @property
    def OrgNodeIdPath(self):
        return self._OrgNodeIdPath

    @OrgNodeIdPath.setter
    def OrgNodeIdPath(self, OrgNodeIdPath):
        self._OrgNodeIdPath = OrgNodeIdPath

    @property
    def OrgNodeNamePath(self):
        return self._OrgNodeNamePath

    @OrgNodeNamePath.setter
    def OrgNodeNamePath(self, OrgNodeNamePath):
        self._OrgNodeNamePath = OrgNodeNamePath

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("OrgNodeChildUserInfo") is not None:
            self._OrgNodeChildUserInfo = []
            for item in params.get("OrgNodeChildUserInfo"):
                obj = OrgNodeChildUserInfo()
                obj._deserialize(item)
                self._OrgNodeChildUserInfo.append(obj)
        self._OrgNodeId = params.get("OrgNodeId")
        if params.get("UserInfo") is not None:
            self._UserInfo = []
            for item in params.get("UserInfo"):
                obj = UserInfo()
                obj._deserialize(item)
                self._UserInfo.append(obj)
        self._TotalUserNum = params.get("TotalUserNum")
        self._OrgNodeIdPath = params.get("OrgNodeIdPath")
        self._OrgNodeNamePath = params.get("OrgNodeNamePath")
        self._RequestId = params.get("RequestId")


class ListUsersInOrgNodeSearchCriteria(AbstractModel):
    """Displays user attribute search criteria under the organization.

    """

    def __init__(self):
        r"""
        :param _UserName: Username, which can contain up to 64 characters.
        :type UserName: str
        :param _Phone: User's mobile number.
        :type Phone: str
        :param _Email: User's email address.
        :type Email: str
        :param _Status: User status. Valid values: NORMAL: normal; FREEZE: frozen; LOCKED: locked; NOT_ENABLED: disabled.
        :type Status: str
        :param _CreationTime: User creation time in ISO 8601 format.
        :type CreationTime: str
        :param _LastUpdateTime: Last update time of the user.
        :type LastUpdateTime: str
        :param _Keyword: Search by name. The match criteria include username and user's mobile number.
        :type Keyword: str
        """
        self._UserName = None
        self._Phone = None
        self._Email = None
        self._Status = None
        self._CreationTime = None
        self._LastUpdateTime = None
        self._Keyword = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def LastUpdateTime(self):
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._Status = params.get("Status")
        self._CreationTime = params.get("CreationTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersInUserGroupRequest(AbstractModel):
    """ListUsersInUserGroup request structure.

    """

    def __init__(self):
        r"""
        :param _UserGroupId: User group ID, which is globally unique.
        :type UserGroupId: str
        :param _SearchCondition: User attribute search criterion. The supported search criteria include username, mobile number, email address, user locking status, user freezing status, creation time, and last modification time, which can also be combined. In addition, multiple query methods such as full match, partial match, and range match are supported. Specifically, double quotation marks ("") indicate full match, an asterisk (*) at the end of the field indicates partial match, brackets separated by a comma ([Min,Max]) indicate query within a closed interval, braces separated by a comma ({Min,Max}) indicate query within an open interval, and a bracket and a brace can be used together (for example, {Min,Max] indicates that the minimum value is excluded and the maximum value is included in the query). Range query supports using an asterisk (for example, {20,*] indicates an interval including all data greater than 20) and querying by time period. The supported attributes include creation time (CreationTime) and last modification time (LastUpdateTime) in ISO 8601 format, such as `2021-01-13T09:44:07.182+0000`.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.UserSearchCriteria`
        :param _Sort: Set of sort criteria. The supported attributes for sorting include username (UserName), nickname (DisplayName), mobile number (Phone), email address (Email), user status (Status), creation time (CreatedDate), and last modification time (LastModifiedDate). If this field is left empty, the results will be sorted in alphabetical order by nickname (DisplayName).
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param _Offset: Pagination offset. Default value: 0. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated, and up to 50 users will be returned.
        :type Offset: int
        :param _Limit: Number of results read per page. Default value: 50. Maximum value: 100. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated, and up to 50 users will be returned.
        :type Limit: int
        """
        self._UserGroupId = None
        self._SearchCondition = None
        self._Sort = None
        self._Offset = None
        self._Limit = None

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

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
        self._UserGroupId = params.get("UserGroupId")
        if params.get("SearchCondition") is not None:
            self._SearchCondition = UserSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self._Sort = SortCondition()
            self._Sort._deserialize(params.get("Sort"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersInUserGroupResponse(AbstractModel):
    """ListUsersInUserGroup response structure.

    """

    def __init__(self):
        r"""
        :param _UserGroupId: User group ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupId: str
        :param _UserInfo: Returned user information list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserInfo: list of UserInfo
        :param _TotalNum: Total number of returned user information items.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalNum: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UserGroupId = None
        self._UserInfo = None
        self._TotalNum = None
        self._RequestId = None

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        if params.get("UserInfo") is not None:
            self._UserInfo = []
            for item in params.get("UserInfo"):
                obj = UserInfo()
                obj._deserialize(item)
                self._UserInfo.append(obj)
        self._TotalNum = params.get("TotalNum")
        self._RequestId = params.get("RequestId")


class ListUsersRequest(AbstractModel):
    """ListUsers request structure.

    """

    def __init__(self):
        r"""
        :param _SearchCondition: User attribute search criterion. The supported search criteria include username, mobile number, email address, user locking status, user freezing status, creation time, and last modification time, which can also be combined. In addition, multiple query methods such as full match, partial match, and range match are supported. Specifically, double quotation marks ("") indicate full match, an asterisk (*) at the end of the field indicates partial match, brackets separated by a comma ([Min,Max]) indicate query within a closed interval, braces separated by a comma ({Min,Max}) indicate query within an open interval, and a bracket and a brace can be used together (for example, {Min,Max] indicates that the minimum value is excluded and the maximum value is included in the query). Range query supports using an asterisk (for example, {20,*] indicates an interval including all data greater than 20) and querying by time period. The supported attributes include creation time (CreationTime) and last modification time (LastUpdateTime) in ISO 8601 format, such as `2021-01-13T09:44:07.182+0000`.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.UserSearchCriteria`
        :param _ExpectedFields: User attributes expected to be returned. All built-in user attributes will be returned by default, including user UUID (UserId), nickname (DisplayName), username (UserName), mobile number (Phone), email address (Email), status (Status), user group (SubjectGroups), organization path (OrgPath), remarks (Description), creation time (CreationTime), last modification time (LastUpdateTime), and last login time (LastLoginTime).
        :type ExpectedFields: list of str
        :param _Sort: Set of sort criteria. The supported attributes for sorting include username (UserName), nickname (DisplayName), mobile number (Phone), email address (Email), user status (Status), creation time (CreatedDate), last modification time (LastUpdateTime), and last login time (LastLoginTime). If this field is left empty, the results will be sorted in alphabetical order by nickname (DisplayName).
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param _Offset: Pagination offset. Default value: 0. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated, and up to 1,000 users will be returned.
        :type Offset: int
        :param _Limit: Number of results read per page. Default value: 50. Maximum value: 100. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated, and up to 1,000 users will be returned.
        :type Limit: int
        :param _IncludeTotal: Whether to view the total number of search results. Default value: false (no).
        :type IncludeTotal: bool
        """
        self._SearchCondition = None
        self._ExpectedFields = None
        self._Sort = None
        self._Offset = None
        self._Limit = None
        self._IncludeTotal = None

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

    @property
    def ExpectedFields(self):
        return self._ExpectedFields

    @ExpectedFields.setter
    def ExpectedFields(self, ExpectedFields):
        self._ExpectedFields = ExpectedFields

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

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
    def IncludeTotal(self):
        return self._IncludeTotal

    @IncludeTotal.setter
    def IncludeTotal(self, IncludeTotal):
        self._IncludeTotal = IncludeTotal


    def _deserialize(self, params):
        if params.get("SearchCondition") is not None:
            self._SearchCondition = UserSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        self._ExpectedFields = params.get("ExpectedFields")
        if params.get("Sort") is not None:
            self._Sort = SortCondition()
            self._Sort._deserialize(params.get("Sort"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._IncludeTotal = params.get("IncludeTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersResponse(AbstractModel):
    """ListUsers response structure.

    """

    def __init__(self):
        r"""
        :param _UserList: List of users returned for the query.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserList: list of UserInformation
        :param _TotalCount: Total number of users returned for the query, which will be returned only when the `IncludeTotal` input parameter is set to `true`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UserList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def UserList(self):
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

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
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self._UserList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ModifyAccountGroupRequest(AbstractModel):
    """ModifyAccountGroup request structure.

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: Account group ID.
        :type AccountGroupId: str
        :param _GroupName: Account group name. When this parameter is not specified, the name will not be modified.
        :type GroupName: str
        :param _Description: Description. When this parameter is not specified, the description will not be modified.
        :type Description: str
        """
        self._AccountGroupId = None
        self._GroupName = None
        self._Description = None

    @property
    def AccountGroupId(self):
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._AccountGroupId = params.get("AccountGroupId")
        self._GroupName = params.get("GroupName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountGroupResponse(AbstractModel):
    """ModifyAccountGroup response structure.

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


class ModifyAppAccountRequest(AbstractModel):
    """ModifyAppAccount request structure.

    """

    def __init__(self):
        r"""
        :param _AccountId: Account ID.
        :type AccountId: str
        :param _AccountName: Account name. When this parameter is not specified, the name will not be modified.
        :type AccountName: str
        :param _Password: Account password. When this parameter is not specified, the password will not be changed.
        :type Password: str
        :param _Description: Description. When this parameter is not specified, the description will not be modified.
        :type Description: str
        """
        self._AccountId = None
        self._AccountName = None
        self._Password = None
        self._Description = None

    @property
    def AccountId(self):
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._AccountId = params.get("AccountId")
        self._AccountName = params.get("AccountName")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppAccountResponse(AbstractModel):
    """ModifyAppAccount response structure.

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


class ModifyApplicationRequest(AbstractModel):
    """ModifyApplication request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID, which is globally unique.
        :type ApplicationId: str
        :param _SecureLevel: Security level.
        :type SecureLevel: str
        :param _DisplayName: Displayed application name, which can contain up to 32 characters and is the same as the application name by default.
        :type DisplayName: str
        :param _AppStatus: Application status. Valid values: true: enabled; false: disabled.
        :type AppStatus: bool
        :param _IconUrl: Access address of the application icon image.
        :type IconUrl: str
        :param _Description: Description, which can contain up to 128 characters.
        :type Description: str
        """
        self._ApplicationId = None
        self._SecureLevel = None
        self._DisplayName = None
        self._AppStatus = None
        self._IconUrl = None
        self._Description = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def SecureLevel(self):
        return self._SecureLevel

    @SecureLevel.setter
    def SecureLevel(self, SecureLevel):
        self._SecureLevel = SecureLevel

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def AppStatus(self):
        return self._AppStatus

    @AppStatus.setter
    def AppStatus(self, AppStatus):
        self._AppStatus = AppStatus

    @property
    def IconUrl(self):
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._SecureLevel = params.get("SecureLevel")
        self._DisplayName = params.get("DisplayName")
        self._AppStatus = params.get("AppStatus")
        self._IconUrl = params.get("IconUrl")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationResponse(AbstractModel):
    """ModifyApplication response structure.

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


class ModifyUserInfoRequest(AbstractModel):
    """ModifyUserInfo request structure.

    """

    def __init__(self):
        r"""
        :param _UserName: Username, which can contain up to 32 characters. You need to select either `Username` or `UserId` as the search criterion; if both are selected, `Username` will be used by default.
        :type UserName: str
        :param _DisplayName: Nickname, which can contain up to 64 characters and is the same as the username by default.
        :type DisplayName: str
        :param _Description: User remarks, which can contain up to 512 characters.
        :type Description: str
        :param _UserGroupIds: List of IDs of the user's user groups.
        :type UserGroupIds: list of str
        :param _UserId: User ID. You need to select either `UserName` or `UserId` as the search criterion. If both are selected, `UserName` will be used by default.
        :type UserId: str
        :param _Phone: User's mobile number.
        :type Phone: str
        :param _ExpirationTime: User expiration time in ISO 8601 format.
        :type ExpirationTime: str
        :param _Password: User password, which needs to be configured according to the password policy.
        :type Password: str
        :param _Email: User's email address.
        :type Email: str
        :param _PwdNeedReset: Whether the password needs to be reset. Default value: false (no).
        :type PwdNeedReset: bool
        :param _OrgNodeId: Unique ID of the user's primary organization. If this parameter is left empty, the user will be created under the root node by default.
        :type OrgNodeId: str
        :param _SecondaryOrgNodeIdList: List of IDs of the user's secondary organizations.
        :type SecondaryOrgNodeIdList: list of str
        """
        self._UserName = None
        self._DisplayName = None
        self._Description = None
        self._UserGroupIds = None
        self._UserId = None
        self._Phone = None
        self._ExpirationTime = None
        self._Password = None
        self._Email = None
        self._PwdNeedReset = None
        self._OrgNodeId = None
        self._SecondaryOrgNodeIdList = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UserGroupIds(self):
        return self._UserGroupIds

    @UserGroupIds.setter
    def UserGroupIds(self, UserGroupIds):
        self._UserGroupIds = UserGroupIds

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def ExpirationTime(self):
        return self._ExpirationTime

    @ExpirationTime.setter
    def ExpirationTime(self, ExpirationTime):
        self._ExpirationTime = ExpirationTime

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def PwdNeedReset(self):
        return self._PwdNeedReset

    @PwdNeedReset.setter
    def PwdNeedReset(self, PwdNeedReset):
        self._PwdNeedReset = PwdNeedReset

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def SecondaryOrgNodeIdList(self):
        return self._SecondaryOrgNodeIdList

    @SecondaryOrgNodeIdList.setter
    def SecondaryOrgNodeIdList(self, SecondaryOrgNodeIdList):
        self._SecondaryOrgNodeIdList = SecondaryOrgNodeIdList


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._UserGroupIds = params.get("UserGroupIds")
        self._UserId = params.get("UserId")
        self._Phone = params.get("Phone")
        self._ExpirationTime = params.get("ExpirationTime")
        self._Password = params.get("Password")
        self._Email = params.get("Email")
        self._PwdNeedReset = params.get("PwdNeedReset")
        self._OrgNodeId = params.get("OrgNodeId")
        self._SecondaryOrgNodeIdList = params.get("SecondaryOrgNodeIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserInfoResponse(AbstractModel):
    """ModifyUserInfo response structure.

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


class OrgNodeChildInfo(AbstractModel):
    """List of sub-nodes under the current organization node

    """

    def __init__(self):
        r"""
        :param _DisplayName: Displayed organization node name, which can contain up to 64 characters and is the same as the organization name by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param _LastModifiedDate: Last modification time of the organization node in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifiedDate: str
        :param _CustomizedOrgNodeId: External ID of the organization node, which is optional and customizable.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CustomizedOrgNodeId: str
        :param _ParentOrgNodeId: Parent node ID of the current organization node.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ParentOrgNodeId: str
        :param _OrgNodeId: Organization node ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeId: str
        :param _DataSource: Data source.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DataSource: str
        :param _CreatedDate: Organization node creation time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedDate: str
        :param _Description: Organization node description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        """
        self._DisplayName = None
        self._LastModifiedDate = None
        self._CustomizedOrgNodeId = None
        self._ParentOrgNodeId = None
        self._OrgNodeId = None
        self._DataSource = None
        self._CreatedDate = None
        self._Description = None

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def LastModifiedDate(self):
        return self._LastModifiedDate

    @LastModifiedDate.setter
    def LastModifiedDate(self, LastModifiedDate):
        self._LastModifiedDate = LastModifiedDate

    @property
    def CustomizedOrgNodeId(self):
        return self._CustomizedOrgNodeId

    @CustomizedOrgNodeId.setter
    def CustomizedOrgNodeId(self, CustomizedOrgNodeId):
        self._CustomizedOrgNodeId = CustomizedOrgNodeId

    @property
    def ParentOrgNodeId(self):
        return self._ParentOrgNodeId

    @ParentOrgNodeId.setter
    def ParentOrgNodeId(self, ParentOrgNodeId):
        self._ParentOrgNodeId = ParentOrgNodeId

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._LastModifiedDate = params.get("LastModifiedDate")
        self._CustomizedOrgNodeId = params.get("CustomizedOrgNodeId")
        self._ParentOrgNodeId = params.get("ParentOrgNodeId")
        self._OrgNodeId = params.get("OrgNodeId")
        self._DataSource = params.get("DataSource")
        self._CreatedDate = params.get("CreatedDate")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgNodeChildUserInfo(AbstractModel):
    """User information list under the organization sub-node

    """

    def __init__(self):
        r"""
        :param _OrgNodeId: Organization node ID, which is globally unique and can contain up to 64 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeId: str
        :param _UserInfo: User information list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserInfo: list of UserInfo
        :param _TotalUserNum: Total number of users under the current organization node.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalUserNum: int
        :param _OrgNodeIdPath: Organization ID path.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeIdPath: str
        :param _OrgNodeNamePath: Organization name path.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeNamePath: str
        """
        self._OrgNodeId = None
        self._UserInfo = None
        self._TotalUserNum = None
        self._OrgNodeIdPath = None
        self._OrgNodeNamePath = None

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def TotalUserNum(self):
        return self._TotalUserNum

    @TotalUserNum.setter
    def TotalUserNum(self, TotalUserNum):
        self._TotalUserNum = TotalUserNum

    @property
    def OrgNodeIdPath(self):
        return self._OrgNodeIdPath

    @OrgNodeIdPath.setter
    def OrgNodeIdPath(self, OrgNodeIdPath):
        self._OrgNodeIdPath = OrgNodeIdPath

    @property
    def OrgNodeNamePath(self):
        return self._OrgNodeNamePath

    @OrgNodeNamePath.setter
    def OrgNodeNamePath(self, OrgNodeNamePath):
        self._OrgNodeNamePath = OrgNodeNamePath


    def _deserialize(self, params):
        self._OrgNodeId = params.get("OrgNodeId")
        if params.get("UserInfo") is not None:
            self._UserInfo = []
            for item in params.get("UserInfo"):
                obj = UserInfo()
                obj._deserialize(item)
                self._UserInfo.append(obj)
        self._TotalUserNum = params.get("TotalUserNum")
        self._OrgNodeIdPath = params.get("OrgNodeIdPath")
        self._OrgNodeNamePath = params.get("OrgNodeNamePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveAccountFromAccountGroupRequest(AbstractModel):
    """RemoveAccountFromAccountGroup request structure.

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: Account group ID
        :type AccountGroupId: str
        :param _AccountIds: List of IDs of the accounts to be removed.
        :type AccountIds: list of str
        """
        self._AccountGroupId = None
        self._AccountIds = None

    @property
    def AccountGroupId(self):
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def AccountIds(self):
        return self._AccountIds

    @AccountIds.setter
    def AccountIds(self, AccountIds):
        self._AccountIds = AccountIds


    def _deserialize(self, params):
        self._AccountGroupId = params.get("AccountGroupId")
        self._AccountIds = params.get("AccountIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveAccountFromAccountGroupResponse(AbstractModel):
    """RemoveAccountFromAccountGroup response structure.

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


class RemoveUserFromUserGroupRequest(AbstractModel):
    """RemoveUserFromUserGroup request structure.

    """

    def __init__(self):
        r"""
        :param _UserIds: List of IDs of the users to be added to the user group.
        :type UserIds: list of str
        :param _UserGroupId: User group ID, which is globally unique.
        :type UserGroupId: str
        """
        self._UserIds = None
        self._UserGroupId = None

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId


    def _deserialize(self, params):
        self._UserIds = params.get("UserIds")
        self._UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserFromUserGroupResponse(AbstractModel):
    """RemoveUserFromUserGroup response structure.

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


class SortCondition(AbstractModel):
    """Sort criterion.

    """

    def __init__(self):
        r"""
        :param _SortKey: Sorting attribute.
        :type SortKey: str
        :param _SortOrder: Sorting order. Valid values: ASC: ascending order; DESC: descending order.
        :type SortOrder: str
        """
        self._SortKey = None
        self._SortOrder = None

    @property
    def SortKey(self):
        return self._SortKey

    @SortKey.setter
    def SortKey(self, SortKey):
        self._SortKey = SortKey

    @property
    def SortOrder(self):
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder


    def _deserialize(self, params):
        self._SortKey = params.get("SortKey")
        self._SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ThirdPartyAccountInfo(AbstractModel):
    """Third-Party account information.

    """

    def __init__(self):
        r"""
        :param _AccountCode: Third-Party account code. `2` indicates WeCom account.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccountCode: str
        :param _AccountName: Username of the account.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccountName: str
        """
        self._AccountCode = None
        self._AccountName = None

    @property
    def AccountCode(self):
        return self._AccountCode

    @AccountCode.setter
    def AccountCode(self, AccountCode):
        self._AccountCode = AccountCode

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName


    def _deserialize(self, params):
        self._AccountCode = params.get("AccountCode")
        self._AccountName = params.get("AccountName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrgNodeRequest(AbstractModel):
    """UpdateOrgNode request structure.

    """

    def __init__(self):
        r"""
        :param _OrgNodeId: Organization node ID, which is globally unique.
        :type OrgNodeId: str
        :param _DisplayName: Organization node name, which can contain up to 64 characters.
        :type DisplayName: str
        :param _Description: Organization node description.
        :type Description: str
        :param _CustomizedOrgNodeId: External ID of the organization node, which is optional and customizable. If this parameter is specified, its uniqueness will be verified.
        :type CustomizedOrgNodeId: str
        """
        self._OrgNodeId = None
        self._DisplayName = None
        self._Description = None
        self._CustomizedOrgNodeId = None

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CustomizedOrgNodeId(self):
        return self._CustomizedOrgNodeId

    @CustomizedOrgNodeId.setter
    def CustomizedOrgNodeId(self, CustomizedOrgNodeId):
        self._CustomizedOrgNodeId = CustomizedOrgNodeId


    def _deserialize(self, params):
        self._OrgNodeId = params.get("OrgNodeId")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._CustomizedOrgNodeId = params.get("CustomizedOrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrgNodeResponse(AbstractModel):
    """UpdateOrgNode response structure.

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


class UserGroupInfo(AbstractModel):
    """Returned user group list.

    """

    def __init__(self):
        r"""
        :param _DisplayName: Nickname, which can contain up to 64 characters and is the same as the username by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param _UserGroupId: User group ID, which is globally unique and can contain up to 64 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupId: str
        :param _Description: User group remarks.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _CreatedDate: Creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedDate: str
        """
        self._DisplayName = None
        self._UserGroupId = None
        self._Description = None
        self._CreatedDate = None

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._UserGroupId = params.get("UserGroupId")
        self._Description = params.get("Description")
        self._CreatedDate = params.get("CreatedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserGroupInfoSearchCriteria(AbstractModel):
    """User group attribute search criteria.

    """

    def __init__(self):
        r"""
        :param _Keyword: Search by name. The match criteria include user group name and user group ID.
        :type Keyword: str
        """
        self._Keyword = None

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserGroupInformation(AbstractModel):
    """Returned user group list.

    """

    def __init__(self):
        r"""
        :param _UserGroupId: User group ID.
        :type UserGroupId: str
        :param _UserGroupName: User group name.
        :type UserGroupName: str
        :param _LastModifiedDate: Last update time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifiedDate: str
        """
        self._UserGroupId = None
        self._UserGroupName = None
        self._LastModifiedDate = None

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def UserGroupName(self):
        return self._UserGroupName

    @UserGroupName.setter
    def UserGroupName(self, UserGroupName):
        self._UserGroupName = UserGroupName

    @property
    def LastModifiedDate(self):
        return self._LastModifiedDate

    @LastModifiedDate.setter
    def LastModifiedDate(self, LastModifiedDate):
        self._LastModifiedDate = LastModifiedDate


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        self._UserGroupName = params.get("UserGroupName")
        self._LastModifiedDate = params.get("LastModifiedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserGroupInformationSearchCriteria(AbstractModel):
    """User group attribute search criteria in the list of the user's user groups.

    """

    def __init__(self):
        r"""
        :param _Keyword: Search by name. The match criteria include user group name.
        :type Keyword: str
        """
        self._Keyword = None

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    """User information list.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID, which is globally unique and can contain up to 64 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param _DisplayName: Nickname, which can contain up to 64 characters and is the same as the username by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param _UserName: Username.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _Phone: User's mobile number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Phone: str
        :param _Email: Email address.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Email: str
        :param _Status: User status.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _DataSource: Data source.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DataSource: str
        """
        self._UserId = None
        self._DisplayName = None
        self._UserName = None
        self._Phone = None
        self._Email = None
        self._Status = None
        self._DataSource = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._DisplayName = params.get("DisplayName")
        self._UserName = params.get("UserName")
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._Status = params.get("Status")
        self._DataSource = params.get("DataSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInformation(AbstractModel):
    """User information list.

    """

    def __init__(self):
        r"""
        :param _UserName: Username, which can contain up to 32 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _Status: User status.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _DisplayName: Nickname, which can contain up to 64 characters and is the same as the username by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param _Description: User remarks, which can contain up to 512 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _LastUpdateTime: Last update time of the user in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastUpdateTime: str
        :param _CreationTime: User creation time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreationTime: str
        :param _OrgPath: Path ID of the user's primary organization.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgPath: str
        :param _Phone: User's mobile number with country code, such as `+86-00000000000`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Phone: str
        :param _SubjectGroups: List of IDs of the user's user groups.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubjectGroups: list of str
        :param _Email: User's email address.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Email: str
        :param _LastLoginTime: Last login time of the user in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastLoginTime: str
        :param _UserId: User ID, which is globally unique and can contain up to 64 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        """
        self._UserName = None
        self._Status = None
        self._DisplayName = None
        self._Description = None
        self._LastUpdateTime = None
        self._CreationTime = None
        self._OrgPath = None
        self._Phone = None
        self._SubjectGroups = None
        self._Email = None
        self._LastLoginTime = None
        self._UserId = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def LastUpdateTime(self):
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def OrgPath(self):
        return self._OrgPath

    @OrgPath.setter
    def OrgPath(self, OrgPath):
        self._OrgPath = OrgPath

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def SubjectGroups(self):
        return self._SubjectGroups

    @SubjectGroups.setter
    def SubjectGroups(self, SubjectGroups):
        self._SubjectGroups = SubjectGroups

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def LastLoginTime(self):
        return self._LastLoginTime

    @LastLoginTime.setter
    def LastLoginTime(self, LastLoginTime):
        self._LastLoginTime = LastLoginTime

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Status = params.get("Status")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._CreationTime = params.get("CreationTime")
        self._OrgPath = params.get("OrgPath")
        self._Phone = params.get("Phone")
        self._SubjectGroups = params.get("SubjectGroups")
        self._Email = params.get("Email")
        self._LastLoginTime = params.get("LastLoginTime")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserSearchCriteria(AbstractModel):
    """User attribute search criteria.

    """

    def __init__(self):
        r"""
        :param _UserName: Username, which can contain up to 64 characters.
        :type UserName: str
        :param _Phone: User's mobile number.
        :type Phone: str
        :param _Email: User's email address.
        :type Email: str
        :param _Status: User status. Valid values: NORMAL: normal; FREEZE: frozen; LOCKED: locked; NOT_ENABLED: disabled.
        :type Status: str
        :param _CreationTime: User creation time in ISO 8601 format.
        :type CreationTime: str
        :param _LastUpdateTime: The user's last update time.
        :type LastUpdateTime: str
        :param _Keyword: Search by name. The match criteria include username and user ID.
        :type Keyword: str
        """
        self._UserName = None
        self._Phone = None
        self._Email = None
        self._Status = None
        self._CreationTime = None
        self._LastUpdateTime = None
        self._Keyword = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def LastUpdateTime(self):
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._Status = params.get("Status")
        self._CreationTime = params.get("CreationTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        