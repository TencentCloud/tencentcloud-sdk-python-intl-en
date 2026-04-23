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


class Alarm(AbstractModel):
    r"""Alarm Rule Details

    """

    def __init__(self):
        r"""
        :param _Id: Alarm rule ID.
        :type Id: int
        :param _Name: Alarm rule name.
        :type Name: str
        :param _ProductId: Product ID
        :type ProductId: int
        :param _QuotaId: Quota ID.
        :type QuotaId: int
        :param _Metrics: Alarm condition.
        :type Metrics: int
        :param _Frequency: Alarm frequency.
        :type Frequency: int
        :param _Threshold: Specifies the Alarm threshold. valid values: 0-100.
        :type Threshold: int
        :param _OwnerUin: Creator UIN
        :type OwnerUin: int
        :param _MemberUin: Specifies the uin of the rule owner.
        :type MemberUin: int
        :param _QuotaName: Specifies the quota name.
        :type QuotaName: str
        :param _ProductName: Product name
        :type ProductName: str
        :param _Status: Whether to delete. 1: not deleted.
2: delete.
        :type Status: int
        """
        self._Id = None
        self._Name = None
        self._ProductId = None
        self._QuotaId = None
        self._Metrics = None
        self._Frequency = None
        self._Threshold = None
        self._OwnerUin = None
        self._MemberUin = None
        self._QuotaName = None
        self._ProductName = None
        self._Status = None

    @property
    def Id(self):
        r"""Alarm rule ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""Alarm rule name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProductId(self):
        r"""Product ID
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def QuotaId(self):
        r"""Quota ID.
        :rtype: int
        """
        return self._QuotaId

    @QuotaId.setter
    def QuotaId(self, QuotaId):
        self._QuotaId = QuotaId

    @property
    def Metrics(self):
        r"""Alarm condition.
        :rtype: int
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def Frequency(self):
        r"""Alarm frequency.
        :rtype: int
        """
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def Threshold(self):
        r"""Specifies the Alarm threshold. valid values: 0-100.
        :rtype: int
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def OwnerUin(self):
        r"""Creator UIN
        :rtype: int
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def MemberUin(self):
        r"""Specifies the uin of the rule owner.
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def QuotaName(self):
        r"""Specifies the quota name.
        :rtype: str
        """
        return self._QuotaName

    @QuotaName.setter
    def QuotaName(self, QuotaName):
        self._QuotaName = QuotaName

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
    def Status(self):
        r"""Whether to delete. 1: not deleted.
2: delete.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._ProductId = params.get("ProductId")
        self._QuotaId = params.get("QuotaId")
        self._Metrics = params.get("Metrics")
        self._Frequency = params.get("Frequency")
        self._Threshold = params.get("Threshold")
        self._OwnerUin = params.get("OwnerUin")
        self._MemberUin = params.get("MemberUin")
        self._QuotaName = params.get("QuotaName")
        self._ProductName = params.get("ProductName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmRequest(AbstractModel):
    r"""CreateAlarm request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Alarm rule name. specifies the name of the Alarm rule
        :type Name: str
        :param _ProductId: Product ID.
        :type ProductId: int
        :param _QuotaId: Quota ID.
        :type QuotaId: int
        :param _Metrics: Alert metrics 1: quota usage 2: quota usage rate 3: remaining quota 4: remaining quota rate.
        :type Metrics: int
        :param _Threshold: Specifies the Alarm threshold. value range: 0-100.
        :type Threshold: int
        :param _Frequency: Alarm frequency.
        :type Frequency: int
        :param _MemberUin:   Member UIN.
        :type MemberUin: int
        """
        self._Name = None
        self._ProductId = None
        self._QuotaId = None
        self._Metrics = None
        self._Threshold = None
        self._Frequency = None
        self._MemberUin = None

    @property
    def Name(self):
        r"""Alarm rule name. specifies the name of the Alarm rule
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProductId(self):
        r"""Product ID.
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def QuotaId(self):
        r"""Quota ID.
        :rtype: int
        """
        return self._QuotaId

    @QuotaId.setter
    def QuotaId(self, QuotaId):
        self._QuotaId = QuotaId

    @property
    def Metrics(self):
        r"""Alert metrics 1: quota usage 2: quota usage rate 3: remaining quota 4: remaining quota rate.
        :rtype: int
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def Threshold(self):
        r"""Specifies the Alarm threshold. value range: 0-100.
        :rtype: int
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Frequency(self):
        r"""Alarm frequency.
        :rtype: int
        """
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def MemberUin(self):
        r"""  Member UIN.
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ProductId = params.get("ProductId")
        self._QuotaId = params.get("QuotaId")
        self._Metrics = params.get("Metrics")
        self._Threshold = params.get("Threshold")
        self._Frequency = params.get("Frequency")
        self._MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmResponse(AbstractModel):
    r"""CreateAlarm response structure.

    """

    def __init__(self):
        r"""
        :param _AlarmId: 1001
        :type AlarmId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AlarmId = None
        self._RequestId = None

    @property
    def AlarmId(self):
        r"""1001
        :rtype: int
        """
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId

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
        self._AlarmId = params.get("AlarmId")
        self._RequestId = params.get("RequestId")


class DeleteAlarmRequest(AbstractModel):
    r"""DeleteAlarm request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Rule ID
        :type Id: int
        :param _MemberUin: Specifies the member uin of the rule owner.
        :type MemberUin: int
        """
        self._Id = None
        self._MemberUin = None

    @property
    def Id(self):
        r"""Rule ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MemberUin(self):
        r"""Specifies the member uin of the rule owner.
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmResponse(AbstractModel):
    r"""DeleteAlarm response structure.

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


class DescribeAggregateUserQuotasRequest(AbstractModel):
    r"""DescribeAggregateUserQuotas request structure.

    """

    def __init__(self):
        r"""
        :param _MemberUins: Member account. Can be empty. If empty, query the current account list.
        :type MemberUins: list of int
        :param _Limit: limit
        :type Limit: int
        :param _Offset: offset
        :type Offset: int
        :param _Filter: Filter
        :type Filter: list of Filter
        :param _Sort: sort
        :type Sort: list of Sort
        :param _ProductId: Product ID
        :type ProductId: int
        :param _QuotaDimensions: Quota dimension
        :type QuotaDimensions: list of QuotaDimension
        """
        self._MemberUins = None
        self._Limit = None
        self._Offset = None
        self._Filter = None
        self._Sort = None
        self._ProductId = None
        self._QuotaDimensions = None

    @property
    def MemberUins(self):
        r"""Member account. Can be empty. If empty, query the current account list.
        :rtype: list of int
        """
        return self._MemberUins

    @MemberUins.setter
    def MemberUins(self, MemberUins):
        self._MemberUins = MemberUins

    @property
    def Limit(self):
        r"""limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filter(self):
        r"""Filter
        :rtype: list of Filter
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Sort(self):
        r"""sort
        :rtype: list of Sort
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def ProductId(self):
        r"""Product ID
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def QuotaDimensions(self):
        r"""Quota dimension
        :rtype: list of QuotaDimension
        """
        return self._QuotaDimensions

    @QuotaDimensions.setter
    def QuotaDimensions(self, QuotaDimensions):
        self._QuotaDimensions = QuotaDimensions


    def _deserialize(self, params):
        self._MemberUins = params.get("MemberUins")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self._Filter.append(obj)
        if params.get("Sort") is not None:
            self._Sort = []
            for item in params.get("Sort"):
                obj = Sort()
                obj._deserialize(item)
                self._Sort.append(obj)
        self._ProductId = params.get("ProductId")
        if params.get("QuotaDimensions") is not None:
            self._QuotaDimensions = []
            for item in params.get("QuotaDimensions"):
                obj = QuotaDimension()
                obj._deserialize(item)
                self._QuotaDimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAggregateUserQuotasResponse(AbstractModel):
    r"""DescribeAggregateUserQuotas response structure.

    """

    def __init__(self):
        r"""
        :param _OwnerUin: Quota Id
        :type OwnerUin: int
        :param _Count: quota name
        :type Count: int
        :param _Data: Quota dimension
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of UserQuota
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OwnerUin = None
        self._Count = None
        self._Data = None
        self._RequestId = None

    @property
    def OwnerUin(self):
        r"""Quota Id
        :rtype: int
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Count(self):
        r"""quota name
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Data(self):
        r"""Quota dimension
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of UserQuota
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._OwnerUin = params.get("OwnerUin")
        self._Count = params.get("Count")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = UserQuota()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAlarmsRequest(AbstractModel):
    r"""DescribeAlarms request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of items per page. maximum 100.
        :type Limit: int
        :param _Offset: Offset.
        :type Offset: int
        :param _ProductId: Product ID.
        :type ProductId: int
        :param _QuotaId: Quota ID.
        :type QuotaId: int
        :param _Content: Alarm, quota name.
        :type Content: str
        :param _MemberUins: Member uins.
        :type MemberUins: list of int
        :param _Metrics: AlAlarm metric.
        :type Metrics: int
        :param _Id: Rule ID
        :type Id: int
        """
        self._Limit = None
        self._Offset = None
        self._ProductId = None
        self._QuotaId = None
        self._Content = None
        self._MemberUins = None
        self._Metrics = None
        self._Id = None

    @property
    def Limit(self):
        r"""Number of items per page. maximum 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ProductId(self):
        r"""Product ID.
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def QuotaId(self):
        r"""Quota ID.
        :rtype: int
        """
        return self._QuotaId

    @QuotaId.setter
    def QuotaId(self, QuotaId):
        self._QuotaId = QuotaId

    @property
    def Content(self):
        r"""Alarm, quota name.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def MemberUins(self):
        r"""Member uins.
        :rtype: list of int
        """
        return self._MemberUins

    @MemberUins.setter
    def MemberUins(self, MemberUins):
        self._MemberUins = MemberUins

    @property
    def Metrics(self):
        r"""AlAlarm metric.
        :rtype: int
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def Id(self):
        r"""Rule ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ProductId = params.get("ProductId")
        self._QuotaId = params.get("QuotaId")
        self._Content = params.get("Content")
        self._MemberUins = params.get("MemberUins")
        self._Metrics = params.get("Metrics")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmsResponse(AbstractModel):
    r"""DescribeAlarms response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Total number.
        :type Count: int
        :param _Data: List of rules
        :type Data: list of Alarm
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._Data = None
        self._RequestId = None

    @property
    def Count(self):
        r"""Total number.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Data(self):
        r"""List of rules
        :rtype: list of Alarm
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Count = params.get("Count")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = Alarm()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserQuotaRequest(AbstractModel):
    r"""DescribeUserQuota request structure.

    """

    def __init__(self):
        r"""
        :param _ProductName: Product name
        :type ProductName: str
        :param _QuotaId: Quota id
        :type QuotaId: :class:`tencentcloud.quota.v20241204.models.Sort`
        :param _QuotaInstanceId: Quota ID of each product
        :type QuotaInstanceId: str
        """
        self._ProductName = None
        self._QuotaId = None
        self._QuotaInstanceId = None

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
    def QuotaId(self):
        r"""Quota id
        :rtype: :class:`tencentcloud.quota.v20241204.models.Sort`
        """
        return self._QuotaId

    @QuotaId.setter
    def QuotaId(self, QuotaId):
        self._QuotaId = QuotaId

    @property
    def QuotaInstanceId(self):
        r"""Quota ID of each product
        :rtype: str
        """
        return self._QuotaInstanceId

    @QuotaInstanceId.setter
    def QuotaInstanceId(self, QuotaInstanceId):
        self._QuotaInstanceId = QuotaInstanceId


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        if params.get("QuotaId") is not None:
            self._QuotaId = Sort()
            self._QuotaId._deserialize(params.get("QuotaId"))
        self._QuotaInstanceId = params.get("QuotaInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserQuotaResponse(AbstractModel):
    r"""DescribeUserQuota response structure.

    """

    def __init__(self):
        r"""
        :param _QuotaId: Quota Id
        :type QuotaId: int
        :param _QuotaName: quota name
        :type QuotaName: str
        :param _ProductName: Product name
        :type ProductName: str
        :param _QuotaUnit: Quota unit
        :type QuotaUnit: str
        :param _TotalQuota: User Quota
        :type TotalQuota: int
        :param _TotalUsage: Quota usage
        :type TotalUsage: int
        :param _QuotaDescription: Quota description
        :type QuotaDescription: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._QuotaId = None
        self._QuotaName = None
        self._ProductName = None
        self._QuotaUnit = None
        self._TotalQuota = None
        self._TotalUsage = None
        self._QuotaDescription = None
        self._RequestId = None

    @property
    def QuotaId(self):
        r"""Quota Id
        :rtype: int
        """
        return self._QuotaId

    @QuotaId.setter
    def QuotaId(self, QuotaId):
        self._QuotaId = QuotaId

    @property
    def QuotaName(self):
        r"""quota name
        :rtype: str
        """
        return self._QuotaName

    @QuotaName.setter
    def QuotaName(self, QuotaName):
        self._QuotaName = QuotaName

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
    def QuotaUnit(self):
        r"""Quota unit
        :rtype: str
        """
        return self._QuotaUnit

    @QuotaUnit.setter
    def QuotaUnit(self, QuotaUnit):
        self._QuotaUnit = QuotaUnit

    @property
    def TotalQuota(self):
        r"""User Quota
        :rtype: int
        """
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def TotalUsage(self):
        r"""Quota usage
        :rtype: int
        """
        return self._TotalUsage

    @TotalUsage.setter
    def TotalUsage(self, TotalUsage):
        self._TotalUsage = TotalUsage

    @property
    def QuotaDescription(self):
        r"""Quota description
        :rtype: str
        """
        return self._QuotaDescription

    @QuotaDescription.setter
    def QuotaDescription(self, QuotaDescription):
        self._QuotaDescription = QuotaDescription

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
        self._QuotaId = params.get("QuotaId")
        self._QuotaName = params.get("QuotaName")
        self._ProductName = params.get("ProductName")
        self._QuotaUnit = params.get("QuotaUnit")
        self._TotalQuota = params.get("TotalQuota")
        self._TotalUsage = params.get("TotalUsage")
        self._QuotaDescription = params.get("QuotaDescription")
        self._RequestId = params.get("RequestId")


class EnableAlarmRequest(AbstractModel):
    r"""EnableAlarm request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Rule ID
        :type Id: int
        :param _MemberUin: Specifies the member uin of the rule owner.
        :type MemberUin: int
        """
        self._Id = None
        self._MemberUin = None

    @property
    def Id(self):
        r"""Rule ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MemberUin(self):
        r"""Specifies the member uin of the rule owner.
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableAlarmResponse(AbstractModel):
    r"""EnableAlarm response structure.

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


class Filter(AbstractModel):
    r"""Filter

    """

    def __init__(self):
        r"""
        :param _Name: Filter name
        :type Name: str
        :param _Value: Values after filtering
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""Filter name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""Values after filtering
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuotaDimension(AbstractModel):
    r"""Quota dimension

    """

    def __init__(self):
        r"""
        :param _DimensionName: Quota dimension
Note: This field may return null, indicating that no valid values can be obtained.
        :type DimensionName: str
        :param _PrimaryValue: Dimension value
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrimaryValue: str
        """
        self._DimensionName = None
        self._PrimaryValue = None

    @property
    def DimensionName(self):
        r"""Quota dimension
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DimensionName

    @DimensionName.setter
    def DimensionName(self, DimensionName):
        self._DimensionName = DimensionName

    @property
    def PrimaryValue(self):
        r"""Dimension value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PrimaryValue

    @PrimaryValue.setter
    def PrimaryValue(self, PrimaryValue):
        self._PrimaryValue = PrimaryValue


    def _deserialize(self, params):
        self._DimensionName = params.get("DimensionName")
        self._PrimaryValue = params.get("PrimaryValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sort(AbstractModel):
    r"""Order.

    """

    def __init__(self):
        r"""
        :param _Type: Ascending Descending Order
        :type Type: str
        :param _Field: Field
        :type Field: str
        """
        self._Type = None
        self._Field = None

    @property
    def Type(self):
        r"""Ascending Descending Order
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Field(self):
        r"""Field
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Field = params.get("Field")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAlarmRequest(AbstractModel):
    r"""UpdateAlarm request structure.

    """

    def __init__(self):
        r"""
        :param _Id: ID
        :type Id: int
        :param _Name: Alarm rule name.
        :type Name: str
        :param _ProductId: Product ID.
        :type ProductId: int
        :param _QuotaId: Quota ID.
        :type QuotaId: int
        :param _Metrics: 1: quota usage 2: quota usage rate 3: remaining quota 4: remaining quota rate.
        :type Metrics: int
        :param _Threshold: Specifies the Alarm threshold. valid values: 0-100.
        :type Threshold: int
        :param _Frequency: Alarm frequency.
        :type Frequency: int
        :param _MemberUin: Specifies the uin of the rule owner.
Operates non-group account rules. this parameter can be omitted.
Operates the organization account rule. specifies the uin of all users under the current rule.
        :type MemberUin: int
        """
        self._Id = None
        self._Name = None
        self._ProductId = None
        self._QuotaId = None
        self._Metrics = None
        self._Threshold = None
        self._Frequency = None
        self._MemberUin = None

    @property
    def Id(self):
        r"""ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""Alarm rule name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProductId(self):
        r"""Product ID.
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def QuotaId(self):
        r"""Quota ID.
        :rtype: int
        """
        return self._QuotaId

    @QuotaId.setter
    def QuotaId(self, QuotaId):
        self._QuotaId = QuotaId

    @property
    def Metrics(self):
        r"""1: quota usage 2: quota usage rate 3: remaining quota 4: remaining quota rate.
        :rtype: int
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def Threshold(self):
        r"""Specifies the Alarm threshold. valid values: 0-100.
        :rtype: int
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Frequency(self):
        r"""Alarm frequency.
        :rtype: int
        """
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def MemberUin(self):
        r"""Specifies the uin of the rule owner.
Operates non-group account rules. this parameter can be omitted.
Operates the organization account rule. specifies the uin of all users under the current rule.
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._ProductId = params.get("ProductId")
        self._QuotaId = params.get("QuotaId")
        self._Metrics = params.get("Metrics")
        self._Threshold = params.get("Threshold")
        self._Frequency = params.get("Frequency")
        self._MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAlarmResponse(AbstractModel):
    r"""UpdateAlarm response structure.

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


class UserQuota(AbstractModel):
    r"""User quota

    """

    def __init__(self):
        r"""
        :param _MemberUin: uin
        :type MemberUin: int
        :param _MemberName: Account nickname
        :type MemberName: str
        :param _QuotaInstanceId: Quota Instance ID
        :type QuotaInstanceId: str
        :param _QuotaId: Quota ID
        :type QuotaId: int
        :param _QuotaName: quota name
        :type QuotaName: str
        :param _ProductName: Product name
        :type ProductName: str
        :param _QuotaUnit: Quota unit
        :type QuotaUnit: str
        :param _ApplyType: Quota application method, enumeration value: 1: Can apply, 2: Ticket application, 3: Cannot apply.
        :type ApplyType: int
        :param _TotalQuota: User Total Quota
        :type TotalQuota: int
        :param _TotalUsage: Total usage of user quota
        :type TotalUsage: int
        :param _QuotaDescription: Quota description
        :type QuotaDescription: str
        :param _QuotaDimensions: Quota Dimension Value
Note: This field may return null, indicating that no valid values can be obtained.
        :type QuotaDimensions: list of QuotaDimension
        :param _Status: Status 5 Pending Approval
        :type Status: int
        """
        self._MemberUin = None
        self._MemberName = None
        self._QuotaInstanceId = None
        self._QuotaId = None
        self._QuotaName = None
        self._ProductName = None
        self._QuotaUnit = None
        self._ApplyType = None
        self._TotalQuota = None
        self._TotalUsage = None
        self._QuotaDescription = None
        self._QuotaDimensions = None
        self._Status = None

    @property
    def MemberUin(self):
        r"""uin
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def MemberName(self):
        r"""Account nickname
        :rtype: str
        """
        return self._MemberName

    @MemberName.setter
    def MemberName(self, MemberName):
        self._MemberName = MemberName

    @property
    def QuotaInstanceId(self):
        r"""Quota Instance ID
        :rtype: str
        """
        return self._QuotaInstanceId

    @QuotaInstanceId.setter
    def QuotaInstanceId(self, QuotaInstanceId):
        self._QuotaInstanceId = QuotaInstanceId

    @property
    def QuotaId(self):
        r"""Quota ID
        :rtype: int
        """
        return self._QuotaId

    @QuotaId.setter
    def QuotaId(self, QuotaId):
        self._QuotaId = QuotaId

    @property
    def QuotaName(self):
        r"""quota name
        :rtype: str
        """
        return self._QuotaName

    @QuotaName.setter
    def QuotaName(self, QuotaName):
        self._QuotaName = QuotaName

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
    def QuotaUnit(self):
        r"""Quota unit
        :rtype: str
        """
        return self._QuotaUnit

    @QuotaUnit.setter
    def QuotaUnit(self, QuotaUnit):
        self._QuotaUnit = QuotaUnit

    @property
    def ApplyType(self):
        r"""Quota application method, enumeration value: 1: Can apply, 2: Ticket application, 3: Cannot apply.
        :rtype: int
        """
        return self._ApplyType

    @ApplyType.setter
    def ApplyType(self, ApplyType):
        self._ApplyType = ApplyType

    @property
    def TotalQuota(self):
        r"""User Total Quota
        :rtype: int
        """
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def TotalUsage(self):
        r"""Total usage of user quota
        :rtype: int
        """
        return self._TotalUsage

    @TotalUsage.setter
    def TotalUsage(self, TotalUsage):
        self._TotalUsage = TotalUsage

    @property
    def QuotaDescription(self):
        r"""Quota description
        :rtype: str
        """
        return self._QuotaDescription

    @QuotaDescription.setter
    def QuotaDescription(self, QuotaDescription):
        self._QuotaDescription = QuotaDescription

    @property
    def QuotaDimensions(self):
        r"""Quota Dimension Value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of QuotaDimension
        """
        return self._QuotaDimensions

    @QuotaDimensions.setter
    def QuotaDimensions(self, QuotaDimensions):
        self._QuotaDimensions = QuotaDimensions

    @property
    def Status(self):
        r"""Status 5 Pending Approval
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._MemberName = params.get("MemberName")
        self._QuotaInstanceId = params.get("QuotaInstanceId")
        self._QuotaId = params.get("QuotaId")
        self._QuotaName = params.get("QuotaName")
        self._ProductName = params.get("ProductName")
        self._QuotaUnit = params.get("QuotaUnit")
        self._ApplyType = params.get("ApplyType")
        self._TotalQuota = params.get("TotalQuota")
        self._TotalUsage = params.get("TotalUsage")
        self._QuotaDescription = params.get("QuotaDescription")
        if params.get("QuotaDimensions") is not None:
            self._QuotaDimensions = []
            for item in params.get("QuotaDimensions"):
                obj = QuotaDimension()
                obj._deserialize(item)
                self._QuotaDimensions.append(obj)
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        