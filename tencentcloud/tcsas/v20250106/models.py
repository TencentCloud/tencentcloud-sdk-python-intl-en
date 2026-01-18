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


class APPOverview(AbstractModel):
    r"""Superapp data overview

    """

    def __init__(self):
        r"""
        :param _BaseData: No data available
Note: This field may return null, indicating that no valid values can be obtained.
        :type BaseData: :class:`tencentcloud.tcsas.v20250106.models.APPOverviewData`
        :param _Overview: Superapp overview summary data
Note: This field may return null, indicating that no valid values can be obtained.
        :type Overview: :class:`tencentcloud.tcsas.v20250106.models.APPOverviewData`
        :param _PageData: No data available
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageData: :class:`tencentcloud.tcsas.v20250106.models.APPOverviewData`
        :param _Payment: No data available
Note: This field may return null, indicating that no valid values can be obtained.
        :type Payment: :class:`tencentcloud.tcsas.v20250106.models.APPOverviewData`
        """
        self._BaseData = None
        self._Overview = None
        self._PageData = None
        self._Payment = None

    @property
    def BaseData(self):
        r"""No data available
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.APPOverviewData`
        """
        return self._BaseData

    @BaseData.setter
    def BaseData(self, BaseData):
        self._BaseData = BaseData

    @property
    def Overview(self):
        r"""Superapp overview summary data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.APPOverviewData`
        """
        return self._Overview

    @Overview.setter
    def Overview(self, Overview):
        self._Overview = Overview

    @property
    def PageData(self):
        r"""No data available
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.APPOverviewData`
        """
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def Payment(self):
        r"""No data available
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.APPOverviewData`
        """
        return self._Payment

    @Payment.setter
    def Payment(self, Payment):
        self._Payment = Payment


    def _deserialize(self, params):
        if params.get("BaseData") is not None:
            self._BaseData = APPOverviewData()
            self._BaseData._deserialize(params.get("BaseData"))
        if params.get("Overview") is not None:
            self._Overview = APPOverviewData()
            self._Overview._deserialize(params.get("Overview"))
        if params.get("PageData") is not None:
            self._PageData = APPOverviewData()
            self._PageData._deserialize(params.get("PageData"))
        if params.get("Payment") is not None:
            self._Payment = APPOverviewData()
            self._Payment._deserialize(params.get("Payment"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class APPOverviewData(AbstractModel):
    r"""Superapp overview data details

    """

    def __init__(self):
        r"""
        :param _AllActiveDeviceNum: Superapp active device count
        :type AllActiveDeviceNum: int
        :param _AllNewDeviceNum: Superapp new device count
        :type AllNewDeviceNum: int
        :param _CorpNum: Mini program team count
        :type CorpNum: int
        :param _GameActiveDeviceNum: Mini game active device count
        :type GameActiveDeviceNum: int
        :param _GameNewDeviceNum: Mini game new device count
        :type GameNewDeviceNum: int
        :param _MiniAppNum: Created mini program count

        :type MiniAppNum: int
        :param _MngNum: Created mini game count

        :type MngNum: int
        :param _NewDeviceNum: Mini program new device count
        :type NewDeviceNum: int
        :param _OnlineMiniAppNum: Released mini program count

        :type OnlineMiniAppNum: int
        :param _OnlineMngNum: Released mini game count

        :type OnlineMngNum: int
        :param _VisitNum: Mini program active device count
        :type VisitNum: int
        :param _FlushTime: Data refresh timestamp
        :type FlushTime: str
        """
        self._AllActiveDeviceNum = None
        self._AllNewDeviceNum = None
        self._CorpNum = None
        self._GameActiveDeviceNum = None
        self._GameNewDeviceNum = None
        self._MiniAppNum = None
        self._MngNum = None
        self._NewDeviceNum = None
        self._OnlineMiniAppNum = None
        self._OnlineMngNum = None
        self._VisitNum = None
        self._FlushTime = None

    @property
    def AllActiveDeviceNum(self):
        r"""Superapp active device count
        :rtype: int
        """
        return self._AllActiveDeviceNum

    @AllActiveDeviceNum.setter
    def AllActiveDeviceNum(self, AllActiveDeviceNum):
        self._AllActiveDeviceNum = AllActiveDeviceNum

    @property
    def AllNewDeviceNum(self):
        r"""Superapp new device count
        :rtype: int
        """
        return self._AllNewDeviceNum

    @AllNewDeviceNum.setter
    def AllNewDeviceNum(self, AllNewDeviceNum):
        self._AllNewDeviceNum = AllNewDeviceNum

    @property
    def CorpNum(self):
        r"""Mini program team count
        :rtype: int
        """
        return self._CorpNum

    @CorpNum.setter
    def CorpNum(self, CorpNum):
        self._CorpNum = CorpNum

    @property
    def GameActiveDeviceNum(self):
        r"""Mini game active device count
        :rtype: int
        """
        return self._GameActiveDeviceNum

    @GameActiveDeviceNum.setter
    def GameActiveDeviceNum(self, GameActiveDeviceNum):
        self._GameActiveDeviceNum = GameActiveDeviceNum

    @property
    def GameNewDeviceNum(self):
        r"""Mini game new device count
        :rtype: int
        """
        return self._GameNewDeviceNum

    @GameNewDeviceNum.setter
    def GameNewDeviceNum(self, GameNewDeviceNum):
        self._GameNewDeviceNum = GameNewDeviceNum

    @property
    def MiniAppNum(self):
        r"""Created mini program count

        :rtype: int
        """
        return self._MiniAppNum

    @MiniAppNum.setter
    def MiniAppNum(self, MiniAppNum):
        self._MiniAppNum = MiniAppNum

    @property
    def MngNum(self):
        r"""Created mini game count

        :rtype: int
        """
        return self._MngNum

    @MngNum.setter
    def MngNum(self, MngNum):
        self._MngNum = MngNum

    @property
    def NewDeviceNum(self):
        r"""Mini program new device count
        :rtype: int
        """
        return self._NewDeviceNum

    @NewDeviceNum.setter
    def NewDeviceNum(self, NewDeviceNum):
        self._NewDeviceNum = NewDeviceNum

    @property
    def OnlineMiniAppNum(self):
        r"""Released mini program count

        :rtype: int
        """
        return self._OnlineMiniAppNum

    @OnlineMiniAppNum.setter
    def OnlineMiniAppNum(self, OnlineMiniAppNum):
        self._OnlineMiniAppNum = OnlineMiniAppNum

    @property
    def OnlineMngNum(self):
        r"""Released mini game count

        :rtype: int
        """
        return self._OnlineMngNum

    @OnlineMngNum.setter
    def OnlineMngNum(self, OnlineMngNum):
        self._OnlineMngNum = OnlineMngNum

    @property
    def VisitNum(self):
        r"""Mini program active device count
        :rtype: int
        """
        return self._VisitNum

    @VisitNum.setter
    def VisitNum(self, VisitNum):
        self._VisitNum = VisitNum

    @property
    def FlushTime(self):
        r"""Data refresh timestamp
        :rtype: str
        """
        return self._FlushTime

    @FlushTime.setter
    def FlushTime(self, FlushTime):
        self._FlushTime = FlushTime


    def _deserialize(self, params):
        self._AllActiveDeviceNum = params.get("AllActiveDeviceNum")
        self._AllNewDeviceNum = params.get("AllNewDeviceNum")
        self._CorpNum = params.get("CorpNum")
        self._GameActiveDeviceNum = params.get("GameActiveDeviceNum")
        self._GameNewDeviceNum = params.get("GameNewDeviceNum")
        self._MiniAppNum = params.get("MiniAppNum")
        self._MngNum = params.get("MngNum")
        self._NewDeviceNum = params.get("NewDeviceNum")
        self._OnlineMiniAppNum = params.get("OnlineMiniAppNum")
        self._OnlineMngNum = params.get("OnlineMngNum")
        self._VisitNum = params.get("VisitNum")
        self._FlushTime = params.get("FlushTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessAnalysisDetail(AbstractModel):
    r"""Detailed visit analysis data

    """

    def __init__(self):
        r"""
        :param _ActiveCount: Number of active devices
        :type ActiveCount: int
        :param _AvgDevice: Average visit duration per user
        :type AvgDevice: str
        :param _AvgOnce: Average visit duration per session
        :type AvgOnce: str
        :param _AvgOpenCount: Average opens per user
        :type AvgOpenCount: str
        :param _DataTime: Date
        :type DataTime: str
        :param _FlushTime: Data time
        :type FlushTime: str
        :param _NewCount: Number of new devices
        :type NewCount: int
        :param _OpenCount: Number of opens
        :type OpenCount: int
        :param _TotalShareNum: Number of shares
        :type TotalShareNum: int
        :param _TotalUserNum: Cumulative users
        :type TotalUserNum: int
        """
        self._ActiveCount = None
        self._AvgDevice = None
        self._AvgOnce = None
        self._AvgOpenCount = None
        self._DataTime = None
        self._FlushTime = None
        self._NewCount = None
        self._OpenCount = None
        self._TotalShareNum = None
        self._TotalUserNum = None

    @property
    def ActiveCount(self):
        r"""Number of active devices
        :rtype: int
        """
        return self._ActiveCount

    @ActiveCount.setter
    def ActiveCount(self, ActiveCount):
        self._ActiveCount = ActiveCount

    @property
    def AvgDevice(self):
        r"""Average visit duration per user
        :rtype: str
        """
        return self._AvgDevice

    @AvgDevice.setter
    def AvgDevice(self, AvgDevice):
        self._AvgDevice = AvgDevice

    @property
    def AvgOnce(self):
        r"""Average visit duration per session
        :rtype: str
        """
        return self._AvgOnce

    @AvgOnce.setter
    def AvgOnce(self, AvgOnce):
        self._AvgOnce = AvgOnce

    @property
    def AvgOpenCount(self):
        r"""Average opens per user
        :rtype: str
        """
        return self._AvgOpenCount

    @AvgOpenCount.setter
    def AvgOpenCount(self, AvgOpenCount):
        self._AvgOpenCount = AvgOpenCount

    @property
    def DataTime(self):
        r"""Date
        :rtype: str
        """
        return self._DataTime

    @DataTime.setter
    def DataTime(self, DataTime):
        self._DataTime = DataTime

    @property
    def FlushTime(self):
        r"""Data time
        :rtype: str
        """
        return self._FlushTime

    @FlushTime.setter
    def FlushTime(self, FlushTime):
        self._FlushTime = FlushTime

    @property
    def NewCount(self):
        r"""Number of new devices
        :rtype: int
        """
        return self._NewCount

    @NewCount.setter
    def NewCount(self, NewCount):
        self._NewCount = NewCount

    @property
    def OpenCount(self):
        r"""Number of opens
        :rtype: int
        """
        return self._OpenCount

    @OpenCount.setter
    def OpenCount(self, OpenCount):
        self._OpenCount = OpenCount

    @property
    def TotalShareNum(self):
        r"""Number of shares
        :rtype: int
        """
        return self._TotalShareNum

    @TotalShareNum.setter
    def TotalShareNum(self, TotalShareNum):
        self._TotalShareNum = TotalShareNum

    @property
    def TotalUserNum(self):
        r"""Cumulative users
        :rtype: int
        """
        return self._TotalUserNum

    @TotalUserNum.setter
    def TotalUserNum(self, TotalUserNum):
        self._TotalUserNum = TotalUserNum


    def _deserialize(self, params):
        self._ActiveCount = params.get("ActiveCount")
        self._AvgDevice = params.get("AvgDevice")
        self._AvgOnce = params.get("AvgOnce")
        self._AvgOpenCount = params.get("AvgOpenCount")
        self._DataTime = params.get("DataTime")
        self._FlushTime = params.get("FlushTime")
        self._NewCount = params.get("NewCount")
        self._OpenCount = params.get("OpenCount")
        self._TotalShareNum = params.get("TotalShareNum")
        self._TotalUserNum = params.get("TotalUserNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessAnalysisOverview(AbstractModel):
    r"""Overview of mini game visit analysis data

    """

    def __init__(self):
        r"""
        :param _BaseData: Overview of visit analysis data
Note: This field may return null, indicating that no valid values can be obtained.
        :type BaseData: :class:`tencentcloud.tcsas.v20250106.models.AccessAnalysisDetail`
        :param _Overview: This API does not respond.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Overview: :class:`tencentcloud.tcsas.v20250106.models.Overview`
        :param _PageData: This API does not respond.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageData: :class:`tencentcloud.tcsas.v20250106.models.AccessAnalysisDetail`
        :param _Payment: This API does not respond.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Payment: :class:`tencentcloud.tcsas.v20250106.models.AccessAnalysisDetail`
        """
        self._BaseData = None
        self._Overview = None
        self._PageData = None
        self._Payment = None

    @property
    def BaseData(self):
        r"""Overview of visit analysis data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.AccessAnalysisDetail`
        """
        return self._BaseData

    @BaseData.setter
    def BaseData(self, BaseData):
        self._BaseData = BaseData

    @property
    def Overview(self):
        r"""This API does not respond.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.Overview`
        """
        return self._Overview

    @Overview.setter
    def Overview(self, Overview):
        self._Overview = Overview

    @property
    def PageData(self):
        r"""This API does not respond.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.AccessAnalysisDetail`
        """
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def Payment(self):
        r"""This API does not respond.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.AccessAnalysisDetail`
        """
        return self._Payment

    @Payment.setter
    def Payment(self, Payment):
        self._Payment = Payment


    def _deserialize(self, params):
        if params.get("BaseData") is not None:
            self._BaseData = AccessAnalysisDetail()
            self._BaseData._deserialize(params.get("BaseData"))
        if params.get("Overview") is not None:
            self._Overview = Overview()
            self._Overview._deserialize(params.get("Overview"))
        if params.get("PageData") is not None:
            self._PageData = AccessAnalysisDetail()
            self._PageData._deserialize(params.get("PageData"))
        if params.get("Payment") is not None:
            self._Payment = AccessAnalysisDetail()
            self._Payment._deserialize(params.get("Payment"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdTrendChart(AbstractModel):
    r"""Advertising line chart data

    """

    def __init__(self):
        r"""
        :param _EstimatedEarnings: Estimated revenue
Note: This field may return null, indicating that no valid values can be obtained.
        :type EstimatedEarnings: list of AnalysisData
        :param _RequestsNumber: Requests
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestsNumber: list of AnalysisData
        :param _Impressions: Impressions
Note: This field may return null, indicating that no valid values can be obtained.
        :type Impressions: list of AnalysisData
        :param _ECPM: Effective Cost Per Mille
Note: This field may return null, indicating that no valid values can be obtained.
        :type ECPM: list of AnalysisData
        :param _ClicksNumber: Taps
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClicksNumber: list of AnalysisData
        """
        self._EstimatedEarnings = None
        self._RequestsNumber = None
        self._Impressions = None
        self._ECPM = None
        self._ClicksNumber = None

    @property
    def EstimatedEarnings(self):
        r"""Estimated revenue
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of AnalysisData
        """
        return self._EstimatedEarnings

    @EstimatedEarnings.setter
    def EstimatedEarnings(self, EstimatedEarnings):
        self._EstimatedEarnings = EstimatedEarnings

    @property
    def RequestsNumber(self):
        r"""Requests
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of AnalysisData
        """
        return self._RequestsNumber

    @RequestsNumber.setter
    def RequestsNumber(self, RequestsNumber):
        self._RequestsNumber = RequestsNumber

    @property
    def Impressions(self):
        r"""Impressions
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of AnalysisData
        """
        return self._Impressions

    @Impressions.setter
    def Impressions(self, Impressions):
        self._Impressions = Impressions

    @property
    def ECPM(self):
        r"""Effective Cost Per Mille
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of AnalysisData
        """
        return self._ECPM

    @ECPM.setter
    def ECPM(self, ECPM):
        self._ECPM = ECPM

    @property
    def ClicksNumber(self):
        r"""Taps
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of AnalysisData
        """
        return self._ClicksNumber

    @ClicksNumber.setter
    def ClicksNumber(self, ClicksNumber):
        self._ClicksNumber = ClicksNumber


    def _deserialize(self, params):
        if params.get("EstimatedEarnings") is not None:
            self._EstimatedEarnings = []
            for item in params.get("EstimatedEarnings"):
                obj = AnalysisData()
                obj._deserialize(item)
                self._EstimatedEarnings.append(obj)
        if params.get("RequestsNumber") is not None:
            self._RequestsNumber = []
            for item in params.get("RequestsNumber"):
                obj = AnalysisData()
                obj._deserialize(item)
                self._RequestsNumber.append(obj)
        if params.get("Impressions") is not None:
            self._Impressions = []
            for item in params.get("Impressions"):
                obj = AnalysisData()
                obj._deserialize(item)
                self._Impressions.append(obj)
        if params.get("ECPM") is not None:
            self._ECPM = []
            for item in params.get("ECPM"):
                obj = AnalysisData()
                obj._deserialize(item)
                self._ECPM.append(obj)
        if params.get("ClicksNumber") is not None:
            self._ClicksNumber = []
            for item in params.get("ClicksNumber"):
                obj = AnalysisData()
                obj._deserialize(item)
                self._ClicksNumber.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTeamMemberRequest(AbstractModel):
    r"""AddTeamMember request structure.

    """

    def __init__(self):
        r"""
        :param _TeamId: Team ID
        :type TeamId: str
        :param _MemberList: Members to be added
        :type MemberList: list of CreateTeamMemberInfoReq
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._TeamId = None
        self._MemberList = None
        self._PlatformId = None

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def MemberList(self):
        r"""Members to be added
        :rtype: list of CreateTeamMemberInfoReq
        """
        return self._MemberList

    @MemberList.setter
    def MemberList(self, MemberList):
        self._MemberList = MemberList

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        if params.get("MemberList") is not None:
            self._MemberList = []
            for item in params.get("MemberList"):
                obj = CreateTeamMemberInfoReq()
                obj._deserialize(item)
                self._MemberList.append(obj)
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTeamMemberResponse(AbstractModel):
    r"""AddTeamMember response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AdvertDataOverview(AbstractModel):
    r"""Advertising data overview

    """

    def __init__(self):
        r"""
        :param _EstimatedEarnings: Estimated revenue
Note: This field may return null, indicating that no valid values can be obtained.
        :type EstimatedEarnings: str
        :param _RequestsNumber: Requests
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestsNumber: int
        :param _Impressions: Impressions
Note: This field may return null, indicating that no valid values can be obtained.
        :type Impressions: int
        :param _ClicksNumber: Taps
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClicksNumber: int
        :param _ECPM: Impressions
Note: This field may return null, indicating that no valid values can be obtained.
        :type ECPM: str
        """
        self._EstimatedEarnings = None
        self._RequestsNumber = None
        self._Impressions = None
        self._ClicksNumber = None
        self._ECPM = None

    @property
    def EstimatedEarnings(self):
        r"""Estimated revenue
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EstimatedEarnings

    @EstimatedEarnings.setter
    def EstimatedEarnings(self, EstimatedEarnings):
        self._EstimatedEarnings = EstimatedEarnings

    @property
    def RequestsNumber(self):
        r"""Requests
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RequestsNumber

    @RequestsNumber.setter
    def RequestsNumber(self, RequestsNumber):
        self._RequestsNumber = RequestsNumber

    @property
    def Impressions(self):
        r"""Impressions
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Impressions

    @Impressions.setter
    def Impressions(self, Impressions):
        self._Impressions = Impressions

    @property
    def ClicksNumber(self):
        r"""Taps
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ClicksNumber

    @ClicksNumber.setter
    def ClicksNumber(self, ClicksNumber):
        self._ClicksNumber = ClicksNumber

    @property
    def ECPM(self):
        r"""Impressions
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ECPM

    @ECPM.setter
    def ECPM(self, ECPM):
        self._ECPM = ECPM


    def _deserialize(self, params):
        self._EstimatedEarnings = params.get("EstimatedEarnings")
        self._RequestsNumber = params.get("RequestsNumber")
        self._Impressions = params.get("Impressions")
        self._ClicksNumber = params.get("ClicksNumber")
        self._ECPM = params.get("ECPM")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalysisAdvertOverview(AbstractModel):
    r"""Advertising analysis data overview

    """

    def __init__(self):
        r"""
        :param _OverviewData: Advertising overview
Note: This field may return null, indicating that no valid values can be obtained.
        :type OverviewData: :class:`tencentcloud.tcsas.v20250106.models.AdvertDataOverview`
        """
        self._OverviewData = None

    @property
    def OverviewData(self):
        r"""Advertising overview
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.AdvertDataOverview`
        """
        return self._OverviewData

    @OverviewData.setter
    def OverviewData(self, OverviewData):
        self._OverviewData = OverviewData


    def _deserialize(self, params):
        if params.get("OverviewData") is not None:
            self._OverviewData = AdvertDataOverview()
            self._OverviewData._deserialize(params.get("OverviewData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalysisData(AbstractModel):
    r"""Line chart data values

    """

    def __init__(self):
        r"""
        :param _DataTime: Time
        :type DataTime: str
        :param _Number: Value
        :type Number: str
        """
        self._DataTime = None
        self._Number = None

    @property
    def DataTime(self):
        r"""Time
        :rtype: str
        """
        return self._DataTime

    @DataTime.setter
    def DataTime(self, DataTime):
        self._DataTime = DataTime

    @property
    def Number(self):
        r"""Value
        :rtype: str
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number


    def _deserialize(self, params):
        self._DataTime = params.get("DataTime")
        self._Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationConfigInfo(AbstractModel):
    r"""Application configuration info

    """

    def __init__(self):
        r"""
        :param _ApplicationType: Superapp configuration type: 1 Non-production, 2 Production
        :type ApplicationType: int
        :param _AppKey: Superapp package name
        :type AppKey: str
        :param _AppURL: Superapp URL
        :type AppURL: str
        :param _Id: Superapp configuration ID
        :type Id: int
        """
        self._ApplicationType = None
        self._AppKey = None
        self._AppURL = None
        self._Id = None

    @property
    def ApplicationType(self):
        r"""Superapp configuration type: 1 Non-production, 2 Production
        :rtype: int
        """
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def AppKey(self):
        r"""Superapp package name
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def AppURL(self):
        r"""Superapp URL
        :rtype: str
        """
        return self._AppURL

    @AppURL.setter
    def AppURL(self, AppURL):
        self._AppURL = AppURL

    @property
    def Id(self):
        r"""Superapp configuration ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._ApplicationType = params.get("ApplicationType")
        self._AppKey = params.get("AppKey")
        self._AppURL = params.get("AppURL")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApprovalItem(AbstractModel):
    r"""Result of the mini program approval requests

    """

    def __init__(self):
        r"""
        :param _AppId: Application ID
        :type AppId: str
        :param _ApprovalResult: Approval result. 2: Rejected;
3: Approved
        :type ApprovalResult: int
        :param _ApprovalNote: Approval notes. It’s required when the request is rejected.
        :type ApprovalNote: str
        """
        self._AppId = None
        self._ApprovalResult = None
        self._ApprovalNote = None

    @property
    def AppId(self):
        r"""Application ID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ApprovalResult(self):
        r"""Approval result. 2: Rejected;
3: Approved
        :rtype: int
        """
        return self._ApprovalResult

    @ApprovalResult.setter
    def ApprovalResult(self, ApprovalResult):
        self._ApprovalResult = ApprovalResult

    @property
    def ApprovalNote(self):
        r"""Approval notes. It’s required when the request is rejected.
        :rtype: str
        """
        return self._ApprovalNote

    @ApprovalNote.setter
    def ApprovalNote(self, ApprovalNote):
        self._ApprovalNote = ApprovalNote


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ApprovalResult = params.get("ApprovalResult")
        self._ApprovalNote = params.get("ApprovalNote")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BooleanInfo(AbstractModel):
    r"""Used for Data object when no data is returned after the a successful action.

    """

    def __init__(self):
        r"""
        :param _Result: Bool type response object
Note: This field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        """
        self._Result = None

    @property
    def Result(self):
        r"""Bool type response object
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureMNPPreviewRequest(AbstractModel):
    r"""ConfigureMNPPreview request structure.

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _ActionType: 1: Set; 2: Cancel
        :type ActionType: int
        :param _MNPVersionId: Mini program version ID
        :type MNPVersionId: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _PreivewEntrancePath: Path to the preview page
        :type PreivewEntrancePath: str
        """
        self._MNPId = None
        self._ActionType = None
        self._MNPVersionId = None
        self._PlatformId = None
        self._PreivewEntrancePath = None

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def ActionType(self):
        r"""1: Set; 2: Cancel
        :rtype: int
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def MNPVersionId(self):
        r"""Mini program version ID
        :rtype: int
        """
        return self._MNPVersionId

    @MNPVersionId.setter
    def MNPVersionId(self, MNPVersionId):
        self._MNPVersionId = MNPVersionId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def PreivewEntrancePath(self):
        r"""Path to the preview page
        :rtype: str
        """
        return self._PreivewEntrancePath

    @PreivewEntrancePath.setter
    def PreivewEntrancePath(self, PreivewEntrancePath):
        self._PreivewEntrancePath = PreivewEntrancePath


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._ActionType = params.get("ActionType")
        self._MNPVersionId = params.get("MNPVersionId")
        self._PlatformId = params.get("PlatformId")
        self._PreivewEntrancePath = params.get("PreivewEntrancePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureMNPPreviewResponse(AbstractModel):
    r"""ConfigureMNPPreview response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateApplicationConfigRequest(AbstractModel):
    r"""CreateApplicationConfig request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Superapp ID
        :type ApplicationId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _ApplicationType: Superapp type. 1: Test; 2: Formal
        :type ApplicationType: int
        :param _ApplicationPlatformType: Superapp operating system. 2 Android 3 iOS
        :type ApplicationPlatformType: int
        :param _AppKey: Package name: corresponds to packageName on Android and bundleId on iOS
        :type AppKey: str
        :param _AppURL: Superapp URL
        :type AppURL: str
        """
        self._ApplicationId = None
        self._PlatformId = None
        self._ApplicationType = None
        self._ApplicationPlatformType = None
        self._AppKey = None
        self._AppURL = None

    @property
    def ApplicationId(self):
        r"""Superapp ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ApplicationType(self):
        r"""Superapp type. 1: Test; 2: Formal
        :rtype: int
        """
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def ApplicationPlatformType(self):
        r"""Superapp operating system. 2 Android 3 iOS
        :rtype: int
        """
        return self._ApplicationPlatformType

    @ApplicationPlatformType.setter
    def ApplicationPlatformType(self, ApplicationPlatformType):
        self._ApplicationPlatformType = ApplicationPlatformType

    @property
    def AppKey(self):
        r"""Package name: corresponds to packageName on Android and bundleId on iOS
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def AppURL(self):
        r"""Superapp URL
        :rtype: str
        """
        return self._AppURL

    @AppURL.setter
    def AppURL(self, AppURL):
        self._AppURL = AppURL


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._PlatformId = params.get("PlatformId")
        self._ApplicationType = params.get("ApplicationType")
        self._ApplicationPlatformType = params.get("ApplicationPlatformType")
        self._AppKey = params.get("AppKey")
        self._AppURL = params.get("AppURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationConfigResponse(AbstractModel):
    r"""CreateApplicationConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateApplicationRequest(AbstractModel):
    r"""CreateApplication request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationName: Application name
        :type ApplicationName: str
        :param _Logo: Logo address
        :type Logo: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _TeamId: Team ID
        :type TeamId: str
        :param _Intro: Introduction
        :type Intro: str
        :param _ApplicationType: Application type. 1: Test; 2: Formal
        :type ApplicationType: int
        :param _AndroidAppKey: Android app package name
        :type AndroidAppKey: str
        :param _IosAppKey: iOS App bundleId
        :type IosAppKey: str
        :param _Remark: Remarks
        :type Remark: str
        :param _Scheme: Scheme
        :type Scheme: str
        """
        self._ApplicationName = None
        self._Logo = None
        self._PlatformId = None
        self._TeamId = None
        self._Intro = None
        self._ApplicationType = None
        self._AndroidAppKey = None
        self._IosAppKey = None
        self._Remark = None
        self._Scheme = None

    @property
    def ApplicationName(self):
        r"""Application name
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def Logo(self):
        r"""Logo address
        :rtype: str
        """
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def Intro(self):
        r"""Introduction
        :rtype: str
        """
        return self._Intro

    @Intro.setter
    def Intro(self, Intro):
        self._Intro = Intro

    @property
    def ApplicationType(self):
        warnings.warn("parameter `ApplicationType` is deprecated", DeprecationWarning) 

        r"""Application type. 1: Test; 2: Formal
        :rtype: int
        """
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        warnings.warn("parameter `ApplicationType` is deprecated", DeprecationWarning) 

        self._ApplicationType = ApplicationType

    @property
    def AndroidAppKey(self):
        warnings.warn("parameter `AndroidAppKey` is deprecated", DeprecationWarning) 

        r"""Android app package name
        :rtype: str
        """
        return self._AndroidAppKey

    @AndroidAppKey.setter
    def AndroidAppKey(self, AndroidAppKey):
        warnings.warn("parameter `AndroidAppKey` is deprecated", DeprecationWarning) 

        self._AndroidAppKey = AndroidAppKey

    @property
    def IosAppKey(self):
        warnings.warn("parameter `IosAppKey` is deprecated", DeprecationWarning) 

        r"""iOS App bundleId
        :rtype: str
        """
        return self._IosAppKey

    @IosAppKey.setter
    def IosAppKey(self, IosAppKey):
        warnings.warn("parameter `IosAppKey` is deprecated", DeprecationWarning) 

        self._IosAppKey = IosAppKey

    @property
    def Remark(self):
        warnings.warn("parameter `Remark` is deprecated", DeprecationWarning) 

        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        warnings.warn("parameter `Remark` is deprecated", DeprecationWarning) 

        self._Remark = Remark

    @property
    def Scheme(self):
        r"""Scheme
        :rtype: str
        """
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme


    def _deserialize(self, params):
        self._ApplicationName = params.get("ApplicationName")
        self._Logo = params.get("Logo")
        self._PlatformId = params.get("PlatformId")
        self._TeamId = params.get("TeamId")
        self._Intro = params.get("Intro")
        self._ApplicationType = params.get("ApplicationType")
        self._AndroidAppKey = params.get("AndroidAppKey")
        self._IosAppKey = params.get("IosAppKey")
        self._Remark = params.get("Remark")
        self._Scheme = params.get("Scheme")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationResponse(AbstractModel):
    r"""CreateApplication response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.ResourceIdStringInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ResourceIdStringInfo`
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
        if params.get("Data") is not None:
            self._Data = ResourceIdStringInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateApplicationSensitiveAPIReq(AbstractModel):
    r"""The request to add a sensitive API

    """

    def __init__(self):
        r"""
        :param _APIName: API name
        :type APIName: str
        :param _APIDesc: API description
        :type APIDesc: str
        :param _APIType: API type. 1: system; 2: custom.
        :type APIType: int
        """
        self._APIName = None
        self._APIDesc = None
        self._APIType = None

    @property
    def APIName(self):
        r"""API name
        :rtype: str
        """
        return self._APIName

    @APIName.setter
    def APIName(self, APIName):
        self._APIName = APIName

    @property
    def APIDesc(self):
        r"""API description
        :rtype: str
        """
        return self._APIDesc

    @APIDesc.setter
    def APIDesc(self, APIDesc):
        self._APIDesc = APIDesc

    @property
    def APIType(self):
        r"""API type. 1: system; 2: custom.
        :rtype: int
        """
        return self._APIType

    @APIType.setter
    def APIType(self, APIType):
        self._APIType = APIType


    def _deserialize(self, params):
        self._APIName = params.get("APIName")
        self._APIDesc = params.get("APIDesc")
        self._APIType = params.get("APIType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationSensitiveAPIRequest(AbstractModel):
    r"""CreateApplicationSensitiveAPI request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _APIList: List of newly-added APIs
        :type APIList: list of CreateApplicationSensitiveAPIReq
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._ApplicationId = None
        self._APIList = None
        self._PlatformId = None

    @property
    def ApplicationId(self):
        r"""Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def APIList(self):
        r"""List of newly-added APIs
        :rtype: list of CreateApplicationSensitiveAPIReq
        """
        return self._APIList

    @APIList.setter
    def APIList(self, APIList):
        self._APIList = APIList

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        if params.get("APIList") is not None:
            self._APIList = []
            for item in params.get("APIList"):
                obj = CreateApplicationSensitiveAPIReq()
                obj._deserialize(item)
                self._APIList.append(obj)
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationSensitiveAPIResponse(AbstractModel):
    r"""CreateApplicationSensitiveAPI response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateDomainParam(AbstractModel):
    r"""Parameters to create a domain name

    """

    def __init__(self):
        r"""
        :param _DomainUrlList: Array of domain name URLs
        :type DomainUrlList: list of str
        :param _DomainType: Domain type. 1: requests domain; 2: WebView load domain, 3: sockets domain; 4: File upload; 5: File download
        :type DomainType: int
        """
        self._DomainUrlList = None
        self._DomainType = None

    @property
    def DomainUrlList(self):
        r"""Array of domain name URLs
        :rtype: list of str
        """
        return self._DomainUrlList

    @DomainUrlList.setter
    def DomainUrlList(self, DomainUrlList):
        self._DomainUrlList = DomainUrlList

    @property
    def DomainType(self):
        r"""Domain type. 1: requests domain; 2: WebView load domain, 3: sockets domain; 4: File upload; 5: File download
        :rtype: int
        """
        return self._DomainType

    @DomainType.setter
    def DomainType(self, DomainType):
        self._DomainType = DomainType


    def _deserialize(self, params):
        self._DomainUrlList = params.get("DomainUrlList")
        self._DomainType = params.get("DomainType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGlobalDomainACLRequest(AbstractModel):
    r"""CreateGlobalDomainACL request structure.

    """

    def __init__(self):
        r"""
        :param _DomainUrlList: Domain name list
        :type DomainUrlList: list of str
        :param _DomainType: Domain type. 1: Allowed; 2: Blocked
        :type DomainType: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._DomainUrlList = None
        self._DomainType = None
        self._PlatformId = None

    @property
    def DomainUrlList(self):
        r"""Domain name list
        :rtype: list of str
        """
        return self._DomainUrlList

    @DomainUrlList.setter
    def DomainUrlList(self, DomainUrlList):
        self._DomainUrlList = DomainUrlList

    @property
    def DomainType(self):
        r"""Domain type. 1: Allowed; 2: Blocked
        :rtype: int
        """
        return self._DomainType

    @DomainType.setter
    def DomainType(self, DomainType):
        self._DomainType = DomainType

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._DomainUrlList = params.get("DomainUrlList")
        self._DomainType = params.get("DomainType")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGlobalDomainACLResponse(AbstractModel):
    r"""CreateGlobalDomainACL response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.CreateGlobalDomainResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateGlobalDomainResp`
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
        if params.get("Data") is not None:
            self._Data = CreateGlobalDomainResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateGlobalDomainResp(AbstractModel):
    r"""Response of creating a global domain name

    """

    def __init__(self):
        r"""
        :param _Result: Result
        :type Result: bool
        :param _RepeatUrls: Indicates the duplicate domain name.
        :type RepeatUrls: list of str
        :param _ExistsWhiteUrls: Lists allowed domain names.
        :type ExistsWhiteUrls: list of str
        :param _ExistsBlackUrls: Indicates the domain name already exists in the blocklist.
        :type ExistsBlackUrls: list of str
        """
        self._Result = None
        self._RepeatUrls = None
        self._ExistsWhiteUrls = None
        self._ExistsBlackUrls = None

    @property
    def Result(self):
        r"""Result
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RepeatUrls(self):
        r"""Indicates the duplicate domain name.
        :rtype: list of str
        """
        return self._RepeatUrls

    @RepeatUrls.setter
    def RepeatUrls(self, RepeatUrls):
        self._RepeatUrls = RepeatUrls

    @property
    def ExistsWhiteUrls(self):
        r"""Lists allowed domain names.
        :rtype: list of str
        """
        return self._ExistsWhiteUrls

    @ExistsWhiteUrls.setter
    def ExistsWhiteUrls(self, ExistsWhiteUrls):
        self._ExistsWhiteUrls = ExistsWhiteUrls

    @property
    def ExistsBlackUrls(self):
        r"""Indicates the domain name already exists in the blocklist.
        :rtype: list of str
        """
        return self._ExistsBlackUrls

    @ExistsBlackUrls.setter
    def ExistsBlackUrls(self, ExistsBlackUrls):
        self._ExistsBlackUrls = ExistsBlackUrls


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RepeatUrls = params.get("RepeatUrls")
        self._ExistsWhiteUrls = params.get("ExistsWhiteUrls")
        self._ExistsBlackUrls = params.get("ExistsBlackUrls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMNPApprovalRequest(AbstractModel):
    r"""CreateMNPApproval request structure.

    """

    def __init__(self):
        r"""
        :param _MNPVersionId: Mini program version ID
        :type MNPVersionId: int
        :param _ApplyAction: submit: Submit an approval request; cancel: Cancel the approval request
        :type ApplyAction: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._MNPVersionId = None
        self._ApplyAction = None
        self._PlatformId = None

    @property
    def MNPVersionId(self):
        r"""Mini program version ID
        :rtype: int
        """
        return self._MNPVersionId

    @MNPVersionId.setter
    def MNPVersionId(self, MNPVersionId):
        self._MNPVersionId = MNPVersionId

    @property
    def ApplyAction(self):
        r"""submit: Submit an approval request; cancel: Cancel the approval request
        :rtype: str
        """
        return self._ApplyAction

    @ApplyAction.setter
    def ApplyAction(self, ApplyAction):
        self._ApplyAction = ApplyAction

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._MNPVersionId = params.get("MNPVersionId")
        self._ApplyAction = params.get("ApplyAction")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMNPApprovalResp(AbstractModel):
    r"""Response for platform review of mini program version submission.

    """

    def __init__(self):
        r"""
        :param _Result: Bool type response object
        :type Result: bool
        :param _ApprovalNo: Approval No.
        :type ApprovalNo: str
        """
        self._Result = None
        self._ApprovalNo = None

    @property
    def Result(self):
        r"""Bool type response object
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ApprovalNo(self):
        r"""Approval No.
        :rtype: str
        """
        return self._ApprovalNo

    @ApprovalNo.setter
    def ApprovalNo(self, ApprovalNo):
        self._ApprovalNo = ApprovalNo


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._ApprovalNo = params.get("ApprovalNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMNPApprovalResponse(AbstractModel):
    r"""CreateMNPApproval response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPApprovalResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPApprovalResp`
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
        if params.get("Data") is not None:
            self._Data = CreateMNPApprovalResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateMNPDomainACLRequest(AbstractModel):
    r"""CreateMNPDomainACL request structure.

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _Domain: Domain name list
        :type Domain: list of CreateDomainParam
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._MNPId = None
        self._Domain = None
        self._PlatformId = None

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def Domain(self):
        r"""Domain name list
        :rtype: list of CreateDomainParam
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        if params.get("Domain") is not None:
            self._Domain = []
            for item in params.get("Domain"):
                obj = CreateDomainParam()
                obj._deserialize(item)
                self._Domain.append(obj)
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMNPDomainACLResponse(AbstractModel):
    r"""CreateMNPDomainACL response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateMNPRequest(AbstractModel):
    r"""CreateMNP request structure.

    """

    def __init__(self):
        r"""
        :param _MNPType: Mini program type
        :type MNPType: str
        :param _MNPName: Mini program name
        :type MNPName: str
        :param _MNPIcon: Mini app icon
        :type MNPIcon: str
        :param _MNPIntro: Mini program introduction
        :type MNPIntro: str
        :param _MNPDesc: Mini program description
        :type MNPDesc: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _TeamId: Team ID
        :type TeamId: str
        """
        self._MNPType = None
        self._MNPName = None
        self._MNPIcon = None
        self._MNPIntro = None
        self._MNPDesc = None
        self._PlatformId = None
        self._TeamId = None

    @property
    def MNPType(self):
        r"""Mini program type
        :rtype: str
        """
        return self._MNPType

    @MNPType.setter
    def MNPType(self, MNPType):
        self._MNPType = MNPType

    @property
    def MNPName(self):
        r"""Mini program name
        :rtype: str
        """
        return self._MNPName

    @MNPName.setter
    def MNPName(self, MNPName):
        self._MNPName = MNPName

    @property
    def MNPIcon(self):
        r"""Mini app icon
        :rtype: str
        """
        return self._MNPIcon

    @MNPIcon.setter
    def MNPIcon(self, MNPIcon):
        self._MNPIcon = MNPIcon

    @property
    def MNPIntro(self):
        r"""Mini program introduction
        :rtype: str
        """
        return self._MNPIntro

    @MNPIntro.setter
    def MNPIntro(self, MNPIntro):
        self._MNPIntro = MNPIntro

    @property
    def MNPDesc(self):
        r"""Mini program description
        :rtype: str
        """
        return self._MNPDesc

    @MNPDesc.setter
    def MNPDesc(self, MNPDesc):
        self._MNPDesc = MNPDesc

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId


    def _deserialize(self, params):
        self._MNPType = params.get("MNPType")
        self._MNPName = params.get("MNPName")
        self._MNPIcon = params.get("MNPIcon")
        self._MNPIntro = params.get("MNPIntro")
        self._MNPDesc = params.get("MNPDesc")
        self._PlatformId = params.get("PlatformId")
        self._TeamId = params.get("TeamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMNPResponse(AbstractModel):
    r"""CreateMNP response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response mini program ID
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.ResourceIdStringInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response mini program ID
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ResourceIdStringInfo`
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
        if params.get("Data") is not None:
            self._Data = ResourceIdStringInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateMNPSensitiveAPIPermissionApprovalRequest(AbstractModel):
    r"""CreateMNPSensitiveAPIPermissionApproval request structure.

    """

    def __init__(self):
        r"""
        :param _APIId: API Id
        :type APIId: str
        :param _ApplyReason: Reason for application
        :type ApplyReason: str
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._APIId = None
        self._ApplyReason = None
        self._MNPId = None
        self._PlatformId = None

    @property
    def APIId(self):
        r"""API Id
        :rtype: str
        """
        return self._APIId

    @APIId.setter
    def APIId(self, APIId):
        self._APIId = APIId

    @property
    def ApplyReason(self):
        r"""Reason for application
        :rtype: str
        """
        return self._ApplyReason

    @ApplyReason.setter
    def ApplyReason(self, ApplyReason):
        self._ApplyReason = ApplyReason

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._APIId = params.get("APIId")
        self._ApplyReason = params.get("ApplyReason")
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMNPSensitiveAPIPermissionApprovalResponse(AbstractModel):
    r"""CreateMNPSensitiveAPIPermissionApproval response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.ResourceIdStringInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ResourceIdStringInfo`
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
        if params.get("Data") is not None:
            self._Data = ResourceIdStringInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateMNPVersionRequest(AbstractModel):
    r"""CreateMNPVersion request structure.

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _MNPVersion: Version number
        :type MNPVersion: str
        :param _FileUrl: Address of the mini program package. You can export the package from IDE and upload it to a file server.
        :type FileUrl: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _MNPVersionIntro: Version introduction
        :type MNPVersionIntro: str
        """
        self._MNPId = None
        self._MNPVersion = None
        self._FileUrl = None
        self._PlatformId = None
        self._MNPVersionIntro = None

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def MNPVersion(self):
        r"""Version number
        :rtype: str
        """
        return self._MNPVersion

    @MNPVersion.setter
    def MNPVersion(self, MNPVersion):
        self._MNPVersion = MNPVersion

    @property
    def FileUrl(self):
        r"""Address of the mini program package. You can export the package from IDE and upload it to a file server.
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def MNPVersionIntro(self):
        r"""Version introduction
        :rtype: str
        """
        return self._MNPVersionIntro

    @MNPVersionIntro.setter
    def MNPVersionIntro(self, MNPVersionIntro):
        self._MNPVersionIntro = MNPVersionIntro


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._MNPVersion = params.get("MNPVersion")
        self._FileUrl = params.get("FileUrl")
        self._PlatformId = params.get("PlatformId")
        self._MNPVersionIntro = params.get("MNPVersionIntro")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMNPVersionResp(AbstractModel):
    r"""Response of creating a mini program version

    """

    def __init__(self):
        r"""
        :param _TaskId: Specifies the ID of the task to create a mini program version.
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""Specifies the ID of the task to create a mini program version.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMNPVersionResponse(AbstractModel):
    r"""CreateMNPVersion response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPVersionResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPVersionResp`
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
        if params.get("Data") is not None:
            self._Data = CreateMNPVersionResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreatePresetKeyRequest(AbstractModel):
    r"""CreatePresetKey request structure.

    """


class CreatePresetKeyResponse(AbstractModel):
    r"""CreatePresetKey response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.PresetResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.PresetResp`
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
        if params.get("Data") is not None:
            self._Data = PresetResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateTeamMemberInfoReq(AbstractModel):
    r"""New team member - Member information

    """

    def __init__(self):
        r"""
        :param _UserId: User ID
        :type UserId: str
        :param _UserRoleId: User role ID
        :type UserRoleId: int
        """
        self._UserId = None
        self._UserRoleId = None

    @property
    def UserId(self):
        r"""User ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserRoleId(self):
        r"""User role ID
        :rtype: int
        """
        return self._UserRoleId

    @UserRoleId.setter
    def UserRoleId(self, UserRoleId):
        self._UserRoleId = UserRoleId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserRoleId = params.get("UserRoleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTeamRequest(AbstractModel):
    r"""CreateTeam request structure.

    """

    def __init__(self):
        r"""
        :param _TeamName: Team name
        :type TeamName: str
        :param _AdminUserId: Admin name
        :type AdminUserId: str
        :param _TeamRoleTypeList: Permission assigned to the team. 1: Mini program; 2: Application (only one of these types is supported)
        :type TeamRoleTypeList: list of int
        :param _Remark: Remarks
        :type Remark: str
        :param _PlatformId: Platform ID, required for API call
        :type PlatformId: str
        :param _RelatedTeamId: Associated team ID
        :type RelatedTeamId: str
        """
        self._TeamName = None
        self._AdminUserId = None
        self._TeamRoleTypeList = None
        self._Remark = None
        self._PlatformId = None
        self._RelatedTeamId = None

    @property
    def TeamName(self):
        r"""Team name
        :rtype: str
        """
        return self._TeamName

    @TeamName.setter
    def TeamName(self, TeamName):
        self._TeamName = TeamName

    @property
    def AdminUserId(self):
        r"""Admin name
        :rtype: str
        """
        return self._AdminUserId

    @AdminUserId.setter
    def AdminUserId(self, AdminUserId):
        self._AdminUserId = AdminUserId

    @property
    def TeamRoleTypeList(self):
        r"""Permission assigned to the team. 1: Mini program; 2: Application (only one of these types is supported)
        :rtype: list of int
        """
        return self._TeamRoleTypeList

    @TeamRoleTypeList.setter
    def TeamRoleTypeList(self, TeamRoleTypeList):
        self._TeamRoleTypeList = TeamRoleTypeList

    @property
    def Remark(self):
        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PlatformId(self):
        r"""Platform ID, required for API call
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def RelatedTeamId(self):
        r"""Associated team ID
        :rtype: str
        """
        return self._RelatedTeamId

    @RelatedTeamId.setter
    def RelatedTeamId(self, RelatedTeamId):
        self._RelatedTeamId = RelatedTeamId


    def _deserialize(self, params):
        self._TeamName = params.get("TeamName")
        self._AdminUserId = params.get("AdminUserId")
        self._TeamRoleTypeList = params.get("TeamRoleTypeList")
        self._Remark = params.get("Remark")
        self._PlatformId = params.get("PlatformId")
        self._RelatedTeamId = params.get("RelatedTeamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTeamResponse(AbstractModel):
    r"""CreateTeam response structure.

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


class CreateUserRequest(AbstractModel):
    r"""CreateUser request structure.

    """

    def __init__(self):
        r"""
        :param _UserAccount: User account
        :type UserAccount: str
        :param _UserName: User name
        :type UserName: str
        :param _AccountType: User account type. 2: Platform admin; 3: Member.
        :type AccountType: int
        :param _Password: Account password. Use CreatePresetKey to get the public key to encrypt the password.
        :type Password: str
        :param _KeyId: Call CreatePresetKey to get the keyID from RequestId
        :type KeyId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._UserAccount = None
        self._UserName = None
        self._AccountType = None
        self._Password = None
        self._KeyId = None
        self._PlatformId = None

    @property
    def UserAccount(self):
        r"""User account
        :rtype: str
        """
        return self._UserAccount

    @UserAccount.setter
    def UserAccount(self, UserAccount):
        self._UserAccount = UserAccount

    @property
    def UserName(self):
        r"""User name
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def AccountType(self):
        r"""User account type. 2: Platform admin; 3: Member.
        :rtype: int
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Password(self):
        r"""Account password. Use CreatePresetKey to get the public key to encrypt the password.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def KeyId(self):
        r"""Call CreatePresetKey to get the keyID from RequestId
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._UserAccount = params.get("UserAccount")
        self._UserName = params.get("UserName")
        self._AccountType = params.get("AccountType")
        self._Password = params.get("Password")
        self._KeyId = params.get("KeyId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    r"""CreateUser response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data, user ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.ResourceIdStringInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data, user ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ResourceIdStringInfo`
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
        if params.get("Data") is not None:
            self._Data = ResourceIdStringInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteApplicationRequest(AbstractModel):
    r"""DeleteApplication request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._ApplicationId = None
        self._PlatformId = None

    @property
    def ApplicationId(self):
        r"""Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationResponse(AbstractModel):
    r"""DeleteApplication response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteApplicationSensitiveAPIRequest(AbstractModel):
    r"""DeleteApplicationSensitiveAPI request structure.

    """

    def __init__(self):
        r"""
        :param _APIId: API ID
        :type APIId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._APIId = None
        self._PlatformId = None

    @property
    def APIId(self):
        r"""API ID
        :rtype: str
        """
        return self._APIId

    @APIId.setter
    def APIId(self, APIId):
        self._APIId = APIId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._APIId = params.get("APIId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationSensitiveAPIResponse(AbstractModel):
    r"""DeleteApplicationSensitiveAPI response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteGlobalDomainRequest(AbstractModel):
    r"""DeleteGlobalDomain request structure.

    """

    def __init__(self):
        r"""
        :param _DomainId: Domain ID
        :type DomainId: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._DomainId = None
        self._PlatformId = None

    @property
    def DomainId(self):
        r"""Domain ID
        :rtype: int
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGlobalDomainResponse(AbstractModel):
    r"""DeleteGlobalDomain response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.GlobalDomainDeleteResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.GlobalDomainDeleteResp`
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
        if params.get("Data") is not None:
            self._Data = GlobalDomainDeleteResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteMNPRequest(AbstractModel):
    r"""DeleteMNP request structure.

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._MNPId = None
        self._PlatformId = None

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMNPResponse(AbstractModel):
    r"""DeleteMNP response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteTeamMemberRequest(AbstractModel):
    r"""DeleteTeamMember request structure.

    """

    def __init__(self):
        r"""
        :param _TeamId: Team ID
        :type TeamId: str
        :param _UserId: User ID
        :type UserId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._TeamId = None
        self._UserId = None
        self._PlatformId = None

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def UserId(self):
        r"""User ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._UserId = params.get("UserId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTeamMemberResponse(AbstractModel):
    r"""DeleteTeamMember response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteTeamRequest(AbstractModel):
    r"""DeleteTeam request structure.

    """

    def __init__(self):
        r"""
        :param _TeamId: Team ID
        :type TeamId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._TeamId = None
        self._PlatformId = None

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTeamResponse(AbstractModel):
    r"""DeleteTeam response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    r"""DeleteUser request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID
        :type UserId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._UserId = None
        self._PlatformId = None

    @property
    def UserId(self):
        r"""User ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    r"""DeleteUser response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeAPPDataDetailLineChartRequest(AbstractModel):
    r"""DescribeAPPDataDetailLineChart request structure.

    """

    def __init__(self):
        r"""
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _ReportId: Fixed value: mnp_data_analysis
        :type ReportId: str
        :param _IndexIds: IndexId (optional):
app_minigame_num: Number of created mini games
app_online_miniapp_num: Number of available mini programs
app_miniapp_num: Number of created mini programs
app_related_corp_num: Mini program team data
app_online_minigame_num: Number of available mini games
app_active_device_num: Number of active devices
app_new_device_num: Number of new devices
        :type IndexIds: list of str
        :param _QueryData: Input parameter base64 string: {"BeginDate":"20251122","EndDate":"20251128"}
        :type QueryData: str
        :param _ApplicationIds: Superapp ID
        :type ApplicationIds: list of str
        """
        self._PlatformId = None
        self._ReportId = None
        self._IndexIds = None
        self._QueryData = None
        self._ApplicationIds = None

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ReportId(self):
        r"""Fixed value: mnp_data_analysis
        :rtype: str
        """
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def IndexIds(self):
        r"""IndexId (optional):
app_minigame_num: Number of created mini games
app_online_miniapp_num: Number of available mini programs
app_miniapp_num: Number of created mini programs
app_related_corp_num: Mini program team data
app_online_minigame_num: Number of available mini games
app_active_device_num: Number of active devices
app_new_device_num: Number of new devices
        :rtype: list of str
        """
        return self._IndexIds

    @IndexIds.setter
    def IndexIds(self, IndexIds):
        self._IndexIds = IndexIds

    @property
    def QueryData(self):
        r"""Input parameter base64 string: {"BeginDate":"20251122","EndDate":"20251128"}
        :rtype: str
        """
        return self._QueryData

    @QueryData.setter
    def QueryData(self, QueryData):
        self._QueryData = QueryData

    @property
    def ApplicationIds(self):
        r"""Superapp ID
        :rtype: list of str
        """
        return self._ApplicationIds

    @ApplicationIds.setter
    def ApplicationIds(self, ApplicationIds):
        self._ApplicationIds = ApplicationIds


    def _deserialize(self, params):
        self._PlatformId = params.get("PlatformId")
        self._ReportId = params.get("ReportId")
        self._IndexIds = params.get("IndexIds")
        self._QueryData = params.get("QueryData")
        self._ApplicationIds = params.get("ApplicationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPPDataDetailLineChartResponse(AbstractModel):
    r"""DescribeAPPDataDetailLineChart response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of ReportDataResult
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ReportDataResult
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ReportDataResult()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAPPDataOverviewRequest(AbstractModel):
    r"""DescribeAPPDataOverview request structure.

    """

    def __init__(self):
        r"""
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _DataTime: Start time in YYYYMMDD format
        :type DataTime: int
        :param _ApplicationIds: Superapp ID
        :type ApplicationIds: list of str
        """
        self._PlatformId = None
        self._DataTime = None
        self._ApplicationIds = None

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def DataTime(self):
        r"""Start time in YYYYMMDD format
        :rtype: int
        """
        return self._DataTime

    @DataTime.setter
    def DataTime(self, DataTime):
        self._DataTime = DataTime

    @property
    def ApplicationIds(self):
        r"""Superapp ID
        :rtype: list of str
        """
        return self._ApplicationIds

    @ApplicationIds.setter
    def ApplicationIds(self, ApplicationIds):
        self._ApplicationIds = ApplicationIds


    def _deserialize(self, params):
        self._PlatformId = params.get("PlatformId")
        self._DataTime = params.get("DataTime")
        self._ApplicationIds = params.get("ApplicationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPPDataOverviewResponse(AbstractModel):
    r"""DescribeAPPDataOverview response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.APPOverview`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.APPOverview`
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
        if params.get("Data") is not None:
            self._Data = APPOverview()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeAdvertisingLineChartRequest(AbstractModel):
    r"""DescribeAdvertisingLineChart request structure.

    """

    def __init__(self):
        r"""
        :param _TimeBegin: Start time in YYYYMMDD format
        :type TimeBegin: str
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _TimeEnd: End time in YYYYMMDD format
        :type TimeEnd: str
        :param _Platform: // 0 All, 2-Android, 3 iOS
        :type Platform: int
        :param _AdUnitType:   1-BANNER  2-REWARDED
        :type AdUnitType: str
        """
        self._TimeBegin = None
        self._MNPId = None
        self._PlatformId = None
        self._TimeEnd = None
        self._Platform = None
        self._AdUnitType = None

    @property
    def TimeBegin(self):
        r"""Start time in YYYYMMDD format
        :rtype: str
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def TimeEnd(self):
        r"""End time in YYYYMMDD format
        :rtype: str
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def Platform(self):
        r"""// 0 All, 2-Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def AdUnitType(self):
        r"""  1-BANNER  2-REWARDED
        :rtype: str
        """
        return self._AdUnitType

    @AdUnitType.setter
    def AdUnitType(self, AdUnitType):
        self._AdUnitType = AdUnitType


    def _deserialize(self, params):
        self._TimeBegin = params.get("TimeBegin")
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._TimeEnd = params.get("TimeEnd")
        self._Platform = params.get("Platform")
        self._AdUnitType = params.get("AdUnitType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAdvertisingLineChartResponse(AbstractModel):
    r"""DescribeAdvertisingLineChart response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.AdTrendChart`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.AdTrendChart`
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
        if params.get("Data") is not None:
            self._Data = AdTrendChart()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeAdvertisingOverviewRequest(AbstractModel):
    r"""DescribeAdvertisingOverview request structure.

    """

    def __init__(self):
        r"""
        :param _TimeBegin: Start time in YYYYMMDD format
        :type TimeBegin: str
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _TimeEnd: End time in YYYYMMDD format
        :type TimeEnd: str
        :param _Platform: // 0 All, 2-Android, 3 iOS
        :type Platform: int
        :param _AdUnitType: //1-BANNER  2-REWARDED
        :type AdUnitType: str
        """
        self._TimeBegin = None
        self._MNPId = None
        self._PlatformId = None
        self._TimeEnd = None
        self._Platform = None
        self._AdUnitType = None

    @property
    def TimeBegin(self):
        r"""Start time in YYYYMMDD format
        :rtype: str
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def TimeEnd(self):
        r"""End time in YYYYMMDD format
        :rtype: str
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def Platform(self):
        r"""// 0 All, 2-Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def AdUnitType(self):
        r"""//1-BANNER  2-REWARDED
        :rtype: str
        """
        return self._AdUnitType

    @AdUnitType.setter
    def AdUnitType(self, AdUnitType):
        self._AdUnitType = AdUnitType


    def _deserialize(self, params):
        self._TimeBegin = params.get("TimeBegin")
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._TimeEnd = params.get("TimeEnd")
        self._Platform = params.get("Platform")
        self._AdUnitType = params.get("AdUnitType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAdvertisingOverviewResponse(AbstractModel):
    r"""DescribeAdvertisingOverview response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.MNPAdvertisingOverview`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.MNPAdvertisingOverview`
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
        if params.get("Data") is not None:
            self._Data = MNPAdvertisingOverview()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationConfigFileRequest(AbstractModel):
    r"""DescribeApplicationConfigFile request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _AppType: Application platform. 2: Android; 3: iOS
        :type AppType: int
        """
        self._ApplicationId = None
        self._PlatformId = None
        self._AppType = None

    @property
    def ApplicationId(self):
        r"""Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def AppType(self):
        warnings.warn("parameter `AppType` is deprecated", DeprecationWarning) 

        r"""Application platform. 2: Android; 3: iOS
        :rtype: int
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        warnings.warn("parameter `AppType` is deprecated", DeprecationWarning) 

        self._AppType = AppType


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._PlatformId = params.get("PlatformId")
        self._AppType = params.get("AppType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationConfigFileResponse(AbstractModel):
    r"""DescribeApplicationConfigFile response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DownloadApplicationConfigResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DownloadApplicationConfigResp`
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
        if params.get("Data") is not None:
            self._Data = DownloadApplicationConfigResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationConfigInfo(AbstractModel):
    r"""Response data for retrieving superapp configuration information

    """

    def __init__(self):
        r"""
        :param _AndroidConfig: Android configuration list
        :type AndroidConfig: list of ApplicationConfigInfo
        :param _IosConfig: iOS configuration list
        :type IosConfig: list of ApplicationConfigInfo
        """
        self._AndroidConfig = None
        self._IosConfig = None

    @property
    def AndroidConfig(self):
        r"""Android configuration list
        :rtype: list of ApplicationConfigInfo
        """
        return self._AndroidConfig

    @AndroidConfig.setter
    def AndroidConfig(self, AndroidConfig):
        self._AndroidConfig = AndroidConfig

    @property
    def IosConfig(self):
        r"""iOS configuration list
        :rtype: list of ApplicationConfigInfo
        """
        return self._IosConfig

    @IosConfig.setter
    def IosConfig(self, IosConfig):
        self._IosConfig = IosConfig


    def _deserialize(self, params):
        if params.get("AndroidConfig") is not None:
            self._AndroidConfig = []
            for item in params.get("AndroidConfig"):
                obj = ApplicationConfigInfo()
                obj._deserialize(item)
                self._AndroidConfig.append(obj)
        if params.get("IosConfig") is not None:
            self._IosConfig = []
            for item in params.get("IosConfig"):
                obj = ApplicationConfigInfo()
                obj._deserialize(item)
                self._IosConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationConfigInfosRequest(AbstractModel):
    r"""DescribeApplicationConfigInfos request structure.

    """

    def __init__(self):
        r"""
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _ApplicationId: Superapp ID
        :type ApplicationId: str
        """
        self._PlatformId = None
        self._ApplicationId = None

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ApplicationId(self):
        r"""Superapp ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._PlatformId = params.get("PlatformId")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationConfigInfosResponse(AbstractModel):
    r"""DescribeApplicationConfigInfos response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationConfigInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationConfigInfo`
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
        if params.get("Data") is not None:
            self._Data = DescribeApplicationConfigInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationListData(AbstractModel):
    r"""Application information

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _AppIdentityId: App Id.
        :type AppIdentityId: int
        :param _ApplicationName: Name
        :type ApplicationName: str
        :param _Logo: Icon
        :type Logo: str
        :param _Remark: Remarks
        :type Remark: str
        :param _AndroidAppKey: Android app package name
        :type AndroidAppKey: str
        :param _IosAppKey: iOS App bundleId
        :type IosAppKey: str
        :param _CreateUser: Creator
        :type CreateUser: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _UpdateUser: Specifies the updater.
        :type UpdateUser: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _Intro: Introduction
        :type Intro: str
        :param _TeamId: Team Id.
        :type TeamId: str
        :param _TeamName: Team name
        :type TeamName: str
        :param _SensitiveApiCount: Number of sensitive apis.
        :type SensitiveApiCount: int
        :param _ApplicationType: Application type. 1: Test; 2: Formal
        :type ApplicationType: int
        """
        self._ApplicationId = None
        self._AppIdentityId = None
        self._ApplicationName = None
        self._Logo = None
        self._Remark = None
        self._AndroidAppKey = None
        self._IosAppKey = None
        self._CreateUser = None
        self._CreateTime = None
        self._UpdateUser = None
        self._UpdateTime = None
        self._Intro = None
        self._TeamId = None
        self._TeamName = None
        self._SensitiveApiCount = None
        self._ApplicationType = None

    @property
    def ApplicationId(self):
        r"""Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def AppIdentityId(self):
        r"""App Id.
        :rtype: int
        """
        return self._AppIdentityId

    @AppIdentityId.setter
    def AppIdentityId(self, AppIdentityId):
        self._AppIdentityId = AppIdentityId

    @property
    def ApplicationName(self):
        r"""Name
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def Logo(self):
        r"""Icon
        :rtype: str
        """
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def Remark(self):
        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def AndroidAppKey(self):
        r"""Android app package name
        :rtype: str
        """
        return self._AndroidAppKey

    @AndroidAppKey.setter
    def AndroidAppKey(self, AndroidAppKey):
        self._AndroidAppKey = AndroidAppKey

    @property
    def IosAppKey(self):
        r"""iOS App bundleId
        :rtype: str
        """
        return self._IosAppKey

    @IosAppKey.setter
    def IosAppKey(self, IosAppKey):
        self._IosAppKey = IosAppKey

    @property
    def CreateUser(self):
        r"""Creator
        :rtype: str
        """
        return self._CreateUser

    @CreateUser.setter
    def CreateUser(self, CreateUser):
        self._CreateUser = CreateUser

    @property
    def CreateTime(self):
        r"""Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateUser(self):
        r"""Specifies the updater.
        :rtype: str
        """
        return self._UpdateUser

    @UpdateUser.setter
    def UpdateUser(self, UpdateUser):
        self._UpdateUser = UpdateUser

    @property
    def UpdateTime(self):
        r"""Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Intro(self):
        r"""Introduction
        :rtype: str
        """
        return self._Intro

    @Intro.setter
    def Intro(self, Intro):
        self._Intro = Intro

    @property
    def TeamId(self):
        r"""Team Id.
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def TeamName(self):
        r"""Team name
        :rtype: str
        """
        return self._TeamName

    @TeamName.setter
    def TeamName(self, TeamName):
        self._TeamName = TeamName

    @property
    def SensitiveApiCount(self):
        r"""Number of sensitive apis.
        :rtype: int
        """
        return self._SensitiveApiCount

    @SensitiveApiCount.setter
    def SensitiveApiCount(self, SensitiveApiCount):
        self._SensitiveApiCount = SensitiveApiCount

    @property
    def ApplicationType(self):
        r"""Application type. 1: Test; 2: Formal
        :rtype: int
        """
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._AppIdentityId = params.get("AppIdentityId")
        self._ApplicationName = params.get("ApplicationName")
        self._Logo = params.get("Logo")
        self._Remark = params.get("Remark")
        self._AndroidAppKey = params.get("AndroidAppKey")
        self._IosAppKey = params.get("IosAppKey")
        self._CreateUser = params.get("CreateUser")
        self._CreateTime = params.get("CreateTime")
        self._UpdateUser = params.get("UpdateUser")
        self._UpdateTime = params.get("UpdateTime")
        self._Intro = params.get("Intro")
        self._TeamId = params.get("TeamId")
        self._TeamName = params.get("TeamName")
        self._SensitiveApiCount = params.get("SensitiveApiCount")
        self._ApplicationType = params.get("ApplicationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationListRequest(AbstractModel):
    r"""DescribeApplicationList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Number of results per page
        :type Limit: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _Keyword: Keywords for search (app name)
        :type Keyword: str
        :param _TeamId: Team ID
        :type TeamId: str
        """
        self._Offset = None
        self._Limit = None
        self._PlatformId = None
        self._Keyword = None
        self._TeamId = None

    @property
    def Offset(self):
        r"""Page offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of results per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def Keyword(self):
        r"""Keywords for search (app name)
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PlatformId = params.get("PlatformId")
        self._Keyword = params.get("Keyword")
        self._TeamId = params.get("TeamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationListResp(AbstractModel):
    r"""List of applications

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _DataList: List information
        :type DataList: list of DescribeApplicationListData
        """
        self._TotalCount = None
        self._DataList = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataList(self):
        r"""List information
        :rtype: list of DescribeApplicationListData
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = DescribeApplicationListData()
                obj._deserialize(item)
                self._DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationListResponse(AbstractModel):
    r"""DescribeApplicationList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationListResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationListResp`
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
        if params.get("Data") is not None:
            self._Data = DescribeApplicationListResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationRequest(AbstractModel):
    r"""DescribeApplication request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._ApplicationId = None
        self._PlatformId = None

    @property
    def ApplicationId(self):
        r"""Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationResp(AbstractModel):
    r"""Application details

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _AppIdentityId: Product ID.
        :type AppIdentityId: int
        :param _ApplicationName: Application name
        :type ApplicationName: str
        :param _Logo: Specifies the application icon.
        :type Logo: str
        :param _Remark: Remarks
        :type Remark: str
        :param _AndroidAppKey: Android package name
        :type AndroidAppKey: str
        :param _IosAppKey: iOS bundleId
        :type IosAppKey: str
        :param _CreateUser: Creator
        :type CreateUser: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _UpdateUser: Specifies the updater.
        :type UpdateUser: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _Intro: Describes the application description.
        :type Intro: str
        :param _TeamId: Team ID
        :type TeamId: str
        :param _TeamName: Team name
        :type TeamName: str
        :param _SensitiveApiCount: Number of sensitive apis.
        :type SensitiveApiCount: int
        :param _ApplicationType: Application type. 1: Test; 2: Formal
        :type ApplicationType: int
        :param _Scheme: Specifies the application Scheme.
        :type Scheme: str
        """
        self._ApplicationId = None
        self._AppIdentityId = None
        self._ApplicationName = None
        self._Logo = None
        self._Remark = None
        self._AndroidAppKey = None
        self._IosAppKey = None
        self._CreateUser = None
        self._CreateTime = None
        self._UpdateUser = None
        self._UpdateTime = None
        self._Intro = None
        self._TeamId = None
        self._TeamName = None
        self._SensitiveApiCount = None
        self._ApplicationType = None
        self._Scheme = None

    @property
    def ApplicationId(self):
        r"""Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def AppIdentityId(self):
        r"""Product ID.
        :rtype: int
        """
        return self._AppIdentityId

    @AppIdentityId.setter
    def AppIdentityId(self, AppIdentityId):
        self._AppIdentityId = AppIdentityId

    @property
    def ApplicationName(self):
        r"""Application name
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def Logo(self):
        r"""Specifies the application icon.
        :rtype: str
        """
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def Remark(self):
        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def AndroidAppKey(self):
        r"""Android package name
        :rtype: str
        """
        return self._AndroidAppKey

    @AndroidAppKey.setter
    def AndroidAppKey(self, AndroidAppKey):
        self._AndroidAppKey = AndroidAppKey

    @property
    def IosAppKey(self):
        r"""iOS bundleId
        :rtype: str
        """
        return self._IosAppKey

    @IosAppKey.setter
    def IosAppKey(self, IosAppKey):
        self._IosAppKey = IosAppKey

    @property
    def CreateUser(self):
        r"""Creator
        :rtype: str
        """
        return self._CreateUser

    @CreateUser.setter
    def CreateUser(self, CreateUser):
        self._CreateUser = CreateUser

    @property
    def CreateTime(self):
        r"""Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateUser(self):
        r"""Specifies the updater.
        :rtype: str
        """
        return self._UpdateUser

    @UpdateUser.setter
    def UpdateUser(self, UpdateUser):
        self._UpdateUser = UpdateUser

    @property
    def UpdateTime(self):
        r"""Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Intro(self):
        r"""Describes the application description.
        :rtype: str
        """
        return self._Intro

    @Intro.setter
    def Intro(self, Intro):
        self._Intro = Intro

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def TeamName(self):
        r"""Team name
        :rtype: str
        """
        return self._TeamName

    @TeamName.setter
    def TeamName(self, TeamName):
        self._TeamName = TeamName

    @property
    def SensitiveApiCount(self):
        r"""Number of sensitive apis.
        :rtype: int
        """
        return self._SensitiveApiCount

    @SensitiveApiCount.setter
    def SensitiveApiCount(self, SensitiveApiCount):
        self._SensitiveApiCount = SensitiveApiCount

    @property
    def ApplicationType(self):
        r"""Application type. 1: Test; 2: Formal
        :rtype: int
        """
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def Scheme(self):
        r"""Specifies the application Scheme.
        :rtype: str
        """
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._AppIdentityId = params.get("AppIdentityId")
        self._ApplicationName = params.get("ApplicationName")
        self._Logo = params.get("Logo")
        self._Remark = params.get("Remark")
        self._AndroidAppKey = params.get("AndroidAppKey")
        self._IosAppKey = params.get("IosAppKey")
        self._CreateUser = params.get("CreateUser")
        self._CreateTime = params.get("CreateTime")
        self._UpdateUser = params.get("UpdateUser")
        self._UpdateTime = params.get("UpdateTime")
        self._Intro = params.get("Intro")
        self._TeamId = params.get("TeamId")
        self._TeamName = params.get("TeamName")
        self._SensitiveApiCount = params.get("SensitiveApiCount")
        self._ApplicationType = params.get("ApplicationType")
        self._Scheme = params.get("Scheme")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationResponse(AbstractModel):
    r"""DescribeApplication response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationResp`
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
        if params.get("Data") is not None:
            self._Data = DescribeApplicationResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationSensitiveAPIListData(AbstractModel):
    r"""List of sensitive APIs of an application

    """

    def __init__(self):
        r"""
        :param _APIId: APIID
        :type APIId: str
        :param _APIName: API name
        :type APIName: str
        :param _APIMethod: API request method
        :type APIMethod: str
        :param _APIDesc: API description
        :type APIDesc: str
        :param _CreateUser: Creator
        :type CreateUser: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _UpdateUser: Updater
        :type UpdateUser: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _ApplicationName: Application name
        :type ApplicationName: str
        :param _TeamId: Team ID
        :type TeamId: str
        :param _TeamName: Team name
        :type TeamName: str
        :param _ApplicationLogo: Specifies the application icon.
        :type ApplicationLogo: str
        :param _APIType: API type. 1: system; 2: custom.
        :type APIType: int
        :param _Status: API status. 0: public; 1: restricted.
        :type Status: int
        """
        self._APIId = None
        self._APIName = None
        self._APIMethod = None
        self._APIDesc = None
        self._CreateUser = None
        self._CreateTime = None
        self._UpdateUser = None
        self._UpdateTime = None
        self._ApplicationId = None
        self._ApplicationName = None
        self._TeamId = None
        self._TeamName = None
        self._ApplicationLogo = None
        self._APIType = None
        self._Status = None

    @property
    def APIId(self):
        r"""APIID
        :rtype: str
        """
        return self._APIId

    @APIId.setter
    def APIId(self, APIId):
        self._APIId = APIId

    @property
    def APIName(self):
        r"""API name
        :rtype: str
        """
        return self._APIName

    @APIName.setter
    def APIName(self, APIName):
        self._APIName = APIName

    @property
    def APIMethod(self):
        r"""API request method
        :rtype: str
        """
        return self._APIMethod

    @APIMethod.setter
    def APIMethod(self, APIMethod):
        self._APIMethod = APIMethod

    @property
    def APIDesc(self):
        r"""API description
        :rtype: str
        """
        return self._APIDesc

    @APIDesc.setter
    def APIDesc(self, APIDesc):
        self._APIDesc = APIDesc

    @property
    def CreateUser(self):
        r"""Creator
        :rtype: str
        """
        return self._CreateUser

    @CreateUser.setter
    def CreateUser(self, CreateUser):
        self._CreateUser = CreateUser

    @property
    def CreateTime(self):
        r"""Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateUser(self):
        r"""Updater
        :rtype: str
        """
        return self._UpdateUser

    @UpdateUser.setter
    def UpdateUser(self, UpdateUser):
        self._UpdateUser = UpdateUser

    @property
    def UpdateTime(self):
        r"""Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ApplicationId(self):
        r"""Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        r"""Application name
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def TeamName(self):
        r"""Team name
        :rtype: str
        """
        return self._TeamName

    @TeamName.setter
    def TeamName(self, TeamName):
        self._TeamName = TeamName

    @property
    def ApplicationLogo(self):
        r"""Specifies the application icon.
        :rtype: str
        """
        return self._ApplicationLogo

    @ApplicationLogo.setter
    def ApplicationLogo(self, ApplicationLogo):
        self._ApplicationLogo = ApplicationLogo

    @property
    def APIType(self):
        r"""API type. 1: system; 2: custom.
        :rtype: int
        """
        return self._APIType

    @APIType.setter
    def APIType(self, APIType):
        self._APIType = APIType

    @property
    def Status(self):
        r"""API status. 0: public; 1: restricted.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._APIId = params.get("APIId")
        self._APIName = params.get("APIName")
        self._APIMethod = params.get("APIMethod")
        self._APIDesc = params.get("APIDesc")
        self._CreateUser = params.get("CreateUser")
        self._CreateTime = params.get("CreateTime")
        self._UpdateUser = params.get("UpdateUser")
        self._UpdateTime = params.get("UpdateTime")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._TeamId = params.get("TeamId")
        self._TeamName = params.get("TeamName")
        self._ApplicationLogo = params.get("ApplicationLogo")
        self._APIType = params.get("APIType")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationSensitiveAPIListRequest(AbstractModel):
    r"""DescribeApplicationSensitiveAPIList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Number of results per page
        :type Limit: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _Keyword: Keywords for search (API name or method)
        :type Keyword: str
        :param _TeamId: Team ID
        :type TeamId: str
        """
        self._Offset = None
        self._Limit = None
        self._PlatformId = None
        self._ApplicationId = None
        self._Keyword = None
        self._TeamId = None

    @property
    def Offset(self):
        r"""Page offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of results per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ApplicationId(self):
        r"""Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def Keyword(self):
        r"""Keywords for search (API name or method)
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PlatformId = params.get("PlatformId")
        self._ApplicationId = params.get("ApplicationId")
        self._Keyword = params.get("Keyword")
        self._TeamId = params.get("TeamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationSensitiveAPIListResp(AbstractModel):
    r"""List of sensitive APIs of the application

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _DataList: List information
        :type DataList: list of DescribeApplicationSensitiveAPIListData
        """
        self._TotalCount = None
        self._DataList = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataList(self):
        r"""List information
        :rtype: list of DescribeApplicationSensitiveAPIListData
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = DescribeApplicationSensitiveAPIListData()
                obj._deserialize(item)
                self._DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationSensitiveAPIListResponse(AbstractModel):
    r"""DescribeApplicationSensitiveAPIList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationSensitiveAPIListResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationSensitiveAPIListResp`
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
        if params.get("Data") is not None:
            self._Data = DescribeApplicationSensitiveAPIListResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDomainInfoParam(AbstractModel):
    r"""Domain information

    """

    def __init__(self):
        r"""
        :param _DomainUrl: Multiple domain separators ';'.
        :type DomainUrl: str
        :param _DomainType: Domain type 1-requests domain 2-business domain.
        :type DomainType: int
        """
        self._DomainUrl = None
        self._DomainType = None

    @property
    def DomainUrl(self):
        r"""Multiple domain separators ';'.
        :rtype: str
        """
        return self._DomainUrl

    @DomainUrl.setter
    def DomainUrl(self, DomainUrl):
        self._DomainUrl = DomainUrl

    @property
    def DomainType(self):
        r"""Domain type 1-requests domain 2-business domain.
        :rtype: int
        """
        return self._DomainType

    @DomainType.setter
    def DomainType(self, DomainType):
        self._DomainType = DomainType


    def _deserialize(self, params):
        self._DomainUrl = params.get("DomainUrl")
        self._DomainType = params.get("DomainType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGlobalDomainACLRequest(AbstractModel):
    r"""DescribeGlobalDomainACL request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Number of results per page
        :type Limit: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _DomainTypes: Domain type. 1: Allowed; 2: Blocked
        :type DomainTypes: list of int
        :param _Keyword: Domain names to be queried
        :type Keyword: str
        """
        self._Offset = None
        self._Limit = None
        self._PlatformId = None
        self._DomainTypes = None
        self._Keyword = None

    @property
    def Offset(self):
        r"""Page offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of results per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def DomainTypes(self):
        r"""Domain type. 1: Allowed; 2: Blocked
        :rtype: list of int
        """
        return self._DomainTypes

    @DomainTypes.setter
    def DomainTypes(self, DomainTypes):
        self._DomainTypes = DomainTypes

    @property
    def Keyword(self):
        r"""Domain names to be queried
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PlatformId = params.get("PlatformId")
        self._DomainTypes = params.get("DomainTypes")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGlobalDomainACLResponse(AbstractModel):
    r"""DescribeGlobalDomainACL response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeGlobalDomainsResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeGlobalDomainsResp`
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
        if params.get("Data") is not None:
            self._Data = DescribeGlobalDomainsResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeGlobalDomainsListData(AbstractModel):
    r"""List of global domain names

    """

    def __init__(self):
        r"""
        :param _DomainId: Domain ID
        :type DomainId: int
        :param _DomainUrl: Domain name
        :type DomainUrl: str
        :param _DomainType: Type. 1: allowlist; 2: blocklist.
        :type DomainType: int
        :param _CreateUser: Creator
        :type CreateUser: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _UpdateUser: Specifies the updater.
        :type UpdateUser: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        """
        self._DomainId = None
        self._DomainUrl = None
        self._DomainType = None
        self._CreateUser = None
        self._CreateTime = None
        self._UpdateUser = None
        self._UpdateTime = None

    @property
    def DomainId(self):
        r"""Domain ID
        :rtype: int
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def DomainUrl(self):
        r"""Domain name
        :rtype: str
        """
        return self._DomainUrl

    @DomainUrl.setter
    def DomainUrl(self, DomainUrl):
        self._DomainUrl = DomainUrl

    @property
    def DomainType(self):
        r"""Type. 1: allowlist; 2: blocklist.
        :rtype: int
        """
        return self._DomainType

    @DomainType.setter
    def DomainType(self, DomainType):
        self._DomainType = DomainType

    @property
    def CreateUser(self):
        r"""Creator
        :rtype: str
        """
        return self._CreateUser

    @CreateUser.setter
    def CreateUser(self, CreateUser):
        self._CreateUser = CreateUser

    @property
    def CreateTime(self):
        r"""Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateUser(self):
        r"""Specifies the updater.
        :rtype: str
        """
        return self._UpdateUser

    @UpdateUser.setter
    def UpdateUser(self, UpdateUser):
        self._UpdateUser = UpdateUser

    @property
    def UpdateTime(self):
        r"""Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._DomainUrl = params.get("DomainUrl")
        self._DomainType = params.get("DomainType")
        self._CreateUser = params.get("CreateUser")
        self._CreateTime = params.get("CreateTime")
        self._UpdateUser = params.get("UpdateUser")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGlobalDomainsResp(AbstractModel):
    r"""Global domain name page list

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _DataList: Describes the domain information.
        :type DataList: list of DescribeGlobalDomainsListData
        """
        self._TotalCount = None
        self._DataList = None

    @property
    def TotalCount(self):
        r"""Total number
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataList(self):
        r"""Describes the domain information.
        :rtype: list of DescribeGlobalDomainsListData
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = DescribeGlobalDomainsListData()
                obj._deserialize(item)
                self._DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGlobalOverviewDataSummaryRequest(AbstractModel):
    r"""DescribeGlobalOverviewDataSummary request structure.

    """

    def __init__(self):
        r"""
        :param _DataType: string: Overview
        :type DataType: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _DataTime: Date in YYYYMMDD format
        :type DataTime: int
        """
        self._DataType = None
        self._PlatformId = None
        self._DataTime = None

    @property
    def DataType(self):
        r"""string: Overview
        :rtype: str
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def DataTime(self):
        r"""Date in YYYYMMDD format
        :rtype: int
        """
        return self._DataTime

    @DataTime.setter
    def DataTime(self, DataTime):
        self._DataTime = DataTime


    def _deserialize(self, params):
        self._DataType = params.get("DataType")
        self._PlatformId = params.get("PlatformId")
        self._DataTime = params.get("DataTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGlobalOverviewDataSummaryResponse(AbstractModel):
    r"""DescribeGlobalOverviewDataSummary response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display at the top of the page
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.AccessAnalysisOverview`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display at the top of the page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.AccessAnalysisOverview`
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
        if params.get("Data") is not None:
            self._Data = AccessAnalysisOverview()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeGlobalOverviewReportDetailRequest(AbstractModel):
    r"""DescribeGlobalOverviewReportDetail request structure.

    """

    def __init__(self):
        r"""
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _ReportId: Parameter value: mnp_data_analysis
        :type ReportId: str
        :param _IndexId: Parameter value: app_num|corp_num|miniapp_num|miniapp_visit_pv|minigame_num|minigame_visit_pv
        :type IndexId: str
        :param _QueryData: Base64 string containing start and end time: {"BeginDate":20251111,"EndDate":20251125}
        :type QueryData: str
        """
        self._PlatformId = None
        self._ReportId = None
        self._IndexId = None
        self._QueryData = None

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ReportId(self):
        r"""Parameter value: mnp_data_analysis
        :rtype: str
        """
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def IndexId(self):
        r"""Parameter value: app_num|corp_num|miniapp_num|miniapp_visit_pv|minigame_num|minigame_visit_pv
        :rtype: str
        """
        return self._IndexId

    @IndexId.setter
    def IndexId(self, IndexId):
        self._IndexId = IndexId

    @property
    def QueryData(self):
        r"""Base64 string containing start and end time: {"BeginDate":20251111,"EndDate":20251125}
        :rtype: str
        """
        return self._QueryData

    @QueryData.setter
    def QueryData(self, QueryData):
        self._QueryData = QueryData


    def _deserialize(self, params):
        self._PlatformId = params.get("PlatformId")
        self._ReportId = params.get("ReportId")
        self._IndexId = params.get("IndexId")
        self._QueryData = params.get("QueryData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGlobalOverviewReportDetailResponse(AbstractModel):
    r"""DescribeGlobalOverviewReportDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of ReportDataResult
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ReportDataResult
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ReportDataResult()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNGAccessAnalysisDetailRequest(AbstractModel):
    r"""DescribeMNGAccessAnalysisDetail request structure.

    """

    def __init__(self):
        r"""
        :param _TimeBegin: Start time in YYYYMMDD format
        :type TimeBegin: int
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _DataType: Type: 0 Non-production data, 1 Production data
        :type DataType: int
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _Platform: 0 All, 2 Android, 3 iOS
        :type Platform: int
        :param _TimeEnd: End time in YYYYMMDD format
        :type TimeEnd: int
        """
        self._TimeBegin = None
        self._MNPId = None
        self._DataType = None
        self._PlatformId = None
        self._Platform = None
        self._TimeEnd = None

    @property
    def TimeBegin(self):
        r"""Start time in YYYYMMDD format
        :rtype: int
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def DataType(self):
        r"""Type: 0 Non-production data, 1 Production data
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def Platform(self):
        r"""0 All, 2 Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def TimeEnd(self):
        r"""End time in YYYYMMDD format
        :rtype: int
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd


    def _deserialize(self, params):
        self._TimeBegin = params.get("TimeBegin")
        self._MNPId = params.get("MNPId")
        self._DataType = params.get("DataType")
        self._PlatformId = params.get("PlatformId")
        self._Platform = params.get("Platform")
        self._TimeEnd = params.get("TimeEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNGAccessAnalysisDetailResponse(AbstractModel):
    r"""DescribeMNGAccessAnalysisDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display at the top of the page
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of AccessAnalysisDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display at the top of the page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of AccessAnalysisDetail
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AccessAnalysisDetail()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNGAccessAnalysisLineChartRequest(AbstractModel):
    r"""DescribeMNGAccessAnalysisLineChart request structure.

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _ReportId: Fixed value: mnp_data_analysis
        :type ReportId: str
        :param _IndexId: IndexId (optional):
active_device_num: Number of active users
new_device_num: Number of new users
total_user_num: Total number of users
share_num: Number of shares
miniapp_open_num: Number of mini game opens
avg_device_open_num: Average opens per user
avg_device_open_duration: Average visit duration per user
avg_count_open_duration: Average visit duration per session
        :type IndexId: str
        :param _QueryData: Input parameter base64 string: {"DataType":"1","Platform":0,"BeginDate":20251118,"EndDate":20251124}
        :type QueryData: str
        """
        self._MNPId = None
        self._PlatformId = None
        self._ReportId = None
        self._IndexId = None
        self._QueryData = None

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ReportId(self):
        r"""Fixed value: mnp_data_analysis
        :rtype: str
        """
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def IndexId(self):
        r"""IndexId (optional):
active_device_num: Number of active users
new_device_num: Number of new users
total_user_num: Total number of users
share_num: Number of shares
miniapp_open_num: Number of mini game opens
avg_device_open_num: Average opens per user
avg_device_open_duration: Average visit duration per user
avg_count_open_duration: Average visit duration per session
        :rtype: str
        """
        return self._IndexId

    @IndexId.setter
    def IndexId(self, IndexId):
        self._IndexId = IndexId

    @property
    def QueryData(self):
        r"""Input parameter base64 string: {"DataType":"1","Platform":0,"BeginDate":20251118,"EndDate":20251124}
        :rtype: str
        """
        return self._QueryData

    @QueryData.setter
    def QueryData(self, QueryData):
        self._QueryData = QueryData


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._ReportId = params.get("ReportId")
        self._IndexId = params.get("IndexId")
        self._QueryData = params.get("QueryData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNGAccessAnalysisLineChartResponse(AbstractModel):
    r"""DescribeMNGAccessAnalysisLineChart response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of ReportDataResult
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ReportDataResult
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ReportDataResult()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNGAccessAnalysisOverviewRequest(AbstractModel):
    r"""DescribeMNGAccessAnalysisOverview request structure.

    """

    def __init__(self):
        r"""
        :param _TimeBegin: Start time
        :type TimeBegin: int
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _TimeEnd: End time
        :type TimeEnd: int
        :param _ProdData: 1 Production data, 0 Non-production data
        :type ProdData: int
        :param _Platform: Operating system: 0 All, 2-Android, 3 iOS
        :type Platform: int
        """
        self._TimeBegin = None
        self._MNPId = None
        self._PlatformId = None
        self._TimeEnd = None
        self._ProdData = None
        self._Platform = None

    @property
    def TimeBegin(self):
        r"""Start time
        :rtype: int
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def TimeEnd(self):
        r"""End time
        :rtype: int
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def ProdData(self):
        r"""1 Production data, 0 Non-production data
        :rtype: int
        """
        return self._ProdData

    @ProdData.setter
    def ProdData(self, ProdData):
        self._ProdData = ProdData

    @property
    def Platform(self):
        r"""Operating system: 0 All, 2-Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._TimeBegin = params.get("TimeBegin")
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._TimeEnd = params.get("TimeEnd")
        self._ProdData = params.get("ProdData")
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNGAccessAnalysisOverviewResponse(AbstractModel):
    r"""DescribeMNGAccessAnalysisOverview response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display at the top of the page
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.AccessAnalysisOverview`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display at the top of the page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.AccessAnalysisOverview`
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
        if params.get("Data") is not None:
            self._Data = AccessAnalysisOverview()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMNGActiveUserRealTimeStatisticsRequest(AbstractModel):
    r"""DescribeMNGActiveUserRealTimeStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _ReportId: Fixed value: mnp_data_analysis
        :type ReportId: str
        :param _IndexId: IndexId
        :type IndexId: str
        :param _QueryData: Input parameter base64 string: {"Platform":0,"DataType":"1","BeginDate":"20251125","EndDate":"20251125"}
        :type QueryData: str
        """
        self._MNPId = None
        self._PlatformId = None
        self._ReportId = None
        self._IndexId = None
        self._QueryData = None

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ReportId(self):
        r"""Fixed value: mnp_data_analysis
        :rtype: str
        """
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def IndexId(self):
        r"""IndexId
        :rtype: str
        """
        return self._IndexId

    @IndexId.setter
    def IndexId(self, IndexId):
        self._IndexId = IndexId

    @property
    def QueryData(self):
        r"""Input parameter base64 string: {"Platform":0,"DataType":"1","BeginDate":"20251125","EndDate":"20251125"}
        :rtype: str
        """
        return self._QueryData

    @QueryData.setter
    def QueryData(self, QueryData):
        self._QueryData = QueryData


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._ReportId = params.get("ReportId")
        self._IndexId = params.get("IndexId")
        self._QueryData = params.get("QueryData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNGActiveUserRealTimeStatisticsResponse(AbstractModel):
    r"""DescribeMNGActiveUserRealTimeStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of ReportDataResult
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ReportDataResult
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ReportDataResult()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNGAdvertisingDetailRequest(AbstractModel):
    r"""DescribeMNGAdvertisingDetail request structure.

    """

    def __init__(self):
        r"""
        :param _TimeBegin: Start time in YYYYMMDD format
        :type TimeBegin: str
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _TimeEnd: End time in YYYYMMDD format
        :type TimeEnd: str
        :param _AdUnitType: //1-BANNER  2-REWARDED
        :type AdUnitType: str
        :param _Platform: // 2 Android, 3 iOS
        :type Platform: int
        """
        self._TimeBegin = None
        self._MNPId = None
        self._PlatformId = None
        self._TimeEnd = None
        self._AdUnitType = None
        self._Platform = None

    @property
    def TimeBegin(self):
        r"""Start time in YYYYMMDD format
        :rtype: str
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def TimeEnd(self):
        r"""End time in YYYYMMDD format
        :rtype: str
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def AdUnitType(self):
        r"""//1-BANNER  2-REWARDED
        :rtype: str
        """
        return self._AdUnitType

    @AdUnitType.setter
    def AdUnitType(self, AdUnitType):
        self._AdUnitType = AdUnitType

    @property
    def Platform(self):
        r"""// 2 Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._TimeBegin = params.get("TimeBegin")
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._TimeEnd = params.get("TimeEnd")
        self._AdUnitType = params.get("AdUnitType")
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNGAdvertisingDetailResponse(AbstractModel):
    r"""DescribeMNGAdvertisingDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of OverviewDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of OverviewDetail
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = OverviewDetail()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNGAdvertisingLineChartRequest(AbstractModel):
    r"""DescribeMNGAdvertisingLineChart request structure.

    """

    def __init__(self):
        r"""
        :param _TimeBegin: Start time in YYYYMMDD format
        :type TimeBegin: str
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _TimeEnd: End time in YYYYMMDD format
        :type TimeEnd: str
        :param _AdUnitType: //1-BANNER  2-REWARDED
        :type AdUnitType: str
        :param _Platform: // 2 Android, 3 iOS
        :type Platform: int
        """
        self._TimeBegin = None
        self._MNPId = None
        self._PlatformId = None
        self._TimeEnd = None
        self._AdUnitType = None
        self._Platform = None

    @property
    def TimeBegin(self):
        r"""Start time in YYYYMMDD format
        :rtype: str
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def TimeEnd(self):
        r"""End time in YYYYMMDD format
        :rtype: str
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def AdUnitType(self):
        r"""//1-BANNER  2-REWARDED
        :rtype: str
        """
        return self._AdUnitType

    @AdUnitType.setter
    def AdUnitType(self, AdUnitType):
        self._AdUnitType = AdUnitType

    @property
    def Platform(self):
        r"""// 2 Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._TimeBegin = params.get("TimeBegin")
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._TimeEnd = params.get("TimeEnd")
        self._AdUnitType = params.get("AdUnitType")
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNGAdvertisingLineChartResponse(AbstractModel):
    r"""DescribeMNGAdvertisingLineChart response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.AdTrendChart`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.AdTrendChart`
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
        if params.get("Data") is not None:
            self._Data = AdTrendChart()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMNGAdvertisingOverviewRequest(AbstractModel):
    r"""DescribeMNGAdvertisingOverview request structure.

    """

    def __init__(self):
        r"""
        :param _TimeBegin: Start time in YYYYMMDD format
        :type TimeBegin: str
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _TimeEnd: End time in YYYYMMDD format
        :type TimeEnd: str
        :param _AdUnitType: //1-BANNER  2-REWARDED
        :type AdUnitType: str
        :param _Platform: // 2 Android, 3 iOS
        :type Platform: int
        """
        self._TimeBegin = None
        self._MNPId = None
        self._PlatformId = None
        self._TimeEnd = None
        self._AdUnitType = None
        self._Platform = None

    @property
    def TimeBegin(self):
        r"""Start time in YYYYMMDD format
        :rtype: str
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def TimeEnd(self):
        r"""End time in YYYYMMDD format
        :rtype: str
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def AdUnitType(self):
        r"""//1-BANNER  2-REWARDED
        :rtype: str
        """
        return self._AdUnitType

    @AdUnitType.setter
    def AdUnitType(self, AdUnitType):
        self._AdUnitType = AdUnitType

    @property
    def Platform(self):
        r"""// 2 Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._TimeBegin = params.get("TimeBegin")
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._TimeEnd = params.get("TimeEnd")
        self._AdUnitType = params.get("AdUnitType")
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNGAdvertisingOverviewResponse(AbstractModel):
    r"""DescribeMNGAdvertisingOverview response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.AnalysisAdvertOverview`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.AnalysisAdvertOverview`
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
        if params.get("Data") is not None:
            self._Data = AnalysisAdvertOverview()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMNGMAUDataDetailRequest(AbstractModel):
    r"""DescribeMNGMAUDataDetail request structure.

    """

    def __init__(self):
        r"""
        :param _DataType: Type
        :type DataType: int
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _ApplicationId: Superapp ID
        :type ApplicationId: str
        :param _MNPId: Mini program appid, required. When provided, the query is performed based on the mini program.
        :type MNPId: str
        :param _MNPTeamId: Mini program team ID
        :type MNPTeamId: int
        """
        self._DataType = None
        self._PlatformId = None
        self._ApplicationId = None
        self._MNPId = None
        self._MNPTeamId = None

    @property
    def DataType(self):
        r"""Type
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ApplicationId(self):
        r"""Superapp ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def MNPId(self):
        r"""Mini program appid, required. When provided, the query is performed based on the mini program.
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def MNPTeamId(self):
        r"""Mini program team ID
        :rtype: int
        """
        return self._MNPTeamId

    @MNPTeamId.setter
    def MNPTeamId(self, MNPTeamId):
        self._MNPTeamId = MNPTeamId


    def _deserialize(self, params):
        self._DataType = params.get("DataType")
        self._PlatformId = params.get("PlatformId")
        self._ApplicationId = params.get("ApplicationId")
        self._MNPId = params.get("MNPId")
        self._MNPTeamId = params.get("MNPTeamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNGMAUDataDetailResponse(AbstractModel):
    r"""DescribeMNGMAUDataDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of MAUDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of MAUDetail
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MAUDetail()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNGMAULineChartRequest(AbstractModel):
    r"""DescribeMNGMAULineChart request structure.

    """

    def __init__(self):
        r"""
        :param _DataType: Type: 0 Non-production data, 1 Production data 
        :type DataType: int
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _ApplicationId: Superapp ID
        :type ApplicationId: str
        :param _MNPTeamId: Mini program team ID
        :type MNPTeamId: int
        :param _MNPId: Mini program appid, required. When provided, the query is performed based on the mini program.
        :type MNPId: str
        """
        self._DataType = None
        self._PlatformId = None
        self._ApplicationId = None
        self._MNPTeamId = None
        self._MNPId = None

    @property
    def DataType(self):
        r"""Type: 0 Non-production data, 1 Production data 
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ApplicationId(self):
        r"""Superapp ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def MNPTeamId(self):
        r"""Mini program team ID
        :rtype: int
        """
        return self._MNPTeamId

    @MNPTeamId.setter
    def MNPTeamId(self, MNPTeamId):
        self._MNPTeamId = MNPTeamId

    @property
    def MNPId(self):
        r"""Mini program appid, required. When provided, the query is performed based on the mini program.
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId


    def _deserialize(self, params):
        self._DataType = params.get("DataType")
        self._PlatformId = params.get("PlatformId")
        self._ApplicationId = params.get("ApplicationId")
        self._MNPTeamId = params.get("MNPTeamId")
        self._MNPId = params.get("MNPId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNGMAULineChartResponse(AbstractModel):
    r"""DescribeMNGMAULineChart response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display at the top of the page
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of MNGMAULineChartData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display at the top of the page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of MNGMAULineChartData
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MNGMAULineChartData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNGMAUMonthlyComparisonMetricCardRequest(AbstractModel):
    r"""DescribeMNGMAUMonthlyComparisonMetricCard request structure.

    """

    def __init__(self):
        r"""
        :param _SourceMonth: Start time in YYYYMMDD format
        :type SourceMonth: int
        :param _DataType: Type: 0 Non-production data, 1 Production data 
        :type DataType: int
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _TargetMonth: End time in YYYYMMDD format
        :type TargetMonth: int
        :param _ApplicationId: Superapp ID starting with App
        :type ApplicationId: str
        :param _MNPId: Mini program appid, required. When provided, the query is performed based on the mini program.
        :type MNPId: str
        :param _MNPTeamId: Mini program team ID, required. When provided, the query is performed based on the mini program team.
        :type MNPTeamId: int
        """
        self._SourceMonth = None
        self._DataType = None
        self._PlatformId = None
        self._TargetMonth = None
        self._ApplicationId = None
        self._MNPId = None
        self._MNPTeamId = None

    @property
    def SourceMonth(self):
        r"""Start time in YYYYMMDD format
        :rtype: int
        """
        return self._SourceMonth

    @SourceMonth.setter
    def SourceMonth(self, SourceMonth):
        self._SourceMonth = SourceMonth

    @property
    def DataType(self):
        r"""Type: 0 Non-production data, 1 Production data 
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def TargetMonth(self):
        r"""End time in YYYYMMDD format
        :rtype: int
        """
        return self._TargetMonth

    @TargetMonth.setter
    def TargetMonth(self, TargetMonth):
        self._TargetMonth = TargetMonth

    @property
    def ApplicationId(self):
        r"""Superapp ID starting with App
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def MNPId(self):
        r"""Mini program appid, required. When provided, the query is performed based on the mini program.
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def MNPTeamId(self):
        r"""Mini program team ID, required. When provided, the query is performed based on the mini program team.
        :rtype: int
        """
        return self._MNPTeamId

    @MNPTeamId.setter
    def MNPTeamId(self, MNPTeamId):
        self._MNPTeamId = MNPTeamId


    def _deserialize(self, params):
        self._SourceMonth = params.get("SourceMonth")
        self._DataType = params.get("DataType")
        self._PlatformId = params.get("PlatformId")
        self._TargetMonth = params.get("TargetMonth")
        self._ApplicationId = params.get("ApplicationId")
        self._MNPId = params.get("MNPId")
        self._MNPTeamId = params.get("MNPTeamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNGMAUMonthlyComparisonMetricCardResponse(AbstractModel):
    r"""DescribeMNGMAUMonthlyComparisonMetricCard response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display at the top of the page
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.MAUIndicatorCard`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display at the top of the page
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.MAUIndicatorCard`
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
        if params.get("Data") is not None:
            self._Data = MAUIndicatorCard()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMNGPaymentLineChartRequest(AbstractModel):
    r"""DescribeMNGPaymentLineChart request structure.

    """

    def __init__(self):
        r"""
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _ReportId: Fixed value: payment_data_analysis
        :type ReportId: str
        :param _IndexId: Valid values:
mng_paid_amount: Virtual payment amount,
paid_user_num: Number of paying users,
new_paid_user_num: Number of new paying users,
new_paid_user_amount: Revenue from new paying users,
new_paid_user_ratio: Percentage of new users who made payments,
arppu: Average revenue per paying user (ARPPU),
mng_refund_num: Number of refund orders
mng_refund_amount: Refund amount
        :type IndexId: str
        :param _QueryData: Input parameter base64 string: {"Platform":0,"MnpId":"mgcp5xc2yzw8aixv","BeginDate":20251028,"EndDate":20251126,"DataType":"1","PaymentType":2}
        :type QueryData: str
        """
        self._PlatformId = None
        self._ReportId = None
        self._IndexId = None
        self._QueryData = None

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ReportId(self):
        r"""Fixed value: payment_data_analysis
        :rtype: str
        """
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def IndexId(self):
        r"""Valid values:
mng_paid_amount: Virtual payment amount,
paid_user_num: Number of paying users,
new_paid_user_num: Number of new paying users,
new_paid_user_amount: Revenue from new paying users,
new_paid_user_ratio: Percentage of new users who made payments,
arppu: Average revenue per paying user (ARPPU),
mng_refund_num: Number of refund orders
mng_refund_amount: Refund amount
        :rtype: str
        """
        return self._IndexId

    @IndexId.setter
    def IndexId(self, IndexId):
        self._IndexId = IndexId

    @property
    def QueryData(self):
        r"""Input parameter base64 string: {"Platform":0,"MnpId":"mgcp5xc2yzw8aixv","BeginDate":20251028,"EndDate":20251126,"DataType":"1","PaymentType":2}
        :rtype: str
        """
        return self._QueryData

    @QueryData.setter
    def QueryData(self, QueryData):
        self._QueryData = QueryData


    def _deserialize(self, params):
        self._PlatformId = params.get("PlatformId")
        self._ReportId = params.get("ReportId")
        self._IndexId = params.get("IndexId")
        self._QueryData = params.get("QueryData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNGPaymentLineChartResponse(AbstractModel):
    r"""DescribeMNGPaymentLineChart response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of ReportDataResult
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ReportDataResult
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ReportDataResult()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNGPaymentOverviewRequest(AbstractModel):
    r"""DescribeMNGPaymentOverview request structure.

    """

    def __init__(self):
        r"""
        :param _TimeBegin: Start time
        :type TimeBegin: int
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _DataType: Type: 0 Non-production data, 1 Production data
        :type DataType: int
        :param _TimeEnd: End time
        :type TimeEnd: int
        :param _Platform: Operating system: 0 All, 2 Android, 3 iOS
        :type Platform: int
        """
        self._TimeBegin = None
        self._MNPId = None
        self._PlatformId = None
        self._DataType = None
        self._TimeEnd = None
        self._Platform = None

    @property
    def TimeBegin(self):
        r"""Start time
        :rtype: int
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def DataType(self):
        r"""Type: 0 Non-production data, 1 Production data
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def TimeEnd(self):
        r"""End time
        :rtype: int
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def Platform(self):
        r"""Operating system: 0 All, 2 Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._TimeBegin = params.get("TimeBegin")
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._DataType = params.get("DataType")
        self._TimeEnd = params.get("TimeEnd")
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNGPaymentOverviewResponse(AbstractModel):
    r"""DescribeMNGPaymentOverview response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.MNGPaymentOverview`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.MNGPaymentOverview`
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
        if params.get("Data") is not None:
            self._Data = MNGPaymentOverview()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMNGPaymentReportDetailRequest(AbstractModel):
    r"""DescribeMNGPaymentReportDetail request structure.

    """

    def __init__(self):
        r"""
        :param _TimeBegin: Start time
        :type TimeBegin: int
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _DataType: Type: 0 Non-production data, 1 Production data
        :type DataType: int
        :param _TimeEnd: End time
        :type TimeEnd: int
        :param _Platform: Operating system: 0 All, 2-Android, 3 iOS
        :type Platform: int
        """
        self._TimeBegin = None
        self._MNPId = None
        self._PlatformId = None
        self._DataType = None
        self._TimeEnd = None
        self._Platform = None

    @property
    def TimeBegin(self):
        r"""Start time
        :rtype: int
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def DataType(self):
        r"""Type: 0 Non-production data, 1 Production data
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def TimeEnd(self):
        r"""End time
        :rtype: int
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def Platform(self):
        r"""Operating system: 0 All, 2-Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._TimeBegin = params.get("TimeBegin")
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._DataType = params.get("DataType")
        self._TimeEnd = params.get("TimeEnd")
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNGPaymentReportDetailResponse(AbstractModel):
    r"""DescribeMNGPaymentReportDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of MNGPaymentOverview
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of MNGPaymentOverview
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MNGPaymentOverview()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNGPaymentRetentionAnalysisRequest(AbstractModel):
    r"""DescribeMNGPaymentRetentionAnalysis request structure.

    """

    def __init__(self):
        r"""
        :param _TimeBegin: Start time in YYYYMMDD format
        :type TimeBegin: int
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _DataType: Type: 0 Non-production data, 1 Production data
        :type DataType: int
        :param _TimeEnd: End time in YYYYMMDD format
        :type TimeEnd: int
        :param _Platform: 0 All, 2-Android, 3 iOS
        :type Platform: int
        """
        self._TimeBegin = None
        self._MNPId = None
        self._PlatformId = None
        self._DataType = None
        self._TimeEnd = None
        self._Platform = None

    @property
    def TimeBegin(self):
        r"""Start time in YYYYMMDD format
        :rtype: int
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def DataType(self):
        r"""Type: 0 Non-production data, 1 Production data
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def TimeEnd(self):
        r"""End time in YYYYMMDD format
        :rtype: int
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def Platform(self):
        r"""0 All, 2-Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._TimeBegin = params.get("TimeBegin")
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._DataType = params.get("DataType")
        self._TimeEnd = params.get("TimeEnd")
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNGPaymentRetentionAnalysisResponse(AbstractModel):
    r"""DescribeMNGPaymentRetentionAnalysis response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of PaymentActiveRetention
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of PaymentActiveRetention
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = PaymentActiveRetention()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNGRetentionDataRequest(AbstractModel):
    r"""DescribeMNGRetentionData request structure.

    """

    def __init__(self):
        r"""
        :param _TimeBegin: Start time
        :type TimeBegin: int
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _DataType: Type: 1 Production data, 0 Non-production data
        :type DataType: int
        :param _TimeEnd: End time
        :type TimeEnd: int
        :param _Platform: 0 All, 2 Android, 3 iOS
        :type Platform: int
        """
        self._TimeBegin = None
        self._MNPId = None
        self._PlatformId = None
        self._DataType = None
        self._TimeEnd = None
        self._Platform = None

    @property
    def TimeBegin(self):
        r"""Start time
        :rtype: int
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def DataType(self):
        r"""Type: 1 Production data, 0 Non-production data
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def TimeEnd(self):
        r"""End time
        :rtype: int
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def Platform(self):
        r"""0 All, 2 Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._TimeBegin = params.get("TimeBegin")
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._DataType = params.get("DataType")
        self._TimeEnd = params.get("TimeEnd")
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNGRetentionDataResponse(AbstractModel):
    r"""DescribeMNGRetentionData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of RetentionData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of RetentionData
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RetentionData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNPAccessAnalysisOverviewRequest(AbstractModel):
    r"""DescribeMNPAccessAnalysisOverview request structure.

    """

    def __init__(self):
        r"""
        :param _TimeBegin: Start time: 20251123 (example)
        :type TimeBegin: int
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _TimeEnd: End time: 20251123 (example)
        :type TimeEnd: int
        :param _ProdData: 1 Production data, 0 Non-production data
        :type ProdData: int
        :param _Platform: Operating system: 0 All, 2 Android, 3 iOS
        :type Platform: int
        """
        self._TimeBegin = None
        self._MNPId = None
        self._PlatformId = None
        self._TimeEnd = None
        self._ProdData = None
        self._Platform = None

    @property
    def TimeBegin(self):
        r"""Start time: 20251123 (example)
        :rtype: int
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def TimeEnd(self):
        r"""End time: 20251123 (example)
        :rtype: int
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def ProdData(self):
        r"""1 Production data, 0 Non-production data
        :rtype: int
        """
        return self._ProdData

    @ProdData.setter
    def ProdData(self, ProdData):
        self._ProdData = ProdData

    @property
    def Platform(self):
        r"""Operating system: 0 All, 2 Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._TimeBegin = params.get("TimeBegin")
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._TimeEnd = params.get("TimeEnd")
        self._ProdData = params.get("ProdData")
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPAccessAnalysisOverviewResponse(AbstractModel):
    r"""DescribeMNPAccessAnalysisOverview response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display at the top of the page
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.AccessAnalysisOverview`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display at the top of the page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.AccessAnalysisOverview`
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
        if params.get("Data") is not None:
            self._Data = AccessAnalysisOverview()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMNPActiveUserRealTimeStatisticsRequest(AbstractModel):
    r"""DescribeMNPActiveUserRealTimeStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _ReportId: Fixed value: mnp_data_analysis
        :type ReportId: str
        :param _IndexId: IndexId 
realtime_pv_num or realtime_uv_num
        :type IndexId: str
        :param _QueryData: Input parameter base64 string: {"Platform":0,"DataType":"1","BeginDate":"20251125","EndDate":"20251125"}
        :type QueryData: str
        """
        self._MNPId = None
        self._PlatformId = None
        self._ReportId = None
        self._IndexId = None
        self._QueryData = None

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ReportId(self):
        r"""Fixed value: mnp_data_analysis
        :rtype: str
        """
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def IndexId(self):
        r"""IndexId 
realtime_pv_num or realtime_uv_num
        :rtype: str
        """
        return self._IndexId

    @IndexId.setter
    def IndexId(self, IndexId):
        self._IndexId = IndexId

    @property
    def QueryData(self):
        r"""Input parameter base64 string: {"Platform":0,"DataType":"1","BeginDate":"20251125","EndDate":"20251125"}
        :rtype: str
        """
        return self._QueryData

    @QueryData.setter
    def QueryData(self, QueryData):
        self._QueryData = QueryData


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._ReportId = params.get("ReportId")
        self._IndexId = params.get("IndexId")
        self._QueryData = params.get("QueryData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPActiveUserRealTimeStatisticsResponse(AbstractModel):
    r"""DescribeMNPActiveUserRealTimeStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of ReportDataResult
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ReportDataResult
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ReportDataResult()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNPAdvertisingDetailRequest(AbstractModel):
    r"""DescribeMNPAdvertisingDetail request structure.

    """

    def __init__(self):
        r"""
        :param _TimeBegin: Start time in YYYYMMDD format
        :type TimeBegin: str
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _TimeEnd: End time in YYYYMMDD format
        :type TimeEnd: str
        :param _Platform: // 2 Android, 3 iOS
        :type Platform: int
        :param _AdUnitType: //1-BANNER  2-REWARDED
        :type AdUnitType: str
        """
        self._TimeBegin = None
        self._MNPId = None
        self._PlatformId = None
        self._TimeEnd = None
        self._Platform = None
        self._AdUnitType = None

    @property
    def TimeBegin(self):
        r"""Start time in YYYYMMDD format
        :rtype: str
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def TimeEnd(self):
        r"""End time in YYYYMMDD format
        :rtype: str
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def Platform(self):
        r"""// 2 Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def AdUnitType(self):
        r"""//1-BANNER  2-REWARDED
        :rtype: str
        """
        return self._AdUnitType

    @AdUnitType.setter
    def AdUnitType(self, AdUnitType):
        self._AdUnitType = AdUnitType


    def _deserialize(self, params):
        self._TimeBegin = params.get("TimeBegin")
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._TimeEnd = params.get("TimeEnd")
        self._Platform = params.get("Platform")
        self._AdUnitType = params.get("AdUnitType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPAdvertisingDetailResponse(AbstractModel):
    r"""DescribeMNPAdvertisingDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of MAUDetailData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of MAUDetailData
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MAUDetailData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNPAllStageVersionsRequest(AbstractModel):
    r"""DescribeMNPAllStageVersions request structure.

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._MNPId = None
        self._PlatformId = None

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPAllStageVersionsResponse(AbstractModel):
    r"""DescribeMNPAllStageVersions response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of DescribeMPAllStageVersionsResp
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DescribeMPAllStageVersionsResp
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeMPAllStageVersionsResp()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNPApprovalListData(AbstractModel):
    r"""List of mini program approval requests of the application

    """

    def __init__(self):
        r"""
        :param _ApprovalNo: Approval ticket ID
        :type ApprovalNo: str
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _ApprovalStatus: Approval status. valid values: 1 (processing), 2 (rejected), 3 (approved), 4 (cancelled).
        :type ApprovalStatus: int
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _MNPVersion: Mini program version.
        :type MNPVersion: str
        :param _MNPVersionId: Mini program version ID
        :type MNPVersionId: int
        :param _ApplyUser: Applicant
        :type ApplyUser: str
        :param _ApplyTime: Application time
        :type ApplyTime: str
        :param _MNPName: Mini program name
        :type MNPName: str
        :param _MNPIcon: Mini program icon
        :type MNPIcon: str
        :param _ApplicationName: Application name
        :type ApplicationName: str
        :param _ApplicationLogo: Specifies the application icon.
        :type ApplicationLogo: str
        :param _TeamId: Team ID
        :type TeamId: str
        :param _TeamName: Team name
        :type TeamName: str
        :param _MNPQrCodeUrl: Mini program review qr code.
        :type MNPQrCodeUrl: str
        :param _MNPType: Mini program type
        :type MNPType: str
        :param _ApprovalUser: Specifies the reviewer.
        :type ApprovalUser: str
        :param _ApprovalTime: Approval time.
        :type ApprovalTime: str
        :param _ApprovalNote: Approval notes
        :type ApprovalNote: str
        """
        self._ApprovalNo = None
        self._ApplicationId = None
        self._ApprovalStatus = None
        self._MNPId = None
        self._MNPVersion = None
        self._MNPVersionId = None
        self._ApplyUser = None
        self._ApplyTime = None
        self._MNPName = None
        self._MNPIcon = None
        self._ApplicationName = None
        self._ApplicationLogo = None
        self._TeamId = None
        self._TeamName = None
        self._MNPQrCodeUrl = None
        self._MNPType = None
        self._ApprovalUser = None
        self._ApprovalTime = None
        self._ApprovalNote = None

    @property
    def ApprovalNo(self):
        r"""Approval ticket ID
        :rtype: str
        """
        return self._ApprovalNo

    @ApprovalNo.setter
    def ApprovalNo(self, ApprovalNo):
        self._ApprovalNo = ApprovalNo

    @property
    def ApplicationId(self):
        r"""Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApprovalStatus(self):
        r"""Approval status. valid values: 1 (processing), 2 (rejected), 3 (approved), 4 (cancelled).
        :rtype: int
        """
        return self._ApprovalStatus

    @ApprovalStatus.setter
    def ApprovalStatus(self, ApprovalStatus):
        self._ApprovalStatus = ApprovalStatus

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def MNPVersion(self):
        r"""Mini program version.
        :rtype: str
        """
        return self._MNPVersion

    @MNPVersion.setter
    def MNPVersion(self, MNPVersion):
        self._MNPVersion = MNPVersion

    @property
    def MNPVersionId(self):
        r"""Mini program version ID
        :rtype: int
        """
        return self._MNPVersionId

    @MNPVersionId.setter
    def MNPVersionId(self, MNPVersionId):
        self._MNPVersionId = MNPVersionId

    @property
    def ApplyUser(self):
        r"""Applicant
        :rtype: str
        """
        return self._ApplyUser

    @ApplyUser.setter
    def ApplyUser(self, ApplyUser):
        self._ApplyUser = ApplyUser

    @property
    def ApplyTime(self):
        r"""Application time
        :rtype: str
        """
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def MNPName(self):
        r"""Mini program name
        :rtype: str
        """
        return self._MNPName

    @MNPName.setter
    def MNPName(self, MNPName):
        self._MNPName = MNPName

    @property
    def MNPIcon(self):
        r"""Mini program icon
        :rtype: str
        """
        return self._MNPIcon

    @MNPIcon.setter
    def MNPIcon(self, MNPIcon):
        self._MNPIcon = MNPIcon

    @property
    def ApplicationName(self):
        r"""Application name
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def ApplicationLogo(self):
        r"""Specifies the application icon.
        :rtype: str
        """
        return self._ApplicationLogo

    @ApplicationLogo.setter
    def ApplicationLogo(self, ApplicationLogo):
        self._ApplicationLogo = ApplicationLogo

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def TeamName(self):
        r"""Team name
        :rtype: str
        """
        return self._TeamName

    @TeamName.setter
    def TeamName(self, TeamName):
        self._TeamName = TeamName

    @property
    def MNPQrCodeUrl(self):
        r"""Mini program review qr code.
        :rtype: str
        """
        return self._MNPQrCodeUrl

    @MNPQrCodeUrl.setter
    def MNPQrCodeUrl(self, MNPQrCodeUrl):
        self._MNPQrCodeUrl = MNPQrCodeUrl

    @property
    def MNPType(self):
        r"""Mini program type
        :rtype: str
        """
        return self._MNPType

    @MNPType.setter
    def MNPType(self, MNPType):
        self._MNPType = MNPType

    @property
    def ApprovalUser(self):
        r"""Specifies the reviewer.
        :rtype: str
        """
        return self._ApprovalUser

    @ApprovalUser.setter
    def ApprovalUser(self, ApprovalUser):
        self._ApprovalUser = ApprovalUser

    @property
    def ApprovalTime(self):
        r"""Approval time.
        :rtype: str
        """
        return self._ApprovalTime

    @ApprovalTime.setter
    def ApprovalTime(self, ApprovalTime):
        self._ApprovalTime = ApprovalTime

    @property
    def ApprovalNote(self):
        r"""Approval notes
        :rtype: str
        """
        return self._ApprovalNote

    @ApprovalNote.setter
    def ApprovalNote(self, ApprovalNote):
        self._ApprovalNote = ApprovalNote


    def _deserialize(self, params):
        self._ApprovalNo = params.get("ApprovalNo")
        self._ApplicationId = params.get("ApplicationId")
        self._ApprovalStatus = params.get("ApprovalStatus")
        self._MNPId = params.get("MNPId")
        self._MNPVersion = params.get("MNPVersion")
        self._MNPVersionId = params.get("MNPVersionId")
        self._ApplyUser = params.get("ApplyUser")
        self._ApplyTime = params.get("ApplyTime")
        self._MNPName = params.get("MNPName")
        self._MNPIcon = params.get("MNPIcon")
        self._ApplicationName = params.get("ApplicationName")
        self._ApplicationLogo = params.get("ApplicationLogo")
        self._TeamId = params.get("TeamId")
        self._TeamName = params.get("TeamName")
        self._MNPQrCodeUrl = params.get("MNPQrCodeUrl")
        self._MNPType = params.get("MNPType")
        self._ApprovalUser = params.get("ApprovalUser")
        self._ApprovalTime = params.get("ApprovalTime")
        self._ApprovalNote = params.get("ApprovalNote")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPApprovalListRequest(AbstractModel):
    r"""DescribeMNPApprovalList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Number of results per page
        :type Limit: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _ApprovalStatusList: Approval status. 1: Processing; 2: Rejected; 3: Approved; 4 Cancelled
        :type ApprovalStatusList: list of int
        :param _Keyword: Keywords of the mini program name to search
        :type Keyword: str
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _TeamId: Team ID
        :type TeamId: str
        """
        self._Offset = None
        self._Limit = None
        self._PlatformId = None
        self._ApprovalStatusList = None
        self._Keyword = None
        self._ApplicationId = None
        self._TeamId = None

    @property
    def Offset(self):
        r"""Page offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of results per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ApprovalStatusList(self):
        r"""Approval status. 1: Processing; 2: Rejected; 3: Approved; 4 Cancelled
        :rtype: list of int
        """
        return self._ApprovalStatusList

    @ApprovalStatusList.setter
    def ApprovalStatusList(self, ApprovalStatusList):
        self._ApprovalStatusList = ApprovalStatusList

    @property
    def Keyword(self):
        r"""Keywords of the mini program name to search
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def ApplicationId(self):
        r"""Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PlatformId = params.get("PlatformId")
        self._ApprovalStatusList = params.get("ApprovalStatusList")
        self._Keyword = params.get("Keyword")
        self._ApplicationId = params.get("ApplicationId")
        self._TeamId = params.get("TeamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPApprovalListResp(AbstractModel):
    r"""List of mini program approval requests of an application

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _DataList: List information
        :type DataList: list of DescribeMNPApprovalListData
        """
        self._TotalCount = None
        self._DataList = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataList(self):
        r"""List information
        :rtype: list of DescribeMNPApprovalListData
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = DescribeMNPApprovalListData()
                obj._deserialize(item)
                self._DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPApprovalListResponse(AbstractModel):
    r"""DescribeMNPApprovalList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPApprovalListResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPApprovalListResp`
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
        if params.get("Data") is not None:
            self._Data = DescribeMNPApprovalListResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMNPCategoryRequest(AbstractModel):
    r"""DescribeMNPCategory request structure.

    """

    def __init__(self):
        r"""
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._PlatformId = None

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPCategoryResponse(AbstractModel):
    r"""DescribeMNPCategory response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of MNPTypeDefine
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of MNPTypeDefine
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MNPTypeDefine()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNPDomainACLRequest(AbstractModel):
    r"""DescribeMNPDomainACL request structure.

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._MNPId = None
        self._PlatformId = None

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPDomainACLResponse(AbstractModel):
    r"""DescribeMNPDomainACL response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of DescribeDomainInfoParam
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DescribeDomainInfoParam
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeDomainInfoParam()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNPListData(AbstractModel):
    r"""Mini program list

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _MNPIcon: Mini program icon
        :type MNPIcon: str
        :param _MNPName: Mini program name
        :type MNPName: str
        :param _TeamName: Name of the associated team
        :type TeamName: str
        :param _MNPType: Mini program type
        :type MNPType: str
        :param _Status: Specifies the mini program listing status. valid values: 1 (submitted), 2 (removed).
        :type Status: int
        :param _MNPIntro: Mini program introduction
        :type MNPIntro: str
        :param _CreateUser: Creator
        :type CreateUser: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _UpdateUser: Specifies the updater.
        :type UpdateUser: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _ApplicationName: Application name
        :type ApplicationName: str
        :param _EffectStatus: Effective status of the bound application. valid values: 1 (not effective), 2 (effective).
        :type EffectStatus: int
        :param _EffectMNPVersionId: Specifies the ID of the application bound with the mini program.
        :type EffectMNPVersionId: int
        :param _EffectMNPVersion: Specifies the effective version number of the application bound to the mini program.
        :type EffectMNPVersion: str
        """
        self._MNPId = None
        self._MNPIcon = None
        self._MNPName = None
        self._TeamName = None
        self._MNPType = None
        self._Status = None
        self._MNPIntro = None
        self._CreateUser = None
        self._CreateTime = None
        self._UpdateUser = None
        self._UpdateTime = None
        self._ApplicationName = None
        self._EffectStatus = None
        self._EffectMNPVersionId = None
        self._EffectMNPVersion = None

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def MNPIcon(self):
        r"""Mini program icon
        :rtype: str
        """
        return self._MNPIcon

    @MNPIcon.setter
    def MNPIcon(self, MNPIcon):
        self._MNPIcon = MNPIcon

    @property
    def MNPName(self):
        r"""Mini program name
        :rtype: str
        """
        return self._MNPName

    @MNPName.setter
    def MNPName(self, MNPName):
        self._MNPName = MNPName

    @property
    def TeamName(self):
        r"""Name of the associated team
        :rtype: str
        """
        return self._TeamName

    @TeamName.setter
    def TeamName(self, TeamName):
        self._TeamName = TeamName

    @property
    def MNPType(self):
        r"""Mini program type
        :rtype: str
        """
        return self._MNPType

    @MNPType.setter
    def MNPType(self, MNPType):
        self._MNPType = MNPType

    @property
    def Status(self):
        r"""Specifies the mini program listing status. valid values: 1 (submitted), 2 (removed).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MNPIntro(self):
        r"""Mini program introduction
        :rtype: str
        """
        return self._MNPIntro

    @MNPIntro.setter
    def MNPIntro(self, MNPIntro):
        self._MNPIntro = MNPIntro

    @property
    def CreateUser(self):
        r"""Creator
        :rtype: str
        """
        return self._CreateUser

    @CreateUser.setter
    def CreateUser(self, CreateUser):
        self._CreateUser = CreateUser

    @property
    def CreateTime(self):
        r"""Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateUser(self):
        r"""Specifies the updater.
        :rtype: str
        """
        return self._UpdateUser

    @UpdateUser.setter
    def UpdateUser(self, UpdateUser):
        self._UpdateUser = UpdateUser

    @property
    def UpdateTime(self):
        r"""Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ApplicationName(self):
        r"""Application name
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def EffectStatus(self):
        r"""Effective status of the bound application. valid values: 1 (not effective), 2 (effective).
        :rtype: int
        """
        return self._EffectStatus

    @EffectStatus.setter
    def EffectStatus(self, EffectStatus):
        self._EffectStatus = EffectStatus

    @property
    def EffectMNPVersionId(self):
        r"""Specifies the ID of the application bound with the mini program.
        :rtype: int
        """
        return self._EffectMNPVersionId

    @EffectMNPVersionId.setter
    def EffectMNPVersionId(self, EffectMNPVersionId):
        self._EffectMNPVersionId = EffectMNPVersionId

    @property
    def EffectMNPVersion(self):
        r"""Specifies the effective version number of the application bound to the mini program.
        :rtype: str
        """
        return self._EffectMNPVersion

    @EffectMNPVersion.setter
    def EffectMNPVersion(self, EffectMNPVersion):
        self._EffectMNPVersion = EffectMNPVersion


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._MNPIcon = params.get("MNPIcon")
        self._MNPName = params.get("MNPName")
        self._TeamName = params.get("TeamName")
        self._MNPType = params.get("MNPType")
        self._Status = params.get("Status")
        self._MNPIntro = params.get("MNPIntro")
        self._CreateUser = params.get("CreateUser")
        self._CreateTime = params.get("CreateTime")
        self._UpdateUser = params.get("UpdateUser")
        self._UpdateTime = params.get("UpdateTime")
        self._ApplicationName = params.get("ApplicationName")
        self._EffectStatus = params.get("EffectStatus")
        self._EffectMNPVersionId = params.get("EffectMNPVersionId")
        self._EffectMNPVersion = params.get("EffectMNPVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPListRequest(AbstractModel):
    r"""DescribeMNPList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Number of results per page
        :type Limit: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _Keyword: Keywords for search (mini program name)
        :type Keyword: str
        :param _TeamId: Team ID
        :type TeamId: str
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        """
        self._Offset = None
        self._Limit = None
        self._PlatformId = None
        self._Keyword = None
        self._TeamId = None
        self._ApplicationId = None

    @property
    def Offset(self):
        r"""Page offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of results per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def Keyword(self):
        r"""Keywords for search (mini program name)
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def ApplicationId(self):
        r"""Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PlatformId = params.get("PlatformId")
        self._Keyword = params.get("Keyword")
        self._TeamId = params.get("TeamId")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPListResp(AbstractModel):
    r"""Mini program list

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _DataList: List information
        :type DataList: list of DescribeMNPListData
        """
        self._TotalCount = None
        self._DataList = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataList(self):
        r"""List information
        :rtype: list of DescribeMNPListData
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = DescribeMNPListData()
                obj._deserialize(item)
                self._DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPListResponse(AbstractModel):
    r"""DescribeMNPList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPListResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPListResp`
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
        if params.get("Data") is not None:
            self._Data = DescribeMNPListResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMNPMAUDataDetailRequest(AbstractModel):
    r"""DescribeMNPMAUDataDetail request structure.

    """

    def __init__(self):
        r"""
        :param _DataType: Type: 0 Non-production data, 1 Production data
        :type DataType: int
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _ApplicationId: Superapp ID
        :type ApplicationId: str
        :param _MNPId: Mini program appid, required. When provided, the query is performed based on the mini program.
        :type MNPId: str
        :param _MNPTeamId: Program team ID, -1 means not provided
        :type MNPTeamId: int
        """
        self._DataType = None
        self._PlatformId = None
        self._ApplicationId = None
        self._MNPId = None
        self._MNPTeamId = None

    @property
    def DataType(self):
        r"""Type: 0 Non-production data, 1 Production data
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ApplicationId(self):
        r"""Superapp ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def MNPId(self):
        r"""Mini program appid, required. When provided, the query is performed based on the mini program.
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def MNPTeamId(self):
        r"""Program team ID, -1 means not provided
        :rtype: int
        """
        return self._MNPTeamId

    @MNPTeamId.setter
    def MNPTeamId(self, MNPTeamId):
        self._MNPTeamId = MNPTeamId


    def _deserialize(self, params):
        self._DataType = params.get("DataType")
        self._PlatformId = params.get("PlatformId")
        self._ApplicationId = params.get("ApplicationId")
        self._MNPId = params.get("MNPId")
        self._MNPTeamId = params.get("MNPTeamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPMAUDataDetailResponse(AbstractModel):
    r"""DescribeMNPMAUDataDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of MAUDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of MAUDetail
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MAUDetail()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNPMAULineChartRequest(AbstractModel):
    r"""DescribeMNPMAULineChart request structure.

    """

    def __init__(self):
        r"""
        :param _DataType: Type: 0 Non-production data, 1 Production data
        :type DataType: int
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _ApplicationId: Superapp ID
        :type ApplicationId: str
        :param _MNPId: Mini program appid, required. When provided, the query is performed based on the mini program.
        :type MNPId: str
        :param _MNPTeamId: Mini program team ID
        :type MNPTeamId: int
        """
        self._DataType = None
        self._PlatformId = None
        self._ApplicationId = None
        self._MNPId = None
        self._MNPTeamId = None

    @property
    def DataType(self):
        r"""Type: 0 Non-production data, 1 Production data
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ApplicationId(self):
        r"""Superapp ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def MNPId(self):
        r"""Mini program appid, required. When provided, the query is performed based on the mini program.
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def MNPTeamId(self):
        r"""Mini program team ID
        :rtype: int
        """
        return self._MNPTeamId

    @MNPTeamId.setter
    def MNPTeamId(self, MNPTeamId):
        self._MNPTeamId = MNPTeamId


    def _deserialize(self, params):
        self._DataType = params.get("DataType")
        self._PlatformId = params.get("PlatformId")
        self._ApplicationId = params.get("ApplicationId")
        self._MNPId = params.get("MNPId")
        self._MNPTeamId = params.get("MNPTeamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPMAULineChartResponse(AbstractModel):
    r"""DescribeMNPMAULineChart response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of MAUChartData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of MAUChartData
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MAUChartData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNPMAUMetricCardRequest(AbstractModel):
    r"""DescribeMNPMAUMetricCard request structure.

    """

    def __init__(self):
        r"""
        :param _SourceMonth: Start time in YYYYMMDD format
        :type SourceMonth: int
        :param _DataType: Type: 0 Non-production data, 1 Production data 
        :type DataType: int
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _TargetMonth: End time in YYYYMMDD format
        :type TargetMonth: int
        :param _ApplicationId: Superapp ID starting with App
        :type ApplicationId: str
        :param _MNPId: Mini program appid, required. When provided, the query is performed based on the mini program.
        :type MNPId: str
        :param _MNPTeamId: Mini program team ID, required. When provided, the query is performed based on the mini program team.
        :type MNPTeamId: int
        """
        self._SourceMonth = None
        self._DataType = None
        self._PlatformId = None
        self._TargetMonth = None
        self._ApplicationId = None
        self._MNPId = None
        self._MNPTeamId = None

    @property
    def SourceMonth(self):
        r"""Start time in YYYYMMDD format
        :rtype: int
        """
        return self._SourceMonth

    @SourceMonth.setter
    def SourceMonth(self, SourceMonth):
        self._SourceMonth = SourceMonth

    @property
    def DataType(self):
        r"""Type: 0 Non-production data, 1 Production data 
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def TargetMonth(self):
        r"""End time in YYYYMMDD format
        :rtype: int
        """
        return self._TargetMonth

    @TargetMonth.setter
    def TargetMonth(self, TargetMonth):
        self._TargetMonth = TargetMonth

    @property
    def ApplicationId(self):
        r"""Superapp ID starting with App
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def MNPId(self):
        r"""Mini program appid, required. When provided, the query is performed based on the mini program.
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def MNPTeamId(self):
        r"""Mini program team ID, required. When provided, the query is performed based on the mini program team.
        :rtype: int
        """
        return self._MNPTeamId

    @MNPTeamId.setter
    def MNPTeamId(self, MNPTeamId):
        self._MNPTeamId = MNPTeamId


    def _deserialize(self, params):
        self._SourceMonth = params.get("SourceMonth")
        self._DataType = params.get("DataType")
        self._PlatformId = params.get("PlatformId")
        self._TargetMonth = params.get("TargetMonth")
        self._ApplicationId = params.get("ApplicationId")
        self._MNPId = params.get("MNPId")
        self._MNPTeamId = params.get("MNPTeamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPMAUMetricCardResponse(AbstractModel):
    r"""DescribeMNPMAUMetricCard response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display at the top of the page
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.MAUIndicatorCard`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display at the top of the page
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.MAUIndicatorCard`
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
        if params.get("Data") is not None:
            self._Data = MAUIndicatorCard()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMNPManagerDetailData(AbstractModel):
    r"""Mini program details

    """

    def __init__(self):
        r"""
        :param _MNPType: Mini program type 
        :type MNPType: str
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _MNPName: Mini program name
        :type MNPName: str
        :param _MNPIcon: Mini program icon
        :type MNPIcon: str
        :param _MNPIntro: Mini program introduction
        :type MNPIntro: str
        :param _MNPDesc: Mini program description
        :type MNPDesc: str
        :param _CreateTime: Creation time, timestamp.
        :type CreateTime: str
        :param _CreateUser: Creator
        :type CreateUser: str
        :param _AccessStatus: Access status. 1: not connected; 2: connected.
        :type AccessStatus: int
        :param _TeamName: Name of the associated team
        :type TeamName: str
        :param _TeamId: Team ID
        :type TeamId: str
        :param _Status: Specifies the mini program listing status. valid values: 1 (submitted), 2 (removed).
        :type Status: int
        """
        self._MNPType = None
        self._MNPId = None
        self._MNPName = None
        self._MNPIcon = None
        self._MNPIntro = None
        self._MNPDesc = None
        self._CreateTime = None
        self._CreateUser = None
        self._AccessStatus = None
        self._TeamName = None
        self._TeamId = None
        self._Status = None

    @property
    def MNPType(self):
        r"""Mini program type 
        :rtype: str
        """
        return self._MNPType

    @MNPType.setter
    def MNPType(self, MNPType):
        self._MNPType = MNPType

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def MNPName(self):
        r"""Mini program name
        :rtype: str
        """
        return self._MNPName

    @MNPName.setter
    def MNPName(self, MNPName):
        self._MNPName = MNPName

    @property
    def MNPIcon(self):
        r"""Mini program icon
        :rtype: str
        """
        return self._MNPIcon

    @MNPIcon.setter
    def MNPIcon(self, MNPIcon):
        self._MNPIcon = MNPIcon

    @property
    def MNPIntro(self):
        r"""Mini program introduction
        :rtype: str
        """
        return self._MNPIntro

    @MNPIntro.setter
    def MNPIntro(self, MNPIntro):
        self._MNPIntro = MNPIntro

    @property
    def MNPDesc(self):
        r"""Mini program description
        :rtype: str
        """
        return self._MNPDesc

    @MNPDesc.setter
    def MNPDesc(self, MNPDesc):
        self._MNPDesc = MNPDesc

    @property
    def CreateTime(self):
        r"""Creation time, timestamp.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CreateUser(self):
        r"""Creator
        :rtype: str
        """
        return self._CreateUser

    @CreateUser.setter
    def CreateUser(self, CreateUser):
        self._CreateUser = CreateUser

    @property
    def AccessStatus(self):
        r"""Access status. 1: not connected; 2: connected.
        :rtype: int
        """
        return self._AccessStatus

    @AccessStatus.setter
    def AccessStatus(self, AccessStatus):
        self._AccessStatus = AccessStatus

    @property
    def TeamName(self):
        r"""Name of the associated team
        :rtype: str
        """
        return self._TeamName

    @TeamName.setter
    def TeamName(self, TeamName):
        self._TeamName = TeamName

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def Status(self):
        r"""Specifies the mini program listing status. valid values: 1 (submitted), 2 (removed).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._MNPType = params.get("MNPType")
        self._MNPId = params.get("MNPId")
        self._MNPName = params.get("MNPName")
        self._MNPIcon = params.get("MNPIcon")
        self._MNPIntro = params.get("MNPIntro")
        self._MNPDesc = params.get("MNPDesc")
        self._CreateTime = params.get("CreateTime")
        self._CreateUser = params.get("CreateUser")
        self._AccessStatus = params.get("AccessStatus")
        self._TeamName = params.get("TeamName")
        self._TeamId = params.get("TeamId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPOfflinePackageURLRequest(AbstractModel):
    r"""DescribeMNPOfflinePackageURL request structure.

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._MNPId = None
        self._PlatformId = None

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPOfflinePackageURLResponse(AbstractModel):
    r"""DescribeMNPOfflinePackageURL response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.StringData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.StringData`
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
        if params.get("Data") is not None:
            self._Data = StringData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMNPPageAnalysisDetailRequest(AbstractModel):
    r"""DescribeMNPPageAnalysisDetail request structure.

    """

    def __init__(self):
        r"""
        :param _DataType: Type: 0 Non-production data, 1 Production data
        :type DataType: int
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _TimeBegin: Start time in YYYYMMDD format
        :type TimeBegin: int
        :param _TimeEnd: End time in YYYYMMDD format
        :type TimeEnd: int
        :param _Platform: 0 All, 2 Android, 3 iOS
        :type Platform: int
        """
        self._DataType = None
        self._PlatformId = None
        self._MNPId = None
        self._TimeBegin = None
        self._TimeEnd = None
        self._Platform = None

    @property
    def DataType(self):
        r"""Type: 0 Non-production data, 1 Production data
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def TimeBegin(self):
        r"""Start time in YYYYMMDD format
        :rtype: int
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def TimeEnd(self):
        r"""End time in YYYYMMDD format
        :rtype: int
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def Platform(self):
        r"""0 All, 2 Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._DataType = params.get("DataType")
        self._PlatformId = params.get("PlatformId")
        self._MNPId = params.get("MNPId")
        self._TimeBegin = params.get("TimeBegin")
        self._TimeEnd = params.get("TimeEnd")
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPPageAnalysisDetailResponse(AbstractModel):
    r"""DescribeMNPPageAnalysisDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of VisitData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of VisitData
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VisitData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNPPreviewRequest(AbstractModel):
    r"""DescribeMNPPreview request structure.

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _MNPVersionId: Mini program version ID
        :type MNPVersionId: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._MNPId = None
        self._MNPVersionId = None
        self._PlatformId = None

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def MNPVersionId(self):
        r"""Mini program version ID
        :rtype: int
        """
        return self._MNPVersionId

    @MNPVersionId.setter
    def MNPVersionId(self, MNPVersionId):
        self._MNPVersionId = MNPVersionId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._MNPVersionId = params.get("MNPVersionId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPPreviewResp(AbstractModel):
    r"""Response of querying the preview

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _MNPName: Mini program name
        :type MNPName: str
        :param _MNPDesc: Mini program description
        :type MNPDesc: str
        :param _MNPVersion: Mini program version.
        :type MNPVersion: str
        :param _MNPVersionIntro: Describes the mini program version.
        :type MNPVersionIntro: str
        :param _QRCodeUrl: Specifies the mini program qr code.
        :type QRCodeUrl: str
        :param _PreviewEntrancePath: Specifies the path to the preview version.
        :type PreviewEntrancePath: str
        :param _QRCodeContent: Specifies the qr code content.
        :type QRCodeContent: str
        """
        self._MNPId = None
        self._MNPName = None
        self._MNPDesc = None
        self._MNPVersion = None
        self._MNPVersionIntro = None
        self._QRCodeUrl = None
        self._PreviewEntrancePath = None
        self._QRCodeContent = None

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def MNPName(self):
        r"""Mini program name
        :rtype: str
        """
        return self._MNPName

    @MNPName.setter
    def MNPName(self, MNPName):
        self._MNPName = MNPName

    @property
    def MNPDesc(self):
        r"""Mini program description
        :rtype: str
        """
        return self._MNPDesc

    @MNPDesc.setter
    def MNPDesc(self, MNPDesc):
        self._MNPDesc = MNPDesc

    @property
    def MNPVersion(self):
        r"""Mini program version.
        :rtype: str
        """
        return self._MNPVersion

    @MNPVersion.setter
    def MNPVersion(self, MNPVersion):
        self._MNPVersion = MNPVersion

    @property
    def MNPVersionIntro(self):
        r"""Describes the mini program version.
        :rtype: str
        """
        return self._MNPVersionIntro

    @MNPVersionIntro.setter
    def MNPVersionIntro(self, MNPVersionIntro):
        self._MNPVersionIntro = MNPVersionIntro

    @property
    def QRCodeUrl(self):
        r"""Specifies the mini program qr code.
        :rtype: str
        """
        return self._QRCodeUrl

    @QRCodeUrl.setter
    def QRCodeUrl(self, QRCodeUrl):
        self._QRCodeUrl = QRCodeUrl

    @property
    def PreviewEntrancePath(self):
        r"""Specifies the path to the preview version.
        :rtype: str
        """
        return self._PreviewEntrancePath

    @PreviewEntrancePath.setter
    def PreviewEntrancePath(self, PreviewEntrancePath):
        self._PreviewEntrancePath = PreviewEntrancePath

    @property
    def QRCodeContent(self):
        r"""Specifies the qr code content.
        :rtype: str
        """
        return self._QRCodeContent

    @QRCodeContent.setter
    def QRCodeContent(self, QRCodeContent):
        self._QRCodeContent = QRCodeContent


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._MNPName = params.get("MNPName")
        self._MNPDesc = params.get("MNPDesc")
        self._MNPVersion = params.get("MNPVersion")
        self._MNPVersionIntro = params.get("MNPVersionIntro")
        self._QRCodeUrl = params.get("QRCodeUrl")
        self._PreviewEntrancePath = params.get("PreviewEntrancePath")
        self._QRCodeContent = params.get("QRCodeContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPPreviewResponse(AbstractModel):
    r"""DescribeMNPPreview response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPPreviewResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPPreviewResp`
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
        if params.get("Data") is not None:
            self._Data = DescribeMNPPreviewResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMNPReleasedVersionHistoryRequest(AbstractModel):
    r"""DescribeMNPReleasedVersionHistory request structure.

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._MNPId = None
        self._PlatformId = None

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPReleasedVersionHistoryResponse(AbstractModel):
    r"""DescribeMNPReleasedVersionHistory response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeRevertOnlineVersionPageResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeRevertOnlineVersionPageResp`
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
        if params.get("Data") is not None:
            self._Data = DescribeRevertOnlineVersionPageResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMNPReportDataLineChartRequest(AbstractModel):
    r"""DescribeMNPReportDataLineChart request structure.

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _ReportId: Fixed value: mnp_data_analysis
        :type ReportId: str
        :param _IndexId: IndexId (optional):
active_device_num: Active users
new_device_num: New users
total_user_num: Total users
share_num: Number of shares
miniapp_open_num: Number of opens
avg_device_open_num: Average opens per user
avg_device_open_duration: Average duration per user
avg_count_open_duration: Average duration per session
        :type IndexId: str
        :param _QueryData: Input parameter base64 string: {"DataType":"1","Platform":0,"BeginDate":20251118,"EndDate":20251124}
        :type QueryData: str
        """
        self._MNPId = None
        self._PlatformId = None
        self._ReportId = None
        self._IndexId = None
        self._QueryData = None

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ReportId(self):
        r"""Fixed value: mnp_data_analysis
        :rtype: str
        """
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def IndexId(self):
        r"""IndexId (optional):
active_device_num: Active users
new_device_num: New users
total_user_num: Total users
share_num: Number of shares
miniapp_open_num: Number of opens
avg_device_open_num: Average opens per user
avg_device_open_duration: Average duration per user
avg_count_open_duration: Average duration per session
        :rtype: str
        """
        return self._IndexId

    @IndexId.setter
    def IndexId(self, IndexId):
        self._IndexId = IndexId

    @property
    def QueryData(self):
        r"""Input parameter base64 string: {"DataType":"1","Platform":0,"BeginDate":20251118,"EndDate":20251124}
        :rtype: str
        """
        return self._QueryData

    @QueryData.setter
    def QueryData(self, QueryData):
        self._QueryData = QueryData


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._ReportId = params.get("ReportId")
        self._IndexId = params.get("IndexId")
        self._QueryData = params.get("QueryData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPReportDataLineChartResponse(AbstractModel):
    r"""DescribeMNPReportDataLineChart response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of ReportDataResult
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ReportDataResult
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ReportDataResult()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNPReportDetailRequest(AbstractModel):
    r"""DescribeMNPReportDetail request structure.

    """

    def __init__(self):
        r"""
        :param _TimeBegin: Start time in YYYYMMDD format
        :type TimeBegin: int
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _DataType: Type: 0 Non-production data, 1 Production data
        :type DataType: int
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _Platform: 0 All, 2 Android, 3 iOS
        :type Platform: int
        :param _TimeEnd: End time in YYYYMMDD format
        :type TimeEnd: int
        """
        self._TimeBegin = None
        self._MNPId = None
        self._DataType = None
        self._PlatformId = None
        self._Platform = None
        self._TimeEnd = None

    @property
    def TimeBegin(self):
        r"""Start time in YYYYMMDD format
        :rtype: int
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def DataType(self):
        r"""Type: 0 Non-production data, 1 Production data
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def Platform(self):
        r"""0 All, 2 Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def TimeEnd(self):
        r"""End time in YYYYMMDD format
        :rtype: int
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd


    def _deserialize(self, params):
        self._TimeBegin = params.get("TimeBegin")
        self._MNPId = params.get("MNPId")
        self._DataType = params.get("DataType")
        self._PlatformId = params.get("PlatformId")
        self._Platform = params.get("Platform")
        self._TimeEnd = params.get("TimeEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPReportDetailResponse(AbstractModel):
    r"""DescribeMNPReportDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display at the top of the page
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of AccessAnalysisDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display at the top of the page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of AccessAnalysisDetail
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AccessAnalysisDetail()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNPRequest(AbstractModel):
    r"""DescribeMNP request structure.

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._MNPId = None
        self._PlatformId = None

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPResponse(AbstractModel):
    r"""DescribeMNP response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPManagerDetailData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPManagerDetailData`
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
        if params.get("Data") is not None:
            self._Data = DescribeMNPManagerDetailData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMNPRetentionDataRequest(AbstractModel):
    r"""DescribeMNPRetentionData request structure.

    """

    def __init__(self):
        r"""
        :param _TimeBegin: Start time
        :type TimeBegin: int
        :param _MNPId: Mini program appid
        :type MNPId: str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _DataType: Type: 1 Production data, 0 Non-production data
        :type DataType: int
        :param _TimeEnd: End time
        :type TimeEnd: int
        :param _Platform: 0 All, 2 Android, 3 iOS
        :type Platform: int
        """
        self._TimeBegin = None
        self._MNPId = None
        self._PlatformId = None
        self._DataType = None
        self._TimeEnd = None
        self._Platform = None

    @property
    def TimeBegin(self):
        r"""Start time
        :rtype: int
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def MNPId(self):
        r"""Mini program appid
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def DataType(self):
        r"""Type: 1 Production data, 0 Non-production data
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def TimeEnd(self):
        r"""End time
        :rtype: int
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def Platform(self):
        r"""0 All, 2 Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._TimeBegin = params.get("TimeBegin")
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._DataType = params.get("DataType")
        self._TimeEnd = params.get("TimeEnd")
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPRetentionDataResponse(AbstractModel):
    r"""DescribeMNPRetentionData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of RetentionData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of RetentionData
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RetentionData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMNPSensitiveAPIPermissionApprovalData(AbstractModel):
    r"""Details of a permission request to allow a mini program to call sensitive APIs

    """

    def __init__(self):
        r"""
        :param _APIId: API ID
        :type APIId: str
        :param _APIMethod: API method.
        :type APIMethod: str
        :param _ApplyReason: Reason for application
        :type ApplyReason: str
        :param _RejectReason: Reason for rejection.
        :type RejectReason: str
        :param _ApprovalStatus: Approval status. valid values: 20 (rejected), 30 (approved).
        :type ApprovalStatus: int
        :param _APIDesc: API feature description.
        :type APIDesc: str
        :param _APIType: API type. 1: system; 2: custom.
        :type APIType: int
        """
        self._APIId = None
        self._APIMethod = None
        self._ApplyReason = None
        self._RejectReason = None
        self._ApprovalStatus = None
        self._APIDesc = None
        self._APIType = None

    @property
    def APIId(self):
        r"""API ID
        :rtype: str
        """
        return self._APIId

    @APIId.setter
    def APIId(self, APIId):
        self._APIId = APIId

    @property
    def APIMethod(self):
        r"""API method.
        :rtype: str
        """
        return self._APIMethod

    @APIMethod.setter
    def APIMethod(self, APIMethod):
        self._APIMethod = APIMethod

    @property
    def ApplyReason(self):
        r"""Reason for application
        :rtype: str
        """
        return self._ApplyReason

    @ApplyReason.setter
    def ApplyReason(self, ApplyReason):
        self._ApplyReason = ApplyReason

    @property
    def RejectReason(self):
        r"""Reason for rejection.
        :rtype: str
        """
        return self._RejectReason

    @RejectReason.setter
    def RejectReason(self, RejectReason):
        self._RejectReason = RejectReason

    @property
    def ApprovalStatus(self):
        r"""Approval status. valid values: 20 (rejected), 30 (approved).
        :rtype: int
        """
        return self._ApprovalStatus

    @ApprovalStatus.setter
    def ApprovalStatus(self, ApprovalStatus):
        self._ApprovalStatus = ApprovalStatus

    @property
    def APIDesc(self):
        r"""API feature description.
        :rtype: str
        """
        return self._APIDesc

    @APIDesc.setter
    def APIDesc(self, APIDesc):
        self._APIDesc = APIDesc

    @property
    def APIType(self):
        r"""API type. 1: system; 2: custom.
        :rtype: int
        """
        return self._APIType

    @APIType.setter
    def APIType(self, APIType):
        self._APIType = APIType


    def _deserialize(self, params):
        self._APIId = params.get("APIId")
        self._APIMethod = params.get("APIMethod")
        self._ApplyReason = params.get("ApplyReason")
        self._RejectReason = params.get("RejectReason")
        self._ApprovalStatus = params.get("ApprovalStatus")
        self._APIDesc = params.get("APIDesc")
        self._APIType = params.get("APIType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPSensitiveAPIPermissionApprovalListData(AbstractModel):
    r"""List of permission requests to allow a mini program to call sensitive APIs

    """

    def __init__(self):
        r"""
        :param _ApprovalNo: Approval ID
        :type ApprovalNo: str
        :param _APIId: Sensitive API ID
        :type APIId: str
        :param _APIName: API name
        :type APIName: str
        :param _APIMethod: API request method
        :type APIMethod: str
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _MNPName: Mini program name
        :type MNPName: str
        :param _ApplyUser: Applicant
        :type ApplyUser: str
        :param _ApplyTime: Application time
        :type ApplyTime: str
        :param _ApplyNote: Application notes
        :type ApplyNote: str
        :param _ApprovalStatus: Approval status. 1: Processing; 20: Rejected; 30: Approved
        :type ApprovalStatus: int
        :param _ApprovalUser: Specifies the review user.
        :type ApprovalUser: str
        :param _ApprovalTime: Approval time.
        :type ApprovalTime: str
        :param _ApprovalNote: Approval notes
        :type ApprovalNote: str
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _ApplicationName: Application name
        :type ApplicationName: str
        :param _ApplicationLogo: Specifies the application icon.
        :type ApplicationLogo: str
        :param _APIType: API type. 1: system; 2: custom.
        :type APIType: int
        :param _APIDesc: API feature description.
        :type APIDesc: str
        """
        self._ApprovalNo = None
        self._APIId = None
        self._APIName = None
        self._APIMethod = None
        self._MNPId = None
        self._MNPName = None
        self._ApplyUser = None
        self._ApplyTime = None
        self._ApplyNote = None
        self._ApprovalStatus = None
        self._ApprovalUser = None
        self._ApprovalTime = None
        self._ApprovalNote = None
        self._ApplicationId = None
        self._ApplicationName = None
        self._ApplicationLogo = None
        self._APIType = None
        self._APIDesc = None

    @property
    def ApprovalNo(self):
        r"""Approval ID
        :rtype: str
        """
        return self._ApprovalNo

    @ApprovalNo.setter
    def ApprovalNo(self, ApprovalNo):
        self._ApprovalNo = ApprovalNo

    @property
    def APIId(self):
        r"""Sensitive API ID
        :rtype: str
        """
        return self._APIId

    @APIId.setter
    def APIId(self, APIId):
        self._APIId = APIId

    @property
    def APIName(self):
        r"""API name
        :rtype: str
        """
        return self._APIName

    @APIName.setter
    def APIName(self, APIName):
        self._APIName = APIName

    @property
    def APIMethod(self):
        r"""API request method
        :rtype: str
        """
        return self._APIMethod

    @APIMethod.setter
    def APIMethod(self, APIMethod):
        self._APIMethod = APIMethod

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def MNPName(self):
        r"""Mini program name
        :rtype: str
        """
        return self._MNPName

    @MNPName.setter
    def MNPName(self, MNPName):
        self._MNPName = MNPName

    @property
    def ApplyUser(self):
        r"""Applicant
        :rtype: str
        """
        return self._ApplyUser

    @ApplyUser.setter
    def ApplyUser(self, ApplyUser):
        self._ApplyUser = ApplyUser

    @property
    def ApplyTime(self):
        r"""Application time
        :rtype: str
        """
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def ApplyNote(self):
        r"""Application notes
        :rtype: str
        """
        return self._ApplyNote

    @ApplyNote.setter
    def ApplyNote(self, ApplyNote):
        self._ApplyNote = ApplyNote

    @property
    def ApprovalStatus(self):
        r"""Approval status. 1: Processing; 20: Rejected; 30: Approved
        :rtype: int
        """
        return self._ApprovalStatus

    @ApprovalStatus.setter
    def ApprovalStatus(self, ApprovalStatus):
        self._ApprovalStatus = ApprovalStatus

    @property
    def ApprovalUser(self):
        r"""Specifies the review user.
        :rtype: str
        """
        return self._ApprovalUser

    @ApprovalUser.setter
    def ApprovalUser(self, ApprovalUser):
        self._ApprovalUser = ApprovalUser

    @property
    def ApprovalTime(self):
        r"""Approval time.
        :rtype: str
        """
        return self._ApprovalTime

    @ApprovalTime.setter
    def ApprovalTime(self, ApprovalTime):
        self._ApprovalTime = ApprovalTime

    @property
    def ApprovalNote(self):
        r"""Approval notes
        :rtype: str
        """
        return self._ApprovalNote

    @ApprovalNote.setter
    def ApprovalNote(self, ApprovalNote):
        self._ApprovalNote = ApprovalNote

    @property
    def ApplicationId(self):
        r"""Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        r"""Application name
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def ApplicationLogo(self):
        r"""Specifies the application icon.
        :rtype: str
        """
        return self._ApplicationLogo

    @ApplicationLogo.setter
    def ApplicationLogo(self, ApplicationLogo):
        self._ApplicationLogo = ApplicationLogo

    @property
    def APIType(self):
        r"""API type. 1: system; 2: custom.
        :rtype: int
        """
        return self._APIType

    @APIType.setter
    def APIType(self, APIType):
        self._APIType = APIType

    @property
    def APIDesc(self):
        r"""API feature description.
        :rtype: str
        """
        return self._APIDesc

    @APIDesc.setter
    def APIDesc(self, APIDesc):
        self._APIDesc = APIDesc


    def _deserialize(self, params):
        self._ApprovalNo = params.get("ApprovalNo")
        self._APIId = params.get("APIId")
        self._APIName = params.get("APIName")
        self._APIMethod = params.get("APIMethod")
        self._MNPId = params.get("MNPId")
        self._MNPName = params.get("MNPName")
        self._ApplyUser = params.get("ApplyUser")
        self._ApplyTime = params.get("ApplyTime")
        self._ApplyNote = params.get("ApplyNote")
        self._ApprovalStatus = params.get("ApprovalStatus")
        self._ApprovalUser = params.get("ApprovalUser")
        self._ApprovalTime = params.get("ApprovalTime")
        self._ApprovalNote = params.get("ApprovalNote")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._ApplicationLogo = params.get("ApplicationLogo")
        self._APIType = params.get("APIType")
        self._APIDesc = params.get("APIDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPSensitiveAPIPermissionApprovalListRequest(AbstractModel):
    r"""DescribeMNPSensitiveAPIPermissionApprovalList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Number of results per page
        :type Limit: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _ApprovalStatusList: Approval status. 1: Processing; 20: Rejected; 30: Approved
        :type ApprovalStatusList: list of int
        :param _Keyword: Keywords for search (API name, API method or application name)
        :type Keyword: str
        """
        self._Offset = None
        self._Limit = None
        self._PlatformId = None
        self._ApprovalStatusList = None
        self._Keyword = None

    @property
    def Offset(self):
        r"""Page offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of results per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ApprovalStatusList(self):
        r"""Approval status. 1: Processing; 20: Rejected; 30: Approved
        :rtype: list of int
        """
        return self._ApprovalStatusList

    @ApprovalStatusList.setter
    def ApprovalStatusList(self, ApprovalStatusList):
        self._ApprovalStatusList = ApprovalStatusList

    @property
    def Keyword(self):
        r"""Keywords for search (API name, API method or application name)
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PlatformId = params.get("PlatformId")
        self._ApprovalStatusList = params.get("ApprovalStatusList")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPSensitiveAPIPermissionApprovalListResp(AbstractModel):
    r"""List of permission requests to allow a mini program to call sensitive APIs

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _DataList: List information
        :type DataList: list of DescribeMNPSensitiveAPIPermissionApprovalListData
        """
        self._TotalCount = None
        self._DataList = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataList(self):
        r"""List information
        :rtype: list of DescribeMNPSensitiveAPIPermissionApprovalListData
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = DescribeMNPSensitiveAPIPermissionApprovalListData()
                obj._deserialize(item)
                self._DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPSensitiveAPIPermissionApprovalListResponse(AbstractModel):
    r"""DescribeMNPSensitiveAPIPermissionApprovalList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSensitiveAPIPermissionApprovalListResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSensitiveAPIPermissionApprovalListResp`
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
        if params.get("Data") is not None:
            self._Data = DescribeMNPSensitiveAPIPermissionApprovalListResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMNPSensitiveAPIPermissionApprovalRequest(AbstractModel):
    r"""DescribeMNPSensitiveAPIPermissionApproval request structure.

    """

    def __init__(self):
        r"""
        :param _ApprovalNo: Approval request number
        :type ApprovalNo: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._ApprovalNo = None
        self._PlatformId = None

    @property
    def ApprovalNo(self):
        r"""Approval request number
        :rtype: str
        """
        return self._ApprovalNo

    @ApprovalNo.setter
    def ApprovalNo(self, ApprovalNo):
        self._ApprovalNo = ApprovalNo

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._ApprovalNo = params.get("ApprovalNo")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPSensitiveAPIPermissionApprovalResponse(AbstractModel):
    r"""DescribeMNPSensitiveAPIPermissionApproval response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSensitiveAPIPermissionApprovalData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSensitiveAPIPermissionApprovalData`
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
        if params.get("Data") is not None:
            self._Data = DescribeMNPSensitiveAPIPermissionApprovalData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMNPSensitiveAPIPermissionListData(AbstractModel):
    r"""List of sensitive APIs that can be called by a mini program

    """

    def __init__(self):
        r"""
        :param _APIId: API ID
        :type APIId: str
        :param _APIName: API name.
        :type APIName: str
        :param _APIMethod: API request method
        :type APIMethod: str
        :param _APIStatus: API status.
        :type APIStatus: int
        :param _APIApplyStatus: API application status.
        :type APIApplyStatus: int
        :param _RejectReason: Reason for rejection.
        :type RejectReason: str
        :param _ApprovalNo: Approval ID
        :type ApprovalNo: str
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _ApplicationIcon: Specifies the application icon.
        :type ApplicationIcon: str
        :param _ApplicationName: Application name
        :type ApplicationName: str
        :param _APIType: API type. 1: system; 2: custom.
        :type APIType: int
        :param _APIDesc: API feature description.
        :type APIDesc: str
        """
        self._APIId = None
        self._APIName = None
        self._APIMethod = None
        self._APIStatus = None
        self._APIApplyStatus = None
        self._RejectReason = None
        self._ApprovalNo = None
        self._ApplicationId = None
        self._ApplicationIcon = None
        self._ApplicationName = None
        self._APIType = None
        self._APIDesc = None

    @property
    def APIId(self):
        r"""API ID
        :rtype: str
        """
        return self._APIId

    @APIId.setter
    def APIId(self, APIId):
        self._APIId = APIId

    @property
    def APIName(self):
        r"""API name.
        :rtype: str
        """
        return self._APIName

    @APIName.setter
    def APIName(self, APIName):
        self._APIName = APIName

    @property
    def APIMethod(self):
        r"""API request method
        :rtype: str
        """
        return self._APIMethod

    @APIMethod.setter
    def APIMethod(self, APIMethod):
        self._APIMethod = APIMethod

    @property
    def APIStatus(self):
        r"""API status.
        :rtype: int
        """
        return self._APIStatus

    @APIStatus.setter
    def APIStatus(self, APIStatus):
        self._APIStatus = APIStatus

    @property
    def APIApplyStatus(self):
        r"""API application status.
        :rtype: int
        """
        return self._APIApplyStatus

    @APIApplyStatus.setter
    def APIApplyStatus(self, APIApplyStatus):
        self._APIApplyStatus = APIApplyStatus

    @property
    def RejectReason(self):
        r"""Reason for rejection.
        :rtype: str
        """
        return self._RejectReason

    @RejectReason.setter
    def RejectReason(self, RejectReason):
        self._RejectReason = RejectReason

    @property
    def ApprovalNo(self):
        r"""Approval ID
        :rtype: str
        """
        return self._ApprovalNo

    @ApprovalNo.setter
    def ApprovalNo(self, ApprovalNo):
        self._ApprovalNo = ApprovalNo

    @property
    def ApplicationId(self):
        r"""Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationIcon(self):
        r"""Specifies the application icon.
        :rtype: str
        """
        return self._ApplicationIcon

    @ApplicationIcon.setter
    def ApplicationIcon(self, ApplicationIcon):
        self._ApplicationIcon = ApplicationIcon

    @property
    def ApplicationName(self):
        r"""Application name
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def APIType(self):
        r"""API type. 1: system; 2: custom.
        :rtype: int
        """
        return self._APIType

    @APIType.setter
    def APIType(self, APIType):
        self._APIType = APIType

    @property
    def APIDesc(self):
        r"""API feature description.
        :rtype: str
        """
        return self._APIDesc

    @APIDesc.setter
    def APIDesc(self, APIDesc):
        self._APIDesc = APIDesc


    def _deserialize(self, params):
        self._APIId = params.get("APIId")
        self._APIName = params.get("APIName")
        self._APIMethod = params.get("APIMethod")
        self._APIStatus = params.get("APIStatus")
        self._APIApplyStatus = params.get("APIApplyStatus")
        self._RejectReason = params.get("RejectReason")
        self._ApprovalNo = params.get("ApprovalNo")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationIcon = params.get("ApplicationIcon")
        self._ApplicationName = params.get("ApplicationName")
        self._APIType = params.get("APIType")
        self._APIDesc = params.get("APIDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPSensitiveAPIPermissionListRequest(AbstractModel):
    r"""DescribeMNPSensitiveAPIPermissionList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Number of results per page
        :type Limit: int
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _Keyword: Keywords for search (API name)
        :type Keyword: str
        """
        self._Offset = None
        self._Limit = None
        self._MNPId = None
        self._PlatformId = None
        self._ApplicationId = None
        self._Keyword = None

    @property
    def Offset(self):
        r"""Page offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of results per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ApplicationId(self):
        r"""Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def Keyword(self):
        r"""Keywords for search (API name)
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._ApplicationId = params.get("ApplicationId")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPSensitiveAPIPermissionListResp(AbstractModel):
    r"""List of sensitive APIs that can be called by a mini program

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _DataList: List data
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataList: list of DescribeMNPSensitiveAPIPermissionListData
        """
        self._TotalCount = None
        self._DataList = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataList(self):
        r"""List data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DescribeMNPSensitiveAPIPermissionListData
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = DescribeMNPSensitiveAPIPermissionListData()
                obj._deserialize(item)
                self._DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPSensitiveAPIPermissionListResponse(AbstractModel):
    r"""DescribeMNPSensitiveAPIPermissionList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response parameters.
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSensitiveAPIPermissionListResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response parameters.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSensitiveAPIPermissionListResp`
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
        if params.get("Data") is not None:
            self._Data = DescribeMNPSensitiveAPIPermissionListResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMNPVersionRequest(AbstractModel):
    r"""DescribeMNPVersion request structure.

    """

    def __init__(self):
        r"""
        :param _BusinessId: ID of the task to create a mini program version
        :type BusinessId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._BusinessId = None
        self._PlatformId = None

    @property
    def BusinessId(self):
        r"""ID of the task to create a mini program version
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPVersionResp(AbstractModel):
    r"""Result of the task to create a mini program version

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _TaskId: Task ID
        :type TaskId: str
        :param _TaskStatus: 1: Pending; 20: Running; 30: Failed; 60: Succeeded
        :type TaskStatus: int
        :param _TaskMsg: Task status message
        :type TaskMsg: str
        :param _MNPVersionId: Mini program version ID (returned when compilation succeeds)
        :type MNPVersionId: int
        """
        self._MNPId = None
        self._TaskId = None
        self._TaskStatus = None
        self._TaskMsg = None
        self._MNPVersionId = None

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskStatus(self):
        r"""1: Pending; 20: Running; 30: Failed; 60: Succeeded
        :rtype: int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskMsg(self):
        r"""Task status message
        :rtype: str
        """
        return self._TaskMsg

    @TaskMsg.setter
    def TaskMsg(self, TaskMsg):
        self._TaskMsg = TaskMsg

    @property
    def MNPVersionId(self):
        r"""Mini program version ID (returned when compilation succeeds)
        :rtype: int
        """
        return self._MNPVersionId

    @MNPVersionId.setter
    def MNPVersionId(self, MNPVersionId):
        self._MNPVersionId = MNPVersionId


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._TaskId = params.get("TaskId")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskMsg = params.get("TaskMsg")
        self._MNPVersionId = params.get("MNPVersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMNPVersionResponse(AbstractModel):
    r"""DescribeMNPVersion response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPVersionResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPVersionResp`
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
        if params.get("Data") is not None:
            self._Data = DescribeMNPVersionResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMPAllStageVersionsResp(AbstractModel):
    r"""List of all developer versions of a mini program

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID.
        :type MNPId: str
        :param _MNPVersionId: Specifies the mini program version primary key id.
        :type MNPVersionId: int
        :param _MNPName: Mini program name
        :type MNPName: str
        :param _MNPIcon: Specifies the mini program avatar.
        :type MNPIcon: str
        :param _MNPType: Mini program type
        :type MNPType: str
        :param _MNPIntro: Mini program introduction
        :type MNPIntro: str
        :param _MNPDesc: Mini program description
        :type MNPDesc: str
        :param _CreateUser: Specifies the developer.
        :type CreateUser: str
        :param _CreateTime: Developer creation time.
        :type CreateTime: str
        :param _MNPVersion: Mini program version.
        :type MNPVersion: str
        :param _MNPVersionIntro: Describes version features.
        :type MNPVersionIntro: str
        :param _Phase: Development Platform Online.
        :type Phase: str
        :param _ApprovalStatus: 0 pending review; 1 under review; 2 review rejection; 3 pass review; 4 review cancellation.
        :type ApprovalStatus: int
        :param _ApprovalNo: Approval ticket ID
        :type ApprovalNo: str
        :param _ShowCase: Specifies whether it is a trial version.
Specifies the version type. valid values: 0 (non-preview version); 1 (trial version).
        :type ShowCase: int
        :param _RollbackVersion: Version number to roll back to.
        :type RollbackVersion: int
        :param _Status: Indicates the release status.
        :type Status: int
        :param _VersionCurrentStatus: Specifies the current main status of the version. valid values: "0" (pending review), "1" (under review), "2" (review rejection), "3" (pass review), "4" (review cancellation).
        :type VersionCurrentStatus: int
        """
        self._MNPId = None
        self._MNPVersionId = None
        self._MNPName = None
        self._MNPIcon = None
        self._MNPType = None
        self._MNPIntro = None
        self._MNPDesc = None
        self._CreateUser = None
        self._CreateTime = None
        self._MNPVersion = None
        self._MNPVersionIntro = None
        self._Phase = None
        self._ApprovalStatus = None
        self._ApprovalNo = None
        self._ShowCase = None
        self._RollbackVersion = None
        self._Status = None
        self._VersionCurrentStatus = None

    @property
    def MNPId(self):
        r"""Mini program ID.
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def MNPVersionId(self):
        r"""Specifies the mini program version primary key id.
        :rtype: int
        """
        return self._MNPVersionId

    @MNPVersionId.setter
    def MNPVersionId(self, MNPVersionId):
        self._MNPVersionId = MNPVersionId

    @property
    def MNPName(self):
        r"""Mini program name
        :rtype: str
        """
        return self._MNPName

    @MNPName.setter
    def MNPName(self, MNPName):
        self._MNPName = MNPName

    @property
    def MNPIcon(self):
        r"""Specifies the mini program avatar.
        :rtype: str
        """
        return self._MNPIcon

    @MNPIcon.setter
    def MNPIcon(self, MNPIcon):
        self._MNPIcon = MNPIcon

    @property
    def MNPType(self):
        r"""Mini program type
        :rtype: str
        """
        return self._MNPType

    @MNPType.setter
    def MNPType(self, MNPType):
        self._MNPType = MNPType

    @property
    def MNPIntro(self):
        r"""Mini program introduction
        :rtype: str
        """
        return self._MNPIntro

    @MNPIntro.setter
    def MNPIntro(self, MNPIntro):
        self._MNPIntro = MNPIntro

    @property
    def MNPDesc(self):
        r"""Mini program description
        :rtype: str
        """
        return self._MNPDesc

    @MNPDesc.setter
    def MNPDesc(self, MNPDesc):
        self._MNPDesc = MNPDesc

    @property
    def CreateUser(self):
        r"""Specifies the developer.
        :rtype: str
        """
        return self._CreateUser

    @CreateUser.setter
    def CreateUser(self, CreateUser):
        self._CreateUser = CreateUser

    @property
    def CreateTime(self):
        r"""Developer creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MNPVersion(self):
        r"""Mini program version.
        :rtype: str
        """
        return self._MNPVersion

    @MNPVersion.setter
    def MNPVersion(self, MNPVersion):
        self._MNPVersion = MNPVersion

    @property
    def MNPVersionIntro(self):
        r"""Describes version features.
        :rtype: str
        """
        return self._MNPVersionIntro

    @MNPVersionIntro.setter
    def MNPVersionIntro(self, MNPVersionIntro):
        self._MNPVersionIntro = MNPVersionIntro

    @property
    def Phase(self):
        r"""Development Platform Online.
        :rtype: str
        """
        return self._Phase

    @Phase.setter
    def Phase(self, Phase):
        self._Phase = Phase

    @property
    def ApprovalStatus(self):
        r"""0 pending review; 1 under review; 2 review rejection; 3 pass review; 4 review cancellation.
        :rtype: int
        """
        return self._ApprovalStatus

    @ApprovalStatus.setter
    def ApprovalStatus(self, ApprovalStatus):
        self._ApprovalStatus = ApprovalStatus

    @property
    def ApprovalNo(self):
        r"""Approval ticket ID
        :rtype: str
        """
        return self._ApprovalNo

    @ApprovalNo.setter
    def ApprovalNo(self, ApprovalNo):
        self._ApprovalNo = ApprovalNo

    @property
    def ShowCase(self):
        r"""Specifies whether it is a trial version.
Specifies the version type. valid values: 0 (non-preview version); 1 (trial version).
        :rtype: int
        """
        return self._ShowCase

    @ShowCase.setter
    def ShowCase(self, ShowCase):
        self._ShowCase = ShowCase

    @property
    def RollbackVersion(self):
        r"""Version number to roll back to.
        :rtype: int
        """
        return self._RollbackVersion

    @RollbackVersion.setter
    def RollbackVersion(self, RollbackVersion):
        self._RollbackVersion = RollbackVersion

    @property
    def Status(self):
        r"""Indicates the release status.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VersionCurrentStatus(self):
        r"""Specifies the current main status of the version. valid values: "0" (pending review), "1" (under review), "2" (review rejection), "3" (pass review), "4" (review cancellation).
        :rtype: int
        """
        return self._VersionCurrentStatus

    @VersionCurrentStatus.setter
    def VersionCurrentStatus(self, VersionCurrentStatus):
        self._VersionCurrentStatus = VersionCurrentStatus


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._MNPVersionId = params.get("MNPVersionId")
        self._MNPName = params.get("MNPName")
        self._MNPIcon = params.get("MNPIcon")
        self._MNPType = params.get("MNPType")
        self._MNPIntro = params.get("MNPIntro")
        self._MNPDesc = params.get("MNPDesc")
        self._CreateUser = params.get("CreateUser")
        self._CreateTime = params.get("CreateTime")
        self._MNPVersion = params.get("MNPVersion")
        self._MNPVersionIntro = params.get("MNPVersionIntro")
        self._Phase = params.get("Phase")
        self._ApprovalStatus = params.get("ApprovalStatus")
        self._ApprovalNo = params.get("ApprovalNo")
        self._ShowCase = params.get("ShowCase")
        self._RollbackVersion = params.get("RollbackVersion")
        self._Status = params.get("Status")
        self._VersionCurrentStatus = params.get("VersionCurrentStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePaymentDataDetailRequest(AbstractModel):
    r"""DescribePaymentDataDetail request structure.

    """

    def __init__(self):
        r"""
        :param _TimeBegin: Start time
        :type TimeBegin: int
        :param _MNPIds: Mini program appid
        :type MNPIds: list of str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _DataType: Type: 0 Non-production data, 1 Production data
        :type DataType: int
        :param _TimeEnd: End time
        :type TimeEnd: int
        :param _Platform: Operating system: 0 All, 2 Android, 3 iOS
        :type Platform: int
        """
        self._TimeBegin = None
        self._MNPIds = None
        self._PlatformId = None
        self._DataType = None
        self._TimeEnd = None
        self._Platform = None

    @property
    def TimeBegin(self):
        r"""Start time
        :rtype: int
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def MNPIds(self):
        r"""Mini program appid
        :rtype: list of str
        """
        return self._MNPIds

    @MNPIds.setter
    def MNPIds(self, MNPIds):
        self._MNPIds = MNPIds

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def DataType(self):
        r"""Type: 0 Non-production data, 1 Production data
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def TimeEnd(self):
        r"""End time
        :rtype: int
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def Platform(self):
        r"""Operating system: 0 All, 2 Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._TimeBegin = params.get("TimeBegin")
        self._MNPIds = params.get("MNPIds")
        self._PlatformId = params.get("PlatformId")
        self._DataType = params.get("DataType")
        self._TimeEnd = params.get("TimeEnd")
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePaymentDataDetailResponse(AbstractModel):
    r"""DescribePaymentDataDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of PaymentDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of PaymentDetail
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = PaymentDetail()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePaymentDataLineChartRequest(AbstractModel):
    r"""DescribePaymentDataLineChart request structure.

    """

    def __init__(self):
        r"""
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _ReportId: Fixed value: payment_data_analysis
        :type ReportId: str
        :param _IndexId: IndexId (optional):
order_user_num: Number of users placing orders
order_num: Total orders
total_amount: Total amount
order_unpaid_num: Total unpaid orders
unpaid_amount: Unpaid amount
order_paid_num: Total paid orders
paid_amount: Amount paid
order_refund_num: Total refunded orders
refund_amount: Total amount refunded
        :type IndexId: str
        :param _QueryData: Input parameter base64 string: {"Platform":0,"MnpIds":["mp9e7qluz4i3z3km"],"BeginDate":20251031,"EndDate":20251129,"DataType":"1","PaymentType":1}
        :type QueryData: str
        """
        self._PlatformId = None
        self._ReportId = None
        self._IndexId = None
        self._QueryData = None

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ReportId(self):
        r"""Fixed value: payment_data_analysis
        :rtype: str
        """
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def IndexId(self):
        r"""IndexId (optional):
order_user_num: Number of users placing orders
order_num: Total orders
total_amount: Total amount
order_unpaid_num: Total unpaid orders
unpaid_amount: Unpaid amount
order_paid_num: Total paid orders
paid_amount: Amount paid
order_refund_num: Total refunded orders
refund_amount: Total amount refunded
        :rtype: str
        """
        return self._IndexId

    @IndexId.setter
    def IndexId(self, IndexId):
        self._IndexId = IndexId

    @property
    def QueryData(self):
        r"""Input parameter base64 string: {"Platform":0,"MnpIds":["mp9e7qluz4i3z3km"],"BeginDate":20251031,"EndDate":20251129,"DataType":"1","PaymentType":1}
        :rtype: str
        """
        return self._QueryData

    @QueryData.setter
    def QueryData(self, QueryData):
        self._QueryData = QueryData


    def _deserialize(self, params):
        self._PlatformId = params.get("PlatformId")
        self._ReportId = params.get("ReportId")
        self._IndexId = params.get("IndexId")
        self._QueryData = params.get("QueryData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePaymentDataLineChartResponse(AbstractModel):
    r"""DescribePaymentDataLineChart response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of ReportDataResult
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ReportDataResult
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ReportDataResult()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePaymentDataOverviewRequest(AbstractModel):
    r"""DescribePaymentDataOverview request structure.

    """

    def __init__(self):
        r"""
        :param _TimeBegin: Start time
        :type TimeBegin: int
        :param _MNPIds: Mini program appid
        :type MNPIds: list of str
        :param _PlatformId: Tenant ID
        :type PlatformId: str
        :param _DataType: Type: 0 Non-production data, 1 Production data
        :type DataType: int
        :param _TimeEnd: End time
        :type TimeEnd: int
        :param _Platform: Operating system: 0 All, 2 Android, 3 iOS
        :type Platform: int
        """
        self._TimeBegin = None
        self._MNPIds = None
        self._PlatformId = None
        self._DataType = None
        self._TimeEnd = None
        self._Platform = None

    @property
    def TimeBegin(self):
        r"""Start time
        :rtype: int
        """
        return self._TimeBegin

    @TimeBegin.setter
    def TimeBegin(self, TimeBegin):
        self._TimeBegin = TimeBegin

    @property
    def MNPIds(self):
        r"""Mini program appid
        :rtype: list of str
        """
        return self._MNPIds

    @MNPIds.setter
    def MNPIds(self, MNPIds):
        self._MNPIds = MNPIds

    @property
    def PlatformId(self):
        r"""Tenant ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def DataType(self):
        r"""Type: 0 Non-production data, 1 Production data
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def TimeEnd(self):
        r"""End time
        :rtype: int
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def Platform(self):
        r"""Operating system: 0 All, 2 Android, 3 iOS
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._TimeBegin = params.get("TimeBegin")
        self._MNPIds = params.get("MNPIds")
        self._PlatformId = params.get("PlatformId")
        self._DataType = params.get("DataType")
        self._TimeEnd = params.get("TimeEnd")
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePaymentDataOverviewResponse(AbstractModel):
    r"""DescribePaymentDataOverview response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.MNPPaymentOverview`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.MNPPaymentOverview`
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
        if params.get("Data") is not None:
            self._Data = MNPPaymentOverview()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRevertOnlineVersionPageResp(AbstractModel):
    r"""Response of querying the rollback version list

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _DataList: List information
        :type DataList: list of QueryOnlineVersionResp
        """
        self._TotalCount = None
        self._DataList = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataList(self):
        r"""List information
        :rtype: list of QueryOnlineVersionResp
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = QueryOnlineVersionResp()
                obj._deserialize(item)
                self._DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoleListData(AbstractModel):
    r"""Role management list

    """

    def __init__(self):
        r"""
        :param _RoleId: Role ID
        :type RoleId: int
        :param _RoleName: Role name.
        :type RoleName: str
        :param _TeamName: Team name
        :type TeamName: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _RoleType: Role type 1-preset role 2-custom role.
        :type RoleType: int
        """
        self._RoleId = None
        self._RoleName = None
        self._TeamName = None
        self._CreateTime = None
        self._RoleType = None

    @property
    def RoleId(self):
        r"""Role ID
        :rtype: int
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        r"""Role name.
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def TeamName(self):
        r"""Team name
        :rtype: str
        """
        return self._TeamName

    @TeamName.setter
    def TeamName(self, TeamName):
        self._TeamName = TeamName

    @property
    def CreateTime(self):
        r"""Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RoleType(self):
        r"""Role type 1-preset role 2-custom role.
        :rtype: int
        """
        return self._RoleType

    @RoleType.setter
    def RoleType(self, RoleType):
        self._RoleType = RoleType


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        self._TeamName = params.get("TeamName")
        self._CreateTime = params.get("CreateTime")
        self._RoleType = params.get("RoleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoleListRequest(AbstractModel):
    r"""DescribeRoleList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Number of results per page
        :type Limit: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _Keyword: Keywords for search (role name)
        :type Keyword: str
        :param _TeamId: Team ID
        :type TeamId: str
        """
        self._Offset = None
        self._Limit = None
        self._PlatformId = None
        self._Keyword = None
        self._TeamId = None

    @property
    def Offset(self):
        r"""Page offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of results per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def Keyword(self):
        r"""Keywords for search (role name)
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PlatformId = params.get("PlatformId")
        self._Keyword = params.get("Keyword")
        self._TeamId = params.get("TeamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoleListResp(AbstractModel):
    r"""Role management list

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _DataList: List data
        :type DataList: list of DescribeRoleListData
        """
        self._TotalCount = None
        self._DataList = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataList(self):
        r"""List data
        :rtype: list of DescribeRoleListData
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = DescribeRoleListData()
                obj._deserialize(item)
                self._DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoleListResponse(AbstractModel):
    r"""DescribeRoleList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeRoleListResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeRoleListResp`
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
        if params.get("Data") is not None:
            self._Data = DescribeRoleListResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTeamDetailResp(AbstractModel):
    r"""Team details

    """

    def __init__(self):
        r"""
        :param _TeamName: Team name
        :type TeamName: str
        :param _TeamRoleType: Team role type 1-mini program team 2-application team
        :type TeamRoleType: int
        :param _AdminUserAccount: Administrator account
        :type AdminUserAccount: str
        :param _CreateUser: Creator
        :type CreateUser: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _MemberCount: Number of team members
        :type MemberCount: int
        :param _BindMiniTeamCount: Number of bound mini program teams
        :type BindMiniTeamCount: int
        :param _BindTeamName: Name of the bound team
        :type BindTeamName: str
        :param _RegisterLink: Team registration link
        :type RegisterLink: str
        :param _ApplicationName: Application name. It Is required when querying details of a mini program team.
        :type ApplicationName: str
        :param _ExpireTime: Team expiration time. 0 means never expire.
        :type ExpireTime: int
        :param _Status: Team status. valid values: 1: normal; 2: disabled; 3: expired.
        :type Status: int
        """
        self._TeamName = None
        self._TeamRoleType = None
        self._AdminUserAccount = None
        self._CreateUser = None
        self._CreateTime = None
        self._MemberCount = None
        self._BindMiniTeamCount = None
        self._BindTeamName = None
        self._RegisterLink = None
        self._ApplicationName = None
        self._ExpireTime = None
        self._Status = None

    @property
    def TeamName(self):
        r"""Team name
        :rtype: str
        """
        return self._TeamName

    @TeamName.setter
    def TeamName(self, TeamName):
        self._TeamName = TeamName

    @property
    def TeamRoleType(self):
        r"""Team role type 1-mini program team 2-application team
        :rtype: int
        """
        return self._TeamRoleType

    @TeamRoleType.setter
    def TeamRoleType(self, TeamRoleType):
        self._TeamRoleType = TeamRoleType

    @property
    def AdminUserAccount(self):
        r"""Administrator account
        :rtype: str
        """
        return self._AdminUserAccount

    @AdminUserAccount.setter
    def AdminUserAccount(self, AdminUserAccount):
        self._AdminUserAccount = AdminUserAccount

    @property
    def CreateUser(self):
        r"""Creator
        :rtype: str
        """
        return self._CreateUser

    @CreateUser.setter
    def CreateUser(self, CreateUser):
        self._CreateUser = CreateUser

    @property
    def CreateTime(self):
        r"""Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MemberCount(self):
        r"""Number of team members
        :rtype: int
        """
        return self._MemberCount

    @MemberCount.setter
    def MemberCount(self, MemberCount):
        self._MemberCount = MemberCount

    @property
    def BindMiniTeamCount(self):
        r"""Number of bound mini program teams
        :rtype: int
        """
        return self._BindMiniTeamCount

    @BindMiniTeamCount.setter
    def BindMiniTeamCount(self, BindMiniTeamCount):
        self._BindMiniTeamCount = BindMiniTeamCount

    @property
    def BindTeamName(self):
        r"""Name of the bound team
        :rtype: str
        """
        return self._BindTeamName

    @BindTeamName.setter
    def BindTeamName(self, BindTeamName):
        self._BindTeamName = BindTeamName

    @property
    def RegisterLink(self):
        r"""Team registration link
        :rtype: str
        """
        return self._RegisterLink

    @RegisterLink.setter
    def RegisterLink(self, RegisterLink):
        self._RegisterLink = RegisterLink

    @property
    def ApplicationName(self):
        r"""Application name. It Is required when querying details of a mini program team.
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def ExpireTime(self):
        r"""Team expiration time. 0 means never expire.
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Status(self):
        r"""Team status. valid values: 1: normal; 2: disabled; 3: expired.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._TeamName = params.get("TeamName")
        self._TeamRoleType = params.get("TeamRoleType")
        self._AdminUserAccount = params.get("AdminUserAccount")
        self._CreateUser = params.get("CreateUser")
        self._CreateTime = params.get("CreateTime")
        self._MemberCount = params.get("MemberCount")
        self._BindMiniTeamCount = params.get("BindMiniTeamCount")
        self._BindTeamName = params.get("BindTeamName")
        self._RegisterLink = params.get("RegisterLink")
        self._ApplicationName = params.get("ApplicationName")
        self._ExpireTime = params.get("ExpireTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTeamListInfoResp(AbstractModel):
    r"""Team list information

    """

    def __init__(self):
        r"""
        :param _TeamId: Team ID
        :type TeamId: str
        :param _TeamName: Team name
        :type TeamName: str
        :param _AdminUserId: Administrator user ID
        :type AdminUserId: str
        :param _AdminUserAccount: Administrator account
        :type AdminUserAccount: str
        :param _AdminUserName: Administrator username
        :type AdminUserName: str
        :param _MemberCount: Number of team members
        :type MemberCount: int
        :param _RegisterLink: Team registration link
        :type RegisterLink: str
        :param _TeamRoleTypeList: Team permission type
        :type TeamRoleTypeList: list of int
        :param _RelatedTeamId: Associated team ID
        :type RelatedTeamId: int
        :param _ExpireTime: Team expiration time. 0 means never expire.
        :type ExpireTime: int
        :param _Status: Team status. valid values: 1: normal; 2: disabled; 3: expired.
        :type Status: int
        """
        self._TeamId = None
        self._TeamName = None
        self._AdminUserId = None
        self._AdminUserAccount = None
        self._AdminUserName = None
        self._MemberCount = None
        self._RegisterLink = None
        self._TeamRoleTypeList = None
        self._RelatedTeamId = None
        self._ExpireTime = None
        self._Status = None

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def TeamName(self):
        r"""Team name
        :rtype: str
        """
        return self._TeamName

    @TeamName.setter
    def TeamName(self, TeamName):
        self._TeamName = TeamName

    @property
    def AdminUserId(self):
        r"""Administrator user ID
        :rtype: str
        """
        return self._AdminUserId

    @AdminUserId.setter
    def AdminUserId(self, AdminUserId):
        self._AdminUserId = AdminUserId

    @property
    def AdminUserAccount(self):
        r"""Administrator account
        :rtype: str
        """
        return self._AdminUserAccount

    @AdminUserAccount.setter
    def AdminUserAccount(self, AdminUserAccount):
        self._AdminUserAccount = AdminUserAccount

    @property
    def AdminUserName(self):
        r"""Administrator username
        :rtype: str
        """
        return self._AdminUserName

    @AdminUserName.setter
    def AdminUserName(self, AdminUserName):
        self._AdminUserName = AdminUserName

    @property
    def MemberCount(self):
        r"""Number of team members
        :rtype: int
        """
        return self._MemberCount

    @MemberCount.setter
    def MemberCount(self, MemberCount):
        self._MemberCount = MemberCount

    @property
    def RegisterLink(self):
        r"""Team registration link
        :rtype: str
        """
        return self._RegisterLink

    @RegisterLink.setter
    def RegisterLink(self, RegisterLink):
        self._RegisterLink = RegisterLink

    @property
    def TeamRoleTypeList(self):
        r"""Team permission type
        :rtype: list of int
        """
        return self._TeamRoleTypeList

    @TeamRoleTypeList.setter
    def TeamRoleTypeList(self, TeamRoleTypeList):
        self._TeamRoleTypeList = TeamRoleTypeList

    @property
    def RelatedTeamId(self):
        r"""Associated team ID
        :rtype: int
        """
        return self._RelatedTeamId

    @RelatedTeamId.setter
    def RelatedTeamId(self, RelatedTeamId):
        self._RelatedTeamId = RelatedTeamId

    @property
    def ExpireTime(self):
        r"""Team expiration time. 0 means never expire.
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Status(self):
        r"""Team status. valid values: 1: normal; 2: disabled; 3: expired.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._TeamName = params.get("TeamName")
        self._AdminUserId = params.get("AdminUserId")
        self._AdminUserAccount = params.get("AdminUserAccount")
        self._AdminUserName = params.get("AdminUserName")
        self._MemberCount = params.get("MemberCount")
        self._RegisterLink = params.get("RegisterLink")
        self._TeamRoleTypeList = params.get("TeamRoleTypeList")
        self._RelatedTeamId = params.get("RelatedTeamId")
        self._ExpireTime = params.get("ExpireTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTeamListRequest(AbstractModel):
    r"""DescribeTeamList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination offset
        :type Offset: int
        :param _Limit: Page size
        :type Limit: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _Keyword: Team name to be queried
        :type Keyword: str
        """
        self._Offset = None
        self._Limit = None
        self._PlatformId = None
        self._Keyword = None

    @property
    def Offset(self):
        r"""Pagination offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Page size
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def Keyword(self):
        r"""Team name to be queried
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PlatformId = params.get("PlatformId")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTeamListResponse(AbstractModel):
    r"""DescribeTeamList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeTeamPageResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeTeamPageResp`
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
        if params.get("Data") is not None:
            self._Data = DescribeTeamPageResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTeamMemberInfoResp(AbstractModel):
    r"""Team member information

    """

    def __init__(self):
        r"""
        :param _UserId: User ID
        :type UserId: str
        :param _UserAccount: User account
        :type UserAccount: str
        :param _UserName: User name
        :type UserName: str
        :param _TeamId: Team ID
        :type TeamId: str
        :param _TeamName: Team name
        :type TeamName: str
        :param _TeamRoleName: Specifies the team role name.
        :type TeamRoleName: str
        :param _TeamRoleId: Specifies the team role ID.
        :type TeamRoleId: int
        :param _CanEdit: Whether it is editable
        :type CanEdit: bool
        """
        self._UserId = None
        self._UserAccount = None
        self._UserName = None
        self._TeamId = None
        self._TeamName = None
        self._TeamRoleName = None
        self._TeamRoleId = None
        self._CanEdit = None

    @property
    def UserId(self):
        r"""User ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserAccount(self):
        r"""User account
        :rtype: str
        """
        return self._UserAccount

    @UserAccount.setter
    def UserAccount(self, UserAccount):
        self._UserAccount = UserAccount

    @property
    def UserName(self):
        r"""User name
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def TeamName(self):
        r"""Team name
        :rtype: str
        """
        return self._TeamName

    @TeamName.setter
    def TeamName(self, TeamName):
        self._TeamName = TeamName

    @property
    def TeamRoleName(self):
        r"""Specifies the team role name.
        :rtype: str
        """
        return self._TeamRoleName

    @TeamRoleName.setter
    def TeamRoleName(self, TeamRoleName):
        self._TeamRoleName = TeamRoleName

    @property
    def TeamRoleId(self):
        r"""Specifies the team role ID.
        :rtype: int
        """
        return self._TeamRoleId

    @TeamRoleId.setter
    def TeamRoleId(self, TeamRoleId):
        self._TeamRoleId = TeamRoleId

    @property
    def CanEdit(self):
        r"""Whether it is editable
        :rtype: bool
        """
        return self._CanEdit

    @CanEdit.setter
    def CanEdit(self, CanEdit):
        self._CanEdit = CanEdit


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserAccount = params.get("UserAccount")
        self._UserName = params.get("UserName")
        self._TeamId = params.get("TeamId")
        self._TeamName = params.get("TeamName")
        self._TeamRoleName = params.get("TeamRoleName")
        self._TeamRoleId = params.get("TeamRoleId")
        self._CanEdit = params.get("CanEdit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTeamMemberListPageResp(AbstractModel):
    r"""List of members

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _DataList: List information
        :type DataList: list of DescribeTeamMemberInfoResp
        """
        self._TotalCount = None
        self._DataList = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataList(self):
        r"""List information
        :rtype: list of DescribeTeamMemberInfoResp
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = DescribeTeamMemberInfoResp()
                obj._deserialize(item)
                self._DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTeamMemberListRequest(AbstractModel):
    r"""DescribeTeamMemberList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Number of results per page
        :type Limit: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _TeamId: Team ID
        :type TeamId: str
        :param _Keyword: Keywords for search (user name)
        :type Keyword: str
        :param _RoleIds: Role ID
        :type RoleIds: list of int
        """
        self._Offset = None
        self._Limit = None
        self._PlatformId = None
        self._TeamId = None
        self._Keyword = None
        self._RoleIds = None

    @property
    def Offset(self):
        r"""Page offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of results per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def Keyword(self):
        r"""Keywords for search (user name)
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def RoleIds(self):
        r"""Role ID
        :rtype: list of int
        """
        return self._RoleIds

    @RoleIds.setter
    def RoleIds(self, RoleIds):
        self._RoleIds = RoleIds


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PlatformId = params.get("PlatformId")
        self._TeamId = params.get("TeamId")
        self._Keyword = params.get("Keyword")
        self._RoleIds = params.get("RoleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTeamMemberListResponse(AbstractModel):
    r"""DescribeTeamMemberList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeTeamMemberListPageResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeTeamMemberListPageResp`
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
        if params.get("Data") is not None:
            self._Data = DescribeTeamMemberListPageResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTeamPageResp(AbstractModel):
    r"""Team list

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total count
        :type TotalCount: int
        :param _DataList: List information
        :type DataList: list of DescribeTeamListInfoResp
        """
        self._TotalCount = None
        self._DataList = None

    @property
    def TotalCount(self):
        r"""Total count
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataList(self):
        r"""List information
        :rtype: list of DescribeTeamListInfoResp
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = DescribeTeamListInfoResp()
                obj._deserialize(item)
                self._DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTeamRequest(AbstractModel):
    r"""DescribeTeam request structure.

    """

    def __init__(self):
        r"""
        :param _TeamId: Team ID
        :type TeamId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._TeamId = None
        self._PlatformId = None

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTeamResponse(AbstractModel):
    r"""DescribeTeam response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeTeamDetailResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeTeamDetailResp`
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
        if params.get("Data") is not None:
            self._Data = DescribeTeamDetailResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTempSecret4UploadFile2CosRequest(AbstractModel):
    r"""DescribeTempSecret4UploadFile2Cos request structure.

    """

    def __init__(self):
        r"""
        :param _BusinessName: Service name
        :type BusinessName: str
        :param _Suffix: File suffix
        :type Suffix: str
        """
        self._BusinessName = None
        self._Suffix = None

    @property
    def BusinessName(self):
        r"""Service name
        :rtype: str
        """
        return self._BusinessName

    @BusinessName.setter
    def BusinessName(self, BusinessName):
        self._BusinessName = BusinessName

    @property
    def Suffix(self):
        r"""File suffix
        :rtype: str
        """
        return self._Suffix

    @Suffix.setter
    def Suffix(self, Suffix):
        self._Suffix = Suffix


    def _deserialize(self, params):
        self._BusinessName = params.get("BusinessName")
        self._Suffix = params.get("Suffix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTempSecret4UploadFile2CosResponse(AbstractModel):
    r"""DescribeTempSecret4UploadFile2Cos response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.UploadFileTempSecret`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.UploadFileTempSecret`
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
        if params.get("Data") is not None:
            self._Data = UploadFileTempSecret()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeUserDetailResp(AbstractModel):
    r"""User details

    """

    def __init__(self):
        r"""
        :param _UserId: User iD.
        :type UserId: str
        :param _UserAccount: User account
        :type UserAccount: str
        :param _AccountType: User account
1 - super admin 2 - platform admin 3 - ordinary member. not passing indicates all.
        :type AccountType: int
        :param _UserName: User name
        :type UserName: str
        """
        self._UserId = None
        self._UserAccount = None
        self._AccountType = None
        self._UserName = None

    @property
    def UserId(self):
        r"""User iD.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserAccount(self):
        r"""User account
        :rtype: str
        """
        return self._UserAccount

    @UserAccount.setter
    def UserAccount(self, UserAccount):
        self._UserAccount = UserAccount

    @property
    def AccountType(self):
        r"""User account
1 - super admin 2 - platform admin 3 - ordinary member. not passing indicates all.
        :rtype: int
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def UserName(self):
        r"""User name
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserAccount = params.get("UserAccount")
        self._AccountType = params.get("AccountType")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserListData(AbstractModel):
    r"""User list data

    """

    def __init__(self):
        r"""
        :param _UserId: User ID
        :type UserId: str
        :param _UserAccount: User account
        :type UserAccount: str
        :param _AccountType: Account type. 1: super administrator; 2: platform administrator; 3: ordinary member.
        :type AccountType: int
        :param _UserName: User name
        :type UserName: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _Status: Status. 1: normal; 2: disabled.
        :type Status: int
        :param _TeamName: Team name
        :type TeamName: str
        """
        self._UserId = None
        self._UserAccount = None
        self._AccountType = None
        self._UserName = None
        self._CreateTime = None
        self._Status = None
        self._TeamName = None

    @property
    def UserId(self):
        r"""User ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserAccount(self):
        r"""User account
        :rtype: str
        """
        return self._UserAccount

    @UserAccount.setter
    def UserAccount(self, UserAccount):
        self._UserAccount = UserAccount

    @property
    def AccountType(self):
        r"""Account type. 1: super administrator; 2: platform administrator; 3: ordinary member.
        :rtype: int
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def UserName(self):
        r"""User name
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def CreateTime(self):
        r"""Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        r"""Status. 1: normal; 2: disabled.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TeamName(self):
        r"""Team name
        :rtype: str
        """
        return self._TeamName

    @TeamName.setter
    def TeamName(self, TeamName):
        self._TeamName = TeamName


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserAccount = params.get("UserAccount")
        self._AccountType = params.get("AccountType")
        self._UserName = params.get("UserName")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        self._TeamName = params.get("TeamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserListRequest(AbstractModel):
    r"""DescribeUserList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Number of results per page
        :type Limit: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _Keyword: Keywords for search (username or account)
        :type Keyword: str
        :param _AccountType: User account 1 - Super admin 2 - Platform admin 3 - Member
        :type AccountType: int
        :param _TeamId: Team ID
        :type TeamId: str
        """
        self._Offset = None
        self._Limit = None
        self._PlatformId = None
        self._Keyword = None
        self._AccountType = None
        self._TeamId = None

    @property
    def Offset(self):
        r"""Page offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of results per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def Keyword(self):
        r"""Keywords for search (username or account)
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def AccountType(self):
        r"""User account 1 - Super admin 2 - Platform admin 3 - Member
        :rtype: int
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PlatformId = params.get("PlatformId")
        self._Keyword = params.get("Keyword")
        self._AccountType = params.get("AccountType")
        self._TeamId = params.get("TeamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserListResp(AbstractModel):
    r"""User management list

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _DataList: List data
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataList: list of DescribeUserListData
        """
        self._TotalCount = None
        self._DataList = None

    @property
    def TotalCount(self):
        r"""Total number of entries
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataList(self):
        r"""List data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DescribeUserListData
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = DescribeUserListData()
                obj._deserialize(item)
                self._DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserListResponse(AbstractModel):
    r"""DescribeUserList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeUserListResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeUserListResp`
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
        if params.get("Data") is not None:
            self._Data = DescribeUserListResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeUserRequest(AbstractModel):
    r"""DescribeUser request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID
        :type UserId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._UserId = None
        self._PlatformId = None

    @property
    def UserId(self):
        r"""User ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserResponse(AbstractModel):
    r"""DescribeUser response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.DescribeUserDetailResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeUserDetailResp`
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
        if params.get("Data") is not None:
            self._Data = DescribeUserDetailResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DisableApplicationSensitiveAPIRequest(AbstractModel):
    r"""DisableApplicationSensitiveAPI request structure.

    """

    def __init__(self):
        r"""
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _APIId: API ID
        :type APIId: str
        """
        self._PlatformId = None
        self._APIId = None

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def APIId(self):
        r"""API ID
        :rtype: str
        """
        return self._APIId

    @APIId.setter
    def APIId(self, APIId):
        self._APIId = APIId


    def _deserialize(self, params):
        self._PlatformId = params.get("PlatformId")
        self._APIId = params.get("APIId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableApplicationSensitiveAPIResponse(AbstractModel):
    r"""DisableApplicationSensitiveAPI response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DownloadApplicationConfigResp(AbstractModel):
    r"""Application configuration info

    """

    def __init__(self):
        r"""
        :param _File: Configuration information in Base64 format
Note: This field may return null, indicating that no valid values can be obtained.
        :type File: str
        """
        self._File = None

    @property
    def File(self):
        r"""Configuration information in Base64 format
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._File

    @File.setter
    def File(self, File):
        self._File = File


    def _deserialize(self, params):
        self._File = params.get("File")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApplicationSensitiveAPIRequest(AbstractModel):
    r"""EnableApplicationSensitiveAPI request structure.

    """

    def __init__(self):
        r"""
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _APIId: API ID
        :type APIId: str
        """
        self._PlatformId = None
        self._APIId = None

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def APIId(self):
        r"""API ID
        :rtype: str
        """
        return self._APIId

    @APIId.setter
    def APIId(self, APIId):
        self._APIId = APIId


    def _deserialize(self, params):
        self._PlatformId = params.get("PlatformId")
        self._APIId = params.get("APIId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApplicationSensitiveAPIResponse(AbstractModel):
    r"""EnableApplicationSensitiveAPI response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GlobalDomainDeleteResp(AbstractModel):
    r"""Response of deleting a global domain name

    """

    def __init__(self):
        r"""
        :param _Result: Result.
        :type Result: bool
        """
        self._Result = None

    @property
    def Result(self):
        r"""Result.
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GlobalDomainModifyRespResp(AbstractModel):
    r"""Response of global domain name modification

    """

    def __init__(self):
        r"""
        :param _Result: 0: success; 1: allowed domains exist; 2: blocked domains exist.
        :type Result: int
        """
        self._Result = None

    @property
    def Result(self):
        r"""0: success; 1: allowed domains exist; 2: blocked domains exist.
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MAUChartData(AbstractModel):
    r"""MAU line chart data

    """

    def __init__(self):
        r"""
        :param _DataTime: Year and month: 2024-12
        :type DataTime: int
        :param _MAUCount: Value
        :type MAUCount: int
        :param _UpdateTime: Data update time, only available when MAUCount is greater than 0.
        :type UpdateTime: int
        """
        self._DataTime = None
        self._MAUCount = None
        self._UpdateTime = None

    @property
    def DataTime(self):
        r"""Year and month: 2024-12
        :rtype: int
        """
        return self._DataTime

    @DataTime.setter
    def DataTime(self, DataTime):
        self._DataTime = DataTime

    @property
    def MAUCount(self):
        r"""Value
        :rtype: int
        """
        return self._MAUCount

    @MAUCount.setter
    def MAUCount(self, MAUCount):
        self._MAUCount = MAUCount

    @property
    def UpdateTime(self):
        r"""Data update time, only available when MAUCount is greater than 0.
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._DataTime = params.get("DataTime")
        self._MAUCount = params.get("MAUCount")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MAUDetail(AbstractModel):
    r"""Mini program MAU details

    """

    def __init__(self):
        r"""
        :param _MNPName: Mini program name
        :type MNPName: str
        :param _DataList: MAU details
        :type DataList: list of MAULineChartData
        """
        self._MNPName = None
        self._DataList = None

    @property
    def MNPName(self):
        r"""Mini program name
        :rtype: str
        """
        return self._MNPName

    @MNPName.setter
    def MNPName(self, MNPName):
        self._MNPName = MNPName

    @property
    def DataList(self):
        r"""MAU details
        :rtype: list of MAULineChartData
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList


    def _deserialize(self, params):
        self._MNPName = params.get("MNPName")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = MAULineChartData()
                obj._deserialize(item)
                self._DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MAUDetailData(AbstractModel):
    r"""MAU detailed data

    """

    def __init__(self):
        r"""
        :param _DataTime: Date
        :type DataTime: str
        :param _MNPName: Mini program name
        :type MNPName: str
        :param _MNPType: Mini program type
        :type MNPType: str
        :param _EstimatedEarnings: Estimated revenue
        :type EstimatedEarnings: str
        :param _RequestsNumber: Requests
        :type RequestsNumber: int
        :param _Impressions: Impressions
        :type Impressions: int
        :param _ECPM: Effective Cost Per Mille
        :type ECPM: str
        :param _ClicksNumber: Taps
        :type ClicksNumber: int
        """
        self._DataTime = None
        self._MNPName = None
        self._MNPType = None
        self._EstimatedEarnings = None
        self._RequestsNumber = None
        self._Impressions = None
        self._ECPM = None
        self._ClicksNumber = None

    @property
    def DataTime(self):
        r"""Date
        :rtype: str
        """
        return self._DataTime

    @DataTime.setter
    def DataTime(self, DataTime):
        self._DataTime = DataTime

    @property
    def MNPName(self):
        r"""Mini program name
        :rtype: str
        """
        return self._MNPName

    @MNPName.setter
    def MNPName(self, MNPName):
        self._MNPName = MNPName

    @property
    def MNPType(self):
        r"""Mini program type
        :rtype: str
        """
        return self._MNPType

    @MNPType.setter
    def MNPType(self, MNPType):
        self._MNPType = MNPType

    @property
    def EstimatedEarnings(self):
        r"""Estimated revenue
        :rtype: str
        """
        return self._EstimatedEarnings

    @EstimatedEarnings.setter
    def EstimatedEarnings(self, EstimatedEarnings):
        self._EstimatedEarnings = EstimatedEarnings

    @property
    def RequestsNumber(self):
        r"""Requests
        :rtype: int
        """
        return self._RequestsNumber

    @RequestsNumber.setter
    def RequestsNumber(self, RequestsNumber):
        self._RequestsNumber = RequestsNumber

    @property
    def Impressions(self):
        r"""Impressions
        :rtype: int
        """
        return self._Impressions

    @Impressions.setter
    def Impressions(self, Impressions):
        self._Impressions = Impressions

    @property
    def ECPM(self):
        r"""Effective Cost Per Mille
        :rtype: str
        """
        return self._ECPM

    @ECPM.setter
    def ECPM(self, ECPM):
        self._ECPM = ECPM

    @property
    def ClicksNumber(self):
        r"""Taps
        :rtype: int
        """
        return self._ClicksNumber

    @ClicksNumber.setter
    def ClicksNumber(self, ClicksNumber):
        self._ClicksNumber = ClicksNumber


    def _deserialize(self, params):
        self._DataTime = params.get("DataTime")
        self._MNPName = params.get("MNPName")
        self._MNPType = params.get("MNPType")
        self._EstimatedEarnings = params.get("EstimatedEarnings")
        self._RequestsNumber = params.get("RequestsNumber")
        self._Impressions = params.get("Impressions")
        self._ECPM = params.get("ECPM")
        self._ClicksNumber = params.get("ClicksNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MAUIndicatorCard(AbstractModel):
    r"""MAU metric comparison response data

    """

    def __init__(self):
        r"""
        :param _ComparisonRatio: Growth rate (targetData - sourceData) / sourceData, returns 0 when SourceMAUNum is 0
        :type ComparisonRatio: str
        :param _ComparisonResult: 1 Increase
2 Decrease
Returns 0 when SourceMAUNum is 0
        :type ComparisonResult: int
        :param _SourceMAUNum: Last month's MAU data
        :type SourceMAUNum: int
        :param _TargetMAUNum: This month's MAU data
        :type TargetMAUNum: int
        :param _FlushTime: Data timestamp
        :type FlushTime: int
        """
        self._ComparisonRatio = None
        self._ComparisonResult = None
        self._SourceMAUNum = None
        self._TargetMAUNum = None
        self._FlushTime = None

    @property
    def ComparisonRatio(self):
        r"""Growth rate (targetData - sourceData) / sourceData, returns 0 when SourceMAUNum is 0
        :rtype: str
        """
        return self._ComparisonRatio

    @ComparisonRatio.setter
    def ComparisonRatio(self, ComparisonRatio):
        self._ComparisonRatio = ComparisonRatio

    @property
    def ComparisonResult(self):
        r"""1 Increase
2 Decrease
Returns 0 when SourceMAUNum is 0
        :rtype: int
        """
        return self._ComparisonResult

    @ComparisonResult.setter
    def ComparisonResult(self, ComparisonResult):
        self._ComparisonResult = ComparisonResult

    @property
    def SourceMAUNum(self):
        r"""Last month's MAU data
        :rtype: int
        """
        return self._SourceMAUNum

    @SourceMAUNum.setter
    def SourceMAUNum(self, SourceMAUNum):
        self._SourceMAUNum = SourceMAUNum

    @property
    def TargetMAUNum(self):
        r"""This month's MAU data
        :rtype: int
        """
        return self._TargetMAUNum

    @TargetMAUNum.setter
    def TargetMAUNum(self, TargetMAUNum):
        self._TargetMAUNum = TargetMAUNum

    @property
    def FlushTime(self):
        r"""Data timestamp
        :rtype: int
        """
        return self._FlushTime

    @FlushTime.setter
    def FlushTime(self, FlushTime):
        self._FlushTime = FlushTime


    def _deserialize(self, params):
        self._ComparisonRatio = params.get("ComparisonRatio")
        self._ComparisonResult = params.get("ComparisonResult")
        self._SourceMAUNum = params.get("SourceMAUNum")
        self._TargetMAUNum = params.get("TargetMAUNum")
        self._FlushTime = params.get("FlushTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MAULineChartData(AbstractModel):
    r"""Line chart data

    """

    def __init__(self):
        r"""
        :param _DataTime: Year-month date data
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataTime: int
        :param _MAUCount: MAU data
Note: This field may return null, indicating that no valid values can be obtained.
        :type MAUCount: str
        """
        self._DataTime = None
        self._MAUCount = None

    @property
    def DataTime(self):
        r"""Year-month date data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DataTime

    @DataTime.setter
    def DataTime(self, DataTime):
        self._DataTime = DataTime

    @property
    def MAUCount(self):
        r"""MAU data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MAUCount

    @MAUCount.setter
    def MAUCount(self, MAUCount):
        self._MAUCount = MAUCount


    def _deserialize(self, params):
        self._DataTime = params.get("DataTime")
        self._MAUCount = params.get("MAUCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MNGMAULineChartData(AbstractModel):
    r"""Mini game MAU line chart data

    """

    def __init__(self):
        r"""
        :param _DataTime: Year-month-date data
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataTime: int
        :param _MAUCount: MAU data
Note: This field may return null, indicating that no valid values can be obtained.
        :type MAUCount: int
        :param _UpdateTime: Update time
        :type UpdateTime: int
        """
        self._DataTime = None
        self._MAUCount = None
        self._UpdateTime = None

    @property
    def DataTime(self):
        r"""Year-month-date data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DataTime

    @DataTime.setter
    def DataTime(self, DataTime):
        self._DataTime = DataTime

    @property
    def MAUCount(self):
        r"""MAU data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MAUCount

    @MAUCount.setter
    def MAUCount(self, MAUCount):
        self._MAUCount = MAUCount

    @property
    def UpdateTime(self):
        r"""Update time
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._DataTime = params.get("DataTime")
        self._MAUCount = params.get("MAUCount")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MNGPaymentOverview(AbstractModel):
    r"""Payment overview data

    """

    def __init__(self):
        r"""
        :param _ARPPu: Paid revenue / Number of paying users * 100%
        :type ARPPu: str
        :param _DataTime: Data time in YYYYMMDD format
        :type DataTime: str
        :param _NewPaidUseRatio: New paying user ratio = NewUserNum / OrderUserNum * 100%
        :type NewPaidUseRatio: str
        :param _NewPaidUserNum: Number of new paying users
        :type NewPaidUserNum: int
        :param _NewUserPaidAmount: Total payment amount from new users
        :type NewUserPaidAmount: str
        :param _PaidAmount: Total payment amount
        :type PaidAmount: str
        :param _PaidUserNum: Number of paying users
        :type PaidUserNum: int
        :param _RefundAmount: Refund amount
        :type RefundAmount: str
        :param _RefundNum: Number of refund orders
        :type RefundNum: int
        :param _UpdateTime: Update time (timestamp in seconds)
        :type UpdateTime: int
        """
        self._ARPPu = None
        self._DataTime = None
        self._NewPaidUseRatio = None
        self._NewPaidUserNum = None
        self._NewUserPaidAmount = None
        self._PaidAmount = None
        self._PaidUserNum = None
        self._RefundAmount = None
        self._RefundNum = None
        self._UpdateTime = None

    @property
    def ARPPu(self):
        r"""Paid revenue / Number of paying users * 100%
        :rtype: str
        """
        return self._ARPPu

    @ARPPu.setter
    def ARPPu(self, ARPPu):
        self._ARPPu = ARPPu

    @property
    def DataTime(self):
        r"""Data time in YYYYMMDD format
        :rtype: str
        """
        return self._DataTime

    @DataTime.setter
    def DataTime(self, DataTime):
        self._DataTime = DataTime

    @property
    def NewPaidUseRatio(self):
        r"""New paying user ratio = NewUserNum / OrderUserNum * 100%
        :rtype: str
        """
        return self._NewPaidUseRatio

    @NewPaidUseRatio.setter
    def NewPaidUseRatio(self, NewPaidUseRatio):
        self._NewPaidUseRatio = NewPaidUseRatio

    @property
    def NewPaidUserNum(self):
        r"""Number of new paying users
        :rtype: int
        """
        return self._NewPaidUserNum

    @NewPaidUserNum.setter
    def NewPaidUserNum(self, NewPaidUserNum):
        self._NewPaidUserNum = NewPaidUserNum

    @property
    def NewUserPaidAmount(self):
        r"""Total payment amount from new users
        :rtype: str
        """
        return self._NewUserPaidAmount

    @NewUserPaidAmount.setter
    def NewUserPaidAmount(self, NewUserPaidAmount):
        self._NewUserPaidAmount = NewUserPaidAmount

    @property
    def PaidAmount(self):
        r"""Total payment amount
        :rtype: str
        """
        return self._PaidAmount

    @PaidAmount.setter
    def PaidAmount(self, PaidAmount):
        self._PaidAmount = PaidAmount

    @property
    def PaidUserNum(self):
        r"""Number of paying users
        :rtype: int
        """
        return self._PaidUserNum

    @PaidUserNum.setter
    def PaidUserNum(self, PaidUserNum):
        self._PaidUserNum = PaidUserNum

    @property
    def RefundAmount(self):
        r"""Refund amount
        :rtype: str
        """
        return self._RefundAmount

    @RefundAmount.setter
    def RefundAmount(self, RefundAmount):
        self._RefundAmount = RefundAmount

    @property
    def RefundNum(self):
        r"""Number of refund orders
        :rtype: int
        """
        return self._RefundNum

    @RefundNum.setter
    def RefundNum(self, RefundNum):
        self._RefundNum = RefundNum

    @property
    def UpdateTime(self):
        r"""Update time (timestamp in seconds)
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._ARPPu = params.get("ARPPu")
        self._DataTime = params.get("DataTime")
        self._NewPaidUseRatio = params.get("NewPaidUseRatio")
        self._NewPaidUserNum = params.get("NewPaidUserNum")
        self._NewUserPaidAmount = params.get("NewUserPaidAmount")
        self._PaidAmount = params.get("PaidAmount")
        self._PaidUserNum = params.get("PaidUserNum")
        self._RefundAmount = params.get("RefundAmount")
        self._RefundNum = params.get("RefundNum")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MNPAdOverview(AbstractModel):
    r"""Mini program advertisement overview

    """

    def __init__(self):
        r"""
        :param _EstimatedEarnings: Estimated revenue
Note: This field may return null, indicating that no valid values can be obtained.
        :type EstimatedEarnings: str
        :param _ECPM: Effective Cost Per Mille
Note: This field may return null, indicating that no valid values can be obtained.
        :type ECPM: str
        :param _RequestsNumber: Requests
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestsNumber: int
        :param _Impressions: Impressions
Note: This field may return null, indicating that no valid values can be obtained.
        :type Impressions: int
        :param _ClicksNumber: Taps
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClicksNumber: int
        """
        self._EstimatedEarnings = None
        self._ECPM = None
        self._RequestsNumber = None
        self._Impressions = None
        self._ClicksNumber = None

    @property
    def EstimatedEarnings(self):
        r"""Estimated revenue
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EstimatedEarnings

    @EstimatedEarnings.setter
    def EstimatedEarnings(self, EstimatedEarnings):
        self._EstimatedEarnings = EstimatedEarnings

    @property
    def ECPM(self):
        r"""Effective Cost Per Mille
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ECPM

    @ECPM.setter
    def ECPM(self, ECPM):
        self._ECPM = ECPM

    @property
    def RequestsNumber(self):
        r"""Requests
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RequestsNumber

    @RequestsNumber.setter
    def RequestsNumber(self, RequestsNumber):
        self._RequestsNumber = RequestsNumber

    @property
    def Impressions(self):
        r"""Impressions
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Impressions

    @Impressions.setter
    def Impressions(self, Impressions):
        self._Impressions = Impressions

    @property
    def ClicksNumber(self):
        r"""Taps
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ClicksNumber

    @ClicksNumber.setter
    def ClicksNumber(self, ClicksNumber):
        self._ClicksNumber = ClicksNumber


    def _deserialize(self, params):
        self._EstimatedEarnings = params.get("EstimatedEarnings")
        self._ECPM = params.get("ECPM")
        self._RequestsNumber = params.get("RequestsNumber")
        self._Impressions = params.get("Impressions")
        self._ClicksNumber = params.get("ClicksNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MNPAdvertisingOverview(AbstractModel):
    r"""Mini program advertising revenue

    """

    def __init__(self):
        r"""
        :param _OverviewData: Data
Note: This field may return null, indicating that no valid values can be obtained.
        :type OverviewData: :class:`tencentcloud.tcsas.v20250106.models.MNPAdOverview`
        """
        self._OverviewData = None

    @property
    def OverviewData(self):
        r"""Data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.MNPAdOverview`
        """
        return self._OverviewData

    @OverviewData.setter
    def OverviewData(self, OverviewData):
        self._OverviewData = OverviewData


    def _deserialize(self, params):
        if params.get("OverviewData") is not None:
            self._OverviewData = MNPAdOverview()
            self._OverviewData._deserialize(params.get("OverviewData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MNPPaymentOverview(AbstractModel):
    r"""Payment overview data

    """

    def __init__(self):
        r"""
        :param _OrderMNPNum: Number of mini programs involved in the order
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrderMNPNum: int
        :param _OrderNum: Total orders

Note: This field may return null, indicating that no valid values can be obtained.
        :type OrderNum: int
        :param _OrderPaidNum: Total paid orders

Note: This field may return null, indicating that no valid values can be obtained.
        :type OrderPaidNum: int
        :param _OrderRefundNum: Total refunded orders

Note: This field may return null, indicating that no valid values can be obtained.
        :type OrderRefundNum: int
        :param _OrderUnpaidNum: Total unpaid orders
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrderUnpaidNum: int
        :param _OrderUserNum: Total order users
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrderUserNum: int
        :param _PaidUserNum: Total paying users
Note: This field may return null, indicating that no valid values can be obtained.
        :type PaidUserNum: int
        :param _PaidAmount: Amount paid
Note: This field may return null, indicating that no valid values can be obtained.
        :type PaidAmount: str
        :param _RefundAmount: Total amount refunded
Note: This field may return null, indicating that no valid values can be obtained.
        :type RefundAmount: str
        :param _TotalAmount: Total order amount
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalAmount: str
        :param _UnpaidAmount: Unpaid amount
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnpaidAmount: str
        :param _UpdateTime: Timestamp
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: int
        :param _DataTime: Data date
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataTime: str
        """
        self._OrderMNPNum = None
        self._OrderNum = None
        self._OrderPaidNum = None
        self._OrderRefundNum = None
        self._OrderUnpaidNum = None
        self._OrderUserNum = None
        self._PaidUserNum = None
        self._PaidAmount = None
        self._RefundAmount = None
        self._TotalAmount = None
        self._UnpaidAmount = None
        self._UpdateTime = None
        self._DataTime = None

    @property
    def OrderMNPNum(self):
        r"""Number of mini programs involved in the order
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._OrderMNPNum

    @OrderMNPNum.setter
    def OrderMNPNum(self, OrderMNPNum):
        self._OrderMNPNum = OrderMNPNum

    @property
    def OrderNum(self):
        r"""Total orders

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._OrderNum

    @OrderNum.setter
    def OrderNum(self, OrderNum):
        self._OrderNum = OrderNum

    @property
    def OrderPaidNum(self):
        r"""Total paid orders

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._OrderPaidNum

    @OrderPaidNum.setter
    def OrderPaidNum(self, OrderPaidNum):
        self._OrderPaidNum = OrderPaidNum

    @property
    def OrderRefundNum(self):
        r"""Total refunded orders

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._OrderRefundNum

    @OrderRefundNum.setter
    def OrderRefundNum(self, OrderRefundNum):
        self._OrderRefundNum = OrderRefundNum

    @property
    def OrderUnpaidNum(self):
        r"""Total unpaid orders
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._OrderUnpaidNum

    @OrderUnpaidNum.setter
    def OrderUnpaidNum(self, OrderUnpaidNum):
        self._OrderUnpaidNum = OrderUnpaidNum

    @property
    def OrderUserNum(self):
        r"""Total order users
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._OrderUserNum

    @OrderUserNum.setter
    def OrderUserNum(self, OrderUserNum):
        self._OrderUserNum = OrderUserNum

    @property
    def PaidUserNum(self):
        r"""Total paying users
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PaidUserNum

    @PaidUserNum.setter
    def PaidUserNum(self, PaidUserNum):
        self._PaidUserNum = PaidUserNum

    @property
    def PaidAmount(self):
        r"""Amount paid
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PaidAmount

    @PaidAmount.setter
    def PaidAmount(self, PaidAmount):
        self._PaidAmount = PaidAmount

    @property
    def RefundAmount(self):
        r"""Total amount refunded
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RefundAmount

    @RefundAmount.setter
    def RefundAmount(self, RefundAmount):
        self._RefundAmount = RefundAmount

    @property
    def TotalAmount(self):
        r"""Total order amount
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TotalAmount

    @TotalAmount.setter
    def TotalAmount(self, TotalAmount):
        self._TotalAmount = TotalAmount

    @property
    def UnpaidAmount(self):
        r"""Unpaid amount
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UnpaidAmount

    @UnpaidAmount.setter
    def UnpaidAmount(self, UnpaidAmount):
        self._UnpaidAmount = UnpaidAmount

    @property
    def UpdateTime(self):
        r"""Timestamp
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DataTime(self):
        r"""Data date
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DataTime

    @DataTime.setter
    def DataTime(self, DataTime):
        self._DataTime = DataTime


    def _deserialize(self, params):
        self._OrderMNPNum = params.get("OrderMNPNum")
        self._OrderNum = params.get("OrderNum")
        self._OrderPaidNum = params.get("OrderPaidNum")
        self._OrderRefundNum = params.get("OrderRefundNum")
        self._OrderUnpaidNum = params.get("OrderUnpaidNum")
        self._OrderUserNum = params.get("OrderUserNum")
        self._PaidUserNum = params.get("PaidUserNum")
        self._PaidAmount = params.get("PaidAmount")
        self._RefundAmount = params.get("RefundAmount")
        self._TotalAmount = params.get("TotalAmount")
        self._UnpaidAmount = params.get("UnpaidAmount")
        self._UpdateTime = params.get("UpdateTime")
        self._DataTime = params.get("DataTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MNPTypeDefine(AbstractModel):
    r"""Mini program category information

    """

    def __init__(self):
        r"""
        :param _TypeName: Specifies the mini program category name.
        :type TypeName: str
        :param _TypeValue: Mini program category value.
        :type TypeValue: list of str
        :param _TypeId: Category ID.
        :type TypeId: int
        :param _CreateTime: Creation time
        :type CreateTime: int
        :param _CreateUser: Creator
        :type CreateUser: str
        :param _IsSystem: Indicates whether it is a system category.
        :type IsSystem: bool
        """
        self._TypeName = None
        self._TypeValue = None
        self._TypeId = None
        self._CreateTime = None
        self._CreateUser = None
        self._IsSystem = None

    @property
    def TypeName(self):
        r"""Specifies the mini program category name.
        :rtype: str
        """
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def TypeValue(self):
        r"""Mini program category value.
        :rtype: list of str
        """
        return self._TypeValue

    @TypeValue.setter
    def TypeValue(self, TypeValue):
        self._TypeValue = TypeValue

    @property
    def TypeId(self):
        r"""Category ID.
        :rtype: int
        """
        return self._TypeId

    @TypeId.setter
    def TypeId(self, TypeId):
        self._TypeId = TypeId

    @property
    def CreateTime(self):
        r"""Creation time
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CreateUser(self):
        r"""Creator
        :rtype: str
        """
        return self._CreateUser

    @CreateUser.setter
    def CreateUser(self, CreateUser):
        self._CreateUser = CreateUser

    @property
    def IsSystem(self):
        r"""Indicates whether it is a system category.
        :rtype: bool
        """
        return self._IsSystem

    @IsSystem.setter
    def IsSystem(self, IsSystem):
        self._IsSystem = IsSystem


    def _deserialize(self, params):
        self._TypeName = params.get("TypeName")
        self._TypeValue = params.get("TypeValue")
        self._TypeId = params.get("TypeId")
        self._CreateTime = params.get("CreateTime")
        self._CreateUser = params.get("CreateUser")
        self._IsSystem = params.get("IsSystem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationConfigRequest(AbstractModel):
    r"""ModifyApplicationConfig request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Superapp ID
        :type ApplicationId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _Id: Superapp configuration ID
        :type Id: int
        :param _AppKey: Package name: corresponds to packageName on Android and bundleId on iOS
        :type AppKey: str
        :param _AppURL: Superapp URL
        :type AppURL: str
        """
        self._ApplicationId = None
        self._PlatformId = None
        self._Id = None
        self._AppKey = None
        self._AppURL = None

    @property
    def ApplicationId(self):
        r"""Superapp ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def Id(self):
        r"""Superapp configuration ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AppKey(self):
        r"""Package name: corresponds to packageName on Android and bundleId on iOS
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def AppURL(self):
        r"""Superapp URL
        :rtype: str
        """
        return self._AppURL

    @AppURL.setter
    def AppURL(self, AppURL):
        self._AppURL = AppURL


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._PlatformId = params.get("PlatformId")
        self._Id = params.get("Id")
        self._AppKey = params.get("AppKey")
        self._AppURL = params.get("AppURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationConfigResponse(AbstractModel):
    r"""ModifyApplicationConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyApplicationRequest(AbstractModel):
    r"""ModifyApplication request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _ApplicationName: Application name
        :type ApplicationName: str
        :param _Intro: Application introduction
        :type Intro: str
        :param _Logo: Icon
        :type Logo: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _AndroidAppKey: Android app package name
        :type AndroidAppKey: str
        :param _IosAppKey: iOS App bundleId
        :type IosAppKey: str
        :param _Remark: Remarks
        :type Remark: str
        :param _Scheme: Scheme
        :type Scheme: str
        """
        self._ApplicationId = None
        self._ApplicationName = None
        self._Intro = None
        self._Logo = None
        self._PlatformId = None
        self._AndroidAppKey = None
        self._IosAppKey = None
        self._Remark = None
        self._Scheme = None

    @property
    def ApplicationId(self):
        r"""Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        r"""Application name
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def Intro(self):
        r"""Application introduction
        :rtype: str
        """
        return self._Intro

    @Intro.setter
    def Intro(self, Intro):
        self._Intro = Intro

    @property
    def Logo(self):
        r"""Icon
        :rtype: str
        """
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def AndroidAppKey(self):
        warnings.warn("parameter `AndroidAppKey` is deprecated", DeprecationWarning) 

        r"""Android app package name
        :rtype: str
        """
        return self._AndroidAppKey

    @AndroidAppKey.setter
    def AndroidAppKey(self, AndroidAppKey):
        warnings.warn("parameter `AndroidAppKey` is deprecated", DeprecationWarning) 

        self._AndroidAppKey = AndroidAppKey

    @property
    def IosAppKey(self):
        warnings.warn("parameter `IosAppKey` is deprecated", DeprecationWarning) 

        r"""iOS App bundleId
        :rtype: str
        """
        return self._IosAppKey

    @IosAppKey.setter
    def IosAppKey(self, IosAppKey):
        warnings.warn("parameter `IosAppKey` is deprecated", DeprecationWarning) 

        self._IosAppKey = IosAppKey

    @property
    def Remark(self):
        warnings.warn("parameter `Remark` is deprecated", DeprecationWarning) 

        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        warnings.warn("parameter `Remark` is deprecated", DeprecationWarning) 

        self._Remark = Remark

    @property
    def Scheme(self):
        r"""Scheme
        :rtype: str
        """
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._Intro = params.get("Intro")
        self._Logo = params.get("Logo")
        self._PlatformId = params.get("PlatformId")
        self._AndroidAppKey = params.get("AndroidAppKey")
        self._IosAppKey = params.get("IosAppKey")
        self._Remark = params.get("Remark")
        self._Scheme = params.get("Scheme")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationResponse(AbstractModel):
    r"""ModifyApplication response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyGlobalDomainRequest(AbstractModel):
    r"""ModifyGlobalDomain request structure.

    """

    def __init__(self):
        r"""
        :param _DomainId: Domain ID
        :type DomainId: int
        :param _DomainUrl: Domain name
        :type DomainUrl: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._DomainId = None
        self._DomainUrl = None
        self._PlatformId = None

    @property
    def DomainId(self):
        r"""Domain ID
        :rtype: int
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def DomainUrl(self):
        r"""Domain name
        :rtype: str
        """
        return self._DomainUrl

    @DomainUrl.setter
    def DomainUrl(self, DomainUrl):
        self._DomainUrl = DomainUrl

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._DomainUrl = params.get("DomainUrl")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGlobalDomainResponse(AbstractModel):
    r"""ModifyGlobalDomain response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.GlobalDomainModifyRespResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.GlobalDomainModifyRespResp`
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
        if params.get("Data") is not None:
            self._Data = GlobalDomainModifyRespResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyMNPDomainRequest(AbstractModel):
    r"""ModifyMNPDomain request structure.

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _Domain: Domain list
        :type Domain: list of CreateDomainParam
        """
        self._MNPId = None
        self._PlatformId = None
        self._Domain = None

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def Domain(self):
        r"""Domain list
        :rtype: list of CreateDomainParam
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        if params.get("Domain") is not None:
            self._Domain = []
            for item in params.get("Domain"):
                obj = CreateDomainParam()
                obj._deserialize(item)
                self._Domain.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMNPDomainResponse(AbstractModel):
    r"""ModifyMNPDomain response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyMNPRequest(AbstractModel):
    r"""ModifyMNP request structure.

    """

    def __init__(self):
        r"""
        :param _MNPType: Mini program type
        :type MNPType: str
        :param _MNPName: Mini program name
        :type MNPName: str
        :param _MNPIntro: Mini program introduction
        :type MNPIntro: str
        :param _MNPDesc: Mini program description
        :type MNPDesc: str
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _MNPIcon: Mini program icon
        :type MNPIcon: str
        """
        self._MNPType = None
        self._MNPName = None
        self._MNPIntro = None
        self._MNPDesc = None
        self._MNPId = None
        self._PlatformId = None
        self._MNPIcon = None

    @property
    def MNPType(self):
        r"""Mini program type
        :rtype: str
        """
        return self._MNPType

    @MNPType.setter
    def MNPType(self, MNPType):
        self._MNPType = MNPType

    @property
    def MNPName(self):
        r"""Mini program name
        :rtype: str
        """
        return self._MNPName

    @MNPName.setter
    def MNPName(self, MNPName):
        self._MNPName = MNPName

    @property
    def MNPIntro(self):
        r"""Mini program introduction
        :rtype: str
        """
        return self._MNPIntro

    @MNPIntro.setter
    def MNPIntro(self, MNPIntro):
        self._MNPIntro = MNPIntro

    @property
    def MNPDesc(self):
        r"""Mini program description
        :rtype: str
        """
        return self._MNPDesc

    @MNPDesc.setter
    def MNPDesc(self, MNPDesc):
        self._MNPDesc = MNPDesc

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def MNPIcon(self):
        r"""Mini program icon
        :rtype: str
        """
        return self._MNPIcon

    @MNPIcon.setter
    def MNPIcon(self, MNPIcon):
        self._MNPIcon = MNPIcon


    def _deserialize(self, params):
        self._MNPType = params.get("MNPType")
        self._MNPName = params.get("MNPName")
        self._MNPIntro = params.get("MNPIntro")
        self._MNPDesc = params.get("MNPDesc")
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        self._MNPIcon = params.get("MNPIcon")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMNPResponse(AbstractModel):
    r"""ModifyMNP response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.ResourceIdInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ResourceIdInfo`
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
        if params.get("Data") is not None:
            self._Data = ResourceIdInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyTeamMemberRequest(AbstractModel):
    r"""ModifyTeamMember request structure.

    """

    def __init__(self):
        r"""
        :param _TeamId: Team ID
        :type TeamId: str
        :param _UserId: User ID
        :type UserId: str
        :param _RoleId: Role ID
        :type RoleId: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._TeamId = None
        self._UserId = None
        self._RoleId = None
        self._PlatformId = None

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def UserId(self):
        r"""User ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoleId(self):
        r"""Role ID
        :rtype: int
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._UserId = params.get("UserId")
        self._RoleId = params.get("RoleId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTeamMemberResponse(AbstractModel):
    r"""ModifyTeamMember response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyTeamRequest(AbstractModel):
    r"""ModifyTeam request structure.

    """

    def __init__(self):
        r"""
        :param _TeamId: Team ID
        :type TeamId: str
        :param _TeamName: Team name
        :type TeamName: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _AdminUserId: Team administrator
        :type AdminUserId: str
        """
        self._TeamId = None
        self._TeamName = None
        self._PlatformId = None
        self._AdminUserId = None

    @property
    def TeamId(self):
        r"""Team ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def TeamName(self):
        r"""Team name
        :rtype: str
        """
        return self._TeamName

    @TeamName.setter
    def TeamName(self, TeamName):
        self._TeamName = TeamName

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def AdminUserId(self):
        r"""Team administrator
        :rtype: str
        """
        return self._AdminUserId

    @AdminUserId.setter
    def AdminUserId(self, AdminUserId):
        self._AdminUserId = AdminUserId


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._TeamName = params.get("TeamName")
        self._PlatformId = params.get("PlatformId")
        self._AdminUserId = params.get("AdminUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTeamResponse(AbstractModel):
    r"""ModifyTeam response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyUserRequest(AbstractModel):
    r"""ModifyUser request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID
        :type UserId: str
        :param _UserName: User name
        :type UserName: str
        :param _AccountType: Account type 2 - Platform admin 3 - Member
        :type AccountType: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._UserId = None
        self._UserName = None
        self._AccountType = None
        self._PlatformId = None

    @property
    def UserId(self):
        r"""User ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        r"""User name
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def AccountType(self):
        r"""Account type 2 - Platform admin 3 - Member
        :rtype: int
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._AccountType = params.get("AccountType")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserResponse(AbstractModel):
    r"""ModifyUser response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class Overview(AbstractModel):
    r"""Global overview data

    """

    def __init__(self):
        r"""
        :param _AppNum: Superapps
        :type AppNum: int
        :param _CorpNum: Teams
        :type CorpNum: int
        :param _FlushTime: Refresh time
        :type FlushTime: str
        :param _MiniAppNum: Mini programs
        :type MiniAppNum: int
        :param _MiniGameNum: Mini games
        :type MiniGameNum: int
        :param _MiniGameVisitNum: Mini game visits
        :type MiniGameVisitNum: int
        :param _UpdateNum: Mini program updates
        :type UpdateNum: int
        :param _VisitNum: Mini program visits
        :type VisitNum: int
        """
        self._AppNum = None
        self._CorpNum = None
        self._FlushTime = None
        self._MiniAppNum = None
        self._MiniGameNum = None
        self._MiniGameVisitNum = None
        self._UpdateNum = None
        self._VisitNum = None

    @property
    def AppNum(self):
        r"""Superapps
        :rtype: int
        """
        return self._AppNum

    @AppNum.setter
    def AppNum(self, AppNum):
        self._AppNum = AppNum

    @property
    def CorpNum(self):
        r"""Teams
        :rtype: int
        """
        return self._CorpNum

    @CorpNum.setter
    def CorpNum(self, CorpNum):
        self._CorpNum = CorpNum

    @property
    def FlushTime(self):
        r"""Refresh time
        :rtype: str
        """
        return self._FlushTime

    @FlushTime.setter
    def FlushTime(self, FlushTime):
        self._FlushTime = FlushTime

    @property
    def MiniAppNum(self):
        r"""Mini programs
        :rtype: int
        """
        return self._MiniAppNum

    @MiniAppNum.setter
    def MiniAppNum(self, MiniAppNum):
        self._MiniAppNum = MiniAppNum

    @property
    def MiniGameNum(self):
        r"""Mini games
        :rtype: int
        """
        return self._MiniGameNum

    @MiniGameNum.setter
    def MiniGameNum(self, MiniGameNum):
        self._MiniGameNum = MiniGameNum

    @property
    def MiniGameVisitNum(self):
        r"""Mini game visits
        :rtype: int
        """
        return self._MiniGameVisitNum

    @MiniGameVisitNum.setter
    def MiniGameVisitNum(self, MiniGameVisitNum):
        self._MiniGameVisitNum = MiniGameVisitNum

    @property
    def UpdateNum(self):
        r"""Mini program updates
        :rtype: int
        """
        return self._UpdateNum

    @UpdateNum.setter
    def UpdateNum(self, UpdateNum):
        self._UpdateNum = UpdateNum

    @property
    def VisitNum(self):
        r"""Mini program visits
        :rtype: int
        """
        return self._VisitNum

    @VisitNum.setter
    def VisitNum(self, VisitNum):
        self._VisitNum = VisitNum


    def _deserialize(self, params):
        self._AppNum = params.get("AppNum")
        self._CorpNum = params.get("CorpNum")
        self._FlushTime = params.get("FlushTime")
        self._MiniAppNum = params.get("MiniAppNum")
        self._MiniGameNum = params.get("MiniGameNum")
        self._MiniGameVisitNum = params.get("MiniGameVisitNum")
        self._UpdateNum = params.get("UpdateNum")
        self._VisitNum = params.get("VisitNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OverviewDetail(AbstractModel):
    r"""Advertising data list fields

    """

    def __init__(self):
        r"""
        :param _DataTime: Time
        :type DataTime: str
        :param _MNPName: Name
        :type MNPName: str
        :param _MNPType: Category
        :type MNPType: str
        :param _EstimatedEarnings: Estimated revenue
        :type EstimatedEarnings: str
        :param _RequestsNumber: Requests
        :type RequestsNumber: int
        :param _Impressions: Impressions
        :type Impressions: int
        :param _ECPM: Effective Cost Per Mille
        :type ECPM: str
        :param _ClicksNumber: Taps
        :type ClicksNumber: int
        """
        self._DataTime = None
        self._MNPName = None
        self._MNPType = None
        self._EstimatedEarnings = None
        self._RequestsNumber = None
        self._Impressions = None
        self._ECPM = None
        self._ClicksNumber = None

    @property
    def DataTime(self):
        r"""Time
        :rtype: str
        """
        return self._DataTime

    @DataTime.setter
    def DataTime(self, DataTime):
        self._DataTime = DataTime

    @property
    def MNPName(self):
        r"""Name
        :rtype: str
        """
        return self._MNPName

    @MNPName.setter
    def MNPName(self, MNPName):
        self._MNPName = MNPName

    @property
    def MNPType(self):
        r"""Category
        :rtype: str
        """
        return self._MNPType

    @MNPType.setter
    def MNPType(self, MNPType):
        self._MNPType = MNPType

    @property
    def EstimatedEarnings(self):
        r"""Estimated revenue
        :rtype: str
        """
        return self._EstimatedEarnings

    @EstimatedEarnings.setter
    def EstimatedEarnings(self, EstimatedEarnings):
        self._EstimatedEarnings = EstimatedEarnings

    @property
    def RequestsNumber(self):
        r"""Requests
        :rtype: int
        """
        return self._RequestsNumber

    @RequestsNumber.setter
    def RequestsNumber(self, RequestsNumber):
        self._RequestsNumber = RequestsNumber

    @property
    def Impressions(self):
        r"""Impressions
        :rtype: int
        """
        return self._Impressions

    @Impressions.setter
    def Impressions(self, Impressions):
        self._Impressions = Impressions

    @property
    def ECPM(self):
        r"""Effective Cost Per Mille
        :rtype: str
        """
        return self._ECPM

    @ECPM.setter
    def ECPM(self, ECPM):
        self._ECPM = ECPM

    @property
    def ClicksNumber(self):
        r"""Taps
        :rtype: int
        """
        return self._ClicksNumber

    @ClicksNumber.setter
    def ClicksNumber(self, ClicksNumber):
        self._ClicksNumber = ClicksNumber


    def _deserialize(self, params):
        self._DataTime = params.get("DataTime")
        self._MNPName = params.get("MNPName")
        self._MNPType = params.get("MNPType")
        self._EstimatedEarnings = params.get("EstimatedEarnings")
        self._RequestsNumber = params.get("RequestsNumber")
        self._Impressions = params.get("Impressions")
        self._ECPM = params.get("ECPM")
        self._ClicksNumber = params.get("ClicksNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PaymentActiveRetention(AbstractModel):
    r"""Payment active retention data

    """

    def __init__(self):
        r"""
        :param _OneDayRetentionUsers: Day 1 active retention of paying users
        :type OneDayRetentionUsers: int
        :param _TwoDayRetentionUsers: Day 2 active retention of paying users
        :type TwoDayRetentionUsers: int
        :param _ThreeDayRetentionUsers: Day 3 active retention of paying users
        :type ThreeDayRetentionUsers: int
        :param _FourDayRetentionUsers: Day 4 active retention of paying users
        :type FourDayRetentionUsers: int
        :param _FiveDayRetentionUsers: Day 5 active retention of paying users
        :type FiveDayRetentionUsers: int
        :param _SixDayRetentionUsers: Day 6 active retention of paying users
        :type SixDayRetentionUsers: int
        :param _SevenDayRetentionUsers: Day 7 active retention of paying users
        :type SevenDayRetentionUsers: int
        :param _FourteenDayRetentionUsers: Day 14 active retention of paying users
        :type FourteenDayRetentionUsers: int
        :param _FifteenDayRetentionUsers: Day 15 active retention of paying users
        :type FifteenDayRetentionUsers: int
        :param _ThirtyDayRetentionUsers: Day 30 active retention of paying users
        :type ThirtyDayRetentionUsers: int
        :param _PaymentUserNum: Number of paying users
        :type PaymentUserNum: int
        :param _DataTime: Data time in YYYYMMDD format
        :type DataTime: str
        """
        self._OneDayRetentionUsers = None
        self._TwoDayRetentionUsers = None
        self._ThreeDayRetentionUsers = None
        self._FourDayRetentionUsers = None
        self._FiveDayRetentionUsers = None
        self._SixDayRetentionUsers = None
        self._SevenDayRetentionUsers = None
        self._FourteenDayRetentionUsers = None
        self._FifteenDayRetentionUsers = None
        self._ThirtyDayRetentionUsers = None
        self._PaymentUserNum = None
        self._DataTime = None

    @property
    def OneDayRetentionUsers(self):
        r"""Day 1 active retention of paying users
        :rtype: int
        """
        return self._OneDayRetentionUsers

    @OneDayRetentionUsers.setter
    def OneDayRetentionUsers(self, OneDayRetentionUsers):
        self._OneDayRetentionUsers = OneDayRetentionUsers

    @property
    def TwoDayRetentionUsers(self):
        r"""Day 2 active retention of paying users
        :rtype: int
        """
        return self._TwoDayRetentionUsers

    @TwoDayRetentionUsers.setter
    def TwoDayRetentionUsers(self, TwoDayRetentionUsers):
        self._TwoDayRetentionUsers = TwoDayRetentionUsers

    @property
    def ThreeDayRetentionUsers(self):
        r"""Day 3 active retention of paying users
        :rtype: int
        """
        return self._ThreeDayRetentionUsers

    @ThreeDayRetentionUsers.setter
    def ThreeDayRetentionUsers(self, ThreeDayRetentionUsers):
        self._ThreeDayRetentionUsers = ThreeDayRetentionUsers

    @property
    def FourDayRetentionUsers(self):
        r"""Day 4 active retention of paying users
        :rtype: int
        """
        return self._FourDayRetentionUsers

    @FourDayRetentionUsers.setter
    def FourDayRetentionUsers(self, FourDayRetentionUsers):
        self._FourDayRetentionUsers = FourDayRetentionUsers

    @property
    def FiveDayRetentionUsers(self):
        r"""Day 5 active retention of paying users
        :rtype: int
        """
        return self._FiveDayRetentionUsers

    @FiveDayRetentionUsers.setter
    def FiveDayRetentionUsers(self, FiveDayRetentionUsers):
        self._FiveDayRetentionUsers = FiveDayRetentionUsers

    @property
    def SixDayRetentionUsers(self):
        r"""Day 6 active retention of paying users
        :rtype: int
        """
        return self._SixDayRetentionUsers

    @SixDayRetentionUsers.setter
    def SixDayRetentionUsers(self, SixDayRetentionUsers):
        self._SixDayRetentionUsers = SixDayRetentionUsers

    @property
    def SevenDayRetentionUsers(self):
        r"""Day 7 active retention of paying users
        :rtype: int
        """
        return self._SevenDayRetentionUsers

    @SevenDayRetentionUsers.setter
    def SevenDayRetentionUsers(self, SevenDayRetentionUsers):
        self._SevenDayRetentionUsers = SevenDayRetentionUsers

    @property
    def FourteenDayRetentionUsers(self):
        r"""Day 14 active retention of paying users
        :rtype: int
        """
        return self._FourteenDayRetentionUsers

    @FourteenDayRetentionUsers.setter
    def FourteenDayRetentionUsers(self, FourteenDayRetentionUsers):
        self._FourteenDayRetentionUsers = FourteenDayRetentionUsers

    @property
    def FifteenDayRetentionUsers(self):
        r"""Day 15 active retention of paying users
        :rtype: int
        """
        return self._FifteenDayRetentionUsers

    @FifteenDayRetentionUsers.setter
    def FifteenDayRetentionUsers(self, FifteenDayRetentionUsers):
        self._FifteenDayRetentionUsers = FifteenDayRetentionUsers

    @property
    def ThirtyDayRetentionUsers(self):
        r"""Day 30 active retention of paying users
        :rtype: int
        """
        return self._ThirtyDayRetentionUsers

    @ThirtyDayRetentionUsers.setter
    def ThirtyDayRetentionUsers(self, ThirtyDayRetentionUsers):
        self._ThirtyDayRetentionUsers = ThirtyDayRetentionUsers

    @property
    def PaymentUserNum(self):
        r"""Number of paying users
        :rtype: int
        """
        return self._PaymentUserNum

    @PaymentUserNum.setter
    def PaymentUserNum(self, PaymentUserNum):
        self._PaymentUserNum = PaymentUserNum

    @property
    def DataTime(self):
        r"""Data time in YYYYMMDD format
        :rtype: str
        """
        return self._DataTime

    @DataTime.setter
    def DataTime(self, DataTime):
        self._DataTime = DataTime


    def _deserialize(self, params):
        self._OneDayRetentionUsers = params.get("OneDayRetentionUsers")
        self._TwoDayRetentionUsers = params.get("TwoDayRetentionUsers")
        self._ThreeDayRetentionUsers = params.get("ThreeDayRetentionUsers")
        self._FourDayRetentionUsers = params.get("FourDayRetentionUsers")
        self._FiveDayRetentionUsers = params.get("FiveDayRetentionUsers")
        self._SixDayRetentionUsers = params.get("SixDayRetentionUsers")
        self._SevenDayRetentionUsers = params.get("SevenDayRetentionUsers")
        self._FourteenDayRetentionUsers = params.get("FourteenDayRetentionUsers")
        self._FifteenDayRetentionUsers = params.get("FifteenDayRetentionUsers")
        self._ThirtyDayRetentionUsers = params.get("ThirtyDayRetentionUsers")
        self._PaymentUserNum = params.get("PaymentUserNum")
        self._DataTime = params.get("DataTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PaymentDetail(AbstractModel):
    r"""Mini program payment detailed data

    """

    def __init__(self):
        r"""
        :param _DataTime: Date in YYYYMMDD format
        :type DataTime: str
        :param _OrderMNPNum: Number of mini programs involved in the order
        :type OrderMNPNum: int
        :param _OrderNum: Total orders
        :type OrderNum: int
        :param _OrderPaidNum: Paid orders
        :type OrderPaidNum: int
        :param _OrderRefundNum: Total refunded orders
        :type OrderRefundNum: int
        :param _OrderUnpaidNum: Unpaid orders
        :type OrderUnpaidNum: int
        :param _OrderUserNum: Number of users placing orders (openid)
        :type OrderUserNum: int
        :param _PaidAmount: Amount paid
        :type PaidAmount: str
        :param _RefundAmount: Amount refunded
        :type RefundAmount: str
        :param _TotalAmount: Total order amount
        :type TotalAmount: str
        :param _UnpaidAmount: Unpaid amount
        :type UnpaidAmount: str
        :param _UpdateTime: Data update timestamp
        :type UpdateTime: int
        """
        self._DataTime = None
        self._OrderMNPNum = None
        self._OrderNum = None
        self._OrderPaidNum = None
        self._OrderRefundNum = None
        self._OrderUnpaidNum = None
        self._OrderUserNum = None
        self._PaidAmount = None
        self._RefundAmount = None
        self._TotalAmount = None
        self._UnpaidAmount = None
        self._UpdateTime = None

    @property
    def DataTime(self):
        r"""Date in YYYYMMDD format
        :rtype: str
        """
        return self._DataTime

    @DataTime.setter
    def DataTime(self, DataTime):
        self._DataTime = DataTime

    @property
    def OrderMNPNum(self):
        r"""Number of mini programs involved in the order
        :rtype: int
        """
        return self._OrderMNPNum

    @OrderMNPNum.setter
    def OrderMNPNum(self, OrderMNPNum):
        self._OrderMNPNum = OrderMNPNum

    @property
    def OrderNum(self):
        r"""Total orders
        :rtype: int
        """
        return self._OrderNum

    @OrderNum.setter
    def OrderNum(self, OrderNum):
        self._OrderNum = OrderNum

    @property
    def OrderPaidNum(self):
        r"""Paid orders
        :rtype: int
        """
        return self._OrderPaidNum

    @OrderPaidNum.setter
    def OrderPaidNum(self, OrderPaidNum):
        self._OrderPaidNum = OrderPaidNum

    @property
    def OrderRefundNum(self):
        r"""Total refunded orders
        :rtype: int
        """
        return self._OrderRefundNum

    @OrderRefundNum.setter
    def OrderRefundNum(self, OrderRefundNum):
        self._OrderRefundNum = OrderRefundNum

    @property
    def OrderUnpaidNum(self):
        r"""Unpaid orders
        :rtype: int
        """
        return self._OrderUnpaidNum

    @OrderUnpaidNum.setter
    def OrderUnpaidNum(self, OrderUnpaidNum):
        self._OrderUnpaidNum = OrderUnpaidNum

    @property
    def OrderUserNum(self):
        r"""Number of users placing orders (openid)
        :rtype: int
        """
        return self._OrderUserNum

    @OrderUserNum.setter
    def OrderUserNum(self, OrderUserNum):
        self._OrderUserNum = OrderUserNum

    @property
    def PaidAmount(self):
        r"""Amount paid
        :rtype: str
        """
        return self._PaidAmount

    @PaidAmount.setter
    def PaidAmount(self, PaidAmount):
        self._PaidAmount = PaidAmount

    @property
    def RefundAmount(self):
        r"""Amount refunded
        :rtype: str
        """
        return self._RefundAmount

    @RefundAmount.setter
    def RefundAmount(self, RefundAmount):
        self._RefundAmount = RefundAmount

    @property
    def TotalAmount(self):
        r"""Total order amount
        :rtype: str
        """
        return self._TotalAmount

    @TotalAmount.setter
    def TotalAmount(self, TotalAmount):
        self._TotalAmount = TotalAmount

    @property
    def UnpaidAmount(self):
        r"""Unpaid amount
        :rtype: str
        """
        return self._UnpaidAmount

    @UnpaidAmount.setter
    def UnpaidAmount(self, UnpaidAmount):
        self._UnpaidAmount = UnpaidAmount

    @property
    def UpdateTime(self):
        r"""Data update timestamp
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._DataTime = params.get("DataTime")
        self._OrderMNPNum = params.get("OrderMNPNum")
        self._OrderNum = params.get("OrderNum")
        self._OrderPaidNum = params.get("OrderPaidNum")
        self._OrderRefundNum = params.get("OrderRefundNum")
        self._OrderUnpaidNum = params.get("OrderUnpaidNum")
        self._OrderUserNum = params.get("OrderUserNum")
        self._PaidAmount = params.get("PaidAmount")
        self._RefundAmount = params.get("RefundAmount")
        self._TotalAmount = params.get("TotalAmount")
        self._UnpaidAmount = params.get("UnpaidAmount")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PresetResp(AbstractModel):
    r"""Encryption key returned

    """

    def __init__(self):
        r"""
        :param _Key: RSA encryption public key.
        :type Key: str
        """
        self._Key = None

    @property
    def Key(self):
        r"""RSA encryption public key.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key


    def _deserialize(self, params):
        self._Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessMNPApprovalRequest(AbstractModel):
    r"""ProcessMNPApproval request structure.

    """

    def __init__(self):
        r"""
        :param _ApprovalNo: Approval ID
        :type ApprovalNo: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _ApprovalItems: Approval details
        :type ApprovalItems: list of ApprovalItem
        """
        self._ApprovalNo = None
        self._PlatformId = None
        self._ApprovalItems = None

    @property
    def ApprovalNo(self):
        r"""Approval ID
        :rtype: str
        """
        return self._ApprovalNo

    @ApprovalNo.setter
    def ApprovalNo(self, ApprovalNo):
        self._ApprovalNo = ApprovalNo

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ApprovalItems(self):
        r"""Approval details
        :rtype: list of ApprovalItem
        """
        return self._ApprovalItems

    @ApprovalItems.setter
    def ApprovalItems(self, ApprovalItems):
        self._ApprovalItems = ApprovalItems


    def _deserialize(self, params):
        self._ApprovalNo = params.get("ApprovalNo")
        self._PlatformId = params.get("PlatformId")
        if params.get("ApprovalItems") is not None:
            self._ApprovalItems = []
            for item in params.get("ApprovalItems"):
                obj = ApprovalItem()
                obj._deserialize(item)
                self._ApprovalItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessMNPApprovalResponse(AbstractModel):
    r"""ProcessMNPApproval response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ProcessMNPSensitiveAPIPermissionApprovalRequest(AbstractModel):
    r"""ProcessMNPSensitiveAPIPermissionApproval request structure.

    """

    def __init__(self):
        r"""
        :param _ApprovalNo: Approval ID
        :type ApprovalNo: str
        :param _ApprovalStatus: Approval status. 20: Rejected; 30: Approved
        :type ApprovalStatus: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _ApprovalNote: Approval notes
        :type ApprovalNote: str
        """
        self._ApprovalNo = None
        self._ApprovalStatus = None
        self._PlatformId = None
        self._ApprovalNote = None

    @property
    def ApprovalNo(self):
        r"""Approval ID
        :rtype: str
        """
        return self._ApprovalNo

    @ApprovalNo.setter
    def ApprovalNo(self, ApprovalNo):
        self._ApprovalNo = ApprovalNo

    @property
    def ApprovalStatus(self):
        r"""Approval status. 20: Rejected; 30: Approved
        :rtype: int
        """
        return self._ApprovalStatus

    @ApprovalStatus.setter
    def ApprovalStatus(self, ApprovalStatus):
        self._ApprovalStatus = ApprovalStatus

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def ApprovalNote(self):
        r"""Approval notes
        :rtype: str
        """
        return self._ApprovalNote

    @ApprovalNote.setter
    def ApprovalNote(self, ApprovalNote):
        self._ApprovalNote = ApprovalNote


    def _deserialize(self, params):
        self._ApprovalNo = params.get("ApprovalNo")
        self._ApprovalStatus = params.get("ApprovalStatus")
        self._PlatformId = params.get("PlatformId")
        self._ApprovalNote = params.get("ApprovalNote")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessMNPSensitiveAPIPermissionApprovalResponse(AbstractModel):
    r"""ProcessMNPSensitiveAPIPermissionApproval response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class QueryOnlineVersionResp(AbstractModel):
    r"""Mini program online version ID

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _MNPVersion: Version number
        :type MNPVersion: str
        :param _MNPVersionId: Version ID.
        :type MNPVersionId: int
        :param _MNPVersionNote: Version remarks.
        :type MNPVersionNote: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        """
        self._MNPId = None
        self._MNPVersion = None
        self._MNPVersionId = None
        self._MNPVersionNote = None
        self._UpdateTime = None

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def MNPVersion(self):
        r"""Version number
        :rtype: str
        """
        return self._MNPVersion

    @MNPVersion.setter
    def MNPVersion(self, MNPVersion):
        self._MNPVersion = MNPVersion

    @property
    def MNPVersionId(self):
        r"""Version ID.
        :rtype: int
        """
        return self._MNPVersionId

    @MNPVersionId.setter
    def MNPVersionId(self, MNPVersionId):
        self._MNPVersionId = MNPVersionId

    @property
    def MNPVersionNote(self):
        r"""Version remarks.
        :rtype: str
        """
        return self._MNPVersionNote

    @MNPVersionNote.setter
    def MNPVersionNote(self, MNPVersionNote):
        self._MNPVersionNote = MNPVersionNote

    @property
    def UpdateTime(self):
        r"""Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._MNPVersion = params.get("MNPVersion")
        self._MNPVersionId = params.get("MNPVersionId")
        self._MNPVersionNote = params.get("MNPVersionNote")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseMNPVersionRequest(AbstractModel):
    r"""ReleaseMNPVersion request structure.

    """

    def __init__(self):
        r"""
        :param _MNPVersionId: Mini program version ID
        :type MNPVersionId: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._MNPVersionId = None
        self._PlatformId = None

    @property
    def MNPVersionId(self):
        r"""Mini program version ID
        :rtype: int
        """
        return self._MNPVersionId

    @MNPVersionId.setter
    def MNPVersionId(self, MNPVersionId):
        self._MNPVersionId = MNPVersionId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._MNPVersionId = params.get("MNPVersionId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseMNPVersionResponse(AbstractModel):
    r"""ReleaseMNPVersion response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class RemoveMNPRequest(AbstractModel):
    r"""RemoveMNP request structure.

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _PlatformId: Platform ID
        :type PlatformId: str
        """
        self._MNPId = None
        self._PlatformId = None

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveMNPResponse(AbstractModel):
    r"""RemoveMNP response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ReportDataResult(AbstractModel):
    r"""General response for data query reports

    """

    def __init__(self):
        r"""
        :param _DataResult: Base64-encoded result data
        :type DataResult: str
        :param _ExecSql: Executed SQL
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExecSql: str
        :param _ExecTime: Execution time
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExecTime: int
        :param _IndexId: Query index ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type IndexId: str
        """
        self._DataResult = None
        self._ExecSql = None
        self._ExecTime = None
        self._IndexId = None

    @property
    def DataResult(self):
        r"""Base64-encoded result data
        :rtype: str
        """
        return self._DataResult

    @DataResult.setter
    def DataResult(self, DataResult):
        self._DataResult = DataResult

    @property
    def ExecSql(self):
        r"""Executed SQL
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExecSql

    @ExecSql.setter
    def ExecSql(self, ExecSql):
        self._ExecSql = ExecSql

    @property
    def ExecTime(self):
        r"""Execution time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ExecTime

    @ExecTime.setter
    def ExecTime(self, ExecTime):
        self._ExecTime = ExecTime

    @property
    def IndexId(self):
        r"""Query index ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IndexId

    @IndexId.setter
    def IndexId(self, IndexId):
        self._IndexId = IndexId


    def _deserialize(self, params):
        self._DataResult = params.get("DataResult")
        self._ExecSql = params.get("ExecSql")
        self._ExecTime = params.get("ExecTime")
        self._IndexId = params.get("IndexId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceIdInfo(AbstractModel):
    r"""Unified operation success ID - integer

    """

    def __init__(self):
        r"""
        :param _ResourceId: Specifies the resource ID returned by the business.
0: no trial version available.
A trial version is currently available and uploaded by the current user.
2: a trial version is currently available and uploaded by another user.
        :type ResourceId: int
        """
        self._ResourceId = None

    @property
    def ResourceId(self):
        r"""Specifies the resource ID returned by the business.
0: no trial version available.
A trial version is currently available and uploaded by the current user.
2: a trial version is currently available and uploaded by another user.
        :rtype: int
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceIdStringInfo(AbstractModel):
    r"""The general parameter for resource ID returned for successful operations

    """

    def __init__(self):
        r"""
        :param _ResourceId: The ID of the resource returned
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceId: str
        """
        self._ResourceId = None

    @property
    def ResourceId(self):
        r"""The ID of the resource returned
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetentionData(AbstractModel):
    r"""Retention data

    """

    def __init__(self):
        r"""
        :param _ActiveUserCount: Number of active users
        :type ActiveUserCount: int
        :param _OneDayRetentionUsers: Day 1 retention of active users
        :type OneDayRetentionUsers: int
        :param _TwoDayRetentionUsers: Day 2 retention of active users
        :type TwoDayRetentionUsers: int
        :param _ThreeDayRetentionUsers: Day 3 retention of active users
        :type ThreeDayRetentionUsers: int
        :param _FourDayRetentionUsers: Day 4 retention of active users
        :type FourDayRetentionUsers: int
        :param _FiveDayRetentionUsers: Day 5 retention of active users
        :type FiveDayRetentionUsers: int
        :param _SixDayRetentionUsers: Day 6 retention of active users
        :type SixDayRetentionUsers: int
        :param _SevenDayRetentionUsers: Day 7 retention of active users
        :type SevenDayRetentionUsers: int
        :param _FourteenDayRetentionUsers: Day 14 retention of active users
        :type FourteenDayRetentionUsers: int
        :param _ThirtyDayRetentionUsers: Day 30 retention of active users
        :type ThirtyDayRetentionUsers: int
        :param _NewUserCount: Number of new users
        :type NewUserCount: int
        :param _OneDayRetentionNewUsers: Day 1 retention of new users
        :type OneDayRetentionNewUsers: int
        :param _TwoDayRetentionNewUsers: Day 2 retention of new users
        :type TwoDayRetentionNewUsers: int
        :param _ThreeDayRetentionNewUsers: Day 3 retention of new users
        :type ThreeDayRetentionNewUsers: int
        :param _FourDayRetentionNewUsers: Day 4 retention of new users
        :type FourDayRetentionNewUsers: int
        :param _FiveDayRetentionNewUsers: Day 5 retention of new users
        :type FiveDayRetentionNewUsers: int
        :param _SixDayRetentionNewUsers: Day 6 retention of new users
        :type SixDayRetentionNewUsers: int
        :param _SevenDayRetentionNewUsers: Day 7 retention of new users
        :type SevenDayRetentionNewUsers: int
        :param _FourteenDayRetentionNewUsers: Day 14 retention of new users
        :type FourteenDayRetentionNewUsers: int
        :param _ThirtyDayRetentionNewUsers: Day 30 retention of new users
        :type ThirtyDayRetentionNewUsers: int
        :param _DataTime: Data time in YYYYMMDD format
        :type DataTime: str
        """
        self._ActiveUserCount = None
        self._OneDayRetentionUsers = None
        self._TwoDayRetentionUsers = None
        self._ThreeDayRetentionUsers = None
        self._FourDayRetentionUsers = None
        self._FiveDayRetentionUsers = None
        self._SixDayRetentionUsers = None
        self._SevenDayRetentionUsers = None
        self._FourteenDayRetentionUsers = None
        self._ThirtyDayRetentionUsers = None
        self._NewUserCount = None
        self._OneDayRetentionNewUsers = None
        self._TwoDayRetentionNewUsers = None
        self._ThreeDayRetentionNewUsers = None
        self._FourDayRetentionNewUsers = None
        self._FiveDayRetentionNewUsers = None
        self._SixDayRetentionNewUsers = None
        self._SevenDayRetentionNewUsers = None
        self._FourteenDayRetentionNewUsers = None
        self._ThirtyDayRetentionNewUsers = None
        self._DataTime = None

    @property
    def ActiveUserCount(self):
        r"""Number of active users
        :rtype: int
        """
        return self._ActiveUserCount

    @ActiveUserCount.setter
    def ActiveUserCount(self, ActiveUserCount):
        self._ActiveUserCount = ActiveUserCount

    @property
    def OneDayRetentionUsers(self):
        r"""Day 1 retention of active users
        :rtype: int
        """
        return self._OneDayRetentionUsers

    @OneDayRetentionUsers.setter
    def OneDayRetentionUsers(self, OneDayRetentionUsers):
        self._OneDayRetentionUsers = OneDayRetentionUsers

    @property
    def TwoDayRetentionUsers(self):
        r"""Day 2 retention of active users
        :rtype: int
        """
        return self._TwoDayRetentionUsers

    @TwoDayRetentionUsers.setter
    def TwoDayRetentionUsers(self, TwoDayRetentionUsers):
        self._TwoDayRetentionUsers = TwoDayRetentionUsers

    @property
    def ThreeDayRetentionUsers(self):
        r"""Day 3 retention of active users
        :rtype: int
        """
        return self._ThreeDayRetentionUsers

    @ThreeDayRetentionUsers.setter
    def ThreeDayRetentionUsers(self, ThreeDayRetentionUsers):
        self._ThreeDayRetentionUsers = ThreeDayRetentionUsers

    @property
    def FourDayRetentionUsers(self):
        r"""Day 4 retention of active users
        :rtype: int
        """
        return self._FourDayRetentionUsers

    @FourDayRetentionUsers.setter
    def FourDayRetentionUsers(self, FourDayRetentionUsers):
        self._FourDayRetentionUsers = FourDayRetentionUsers

    @property
    def FiveDayRetentionUsers(self):
        r"""Day 5 retention of active users
        :rtype: int
        """
        return self._FiveDayRetentionUsers

    @FiveDayRetentionUsers.setter
    def FiveDayRetentionUsers(self, FiveDayRetentionUsers):
        self._FiveDayRetentionUsers = FiveDayRetentionUsers

    @property
    def SixDayRetentionUsers(self):
        r"""Day 6 retention of active users
        :rtype: int
        """
        return self._SixDayRetentionUsers

    @SixDayRetentionUsers.setter
    def SixDayRetentionUsers(self, SixDayRetentionUsers):
        self._SixDayRetentionUsers = SixDayRetentionUsers

    @property
    def SevenDayRetentionUsers(self):
        r"""Day 7 retention of active users
        :rtype: int
        """
        return self._SevenDayRetentionUsers

    @SevenDayRetentionUsers.setter
    def SevenDayRetentionUsers(self, SevenDayRetentionUsers):
        self._SevenDayRetentionUsers = SevenDayRetentionUsers

    @property
    def FourteenDayRetentionUsers(self):
        r"""Day 14 retention of active users
        :rtype: int
        """
        return self._FourteenDayRetentionUsers

    @FourteenDayRetentionUsers.setter
    def FourteenDayRetentionUsers(self, FourteenDayRetentionUsers):
        self._FourteenDayRetentionUsers = FourteenDayRetentionUsers

    @property
    def ThirtyDayRetentionUsers(self):
        r"""Day 30 retention of active users
        :rtype: int
        """
        return self._ThirtyDayRetentionUsers

    @ThirtyDayRetentionUsers.setter
    def ThirtyDayRetentionUsers(self, ThirtyDayRetentionUsers):
        self._ThirtyDayRetentionUsers = ThirtyDayRetentionUsers

    @property
    def NewUserCount(self):
        r"""Number of new users
        :rtype: int
        """
        return self._NewUserCount

    @NewUserCount.setter
    def NewUserCount(self, NewUserCount):
        self._NewUserCount = NewUserCount

    @property
    def OneDayRetentionNewUsers(self):
        r"""Day 1 retention of new users
        :rtype: int
        """
        return self._OneDayRetentionNewUsers

    @OneDayRetentionNewUsers.setter
    def OneDayRetentionNewUsers(self, OneDayRetentionNewUsers):
        self._OneDayRetentionNewUsers = OneDayRetentionNewUsers

    @property
    def TwoDayRetentionNewUsers(self):
        r"""Day 2 retention of new users
        :rtype: int
        """
        return self._TwoDayRetentionNewUsers

    @TwoDayRetentionNewUsers.setter
    def TwoDayRetentionNewUsers(self, TwoDayRetentionNewUsers):
        self._TwoDayRetentionNewUsers = TwoDayRetentionNewUsers

    @property
    def ThreeDayRetentionNewUsers(self):
        r"""Day 3 retention of new users
        :rtype: int
        """
        return self._ThreeDayRetentionNewUsers

    @ThreeDayRetentionNewUsers.setter
    def ThreeDayRetentionNewUsers(self, ThreeDayRetentionNewUsers):
        self._ThreeDayRetentionNewUsers = ThreeDayRetentionNewUsers

    @property
    def FourDayRetentionNewUsers(self):
        r"""Day 4 retention of new users
        :rtype: int
        """
        return self._FourDayRetentionNewUsers

    @FourDayRetentionNewUsers.setter
    def FourDayRetentionNewUsers(self, FourDayRetentionNewUsers):
        self._FourDayRetentionNewUsers = FourDayRetentionNewUsers

    @property
    def FiveDayRetentionNewUsers(self):
        r"""Day 5 retention of new users
        :rtype: int
        """
        return self._FiveDayRetentionNewUsers

    @FiveDayRetentionNewUsers.setter
    def FiveDayRetentionNewUsers(self, FiveDayRetentionNewUsers):
        self._FiveDayRetentionNewUsers = FiveDayRetentionNewUsers

    @property
    def SixDayRetentionNewUsers(self):
        r"""Day 6 retention of new users
        :rtype: int
        """
        return self._SixDayRetentionNewUsers

    @SixDayRetentionNewUsers.setter
    def SixDayRetentionNewUsers(self, SixDayRetentionNewUsers):
        self._SixDayRetentionNewUsers = SixDayRetentionNewUsers

    @property
    def SevenDayRetentionNewUsers(self):
        r"""Day 7 retention of new users
        :rtype: int
        """
        return self._SevenDayRetentionNewUsers

    @SevenDayRetentionNewUsers.setter
    def SevenDayRetentionNewUsers(self, SevenDayRetentionNewUsers):
        self._SevenDayRetentionNewUsers = SevenDayRetentionNewUsers

    @property
    def FourteenDayRetentionNewUsers(self):
        r"""Day 14 retention of new users
        :rtype: int
        """
        return self._FourteenDayRetentionNewUsers

    @FourteenDayRetentionNewUsers.setter
    def FourteenDayRetentionNewUsers(self, FourteenDayRetentionNewUsers):
        self._FourteenDayRetentionNewUsers = FourteenDayRetentionNewUsers

    @property
    def ThirtyDayRetentionNewUsers(self):
        r"""Day 30 retention of new users
        :rtype: int
        """
        return self._ThirtyDayRetentionNewUsers

    @ThirtyDayRetentionNewUsers.setter
    def ThirtyDayRetentionNewUsers(self, ThirtyDayRetentionNewUsers):
        self._ThirtyDayRetentionNewUsers = ThirtyDayRetentionNewUsers

    @property
    def DataTime(self):
        r"""Data time in YYYYMMDD format
        :rtype: str
        """
        return self._DataTime

    @DataTime.setter
    def DataTime(self, DataTime):
        self._DataTime = DataTime


    def _deserialize(self, params):
        self._ActiveUserCount = params.get("ActiveUserCount")
        self._OneDayRetentionUsers = params.get("OneDayRetentionUsers")
        self._TwoDayRetentionUsers = params.get("TwoDayRetentionUsers")
        self._ThreeDayRetentionUsers = params.get("ThreeDayRetentionUsers")
        self._FourDayRetentionUsers = params.get("FourDayRetentionUsers")
        self._FiveDayRetentionUsers = params.get("FiveDayRetentionUsers")
        self._SixDayRetentionUsers = params.get("SixDayRetentionUsers")
        self._SevenDayRetentionUsers = params.get("SevenDayRetentionUsers")
        self._FourteenDayRetentionUsers = params.get("FourteenDayRetentionUsers")
        self._ThirtyDayRetentionUsers = params.get("ThirtyDayRetentionUsers")
        self._NewUserCount = params.get("NewUserCount")
        self._OneDayRetentionNewUsers = params.get("OneDayRetentionNewUsers")
        self._TwoDayRetentionNewUsers = params.get("TwoDayRetentionNewUsers")
        self._ThreeDayRetentionNewUsers = params.get("ThreeDayRetentionNewUsers")
        self._FourDayRetentionNewUsers = params.get("FourDayRetentionNewUsers")
        self._FiveDayRetentionNewUsers = params.get("FiveDayRetentionNewUsers")
        self._SixDayRetentionNewUsers = params.get("SixDayRetentionNewUsers")
        self._SevenDayRetentionNewUsers = params.get("SevenDayRetentionNewUsers")
        self._FourteenDayRetentionNewUsers = params.get("FourteenDayRetentionNewUsers")
        self._ThirtyDayRetentionNewUsers = params.get("ThirtyDayRetentionNewUsers")
        self._DataTime = params.get("DataTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackMNPVersionRequest(AbstractModel):
    r"""RollbackMNPVersion request structure.

    """

    def __init__(self):
        r"""
        :param _MNPId: Mini program ID
        :type MNPId: str
        :param _MNPVersionId: Mini program version ID
        :type MNPVersionId: int
        :param _PlatformId: Platform ID
        :type PlatformId: str
        :param _MNPVersion: Mini program version number
        :type MNPVersion: str
        """
        self._MNPId = None
        self._MNPVersionId = None
        self._PlatformId = None
        self._MNPVersion = None

    @property
    def MNPId(self):
        r"""Mini program ID
        :rtype: str
        """
        return self._MNPId

    @MNPId.setter
    def MNPId(self, MNPId):
        self._MNPId = MNPId

    @property
    def MNPVersionId(self):
        r"""Mini program version ID
        :rtype: int
        """
        return self._MNPVersionId

    @MNPVersionId.setter
    def MNPVersionId(self, MNPVersionId):
        self._MNPVersionId = MNPVersionId

    @property
    def PlatformId(self):
        r"""Platform ID
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId

    @property
    def MNPVersion(self):
        r"""Mini program version number
        :rtype: str
        """
        return self._MNPVersion

    @MNPVersion.setter
    def MNPVersion(self, MNPVersion):
        self._MNPVersion = MNPVersion


    def _deserialize(self, params):
        self._MNPId = params.get("MNPId")
        self._MNPVersionId = params.get("MNPVersionId")
        self._PlatformId = params.get("PlatformId")
        self._MNPVersion = params.get("MNPVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackMNPVersionResponse(AbstractModel):
    r"""RollbackMNPVersion response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response data
        :type Data: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Response data
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.BooleanInfo`
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
        if params.get("Data") is not None:
            self._Data = BooleanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class StringData(AbstractModel):
    r"""String object

    """

    def __init__(self):
        r"""
        :param _Data: string type response data.
        :type Data: str
        """
        self._Data = None

    @property
    def Data(self):
        r"""string type response data.
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFileTempSecret(AbstractModel):
    r"""Temporary key for file upload

    """

    def __init__(self):
        r"""
        :param _Bucket: Bucket
Note: This field may return null, indicating that no valid values can be obtained.
        :type Bucket: str
        :param _Region: Region
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Path: Destination of upload
Note: This field may return null, indicating that no valid values can be obtained.
        :type Path: str
        :param _TempSecretId: Temporary secret ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TempSecretId: str
        :param _TempSecretKey: Temporary secret key
Note: This field may return null, indicating that no valid values can be obtained.
        :type TempSecretKey: str
        :param _Token: Token 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Token: str
        :param _AccelerateEnable: Whether to enable global acceleration. Valid values: 0 (no), 1 (yes)
        :type AccelerateEnable: int
        """
        self._Bucket = None
        self._Region = None
        self._Path = None
        self._TempSecretId = None
        self._TempSecretKey = None
        self._Token = None
        self._AccelerateEnable = None

    @property
    def Bucket(self):
        r"""Bucket
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        r"""Region
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Path(self):
        r"""Destination of upload
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def TempSecretId(self):
        r"""Temporary secret ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TempSecretId

    @TempSecretId.setter
    def TempSecretId(self, TempSecretId):
        self._TempSecretId = TempSecretId

    @property
    def TempSecretKey(self):
        r"""Temporary secret key
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TempSecretKey

    @TempSecretKey.setter
    def TempSecretKey(self, TempSecretKey):
        self._TempSecretKey = TempSecretKey

    @property
    def Token(self):
        r"""Token 
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def AccelerateEnable(self):
        r"""Whether to enable global acceleration. Valid values: 0 (no), 1 (yes)
        :rtype: int
        """
        return self._AccelerateEnable

    @AccelerateEnable.setter
    def AccelerateEnable(self, AccelerateEnable):
        self._AccelerateEnable = AccelerateEnable


    def _deserialize(self, params):
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._Path = params.get("Path")
        self._TempSecretId = params.get("TempSecretId")
        self._TempSecretKey = params.get("TempSecretKey")
        self._Token = params.get("Token")
        self._AccelerateEnable = params.get("AccelerateEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VisitData(AbstractModel):
    r"""Page visit data

    """

    def __init__(self):
        r"""
        :param _VisitCount: Number of visits
        :type VisitCount: int
        :param _AvgDeviceVisitDeep: Average pages per device - visit_page_count / active_device_num
        :type AvgDeviceVisitDeep: str
        :param _AvgCountVisitDeep: Pages per visit - visit_page_count / miniapp_open_num
        :type AvgCountVisitDeep: str
        :param _AvgPageVisitDuration: Average visit duration - miniapp_total_duration / visit_page_count
        :type AvgPageVisitDuration: str
        :param _AvgCountVisitDuration: Average visit duration per session
miniapp_total_duration/miniapp_open_num
        :type AvgCountVisitDuration: str
        :param _DataTime: Refresh time in YYYYMMDD format
        :type DataTime: int
        """
        self._VisitCount = None
        self._AvgDeviceVisitDeep = None
        self._AvgCountVisitDeep = None
        self._AvgPageVisitDuration = None
        self._AvgCountVisitDuration = None
        self._DataTime = None

    @property
    def VisitCount(self):
        r"""Number of visits
        :rtype: int
        """
        return self._VisitCount

    @VisitCount.setter
    def VisitCount(self, VisitCount):
        self._VisitCount = VisitCount

    @property
    def AvgDeviceVisitDeep(self):
        r"""Average pages per device - visit_page_count / active_device_num
        :rtype: str
        """
        return self._AvgDeviceVisitDeep

    @AvgDeviceVisitDeep.setter
    def AvgDeviceVisitDeep(self, AvgDeviceVisitDeep):
        self._AvgDeviceVisitDeep = AvgDeviceVisitDeep

    @property
    def AvgCountVisitDeep(self):
        r"""Pages per visit - visit_page_count / miniapp_open_num
        :rtype: str
        """
        return self._AvgCountVisitDeep

    @AvgCountVisitDeep.setter
    def AvgCountVisitDeep(self, AvgCountVisitDeep):
        self._AvgCountVisitDeep = AvgCountVisitDeep

    @property
    def AvgPageVisitDuration(self):
        r"""Average visit duration - miniapp_total_duration / visit_page_count
        :rtype: str
        """
        return self._AvgPageVisitDuration

    @AvgPageVisitDuration.setter
    def AvgPageVisitDuration(self, AvgPageVisitDuration):
        self._AvgPageVisitDuration = AvgPageVisitDuration

    @property
    def AvgCountVisitDuration(self):
        r"""Average visit duration per session
miniapp_total_duration/miniapp_open_num
        :rtype: str
        """
        return self._AvgCountVisitDuration

    @AvgCountVisitDuration.setter
    def AvgCountVisitDuration(self, AvgCountVisitDuration):
        self._AvgCountVisitDuration = AvgCountVisitDuration

    @property
    def DataTime(self):
        r"""Refresh time in YYYYMMDD format
        :rtype: int
        """
        return self._DataTime

    @DataTime.setter
    def DataTime(self, DataTime):
        self._DataTime = DataTime


    def _deserialize(self, params):
        self._VisitCount = params.get("VisitCount")
        self._AvgDeviceVisitDeep = params.get("AvgDeviceVisitDeep")
        self._AvgCountVisitDeep = params.get("AvgCountVisitDeep")
        self._AvgPageVisitDuration = params.get("AvgPageVisitDuration")
        self._AvgCountVisitDuration = params.get("AvgCountVisitDuration")
        self._DataTime = params.get("DataTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        