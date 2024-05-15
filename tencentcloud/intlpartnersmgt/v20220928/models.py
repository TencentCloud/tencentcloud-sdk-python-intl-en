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
    """Transaction type details in the customer bill data totaled by payment mode

    """

    def __init__(self):
        r"""
        :param _ActionType: Transaction type code
Note: This field may return null, indicating that no valid values can be obtained.
        :type ActionType: str
        :param _ActionTypeName: Transaction type name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ActionTypeName: str
        :param _OriginalCost: The actual total consumption amount accurate down to eight decimal places
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalCost: str
        :param _VoucherPayAmount: The deducted voucher amount accurate down to eight decimal places
Note: This field may return null, indicating that no valid values can be obtained.
        :type VoucherPayAmount: str
        :param _TotalCost: Total consumption amount accurate down to eight decimal places
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCost: str
        """
        self._ActionType = None
        self._ActionTypeName = None
        self._OriginalCost = None
        self._VoucherPayAmount = None
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
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._ActionType = params.get("ActionType")
        self._ActionTypeName = params.get("ActionTypeName")
        self._OriginalCost = params.get("OriginalCost")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateCustomerCreditRequest(AbstractModel):
    """AllocateCustomerCredit request structure.

    """

    def __init__(self):
        r"""
        :param _AddedCredit: Specific value of the credit allocated to the customer
        :type AddedCredit: float
        :param _ClientUin: Customer UIN
        :type ClientUin: int
        """
        self._AddedCredit = None
        self._ClientUin = None

    @property
    def AddedCredit(self):
        return self._AddedCredit

    @AddedCredit.setter
    def AddedCredit(self, AddedCredit):
        self._AddedCredit = AddedCredit

    @property
    def ClientUin(self):
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin


    def _deserialize(self, params):
        self._AddedCredit = params.get("AddedCredit")
        self._ClientUin = params.get("ClientUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateCustomerCreditResponse(AbstractModel):
    """AllocateCustomerCredit response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCredit: The updated total credit
        :type TotalCredit: float
        :param _RemainingCredit: The updated available credit
        :type RemainingCredit: float
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCredit = None
        self._RemainingCredit = None
        self._RequestId = None

    @property
    def TotalCredit(self):
        return self._TotalCredit

    @TotalCredit.setter
    def TotalCredit(self, TotalCredit):
        self._TotalCredit = TotalCredit

    @property
    def RemainingCredit(self):
        return self._RemainingCredit

    @RemainingCredit.setter
    def RemainingCredit(self, RemainingCredit):
        self._RemainingCredit = RemainingCredit

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCredit = params.get("TotalCredit")
        self._RemainingCredit = params.get("RemainingCredit")
        self._RequestId = params.get("RequestId")


class BillDetailData(AbstractModel):
    """Customer bill details

    """

    def __init__(self):
        r"""
        :param _PayerAccountId: Reseller account
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayerAccountId: int
        :param _OwnerAccountId: Customer account
Note: This field may return null, indicating that no valid values can be obtained.
        :type OwnerAccountId: int
        :param _OperatorAccountId: Operator account
Note: This field may return null, indicating that no valid values can be obtained.
        :type OperatorAccountId: int
        :param _ProductName: Product name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProductName: str
        :param _BillingMode: Billing mode
`Monthly subscription` (Monthly subscription)
`Pay-As-You-Go resources` (Pay-as-you-go)
`Standard RI` (Reserved instance)
Note: This field may return null, indicating that no valid values can be obtained.
        :type BillingMode: str
        :param _ProjectName: Project name

Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectName: str
        :param _Region: Resource region
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _AvailabilityZone: Resource AZ
Note: This field may return null, indicating that no valid values can be obtained.
        :type AvailabilityZone: str
        :param _InstanceId: Instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _InstanceName: Instance name
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _SubProductName: Subproduct name

Note: This field may return null, indicating that no valid values can be obtained.
        :type SubProductName: str
        :param _TransactionType: Settlement type
Note: This field may return null, indicating that no valid values can be obtained.
        :type TransactionType: str
        :param _TransactionId: Transaction ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TransactionId: str
        :param _TransactionTime: Settlement time

Note: This field may return null, indicating that no valid values can be obtained.
        :type TransactionTime: str
        :param _UsageStartTime: Start time of resource use
Note: This field may return null, indicating that no valid values can be obtained.
        :type UsageStartTime: str
        :param _UsageEndTime: End time of resource use
Note: This field may return null, indicating that no valid values can be obtained.
        :type UsageEndTime: str
        :param _ComponentType: Component
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentType: str
        :param _ComponentName: Component name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentName: str
        :param _ComponentListPrice: Component list price
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentListPrice: str
        :param _ComponentPriceMeasurementUnit: Price unit
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentPriceMeasurementUnit: str
        :param _ComponentUsage: Component usage
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentUsage: str
        :param _ComponentUsageUnit: Component usage unit
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentUsageUnit: str
        :param _UsageDuration: Resource usage duration
Note: This field may return null, indicating that no valid values can be obtained.
        :type UsageDuration: str
        :param _DurationUnit: Duration unit
Note: This field may return null, indicating that no valid values can be obtained.
        :type DurationUnit: str
        :param _OriginalCost: Original cost
Original cost = component list price * component usage * usage duration
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalCost: str
        :param _DiscountRate: Discount, which defaults to `1`, indicating there is no discount.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiscountRate: str
        :param _Currency: Currency
Note: This field may return null, indicating that no valid values can be obtained.
        :type Currency: str
        :param _TotalAmountAfterDiscount: Discounted total
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalAmountAfterDiscount: str
        :param _VoucherDeduction: Voucher deduction
Note: This field may return null, indicating that no valid values can be obtained.
        :type VoucherDeduction: str
        :param _TotalCost: Total cost = discounted total - voucher deduction
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCost: str
        :param _Id: ID
Note: The return value may be null, indicating that no valid data can be obtained.
        :type Id: str
        """
        self._PayerAccountId = None
        self._OwnerAccountId = None
        self._OperatorAccountId = None
        self._ProductName = None
        self._BillingMode = None
        self._ProjectName = None
        self._Region = None
        self._AvailabilityZone = None
        self._InstanceId = None
        self._InstanceName = None
        self._SubProductName = None
        self._TransactionType = None
        self._TransactionId = None
        self._TransactionTime = None
        self._UsageStartTime = None
        self._UsageEndTime = None
        self._ComponentType = None
        self._ComponentName = None
        self._ComponentListPrice = None
        self._ComponentPriceMeasurementUnit = None
        self._ComponentUsage = None
        self._ComponentUsageUnit = None
        self._UsageDuration = None
        self._DurationUnit = None
        self._OriginalCost = None
        self._DiscountRate = None
        self._Currency = None
        self._TotalAmountAfterDiscount = None
        self._VoucherDeduction = None
        self._TotalCost = None
        self._Id = None

    @property
    def PayerAccountId(self):
        return self._PayerAccountId

    @PayerAccountId.setter
    def PayerAccountId(self, PayerAccountId):
        self._PayerAccountId = PayerAccountId

    @property
    def OwnerAccountId(self):
        return self._OwnerAccountId

    @OwnerAccountId.setter
    def OwnerAccountId(self, OwnerAccountId):
        self._OwnerAccountId = OwnerAccountId

    @property
    def OperatorAccountId(self):
        return self._OperatorAccountId

    @OperatorAccountId.setter
    def OperatorAccountId(self, OperatorAccountId):
        self._OperatorAccountId = OperatorAccountId

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def BillingMode(self):
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AvailabilityZone(self):
        return self._AvailabilityZone

    @AvailabilityZone.setter
    def AvailabilityZone(self, AvailabilityZone):
        self._AvailabilityZone = AvailabilityZone

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def SubProductName(self):
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName

    @property
    def TransactionType(self):
        return self._TransactionType

    @TransactionType.setter
    def TransactionType(self, TransactionType):
        self._TransactionType = TransactionType

    @property
    def TransactionId(self):
        return self._TransactionId

    @TransactionId.setter
    def TransactionId(self, TransactionId):
        self._TransactionId = TransactionId

    @property
    def TransactionTime(self):
        return self._TransactionTime

    @TransactionTime.setter
    def TransactionTime(self, TransactionTime):
        self._TransactionTime = TransactionTime

    @property
    def UsageStartTime(self):
        return self._UsageStartTime

    @UsageStartTime.setter
    def UsageStartTime(self, UsageStartTime):
        self._UsageStartTime = UsageStartTime

    @property
    def UsageEndTime(self):
        return self._UsageEndTime

    @UsageEndTime.setter
    def UsageEndTime(self, UsageEndTime):
        self._UsageEndTime = UsageEndTime

    @property
    def ComponentType(self):
        return self._ComponentType

    @ComponentType.setter
    def ComponentType(self, ComponentType):
        self._ComponentType = ComponentType

    @property
    def ComponentName(self):
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def ComponentListPrice(self):
        return self._ComponentListPrice

    @ComponentListPrice.setter
    def ComponentListPrice(self, ComponentListPrice):
        self._ComponentListPrice = ComponentListPrice

    @property
    def ComponentPriceMeasurementUnit(self):
        return self._ComponentPriceMeasurementUnit

    @ComponentPriceMeasurementUnit.setter
    def ComponentPriceMeasurementUnit(self, ComponentPriceMeasurementUnit):
        self._ComponentPriceMeasurementUnit = ComponentPriceMeasurementUnit

    @property
    def ComponentUsage(self):
        return self._ComponentUsage

    @ComponentUsage.setter
    def ComponentUsage(self, ComponentUsage):
        self._ComponentUsage = ComponentUsage

    @property
    def ComponentUsageUnit(self):
        return self._ComponentUsageUnit

    @ComponentUsageUnit.setter
    def ComponentUsageUnit(self, ComponentUsageUnit):
        self._ComponentUsageUnit = ComponentUsageUnit

    @property
    def UsageDuration(self):
        return self._UsageDuration

    @UsageDuration.setter
    def UsageDuration(self, UsageDuration):
        self._UsageDuration = UsageDuration

    @property
    def DurationUnit(self):
        return self._DurationUnit

    @DurationUnit.setter
    def DurationUnit(self, DurationUnit):
        self._DurationUnit = DurationUnit

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountRate(self):
        return self._DiscountRate

    @DiscountRate.setter
    def DiscountRate(self, DiscountRate):
        self._DiscountRate = DiscountRate

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def TotalAmountAfterDiscount(self):
        return self._TotalAmountAfterDiscount

    @TotalAmountAfterDiscount.setter
    def TotalAmountAfterDiscount(self, TotalAmountAfterDiscount):
        self._TotalAmountAfterDiscount = TotalAmountAfterDiscount

    @property
    def VoucherDeduction(self):
        return self._VoucherDeduction

    @VoucherDeduction.setter
    def VoucherDeduction(self, VoucherDeduction):
        self._VoucherDeduction = VoucherDeduction

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._PayerAccountId = params.get("PayerAccountId")
        self._OwnerAccountId = params.get("OwnerAccountId")
        self._OperatorAccountId = params.get("OperatorAccountId")
        self._ProductName = params.get("ProductName")
        self._BillingMode = params.get("BillingMode")
        self._ProjectName = params.get("ProjectName")
        self._Region = params.get("Region")
        self._AvailabilityZone = params.get("AvailabilityZone")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._SubProductName = params.get("SubProductName")
        self._TransactionType = params.get("TransactionType")
        self._TransactionId = params.get("TransactionId")
        self._TransactionTime = params.get("TransactionTime")
        self._UsageStartTime = params.get("UsageStartTime")
        self._UsageEndTime = params.get("UsageEndTime")
        self._ComponentType = params.get("ComponentType")
        self._ComponentName = params.get("ComponentName")
        self._ComponentListPrice = params.get("ComponentListPrice")
        self._ComponentPriceMeasurementUnit = params.get("ComponentPriceMeasurementUnit")
        self._ComponentUsage = params.get("ComponentUsage")
        self._ComponentUsageUnit = params.get("ComponentUsageUnit")
        self._UsageDuration = params.get("UsageDuration")
        self._DurationUnit = params.get("DurationUnit")
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountRate = params.get("DiscountRate")
        self._Currency = params.get("Currency")
        self._TotalAmountAfterDiscount = params.get("TotalAmountAfterDiscount")
        self._VoucherDeduction = params.get("VoucherDeduction")
        self._TotalCost = params.get("TotalCost")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusinessInfo(AbstractModel):
    """Product information

    """

    def __init__(self):
        r"""
        :param _BusinessCodeName: ProductNote: This field may return null, indicating that no valid values can be obtained.
        :type BusinessCodeName: str
        :param _BusinessCode: Product codeNote: This field may return null, indicating that no valid values can be obtained.
        :type BusinessCode: str
        :param _OriginalCost: Original price
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalCost: str
        :param _VoucherPayAmount: Voucher amount
Note: This field may return null, indicating that no valid values can be obtained.
        :type VoucherPayAmount: str
        :param _RICost: Daily deduction
Note: This field may return null, indicating that no valid values can be obtained.
        :type RICost: str
        :param _TotalCost: Total amount
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCost: str
        """
        self._BusinessCodeName = None
        self._BusinessCode = None
        self._OriginalCost = None
        self._VoucherPayAmount = None
        self._RICost = None
        self._TotalCost = None

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def RICost(self):
        return self._RICost

    @RICost.setter
    def RICost(self, RICost):
        self._RICost = RICost

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._BusinessCode = params.get("BusinessCode")
        self._OriginalCost = params.get("OriginalCost")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._RICost = params.get("RICost")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusinessSummaryOverviewItem(AbstractModel):
    """Product details in the customer bill data totaled by product

    """

    def __init__(self):
        r"""
        :param _BusinessCode: Product code
Note: This field may return null, indicating that no valid values can be obtained.
        :type BusinessCode: str
        :param _BusinessCodeName: Product name
Note: This field may return null, indicating that no valid values can be obtained.
        :type BusinessCodeName: str
        :param _OriginalCost: List price accurate down to eight decimal places
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalCost: str
        :param _VoucherPayAmount: The deducted voucher amount accurate down to eight decimal places
Note: This field may return null, indicating that no valid values can be obtained.
        :type VoucherPayAmount: str
        :param _TotalCost: Consumption amount accurate down to eight decimal places
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCost: str
        """
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._OriginalCost = None
        self._VoucherPayAmount = None
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
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._OriginalCost = params.get("OriginalCost")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CountryCodeItem(AbstractModel):
    """Element type of the `GetCountryCodes` API

    """

    def __init__(self):
        r"""
        :param _EnName: Country/region name in English
        :type EnName: str
        :param _Name: Country/region name in Chinese
        :type Name: str
        :param _IOS2: 
        :type IOS2: str
        :param _IOS3: 
        :type IOS3: str
        :param _Code: International dialing code
        :type Code: str
        """
        self._EnName = None
        self._Name = None
        self._IOS2 = None
        self._IOS3 = None
        self._Code = None

    @property
    def EnName(self):
        return self._EnName

    @EnName.setter
    def EnName(self, EnName):
        self._EnName = EnName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IOS2(self):
        return self._IOS2

    @IOS2.setter
    def IOS2(self, IOS2):
        self._IOS2 = IOS2

    @property
    def IOS3(self):
        return self._IOS3

    @IOS3.setter
    def IOS3(self, IOS3):
        self._IOS3 = IOS3

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._EnName = params.get("EnName")
        self._Name = params.get("Name")
        self._IOS2 = params.get("IOS2")
        self._IOS3 = params.get("IOS3")
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountRequest(AbstractModel):
    """CreateAccount request structure.

    """

    def __init__(self):
        r"""
        :param _AccountType: Account type of a new customer. Valid values: `personal`, `company`.
        :type AccountType: str
        :param _Mail: Registered email address, which should be valid and correct.
For example, account@qq.com.
        :type Mail: str
        :param _Password: Account password
Length limit: 8-20 characters
A password must contain numbers, letters, and symbols (!@#$%^&*()). Space is not allowed.
        :type Password: str
        :param _ConfirmPassword: The confirmed password, which must be the same as that entered in the `Password` field.
        :type ConfirmPassword: str
        :param _PhoneNum: Customer mobile number, which should be valid and correct.
A global mobile number within 1-32 digits is allowed, such as 18888888888.
        :type PhoneNum: str
        :param _CountryCode: Customer's country/region code, which can be obtained via the `GetCountryCodes` API, such as "852".
        :type CountryCode: str
        :param _Area: Customer's ISO2 standard country/region code, which can be obtained via the `GetCountryCodes` API. It should correspond to the `CountryCode` field, such as `HK`.
        :type Area: str
        :param _Extended: Extension field, which is left empty by default.
        :type Extended: str
        """
        self._AccountType = None
        self._Mail = None
        self._Password = None
        self._ConfirmPassword = None
        self._PhoneNum = None
        self._CountryCode = None
        self._Area = None
        self._Extended = None

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Mail(self):
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ConfirmPassword(self):
        return self._ConfirmPassword

    @ConfirmPassword.setter
    def ConfirmPassword(self, ConfirmPassword):
        self._ConfirmPassword = ConfirmPassword

    @property
    def PhoneNum(self):
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def CountryCode(self):
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Extended(self):
        return self._Extended

    @Extended.setter
    def Extended(self, Extended):
        self._Extended = Extended


    def _deserialize(self, params):
        self._AccountType = params.get("AccountType")
        self._Mail = params.get("Mail")
        self._Password = params.get("Password")
        self._ConfirmPassword = params.get("ConfirmPassword")
        self._PhoneNum = params.get("PhoneNum")
        self._CountryCode = params.get("CountryCode")
        self._Area = params.get("Area")
        self._Extended = params.get("Extended")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountResponse(AbstractModel):
    """CreateAccount response structure.

    """

    def __init__(self):
        r"""
        :param _Uin: Account UIN
        :type Uin: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Uin = None
        self._RequestId = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._RequestId = params.get("RequestId")


class CustomerBillDetailData(AbstractModel):
    """Customer bill details

    """

    def __init__(self):
        r"""
        :param _PayerAccountId: Reseller account
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayerAccountId: int
        :param _OwnerAccountId: Customer account
Note: This field may return null, indicating that no valid values can be obtained.
        :type OwnerAccountId: int
        :param _OperatorAccountId: Operator account
Note: This field may return null, indicating that no valid values can be obtained.
        :type OperatorAccountId: int
        :param _ProductName: Product name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProductName: str
        :param _BillingMode: Billing mode
`Monthly subscription` (Monthly subscription)
`Pay-As-You-Go resources` (Pay-as-you-go)
`Standard RI` (Reserved instance)
Note: This field may return null, indicating that no valid values can be obtained.
        :type BillingMode: str
        :param _ProjectName: Project name

Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectName: str
        :param _Region: Resource region
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _AvailabilityZone: Resource AZ
Note: This field may return null, indicating that no valid values can be obtained.
        :type AvailabilityZone: str
        :param _InstanceId: Instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _InstanceName: Instance name
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _SubProductName: Subproduct name

Note: This field may return null, indicating that no valid values can be obtained.
        :type SubProductName: str
        :param _TransactionType: Settlement type
Note: This field may return null, indicating that no valid values can be obtained.
        :type TransactionType: str
        :param _TransactionId: Transaction ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TransactionId: str
        :param _TransactionTime: Settlement time

Note: This field may return null, indicating that no valid values can be obtained.
        :type TransactionTime: str
        :param _UsageStartTime: Start time of resource use
Note: This field may return null, indicating that no valid values can be obtained.
        :type UsageStartTime: str
        :param _UsageEndTime: End time of resource use
Note: This field may return null, indicating that no valid values can be obtained.
        :type UsageEndTime: str
        :param _ComponentType: Component
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentType: str
        :param _ComponentName: Component name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentName: str
        :param _ComponentListPrice: Component list price
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentListPrice: str
        :param _ComponentPriceMeasurementUnit: Price unit
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentPriceMeasurementUnit: str
        :param _ComponentUsage: Component usage
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentUsage: str
        :param _ComponentUsageUnit: Component usage unit
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentUsageUnit: str
        :param _UsageDuration: Resource usage duration
Note: This field may return null, indicating that no valid values can be obtained.
        :type UsageDuration: str
        :param _DurationUnit: Duration unit
Note: This field may return null, indicating that no valid values can be obtained.
        :type DurationUnit: str
        :param _OriginalCost: Original cost
Original cost = component list price * component usage * usage duration
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalCost: str
        :param _Currency: Currency
Note: This field may return null, indicating that no valid values can be obtained.
        :type Currency: str
        :param _TotalCost: Total cost = discounted total - voucher deduction
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCost: str
        :param _Id: ID
Note: The return value may be null, indicating that no valid data can be obtained.
        :type Id: str
        :param _Tags: Tag informationNote: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagInfo
        """
        self._PayerAccountId = None
        self._OwnerAccountId = None
        self._OperatorAccountId = None
        self._ProductName = None
        self._BillingMode = None
        self._ProjectName = None
        self._Region = None
        self._AvailabilityZone = None
        self._InstanceId = None
        self._InstanceName = None
        self._SubProductName = None
        self._TransactionType = None
        self._TransactionId = None
        self._TransactionTime = None
        self._UsageStartTime = None
        self._UsageEndTime = None
        self._ComponentType = None
        self._ComponentName = None
        self._ComponentListPrice = None
        self._ComponentPriceMeasurementUnit = None
        self._ComponentUsage = None
        self._ComponentUsageUnit = None
        self._UsageDuration = None
        self._DurationUnit = None
        self._OriginalCost = None
        self._Currency = None
        self._TotalCost = None
        self._Id = None
        self._Tags = None

    @property
    def PayerAccountId(self):
        return self._PayerAccountId

    @PayerAccountId.setter
    def PayerAccountId(self, PayerAccountId):
        self._PayerAccountId = PayerAccountId

    @property
    def OwnerAccountId(self):
        return self._OwnerAccountId

    @OwnerAccountId.setter
    def OwnerAccountId(self, OwnerAccountId):
        self._OwnerAccountId = OwnerAccountId

    @property
    def OperatorAccountId(self):
        return self._OperatorAccountId

    @OperatorAccountId.setter
    def OperatorAccountId(self, OperatorAccountId):
        self._OperatorAccountId = OperatorAccountId

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def BillingMode(self):
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AvailabilityZone(self):
        return self._AvailabilityZone

    @AvailabilityZone.setter
    def AvailabilityZone(self, AvailabilityZone):
        self._AvailabilityZone = AvailabilityZone

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def SubProductName(self):
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName

    @property
    def TransactionType(self):
        return self._TransactionType

    @TransactionType.setter
    def TransactionType(self, TransactionType):
        self._TransactionType = TransactionType

    @property
    def TransactionId(self):
        return self._TransactionId

    @TransactionId.setter
    def TransactionId(self, TransactionId):
        self._TransactionId = TransactionId

    @property
    def TransactionTime(self):
        return self._TransactionTime

    @TransactionTime.setter
    def TransactionTime(self, TransactionTime):
        self._TransactionTime = TransactionTime

    @property
    def UsageStartTime(self):
        return self._UsageStartTime

    @UsageStartTime.setter
    def UsageStartTime(self, UsageStartTime):
        self._UsageStartTime = UsageStartTime

    @property
    def UsageEndTime(self):
        return self._UsageEndTime

    @UsageEndTime.setter
    def UsageEndTime(self, UsageEndTime):
        self._UsageEndTime = UsageEndTime

    @property
    def ComponentType(self):
        return self._ComponentType

    @ComponentType.setter
    def ComponentType(self, ComponentType):
        self._ComponentType = ComponentType

    @property
    def ComponentName(self):
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def ComponentListPrice(self):
        return self._ComponentListPrice

    @ComponentListPrice.setter
    def ComponentListPrice(self, ComponentListPrice):
        self._ComponentListPrice = ComponentListPrice

    @property
    def ComponentPriceMeasurementUnit(self):
        return self._ComponentPriceMeasurementUnit

    @ComponentPriceMeasurementUnit.setter
    def ComponentPriceMeasurementUnit(self, ComponentPriceMeasurementUnit):
        self._ComponentPriceMeasurementUnit = ComponentPriceMeasurementUnit

    @property
    def ComponentUsage(self):
        return self._ComponentUsage

    @ComponentUsage.setter
    def ComponentUsage(self, ComponentUsage):
        self._ComponentUsage = ComponentUsage

    @property
    def ComponentUsageUnit(self):
        return self._ComponentUsageUnit

    @ComponentUsageUnit.setter
    def ComponentUsageUnit(self, ComponentUsageUnit):
        self._ComponentUsageUnit = ComponentUsageUnit

    @property
    def UsageDuration(self):
        return self._UsageDuration

    @UsageDuration.setter
    def UsageDuration(self, UsageDuration):
        self._UsageDuration = UsageDuration

    @property
    def DurationUnit(self):
        return self._DurationUnit

    @DurationUnit.setter
    def DurationUnit(self, DurationUnit):
        self._DurationUnit = DurationUnit

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._PayerAccountId = params.get("PayerAccountId")
        self._OwnerAccountId = params.get("OwnerAccountId")
        self._OperatorAccountId = params.get("OperatorAccountId")
        self._ProductName = params.get("ProductName")
        self._BillingMode = params.get("BillingMode")
        self._ProjectName = params.get("ProjectName")
        self._Region = params.get("Region")
        self._AvailabilityZone = params.get("AvailabilityZone")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._SubProductName = params.get("SubProductName")
        self._TransactionType = params.get("TransactionType")
        self._TransactionId = params.get("TransactionId")
        self._TransactionTime = params.get("TransactionTime")
        self._UsageStartTime = params.get("UsageStartTime")
        self._UsageEndTime = params.get("UsageEndTime")
        self._ComponentType = params.get("ComponentType")
        self._ComponentName = params.get("ComponentName")
        self._ComponentListPrice = params.get("ComponentListPrice")
        self._ComponentPriceMeasurementUnit = params.get("ComponentPriceMeasurementUnit")
        self._ComponentUsage = params.get("ComponentUsage")
        self._ComponentUsageUnit = params.get("ComponentUsageUnit")
        self._UsageDuration = params.get("UsageDuration")
        self._DurationUnit = params.get("DurationUnit")
        self._OriginalCost = params.get("OriginalCost")
        self._Currency = params.get("Currency")
        self._TotalCost = params.get("TotalCost")
        self._Id = params.get("Id")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillDetailRequest(AbstractModel):
    """DescribeBillDetail request structure.

    """

    def __init__(self):
        r"""
        :param _Month: The queried month in the format of “YYYY-MM”, such as 2023-01.
        :type Month: str
        :param _PageSize: Page parameter: Indicates the number of entries per page. Value range: [1, 200]
        :type PageSize: int
        :param _Page: Page parameter: Indicates the current page number. The minimum value is 1.
        :type Page: int
        :param _PayMode: Billing mode. Valid values: `prePay` (Monthly subscription), postPay` (Pay-As-You-Go resources).
        :type PayMode: str
        :param _ActionType: Transaction type. Valid values: `prepay_purchase` (Purchase), `prepay_renew` (Renewal), `prepay_modify` (Upgrade/Downgrade), `prepay_return` ( Monthly subscription refund), `postpay_deduct` (Pay-as-you-go), `postpay_deduct_h` (Hourly settlement), `postpay_deduct_d` (Daily settlement), `postpay_deduct_m` (Monthly settlement), `offline_deduct` (Offline project deduction), `online_deduct` (Offline product deduction), `recon_deduct` (Adjustment - deduction), `recon_increase` (Adjustment - compensation), `ripay_purchase` (One-off RI Fee), `postpay_deduct_s` (Spot), `ri_hour_pay` (Hourly RI fee), `prePurchase` (New monthly subscription), `preRenew` (Monthly subscription renewal), `preUpgrade` (Upgrade/Downgrade), `preDowngrade` (Upgrade/Downgrade), `svp_hour_pay` (Hourly Savings Plan fee), `recon_guarantee` (Minimum spend deduction), `pre_purchase` (New monthly subscription), `pre_renew` (Monthly subscription renewal), `pre_upgrade` (Upgrade/Downgrade), `pre_downgrade` (Upgrade/Downgrade).
        :type ActionType: str
        """
        self._Month = None
        self._PageSize = None
        self._Page = None
        self._PayMode = None
        self._ActionType = None

    @property
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

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


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._PageSize = params.get("PageSize")
        self._Page = params.get("Page")
        self._PayMode = params.get("PayMode")
        self._ActionType = params.get("ActionType")
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
        :param _DetailSet: Data details
Note: This field may return null, indicating that no valid values can be obtained.
        :type DetailSet: list of CustomerBillDetailData
        :param _Total: Total number of data entries
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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
                obj = CustomerBillDetailData()
                obj._deserialize(item)
                self._DetailSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeBillDownloadUrlRequest(AbstractModel):
    """DescribeBillDownloadUrl request structure.

    """

    def __init__(self):
        r"""
        :param _Month: Bill month in the format of "yyyy-mm"; the earliest month available for query is June, 2022. Current month's billing data may be inaccurate; please download the current month's bill after it is generated at 1:00 on the 5th of the next month.
        :type Month: str
        :param _FileType: Type of bill. Valid values: L2 or L3
        :type FileType: str
        """
        self._Month = None
        self._FileType = None

    @property
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._FileType = params.get("FileType")
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
        :param _DownloadUrl: File download address, valid for one hour.
        :type DownloadUrl: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

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
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryByPayModeRequest(AbstractModel):
    """DescribeBillSummaryByPayMode request structure.

    """

    def __init__(self):
        r"""
        :param _BillMonth: Bill month in the format of "yyyy-MM"
        :type BillMonth: str
        :param _CustomerUin: Customer UIN
        :type CustomerUin: int
        """
        self._BillMonth = None
        self._CustomerUin = None

    @property
    def BillMonth(self):
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def CustomerUin(self):
        return self._CustomerUin

    @CustomerUin.setter
    def CustomerUin(self, CustomerUin):
        self._CustomerUin = CustomerUin


    def _deserialize(self, params):
        self._BillMonth = params.get("BillMonth")
        self._CustomerUin = params.get("CustomerUin")
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
        :param _SummaryOverview: Payment mode details in the customer bill data totaled by payment mode
Note: This field may return null, indicating that no valid values can be obtained.
        :type SummaryOverview: list of PayModeSummaryOverviewItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SummaryOverview = None
        self._RequestId = None

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
        :param _BillMonth: Bill month in the format of "yyyy-MM"
        :type BillMonth: str
        :param _CustomerUin: Customer UIN
        :type CustomerUin: int
        """
        self._BillMonth = None
        self._CustomerUin = None

    @property
    def BillMonth(self):
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def CustomerUin(self):
        return self._CustomerUin

    @CustomerUin.setter
    def CustomerUin(self, CustomerUin):
        self._CustomerUin = CustomerUin


    def _deserialize(self, params):
        self._BillMonth = params.get("BillMonth")
        self._CustomerUin = params.get("CustomerUin")
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
        :param _SummaryOverview: Bill details from the product dimension
Note: This field may return null, indicating that no valid values can be obtained.
        :type SummaryOverview: list of BusinessSummaryOverviewItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SummaryOverview = None
        self._RequestId = None

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
        if params.get("SummaryOverview") is not None:
            self._SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = BusinessSummaryOverviewItem()
                obj._deserialize(item)
                self._SummaryOverview.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryByRegionRequest(AbstractModel):
    """DescribeBillSummaryByRegion request structure.

    """

    def __init__(self):
        r"""
        :param _BillMonth: Bill month in the format of "yyyy-MM"
        :type BillMonth: str
        :param _CustomerUin: Customer UIN
        :type CustomerUin: int
        """
        self._BillMonth = None
        self._CustomerUin = None

    @property
    def BillMonth(self):
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def CustomerUin(self):
        return self._CustomerUin

    @CustomerUin.setter
    def CustomerUin(self, CustomerUin):
        self._CustomerUin = CustomerUin


    def _deserialize(self, params):
        self._BillMonth = params.get("BillMonth")
        self._CustomerUin = params.get("CustomerUin")
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
        :param _SummaryOverview: Region details in the customer bill data totaled by region
Note: This field may return null, indicating that no valid values can be obtained.
        :type SummaryOverview: list of RegionSummaryOverviewItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SummaryOverview = None
        self._RequestId = None

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
        if params.get("SummaryOverview") is not None:
            self._SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = RegionSummaryOverviewItem()
                obj._deserialize(item)
                self._SummaryOverview.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryRequest(AbstractModel):
    """DescribeBillSummary request structure.

    """

    def __init__(self):
        r"""
        :param _Month: Bill month in the format of "yyyy-mm".
        :type Month: str
        :param _GroupType: Billing dimension. Optional parameters: product, project, tag
        :type GroupType: str
        :param _TagKey: Tag value list
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
        :param _SummaryDetail: Detailed summary by billing dimensionNote: This field may return null, indicating that no valid values can be obtained.
        :type SummaryDetail: list of SummaryDetails
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SummaryDetail = None
        self._RequestId = None

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
        if params.get("SummaryDetail") is not None:
            self._SummaryDetail = []
            for item in params.get("SummaryDetail"):
                obj = SummaryDetails()
                obj._deserialize(item)
                self._SummaryDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCustomerBillDetailRequest(AbstractModel):
    """DescribeCustomerBillDetail request structure.

    """

    def __init__(self):
        r"""
        :param _CustomerUin: Customer UIN
        :type CustomerUin: int
        :param _Month: The queried month in “YYYY-MM” format, such as 2023-01.
        :type Month: str
        :param _PageSize: Page parameter: Indicates the number of entries per page. Value range: [1, 200]
        :type PageSize: int
        :param _Page: Page parameter: Indicates the current page number. The minimum value is 1.
        :type Page: int
        :param _PayMode: Billing mode. Valid values:
`prePay` (Monthly subscription)
`postPay` (Pay-as-you-go)
        :type PayMode: str
        :param _ActionType: Transaction type. Valid values:
`prepay_purchase` (Purchase)
`prepay_renew` (Renewal)
`prepay_modify` (Upgrade/Downgrade)
`prepay_return` ( Monthly subscription refund)
`postpay_deduct` (Pay-as-you-go)
`postpay_deduct_h` (Hourly settlement)
`postpay_deduct_d` (Daily settlement)
`postpay_deduct_m` (Monthly settlement)
`offline_deduct` (Offline project deduction)
`online_deduct` (Offline product deduction)
`recon_deduct` (Adjustment - deduction)
`recon_increase` (Adjustment - compensation)
`ripay_purchase` (One-off RI Fee)
`postpay_deduct_s` (Spot)
`ri_hour_pay` (Hourly RI fee)
`prePurchase` (New monthly subscription)
`preRenew` (Monthly subscription renewal)
`preUpgrade` (Upgrade/Downgrade)
`preDowngrade` (Upgrade/Downgrade)
`svp_hour_pay` (Hourly Savings Plan fee)
`recon_guarantee` (Minimum spend deduction)
`pre_purchase` (New monthly subscription)
`pre_renew` (Monthly subscription renewal)
`pre_upgrade` (Upgrade/Downgrade)
`pre_downgrade` (Upgrade/Downgrade)
        :type ActionType: str
        :param _IsConfirmed: Payment status
`0`: N/A
`1`: Paid
`2`: Unpaid
        :type IsConfirmed: str
        """
        self._CustomerUin = None
        self._Month = None
        self._PageSize = None
        self._Page = None
        self._PayMode = None
        self._ActionType = None
        self._IsConfirmed = None

    @property
    def CustomerUin(self):
        return self._CustomerUin

    @CustomerUin.setter
    def CustomerUin(self, CustomerUin):
        self._CustomerUin = CustomerUin

    @property
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

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
    def IsConfirmed(self):
        return self._IsConfirmed

    @IsConfirmed.setter
    def IsConfirmed(self, IsConfirmed):
        self._IsConfirmed = IsConfirmed


    def _deserialize(self, params):
        self._CustomerUin = params.get("CustomerUin")
        self._Month = params.get("Month")
        self._PageSize = params.get("PageSize")
        self._Page = params.get("Page")
        self._PayMode = params.get("PayMode")
        self._ActionType = params.get("ActionType")
        self._IsConfirmed = params.get("IsConfirmed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomerBillDetailResponse(AbstractModel):
    """DescribeCustomerBillDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of data entries
        :type Total: int
        :param _DetailSet: Data details
Note: This field may return null, indicating that no valid values can be obtained.
        :type DetailSet: list of BillDetailData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._DetailSet = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def DetailSet(self):
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("DetailSet") is not None:
            self._DetailSet = []
            for item in params.get("DetailSet"):
                obj = BillDetailData()
                obj._deserialize(item)
                self._DetailSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCustomerBillSummaryRequest(AbstractModel):
    """DescribeCustomerBillSummary request structure.

    """

    def __init__(self):
        r"""
        :param _CustomerUin: Customer UIN
        :type CustomerUin: int
        :param _Month: The queried month in “YYYY-MM” format, such as 2023-01.
        :type Month: str
        :param _PayMode: Billing mode. Valid values:
`prePay` (Monthly subscription)
`postPay` (Pay-as-you-go)
        :type PayMode: str
        :param _ActionType: Transaction type. Valid values:
`prepay_purchase` (Purchase)
`prepay_renew` (Renewal)
`prepay_modify` (Upgrade/Downgrade)
`prepay_return` (Monthly subscription refund)
`postpay_deduct` (Pay-as-you-go)
`postpay_deduct_h` (Hourly settlement)
`postpay_deduct_d` (Daily settlement)
`postpay_deduct_m` (Monthly settlement)
`offline_deduct` (Offline project deduction)
`online_deduct` (Offline product deduction)
`recon_deduct` (Adjustment - deduction)
`recon_increase` (Adjustment - compensation)
`ripay_purchase` (One-off RI Fee)
`postpay_deduct_s` (Spot)
`ri_hour_pay` (Hourly RI fee)
`prePurchase` (New monthly subscription)
`preRenew` (Monthly subscription renewal)
`preUpgrade` (Upgrade/Downgrade)
`preDowngrade` (Upgrade/Downgrade)
`svp_hour_pay` (Hourly Savings Plan fee)
`recon_guarantee` (Minimum spend deduction)
`pre_purchase` (New monthly subscription)
`pre_renew` (Monthly subscription renewal)
`pre_upgrade` (Upgrade/Downgrade)
`pre_downgrade` (Upgrade/Downgrade)
        :type ActionType: str
        :param _IsConfirmed: Payment status
`0`: N/A
`1`: Paid
`2`: Unpaid
        :type IsConfirmed: str
        """
        self._CustomerUin = None
        self._Month = None
        self._PayMode = None
        self._ActionType = None
        self._IsConfirmed = None

    @property
    def CustomerUin(self):
        return self._CustomerUin

    @CustomerUin.setter
    def CustomerUin(self, CustomerUin):
        self._CustomerUin = CustomerUin

    @property
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

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
    def IsConfirmed(self):
        return self._IsConfirmed

    @IsConfirmed.setter
    def IsConfirmed(self, IsConfirmed):
        self._IsConfirmed = IsConfirmed


    def _deserialize(self, params):
        self._CustomerUin = params.get("CustomerUin")
        self._Month = params.get("Month")
        self._PayMode = params.get("PayMode")
        self._ActionType = params.get("ActionType")
        self._IsConfirmed = params.get("IsConfirmed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomerBillSummaryResponse(AbstractModel):
    """DescribeCustomerBillSummary response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCost: Total amount
        :type TotalCost: float
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCost = None
        self._RequestId = None

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCost = params.get("TotalCost")
        self._RequestId = params.get("RequestId")


class DescribeCustomerInfoData(AbstractModel):
    """Customer information

    """

    def __init__(self):
        r"""
        :param _CustomerUin: Customer UIN Note: This field may return null, indicating that no valid values can be obtained.
        :type CustomerUin: str
        :param _Email: Email Note: This field may return null, indicating that no valid values can be obtained.
        :type Email: str
        :param _Phone: Mobile number Note: This field may return null, indicating that no valid values can be obtained.
        :type Phone: str
        :param _Mark: Remarks Note: This field may return null, indicating that no valid values can be obtained.
        :type Mark: str
        :param _Name: Displayed name Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _BindTime: Binding time Note: This field may return null, indicating that no valid values can be obtained.
        :type BindTime: str
        :param _AccountStatus: Account status
0: Normal
1: Forcibly mandatory (this function is not supported yet)
2. Mandatory arrears
Note: The return value may be null, indicating that no valid data can be obtained.
        :type AccountStatus: str
        :param _AuthStatus: Identity verification status
-1: Files not uploaded
0: Not submitted for review
1: Under review
2: Review error
3: Approved
Note: The return value may be null, indicating that no valid data can be obtained.
        :type AuthStatus: str
        """
        self._CustomerUin = None
        self._Email = None
        self._Phone = None
        self._Mark = None
        self._Name = None
        self._BindTime = None
        self._AccountStatus = None
        self._AuthStatus = None

    @property
    def CustomerUin(self):
        return self._CustomerUin

    @CustomerUin.setter
    def CustomerUin(self, CustomerUin):
        self._CustomerUin = CustomerUin

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
    def Mark(self):
        return self._Mark

    @Mark.setter
    def Mark(self, Mark):
        self._Mark = Mark

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BindTime(self):
        return self._BindTime

    @BindTime.setter
    def BindTime(self, BindTime):
        self._BindTime = BindTime

    @property
    def AccountStatus(self):
        return self._AccountStatus

    @AccountStatus.setter
    def AccountStatus(self, AccountStatus):
        self._AccountStatus = AccountStatus

    @property
    def AuthStatus(self):
        return self._AuthStatus

    @AuthStatus.setter
    def AuthStatus(self, AuthStatus):
        self._AuthStatus = AuthStatus


    def _deserialize(self, params):
        self._CustomerUin = params.get("CustomerUin")
        self._Email = params.get("Email")
        self._Phone = params.get("Phone")
        self._Mark = params.get("Mark")
        self._Name = params.get("Name")
        self._BindTime = params.get("BindTime")
        self._AccountStatus = params.get("AccountStatus")
        self._AuthStatus = params.get("AuthStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomerInfoRequest(AbstractModel):
    """DescribeCustomerInfo request structure.

    """

    def __init__(self):
        r"""
        :param _CustomerUin: List of customer UIN. Array length value: 1-20.
        :type CustomerUin: list of int
        """
        self._CustomerUin = None

    @property
    def CustomerUin(self):
        return self._CustomerUin

    @CustomerUin.setter
    def CustomerUin(self, CustomerUin):
        self._CustomerUin = CustomerUin


    def _deserialize(self, params):
        self._CustomerUin = params.get("CustomerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomerInfoResponse(AbstractModel):
    """DescribeCustomerInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Customer information Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of DescribeCustomerInfoData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeCustomerInfoData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCustomerUinData(AbstractModel):
    """List of customer UINs

    """

    def __init__(self):
        r"""
        :param _CustomerUin: Customer UIN Note: This field may return null, indicating that no valid values can be obtained.
        :type CustomerUin: str
        """
        self._CustomerUin = None

    @property
    def CustomerUin(self):
        return self._CustomerUin

    @CustomerUin.setter
    def CustomerUin(self, CustomerUin):
        self._CustomerUin = CustomerUin


    def _deserialize(self, params):
        self._CustomerUin = params.get("CustomerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomerUinRequest(AbstractModel):
    """DescribeCustomerUin request structure.

    """

    def __init__(self):
        r"""
        :param _Page: Page number
        :type Page: int
        :param _PageSize: Number of data entries per page
        :type PageSize: int
        """
        self._Page = None
        self._PageSize = None

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomerUinResponse(AbstractModel):
    """DescribeCustomerUin response structure.

    """

    def __init__(self):
        r"""
        :param _Data: List of customer UINs Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of DescribeCustomerUinData
        :param _Total: The number of customers
        :type Total: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeCustomerUinData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetCountryCodesRequest(AbstractModel):
    """GetCountryCodes request structure.

    """


class GetCountryCodesResponse(AbstractModel):
    """GetCountryCodes response structure.

    """

    def __init__(self):
        r"""
        :param _Data: List of country/region codes
        :type Data: list of CountryCodeItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CountryCodeItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyClientRemarkRequest(AbstractModel):
    """ModifyClientRemark request structure.

    """

    def __init__(self):
        r"""
        :param _ClientUin: Customer UIN
        :type ClientUin: str
        :param _Remark: New customer remarks
        :type Remark: str
        """
        self._ClientUin = None
        self._Remark = None

    @property
    def ClientUin(self):
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClientRemarkResponse(AbstractModel):
    """ModifyClientRemark response structure.

    """

    def __init__(self):
        r"""
        :param _ClientRemark: If successful, returns the new customer remarks
        :type ClientRemark: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClientRemark = None
        self._RequestId = None

    @property
    def ClientRemark(self):
        return self._ClientRemark

    @ClientRemark.setter
    def ClientRemark(self, ClientRemark):
        self._ClientRemark = ClientRemark

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClientRemark = params.get("ClientRemark")
        self._RequestId = params.get("RequestId")


class PayModeSummaryOverviewItem(AbstractModel):
    """Payment mode details in the customer bill data totaled by payment mode

    """

    def __init__(self):
        r"""
        :param _PayMode: Billing mode
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayMode: str
        :param _PayModeName: Billing mode name
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayModeName: str
        :param _OriginalCost: The actual total consumption amount accurate down to eight decimal places
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalCost: str
        :param _Detail: Bill details in each payment mode
Note: This field may return null, indicating that no valid values can be obtained.
        :type Detail: list of ActionSummaryOverviewItem
        :param _VoucherPayAmount: The deducted voucher amount accurate down to eight decimal places
Note: This field may return null, indicating that no valid values can be obtained.
        :type VoucherPayAmount: str
        :param _TotalCost: Total consumption amount accurate down to eight decimal places
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCost: str
        """
        self._PayMode = None
        self._PayModeName = None
        self._OriginalCost = None
        self._Detail = None
        self._VoucherPayAmount = None
        self._TotalCost = None

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
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._PayMode = params.get("PayMode")
        self._PayModeName = params.get("PayModeName")
        self._OriginalCost = params.get("OriginalCost")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = ActionSummaryOverviewItem()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAccountVerificationStatusRequest(AbstractModel):
    """QueryAccountVerificationStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ClientUin: Customer UIN
        :type ClientUin: int
        """
        self._ClientUin = None

    @property
    def ClientUin(self):
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAccountVerificationStatusResponse(AbstractModel):
    """QueryAccountVerificationStatus response structure.

    """

    def __init__(self):
        r"""
        :param _AccountStatus: Account verification status
        :type AccountStatus: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccountStatus = None
        self._RequestId = None

    @property
    def AccountStatus(self):
        return self._AccountStatus

    @AccountStatus.setter
    def AccountStatus(self, AccountStatus):
        self._AccountStatus = AccountStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AccountStatus = params.get("AccountStatus")
        self._RequestId = params.get("RequestId")


class QueryCreditAllocationHistoryData(AbstractModel):
    """Returned information for querying the customer credit allocation records

    """

    def __init__(self):
        r"""
        :param _AllocatedTime: Allocation time
        :type AllocatedTime: str
        :param _Operator: Operator
        :type Operator: str
        :param _Credit: Allocated credit value
        :type Credit: float
        :param _AllocatedCredit: The allocated total credit
        :type AllocatedCredit: float
        :param _ClientCreditAfter: Available credits after allocation
Note: The return value may be null, indicating that no valid data can be obtained.
        :type ClientCreditAfter: float
        """
        self._AllocatedTime = None
        self._Operator = None
        self._Credit = None
        self._AllocatedCredit = None
        self._ClientCreditAfter = None

    @property
    def AllocatedTime(self):
        return self._AllocatedTime

    @AllocatedTime.setter
    def AllocatedTime(self, AllocatedTime):
        self._AllocatedTime = AllocatedTime

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Credit(self):
        return self._Credit

    @Credit.setter
    def Credit(self, Credit):
        self._Credit = Credit

    @property
    def AllocatedCredit(self):
        return self._AllocatedCredit

    @AllocatedCredit.setter
    def AllocatedCredit(self, AllocatedCredit):
        self._AllocatedCredit = AllocatedCredit

    @property
    def ClientCreditAfter(self):
        return self._ClientCreditAfter

    @ClientCreditAfter.setter
    def ClientCreditAfter(self, ClientCreditAfter):
        self._ClientCreditAfter = ClientCreditAfter


    def _deserialize(self, params):
        self._AllocatedTime = params.get("AllocatedTime")
        self._Operator = params.get("Operator")
        self._Credit = params.get("Credit")
        self._AllocatedCredit = params.get("AllocatedCredit")
        self._ClientCreditAfter = params.get("ClientCreditAfter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCreditAllocationHistoryRequest(AbstractModel):
    """QueryCreditAllocationHistory request structure.

    """

    def __init__(self):
        r"""
        :param _ClientUin: Customer UIN
        :type ClientUin: int
        :param _Page: Page number
        :type Page: int
        :param _PageSize: Number of data entries per page
        :type PageSize: int
        """
        self._ClientUin = None
        self._Page = None
        self._PageSize = None

    @property
    def ClientUin(self):
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCreditAllocationHistoryResponse(AbstractModel):
    """QueryCreditAllocationHistory response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of records
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _History: List of record details
Note: This field may return null, indicating that no valid values can be obtained.
        :type History: list of QueryCreditAllocationHistoryData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._History = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def History(self):
        return self._History

    @History.setter
    def History(self, History):
        self._History = History

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("History") is not None:
            self._History = []
            for item in params.get("History"):
                obj = QueryCreditAllocationHistoryData()
                obj._deserialize(item)
                self._History.append(obj)
        self._RequestId = params.get("RequestId")


class QueryCreditByUinListRequest(AbstractModel):
    """QueryCreditByUinList request structure.

    """

    def __init__(self):
        r"""
        :param _UinList: List of user. Array length value: 1-50.
        :type UinList: list of int non-negative
        """
        self._UinList = None

    @property
    def UinList(self):
        return self._UinList

    @UinList.setter
    def UinList(self, UinList):
        self._UinList = UinList


    def _deserialize(self, params):
        self._UinList = params.get("UinList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCreditByUinListResponse(AbstractModel):
    """QueryCreditByUinList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: User information list
        :type Data: list of QueryDirectCustomersCreditData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = QueryDirectCustomersCreditData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class QueryCreditQuotaRequest(AbstractModel):
    """QueryCreditQuota request structure.

    """


class QueryCreditQuotaResponse(AbstractModel):
    """QueryCreditQuota response structure.

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


class QueryCustomersCreditData(AbstractModel):
    """Complex type of output parameters for querying customer's credit

    """

    def __init__(self):
        r"""
        :param _Name: Name
        :type Name: str
        :param _Type: Type
        :type Type: str
        :param _Mobile: Mobile number
        :type Mobile: str
        :param _Email: Email
        :type Email: str
        :param _Arrears: Overdue payment flag
        :type Arrears: str
        :param _AssociationTime: Binding time
        :type AssociationTime: str
        :param _RecentExpiry: Expiration time
        :type RecentExpiry: str
        :param _ClientUin: Customer UIN
        :type ClientUin: int
        :param _Credit: Credit allocated to a customer
        :type Credit: float
        :param _RemainingCredit: The remaining credit of a customer
        :type RemainingCredit: float
        :param _IdentifyType: `0`: Identity not verified; `1`: Individual identity verified; `2`: Enterprise identity verified.
        :type IdentifyType: int
        :param _Remark: Customer remarks
        :type Remark: str
        :param _Force: Forced status
        :type Force: int
        """
        self._Name = None
        self._Type = None
        self._Mobile = None
        self._Email = None
        self._Arrears = None
        self._AssociationTime = None
        self._RecentExpiry = None
        self._ClientUin = None
        self._Credit = None
        self._RemainingCredit = None
        self._IdentifyType = None
        self._Remark = None
        self._Force = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Arrears(self):
        return self._Arrears

    @Arrears.setter
    def Arrears(self, Arrears):
        self._Arrears = Arrears

    @property
    def AssociationTime(self):
        return self._AssociationTime

    @AssociationTime.setter
    def AssociationTime(self, AssociationTime):
        self._AssociationTime = AssociationTime

    @property
    def RecentExpiry(self):
        return self._RecentExpiry

    @RecentExpiry.setter
    def RecentExpiry(self, RecentExpiry):
        self._RecentExpiry = RecentExpiry

    @property
    def ClientUin(self):
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def Credit(self):
        return self._Credit

    @Credit.setter
    def Credit(self, Credit):
        self._Credit = Credit

    @property
    def RemainingCredit(self):
        return self._RemainingCredit

    @RemainingCredit.setter
    def RemainingCredit(self, RemainingCredit):
        self._RemainingCredit = RemainingCredit

    @property
    def IdentifyType(self):
        return self._IdentifyType

    @IdentifyType.setter
    def IdentifyType(self, IdentifyType):
        self._IdentifyType = IdentifyType

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Mobile = params.get("Mobile")
        self._Email = params.get("Email")
        self._Arrears = params.get("Arrears")
        self._AssociationTime = params.get("AssociationTime")
        self._RecentExpiry = params.get("RecentExpiry")
        self._ClientUin = params.get("ClientUin")
        self._Credit = params.get("Credit")
        self._RemainingCredit = params.get("RemainingCredit")
        self._IdentifyType = params.get("IdentifyType")
        self._Remark = params.get("Remark")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCustomersCreditRequest(AbstractModel):
    """QueryCustomersCredit request structure.

    """

    def __init__(self):
        r"""
        :param _FilterType: Search condition type. You can only search by customer ID, name, remarks, or email.
        :type FilterType: str
        :param _Filter: Search condition
        :type Filter: str
        :param _Page: A pagination parameter that specifies the current page number, with a value starting from 1.
        :type Page: int
        :param _PageSize: A pagination parameter that specifies the number of entries per page.
        :type PageSize: int
        :param _Order: A sort parameter that specifies the sort order. Valid values: `desc` (descending order), or `asc` (ascending order) based on `AssociationTime`. The value will be `desc` if left empty.
        :type Order: str
        """
        self._FilterType = None
        self._Filter = None
        self._Page = None
        self._PageSize = None
        self._Order = None

    @property
    def FilterType(self):
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._FilterType = params.get("FilterType")
        self._Filter = params.get("Filter")
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCustomersCreditResponse(AbstractModel):
    """QueryCustomersCredit response structure.

    """

    def __init__(self):
        r"""
        :param _Data: The list of queried customers
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of QueryCustomersCreditData
        :param _Total: Number of customers
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = QueryCustomersCreditData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class QueryDirectCustomersCreditData(AbstractModel):
    """The credit information of direct customers

    """

    def __init__(self):
        r"""
        :param _Uin: User UIN
        :type Uin: int
        :param _TotalCredit: Total credit
        :type TotalCredit: float
        :param _RemainingCredit: Remaining credit
        :type RemainingCredit: float
        """
        self._Uin = None
        self._TotalCredit = None
        self._RemainingCredit = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def TotalCredit(self):
        return self._TotalCredit

    @TotalCredit.setter
    def TotalCredit(self, TotalCredit):
        self._TotalCredit = TotalCredit

    @property
    def RemainingCredit(self):
        return self._RemainingCredit

    @RemainingCredit.setter
    def RemainingCredit(self, RemainingCredit):
        self._RemainingCredit = RemainingCredit


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._TotalCredit = params.get("TotalCredit")
        self._RemainingCredit = params.get("RemainingCredit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryDirectCustomersCreditRequest(AbstractModel):
    """QueryDirectCustomersCredit request structure.

    """


class QueryDirectCustomersCreditResponse(AbstractModel):
    """QueryDirectCustomersCredit response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Direct customer information list
        :type Data: list of QueryDirectCustomersCreditData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = QueryDirectCustomersCreditData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class QueryPartnerCreditRequest(AbstractModel):
    """QueryPartnerCredit request structure.

    """


class QueryPartnerCreditResponse(AbstractModel):
    """QueryPartnerCredit response structure.

    """

    def __init__(self):
        r"""
        :param _AllocatedCredit: Allocated credit
        :type AllocatedCredit: float
        :param _TotalCredit: Total credit
        :type TotalCredit: float
        :param _RemainingCredit: Remaining credit
        :type RemainingCredit: float
        :param _CustomerTotalCredit: Allocated quota for the client
        :type CustomerTotalCredit: float
        :param _CustomerRemainingCredit: Remaining quota for the client
        :type CustomerRemainingCredit: float
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AllocatedCredit = None
        self._TotalCredit = None
        self._RemainingCredit = None
        self._CustomerTotalCredit = None
        self._CustomerRemainingCredit = None
        self._RequestId = None

    @property
    def AllocatedCredit(self):
        return self._AllocatedCredit

    @AllocatedCredit.setter
    def AllocatedCredit(self, AllocatedCredit):
        self._AllocatedCredit = AllocatedCredit

    @property
    def TotalCredit(self):
        return self._TotalCredit

    @TotalCredit.setter
    def TotalCredit(self, TotalCredit):
        self._TotalCredit = TotalCredit

    @property
    def RemainingCredit(self):
        return self._RemainingCredit

    @RemainingCredit.setter
    def RemainingCredit(self, RemainingCredit):
        self._RemainingCredit = RemainingCredit

    @property
    def CustomerTotalCredit(self):
        return self._CustomerTotalCredit

    @CustomerTotalCredit.setter
    def CustomerTotalCredit(self, CustomerTotalCredit):
        self._CustomerTotalCredit = CustomerTotalCredit

    @property
    def CustomerRemainingCredit(self):
        return self._CustomerRemainingCredit

    @CustomerRemainingCredit.setter
    def CustomerRemainingCredit(self, CustomerRemainingCredit):
        self._CustomerRemainingCredit = CustomerRemainingCredit

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AllocatedCredit = params.get("AllocatedCredit")
        self._TotalCredit = params.get("TotalCredit")
        self._RemainingCredit = params.get("RemainingCredit")
        self._CustomerTotalCredit = params.get("CustomerTotalCredit")
        self._CustomerRemainingCredit = params.get("CustomerRemainingCredit")
        self._RequestId = params.get("RequestId")


class QueryVoucherAmountByUinItem(AbstractModel):
    """Customer voucher quota

    """

    def __init__(self):
        r"""
        :param _ClientUin: Customer UIN
        :type ClientUin: int
        :param _TotalAmount: Voucher quota
        :type TotalAmount: float
        :param _RemainAmount: Voucher amount
        :type RemainAmount: float
        """
        self._ClientUin = None
        self._TotalAmount = None
        self._RemainAmount = None

    @property
    def ClientUin(self):
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def TotalAmount(self):
        return self._TotalAmount

    @TotalAmount.setter
    def TotalAmount(self, TotalAmount):
        self._TotalAmount = TotalAmount

    @property
    def RemainAmount(self):
        return self._RemainAmount

    @RemainAmount.setter
    def RemainAmount(self, RemainAmount):
        self._RemainAmount = RemainAmount


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        self._TotalAmount = params.get("TotalAmount")
        self._RemainAmount = params.get("RemainAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryVoucherAmountByUinRequest(AbstractModel):
    """QueryVoucherAmountByUin request structure.

    """

    def __init__(self):
        r"""
        :param _ClientUins: Customer UIN list. Array length value: 1-20.
        :type ClientUins: list of int non-negative
        """
        self._ClientUins = None

    @property
    def ClientUins(self):
        return self._ClientUins

    @ClientUins.setter
    def ClientUins(self, ClientUins):
        self._ClientUins = ClientUins


    def _deserialize(self, params):
        self._ClientUins = params.get("ClientUins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryVoucherAmountByUinResponse(AbstractModel):
    """QueryVoucherAmountByUin response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Customer voucher quota information
        :type Data: list of QueryVoucherAmountByUinItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = QueryVoucherAmountByUinItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class QueryVoucherListByUinItem(AbstractModel):
    """Voucher information of a single customer

    """

    def __init__(self):
        r"""
        :param _ClientUin: Customer UIN
        :type ClientUin: int
        :param _TotalCount: The total number of vouchers
        :type TotalCount: int
        :param _Data: Voucher details
        :type Data: list of QueryVoucherListByUinVoucherItem
        """
        self._ClientUin = None
        self._TotalCount = None
        self._Data = None

    @property
    def ClientUin(self):
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = QueryVoucherListByUinVoucherItem()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryVoucherListByUinRequest(AbstractModel):
    """QueryVoucherListByUin request structure.

    """

    def __init__(self):
        r"""
        :param _ClientUins: Customer UIN list. Array length value: 1-20.
        :type ClientUins: list of int non-negative
        :param _Status: Voucher status. If this parameter is not passed in, all status will be queried by default. Valid values: `Unused`, `Used`, `Expired`.
        :type Status: str
        """
        self._ClientUins = None
        self._Status = None

    @property
    def ClientUins(self):
        return self._ClientUins

    @ClientUins.setter
    def ClientUins(self, ClientUins):
        self._ClientUins = ClientUins

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ClientUins = params.get("ClientUins")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryVoucherListByUinResponse(AbstractModel):
    """QueryVoucherListByUin response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Customer voucher information
        :type Data: list of QueryVoucherListByUinItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = QueryVoucherListByUinItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class QueryVoucherListByUinVoucherItem(AbstractModel):
    """Customer voucher information

    """

    def __init__(self):
        r"""
        :param _VoucherId: Voucher ID
        :type VoucherId: str
        :param _VoucherStatus: Voucher status
        :type VoucherStatus: str
        :param _TotalAmount: Voucher value
        :type TotalAmount: float
        :param _RemainAmount: Balance
        :type RemainAmount: float
        """
        self._VoucherId = None
        self._VoucherStatus = None
        self._TotalAmount = None
        self._RemainAmount = None

    @property
    def VoucherId(self):
        return self._VoucherId

    @VoucherId.setter
    def VoucherId(self, VoucherId):
        self._VoucherId = VoucherId

    @property
    def VoucherStatus(self):
        return self._VoucherStatus

    @VoucherStatus.setter
    def VoucherStatus(self, VoucherStatus):
        self._VoucherStatus = VoucherStatus

    @property
    def TotalAmount(self):
        return self._TotalAmount

    @TotalAmount.setter
    def TotalAmount(self, TotalAmount):
        self._TotalAmount = TotalAmount

    @property
    def RemainAmount(self):
        return self._RemainAmount

    @RemainAmount.setter
    def RemainAmount(self, RemainAmount):
        self._RemainAmount = RemainAmount


    def _deserialize(self, params):
        self._VoucherId = params.get("VoucherId")
        self._VoucherStatus = params.get("VoucherStatus")
        self._TotalAmount = params.get("TotalAmount")
        self._RemainAmount = params.get("RemainAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryVoucherPoolRequest(AbstractModel):
    """QueryVoucherPool request structure.

    """


class QueryVoucherPoolResponse(AbstractModel):
    """QueryVoucherPool response structure.

    """

    def __init__(self):
        r"""
        :param _AgentName: Reseller name
        :type AgentName: str
        :param _AccountType: Reseller role type (1: Reseller; 2: Distributor; 3: Second-level reseller)
        :type AccountType: int
        :param _TotalQuota: Total quota
        :type TotalQuota: float
        :param _RemainingQuota: Remaining quota
        :type RemainingQuota: float
        :param _IssuedNum: The number of issued vouchers
        :type IssuedNum: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AgentName = None
        self._AccountType = None
        self._TotalQuota = None
        self._RemainingQuota = None
        self._IssuedNum = None
        self._RequestId = None

    @property
    def AgentName(self):
        return self._AgentName

    @AgentName.setter
    def AgentName(self, AgentName):
        self._AgentName = AgentName

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def TotalQuota(self):
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def RemainingQuota(self):
        return self._RemainingQuota

    @RemainingQuota.setter
    def RemainingQuota(self, RemainingQuota):
        self._RemainingQuota = RemainingQuota

    @property
    def IssuedNum(self):
        return self._IssuedNum

    @IssuedNum.setter
    def IssuedNum(self, IssuedNum):
        self._IssuedNum = IssuedNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AgentName = params.get("AgentName")
        self._AccountType = params.get("AccountType")
        self._TotalQuota = params.get("TotalQuota")
        self._RemainingQuota = params.get("RemainingQuota")
        self._IssuedNum = params.get("IssuedNum")
        self._RequestId = params.get("RequestId")


class RegionSummaryOverviewItem(AbstractModel):
    """Region details in the customer bill data totaled by region

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionId: str
        :param _RegionName: Region name
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionName: str
        :param _OriginalCost: The actual total consumption amount accurate down to eight decimal places
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalCost: str
        :param _VoucherPayAmount: The deducted voucher amount accurate down to eight decimal places
Note: This field may return null, indicating that no valid values can be obtained.
        :type VoucherPayAmount: str
        :param _TotalCost: Total consumption amount accurate down to eight decimal places
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCost: str
        """
        self._RegionId = None
        self._RegionName = None
        self._OriginalCost = None
        self._VoucherPayAmount = None
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
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._OriginalCost = params.get("OriginalCost")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SummaryDetails(AbstractModel):
    """Detailed summary by billing dimension

    """

    def __init__(self):
        r"""
        :param _Business: Product information list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Business: list of BusinessInfo
        :param _OriginalCost: Original price
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalCost: str
        :param _VoucherPayAmount: Voucher amount
Note: This field may return null, indicating that no valid values can be obtained.
        :type VoucherPayAmount: str
        :param _RICost: Daily deduction
Note: This field may return null, indicating that no valid values can be obtained.
        :type RICost: str
        :param _TotalCost: Total amount
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCost: str
        :param _GroupKey: Summary key by classification dimension Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupKey: str
        :param _GroupValue:  Summary value by classification dimension
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupValue: str
        """
        self._Business = None
        self._OriginalCost = None
        self._VoucherPayAmount = None
        self._RICost = None
        self._TotalCost = None
        self._GroupKey = None
        self._GroupValue = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def RICost(self):
        return self._RICost

    @RICost.setter
    def RICost(self, RICost):
        self._RICost = RICost

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

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


    def _deserialize(self, params):
        if params.get("Business") is not None:
            self._Business = []
            for item in params.get("Business"):
                obj = BusinessInfo()
                obj._deserialize(item)
                self._Business.append(obj)
        self._OriginalCost = params.get("OriginalCost")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._RICost = params.get("RICost")
        self._TotalCost = params.get("TotalCost")
        self._GroupKey = params.get("GroupKey")
        self._GroupValue = params.get("GroupValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """Cost Allocation Tags

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag keyNote: This field may return null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param _TagValue: Tag valueNote: This field may return null, indicating that no valid values can be obtained.
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
        