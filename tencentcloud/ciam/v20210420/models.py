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


class ListUserGroupsRequest(AbstractModel):
    """ListUserGroups request structure.

    """

    def __init__(self):
        r"""
        :param _UserStoreId: User directory ID
        :type UserStoreId: str
        :param _Page: Number of queried pages
        :type Page: int
        :param _Size: Number of entries per page
        :type Size: int
        :param _Condition: Query conditions (user group ID or user group name)
        :type Condition: str
        """
        self._UserStoreId = None
        self._Page = None
        self._Size = None
        self._Condition = None

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._Page = params.get("Page")
        self._Size = params.get("Size")
        self._Condition = params.get("Condition")
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
        :param _Content: User group list
Note: this field may return null, indicating that no valid values can be obtained.
        :type Content: list of UserGroup
        :param _Total: Total number
Note: this field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _Pageable: Pagination
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pageable: :class:`tencentcloud.ciam.v20210420.models.Pageable`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Content = None
        self._Total = None
        self._Pageable = None
        self._RequestId = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Pageable(self):
        return self._Pageable

    @Pageable.setter
    def Pageable(self, Pageable):
        self._Pageable = Pageable

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = UserGroup()
                obj._deserialize(item)
                self._Content.append(obj)
        self._Total = params.get("Total")
        if params.get("Pageable") is not None:
            self._Pageable = Pageable()
            self._Pageable._deserialize(params.get("Pageable"))
        self._RequestId = params.get("RequestId")


class Pageable(AbstractModel):
    """Pagination object

    """

    def __init__(self):
        r"""
        :param _PageSize: Number of entries per page
        :type PageSize: int
        :param _PageNumber: Current page number
        :type PageNumber: int
        """
        self._PageSize = None
        self._PageNumber = None

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserGroup(AbstractModel):
    """User group

    """

    def __init__(self):
        r"""
        :param _UserGroupId: User group ID
        :type UserGroupId: str
        :param _DisplayName: User group name
        :type DisplayName: str
        :param _Description: User group description
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _UserStoreId: User directory ID
        :type UserStoreId: str
        :param _TenantId: Tenant ID
        :type TenantId: str
        """
        self._UserGroupId = None
        self._DisplayName = None
        self._Description = None
        self._UserStoreId = None
        self._TenantId = None

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

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
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def TenantId(self):
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._UserStoreId = params.get("UserStoreId")
        self._TenantId = params.get("TenantId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        