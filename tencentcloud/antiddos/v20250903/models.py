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


class DDoSBlockRecord(AbstractModel):
    r"""Block history

    """

    def __init__(self):
        r"""
        :param _Resource: <p>Blocked resources, public IP address, for example:</p><ul><li>Public IP address: 117.175.94.231.</li></ul>
        :type Resource: str
        :param _BlockTime: <p>The time when it was blocked.</p>
        :type BlockTime: str
        :param _Status: <p>Blocking and unblocking status.</p><p>Enumeration value:</p><ul><li>Blocked: Blocked;</li><li>Unblocking: Unblocking;</li><li>Unblocked: Unblocked.</li></ul>
        :type Status: str
        """
        self._Resource = None
        self._BlockTime = None
        self._Status = None

    @property
    def Resource(self):
        r"""<p>Blocked resources, public IP address, for example:</p><ul><li>Public IP address: 117.175.94.231.</li></ul>
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def BlockTime(self):
        r"""<p>The time when it was blocked.</p>
        :rtype: str
        """
        return self._BlockTime

    @BlockTime.setter
    def BlockTime(self, BlockTime):
        self._BlockTime = BlockTime

    @property
    def Status(self):
        r"""<p>Blocking and unblocking status.</p><p>Enumeration value:</p><ul><li>Blocked: Blocked;</li><li>Unblocking: Unblocking;</li><li>Unblocked: Unblocked.</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._BlockTime = params.get("BlockTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSUnblockQuota(AbstractModel):
    r"""Unconsumed unblocking quota info of the current account. Users who purchase Anti-DDoS products have a default unblocking quota of 3 resources. The system will reset the unblocking quota count at zero point (UTC+8) time zone each day. Unused unblocking quota on the day will not accumulate to the next day. The unblocking quota for Anti-DDoS Package (Lite) is 3 resources per month and resets monthly.

    """

    def __init__(self):
        r"""
        :param _TotalQuota: <p>Total quota of the number of unblocking times.</p>
        :type TotalQuota: int
        :param _UsedQuota: <p>Total quota used.</p>
        :type UsedQuota: int
        :param _QuotaStartTime: <p>Start time when the quota takes effect.</p>
        :type QuotaStartTime: str
        :param _QuotaEndTime: <p>End time when the quota takes effect.</p>
        :type QuotaEndTime: str
        """
        self._TotalQuota = None
        self._UsedQuota = None
        self._QuotaStartTime = None
        self._QuotaEndTime = None

    @property
    def TotalQuota(self):
        r"""<p>Total quota of the number of unblocking times.</p>
        :rtype: int
        """
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def UsedQuota(self):
        r"""<p>Total quota used.</p>
        :rtype: int
        """
        return self._UsedQuota

    @UsedQuota.setter
    def UsedQuota(self, UsedQuota):
        self._UsedQuota = UsedQuota

    @property
    def QuotaStartTime(self):
        r"""<p>Start time when the quota takes effect.</p>
        :rtype: str
        """
        return self._QuotaStartTime

    @QuotaStartTime.setter
    def QuotaStartTime(self, QuotaStartTime):
        self._QuotaStartTime = QuotaStartTime

    @property
    def QuotaEndTime(self):
        r"""<p>End time when the quota takes effect.</p>
        :rtype: str
        """
        return self._QuotaEndTime

    @QuotaEndTime.setter
    def QuotaEndTime(self, QuotaEndTime):
        self._QuotaEndTime = QuotaEndTime


    def _deserialize(self, params):
        self._TotalQuota = params.get("TotalQuota")
        self._UsedQuota = params.get("UsedQuota")
        self._QuotaStartTime = params.get("QuotaStartTime")
        self._QuotaEndTime = params.get("QuotaEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSBlockRecordsRequest(AbstractModel):
    r"""DescribeDDoSBlockRecords request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: <p>Start time of the query. Support up to data query for the past one year.</p><p>Parameter format: 2026-02-04T11:30:00+08:00.</p>
        :type StartTime: str
        :param _EndTime: <p>End time of query. The query time range (EndTime - StartTime) must be less than or equal to 31 days.</p><p>Parameter format: 2026-03-04T11:30:00+08:00.</p>
        :type EndTime: str
        :param _Filters: <p>Filter criteria. The maximum number of Filters.Values is 20. If this parameter is left empty, return the current list of resources blocked under the appid. Detailed filter criteria:</p><ul><li> Resource: Filter by blocked IP or six-segment resource format;</li><li> Status: Filter by blocked resource status.</li></ul><p>When Filters.Name value is Status, Filters.Values valid values:</p><ul><li>Blocked: blocked;</li><li>Unblocking: unblocking;</li><li>Unblocked: unblocked.</li></ul>
        :type Filters: list of Filter
        :param _Limit: <p>Paginated query limit count. Maximum value: 100.</p><p>Default value: 20</p>
        :type Limit: int
        :param _Offset: <p>Paginated query offset.</p><p>Default value: 0.</p>
        :type Offset: int
        """
        self._StartTime = None
        self._EndTime = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def StartTime(self):
        r"""<p>Start time of the query. Support up to data query for the past one year.</p><p>Parameter format: 2026-02-04T11:30:00+08:00.</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>End time of query. The query time range (EndTime - StartTime) must be less than or equal to 31 days.</p><p>Parameter format: 2026-03-04T11:30:00+08:00.</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        r"""<p>Filter criteria. The maximum number of Filters.Values is 20. If this parameter is left empty, return the current list of resources blocked under the appid. Detailed filter criteria:</p><ul><li> Resource: Filter by blocked IP or six-segment resource format;</li><li> Status: Filter by blocked resource status.</li></ul><p>When Filters.Name value is Status, Filters.Values valid values:</p><ul><li>Blocked: blocked;</li><li>Unblocking: unblocking;</li><li>Unblocked: unblocked.</li></ul>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""<p>Paginated query limit count. Maximum value: 100.</p><p>Default value: 20</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>Paginated query offset.</p><p>Default value: 0.</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSBlockRecordsResponse(AbstractModel):
    r"""DescribeDDoSBlockRecords response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>Total number of block and unblock records.</p>
        :type TotalCount: int
        :param _BlockRecords: <p>Unblock record.</p>
        :type BlockRecords: list of DDoSBlockRecord
        :param _UnblockQuotaInfo: <p>Quota information of the number of unblocking times.</p>
        :type UnblockQuotaInfo: :class:`tencentcloud.antiddos.v20250903.models.DDoSUnblockQuota`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._BlockRecords = None
        self._UnblockQuotaInfo = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>Total number of block and unblock records.</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BlockRecords(self):
        r"""<p>Unblock record.</p>
        :rtype: list of DDoSBlockRecord
        """
        return self._BlockRecords

    @BlockRecords.setter
    def BlockRecords(self, BlockRecords):
        self._BlockRecords = BlockRecords

    @property
    def UnblockQuotaInfo(self):
        r"""<p>Quota information of the number of unblocking times.</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.DDoSUnblockQuota`
        """
        return self._UnblockQuotaInfo

    @UnblockQuotaInfo.setter
    def UnblockQuotaInfo(self, UnblockQuotaInfo):
        self._UnblockQuotaInfo = UnblockQuotaInfo

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
        self._TotalCount = params.get("TotalCount")
        if params.get("BlockRecords") is not None:
            self._BlockRecords = []
            for item in params.get("BlockRecords"):
                obj = DDoSBlockRecord()
                obj._deserialize(item)
                self._BlockRecords.append(obj)
        if params.get("UnblockQuotaInfo") is not None:
            self._UnblockQuotaInfo = DDoSUnblockQuota()
            self._UnblockQuotaInfo._deserialize(params.get("UnblockQuotaInfo"))
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    r"""Describe key-value pair filter, used for condition filtering query, such as filtering ID, name, status. When multiple Filters exist, the relationship between Filters is logical AND. When the same Filter has multiple Values, the relationship between Values under the same Filter is logical OR.

    """

    def __init__(self):
        r"""
        :param _Name: <p>Fields to be filtered. Check corresponding API for specific available values.</p>
        :type Name: str
        :param _Values: <p>Field's filter value.</p>
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""<p>Fields to be filtered. Check corresponding API for specific available values.</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""<p>Field's filter value.</p>
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnblockResourcesRequest(AbstractModel):
    r"""UnblockResources request structure.

    """

    def __init__(self):
        r"""
        :param _Resources: <p>List of resources to apply for unblocking. Supports unblocking based on public IP. You can obtain detailed resource information of blocked resources through the DescribeDDoSBlockRecords API. Parameter example:</p><ul><li>Public IP: 117.175.94.230.</li></ul><p>Input parameter limit: Maximum list length is 10.</p>
        :type Resources: list of str
        """
        self._Resources = None

    @property
    def Resources(self):
        r"""<p>List of resources to apply for unblocking. Supports unblocking based on public IP. You can obtain detailed resource information of blocked resources through the DescribeDDoSBlockRecords API. Parameter example:</p><ul><li>Public IP: 117.175.94.230.</li></ul><p>Input parameter limit: Maximum list length is 10.</p>
        :rtype: list of str
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources


    def _deserialize(self, params):
        self._Resources = params.get("Resources")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnblockResourcesResponse(AbstractModel):
    r"""UnblockResources response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")