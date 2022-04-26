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
        :param AccountGroupId: Account group ID.
        :type AccountGroupId: str
        :param GroupName: Account group name.
        :type GroupName: str
        :param Description: Remarks.
        :type Description: str
        :param CreatedDate: Creation time.
        :type CreatedDate: str
        """
        self.AccountGroupId = None
        self.GroupName = None
        self.Description = None
        self.CreatedDate = None


    def _deserialize(self, params):
        self.AccountGroupId = params.get("AccountGroupId")
        self.GroupName = params.get("GroupName")
        self.Description = params.get("Description")
        self.CreatedDate = params.get("CreatedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountGroupSearchCriteria(AbstractModel):
    """Account group query parameters

    """

    def __init__(self):
        r"""
        :param Keyword: Keyword
        :type Keyword: str
        """
        self.Keyword = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAccountToAccountGroupRequest(AbstractModel):
    """AddAccountToAccountGroup request structure.

    """

    def __init__(self):
        r"""
        :param AccountGroupId: Account group ID
        :type AccountGroupId: str
        :param AccountIds: List of IDs of the accounts to be added to the account group.
        :type AccountIds: list of str
        """
        self.AccountGroupId = None
        self.AccountIds = None


    def _deserialize(self, params):
        self.AccountGroupId = params.get("AccountGroupId")
        self.AccountIds = params.get("AccountIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAccountToAccountGroupResponse(AbstractModel):
    """AddAccountToAccountGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddUserToUserGroupRequest(AbstractModel):
    """AddUserToUserGroup request structure.

    """

    def __init__(self):
        r"""
        :param UserIds: List of IDs of the users to be added to the user group.
        :type UserIds: list of str
        :param UserGroupId: User group ID, which is globally unique.
        :type UserGroupId: str
        """
        self.UserIds = None
        self.UserGroupId = None


    def _deserialize(self, params):
        self.UserIds = params.get("UserIds")
        self.UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserToUserGroupResponse(AbstractModel):
    """AddUserToUserGroup response structure.

    """

    def __init__(self):
        r"""
        :param FailedItems: List of IDs of the users failed to be added to the user group.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FailedItems: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FailedItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailedItems = params.get("FailedItems")
        self.RequestId = params.get("RequestId")


class AppAccountInfo(AbstractModel):
    """List of queried account information.

    """

    def __init__(self):
        r"""
        :param AccountId: Account ID.
        :type AccountId: str
        :param AccountName: Account name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccountName: str
        :param UserList: User information list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserList: list of LinkUserInfo
        :param Description: Description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param CreatedDate: Creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedDate: str
        """
        self.AccountId = None
        self.AccountName = None
        self.UserList = None
        self.Description = None
        self.CreatedDate = None


    def _deserialize(self, params):
        self.AccountId = params.get("AccountId")
        self.AccountName = params.get("AccountName")
        if params.get("UserList") is not None:
            self.UserList = []
            for item in params.get("UserList"):
                obj = LinkUserInfo()
                obj._deserialize(item)
                self.UserList.append(obj)
        self.Description = params.get("Description")
        self.CreatedDate = params.get("CreatedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppAccountSearchCriteria(AbstractModel):
    """Account query parameters

    """

    def __init__(self):
        r"""
        :param Keyword: Keyword
        :type Keyword: str
        """
        self.Keyword = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationAuthorizationInfo(AbstractModel):
    """Application information list.

    """

    def __init__(self):
        r"""
        :param ApplicationAccounts: List of the user's accounts under authorized applications
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationAccounts: list of str
        :param ApplicationId: Application ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param InheritedForm: List of IDs of the user's user groups and organization nodes that have access to the application.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InheritedForm: :class:`tencentcloud.eiam.v20210420.models.InheritedForm`
        :param ApplicationName: Application name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param CreatedDate: Application creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedDate: str
        """
        self.ApplicationAccounts = None
        self.ApplicationId = None
        self.InheritedForm = None
        self.ApplicationName = None
        self.CreatedDate = None


    def _deserialize(self, params):
        self.ApplicationAccounts = params.get("ApplicationAccounts")
        self.ApplicationId = params.get("ApplicationId")
        if params.get("InheritedForm") is not None:
            self.InheritedForm = InheritedForm()
            self.InheritedForm._deserialize(params.get("InheritedForm"))
        self.ApplicationName = params.get("ApplicationName")
        self.CreatedDate = params.get("CreatedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationInfoSearchCriteria(AbstractModel):
    """Application attribute search criteria.

    """

    def __init__(self):
        r"""
        :param Keyword: Application search keyword, which can be application name or ID.
        :type Keyword: str
        :param ApplicationType: Application type. Valid values: OAUTH2, JWT, CAS, SAML2, FORM, OIDC, APIGW
        :type ApplicationType: str
        """
        self.Keyword = None
        self.ApplicationType = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.ApplicationType = params.get("ApplicationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationInformation(AbstractModel):
    """Application information list.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID, which is globally unique.
        :type ApplicationId: str
        :param DisplayName: Displayed application name, which can contain up to 64 characters and is the same as the application name by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param CreatedDate: Application creation time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedDate: str
        :param LastModifiedDate: Last update time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifiedDate: str
        :param AppStatus: Application status.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AppStatus: bool
        :param Icon: Application icon.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Icon: str
        :param ApplicationType: Application type.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationType: str
        :param ClientId: Client ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClientId: str
        """
        self.ApplicationId = None
        self.DisplayName = None
        self.CreatedDate = None
        self.LastModifiedDate = None
        self.AppStatus = None
        self.Icon = None
        self.ApplicationType = None
        self.ClientId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.DisplayName = params.get("DisplayName")
        self.CreatedDate = params.get("CreatedDate")
        self.LastModifiedDate = params.get("LastModifiedDate")
        self.AppStatus = params.get("AppStatus")
        self.Icon = params.get("Icon")
        self.ApplicationType = params.get("ApplicationType")
        self.ClientId = params.get("ClientId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizationInfo(AbstractModel):
    """Returned authorization information.

    """

    def __init__(self):
        r"""
        :param AppId: Unique application ID.
        :type AppId: str
        :param AppName: Application name.
        :type AppName: str
        :param EntityName: Type name.
        :type EntityName: str
        :param EntityId: Unique type ID.
        :type EntityId: str
        :param LastModifiedDate: Last update time in ISO 8601 format.
        :type LastModifiedDate: str
        :param AuthorizationId: Unique authorization type ID.
        :type AuthorizationId: str
        """
        self.AppId = None
        self.AppName = None
        self.EntityName = None
        self.EntityId = None
        self.LastModifiedDate = None
        self.AuthorizationId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.AppName = params.get("AppName")
        self.EntityName = params.get("EntityName")
        self.EntityId = params.get("EntityId")
        self.LastModifiedDate = params.get("LastModifiedDate")
        self.AuthorizationId = params.get("AuthorizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizationInfoSearchCriteria(AbstractModel):
    """User attribute search criteria.

    """

    def __init__(self):
        r"""
        :param Keyword: Search by name. When the query type is user, the match criteria include username and application name. When the query type is user group, the match criteria include user group name and application name. When the query type is organization, the match criteria include organization name and application name.
        :type Keyword: str
        """
        self.Keyword = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizationUserResouceInfo(AbstractModel):
    """Returned list of eligible user data

    """

    def __init__(self):
        r"""
        :param ResourceId: Resource ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceId: str
        :param ResourceType: Resource type
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceType: str
        :param Resource: Authorized resource
Note: this field may return null, indicating that no valid values can be obtained.
        :type Resource: str
        :param InheritedForm: Inheritance relationship
Note: this field may return null, indicating that no valid values can be obtained.
        :type InheritedForm: :class:`tencentcloud.eiam.v20210420.models.InheritedForm`
        :param ApplicationAccounts: Application account
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationAccounts: list of str
        :param ResourceName: Resource name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceName: str
        """
        self.ResourceId = None
        self.ResourceType = None
        self.Resource = None
        self.InheritedForm = None
        self.ApplicationAccounts = None
        self.ResourceName = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.ResourceType = params.get("ResourceType")
        self.Resource = params.get("Resource")
        if params.get("InheritedForm") is not None:
            self.InheritedForm = InheritedForm()
            self.InheritedForm._deserialize(params.get("InheritedForm"))
        self.ApplicationAccounts = params.get("ApplicationAccounts")
        self.ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountGroupRequest(AbstractModel):
    """CreateAccountGroup request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID.
        :type ApplicationId: str
        :param GroupName: Account group name.
        :type GroupName: str
        :param Description: Description.
        :type Description: str
        """
        self.ApplicationId = None
        self.GroupName = None
        self.Description = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.GroupName = params.get("GroupName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountGroupResponse(AbstractModel):
    """CreateAccountGroup response structure.

    """

    def __init__(self):
        r"""
        :param AccountGroupId: Account group ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccountGroupId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AccountGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AccountGroupId = params.get("AccountGroupId")
        self.RequestId = params.get("RequestId")


class CreateAppAccountRequest(AbstractModel):
    """CreateAppAccount request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param AccountName: Account name
        :type AccountName: str
        :param Password: Account password
        :type Password: str
        :param Description: Description
        :type Description: str
        """
        self.ApplicationId = None
        self.AccountName = None
        self.Password = None
        self.Description = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.AccountName = params.get("AccountName")
        self.Password = params.get("Password")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppAccountResponse(AbstractModel):
    """CreateAppAccount response structure.

    """

    def __init__(self):
        r"""
        :param AccountId: Account ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccountId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AccountId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AccountId = params.get("AccountId")
        self.RequestId = params.get("RequestId")


class CreateOrgNodeRequest(AbstractModel):
    """CreateOrgNode request structure.

    """

    def __init__(self):
        r"""
        :param DisplayName: Organization node name, which can contain up to 64 characters.
        :type DisplayName: str
        :param ParentOrgNodeId: Parent organization node ID. If this parameter is left empty, the organization will be created under the root organization node by default.
        :type ParentOrgNodeId: str
        :param Description: Organization node description.
        :type Description: str
        :param CustomizedOrgNodeId: External ID of the organization node, which is optional and customizable. If this parameter is specified, its uniqueness will be verified.
        :type CustomizedOrgNodeId: str
        """
        self.DisplayName = None
        self.ParentOrgNodeId = None
        self.Description = None
        self.CustomizedOrgNodeId = None


    def _deserialize(self, params):
        self.DisplayName = params.get("DisplayName")
        self.ParentOrgNodeId = params.get("ParentOrgNodeId")
        self.Description = params.get("Description")
        self.CustomizedOrgNodeId = params.get("CustomizedOrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrgNodeResponse(AbstractModel):
    """CreateOrgNode response structure.

    """

    def __init__(self):
        r"""
        :param OrgNodeId: Organization node ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OrgNodeId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrgNodeId = params.get("OrgNodeId")
        self.RequestId = params.get("RequestId")


class CreateUserGroupRequest(AbstractModel):
    """CreateUserGroup request structure.

    """

    def __init__(self):
        r"""
        :param DisplayName: User group nickname, which is unique and can contain up to 64 characters.
        :type DisplayName: str
        :param Description: User group remarks, which can contain up to 512 characters.
        :type Description: str
        """
        self.DisplayName = None
        self.Description = None


    def _deserialize(self, params):
        self.DisplayName = params.get("DisplayName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserGroupResponse(AbstractModel):
    """CreateUserGroup response structure.

    """

    def __init__(self):
        r"""
        :param UserGroupId: User group ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UserGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserGroupId = params.get("UserGroupId")
        self.RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser request structure.

    """

    def __init__(self):
        r"""
        :param UserName: Username, which can contain up to 64 characters.
        :type UserName: str
        :param Password: User password, which needs to be configured according to the password policy.
        :type Password: str
        :param DisplayName: Nickname, which can contain up to 64 characters and is the same as the username by default.
        :type DisplayName: str
        :param Description: User remarks, which can contain up to 512 characters.
        :type Description: str
        :param UserGroupIds: List of IDs of the user's user groups.
        :type UserGroupIds: list of str
        :param Phone: User's mobile number, such as `+86-1xxxxxxxxxx`.
        :type Phone: str
        :param OrgNodeId: Unique ID of the user's primary organization. If this parameter is left empty, the user will be created under the root node by default.
        :type OrgNodeId: str
        :param ExpirationTime: User expiration time in ISO 8601 format.
        :type ExpirationTime: str
        :param Email: User's email address.
        :type Email: str
        :param PwdNeedReset: Whether the password needs to be reset. Default value: false (no).
        :type PwdNeedReset: bool
        :param SecondaryOrgNodeIdList: List of IDs of the user's secondary organizations.
        :type SecondaryOrgNodeIdList: list of str
        """
        self.UserName = None
        self.Password = None
        self.DisplayName = None
        self.Description = None
        self.UserGroupIds = None
        self.Phone = None
        self.OrgNodeId = None
        self.ExpirationTime = None
        self.Email = None
        self.PwdNeedReset = None
        self.SecondaryOrgNodeIdList = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.DisplayName = params.get("DisplayName")
        self.Description = params.get("Description")
        self.UserGroupIds = params.get("UserGroupIds")
        self.Phone = params.get("Phone")
        self.OrgNodeId = params.get("OrgNodeId")
        self.ExpirationTime = params.get("ExpirationTime")
        self.Email = params.get("Email")
        self.PwdNeedReset = params.get("PwdNeedReset")
        self.SecondaryOrgNodeIdList = params.get("SecondaryOrgNodeIdList")
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
        :param UserId: Returned ID of the newly created user, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UserId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.RequestId = params.get("RequestId")


class DeleteAccountGroupRequest(AbstractModel):
    """DeleteAccountGroup request structure.

    """

    def __init__(self):
        r"""
        :param AccountGroupIdList: Array of account group IDs.
        :type AccountGroupIdList: list of str
        """
        self.AccountGroupIdList = None


    def _deserialize(self, params):
        self.AccountGroupIdList = params.get("AccountGroupIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountGroupResponse(AbstractModel):
    """DeleteAccountGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAppAccountRequest(AbstractModel):
    """DeleteAppAccount request structure.

    """

    def __init__(self):
        r"""
        :param AccountIdList: Array of account IDs .
        :type AccountIdList: list of str
        """
        self.AccountIdList = None


    def _deserialize(self, params):
        self.AccountIdList = params.get("AccountIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAppAccountResponse(AbstractModel):
    """DeleteAppAccount response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteOrgNodeRequest(AbstractModel):
    """DeleteOrgNode request structure.

    """

    def __init__(self):
        r"""
        :param OrgNodeId: Organization node ID, which is globally unique.
        :type OrgNodeId: str
        """
        self.OrgNodeId = None


    def _deserialize(self, params):
        self.OrgNodeId = params.get("OrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrgNodeResponse(AbstractModel):
    """DeleteOrgNode response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUserGroupRequest(AbstractModel):
    """DeleteUserGroup request structure.

    """

    def __init__(self):
        r"""
        :param UserGroupId: User group ID, which is globally unique.
        :type UserGroupId: str
        """
        self.UserGroupId = None


    def _deserialize(self, params):
        self.UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserGroupResponse(AbstractModel):
    """DeleteUserGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    """DeleteUser request structure.

    """

    def __init__(self):
        r"""
        :param UserName: Username, which can contain up to 32 characters. You need to select either `UserName` or `UserId` as the search criterion; if both are selected, `UserName` will be used by default.
        :type UserName: str
        :param UserId: User ID. You need to select either `UserName` or `UserId` as the search criterion. If both are selected, `UserName` will be used by default.
        :type UserId: str
        """
        self.UserName = None
        self.UserId = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    """DeleteUser response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUsersRequest(AbstractModel):
    """DeleteUsers request structure.

    """

    def __init__(self):
        r"""
        :param DeleteIdList: List of IDs of the users to be deleted. You need to specify at least `DeleteIdList` or `DeleteNameList`. If both are specified, `DeleteNameList` will be used first.
        :type DeleteIdList: list of str
        :param DeleteNameList: List of usernames of the users to be deleted. You need to specify at least `DeleteIdList` or `DeleteNameList`. If both are specified, `DeleteNameList` will be used first.
        :type DeleteNameList: list of str
        """
        self.DeleteIdList = None
        self.DeleteNameList = None


    def _deserialize(self, params):
        self.DeleteIdList = params.get("DeleteIdList")
        self.DeleteNameList = params.get("DeleteNameList")
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
        :param FailedItems: Information of the users failed to be deleted. When the business parameter is `DeleteIdList`, this field will return the list of IDs of the users failed to be deleted. When the business parameter is `DeleteNameList`, this field will return the list of usernames of the users failed to be deleted.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FailedItems: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FailedItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailedItems = params.get("FailedItems")
        self.RequestId = params.get("RequestId")


class DescribeAccountGroupRequest(AbstractModel):
    """DescribeAccountGroup request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID.
        :type ApplicationId: str
        :param SearchCondition: Search criterion. You can combine multiple search criteria and search in multiple data ranges. In addition, multiple query methods such as full match, partial match, and range match are supported. Specifically, double quotation marks ("") indicate full match, an asterisk (*) at the end of the field indicates partial match, and an empty field indicates to query the full table by default.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.AccountGroupSearchCriteria`
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self.ApplicationId = None
        self.SearchCondition = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        if params.get("SearchCondition") is not None:
            self.SearchCondition = AccountGroupSearchCriteria()
            self.SearchCondition._deserialize(params.get("SearchCondition"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountGroupResponse(AbstractModel):
    """DescribeAccountGroup response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of records returned for the query.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param ApplicationId: Application ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param AccountGroupList: Returned list of eligible data.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccountGroupList: list of AccountGroupInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ApplicationId = None
        self.AccountGroupList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.ApplicationId = params.get("ApplicationId")
        if params.get("AccountGroupList") is not None:
            self.AccountGroupList = []
            for item in params.get("AccountGroupList"):
                obj = AccountGroupInfo()
                obj._deserialize(item)
                self.AccountGroupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAppAccountRequest(AbstractModel):
    """DescribeAppAccount request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID.
        :type ApplicationId: str
        :param SearchCondition: Search criterion. You can combine multiple search criteria and search in multiple data ranges. In addition, multiple query methods such as full match, partial match, and range match are supported. Specifically, double quotation marks ("") indicate full match, an asterisk (*) at the end of the field indicates partial match, and an empty field indicates to query the full table by default.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.AppAccountSearchCriteria`
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self.ApplicationId = None
        self.SearchCondition = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        if params.get("SearchCondition") is not None:
            self.SearchCondition = AppAccountSearchCriteria()
            self.SearchCondition._deserialize(params.get("SearchCondition"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppAccountResponse(AbstractModel):
    """DescribeAppAccount response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of records returned for the query.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param ApplicationId: Application ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param AppAccountList: Returned list of eligible data.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AppAccountList: list of AppAccountInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ApplicationId = None
        self.AppAccountList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.ApplicationId = params.get("ApplicationId")
        if params.get("AppAccountList") is not None:
            self.AppAccountList = []
            for item in params.get("AppAccountList"):
                obj = AppAccountInfo()
                obj._deserialize(item)
                self.AppAccountList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeApplicationRequest(AbstractModel):
    """DescribeApplication request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID, which is globally unique. You must specify at least this parameter or `ClientId`.
        :type ApplicationId: str
        :param ClientId: Client ID. You must specify at least this parameter or `ApplicationId`.
        :type ClientId: str
        """
        self.ApplicationId = None
        self.ClientId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ClientId = params.get("ClientId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationResponse(AbstractModel):
    """DescribeApplication response structure.

    """

    def __init__(self):
        r"""
        :param KeyId: Key ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyId: str
        :param DisplayName: Displayed application name, which can contain up to 64 characters and is the same as the application name by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param LastModifiedDate: Last modification time of the application in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifiedDate: str
        :param ClientId: Client ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClientId: str
        :param ApplicationType: Application type, i.e., the application template type selected during application creation.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationType: str
        :param CreatedDate: Application creation time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedDate: str
        :param ApplicationId: Application ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param TokenExpired: Token validity period in seconds.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TokenExpired: int
        :param ClientSecret: Client secret.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClientSecret: str
        :param PublicKey: Public key information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicKey: str
        :param AuthorizeUrl: Authorization address.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthorizeUrl: str
        :param IconUrl: Access address of the application icon image.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IconUrl: str
        :param SecureLevel: Security level.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecureLevel: str
        :param AppStatus: Application status.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AppStatus: bool
        :param Description: Description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.KeyId = None
        self.DisplayName = None
        self.LastModifiedDate = None
        self.ClientId = None
        self.ApplicationType = None
        self.CreatedDate = None
        self.ApplicationId = None
        self.TokenExpired = None
        self.ClientSecret = None
        self.PublicKey = None
        self.AuthorizeUrl = None
        self.IconUrl = None
        self.SecureLevel = None
        self.AppStatus = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.DisplayName = params.get("DisplayName")
        self.LastModifiedDate = params.get("LastModifiedDate")
        self.ClientId = params.get("ClientId")
        self.ApplicationType = params.get("ApplicationType")
        self.CreatedDate = params.get("CreatedDate")
        self.ApplicationId = params.get("ApplicationId")
        self.TokenExpired = params.get("TokenExpired")
        self.ClientSecret = params.get("ClientSecret")
        self.PublicKey = params.get("PublicKey")
        self.AuthorizeUrl = params.get("AuthorizeUrl")
        self.IconUrl = params.get("IconUrl")
        self.SecureLevel = params.get("SecureLevel")
        self.AppStatus = params.get("AppStatus")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class DescribeOrgNodeRequest(AbstractModel):
    """DescribeOrgNode request structure.

    """

    def __init__(self):
        r"""
        :param OrgNodeId: Organization node ID, which is globally unique and can contain up to 64 characters. If this parameter is left empty, the information of the root organization node will be read by default.
        :type OrgNodeId: str
        :param IncludeOrgNodeChildInfo: Whether to read the information of its sub-nodes. When this parameter is left empty or specified as `false`, only the information of the current organization node will be read by default. When it is specified as `true`, the information of the current organization node and its level-1 sub-nodes will be read.
        :type IncludeOrgNodeChildInfo: bool
        """
        self.OrgNodeId = None
        self.IncludeOrgNodeChildInfo = None


    def _deserialize(self, params):
        self.OrgNodeId = params.get("OrgNodeId")
        self.IncludeOrgNodeChildInfo = params.get("IncludeOrgNodeChildInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrgNodeResponse(AbstractModel):
    """DescribeOrgNode response structure.

    """

    def __init__(self):
        r"""
        :param DisplayName: Displayed organization node name, which can contain up to 64 characters and is the same as the organization name by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param LastModifiedDate: Last modification time of the organization node in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifiedDate: str
        :param CustomizedOrgNodeId: External ID of the organization node.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CustomizedOrgNodeId: str
        :param ParentOrgNodeId: Parent node ID of the current organization node.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ParentOrgNodeId: str
        :param OrgNodeId: Organization node ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeId: str
        :param DataSource: Data source.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DataSource: str
        :param CreatedDate: Organization node creation time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedDate: str
        :param OrgNodeChildInfo: List of sub-nodes under the current organization node.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeChildInfo: list of OrgNodeChildInfo
        :param Description: Organization node description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DisplayName = None
        self.LastModifiedDate = None
        self.CustomizedOrgNodeId = None
        self.ParentOrgNodeId = None
        self.OrgNodeId = None
        self.DataSource = None
        self.CreatedDate = None
        self.OrgNodeChildInfo = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DisplayName = params.get("DisplayName")
        self.LastModifiedDate = params.get("LastModifiedDate")
        self.CustomizedOrgNodeId = params.get("CustomizedOrgNodeId")
        self.ParentOrgNodeId = params.get("ParentOrgNodeId")
        self.OrgNodeId = params.get("OrgNodeId")
        self.DataSource = params.get("DataSource")
        self.CreatedDate = params.get("CreatedDate")
        if params.get("OrgNodeChildInfo") is not None:
            self.OrgNodeChildInfo = []
            for item in params.get("OrgNodeChildInfo"):
                obj = OrgNodeChildInfo()
                obj._deserialize(item)
                self.OrgNodeChildInfo.append(obj)
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class DescribePublicKeyRequest(AbstractModel):
    """DescribePublicKey request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID, which is globally unique.
        :type ApplicationId: str
        """
        self.ApplicationId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicKeyResponse(AbstractModel):
    """DescribePublicKey response structure.

    """

    def __init__(self):
        r"""
        :param PublicKey: Public key information used for JWT signature verification.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicKey: str
        :param KeyId: JWT key ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyId: str
        :param ApplicationId: Application ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PublicKey = None
        self.KeyId = None
        self.ApplicationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PublicKey = params.get("PublicKey")
        self.KeyId = params.get("KeyId")
        self.ApplicationId = params.get("ApplicationId")
        self.RequestId = params.get("RequestId")


class DescribeUserGroupRequest(AbstractModel):
    """DescribeUserGroup request structure.

    """

    def __init__(self):
        r"""
        :param UserGroupId: User group ID, which is globally unique.
        :type UserGroupId: str
        """
        self.UserGroupId = None


    def _deserialize(self, params):
        self.UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserGroupResponse(AbstractModel):
    """DescribeUserGroup response structure.

    """

    def __init__(self):
        r"""
        :param DisplayName: User group nickname, which is not unique and can contain up to 64 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param Description: User group remarks, which can contain up to 512 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param UserGroupId: User group ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DisplayName = None
        self.Description = None
        self.UserGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DisplayName = params.get("DisplayName")
        self.Description = params.get("Description")
        self.UserGroupId = params.get("UserGroupId")
        self.RequestId = params.get("RequestId")


class DescribeUserInfoRequest(AbstractModel):
    """DescribeUserInfo request structure.

    """

    def __init__(self):
        r"""
        :param UserName: Username, which can contain up to 64 characters. You need to specify at least `UserName` or `UserId`. If both are specified, `UserName` will be used first.
        :type UserName: str
        :param UserId: User ID, which can contain up to 64 characters. You need to specify at least `UserName` or `UserId`. If both are specified, `UserName` will be used first.
        :type UserId: str
        """
        self.UserName = None
        self.UserId = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserInfoResponse(AbstractModel):
    """DescribeUserInfo response structure.

    """

    def __init__(self):
        r"""
        :param UserName: Username.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param Status: User status. Valid values: NORMAL: normal; FREEZE: frozen; LOCKED: locked; NOT_ENABLED: disabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param DisplayName: Nickname
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param Description: User remarks.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param UserGroupIds: List of IDs of the user's user groups.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupIds: list of str
        :param UserId: User ID, which can contain up to 64 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param Email: User's email address.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Email: str
        :param Phone: User's mobile number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Phone: str
        :param OrgNodeId: Unique ID of the user's primary organization.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeId: str
        :param DataSource: Data source
Note: this field may return null, indicating that no valid values can be obtained.
        :type DataSource: str
        :param ExpirationTime: User expiration time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpirationTime: str
        :param ActivationTime: User activation time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ActivationTime: str
        :param PwdNeedReset: Whether the password of the current user needs to be reset. `false` indicates no.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PwdNeedReset: bool
        :param SecondaryOrgNodeIdList: List of IDs of the user's secondary organizations.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecondaryOrgNodeIdList: list of str
        :param AdminFlag: Whether the user is an admin. Valid values: 0: no; 1: yes.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AdminFlag: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UserName = None
        self.Status = None
        self.DisplayName = None
        self.Description = None
        self.UserGroupIds = None
        self.UserId = None
        self.Email = None
        self.Phone = None
        self.OrgNodeId = None
        self.DataSource = None
        self.ExpirationTime = None
        self.ActivationTime = None
        self.PwdNeedReset = None
        self.SecondaryOrgNodeIdList = None
        self.AdminFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Status = params.get("Status")
        self.DisplayName = params.get("DisplayName")
        self.Description = params.get("Description")
        self.UserGroupIds = params.get("UserGroupIds")
        self.UserId = params.get("UserId")
        self.Email = params.get("Email")
        self.Phone = params.get("Phone")
        self.OrgNodeId = params.get("OrgNodeId")
        self.DataSource = params.get("DataSource")
        self.ExpirationTime = params.get("ExpirationTime")
        self.ActivationTime = params.get("ActivationTime")
        self.PwdNeedReset = params.get("PwdNeedReset")
        self.SecondaryOrgNodeIdList = params.get("SecondaryOrgNodeIdList")
        self.AdminFlag = params.get("AdminFlag")
        self.RequestId = params.get("RequestId")


class DescribeUserResourcesAuthorizationRequest(AbstractModel):
    """DescribeUserResourcesAuthorization request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID.
        :type ApplicationId: str
        :param UserId: User ID. You need to specify at least `UserName` or `UserId`. If both are specified, `UserName` will be used first.
        :type UserId: str
        :param UserName: Username. You need to specify at least `UserName` or `UserId`. If both are specified, `UserName` will be used first.
        :type UserName: str
        :param IncludeInheritedAuthorizations: Whether the query scope includes the application access of the user groups and organizations associated with the user. Valid values: false: no; true: yes. Default value: false.
        :type IncludeInheritedAuthorizations: bool
        """
        self.ApplicationId = None
        self.UserId = None
        self.UserName = None
        self.IncludeInheritedAuthorizations = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.UserId = params.get("UserId")
        self.UserName = params.get("UserName")
        self.IncludeInheritedAuthorizations = params.get("IncludeInheritedAuthorizations")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserResourcesAuthorizationResponse(AbstractModel):
    """DescribeUserResourcesAuthorization response structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Unique application ID.
        :type ApplicationId: str
        :param ApplicationAccounts: Application account.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationAccounts: list of str
        :param UserId: Unique ID of the authorized user.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param UserName: Username of the authorized user.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param AuthorizationUserResourceList: Returned resource list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthorizationUserResourceList: list of AuthorizationUserResouceInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ApplicationId = None
        self.ApplicationAccounts = None
        self.UserId = None
        self.UserName = None
        self.AuthorizationUserResourceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationAccounts = params.get("ApplicationAccounts")
        self.UserId = params.get("UserId")
        self.UserName = params.get("UserName")
        if params.get("AuthorizationUserResourceList") is not None:
            self.AuthorizationUserResourceList = []
            for item in params.get("AuthorizationUserResourceList"):
                obj = AuthorizationUserResouceInfo()
                obj._deserialize(item)
                self.AuthorizationUserResourceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserThirdPartyAccountInfoRequest(AbstractModel):
    """DescribeUserThirdPartyAccountInfo request structure.

    """

    def __init__(self):
        r"""
        :param UserName: Username. You need to specify at least `Username` or `UserId`. If both are specified, `Username` will be used first.
        :type UserName: str
        :param UserId: User ID. You need to specify at least `Username` or `UserId`. If both are specified, `Username` will be used first.
        :type UserId: str
        """
        self.UserName = None
        self.UserId = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserThirdPartyAccountInfoResponse(AbstractModel):
    """DescribeUserThirdPartyAccountInfo response structure.

    """

    def __init__(self):
        r"""
        :param UserId: User ID.
        :type UserId: str
        :param UserName: Username.
        :type UserName: str
        :param ThirdPartyAccounts: Third-Party account binding information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ThirdPartyAccounts: list of ThirdPartyAccountInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UserId = None
        self.UserName = None
        self.ThirdPartyAccounts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserName = params.get("UserName")
        if params.get("ThirdPartyAccounts") is not None:
            self.ThirdPartyAccounts = []
            for item in params.get("ThirdPartyAccounts"):
                obj = ThirdPartyAccountInfo()
                obj._deserialize(item)
                self.ThirdPartyAccounts.append(obj)
        self.RequestId = params.get("RequestId")


class InheritedForm(AbstractModel):
    """Application information list.

    """

    def __init__(self):
        r"""
        :param UserGroupIds: List of IDs of the user's user groups.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupIds: list of str
        :param OrgNodeIds: List of IDs of the user's organization nodes.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeIds: list of str
        """
        self.UserGroupIds = None
        self.OrgNodeIds = None


    def _deserialize(self, params):
        self.UserGroupIds = params.get("UserGroupIds")
        self.OrgNodeIds = params.get("OrgNodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkUserInfo(AbstractModel):
    """User information associated with the account

    """

    def __init__(self):
        r"""
        :param UserId: User ID, which is globally unique and can contain up to 64 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param UserName: Username.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        """
        self.UserId = None
        self.UserName = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccountInAccountGroupRequest(AbstractModel):
    """ListAccountInAccountGroup request structure.

    """

    def __init__(self):
        r"""
        :param AccountGroupId: Account group ID.
        :type AccountGroupId: str
        :param SearchCondition: Search criterion. You can combine multiple search criteria and search in multiple data ranges.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.AccountGroupSearchCriteria`
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self.AccountGroupId = None
        self.SearchCondition = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.AccountGroupId = params.get("AccountGroupId")
        if params.get("SearchCondition") is not None:
            self.SearchCondition = AccountGroupSearchCriteria()
            self.SearchCondition._deserialize(params.get("SearchCondition"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccountInAccountGroupResponse(AbstractModel):
    """ListAccountInAccountGroup response structure.

    """

    def __init__(self):
        r"""
        :param AccountList: List of accounts returned for the query.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccountList: list of AppAccountInfo
        :param TotalCount: Total number of accounts returned for the query.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param AccountGroupId: Account group ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccountGroupId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AccountList = None
        self.TotalCount = None
        self.AccountGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccountList") is not None:
            self.AccountList = []
            for item in params.get("AccountList"):
                obj = AppAccountInfo()
                obj._deserialize(item)
                self.AccountList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.AccountGroupId = params.get("AccountGroupId")
        self.RequestId = params.get("RequestId")


class ListApplicationAuthorizationsRequest(AbstractModel):
    """ListApplicationAuthorizations request structure.

    """

    def __init__(self):
        r"""
        :param EntityType: Query type. Valid values: User: user; UserGroup: user group; OrgNode: organization.
        :type EntityType: str
        :param SearchCondition: Search criterion. You can combine multiple search criteria and search in multiple data ranges. In addition, multiple query methods such as full match, partial match, and range match are supported. Specifically, double quotation marks ("") indicate full match, an asterisk (*) at the end of the field indicates partial match, and an empty field indicates to query the full table by default.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.AuthorizationInfoSearchCriteria`
        :param Sort: Set of sort criteria. You can sort the results by last modification time (lastModifiedDate). If this field is left empty, the results will be sorted in alphabetical order by application name.
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param Offset: Pagination offset. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated.
        :type Offset: int
        :param Limit: Number of results read per page. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated.
        :type Limit: int
        """
        self.EntityType = None
        self.SearchCondition = None
        self.Sort = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.EntityType = params.get("EntityType")
        if params.get("SearchCondition") is not None:
            self.SearchCondition = AuthorizationInfoSearchCriteria()
            self.SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self.Sort = SortCondition()
            self.Sort._deserialize(params.get("Sort"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListApplicationAuthorizationsResponse(AbstractModel):
    """ListApplicationAuthorizations response structure.

    """

    def __init__(self):
        r"""
        :param AuthorizationInfoList: Returned list of application authorization information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthorizationInfoList: list of AuthorizationInfo
        :param TotalCount: Total number of returned application information items.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AuthorizationInfoList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AuthorizationInfoList") is not None:
            self.AuthorizationInfoList = []
            for item in params.get("AuthorizationInfoList"):
                obj = AuthorizationInfo()
                obj._deserialize(item)
                self.AuthorizationInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListApplicationsRequest(AbstractModel):
    """ListApplications request structure.

    """

    def __init__(self):
        r"""
        :param SearchCondition: Fuzzy match search criterion. You can combine multiple search criteria and search in multiple data ranges. In addition, multiple query methods such as full match, partial match, and range match are supported. Specifically, double quotation marks ("") indicate full match, and an asterisk (*) at the end of the field indicates partial match. The fuzzy match search feature and the exact match query feature will not take effect at the same time. If both `SearchCondition` and `ApplicationIdList` are specified, `ApplicationIdList` will take effect by default for exact match query; otherwise, the information of all applications will be returned by default.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.ApplicationInfoSearchCriteria`
        :param Sort: Set of sort criteria. Valid values: DisplayName: application name; CreatedDate: creation time; LastModifiedDate: last modification time. If this field is left empty, the results will be sorted in alphabetical order by application name.
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param Offset: Set of sort criteria. Valid values: DisplayName: application name; CreatedDate: creation time; LastModifiedDate: last modification time. If this field is left empty, the results will be sorted in alphabetical order by application name.
        :type Offset: int
        :param Limit: Number of results read per page. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated.
        :type Limit: int
        :param ApplicationIdList: Application ID list, through which the corresponding application information will be matched exactly. The fuzzy match search feature and the exact match query feature will not take effect at the same time. If both `SearchCondition` and `ApplicationIdList` are specified, `ApplicationIdList` will take effect by default for exact match query; otherwise, the information of all applications will be returned by default.
        :type ApplicationIdList: list of str
        """
        self.SearchCondition = None
        self.Sort = None
        self.Offset = None
        self.Limit = None
        self.ApplicationIdList = None


    def _deserialize(self, params):
        if params.get("SearchCondition") is not None:
            self.SearchCondition = ApplicationInfoSearchCriteria()
            self.SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self.Sort = SortCondition()
            self.Sort._deserialize(params.get("Sort"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ApplicationIdList = params.get("ApplicationIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListApplicationsResponse(AbstractModel):
    """ListApplications response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of returned application information items.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param ApplicationInfoList: Returned application information list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationInfoList: list of ApplicationInformation
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ApplicationInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApplicationInfoList") is not None:
            self.ApplicationInfoList = []
            for item in params.get("ApplicationInfoList"):
                obj = ApplicationInformation()
                obj._deserialize(item)
                self.ApplicationInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class ListAuthorizedApplicationsToOrgNodeRequest(AbstractModel):
    """ListAuthorizedApplicationsToOrgNode request structure.

    """

    def __init__(self):
        r"""
        :param OrgNodeId: Organization node ID.
        :type OrgNodeId: str
        """
        self.OrgNodeId = None


    def _deserialize(self, params):
        self.OrgNodeId = params.get("OrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAuthorizedApplicationsToOrgNodeResponse(AbstractModel):
    """ListAuthorizedApplicationsToOrgNode response structure.

    """

    def __init__(self):
        r"""
        :param ApplicationIds: List of IDs of the applications accessible to the organization node.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ApplicationIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ApplicationIds = params.get("ApplicationIds")
        self.RequestId = params.get("RequestId")


class ListAuthorizedApplicationsToUserGroupRequest(AbstractModel):
    """ListAuthorizedApplicationsToUserGroup request structure.

    """

    def __init__(self):
        r"""
        :param UserGroupId: User group ID.
        :type UserGroupId: str
        """
        self.UserGroupId = None


    def _deserialize(self, params):
        self.UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAuthorizedApplicationsToUserGroupResponse(AbstractModel):
    """ListAuthorizedApplicationsToUserGroup response structure.

    """

    def __init__(self):
        r"""
        :param ApplicationIds: List of IDs of the applications accessible to the user group.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ApplicationIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ApplicationIds = params.get("ApplicationIds")
        self.RequestId = params.get("RequestId")


class ListAuthorizedApplicationsToUserRequest(AbstractModel):
    """ListAuthorizedApplicationsToUser request structure.

    """

    def __init__(self):
        r"""
        :param UserId: User ID.
        :type UserId: str
        :param IncludeInheritedAuthorizations: Whether the query scope includes the application access of the user groups and organizations associated with the user. Valid values: false: no; true: yes. Default value: false.
        :type IncludeInheritedAuthorizations: bool
        """
        self.UserId = None
        self.IncludeInheritedAuthorizations = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.IncludeInheritedAuthorizations = params.get("IncludeInheritedAuthorizations")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAuthorizedApplicationsToUserResponse(AbstractModel):
    """ListAuthorizedApplicationsToUser response structure.

    """

    def __init__(self):
        r"""
        :param ApplicationAuthorizationInfo: List of information of the applications accessible to the user.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplicationAuthorizationInfo: list of ApplicationAuthorizationInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ApplicationAuthorizationInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ApplicationAuthorizationInfo") is not None:
            self.ApplicationAuthorizationInfo = []
            for item in params.get("ApplicationAuthorizationInfo"):
                obj = ApplicationAuthorizationInfo()
                obj._deserialize(item)
                self.ApplicationAuthorizationInfo.append(obj)
        self.RequestId = params.get("RequestId")


class ListUserGroupsOfUserRequest(AbstractModel):
    """ListUserGroupsOfUser request structure.

    """

    def __init__(self):
        r"""
        :param UserId: User ID, which is globally unique.
        :type UserId: str
        :param SearchCondition: Fuzzy search criterion. You can search by user group name (DisplayName). If this field is left empty, all of the user's user groups will be displayed by default.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.UserGroupInformationSearchCriteria`
        :param Sort: Set of sort criteria. Valid values: DisplayName: user group name; UserGroupId: user group ID; CreatedDate: creation time. If this field is left empty, the results will be sorted in alphabetical order by user group name.
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param Offset: Pagination offset. Default value: 0. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated, and up to 50 user groups will be returned.
        :type Offset: int
        :param Limit: Number of results read per page. Default value: 50. Maximum value: 100. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated, and up to 50 user groups will be returned.
        :type Limit: int
        """
        self.UserId = None
        self.SearchCondition = None
        self.Sort = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        if params.get("SearchCondition") is not None:
            self.SearchCondition = UserGroupInformationSearchCriteria()
            self.SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self.Sort = SortCondition()
            self.Sort._deserialize(params.get("Sort"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserGroupsOfUserResponse(AbstractModel):
    """ListUserGroupsOfUser response structure.

    """

    def __init__(self):
        r"""
        :param UserGroupIds: List of IDs of the user's user groups.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupIds: list of str
        :param UserId: User ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param UserGroupInfoList: List of information of the user's user groups.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupInfoList: list of UserGroupInfo
        :param TotalCount: Total number of returned user group information items.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UserGroupIds = None
        self.UserId = None
        self.UserGroupInfoList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserGroupIds = params.get("UserGroupIds")
        self.UserId = params.get("UserId")
        if params.get("UserGroupInfoList") is not None:
            self.UserGroupInfoList = []
            for item in params.get("UserGroupInfoList"):
                obj = UserGroupInfo()
                obj._deserialize(item)
                self.UserGroupInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListUserGroupsRequest(AbstractModel):
    """ListUserGroups request structure.

    """

    def __init__(self):
        r"""
        :param SearchCondition: Search criterion. You can combine multiple search criteria and search in multiple data ranges. In addition, multiple query methods such as full match, partial match, and range match are supported. Specifically, double quotation marks ("") indicate full match, an asterisk (*) at the end of the field indicates partial match, and an empty field indicates to query the full table by default.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.UserGroupInfoSearchCriteria`
        :param Sort: Set of sort criteria. The supported attributes for sorting include user group name (DisplayName), user group ID (UserGroupId), and last modification time (LastModifiedDate). If this field is left empty, the results will be sorted in alphabetical order by user group name.
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param Offset: Pagination offset. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated.
        :type Offset: int
        :param Limit: Number of results read per page. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated.
        :type Limit: int
        """
        self.SearchCondition = None
        self.Sort = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("SearchCondition") is not None:
            self.SearchCondition = UserGroupInfoSearchCriteria()
            self.SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self.Sort = SortCondition()
            self.Sort._deserialize(params.get("Sort"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserGroupsResponse(AbstractModel):
    """ListUserGroups response structure.

    """

    def __init__(self):
        r"""
        :param UserGroupList: Returned user group list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupList: list of UserGroupInformation
        :param TotalCount: Total number of returned user group information items.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UserGroupList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UserGroupList") is not None:
            self.UserGroupList = []
            for item in params.get("UserGroupList"):
                obj = UserGroupInformation()
                obj._deserialize(item)
                self.UserGroupList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListUsersInOrgNodeRequest(AbstractModel):
    """ListUsersInOrgNode request structure.

    """

    def __init__(self):
        r"""
        :param OrgNodeId: Organization node ID, which is globally unique and can contain up to 64 characters. If this parameter is left empty, the user information under the root organization node will be read by default.
        :type OrgNodeId: str
        :param IncludeOrgNodeChildInfo: Whether to read the information of its sub-nodes. When this parameter is left empty or specified as `false`, only the information of the current organization node will be read by default. When it is specified as `true`, the information of the current organization node and its level-1 sub-nodes will be read.
        :type IncludeOrgNodeChildInfo: bool
        :param SearchCondition: User attribute search criterion. The supported search criteria include username, mobile number, email address, user locking status, user freezing status, creation time, and last modification time, which can also be combined. In addition, multiple query methods such as full match, partial match, and range match are supported. Specifically, double quotation marks ("") indicate full match, an asterisk (*) at the end of the field indicates partial match, brackets separated by a comma ([Min,Max]) indicate query within a closed interval, braces separated by a comma ({Min,Max}) indicate query within an open interval, and a bracket and a brace can be used together (for example, {Min,Max] indicates that the minimum value is excluded and the maximum value is included in the query). Range query supports using an asterisk (for example, {20,*] indicates an interval including all data greater than 20) and querying by time period. The supported attributes include creation time (CreationTime) and last modification time (LastUpdateTime) in ISO 8601 format, such as `2021-01-13T09:44:07.182+0000`.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.ListUsersInOrgNodeSearchCriteria`
        :param Sort: Set of sort criteria. The supported attributes for sorting include username (UserName), mobile number (Phone), email address (Email), user status (Status), creation time (CreatedDate), and last modification time (LastModifiedDate). If this field is left empty, the results will be sorted in alphabetical order by nickname (DisplayName).
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param Offset: Pagination offset. Default value: 0. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated, and up to 50 users will be returned.
        :type Offset: int
        :param Limit: Number of results read per page. Default value: 50. Maximum value: 100. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated, and up to 50 users will be returned.
        :type Limit: int
        """
        self.OrgNodeId = None
        self.IncludeOrgNodeChildInfo = None
        self.SearchCondition = None
        self.Sort = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.OrgNodeId = params.get("OrgNodeId")
        self.IncludeOrgNodeChildInfo = params.get("IncludeOrgNodeChildInfo")
        if params.get("SearchCondition") is not None:
            self.SearchCondition = ListUsersInOrgNodeSearchCriteria()
            self.SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self.Sort = SortCondition()
            self.Sort._deserialize(params.get("Sort"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersInOrgNodeResponse(AbstractModel):
    """ListUsersInOrgNode response structure.

    """

    def __init__(self):
        r"""
        :param OrgNodeChildUserInfo: User information list under the organization sub-node.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeChildUserInfo: list of OrgNodeChildUserInfo
        :param OrgNodeId: Organization node ID, which is globally unique and can contain up to 64 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeId: str
        :param UserInfo: User information list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserInfo: list of UserInfo
        :param TotalUserNum: Total number of users under the current organization node.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalUserNum: int
        :param OrgNodeIdPath: Organization ID path.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeIdPath: str
        :param OrgNodeNamePath: Organization name path.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeNamePath: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OrgNodeChildUserInfo = None
        self.OrgNodeId = None
        self.UserInfo = None
        self.TotalUserNum = None
        self.OrgNodeIdPath = None
        self.OrgNodeNamePath = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("OrgNodeChildUserInfo") is not None:
            self.OrgNodeChildUserInfo = []
            for item in params.get("OrgNodeChildUserInfo"):
                obj = OrgNodeChildUserInfo()
                obj._deserialize(item)
                self.OrgNodeChildUserInfo.append(obj)
        self.OrgNodeId = params.get("OrgNodeId")
        if params.get("UserInfo") is not None:
            self.UserInfo = []
            for item in params.get("UserInfo"):
                obj = UserInfo()
                obj._deserialize(item)
                self.UserInfo.append(obj)
        self.TotalUserNum = params.get("TotalUserNum")
        self.OrgNodeIdPath = params.get("OrgNodeIdPath")
        self.OrgNodeNamePath = params.get("OrgNodeNamePath")
        self.RequestId = params.get("RequestId")


class ListUsersInOrgNodeSearchCriteria(AbstractModel):
    """Displays user attribute search criteria under the organization.

    """

    def __init__(self):
        r"""
        :param UserName: Username, which can contain up to 64 characters.
        :type UserName: str
        :param Phone: User's mobile number.
        :type Phone: str
        :param Email: User's email address.
        :type Email: str
        :param Status: User status. Valid values: NORMAL: normal; FREEZE: frozen; LOCKED: locked; NOT_ENABLED: disabled.
        :type Status: str
        :param CreationTime: User creation time in ISO 8601 format.
        :type CreationTime: str
        :param LastUpdateTime: Last update time of the user.
        :type LastUpdateTime: str
        :param Keyword: Search by name. The match criteria include username and user's mobile number.
        :type Keyword: str
        """
        self.UserName = None
        self.Phone = None
        self.Email = None
        self.Status = None
        self.CreationTime = None
        self.LastUpdateTime = None
        self.Keyword = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Phone = params.get("Phone")
        self.Email = params.get("Email")
        self.Status = params.get("Status")
        self.CreationTime = params.get("CreationTime")
        self.LastUpdateTime = params.get("LastUpdateTime")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersInUserGroupRequest(AbstractModel):
    """ListUsersInUserGroup request structure.

    """

    def __init__(self):
        r"""
        :param UserGroupId: User group ID, which is globally unique.
        :type UserGroupId: str
        :param SearchCondition: User attribute search criterion. The supported search criteria include username, mobile number, email address, user locking status, user freezing status, creation time, and last modification time, which can also be combined. In addition, multiple query methods such as full match, partial match, and range match are supported. Specifically, double quotation marks ("") indicate full match, an asterisk (*) at the end of the field indicates partial match, brackets separated by a comma ([Min,Max]) indicate query within a closed interval, braces separated by a comma ({Min,Max}) indicate query within an open interval, and a bracket and a brace can be used together (for example, {Min,Max] indicates that the minimum value is excluded and the maximum value is included in the query). Range query supports using an asterisk (for example, {20,*] indicates an interval including all data greater than 20) and querying by time period. The supported attributes include creation time (CreationTime) and last modification time (LastUpdateTime) in ISO 8601 format, such as `2021-01-13T09:44:07.182+0000`.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.UserSearchCriteria`
        :param Sort: Set of sort criteria. The supported attributes for sorting include username (UserName), nickname (DisplayName), mobile number (Phone), email address (Email), user status (Status), creation time (CreatedDate), and last modification time (LastModifiedDate). If this field is left empty, the results will be sorted in alphabetical order by nickname (DisplayName).
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param Offset: Pagination offset. Default value: 0. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated, and up to 50 users will be returned.
        :type Offset: int
        :param Limit: Number of results read per page. Default value: 50. Maximum value: 100. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated, and up to 50 users will be returned.
        :type Limit: int
        """
        self.UserGroupId = None
        self.SearchCondition = None
        self.Sort = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.UserGroupId = params.get("UserGroupId")
        if params.get("SearchCondition") is not None:
            self.SearchCondition = UserSearchCriteria()
            self.SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self.Sort = SortCondition()
            self.Sort._deserialize(params.get("Sort"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersInUserGroupResponse(AbstractModel):
    """ListUsersInUserGroup response structure.

    """

    def __init__(self):
        r"""
        :param UserGroupId: User group ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupId: str
        :param UserInfo: Returned user information list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserInfo: list of UserInfo
        :param TotalNum: Total number of returned user information items.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalNum: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UserGroupId = None
        self.UserInfo = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserGroupId = params.get("UserGroupId")
        if params.get("UserInfo") is not None:
            self.UserInfo = []
            for item in params.get("UserInfo"):
                obj = UserInfo()
                obj._deserialize(item)
                self.UserInfo.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class ListUsersRequest(AbstractModel):
    """ListUsers request structure.

    """

    def __init__(self):
        r"""
        :param SearchCondition: User attribute search criterion. The supported search criteria include username, mobile number, email address, user locking status, user freezing status, creation time, and last modification time, which can also be combined. In addition, multiple query methods such as full match, partial match, and range match are supported. Specifically, double quotation marks ("") indicate full match, an asterisk (*) at the end of the field indicates partial match, brackets separated by a comma ([Min,Max]) indicate query within a closed interval, braces separated by a comma ({Min,Max}) indicate query within an open interval, and a bracket and a brace can be used together (for example, {Min,Max] indicates that the minimum value is excluded and the maximum value is included in the query). Range query supports using an asterisk (for example, {20,*] indicates an interval including all data greater than 20) and querying by time period. The supported attributes include creation time (CreationTime) and last modification time (LastUpdateTime) in ISO 8601 format, such as `2021-01-13T09:44:07.182+0000`.
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.UserSearchCriteria`
        :param ExpectedFields: User attributes expected to be returned. All built-in user attributes will be returned by default, including user UUID (UserId), nickname (DisplayName), username (UserName), mobile number (Phone), email address (Email), status (Status), user group (SubjectGroups), organization path (OrgPath), remarks (Description), creation time (CreationTime), last modification time (LastUpdateTime), and last login time (LastLoginTime).
        :type ExpectedFields: list of str
        :param Sort: Set of sort criteria. The supported attributes for sorting include username (UserName), nickname (DisplayName), mobile number (Phone), email address (Email), user status (Status), creation time (CreatedDate), last modification time (LastUpdateTime), and last login time (LastLoginTime). If this field is left empty, the results will be sorted in alphabetical order by nickname (DisplayName).
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param Offset: Pagination offset. Default value: 0. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated, and up to 1,000 users will be returned.
        :type Offset: int
        :param Limit: Number of results read per page. Default value: 50. Maximum value: 100. The `Offset` and `Limit` fields need to be used together; otherwise, the query results will not be paginated, and up to 1,000 users will be returned.
        :type Limit: int
        :param IncludeTotal: Whether to view the total number of search results. Default value: false (no).
        :type IncludeTotal: bool
        """
        self.SearchCondition = None
        self.ExpectedFields = None
        self.Sort = None
        self.Offset = None
        self.Limit = None
        self.IncludeTotal = None


    def _deserialize(self, params):
        if params.get("SearchCondition") is not None:
            self.SearchCondition = UserSearchCriteria()
            self.SearchCondition._deserialize(params.get("SearchCondition"))
        self.ExpectedFields = params.get("ExpectedFields")
        if params.get("Sort") is not None:
            self.Sort = SortCondition()
            self.Sort._deserialize(params.get("Sort"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.IncludeTotal = params.get("IncludeTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersResponse(AbstractModel):
    """ListUsers response structure.

    """

    def __init__(self):
        r"""
        :param UserList: List of users returned for the query.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserList: list of UserInformation
        :param TotalCount: Total number of users returned for the query, which will be returned only when the `IncludeTotal` input parameter is set to `true`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UserList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UserList") is not None:
            self.UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self.UserList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ModifyAccountGroupRequest(AbstractModel):
    """ModifyAccountGroup request structure.

    """

    def __init__(self):
        r"""
        :param AccountGroupId: Account group ID.
        :type AccountGroupId: str
        :param GroupName: Account group name. When this parameter is not specified, the name will not be modified.
        :type GroupName: str
        :param Description: Description. When this parameter is not specified, the description will not be modified.
        :type Description: str
        """
        self.AccountGroupId = None
        self.GroupName = None
        self.Description = None


    def _deserialize(self, params):
        self.AccountGroupId = params.get("AccountGroupId")
        self.GroupName = params.get("GroupName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountGroupResponse(AbstractModel):
    """ModifyAccountGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAppAccountRequest(AbstractModel):
    """ModifyAppAccount request structure.

    """

    def __init__(self):
        r"""
        :param AccountId: Account ID.
        :type AccountId: str
        :param AccountName: Account name. When this parameter is not specified, the name will not be modified.
        :type AccountName: str
        :param Password: Account password. When this parameter is not specified, the password will not be changed.
        :type Password: str
        :param Description: Description. When this parameter is not specified, the description will not be modified.
        :type Description: str
        """
        self.AccountId = None
        self.AccountName = None
        self.Password = None
        self.Description = None


    def _deserialize(self, params):
        self.AccountId = params.get("AccountId")
        self.AccountName = params.get("AccountName")
        self.Password = params.get("Password")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppAccountResponse(AbstractModel):
    """ModifyAppAccount response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApplicationRequest(AbstractModel):
    """ModifyApplication request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID, which is globally unique.
        :type ApplicationId: str
        :param SecureLevel: Security level.
        :type SecureLevel: str
        :param DisplayName: Displayed application name, which can contain up to 32 characters and is the same as the application name by default.
        :type DisplayName: str
        :param AppStatus: Application status. Valid values: true: enabled; false: disabled.
        :type AppStatus: bool
        :param IconUrl: Access address of the application icon image.
        :type IconUrl: str
        :param Description: Description, which can contain up to 128 characters.
        :type Description: str
        """
        self.ApplicationId = None
        self.SecureLevel = None
        self.DisplayName = None
        self.AppStatus = None
        self.IconUrl = None
        self.Description = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SecureLevel = params.get("SecureLevel")
        self.DisplayName = params.get("DisplayName")
        self.AppStatus = params.get("AppStatus")
        self.IconUrl = params.get("IconUrl")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationResponse(AbstractModel):
    """ModifyApplication response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyUserInfoRequest(AbstractModel):
    """ModifyUserInfo request structure.

    """

    def __init__(self):
        r"""
        :param UserName: Username, which can contain up to 32 characters. You need to select either `Username` or `UserId` as the search criterion; if both are selected, `Username` will be used by default.
        :type UserName: str
        :param DisplayName: Nickname, which can contain up to 64 characters and is the same as the username by default.
        :type DisplayName: str
        :param Description: User remarks, which can contain up to 512 characters.
        :type Description: str
        :param UserGroupIds: List of IDs of the user's user groups.
        :type UserGroupIds: list of str
        :param UserId: User ID. You need to select either `UserName` or `UserId` as the search criterion. If both are selected, `UserName` will be used by default.
        :type UserId: str
        :param Phone: User's mobile number.
        :type Phone: str
        :param ExpirationTime: User expiration time in ISO 8601 format.
        :type ExpirationTime: str
        :param Password: User password, which needs to be configured according to the password policy.
        :type Password: str
        :param Email: User's email address.
        :type Email: str
        :param PwdNeedReset: Whether the password needs to be reset. Default value: false (no).
        :type PwdNeedReset: bool
        :param OrgNodeId: Unique ID of the user's primary organization. If this parameter is left empty, the user will be created under the root node by default.
        :type OrgNodeId: str
        :param SecondaryOrgNodeIdList: List of IDs of the user's secondary organizations.
        :type SecondaryOrgNodeIdList: list of str
        """
        self.UserName = None
        self.DisplayName = None
        self.Description = None
        self.UserGroupIds = None
        self.UserId = None
        self.Phone = None
        self.ExpirationTime = None
        self.Password = None
        self.Email = None
        self.PwdNeedReset = None
        self.OrgNodeId = None
        self.SecondaryOrgNodeIdList = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.DisplayName = params.get("DisplayName")
        self.Description = params.get("Description")
        self.UserGroupIds = params.get("UserGroupIds")
        self.UserId = params.get("UserId")
        self.Phone = params.get("Phone")
        self.ExpirationTime = params.get("ExpirationTime")
        self.Password = params.get("Password")
        self.Email = params.get("Email")
        self.PwdNeedReset = params.get("PwdNeedReset")
        self.OrgNodeId = params.get("OrgNodeId")
        self.SecondaryOrgNodeIdList = params.get("SecondaryOrgNodeIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserInfoResponse(AbstractModel):
    """ModifyUserInfo response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OrgNodeChildInfo(AbstractModel):
    """List of sub-nodes under the current organization node

    """

    def __init__(self):
        r"""
        :param DisplayName: Displayed organization node name, which can contain up to 64 characters and is the same as the organization name by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param LastModifiedDate: Last modification time of the organization node in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifiedDate: str
        :param CustomizedOrgNodeId: External ID of the organization node, which is optional and customizable.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CustomizedOrgNodeId: str
        :param ParentOrgNodeId: Parent node ID of the current organization node.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ParentOrgNodeId: str
        :param OrgNodeId: Organization node ID, which is globally unique.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeId: str
        :param DataSource: Data source.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DataSource: str
        :param CreatedDate: Organization node creation time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedDate: str
        :param Description: Organization node description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        """
        self.DisplayName = None
        self.LastModifiedDate = None
        self.CustomizedOrgNodeId = None
        self.ParentOrgNodeId = None
        self.OrgNodeId = None
        self.DataSource = None
        self.CreatedDate = None
        self.Description = None


    def _deserialize(self, params):
        self.DisplayName = params.get("DisplayName")
        self.LastModifiedDate = params.get("LastModifiedDate")
        self.CustomizedOrgNodeId = params.get("CustomizedOrgNodeId")
        self.ParentOrgNodeId = params.get("ParentOrgNodeId")
        self.OrgNodeId = params.get("OrgNodeId")
        self.DataSource = params.get("DataSource")
        self.CreatedDate = params.get("CreatedDate")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgNodeChildUserInfo(AbstractModel):
    """User information list under the organization sub-node

    """

    def __init__(self):
        r"""
        :param OrgNodeId: Organization node ID, which is globally unique and can contain up to 64 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeId: str
        :param UserInfo: User information list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserInfo: list of UserInfo
        :param TotalUserNum: Total number of users under the current organization node.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalUserNum: int
        :param OrgNodeIdPath: Organization ID path.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeIdPath: str
        :param OrgNodeNamePath: Organization name path.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgNodeNamePath: str
        """
        self.OrgNodeId = None
        self.UserInfo = None
        self.TotalUserNum = None
        self.OrgNodeIdPath = None
        self.OrgNodeNamePath = None


    def _deserialize(self, params):
        self.OrgNodeId = params.get("OrgNodeId")
        if params.get("UserInfo") is not None:
            self.UserInfo = []
            for item in params.get("UserInfo"):
                obj = UserInfo()
                obj._deserialize(item)
                self.UserInfo.append(obj)
        self.TotalUserNum = params.get("TotalUserNum")
        self.OrgNodeIdPath = params.get("OrgNodeIdPath")
        self.OrgNodeNamePath = params.get("OrgNodeNamePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveAccountFromAccountGroupRequest(AbstractModel):
    """RemoveAccountFromAccountGroup request structure.

    """

    def __init__(self):
        r"""
        :param AccountGroupId: Account group ID
        :type AccountGroupId: str
        :param AccountIds: List of IDs of the accounts to be removed.
        :type AccountIds: list of str
        """
        self.AccountGroupId = None
        self.AccountIds = None


    def _deserialize(self, params):
        self.AccountGroupId = params.get("AccountGroupId")
        self.AccountIds = params.get("AccountIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveAccountFromAccountGroupResponse(AbstractModel):
    """RemoveAccountFromAccountGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveUserFromUserGroupRequest(AbstractModel):
    """RemoveUserFromUserGroup request structure.

    """

    def __init__(self):
        r"""
        :param UserIds: List of IDs of the users to be added to the user group.
        :type UserIds: list of str
        :param UserGroupId: User group ID, which is globally unique.
        :type UserGroupId: str
        """
        self.UserIds = None
        self.UserGroupId = None


    def _deserialize(self, params):
        self.UserIds = params.get("UserIds")
        self.UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserFromUserGroupResponse(AbstractModel):
    """RemoveUserFromUserGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SortCondition(AbstractModel):
    """Sort criterion.

    """

    def __init__(self):
        r"""
        :param SortKey: Sorting attribute.
        :type SortKey: str
        :param SortOrder: Sorting order. Valid values: ASC: ascending order; DESC: descending order.
        :type SortOrder: str
        """
        self.SortKey = None
        self.SortOrder = None


    def _deserialize(self, params):
        self.SortKey = params.get("SortKey")
        self.SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ThirdPartyAccountInfo(AbstractModel):
    """Third-Party account information.

    """

    def __init__(self):
        r"""
        :param AccountCode: Third-Party account code. `2` indicates WeCom account.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccountCode: str
        :param AccountName: Username of the account.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccountName: str
        """
        self.AccountCode = None
        self.AccountName = None


    def _deserialize(self, params):
        self.AccountCode = params.get("AccountCode")
        self.AccountName = params.get("AccountName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrgNodeRequest(AbstractModel):
    """UpdateOrgNode request structure.

    """

    def __init__(self):
        r"""
        :param OrgNodeId: Organization node ID, which is globally unique.
        :type OrgNodeId: str
        :param DisplayName: Organization node name, which can contain up to 64 characters.
        :type DisplayName: str
        :param Description: Organization node description.
        :type Description: str
        :param CustomizedOrgNodeId: External ID of the organization node, which is optional and customizable. If this parameter is specified, its uniqueness will be verified.
        :type CustomizedOrgNodeId: str
        """
        self.OrgNodeId = None
        self.DisplayName = None
        self.Description = None
        self.CustomizedOrgNodeId = None


    def _deserialize(self, params):
        self.OrgNodeId = params.get("OrgNodeId")
        self.DisplayName = params.get("DisplayName")
        self.Description = params.get("Description")
        self.CustomizedOrgNodeId = params.get("CustomizedOrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrgNodeResponse(AbstractModel):
    """UpdateOrgNode response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UserGroupInfo(AbstractModel):
    """Returned user group list.

    """

    def __init__(self):
        r"""
        :param DisplayName: Nickname, which can contain up to 64 characters and is the same as the username by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param UserGroupId: User group ID, which is globally unique and can contain up to 64 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserGroupId: str
        :param Description: User group remarks.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param CreatedDate: Creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedDate: str
        """
        self.DisplayName = None
        self.UserGroupId = None
        self.Description = None
        self.CreatedDate = None


    def _deserialize(self, params):
        self.DisplayName = params.get("DisplayName")
        self.UserGroupId = params.get("UserGroupId")
        self.Description = params.get("Description")
        self.CreatedDate = params.get("CreatedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserGroupInfoSearchCriteria(AbstractModel):
    """User group attribute search criteria.

    """

    def __init__(self):
        r"""
        :param Keyword: Search by name. The match criteria include user group name and user group ID.
        :type Keyword: str
        """
        self.Keyword = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserGroupInformation(AbstractModel):
    """Returned user group list.

    """

    def __init__(self):
        r"""
        :param UserGroupId: User group ID.
        :type UserGroupId: str
        :param UserGroupName: User group name.
        :type UserGroupName: str
        :param LastModifiedDate: Last update time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifiedDate: str
        """
        self.UserGroupId = None
        self.UserGroupName = None
        self.LastModifiedDate = None


    def _deserialize(self, params):
        self.UserGroupId = params.get("UserGroupId")
        self.UserGroupName = params.get("UserGroupName")
        self.LastModifiedDate = params.get("LastModifiedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserGroupInformationSearchCriteria(AbstractModel):
    """User group attribute search criteria in the list of the user's user groups.

    """

    def __init__(self):
        r"""
        :param Keyword: Search by name. The match criteria include user group name.
        :type Keyword: str
        """
        self.Keyword = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    """User information list.

    """

    def __init__(self):
        r"""
        :param UserId: User ID, which is globally unique and can contain up to 64 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param DisplayName: Nickname, which can contain up to 64 characters and is the same as the username by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param UserName: Username.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param Phone: User's mobile number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Phone: str
        :param Email: Email address.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Email: str
        :param Status: User status.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param DataSource: Data source.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DataSource: str
        """
        self.UserId = None
        self.DisplayName = None
        self.UserName = None
        self.Phone = None
        self.Email = None
        self.Status = None
        self.DataSource = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.DisplayName = params.get("DisplayName")
        self.UserName = params.get("UserName")
        self.Phone = params.get("Phone")
        self.Email = params.get("Email")
        self.Status = params.get("Status")
        self.DataSource = params.get("DataSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInformation(AbstractModel):
    """User information list.

    """

    def __init__(self):
        r"""
        :param UserName: Username, which can contain up to 32 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param Status: User status.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param DisplayName: Nickname, which can contain up to 64 characters and is the same as the username by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DisplayName: str
        :param Description: User remarks, which can contain up to 512 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param LastUpdateTime: Last update time of the user in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastUpdateTime: str
        :param CreationTime: User creation time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreationTime: str
        :param OrgPath: Path ID of the user's primary organization.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrgPath: str
        :param Phone: User's mobile number with country code, such as `+86-00000000000`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Phone: str
        :param SubjectGroups: List of IDs of the user's user groups.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubjectGroups: list of str
        :param Email: User's email address.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Email: str
        :param LastLoginTime: Last login time of the user in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastLoginTime: str
        :param UserId: User ID, which is globally unique and can contain up to 64 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        """
        self.UserName = None
        self.Status = None
        self.DisplayName = None
        self.Description = None
        self.LastUpdateTime = None
        self.CreationTime = None
        self.OrgPath = None
        self.Phone = None
        self.SubjectGroups = None
        self.Email = None
        self.LastLoginTime = None
        self.UserId = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Status = params.get("Status")
        self.DisplayName = params.get("DisplayName")
        self.Description = params.get("Description")
        self.LastUpdateTime = params.get("LastUpdateTime")
        self.CreationTime = params.get("CreationTime")
        self.OrgPath = params.get("OrgPath")
        self.Phone = params.get("Phone")
        self.SubjectGroups = params.get("SubjectGroups")
        self.Email = params.get("Email")
        self.LastLoginTime = params.get("LastLoginTime")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserSearchCriteria(AbstractModel):
    """User attribute search criteria.

    """

    def __init__(self):
        r"""
        :param UserName: Username, which can contain up to 64 characters.
        :type UserName: str
        :param Phone: User's mobile number.
        :type Phone: str
        :param Email: User's email address.
        :type Email: str
        :param Status: User status. Valid values: NORMAL: normal; FREEZE: frozen; LOCKED: locked; NOT_ENABLED: disabled.
        :type Status: str
        :param CreationTime: User creation time in ISO 8601 format.
        :type CreationTime: str
        :param LastUpdateTime: The user's last update time.
        :type LastUpdateTime: str
        :param Keyword: Search by name. The match criteria include username and user ID.
        :type Keyword: str
        """
        self.UserName = None
        self.Phone = None
        self.Email = None
        self.Status = None
        self.CreationTime = None
        self.LastUpdateTime = None
        self.Keyword = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Phone = params.get("Phone")
        self.Email = params.get("Email")
        self.Status = params.get("Status")
        self.CreationTime = params.get("CreationTime")
        self.LastUpdateTime = params.get("LastUpdateTime")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        