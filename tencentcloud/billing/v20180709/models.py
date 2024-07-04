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


class ActionSummaryOverviewItem(AbstractModel):
    """Detailed summary of costs by transaction type

    """

    def __init__(self):
        r"""
        :param _ActionType: Transaction type code
        :type ActionType: str
        :param _ActionTypeName: Transaction type, which can be monthly subscription purchase, monthly subscription renewal, or pay-as-you-go deduction.
        :type ActionTypeName: str
        :param _RealTotalCostRatio: Cost ratio, to two decimal points
        :type RealTotalCostRatio: str
        :param _RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param _CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param _IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param _TransferPayAmount: Commission credit: The amount paid with the user’s commission credit. Note: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        :param _BillMonth: Billing month, e.g. `2019-08`
        :type BillMonth: str
        :param _TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        """
        self._ActionType = None
        self._ActionTypeName = None
        self._RealTotalCostRatio = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None
        self._BillMonth = None
        self._TotalCost = None

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def RealTotalCostRatio(self):
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def BillMonth(self):
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._ActionType = params.get("ActionType")
        self._ActionTypeName = params.get("ActionTypeName")
        self._RealTotalCostRatio = params.get("RealTotalCostRatio")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._BillMonth = params.get("BillMonth")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseActionTypeDetail(AbstractModel):
    """Cost analysis transaction type complex type

    """

    def __init__(self):
        r"""
        :param _ActionType: Transaction type codeNote: This field may return null, indicating that no valid values can be obtained.
        :type ActionType: str
        :param _ActionTypeName: Transaction type nameNote: This field may return null, indicating that no valid values can be obtained.
        :type ActionTypeName: str
        """
        self._ActionType = None
        self._ActionTypeName = None

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName


    def _deserialize(self, params):
        self._ActionType = params.get("ActionType")
        self._ActionTypeName = params.get("ActionTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseAmountDetail(AbstractModel):
    """Cost analysis amount return data model

    """

    def __init__(self):
        r"""
        :param _Key: Fee typeNote: This field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param _Display: Whether to displayNote: This field may return null, indicating that no valid values can be obtained.
        :type Display: int
        """
        self._Key = None
        self._Display = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Display(self):
        return self._Display

    @Display.setter
    def Display(self, Display):
        self._Display = Display


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Display = params.get("Display")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseBusinessDetail(AbstractModel):
    """Cost analysis product return complex type

    """

    def __init__(self):
        r"""
        :param _BusinessCode: Product codeNote: This field may return null, indicating that no valid values can be obtained.
        :type BusinessCode: str
        :param _BusinessCodeName: Product nameNote: This field may return null, indicating that no valid values can be obtained.
        :type BusinessCodeName: str
        """
        self._BusinessCode = None
        self._BusinessCodeName = None

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName


    def _deserialize(self, params):
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseConditionDetail(AbstractModel):
    """Cost analysis filter box complex type

    """

    def __init__(self):
        r"""
        :param _Business: ProductNote: This field may return null, indicating that no valid values can be obtained.
        :type Business: list of AnalyseBusinessDetail
        :param _Project: ItemNote: This field may return null, indicating that no valid values can be obtained.
        :type Project: list of AnalyseProjectDetail
        :param _Region: RegionNote: This field may return null, indicating that no valid values can be obtained.
        :type Region: list of AnalyseRegionDetail
        :param _PayMode: Billing modeNote: This field may return null, indicating that no valid values can be obtained.
        :type PayMode: list of AnalysePayModeDetail
        :param _ActionType: Transaction typeNote: This field may return null, indicating that no valid values can be obtained.
        :type ActionType: list of AnalyseActionTypeDetail
        :param _Zone: Availability zoneNote: This field may return null, indicating that no valid values can be obtained.
        :type Zone: list of AnalyseZoneDetail
        :param _OwnerUin: Resource owner UINNote: This field may return null, indicating that no valid values can be obtained.
        :type OwnerUin: list of AnalyseOwnerUinDetail
        :param _Amount: Fee typeNote: This field may return null, indicating that no valid values can be obtained.
        :type Amount: list of AnalyseAmountDetail
        """
        self._Business = None
        self._Project = None
        self._Region = None
        self._PayMode = None
        self._ActionType = None
        self._Zone = None
        self._OwnerUin = None
        self._Amount = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Project(self):
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Amount(self):
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount


    def _deserialize(self, params):
        if params.get("Business") is not None:
            self._Business = []
            for item in params.get("Business"):
                obj = AnalyseBusinessDetail()
                obj._deserialize(item)
                self._Business.append(obj)
        if params.get("Project") is not None:
            self._Project = []
            for item in params.get("Project"):
                obj = AnalyseProjectDetail()
                obj._deserialize(item)
                self._Project.append(obj)
        if params.get("Region") is not None:
            self._Region = []
            for item in params.get("Region"):
                obj = AnalyseRegionDetail()
                obj._deserialize(item)
                self._Region.append(obj)
        if params.get("PayMode") is not None:
            self._PayMode = []
            for item in params.get("PayMode"):
                obj = AnalysePayModeDetail()
                obj._deserialize(item)
                self._PayMode.append(obj)
        if params.get("ActionType") is not None:
            self._ActionType = []
            for item in params.get("ActionType"):
                obj = AnalyseActionTypeDetail()
                obj._deserialize(item)
                self._ActionType.append(obj)
        if params.get("Zone") is not None:
            self._Zone = []
            for item in params.get("Zone"):
                obj = AnalyseZoneDetail()
                obj._deserialize(item)
                self._Zone.append(obj)
        if params.get("OwnerUin") is not None:
            self._OwnerUin = []
            for item in params.get("OwnerUin"):
                obj = AnalyseOwnerUinDetail()
                obj._deserialize(item)
                self._OwnerUin.append(obj)
        if params.get("Amount") is not None:
            self._Amount = []
            for item in params.get("Amount"):
                obj = AnalyseAmountDetail()
                obj._deserialize(item)
                self._Amount.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseConditions(AbstractModel):
    """Cost analysis query conditions

    """

    def __init__(self):
        r"""
        :param _BusinessCodes: Product name codeNote: This field may return null, indicating that no valid values can be obtained.
        :type BusinessCodes: str
        :param _ProductCodes: Sub-product name codeNote: This field may return null, indicating that no valid values can be obtained.
        :type ProductCodes: str
        :param _ComponentCode: Component type codeNote: This field may return null, indicating that no valid values can be obtained.
        :type ComponentCode: str
        :param _ZoneIds: Availability zone ID: The availability zone ID to which the resource belongsNote: This field may return null, indicating that no valid values can be obtained.
        :type ZoneIds: str
        :param _RegionIds: Region ID: The region ID to which the resource belongsNote: This field may return null, indicating that no valid values can be obtained.
        :type RegionIds: str
        :param _ProjectIds: Project ID: The project ID to which the resource belongsNote: This field may return null, indicating that no valid values can be obtained.
        :type ProjectIds: str
        :param _PayModes: Billing mode prePay (indicates monthly subscription)/postPay (indicates pay-as-you-go billing)Note: This field may return null, indicating that no valid values can be obtained.
        :type PayModes: str
        :param _ActionTypes: Transaction type. Query transaction type. (Use transaction type code input parameter.)Note: This field may return null, indicating that no valid values can be obtained.
        :type ActionTypes: str
        :param _Tags: Cost allocation tag keyNote: This field may return null, indicating that no valid values can be obtained.
        :type Tags: str
        :param _FeeType: Fee type. Query fee type. (Use fee type code input parameter.) The input parameter enumeration is as follows:cashPayAmount: cash incentivePayAmount: free credits voucherPayAmount: coupons tax:taxes costBeforeTax: price before taxNote: This field may return null, indicating that no valid values can be obtained.
        :type FeeType: str
        :param _PayerUins: User UIN for querying cost analysis dataNote: This field may return null, indicating that no valid values can be obtained.
        :type PayerUins: str
        :param _OwnerUins: User UIN for using resourcesNote: This field may return null, indicating that no valid values can be obtained.
        :type OwnerUins: str
        :param _ConsumptionTypes: Consumption type. Query consumption type. (Use consumption type code input parameter.)Note: This field may return null, indicating that no valid values can be obtained.
        :type ConsumptionTypes: str
        """
        self._BusinessCodes = None
        self._ProductCodes = None
        self._ComponentCode = None
        self._ZoneIds = None
        self._RegionIds = None
        self._ProjectIds = None
        self._PayModes = None
        self._ActionTypes = None
        self._Tags = None
        self._FeeType = None
        self._PayerUins = None
        self._OwnerUins = None
        self._ConsumptionTypes = None

    @property
    def BusinessCodes(self):
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def ProductCodes(self):
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes

    @property
    def ComponentCode(self):
        return self._ComponentCode

    @ComponentCode.setter
    def ComponentCode(self, ComponentCode):
        self._ComponentCode = ComponentCode

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def RegionIds(self):
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def PayModes(self):
        return self._PayModes

    @PayModes.setter
    def PayModes(self, PayModes):
        self._PayModes = PayModes

    @property
    def ActionTypes(self):
        return self._ActionTypes

    @ActionTypes.setter
    def ActionTypes(self, ActionTypes):
        self._ActionTypes = ActionTypes

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def FeeType(self):
        return self._FeeType

    @FeeType.setter
    def FeeType(self, FeeType):
        self._FeeType = FeeType

    @property
    def PayerUins(self):
        return self._PayerUins

    @PayerUins.setter
    def PayerUins(self, PayerUins):
        self._PayerUins = PayerUins

    @property
    def OwnerUins(self):
        return self._OwnerUins

    @OwnerUins.setter
    def OwnerUins(self, OwnerUins):
        self._OwnerUins = OwnerUins

    @property
    def ConsumptionTypes(self):
        return self._ConsumptionTypes

    @ConsumptionTypes.setter
    def ConsumptionTypes(self, ConsumptionTypes):
        self._ConsumptionTypes = ConsumptionTypes


    def _deserialize(self, params):
        self._BusinessCodes = params.get("BusinessCodes")
        self._ProductCodes = params.get("ProductCodes")
        self._ComponentCode = params.get("ComponentCode")
        self._ZoneIds = params.get("ZoneIds")
        self._RegionIds = params.get("RegionIds")
        self._ProjectIds = params.get("ProjectIds")
        self._PayModes = params.get("PayModes")
        self._ActionTypes = params.get("ActionTypes")
        self._Tags = params.get("Tags")
        self._FeeType = params.get("FeeType")
        self._PayerUins = params.get("PayerUins")
        self._OwnerUins = params.get("OwnerUins")
        self._ConsumptionTypes = params.get("ConsumptionTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseDetail(AbstractModel):
    """Cost analysis data complex type

    """

    def __init__(self):
        r"""
        :param _Name: Time
        :type Name: str
        :param _Total: Amount
        :type Total: str
        :param _TimeDetail: Date detailed amountNote: This field may return null, indicating that no valid values can be obtained.
        :type TimeDetail: list of AnalyseTimeDetail
        """
        self._Name = None
        self._Total = None
        self._TimeDetail = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TimeDetail(self):
        return self._TimeDetail

    @TimeDetail.setter
    def TimeDetail(self, TimeDetail):
        self._TimeDetail = TimeDetail


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Total = params.get("Total")
        if params.get("TimeDetail") is not None:
            self._TimeDetail = []
            for item in params.get("TimeDetail"):
                obj = AnalyseTimeDetail()
                obj._deserialize(item)
                self._TimeDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseHeaderDetail(AbstractModel):
    """Cost analysis header data complex type

    """

    def __init__(self):
        r"""
        :param _HeadDetail: Header dateNote: This field may return null, indicating that no valid values can be obtained.
        :type HeadDetail: list of AnalyseHeaderTimeDetail
        :param _Name: TimeNote: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Total: TotalNote: This field may return null, indicating that no valid values can be obtained.
        :type Total: str
        """
        self._HeadDetail = None
        self._Name = None
        self._Total = None

    @property
    def HeadDetail(self):
        return self._HeadDetail

    @HeadDetail.setter
    def HeadDetail(self, HeadDetail):
        self._HeadDetail = HeadDetail

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        if params.get("HeadDetail") is not None:
            self._HeadDetail = []
            for item in params.get("HeadDetail"):
                obj = AnalyseHeaderTimeDetail()
                obj._deserialize(item)
                self._HeadDetail.append(obj)
        self._Name = params.get("Name")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseHeaderTimeDetail(AbstractModel):
    """Cost analysis header data

    """

    def __init__(self):
        r"""
        :param _Name: DateNote: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseOwnerUinDetail(AbstractModel):
    """Cost analysis user UIN complex type

    """

    def __init__(self):
        r"""
        :param _OwnerUin: User UIN
Note: This field may return null, indicating that no valid values can be obtained.
        :type OwnerUin: str
        """
        self._OwnerUin = None

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalysePayModeDetail(AbstractModel):
    """Cost analysis payment method complex type

    """

    def __init__(self):
        r"""
        :param _PayMode: Billing mode codeNote: This field may return null, indicating that no valid values can be obtained.
        :type PayMode: str
        :param _PayModeName: Billing mode nameNote: This field may return null, indicating that no valid values can be obtained.
        :type PayModeName: str
        """
        self._PayMode = None
        self._PayModeName = None

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName


    def _deserialize(self, params):
        self._PayMode = params.get("PayMode")
        self._PayModeName = params.get("PayModeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseProjectDetail(AbstractModel):
    """Cost analysis project return complex type

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectId: str
        :param _ProjectName: Default projectNote: This field may return null, indicating that no valid values can be obtained.
        :type ProjectName: str
        """
        self._ProjectId = None
        self._ProjectName = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseRegionDetail(AbstractModel):
    """Cost analysis region return complex type

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionId: str
        :param _RegionName: Region nameNote: This field may return null, indicating that no valid values can be obtained.
        :type RegionName: str
        """
        self._RegionId = None
        self._RegionName = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseTimeDetail(AbstractModel):
    """Cost analysis return value complex type

    """

    def __init__(self):
        r"""
        :param _Time: DateNote: This field may return null, indicating that no valid values can be obtained.
        :type Time: str
        :param _Money: AmountNote: This field may return null, indicating that no valid values can be obtained.
        :type Money: str
        """
        self._Time = None
        self._Money = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Money(self):
        return self._Money

    @Money.setter
    def Money(self, Money):
        self._Money = Money


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Money = params.get("Money")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseZoneDetail(AbstractModel):
    """Cost analysis availability zone complex type

    """

    def __init__(self):
        r"""
        :param _ZoneId: Availability zone IDNote: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: str
        :param _ZoneName: Availability zone nameNote: This field may return null, indicating that no valid values can be obtained.
        :type ZoneName: str
        """
        self._ZoneId = None
        self._ZoneName = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicableProducts(AbstractModel):
    """The products that are applicable.

    """

    def __init__(self):
        r"""
        :param _GoodsName: Valid values: `all products` or names of the applicable products (string). Multiple names are separated by commas.
        :type GoodsName: str
        :param _PayMode: Valid values: `postPay`: pay-as-you-go; `prePay`: prepaid; `riPay`: reserved instance; empty or `*`: all. If `GoodsName` contains multiple product names and `PayMode` is `*`, it indicates that the voucher can be used in all billing modes for each of the products.
        :type PayMode: str
        """
        self._GoodsName = None
        self._PayMode = None

    @property
    def GoodsName(self):
        return self._GoodsName

    @GoodsName.setter
    def GoodsName(self, GoodsName):
        self._GoodsName = GoodsName

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._GoodsName = params.get("GoodsName")
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDetail(AbstractModel):
    """Bill details

    """

    def __init__(self):
        r"""
        :param _BusinessCodeName: Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :type BusinessCodeName: str
        :param _ProductCodeName: Subproduct name: The subcategory of a Tencent Cloud product purchased by the user, such as CVM – Standard S1.
        :type ProductCodeName: str
        :param _PayModeName: Billing mode, which can be monthly subscription or pay-as-you-go.
        :type PayModeName: str
        :param _ProjectName: Project name: The project to which a resource belongs, which is user-designated. If a resource has not been assigned to a project, it will automatically belong to the default project.
        :type ProjectName: str
        :param _RegionName: Region: The region to which a resource belongs, such as South China (Guangzhou).
        :type RegionName: str
        :param _ZoneName: Availability zone: availability zone of a resource, e.g. Guangzhou Zone 3
        :type ZoneName: str
        :param _ResourceId: Instance ID: The object ID of a billed resource, such as a CVM instance ID. This object ID may vary due to various forms and contents of resources in different products.
        :type ResourceId: str
        :param _ResourceName: Instance name: The resource name set by the user in the console. If it is not set, it will be empty by default.
        :type ResourceName: str
        :param _ActionTypeName: Transaction type, which can be monthly subscription purchase, monthly subscription renewal, or pay-as-you-go deduction.
        :type ActionTypeName: str
        :param _OrderId: Order ID: The order number for a monthly subscription purchase
        :type OrderId: str
        :param _BillId: Transaction ID: The bill number for a deducted payment
        :type BillId: str
        :param _PayTime: Transaction time: The time at which a payment was deducted
        :type PayTime: str
        :param _FeeBeginTime: Usage start time: The time at which product or service usage starts
        :type FeeBeginTime: str
        :param _FeeEndTime: Usage end time: The time at which product or service usage ends
        :type FeeEndTime: str
        :param _ComponentSet: Component list
        :type ComponentSet: list of BillDetailComponent
        :param _PayerUin: Payer account ID: The account ID of the payer, which is the unique identifier of a Tencent Cloud user.
        :type PayerUin: str
        :param _OwnerUin: Owner account ID: The account ID of the actual resource user
        :type OwnerUin: str
        :param _OperateUin: Operator account ID: The account or role ID of the operator who purchases or activates a resource
        :type OperateUin: str
        :param _Tags: Tag information. Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of BillTagInfo
        :param _BusinessCode: Product code. Note: This field may return null, indicating that no valid values can be obtained.
        :type BusinessCode: str
        :param _ProductCode: Subproduct code. Note: This field may return null, indicating that no valid values can be obtained.
        :type ProductCode: str
        :param _ActionType: Transaction type code. Note: This field may return null, indicating that no valid values can be obtained.
        :type ActionType: str
        :param _RegionId: Region ID. Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionId: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _PriceInfo: Price attribute: A set of attributes which will determine the price of a component, apart from unit price and usage duration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PriceInfo: list of str
        :param _AssociatedOrder: Associated transaction document ID: The ID of the document associated with a transaction, such as a write-off order, the original order showing a deduction error during first settlement, a restructured order, or the original purchase order corresponding to a refund order.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AssociatedOrder: :class:`tencentcloud.billing.v20180709.models.BillDetailAssociatedOrder`
        :param _Formula: Calculation formula: The detailed calculation formula for a specific transaction type, such as refund or configuration change.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Formula: str
        :param _FormulaUrl: Billing rules: Official website links for detailed billing rules of each product.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FormulaUrl: str
        :param _BillDay: Billing dayNote: This field may return null, indicating that no valid values can be obtained.
        :type BillDay: str
        :param _BillMonth: Billing monthNote: This field may return null, indicating that no valid values can be obtained.
        :type BillMonth: str
        :param _Id: Billing record IDNote: This field may return null, indicating that no valid values can be obtained.
        :type Id: str
        :param _RegionType: Domestic and international codesNote: This field may return null, indicating that no valid values can be obtained.
        :type RegionType: str
        :param _RegionTypeName: Domestic and International: The region type to which the resource belongs (domestic, international)Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionTypeName: str
        :param _ReserveDetail: Note attributes (instance configuration): Other note information, such as the reserved instance, the reserved instance type, the transaction type, and the region information on both ends of the CCN product.Note: This field may return null, indicating that no valid values can be obtained.
        :type ReserveDetail: str
        """
        self._BusinessCodeName = None
        self._ProductCodeName = None
        self._PayModeName = None
        self._ProjectName = None
        self._RegionName = None
        self._ZoneName = None
        self._ResourceId = None
        self._ResourceName = None
        self._ActionTypeName = None
        self._OrderId = None
        self._BillId = None
        self._PayTime = None
        self._FeeBeginTime = None
        self._FeeEndTime = None
        self._ComponentSet = None
        self._PayerUin = None
        self._OwnerUin = None
        self._OperateUin = None
        self._Tags = None
        self._BusinessCode = None
        self._ProductCode = None
        self._ActionType = None
        self._RegionId = None
        self._ProjectId = None
        self._PriceInfo = None
        self._AssociatedOrder = None
        self._Formula = None
        self._FormulaUrl = None
        self._BillDay = None
        self._BillMonth = None
        self._Id = None
        self._RegionType = None
        self._RegionTypeName = None
        self._ReserveDetail = None

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def BillId(self):
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def PayTime(self):
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def FeeBeginTime(self):
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ComponentSet(self):
        return self._ComponentSet

    @ComponentSet.setter
    def ComponentSet(self, ComponentSet):
        self._ComponentSet = ComponentSet

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PriceInfo(self):
        return self._PriceInfo

    @PriceInfo.setter
    def PriceInfo(self, PriceInfo):
        self._PriceInfo = PriceInfo

    @property
    def AssociatedOrder(self):
        return self._AssociatedOrder

    @AssociatedOrder.setter
    def AssociatedOrder(self, AssociatedOrder):
        self._AssociatedOrder = AssociatedOrder

    @property
    def Formula(self):
        return self._Formula

    @Formula.setter
    def Formula(self, Formula):
        self._Formula = Formula

    @property
    def FormulaUrl(self):
        return self._FormulaUrl

    @FormulaUrl.setter
    def FormulaUrl(self, FormulaUrl):
        self._FormulaUrl = FormulaUrl

    @property
    def BillDay(self):
        return self._BillDay

    @BillDay.setter
    def BillDay(self, BillDay):
        self._BillDay = BillDay

    @property
    def BillMonth(self):
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RegionType(self):
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def RegionTypeName(self):
        return self._RegionTypeName

    @RegionTypeName.setter
    def RegionTypeName(self, RegionTypeName):
        self._RegionTypeName = RegionTypeName

    @property
    def ReserveDetail(self):
        return self._ReserveDetail

    @ReserveDetail.setter
    def ReserveDetail(self, ReserveDetail):
        self._ReserveDetail = ReserveDetail


    def _deserialize(self, params):
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._ProductCodeName = params.get("ProductCodeName")
        self._PayModeName = params.get("PayModeName")
        self._ProjectName = params.get("ProjectName")
        self._RegionName = params.get("RegionName")
        self._ZoneName = params.get("ZoneName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._ActionTypeName = params.get("ActionTypeName")
        self._OrderId = params.get("OrderId")
        self._BillId = params.get("BillId")
        self._PayTime = params.get("PayTime")
        self._FeeBeginTime = params.get("FeeBeginTime")
        self._FeeEndTime = params.get("FeeEndTime")
        if params.get("ComponentSet") is not None:
            self._ComponentSet = []
            for item in params.get("ComponentSet"):
                obj = BillDetailComponent()
                obj._deserialize(item)
                self._ComponentSet.append(obj)
        self._PayerUin = params.get("PayerUin")
        self._OwnerUin = params.get("OwnerUin")
        self._OperateUin = params.get("OperateUin")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = BillTagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._BusinessCode = params.get("BusinessCode")
        self._ProductCode = params.get("ProductCode")
        self._ActionType = params.get("ActionType")
        self._RegionId = params.get("RegionId")
        self._ProjectId = params.get("ProjectId")
        self._PriceInfo = params.get("PriceInfo")
        if params.get("AssociatedOrder") is not None:
            self._AssociatedOrder = BillDetailAssociatedOrder()
            self._AssociatedOrder._deserialize(params.get("AssociatedOrder"))
        self._Formula = params.get("Formula")
        self._FormulaUrl = params.get("FormulaUrl")
        self._BillDay = params.get("BillDay")
        self._BillMonth = params.get("BillMonth")
        self._Id = params.get("Id")
        self._RegionType = params.get("RegionType")
        self._RegionTypeName = params.get("RegionTypeName")
        self._ReserveDetail = params.get("ReserveDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDetailAssociatedOrder(AbstractModel):
    """Information of the document associated with bill details

    """

    def __init__(self):
        r"""
        :param _PrepayPurchase: Purchase order.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrepayPurchase: str
        :param _PrepayRenew: Renewal order.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrepayRenew: str
        :param _PrepayModifyUp: Upgrade order.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrepayModifyUp: str
        :param _ReverseOrder: Write-off order.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReverseOrder: str
        :param _NewOrder: The order after discount.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewOrder: str
        :param _Original: The original order before discount.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Original: str
        """
        self._PrepayPurchase = None
        self._PrepayRenew = None
        self._PrepayModifyUp = None
        self._ReverseOrder = None
        self._NewOrder = None
        self._Original = None

    @property
    def PrepayPurchase(self):
        return self._PrepayPurchase

    @PrepayPurchase.setter
    def PrepayPurchase(self, PrepayPurchase):
        self._PrepayPurchase = PrepayPurchase

    @property
    def PrepayRenew(self):
        return self._PrepayRenew

    @PrepayRenew.setter
    def PrepayRenew(self, PrepayRenew):
        self._PrepayRenew = PrepayRenew

    @property
    def PrepayModifyUp(self):
        return self._PrepayModifyUp

    @PrepayModifyUp.setter
    def PrepayModifyUp(self, PrepayModifyUp):
        self._PrepayModifyUp = PrepayModifyUp

    @property
    def ReverseOrder(self):
        return self._ReverseOrder

    @ReverseOrder.setter
    def ReverseOrder(self, ReverseOrder):
        self._ReverseOrder = ReverseOrder

    @property
    def NewOrder(self):
        return self._NewOrder

    @NewOrder.setter
    def NewOrder(self, NewOrder):
        self._NewOrder = NewOrder

    @property
    def Original(self):
        return self._Original

    @Original.setter
    def Original(self, Original):
        self._Original = Original


    def _deserialize(self, params):
        self._PrepayPurchase = params.get("PrepayPurchase")
        self._PrepayRenew = params.get("PrepayRenew")
        self._PrepayModifyUp = params.get("PrepayModifyUp")
        self._ReverseOrder = params.get("ReverseOrder")
        self._NewOrder = params.get("NewOrder")
        self._Original = params.get("Original")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDetailComponent(AbstractModel):
    """Information about components charged in the bill

    """

    def __init__(self):
        r"""
        :param _ComponentCodeName: Component type: The component type of a product or service purchased, such as CVM instance components including CPU and memory.
        :type ComponentCodeName: str
        :param _ItemCodeName: Component name: The specific component of a product or service purchased
        :type ItemCodeName: str
        :param _SinglePrice: Component list price: The listed unit price of a component. If a customer has applied for a fixed preferential price or contract price, this parameter will not be displayed by default.
        :type SinglePrice: str
        :param _SpecifiedPrice: Specified price of a component. This parameter has been deprecated.
        :type SpecifiedPrice: str
        :param _PriceUnit: Component price measurement unit: The unit of measurement for a component price, which is composed of USD, usage unit, and duration unit.
        :type PriceUnit: str
        :param _UsedAmount: Component usage: The actually settled usage of a component, which is "Raw usage - Deducted usage (including packages)".
        :type UsedAmount: str
        :param _UsedAmountUnit: Component usage unit: The unit of measurement for component usage
        :type UsedAmountUnit: str
        :param _RealTotalMeasure: Raw usage/duration: The raw usage/duration of a component before deduction. Note: This field may return null, indicating that no valid values can be obtained.
        :type RealTotalMeasure: str
        :param _DeductedMeasure: Deducted usage/duration (including packages): The usage/duration deducted with a package. Note: This field may return null, indicating that no valid values can be obtained.
        :type DeductedMeasure: str
        :param _TimeSpan: Usage duration: The resource usage duration
        :type TimeSpan: str
        :param _TimeUnitName: Duration unit: The unit of measurement for usage duration
        :type TimeUnitName: str
        :param _Cost: Original cost: The original cost of a resource, which is "List price x Usage x Usage duration". If a customer has applied for a fixed preferential price or contract price or is in a refund scenario, this parameter will not be displayed by default.
        :type Cost: str
        :param _Discount: Discount multiplier: The discount multiplier applied to the cost of the resource. If a customer has applied for a fixed preferential price or contract price or is in a refund scenario, this parameter will not be displayed by default.
        :type Discount: str
        :param _ReduceType: Offer type
        :type ReduceType: str
        :param _RealCost: Total amount after discount: Total amount after discount = (Original cost - RI deduction (cost) - SP deduction (cost)) x Discount multiplier
        :type RealCost: str
        :param _VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param _CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param _IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param _TransferPayAmount: Commission credit: The amount paid with the user’s commission credit. Note: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        :param _ItemCode: Component type code. Note: This field may return null, indicating that no valid values can be obtained.
        :type ItemCode: str
        :param _ComponentCode: Component name code. Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentCode: str
        :param _ContractPrice: Component contracted price: The contracted unit price of a component, which is "List price x Discount". Note: This field may return null, indicating that no valid values can be obtained.
        :type ContractPrice: str
        :param _InstanceType: Instance type: The instance type of a product or service purchased, which can be resource package, RI, SP, or spot instance. Other instance types are not displayed by default. Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param _RiTimeSpan: RI deduction (duration): The usage duration deducted by RI. Note: This field may return null, indicating that no valid values can be obtained.
        :type RiTimeSpan: str
        :param _OriginalCostWithRI: RI deduction (cost): The amount deducted from the original cost by RI. Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalCostWithRI: str
        :param _SPDeductionRate: Savings plan deduction rate: The discount multiplier that applies to the component based on the remaining commitment of the savings plan. Note: This field may return null, indicating that no valid values can be obtained.
        :type SPDeductionRate: str
        :param _SPDeduction: Cost deduction by SP. This parameter has been deprecated. Note: This field may return null, indicating that no valid values can be obtained.
        :type SPDeduction: str
        :param _OriginalCostWithSP: SP deduction (cost): SP deduction (cost) = Cost deduction by SP / SP deduction rate. Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalCostWithSP: str
        :param _BlendedDiscount: Blended discount multiplier: The final discount multiplier that is applied after combining multiple discount types, which is "Total amount after discount / Original cost". Note: This field may return null, indicating that no valid values can be obtained.
        :type BlendedDiscount: str
        :param _ComponentConfig: Configuration description: The specification configuration of an instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentConfig: list of BillDetailComponentConfig
        """
        self._ComponentCodeName = None
        self._ItemCodeName = None
        self._SinglePrice = None
        self._SpecifiedPrice = None
        self._PriceUnit = None
        self._UsedAmount = None
        self._UsedAmountUnit = None
        self._RealTotalMeasure = None
        self._DeductedMeasure = None
        self._TimeSpan = None
        self._TimeUnitName = None
        self._Cost = None
        self._Discount = None
        self._ReduceType = None
        self._RealCost = None
        self._VoucherPayAmount = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None
        self._ItemCode = None
        self._ComponentCode = None
        self._ContractPrice = None
        self._InstanceType = None
        self._RiTimeSpan = None
        self._OriginalCostWithRI = None
        self._SPDeductionRate = None
        self._SPDeduction = None
        self._OriginalCostWithSP = None
        self._BlendedDiscount = None
        self._ComponentConfig = None

    @property
    def ComponentCodeName(self):
        return self._ComponentCodeName

    @ComponentCodeName.setter
    def ComponentCodeName(self, ComponentCodeName):
        self._ComponentCodeName = ComponentCodeName

    @property
    def ItemCodeName(self):
        return self._ItemCodeName

    @ItemCodeName.setter
    def ItemCodeName(self, ItemCodeName):
        self._ItemCodeName = ItemCodeName

    @property
    def SinglePrice(self):
        return self._SinglePrice

    @SinglePrice.setter
    def SinglePrice(self, SinglePrice):
        self._SinglePrice = SinglePrice

    @property
    def SpecifiedPrice(self):
        warnings.warn("parameter `SpecifiedPrice` is deprecated", DeprecationWarning) 

        return self._SpecifiedPrice

    @SpecifiedPrice.setter
    def SpecifiedPrice(self, SpecifiedPrice):
        warnings.warn("parameter `SpecifiedPrice` is deprecated", DeprecationWarning) 

        self._SpecifiedPrice = SpecifiedPrice

    @property
    def PriceUnit(self):
        return self._PriceUnit

    @PriceUnit.setter
    def PriceUnit(self, PriceUnit):
        self._PriceUnit = PriceUnit

    @property
    def UsedAmount(self):
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

    @property
    def UsedAmountUnit(self):
        return self._UsedAmountUnit

    @UsedAmountUnit.setter
    def UsedAmountUnit(self, UsedAmountUnit):
        self._UsedAmountUnit = UsedAmountUnit

    @property
    def RealTotalMeasure(self):
        return self._RealTotalMeasure

    @RealTotalMeasure.setter
    def RealTotalMeasure(self, RealTotalMeasure):
        self._RealTotalMeasure = RealTotalMeasure

    @property
    def DeductedMeasure(self):
        return self._DeductedMeasure

    @DeductedMeasure.setter
    def DeductedMeasure(self, DeductedMeasure):
        self._DeductedMeasure = DeductedMeasure

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnitName(self):
        return self._TimeUnitName

    @TimeUnitName.setter
    def TimeUnitName(self, TimeUnitName):
        self._TimeUnitName = TimeUnitName

    @property
    def Cost(self):
        return self._Cost

    @Cost.setter
    def Cost(self, Cost):
        self._Cost = Cost

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def ReduceType(self):
        return self._ReduceType

    @ReduceType.setter
    def ReduceType(self, ReduceType):
        self._ReduceType = ReduceType

    @property
    def RealCost(self):
        return self._RealCost

    @RealCost.setter
    def RealCost(self, RealCost):
        self._RealCost = RealCost

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def ItemCode(self):
        return self._ItemCode

    @ItemCode.setter
    def ItemCode(self, ItemCode):
        self._ItemCode = ItemCode

    @property
    def ComponentCode(self):
        return self._ComponentCode

    @ComponentCode.setter
    def ComponentCode(self, ComponentCode):
        self._ComponentCode = ComponentCode

    @property
    def ContractPrice(self):
        return self._ContractPrice

    @ContractPrice.setter
    def ContractPrice(self, ContractPrice):
        self._ContractPrice = ContractPrice

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def RiTimeSpan(self):
        return self._RiTimeSpan

    @RiTimeSpan.setter
    def RiTimeSpan(self, RiTimeSpan):
        self._RiTimeSpan = RiTimeSpan

    @property
    def OriginalCostWithRI(self):
        return self._OriginalCostWithRI

    @OriginalCostWithRI.setter
    def OriginalCostWithRI(self, OriginalCostWithRI):
        self._OriginalCostWithRI = OriginalCostWithRI

    @property
    def SPDeductionRate(self):
        return self._SPDeductionRate

    @SPDeductionRate.setter
    def SPDeductionRate(self, SPDeductionRate):
        self._SPDeductionRate = SPDeductionRate

    @property
    def SPDeduction(self):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        return self._SPDeduction

    @SPDeduction.setter
    def SPDeduction(self, SPDeduction):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        self._SPDeduction = SPDeduction

    @property
    def OriginalCostWithSP(self):
        return self._OriginalCostWithSP

    @OriginalCostWithSP.setter
    def OriginalCostWithSP(self, OriginalCostWithSP):
        self._OriginalCostWithSP = OriginalCostWithSP

    @property
    def BlendedDiscount(self):
        return self._BlendedDiscount

    @BlendedDiscount.setter
    def BlendedDiscount(self, BlendedDiscount):
        self._BlendedDiscount = BlendedDiscount

    @property
    def ComponentConfig(self):
        return self._ComponentConfig

    @ComponentConfig.setter
    def ComponentConfig(self, ComponentConfig):
        self._ComponentConfig = ComponentConfig


    def _deserialize(self, params):
        self._ComponentCodeName = params.get("ComponentCodeName")
        self._ItemCodeName = params.get("ItemCodeName")
        self._SinglePrice = params.get("SinglePrice")
        self._SpecifiedPrice = params.get("SpecifiedPrice")
        self._PriceUnit = params.get("PriceUnit")
        self._UsedAmount = params.get("UsedAmount")
        self._UsedAmountUnit = params.get("UsedAmountUnit")
        self._RealTotalMeasure = params.get("RealTotalMeasure")
        self._DeductedMeasure = params.get("DeductedMeasure")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnitName = params.get("TimeUnitName")
        self._Cost = params.get("Cost")
        self._Discount = params.get("Discount")
        self._ReduceType = params.get("ReduceType")
        self._RealCost = params.get("RealCost")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._ItemCode = params.get("ItemCode")
        self._ComponentCode = params.get("ComponentCode")
        self._ContractPrice = params.get("ContractPrice")
        self._InstanceType = params.get("InstanceType")
        self._RiTimeSpan = params.get("RiTimeSpan")
        self._OriginalCostWithRI = params.get("OriginalCostWithRI")
        self._SPDeductionRate = params.get("SPDeductionRate")
        self._SPDeduction = params.get("SPDeduction")
        self._OriginalCostWithSP = params.get("OriginalCostWithSP")
        self._BlendedDiscount = params.get("BlendedDiscount")
        if params.get("ComponentConfig") is not None:
            self._ComponentConfig = []
            for item in params.get("ComponentConfig"):
                obj = BillDetailComponentConfig()
                obj._deserialize(item)
                self._ComponentConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDetailComponentConfig(AbstractModel):
    """Bill details configuration descriptions

    """

    def __init__(self):
        r"""
        :param _Name: Configuration description name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Value: Configuration description value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
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
        


class BillDistributionResourceSummary(AbstractModel):
    """Summary objects for a reseller bill

    """

    def __init__(self):
        r"""
        :param _BusinessCodeName: Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :type BusinessCodeName: str
        :param _ProductCodeName: Subproduct name: The subcategory of a Tencent Cloud product purchased by the user, such as CVM - Standard S1.
        :type ProductCodeName: str
        :param _PayModeName: Billing mode: The billing mode, which can be monthly subscription or pay-as-you-go.
        :type PayModeName: str
        :param _ProjectName: Project Name: The project to which a resource belongs, which is user-designated. If a resource has not been assigned to a project, it will automatically belong to the default project.
        :type ProjectName: str
        :param _RegionName: Region: The region of a resource, e.g. South China (Guangzhou).
        :type RegionName: str
        :param _ZoneName: Availability zone: The availability zone of a resource, e.g. Guangzhou Zone 3.
        :type ZoneName: str
        :param _ResourceId: Instance ID: The object ID of a billed resource, such as a CVM instance ID. This object ID may vary due to various forms and contents of resources in different products.	
        :type ResourceId: str
        :param _ResourceName: Instance name: The resource name set by the user in the console. If it is not set, it will be empty by default.
        :type ResourceName: str
        :param _ActionTypeName: Transaction type, which can be monthly subscription purchase, monthly subscription renewal, pay-as-you-go deduction, etc.
        :type ActionTypeName: str
        :param _OrderId: Order ID: The ID of a monthly subscription order.
        :type OrderId: str
        :param _PayTime: Deduction time: The settlement cost deduction time.
        :type PayTime: str
        :param _FeeBeginTime: Usage start time: The time at which product or service usage starts.
        :type FeeBeginTime: str
        :param _FeeEndTime: Usage end time: The time at which product or service usage ends.
        :type FeeEndTime: str
        :param _ConfigDesc: Configuration description: The billable item names and usage of a resource, which are displayed on the resource bill only.
        :type ConfigDesc: str
        :param _ExtendField1: Extended Field 1: The extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField1: str
        :param _ExtendField2: Extended field 2: The extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField2: str
        :param _TotalCost: Original cost. The original cost of a component = Component price x Usage x Usage duration. If a customer has applied for a fixed preferential price or contract price or if a customer is in a refund scenario, this parameter will not be displayed by default.
        :type TotalCost: str
        :param _Discount: Discount multiplier: The discount multiplier that applies to the component. If a customer has applied for a fixed preferential price or contract price or if a customer is in a refund scenario, this parameter will not be displayed by default.
        :type Discount: str
        :param _ReduceType: Offer type.
        :type ReduceType: str
        :param _RealTotalCost: Total amount after discount.
        :type RealTotalCost: str
        :param _VoucherPayAmount: Voucher payment: The voucher deduction amount.
        :type VoucherPayAmount: str
        :param _CashPayAmount: Cash credit payment: The amount paid through the user's cash account.
        :type CashPayAmount: str
        :param _IncentivePayAmount: Free credit payment: The amount paid with the user's free credit.
        :type IncentivePayAmount: str
        :param _TransferPayAmount: Commission credit payment: The amount paid with the user's commission credit.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        :param _ExtendField3: Extended field 3: The extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField3: str
        :param _ExtendField4: Extended field 4: The extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField4: str
        :param _ExtendField5: Extended field 5: The extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField5: str
        :param _Tags: Tag information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of BillTagInfo
        :param _OwnerUin: Owner account ID: The account ID of the actual resource user.
        :type OwnerUin: str
        :param _OperateUin: Operator account ID: The account or role ID of the operator who purchases or activates a resource.
        :type OperateUin: str
        :param _BusinessCode: Product code.
        :type BusinessCode: str
        :param _ProductCode: Subproduct code.
        :type ProductCode: str
        :param _RegionId: Region ID.
        :type RegionId: int
        :param _InstanceType: Instance type: The instance type of a product or service purchased, which can be resource package, RI, SP, or spot instance. Other instance types are not displayed by default.
        :type InstanceType: str
        :param _OriginalCostWithRI: RI deduction (cost): The amount deducted from the original cost by RI.	
        :type OriginalCostWithRI: str
        :param _SPDeduction: Savings plan deduction (disused).
        :type SPDeduction: str
        :param _OriginalCostWithSP: SP deduction (cost): The amount of cost deducted by a savings plan based on the component's original cost. SP deduction (cost) = Cost deduction by SP / SP deduction rate	
        :type OriginalCostWithSP: str
        :param _BillMonth: Billing monthNote: This field may return null, indicating that no valid values can be obtained.
        :type BillMonth: str
        """
        self._BusinessCodeName = None
        self._ProductCodeName = None
        self._PayModeName = None
        self._ProjectName = None
        self._RegionName = None
        self._ZoneName = None
        self._ResourceId = None
        self._ResourceName = None
        self._ActionTypeName = None
        self._OrderId = None
        self._PayTime = None
        self._FeeBeginTime = None
        self._FeeEndTime = None
        self._ConfigDesc = None
        self._ExtendField1 = None
        self._ExtendField2 = None
        self._TotalCost = None
        self._Discount = None
        self._ReduceType = None
        self._RealTotalCost = None
        self._VoucherPayAmount = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None
        self._ExtendField3 = None
        self._ExtendField4 = None
        self._ExtendField5 = None
        self._Tags = None
        self._OwnerUin = None
        self._OperateUin = None
        self._BusinessCode = None
        self._ProductCode = None
        self._RegionId = None
        self._InstanceType = None
        self._OriginalCostWithRI = None
        self._SPDeduction = None
        self._OriginalCostWithSP = None
        self._BillMonth = None

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def PayTime(self):
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def FeeBeginTime(self):
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ConfigDesc(self):
        return self._ConfigDesc

    @ConfigDesc.setter
    def ConfigDesc(self, ConfigDesc):
        self._ConfigDesc = ConfigDesc

    @property
    def ExtendField1(self):
        return self._ExtendField1

    @ExtendField1.setter
    def ExtendField1(self, ExtendField1):
        self._ExtendField1 = ExtendField1

    @property
    def ExtendField2(self):
        return self._ExtendField2

    @ExtendField2.setter
    def ExtendField2(self, ExtendField2):
        self._ExtendField2 = ExtendField2

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def ReduceType(self):
        return self._ReduceType

    @ReduceType.setter
    def ReduceType(self, ReduceType):
        self._ReduceType = ReduceType

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def ExtendField3(self):
        return self._ExtendField3

    @ExtendField3.setter
    def ExtendField3(self, ExtendField3):
        self._ExtendField3 = ExtendField3

    @property
    def ExtendField4(self):
        return self._ExtendField4

    @ExtendField4.setter
    def ExtendField4(self, ExtendField4):
        self._ExtendField4 = ExtendField4

    @property
    def ExtendField5(self):
        return self._ExtendField5

    @ExtendField5.setter
    def ExtendField5(self, ExtendField5):
        self._ExtendField5 = ExtendField5

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def OriginalCostWithRI(self):
        return self._OriginalCostWithRI

    @OriginalCostWithRI.setter
    def OriginalCostWithRI(self, OriginalCostWithRI):
        self._OriginalCostWithRI = OriginalCostWithRI

    @property
    def SPDeduction(self):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        return self._SPDeduction

    @SPDeduction.setter
    def SPDeduction(self, SPDeduction):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        self._SPDeduction = SPDeduction

    @property
    def OriginalCostWithSP(self):
        return self._OriginalCostWithSP

    @OriginalCostWithSP.setter
    def OriginalCostWithSP(self, OriginalCostWithSP):
        self._OriginalCostWithSP = OriginalCostWithSP

    @property
    def BillMonth(self):
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth


    def _deserialize(self, params):
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._ProductCodeName = params.get("ProductCodeName")
        self._PayModeName = params.get("PayModeName")
        self._ProjectName = params.get("ProjectName")
        self._RegionName = params.get("RegionName")
        self._ZoneName = params.get("ZoneName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._ActionTypeName = params.get("ActionTypeName")
        self._OrderId = params.get("OrderId")
        self._PayTime = params.get("PayTime")
        self._FeeBeginTime = params.get("FeeBeginTime")
        self._FeeEndTime = params.get("FeeEndTime")
        self._ConfigDesc = params.get("ConfigDesc")
        self._ExtendField1 = params.get("ExtendField1")
        self._ExtendField2 = params.get("ExtendField2")
        self._TotalCost = params.get("TotalCost")
        self._Discount = params.get("Discount")
        self._ReduceType = params.get("ReduceType")
        self._RealTotalCost = params.get("RealTotalCost")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._ExtendField3 = params.get("ExtendField3")
        self._ExtendField4 = params.get("ExtendField4")
        self._ExtendField5 = params.get("ExtendField5")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = BillTagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._OwnerUin = params.get("OwnerUin")
        self._OperateUin = params.get("OperateUin")
        self._BusinessCode = params.get("BusinessCode")
        self._ProductCode = params.get("ProductCode")
        self._RegionId = params.get("RegionId")
        self._InstanceType = params.get("InstanceType")
        self._OriginalCostWithRI = params.get("OriginalCostWithRI")
        self._SPDeduction = params.get("SPDeduction")
        self._OriginalCostWithSP = params.get("OriginalCostWithSP")
        self._BillMonth = params.get("BillMonth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillResourceSummary(AbstractModel):
    """Information about resources charged in the bill

    """

    def __init__(self):
        r"""
        :param _BusinessCodeName: Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :type BusinessCodeName: str
        :param _ProductCodeName: Subproduct name: The subcategory of a Tencent Cloud product purchased by the user, such as CVM – Standard S1.
        :type ProductCodeName: str
        :param _PayModeName: Billing mode, which can be monthly subscription or pay-as-you-go.
        :type PayModeName: str
        :param _ProjectName: Project name: The project to which a resource belongs, which is user-designated. If a resource has not been assigned to a project, it will automatically belong to the default project.
        :type ProjectName: str
        :param _RegionName: Region: The region to which a resource belongs, such as South China (Guangzhou).
        :type RegionName: str
        :param _ZoneName: Availability zone: The availability zone to which a resource belongs, such as Guangzhou Zone 3.
        :type ZoneName: str
        :param _ResourceId: Instance ID: The object ID of a billed resource, such as a CVM instance ID. This object ID may vary due to various forms and contents of resources in different products.	
        :type ResourceId: str
        :param _ResourceName: Instance name: The resource name set by the user in the console. If it is not set, it will be empty by default.
        :type ResourceName: str
        :param _ActionTypeName: Transaction type, which can be monthly subscription purchase, monthly subscription renewal, or pay-as-you-go deduction.
        :type ActionTypeName: str
        :param _OrderId: Order ID: The order number for a monthly subscription purchase
        :type OrderId: str
        :param _PayTime: Transaction time: The time at which a payment was deducted
        :type PayTime: str
        :param _FeeBeginTime: Usage start time: The time at which product or service usage starts
        :type FeeBeginTime: str
        :param _FeeEndTime: Usage end time: The time at which product or service usage ends
        :type FeeEndTime: str
        :param _ConfigDesc: Configuration description: The billable item names and usage of a resource, which are displayed on the resource bill only.
        :type ConfigDesc: str
        :param _ExtendField1: Extended field 1: Extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField1: str
        :param _ExtendField2: Extended field 2: Extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField2: str
        :param _TotalCost: Original cost: The original cost of a resource, which is "List price x Usage x Usage duration". If a customer has applied for a fixed preferential price or contract price or applied for a refund, this parameter will not be displayed by default.
        :type TotalCost: str
        :param _Discount: Discount multiplier: The discount multiplier applied to the cost of the resource. If a customer has applied for a fixed preferential price or contract price or applied for a refund, this parameter will not be displayed by default.
        :type Discount: str
        :param _ReduceType: Offer type
        :type ReduceType: str
        :param _RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param _VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param _CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param _IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param _TransferPayAmount: Commission credit: The amount paid with the user’s commission credit. Note: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        :param _ExtendField3: Extended field 3: Extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField3: str
        :param _ExtendField4: Extended field 4: Extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField4: str
        :param _ExtendField5: Extended field 5: Extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField5: str
        :param _Tags: Tag information. Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of BillTagInfo
        :param _PayerUin: Payer account ID: The account ID of the payer, which is the unique identifier of a Tencent Cloud user.
        :type PayerUin: str
        :param _OwnerUin: Owner account ID: The account ID of the actual resource user
        :type OwnerUin: str
        :param _OperateUin: Operator account ID: The account or role ID of the operator who purchases or activates a resource.
        :type OperateUin: str
        :param _BusinessCode: Product code
        :type BusinessCode: str
        :param _ProductCode: Subproduct code
        :type ProductCode: str
        :param _RegionId: Region ID
        :type RegionId: int
        :param _InstanceType: Instance type: The instance type of a product or service purchased, which can be resource package, RI, SP, or spot instance. Other instance types are not displayed by default.
        :type InstanceType: str
        :param _OriginalCostWithRI: RI deduction (cost): The amount deducted from the original cost by RI	
        :type OriginalCostWithRI: str
        :param _SPDeduction: Cost deduction by SP. This parameter has been deprecated.
        :type SPDeduction: str
        :param _OriginalCostWithSP: SP deduction (cost): SP deduction (cost) = Cost deduction by SP / SP deduction rate	
        :type OriginalCostWithSP: str
        :param _BillMonth: Billing monthNote: This field may return null, indicating that no valid values can be obtained.
        :type BillMonth: str
        """
        self._BusinessCodeName = None
        self._ProductCodeName = None
        self._PayModeName = None
        self._ProjectName = None
        self._RegionName = None
        self._ZoneName = None
        self._ResourceId = None
        self._ResourceName = None
        self._ActionTypeName = None
        self._OrderId = None
        self._PayTime = None
        self._FeeBeginTime = None
        self._FeeEndTime = None
        self._ConfigDesc = None
        self._ExtendField1 = None
        self._ExtendField2 = None
        self._TotalCost = None
        self._Discount = None
        self._ReduceType = None
        self._RealTotalCost = None
        self._VoucherPayAmount = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None
        self._ExtendField3 = None
        self._ExtendField4 = None
        self._ExtendField5 = None
        self._Tags = None
        self._PayerUin = None
        self._OwnerUin = None
        self._OperateUin = None
        self._BusinessCode = None
        self._ProductCode = None
        self._RegionId = None
        self._InstanceType = None
        self._OriginalCostWithRI = None
        self._SPDeduction = None
        self._OriginalCostWithSP = None
        self._BillMonth = None

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def PayTime(self):
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def FeeBeginTime(self):
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ConfigDesc(self):
        return self._ConfigDesc

    @ConfigDesc.setter
    def ConfigDesc(self, ConfigDesc):
        self._ConfigDesc = ConfigDesc

    @property
    def ExtendField1(self):
        return self._ExtendField1

    @ExtendField1.setter
    def ExtendField1(self, ExtendField1):
        self._ExtendField1 = ExtendField1

    @property
    def ExtendField2(self):
        return self._ExtendField2

    @ExtendField2.setter
    def ExtendField2(self, ExtendField2):
        self._ExtendField2 = ExtendField2

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def ReduceType(self):
        return self._ReduceType

    @ReduceType.setter
    def ReduceType(self, ReduceType):
        self._ReduceType = ReduceType

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def ExtendField3(self):
        return self._ExtendField3

    @ExtendField3.setter
    def ExtendField3(self, ExtendField3):
        self._ExtendField3 = ExtendField3

    @property
    def ExtendField4(self):
        return self._ExtendField4

    @ExtendField4.setter
    def ExtendField4(self, ExtendField4):
        self._ExtendField4 = ExtendField4

    @property
    def ExtendField5(self):
        return self._ExtendField5

    @ExtendField5.setter
    def ExtendField5(self, ExtendField5):
        self._ExtendField5 = ExtendField5

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def OriginalCostWithRI(self):
        return self._OriginalCostWithRI

    @OriginalCostWithRI.setter
    def OriginalCostWithRI(self, OriginalCostWithRI):
        self._OriginalCostWithRI = OriginalCostWithRI

    @property
    def SPDeduction(self):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        return self._SPDeduction

    @SPDeduction.setter
    def SPDeduction(self, SPDeduction):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        self._SPDeduction = SPDeduction

    @property
    def OriginalCostWithSP(self):
        return self._OriginalCostWithSP

    @OriginalCostWithSP.setter
    def OriginalCostWithSP(self, OriginalCostWithSP):
        self._OriginalCostWithSP = OriginalCostWithSP

    @property
    def BillMonth(self):
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth


    def _deserialize(self, params):
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._ProductCodeName = params.get("ProductCodeName")
        self._PayModeName = params.get("PayModeName")
        self._ProjectName = params.get("ProjectName")
        self._RegionName = params.get("RegionName")
        self._ZoneName = params.get("ZoneName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._ActionTypeName = params.get("ActionTypeName")
        self._OrderId = params.get("OrderId")
        self._PayTime = params.get("PayTime")
        self._FeeBeginTime = params.get("FeeBeginTime")
        self._FeeEndTime = params.get("FeeEndTime")
        self._ConfigDesc = params.get("ConfigDesc")
        self._ExtendField1 = params.get("ExtendField1")
        self._ExtendField2 = params.get("ExtendField2")
        self._TotalCost = params.get("TotalCost")
        self._Discount = params.get("Discount")
        self._ReduceType = params.get("ReduceType")
        self._RealTotalCost = params.get("RealTotalCost")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._ExtendField3 = params.get("ExtendField3")
        self._ExtendField4 = params.get("ExtendField4")
        self._ExtendField5 = params.get("ExtendField5")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = BillTagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._PayerUin = params.get("PayerUin")
        self._OwnerUin = params.get("OwnerUin")
        self._OperateUin = params.get("OperateUin")
        self._BusinessCode = params.get("BusinessCode")
        self._ProductCode = params.get("ProductCode")
        self._RegionId = params.get("RegionId")
        self._InstanceType = params.get("InstanceType")
        self._OriginalCostWithRI = params.get("OriginalCostWithRI")
        self._SPDeduction = params.get("SPDeduction")
        self._OriginalCostWithSP = params.get("OriginalCostWithSP")
        self._BillMonth = params.get("BillMonth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillTagInfo(AbstractModel):
    """Bill tag information.

    """

    def __init__(self):
        r"""
        :param _TagKey: Cost allocation tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusinessSummaryInfo(AbstractModel):
    """Detailed summary of products

    """

    def __init__(self):
        r"""
        :param _BusinessCode: Product code
        :type BusinessCode: str
        :param _BusinessCodeName: Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :type BusinessCodeName: str
        :param _TotalCost: Original cost in USD. This parameter became valid when Bill 3.0 took effect in May 2021. Before that, `-` was returned for this parameter. If a customer has applied for a contract price different from the prices listed on the official website, `-` will also be returned for this parameter. 
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCost: str
        :param _RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param _CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param _IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param _TransferPayAmount: Commission credit: The amount paid with the user’s commission credit. Note: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        """
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._TotalCost = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount


    def _deserialize(self, params):
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._TotalCost = params.get("TotalCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusinessSummaryOverviewItem(AbstractModel):
    """Summarize product details by product

    """

    def __init__(self):
        r"""
        :param _BusinessCode: Product code. Note: This field may return null, indicating that no valid values can be obtained.
        :type BusinessCode: str
        :param _BusinessCodeName: Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :type BusinessCodeName: str
        :param _RealTotalCostRatio: Cost ratio, to two decimal points
        :type RealTotalCostRatio: str
        :param _RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param _CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param _IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param _TransferPayAmount: Commission credit: The amount paid with the user’s commission credit.
        :type TransferPayAmount: str
        :param _BillMonth: Billing month, e.g. `2019-08`
        :type BillMonth: str
        :param _TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        """
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._RealTotalCostRatio = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None
        self._BillMonth = None
        self._TotalCost = None

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def RealTotalCostRatio(self):
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def BillMonth(self):
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._RealTotalCostRatio = params.get("RealTotalCostRatio")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._BillMonth = params.get("BillMonth")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusinessSummaryTotal(AbstractModel):
    """Summarize total cost by product

    """

    def __init__(self):
        r"""
        :param _RealTotalCost: Total amount after discount

        :type RealTotalCost: str
        :param _VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param _IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param _CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param _TransferPayAmount: Commission credit: The amount paid with the user’s commission credit.
        :type TransferPayAmount: str
        :param _TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        """
        self._RealTotalCost = None
        self._VoucherPayAmount = None
        self._IncentivePayAmount = None
        self._CashPayAmount = None
        self._TransferPayAmount = None
        self._TotalCost = None

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._RealTotalCost = params.get("RealTotalCost")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._CashPayAmount = params.get("CashPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConditionBusiness(AbstractModel):
    """Product filter criteria

    """

    def __init__(self):
        r"""
        :param _BusinessCode: Product name code
        :type BusinessCode: str
        :param _BusinessCodeName: Product name
        :type BusinessCodeName: str
        """
        self._BusinessCode = None
        self._BusinessCodeName = None

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName


    def _deserialize(self, params):
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConditionPayMode(AbstractModel):
    """Payment mode filter criteria

    """

    def __init__(self):
        r"""
        :param _PayMode: Payment mode
        :type PayMode: str
        :param _PayModeName: Payment mode name
        :type PayModeName: str
        """
        self._PayMode = None
        self._PayModeName = None

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName


    def _deserialize(self, params):
        self._PayMode = params.get("PayMode")
        self._PayModeName = params.get("PayModeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConditionProject(AbstractModel):
    """Project filter criteria

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: str
        :param _ProjectName: Project name
        :type ProjectName: str
        """
        self._ProjectId = None
        self._ProjectName = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConditionRegion(AbstractModel):
    """Regional filter criteria

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID
        :type RegionId: str
        :param _RegionName: Region name
        :type RegionName: str
        """
        self._RegionId = None
        self._RegionName = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Conditions(AbstractModel):
    """Billing filter criteria object

    """

    def __init__(self):
        r"""
        :param _TimeRange: Only supports two values: 6 and 12.
        :type TimeRange: int
        :param _BusinessCode: Product name code
        :type BusinessCode: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _RegionId: Region ID
        :type RegionId: int
        :param _PayMode: Payment mode. Options include prePay and postPay.
        :type PayMode: str
        :param _ResourceKeyword: Resource keyword
        :type ResourceKeyword: str
        :param _BusinessCodes: Product name code
        :type BusinessCodes: list of str
        :param _ProductCodes: Subproduct name code
        :type ProductCodes: list of str
        :param _RegionIds: Region ID
        :type RegionIds: list of int
        :param _ProjectIds: Project ID
        :type ProjectIds: list of int
        :param _PayModes: Payment mode. Options include prePay and postPay.
        :type PayModes: list of str
        :param _ActionTypes: Transaction type
        :type ActionTypes: list of str
        :param _HideFreeCost: Whether to hide zero-amount transactions
        :type HideFreeCost: int
        :param _OrderByCost: Sorting rule. Options include desc and asc.
        :type OrderByCost: str
        :param _BillIds: Transaction ID
        :type BillIds: list of str
        :param _ComponentCodes: Component code
        :type ComponentCodes: list of str
        :param _FileIds: File ID
        :type FileIds: list of str
        :param _FileTypes: File type
        :type FileTypes: list of str
        :param _Status: Status
        :type Status: list of int non-negative
        """
        self._TimeRange = None
        self._BusinessCode = None
        self._ProjectId = None
        self._RegionId = None
        self._PayMode = None
        self._ResourceKeyword = None
        self._BusinessCodes = None
        self._ProductCodes = None
        self._RegionIds = None
        self._ProjectIds = None
        self._PayModes = None
        self._ActionTypes = None
        self._HideFreeCost = None
        self._OrderByCost = None
        self._BillIds = None
        self._ComponentCodes = None
        self._FileIds = None
        self._FileTypes = None
        self._Status = None

    @property
    def TimeRange(self):
        return self._TimeRange

    @TimeRange.setter
    def TimeRange(self, TimeRange):
        self._TimeRange = TimeRange

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResourceKeyword(self):
        return self._ResourceKeyword

    @ResourceKeyword.setter
    def ResourceKeyword(self, ResourceKeyword):
        self._ResourceKeyword = ResourceKeyword

    @property
    def BusinessCodes(self):
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def ProductCodes(self):
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes

    @property
    def RegionIds(self):
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def PayModes(self):
        return self._PayModes

    @PayModes.setter
    def PayModes(self, PayModes):
        self._PayModes = PayModes

    @property
    def ActionTypes(self):
        return self._ActionTypes

    @ActionTypes.setter
    def ActionTypes(self, ActionTypes):
        self._ActionTypes = ActionTypes

    @property
    def HideFreeCost(self):
        return self._HideFreeCost

    @HideFreeCost.setter
    def HideFreeCost(self, HideFreeCost):
        self._HideFreeCost = HideFreeCost

    @property
    def OrderByCost(self):
        return self._OrderByCost

    @OrderByCost.setter
    def OrderByCost(self, OrderByCost):
        self._OrderByCost = OrderByCost

    @property
    def BillIds(self):
        return self._BillIds

    @BillIds.setter
    def BillIds(self, BillIds):
        self._BillIds = BillIds

    @property
    def ComponentCodes(self):
        return self._ComponentCodes

    @ComponentCodes.setter
    def ComponentCodes(self, ComponentCodes):
        self._ComponentCodes = ComponentCodes

    @property
    def FileIds(self):
        return self._FileIds

    @FileIds.setter
    def FileIds(self, FileIds):
        self._FileIds = FileIds

    @property
    def FileTypes(self):
        return self._FileTypes

    @FileTypes.setter
    def FileTypes(self, FileTypes):
        self._FileTypes = FileTypes

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._TimeRange = params.get("TimeRange")
        self._BusinessCode = params.get("BusinessCode")
        self._ProjectId = params.get("ProjectId")
        self._RegionId = params.get("RegionId")
        self._PayMode = params.get("PayMode")
        self._ResourceKeyword = params.get("ResourceKeyword")
        self._BusinessCodes = params.get("BusinessCodes")
        self._ProductCodes = params.get("ProductCodes")
        self._RegionIds = params.get("RegionIds")
        self._ProjectIds = params.get("ProjectIds")
        self._PayModes = params.get("PayModes")
        self._ActionTypes = params.get("ActionTypes")
        self._HideFreeCost = params.get("HideFreeCost")
        self._OrderByCost = params.get("OrderByCost")
        self._BillIds = params.get("BillIds")
        self._ComponentCodes = params.get("ComponentCodes")
        self._FileIds = params.get("FileIds")
        self._FileTypes = params.get("FileTypes")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionBusinessSummaryDataItem(AbstractModel):
    """Consumption details summarized by product

    """

    def __init__(self):
        r"""
        :param _BusinessCode: Product name code
        :type BusinessCode: str
        :param _BusinessCodeName: Product name
        :type BusinessCodeName: str
        :param _RealTotalCost: Discounted total price
        :type RealTotalCost: str
        :param _Trend: Cost trend
        :type Trend: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        :param _CashPayAmount: Cash
Note: This field may return null, indicating that no valid values can be obtained.
        :type CashPayAmount: str
        :param _IncentivePayAmount: Bonus
Note: This field may return null, indicating that no valid values can be obtained.
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: VoucherNote: This field may return null, indicating that no valid values can be obtained.
        :type VoucherPayAmount: str
        :param _TransferPayAmount: Share revenueNote: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        :param _RegionName: Region name (only shown in regional summary)
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionName: str
        """
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._RealTotalCost = None
        self._Trend = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None
        self._RegionName = None

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Trend(self):
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName


    def _deserialize(self, params):
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._RealTotalCost = params.get("RealTotalCost")
        if params.get("Trend") is not None:
            self._Trend = ConsumptionSummaryTrend()
            self._Trend._deserialize(params.get("Trend"))
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionProjectSummaryDataItem(AbstractModel):
    """Consumption details summarized by project

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: str
        :param _ProjectName: Project name
        :type ProjectName: str
        :param _RealTotalCost: Discounted total price
        :type RealTotalCost: str
        :param _Trend: Trend
        :type Trend: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        :param _Business: Product consumption details
        :type Business: list of ConsumptionBusinessSummaryDataItem
        :param _CashPayAmount: Cash
Note: This field may return null, indicating that no valid values can be obtained.
        :type CashPayAmount: str
        :param _IncentivePayAmount: Bonus
Note: This field may return null, indicating that no valid values can be obtained.
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: VoucherNote: This field may return null, indicating that no valid values can be obtained.
        :type VoucherPayAmount: str
        :param _TransferPayAmount: Share revenueNote: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        """
        self._ProjectId = None
        self._ProjectName = None
        self._RealTotalCost = None
        self._Trend = None
        self._Business = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Trend(self):
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._RealTotalCost = params.get("RealTotalCost")
        if params.get("Trend") is not None:
            self._Trend = ConsumptionSummaryTrend()
            self._Trend._deserialize(params.get("Trend"))
        if params.get("Business") is not None:
            self._Business = []
            for item in params.get("Business"):
                obj = ConsumptionBusinessSummaryDataItem()
                obj._deserialize(item)
                self._Business.append(obj)
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionRegionSummaryDataItem(AbstractModel):
    """Consumption details summarized by region

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID
        :type RegionId: str
        :param _RegionName: Region name
        :type RegionName: str
        :param _RealTotalCost: Discounted total price
        :type RealTotalCost: str
        :param _Trend: Trend
        :type Trend: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        :param _Business: Product consumption details
        :type Business: list of ConsumptionBusinessSummaryDataItem
        :param _CashPayAmount: Cash
Note: This field may return null, indicating that no valid values can be obtained.
        :type CashPayAmount: str
        :param _VoucherPayAmount: VoucherNote: This field may return null, indicating that no valid values can be obtained.
        :type VoucherPayAmount: str
        :param _IncentivePayAmount: Bonus
Note: This field may return null, indicating that no valid values can be obtained.
        :type IncentivePayAmount: str
        :param _TransferPayAmount: Share revenueNote: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        """
        self._RegionId = None
        self._RegionName = None
        self._RealTotalCost = None
        self._Trend = None
        self._Business = None
        self._CashPayAmount = None
        self._VoucherPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Trend(self):
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._RealTotalCost = params.get("RealTotalCost")
        if params.get("Trend") is not None:
            self._Trend = ConsumptionSummaryTrend()
            self._Trend._deserialize(params.get("Trend"))
        if params.get("Business") is not None:
            self._Business = []
            for item in params.get("Business"):
                obj = ConsumptionBusinessSummaryDataItem()
                obj._deserialize(item)
                self._Business.append(obj)
        self._CashPayAmount = params.get("CashPayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionResourceSummaryConditionValue(AbstractModel):
    """Filter criteria of consumption details summarized by resource

    """

    def __init__(self):
        r"""
        :param _Business: Product list
        :type Business: list of ConditionBusiness
        :param _Project: Project list
        :type Project: list of ConditionProject
        :param _Region: Region list
        :type Region: list of ConditionRegion
        :param _PayMode: Payment mode list
        :type PayMode: list of ConditionPayMode
        """
        self._Business = None
        self._Project = None
        self._Region = None
        self._PayMode = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Project(self):
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        if params.get("Business") is not None:
            self._Business = []
            for item in params.get("Business"):
                obj = ConditionBusiness()
                obj._deserialize(item)
                self._Business.append(obj)
        if params.get("Project") is not None:
            self._Project = []
            for item in params.get("Project"):
                obj = ConditionProject()
                obj._deserialize(item)
                self._Project.append(obj)
        if params.get("Region") is not None:
            self._Region = []
            for item in params.get("Region"):
                obj = ConditionRegion()
                obj._deserialize(item)
                self._Region.append(obj)
        if params.get("PayMode") is not None:
            self._PayMode = []
            for item in params.get("PayMode"):
                obj = ConditionPayMode()
                obj._deserialize(item)
                self._PayMode.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionResourceSummaryDataItem(AbstractModel):
    """Consumption details summarized by resource

    """

    def __init__(self):
        r"""
        :param _ResourceId: Resource ID
        :type ResourceId: str
        :param _ResourceName: Resource name
        :type ResourceName: str
        :param _RealTotalCost: Discounted total price
        :type RealTotalCost: str
        :param _CashPayAmount: Cash expenditure
        :type CashPayAmount: str
        :param _ProjectId: Project ID
        :type ProjectId: str
        :param _ProjectName: Project name
        :type ProjectName: str
        :param _RegionId: Region ID
        :type RegionId: str
        :param _RegionName: Region name
        :type RegionName: str
        :param _PayMode: Payment mode
        :type PayMode: str
        :param _PayModeName: Payment mode name
        :type PayModeName: str
        :param _BusinessCode: Product name code
        :type BusinessCode: str
        :param _BusinessCodeName: Product name
        :type BusinessCodeName: str
        :param _ConsumptionTypeName: Consumption type
        :type ConsumptionTypeName: str
        :param _RealCost: Pre-discount priceNote: This field may return null, indicating that no valid values can be obtained.
        :type RealCost: str
        :param _FeeBeginTime: Start time of feesNote: This field may return null, indicating that no valid values can be obtained.
        :type FeeBeginTime: str
        :param _FeeEndTime: End time of feesNote: This field may return null, indicating that no valid values can be obtained.
        :type FeeEndTime: str
        :param _DayDiff: Days
Note: This field may return null, indicating that no valid values can be obtained.
        :type DayDiff: str
        :param _DailyTotalCost: Daily consumptionNote: This field may return null, indicating that no valid values can be obtained.
        :type DailyTotalCost: str
        :param _OrderId: Order numberNote: This field may return null, indicating that no valid values can be obtained.
        :type OrderId: str
        :param _VoucherPayAmount: VoucherNote: This field may return null, indicating that no valid values can be obtained.
        :type VoucherPayAmount: str
        :param _IncentivePayAmount: Bonus
Note: This field may return null, indicating that no valid values can be obtained.
        :type IncentivePayAmount: str
        :param _TransferPayAmount: Share revenueNote: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        :param _PayerUin: Payer UIN: the account ID of the payer, which is the unique identifier of a Tencent Cloud userNote: This field may return null, indicating that no valid values can be obtained.
        :type PayerUin: str
        :param _OwnerUin: User UIN: the account ID of the actual resource userNote: This field may return null, indicating that no valid values can be obtained.
        :type OwnerUin: str
        :param _OperateUin: Operator UIN: the account ID or role ID of the operator who places orders for prepaid resources or activates postpaid resourcesNote: This field may return null, indicating that no valid values can be obtained.
        :type OperateUin: str
        :param _ProductCode: Subproduct codeNote: This field may return null, indicating that no valid values can be obtained.
        :type ProductCode: str
        :param _ProductCodeName: Subproduct name: the subcategory of a product purchased by the user, such as CVM – Standard S1Note: This field may return null, indicating that no valid values can be obtained.
        :type ProductCodeName: str
        :param _RegionType: Region typeNote: This field may return null, indicating that no valid values can be obtained.
        :type RegionType: str
        :param _RegionTypeName: Region type nameNote: This field may return null, indicating that no valid values can be obtained.
        :type RegionTypeName: str
        :param _Extend1: Extended field 1Note: This field may return null, indicating that no valid values can be obtained.
        :type Extend1: str
        :param _Extend2: Extended field 2Note: This field may return null, indicating that no valid values can be obtained.
        :type Extend2: str
        :param _Extend3: Extended field 3Note: This field may return null, indicating that no valid values can be obtained.
        :type Extend3: str
        :param _Extend4: Extended field 4Note: This field may return null, indicating that no valid values can be obtained.
        :type Extend4: str
        :param _Extend5: Extended field 5Note: This field may return null, indicating that no valid values can be obtained.
        :type Extend5: str
        :param _InstanceType: Instance typeNote: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param _InstanceTypeName: Instance type nameNote: This field may return null, indicating that no valid values can be obtained.
        :type InstanceTypeName: str
        :param _PayTime: Deduction time: the time at which a payment is deductedNote: This field may return null, indicating that no valid values can be obtained.
        :type PayTime: str
        :param _ZoneName: Availability zone: availability zone of a resource, e.g. Guangzhou Zone 3Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneName: str
        :param _ComponentConfig: Configuration descriptionNote: This field may return null, indicating that no valid values can be obtained.
        :type ComponentConfig: str
        :param _Tags: Tag information.Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: str
        """
        self._ResourceId = None
        self._ResourceName = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._ProjectId = None
        self._ProjectName = None
        self._RegionId = None
        self._RegionName = None
        self._PayMode = None
        self._PayModeName = None
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._ConsumptionTypeName = None
        self._RealCost = None
        self._FeeBeginTime = None
        self._FeeEndTime = None
        self._DayDiff = None
        self._DailyTotalCost = None
        self._OrderId = None
        self._VoucherPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None
        self._PayerUin = None
        self._OwnerUin = None
        self._OperateUin = None
        self._ProductCode = None
        self._ProductCodeName = None
        self._RegionType = None
        self._RegionTypeName = None
        self._Extend1 = None
        self._Extend2 = None
        self._Extend3 = None
        self._Extend4 = None
        self._Extend5 = None
        self._InstanceType = None
        self._InstanceTypeName = None
        self._PayTime = None
        self._ZoneName = None
        self._ComponentConfig = None
        self._Tags = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ConsumptionTypeName(self):
        return self._ConsumptionTypeName

    @ConsumptionTypeName.setter
    def ConsumptionTypeName(self, ConsumptionTypeName):
        self._ConsumptionTypeName = ConsumptionTypeName

    @property
    def RealCost(self):
        return self._RealCost

    @RealCost.setter
    def RealCost(self, RealCost):
        self._RealCost = RealCost

    @property
    def FeeBeginTime(self):
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def DayDiff(self):
        return self._DayDiff

    @DayDiff.setter
    def DayDiff(self, DayDiff):
        self._DayDiff = DayDiff

    @property
    def DailyTotalCost(self):
        return self._DailyTotalCost

    @DailyTotalCost.setter
    def DailyTotalCost(self, DailyTotalCost):
        self._DailyTotalCost = DailyTotalCost

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductCodeName(self):
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def RegionType(self):
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def RegionTypeName(self):
        return self._RegionTypeName

    @RegionTypeName.setter
    def RegionTypeName(self, RegionTypeName):
        self._RegionTypeName = RegionTypeName

    @property
    def Extend1(self):
        return self._Extend1

    @Extend1.setter
    def Extend1(self, Extend1):
        self._Extend1 = Extend1

    @property
    def Extend2(self):
        return self._Extend2

    @Extend2.setter
    def Extend2(self, Extend2):
        self._Extend2 = Extend2

    @property
    def Extend3(self):
        return self._Extend3

    @Extend3.setter
    def Extend3(self, Extend3):
        self._Extend3 = Extend3

    @property
    def Extend4(self):
        return self._Extend4

    @Extend4.setter
    def Extend4(self, Extend4):
        self._Extend4 = Extend4

    @property
    def Extend5(self):
        return self._Extend5

    @Extend5.setter
    def Extend5(self, Extend5):
        self._Extend5 = Extend5

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceTypeName(self):
        return self._InstanceTypeName

    @InstanceTypeName.setter
    def InstanceTypeName(self, InstanceTypeName):
        self._InstanceTypeName = InstanceTypeName

    @property
    def PayTime(self):
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ComponentConfig(self):
        return self._ComponentConfig

    @ComponentConfig.setter
    def ComponentConfig(self, ComponentConfig):
        self._ComponentConfig = ComponentConfig

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._PayMode = params.get("PayMode")
        self._PayModeName = params.get("PayModeName")
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._ConsumptionTypeName = params.get("ConsumptionTypeName")
        self._RealCost = params.get("RealCost")
        self._FeeBeginTime = params.get("FeeBeginTime")
        self._FeeEndTime = params.get("FeeEndTime")
        self._DayDiff = params.get("DayDiff")
        self._DailyTotalCost = params.get("DailyTotalCost")
        self._OrderId = params.get("OrderId")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._PayerUin = params.get("PayerUin")
        self._OwnerUin = params.get("OwnerUin")
        self._OperateUin = params.get("OperateUin")
        self._ProductCode = params.get("ProductCode")
        self._ProductCodeName = params.get("ProductCodeName")
        self._RegionType = params.get("RegionType")
        self._RegionTypeName = params.get("RegionTypeName")
        self._Extend1 = params.get("Extend1")
        self._Extend2 = params.get("Extend2")
        self._Extend3 = params.get("Extend3")
        self._Extend4 = params.get("Extend4")
        self._Extend5 = params.get("Extend5")
        self._InstanceType = params.get("InstanceType")
        self._InstanceTypeName = params.get("InstanceTypeName")
        self._PayTime = params.get("PayTime")
        self._ZoneName = params.get("ZoneName")
        self._ComponentConfig = params.get("ComponentConfig")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionSummaryTotal(AbstractModel):
    """Consumption summary details

    """

    def __init__(self):
        r"""
        :param _RealTotalCost: Discounted total price
        :type RealTotalCost: str
        """
        self._RealTotalCost = None

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost


    def _deserialize(self, params):
        self._RealTotalCost = params.get("RealTotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionSummaryTrend(AbstractModel):
    """Consumption cost trend

    """

    def __init__(self):
        r"""
        :param _Type: Trend type, upward for rising, downward for falling, none for no change
        :type Type: str
        :param _Value: Trend value. The value is null when Type is none.Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        """
        self._Type = None
        self._Value = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosDetailSets(AbstractModel):
    """Information about the data structure of the returned COS usage details

    """

    def __init__(self):
        r"""
        :param _BucketName: Bucket name
        :type BucketName: str
        :param _DosageBeginTime: The start time of the usage
        :type DosageBeginTime: str
        :param _DosageEndTime: The end time of the usage
        :type DosageEndTime: str
        :param _SubProductCodeName: Subproduct name
        :type SubProductCodeName: str
        :param _BillingItemCodeName: Billable item name
        :type BillingItemCodeName: str
        :param _DosageValue: Usage
        :type DosageValue: str
        :param _Unit: Unit of the billable item
        :type Unit: str
        """
        self._BucketName = None
        self._DosageBeginTime = None
        self._DosageEndTime = None
        self._SubProductCodeName = None
        self._BillingItemCodeName = None
        self._DosageValue = None
        self._Unit = None

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def DosageBeginTime(self):
        return self._DosageBeginTime

    @DosageBeginTime.setter
    def DosageBeginTime(self, DosageBeginTime):
        self._DosageBeginTime = DosageBeginTime

    @property
    def DosageEndTime(self):
        return self._DosageEndTime

    @DosageEndTime.setter
    def DosageEndTime(self, DosageEndTime):
        self._DosageEndTime = DosageEndTime

    @property
    def SubProductCodeName(self):
        return self._SubProductCodeName

    @SubProductCodeName.setter
    def SubProductCodeName(self, SubProductCodeName):
        self._SubProductCodeName = SubProductCodeName

    @property
    def BillingItemCodeName(self):
        return self._BillingItemCodeName

    @BillingItemCodeName.setter
    def BillingItemCodeName(self, BillingItemCodeName):
        self._BillingItemCodeName = BillingItemCodeName

    @property
    def DosageValue(self):
        return self._DosageValue

    @DosageValue.setter
    def DosageValue(self, DosageValue):
        self._DosageValue = DosageValue

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit


    def _deserialize(self, params):
        self._BucketName = params.get("BucketName")
        self._DosageBeginTime = params.get("DosageBeginTime")
        self._DosageEndTime = params.get("DosageEndTime")
        self._SubProductCodeName = params.get("SubProductCodeName")
        self._BillingItemCodeName = params.get("BillingItemCodeName")
        self._DosageValue = params.get("DosageValue")
        self._Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CostComponentSet(AbstractModel):
    """Consumption component details

    """

    def __init__(self):
        r"""
        :param _ComponentCodeName: Component type name
        :type ComponentCodeName: str
        :param _ItemCodeName: Component name
        :type ItemCodeName: str
        :param _SinglePrice: List price
        :type SinglePrice: str
        :param _PriceUnit: List price unit
        :type PriceUnit: str
        :param _UsedAmount: Usage
        :type UsedAmount: str
        :param _UsedAmountUnit: Usage unit
        :type UsedAmountUnit: str
        :param _Cost: Original price
        :type Cost: str
        :param _Discount: Discount
        :type Discount: str
        :param _RealCost: Discounted price
        :type RealCost: str
        :param _VoucherPayAmount: Voucher payment amount
        :type VoucherPayAmount: str
        :param _CashPayAmount: Cash payment amount
        :type CashPayAmount: str
        :param _IncentivePayAmount: Bonus payment amount
        :type IncentivePayAmount: str
        """
        self._ComponentCodeName = None
        self._ItemCodeName = None
        self._SinglePrice = None
        self._PriceUnit = None
        self._UsedAmount = None
        self._UsedAmountUnit = None
        self._Cost = None
        self._Discount = None
        self._RealCost = None
        self._VoucherPayAmount = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None

    @property
    def ComponentCodeName(self):
        return self._ComponentCodeName

    @ComponentCodeName.setter
    def ComponentCodeName(self, ComponentCodeName):
        self._ComponentCodeName = ComponentCodeName

    @property
    def ItemCodeName(self):
        return self._ItemCodeName

    @ItemCodeName.setter
    def ItemCodeName(self, ItemCodeName):
        self._ItemCodeName = ItemCodeName

    @property
    def SinglePrice(self):
        return self._SinglePrice

    @SinglePrice.setter
    def SinglePrice(self, SinglePrice):
        self._SinglePrice = SinglePrice

    @property
    def PriceUnit(self):
        return self._PriceUnit

    @PriceUnit.setter
    def PriceUnit(self, PriceUnit):
        self._PriceUnit = PriceUnit

    @property
    def UsedAmount(self):
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

    @property
    def UsedAmountUnit(self):
        return self._UsedAmountUnit

    @UsedAmountUnit.setter
    def UsedAmountUnit(self, UsedAmountUnit):
        self._UsedAmountUnit = UsedAmountUnit

    @property
    def Cost(self):
        return self._Cost

    @Cost.setter
    def Cost(self, Cost):
        self._Cost = Cost

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def RealCost(self):
        return self._RealCost

    @RealCost.setter
    def RealCost(self, RealCost):
        self._RealCost = RealCost

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount


    def _deserialize(self, params):
        self._ComponentCodeName = params.get("ComponentCodeName")
        self._ItemCodeName = params.get("ItemCodeName")
        self._SinglePrice = params.get("SinglePrice")
        self._PriceUnit = params.get("PriceUnit")
        self._UsedAmount = params.get("UsedAmount")
        self._UsedAmountUnit = params.get("UsedAmountUnit")
        self._Cost = params.get("Cost")
        self._Discount = params.get("Discount")
        self._RealCost = params.get("RealCost")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CostDetail(AbstractModel):
    """Consumption details data type

    """

    def __init__(self):
        r"""
        :param _PayerUin: Payer UIN
        :type PayerUin: str
        :param _BusinessCodeName: Product name
        :type BusinessCodeName: str
        :param _ProductCodeName: Subproduct name
        :type ProductCodeName: str
        :param _PayModeName: Billing mode name
        :type PayModeName: str
        :param _ProjectName: Project name
        :type ProjectName: str
        :param _RegionName: Region Name
        :type RegionName: str
        :param _ZoneName: Zone name
        :type ZoneName: str
        :param _ResourceId: Resource ID
        :type ResourceId: str
        :param _ResourceName: Resource name
        :type ResourceName: str
        :param _ActionTypeName: Type nameNote: This field may return null, indicating that no valid values can be obtained.
        :type ActionTypeName: str
        :param _OrderId: Order ID
        :type OrderId: str
        :param _BillId: Transaction ID
        :type BillId: str
        :param _FeeBeginTime: Start time of fees
        :type FeeBeginTime: str
        :param _FeeEndTime: End time of fees
        :type FeeEndTime: str
        :param _ComponentSet: Component details
        :type ComponentSet: list of CostComponentSet
        :param _ProductCode: Subproduct name code
        :type ProductCode: str
        """
        self._PayerUin = None
        self._BusinessCodeName = None
        self._ProductCodeName = None
        self._PayModeName = None
        self._ProjectName = None
        self._RegionName = None
        self._ZoneName = None
        self._ResourceId = None
        self._ResourceName = None
        self._ActionTypeName = None
        self._OrderId = None
        self._BillId = None
        self._FeeBeginTime = None
        self._FeeEndTime = None
        self._ComponentSet = None
        self._ProductCode = None

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def BillId(self):
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def FeeBeginTime(self):
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ComponentSet(self):
        return self._ComponentSet

    @ComponentSet.setter
    def ComponentSet(self, ComponentSet):
        self._ComponentSet = ComponentSet

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode


    def _deserialize(self, params):
        self._PayerUin = params.get("PayerUin")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._ProductCodeName = params.get("ProductCodeName")
        self._PayModeName = params.get("PayModeName")
        self._ProjectName = params.get("ProjectName")
        self._RegionName = params.get("RegionName")
        self._ZoneName = params.get("ZoneName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._ActionTypeName = params.get("ActionTypeName")
        self._OrderId = params.get("OrderId")
        self._BillId = params.get("BillId")
        self._FeeBeginTime = params.get("FeeBeginTime")
        self._FeeEndTime = params.get("FeeEndTime")
        if params.get("ComponentSet") is not None:
            self._ComponentSet = []
            for item in params.get("ComponentSet"):
                obj = CostComponentSet()
                obj._deserialize(item)
                self._ComponentSet.append(obj)
        self._ProductCode = params.get("ProductCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAllocationTagRequest(AbstractModel):
    """CreateAllocationTag request structure.

    """

    def __init__(self):
        r"""
        :param _TagKey: Cost allocation tag key.
        :type TagKey: list of str
        """
        self._TagKey = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAllocationTagResponse(AbstractModel):
    """CreateAllocationTag response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteAllocationTagRequest(AbstractModel):
    """DeleteAllocationTag request structure.

    """

    def __init__(self):
        r"""
        :param _TagKey: Cost allocation tag key
        :type TagKey: list of str
        """
        self._TagKey = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAllocationTagResponse(AbstractModel):
    """DeleteAllocationTag response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DescribeAccountBalanceRequest(AbstractModel):
    """DescribeAccountBalance request structure.

    """


class DescribeAccountBalanceResponse(AbstractModel):
    """DescribeAccountBalance response structure.

    """

    def __init__(self):
        r"""
        :param _Balance: Available account balance in cents, which takes the same calculation rules as `RealBalance`, `CreditBalance`, and `RealCreditBalance`.
        :type Balance: int
        :param _Uin: The UIN to query.
        :type Uin: int
        :param _RealBalance: Available account balance in cents, which takes the same calculation rules as `Balance`, `CreditBalance`, and `RealCreditBalance`.
        :type RealBalance: float
        :param _CashAccountBalance: Cash account balance in cents. Currently, this field is not applied.
        :type CashAccountBalance: float
        :param _IncomeIntoAccountBalance: Income account balance in cents. Currently, this field is not applied.
        :type IncomeIntoAccountBalance: float
        :param _PresentAccountBalance: Present account balance in cents. Currently, this field is not applied.
        :type PresentAccountBalance: float
        :param _FreezeAmount: Frozen amount in cents.
        :type FreezeAmount: float
        :param _OweAmount: Overdue amount in cents, which is when the available credit balance is negative.
        :type OweAmount: float
        :param _IsAllowArrears: Whether overdue payments are allowed. Currently, this field is not applied.
        :type IsAllowArrears: bool
        :param _IsCreditLimited: Whether you have a credit limit. Currently, this field is not applied.
        :type IsCreditLimited: bool
        :param _CreditAmount: Credit limit in cents. Credit limit－available credit balance = consumption amount
        :type CreditAmount: float
        :param _CreditBalance: Available credit balance in cents, which takes the same calculation rules as `Balance`, `RealBalance`, and `RealCreditBalance`.
        :type CreditBalance: float
        :param _RealCreditBalance: Available account balance in cents, which takes the same calculation rules as `Balance`, `RealBalance`, and `CreditBalance`.
        :type RealCreditBalance: float
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Balance = None
        self._Uin = None
        self._RealBalance = None
        self._CashAccountBalance = None
        self._IncomeIntoAccountBalance = None
        self._PresentAccountBalance = None
        self._FreezeAmount = None
        self._OweAmount = None
        self._IsAllowArrears = None
        self._IsCreditLimited = None
        self._CreditAmount = None
        self._CreditBalance = None
        self._RealCreditBalance = None
        self._RequestId = None

    @property
    def Balance(self):
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def RealBalance(self):
        return self._RealBalance

    @RealBalance.setter
    def RealBalance(self, RealBalance):
        self._RealBalance = RealBalance

    @property
    def CashAccountBalance(self):
        return self._CashAccountBalance

    @CashAccountBalance.setter
    def CashAccountBalance(self, CashAccountBalance):
        self._CashAccountBalance = CashAccountBalance

    @property
    def IncomeIntoAccountBalance(self):
        return self._IncomeIntoAccountBalance

    @IncomeIntoAccountBalance.setter
    def IncomeIntoAccountBalance(self, IncomeIntoAccountBalance):
        self._IncomeIntoAccountBalance = IncomeIntoAccountBalance

    @property
    def PresentAccountBalance(self):
        return self._PresentAccountBalance

    @PresentAccountBalance.setter
    def PresentAccountBalance(self, PresentAccountBalance):
        self._PresentAccountBalance = PresentAccountBalance

    @property
    def FreezeAmount(self):
        return self._FreezeAmount

    @FreezeAmount.setter
    def FreezeAmount(self, FreezeAmount):
        self._FreezeAmount = FreezeAmount

    @property
    def OweAmount(self):
        return self._OweAmount

    @OweAmount.setter
    def OweAmount(self, OweAmount):
        self._OweAmount = OweAmount

    @property
    def IsAllowArrears(self):
        return self._IsAllowArrears

    @IsAllowArrears.setter
    def IsAllowArrears(self, IsAllowArrears):
        self._IsAllowArrears = IsAllowArrears

    @property
    def IsCreditLimited(self):
        return self._IsCreditLimited

    @IsCreditLimited.setter
    def IsCreditLimited(self, IsCreditLimited):
        self._IsCreditLimited = IsCreditLimited

    @property
    def CreditAmount(self):
        return self._CreditAmount

    @CreditAmount.setter
    def CreditAmount(self, CreditAmount):
        self._CreditAmount = CreditAmount

    @property
    def CreditBalance(self):
        return self._CreditBalance

    @CreditBalance.setter
    def CreditBalance(self, CreditBalance):
        self._CreditBalance = CreditBalance

    @property
    def RealCreditBalance(self):
        return self._RealCreditBalance

    @RealCreditBalance.setter
    def RealCreditBalance(self, RealCreditBalance):
        self._RealCreditBalance = RealCreditBalance

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Balance = params.get("Balance")
        self._Uin = params.get("Uin")
        self._RealBalance = params.get("RealBalance")
        self._CashAccountBalance = params.get("CashAccountBalance")
        self._IncomeIntoAccountBalance = params.get("IncomeIntoAccountBalance")
        self._PresentAccountBalance = params.get("PresentAccountBalance")
        self._FreezeAmount = params.get("FreezeAmount")
        self._OweAmount = params.get("OweAmount")
        self._IsAllowArrears = params.get("IsAllowArrears")
        self._IsCreditLimited = params.get("IsCreditLimited")
        self._CreditAmount = params.get("CreditAmount")
        self._CreditBalance = params.get("CreditBalance")
        self._RealCreditBalance = params.get("RealCreditBalance")
        self._RequestId = params.get("RequestId")


class DescribeBillDetailForOrganizationRequest(AbstractModel):
    """DescribeBillDetailForOrganization request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination offset. If `Offset` is `0`, it indicates the first page. When `Limit` is `100`, if `Offset` is `100`, it indicates the second page; if `Offset` is `200`, it indicates the third page, and so on.
        :type Offset: int
        :param _Limit: The number of entries returned at a time. The maximum value is `100`.
        :type Limit: int
        :param _PeriodType: Cycle type, which can be `byUsedTime` (by billing cycle) or `byPayTime` (by deduction time). This value must be the same as the billing period type in Billing Center for that particular month. You can check your billing cycle at the top of the [Bill Overview](https://console.cloud.tencent.com/expense/bill/overview) page.
        :type PeriodType: str
        :param _Month: The month is in the format of yyyy-mm. Either Month or BeginTime&EndTime must be specified. If BeginTime&EndTime is specified, the Month field is invalid. Data within the last 18 months can be pulled at most.
        :type Month: str
        :param _BeginTime: The start time of the period in the format of yyyy-mm-dd hh:ii:ss. Either Month or BeginTime&EndTime must be specified. If BeginTime&EndTime is specified, the Month field is invalid. BeginTime and EndTime must be specified together and must be in the same month. Cross-month queries are not supported and the query results are data for the entire month. Data within the last 18 months can be pulled at most.
        :type BeginTime: str
        :param _EndTime: The end time of the period in the format of yyyy-mm-dd hh:ii:ss. Either Month or BeginTime&EndTime must be specified. If BeginTime&EndTime is specified, the Month field is invalid. BeginTime and EndTime must be specified together and must be in the same month. Cross-month queries are not supported and the query results are data for the entire month. Data within the last 18 months can be pulled at most.
        :type EndTime: str
        :param _NeedRecordNum: Indicates whether the total number of records is required, used for pagination.
Valid values: `1` (required), `0` (not required).
        :type NeedRecordNum: int
        :param _PayMode: Billing mode, which can be `prePay` (monthly subscription) or `postPay` (pay-as-you-go).
        :type PayMode: str
        :param _ResourceId: ID of the instance to be queried.
        :type ResourceId: str
        :param _ActionType: Transaction type. This parameter needs to be input using the `ActionTypeName` value. Valid values:
Monthly subscription purchase
Monthly subscription renewal
Monthly subscription upgrade/downgrade
Monthly subscription refund 
Pay-as-you-go deduction 
Offline project deduction 
Offline product deduction 
Adjustment deduction 
Adjustment compensation 
Hourly pay-as-you-go 
Daily pay-as-you-go 
Monthly pay-as-you-go 
Hourly spot instance 
Offline project adjustment compensation 
Offline product adjustment compensation 
Offer deduction 
Offer compensation 
Pay-as-you-go resource migration in 
Pay-as-you-go resource migration out 
Monthly subscription resource migration in 
Monthly subscription resource migration out 
Prepaid 
Hourly 
RI refund 
Pay-as-you-go reversal 
Monthly subscription to pay-as-you-go 
Minimum spend deduction 
Hourly savings plan fee
        :type ActionType: str
        :param _ProjectId: Project ID: The ID of the project to which the resource belongs.
        :type ProjectId: int
        :param _BusinessCode: Product code.
Note: To query the product codes used in the current month, call <a href="https://intl.cloud.tencent.com/document/product/555/35761?from_cn_redirect=1">DescribeBillSummaryByProduct</a>.
        :type BusinessCode: str
        :param _Context: Context information returned by the last response. You can view multiple pages when querying for data after May 2023 to speed up the query. We recommend you use this query method if your data volume is above 100 thousand entries, which can improve query speed by 2-10 times.
        :type Context: str
        """
        self._Offset = None
        self._Limit = None
        self._PeriodType = None
        self._Month = None
        self._BeginTime = None
        self._EndTime = None
        self._NeedRecordNum = None
        self._PayMode = None
        self._ResourceId = None
        self._ActionType = None
        self._ProjectId = None
        self._BusinessCode = None
        self._Context = None

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
    def PeriodType(self):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        self._PeriodType = PeriodType

    @property
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NeedRecordNum(self):
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PeriodType = params.get("PeriodType")
        self._Month = params.get("Month")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._NeedRecordNum = params.get("NeedRecordNum")
        self._PayMode = params.get("PayMode")
        self._ResourceId = params.get("ResourceId")
        self._ActionType = params.get("ActionType")
        self._ProjectId = params.get("ProjectId")
        self._BusinessCode = params.get("BusinessCode")
        self._Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillDetailForOrganizationResponse(AbstractModel):
    """DescribeBillDetailForOrganization response structure.

    """

    def __init__(self):
        r"""
        :param _DetailSet: Details list.
        :type DetailSet: list of DistributionBillDetail
        :param _Total: Total number of records, which is cached every 24 hours and may be less than the actual total number of records.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _Context: Context information of the current request, which can be used in the parameters of the next request to speed up the query.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Context: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DetailSet = None
        self._Total = None
        self._Context = None
        self._RequestId = None

    @property
    def DetailSet(self):
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DetailSet") is not None:
            self._DetailSet = []
            for item in params.get("DetailSet"):
                obj = DistributionBillDetail()
                obj._deserialize(item)
                self._DetailSet.append(obj)
        self._Total = params.get("Total")
        self._Context = params.get("Context")
        self._RequestId = params.get("RequestId")


class DescribeBillDetailRequest(AbstractModel):
    """DescribeBillDetail request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Quantity, maximum is 100
        :type Limit: int
        :param _PeriodType: The period type. byUsedTime: By usage period; byPayTime: By payment period. Must be the same as the period of the current monthly bill of the Billing Center. You can check your bill statistics period type at the top of the [Bill Overview](https://console.cloud.tencent.com/expense/bill/overview) page. 
        :type PeriodType: str
        :param _Month: Month; format: yyyy-mm. You only have to enter either Month or BeginTime and EndTime. When you enter values for BeginTime and EndTime, Month becomes invalid. This value must be no earlier than the month when Bill 2.0 is activated; last 24 months data are available.
        :type Month: str
        :param _BeginTime: The start time of the query range, which should be in the format Y-m-d H:i:s . The query range must be in the last 18 months and cannot be earlier than May 2018 (when Bill 2.0 was introduced). The start time and end time must be in the same month.

Example: tccli billing DescribeBillDetail --cli-unfold-argument --Offset 1 --Limit 100 --BeginTime '2023-04-01 12:05:15' --EndTime '2023-04-18 12:00:10' --ProjectId 1000000731  --version "2018-07-09"

Alternatively, you can use Month to query the billing details of a month.
Example:
ccli billing DescribeBillDetail --cli-unfold-argument --Offset 1 --Limit 100 --Month 2023-04  --version "2018-07-09" --ResourceId "disk-oj9okstm"
        :type BeginTime: str
        :param _EndTime: The end time of the query range, which should be in the format `Y-m-d H:i:s `. The query range must be in the last 18 months and cannot be earlier than May 2018 (when Bill 2.0 was introduced). The start time and end time must be in the same month.

Example: tccli billing DescribeBillDetail --cli-unfold-argument --Offset 1 --Limit 100 --BeginTime '2023-04-01 12:05:15' --EndTime '2023-04-18 12:00:10' --ProjectId 1000000731  --version "2018-07-09"

Alternatively, you can use `Month` to query the billing details of a month. 
Example:
ccli billing DescribeBillDetail --cli-unfold-argument --Offset 1 --Limit 100 --Month 2023-04  --version "2018-07-09" --ResourceId "disk-oj9okstm"
        :type EndTime: str
        :param _NeedRecordNum: Indicates whether or not the total number of records of accessing the list is required, used for frontend pages.
1 = yes, 0 = no
        :type NeedRecordNum: int
        :param _ProductCode: Queries information on a specified product
        :type ProductCode: str
        :param _PayMode: Billing mode: prePay/postPay
        :type PayMode: str
        :param _ResourceId: Queries information on a specified resource
        :type ResourceId: str
        :param _ActionType: Action type to query. Valid values:
Purchase
Renewal
Modify
Refund
Deduction
Hourly settlement
Daily settlement
Monthly settlement
Offline project deduction
Offline deduction
adjust-CR
adjust-DR
One-off RI Fee
Spot
Hourly RI fee
New monthly subscription
Monthly subscription renewal
Monthly subscription specification adjustment
Monthly subscription specification adjustment
Monthly subscription refund
        :type ActionType: str
        :param _ProjectId: Project ID: ID of the project to which the resource belongs
        :type ProjectId: int
        :param _BusinessCode: Product code
Note: To query the product codes used in the current month, call <a href="https://intl.cloud.tencent.com/document/product/555/35761?from_cn_redirect=1">DescribeBillSummaryByProduct</a>.
        :type BusinessCode: str
        :param _Context: Context information returned by the last request. You can set `Month` to `2023-05` or later to accelerate queries. We recommend users whose data volume is over 100 thousand entries use the paginated query feature, which can help greatly speed up your queries.
        :type Context: str
        :param _PayerUin: The account ID of the payer, which is the unique identifier of a Tencent Cloud user. This account is allowed to query its own bills by default. If an organization admin account needs to query the self-pay bills of members, this field should be specified as the member account ID.
        :type PayerUin: str
        """
        self._Offset = None
        self._Limit = None
        self._PeriodType = None
        self._Month = None
        self._BeginTime = None
        self._EndTime = None
        self._NeedRecordNum = None
        self._ProductCode = None
        self._PayMode = None
        self._ResourceId = None
        self._ActionType = None
        self._ProjectId = None
        self._BusinessCode = None
        self._Context = None
        self._PayerUin = None

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
    def PeriodType(self):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        self._PeriodType = PeriodType

    @property
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NeedRecordNum(self):
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PeriodType = params.get("PeriodType")
        self._Month = params.get("Month")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._NeedRecordNum = params.get("NeedRecordNum")
        self._ProductCode = params.get("ProductCode")
        self._PayMode = params.get("PayMode")
        self._ResourceId = params.get("ResourceId")
        self._ActionType = params.get("ActionType")
        self._ProjectId = params.get("ProjectId")
        self._BusinessCode = params.get("BusinessCode")
        self._Context = params.get("Context")
        self._PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillDetailResponse(AbstractModel):
    """DescribeBillDetail response structure.

    """

    def __init__(self):
        r"""
        :param _DetailSet: Details list
        :type DetailSet: list of BillDetail
        :param _Total: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _Context: Note: This field may return null, indicating that no valid values can be obtained.
        :type Context: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DetailSet = None
        self._Total = None
        self._Context = None
        self._RequestId = None

    @property
    def DetailSet(self):
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DetailSet") is not None:
            self._DetailSet = []
            for item in params.get("DetailSet"):
                obj = BillDetail()
                obj._deserialize(item)
                self._DetailSet.append(obj)
        self._Total = params.get("Total")
        self._Context = params.get("Context")
        self._RequestId = params.get("RequestId")


class DescribeBillDownloadUrlRequest(AbstractModel):
    """DescribeBillDownloadUrl request structure.

    """

    def __init__(self):
        r"""
        :param _FileType: Bill type. Valid values:
`billOverview` (L0: PDF bills)
`billSummary` (L1: Bill summary)	
`billResource` (L2: Bill by instance)	
`billDetail` (L3: Bill details)	
`billPack` (Bill packs)
        :type FileType: str
        :param _Month: Bill month.
The earliest month that can be queried is January 2021.
L0 bills and bill packs cannot be downloaded for the current month. Please download the current month's bills after it is generated at 19:00 on the 1st day of the next month.
        :type Month: str
        :param _ChildUin: List of account IDs for downloading the bill. By default, it queries the bill for the current account. If you are an admin account and need to download bills for member accounts with their own payment, input the member account's UIN for this parameter.
        :type ChildUin: list of str
        """
        self._FileType = None
        self._Month = None
        self._ChildUin = None

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def ChildUin(self):
        return self._ChildUin

    @ChildUin.setter
    def ChildUin(self, ChildUin):
        self._ChildUin = ChildUin


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._Month = params.get("Month")
        self._ChildUin = params.get("ChildUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillDownloadUrlResponse(AbstractModel):
    """DescribeBillDownloadUrl response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: Indicates whether the bill file is ready. Valid values: `0` (the file is being generated), `1` (the file has been generated).
        :type Ready: int
        :param _DownloadUrl: Billing file download link, valid for 1 day. Note: This field may return null, indicating that no valid values can be obtained.
        :type DownloadUrl: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ready = None
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class DescribeBillResourceSummaryForOrganizationRequest(AbstractModel):
    """DescribeBillResourceSummaryForOrganization request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination offset. If `Offset` is `0`, it indicates the first page. When `Limit` is `100`, if `Offset` is `100`, it indicates the second page; if `Offset` is `200`, it indicates the third page, and so on.
        :type Offset: int
        :param _Limit: The number of entries returned at a time. The maximum value is `1000`.
        :type Limit: int
        :param _Month: Bill month in the format of "yyyy-mm". This value must be no earlier than the month when Bill 2.0 is activated.
        :type Month: str
        :param _PeriodType: Cycle type, which can be `byUsedTime` (by billing cycle) or `byPayTime` (by deduction time). This value must be the same as the billing period type in Billing Center for that particular month. You can check your billing cycle at the top of the [Bill Overview](https://console.cloud.tencent.com/expense/bill/overview) page.
        :type PeriodType: str
        :param _NeedRecordNum: Indicates whether the total number of records is required, used for pagination.
Valid values: `1` (required), `0` (not required).
        :type NeedRecordNum: int
        :param _ActionType: Transaction type. This parameter needs to be input using the `ActionTypeName` value. Valid values:
Monthly subscription purchase
Monthly subscription renewal
Monthly subscription upgrade/downgrade
Monthly subscription refund 
Pay-as-you-go deduction 
Offline project deduction 
Offline product deduction 
Adjustment deduction 
Adjustment compensation 
Hourly pay-as-you-go 
Daily pay-as-you-go 
Monthly pay-as-you-go 
Hourly spot instance 
Offline project adjustment compensation 
Offline product adjustment compensation 
Offer deduction 
Offer compensation 
Pay-as-you-go resource migration in 
Pay-as-you-go resource migration out 
Monthly subscription resource migration in 
Monthly subscription resource migration out 
Prepaid 
Hourly 
RI refund 
Pay-as-you-go reversal 
Monthly subscription to pay-as-you-go 
Minimum spend deduction 
Hourly savings plan fee
        :type ActionType: str
        :param _ResourceId: ID of the instance to be queried.
        :type ResourceId: str
        :param _PayMode: Billing mode. Valid values: `prePay`, `postPay`.
        :type PayMode: str
        :param _BusinessCode: Product code
Note: To query the product codes (`BusinessCode`) used in the current month, call <a href="https://intl.cloud.tencent.com/document/product/555/35761?from_cn_redirect=1">DescribeBillSummaryByProduct</a>.
        :type BusinessCode: str
        :param _TagKey: Cost allocation tag key, which can be customized. This parameter can be used for querying bills after January 2021.
        :type TagKey: str
        :param _TagValue: Resource tag value. If it is left empty, there are no records with tag values set under this tag key.
This parameter can be used for querying bills after January 2021.
        :type TagValue: str
        """
        self._Offset = None
        self._Limit = None
        self._Month = None
        self._PeriodType = None
        self._NeedRecordNum = None
        self._ActionType = None
        self._ResourceId = None
        self._PayMode = None
        self._BusinessCode = None
        self._TagKey = None
        self._TagValue = None

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
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PeriodType(self):
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType

    @property
    def NeedRecordNum(self):
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Month = params.get("Month")
        self._PeriodType = params.get("PeriodType")
        self._NeedRecordNum = params.get("NeedRecordNum")
        self._ActionType = params.get("ActionType")
        self._ResourceId = params.get("ResourceId")
        self._PayMode = params.get("PayMode")
        self._BusinessCode = params.get("BusinessCode")
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillResourceSummaryForOrganizationResponse(AbstractModel):
    """DescribeBillResourceSummaryForOrganization response structure.

    """

    def __init__(self):
        r"""
        :param _ResourceSummarySet: Resource summary list.
        :type ResourceSummarySet: list of BillDistributionResourceSummary
        :param _Total: Total number of resource summary lists. It will not be returned if `NeedRecordNum` is `0`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ResourceSummarySet = None
        self._Total = None
        self._RequestId = None

    @property
    def ResourceSummarySet(self):
        return self._ResourceSummarySet

    @ResourceSummarySet.setter
    def ResourceSummarySet(self, ResourceSummarySet):
        self._ResourceSummarySet = ResourceSummarySet

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResourceSummarySet") is not None:
            self._ResourceSummarySet = []
            for item in params.get("ResourceSummarySet"):
                obj = BillDistributionResourceSummary()
                obj._deserialize(item)
                self._ResourceSummarySet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeBillResourceSummaryRequest(AbstractModel):
    """DescribeBillResourceSummary request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination offset. If `Offset` is `0`, it indicates the first page. If `Limit` is `100`, "`Offset` = `100`" indicates the second page, then "`Offset` = `200`" indicates the third page, and so on.
        :type Offset: int
        :param _Limit: Quantity, maximum is 1000
        :type Limit: int
        :param _Month: Bill month in the format of "yyyy-mm". This value must be no earlier than March 2019, when Bill 2.0 was launched.
        :type Month: str
        :param _PeriodType: The period type. byUsedTime: By usage period; byPayTime: by payment period. Must be the same as the period of the current monthly bill of the Billing Center. You can check your bill statistics period type at the top of the [Bill Overview](https://console.cloud.tencent.com/expense/bill/overview) page.
        :type PeriodType: str
        :param _NeedRecordNum: Indicates whether or not the total number of records of accessing the list is required, used for frontend pages.
1 = yes, 0 = no
        :type NeedRecordNum: int
        :param _ActionType: Action type to query. Valid values:
Purchase
Renewal
Modify
Refund
Deduction
Hourly settlement
Daily settlement
Monthly settlement
Offline project deduction
Offline deduction
adjust-CR
adjust-DR
One-off RI Fee
Spot
Hourly RI fee
New monthly subscription
Monthly subscription renewal
Monthly subscription specification adjustment
Monthly subscription refund
        :type ActionType: str
        :param _ResourceId: ID of the instance to be queried
        :type ResourceId: str
        :param _PayMode: Billing mode. Valid values: `prePay` (prepaid), `postPay` (postpaid)
        :type PayMode: str
        :param _BusinessCode: Product code
Note: To query the product codes used in the current month, call <a href="https://intl.cloud.tencent.com/document/product/555/35761?from_cn_redirect=1">DescribeBillSummaryByProduct</a>.
        :type BusinessCode: str
        :param _PayerUin: The account ID of the payer, which is the unique identifier of a Tencent Cloud user. This account is allowed to query its own bills by default. If an organization admin account needs to query the self-pay bills of members, this field should be specified as the member account ID.
        :type PayerUin: str
        :param _TagKey: Cost allocation tag key, which can be customized. This parameter can be used for querying bills after January 2021.
        :type TagKey: str
        :param _TagValue: Resource tag value. If it is left empty, there are no records with tag values set under this tag key.
This parameter can be used for querying bills after January 2021.
        :type TagValue: str
        """
        self._Offset = None
        self._Limit = None
        self._Month = None
        self._PeriodType = None
        self._NeedRecordNum = None
        self._ActionType = None
        self._ResourceId = None
        self._PayMode = None
        self._BusinessCode = None
        self._PayerUin = None
        self._TagKey = None
        self._TagValue = None

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
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PeriodType(self):
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType

    @property
    def NeedRecordNum(self):
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Month = params.get("Month")
        self._PeriodType = params.get("PeriodType")
        self._NeedRecordNum = params.get("NeedRecordNum")
        self._ActionType = params.get("ActionType")
        self._ResourceId = params.get("ResourceId")
        self._PayMode = params.get("PayMode")
        self._BusinessCode = params.get("BusinessCode")
        self._PayerUin = params.get("PayerUin")
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillResourceSummaryResponse(AbstractModel):
    """DescribeBillResourceSummary response structure.

    """

    def __init__(self):
        r"""
        :param _ResourceSummarySet: Resource summary list
        :type ResourceSummarySet: list of BillResourceSummary
        :param _Total: Total number of resource summary lists, which will not be returned when `NeedRecordNum` is `0`. This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ResourceSummarySet = None
        self._Total = None
        self._RequestId = None

    @property
    def ResourceSummarySet(self):
        return self._ResourceSummarySet

    @ResourceSummarySet.setter
    def ResourceSummarySet(self, ResourceSummarySet):
        self._ResourceSummarySet = ResourceSummarySet

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResourceSummarySet") is not None:
            self._ResourceSummarySet = []
            for item in params.get("ResourceSummarySet"):
                obj = BillResourceSummary()
                obj._deserialize(item)
                self._ResourceSummarySet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryByPayModeRequest(AbstractModel):
    """DescribeBillSummaryByPayMode request structure.

    """

    def __init__(self):
        r"""
        :param _BeginTime: The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type BeginTime: str
        :param _EndTime: The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type EndTime: str
        :param _PayerUin: Query bill data user's UIN
        :type PayerUin: str
        """
        self._BeginTime = None
        self._EndTime = None
        self._PayerUin = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByPayModeResponse(AbstractModel):
    """DescribeBillSummaryByPayMode response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: Indicates whether the data is ready. `0`: Not ready. `1`: Ready. If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first time. Wait for 5-10 minutes and try again.
        :type Ready: int
        :param _SummaryOverview: Detailed cost distribution for all billing modes
Note: This field may return null, indicating that no valid value was found.
        :type SummaryOverview: list of PayModeSummaryOverviewItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryOverview = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryOverview(self):
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self._SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = PayModeSummaryOverviewItem()
                obj._deserialize(item)
                self._SummaryOverview.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryByProductRequest(AbstractModel):
    """DescribeBillSummaryByProduct request structure.

    """

    def __init__(self):
        r"""
        :param _BeginTime: The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type BeginTime: str
        :param _EndTime: The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type EndTime: str
        :param _PayerUin: Queries bill data user's UIN
        :type PayerUin: str
        :param _PayType: A bill type, which corresponds to a subtotal type of L0 bills.
This parameter has become valid since v3.0 bills took effect in May 2021.
Valid values:
`consume`: consumption
`refund`: refund
`adjustment`: bill adjustment
        :type PayType: str
        """
        self._BeginTime = None
        self._EndTime = None
        self._PayerUin = None
        self._PayType = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._PayerUin = params.get("PayerUin")
        self._PayType = params.get("PayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByProductResponse(AbstractModel):
    """DescribeBillSummaryByProduct response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: Indicates whether the data is ready. `0`: Not ready. `1`: Ready. If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first time. Wait for 5-10 minutes and try again.
        :type Ready: int
        :param _SummaryTotal: Total cost details
Note: This field may return null, indicating that no valid value was found.
        :type SummaryTotal: :class:`tencentcloud.billing.v20180709.models.BusinessSummaryTotal`
        :param _SummaryOverview: Cost distribution of all products
Note: This field may return null, indicating that no valid value was found.
        :type SummaryOverview: list of BusinessSummaryOverviewItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryTotal = None
        self._SummaryOverview = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryTotal(self):
        return self._SummaryTotal

    @SummaryTotal.setter
    def SummaryTotal(self, SummaryTotal):
        self._SummaryTotal = SummaryTotal

    @property
    def SummaryOverview(self):
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("SummaryTotal") is not None:
            self._SummaryTotal = BusinessSummaryTotal()
            self._SummaryTotal._deserialize(params.get("SummaryTotal"))
        if params.get("SummaryOverview") is not None:
            self._SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = BusinessSummaryOverviewItem()
                obj._deserialize(item)
                self._SummaryOverview.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryByProjectRequest(AbstractModel):
    """DescribeBillSummaryByProject request structure.

    """

    def __init__(self):
        r"""
        :param _BeginTime: The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type BeginTime: str
        :param _EndTime: The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type EndTime: str
        :param _PayerUin: Queries bill data user's UIN
        :type PayerUin: str
        """
        self._BeginTime = None
        self._EndTime = None
        self._PayerUin = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByProjectResponse(AbstractModel):
    """DescribeBillSummaryByProject response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: Indicates whether the data is ready. `0`: Not ready. `1`: Ready. If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first time. Wait for 5-10 minutes and try again.
        :type Ready: int
        :param _SummaryOverview: Detailed cost distribution for all projects
Note: This field may return null, indicating that no valid value was found.
        :type SummaryOverview: list of ProjectSummaryOverviewItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryOverview = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryOverview(self):
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self._SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = ProjectSummaryOverviewItem()
                obj._deserialize(item)
                self._SummaryOverview.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryByRegionRequest(AbstractModel):
    """DescribeBillSummaryByRegion request structure.

    """

    def __init__(self):
        r"""
        :param _BeginTime: The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type BeginTime: str
        :param _EndTime: The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type EndTime: str
        :param _PayerUin: Queries bill data user's UIN
        :type PayerUin: str
        """
        self._BeginTime = None
        self._EndTime = None
        self._PayerUin = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByRegionResponse(AbstractModel):
    """DescribeBillSummaryByRegion response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: Indicates whether the data is ready. `0`: Not ready. `1`: Ready. If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first time. Wait for 5-10 minutes and try again.
        :type Ready: int
        :param _SummaryOverview: Detailed cost distribution for all regions
Note: This field may return null, indicating that no valid value was found.
        :type SummaryOverview: list of RegionSummaryOverviewItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryOverview = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryOverview(self):
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self._SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = RegionSummaryOverviewItem()
                obj._deserialize(item)
                self._SummaryOverview.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryByTagRequest(AbstractModel):
    """DescribeBillSummaryByTag request structure.

    """

    def __init__(self):
        r"""
        :param _BeginTime: The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type BeginTime: str
        :param _EndTime: The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type EndTime: str
        :param _TagKey: Cost allocation tag key, which can be customized.
        :type TagKey: str
        :param _PayerUin: Payer UIN
        :type PayerUin: str
        :param _TagValue: Resource tag value
        :type TagValue: str
        """
        self._BeginTime = None
        self._EndTime = None
        self._TagKey = None
        self._PayerUin = None
        self._TagValue = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._TagKey = params.get("TagKey")
        self._PayerUin = params.get("PayerUin")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByTagResponse(AbstractModel):
    """DescribeBillSummaryByTag response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: Indicates whether the data is ready. `0`: Not ready. `1`: Ready. If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first time. Wait for 5-10 minutes and try again.
        :type Ready: int
        :param _SummaryOverview: Details about cost distribution over different tags
Note: This field may return null, indicating that no valid values can be obtained.
        :type SummaryOverview: list of TagSummaryOverviewItem
        :param _SummaryTotal: Total cost
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SummaryTotal: :class:`tencentcloud.billing.v20180709.models.SummaryTotal`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryOverview = None
        self._SummaryTotal = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryOverview(self):
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

    @property
    def SummaryTotal(self):
        return self._SummaryTotal

    @SummaryTotal.setter
    def SummaryTotal(self, SummaryTotal):
        self._SummaryTotal = SummaryTotal

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self._SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = TagSummaryOverviewItem()
                obj._deserialize(item)
                self._SummaryOverview.append(obj)
        if params.get("SummaryTotal") is not None:
            self._SummaryTotal = SummaryTotal()
            self._SummaryTotal._deserialize(params.get("SummaryTotal"))
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryForOrganizationRequest(AbstractModel):
    """DescribeBillSummaryForOrganization request structure.

    """

    def __init__(self):
        r"""
        :param _Month: Bill month in the format of "yyyy-mm".
        :type Month: str
        :param _GroupType: Bill dimension. Valid values: `business`, `project`, `region`, `payMode`, and `tag`.
        :type GroupType: str
        :param _TagKey: Tag key. Pass in it when `GroupType` is `tag`.
        :type TagKey: list of str
        """
        self._Month = None
        self._GroupType = None
        self._TagKey = None

    @property
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def GroupType(self):
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._GroupType = params.get("GroupType")
        self._TagKey = params.get("TagKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryForOrganizationResponse(AbstractModel):
    """DescribeBillSummaryForOrganization response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: Indicates whether the data is ready. Valid values: `0` (not ready), `1` (ready). If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first time. Wait for 5-10 minutes and try again.
        :type Ready: int
        :param _SummaryDetail: Bills summarized by multiple dimensions.
        :type SummaryDetail: list of SummaryDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryDetail = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryDetail(self):
        return self._SummaryDetail

    @SummaryDetail.setter
    def SummaryDetail(self, SummaryDetail):
        self._SummaryDetail = SummaryDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("SummaryDetail") is not None:
            self._SummaryDetail = []
            for item in params.get("SummaryDetail"):
                obj = SummaryDetail()
                obj._deserialize(item)
                self._SummaryDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryRequest(AbstractModel):
    """DescribeBillSummary request structure.

    """

    def __init__(self):
        r"""
        :param _Month: Bill month in the format of "yyyy-mm"
        :type Month: str
        :param _GroupType: Bill dimension. Valid values: `business`, `project`, `region`, `payMode`, and `tag`
        :type GroupType: str
        :param _TagKey: Tag key, which is used when `GroupType` is `tag`.
        :type TagKey: list of str
        """
        self._Month = None
        self._GroupType = None
        self._TagKey = None

    @property
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def GroupType(self):
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._GroupType = params.get("GroupType")
        self._TagKey = params.get("TagKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryResponse(AbstractModel):
    """DescribeBillSummary response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: Indicates whether the data is ready. `0`: Not ready. `1`: Ready. If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first time. Wait for 5-10 minutes and try again.
        :type Ready: int
        :param _SummaryDetail: Detailed summary of costs by multiple dimensions
        :type SummaryDetail: list of SummaryDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryDetail = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryDetail(self):
        return self._SummaryDetail

    @SummaryDetail.setter
    def SummaryDetail(self, SummaryDetail):
        self._SummaryDetail = SummaryDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("SummaryDetail") is not None:
            self._SummaryDetail = []
            for item in params.get("SummaryDetail"):
                obj = SummaryDetail()
                obj._deserialize(item)
                self._SummaryDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCostDetailRequest(AbstractModel):
    """DescribeCostDetail request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: The number of entries returned at a time. The maximum value is `100`.
        :type Limit: int
        :param _Offset: Offset
        :type Offset: int
        :param _BeginTime: Cycle start time in the format of yyyy-mm-dd hh:ii:ss. Either Month or BeginTime&EndTime must be entered, and if this field is present, Month becomes invalid. BeginTime and EndTime must be entered together, and must be in the same month. Cross-month retrieval is not currently supported. Data retrievable is the data after cost analysis is activated and within the past 24 months.
        :type BeginTime: str
        :param _EndTime: Cycle end time in the format of yyyy-mm-dd hh:ii:ss. Either Month or BeginTime&EndTime must be entered, and if this field is present, Month becomes invalid. BeginTime and EndTime must be entered together, and must be in the same month. Cross-month retrieval is not currently supported. Data retrievable is the data after cost analysis is activated and within the past 24 months.
        :type EndTime: str
        :param _NeedRecordNum: Whether the total number of records in the list is needed, for frontend pagination1: needed, 0: not needed
        :type NeedRecordNum: int
        :param _Month: Month, in the format of yyyy-mm. Either Month or BeginTime&EndTime must be entered, and if BeginTime&EndTime is entered, Month becomes invalid. It cannot be earlier than the month when cost analysis is activated. Data of up to 24 months can be retrieved.
        :type Month: str
        :param _ProductCode: Used to query information of a specified product (currently not available)
        :type ProductCode: str
        :param _PayMode: Payment mode. Options include prePay and postPay.
        :type PayMode: str
        :param _ResourceId: Used to query information of a specified resource
        :type ResourceId: str
        """
        self._Limit = None
        self._Offset = None
        self._BeginTime = None
        self._EndTime = None
        self._NeedRecordNum = None
        self._Month = None
        self._ProductCode = None
        self._PayMode = None
        self._ResourceId = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NeedRecordNum(self):
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._NeedRecordNum = params.get("NeedRecordNum")
        self._Month = params.get("Month")
        self._ProductCode = params.get("ProductCode")
        self._PayMode = params.get("PayMode")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCostDetailResponse(AbstractModel):
    """DescribeCostDetail response structure.

    """

    def __init__(self):
        r"""
        :param _DetailSet: Consumption details
Note: This field may return null, indicating that no valid values can be obtained.
        :type DetailSet: list of CostDetail
        :param _Total: Record countNote: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DetailSet = None
        self._Total = None
        self._RequestId = None

    @property
    def DetailSet(self):
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DetailSet") is not None:
            self._DetailSet = []
            for item in params.get("DetailSet"):
                obj = CostDetail()
                obj._deserialize(item)
                self._DetailSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeCostExplorerSummaryRequest(AbstractModel):
    """DescribeCostExplorerSummary request structure.

    """

    def __init__(self):
        r"""
        :param _BeginTime: The start time of the period in the format of yyyy-mm-dd hh:ii:ss.
        :type BeginTime: str
        :param _EndTime: The end time of the period in the format of yyyy-mm-dd hh:ii:ss.
        :type EndTime: str
        :param _BillType: Bill type: 1-cost bill, 2-consumption bill
        :type BillType: str
        :param _PeriodType: Statistical period: day-day, month-month;
        :type PeriodType: str
        :param _Dimensions: Classification dimension (data aggregation dimension). Query classification dimension. (Use classification dimension code input parameter.) Input parameter enumeration value:default = Total only
feeType = Fee typebillType = Bill typebusiness = Product
product = Sub-productregion=Region
zone = Availability zoneactionType = Transaction typepayMode = Billing modetags = Tagproject = ProjectpayerUin = Payer accountownerUin = User account
        :type Dimensions: str
        :param _FeeType: Fee type: cost-total cost, totalCost-original price cost
        :type FeeType: str
        :param _PageSize: Quantity. The maximum value per page is 100.
        :type PageSize: int
        :param _PageNo: Starting page, where PageNo=1 indicates the first page, PageNo=2 indicates the second page, and so on.
        :type PageNo: int
        :param _TagKeyStr: Cost allocation tag value
        :type TagKeyStr: str
        :param _NeedConditionValue: Whether the filter box is needed: 1- indicates it is needed, 0- indicates it is not needed. If it is not specified, it is not required by default.
        :type NeedConditionValue: str
        :param _Conditions: Filter parameters
        :type Conditions: :class:`tencentcloud.billing.v20180709.models.AnalyseConditions`
        """
        self._BeginTime = None
        self._EndTime = None
        self._BillType = None
        self._PeriodType = None
        self._Dimensions = None
        self._FeeType = None
        self._PageSize = None
        self._PageNo = None
        self._TagKeyStr = None
        self._NeedConditionValue = None
        self._Conditions = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def BillType(self):
        return self._BillType

    @BillType.setter
    def BillType(self, BillType):
        self._BillType = BillType

    @property
    def PeriodType(self):
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def FeeType(self):
        return self._FeeType

    @FeeType.setter
    def FeeType(self, FeeType):
        self._FeeType = FeeType

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNo(self):
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def TagKeyStr(self):
        return self._TagKeyStr

    @TagKeyStr.setter
    def TagKeyStr(self, TagKeyStr):
        self._TagKeyStr = TagKeyStr

    @property
    def NeedConditionValue(self):
        return self._NeedConditionValue

    @NeedConditionValue.setter
    def NeedConditionValue(self, NeedConditionValue):
        self._NeedConditionValue = NeedConditionValue

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._BillType = params.get("BillType")
        self._PeriodType = params.get("PeriodType")
        self._Dimensions = params.get("Dimensions")
        self._FeeType = params.get("FeeType")
        self._PageSize = params.get("PageSize")
        self._PageNo = params.get("PageNo")
        self._TagKeyStr = params.get("TagKeyStr")
        self._NeedConditionValue = params.get("NeedConditionValue")
        if params.get("Conditions") is not None:
            self._Conditions = AnalyseConditions()
            self._Conditions._deserialize(params.get("Conditions"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCostExplorerSummaryResponse(AbstractModel):
    """DescribeCostExplorerSummary response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Number of data entries
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _Header: Header informationNote: This field may return null, indicating that no valid values can be obtained.
        :type Header: :class:`tencentcloud.billing.v20180709.models.AnalyseHeaderDetail`
        :param _Detail: Data detailsNote: This field may return null, indicating that no valid values can be obtained.
        :type Detail: list of AnalyseDetail
        :param _TotalDetail: Data amountNote: This field may return null, indicating that no valid values can be obtained.
        :type TotalDetail: :class:`tencentcloud.billing.v20180709.models.AnalyseDetail`
        :param _ConditionValue: Filter boxNote: This field may return null, indicating that no valid values can be obtained.
        :type ConditionValue: :class:`tencentcloud.billing.v20180709.models.AnalyseConditionDetail`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Header = None
        self._Detail = None
        self._TotalDetail = None
        self._ConditionValue = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Header(self):
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def TotalDetail(self):
        return self._TotalDetail

    @TotalDetail.setter
    def TotalDetail(self, TotalDetail):
        self._TotalDetail = TotalDetail

    @property
    def ConditionValue(self):
        return self._ConditionValue

    @ConditionValue.setter
    def ConditionValue(self, ConditionValue):
        self._ConditionValue = ConditionValue

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Header") is not None:
            self._Header = AnalyseHeaderDetail()
            self._Header._deserialize(params.get("Header"))
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = AnalyseDetail()
                obj._deserialize(item)
                self._Detail.append(obj)
        if params.get("TotalDetail") is not None:
            self._TotalDetail = AnalyseDetail()
            self._TotalDetail._deserialize(params.get("TotalDetail"))
        if params.get("ConditionValue") is not None:
            self._ConditionValue = AnalyseConditionDetail()
            self._ConditionValue._deserialize(params.get("ConditionValue"))
        self._RequestId = params.get("RequestId")


class DescribeCostSummaryByProductRequest(AbstractModel):
    """DescribeCostSummaryByProduct request structure.

    """

    def __init__(self):
        r"""
        :param _BeginTime: The value must be of the same month as `EndTime`. The query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type BeginTime: str
        :param _EndTime: The value must be of the same month as `BeginTime`. The query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type EndTime: str
        :param _Limit: Data quantity per fetch. The maximum value is 100.
        :type Limit: int
        :param _Offset: Offset, which starts from 0 by default
        :type Offset: int
        :param _PayerUin: UIN of the user querying the bill data
        :type PayerUin: str
        :param _NeedRecordNum: Whether to return the record count. 0 for no, 1 for yes. Default is no.
        :type NeedRecordNum: int
        """
        self._BeginTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._PayerUin = None
        self._NeedRecordNum = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def NeedRecordNum(self):
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._PayerUin = params.get("PayerUin")
        self._NeedRecordNum = params.get("NeedRecordNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCostSummaryByProductResponse(AbstractModel):
    """DescribeCostSummaryByProduct response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: Data readiness, 0 for not ready, 1 for ready
        :type Ready: int
        :param _Total: Consumption details
        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param _Data: Consumption details summarized by productNote: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of ConsumptionBusinessSummaryDataItem
        :param _RecordNum: Record count. The system returns null when NeedRecordNum is 0.Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordNum: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ready = None
        self._Total = None
        self._Data = None
        self._RecordNum = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RecordNum(self):
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("Total") is not None:
            self._Total = ConsumptionSummaryTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ConsumptionBusinessSummaryDataItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RecordNum = params.get("RecordNum")
        self._RequestId = params.get("RequestId")


class DescribeCostSummaryByProjectRequest(AbstractModel):
    """DescribeCostSummaryByProject request structure.

    """

    def __init__(self):
        r"""
        :param _BeginTime: The value must be of the same month as `EndTime`. The query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type BeginTime: str
        :param _EndTime: The value must be of the same month as `BeginTime`. The query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type EndTime: str
        :param _Limit: Data quantity per fetch. The maximum value is `100`.
        :type Limit: int
        :param _Offset: Offset, which starts from 0 by default
        :type Offset: int
        :param _PayerUin: UIN of the user querying the bill data
        :type PayerUin: str
        :param _NeedRecordNum: Whether to return the record count. 0 for no, 1 for yes. Default is no.
        :type NeedRecordNum: int
        """
        self._BeginTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._PayerUin = None
        self._NeedRecordNum = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def NeedRecordNum(self):
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._PayerUin = params.get("PayerUin")
        self._NeedRecordNum = params.get("NeedRecordNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCostSummaryByProjectResponse(AbstractModel):
    """DescribeCostSummaryByProject response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: Data readiness, 0 for not ready, 1 for ready
        :type Ready: int
        :param _Total: Consumption details
        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param _Data: Consumption details summarized by business
        :type Data: list of ConsumptionProjectSummaryDataItem
        :param _RecordNum: Record count. The system returns null when NeedRecordNum is 0.
        :type RecordNum: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ready = None
        self._Total = None
        self._Data = None
        self._RecordNum = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RecordNum(self):
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("Total") is not None:
            self._Total = ConsumptionSummaryTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ConsumptionProjectSummaryDataItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RecordNum = params.get("RecordNum")
        self._RequestId = params.get("RequestId")


class DescribeCostSummaryByRegionRequest(AbstractModel):
    """DescribeCostSummaryByRegion request structure.

    """

    def __init__(self):
        r"""
        :param _BeginTime: The value must be of the same month as `EndTime`. The query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type BeginTime: str
        :param _EndTime: The value must be of the same month as `BeginTime`. The query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type EndTime: str
        :param _Limit: Data quantity per fetch. The maximum value is `100`.
        :type Limit: int
        :param _Offset: Offset, which starts from 0 by default
        :type Offset: int
        :param _PayerUin: UIN of the user querying the bill data
        :type PayerUin: str
        :param _NeedRecordNum: Whether to return the record count. 0 for no, 1 for yes. Default is no.
        :type NeedRecordNum: int
        """
        self._BeginTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._PayerUin = None
        self._NeedRecordNum = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def NeedRecordNum(self):
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._PayerUin = params.get("PayerUin")
        self._NeedRecordNum = params.get("NeedRecordNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCostSummaryByRegionResponse(AbstractModel):
    """DescribeCostSummaryByRegion response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: Data readiness, 0 for not ready, 1 for ready
        :type Ready: int
        :param _Total: Consumption details
        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param _Data: Consumption details summarized by region
        :type Data: list of ConsumptionRegionSummaryDataItem
        :param _RecordNum: Record count. The system returns null when NeedRecordNum is 0.Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordNum: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ready = None
        self._Total = None
        self._Data = None
        self._RecordNum = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RecordNum(self):
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("Total") is not None:
            self._Total = ConsumptionSummaryTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ConsumptionRegionSummaryDataItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RecordNum = params.get("RecordNum")
        self._RequestId = params.get("RequestId")


class DescribeCostSummaryByResourceRequest(AbstractModel):
    """DescribeCostSummaryByResource request structure.

    """

    def __init__(self):
        r"""
        :param _BeginTime: The value must be of the same month as EndTime. The query period must start and end on the same month and the query result returned will be of the entire month. For example, if both BeginTime and EndTime are 2018-09, the data returned will be for the entire month of September 2018.
        :type BeginTime: str
        :param _EndTime: The value must be of the same month as BeginTime. The query period must start and end on the same month and the query result returned will be of the entire month. For example, if both BeginTime and EndTime are 2018-09, the data returned will be for the entire month of September 2018.
        :type EndTime: str
        :param _Limit: Data quantity per fetch. The maximum value is 100.
        :type Limit: int
        :param _Offset: Offset, which starts from 0 by default
        :type Offset: int
        :param _PayerUin: UIN of the user querying the bill data
        :type PayerUin: str
        :param _NeedRecordNum: Whether to return the record count. 0 for no, 1 for yes. Default is no.
        :type NeedRecordNum: int
        :param _NeedConditionValue: Whether to return filter criteria. 0 for no, 1 for yes. Default is no.
        :type NeedConditionValue: int
        :param _Conditions: Filter criteria. It only supports ResourceKeyword (resource keyword, which supports fuzzy query by resource ID or resource name), ProjectIds (project ID), RegionIds (region ID), PayModes (payment mode, prePay or postPay), HideFreeCost (whether to hide zero-amount transactions, 0 or 1), and OrderByCost (sorting rule by fees, desc or asc).
        :type Conditions: :class:`tencentcloud.billing.v20180709.models.Conditions`
        """
        self._BeginTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._PayerUin = None
        self._NeedRecordNum = None
        self._NeedConditionValue = None
        self._Conditions = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def NeedRecordNum(self):
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def NeedConditionValue(self):
        return self._NeedConditionValue

    @NeedConditionValue.setter
    def NeedConditionValue(self, NeedConditionValue):
        self._NeedConditionValue = NeedConditionValue

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._PayerUin = params.get("PayerUin")
        self._NeedRecordNum = params.get("NeedRecordNum")
        self._NeedConditionValue = params.get("NeedConditionValue")
        if params.get("Conditions") is not None:
            self._Conditions = Conditions()
            self._Conditions._deserialize(params.get("Conditions"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCostSummaryByResourceResponse(AbstractModel):
    """DescribeCostSummaryByResource response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: Data readiness, 0 for not ready, 1 for ready
        :type Ready: int
        :param _Total: Consumption detailsNote: This field may return null, indicating that no valid values can be obtained.
        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param _ConditionValue: Filter criteria
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConditionValue: :class:`tencentcloud.billing.v20180709.models.ConsumptionResourceSummaryConditionValue`
        :param _RecordNum: Record countNote: This field may return null, indicating that no valid values can be obtained.
        :type RecordNum: int
        :param _Data: Resource consumption detailsNote: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of ConsumptionResourceSummaryDataItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ready = None
        self._Total = None
        self._ConditionValue = None
        self._RecordNum = None
        self._Data = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConditionValue(self):
        return self._ConditionValue

    @ConditionValue.setter
    def ConditionValue(self, ConditionValue):
        self._ConditionValue = ConditionValue

    @property
    def RecordNum(self):
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("Total") is not None:
            self._Total = ConsumptionSummaryTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("ConditionValue") is not None:
            self._ConditionValue = ConsumptionResourceSummaryConditionValue()
            self._ConditionValue._deserialize(params.get("ConditionValue"))
        self._RecordNum = params.get("RecordNum")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ConsumptionResourceSummaryDataItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDosageCosDetailByDateRequest(AbstractModel):
    """DescribeDosageCosDetailByDate request structure.

    """

    def __init__(self):
        r"""
        :param _StartDate: The start date of the usage query, such as `2020-09-01`.
        :type StartDate: str
        :param _EndDate: The end date of the usage query (end date must be in the same month as the start date), such as `2020-09-30`.
        :type EndDate: str
        :param _BucketName: Bucket name. You can use `Get Service` to query the list of all buckets under a requester account. For details, see [GET Service (List Buckets)](https://www.tencentcloud.com/document/product/436/8291).
        :type BucketName: str
        """
        self._StartDate = None
        self._EndDate = None
        self._BucketName = None

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName


    def _deserialize(self, params):
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._BucketName = params.get("BucketName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDosageCosDetailByDateResponse(AbstractModel):
    """DescribeDosageCosDetailByDate response structure.

    """

    def __init__(self):
        r"""
        :param _DetailSets: Array of usage
        :type DetailSets: list of CosDetailSets
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DetailSets = None
        self._RequestId = None

    @property
    def DetailSets(self):
        return self._DetailSets

    @DetailSets.setter
    def DetailSets(self, DetailSets):
        self._DetailSets = DetailSets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DetailSets") is not None:
            self._DetailSets = []
            for item in params.get("DetailSets"):
                obj = CosDetailSets()
                obj._deserialize(item)
                self._DetailSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTagListRequest(AbstractModel):
    """DescribeTagList request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: The number of entries returned at a time. The maximum value is `1000`.
        :type Limit: int
        :param _Offset: Pagination offset. If `Offset` is `0`, it indicates the first page. When `Limit` is `100`, if `Offset` is `100`, it indicates the second page; if `Offset` is `200`, it indicates the third page, and so on.
        :type Offset: int
        :param _TagKey: Cost allocation tag key, used for fuzzy search.
        :type TagKey: str
        :param _Status: Tag type, used for tag filtering. Valid values: `0` (general tags), `1` (cost allocation tags). If it is not specified, all tag keys will be queried.
        :type Status: int
        :param _OrderType: Sorting order. Valid values: `asc` (ascending order), `desc` (descending order).
        :type OrderType: str
        """
        self._Limit = None
        self._Offset = None
        self._TagKey = None
        self._Status = None
        self._OrderType = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._TagKey = params.get("TagKey")
        self._Status = params.get("Status")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagListResponse(AbstractModel):
    """DescribeTagList response structure.

    """

    def __init__(self):
        r"""
        :param _RecordNum: Total number of records.
        :type RecordNum: int
        :param _Data: Tag information.
        :type Data: list of TagDataInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecordNum = None
        self._Data = None
        self._RequestId = None

    @property
    def RecordNum(self):
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RecordNum = params.get("RecordNum")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TagDataInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVoucherInfoRequest(AbstractModel):
    """DescribeVoucherInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: The number of records per page. The default is 20, and the maximum is 1,000.
        :type Limit: int
        :param _Offset: The page number the records start from. The default is 1.
        :type Offset: int
        :param _Status: The voucher status. Valid values: `unUsed`, `used`, `delivered`, `cancel`, `overdue`.
        :type Status: str
        :param _VoucherId: The voucher ID.
        :type VoucherId: str
        :param _CodeId: The voucher order ID.
        :type CodeId: str
        :param _ProductCode: The product code.
        :type ProductCode: str
        :param _ActivityId: The campaign ID.
        :type ActivityId: str
        :param _VoucherName: The voucher name.
        :type VoucherName: str
        :param _TimeFrom: The start date of the voucher issuance, such as `2021-01-01`.
        :type TimeFrom: str
        :param _TimeTo: The end date of the voucher issuance, such as `2021-01-01`.
        :type TimeTo: str
        :param _SortField: The field used to sort the records. Valid values: BeginTime, EndTime, CreateTime.
        :type SortField: str
        :param _SortOrder: Whether to sort the records in ascending or descending order. Valid values: desc, asc.
        :type SortOrder: str
        :param _PayMode: The payment mode. Valid values: `postPay`: pay-as-you-go; `prePay`: prepaid; `riPay`: reserved instance; empty or `*`: all. If this parameter is empty or `*`, `productCode` and `subProductCode` must also be empty.
        :type PayMode: str
        :param _PayScene: If `PayMode` is `postPay`, this parameter may be `spotpay` (spot instance) or `settle account` (regular pay-as-you-go). If `PayMode` is `prePay`, this parameter may be `purchase`, `renew`, or `modify` (downgrade/upgrade). If `PayMode` is `riPay`, this parameter may be `oneOffFee` (prepayment of reserved instance) or `hourlyFee` (hourly billing of reserved instance). `*` means to query vouchers that support all billing scenarios.
        :type PayScene: str
        :param _Operator: The operator. The default is the UIN of the current user.
        :type Operator: str
        :param _VoucherMainType: The primary types of vouchers are has_price and no_price, which represent the cash voucher with a price and the cash voucher without a price respectively.
        :type VoucherMainType: str
        :param _VoucherSubType: Voucher subtype: Discount is a discount voucher, and deduct is a deduction voucher.
        :type VoucherSubType: str
        """
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._VoucherId = None
        self._CodeId = None
        self._ProductCode = None
        self._ActivityId = None
        self._VoucherName = None
        self._TimeFrom = None
        self._TimeTo = None
        self._SortField = None
        self._SortOrder = None
        self._PayMode = None
        self._PayScene = None
        self._Operator = None
        self._VoucherMainType = None
        self._VoucherSubType = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VoucherId(self):
        return self._VoucherId

    @VoucherId.setter
    def VoucherId(self, VoucherId):
        self._VoucherId = VoucherId

    @property
    def CodeId(self):
        return self._CodeId

    @CodeId.setter
    def CodeId(self, CodeId):
        self._CodeId = CodeId

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def VoucherName(self):
        return self._VoucherName

    @VoucherName.setter
    def VoucherName(self, VoucherName):
        self._VoucherName = VoucherName

    @property
    def TimeFrom(self):
        return self._TimeFrom

    @TimeFrom.setter
    def TimeFrom(self, TimeFrom):
        self._TimeFrom = TimeFrom

    @property
    def TimeTo(self):
        return self._TimeTo

    @TimeTo.setter
    def TimeTo(self, TimeTo):
        self._TimeTo = TimeTo

    @property
    def SortField(self):
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortOrder(self):
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayScene(self):
        return self._PayScene

    @PayScene.setter
    def PayScene(self, PayScene):
        self._PayScene = PayScene

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def VoucherMainType(self):
        return self._VoucherMainType

    @VoucherMainType.setter
    def VoucherMainType(self, VoucherMainType):
        self._VoucherMainType = VoucherMainType

    @property
    def VoucherSubType(self):
        return self._VoucherSubType

    @VoucherSubType.setter
    def VoucherSubType(self, VoucherSubType):
        self._VoucherSubType = VoucherSubType


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Status = params.get("Status")
        self._VoucherId = params.get("VoucherId")
        self._CodeId = params.get("CodeId")
        self._ProductCode = params.get("ProductCode")
        self._ActivityId = params.get("ActivityId")
        self._VoucherName = params.get("VoucherName")
        self._TimeFrom = params.get("TimeFrom")
        self._TimeTo = params.get("TimeTo")
        self._SortField = params.get("SortField")
        self._SortOrder = params.get("SortOrder")
        self._PayMode = params.get("PayMode")
        self._PayScene = params.get("PayScene")
        self._Operator = params.get("Operator")
        self._VoucherMainType = params.get("VoucherMainType")
        self._VoucherSubType = params.get("VoucherSubType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVoucherInfoResponse(AbstractModel):
    """DescribeVoucherInfo response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total number of vouchers.
        :type TotalCount: int
        :param _TotalBalance: The total voucher balance. The value of this parameter is the total balance (USD, rounded to 8 decimal places) multiplied by 100,000,000.
        :type TotalBalance: int
        :param _VoucherInfos: The voucher information.
Note: This field may return `null`, indicating that no valid value was found.
        :type VoucherInfos: list of VoucherInfos
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TotalBalance = None
        self._VoucherInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalBalance(self):
        return self._TotalBalance

    @TotalBalance.setter
    def TotalBalance(self, TotalBalance):
        self._TotalBalance = TotalBalance

    @property
    def VoucherInfos(self):
        return self._VoucherInfos

    @VoucherInfos.setter
    def VoucherInfos(self, VoucherInfos):
        self._VoucherInfos = VoucherInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalBalance = params.get("TotalBalance")
        if params.get("VoucherInfos") is not None:
            self._VoucherInfos = []
            for item in params.get("VoucherInfos"):
                obj = VoucherInfos()
                obj._deserialize(item)
                self._VoucherInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVoucherUsageDetailsRequest(AbstractModel):
    """DescribeVoucherUsageDetails request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: The number of records per page. The default is 20, and the maximum is 1,000.
        :type Limit: int
        :param _Offset: The page number the records start from. The default is 1.
        :type Offset: int
        :param _VoucherId: The voucher ID.
        :type VoucherId: str
        :param _Operator: The operator. The default is the UIN of the current.
        :type Operator: str
        """
        self._Limit = None
        self._Offset = None
        self._VoucherId = None
        self._Operator = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def VoucherId(self):
        return self._VoucherId

    @VoucherId.setter
    def VoucherId(self, VoucherId):
        self._VoucherId = VoucherId

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._VoucherId = params.get("VoucherId")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVoucherUsageDetailsResponse(AbstractModel):
    """DescribeVoucherUsageDetails response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total number of vouchers.
        :type TotalCount: int
        :param _TotalUsedAmount: The total amount used. The value of this parameter is the total amount used (USD, rounded to 8 decimal places) multiplied by 100,000,000.
        :type TotalUsedAmount: int
        :param _UsageRecords: The usage details.
Note: This field may return `null`, indicating that no valid value was found.
        :type UsageRecords: list of UsageRecords
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TotalUsedAmount = None
        self._UsageRecords = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalUsedAmount(self):
        return self._TotalUsedAmount

    @TotalUsedAmount.setter
    def TotalUsedAmount(self, TotalUsedAmount):
        self._TotalUsedAmount = TotalUsedAmount

    @property
    def UsageRecords(self):
        return self._UsageRecords

    @UsageRecords.setter
    def UsageRecords(self, UsageRecords):
        self._UsageRecords = UsageRecords

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalUsedAmount = params.get("TotalUsedAmount")
        if params.get("UsageRecords") is not None:
            self._UsageRecords = []
            for item in params.get("UsageRecords"):
                obj = UsageRecords()
                obj._deserialize(item)
                self._UsageRecords.append(obj)
        self._RequestId = params.get("RequestId")


class DistributionBillDetail(AbstractModel):
    """Objects of reseller bill details

    """

    def __init__(self):
        r"""
        :param _BusinessCodeName: Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :type BusinessCodeName: str
        :param _ProductCodeName: Subproduct name: The subcategory of a Tencent Cloud product purchased by the user, such as CVM - Standard S1.
        :type ProductCodeName: str
        :param _PayModeName: Billing mode: The billing mode, which can be monthly subscription or pay-as-you-go.
        :type PayModeName: str
        :param _ProjectName: Project Name: The project to which a resource belongs, which is user-designated. If a resource has not been assigned to a project, it will automatically belong to the default project.
        :type ProjectName: str
        :param _RegionName: Region: The region of a resource, e.g. South China (Guangzhou).
        :type RegionName: str
        :param _ZoneName: Availability zone: availability zone of a resource, e.g. Guangzhou Zone 3.
        :type ZoneName: str
        :param _ResourceId: Instance ID: The object ID of a billed resource, such as a CVM instance ID. This object ID may vary due to various forms and contents of resources in different products.
        :type ResourceId: str
        :param _ResourceName: Instance name: The resource name set by the user in the console. If it is not set, it will be empty by default.
        :type ResourceName: str
        :param _ActionTypeName: Transaction type, which can be monthly subscription purchase, monthly subscription renewal, pay-as-you-go deduction, etc.
        :type ActionTypeName: str
        :param _OrderId: Order ID: The ID of a monthly subscription order.
        :type OrderId: str
        :param _BillId: Transaction ID: The ID of a settlement bill.
        :type BillId: str
        :param _PayTime: Deduction time: The settlement cost deduction time.
        :type PayTime: str
        :param _FeeBeginTime: Usage start time: The time at which product or service usage starts.
        :type FeeBeginTime: str
        :param _FeeEndTime: Usage end time: The time at which product or service usage ends.
        :type FeeEndTime: str
        :param _ComponentSet: List of components.
        :type ComponentSet: list of BillDetailComponent
        :param _OwnerUin: Owner account ID: The account ID of the actual resource user.
        :type OwnerUin: str
        :param _OperateUin: Operator account ID: The account or role ID of the operator who purchases or activates a resource.
        :type OperateUin: str
        :param _Tags: Tag information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of BillTagInfo
        :param _BusinessCode: Product code.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BusinessCode: str
        :param _ProductCode: Subproduct code.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProductCode: str
        :param _ActionType: Transaction type code.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ActionType: str
        :param _RegionId: Region ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionId: str
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _PriceInfo: Price attribute: A set of attributes which will determine the price of a component, apart from unit price and usage duration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PriceInfo: list of str
        :param _AssociatedOrder: Associated transaction document ID: The ID of the document associated with a transaction, such as a write-off order, the original order showing a deduction error during first settlement, a restructured order, or the original purchase order corresponding to a refund order.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AssociatedOrder: :class:`tencentcloud.billing.v20180709.models.BillDetailAssociatedOrder`
        :param _Formula: Calculation formula: The detailed calculation formula for a specific transaction type, such as refund or configuration change.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Formula: str
        :param _FormulaUrl: Billing rules: Official website links for detailed billing rules of each product.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FormulaUrl: str
        :param _BillMonth: Billing monthNote: This field may return null, indicating that no valid values can be obtained.
        :type BillMonth: str
        :param _BillDay: Billing dayNote: This field may return null, indicating that no valid values can be obtained.
        :type BillDay: str
        """
        self._BusinessCodeName = None
        self._ProductCodeName = None
        self._PayModeName = None
        self._ProjectName = None
        self._RegionName = None
        self._ZoneName = None
        self._ResourceId = None
        self._ResourceName = None
        self._ActionTypeName = None
        self._OrderId = None
        self._BillId = None
        self._PayTime = None
        self._FeeBeginTime = None
        self._FeeEndTime = None
        self._ComponentSet = None
        self._OwnerUin = None
        self._OperateUin = None
        self._Tags = None
        self._BusinessCode = None
        self._ProductCode = None
        self._ActionType = None
        self._RegionId = None
        self._ProjectId = None
        self._PriceInfo = None
        self._AssociatedOrder = None
        self._Formula = None
        self._FormulaUrl = None
        self._BillMonth = None
        self._BillDay = None

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def BillId(self):
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def PayTime(self):
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def FeeBeginTime(self):
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ComponentSet(self):
        return self._ComponentSet

    @ComponentSet.setter
    def ComponentSet(self, ComponentSet):
        self._ComponentSet = ComponentSet

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PriceInfo(self):
        return self._PriceInfo

    @PriceInfo.setter
    def PriceInfo(self, PriceInfo):
        self._PriceInfo = PriceInfo

    @property
    def AssociatedOrder(self):
        return self._AssociatedOrder

    @AssociatedOrder.setter
    def AssociatedOrder(self, AssociatedOrder):
        self._AssociatedOrder = AssociatedOrder

    @property
    def Formula(self):
        return self._Formula

    @Formula.setter
    def Formula(self, Formula):
        self._Formula = Formula

    @property
    def FormulaUrl(self):
        return self._FormulaUrl

    @FormulaUrl.setter
    def FormulaUrl(self, FormulaUrl):
        self._FormulaUrl = FormulaUrl

    @property
    def BillMonth(self):
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def BillDay(self):
        return self._BillDay

    @BillDay.setter
    def BillDay(self, BillDay):
        self._BillDay = BillDay


    def _deserialize(self, params):
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._ProductCodeName = params.get("ProductCodeName")
        self._PayModeName = params.get("PayModeName")
        self._ProjectName = params.get("ProjectName")
        self._RegionName = params.get("RegionName")
        self._ZoneName = params.get("ZoneName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._ActionTypeName = params.get("ActionTypeName")
        self._OrderId = params.get("OrderId")
        self._BillId = params.get("BillId")
        self._PayTime = params.get("PayTime")
        self._FeeBeginTime = params.get("FeeBeginTime")
        self._FeeEndTime = params.get("FeeEndTime")
        if params.get("ComponentSet") is not None:
            self._ComponentSet = []
            for item in params.get("ComponentSet"):
                obj = BillDetailComponent()
                obj._deserialize(item)
                self._ComponentSet.append(obj)
        self._OwnerUin = params.get("OwnerUin")
        self._OperateUin = params.get("OperateUin")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = BillTagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._BusinessCode = params.get("BusinessCode")
        self._ProductCode = params.get("ProductCode")
        self._ActionType = params.get("ActionType")
        self._RegionId = params.get("RegionId")
        self._ProjectId = params.get("ProjectId")
        self._PriceInfo = params.get("PriceInfo")
        if params.get("AssociatedOrder") is not None:
            self._AssociatedOrder = BillDetailAssociatedOrder()
            self._AssociatedOrder._deserialize(params.get("AssociatedOrder"))
        self._Formula = params.get("Formula")
        self._FormulaUrl = params.get("FormulaUrl")
        self._BillMonth = params.get("BillMonth")
        self._BillDay = params.get("BillDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExcludedProducts(AbstractModel):
    """The products that are not applicable.

    """

    def __init__(self):
        r"""
        :param _GoodsName: The names of non-applicable products.
        :type GoodsName: str
        :param _PayMode: `postPay`: pay-as-you-go; `prePay`: prepaid; `riPay`: reserved instance; empty or `*`: all.
        :type PayMode: str
        """
        self._GoodsName = None
        self._PayMode = None

    @property
    def GoodsName(self):
        return self._GoodsName

    @GoodsName.setter
    def GoodsName(self, GoodsName):
        self._GoodsName = GoodsName

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._GoodsName = params.get("GoodsName")
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayModeSummaryOverviewItem(AbstractModel):
    """Detailed summary of costs by billing mode

    """

    def __init__(self):
        r"""
        :param _PayMode: Billing mode code
        :type PayMode: str
        :param _PayModeName: Billing mode, which can be monthly subscription or pay-as-you-go.
        :type PayModeName: str
        :param _RealTotalCostRatio: Cost ratio, to two decimal points
        :type RealTotalCostRatio: str
        :param _RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param _CashPayAmount: Cash credit: The amount paid from the user’s cash balance
        :type CashPayAmount: str
        :param _IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param _TransferPayAmount: Commission credit: The amount paid with the user’s commission credit.
        :type TransferPayAmount: str
        :param _TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        :param _Detail: Detailed summary of costs by transaction type
        :type Detail: list of ActionSummaryOverviewItem
        """
        self._PayMode = None
        self._PayModeName = None
        self._RealTotalCostRatio = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None
        self._TotalCost = None
        self._Detail = None

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def RealTotalCostRatio(self):
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail


    def _deserialize(self, params):
        self._PayMode = params.get("PayMode")
        self._PayModeName = params.get("PayModeName")
        self._RealTotalCostRatio = params.get("RealTotalCostRatio")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._TotalCost = params.get("TotalCost")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = ActionSummaryOverviewItem()
                obj._deserialize(item)
                self._Detail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectSummaryOverviewItem(AbstractModel):
    """Detailed summary of purchases by project

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: str
        :param _ProjectName: Project name: The project to which a resource belongs, which is user-designated. If a resource has not been assigned to a project, it will automatically belong to the default project.
        :type ProjectName: str
        :param _RealTotalCostRatio: Cost ratio, to two decimal points
        :type RealTotalCostRatio: str
        :param _RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param _CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param _IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param _TransferPayAmount: Commission credit: The amount paid with the user’s commission credit.
        :type TransferPayAmount: str
        :param _BillMonth: Billing month, e.g. `2019-08`
        :type BillMonth: str
        :param _TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        """
        self._ProjectId = None
        self._ProjectName = None
        self._RealTotalCostRatio = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None
        self._BillMonth = None
        self._TotalCost = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RealTotalCostRatio(self):
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def BillMonth(self):
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._RealTotalCostRatio = params.get("RealTotalCostRatio")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._BillMonth = params.get("BillMonth")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionSummaryOverviewItem(AbstractModel):
    """Detailed summary of purchases by region

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID
Note: This field may return null, indicating that no valid value was found.
        :type RegionId: str
        :param _RegionName: Region: The region to which a resource belongs, such as South China (Guangzhou).
        :type RegionName: str
        :param _RealTotalCostRatio: Cost ratio, to two decimal points
        :type RealTotalCostRatio: str
        :param _RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param _CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param _IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param _TransferPayAmount: Commission credit: The amount paid with the user’s commission credit.
        :type TransferPayAmount: str
        :param _BillMonth: Billing month, e.g. `2019-08`
        :type BillMonth: str
        :param _TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        """
        self._RegionId = None
        self._RegionName = None
        self._RealTotalCostRatio = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None
        self._BillMonth = None
        self._TotalCost = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RealTotalCostRatio(self):
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def BillMonth(self):
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._RealTotalCostRatio = params.get("RealTotalCostRatio")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._BillMonth = params.get("BillMonth")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SummaryDetail(AbstractModel):
    """Detailed summary of costs by multiple dimensions

    """

    def __init__(self):
        r"""
        :param _GroupKey: Bill dimension code. Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupKey: str
        :param _GroupValue: Bill dimension value. Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupValue: str
        :param _TotalCost: Original cost in USD. This parameter has become valid since Bill 3.0 took effect in May 2021, and before that `-` was returned for this parameter. If a customer has applied for a contract price different from the prices listed on the official website, `-` will also be returned for this parameter.
        :type TotalCost: str
        :param _RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param _CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param _IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param _TransferPayAmount: Commission credit: The amount paid with the user’s commission credit. Note: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        :param _Business: Detailed summary of products. Note: This field may return null, indicating that no valid values can be obtained.
        :type Business: list of BusinessSummaryInfo
        """
        self._GroupKey = None
        self._GroupValue = None
        self._TotalCost = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None
        self._Business = None

    @property
    def GroupKey(self):
        return self._GroupKey

    @GroupKey.setter
    def GroupKey(self, GroupKey):
        self._GroupKey = GroupKey

    @property
    def GroupValue(self):
        return self._GroupValue

    @GroupValue.setter
    def GroupValue(self, GroupValue):
        self._GroupValue = GroupValue

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business


    def _deserialize(self, params):
        self._GroupKey = params.get("GroupKey")
        self._GroupValue = params.get("GroupValue")
        self._TotalCost = params.get("TotalCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        if params.get("Business") is not None:
            self._Business = []
            for item in params.get("Business"):
                obj = BusinessSummaryInfo()
                obj._deserialize(item)
                self._Business.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SummaryTotal(AbstractModel):
    """Total cost

    """

    def __init__(self):
        r"""
        :param _RealTotalCost: Total amount after discount. Note: This field may return null, indicating that no valid values can be obtained.
        :type RealTotalCost: str
        :param _TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TotalCost: str
        """
        self._RealTotalCost = None
        self._TotalCost = None

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._RealTotalCost = params.get("RealTotalCost")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagDataInfo(AbstractModel):
    """Tag information.

    """

    def __init__(self):
        r"""
        :param _TagKey: Cost allocation tag key.
        :type TagKey: str
        :param _Status: Tag type. Valid values: `0` (general tags), `1` (cost allocation tags).
        :type Status: int
        :param _UpdateTime: Time to set the cost allocation tag. It will not be returned if `Status` is `0`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self._TagKey = None
        self._Status = None
        self._UpdateTime = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._Status = params.get("Status")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagSummaryOverviewItem(AbstractModel):
    """Details about cost distribution over different tags.

    """

    def __init__(self):
        r"""
        :param _TagValue: Tag value
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagValue: str
        :param _RealTotalCostRatio: Cost percentage rounded to two decimal places
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealTotalCostRatio: str
        :param _RealTotalCost: Total amount after discount. Note: This field may return null, indicating that no valid values can be obtained.
        :type RealTotalCost: str
        :param _CashPayAmount: Cash credit: The amount paid from the user’s cash account. Note: This field may return null, indicating that no valid values can be obtained.
        :type CashPayAmount: str
        :param _IncentivePayAmount: Free credit: The amount paid with the user’s free credit. Note: This field may return null, indicating that no valid values can be obtained.
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: Voucher payment: The amount deducted by using vouchers. Note: This field may return null, indicating that no valid values can be obtained.
        :type VoucherPayAmount: str
        :param _TransferPayAmount: Commission credit: The amount paid with the user’s commission credit. Note: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        :param _TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TotalCost: str
        """
        self._TagValue = None
        self._RealTotalCostRatio = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None
        self._TotalCost = None

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def RealTotalCostRatio(self):
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._TagValue = params.get("TagValue")
        self._RealTotalCostRatio = params.get("RealTotalCostRatio")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageDetails(AbstractModel):
    """The product purchased.

    """

    def __init__(self):
        r"""
        :param _ProductName: The name of the product.
Note: This field may return `null`, indicating that no valid value was found.
        :type ProductName: str
        :param _SubProductName: 
        :type SubProductName: str
        """
        self._ProductName = None
        self._SubProductName = None

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def SubProductName(self):
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._SubProductName = params.get("SubProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageRecords(AbstractModel):
    """The usage records.

    """

    def __init__(self):
        r"""
        :param _UsedAmount: The amount used. The value of this parameter is the amount used (USD, rounded to 8 decimal places) multiplied by 100,000,000.
        :type UsedAmount: int
        :param _UsedTime: The time when the voucher was used.
        :type UsedTime: str
        :param _UsageDetails: The details of the product purchased.
Note: This field may return `null`, indicating that no valid value was found.
        :type UsageDetails: list of UsageDetails
        """
        self._UsedAmount = None
        self._UsedTime = None
        self._UsageDetails = None

    @property
    def UsedAmount(self):
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

    @property
    def UsedTime(self):
        return self._UsedTime

    @UsedTime.setter
    def UsedTime(self, UsedTime):
        self._UsedTime = UsedTime

    @property
    def UsageDetails(self):
        return self._UsageDetails

    @UsageDetails.setter
    def UsageDetails(self, UsageDetails):
        self._UsageDetails = UsageDetails


    def _deserialize(self, params):
        self._UsedAmount = params.get("UsedAmount")
        self._UsedTime = params.get("UsedTime")
        if params.get("UsageDetails") is not None:
            self._UsageDetails = []
            for item in params.get("UsageDetails"):
                obj = UsageDetails()
                obj._deserialize(item)
                self._UsageDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoucherInfos(AbstractModel):
    """Voucher information.

    """

    def __init__(self):
        r"""
        :param _OwnerUin: The owner of the voucher.
        :type OwnerUin: str
        :param _Status: The status of the voucher: `unUsed`, `used`, `delivered`, `cancel`, `overdue`
        :type Status: str
        :param _NominalValue: The value of the voucher. The value of this parameter is the voucher value (USD, rounded to 8 decimal places) multiplied by 100,000,000.
        :type NominalValue: int
        :param _Balance: The balance left. The value of this parameter is the balance left (USD, rounded to 8 decimal places) multiplied by 100,000,000.
        :type Balance: int
        :param _VoucherId: The voucher ID.
        :type VoucherId: str
        :param _PayMode: `postPay`: pay-as-you-go; `prePay`: prepaid; `riPay`: reserved instance; empty or `*`: all.
        :type PayMode: str
        :param _PayScene: If `PayMode` is `postPay`, this parameter may be `spotpay` (spot instance) or `settle account` (regular pay-as-you-go). If `PayMode` is `prePay`, this parameter may be `purchase`, `renew`, or `modify` (downgrade/upgrade). If `PayMode` is `riPay`, this parameter may be `oneOffFee` (prepayment of reserved instance) or `hourlyFee` (hourly billing of reserved instance). `*` means to query vouchers that support all billing scenarios.
        :type PayScene: str
        :param _BeginTime: The start time of the validity period.
        :type BeginTime: str
        :param _EndTime: The end time of the validity period.
        :type EndTime: str
        :param _ApplicableProducts: The products that are applicable.
Note: This field may return `null`, indicating that no valid value was found.
        :type ApplicableProducts: :class:`tencentcloud.billing.v20180709.models.ApplicableProducts`
        :param _ExcludedProducts: The products that are not applicable.
Note: This field may return `null`, indicating that no valid value was found.
        :type ExcludedProducts: list of ExcludedProducts
        """
        self._OwnerUin = None
        self._Status = None
        self._NominalValue = None
        self._Balance = None
        self._VoucherId = None
        self._PayMode = None
        self._PayScene = None
        self._BeginTime = None
        self._EndTime = None
        self._ApplicableProducts = None
        self._ExcludedProducts = None

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NominalValue(self):
        return self._NominalValue

    @NominalValue.setter
    def NominalValue(self, NominalValue):
        self._NominalValue = NominalValue

    @property
    def Balance(self):
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def VoucherId(self):
        return self._VoucherId

    @VoucherId.setter
    def VoucherId(self, VoucherId):
        self._VoucherId = VoucherId

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayScene(self):
        return self._PayScene

    @PayScene.setter
    def PayScene(self, PayScene):
        self._PayScene = PayScene

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ApplicableProducts(self):
        return self._ApplicableProducts

    @ApplicableProducts.setter
    def ApplicableProducts(self, ApplicableProducts):
        self._ApplicableProducts = ApplicableProducts

    @property
    def ExcludedProducts(self):
        return self._ExcludedProducts

    @ExcludedProducts.setter
    def ExcludedProducts(self, ExcludedProducts):
        self._ExcludedProducts = ExcludedProducts


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        self._Status = params.get("Status")
        self._NominalValue = params.get("NominalValue")
        self._Balance = params.get("Balance")
        self._VoucherId = params.get("VoucherId")
        self._PayMode = params.get("PayMode")
        self._PayScene = params.get("PayScene")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        if params.get("ApplicableProducts") is not None:
            self._ApplicableProducts = ApplicableProducts()
            self._ApplicableProducts._deserialize(params.get("ApplicableProducts"))
        if params.get("ExcludedProducts") is not None:
            self._ExcludedProducts = []
            for item in params.get("ExcludedProducts"):
                obj = ExcludedProducts()
                obj._deserialize(item)
                self._ExcludedProducts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        