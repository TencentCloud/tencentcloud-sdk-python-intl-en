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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class CloudDedicatedZoneResourceStatisticsInfo(AbstractModel):
    r"""Details of the queried data for the statistical item of the CDZ resource, corresponding to a specific vertical product resource statistics.

    """

    def __init__(self):
        r"""
        :param _Item: Specifies the item name of resource statistics.
        :type Item: str
        :param _Unit: Resource statistics item measurement unit.
        :type Unit: str
        :param _Total: Total resource amount.
        :type Total: str
        :param _Usage: Used resources.
        :type Usage: str
        :param _UsageRate: Specifies the percentage of used resources.
        :type UsageRate: str
        :param _Remain: Remaining resource.
        :type Remain: str
        :param _RemainRate: Remaining resource percentage.
        :type RemainRate: str
        :param _ThisMondayUsageRate: Resource utilization rate at midnight this monday.
        :type ThisMondayUsageRate: str
        :param _ThisMondayUsageGrowthRate: Resource growth rate this week.
        :type ThisMondayUsageGrowthRate: str
        :param _LastMondayUsageGrowthRate: Resource growth rate last week.
        :type LastMondayUsageGrowthRate: str
        """
        self._Item = None
        self._Unit = None
        self._Total = None
        self._Usage = None
        self._UsageRate = None
        self._Remain = None
        self._RemainRate = None
        self._ThisMondayUsageRate = None
        self._ThisMondayUsageGrowthRate = None
        self._LastMondayUsageGrowthRate = None

    @property
    def Item(self):
        r"""Specifies the item name of resource statistics.
        :rtype: str
        """
        return self._Item

    @Item.setter
    def Item(self, Item):
        self._Item = Item

    @property
    def Unit(self):
        r"""Resource statistics item measurement unit.
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Total(self):
        r"""Total resource amount.
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Usage(self):
        r"""Used resources.
        :rtype: str
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def UsageRate(self):
        r"""Specifies the percentage of used resources.
        :rtype: str
        """
        return self._UsageRate

    @UsageRate.setter
    def UsageRate(self, UsageRate):
        self._UsageRate = UsageRate

    @property
    def Remain(self):
        r"""Remaining resource.
        :rtype: str
        """
        return self._Remain

    @Remain.setter
    def Remain(self, Remain):
        self._Remain = Remain

    @property
    def RemainRate(self):
        r"""Remaining resource percentage.
        :rtype: str
        """
        return self._RemainRate

    @RemainRate.setter
    def RemainRate(self, RemainRate):
        self._RemainRate = RemainRate

    @property
    def ThisMondayUsageRate(self):
        r"""Resource utilization rate at midnight this monday.
        :rtype: str
        """
        return self._ThisMondayUsageRate

    @ThisMondayUsageRate.setter
    def ThisMondayUsageRate(self, ThisMondayUsageRate):
        self._ThisMondayUsageRate = ThisMondayUsageRate

    @property
    def ThisMondayUsageGrowthRate(self):
        r"""Resource growth rate this week.
        :rtype: str
        """
        return self._ThisMondayUsageGrowthRate

    @ThisMondayUsageGrowthRate.setter
    def ThisMondayUsageGrowthRate(self, ThisMondayUsageGrowthRate):
        self._ThisMondayUsageGrowthRate = ThisMondayUsageGrowthRate

    @property
    def LastMondayUsageGrowthRate(self):
        r"""Resource growth rate last week.
        :rtype: str
        """
        return self._LastMondayUsageGrowthRate

    @LastMondayUsageGrowthRate.setter
    def LastMondayUsageGrowthRate(self, LastMondayUsageGrowthRate):
        self._LastMondayUsageGrowthRate = LastMondayUsageGrowthRate


    def _deserialize(self, params):
        self._Item = params.get("Item")
        self._Unit = params.get("Unit")
        self._Total = params.get("Total")
        self._Usage = params.get("Usage")
        self._UsageRate = params.get("UsageRate")
        self._Remain = params.get("Remain")
        self._RemainRate = params.get("RemainRate")
        self._ThisMondayUsageRate = params.get("ThisMondayUsageRate")
        self._ThisMondayUsageGrowthRate = params.get("ThisMondayUsageGrowthRate")
        self._LastMondayUsageGrowthRate = params.get("LastMondayUsageGrowthRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudDedicatedZoneResourceSummaryInfo(AbstractModel):
    r"""Details of the CDZ resource water level, corresponding to a specific vertical product.

    """

    def __init__(self):
        r"""
        :param _ProductName: Product name
        :type ProductName: str
        :param _SubProductName: Subproduct name
        :type SubProductName: str
        :param _Statistics: Statistical detail of the resource.
        :type Statistics: list of CloudDedicatedZoneResourceStatisticsInfo
        """
        self._ProductName = None
        self._SubProductName = None
        self._Statistics = None

    @property
    def ProductName(self):
        r"""Product name
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def SubProductName(self):
        r"""Subproduct name
        :rtype: str
        """
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName

    @property
    def Statistics(self):
        r"""Statistical detail of the resource.
        :rtype: list of CloudDedicatedZoneResourceStatisticsInfo
        """
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._SubProductName = params.get("SubProductName")
        if params.get("Statistics") is not None:
            self._Statistics = []
            for item in params.get("Statistics"):
                obj = CloudDedicatedZoneResourceStatisticsInfo()
                obj._deserialize(item)
                self._Statistics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudDedicatedZoneResourceSummaryRequest(AbstractModel):
    r"""DescribeCloudDedicatedZoneResourceSummary request structure.

    """

    def __init__(self):
        r"""
        :param _CdzId: Unique id of the cloud dedicated zone.
        :type CdzId: str
        """
        self._CdzId = None

    @property
    def CdzId(self):
        r"""Unique id of the cloud dedicated zone.
        :rtype: str
        """
        return self._CdzId

    @CdzId.setter
    def CdzId(self, CdzId):
        self._CdzId = CdzId


    def _deserialize(self, params):
        self._CdzId = params.get("CdzId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudDedicatedZoneResourceSummaryResponse(AbstractModel):
    r"""DescribeCloudDedicatedZoneResourceSummary response structure.

    """

    def __init__(self):
        r"""
        :param _ResourceSummarySet: Resource utilization.
        :type ResourceSummarySet: list of CloudDedicatedZoneResourceSummaryInfo
        :param _ExtraInfo: Extended information of resource utilization.
        :type ExtraInfo: :class:`tencentcloud.cdz.v20221123.models.ExtraInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ResourceSummarySet = None
        self._ExtraInfo = None
        self._RequestId = None

    @property
    def ResourceSummarySet(self):
        r"""Resource utilization.
        :rtype: list of CloudDedicatedZoneResourceSummaryInfo
        """
        return self._ResourceSummarySet

    @ResourceSummarySet.setter
    def ResourceSummarySet(self, ResourceSummarySet):
        self._ResourceSummarySet = ResourceSummarySet

    @property
    def ExtraInfo(self):
        r"""Extended information of resource utilization.
        :rtype: :class:`tencentcloud.cdz.v20221123.models.ExtraInfo`
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResourceSummarySet") is not None:
            self._ResourceSummarySet = []
            for item in params.get("ResourceSummarySet"):
                obj = CloudDedicatedZoneResourceSummaryInfo()
                obj._deserialize(item)
                self._ResourceSummarySet.append(obj)
        if params.get("ExtraInfo") is not None:
            self._ExtraInfo = ExtraInfo()
            self._ExtraInfo._deserialize(params.get("ExtraInfo"))
        self._RequestId = params.get("RequestId")


class ExtraInfo(AbstractModel):
    r"""Extended information of CDZ resource water level data, including availability zone local time and wait for data.

    """

    def __init__(self):
        r"""
        :param _ThisMondayLocalDate: Cloud dedicated zone local time this monday date.
        :type ThisMondayLocalDate: str
        :param _LastMondayLocalDate: Cloud dedicated zone local time last monday date.
        :type LastMondayLocalDate: str
        """
        self._ThisMondayLocalDate = None
        self._LastMondayLocalDate = None

    @property
    def ThisMondayLocalDate(self):
        r"""Cloud dedicated zone local time this monday date.
        :rtype: str
        """
        return self._ThisMondayLocalDate

    @ThisMondayLocalDate.setter
    def ThisMondayLocalDate(self, ThisMondayLocalDate):
        self._ThisMondayLocalDate = ThisMondayLocalDate

    @property
    def LastMondayLocalDate(self):
        r"""Cloud dedicated zone local time last monday date.
        :rtype: str
        """
        return self._LastMondayLocalDate

    @LastMondayLocalDate.setter
    def LastMondayLocalDate(self, LastMondayLocalDate):
        self._LastMondayLocalDate = LastMondayLocalDate


    def _deserialize(self, params):
        self._ThisMondayLocalDate = params.get("ThisMondayLocalDate")
        self._LastMondayLocalDate = params.get("LastMondayLocalDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        