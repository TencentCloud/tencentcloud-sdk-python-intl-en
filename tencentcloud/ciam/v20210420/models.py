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
        :param UserStoreId: User directory ID
        :type UserStoreId: str
        :param Page: Number of queried pages
        :type Page: int
        :param Size: Number of entries per page
        :type Size: int
        :param Condition: Query conditions (user group ID or user group name)
        :type Condition: str
        """
        self.UserStoreId = None
        self.Page = None
        self.Size = None
        self.Condition = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        self.Page = params.get("Page")
        self.Size = params.get("Size")
        self.Condition = params.get("Condition")
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
        :param Content: User group list
Note: this field may return null, indicating that no valid values can be obtained.
        :type Content: list of UserGroup
        :param Total: Total number
Note: this field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param Pageable: Pagination
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pageable: :class:`tencentcloud.ciam.v20210420.models.Pageable`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Content = None
        self.Total = None
        self.Pageable = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = UserGroup()
                obj._deserialize(item)
                self.Content.append(obj)
        self.Total = params.get("Total")
        if params.get("Pageable") is not None:
            self.Pageable = Pageable()
            self.Pageable._deserialize(params.get("Pageable"))
        self.RequestId = params.get("RequestId")


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
        


class UserGroup(AbstractModel):
    """User group

    """

    def __init__(self):
        r"""
        :param UserGroupId: User group ID
        :type UserGroupId: str
        :param DisplayName: User group name
        :type DisplayName: str
        :param Description: User group description
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param UserStoreId: User directory ID
        :type UserStoreId: str
        :param TenantId: Tenant ID
        :type TenantId: str
        """
        self.UserGroupId = None
        self.DisplayName = None
        self.Description = None
        self.UserStoreId = None
        self.TenantId = None


    def _deserialize(self, params):
        self.UserGroupId = params.get("UserGroupId")
        self.DisplayName = params.get("DisplayName")
        self.Description = params.get("Description")
        self.UserStoreId = params.get("UserStoreId")
        self.TenantId = params.get("TenantId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        