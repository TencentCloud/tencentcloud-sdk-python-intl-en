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


class BaselineConfigItem(AbstractModel):
    """Account Factory baseline configuration item.

    """

    def __init__(self):
        r"""
        :param _Identifier: A unique identifier for an Account Factory baseline item, which can only contain English letters, digits, and @,._[]-:()+=. It must be 2-128 characters long.Note: This field may return null, indicating that no valid values can be obtained.
        :type Identifier: str
        :param _Configuration: Account Factory baseline item configuration. Different items have different parameters.Note: This field may return null, indicating that no valid values can be obtained.
        :type Configuration: str
        """
        self._Identifier = None
        self._Configuration = None

    @property
    def Identifier(self):
        """A unique identifier for an Account Factory baseline item, which can only contain English letters, digits, and @,._[]-:()+=. It must be 2-128 characters long.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def Configuration(self):
        """Account Factory baseline item configuration. Different items have different parameters.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration


    def _deserialize(self, params):
        self._Identifier = params.get("Identifier")
        self._Configuration = params.get("Configuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchApplyAccountBaselinesRequest(AbstractModel):
    """BatchApplyAccountBaselines request structure.

    """

    def __init__(self):
        r"""
        :param _MemberUinList: Member account UIN, which is also the UIN of the account to which the baseline is applied.
        :type MemberUinList: list of int
        :param _BaselineConfigItems: List of baseline item configuration information.
        :type BaselineConfigItems: list of BaselineConfigItem
        """
        self._MemberUinList = None
        self._BaselineConfigItems = None

    @property
    def MemberUinList(self):
        """Member account UIN, which is also the UIN of the account to which the baseline is applied.
        :rtype: list of int
        """
        return self._MemberUinList

    @MemberUinList.setter
    def MemberUinList(self, MemberUinList):
        self._MemberUinList = MemberUinList

    @property
    def BaselineConfigItems(self):
        """List of baseline item configuration information.
        :rtype: list of BaselineConfigItem
        """
        return self._BaselineConfigItems

    @BaselineConfigItems.setter
    def BaselineConfigItems(self, BaselineConfigItems):
        self._BaselineConfigItems = BaselineConfigItems


    def _deserialize(self, params):
        self._MemberUinList = params.get("MemberUinList")
        if params.get("BaselineConfigItems") is not None:
            self._BaselineConfigItems = []
            for item in params.get("BaselineConfigItems"):
                obj = BaselineConfigItem()
                obj._deserialize(item)
                self._BaselineConfigItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchApplyAccountBaselinesResponse(AbstractModel):
    """BatchApplyAccountBaselines response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")