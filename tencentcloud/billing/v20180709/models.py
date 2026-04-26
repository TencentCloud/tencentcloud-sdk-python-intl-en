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


class ActionSummaryOverviewItem(AbstractModel):
    r"""Detailed summary of costs by transaction type

    """

    def __init__(self):
        r"""
        :param _ActionType: Transaction type code
        :type ActionType: str
        :param _ActionTypeName: Transaction type, which can be yearly/monthly subscription purchase, yearly/monthly subscription renewal, or pay-as-you-go deduction.
        :type ActionTypeName: str
        :param _RealTotalCostRatio: Cost ratio, to two decimal points
        :type RealTotalCostRatio: str
        :param _RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param _CashPayAmount: Cash credit: The amount paid from the user's cash account
        :type CashPayAmount: str
        :param _IncentivePayAmount: Free credit: The amount paid with the user's free credit
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param _TransferPayAmount: Royalty account expenditure: The amount paid through the royalty account
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
        r"""Transaction type code
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        r"""Transaction type, which can be yearly/monthly subscription purchase, yearly/monthly subscription renewal, or pay-as-you-go deduction.
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def RealTotalCostRatio(self):
        r"""Cost ratio, to two decimal points
        :rtype: str
        """
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        r"""Total amount after discount
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        r"""Cash credit: The amount paid from the user's cash account
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Free credit: The amount paid with the user's free credit
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        r"""Voucher payment: The voucher deduction amount
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        r"""Royalty account expenditure: The amount paid through the royalty account
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def BillMonth(self):
        r"""Billing month, e.g. `2019-08`
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def TotalCost(self):
        r"""The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :rtype: str
        """
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
        


class AdjustInfoDetail(AbstractModel):
    r"""Abnormal adjustment details of UIN

    """

    def __init__(self):
        r"""
        :param _PayerUin: Payer UIN: Account ID of the payer, which is the unique account identifier for the user in Tencent Cloud.
        :type PayerUin: str
        :param _Month: Bill month, formatted as yyyy-MM.
        :type Month: str
        :param _AdjustType: Adjustment type
Bill adjustment: manualAdjustment
Supplementary settlement: supplementarySettlement
Re-settlement
        :type AdjustType: str
        :param _AdjustNum: Adjustment Number
        :type AdjustNum: str
        :param _AdjustCompletionTime: Abnormal adjustment completion time. Format: yyyy-MM-dd HH:mm:ss
        :type AdjustCompletionTime: str
        :param _AdjustAmount: Adjustment Amount
        :type AdjustAmount: float
        """
        self._PayerUin = None
        self._Month = None
        self._AdjustType = None
        self._AdjustNum = None
        self._AdjustCompletionTime = None
        self._AdjustAmount = None

    @property
    def PayerUin(self):
        r"""Payer UIN: Account ID of the payer, which is the unique account identifier for the user in Tencent Cloud.
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def Month(self):
        r"""Bill month, formatted as yyyy-MM.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def AdjustType(self):
        r"""Adjustment type
Bill adjustment: manualAdjustment
Supplementary settlement: supplementarySettlement
Re-settlement
        :rtype: str
        """
        return self._AdjustType

    @AdjustType.setter
    def AdjustType(self, AdjustType):
        self._AdjustType = AdjustType

    @property
    def AdjustNum(self):
        r"""Adjustment Number
        :rtype: str
        """
        return self._AdjustNum

    @AdjustNum.setter
    def AdjustNum(self, AdjustNum):
        self._AdjustNum = AdjustNum

    @property
    def AdjustCompletionTime(self):
        r"""Abnormal adjustment completion time. Format: yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._AdjustCompletionTime

    @AdjustCompletionTime.setter
    def AdjustCompletionTime(self, AdjustCompletionTime):
        self._AdjustCompletionTime = AdjustCompletionTime

    @property
    def AdjustAmount(self):
        r"""Adjustment Amount
        :rtype: float
        """
        return self._AdjustAmount

    @AdjustAmount.setter
    def AdjustAmount(self, AdjustAmount):
        self._AdjustAmount = AdjustAmount


    def _deserialize(self, params):
        self._PayerUin = params.get("PayerUin")
        self._Month = params.get("Month")
        self._AdjustType = params.get("AdjustType")
        self._AdjustNum = params.get("AdjustNum")
        self._AdjustCompletionTime = params.get("AdjustCompletionTime")
        self._AdjustAmount = params.get("AdjustAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationAverageData(AbstractModel):
    r"""Average value for the trend graph of a cost allocation bill

    """

    def __init__(self):
        r"""
        :param _BeginMonth: Start month
        :type BeginMonth: str
        :param _EndMonth: End month.
        :type EndMonth: str
        :param _RealTotalCost: Average value of total fees (discounted total)
        :type RealTotalCost: str
        """
        self._BeginMonth = None
        self._EndMonth = None
        self._RealTotalCost = None

    @property
    def BeginMonth(self):
        r"""Start month
        :rtype: str
        """
        return self._BeginMonth

    @BeginMonth.setter
    def BeginMonth(self, BeginMonth):
        self._BeginMonth = BeginMonth

    @property
    def EndMonth(self):
        r"""End month.
        :rtype: str
        """
        return self._EndMonth

    @EndMonth.setter
    def EndMonth(self, EndMonth):
        self._EndMonth = EndMonth

    @property
    def RealTotalCost(self):
        r"""Average value of total fees (discounted total)
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost


    def _deserialize(self, params):
        self._BeginMonth = params.get("BeginMonth")
        self._EndMonth = params.get("EndMonth")
        self._RealTotalCost = params.get("RealTotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationBillTrendDetail(AbstractModel):
    r"""Detail data of cost allocation trend chart

    """

    def __init__(self):
        r"""
        :param _Month: Bill month
        :type Month: str
        :param _Name: Displayed name of bill month
        :type Name: str
        :param _RealTotalCost: Total fees (discounted total): Total fees of the cost allocation unit, Collected Fees (discounted total) + Allocated Fees (discounted total)
        :type RealTotalCost: str
        """
        self._Month = None
        self._Name = None
        self._RealTotalCost = None

    @property
    def Month(self):
        r"""Bill month
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def Name(self):
        r"""Displayed name of bill month
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RealTotalCost(self):
        r"""Total fees (discounted total): Total fees of the cost allocation unit, Collected Fees (discounted total) + Allocated Fees (discounted total)
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._Name = params.get("Name")
        self._RealTotalCost = params.get("RealTotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationDetail(AbstractModel):
    r"""Details of a cost allocation bill

    """

    def __init__(self):
        r"""
        :param _TreeNodeUniqKey: Unique identifier of a cost allocation unit
        :type TreeNodeUniqKey: str
        :param _TreeNodeUniqKeyName: Name of a cost allocation unit
        :type TreeNodeUniqKeyName: str
        :param _BillDate: Date: Settlement date
        :type BillDate: str
        :param _PayerUin: Payer UIN: Account ID of the payer, which is the unique account identifier for the user in Tencent Cloud.
        :type PayerUin: str
        :param _OwnerUin: User UIN: Account ID of the actual resource user
        :type OwnerUin: str
        :param _OperateUin: Operator account ID (the resource account ID or role ID opened by prepaid resource ordering or postpaid operation)
        :type OperateUin: str
        :param _BusinessCode: Product code
        :type BusinessCode: str
        :param _BusinessCodeName: Product name: Various cloud products purchased by users
        :type BusinessCodeName: str
        :param _PayMode: Billing mode code
        :type PayMode: str
        :param _PayModeName: Billing mode: Resource billing mode, which can be monthly subscription or pay-as-you-go.
        :type PayModeName: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _ProjectName: Project name: The Project to which a resource belongs, which is independently allocated by the user for the resource in the console. If a resource has not been allocated to an Project, it will be a default Project.
        :type ProjectName: str
        :param _RegionId: Region ID
        :type RegionId: int
        :param _RegionName: Region name: The region where the resource is located
        :type RegionName: str
        :param _ZoneId: AZ ID
        :type ZoneId: int
        :param _ZoneName: Availability zone: The availability zone where the resource is located.
        :type ZoneName: str
        :param _ResourceId: Resource ID: Resources vary by product, and the content is not identical. For example, Cloud Virtual Machine (CVM) corresponds to the instance ID. If the product is split, it shows the split item ID, such as COS bucket ID and CDN domain name.
        :type ResourceId: str
        :param _ResourceName: Instance name: The name set by the user for the resource in the console, which is empty by default if not set. If the product is split, it shows the split resource alias.
        :type ResourceName: str
        :param _InstanceType: Instance type code
        :type InstanceType: str
        :param _InstanceTypeName: Instance type: The type of an instance corresponding to the product service purchased, including resource packages, RI, SP, and spot instances. It is displayed as "-" by default for regular instances.
        :type InstanceTypeName: str
        :param _SplitItemId: Split item ID: The ID of the split item involved in the split product, such as COS bucket ID and CDN domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SplitItemId: str
        :param _SplitItemName: Split item name: The split item involved in the split product
Note: This field may return null, indicating that no valid values can be obtained.
        :type SplitItemName: str
        :param _ProductCode: Subproduct code
        :type ProductCode: str
        :param _ProductCodeName: Subproduct name: Product subdivision type purchased by the user
        :type ProductCodeName: str
        :param _ActionType: Transaction type code
        :type ActionType: str
        :param _ActionTypeName: Transaction type: Detailed transaction type
        :type ActionTypeName: str
        :param _OrderId: Order ID: The order number for purchase in the annual and monthly billing mode

        :type OrderId: str
        :param _BillId: Transaction ID: The settlement and deduction number
        :type BillId: str
        :param _PayTime: Deduction time: Deduction time
        :type PayTime: str
        :param _FeeBeginTime: Usage start time: Usage start time
        :type FeeBeginTime: str
        :param _FeeEndTime: Usage end time: Product or service usage end time
        :type FeeEndTime: str
        :param _ComponentCode: Component type code
        :type ComponentCode: str
        :param _ComponentCodeName: Component type: The major component category corresponding to the product or service purchased by the user
        :type ComponentCodeName: str
        :param _SinglePrice: Component list price: The original unit price of the component on the portal (not displayed if the customer enjoys a fixed price/contract price)
        :type SinglePrice: str
        :param _ContractPrice: Component unit price: Discounted unit price of the component. Component unit price = list price * discount.
        :type ContractPrice: str
        :param _SinglePriceUnit: Component Price Unit: Unit of component price, Unit Composition: CNY/usage unit/duration unit
        :type SinglePriceUnit: str
        :param _UsedAmount: Component usage: The actual settlement usage of the component, Component Usage = Original Component Usage - Deducted Usage (including resource packages)
        :type UsedAmount: str
        :param _UsedAmountUnit: Component usage unit: Unit of measurement corresponding to component usage.
        :type UsedAmountUnit: str
        :param _TimeSpan: Usage duration: The duration of resource usage, Component Usage = Original Component Usage Duration - Deducted Duration (including resource packages)
        :type TimeSpan: str
        :param _TimeUnit: Duration unit: Unit of resource usage duration.
        :type TimeUnit: str
        :param _ReserveDetail: Remark attribute (instance configuration): Additional remark information, such as reserved instance type and transaction type for reserved instances, regional information of both ends for CCN products.
        :type ReserveDetail: str
        :param _SplitRatio: Split item usage/duration ratio: Split item usage (duration) ratio, Split Item Usage (Duration) /Total Usage Before Splitting (Duration)
        :type SplitRatio: str
        :param _TotalCost: Original price of a component: Original Price = Component List Price * Component Usage * Duration of Use (not displayed if the customer enjoys a fixed price/contract price, and not displayed by default in refund scenarios), specified price mode
        :type TotalCost: str
        :param _RITimeSpan: Reserved instance deduction duration: The duration of use deducted by reserved instances for this product or service.
        :type RITimeSpan: str
        :param _RICost: Original price deducted by a reserved instance: The original price of a component deducted by reserved instances for this product or service
        :type RICost: str
        :param _SPCost: Savings plan deduction from original price: Savings Plan Deduction from Original Price = Monetary Value of Savings Plan Deduction/ Savings Plan Deduction Rate
        :type SPCost: str
        :param _Discount: Discount rate: The discount rate enjoyed by this resource (it is not shown by default if the customer enjoys a fixed/contract price, and it is also not shown by default in the refund scenario)
        :type Discount: str
        :param _BlendedDiscount: Mixed discount rate: The final discount rate after integrating various discount deductions. Mixed Discount Rate = Discounted total price/Original Price.
        :type BlendedDiscount: str
        :param _RealTotalCost: Discounted total: discounted total = (Original Price - Original Price Deducted by a Reserved Instance - Savings Plan Deduction from Original Price) * Discount Rate
        :type RealTotalCost: str
        :param _CashPayAmount: Cash account expenditure (CNY): The amount paid through the cash account
        :type CashPayAmount: str
        :param _VoucherPayAmount: Promo voucher expenditure (CNY): The amount paid using various vouchers (such as promo vouchers and cash vouchers)
        :type VoucherPayAmount: str
        :param _IncentivePayAmount: Gift account expenditure (CNY): The amount paid using free credits
        :type IncentivePayAmount: str
        :param _TransferPayAmount: Royalty account expenditure (CNY): The amount paid through the royalty account
        :type TransferPayAmount: str
        :param _Tag: Allocation tag: The resource-bound tag
        :type Tag: list of BillTag
        :param _RegionType: Domestic and international codes
        :type RegionType: str
        :param _RegionTypeName: Domestic and international: Resource region type (domestic, international)
        :type RegionTypeName: str
        :param _ItemCode: Component name code
        :type ItemCode: str
        :param _ItemCodeName: Component name: The specific component of a product or service purchased by the user
        :type ItemCodeName: str
        :param _AssociatedOrder: Associated document ID: Document ID associated with this transaction, such as the original new purchase order corresponding to a refund order
        :type AssociatedOrder: str
        :param _PriceInfo: Price attribute: Other attributes of the component that affect discount pricing besides unit price and duration
        :type PriceInfo: list of str
        :param _Formula: Calculation rule explanation: A detailed explanation to calculations of billing settlement for special transaction types, such as refund and configuration changes.
        :type Formula: str
        :param _FormulaUrl: Billing Rules: The detailed billing rules for each product shown in the portal explanation link
        :type FormulaUrl: str
        :param _RealTotalMeasure: Original usage/duration: The original usage of the component before deduction by resource packages.
(Currently only TRTC, TEM, Cloud Call Center, and CDZ products support this information display. Other products are being integrated.)
        :type RealTotalMeasure: str
        :param _DeductedMeasure: Deduction of usage/duration (including resource packages): The amount of usage deducted by resource packages
(Currently only TRTC, TEM, Cloud Call Center, and CDZ products support this information display. Other products are being integrated.)
        :type DeductedMeasure: str
        :param _ComponentConfig: Configuration description: Information on specification of resource configuration
        :type ComponentConfig: str
        :param _AllocationType: Cost collection type: The source types of fees, including allocated, collection and unallocated.
0 - Allocation
1 - Collection
2 - Unallocated
        :type AllocationType: int
        :param _CostBeforeTax: CostBeforeTax
        :type CostBeforeTax: str
        :param _Tax: Tax
        :type Tax: str
        :param _AmountBeforeTax: AmountBeforeTax
        :type AmountBeforeTax: str
        :param _DiscountObject: Discount object of the current consumption item, such as official website discount, user discount and activity discount.
        :type DiscountObject: str
        :param _DiscountType: Discount type of the current consumption item, such as discount and contract price.
        :type DiscountType: str
        :param _DiscountContent: Supplementary description of the offer type, for example: business discount 20% off, the offer type is "discount" and the discount content is "0.8".
        :type DiscountContent: str
        :param _SPDeduction: SPDeduction
        :type SPDeduction: str
        :param _SPDeductionRate: SPDeduction
        :type SPDeductionRate: str
        :param _Currency: Currency
        :type Currency: str
        :param _BillMonth: Billing month
        :type BillMonth: str
        :param _TaxRate: tax rate
        :type TaxRate: str
        """
        self._TreeNodeUniqKey = None
        self._TreeNodeUniqKeyName = None
        self._BillDate = None
        self._PayerUin = None
        self._OwnerUin = None
        self._OperateUin = None
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._PayMode = None
        self._PayModeName = None
        self._ProjectId = None
        self._ProjectName = None
        self._RegionId = None
        self._RegionName = None
        self._ZoneId = None
        self._ZoneName = None
        self._ResourceId = None
        self._ResourceName = None
        self._InstanceType = None
        self._InstanceTypeName = None
        self._SplitItemId = None
        self._SplitItemName = None
        self._ProductCode = None
        self._ProductCodeName = None
        self._ActionType = None
        self._ActionTypeName = None
        self._OrderId = None
        self._BillId = None
        self._PayTime = None
        self._FeeBeginTime = None
        self._FeeEndTime = None
        self._ComponentCode = None
        self._ComponentCodeName = None
        self._SinglePrice = None
        self._ContractPrice = None
        self._SinglePriceUnit = None
        self._UsedAmount = None
        self._UsedAmountUnit = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._ReserveDetail = None
        self._SplitRatio = None
        self._TotalCost = None
        self._RITimeSpan = None
        self._RICost = None
        self._SPCost = None
        self._Discount = None
        self._BlendedDiscount = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._VoucherPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None
        self._Tag = None
        self._RegionType = None
        self._RegionTypeName = None
        self._ItemCode = None
        self._ItemCodeName = None
        self._AssociatedOrder = None
        self._PriceInfo = None
        self._Formula = None
        self._FormulaUrl = None
        self._RealTotalMeasure = None
        self._DeductedMeasure = None
        self._ComponentConfig = None
        self._AllocationType = None
        self._CostBeforeTax = None
        self._Tax = None
        self._AmountBeforeTax = None
        self._DiscountObject = None
        self._DiscountType = None
        self._DiscountContent = None
        self._SPDeduction = None
        self._SPDeductionRate = None
        self._Currency = None
        self._BillMonth = None
        self._TaxRate = None

    @property
    def TreeNodeUniqKey(self):
        r"""Unique identifier of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def TreeNodeUniqKeyName(self):
        r"""Name of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKeyName

    @TreeNodeUniqKeyName.setter
    def TreeNodeUniqKeyName(self, TreeNodeUniqKeyName):
        self._TreeNodeUniqKeyName = TreeNodeUniqKeyName

    @property
    def BillDate(self):
        r"""Date: Settlement date
        :rtype: str
        """
        return self._BillDate

    @BillDate.setter
    def BillDate(self, BillDate):
        self._BillDate = BillDate

    @property
    def PayerUin(self):
        r"""Payer UIN: Account ID of the payer, which is the unique account identifier for the user in Tencent Cloud.
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        r"""User UIN: Account ID of the actual resource user
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        r"""Operator account ID (the resource account ID or role ID opened by prepaid resource ordering or postpaid operation)
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def BusinessCode(self):
        r"""Product code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        r"""Product name: Various cloud products purchased by users
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def PayMode(self):
        r"""Billing mode code
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        r"""Billing mode: Resource billing mode, which can be monthly subscription or pay-as-you-go.
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""Project name: The Project to which a resource belongs, which is independently allocated by the user for the resource in the console. If a resource has not been allocated to an Project, it will be a default Project.
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionId(self):
        r"""Region ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        r"""Region name: The region where the resource is located
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneId(self):
        r"""AZ ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        r"""Availability zone: The availability zone where the resource is located.
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        r"""Resource ID: Resources vary by product, and the content is not identical. For example, Cloud Virtual Machine (CVM) corresponds to the instance ID. If the product is split, it shows the split item ID, such as COS bucket ID and CDN domain name.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        r"""Instance name: The name set by the user for the resource in the console, which is empty by default if not set. If the product is split, it shows the split resource alias.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def InstanceType(self):
        r"""Instance type code
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceTypeName(self):
        r"""Instance type: The type of an instance corresponding to the product service purchased, including resource packages, RI, SP, and spot instances. It is displayed as "-" by default for regular instances.
        :rtype: str
        """
        return self._InstanceTypeName

    @InstanceTypeName.setter
    def InstanceTypeName(self, InstanceTypeName):
        self._InstanceTypeName = InstanceTypeName

    @property
    def SplitItemId(self):
        warnings.warn("parameter `SplitItemId` is deprecated", DeprecationWarning) 

        r"""Split item ID: The ID of the split item involved in the split product, such as COS bucket ID and CDN domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SplitItemId

    @SplitItemId.setter
    def SplitItemId(self, SplitItemId):
        warnings.warn("parameter `SplitItemId` is deprecated", DeprecationWarning) 

        self._SplitItemId = SplitItemId

    @property
    def SplitItemName(self):
        warnings.warn("parameter `SplitItemName` is deprecated", DeprecationWarning) 

        r"""Split item name: The split item involved in the split product
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SplitItemName

    @SplitItemName.setter
    def SplitItemName(self, SplitItemName):
        warnings.warn("parameter `SplitItemName` is deprecated", DeprecationWarning) 

        self._SplitItemName = SplitItemName

    @property
    def ProductCode(self):
        r"""Subproduct code
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductCodeName(self):
        r"""Subproduct name: Product subdivision type purchased by the user
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def ActionType(self):
        r"""Transaction type code
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        r"""Transaction type: Detailed transaction type
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        r"""Order ID: The order number for purchase in the annual and monthly billing mode

        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def BillId(self):
        r"""Transaction ID: The settlement and deduction number
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def PayTime(self):
        r"""Deduction time: Deduction time
        :rtype: str
        """
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def FeeBeginTime(self):
        r"""Usage start time: Usage start time
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        r"""Usage end time: Product or service usage end time
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ComponentCode(self):
        r"""Component type code
        :rtype: str
        """
        return self._ComponentCode

    @ComponentCode.setter
    def ComponentCode(self, ComponentCode):
        self._ComponentCode = ComponentCode

    @property
    def ComponentCodeName(self):
        r"""Component type: The major component category corresponding to the product or service purchased by the user
        :rtype: str
        """
        return self._ComponentCodeName

    @ComponentCodeName.setter
    def ComponentCodeName(self, ComponentCodeName):
        self._ComponentCodeName = ComponentCodeName

    @property
    def SinglePrice(self):
        r"""Component list price: The original unit price of the component on the portal (not displayed if the customer enjoys a fixed price/contract price)
        :rtype: str
        """
        return self._SinglePrice

    @SinglePrice.setter
    def SinglePrice(self, SinglePrice):
        self._SinglePrice = SinglePrice

    @property
    def ContractPrice(self):
        r"""Component unit price: Discounted unit price of the component. Component unit price = list price * discount.
        :rtype: str
        """
        return self._ContractPrice

    @ContractPrice.setter
    def ContractPrice(self, ContractPrice):
        self._ContractPrice = ContractPrice

    @property
    def SinglePriceUnit(self):
        r"""Component Price Unit: Unit of component price, Unit Composition: CNY/usage unit/duration unit
        :rtype: str
        """
        return self._SinglePriceUnit

    @SinglePriceUnit.setter
    def SinglePriceUnit(self, SinglePriceUnit):
        self._SinglePriceUnit = SinglePriceUnit

    @property
    def UsedAmount(self):
        r"""Component usage: The actual settlement usage of the component, Component Usage = Original Component Usage - Deducted Usage (including resource packages)
        :rtype: str
        """
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

    @property
    def UsedAmountUnit(self):
        r"""Component usage unit: Unit of measurement corresponding to component usage.
        :rtype: str
        """
        return self._UsedAmountUnit

    @UsedAmountUnit.setter
    def UsedAmountUnit(self, UsedAmountUnit):
        self._UsedAmountUnit = UsedAmountUnit

    @property
    def TimeSpan(self):
        r"""Usage duration: The duration of resource usage, Component Usage = Original Component Usage Duration - Deducted Duration (including resource packages)
        :rtype: str
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        r"""Duration unit: Unit of resource usage duration.
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def ReserveDetail(self):
        r"""Remark attribute (instance configuration): Additional remark information, such as reserved instance type and transaction type for reserved instances, regional information of both ends for CCN products.
        :rtype: str
        """
        return self._ReserveDetail

    @ReserveDetail.setter
    def ReserveDetail(self, ReserveDetail):
        self._ReserveDetail = ReserveDetail

    @property
    def SplitRatio(self):
        r"""Split item usage/duration ratio: Split item usage (duration) ratio, Split Item Usage (Duration) /Total Usage Before Splitting (Duration)
        :rtype: str
        """
        return self._SplitRatio

    @SplitRatio.setter
    def SplitRatio(self, SplitRatio):
        self._SplitRatio = SplitRatio

    @property
    def TotalCost(self):
        r"""Original price of a component: Original Price = Component List Price * Component Usage * Duration of Use (not displayed if the customer enjoys a fixed price/contract price, and not displayed by default in refund scenarios), specified price mode
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RITimeSpan(self):
        r"""Reserved instance deduction duration: The duration of use deducted by reserved instances for this product or service.
        :rtype: str
        """
        return self._RITimeSpan

    @RITimeSpan.setter
    def RITimeSpan(self, RITimeSpan):
        self._RITimeSpan = RITimeSpan

    @property
    def RICost(self):
        r"""Original price deducted by a reserved instance: The original price of a component deducted by reserved instances for this product or service
        :rtype: str
        """
        return self._RICost

    @RICost.setter
    def RICost(self, RICost):
        self._RICost = RICost

    @property
    def SPCost(self):
        r"""Savings plan deduction from original price: Savings Plan Deduction from Original Price = Monetary Value of Savings Plan Deduction/ Savings Plan Deduction Rate
        :rtype: str
        """
        return self._SPCost

    @SPCost.setter
    def SPCost(self, SPCost):
        self._SPCost = SPCost

    @property
    def Discount(self):
        r"""Discount rate: The discount rate enjoyed by this resource (it is not shown by default if the customer enjoys a fixed/contract price, and it is also not shown by default in the refund scenario)
        :rtype: str
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def BlendedDiscount(self):
        r"""Mixed discount rate: The final discount rate after integrating various discount deductions. Mixed Discount Rate = Discounted total price/Original Price.
        :rtype: str
        """
        return self._BlendedDiscount

    @BlendedDiscount.setter
    def BlendedDiscount(self, BlendedDiscount):
        self._BlendedDiscount = BlendedDiscount

    @property
    def RealTotalCost(self):
        r"""Discounted total: discounted total = (Original Price - Original Price Deducted by a Reserved Instance - Savings Plan Deduction from Original Price) * Discount Rate
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        r"""Cash account expenditure (CNY): The amount paid through the cash account
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def VoucherPayAmount(self):
        r"""Promo voucher expenditure (CNY): The amount paid using various vouchers (such as promo vouchers and cash vouchers)
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Gift account expenditure (CNY): The amount paid using free credits
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        r"""Royalty account expenditure (CNY): The amount paid through the royalty account
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def Tag(self):
        r"""Allocation tag: The resource-bound tag
        :rtype: list of BillTag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def RegionType(self):
        r"""Domestic and international codes
        :rtype: str
        """
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def RegionTypeName(self):
        r"""Domestic and international: Resource region type (domestic, international)
        :rtype: str
        """
        return self._RegionTypeName

    @RegionTypeName.setter
    def RegionTypeName(self, RegionTypeName):
        self._RegionTypeName = RegionTypeName

    @property
    def ItemCode(self):
        r"""Component name code
        :rtype: str
        """
        return self._ItemCode

    @ItemCode.setter
    def ItemCode(self, ItemCode):
        self._ItemCode = ItemCode

    @property
    def ItemCodeName(self):
        r"""Component name: The specific component of a product or service purchased by the user
        :rtype: str
        """
        return self._ItemCodeName

    @ItemCodeName.setter
    def ItemCodeName(self, ItemCodeName):
        self._ItemCodeName = ItemCodeName

    @property
    def AssociatedOrder(self):
        r"""Associated document ID: Document ID associated with this transaction, such as the original new purchase order corresponding to a refund order
        :rtype: str
        """
        return self._AssociatedOrder

    @AssociatedOrder.setter
    def AssociatedOrder(self, AssociatedOrder):
        self._AssociatedOrder = AssociatedOrder

    @property
    def PriceInfo(self):
        r"""Price attribute: Other attributes of the component that affect discount pricing besides unit price and duration
        :rtype: list of str
        """
        return self._PriceInfo

    @PriceInfo.setter
    def PriceInfo(self, PriceInfo):
        self._PriceInfo = PriceInfo

    @property
    def Formula(self):
        r"""Calculation rule explanation: A detailed explanation to calculations of billing settlement for special transaction types, such as refund and configuration changes.
        :rtype: str
        """
        return self._Formula

    @Formula.setter
    def Formula(self, Formula):
        self._Formula = Formula

    @property
    def FormulaUrl(self):
        r"""Billing Rules: The detailed billing rules for each product shown in the portal explanation link
        :rtype: str
        """
        return self._FormulaUrl

    @FormulaUrl.setter
    def FormulaUrl(self, FormulaUrl):
        self._FormulaUrl = FormulaUrl

    @property
    def RealTotalMeasure(self):
        r"""Original usage/duration: The original usage of the component before deduction by resource packages.
(Currently only TRTC, TEM, Cloud Call Center, and CDZ products support this information display. Other products are being integrated.)
        :rtype: str
        """
        return self._RealTotalMeasure

    @RealTotalMeasure.setter
    def RealTotalMeasure(self, RealTotalMeasure):
        self._RealTotalMeasure = RealTotalMeasure

    @property
    def DeductedMeasure(self):
        r"""Deduction of usage/duration (including resource packages): The amount of usage deducted by resource packages
(Currently only TRTC, TEM, Cloud Call Center, and CDZ products support this information display. Other products are being integrated.)
        :rtype: str
        """
        return self._DeductedMeasure

    @DeductedMeasure.setter
    def DeductedMeasure(self, DeductedMeasure):
        self._DeductedMeasure = DeductedMeasure

    @property
    def ComponentConfig(self):
        r"""Configuration description: Information on specification of resource configuration
        :rtype: str
        """
        return self._ComponentConfig

    @ComponentConfig.setter
    def ComponentConfig(self, ComponentConfig):
        self._ComponentConfig = ComponentConfig

    @property
    def AllocationType(self):
        r"""Cost collection type: The source types of fees, including allocated, collection and unallocated.
0 - Allocation
1 - Collection
2 - Unallocated
        :rtype: int
        """
        return self._AllocationType

    @AllocationType.setter
    def AllocationType(self, AllocationType):
        self._AllocationType = AllocationType

    @property
    def CostBeforeTax(self):
        r"""CostBeforeTax
        :rtype: str
        """
        return self._CostBeforeTax

    @CostBeforeTax.setter
    def CostBeforeTax(self, CostBeforeTax):
        self._CostBeforeTax = CostBeforeTax

    @property
    def Tax(self):
        r"""Tax
        :rtype: str
        """
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def AmountBeforeTax(self):
        r"""AmountBeforeTax
        :rtype: str
        """
        return self._AmountBeforeTax

    @AmountBeforeTax.setter
    def AmountBeforeTax(self, AmountBeforeTax):
        self._AmountBeforeTax = AmountBeforeTax

    @property
    def DiscountObject(self):
        r"""Discount object of the current consumption item, such as official website discount, user discount and activity discount.
        :rtype: str
        """
        return self._DiscountObject

    @DiscountObject.setter
    def DiscountObject(self, DiscountObject):
        self._DiscountObject = DiscountObject

    @property
    def DiscountType(self):
        r"""Discount type of the current consumption item, such as discount and contract price.
        :rtype: str
        """
        return self._DiscountType

    @DiscountType.setter
    def DiscountType(self, DiscountType):
        self._DiscountType = DiscountType

    @property
    def DiscountContent(self):
        r"""Supplementary description of the offer type, for example: business discount 20% off, the offer type is "discount" and the discount content is "0.8".
        :rtype: str
        """
        return self._DiscountContent

    @DiscountContent.setter
    def DiscountContent(self, DiscountContent):
        self._DiscountContent = DiscountContent

    @property
    def SPDeduction(self):
        r"""SPDeduction
        :rtype: str
        """
        return self._SPDeduction

    @SPDeduction.setter
    def SPDeduction(self, SPDeduction):
        self._SPDeduction = SPDeduction

    @property
    def SPDeductionRate(self):
        r"""SPDeduction
        :rtype: str
        """
        return self._SPDeductionRate

    @SPDeductionRate.setter
    def SPDeductionRate(self, SPDeductionRate):
        self._SPDeductionRate = SPDeductionRate

    @property
    def Currency(self):
        r"""Currency
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def BillMonth(self):
        r"""Billing month
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def TaxRate(self):
        r"""tax rate
        :rtype: str
        """
        return self._TaxRate

    @TaxRate.setter
    def TaxRate(self, TaxRate):
        self._TaxRate = TaxRate


    def _deserialize(self, params):
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._TreeNodeUniqKeyName = params.get("TreeNodeUniqKeyName")
        self._BillDate = params.get("BillDate")
        self._PayerUin = params.get("PayerUin")
        self._OwnerUin = params.get("OwnerUin")
        self._OperateUin = params.get("OperateUin")
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._PayMode = params.get("PayMode")
        self._PayModeName = params.get("PayModeName")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._InstanceType = params.get("InstanceType")
        self._InstanceTypeName = params.get("InstanceTypeName")
        self._SplitItemId = params.get("SplitItemId")
        self._SplitItemName = params.get("SplitItemName")
        self._ProductCode = params.get("ProductCode")
        self._ProductCodeName = params.get("ProductCodeName")
        self._ActionType = params.get("ActionType")
        self._ActionTypeName = params.get("ActionTypeName")
        self._OrderId = params.get("OrderId")
        self._BillId = params.get("BillId")
        self._PayTime = params.get("PayTime")
        self._FeeBeginTime = params.get("FeeBeginTime")
        self._FeeEndTime = params.get("FeeEndTime")
        self._ComponentCode = params.get("ComponentCode")
        self._ComponentCodeName = params.get("ComponentCodeName")
        self._SinglePrice = params.get("SinglePrice")
        self._ContractPrice = params.get("ContractPrice")
        self._SinglePriceUnit = params.get("SinglePriceUnit")
        self._UsedAmount = params.get("UsedAmount")
        self._UsedAmountUnit = params.get("UsedAmountUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._ReserveDetail = params.get("ReserveDetail")
        self._SplitRatio = params.get("SplitRatio")
        self._TotalCost = params.get("TotalCost")
        self._RITimeSpan = params.get("RITimeSpan")
        self._RICost = params.get("RICost")
        self._SPCost = params.get("SPCost")
        self._Discount = params.get("Discount")
        self._BlendedDiscount = params.get("BlendedDiscount")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = BillTag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._RegionType = params.get("RegionType")
        self._RegionTypeName = params.get("RegionTypeName")
        self._ItemCode = params.get("ItemCode")
        self._ItemCodeName = params.get("ItemCodeName")
        self._AssociatedOrder = params.get("AssociatedOrder")
        self._PriceInfo = params.get("PriceInfo")
        self._Formula = params.get("Formula")
        self._FormulaUrl = params.get("FormulaUrl")
        self._RealTotalMeasure = params.get("RealTotalMeasure")
        self._DeductedMeasure = params.get("DeductedMeasure")
        self._ComponentConfig = params.get("ComponentConfig")
        self._AllocationType = params.get("AllocationType")
        self._CostBeforeTax = params.get("CostBeforeTax")
        self._Tax = params.get("Tax")
        self._AmountBeforeTax = params.get("AmountBeforeTax")
        self._DiscountObject = params.get("DiscountObject")
        self._DiscountType = params.get("DiscountType")
        self._DiscountContent = params.get("DiscountContent")
        self._SPDeduction = params.get("SPDeduction")
        self._SPDeductionRate = params.get("SPDeductionRate")
        self._Currency = params.get("Currency")
        self._BillMonth = params.get("BillMonth")
        self._TaxRate = params.get("TaxRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationMonthOverviewDetail(AbstractModel):
    r"""Monthly overview amount details of a cost allocation bill

    """

    def __init__(self):
        r"""
        :param _GatherCashPayAmount: Collected fees (cash): Cash directly collected to the cost allocation unit based on the collection rules
        :type GatherCashPayAmount: str
        :param _GatherVoucherPayAmount: Collected fees (voucher): Resource vouchers directly collected to the cost allocation unit based on the collection rules
        :type GatherVoucherPayAmount: str
        :param _GatherIncentivePayAmount: Collected fees (free credit): Resource free credit directly collected to the cost allocation unit based on the collection rules
        :type GatherIncentivePayAmount: str
        :param _GatherTransferPayAmount: Collected fees (royalty amount): Resource royalty amount directly collected to the cost allocation unit based on the collection rules
        :type GatherTransferPayAmount: str
        :param _AllocateCashPayAmount: Allocated fees (cash): Resource cash allocated to the cost allocation unit based on the allocation rules
        :type AllocateCashPayAmount: str
        :param _AllocateVoucherPayAmount: Allocated fees (vouchers): Resource vouchers allocated to the cost allocation unit based on the allocation rules
        :type AllocateVoucherPayAmount: str
        :param _AllocateIncentivePayAmount: Allocated fees (free credit): Resource free credit allocated to the cost allocation unit based on the allocation rules
        :type AllocateIncentivePayAmount: str
        :param _AllocateTransferPayAmount: Allocated fees (royalty amount): Resource royalty amount allocated to the cost allocation unit based on the allocation rules
        :type AllocateTransferPayAmount: str
        :param _TotalCashPayAmount: Total fees (cash): Total fees of the cost allocation unit, Collected Fees (Cash) + Allocated fees (Cash)
        :type TotalCashPayAmount: str
        :param _TotalVoucherPayAmount: Total fees (voucher): Total fees of the cost allocation unit, Collected Fees (Voucher) + Allocated fees (Voucher)
        :type TotalVoucherPayAmount: str
        :param _TotalIncentivePayAmount: Total fees (free credit): Total fees of the cost allocation unit, Collected Fees (Free Credit) + Allocated fees (Free Credit)
        :type TotalIncentivePayAmount: str
        :param _TotalTransferPayAmount: Total fees (royalty amount): Total cost of the cost allocation unit, Collected Fees (Royalty Amount) + Allocated fees (Royalty Amount)
        :type TotalTransferPayAmount: str
        :param _GatherRealCost: Collected fees (discounted total): Total resource amount after discount directly collected to the cost allocation unit based on the collection rules
        :type GatherRealCost: str
        :param _AllocateRealCost: Allocated fees (discounted total): Total resource amount after discount directly allocated to the cost allocation unit based on the allocation rules
        :type AllocateRealCost: str
        :param _RealTotalCost: Total fees (discounted total): Total fees of the cost allocation unit, Collected Fees (discounted total) + Allocated fees (discounted total)
        :type RealTotalCost: str
        :param _Ratio: Proportion (discounted total): Total fees (discounted total) of the Cost Allocation Unit/Total Fees (discounted total) * 100%
        :type Ratio: str
        :param _Trend: Month-on-month ratio (discounted total): [Total fees (discounted total) of the cost allocation unit in this month - Total fees (discounted total) of the cost allocation unit in the previous month]/Total fees (discounted total) of the cost allocation unit in the previous month * 100%
        :type Trend: str
        :param _TrendType: Sequential Comparison Arrow
upward - Upward
downward - Downward
none - Stable
        :type TrendType: str
        :param _AllocateCostBeforeTax: AllocateCostBeforeTax
        :type AllocateCostBeforeTax: str
        :param _GatherCostBeforeTax: GatherCostBeforeTax
        :type GatherCostBeforeTax: str
        :param _TotalCostBeforeTax: TotalCostBeforeTax
        :type TotalCostBeforeTax: str
        :param _AllocateTax: AllocateTax
        :type AllocateTax: str
        :param _GatherTax: GatherTax
        :type GatherTax: str
        :param _TotalTax: TotalTax
        :type TotalTax: str
        """
        self._GatherCashPayAmount = None
        self._GatherVoucherPayAmount = None
        self._GatherIncentivePayAmount = None
        self._GatherTransferPayAmount = None
        self._AllocateCashPayAmount = None
        self._AllocateVoucherPayAmount = None
        self._AllocateIncentivePayAmount = None
        self._AllocateTransferPayAmount = None
        self._TotalCashPayAmount = None
        self._TotalVoucherPayAmount = None
        self._TotalIncentivePayAmount = None
        self._TotalTransferPayAmount = None
        self._GatherRealCost = None
        self._AllocateRealCost = None
        self._RealTotalCost = None
        self._Ratio = None
        self._Trend = None
        self._TrendType = None
        self._AllocateCostBeforeTax = None
        self._GatherCostBeforeTax = None
        self._TotalCostBeforeTax = None
        self._AllocateTax = None
        self._GatherTax = None
        self._TotalTax = None

    @property
    def GatherCashPayAmount(self):
        r"""Collected fees (cash): Cash directly collected to the cost allocation unit based on the collection rules
        :rtype: str
        """
        return self._GatherCashPayAmount

    @GatherCashPayAmount.setter
    def GatherCashPayAmount(self, GatherCashPayAmount):
        self._GatherCashPayAmount = GatherCashPayAmount

    @property
    def GatherVoucherPayAmount(self):
        r"""Collected fees (voucher): Resource vouchers directly collected to the cost allocation unit based on the collection rules
        :rtype: str
        """
        return self._GatherVoucherPayAmount

    @GatherVoucherPayAmount.setter
    def GatherVoucherPayAmount(self, GatherVoucherPayAmount):
        self._GatherVoucherPayAmount = GatherVoucherPayAmount

    @property
    def GatherIncentivePayAmount(self):
        r"""Collected fees (free credit): Resource free credit directly collected to the cost allocation unit based on the collection rules
        :rtype: str
        """
        return self._GatherIncentivePayAmount

    @GatherIncentivePayAmount.setter
    def GatherIncentivePayAmount(self, GatherIncentivePayAmount):
        self._GatherIncentivePayAmount = GatherIncentivePayAmount

    @property
    def GatherTransferPayAmount(self):
        r"""Collected fees (royalty amount): Resource royalty amount directly collected to the cost allocation unit based on the collection rules
        :rtype: str
        """
        return self._GatherTransferPayAmount

    @GatherTransferPayAmount.setter
    def GatherTransferPayAmount(self, GatherTransferPayAmount):
        self._GatherTransferPayAmount = GatherTransferPayAmount

    @property
    def AllocateCashPayAmount(self):
        r"""Allocated fees (cash): Resource cash allocated to the cost allocation unit based on the allocation rules
        :rtype: str
        """
        return self._AllocateCashPayAmount

    @AllocateCashPayAmount.setter
    def AllocateCashPayAmount(self, AllocateCashPayAmount):
        self._AllocateCashPayAmount = AllocateCashPayAmount

    @property
    def AllocateVoucherPayAmount(self):
        r"""Allocated fees (vouchers): Resource vouchers allocated to the cost allocation unit based on the allocation rules
        :rtype: str
        """
        return self._AllocateVoucherPayAmount

    @AllocateVoucherPayAmount.setter
    def AllocateVoucherPayAmount(self, AllocateVoucherPayAmount):
        self._AllocateVoucherPayAmount = AllocateVoucherPayAmount

    @property
    def AllocateIncentivePayAmount(self):
        r"""Allocated fees (free credit): Resource free credit allocated to the cost allocation unit based on the allocation rules
        :rtype: str
        """
        return self._AllocateIncentivePayAmount

    @AllocateIncentivePayAmount.setter
    def AllocateIncentivePayAmount(self, AllocateIncentivePayAmount):
        self._AllocateIncentivePayAmount = AllocateIncentivePayAmount

    @property
    def AllocateTransferPayAmount(self):
        r"""Allocated fees (royalty amount): Resource royalty amount allocated to the cost allocation unit based on the allocation rules
        :rtype: str
        """
        return self._AllocateTransferPayAmount

    @AllocateTransferPayAmount.setter
    def AllocateTransferPayAmount(self, AllocateTransferPayAmount):
        self._AllocateTransferPayAmount = AllocateTransferPayAmount

    @property
    def TotalCashPayAmount(self):
        r"""Total fees (cash): Total fees of the cost allocation unit, Collected Fees (Cash) + Allocated fees (Cash)
        :rtype: str
        """
        return self._TotalCashPayAmount

    @TotalCashPayAmount.setter
    def TotalCashPayAmount(self, TotalCashPayAmount):
        self._TotalCashPayAmount = TotalCashPayAmount

    @property
    def TotalVoucherPayAmount(self):
        r"""Total fees (voucher): Total fees of the cost allocation unit, Collected Fees (Voucher) + Allocated fees (Voucher)
        :rtype: str
        """
        return self._TotalVoucherPayAmount

    @TotalVoucherPayAmount.setter
    def TotalVoucherPayAmount(self, TotalVoucherPayAmount):
        self._TotalVoucherPayAmount = TotalVoucherPayAmount

    @property
    def TotalIncentivePayAmount(self):
        r"""Total fees (free credit): Total fees of the cost allocation unit, Collected Fees (Free Credit) + Allocated fees (Free Credit)
        :rtype: str
        """
        return self._TotalIncentivePayAmount

    @TotalIncentivePayAmount.setter
    def TotalIncentivePayAmount(self, TotalIncentivePayAmount):
        self._TotalIncentivePayAmount = TotalIncentivePayAmount

    @property
    def TotalTransferPayAmount(self):
        r"""Total fees (royalty amount): Total cost of the cost allocation unit, Collected Fees (Royalty Amount) + Allocated fees (Royalty Amount)
        :rtype: str
        """
        return self._TotalTransferPayAmount

    @TotalTransferPayAmount.setter
    def TotalTransferPayAmount(self, TotalTransferPayAmount):
        self._TotalTransferPayAmount = TotalTransferPayAmount

    @property
    def GatherRealCost(self):
        r"""Collected fees (discounted total): Total resource amount after discount directly collected to the cost allocation unit based on the collection rules
        :rtype: str
        """
        return self._GatherRealCost

    @GatherRealCost.setter
    def GatherRealCost(self, GatherRealCost):
        self._GatherRealCost = GatherRealCost

    @property
    def AllocateRealCost(self):
        r"""Allocated fees (discounted total): Total resource amount after discount directly allocated to the cost allocation unit based on the allocation rules
        :rtype: str
        """
        return self._AllocateRealCost

    @AllocateRealCost.setter
    def AllocateRealCost(self, AllocateRealCost):
        self._AllocateRealCost = AllocateRealCost

    @property
    def RealTotalCost(self):
        r"""Total fees (discounted total): Total fees of the cost allocation unit, Collected Fees (discounted total) + Allocated fees (discounted total)
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Ratio(self):
        r"""Proportion (discounted total): Total fees (discounted total) of the Cost Allocation Unit/Total Fees (discounted total) * 100%
        :rtype: str
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio

    @property
    def Trend(self):
        r"""Month-on-month ratio (discounted total): [Total fees (discounted total) of the cost allocation unit in this month - Total fees (discounted total) of the cost allocation unit in the previous month]/Total fees (discounted total) of the cost allocation unit in the previous month * 100%
        :rtype: str
        """
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def TrendType(self):
        r"""Sequential Comparison Arrow
upward - Upward
downward - Downward
none - Stable
        :rtype: str
        """
        return self._TrendType

    @TrendType.setter
    def TrendType(self, TrendType):
        self._TrendType = TrendType

    @property
    def AllocateCostBeforeTax(self):
        r"""AllocateCostBeforeTax
        :rtype: str
        """
        return self._AllocateCostBeforeTax

    @AllocateCostBeforeTax.setter
    def AllocateCostBeforeTax(self, AllocateCostBeforeTax):
        self._AllocateCostBeforeTax = AllocateCostBeforeTax

    @property
    def GatherCostBeforeTax(self):
        r"""GatherCostBeforeTax
        :rtype: str
        """
        return self._GatherCostBeforeTax

    @GatherCostBeforeTax.setter
    def GatherCostBeforeTax(self, GatherCostBeforeTax):
        self._GatherCostBeforeTax = GatherCostBeforeTax

    @property
    def TotalCostBeforeTax(self):
        r"""TotalCostBeforeTax
        :rtype: str
        """
        return self._TotalCostBeforeTax

    @TotalCostBeforeTax.setter
    def TotalCostBeforeTax(self, TotalCostBeforeTax):
        self._TotalCostBeforeTax = TotalCostBeforeTax

    @property
    def AllocateTax(self):
        r"""AllocateTax
        :rtype: str
        """
        return self._AllocateTax

    @AllocateTax.setter
    def AllocateTax(self, AllocateTax):
        self._AllocateTax = AllocateTax

    @property
    def GatherTax(self):
        r"""GatherTax
        :rtype: str
        """
        return self._GatherTax

    @GatherTax.setter
    def GatherTax(self, GatherTax):
        self._GatherTax = GatherTax

    @property
    def TotalTax(self):
        r"""TotalTax
        :rtype: str
        """
        return self._TotalTax

    @TotalTax.setter
    def TotalTax(self, TotalTax):
        self._TotalTax = TotalTax


    def _deserialize(self, params):
        self._GatherCashPayAmount = params.get("GatherCashPayAmount")
        self._GatherVoucherPayAmount = params.get("GatherVoucherPayAmount")
        self._GatherIncentivePayAmount = params.get("GatherIncentivePayAmount")
        self._GatherTransferPayAmount = params.get("GatherTransferPayAmount")
        self._AllocateCashPayAmount = params.get("AllocateCashPayAmount")
        self._AllocateVoucherPayAmount = params.get("AllocateVoucherPayAmount")
        self._AllocateIncentivePayAmount = params.get("AllocateIncentivePayAmount")
        self._AllocateTransferPayAmount = params.get("AllocateTransferPayAmount")
        self._TotalCashPayAmount = params.get("TotalCashPayAmount")
        self._TotalVoucherPayAmount = params.get("TotalVoucherPayAmount")
        self._TotalIncentivePayAmount = params.get("TotalIncentivePayAmount")
        self._TotalTransferPayAmount = params.get("TotalTransferPayAmount")
        self._GatherRealCost = params.get("GatherRealCost")
        self._AllocateRealCost = params.get("AllocateRealCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._Ratio = params.get("Ratio")
        self._Trend = params.get("Trend")
        self._TrendType = params.get("TrendType")
        self._AllocateCostBeforeTax = params.get("AllocateCostBeforeTax")
        self._GatherCostBeforeTax = params.get("GatherCostBeforeTax")
        self._TotalCostBeforeTax = params.get("TotalCostBeforeTax")
        self._AllocateTax = params.get("AllocateTax")
        self._GatherTax = params.get("GatherTax")
        self._TotalTax = params.get("TotalTax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationOverviewDetail(AbstractModel):
    r"""Details of the cost allocation overview

    """

    def __init__(self):
        r"""
        :param _TreeNodeUniqKey: Unique identifier of a cost allocation unit
        :type TreeNodeUniqKey: str
        :param _TreeNodeUniqKeyName: Name of a cost allocation unit
        :type TreeNodeUniqKeyName: str
        :param _BillDate: Date: Settlement date
        :type BillDate: str
        :param _GatherCashPayAmount: Collected fees (cash): Cash directly collected to the cost allocation unit based on the collection rules
        :type GatherCashPayAmount: str
        :param _GatherVoucherPayAmount: Collected fees (voucher): Resource vouchers directly collected to the cost allocation unit based on the collection rules
        :type GatherVoucherPayAmount: str
        :param _GatherIncentivePayAmount: Collected fees (free credit): Resource free credit directly collected to the cost allocation unit based on the collection rules
        :type GatherIncentivePayAmount: str
        :param _GatherTransferPayAmount: Collected fees (royalty amount): Resource royalty amount directly collected to the cost allocation unit based on the collection rules
        :type GatherTransferPayAmount: str
        :param _AllocateCashPayAmount: Allocated fees (cash): Resource cash allocated to the cost allocation unit based on the allocation rules
        :type AllocateCashPayAmount: str
        :param _AllocateVoucherPayAmount: Allocated fees (voucher): Resource vouchers allocated to the cost allocation unit based on the allocation rules
        :type AllocateVoucherPayAmount: str
        :param _AllocateIncentivePayAmount: Allocated fees (free credit): Resource free credit allocated to the cost allocation unit based on the allocation rules
        :type AllocateIncentivePayAmount: str
        :param _AllocateTransferPayAmount: Allocated fees (royalty amount): Resource royalty amount allocated to the cost allocation unit based on the allocation rules
        :type AllocateTransferPayAmount: str
        :param _TotalCashPayAmount: Total fees (cash): Total fees of the cost allocation unit, Collected Fees (Cash) + Allocated Fees (Cash)
        :type TotalCashPayAmount: str
        :param _TotalVoucherPayAmount: Total fees (voucher): Total fees of the cost allocation unit, Collected Fees (Voucher) + Allocated Fees (Voucher)
        :type TotalVoucherPayAmount: str
        :param _TotalIncentivePayAmount: Total fees (free credit): Total fees of the cost allocation unit, Collected Fees (Free Credit) + Allocated Fees (Free Credit)
        :type TotalIncentivePayAmount: str
        :param _TotalTransferPayAmount: Total fees (royalty amount): Total fees of the cost allocation unit, Collected Fees (Royalty Amount) + Allocated Fees (Royalty Amount)
        :type TotalTransferPayAmount: str
        :param _GatherRealCost: Collected fees (discounted total): Total resource amount after discount directly collected to the cost allocation unit based on the collection rules
        :type GatherRealCost: str
        :param _AllocateRealCost: Allocated fees (discounted total): Total resource amount after discount directly allocated to the cost allocation unit based on the allocation rules
        :type AllocateRealCost: str
        :param _RealTotalCost: Total fees (discounted total): Total fees of the cost allocation unit, Collected Fees (discounted total) + Allocated Fees (discounted total)
        :type RealTotalCost: str
        :param _Ratio: Proportion (discounted total): Total fees (discounted total) of the Cost Allocation Unit/Total Fees (discounted total) * 100%
        :type Ratio: str
        :param _Trend: Month-on-month ratio (discounted total): [Total fees (discounted total) of the cost allocation unit in this month - Total fees (discounted total) of the cost allocation unit in the previous month]/Total fees (discounted total) of the cost allocation unit in the previous month * 100%
        :type Trend: str
        :param _TrendType: Sequential Comparison Arrow
upward - Upward
downward - Downward
none - Stable
        :type TrendType: str
        :param _GatherCostBeforeTax: GatherCostBeforeTax
        :type GatherCostBeforeTax: str
        :param _AllocateCostBeforeTax: AllocateCostBeforeTax
        :type AllocateCostBeforeTax: str
        :param _TotalCostBeforeTax: TotalCostBeforeTax
        :type TotalCostBeforeTax: str
        :param _GatherTax: GatherTax
        :type GatherTax: str
        :param _AllocateTax: AllocateTax
        :type AllocateTax: str
        :param _TotalTax: TotalTax
        :type TotalTax: str
        """
        self._TreeNodeUniqKey = None
        self._TreeNodeUniqKeyName = None
        self._BillDate = None
        self._GatherCashPayAmount = None
        self._GatherVoucherPayAmount = None
        self._GatherIncentivePayAmount = None
        self._GatherTransferPayAmount = None
        self._AllocateCashPayAmount = None
        self._AllocateVoucherPayAmount = None
        self._AllocateIncentivePayAmount = None
        self._AllocateTransferPayAmount = None
        self._TotalCashPayAmount = None
        self._TotalVoucherPayAmount = None
        self._TotalIncentivePayAmount = None
        self._TotalTransferPayAmount = None
        self._GatherRealCost = None
        self._AllocateRealCost = None
        self._RealTotalCost = None
        self._Ratio = None
        self._Trend = None
        self._TrendType = None
        self._GatherCostBeforeTax = None
        self._AllocateCostBeforeTax = None
        self._TotalCostBeforeTax = None
        self._GatherTax = None
        self._AllocateTax = None
        self._TotalTax = None

    @property
    def TreeNodeUniqKey(self):
        r"""Unique identifier of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def TreeNodeUniqKeyName(self):
        r"""Name of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKeyName

    @TreeNodeUniqKeyName.setter
    def TreeNodeUniqKeyName(self, TreeNodeUniqKeyName):
        self._TreeNodeUniqKeyName = TreeNodeUniqKeyName

    @property
    def BillDate(self):
        r"""Date: Settlement date
        :rtype: str
        """
        return self._BillDate

    @BillDate.setter
    def BillDate(self, BillDate):
        self._BillDate = BillDate

    @property
    def GatherCashPayAmount(self):
        r"""Collected fees (cash): Cash directly collected to the cost allocation unit based on the collection rules
        :rtype: str
        """
        return self._GatherCashPayAmount

    @GatherCashPayAmount.setter
    def GatherCashPayAmount(self, GatherCashPayAmount):
        self._GatherCashPayAmount = GatherCashPayAmount

    @property
    def GatherVoucherPayAmount(self):
        r"""Collected fees (voucher): Resource vouchers directly collected to the cost allocation unit based on the collection rules
        :rtype: str
        """
        return self._GatherVoucherPayAmount

    @GatherVoucherPayAmount.setter
    def GatherVoucherPayAmount(self, GatherVoucherPayAmount):
        self._GatherVoucherPayAmount = GatherVoucherPayAmount

    @property
    def GatherIncentivePayAmount(self):
        r"""Collected fees (free credit): Resource free credit directly collected to the cost allocation unit based on the collection rules
        :rtype: str
        """
        return self._GatherIncentivePayAmount

    @GatherIncentivePayAmount.setter
    def GatherIncentivePayAmount(self, GatherIncentivePayAmount):
        self._GatherIncentivePayAmount = GatherIncentivePayAmount

    @property
    def GatherTransferPayAmount(self):
        r"""Collected fees (royalty amount): Resource royalty amount directly collected to the cost allocation unit based on the collection rules
        :rtype: str
        """
        return self._GatherTransferPayAmount

    @GatherTransferPayAmount.setter
    def GatherTransferPayAmount(self, GatherTransferPayAmount):
        self._GatherTransferPayAmount = GatherTransferPayAmount

    @property
    def AllocateCashPayAmount(self):
        r"""Allocated fees (cash): Resource cash allocated to the cost allocation unit based on the allocation rules
        :rtype: str
        """
        return self._AllocateCashPayAmount

    @AllocateCashPayAmount.setter
    def AllocateCashPayAmount(self, AllocateCashPayAmount):
        self._AllocateCashPayAmount = AllocateCashPayAmount

    @property
    def AllocateVoucherPayAmount(self):
        r"""Allocated fees (voucher): Resource vouchers allocated to the cost allocation unit based on the allocation rules
        :rtype: str
        """
        return self._AllocateVoucherPayAmount

    @AllocateVoucherPayAmount.setter
    def AllocateVoucherPayAmount(self, AllocateVoucherPayAmount):
        self._AllocateVoucherPayAmount = AllocateVoucherPayAmount

    @property
    def AllocateIncentivePayAmount(self):
        r"""Allocated fees (free credit): Resource free credit allocated to the cost allocation unit based on the allocation rules
        :rtype: str
        """
        return self._AllocateIncentivePayAmount

    @AllocateIncentivePayAmount.setter
    def AllocateIncentivePayAmount(self, AllocateIncentivePayAmount):
        self._AllocateIncentivePayAmount = AllocateIncentivePayAmount

    @property
    def AllocateTransferPayAmount(self):
        r"""Allocated fees (royalty amount): Resource royalty amount allocated to the cost allocation unit based on the allocation rules
        :rtype: str
        """
        return self._AllocateTransferPayAmount

    @AllocateTransferPayAmount.setter
    def AllocateTransferPayAmount(self, AllocateTransferPayAmount):
        self._AllocateTransferPayAmount = AllocateTransferPayAmount

    @property
    def TotalCashPayAmount(self):
        r"""Total fees (cash): Total fees of the cost allocation unit, Collected Fees (Cash) + Allocated Fees (Cash)
        :rtype: str
        """
        return self._TotalCashPayAmount

    @TotalCashPayAmount.setter
    def TotalCashPayAmount(self, TotalCashPayAmount):
        self._TotalCashPayAmount = TotalCashPayAmount

    @property
    def TotalVoucherPayAmount(self):
        r"""Total fees (voucher): Total fees of the cost allocation unit, Collected Fees (Voucher) + Allocated Fees (Voucher)
        :rtype: str
        """
        return self._TotalVoucherPayAmount

    @TotalVoucherPayAmount.setter
    def TotalVoucherPayAmount(self, TotalVoucherPayAmount):
        self._TotalVoucherPayAmount = TotalVoucherPayAmount

    @property
    def TotalIncentivePayAmount(self):
        r"""Total fees (free credit): Total fees of the cost allocation unit, Collected Fees (Free Credit) + Allocated Fees (Free Credit)
        :rtype: str
        """
        return self._TotalIncentivePayAmount

    @TotalIncentivePayAmount.setter
    def TotalIncentivePayAmount(self, TotalIncentivePayAmount):
        self._TotalIncentivePayAmount = TotalIncentivePayAmount

    @property
    def TotalTransferPayAmount(self):
        r"""Total fees (royalty amount): Total fees of the cost allocation unit, Collected Fees (Royalty Amount) + Allocated Fees (Royalty Amount)
        :rtype: str
        """
        return self._TotalTransferPayAmount

    @TotalTransferPayAmount.setter
    def TotalTransferPayAmount(self, TotalTransferPayAmount):
        self._TotalTransferPayAmount = TotalTransferPayAmount

    @property
    def GatherRealCost(self):
        r"""Collected fees (discounted total): Total resource amount after discount directly collected to the cost allocation unit based on the collection rules
        :rtype: str
        """
        return self._GatherRealCost

    @GatherRealCost.setter
    def GatherRealCost(self, GatherRealCost):
        self._GatherRealCost = GatherRealCost

    @property
    def AllocateRealCost(self):
        r"""Allocated fees (discounted total): Total resource amount after discount directly allocated to the cost allocation unit based on the allocation rules
        :rtype: str
        """
        return self._AllocateRealCost

    @AllocateRealCost.setter
    def AllocateRealCost(self, AllocateRealCost):
        self._AllocateRealCost = AllocateRealCost

    @property
    def RealTotalCost(self):
        r"""Total fees (discounted total): Total fees of the cost allocation unit, Collected Fees (discounted total) + Allocated Fees (discounted total)
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Ratio(self):
        r"""Proportion (discounted total): Total fees (discounted total) of the Cost Allocation Unit/Total Fees (discounted total) * 100%
        :rtype: str
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio

    @property
    def Trend(self):
        r"""Month-on-month ratio (discounted total): [Total fees (discounted total) of the cost allocation unit in this month - Total fees (discounted total) of the cost allocation unit in the previous month]/Total fees (discounted total) of the cost allocation unit in the previous month * 100%
        :rtype: str
        """
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def TrendType(self):
        r"""Sequential Comparison Arrow
upward - Upward
downward - Downward
none - Stable
        :rtype: str
        """
        return self._TrendType

    @TrendType.setter
    def TrendType(self, TrendType):
        self._TrendType = TrendType

    @property
    def GatherCostBeforeTax(self):
        r"""GatherCostBeforeTax
        :rtype: str
        """
        return self._GatherCostBeforeTax

    @GatherCostBeforeTax.setter
    def GatherCostBeforeTax(self, GatherCostBeforeTax):
        self._GatherCostBeforeTax = GatherCostBeforeTax

    @property
    def AllocateCostBeforeTax(self):
        r"""AllocateCostBeforeTax
        :rtype: str
        """
        return self._AllocateCostBeforeTax

    @AllocateCostBeforeTax.setter
    def AllocateCostBeforeTax(self, AllocateCostBeforeTax):
        self._AllocateCostBeforeTax = AllocateCostBeforeTax

    @property
    def TotalCostBeforeTax(self):
        r"""TotalCostBeforeTax
        :rtype: str
        """
        return self._TotalCostBeforeTax

    @TotalCostBeforeTax.setter
    def TotalCostBeforeTax(self, TotalCostBeforeTax):
        self._TotalCostBeforeTax = TotalCostBeforeTax

    @property
    def GatherTax(self):
        r"""GatherTax
        :rtype: str
        """
        return self._GatherTax

    @GatherTax.setter
    def GatherTax(self, GatherTax):
        self._GatherTax = GatherTax

    @property
    def AllocateTax(self):
        r"""AllocateTax
        :rtype: str
        """
        return self._AllocateTax

    @AllocateTax.setter
    def AllocateTax(self, AllocateTax):
        self._AllocateTax = AllocateTax

    @property
    def TotalTax(self):
        r"""TotalTax
        :rtype: str
        """
        return self._TotalTax

    @TotalTax.setter
    def TotalTax(self, TotalTax):
        self._TotalTax = TotalTax


    def _deserialize(self, params):
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._TreeNodeUniqKeyName = params.get("TreeNodeUniqKeyName")
        self._BillDate = params.get("BillDate")
        self._GatherCashPayAmount = params.get("GatherCashPayAmount")
        self._GatherVoucherPayAmount = params.get("GatherVoucherPayAmount")
        self._GatherIncentivePayAmount = params.get("GatherIncentivePayAmount")
        self._GatherTransferPayAmount = params.get("GatherTransferPayAmount")
        self._AllocateCashPayAmount = params.get("AllocateCashPayAmount")
        self._AllocateVoucherPayAmount = params.get("AllocateVoucherPayAmount")
        self._AllocateIncentivePayAmount = params.get("AllocateIncentivePayAmount")
        self._AllocateTransferPayAmount = params.get("AllocateTransferPayAmount")
        self._TotalCashPayAmount = params.get("TotalCashPayAmount")
        self._TotalVoucherPayAmount = params.get("TotalVoucherPayAmount")
        self._TotalIncentivePayAmount = params.get("TotalIncentivePayAmount")
        self._TotalTransferPayAmount = params.get("TotalTransferPayAmount")
        self._GatherRealCost = params.get("GatherRealCost")
        self._AllocateRealCost = params.get("AllocateRealCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._Ratio = params.get("Ratio")
        self._Trend = params.get("Trend")
        self._TrendType = params.get("TrendType")
        self._GatherCostBeforeTax = params.get("GatherCostBeforeTax")
        self._AllocateCostBeforeTax = params.get("AllocateCostBeforeTax")
        self._TotalCostBeforeTax = params.get("TotalCostBeforeTax")
        self._GatherTax = params.get("GatherTax")
        self._AllocateTax = params.get("AllocateTax")
        self._TotalTax = params.get("TotalTax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationOverviewNode(AbstractModel):
    r"""Monthly overview of a cost allocation bill

    """

    def __init__(self):
        r"""
        :param _Id: Cost allocation unit ID
        :type Id: int
        :param _Name: Name of a cost allocation unit
        :type Name: str
        :param _TreeNodeUniqKey: Unique identifier of a cost allocation unit
        :type TreeNodeUniqKey: str
        :param _Symbol: Billing unit including a rule flag
0 - No rule exists.
1 - Both collection rules and allocation rules exist.
2 - Only collection rules exist.
3 - Only allocation rules exist.
        :type Symbol: int
        :param _Children: Detailed monthly overview of a sub-unit
        :type Children: list of AllocationOverviewNode
        :param _Detail: Monthly overview amount details of a cost allocation bill
        :type Detail: :class:`tencentcloud.billing.v20180709.models.AllocationMonthOverviewDetail`
        """
        self._Id = None
        self._Name = None
        self._TreeNodeUniqKey = None
        self._Symbol = None
        self._Children = None
        self._Detail = None

    @property
    def Id(self):
        r"""Cost allocation unit ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""Name of a cost allocation unit
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TreeNodeUniqKey(self):
        r"""Unique identifier of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def Symbol(self):
        r"""Billing unit including a rule flag
0 - No rule exists.
1 - Both collection rules and allocation rules exist.
2 - Only collection rules exist.
3 - Only allocation rules exist.
        :rtype: int
        """
        return self._Symbol

    @Symbol.setter
    def Symbol(self, Symbol):
        self._Symbol = Symbol

    @property
    def Children(self):
        r"""Detailed monthly overview of a sub-unit
        :rtype: list of AllocationOverviewNode
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children

    @property
    def Detail(self):
        r"""Monthly overview amount details of a cost allocation bill
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationMonthOverviewDetail`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._Symbol = params.get("Symbol")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = AllocationOverviewNode()
                obj._deserialize(item)
                self._Children.append(obj)
        if params.get("Detail") is not None:
            self._Detail = AllocationMonthOverviewDetail()
            self._Detail._deserialize(params.get("Detail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationOverviewTotal(AbstractModel):
    r"""Total amount of a cost allocation bill

    """

    def __init__(self):
        r"""
        :param _RealTotalCost: Total fees: Total Fees (Cash) + Total Fees (Royalty Amount) + Total Fees (Free Credit) + Total Fees (Voucher)
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealTotalCost: str
        :param _CashPayAmount: Cash: Total fees of cash
Note: This field may return null, indicating that no valid values can be obtained.
        :type CashPayAmount: str
        :param _IncentivePayAmount: Free credit: Total fees of free credit
Note: This field may return null, indicating that no valid values can be obtained.
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: Voucher: Total fees of voucher
Note: This field may return null, indicating that no valid values can be obtained.
        :type VoucherPayAmount: str
        :param _TransferPayAmount: Royalty amount: Total fees of royalty amount
Note: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        :param _CostBeforeTax: Pre-tax price after discount
        :type CostBeforeTax: str
        :param _Tax: Tax
        :type Tax: str
        """
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None
        self._CostBeforeTax = None
        self._Tax = None

    @property
    def RealTotalCost(self):
        r"""Total fees: Total Fees (Cash) + Total Fees (Royalty Amount) + Total Fees (Free Credit) + Total Fees (Voucher)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        r"""Cash: Total fees of cash
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Free credit: Total fees of free credit
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        r"""Voucher: Total fees of voucher
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        r"""Royalty amount: Total fees of royalty amount
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def CostBeforeTax(self):
        r"""Pre-tax price after discount
        :rtype: str
        """
        return self._CostBeforeTax

    @CostBeforeTax.setter
    def CostBeforeTax(self, CostBeforeTax):
        self._CostBeforeTax = CostBeforeTax

    @property
    def Tax(self):
        r"""Tax
        :rtype: str
        """
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax


    def _deserialize(self, params):
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._CostBeforeTax = params.get("CostBeforeTax")
        self._Tax = params.get("Tax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationRationExpression(AbstractModel):
    r"""Expression for sharing proportion.

    """

    def __init__(self):
        r"""
        :param _NodeId: Cost allocation unit ID that the sharing rule belongs to.
        :type NodeId: int
        :param _Ratio: Sharing proportion occupied by allocation unit, pass 0 for allocation by proportion.
        :type Ratio: float
        """
        self._NodeId = None
        self._Ratio = None

    @property
    def NodeId(self):
        r"""Cost allocation unit ID that the sharing rule belongs to.
        :rtype: int
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Ratio(self):
        r"""Sharing proportion occupied by allocation unit, pass 0 for allocation by proportion.
        :rtype: float
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Ratio = params.get("Ratio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationRule(AbstractModel):
    r"""Information on allocation rules hit by the current resource

    """

    def __init__(self):
        r"""
        :param _RuleId: Allocation rule ID
        :type RuleId: int
        :param _RuleName: Allocation rule name
        :type RuleName: str
        """
        self._RuleId = None
        self._RuleName = None

    @property
    def RuleId(self):
        r"""Allocation rule ID
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        r"""Allocation rule name
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationRuleExpression(AbstractModel):
    r"""Cost allocation regular expression.

    """

    def __init__(self):
        r"""
        :param _RuleKey: RuleKey: cost allocation dimension.
Enumeration value.
ownerUin - user UIN.
Operator UIN.
businessCode - product-level code.
productCode - 2-tier product code.
itemCode - 4-tier product code.
projectId - specifies the project ID.
regionId.
resourceId - specifies the resource ID.
tag - tag key-value pair.
payMode - billing mode.
instanceType - instance type.
actionType - transaction type.
        :type RuleKey: str
        :param _Operator: Specifies the dimension rules for cost allocation.
Enumeration value.
in.
not in.
        :type Operator: str
        :param _RuleValue: Cost allocation dimension value. for example, when RuleKey is businessCode, ["p_cbs","p_sqlserver"] indicates the cost of products at the "p_cbs","p_sqlserver" level.
        :type RuleValue: list of str
        :param _Connectors: Logical connection for cost allocation, enumeration values are as follows:.
Create and bind a policy query an instance reset the access password of an instance.
Create and bind a policy query an instance reset the access password of an instance.
        :type Connectors: str
        :param _Children: Nested rule.
        :type Children: list of AllocationRuleExpression
        """
        self._RuleKey = None
        self._Operator = None
        self._RuleValue = None
        self._Connectors = None
        self._Children = None

    @property
    def RuleKey(self):
        r"""RuleKey: cost allocation dimension.
Enumeration value.
ownerUin - user UIN.
Operator UIN.
businessCode - product-level code.
productCode - 2-tier product code.
itemCode - 4-tier product code.
projectId - specifies the project ID.
regionId.
resourceId - specifies the resource ID.
tag - tag key-value pair.
payMode - billing mode.
instanceType - instance type.
actionType - transaction type.
        :rtype: str
        """
        return self._RuleKey

    @RuleKey.setter
    def RuleKey(self, RuleKey):
        self._RuleKey = RuleKey

    @property
    def Operator(self):
        r"""Specifies the dimension rules for cost allocation.
Enumeration value.
in.
not in.
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def RuleValue(self):
        r"""Cost allocation dimension value. for example, when RuleKey is businessCode, ["p_cbs","p_sqlserver"] indicates the cost of products at the "p_cbs","p_sqlserver" level.
        :rtype: list of str
        """
        return self._RuleValue

    @RuleValue.setter
    def RuleValue(self, RuleValue):
        self._RuleValue = RuleValue

    @property
    def Connectors(self):
        r"""Logical connection for cost allocation, enumeration values are as follows:.
Create and bind a policy query an instance reset the access password of an instance.
Create and bind a policy query an instance reset the access password of an instance.
        :rtype: str
        """
        return self._Connectors

    @Connectors.setter
    def Connectors(self, Connectors):
        self._Connectors = Connectors

    @property
    def Children(self):
        r"""Nested rule.
        :rtype: list of AllocationRuleExpression
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children


    def _deserialize(self, params):
        self._RuleKey = params.get("RuleKey")
        self._Operator = params.get("Operator")
        self._RuleValue = params.get("RuleValue")
        self._Connectors = params.get("Connectors")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = AllocationRuleExpression()
                obj._deserialize(item)
                self._Children.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationRuleOverview(AbstractModel):
    r"""Overview of sharing rules.

    """

    def __init__(self):
        r"""
        :param _RuleId: Sharing rule ID.
        :type RuleId: int
        :param _RuleName: Sharing rule name.
        :type RuleName: str
        :param _Type: Public area policy type.
Enumeration value.
1 - custom sharing proportion. 
2 - proportional allocation. 
3 - allocation by proportion.
        :type Type: int
        :param _UpdateTime: Last update time of the sharing rules.
        :type UpdateTime: str
        :param _AllocationNode: Overview of cost allocation units.
        :type AllocationNode: list of AllocationUnit
        """
        self._RuleId = None
        self._RuleName = None
        self._Type = None
        self._UpdateTime = None
        self._AllocationNode = None

    @property
    def RuleId(self):
        r"""Sharing rule ID.
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        r"""Sharing rule name.
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Type(self):
        r"""Public area policy type.
Enumeration value.
1 - custom sharing proportion. 
2 - proportional allocation. 
3 - allocation by proportion.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UpdateTime(self):
        r"""Last update time of the sharing rules.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AllocationNode(self):
        r"""Overview of cost allocation units.
        :rtype: list of AllocationUnit
        """
        return self._AllocationNode

    @AllocationNode.setter
    def AllocationNode(self, AllocationNode):
        self._AllocationNode = AllocationNode


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._Type = params.get("Type")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("AllocationNode") is not None:
            self._AllocationNode = []
            for item in params.get("AllocationNode"):
                obj = AllocationUnit()
                obj._deserialize(item)
                self._AllocationNode.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationRulesSummary(AbstractModel):
    r"""List of sharing rules.

    """

    def __init__(self):
        r"""
        :param _Name: Add new sharing rule name.
        :type Name: str
        :param _Type: Specifies the sharing rule policy type. the enumeration values are as follows:.
1 - custom sharing proportion. 
2 - proportional allocation.
3 - allocation by proportion.
        :type Type: int
        :param _RuleDetail: Sharing rule expression.
        :type RuleDetail: :class:`tencentcloud.billing.v20180709.models.AllocationRuleExpression`
        :param _RatioDetail: Sharing proportion expression, allocation by proportion not passed.
        :type RatioDetail: list of AllocationRationExpression
        """
        self._Name = None
        self._Type = None
        self._RuleDetail = None
        self._RatioDetail = None

    @property
    def Name(self):
        r"""Add new sharing rule name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""Specifies the sharing rule policy type. the enumeration values are as follows:.
1 - custom sharing proportion. 
2 - proportional allocation.
3 - allocation by proportion.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RuleDetail(self):
        r"""Sharing rule expression.
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationRuleExpression`
        """
        return self._RuleDetail

    @RuleDetail.setter
    def RuleDetail(self, RuleDetail):
        self._RuleDetail = RuleDetail

    @property
    def RatioDetail(self):
        r"""Sharing proportion expression, allocation by proportion not passed.
        :rtype: list of AllocationRationExpression
        """
        return self._RatioDetail

    @RatioDetail.setter
    def RatioDetail(self, RatioDetail):
        self._RatioDetail = RatioDetail


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("RuleDetail") is not None:
            self._RuleDetail = AllocationRuleExpression()
            self._RuleDetail._deserialize(params.get("RuleDetail"))
        if params.get("RatioDetail") is not None:
            self._RatioDetail = []
            for item in params.get("RatioDetail"):
                obj = AllocationRationExpression()
                obj._deserialize(item)
                self._RatioDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationStat(AbstractModel):
    r"""Trend graph of a cost allocation bill

    """

    def __init__(self):
        r"""
        :param _Average: Average cost information
        :type Average: :class:`tencentcloud.billing.v20180709.models.AllocationAverageData`
        """
        self._Average = None

    @property
    def Average(self):
        r"""Average cost information
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationAverageData`
        """
        return self._Average

    @Average.setter
    def Average(self, Average):
        self._Average = Average


    def _deserialize(self, params):
        if params.get("Average") is not None:
            self._Average = AllocationAverageData()
            self._Average._deserialize(params.get("Average"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationSummaryByBusiness(AbstractModel):
    r"""Detailed summary of the cost allocation bill by business

    """

    def __init__(self):
        r"""
        :param _TreeNodeUniqKey: Unique identifier of a cost allocation unit
        :type TreeNodeUniqKey: str
        :param _TreeNodeUniqKeyName: Name of a cost allocation unit
        :type TreeNodeUniqKeyName: str
        :param _BillDate: Date: Settlement date
        :type BillDate: str
        :param _GatherCashPayAmount: Collected fees (cash): Cash directly collected to the cost allocation unit based on the collection rules
        :type GatherCashPayAmount: str
        :param _GatherVoucherPayAmount: Collected fees (voucher): Resource vouchers directly collected to the cost allocation unit based on the collection rules
        :type GatherVoucherPayAmount: str
        :param _GatherIncentivePayAmount: Collected fees (free credit): Resource free credit directly collected to the cost allocation unit based on the collection rules
        :type GatherIncentivePayAmount: str
        :param _GatherTransferPayAmount: Collected fees (royalty amount): Resource royalty amount directly collected to the cost allocation unit based on the collection rules
        :type GatherTransferPayAmount: str
        :param _AllocateCashPayAmount: Allocated fees (cash): Resource cash allocated to the cost allocation unit based on the allocation rules
        :type AllocateCashPayAmount: str
        :param _AllocateVoucherPayAmount: Allocated fees (voucher): Resource vouchers allocated to the cost allocation unit based on the allocation rules
        :type AllocateVoucherPayAmount: str
        :param _AllocateIncentivePayAmount: Allocated fees (free credit): Resource free credit allocated to the cost allocation unit based on the allocation rules
        :type AllocateIncentivePayAmount: str
        :param _AllocateTransferPayAmount: Allocated fees (royalty amount): Resource royalty amount allocated to the cost allocation unit based on the allocation rules
        :type AllocateTransferPayAmount: str
        :param _TotalCashPayAmount: Total fees (cash): Total fees of the cost allocation unit, Collected Fees (Cash) + Allocated fees (Cash)
        :type TotalCashPayAmount: str
        :param _TotalVoucherPayAmount: Total fees (voucher): Total fees of the cost allocation unit, Collected Fees (Vouchers) + Allocated fees (Vouchers)
        :type TotalVoucherPayAmount: str
        :param _TotalIncentivePayAmount: Total fees (free credit): Total fees of the cost allocation unit, Collected Fees (Free Credit) + Allocated fees (Free Credit)
        :type TotalIncentivePayAmount: str
        :param _TotalTransferPayAmount: Total fees (royalty amount): Total fees of the cost allocation unit, Collected Fees (Royalty Amount) + Allocated fees (Royalty Amount)
        :type TotalTransferPayAmount: str
        :param _GatherRealCost: Collected fees (discounted total): Total resource amount after discount directly collected to the cost allocation unit based on the collection rules
        :type GatherRealCost: str
        :param _AllocateRealCost: Allocated fees (discounted total): Total resource amount after discount allocated to the cost allocation unit based on the allocation rules
        :type AllocateRealCost: str
        :param _RealTotalCost: Total fees (discounted total): Total fees of the cost allocation unit, Collected Fees (discounted total) + Allocated fees (discounted total)
        :type RealTotalCost: str
        :param _Ratio: Proportion (discounted total): Total fees (discounted total) of the Cost Allocation Unit/Total Fees (discounted total) * 100%
        :type Ratio: str
        :param _Trend: Month-on-month ratio (discounted total): [Total fees (discounted total) of the cost allocation unit in this month - Total fees (discounted total) of the cost allocation unit in the previous month]/Total fees (discounted total) of the cost allocation unit in the previous month * 100%
        :type Trend: str
        :param _TrendType: Sequential Comparison Arrow
upward - Upward
downward - Downward
none - Stable
        :type TrendType: str
        :param _BusinessCode: Product code
        :type BusinessCode: str
        :param _BusinessCodeName: Product name: Various cloud products purchased by users
        :type BusinessCodeName: str
        :param _TotalCost: Original price of a component: Original Price = Component List Price * Component Usage * Duration of Use (not displayed if the customer enjoys a fixed price/contract price, and not displayed by default in refund scenarios), specified price mode
        :type TotalCost: str
        :param _RICost: Original price deducted by a reserved instance: The original price of a component deducted by reserved instances for this product or service
        :type RICost: str
        :param _SPCost: Savings plan deduction from original price: Savings Plan Deduction from Original Price = Monetary Value of Savings Plan Deduction/ Savings Plan Deduction Rate
        :type SPCost: str
        :param _CashPayAmount: Cash account expenditure (CNY): The amount paid through the cash account
        :type CashPayAmount: str
        :param _VoucherPayAmount: Promo voucher expenditure (CNY): The amount paid using various vouchers (such as promo vouchers and cash vouchers)

        :type VoucherPayAmount: str
        :param _IncentivePayAmount: Gift account expenditure (CNY): The amount paid using free credits
        :type IncentivePayAmount: str
        :param _TransferPayAmount: Royalty account expenditure (CNY): The amount paid through the royalty account
        :type TransferPayAmount: str
        :param _AllocationRealTotalCost: Discounted total: discounted total = (Original Price - Original Price Deducted by a Reserved Instance - Savings Plan Deduction from Original Price) * Discount Rate
        :type AllocationRealTotalCost: str
        :param _GatherTax: Collected fees (tax): Tax directly collected to the cost allocation unit based on the collection rules
        :type GatherTax: str
        :param _AllocateTax: Allocated fees (tax): Resource tax allocated to the cost allocation unit based on the allocation rules
        :type AllocateTax: str
        :param _TotalTax: Total fees (tax): Total fees of the cost allocation unit, Collected Fees (Tax) + Allocated fees (Tax)
        :type TotalTax: str
        :param _GatherCostBeforeTax: GatherCostBeforeTax
        :type GatherCostBeforeTax: str
        :param _AllocateCostBeforeTax: AllocateCostBeforeTax
        :type AllocateCostBeforeTax: str
        :param _TotalCostBeforeTax: TotalCostBeforeTax
        :type TotalCostBeforeTax: str
        :param _Tax: Tax
        :type Tax: str
        :param _CostBeforeTax: CostBeforeTax
        :type CostBeforeTax: str
        """
        self._TreeNodeUniqKey = None
        self._TreeNodeUniqKeyName = None
        self._BillDate = None
        self._GatherCashPayAmount = None
        self._GatherVoucherPayAmount = None
        self._GatherIncentivePayAmount = None
        self._GatherTransferPayAmount = None
        self._AllocateCashPayAmount = None
        self._AllocateVoucherPayAmount = None
        self._AllocateIncentivePayAmount = None
        self._AllocateTransferPayAmount = None
        self._TotalCashPayAmount = None
        self._TotalVoucherPayAmount = None
        self._TotalIncentivePayAmount = None
        self._TotalTransferPayAmount = None
        self._GatherRealCost = None
        self._AllocateRealCost = None
        self._RealTotalCost = None
        self._Ratio = None
        self._Trend = None
        self._TrendType = None
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._TotalCost = None
        self._RICost = None
        self._SPCost = None
        self._CashPayAmount = None
        self._VoucherPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None
        self._AllocationRealTotalCost = None
        self._GatherTax = None
        self._AllocateTax = None
        self._TotalTax = None
        self._GatherCostBeforeTax = None
        self._AllocateCostBeforeTax = None
        self._TotalCostBeforeTax = None
        self._Tax = None
        self._CostBeforeTax = None

    @property
    def TreeNodeUniqKey(self):
        r"""Unique identifier of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def TreeNodeUniqKeyName(self):
        r"""Name of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKeyName

    @TreeNodeUniqKeyName.setter
    def TreeNodeUniqKeyName(self, TreeNodeUniqKeyName):
        self._TreeNodeUniqKeyName = TreeNodeUniqKeyName

    @property
    def BillDate(self):
        r"""Date: Settlement date
        :rtype: str
        """
        return self._BillDate

    @BillDate.setter
    def BillDate(self, BillDate):
        self._BillDate = BillDate

    @property
    def GatherCashPayAmount(self):
        r"""Collected fees (cash): Cash directly collected to the cost allocation unit based on the collection rules
        :rtype: str
        """
        return self._GatherCashPayAmount

    @GatherCashPayAmount.setter
    def GatherCashPayAmount(self, GatherCashPayAmount):
        self._GatherCashPayAmount = GatherCashPayAmount

    @property
    def GatherVoucherPayAmount(self):
        r"""Collected fees (voucher): Resource vouchers directly collected to the cost allocation unit based on the collection rules
        :rtype: str
        """
        return self._GatherVoucherPayAmount

    @GatherVoucherPayAmount.setter
    def GatherVoucherPayAmount(self, GatherVoucherPayAmount):
        self._GatherVoucherPayAmount = GatherVoucherPayAmount

    @property
    def GatherIncentivePayAmount(self):
        r"""Collected fees (free credit): Resource free credit directly collected to the cost allocation unit based on the collection rules
        :rtype: str
        """
        return self._GatherIncentivePayAmount

    @GatherIncentivePayAmount.setter
    def GatherIncentivePayAmount(self, GatherIncentivePayAmount):
        self._GatherIncentivePayAmount = GatherIncentivePayAmount

    @property
    def GatherTransferPayAmount(self):
        r"""Collected fees (royalty amount): Resource royalty amount directly collected to the cost allocation unit based on the collection rules
        :rtype: str
        """
        return self._GatherTransferPayAmount

    @GatherTransferPayAmount.setter
    def GatherTransferPayAmount(self, GatherTransferPayAmount):
        self._GatherTransferPayAmount = GatherTransferPayAmount

    @property
    def AllocateCashPayAmount(self):
        r"""Allocated fees (cash): Resource cash allocated to the cost allocation unit based on the allocation rules
        :rtype: str
        """
        return self._AllocateCashPayAmount

    @AllocateCashPayAmount.setter
    def AllocateCashPayAmount(self, AllocateCashPayAmount):
        self._AllocateCashPayAmount = AllocateCashPayAmount

    @property
    def AllocateVoucherPayAmount(self):
        r"""Allocated fees (voucher): Resource vouchers allocated to the cost allocation unit based on the allocation rules
        :rtype: str
        """
        return self._AllocateVoucherPayAmount

    @AllocateVoucherPayAmount.setter
    def AllocateVoucherPayAmount(self, AllocateVoucherPayAmount):
        self._AllocateVoucherPayAmount = AllocateVoucherPayAmount

    @property
    def AllocateIncentivePayAmount(self):
        r"""Allocated fees (free credit): Resource free credit allocated to the cost allocation unit based on the allocation rules
        :rtype: str
        """
        return self._AllocateIncentivePayAmount

    @AllocateIncentivePayAmount.setter
    def AllocateIncentivePayAmount(self, AllocateIncentivePayAmount):
        self._AllocateIncentivePayAmount = AllocateIncentivePayAmount

    @property
    def AllocateTransferPayAmount(self):
        r"""Allocated fees (royalty amount): Resource royalty amount allocated to the cost allocation unit based on the allocation rules
        :rtype: str
        """
        return self._AllocateTransferPayAmount

    @AllocateTransferPayAmount.setter
    def AllocateTransferPayAmount(self, AllocateTransferPayAmount):
        self._AllocateTransferPayAmount = AllocateTransferPayAmount

    @property
    def TotalCashPayAmount(self):
        r"""Total fees (cash): Total fees of the cost allocation unit, Collected Fees (Cash) + Allocated fees (Cash)
        :rtype: str
        """
        return self._TotalCashPayAmount

    @TotalCashPayAmount.setter
    def TotalCashPayAmount(self, TotalCashPayAmount):
        self._TotalCashPayAmount = TotalCashPayAmount

    @property
    def TotalVoucherPayAmount(self):
        r"""Total fees (voucher): Total fees of the cost allocation unit, Collected Fees (Vouchers) + Allocated fees (Vouchers)
        :rtype: str
        """
        return self._TotalVoucherPayAmount

    @TotalVoucherPayAmount.setter
    def TotalVoucherPayAmount(self, TotalVoucherPayAmount):
        self._TotalVoucherPayAmount = TotalVoucherPayAmount

    @property
    def TotalIncentivePayAmount(self):
        r"""Total fees (free credit): Total fees of the cost allocation unit, Collected Fees (Free Credit) + Allocated fees (Free Credit)
        :rtype: str
        """
        return self._TotalIncentivePayAmount

    @TotalIncentivePayAmount.setter
    def TotalIncentivePayAmount(self, TotalIncentivePayAmount):
        self._TotalIncentivePayAmount = TotalIncentivePayAmount

    @property
    def TotalTransferPayAmount(self):
        r"""Total fees (royalty amount): Total fees of the cost allocation unit, Collected Fees (Royalty Amount) + Allocated fees (Royalty Amount)
        :rtype: str
        """
        return self._TotalTransferPayAmount

    @TotalTransferPayAmount.setter
    def TotalTransferPayAmount(self, TotalTransferPayAmount):
        self._TotalTransferPayAmount = TotalTransferPayAmount

    @property
    def GatherRealCost(self):
        r"""Collected fees (discounted total): Total resource amount after discount directly collected to the cost allocation unit based on the collection rules
        :rtype: str
        """
        return self._GatherRealCost

    @GatherRealCost.setter
    def GatherRealCost(self, GatherRealCost):
        self._GatherRealCost = GatherRealCost

    @property
    def AllocateRealCost(self):
        r"""Allocated fees (discounted total): Total resource amount after discount allocated to the cost allocation unit based on the allocation rules
        :rtype: str
        """
        return self._AllocateRealCost

    @AllocateRealCost.setter
    def AllocateRealCost(self, AllocateRealCost):
        self._AllocateRealCost = AllocateRealCost

    @property
    def RealTotalCost(self):
        r"""Total fees (discounted total): Total fees of the cost allocation unit, Collected Fees (discounted total) + Allocated fees (discounted total)
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Ratio(self):
        r"""Proportion (discounted total): Total fees (discounted total) of the Cost Allocation Unit/Total Fees (discounted total) * 100%
        :rtype: str
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio

    @property
    def Trend(self):
        r"""Month-on-month ratio (discounted total): [Total fees (discounted total) of the cost allocation unit in this month - Total fees (discounted total) of the cost allocation unit in the previous month]/Total fees (discounted total) of the cost allocation unit in the previous month * 100%
        :rtype: str
        """
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def TrendType(self):
        r"""Sequential Comparison Arrow
upward - Upward
downward - Downward
none - Stable
        :rtype: str
        """
        return self._TrendType

    @TrendType.setter
    def TrendType(self, TrendType):
        self._TrendType = TrendType

    @property
    def BusinessCode(self):
        r"""Product code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        r"""Product name: Various cloud products purchased by users
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def TotalCost(self):
        r"""Original price of a component: Original Price = Component List Price * Component Usage * Duration of Use (not displayed if the customer enjoys a fixed price/contract price, and not displayed by default in refund scenarios), specified price mode
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RICost(self):
        r"""Original price deducted by a reserved instance: The original price of a component deducted by reserved instances for this product or service
        :rtype: str
        """
        return self._RICost

    @RICost.setter
    def RICost(self, RICost):
        self._RICost = RICost

    @property
    def SPCost(self):
        r"""Savings plan deduction from original price: Savings Plan Deduction from Original Price = Monetary Value of Savings Plan Deduction/ Savings Plan Deduction Rate
        :rtype: str
        """
        return self._SPCost

    @SPCost.setter
    def SPCost(self, SPCost):
        self._SPCost = SPCost

    @property
    def CashPayAmount(self):
        r"""Cash account expenditure (CNY): The amount paid through the cash account
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def VoucherPayAmount(self):
        r"""Promo voucher expenditure (CNY): The amount paid using various vouchers (such as promo vouchers and cash vouchers)

        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Gift account expenditure (CNY): The amount paid using free credits
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        r"""Royalty account expenditure (CNY): The amount paid through the royalty account
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def AllocationRealTotalCost(self):
        r"""Discounted total: discounted total = (Original Price - Original Price Deducted by a Reserved Instance - Savings Plan Deduction from Original Price) * Discount Rate
        :rtype: str
        """
        return self._AllocationRealTotalCost

    @AllocationRealTotalCost.setter
    def AllocationRealTotalCost(self, AllocationRealTotalCost):
        self._AllocationRealTotalCost = AllocationRealTotalCost

    @property
    def GatherTax(self):
        r"""Collected fees (tax): Tax directly collected to the cost allocation unit based on the collection rules
        :rtype: str
        """
        return self._GatherTax

    @GatherTax.setter
    def GatherTax(self, GatherTax):
        self._GatherTax = GatherTax

    @property
    def AllocateTax(self):
        r"""Allocated fees (tax): Resource tax allocated to the cost allocation unit based on the allocation rules
        :rtype: str
        """
        return self._AllocateTax

    @AllocateTax.setter
    def AllocateTax(self, AllocateTax):
        self._AllocateTax = AllocateTax

    @property
    def TotalTax(self):
        r"""Total fees (tax): Total fees of the cost allocation unit, Collected Fees (Tax) + Allocated fees (Tax)
        :rtype: str
        """
        return self._TotalTax

    @TotalTax.setter
    def TotalTax(self, TotalTax):
        self._TotalTax = TotalTax

    @property
    def GatherCostBeforeTax(self):
        r"""GatherCostBeforeTax
        :rtype: str
        """
        return self._GatherCostBeforeTax

    @GatherCostBeforeTax.setter
    def GatherCostBeforeTax(self, GatherCostBeforeTax):
        self._GatherCostBeforeTax = GatherCostBeforeTax

    @property
    def AllocateCostBeforeTax(self):
        r"""AllocateCostBeforeTax
        :rtype: str
        """
        return self._AllocateCostBeforeTax

    @AllocateCostBeforeTax.setter
    def AllocateCostBeforeTax(self, AllocateCostBeforeTax):
        self._AllocateCostBeforeTax = AllocateCostBeforeTax

    @property
    def TotalCostBeforeTax(self):
        r"""TotalCostBeforeTax
        :rtype: str
        """
        return self._TotalCostBeforeTax

    @TotalCostBeforeTax.setter
    def TotalCostBeforeTax(self, TotalCostBeforeTax):
        self._TotalCostBeforeTax = TotalCostBeforeTax

    @property
    def Tax(self):
        r"""Tax
        :rtype: str
        """
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def CostBeforeTax(self):
        r"""CostBeforeTax
        :rtype: str
        """
        return self._CostBeforeTax

    @CostBeforeTax.setter
    def CostBeforeTax(self, CostBeforeTax):
        self._CostBeforeTax = CostBeforeTax


    def _deserialize(self, params):
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._TreeNodeUniqKeyName = params.get("TreeNodeUniqKeyName")
        self._BillDate = params.get("BillDate")
        self._GatherCashPayAmount = params.get("GatherCashPayAmount")
        self._GatherVoucherPayAmount = params.get("GatherVoucherPayAmount")
        self._GatherIncentivePayAmount = params.get("GatherIncentivePayAmount")
        self._GatherTransferPayAmount = params.get("GatherTransferPayAmount")
        self._AllocateCashPayAmount = params.get("AllocateCashPayAmount")
        self._AllocateVoucherPayAmount = params.get("AllocateVoucherPayAmount")
        self._AllocateIncentivePayAmount = params.get("AllocateIncentivePayAmount")
        self._AllocateTransferPayAmount = params.get("AllocateTransferPayAmount")
        self._TotalCashPayAmount = params.get("TotalCashPayAmount")
        self._TotalVoucherPayAmount = params.get("TotalVoucherPayAmount")
        self._TotalIncentivePayAmount = params.get("TotalIncentivePayAmount")
        self._TotalTransferPayAmount = params.get("TotalTransferPayAmount")
        self._GatherRealCost = params.get("GatherRealCost")
        self._AllocateRealCost = params.get("AllocateRealCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._Ratio = params.get("Ratio")
        self._Trend = params.get("Trend")
        self._TrendType = params.get("TrendType")
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._TotalCost = params.get("TotalCost")
        self._RICost = params.get("RICost")
        self._SPCost = params.get("SPCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._AllocationRealTotalCost = params.get("AllocationRealTotalCost")
        self._GatherTax = params.get("GatherTax")
        self._AllocateTax = params.get("AllocateTax")
        self._TotalTax = params.get("TotalTax")
        self._GatherCostBeforeTax = params.get("GatherCostBeforeTax")
        self._AllocateCostBeforeTax = params.get("AllocateCostBeforeTax")
        self._TotalCostBeforeTax = params.get("TotalCostBeforeTax")
        self._Tax = params.get("Tax")
        self._CostBeforeTax = params.get("CostBeforeTax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationSummaryByItem(AbstractModel):
    r"""Details of a Cost Allocation Bill by item

    """

    def __init__(self):
        r"""
        :param _TreeNodeUniqKey: Unique identifier of a cost allocation unit
        :type TreeNodeUniqKey: str
        :param _TreeNodeUniqKeyName: Name of a cost allocation unit
        :type TreeNodeUniqKeyName: str
        :param _BillDate: Date: Settlement date
        :type BillDate: str
        :param _PayerUin: Payer UIN: Account ID of the payer, which is the unique account identifier for the user in Tencent Cloud.
        :type PayerUin: str
        :param _OwnerUin: User UIN: Account ID of the actual resource user
        :type OwnerUin: str
        :param _OperateUin: Operator account ID (the resource account ID or role ID opened by prepaid resource ordering or postpaid operation)
        :type OperateUin: str
        :param _PayMode: Billing mode code
        :type PayMode: str
        :param _PayModeName: Billing mode: Resource billing mode, which can be monthly subscription or pay-as-you-go.
        :type PayModeName: str
        :param _ActionType: Transaction type code
        :type ActionType: str
        :param _ActionTypeName: Transaction type: Detailed transaction type
        :type ActionTypeName: str
        :param _BusinessCode: Product code
        :type BusinessCode: str
        :param _BusinessCodeName: Product name: Various cloud products purchased by users
        :type BusinessCodeName: str
        :param _ProductCode: Subproduct code
        :type ProductCode: str
        :param _ProductCodeName: Subproduct name: Product subdivision type purchased by the user
        :type ProductCodeName: str
        :param _RegionId: Region ID
        :type RegionId: int
        :param _RegionName: Region name: The region where the resource is located
        :type RegionName: str
        :param _ZoneId: AZ ID
        :type ZoneId: int
        :param _ZoneName: Availability zone: The availability zone where the resource is located.
        :type ZoneName: str
        :param _InstanceType: Instance type code
        :type InstanceType: str
        :param _InstanceTypeName: Instance type: The type of an instance corresponding to the product service purchased, including resource packages, RI, SP, and spot instances. It is displayed as "-" by default for regular instances.
        :type InstanceTypeName: str
        :param _ResourceId: Resource ID: Resources vary by product, and the content is not identical. For example, Cloud Virtual Machine (CVM) corresponds to the instance ID. If the product is split, it shows the split item ID, such as COS bucket ID and CDN domain name.
        :type ResourceId: str
        :param _ResourceName: Instance name: The name set by the user for the resource in the console, which is empty by default if not set. If the product is split, it shows the split resource alias.
        :type ResourceName: str
        :param _Tag: Allocation tag: The resource-bound tag
        :type Tag: list of BillTag
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _ProjectName: Project name: The Project to which a resource belongs, which is independently allocated by the user for the resource in the console. If a resource has not been allocated to an Project, it will be a default Project.
        :type ProjectName: str
        :param _AllocationType: Cost collection type: The source types of fees, including allocated, collection and unallocated.
0 - Allocation
1 - Collection
-1 - Unallocated
        :type AllocationType: int
        :param _TotalCost: Original price of a component: Original Price = Component List Price * Component Usage * Duration of Use (not displayed if the customer enjoys a fixed price/contract price, and not displayed by default in refund scenarios), specified price mode
        :type TotalCost: str
        :param _RiTimeSpan: Reserved instance deduction duration: The duration of use deducted by reserved instances for this product or service.
        :type RiTimeSpan: str
        :param _RiCost: Original price deducted by a reserved instance: The original price of a component deducted by reserved instances for this product or service
        :type RiCost: str
        :param _RealTotalCost: Discounted total: discounted total = (Original Price - Original Price Deducted by a Reserved Instance - Savings Plan Deduction from Original Price) * Discount Rate
        :type RealTotalCost: str
        :param _CashPayAmount: Cash account expenditure (CNY): The amount paid through the cash account
        :type CashPayAmount: str
        :param _VoucherPayAmount: Promo voucher expenditure (CNY): The amount paid using various vouchers (such as promo vouchers and cash vouchers)
        :type VoucherPayAmount: str
        :param _IncentivePayAmount: Gift account expenditure (CNY): The amount paid using free credits
        :type IncentivePayAmount: str
        :param _TransferPayAmount: Royalty account expenditure (CNY): The amount paid through the royalty account
        :type TransferPayAmount: str
        :param _ItemCode: Component name code
        :type ItemCode: str
        :param _ItemCodeName: Component name: The specific component of a product or service purchased by the user
        :type ItemCodeName: str
        :param _ComponentCode: Component type code
        :type ComponentCode: str
        :param _ComponentCodeName: Component type: The major component category corresponding to the product or service purchased by the user
        :type ComponentCodeName: str
        :param _SplitItemId: Split item ID: The ID of the split item involved in the split product, such as COS bucket ID and CDN domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SplitItemId: str
        :param _SplitItemName: Split item name: The split item involved in the split product
Note: This field may return null, indicating that no valid values can be obtained.
        :type SplitItemName: str
        :param _FeeBeginTime: Usage start time: Usage start time
        :type FeeBeginTime: str
        :param _FeeEndTime: Usage end time: Product or service usage end time
        :type FeeEndTime: str
        :param _SPCost: Savings plan deduction from original price: Savings Plan Deduction from Original Price = Monetary Value of Savings Plan Deduction/ Savings Plan Deduction Rate
        :type SPCost: str
        :param _RegionType: Domestic and international codes
        :type RegionType: str
        :param _RegionTypeName: Domestic and international: Resource region type (domestic, international)
        :type RegionTypeName: str
        :param _SinglePrice: Component list price: The original unit price of the component on the portal (not displayed if the customer enjoys a fixed price/contract price)
        :type SinglePrice: str
        :param _ContractPrice: Component unit price: Discounted unit price of the component. Component unit price = list price * discount.
        :type ContractPrice: str
        :param _SinglePriceUnit: Component Price Unit: Unit of component price, Unit Composition: CNY/usage unit/duration unit
        :type SinglePriceUnit: str
        :param _UsedAmount: Component usage: The actual settlement usage of the component, Component Usage = Original Component Usage - Deducted Usage (including resource packages)
        :type UsedAmount: str
        :param _UsedAmountUnit: Component usage unit: Unit of measurement corresponding to component usage.
        :type UsedAmountUnit: str
        :param _TimeSpan: Usage duration: The duration of resource usage, Component Usage = Original Component Usage Duration - Deducted Duration (including resource packages)
        :type TimeSpan: str
        :param _TimeUnit: Duration unit: Unit of resource usage duration.
        :type TimeUnit: str
        :param _ReserveDetail: Remark attribute (instance configuration): Additional remark information, such as reserved instance type and transaction type for reserved instances, regional information of both ends for CCN products.
        :type ReserveDetail: str
        :param _RealTotalMeasure: Original usage/duration: The original usage of the component before deduction by resource packages.
(Currently only TRTC, TEM, Cloud Call Center, and CDZ products support this information display. Other products are being integrated.)
        :type RealTotalMeasure: str
        :param _DeductedMeasure: Deduction of usage/duration (including resource packages): The amount of usage deducted by resource packages
(Currently only TRTC, TEM, Cloud Call Center, and CDZ products support this information display. Other products are being integrated.)
        :type DeductedMeasure: str
        :param _Discount: Discount rate: The discount rate enjoyed by this resource (it is not shown by default if the customer enjoys a fixed/contract price, and it is also not shown by default in the refund scenario)
        :type Discount: str
        :param _BlendedDiscount: Mixed discount rate: The final discount rate after integrating various discount deductions. Mixed Discount Rate = Discounted total price/Original Price.
        :type BlendedDiscount: str
        :param _PriceInfo: Price attribute: Other attributes of the component that affect discount pricing besides unit price and duration
        :type PriceInfo: list of str
        :param _Formula: Calculation rule explanation: A detailed explanation to calculations of billing settlement for special transaction types, such as refund and configuration changes.
        :type Formula: str
        :param _FormulaUrl: Billing Rules: The detailed billing rules for each product shown in the portal explanation link
        :type FormulaUrl: str
        :param _ComponentConfig: Configuration description: Information on specification of resource configuration
        :type ComponentConfig: str
        :param _SPDeduction: SPDeduction
        :type SPDeduction: str
        :param _SPDeductionRate: Savings plan deduction rate: The discount rate for this component within the available balance limit of the savings plan
        :type SPDeductionRate: str
        :param _Currency: Currency.
        :type Currency: str
        :param _Tax: Tax
        :type Tax: str
        :param _TaxRate: tax rate
        :type TaxRate: str
        :param _CostBeforeTax: CostBeforeTax
        :type CostBeforeTax: str
        :param _AmountBeforeTax: AmountBeforeTax
        :type AmountBeforeTax: str
        :param _AssociatedOrder: AssociatedOrder
        :type AssociatedOrder: str
        :param _DiscountObject: Discount object of the current consumption item, such as official website discount, user discount and activity discount.
        :type DiscountObject: str
        :param _DiscountType: Discount type of the current consumption item, such as discount and contract price.
        :type DiscountType: str
        :param _DiscountContent: Supplementary description of the offer type, for example: business discount 20% off, the offer type is "discount" and the discount content is "0.8".
        :type DiscountContent: str
        :param _BillMonth: Billing month
        :type BillMonth: str
        """
        self._TreeNodeUniqKey = None
        self._TreeNodeUniqKeyName = None
        self._BillDate = None
        self._PayerUin = None
        self._OwnerUin = None
        self._OperateUin = None
        self._PayMode = None
        self._PayModeName = None
        self._ActionType = None
        self._ActionTypeName = None
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._ProductCode = None
        self._ProductCodeName = None
        self._RegionId = None
        self._RegionName = None
        self._ZoneId = None
        self._ZoneName = None
        self._InstanceType = None
        self._InstanceTypeName = None
        self._ResourceId = None
        self._ResourceName = None
        self._Tag = None
        self._ProjectId = None
        self._ProjectName = None
        self._AllocationType = None
        self._TotalCost = None
        self._RiTimeSpan = None
        self._RiCost = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._VoucherPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None
        self._ItemCode = None
        self._ItemCodeName = None
        self._ComponentCode = None
        self._ComponentCodeName = None
        self._SplitItemId = None
        self._SplitItemName = None
        self._FeeBeginTime = None
        self._FeeEndTime = None
        self._SPCost = None
        self._RegionType = None
        self._RegionTypeName = None
        self._SinglePrice = None
        self._ContractPrice = None
        self._SinglePriceUnit = None
        self._UsedAmount = None
        self._UsedAmountUnit = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._ReserveDetail = None
        self._RealTotalMeasure = None
        self._DeductedMeasure = None
        self._Discount = None
        self._BlendedDiscount = None
        self._PriceInfo = None
        self._Formula = None
        self._FormulaUrl = None
        self._ComponentConfig = None
        self._SPDeduction = None
        self._SPDeductionRate = None
        self._Currency = None
        self._Tax = None
        self._TaxRate = None
        self._CostBeforeTax = None
        self._AmountBeforeTax = None
        self._AssociatedOrder = None
        self._DiscountObject = None
        self._DiscountType = None
        self._DiscountContent = None
        self._BillMonth = None

    @property
    def TreeNodeUniqKey(self):
        r"""Unique identifier of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def TreeNodeUniqKeyName(self):
        r"""Name of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKeyName

    @TreeNodeUniqKeyName.setter
    def TreeNodeUniqKeyName(self, TreeNodeUniqKeyName):
        self._TreeNodeUniqKeyName = TreeNodeUniqKeyName

    @property
    def BillDate(self):
        r"""Date: Settlement date
        :rtype: str
        """
        return self._BillDate

    @BillDate.setter
    def BillDate(self, BillDate):
        self._BillDate = BillDate

    @property
    def PayerUin(self):
        r"""Payer UIN: Account ID of the payer, which is the unique account identifier for the user in Tencent Cloud.
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        r"""User UIN: Account ID of the actual resource user
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        r"""Operator account ID (the resource account ID or role ID opened by prepaid resource ordering or postpaid operation)
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def PayMode(self):
        r"""Billing mode code
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        r"""Billing mode: Resource billing mode, which can be monthly subscription or pay-as-you-go.
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ActionType(self):
        r"""Transaction type code
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        r"""Transaction type: Detailed transaction type
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def BusinessCode(self):
        r"""Product code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        r"""Product name: Various cloud products purchased by users
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCode(self):
        r"""Subproduct code
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductCodeName(self):
        r"""Subproduct name: Product subdivision type purchased by the user
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def RegionId(self):
        r"""Region ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        r"""Region name: The region where the resource is located
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneId(self):
        r"""AZ ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        r"""Availability zone: The availability zone where the resource is located.
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def InstanceType(self):
        r"""Instance type code
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceTypeName(self):
        r"""Instance type: The type of an instance corresponding to the product service purchased, including resource packages, RI, SP, and spot instances. It is displayed as "-" by default for regular instances.
        :rtype: str
        """
        return self._InstanceTypeName

    @InstanceTypeName.setter
    def InstanceTypeName(self, InstanceTypeName):
        self._InstanceTypeName = InstanceTypeName

    @property
    def ResourceId(self):
        r"""Resource ID: Resources vary by product, and the content is not identical. For example, Cloud Virtual Machine (CVM) corresponds to the instance ID. If the product is split, it shows the split item ID, such as COS bucket ID and CDN domain name.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        r"""Instance name: The name set by the user for the resource in the console, which is empty by default if not set. If the product is split, it shows the split resource alias.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Tag(self):
        r"""Allocation tag: The resource-bound tag
        :rtype: list of BillTag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""Project name: The Project to which a resource belongs, which is independently allocated by the user for the resource in the console. If a resource has not been allocated to an Project, it will be a default Project.
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def AllocationType(self):
        r"""Cost collection type: The source types of fees, including allocated, collection and unallocated.
0 - Allocation
1 - Collection
-1 - Unallocated
        :rtype: int
        """
        return self._AllocationType

    @AllocationType.setter
    def AllocationType(self, AllocationType):
        self._AllocationType = AllocationType

    @property
    def TotalCost(self):
        r"""Original price of a component: Original Price = Component List Price * Component Usage * Duration of Use (not displayed if the customer enjoys a fixed price/contract price, and not displayed by default in refund scenarios), specified price mode
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RiTimeSpan(self):
        r"""Reserved instance deduction duration: The duration of use deducted by reserved instances for this product or service.
        :rtype: str
        """
        return self._RiTimeSpan

    @RiTimeSpan.setter
    def RiTimeSpan(self, RiTimeSpan):
        self._RiTimeSpan = RiTimeSpan

    @property
    def RiCost(self):
        r"""Original price deducted by a reserved instance: The original price of a component deducted by reserved instances for this product or service
        :rtype: str
        """
        return self._RiCost

    @RiCost.setter
    def RiCost(self, RiCost):
        self._RiCost = RiCost

    @property
    def RealTotalCost(self):
        r"""Discounted total: discounted total = (Original Price - Original Price Deducted by a Reserved Instance - Savings Plan Deduction from Original Price) * Discount Rate
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        r"""Cash account expenditure (CNY): The amount paid through the cash account
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def VoucherPayAmount(self):
        r"""Promo voucher expenditure (CNY): The amount paid using various vouchers (such as promo vouchers and cash vouchers)
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Gift account expenditure (CNY): The amount paid using free credits
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        r"""Royalty account expenditure (CNY): The amount paid through the royalty account
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def ItemCode(self):
        r"""Component name code
        :rtype: str
        """
        return self._ItemCode

    @ItemCode.setter
    def ItemCode(self, ItemCode):
        self._ItemCode = ItemCode

    @property
    def ItemCodeName(self):
        r"""Component name: The specific component of a product or service purchased by the user
        :rtype: str
        """
        return self._ItemCodeName

    @ItemCodeName.setter
    def ItemCodeName(self, ItemCodeName):
        self._ItemCodeName = ItemCodeName

    @property
    def ComponentCode(self):
        r"""Component type code
        :rtype: str
        """
        return self._ComponentCode

    @ComponentCode.setter
    def ComponentCode(self, ComponentCode):
        self._ComponentCode = ComponentCode

    @property
    def ComponentCodeName(self):
        r"""Component type: The major component category corresponding to the product or service purchased by the user
        :rtype: str
        """
        return self._ComponentCodeName

    @ComponentCodeName.setter
    def ComponentCodeName(self, ComponentCodeName):
        self._ComponentCodeName = ComponentCodeName

    @property
    def SplitItemId(self):
        warnings.warn("parameter `SplitItemId` is deprecated", DeprecationWarning) 

        r"""Split item ID: The ID of the split item involved in the split product, such as COS bucket ID and CDN domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SplitItemId

    @SplitItemId.setter
    def SplitItemId(self, SplitItemId):
        warnings.warn("parameter `SplitItemId` is deprecated", DeprecationWarning) 

        self._SplitItemId = SplitItemId

    @property
    def SplitItemName(self):
        warnings.warn("parameter `SplitItemName` is deprecated", DeprecationWarning) 

        r"""Split item name: The split item involved in the split product
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SplitItemName

    @SplitItemName.setter
    def SplitItemName(self, SplitItemName):
        warnings.warn("parameter `SplitItemName` is deprecated", DeprecationWarning) 

        self._SplitItemName = SplitItemName

    @property
    def FeeBeginTime(self):
        r"""Usage start time: Usage start time
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        r"""Usage end time: Product or service usage end time
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def SPCost(self):
        r"""Savings plan deduction from original price: Savings Plan Deduction from Original Price = Monetary Value of Savings Plan Deduction/ Savings Plan Deduction Rate
        :rtype: str
        """
        return self._SPCost

    @SPCost.setter
    def SPCost(self, SPCost):
        self._SPCost = SPCost

    @property
    def RegionType(self):
        r"""Domestic and international codes
        :rtype: str
        """
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def RegionTypeName(self):
        r"""Domestic and international: Resource region type (domestic, international)
        :rtype: str
        """
        return self._RegionTypeName

    @RegionTypeName.setter
    def RegionTypeName(self, RegionTypeName):
        self._RegionTypeName = RegionTypeName

    @property
    def SinglePrice(self):
        r"""Component list price: The original unit price of the component on the portal (not displayed if the customer enjoys a fixed price/contract price)
        :rtype: str
        """
        return self._SinglePrice

    @SinglePrice.setter
    def SinglePrice(self, SinglePrice):
        self._SinglePrice = SinglePrice

    @property
    def ContractPrice(self):
        r"""Component unit price: Discounted unit price of the component. Component unit price = list price * discount.
        :rtype: str
        """
        return self._ContractPrice

    @ContractPrice.setter
    def ContractPrice(self, ContractPrice):
        self._ContractPrice = ContractPrice

    @property
    def SinglePriceUnit(self):
        r"""Component Price Unit: Unit of component price, Unit Composition: CNY/usage unit/duration unit
        :rtype: str
        """
        return self._SinglePriceUnit

    @SinglePriceUnit.setter
    def SinglePriceUnit(self, SinglePriceUnit):
        self._SinglePriceUnit = SinglePriceUnit

    @property
    def UsedAmount(self):
        r"""Component usage: The actual settlement usage of the component, Component Usage = Original Component Usage - Deducted Usage (including resource packages)
        :rtype: str
        """
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

    @property
    def UsedAmountUnit(self):
        r"""Component usage unit: Unit of measurement corresponding to component usage.
        :rtype: str
        """
        return self._UsedAmountUnit

    @UsedAmountUnit.setter
    def UsedAmountUnit(self, UsedAmountUnit):
        self._UsedAmountUnit = UsedAmountUnit

    @property
    def TimeSpan(self):
        r"""Usage duration: The duration of resource usage, Component Usage = Original Component Usage Duration - Deducted Duration (including resource packages)
        :rtype: str
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        r"""Duration unit: Unit of resource usage duration.
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def ReserveDetail(self):
        r"""Remark attribute (instance configuration): Additional remark information, such as reserved instance type and transaction type for reserved instances, regional information of both ends for CCN products.
        :rtype: str
        """
        return self._ReserveDetail

    @ReserveDetail.setter
    def ReserveDetail(self, ReserveDetail):
        self._ReserveDetail = ReserveDetail

    @property
    def RealTotalMeasure(self):
        r"""Original usage/duration: The original usage of the component before deduction by resource packages.
(Currently only TRTC, TEM, Cloud Call Center, and CDZ products support this information display. Other products are being integrated.)
        :rtype: str
        """
        return self._RealTotalMeasure

    @RealTotalMeasure.setter
    def RealTotalMeasure(self, RealTotalMeasure):
        self._RealTotalMeasure = RealTotalMeasure

    @property
    def DeductedMeasure(self):
        r"""Deduction of usage/duration (including resource packages): The amount of usage deducted by resource packages
(Currently only TRTC, TEM, Cloud Call Center, and CDZ products support this information display. Other products are being integrated.)
        :rtype: str
        """
        return self._DeductedMeasure

    @DeductedMeasure.setter
    def DeductedMeasure(self, DeductedMeasure):
        self._DeductedMeasure = DeductedMeasure

    @property
    def Discount(self):
        r"""Discount rate: The discount rate enjoyed by this resource (it is not shown by default if the customer enjoys a fixed/contract price, and it is also not shown by default in the refund scenario)
        :rtype: str
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def BlendedDiscount(self):
        r"""Mixed discount rate: The final discount rate after integrating various discount deductions. Mixed Discount Rate = Discounted total price/Original Price.
        :rtype: str
        """
        return self._BlendedDiscount

    @BlendedDiscount.setter
    def BlendedDiscount(self, BlendedDiscount):
        self._BlendedDiscount = BlendedDiscount

    @property
    def PriceInfo(self):
        r"""Price attribute: Other attributes of the component that affect discount pricing besides unit price and duration
        :rtype: list of str
        """
        return self._PriceInfo

    @PriceInfo.setter
    def PriceInfo(self, PriceInfo):
        self._PriceInfo = PriceInfo

    @property
    def Formula(self):
        r"""Calculation rule explanation: A detailed explanation to calculations of billing settlement for special transaction types, such as refund and configuration changes.
        :rtype: str
        """
        return self._Formula

    @Formula.setter
    def Formula(self, Formula):
        self._Formula = Formula

    @property
    def FormulaUrl(self):
        r"""Billing Rules: The detailed billing rules for each product shown in the portal explanation link
        :rtype: str
        """
        return self._FormulaUrl

    @FormulaUrl.setter
    def FormulaUrl(self, FormulaUrl):
        self._FormulaUrl = FormulaUrl

    @property
    def ComponentConfig(self):
        r"""Configuration description: Information on specification of resource configuration
        :rtype: str
        """
        return self._ComponentConfig

    @ComponentConfig.setter
    def ComponentConfig(self, ComponentConfig):
        self._ComponentConfig = ComponentConfig

    @property
    def SPDeduction(self):
        r"""SPDeduction
        :rtype: str
        """
        return self._SPDeduction

    @SPDeduction.setter
    def SPDeduction(self, SPDeduction):
        self._SPDeduction = SPDeduction

    @property
    def SPDeductionRate(self):
        r"""Savings plan deduction rate: The discount rate for this component within the available balance limit of the savings plan
        :rtype: str
        """
        return self._SPDeductionRate

    @SPDeductionRate.setter
    def SPDeductionRate(self, SPDeductionRate):
        self._SPDeductionRate = SPDeductionRate

    @property
    def Currency(self):
        r"""Currency.
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def Tax(self):
        r"""Tax
        :rtype: str
        """
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def TaxRate(self):
        r"""tax rate
        :rtype: str
        """
        return self._TaxRate

    @TaxRate.setter
    def TaxRate(self, TaxRate):
        self._TaxRate = TaxRate

    @property
    def CostBeforeTax(self):
        r"""CostBeforeTax
        :rtype: str
        """
        return self._CostBeforeTax

    @CostBeforeTax.setter
    def CostBeforeTax(self, CostBeforeTax):
        self._CostBeforeTax = CostBeforeTax

    @property
    def AmountBeforeTax(self):
        r"""AmountBeforeTax
        :rtype: str
        """
        return self._AmountBeforeTax

    @AmountBeforeTax.setter
    def AmountBeforeTax(self, AmountBeforeTax):
        self._AmountBeforeTax = AmountBeforeTax

    @property
    def AssociatedOrder(self):
        r"""AssociatedOrder
        :rtype: str
        """
        return self._AssociatedOrder

    @AssociatedOrder.setter
    def AssociatedOrder(self, AssociatedOrder):
        self._AssociatedOrder = AssociatedOrder

    @property
    def DiscountObject(self):
        r"""Discount object of the current consumption item, such as official website discount, user discount and activity discount.
        :rtype: str
        """
        return self._DiscountObject

    @DiscountObject.setter
    def DiscountObject(self, DiscountObject):
        self._DiscountObject = DiscountObject

    @property
    def DiscountType(self):
        r"""Discount type of the current consumption item, such as discount and contract price.
        :rtype: str
        """
        return self._DiscountType

    @DiscountType.setter
    def DiscountType(self, DiscountType):
        self._DiscountType = DiscountType

    @property
    def DiscountContent(self):
        r"""Supplementary description of the offer type, for example: business discount 20% off, the offer type is "discount" and the discount content is "0.8".
        :rtype: str
        """
        return self._DiscountContent

    @DiscountContent.setter
    def DiscountContent(self, DiscountContent):
        self._DiscountContent = DiscountContent

    @property
    def BillMonth(self):
        r"""Billing month
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth


    def _deserialize(self, params):
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._TreeNodeUniqKeyName = params.get("TreeNodeUniqKeyName")
        self._BillDate = params.get("BillDate")
        self._PayerUin = params.get("PayerUin")
        self._OwnerUin = params.get("OwnerUin")
        self._OperateUin = params.get("OperateUin")
        self._PayMode = params.get("PayMode")
        self._PayModeName = params.get("PayModeName")
        self._ActionType = params.get("ActionType")
        self._ActionTypeName = params.get("ActionTypeName")
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._ProductCode = params.get("ProductCode")
        self._ProductCodeName = params.get("ProductCodeName")
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._InstanceType = params.get("InstanceType")
        self._InstanceTypeName = params.get("InstanceTypeName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = BillTag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._AllocationType = params.get("AllocationType")
        self._TotalCost = params.get("TotalCost")
        self._RiTimeSpan = params.get("RiTimeSpan")
        self._RiCost = params.get("RiCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._ItemCode = params.get("ItemCode")
        self._ItemCodeName = params.get("ItemCodeName")
        self._ComponentCode = params.get("ComponentCode")
        self._ComponentCodeName = params.get("ComponentCodeName")
        self._SplitItemId = params.get("SplitItemId")
        self._SplitItemName = params.get("SplitItemName")
        self._FeeBeginTime = params.get("FeeBeginTime")
        self._FeeEndTime = params.get("FeeEndTime")
        self._SPCost = params.get("SPCost")
        self._RegionType = params.get("RegionType")
        self._RegionTypeName = params.get("RegionTypeName")
        self._SinglePrice = params.get("SinglePrice")
        self._ContractPrice = params.get("ContractPrice")
        self._SinglePriceUnit = params.get("SinglePriceUnit")
        self._UsedAmount = params.get("UsedAmount")
        self._UsedAmountUnit = params.get("UsedAmountUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._ReserveDetail = params.get("ReserveDetail")
        self._RealTotalMeasure = params.get("RealTotalMeasure")
        self._DeductedMeasure = params.get("DeductedMeasure")
        self._Discount = params.get("Discount")
        self._BlendedDiscount = params.get("BlendedDiscount")
        self._PriceInfo = params.get("PriceInfo")
        self._Formula = params.get("Formula")
        self._FormulaUrl = params.get("FormulaUrl")
        self._ComponentConfig = params.get("ComponentConfig")
        self._SPDeduction = params.get("SPDeduction")
        self._SPDeductionRate = params.get("SPDeductionRate")
        self._Currency = params.get("Currency")
        self._Tax = params.get("Tax")
        self._TaxRate = params.get("TaxRate")
        self._CostBeforeTax = params.get("CostBeforeTax")
        self._AmountBeforeTax = params.get("AmountBeforeTax")
        self._AssociatedOrder = params.get("AssociatedOrder")
        self._DiscountObject = params.get("DiscountObject")
        self._DiscountType = params.get("DiscountType")
        self._DiscountContent = params.get("DiscountContent")
        self._BillMonth = params.get("BillMonth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationSummaryByResource(AbstractModel):
    r"""Detailed summary of the cost allocation bill by resource

    """

    def __init__(self):
        r"""
        :param _TreeNodeUniqKey: Unique identifier of a cost allocation unit
        :type TreeNodeUniqKey: str
        :param _TreeNodeUniqKeyName: Name of a cost allocation unit
        :type TreeNodeUniqKeyName: str
        :param _BillDate: Date: Settlement date
        :type BillDate: str
        :param _PayerUin: Payer UIN: Account ID of the payer, which is the unique account identifier for the user in Tencent Cloud.
        :type PayerUin: str
        :param _OwnerUin: User UIN: Account ID of the actual resource user
        :type OwnerUin: str
        :param _OperateUin: Operator account ID (the resource account ID or role ID opened by prepaid resource ordering or postpaid operation)
        :type OperateUin: str
        :param _PayMode: Billing mode code
        :type PayMode: str
        :param _PayModeName: Billing mode: Resource billing mode, which can be monthly subscription or pay-as-you-go.
        :type PayModeName: str
        :param _ActionType: Transaction type code
        :type ActionType: str
        :param _ActionTypeName: Transaction type: Detailed transaction type
        :type ActionTypeName: str
        :param _BusinessCode: Product code
        :type BusinessCode: str
        :param _BusinessCodeName: Product name: Various cloud products purchased by users
        :type BusinessCodeName: str
        :param _ProductCode: Subproduct code
        :type ProductCode: str
        :param _ProductCodeName: Subproduct name: Product subdivision type purchased by the user
        :type ProductCodeName: str
        :param _RegionId: Region ID
        :type RegionId: int
        :param _RegionName: Region name: The region where the resource is located
        :type RegionName: str
        :param _ZoneId: AZ ID
        :type ZoneId: int
        :param _ZoneName: Availability zone: The availability zone where the resource is located.
        :type ZoneName: str
        :param _InstanceType: Instance type code
        :type InstanceType: str
        :param _InstanceTypeName: Instance type: The type of an instance corresponding to the product service purchased, including resource packages, RI, SP, and spot instances. It is displayed as "-" by default for regular instances.
        :type InstanceTypeName: str
        :param _ResourceId: Resource ID: Resources vary by product, and the content is not identical. For example, Cloud Virtual Machine (CVM) corresponds to the instance ID. If the product is split, it shows the split item ID, such as COS bucket ID and CDN domain name.
        :type ResourceId: str
        :param _ResourceName: Instance name: The name set by the user for the resource in the console, which is empty by default if not set. If the product is split, it shows the split resource alias.
        :type ResourceName: str
        :param _Tag: Allocation tag: The resource-bound tag
        :type Tag: list of BillTag
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _ProjectName: Project name: The Project to which a resource belongs, which is independently allocated by the user for the resource in the console. If a resource has not been allocated to an Project, it will be a default Project.
        :type ProjectName: str
        :param _AllocationType: Cost collection type: The source types of fees, including allocated, collection and unallocated.
0 - Allocation 
1 - Collection 
-1 - Unallocated
        :type AllocationType: int
        :param _TotalCost: Original price of a component: Original Price = Component List Price * Component Usage * Duration of Use (not displayed if the customer enjoys a fixed price/contract price, and not displayed by default in refund scenarios), specified price mode
        :type TotalCost: str
        :param _RiTimeSpan: Reserved instance deduction duration: The duration of use deducted by reserved instances for this product or service.
        :type RiTimeSpan: str
        :param _RiCost: Original price deducted by a reserved instance: The original price of a component deducted by reserved instances for this product or service
        :type RiCost: str
        :param _RealTotalCost: Discounted total: discounted total = (Original Price - Original Price Deducted by a Reserved Instance - Savings Plan Deduction from Original Price) * Discount Rate
        :type RealTotalCost: str
        :param _CashPayAmount: Cash account expenditure (CNY): The amount paid through the cash account
        :type CashPayAmount: str
        :param _VoucherPayAmount: Promo voucher expenditure (CNY): The amount paid using various vouchers (such as promo vouchers and cash vouchers)
        :type VoucherPayAmount: str
        :param _IncentivePayAmount: Gift account expenditure (CNY): The amount paid using free credits
        :type IncentivePayAmount: str
        :param _TransferPayAmount: Royalty account expenditure (CNY): The amount paid through the royalty account
        :type TransferPayAmount: str
        :param _SplitItemId: Split item ID: The ID of the split item involved in the split product, such as COS bucket ID and CDN domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SplitItemId: str
        :param _SplitItemName: Split item name: The split item involved in the split product
Note: This field may return null, indicating that no valid values can be obtained.
        :type SplitItemName: str
        :param _FeeBeginTime: Usage start time: Usage start time
        :type FeeBeginTime: str
        :param _FeeEndTime: Usage end time: Product or service usage end time
        :type FeeEndTime: str
        :param _SPCost: Savings plan deduction from original price: Savings Plan Deduction from Original Price = Monetary Value of Savings Plan Deduction/ Savings Plan Deduction Rate
        :type SPCost: str
        :param _RegionType: Domestic and international codes
        :type RegionType: str
        :param _RegionTypeName: Domestic and international: Resource region type (domestic, international)
        :type RegionTypeName: str
        :param _ComponentConfig: Configuration description: Name and usage of each component under the corresponding resource (the total usage if the component is cumulative usage billing type)
        :type ComponentConfig: str
        :param _SPDeduction: SPDeduction
        :type SPDeduction: str
        :param _Currency: Currency.
        :type Currency: str
        :param _Tax: Tax
        :type Tax: str
        :param _TaxRate: tax rate
        :type TaxRate: str
        :param _CostBeforeTax: CostBeforeTax
        :type CostBeforeTax: str
        :param _AmountBeforeTax: AmountBeforeTax
        :type AmountBeforeTax: str
        :param _BillMonth: Billing month
        :type BillMonth: str
        """
        self._TreeNodeUniqKey = None
        self._TreeNodeUniqKeyName = None
        self._BillDate = None
        self._PayerUin = None
        self._OwnerUin = None
        self._OperateUin = None
        self._PayMode = None
        self._PayModeName = None
        self._ActionType = None
        self._ActionTypeName = None
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._ProductCode = None
        self._ProductCodeName = None
        self._RegionId = None
        self._RegionName = None
        self._ZoneId = None
        self._ZoneName = None
        self._InstanceType = None
        self._InstanceTypeName = None
        self._ResourceId = None
        self._ResourceName = None
        self._Tag = None
        self._ProjectId = None
        self._ProjectName = None
        self._AllocationType = None
        self._TotalCost = None
        self._RiTimeSpan = None
        self._RiCost = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._VoucherPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None
        self._SplitItemId = None
        self._SplitItemName = None
        self._FeeBeginTime = None
        self._FeeEndTime = None
        self._SPCost = None
        self._RegionType = None
        self._RegionTypeName = None
        self._ComponentConfig = None
        self._SPDeduction = None
        self._Currency = None
        self._Tax = None
        self._TaxRate = None
        self._CostBeforeTax = None
        self._AmountBeforeTax = None
        self._BillMonth = None

    @property
    def TreeNodeUniqKey(self):
        r"""Unique identifier of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def TreeNodeUniqKeyName(self):
        r"""Name of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKeyName

    @TreeNodeUniqKeyName.setter
    def TreeNodeUniqKeyName(self, TreeNodeUniqKeyName):
        self._TreeNodeUniqKeyName = TreeNodeUniqKeyName

    @property
    def BillDate(self):
        r"""Date: Settlement date
        :rtype: str
        """
        return self._BillDate

    @BillDate.setter
    def BillDate(self, BillDate):
        self._BillDate = BillDate

    @property
    def PayerUin(self):
        r"""Payer UIN: Account ID of the payer, which is the unique account identifier for the user in Tencent Cloud.
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        r"""User UIN: Account ID of the actual resource user
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        r"""Operator account ID (the resource account ID or role ID opened by prepaid resource ordering or postpaid operation)
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def PayMode(self):
        r"""Billing mode code
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        r"""Billing mode: Resource billing mode, which can be monthly subscription or pay-as-you-go.
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ActionType(self):
        r"""Transaction type code
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        r"""Transaction type: Detailed transaction type
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def BusinessCode(self):
        r"""Product code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        r"""Product name: Various cloud products purchased by users
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCode(self):
        r"""Subproduct code
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductCodeName(self):
        r"""Subproduct name: Product subdivision type purchased by the user
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def RegionId(self):
        r"""Region ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        r"""Region name: The region where the resource is located
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneId(self):
        r"""AZ ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        r"""Availability zone: The availability zone where the resource is located.
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def InstanceType(self):
        r"""Instance type code
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceTypeName(self):
        r"""Instance type: The type of an instance corresponding to the product service purchased, including resource packages, RI, SP, and spot instances. It is displayed as "-" by default for regular instances.
        :rtype: str
        """
        return self._InstanceTypeName

    @InstanceTypeName.setter
    def InstanceTypeName(self, InstanceTypeName):
        self._InstanceTypeName = InstanceTypeName

    @property
    def ResourceId(self):
        r"""Resource ID: Resources vary by product, and the content is not identical. For example, Cloud Virtual Machine (CVM) corresponds to the instance ID. If the product is split, it shows the split item ID, such as COS bucket ID and CDN domain name.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        r"""Instance name: The name set by the user for the resource in the console, which is empty by default if not set. If the product is split, it shows the split resource alias.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Tag(self):
        r"""Allocation tag: The resource-bound tag
        :rtype: list of BillTag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""Project name: The Project to which a resource belongs, which is independently allocated by the user for the resource in the console. If a resource has not been allocated to an Project, it will be a default Project.
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def AllocationType(self):
        r"""Cost collection type: The source types of fees, including allocated, collection and unallocated.
0 - Allocation 
1 - Collection 
-1 - Unallocated
        :rtype: int
        """
        return self._AllocationType

    @AllocationType.setter
    def AllocationType(self, AllocationType):
        self._AllocationType = AllocationType

    @property
    def TotalCost(self):
        r"""Original price of a component: Original Price = Component List Price * Component Usage * Duration of Use (not displayed if the customer enjoys a fixed price/contract price, and not displayed by default in refund scenarios), specified price mode
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RiTimeSpan(self):
        r"""Reserved instance deduction duration: The duration of use deducted by reserved instances for this product or service.
        :rtype: str
        """
        return self._RiTimeSpan

    @RiTimeSpan.setter
    def RiTimeSpan(self, RiTimeSpan):
        self._RiTimeSpan = RiTimeSpan

    @property
    def RiCost(self):
        r"""Original price deducted by a reserved instance: The original price of a component deducted by reserved instances for this product or service
        :rtype: str
        """
        return self._RiCost

    @RiCost.setter
    def RiCost(self, RiCost):
        self._RiCost = RiCost

    @property
    def RealTotalCost(self):
        r"""Discounted total: discounted total = (Original Price - Original Price Deducted by a Reserved Instance - Savings Plan Deduction from Original Price) * Discount Rate
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        r"""Cash account expenditure (CNY): The amount paid through the cash account
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def VoucherPayAmount(self):
        r"""Promo voucher expenditure (CNY): The amount paid using various vouchers (such as promo vouchers and cash vouchers)
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Gift account expenditure (CNY): The amount paid using free credits
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        r"""Royalty account expenditure (CNY): The amount paid through the royalty account
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def SplitItemId(self):
        warnings.warn("parameter `SplitItemId` is deprecated", DeprecationWarning) 

        r"""Split item ID: The ID of the split item involved in the split product, such as COS bucket ID and CDN domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SplitItemId

    @SplitItemId.setter
    def SplitItemId(self, SplitItemId):
        warnings.warn("parameter `SplitItemId` is deprecated", DeprecationWarning) 

        self._SplitItemId = SplitItemId

    @property
    def SplitItemName(self):
        warnings.warn("parameter `SplitItemName` is deprecated", DeprecationWarning) 

        r"""Split item name: The split item involved in the split product
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SplitItemName

    @SplitItemName.setter
    def SplitItemName(self, SplitItemName):
        warnings.warn("parameter `SplitItemName` is deprecated", DeprecationWarning) 

        self._SplitItemName = SplitItemName

    @property
    def FeeBeginTime(self):
        r"""Usage start time: Usage start time
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        r"""Usage end time: Product or service usage end time
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def SPCost(self):
        r"""Savings plan deduction from original price: Savings Plan Deduction from Original Price = Monetary Value of Savings Plan Deduction/ Savings Plan Deduction Rate
        :rtype: str
        """
        return self._SPCost

    @SPCost.setter
    def SPCost(self, SPCost):
        self._SPCost = SPCost

    @property
    def RegionType(self):
        r"""Domestic and international codes
        :rtype: str
        """
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def RegionTypeName(self):
        r"""Domestic and international: Resource region type (domestic, international)
        :rtype: str
        """
        return self._RegionTypeName

    @RegionTypeName.setter
    def RegionTypeName(self, RegionTypeName):
        self._RegionTypeName = RegionTypeName

    @property
    def ComponentConfig(self):
        r"""Configuration description: Name and usage of each component under the corresponding resource (the total usage if the component is cumulative usage billing type)
        :rtype: str
        """
        return self._ComponentConfig

    @ComponentConfig.setter
    def ComponentConfig(self, ComponentConfig):
        self._ComponentConfig = ComponentConfig

    @property
    def SPDeduction(self):
        r"""SPDeduction
        :rtype: str
        """
        return self._SPDeduction

    @SPDeduction.setter
    def SPDeduction(self, SPDeduction):
        self._SPDeduction = SPDeduction

    @property
    def Currency(self):
        r"""Currency.
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def Tax(self):
        r"""Tax
        :rtype: str
        """
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def TaxRate(self):
        r"""tax rate
        :rtype: str
        """
        return self._TaxRate

    @TaxRate.setter
    def TaxRate(self, TaxRate):
        self._TaxRate = TaxRate

    @property
    def CostBeforeTax(self):
        r"""CostBeforeTax
        :rtype: str
        """
        return self._CostBeforeTax

    @CostBeforeTax.setter
    def CostBeforeTax(self, CostBeforeTax):
        self._CostBeforeTax = CostBeforeTax

    @property
    def AmountBeforeTax(self):
        r"""AmountBeforeTax
        :rtype: str
        """
        return self._AmountBeforeTax

    @AmountBeforeTax.setter
    def AmountBeforeTax(self, AmountBeforeTax):
        self._AmountBeforeTax = AmountBeforeTax

    @property
    def BillMonth(self):
        r"""Billing month
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth


    def _deserialize(self, params):
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._TreeNodeUniqKeyName = params.get("TreeNodeUniqKeyName")
        self._BillDate = params.get("BillDate")
        self._PayerUin = params.get("PayerUin")
        self._OwnerUin = params.get("OwnerUin")
        self._OperateUin = params.get("OperateUin")
        self._PayMode = params.get("PayMode")
        self._PayModeName = params.get("PayModeName")
        self._ActionType = params.get("ActionType")
        self._ActionTypeName = params.get("ActionTypeName")
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._ProductCode = params.get("ProductCode")
        self._ProductCodeName = params.get("ProductCodeName")
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._InstanceType = params.get("InstanceType")
        self._InstanceTypeName = params.get("InstanceTypeName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = BillTag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._AllocationType = params.get("AllocationType")
        self._TotalCost = params.get("TotalCost")
        self._RiTimeSpan = params.get("RiTimeSpan")
        self._RiCost = params.get("RiCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._SplitItemId = params.get("SplitItemId")
        self._SplitItemName = params.get("SplitItemName")
        self._FeeBeginTime = params.get("FeeBeginTime")
        self._FeeEndTime = params.get("FeeEndTime")
        self._SPCost = params.get("SPCost")
        self._RegionType = params.get("RegionType")
        self._RegionTypeName = params.get("RegionTypeName")
        self._ComponentConfig = params.get("ComponentConfig")
        self._SPDeduction = params.get("SPDeduction")
        self._Currency = params.get("Currency")
        self._Tax = params.get("Tax")
        self._TaxRate = params.get("TaxRate")
        self._CostBeforeTax = params.get("CostBeforeTax")
        self._AmountBeforeTax = params.get("AmountBeforeTax")
        self._BillMonth = params.get("BillMonth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationTree(AbstractModel):
    r"""Cost allocation tree.

    """

    def __init__(self):
        r"""
        :param _Id: ID of a cost allocation unit.
        :type Id: int
        :param _Name: Cost allocation unit name.
        :type Name: str
        :param _TreeNodeUniqKey: Unique identifier of a cost allocation unit
        :type TreeNodeUniqKey: str
        :param _Children: Subtree.
        :type Children: list of AllocationTree
        """
        self._Id = None
        self._Name = None
        self._TreeNodeUniqKey = None
        self._Children = None

    @property
    def Id(self):
        r"""ID of a cost allocation unit.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""Cost allocation unit name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TreeNodeUniqKey(self):
        r"""Unique identifier of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def Children(self):
        r"""Subtree.
        :rtype: list of AllocationTree
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = AllocationTree()
                obj._deserialize(item)
                self._Children.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationTreeNode(AbstractModel):
    r"""Information of the current allocation unit

    """

    def __init__(self):
        r"""
        :param _TreeNodeUniqKey: Unique identifier of a cost allocation unit
        :type TreeNodeUniqKey: str
        :param _TreeNodeUniqKeyName: Name of a cost allocation unit
        :type TreeNodeUniqKeyName: str
        """
        self._TreeNodeUniqKey = None
        self._TreeNodeUniqKeyName = None

    @property
    def TreeNodeUniqKey(self):
        r"""Unique identifier of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def TreeNodeUniqKeyName(self):
        r"""Name of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKeyName

    @TreeNodeUniqKeyName.setter
    def TreeNodeUniqKeyName(self, TreeNodeUniqKeyName):
        self._TreeNodeUniqKeyName = TreeNodeUniqKeyName


    def _deserialize(self, params):
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._TreeNodeUniqKeyName = params.get("TreeNodeUniqKeyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationUnit(AbstractModel):
    r"""Specifies the ID and name of a cost allocation unit.

    """

    def __init__(self):
        r"""
        :param _NodeId: Cost allocation unit ID.
        :type NodeId: int
        :param _TreeNodeUniqKeyName: Specifies the name of a cost allocation rule.
        :type TreeNodeUniqKeyName: str
        """
        self._NodeId = None
        self._TreeNodeUniqKeyName = None

    @property
    def NodeId(self):
        r"""Cost allocation unit ID.
        :rtype: int
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def TreeNodeUniqKeyName(self):
        r"""Specifies the name of a cost allocation rule.
        :rtype: str
        """
        return self._TreeNodeUniqKeyName

    @TreeNodeUniqKeyName.setter
    def TreeNodeUniqKeyName(self, TreeNodeUniqKeyName):
        self._TreeNodeUniqKeyName = TreeNodeUniqKeyName


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._TreeNodeUniqKeyName = params.get("TreeNodeUniqKeyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseActionTypeDetail(AbstractModel):
    r"""Cost analysis transaction type complex type

    """

    def __init__(self):
        r"""
        :param _ActionType: Transaction type code
        :type ActionType: str
        :param _ActionTypeName: Transaction type Name
        :type ActionTypeName: str
        """
        self._ActionType = None
        self._ActionTypeName = None

    @property
    def ActionType(self):
        r"""Transaction type code
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        r"""Transaction type Name
        :rtype: str
        """
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
    r"""Cost analysis amount return data model

    """

    def __init__(self):
        r"""
        :param _Key: Fee type
        :type Key: str
        :param _Display: Indicates whether to display
        :type Display: int
        """
        self._Key = None
        self._Display = None

    @property
    def Key(self):
        r"""Fee type
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Display(self):
        r"""Indicates whether to display
        :rtype: int
        """
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
    r"""Cost analysis product return complex type

    """

    def __init__(self):
        r"""
        :param _BusinessCode: Product code
        :type BusinessCode: str
        :param _BusinessCodeName: Product name
        :type BusinessCodeName: str
        """
        self._BusinessCode = None
        self._BusinessCodeName = None

    @property
    def BusinessCode(self):
        r"""Product code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        r"""Product name
        :rtype: str
        """
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
    r"""Cost analysis filter box complex type

    """

    def __init__(self):
        r"""
        :param _Business: product
        :type Business: list of AnalyseBusinessDetail
        :param _Project: Project
        :type Project: list of AnalyseProjectDetail
        :param _Region: Region.
        :type Region: list of AnalyseRegionDetail
        :param _PayMode: Billing mode.
        :type PayMode: list of AnalysePayModeDetail
        :param _ActionType: Transaction type
        :type ActionType: list of AnalyseActionTypeDetail
        :param _Zone: Availability zone
        :type Zone: list of AnalyseZoneDetail
        :param _OwnerUin: Resource owner Uin
        :type OwnerUin: list of AnalyseOwnerUinDetail
        :param _Amount: Fee type
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
        r"""product
        :rtype: list of AnalyseBusinessDetail
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Project(self):
        r"""Project
        :rtype: list of AnalyseProjectDetail
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Region(self):
        r"""Region.
        :rtype: list of AnalyseRegionDetail
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PayMode(self):
        r"""Billing mode.
        :rtype: list of AnalysePayModeDetail
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ActionType(self):
        r"""Transaction type
        :rtype: list of AnalyseActionTypeDetail
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def Zone(self):
        r"""Availability zone
        :rtype: list of AnalyseZoneDetail
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def OwnerUin(self):
        r"""Resource owner Uin
        :rtype: list of AnalyseOwnerUinDetail
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Amount(self):
        r"""Fee type
        :rtype: list of AnalyseAmountDetail
        """
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
    r"""Cost analysis query conditions

    """

    def __init__(self):
        r"""
        :param _BusinessCodes: Product name code
        :type BusinessCodes: str
        :param _ProductCodes: Subproduct name code
        :type ProductCodes: str
        :param _ComponentCode: Component type code
        :type ComponentCode: str
        :param _ZoneIds: Availability zone ID: The availability zone ID where the resource is located.
        :type ZoneIds: str
        :param _RegionIds: Region ID: Resource region ID
        :type RegionIds: str
        :param _ProjectIds: Project ID: Project ID of the resource
        :type ProjectIds: str
        :param _PayModes: Billing mode prePay (monthly subscription)/postPay (pay-as-you-go billing)
        :type PayModes: str
        :param _ActionTypes: Transaction type. Query transaction type (please use transaction type code as input parameter).
        :type ActionTypes: str
        :param _Tags: Cost allocation tag key
        :type Tags: str
        :param _FeeType: Fee type. Query fee type (please use fee type code input parameter). The input parameter enumeration is as follows:
cashPayAmount: Cash 
incentivePayAmount: Bonus 
voucherPayAmount: Coupon 
tax: tax. 
costBeforeTax: pre-tax price
        :type FeeType: str
        :param _PayerUins: User UIN for querying cost analysis data
        :type PayerUins: str
        :param _OwnerUins: User UIN for using resources
        :type OwnerUins: str
        :param _ConsumptionTypes: Consumption type. Query consumption type (please use consumption type code input parameter).
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
        r"""Product name code
        :rtype: str
        """
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def ProductCodes(self):
        r"""Subproduct name code
        :rtype: str
        """
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes

    @property
    def ComponentCode(self):
        r"""Component type code
        :rtype: str
        """
        return self._ComponentCode

    @ComponentCode.setter
    def ComponentCode(self, ComponentCode):
        self._ComponentCode = ComponentCode

    @property
    def ZoneIds(self):
        r"""Availability zone ID: The availability zone ID where the resource is located.
        :rtype: str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def RegionIds(self):
        r"""Region ID: Resource region ID
        :rtype: str
        """
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def ProjectIds(self):
        r"""Project ID: Project ID of the resource
        :rtype: str
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def PayModes(self):
        r"""Billing mode prePay (monthly subscription)/postPay (pay-as-you-go billing)
        :rtype: str
        """
        return self._PayModes

    @PayModes.setter
    def PayModes(self, PayModes):
        self._PayModes = PayModes

    @property
    def ActionTypes(self):
        r"""Transaction type. Query transaction type (please use transaction type code as input parameter).
        :rtype: str
        """
        return self._ActionTypes

    @ActionTypes.setter
    def ActionTypes(self, ActionTypes):
        self._ActionTypes = ActionTypes

    @property
    def Tags(self):
        r"""Cost allocation tag key
        :rtype: str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def FeeType(self):
        r"""Fee type. Query fee type (please use fee type code input parameter). The input parameter enumeration is as follows:
cashPayAmount: Cash 
incentivePayAmount: Bonus 
voucherPayAmount: Coupon 
tax: tax. 
costBeforeTax: pre-tax price
        :rtype: str
        """
        return self._FeeType

    @FeeType.setter
    def FeeType(self, FeeType):
        self._FeeType = FeeType

    @property
    def PayerUins(self):
        r"""User UIN for querying cost analysis data
        :rtype: str
        """
        return self._PayerUins

    @PayerUins.setter
    def PayerUins(self, PayerUins):
        self._PayerUins = PayerUins

    @property
    def OwnerUins(self):
        r"""User UIN for using resources
        :rtype: str
        """
        return self._OwnerUins

    @OwnerUins.setter
    def OwnerUins(self, OwnerUins):
        self._OwnerUins = OwnerUins

    @property
    def ConsumptionTypes(self):
        r"""Consumption type. Query consumption type (please use consumption type code input parameter).
        :rtype: str
        """
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
    r"""Cost analysis data complex type

    """

    def __init__(self):
        r"""
        :param _Name: Time
        :type Name: str
        :param _Total: Amount
        :type Total: str
        :param _TimeDetail: Date Detail Amount
        :type TimeDetail: list of AnalyseTimeDetail
        """
        self._Name = None
        self._Total = None
        self._TimeDetail = None

    @property
    def Name(self):
        r"""Time
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Total(self):
        r"""Amount
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TimeDetail(self):
        r"""Date Detail Amount
        :rtype: list of AnalyseTimeDetail
        """
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
    r"""Cost analysis header data complex type

    """

    def __init__(self):
        r"""
        :param _HeadDetail: Header date
        :type HeadDetail: list of AnalyseHeaderTimeDetail
        :param _Name: Time
        :type Name: str
        :param _Total: total
        :type Total: str
        """
        self._HeadDetail = None
        self._Name = None
        self._Total = None

    @property
    def HeadDetail(self):
        r"""Header date
        :rtype: list of AnalyseHeaderTimeDetail
        """
        return self._HeadDetail

    @HeadDetail.setter
    def HeadDetail(self, HeadDetail):
        self._HeadDetail = HeadDetail

    @property
    def Name(self):
        r"""Time
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Total(self):
        r"""total
        :rtype: str
        """
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
    r"""Cost analysis header data

    """

    def __init__(self):
        r"""
        :param _Name: Date
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        r"""Date
        :rtype: str
        """
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
    r"""Cost analysis user UIN complex type

    """

    def __init__(self):
        r"""
        :param _OwnerUin: User uin
        :type OwnerUin: str
        """
        self._OwnerUin = None

    @property
    def OwnerUin(self):
        r"""User uin
        :rtype: str
        """
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
    r"""Cost analysis payment method complex type

    """

    def __init__(self):
        r"""
        :param _PayMode: Billing mode code
        :type PayMode: str
        :param _PayModeName: Billing mode Name
        :type PayModeName: str
        """
        self._PayMode = None
        self._PayModeName = None

    @property
    def PayMode(self):
        r"""Billing mode code
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        r"""Billing mode Name
        :rtype: str
        """
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
    r"""Cost analysis project return complex type

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: str
        :param _ProjectName: default project
        :type ProjectName: str
        """
        self._ProjectId = None
        self._ProjectName = None

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""default project
        :rtype: str
        """
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
    r"""Cost analysis region return complex type

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID.
        :type RegionId: str
        :param _RegionName: Region name
        :type RegionName: str
        """
        self._RegionId = None
        self._RegionName = None

    @property
    def RegionId(self):
        r"""Region ID.
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        r"""Region name
        :rtype: str
        """
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
    r"""Cost analysis return value complex type

    """

    def __init__(self):
        r"""
        :param _Time: Date
        :type Time: str
        :param _Money: Amount
        :type Money: str
        """
        self._Time = None
        self._Money = None

    @property
    def Time(self):
        r"""Date
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Money(self):
        r"""Amount
        :rtype: str
        """
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
    r"""Cost analysis availability zone complex type

    """

    def __init__(self):
        r"""
        :param _ZoneId: AZ ID.
        :type ZoneId: str
        :param _ZoneName: Available zone Name
        :type ZoneName: str
        """
        self._ZoneId = None
        self._ZoneName = None

    @property
    def ZoneId(self):
        r"""AZ ID.
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        r"""Available zone Name
        :rtype: str
        """
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
    r"""The products that are applicable.

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
        r"""Valid values: `all products` or names of the applicable products (string). Multiple names are separated by commas.
        :rtype: str
        """
        return self._GoodsName

    @GoodsName.setter
    def GoodsName(self, GoodsName):
        self._GoodsName = GoodsName

    @property
    def PayMode(self):
        r"""Valid values: `postPay`: pay-as-you-go; `prePay`: prepaid; `riPay`: reserved instance; empty or `*`: all. If `GoodsName` contains multiple product names and `PayMode` is `*`, it indicates that the voucher can be used in all billing modes for each of the products.
        :rtype: str
        """
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
        


class BillActionType(AbstractModel):
    r"""Transaction type filter list

    """

    def __init__(self):
        r"""
        :param _ActionType: Transaction type code
        :type ActionType: str
        :param _ActionTypeName: Transaction type: Detailed transaction type
        :type ActionTypeName: str
        """
        self._ActionType = None
        self._ActionTypeName = None

    @property
    def ActionType(self):
        r"""Transaction type code
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        r"""Transaction type: Detailed transaction type
        :rtype: str
        """
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
        


class BillBusiness(AbstractModel):
    r"""Product filter list

    """

    def __init__(self):
        r"""
        :param _BusinessCode: Product code


        :type BusinessCode: str
        :param _BusinessCodeName: Product name: Various cloud products purchased by users
        :type BusinessCodeName: str
        """
        self._BusinessCode = None
        self._BusinessCodeName = None

    @property
    def BusinessCode(self):
        r"""Product code


        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        r"""Product name: Various cloud products purchased by users
        :rtype: str
        """
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
        


class BillBusinessLink(AbstractModel):
    r"""Product cascade filter value

    """

    def __init__(self):
        r"""
        :param _BusinessCode: Product code
        :type BusinessCode: str
        :param _BusinessCodeName: Product name
        :type BusinessCodeName: str
        :param _Children: Subproduct
        :type Children: list of BillProductLink
        """
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._Children = None

    @property
    def BusinessCode(self):
        r"""Product code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        r"""Product name
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def Children(self):
        r"""Subproduct
        :rtype: list of BillProductLink
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children


    def _deserialize(self, params):
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = BillProductLink()
                obj._deserialize(item)
                self._Children.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillComponent(AbstractModel):
    r"""Component type filter list

    """

    def __init__(self):
        r"""
        :param _ComponentCode: Component type code
        :type ComponentCode: str
        :param _ComponentCodeName: Component type: The major component category corresponding to the product or service purchased by the user
        :type ComponentCodeName: str
        """
        self._ComponentCode = None
        self._ComponentCodeName = None

    @property
    def ComponentCode(self):
        r"""Component type code
        :rtype: str
        """
        return self._ComponentCode

    @ComponentCode.setter
    def ComponentCode(self, ComponentCode):
        self._ComponentCode = ComponentCode

    @property
    def ComponentCodeName(self):
        r"""Component type: The major component category corresponding to the product or service purchased by the user
        :rtype: str
        """
        return self._ComponentCodeName

    @ComponentCodeName.setter
    def ComponentCodeName(self, ComponentCodeName):
        self._ComponentCodeName = ComponentCodeName


    def _deserialize(self, params):
        self._ComponentCode = params.get("ComponentCode")
        self._ComponentCodeName = params.get("ComponentCodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDays(AbstractModel):
    r"""Date filter list

    """

    def __init__(self):
        r"""
        :param _BillDay: Date: Settlement date
        :type BillDay: str
        """
        self._BillDay = None

    @property
    def BillDay(self):
        r"""Date: Settlement date
        :rtype: str
        """
        return self._BillDay

    @BillDay.setter
    def BillDay(self, BillDay):
        self._BillDay = BillDay


    def _deserialize(self, params):
        self._BillDay = params.get("BillDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDetail(AbstractModel):
    r"""Bill details

    """

    def __init__(self):
        r"""
        :param _BusinessCodeName: Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :type BusinessCodeName: str
        :param _ProductCodeName: Subproduct name: The subcategory of a Tencent Cloud product purchased by the user, such as CVM Standard S1.
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
        :param _OrderId: Order ID: The sub-order number corresponding to the monthly subscription mode. In the postpaid billing model, the bill amount does not exist as an order concept, and this parameter can be ignored.

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
        :param _Tags: Tag information.
        :type Tags: list of BillTagInfo
        :param _BusinessCode: Product code
        :type BusinessCode: str
        :param _ProductCode: Subproduct code
        :type ProductCode: str
        :param _ActionType: Transaction type code
        :type ActionType: str
        :param _RegionId: Region ID
        :type RegionId: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _PriceInfo: Price attribute: Other attributes of the component that affect discount pricing besides unit price and duration
        :type PriceInfo: list of str
        :param _AssociatedOrder: Associated transaction document ID: Document ID associated with this transaction, such as a write-off order, the original order, a resettlement order, or the original purchase order number recorded in a refund order.
        :type AssociatedOrder: :class:`tencentcloud.billing.v20180709.models.BillDetailAssociatedOrder`
        :param _Formula: Calculation explanation: A detailed explanation to calculations of billing settlement for special transaction types, such as refund and configuration changes.
        :type Formula: str
        :param _FormulaUrl: Billing Rules: The detailed billing rules for each product shown in the portal explanation link
        :type FormulaUrl: str
        :param _BillDay: Billing day
        :type BillDay: str
        :param _BillMonth: Billing month
        :type BillMonth: str
        :param _Id: Billing record ID
        :type Id: str
        :param _RegionType: Domestic and international codes
        :type RegionType: str
        :param _RegionTypeName: Domestic and international: Resource region type (domestic, international)
        :type RegionTypeName: str
        :param _ReserveDetail: Remark attribute (instance configuration): Additional remark information, such as reserved instance type and transaction type for reserved instances, regional information of both ends for CCN products.
        :type ReserveDetail: str
        :param _DiscountObject: discount object
        :type DiscountObject: str
        :param _DiscountType: Offer type
        :type DiscountType: str
        :param _DiscountContent: discount content
        :type DiscountContent: str
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
        self._DiscountObject = None
        self._DiscountType = None
        self._DiscountContent = None

    @property
    def BusinessCodeName(self):
        r"""Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        r"""Subproduct name: The subcategory of a Tencent Cloud product purchased by the user, such as CVM Standard S1.
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        r"""Billing mode, which can be monthly subscription or pay-as-you-go.
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        r"""Project name: The project to which a resource belongs, which is user-designated. If a resource has not been assigned to a project, it will automatically belong to the default project.
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        r"""Region: The region to which a resource belongs, such as South China (Guangzhou).
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        r"""Availability zone: availability zone of a resource, e.g. Guangzhou Zone 3
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        r"""Instance ID: The object ID of a billed resource, such as a CVM instance ID. This object ID may vary due to various forms and contents of resources in different products.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        r"""Instance name: The resource name set by the user in the console. If it is not set, it will be empty by default.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        r"""Transaction type, which can be monthly subscription purchase, monthly subscription renewal, or pay-as-you-go deduction.
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        r"""Order ID: The sub-order number corresponding to the monthly subscription mode. In the postpaid billing model, the bill amount does not exist as an order concept, and this parameter can be ignored.

        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def BillId(self):
        r"""Transaction ID: The bill number for a deducted payment
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def PayTime(self):
        r"""Transaction time: The time at which a payment was deducted
        :rtype: str
        """
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def FeeBeginTime(self):
        r"""Usage start time: The time at which product or service usage starts
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        r"""Usage end time: The time at which product or service usage ends
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ComponentSet(self):
        r"""Component list
        :rtype: list of BillDetailComponent
        """
        return self._ComponentSet

    @ComponentSet.setter
    def ComponentSet(self, ComponentSet):
        self._ComponentSet = ComponentSet

    @property
    def PayerUin(self):
        r"""Payer account ID: The account ID of the payer, which is the unique identifier of a Tencent Cloud user.
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        r"""Owner account ID: The account ID of the actual resource user
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        r"""Operator account ID: The account or role ID of the operator who purchases or activates a resource
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def Tags(self):
        r"""Tag information.
        :rtype: list of BillTagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def BusinessCode(self):
        r"""Product code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProductCode(self):
        r"""Subproduct code
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ActionType(self):
        r"""Transaction type code
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def RegionId(self):
        r"""Region ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PriceInfo(self):
        r"""Price attribute: Other attributes of the component that affect discount pricing besides unit price and duration
        :rtype: list of str
        """
        return self._PriceInfo

    @PriceInfo.setter
    def PriceInfo(self, PriceInfo):
        self._PriceInfo = PriceInfo

    @property
    def AssociatedOrder(self):
        r"""Associated transaction document ID: Document ID associated with this transaction, such as a write-off order, the original order, a resettlement order, or the original purchase order number recorded in a refund order.
        :rtype: :class:`tencentcloud.billing.v20180709.models.BillDetailAssociatedOrder`
        """
        return self._AssociatedOrder

    @AssociatedOrder.setter
    def AssociatedOrder(self, AssociatedOrder):
        self._AssociatedOrder = AssociatedOrder

    @property
    def Formula(self):
        r"""Calculation explanation: A detailed explanation to calculations of billing settlement for special transaction types, such as refund and configuration changes.
        :rtype: str
        """
        return self._Formula

    @Formula.setter
    def Formula(self, Formula):
        self._Formula = Formula

    @property
    def FormulaUrl(self):
        r"""Billing Rules: The detailed billing rules for each product shown in the portal explanation link
        :rtype: str
        """
        return self._FormulaUrl

    @FormulaUrl.setter
    def FormulaUrl(self, FormulaUrl):
        self._FormulaUrl = FormulaUrl

    @property
    def BillDay(self):
        r"""Billing day
        :rtype: str
        """
        return self._BillDay

    @BillDay.setter
    def BillDay(self, BillDay):
        self._BillDay = BillDay

    @property
    def BillMonth(self):
        r"""Billing month
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def Id(self):
        r"""Billing record ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RegionType(self):
        r"""Domestic and international codes
        :rtype: str
        """
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def RegionTypeName(self):
        r"""Domestic and international: Resource region type (domestic, international)
        :rtype: str
        """
        return self._RegionTypeName

    @RegionTypeName.setter
    def RegionTypeName(self, RegionTypeName):
        self._RegionTypeName = RegionTypeName

    @property
    def ReserveDetail(self):
        r"""Remark attribute (instance configuration): Additional remark information, such as reserved instance type and transaction type for reserved instances, regional information of both ends for CCN products.
        :rtype: str
        """
        return self._ReserveDetail

    @ReserveDetail.setter
    def ReserveDetail(self, ReserveDetail):
        self._ReserveDetail = ReserveDetail

    @property
    def DiscountObject(self):
        r"""discount object
        :rtype: str
        """
        return self._DiscountObject

    @DiscountObject.setter
    def DiscountObject(self, DiscountObject):
        self._DiscountObject = DiscountObject

    @property
    def DiscountType(self):
        r"""Offer type
        :rtype: str
        """
        return self._DiscountType

    @DiscountType.setter
    def DiscountType(self, DiscountType):
        self._DiscountType = DiscountType

    @property
    def DiscountContent(self):
        r"""discount content
        :rtype: str
        """
        return self._DiscountContent

    @DiscountContent.setter
    def DiscountContent(self, DiscountContent):
        self._DiscountContent = DiscountContent


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
        self._DiscountObject = params.get("DiscountObject")
        self._DiscountType = params.get("DiscountType")
        self._DiscountContent = params.get("DiscountContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDetailAssociatedOrder(AbstractModel):
    r"""Information of the document associated with bill details

    """

    def __init__(self):
        r"""
        :param _PrepayPurchase: Newly purchased order
        :type PrepayPurchase: str
        :param _PrepayRenew: Renewal order
        :type PrepayRenew: str
        :param _PrepayModifyUp: Configuration upgrade order
        :type PrepayModifyUp: str
        :param _ReverseOrder: Write-off order
        :type ReverseOrder: str
        :param _NewOrder: Order after discount adjustment
        :type NewOrder: str
        :param _Original: Order before discount adjustment
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
        r"""Newly purchased order
        :rtype: str
        """
        return self._PrepayPurchase

    @PrepayPurchase.setter
    def PrepayPurchase(self, PrepayPurchase):
        self._PrepayPurchase = PrepayPurchase

    @property
    def PrepayRenew(self):
        r"""Renewal order
        :rtype: str
        """
        return self._PrepayRenew

    @PrepayRenew.setter
    def PrepayRenew(self, PrepayRenew):
        self._PrepayRenew = PrepayRenew

    @property
    def PrepayModifyUp(self):
        r"""Configuration upgrade order
        :rtype: str
        """
        return self._PrepayModifyUp

    @PrepayModifyUp.setter
    def PrepayModifyUp(self, PrepayModifyUp):
        self._PrepayModifyUp = PrepayModifyUp

    @property
    def ReverseOrder(self):
        r"""Write-off order
        :rtype: str
        """
        return self._ReverseOrder

    @ReverseOrder.setter
    def ReverseOrder(self, ReverseOrder):
        self._ReverseOrder = ReverseOrder

    @property
    def NewOrder(self):
        r"""Order after discount adjustment
        :rtype: str
        """
        return self._NewOrder

    @NewOrder.setter
    def NewOrder(self, NewOrder):
        self._NewOrder = NewOrder

    @property
    def Original(self):
        r"""Order before discount adjustment
        :rtype: str
        """
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
    r"""Information about components charged in the bill

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
        :param _RealTotalMeasure: Original usage/duration: The original usage of the component before deduction by resource packages.
        :type RealTotalMeasure: str
        :param _DeductedMeasure: Deduction of usage/duration (including resource packages): The amount of usage/duration deducted by resource packages
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
        :param _CashPayAmount: Cash credit: The amount paid from the user's cash account

        :type CashPayAmount: str
        :param _IncentivePayAmount: Free credit: The amount paid with the user's free credit

        :type IncentivePayAmount: str
        :param _TransferPayAmount: Royalty account expenditure: The amount paid through the royalty account
        :type TransferPayAmount: str
        :param _ItemCode: Component type code
        :type ItemCode: str
        :param _ComponentCode: Component name code
        :type ComponentCode: str
        :param _ContractPrice: Component unit price: Discounted unit price of the component. Component unit price = list price * discount.
        :type ContractPrice: str
        :param _InstanceType: Instance type: The type of an instance corresponding to the product service purchased, including resource packages, RI, SP, and spot instances. Normal instance display is not displayed by default.
        :type InstanceType: str
        :param _RiTimeSpan: RI deduction duration: The duration of use deducted by reserved instances for this product or service.
        :type RiTimeSpan: str
        :param _OriginalCostWithRI: Reserved Instance Deduction Component Original Price: The original price of a component deducted by reserved instances for this product or service
        :type OriginalCostWithRI: str
        :param _SPDeductionRate: Savings plan deduction rate: The discount rate for this component within the available balance limit of the savings plan
        :type SPDeductionRate: str
        :param _SPDeduction: Cost deduction by SP. This parameter has been deprecated. Note: This field may return null, indicating that no valid values can be obtained.
        :type SPDeduction: str
        :param _OriginalCostWithSP: Original Price of Savings Plan Deduction Component: Savings Plan Deduction from Original Price = Deduction Amount of Savings Plan Package / Savings Plan Deduction Rate
        :type OriginalCostWithSP: str
        :param _BlendedDiscount: Mixed discount rate: The final discount rate after integrating various discount deductions. Mixed Discount Rate = Discounted total price/Component original price.
        :type BlendedDiscount: str
        :param _ComponentConfig: Configuration description: Information on specification of resource configuration
        :type ComponentConfig: list of BillDetailComponentConfig
        :param _TaxRate: tax rate
        :type TaxRate: str
        :param _TaxAmount: Tax.
        :type TaxAmount: str
        :param _Currency: Currency.
        :type Currency: str
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
        self._TaxRate = None
        self._TaxAmount = None
        self._Currency = None

    @property
    def ComponentCodeName(self):
        r"""Component type: The component type of a product or service purchased, such as CVM instance components including CPU and memory.
        :rtype: str
        """
        return self._ComponentCodeName

    @ComponentCodeName.setter
    def ComponentCodeName(self, ComponentCodeName):
        self._ComponentCodeName = ComponentCodeName

    @property
    def ItemCodeName(self):
        r"""Component name: The specific component of a product or service purchased
        :rtype: str
        """
        return self._ItemCodeName

    @ItemCodeName.setter
    def ItemCodeName(self, ItemCodeName):
        self._ItemCodeName = ItemCodeName

    @property
    def SinglePrice(self):
        r"""Component list price: The listed unit price of a component. If a customer has applied for a fixed preferential price or contract price, this parameter will not be displayed by default.
        :rtype: str
        """
        return self._SinglePrice

    @SinglePrice.setter
    def SinglePrice(self, SinglePrice):
        self._SinglePrice = SinglePrice

    @property
    def SpecifiedPrice(self):
        warnings.warn("parameter `SpecifiedPrice` is deprecated", DeprecationWarning) 

        r"""Specified price of a component. This parameter has been deprecated.
        :rtype: str
        """
        return self._SpecifiedPrice

    @SpecifiedPrice.setter
    def SpecifiedPrice(self, SpecifiedPrice):
        warnings.warn("parameter `SpecifiedPrice` is deprecated", DeprecationWarning) 

        self._SpecifiedPrice = SpecifiedPrice

    @property
    def PriceUnit(self):
        r"""Component price measurement unit: The unit of measurement for a component price, which is composed of USD, usage unit, and duration unit.
        :rtype: str
        """
        return self._PriceUnit

    @PriceUnit.setter
    def PriceUnit(self, PriceUnit):
        self._PriceUnit = PriceUnit

    @property
    def UsedAmount(self):
        r"""Component usage: The actually settled usage of a component, which is "Raw usage - Deducted usage (including packages)".
        :rtype: str
        """
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

    @property
    def UsedAmountUnit(self):
        r"""Component usage unit: The unit of measurement for component usage
        :rtype: str
        """
        return self._UsedAmountUnit

    @UsedAmountUnit.setter
    def UsedAmountUnit(self, UsedAmountUnit):
        self._UsedAmountUnit = UsedAmountUnit

    @property
    def RealTotalMeasure(self):
        r"""Original usage/duration: The original usage of the component before deduction by resource packages.
        :rtype: str
        """
        return self._RealTotalMeasure

    @RealTotalMeasure.setter
    def RealTotalMeasure(self, RealTotalMeasure):
        self._RealTotalMeasure = RealTotalMeasure

    @property
    def DeductedMeasure(self):
        r"""Deduction of usage/duration (including resource packages): The amount of usage/duration deducted by resource packages
        :rtype: str
        """
        return self._DeductedMeasure

    @DeductedMeasure.setter
    def DeductedMeasure(self, DeductedMeasure):
        self._DeductedMeasure = DeductedMeasure

    @property
    def TimeSpan(self):
        r"""Usage duration: The resource usage duration
        :rtype: str
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnitName(self):
        r"""Duration unit: The unit of measurement for usage duration
        :rtype: str
        """
        return self._TimeUnitName

    @TimeUnitName.setter
    def TimeUnitName(self, TimeUnitName):
        self._TimeUnitName = TimeUnitName

    @property
    def Cost(self):
        r"""Original cost: The original cost of a resource, which is "List price x Usage x Usage duration". If a customer has applied for a fixed preferential price or contract price or is in a refund scenario, this parameter will not be displayed by default.
        :rtype: str
        """
        return self._Cost

    @Cost.setter
    def Cost(self, Cost):
        self._Cost = Cost

    @property
    def Discount(self):
        r"""Discount multiplier: The discount multiplier applied to the cost of the resource. If a customer has applied for a fixed preferential price or contract price or is in a refund scenario, this parameter will not be displayed by default.
        :rtype: str
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def ReduceType(self):
        r"""Offer type
        :rtype: str
        """
        return self._ReduceType

    @ReduceType.setter
    def ReduceType(self, ReduceType):
        self._ReduceType = ReduceType

    @property
    def RealCost(self):
        r"""Total amount after discount: Total amount after discount = (Original cost - RI deduction (cost) - SP deduction (cost)) x Discount multiplier
        :rtype: str
        """
        return self._RealCost

    @RealCost.setter
    def RealCost(self, RealCost):
        self._RealCost = RealCost

    @property
    def VoucherPayAmount(self):
        r"""Voucher payment: The voucher deduction amount
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def CashPayAmount(self):
        r"""Cash credit: The amount paid from the user's cash account

        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Free credit: The amount paid with the user's free credit

        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        r"""Royalty account expenditure: The amount paid through the royalty account
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def ItemCode(self):
        r"""Component type code
        :rtype: str
        """
        return self._ItemCode

    @ItemCode.setter
    def ItemCode(self, ItemCode):
        self._ItemCode = ItemCode

    @property
    def ComponentCode(self):
        r"""Component name code
        :rtype: str
        """
        return self._ComponentCode

    @ComponentCode.setter
    def ComponentCode(self, ComponentCode):
        self._ComponentCode = ComponentCode

    @property
    def ContractPrice(self):
        r"""Component unit price: Discounted unit price of the component. Component unit price = list price * discount.
        :rtype: str
        """
        return self._ContractPrice

    @ContractPrice.setter
    def ContractPrice(self, ContractPrice):
        self._ContractPrice = ContractPrice

    @property
    def InstanceType(self):
        r"""Instance type: The type of an instance corresponding to the product service purchased, including resource packages, RI, SP, and spot instances. Normal instance display is not displayed by default.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def RiTimeSpan(self):
        r"""RI deduction duration: The duration of use deducted by reserved instances for this product or service.
        :rtype: str
        """
        return self._RiTimeSpan

    @RiTimeSpan.setter
    def RiTimeSpan(self, RiTimeSpan):
        self._RiTimeSpan = RiTimeSpan

    @property
    def OriginalCostWithRI(self):
        r"""Reserved Instance Deduction Component Original Price: The original price of a component deducted by reserved instances for this product or service
        :rtype: str
        """
        return self._OriginalCostWithRI

    @OriginalCostWithRI.setter
    def OriginalCostWithRI(self, OriginalCostWithRI):
        self._OriginalCostWithRI = OriginalCostWithRI

    @property
    def SPDeductionRate(self):
        r"""Savings plan deduction rate: The discount rate for this component within the available balance limit of the savings plan
        :rtype: str
        """
        return self._SPDeductionRate

    @SPDeductionRate.setter
    def SPDeductionRate(self, SPDeductionRate):
        self._SPDeductionRate = SPDeductionRate

    @property
    def SPDeduction(self):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        r"""Cost deduction by SP. This parameter has been deprecated. Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SPDeduction

    @SPDeduction.setter
    def SPDeduction(self, SPDeduction):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        self._SPDeduction = SPDeduction

    @property
    def OriginalCostWithSP(self):
        r"""Original Price of Savings Plan Deduction Component: Savings Plan Deduction from Original Price = Deduction Amount of Savings Plan Package / Savings Plan Deduction Rate
        :rtype: str
        """
        return self._OriginalCostWithSP

    @OriginalCostWithSP.setter
    def OriginalCostWithSP(self, OriginalCostWithSP):
        self._OriginalCostWithSP = OriginalCostWithSP

    @property
    def BlendedDiscount(self):
        r"""Mixed discount rate: The final discount rate after integrating various discount deductions. Mixed Discount Rate = Discounted total price/Component original price.
        :rtype: str
        """
        return self._BlendedDiscount

    @BlendedDiscount.setter
    def BlendedDiscount(self, BlendedDiscount):
        self._BlendedDiscount = BlendedDiscount

    @property
    def ComponentConfig(self):
        r"""Configuration description: Information on specification of resource configuration
        :rtype: list of BillDetailComponentConfig
        """
        return self._ComponentConfig

    @ComponentConfig.setter
    def ComponentConfig(self, ComponentConfig):
        self._ComponentConfig = ComponentConfig

    @property
    def TaxRate(self):
        r"""tax rate
        :rtype: str
        """
        return self._TaxRate

    @TaxRate.setter
    def TaxRate(self, TaxRate):
        self._TaxRate = TaxRate

    @property
    def TaxAmount(self):
        r"""Tax.
        :rtype: str
        """
        return self._TaxAmount

    @TaxAmount.setter
    def TaxAmount(self, TaxAmount):
        self._TaxAmount = TaxAmount

    @property
    def Currency(self):
        r"""Currency.
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency


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
        self._TaxRate = params.get("TaxRate")
        self._TaxAmount = params.get("TaxAmount")
        self._Currency = params.get("Currency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDetailComponentConfig(AbstractModel):
    r"""Bill details configuration descriptions

    """

    def __init__(self):
        r"""
        :param _Name: Configuration description name
        :type Name: str
        :param _Value: Configuration description value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""Configuration description name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""Configuration description value
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
        


class BillDistributionResourceSummary(AbstractModel):
    r"""Summary objects for a reseller bill

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
        :param _TransferPayAmount: Royalty account expenditure: The amount paid through the royalty account
        :type TransferPayAmount: str
        :param _ExtendField3: Extended field 3: The extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField3: str
        :param _ExtendField4: Extended field 4: The extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField4: str
        :param _ExtendField5: Extended field 5: The extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField5: str
        :param _Tags: Tag information.
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
        :param _BillMonth: Billing month
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
        r"""Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        r"""Subproduct name: The subcategory of a Tencent Cloud product purchased by the user, such as CVM - Standard S1.
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        r"""Billing mode: The billing mode, which can be monthly subscription or pay-as-you-go.
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        r"""Project Name: The project to which a resource belongs, which is user-designated. If a resource has not been assigned to a project, it will automatically belong to the default project.
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        r"""Region: The region of a resource, e.g. South China (Guangzhou).
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        r"""Availability zone: The availability zone of a resource, e.g. Guangzhou Zone 3.
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        r"""Instance ID: The object ID of a billed resource, such as a CVM instance ID. This object ID may vary due to various forms and contents of resources in different products.	
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        r"""Instance name: The resource name set by the user in the console. If it is not set, it will be empty by default.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        r"""Transaction type, which can be monthly subscription purchase, monthly subscription renewal, pay-as-you-go deduction, etc.
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        r"""Order ID: The ID of a monthly subscription order.
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def PayTime(self):
        r"""Deduction time: The settlement cost deduction time.
        :rtype: str
        """
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def FeeBeginTime(self):
        r"""Usage start time: The time at which product or service usage starts.
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        r"""Usage end time: The time at which product or service usage ends.
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ConfigDesc(self):
        r"""Configuration description: The billable item names and usage of a resource, which are displayed on the resource bill only.
        :rtype: str
        """
        return self._ConfigDesc

    @ConfigDesc.setter
    def ConfigDesc(self, ConfigDesc):
        self._ConfigDesc = ConfigDesc

    @property
    def ExtendField1(self):
        r"""Extended Field 1: The extended attribute information of a product, which is displayed on the resource bill only.
        :rtype: str
        """
        return self._ExtendField1

    @ExtendField1.setter
    def ExtendField1(self, ExtendField1):
        self._ExtendField1 = ExtendField1

    @property
    def ExtendField2(self):
        r"""Extended field 2: The extended attribute information of a product, which is displayed on the resource bill only.
        :rtype: str
        """
        return self._ExtendField2

    @ExtendField2.setter
    def ExtendField2(self, ExtendField2):
        self._ExtendField2 = ExtendField2

    @property
    def TotalCost(self):
        r"""Original cost. The original cost of a component = Component price x Usage x Usage duration. If a customer has applied for a fixed preferential price or contract price or if a customer is in a refund scenario, this parameter will not be displayed by default.
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Discount(self):
        r"""Discount multiplier: The discount multiplier that applies to the component. If a customer has applied for a fixed preferential price or contract price or if a customer is in a refund scenario, this parameter will not be displayed by default.
        :rtype: str
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def ReduceType(self):
        r"""Offer type.
        :rtype: str
        """
        return self._ReduceType

    @ReduceType.setter
    def ReduceType(self, ReduceType):
        self._ReduceType = ReduceType

    @property
    def RealTotalCost(self):
        r"""Total amount after discount.
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def VoucherPayAmount(self):
        r"""Voucher payment: The voucher deduction amount.
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def CashPayAmount(self):
        r"""Cash credit payment: The amount paid through the user's cash account.
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Free credit payment: The amount paid with the user's free credit.
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        r"""Royalty account expenditure: The amount paid through the royalty account
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def ExtendField3(self):
        r"""Extended field 3: The extended attribute information of a product, which is displayed on the resource bill only.
        :rtype: str
        """
        return self._ExtendField3

    @ExtendField3.setter
    def ExtendField3(self, ExtendField3):
        self._ExtendField3 = ExtendField3

    @property
    def ExtendField4(self):
        r"""Extended field 4: The extended attribute information of a product, which is displayed on the resource bill only.
        :rtype: str
        """
        return self._ExtendField4

    @ExtendField4.setter
    def ExtendField4(self, ExtendField4):
        self._ExtendField4 = ExtendField4

    @property
    def ExtendField5(self):
        r"""Extended field 5: The extended attribute information of a product, which is displayed on the resource bill only.
        :rtype: str
        """
        return self._ExtendField5

    @ExtendField5.setter
    def ExtendField5(self, ExtendField5):
        self._ExtendField5 = ExtendField5

    @property
    def Tags(self):
        r"""Tag information.
        :rtype: list of BillTagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def OwnerUin(self):
        r"""Owner account ID: The account ID of the actual resource user.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        r"""Operator account ID: The account or role ID of the operator who purchases or activates a resource.
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def BusinessCode(self):
        r"""Product code.
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProductCode(self):
        r"""Subproduct code.
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def RegionId(self):
        r"""Region ID.
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def InstanceType(self):
        r"""Instance type: The instance type of a product or service purchased, which can be resource package, RI, SP, or spot instance. Other instance types are not displayed by default.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def OriginalCostWithRI(self):
        r"""RI deduction (cost): The amount deducted from the original cost by RI.	
        :rtype: str
        """
        return self._OriginalCostWithRI

    @OriginalCostWithRI.setter
    def OriginalCostWithRI(self, OriginalCostWithRI):
        self._OriginalCostWithRI = OriginalCostWithRI

    @property
    def SPDeduction(self):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        r"""Savings plan deduction (disused).
        :rtype: str
        """
        return self._SPDeduction

    @SPDeduction.setter
    def SPDeduction(self, SPDeduction):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        self._SPDeduction = SPDeduction

    @property
    def OriginalCostWithSP(self):
        r"""SP deduction (cost): The amount of cost deducted by a savings plan based on the component's original cost. SP deduction (cost) = Cost deduction by SP / SP deduction rate	
        :rtype: str
        """
        return self._OriginalCostWithSP

    @OriginalCostWithSP.setter
    def OriginalCostWithSP(self, OriginalCostWithSP):
        self._OriginalCostWithSP = OriginalCostWithSP

    @property
    def BillMonth(self):
        r"""Billing month
        :rtype: str
        """
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
        


class BillInstanceType(AbstractModel):
    r"""Instance type filter list

    """

    def __init__(self):
        r"""
        :param _InstanceType: Instance type code
        :type InstanceType: str
        :param _InstanceTypeName: Instance type: The type of an instance corresponding to the product service purchased, including resource packages, RI, SP, and spot instances. It is displayed as "-" by default for regular instances.
        :type InstanceTypeName: str
        """
        self._InstanceType = None
        self._InstanceTypeName = None

    @property
    def InstanceType(self):
        r"""Instance type code
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceTypeName(self):
        r"""Instance type: The type of an instance corresponding to the product service purchased, including resource packages, RI, SP, and spot instances. It is displayed as "-" by default for regular instances.
        :rtype: str
        """
        return self._InstanceTypeName

    @InstanceTypeName.setter
    def InstanceTypeName(self, InstanceTypeName):
        self._InstanceTypeName = InstanceTypeName


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._InstanceTypeName = params.get("InstanceTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillItem(AbstractModel):
    r"""Component name filter list

    """

    def __init__(self):
        r"""
        :param _ItemCode: Component name code
        :type ItemCode: str
        :param _ItemCodeName: Component name: The specific component of a product or service purchased by the user
        :type ItemCodeName: str
        """
        self._ItemCode = None
        self._ItemCodeName = None

    @property
    def ItemCode(self):
        r"""Component name code
        :rtype: str
        """
        return self._ItemCode

    @ItemCode.setter
    def ItemCode(self, ItemCode):
        self._ItemCode = ItemCode

    @property
    def ItemCodeName(self):
        r"""Component name: The specific component of a product or service purchased by the user
        :rtype: str
        """
        return self._ItemCodeName

    @ItemCodeName.setter
    def ItemCodeName(self, ItemCodeName):
        self._ItemCodeName = ItemCodeName


    def _deserialize(self, params):
        self._ItemCode = params.get("ItemCode")
        self._ItemCodeName = params.get("ItemCodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillOperateUin(AbstractModel):
    r"""Operator UIN filter list

    """

    def __init__(self):
        r"""
        :param _OperateUin: Operator account ID (the resource account ID or role ID opened by prepaid resource ordering or postpaid operation)
        :type OperateUin: str
        """
        self._OperateUin = None

    @property
    def OperateUin(self):
        r"""Operator account ID (the resource account ID or role ID opened by prepaid resource ordering or postpaid operation)
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin


    def _deserialize(self, params):
        self._OperateUin = params.get("OperateUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillOwnerUin(AbstractModel):
    r"""User UIN filter list

    """

    def __init__(self):
        r"""
        :param _OwnerUin: User UIN: Account ID of the actual resource user
        :type OwnerUin: str
        """
        self._OwnerUin = None

    @property
    def OwnerUin(self):
        r"""User UIN: Account ID of the actual resource user
        :rtype: str
        """
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
        


class BillPayMode(AbstractModel):
    r"""Billing mode filter list

    """

    def __init__(self):
        r"""
        :param _PayMode: Billing mode code
        :type PayMode: str
        :param _PayModeName: Billing mode: Resource billing mode, which can be monthly subscription or pay-as-you-go.
        :type PayModeName: str
        """
        self._PayMode = None
        self._PayModeName = None

    @property
    def PayMode(self):
        r"""Billing mode code
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        r"""Billing mode: Resource billing mode, which can be monthly subscription or pay-as-you-go.
        :rtype: str
        """
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
        


class BillProduct(AbstractModel):
    r"""Subproduct filter list

    """

    def __init__(self):
        r"""
        :param _ProductCode: Subproduct code
        :type ProductCode: str
        :param _ProductCodeName: Subproduct name: Product subdivision type purchased by the user
        :type ProductCodeName: str
        """
        self._ProductCode = None
        self._ProductCodeName = None

    @property
    def ProductCode(self):
        r"""Subproduct code
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductCodeName(self):
        r"""Subproduct name: Product subdivision type purchased by the user
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName


    def _deserialize(self, params):
        self._ProductCode = params.get("ProductCode")
        self._ProductCodeName = params.get("ProductCodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillProductLink(AbstractModel):
    r"""Subproduct filtering under cost allocation conditions

    """

    def __init__(self):
        r"""
        :param _ProductCode: Subproduct code
        :type ProductCode: str
        :param _ProductCodeName: Subproduct name
        :type ProductCodeName: str
        :param _Children: Component name
        :type Children: list of BillItem
        """
        self._ProductCode = None
        self._ProductCodeName = None
        self._Children = None

    @property
    def ProductCode(self):
        r"""Subproduct code
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductCodeName(self):
        r"""Subproduct name
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def Children(self):
        r"""Component name
        :rtype: list of BillItem
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children


    def _deserialize(self, params):
        self._ProductCode = params.get("ProductCode")
        self._ProductCodeName = params.get("ProductCodeName")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = BillItem()
                obj._deserialize(item)
                self._Children.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillProject(AbstractModel):
    r"""Project filter list

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _ProjectName: Project name: The Project to which a resource belongs, which is independently allocated by the user for the resource in the console. If a resource has not been allocated to an Project, it will be a default Project.
        :type ProjectName: str
        """
        self._ProjectId = None
        self._ProjectName = None

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""Project name: The Project to which a resource belongs, which is independently allocated by the user for the resource in the console. If a resource has not been allocated to an Project, it will be a default Project.
        :rtype: str
        """
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
        


class BillRegion(AbstractModel):
    r"""Region filter list

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID
        :type RegionId: int
        :param _RegionName: Region name: The region where the resource is located
        :type RegionName: str
        """
        self._RegionId = None
        self._RegionName = None

    @property
    def RegionId(self):
        r"""Region ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        r"""Region name: The region where the resource is located
        :rtype: str
        """
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
        


class BillResourceSummary(AbstractModel):
    r"""Information about resources charged in the bill

    """

    def __init__(self):
        r"""
        :param _BusinessCodeName: Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :type BusinessCodeName: str
        :param _ProductCodeName: Subproduct name: The subcategory of a Tencent Cloud product purchased by the user, such as CVM Computing C5t.
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
        :param _RealTotalCost: Total amount after discount (Including Tax):  = Total Amount After Discount (Excluding Tax) + TaxAmount
        :type RealTotalCost: str
        :param _VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param _CashPayAmount: Cash credit: The amount paid from the user's cash account

        :type CashPayAmount: str
        :param _IncentivePayAmount: Free credit: The amount paid with the user's free credit

        :type IncentivePayAmount: str
        :param _TransferPayAmount: Royalty account expenditure: The amount paid through the royalty account
        :type TransferPayAmount: str
        :param _ExtendField3: Extended field 3: Extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField3: str
        :param _ExtendField4: Extended field 4: Extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField4: str
        :param _ExtendField5: Extended field 5: Extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField5: str
        :param _Tags: Tag information.
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
        :param _BillMonth: Billing month
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
        r"""Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        r"""Subproduct name: The subcategory of a Tencent Cloud product purchased by the user, such as CVM Computing C5t.
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        r"""Billing mode, which can be monthly subscription or pay-as-you-go.
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        r"""Project name: The project to which a resource belongs, which is user-designated. If a resource has not been assigned to a project, it will automatically belong to the default project.
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        r"""Region: The region to which a resource belongs, such as South China (Guangzhou).
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        r"""Availability zone: The availability zone to which a resource belongs, such as Guangzhou Zone 3.
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        r"""Instance ID: The object ID of a billed resource, such as a CVM instance ID. This object ID may vary due to various forms and contents of resources in different products.	
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        r"""Instance name: The resource name set by the user in the console. If it is not set, it will be empty by default.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        r"""Transaction type, which can be monthly subscription purchase, monthly subscription renewal, or pay-as-you-go deduction.
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        r"""Order ID: The order number for a monthly subscription purchase
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def PayTime(self):
        r"""Transaction time: The time at which a payment was deducted
        :rtype: str
        """
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def FeeBeginTime(self):
        r"""Usage start time: The time at which product or service usage starts
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        r"""Usage end time: The time at which product or service usage ends
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ConfigDesc(self):
        r"""Configuration description: The billable item names and usage of a resource, which are displayed on the resource bill only.
        :rtype: str
        """
        return self._ConfigDesc

    @ConfigDesc.setter
    def ConfigDesc(self, ConfigDesc):
        self._ConfigDesc = ConfigDesc

    @property
    def ExtendField1(self):
        r"""Extended field 1: Extended attribute information of a product, which is displayed on the resource bill only.
        :rtype: str
        """
        return self._ExtendField1

    @ExtendField1.setter
    def ExtendField1(self, ExtendField1):
        self._ExtendField1 = ExtendField1

    @property
    def ExtendField2(self):
        r"""Extended field 2: Extended attribute information of a product, which is displayed on the resource bill only.
        :rtype: str
        """
        return self._ExtendField2

    @ExtendField2.setter
    def ExtendField2(self, ExtendField2):
        self._ExtendField2 = ExtendField2

    @property
    def TotalCost(self):
        r"""Original cost: The original cost of a resource, which is "List price x Usage x Usage duration". If a customer has applied for a fixed preferential price or contract price or applied for a refund, this parameter will not be displayed by default.
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Discount(self):
        r"""Discount multiplier: The discount multiplier applied to the cost of the resource. If a customer has applied for a fixed preferential price or contract price or applied for a refund, this parameter will not be displayed by default.
        :rtype: str
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def ReduceType(self):
        r"""Offer type
        :rtype: str
        """
        return self._ReduceType

    @ReduceType.setter
    def ReduceType(self, ReduceType):
        self._ReduceType = ReduceType

    @property
    def RealTotalCost(self):
        r"""Total amount after discount (Including Tax):  = Total Amount After Discount (Excluding Tax) + TaxAmount
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def VoucherPayAmount(self):
        r"""Voucher payment: The voucher deduction amount
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def CashPayAmount(self):
        r"""Cash credit: The amount paid from the user's cash account

        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Free credit: The amount paid with the user's free credit

        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        r"""Royalty account expenditure: The amount paid through the royalty account
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def ExtendField3(self):
        r"""Extended field 3: Extended attribute information of a product, which is displayed on the resource bill only.
        :rtype: str
        """
        return self._ExtendField3

    @ExtendField3.setter
    def ExtendField3(self, ExtendField3):
        self._ExtendField3 = ExtendField3

    @property
    def ExtendField4(self):
        r"""Extended field 4: Extended attribute information of a product, which is displayed on the resource bill only.
        :rtype: str
        """
        return self._ExtendField4

    @ExtendField4.setter
    def ExtendField4(self, ExtendField4):
        self._ExtendField4 = ExtendField4

    @property
    def ExtendField5(self):
        r"""Extended field 5: Extended attribute information of a product, which is displayed on the resource bill only.
        :rtype: str
        """
        return self._ExtendField5

    @ExtendField5.setter
    def ExtendField5(self, ExtendField5):
        self._ExtendField5 = ExtendField5

    @property
    def Tags(self):
        r"""Tag information.
        :rtype: list of BillTagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def PayerUin(self):
        r"""Payer account ID: The account ID of the payer, which is the unique identifier of a Tencent Cloud user.
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        r"""Owner account ID: The account ID of the actual resource user
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        r"""Operator account ID: The account or role ID of the operator who purchases or activates a resource.
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def BusinessCode(self):
        r"""Product code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProductCode(self):
        r"""Subproduct code
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def RegionId(self):
        r"""Region ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def InstanceType(self):
        r"""Instance type: The instance type of a product or service purchased, which can be resource package, RI, SP, or spot instance. Other instance types are not displayed by default.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def OriginalCostWithRI(self):
        r"""RI deduction (cost): The amount deducted from the original cost by RI	
        :rtype: str
        """
        return self._OriginalCostWithRI

    @OriginalCostWithRI.setter
    def OriginalCostWithRI(self, OriginalCostWithRI):
        self._OriginalCostWithRI = OriginalCostWithRI

    @property
    def SPDeduction(self):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        r"""Cost deduction by SP. This parameter has been deprecated.
        :rtype: str
        """
        return self._SPDeduction

    @SPDeduction.setter
    def SPDeduction(self, SPDeduction):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        self._SPDeduction = SPDeduction

    @property
    def OriginalCostWithSP(self):
        r"""SP deduction (cost): SP deduction (cost) = Cost deduction by SP / SP deduction rate	
        :rtype: str
        """
        return self._OriginalCostWithSP

    @OriginalCostWithSP.setter
    def OriginalCostWithSP(self, OriginalCostWithSP):
        self._OriginalCostWithSP = OriginalCostWithSP

    @property
    def BillMonth(self):
        r"""Billing month
        :rtype: str
        """
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
        


class BillTag(AbstractModel):
    r"""Tag filter list

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""Tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Tag value
        :rtype: str
        """
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
        


class BillTagInfo(AbstractModel):
    r"""Bill tag information.

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
        r"""Cost allocation tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Tag value
        :rtype: str
        """
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
        


class BillZoneId(AbstractModel):
    r"""Availability zone filter list

    """

    def __init__(self):
        r"""
        :param _ZoneId: AZ ID
        :type ZoneId: int
        :param _ZoneName: Availability zone: The availability zone where the resource is located.
        :type ZoneName: str
        """
        self._ZoneId = None
        self._ZoneName = None

    @property
    def ZoneId(self):
        r"""AZ ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        r"""Availability zone: The availability zone where the resource is located.
        :rtype: str
        """
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
        


class BusinessSummaryInfo(AbstractModel):
    r"""Detailed summary of products

    """

    def __init__(self):
        r"""
        :param _BusinessCode: Product code
        :type BusinessCode: str
        :param _BusinessCodeName: Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :type BusinessCodeName: str
        :param _TotalCost: Original price in CNY. The TotalCost field comes into effect after bill 3.0 (May 2021) and returns "-" before bill 3.0. In the current situation of contract price, the TotalCost field returns "-" if a price difference exists with the official website price.
        :type TotalCost: str
        :param _RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param _CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param _IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param _TransferPayAmount: Royalty account expenditure: The amount paid through the royalty account
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
        r"""Product code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        r"""Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def TotalCost(self):
        r"""Original price in CNY. The TotalCost field comes into effect after bill 3.0 (May 2021) and returns "-" before bill 3.0. In the current situation of contract price, the TotalCost field returns "-" if a price difference exists with the official website price.
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RealTotalCost(self):
        r"""Total amount after discount
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        r"""Cash credit: The amount paid from the user’s cash account
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Free credit: The amount paid with the user’s free credit
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        r"""Voucher payment: The voucher deduction amount
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        r"""Royalty account expenditure: The amount paid through the royalty account
        :rtype: str
        """
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
    r"""Summarize product details by product

    """

    def __init__(self):
        r"""
        :param _BusinessCode: Product code
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
        r"""Product code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        r"""Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def RealTotalCostRatio(self):
        r"""Cost ratio, to two decimal points
        :rtype: str
        """
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        r"""Total amount after discount
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        r"""Cash credit: The amount paid from the user’s cash account
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Free credit: The amount paid with the user’s free credit
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        r"""Voucher payment: The voucher deduction amount
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        r"""Commission credit: The amount paid with the user’s commission credit.
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def BillMonth(self):
        r"""Billing month, e.g. `2019-08`
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def TotalCost(self):
        r"""The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :rtype: str
        """
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
    r"""Summarize total cost by product

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
        r"""Total amount after discount

        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def VoucherPayAmount(self):
        r"""Voucher payment: The voucher deduction amount
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Free credit: The amount paid with the user’s free credit
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def CashPayAmount(self):
        r"""Cash credit: The amount paid from the user’s cash account
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def TransferPayAmount(self):
        r"""Commission credit: The amount paid with the user’s commission credit.
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def TotalCost(self):
        r"""The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :rtype: str
        """
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
    r"""Product filter criteria

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
        r"""Product name code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        r"""Product name
        :rtype: str
        """
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
    r"""Payment mode filter criteria

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
        r"""Payment mode
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        r"""Payment mode name
        :rtype: str
        """
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
    r"""Project filter criteria

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
        r"""Project ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""Project name
        :rtype: str
        """
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
    r"""Regional filter criteria

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
        r"""Region ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        r"""Region name
        :rtype: str
        """
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
    r"""Billing filter criteria object

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
        r"""Only supports two values: 6 and 12.
        :rtype: int
        """
        return self._TimeRange

    @TimeRange.setter
    def TimeRange(self, TimeRange):
        self._TimeRange = TimeRange

    @property
    def BusinessCode(self):
        r"""Product name code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RegionId(self):
        r"""Region ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def PayMode(self):
        r"""Payment mode. Options include prePay and postPay.
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResourceKeyword(self):
        r"""Resource keyword
        :rtype: str
        """
        return self._ResourceKeyword

    @ResourceKeyword.setter
    def ResourceKeyword(self, ResourceKeyword):
        self._ResourceKeyword = ResourceKeyword

    @property
    def BusinessCodes(self):
        r"""Product name code
        :rtype: list of str
        """
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def ProductCodes(self):
        r"""Subproduct name code
        :rtype: list of str
        """
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes

    @property
    def RegionIds(self):
        r"""Region ID
        :rtype: list of int
        """
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def ProjectIds(self):
        r"""Project ID
        :rtype: list of int
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def PayModes(self):
        r"""Payment mode. Options include prePay and postPay.
        :rtype: list of str
        """
        return self._PayModes

    @PayModes.setter
    def PayModes(self, PayModes):
        self._PayModes = PayModes

    @property
    def ActionTypes(self):
        r"""Transaction type
        :rtype: list of str
        """
        return self._ActionTypes

    @ActionTypes.setter
    def ActionTypes(self, ActionTypes):
        self._ActionTypes = ActionTypes

    @property
    def HideFreeCost(self):
        r"""Whether to hide zero-amount transactions
        :rtype: int
        """
        return self._HideFreeCost

    @HideFreeCost.setter
    def HideFreeCost(self, HideFreeCost):
        self._HideFreeCost = HideFreeCost

    @property
    def OrderByCost(self):
        r"""Sorting rule. Options include desc and asc.
        :rtype: str
        """
        return self._OrderByCost

    @OrderByCost.setter
    def OrderByCost(self, OrderByCost):
        self._OrderByCost = OrderByCost

    @property
    def BillIds(self):
        r"""Transaction ID
        :rtype: list of str
        """
        return self._BillIds

    @BillIds.setter
    def BillIds(self, BillIds):
        self._BillIds = BillIds

    @property
    def ComponentCodes(self):
        r"""Component code
        :rtype: list of str
        """
        return self._ComponentCodes

    @ComponentCodes.setter
    def ComponentCodes(self, ComponentCodes):
        self._ComponentCodes = ComponentCodes

    @property
    def FileIds(self):
        r"""File ID
        :rtype: list of str
        """
        return self._FileIds

    @FileIds.setter
    def FileIds(self, FileIds):
        self._FileIds = FileIds

    @property
    def FileTypes(self):
        r"""File type
        :rtype: list of str
        """
        return self._FileTypes

    @FileTypes.setter
    def FileTypes(self, FileTypes):
        self._FileTypes = FileTypes

    @property
    def Status(self):
        r"""Status
        :rtype: list of int non-negative
        """
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
    r"""Consumption details summarized by product

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
        :type CashPayAmount: str
        :param _IncentivePayAmount: Bonus
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: Voucher
        :type VoucherPayAmount: str
        :param _TransferPayAmount: Royalty amount
        :type TransferPayAmount: str
        :param _AmountBeforeTax: Cash payment (pre-tax)
        :type AmountBeforeTax: str
        :param _Tax: Tax
        :type Tax: str
        :param _RegionName: Region name (only shown in regional summary)
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
        self._AmountBeforeTax = None
        self._Tax = None
        self._RegionName = None

    @property
    def BusinessCode(self):
        r"""Product name code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        r"""Product name
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def RealTotalCost(self):
        r"""Discounted total price
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Trend(self):
        r"""Cost trend
        :rtype: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        """
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def CashPayAmount(self):
        r"""Cash
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Bonus
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        r"""Voucher
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        r"""Royalty amount
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def AmountBeforeTax(self):
        r"""Cash payment (pre-tax)
        :rtype: str
        """
        return self._AmountBeforeTax

    @AmountBeforeTax.setter
    def AmountBeforeTax(self, AmountBeforeTax):
        self._AmountBeforeTax = AmountBeforeTax

    @property
    def Tax(self):
        r"""Tax
        :rtype: str
        """
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def RegionName(self):
        r"""Region name (only shown in regional summary)
        :rtype: str
        """
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
        self._AmountBeforeTax = params.get("AmountBeforeTax")
        self._Tax = params.get("Tax")
        self._RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionProjectSummaryDataItem(AbstractModel):
    r"""Consumption details summarized by project

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
        :type CashPayAmount: str
        :param _IncentivePayAmount: Bonus
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: Voucher
        :type VoucherPayAmount: str
        :param _TransferPayAmount: Royalty amount
        :type TransferPayAmount: str
        :param _Tax: Tax
        :type Tax: str
        :param _AmountBeforeTax: Cash payment (pre-tax)
        :type AmountBeforeTax: str
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
        self._Tax = None
        self._AmountBeforeTax = None

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""Project name
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RealTotalCost(self):
        r"""Discounted total price
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Trend(self):
        r"""Trend
        :rtype: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        """
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def Business(self):
        r"""Product consumption details
        :rtype: list of ConsumptionBusinessSummaryDataItem
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def CashPayAmount(self):
        r"""Cash
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Bonus
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        r"""Voucher
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        r"""Royalty amount
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def Tax(self):
        r"""Tax
        :rtype: str
        """
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def AmountBeforeTax(self):
        r"""Cash payment (pre-tax)
        :rtype: str
        """
        return self._AmountBeforeTax

    @AmountBeforeTax.setter
    def AmountBeforeTax(self, AmountBeforeTax):
        self._AmountBeforeTax = AmountBeforeTax


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
        self._Tax = params.get("Tax")
        self._AmountBeforeTax = params.get("AmountBeforeTax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionRegionSummaryDataItem(AbstractModel):
    r"""Consumption details summarized by region

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
        :type CashPayAmount: str
        :param _VoucherPayAmount: Voucher
        :type VoucherPayAmount: str
        :param _IncentivePayAmount: Bonus
        :type IncentivePayAmount: str
        :param _TransferPayAmount: Royalty amount
        :type TransferPayAmount: str
        :param _Tax: Tax
        :type Tax: str
        :param _AmountBeforeTax: Cash payment (pre-tax)
        :type AmountBeforeTax: str
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
        self._Tax = None
        self._AmountBeforeTax = None

    @property
    def RegionId(self):
        r"""Region ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        r"""Region name
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RealTotalCost(self):
        r"""Discounted total price
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Trend(self):
        r"""Trend
        :rtype: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        """
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def Business(self):
        r"""Product consumption details
        :rtype: list of ConsumptionBusinessSummaryDataItem
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def CashPayAmount(self):
        r"""Cash
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def VoucherPayAmount(self):
        r"""Voucher
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Bonus
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        r"""Royalty amount
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def Tax(self):
        r"""Tax
        :rtype: str
        """
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def AmountBeforeTax(self):
        r"""Cash payment (pre-tax)
        :rtype: str
        """
        return self._AmountBeforeTax

    @AmountBeforeTax.setter
    def AmountBeforeTax(self, AmountBeforeTax):
        self._AmountBeforeTax = AmountBeforeTax


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
        self._Tax = params.get("Tax")
        self._AmountBeforeTax = params.get("AmountBeforeTax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionResourceSummaryConditionValue(AbstractModel):
    r"""Filter criteria of consumption details summarized by resource

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
        r"""Product list
        :rtype: list of ConditionBusiness
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Project(self):
        r"""Project list
        :rtype: list of ConditionProject
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Region(self):
        r"""Region list
        :rtype: list of ConditionRegion
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PayMode(self):
        r"""Payment mode list
        :rtype: list of ConditionPayMode
        """
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
    r"""Consumption details summarized by resource

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
        :param _RealCost: Original price
        :type RealCost: str
        :param _FeeBeginTime: Fee start time
        :type FeeBeginTime: str
        :param _FeeEndTime: End time of fees
        :type FeeEndTime: str
        :param _DayDiff: Days
        :type DayDiff: str
        :param _DailyTotalCost: Daily consumption
        :type DailyTotalCost: str
        :param _OrderId: Order ID
        :type OrderId: str
        :param _VoucherPayAmount: Voucher
        :type VoucherPayAmount: str
        :param _IncentivePayAmount: Bonus
        :type IncentivePayAmount: str
        :param _TransferPayAmount: Royalty amount
        :type TransferPayAmount: str
        :param _Tax: Tax
        :type Tax: str
        :param _TaxRate: tax rate
        :type TaxRate: str
        :param _AmountBeforeTax: Cash payment (pre-tax)
        :type AmountBeforeTax: str
        :param _PayerUin: Payer UIN: Account ID of the payer, which is the unique account identifier for the user in Tencent Cloud.
        :type PayerUin: str
        :param _OwnerUin: User UIN: Account ID of the actual resource user
        :type OwnerUin: str
        :param _OperateUin: Operator UIN: Operator account ID (ID of the operator who places orders for prepaid resources or activates postpaid resource account, or role ID).
        :type OperateUin: str
        :param _ProductCode: Subproduct code
        :type ProductCode: str
        :param _ProductCodeName: Subproduct name: Product subdivision type purchased by the user, such as Cloud Virtual Machine (CVM)-Standard Type S1
        :type ProductCodeName: str
        :param _RegionType: Region type
        :type RegionType: str
        :param _RegionTypeName: Region type name.
        :type RegionTypeName: str
        :param _Extend1: Extension Field 1
        :type Extend1: str
        :param _Extend2: Extension Field 2
        :type Extend2: str
        :param _Extend3: Extension Field 3
        :type Extend3: str
        :param _Extend4: Extension Field 4
        :type Extend4: str
        :param _Extend5: Extension Field 5
        :type Extend5: str
        :param _InstanceType: Instance type
        :type InstanceType: str
        :param _InstanceTypeName: Instance Type Name
        :type InstanceTypeName: str
        :param _PayTime: Deduction time: Deduction time
        :type PayTime: str
        :param _ZoneName: Availability zone: The availability zone where the resource is located, such as Guangzhou Zone 3.
        :type ZoneName: str
        :param _ComponentConfig: Describing Configurations
        :type ComponentConfig: str
        :param _Tags: Tag information.
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
        self._Tax = None
        self._TaxRate = None
        self._AmountBeforeTax = None
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
        r"""Resource ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        r"""Resource name
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def RealTotalCost(self):
        r"""Discounted total price
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        r"""Cash expenditure
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""Project name
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionId(self):
        r"""Region ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        r"""Region name
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def PayMode(self):
        r"""Payment mode
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        r"""Payment mode name
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def BusinessCode(self):
        r"""Product name code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        r"""Product name
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ConsumptionTypeName(self):
        r"""Consumption type
        :rtype: str
        """
        return self._ConsumptionTypeName

    @ConsumptionTypeName.setter
    def ConsumptionTypeName(self, ConsumptionTypeName):
        self._ConsumptionTypeName = ConsumptionTypeName

    @property
    def RealCost(self):
        r"""Original price
        :rtype: str
        """
        return self._RealCost

    @RealCost.setter
    def RealCost(self, RealCost):
        self._RealCost = RealCost

    @property
    def FeeBeginTime(self):
        r"""Fee start time
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        r"""End time of fees
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def DayDiff(self):
        r"""Days
        :rtype: str
        """
        return self._DayDiff

    @DayDiff.setter
    def DayDiff(self, DayDiff):
        self._DayDiff = DayDiff

    @property
    def DailyTotalCost(self):
        r"""Daily consumption
        :rtype: str
        """
        return self._DailyTotalCost

    @DailyTotalCost.setter
    def DailyTotalCost(self, DailyTotalCost):
        self._DailyTotalCost = DailyTotalCost

    @property
    def OrderId(self):
        r"""Order ID
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def VoucherPayAmount(self):
        r"""Voucher
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Bonus
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        r"""Royalty amount
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def Tax(self):
        r"""Tax
        :rtype: str
        """
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def TaxRate(self):
        r"""tax rate
        :rtype: str
        """
        return self._TaxRate

    @TaxRate.setter
    def TaxRate(self, TaxRate):
        self._TaxRate = TaxRate

    @property
    def AmountBeforeTax(self):
        r"""Cash payment (pre-tax)
        :rtype: str
        """
        return self._AmountBeforeTax

    @AmountBeforeTax.setter
    def AmountBeforeTax(self, AmountBeforeTax):
        self._AmountBeforeTax = AmountBeforeTax

    @property
    def PayerUin(self):
        r"""Payer UIN: Account ID of the payer, which is the unique account identifier for the user in Tencent Cloud.
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        r"""User UIN: Account ID of the actual resource user
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        r"""Operator UIN: Operator account ID (ID of the operator who places orders for prepaid resources or activates postpaid resource account, or role ID).
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def ProductCode(self):
        r"""Subproduct code
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductCodeName(self):
        r"""Subproduct name: Product subdivision type purchased by the user, such as Cloud Virtual Machine (CVM)-Standard Type S1
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def RegionType(self):
        r"""Region type
        :rtype: str
        """
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def RegionTypeName(self):
        r"""Region type name.
        :rtype: str
        """
        return self._RegionTypeName

    @RegionTypeName.setter
    def RegionTypeName(self, RegionTypeName):
        self._RegionTypeName = RegionTypeName

    @property
    def Extend1(self):
        r"""Extension Field 1
        :rtype: str
        """
        return self._Extend1

    @Extend1.setter
    def Extend1(self, Extend1):
        self._Extend1 = Extend1

    @property
    def Extend2(self):
        r"""Extension Field 2
        :rtype: str
        """
        return self._Extend2

    @Extend2.setter
    def Extend2(self, Extend2):
        self._Extend2 = Extend2

    @property
    def Extend3(self):
        r"""Extension Field 3
        :rtype: str
        """
        return self._Extend3

    @Extend3.setter
    def Extend3(self, Extend3):
        self._Extend3 = Extend3

    @property
    def Extend4(self):
        r"""Extension Field 4
        :rtype: str
        """
        return self._Extend4

    @Extend4.setter
    def Extend4(self, Extend4):
        self._Extend4 = Extend4

    @property
    def Extend5(self):
        r"""Extension Field 5
        :rtype: str
        """
        return self._Extend5

    @Extend5.setter
    def Extend5(self, Extend5):
        self._Extend5 = Extend5

    @property
    def InstanceType(self):
        r"""Instance type
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceTypeName(self):
        r"""Instance Type Name
        :rtype: str
        """
        return self._InstanceTypeName

    @InstanceTypeName.setter
    def InstanceTypeName(self, InstanceTypeName):
        self._InstanceTypeName = InstanceTypeName

    @property
    def PayTime(self):
        r"""Deduction time: Deduction time
        :rtype: str
        """
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def ZoneName(self):
        r"""Availability zone: The availability zone where the resource is located, such as Guangzhou Zone 3.
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ComponentConfig(self):
        r"""Describing Configurations
        :rtype: str
        """
        return self._ComponentConfig

    @ComponentConfig.setter
    def ComponentConfig(self, ComponentConfig):
        self._ComponentConfig = ComponentConfig

    @property
    def Tags(self):
        r"""Tag information.
        :rtype: str
        """
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
        self._Tax = params.get("Tax")
        self._TaxRate = params.get("TaxRate")
        self._AmountBeforeTax = params.get("AmountBeforeTax")
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
    r"""Consumption summary details

    """

    def __init__(self):
        r"""
        :param _RealTotalCost: Discounted total price
        :type RealTotalCost: str
        """
        self._RealTotalCost = None

    @property
    def RealTotalCost(self):
        r"""Discounted total price
        :rtype: str
        """
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
    r"""Consumption cost trend

    """

    def __init__(self):
        r"""
        :param _Type: Trend type, upward for rising, downward for falling, none for no change
        :type Type: str
        :param _Value: Trend value. The value of this field is null when Type is none.
        :type Value: str
        """
        self._Type = None
        self._Value = None

    @property
    def Type(self):
        r"""Trend type, upward for rising, downward for falling, none for no change
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        r"""Trend value. The value of this field is null when Type is none.
        :rtype: str
        """
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
    r"""Information about the data structure of the returned COS usage details

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
        r"""Bucket name
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def DosageBeginTime(self):
        r"""The start time of the usage
        :rtype: str
        """
        return self._DosageBeginTime

    @DosageBeginTime.setter
    def DosageBeginTime(self, DosageBeginTime):
        self._DosageBeginTime = DosageBeginTime

    @property
    def DosageEndTime(self):
        r"""The end time of the usage
        :rtype: str
        """
        return self._DosageEndTime

    @DosageEndTime.setter
    def DosageEndTime(self, DosageEndTime):
        self._DosageEndTime = DosageEndTime

    @property
    def SubProductCodeName(self):
        r"""Subproduct name
        :rtype: str
        """
        return self._SubProductCodeName

    @SubProductCodeName.setter
    def SubProductCodeName(self, SubProductCodeName):
        self._SubProductCodeName = SubProductCodeName

    @property
    def BillingItemCodeName(self):
        r"""Billable item name
        :rtype: str
        """
        return self._BillingItemCodeName

    @BillingItemCodeName.setter
    def BillingItemCodeName(self, BillingItemCodeName):
        self._BillingItemCodeName = BillingItemCodeName

    @property
    def DosageValue(self):
        r"""Usage
        :rtype: str
        """
        return self._DosageValue

    @DosageValue.setter
    def DosageValue(self, DosageValue):
        self._DosageValue = DosageValue

    @property
    def Unit(self):
        r"""Unit of the billable item
        :rtype: str
        """
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
    r"""Consumption component details

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
        :param _Tax: Tax
        :type Tax: str
        :param _TaxRate: tax rate
        :type TaxRate: str
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
        self._Tax = None
        self._TaxRate = None

    @property
    def ComponentCodeName(self):
        r"""Component type name
        :rtype: str
        """
        return self._ComponentCodeName

    @ComponentCodeName.setter
    def ComponentCodeName(self, ComponentCodeName):
        self._ComponentCodeName = ComponentCodeName

    @property
    def ItemCodeName(self):
        r"""Component name
        :rtype: str
        """
        return self._ItemCodeName

    @ItemCodeName.setter
    def ItemCodeName(self, ItemCodeName):
        self._ItemCodeName = ItemCodeName

    @property
    def SinglePrice(self):
        r"""List price
        :rtype: str
        """
        return self._SinglePrice

    @SinglePrice.setter
    def SinglePrice(self, SinglePrice):
        self._SinglePrice = SinglePrice

    @property
    def PriceUnit(self):
        r"""List price unit
        :rtype: str
        """
        return self._PriceUnit

    @PriceUnit.setter
    def PriceUnit(self, PriceUnit):
        self._PriceUnit = PriceUnit

    @property
    def UsedAmount(self):
        r"""Usage
        :rtype: str
        """
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

    @property
    def UsedAmountUnit(self):
        r"""Usage unit
        :rtype: str
        """
        return self._UsedAmountUnit

    @UsedAmountUnit.setter
    def UsedAmountUnit(self, UsedAmountUnit):
        self._UsedAmountUnit = UsedAmountUnit

    @property
    def Cost(self):
        r"""Original price
        :rtype: str
        """
        return self._Cost

    @Cost.setter
    def Cost(self, Cost):
        self._Cost = Cost

    @property
    def Discount(self):
        r"""Discount
        :rtype: str
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def RealCost(self):
        r"""Discounted price
        :rtype: str
        """
        return self._RealCost

    @RealCost.setter
    def RealCost(self, RealCost):
        self._RealCost = RealCost

    @property
    def VoucherPayAmount(self):
        r"""Voucher payment amount
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def CashPayAmount(self):
        r"""Cash payment amount
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Bonus payment amount
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def Tax(self):
        r"""Tax
        :rtype: str
        """
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def TaxRate(self):
        r"""tax rate
        :rtype: str
        """
        return self._TaxRate

    @TaxRate.setter
    def TaxRate(self, TaxRate):
        self._TaxRate = TaxRate


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
        self._Tax = params.get("Tax")
        self._TaxRate = params.get("TaxRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CostDetail(AbstractModel):
    r"""Consumption details data type

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
        :param _ActionTypeName: Type name
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
        :param _Tags: Tag information.	
        :type Tags: list of BillTagInfo
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
        self._Tags = None

    @property
    def PayerUin(self):
        r"""Payer UIN
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def BusinessCodeName(self):
        r"""Product name
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        r"""Subproduct name
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        r"""Billing mode name
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        r"""Project name
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        r"""Region Name
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        r"""Zone name
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        r"""Resource ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        r"""Resource name
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        r"""Type name
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        r"""Order ID
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def BillId(self):
        r"""Transaction ID
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def FeeBeginTime(self):
        r"""Start time of fees
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        r"""End time of fees
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ComponentSet(self):
        r"""Component details
        :rtype: list of CostComponentSet
        """
        return self._ComponentSet

    @ComponentSet.setter
    def ComponentSet(self, ComponentSet):
        self._ComponentSet = ComponentSet

    @property
    def ProductCode(self):
        r"""Subproduct name code
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def Tags(self):
        r"""Tag information.	
        :rtype: list of BillTagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


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
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = BillTagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAllocationRuleRequest(AbstractModel):
    r"""CreateAllocationRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleList: List of sharing rules
        :type RuleList: :class:`tencentcloud.billing.v20180709.models.AllocationRulesSummary`
        :param _Month: Month, the current month by default if not provided.
        :type Month: str
        """
        self._RuleList = None
        self._Month = None

    @property
    def RuleList(self):
        r"""List of sharing rules
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationRulesSummary`
        """
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def Month(self):
        r"""Month, the current month by default if not provided.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month


    def _deserialize(self, params):
        if params.get("RuleList") is not None:
            self._RuleList = AllocationRulesSummary()
            self._RuleList._deserialize(params.get("RuleList"))
        self._Month = params.get("Month")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAllocationRuleResponse(AbstractModel):
    r"""CreateAllocationRule response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Add new sharing rule ID.
        :type Id: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        r"""Add new sharing rule ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateAllocationTagRequest(AbstractModel):
    r"""CreateAllocationTag request structure.

    """

    def __init__(self):
        r"""
        :param _TagKey: Cost allocation tag key.
        :type TagKey: list of str
        """
        self._TagKey = None

    @property
    def TagKey(self):
        r"""Cost allocation tag key.
        :rtype: list of str
        """
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
    r"""CreateAllocationTag response structure.

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


class CreateAllocationUnitRequest(AbstractModel):
    r"""CreateAllocationUnit request structure.

    """

    def __init__(self):
        r"""
        :param _ParentId: New cost allocation unit parent node ID.
        :type ParentId: int
        :param _Name: Specifies the name of a newly-added cost allocation unit.
        :type Name: str
        :param _Month: Month, which is the current month by default if not provided.
        :type Month: str
        """
        self._ParentId = None
        self._Name = None
        self._Month = None

    @property
    def ParentId(self):
        r"""New cost allocation unit parent node ID.
        :rtype: int
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def Name(self):
        r"""Specifies the name of a newly-added cost allocation unit.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Month(self):
        r"""Month, which is the current month by default if not provided.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month


    def _deserialize(self, params):
        self._ParentId = params.get("ParentId")
        self._Name = params.get("Name")
        self._Month = params.get("Month")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAllocationUnitResponse(AbstractModel):
    r"""CreateAllocationUnit response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Specifies the ID of a newly-added cost allocation unit.
        :type Id: int
        :param _TreeNodeUniqKey: Unique identifier of a cost allocation unit
        :type TreeNodeUniqKey: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._TreeNodeUniqKey = None
        self._RequestId = None

    @property
    def Id(self):
        r"""Specifies the ID of a newly-added cost allocation unit.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TreeNodeUniqKey(self):
        r"""Unique identifier of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

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
        self._Id = params.get("Id")
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._RequestId = params.get("RequestId")


class CreateGatherRuleRequest(AbstractModel):
    r"""CreateGatherRule request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Cost allocation unit ID that the rule belongs to.
        :type Id: int
        :param _RuleList: Collection rule details.
        :type RuleList: :class:`tencentcloud.billing.v20180709.models.GatherRuleSummary`
        :param _Month: Month, which is the current month by default if not provided.
        :type Month: str
        """
        self._Id = None
        self._RuleList = None
        self._Month = None

    @property
    def Id(self):
        r"""Cost allocation unit ID that the rule belongs to.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleList(self):
        r"""Collection rule details.
        :rtype: :class:`tencentcloud.billing.v20180709.models.GatherRuleSummary`
        """
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def Month(self):
        r"""Month, which is the current month by default if not provided.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("RuleList") is not None:
            self._RuleList = GatherRuleSummary()
            self._RuleList._deserialize(params.get("RuleList"))
        self._Month = params.get("Month")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGatherRuleResponse(AbstractModel):
    r"""CreateGatherRule response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Collection  rule ID.
        :type Id: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        r"""Collection  rule ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateInstanceRequest(AbstractModel):
    r"""CreateInstance request structure.

    """

    def __init__(self):
        r"""
        :param _ClientToken: ClientToken is an unique, case-sensitive string generated by the client with no more than 64 ASCII characters. for example, ClientToken=123e4567-e89b-12d3-a456-42665544****.
        :type ClientToken: str
        :param _ProductCode: Product code.
        :type ProductCode: str
        :param _SubProductCode: Sub-product code.
        :type SubProductCode: str
        :param _RegionCode: Region code.
        :type RegionCode: str
        :param _ZoneCode: Availability zone code.
        :type ZoneCode: str
        :param _PayMode: Payment mode. Available values: PrePay: upfront charge.
        :type PayMode: str
        :param _Parameter: Product detailed information.
        :type Parameter: str
        :param _Quantity: Product quantity, default value is 1.
        :type Quantity: int
        :param _ProjectId: Project id, default value is 0.
        :type ProjectId: int
        :param _Period: Purchase duration, max number is 36, default value is 1.
        :type Period: int
        :param _PeriodUnit: Purchase duration unit. valid values: 
m: month,
y: year. 
default value is: m.
        :type PeriodUnit: str
        :param _RenewFlag: Auto-renewal flag. valid values: NOTIFY_AND_MANUAL_RENEW: manually renew, NOTIFY_AND_AUTO_RENEW: automatically renew, DISABLE_NOTIFY_AND_MANUAL_RENEW: renewal is disabled. 
default value is NOTIFY_AND_MANUAL_RENEW.
        :type RenewFlag: str
        """
        self._ClientToken = None
        self._ProductCode = None
        self._SubProductCode = None
        self._RegionCode = None
        self._ZoneCode = None
        self._PayMode = None
        self._Parameter = None
        self._Quantity = None
        self._ProjectId = None
        self._Period = None
        self._PeriodUnit = None
        self._RenewFlag = None

    @property
    def ClientToken(self):
        r"""ClientToken is an unique, case-sensitive string generated by the client with no more than 64 ASCII characters. for example, ClientToken=123e4567-e89b-12d3-a456-42665544****.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ProductCode(self):
        r"""Product code.
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def SubProductCode(self):
        r"""Sub-product code.
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def RegionCode(self):
        r"""Region code.
        :rtype: str
        """
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode

    @property
    def ZoneCode(self):
        r"""Availability zone code.
        :rtype: str
        """
        return self._ZoneCode

    @ZoneCode.setter
    def ZoneCode(self, ZoneCode):
        self._ZoneCode = ZoneCode

    @property
    def PayMode(self):
        r"""Payment mode. Available values: PrePay: upfront charge.
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Parameter(self):
        r"""Product detailed information.
        :rtype: str
        """
        return self._Parameter

    @Parameter.setter
    def Parameter(self, Parameter):
        self._Parameter = Parameter

    @property
    def Quantity(self):
        r"""Product quantity, default value is 1.
        :rtype: int
        """
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def ProjectId(self):
        r"""Project id, default value is 0.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Period(self):
        r"""Purchase duration, max number is 36, default value is 1.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def PeriodUnit(self):
        r"""Purchase duration unit. valid values: 
m: month,
y: year. 
default value is: m.
        :rtype: str
        """
        return self._PeriodUnit

    @PeriodUnit.setter
    def PeriodUnit(self, PeriodUnit):
        self._PeriodUnit = PeriodUnit

    @property
    def RenewFlag(self):
        r"""Auto-renewal flag. valid values: NOTIFY_AND_MANUAL_RENEW: manually renew, NOTIFY_AND_AUTO_RENEW: automatically renew, DISABLE_NOTIFY_AND_MANUAL_RENEW: renewal is disabled. 
default value is NOTIFY_AND_MANUAL_RENEW.
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._ClientToken = params.get("ClientToken")
        self._ProductCode = params.get("ProductCode")
        self._SubProductCode = params.get("SubProductCode")
        self._RegionCode = params.get("RegionCode")
        self._ZoneCode = params.get("ZoneCode")
        self._PayMode = params.get("PayMode")
        self._Parameter = params.get("Parameter")
        self._Quantity = params.get("Quantity")
        self._ProjectId = params.get("ProjectId")
        self._Period = params.get("Period")
        self._PeriodUnit = params.get("PeriodUnit")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    r"""CreateInstance response structure.

    """

    def __init__(self):
        r"""
        :param _OrderId: Order ID
        :type OrderId: str
        :param _InstanceIdList: Instance id list. Empty list will be returned once product delivery is delayed. 
        :type InstanceIdList: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OrderId = None
        self._InstanceIdList = None
        self._RequestId = None

    @property
    def OrderId(self):
        r"""Order ID
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def InstanceIdList(self):
        r"""Instance id list. Empty list will be returned once product delivery is delayed. 
        :rtype: list of str
        """
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

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
        self._OrderId = params.get("OrderId")
        self._InstanceIdList = params.get("InstanceIdList")
        self._RequestId = params.get("RequestId")


class Deal(AbstractModel):
    r"""Order data object

    """

    def __init__(self):
        r"""
        :param _OrderId: Order ID.
        :type OrderId: str
        :param _Status: The status of the order. 1: unpaid; 2: paid; 3: shipping; 4: shipped; 5: shipment failed; 6: refunded; 7: closed case; 8: order expired; 9: order invalidated; 10: product invalidated; 11: third-party payment refused; 12: payment in process
        :type Status: int
        :param _Payer: Payer
        :type Payer: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _Creator: Creator
        :type Creator: str
        :param _RealTotalCost: Actual payment amount (pent)
        :type RealTotalCost: int
        :param _VoucherDecline: Voucher offset amount (pent)
        :type VoucherDecline: int
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _GoodsCategoryId: Product category ID
        :type GoodsCategoryId: int
        :param _ProductInfo: Product details
        :type ProductInfo: list of ProductInfo
        :param _TimeSpan: Duration
        :type TimeSpan: float
        :param _TimeUnit: Time unit
        :type TimeUnit: str
        :param _Currency: Currency unit
        :type Currency: str
        :param _Policy: Discount rate
        :type Policy: float
        :param _Price: Unit price (cents)
        :type Price: float
        :param _TotalCost: Original price (cents)
        :type TotalCost: float
        :param _ProductCode: Product code
        :type ProductCode: str
        :param _SubProductCode: Subproduct code
        :type SubProductCode: str
        :param _BigDealId: Large order number.
        :type BigDealId: str
        :param _Formula: Refund formula.
        :type Formula: str
        :param _RefReturnDeals: Refund involves order information.
        :type RefReturnDeals: str
        :param _PayMode: Billing mode: `prePay` (prepaid), `postPay` (pay-as-you-go), `riPay` (reserved instance)
        :type PayMode: str
        :param _Action: Transaction type

Modify network mode adjust bandwidth mode.
Adjust bandwidth size.
`Refund`: refund.
downgrade.
upgrade configuration.
renew.
purchase.
preMoveOut monthly subscription resource migration out.
preMoveIn specifies the monthly subscription resources to migrate.
preToPost specifies the prepaid to postpaid conversion.
postMoveOut specifies the pay-as-you-go resources to be migrated out.
postMoveIn specifies the pay-as-you-go resources for inbound migration.
        :type Action: str
        :param _ProductName: Product code chinese name.
        :type ProductName: str
        :param _SubProductName: Sub-Product code chinese name.
        :type SubProductName: str
        :param _ResourceId: The resource ID corresponding to the order. If the query parameter `Limit` exceeds 200, null will be returned.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceId: list of str
        :param _ZoneCode: Availability zone Id corresponding to the order
        :type ZoneCode: str
        """
        self._OrderId = None
        self._Status = None
        self._Payer = None
        self._CreateTime = None
        self._Creator = None
        self._RealTotalCost = None
        self._VoucherDecline = None
        self._ProjectId = None
        self._GoodsCategoryId = None
        self._ProductInfo = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._Currency = None
        self._Policy = None
        self._Price = None
        self._TotalCost = None
        self._ProductCode = None
        self._SubProductCode = None
        self._BigDealId = None
        self._Formula = None
        self._RefReturnDeals = None
        self._PayMode = None
        self._Action = None
        self._ProductName = None
        self._SubProductName = None
        self._ResourceId = None
        self._ZoneCode = None

    @property
    def OrderId(self):
        r"""Order ID.
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Status(self):
        r"""The status of the order. 1: unpaid; 2: paid; 3: shipping; 4: shipped; 5: shipment failed; 6: refunded; 7: closed case; 8: order expired; 9: order invalidated; 10: product invalidated; 11: third-party payment refused; 12: payment in process
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Payer(self):
        r"""Payer
        :rtype: str
        """
        return self._Payer

    @Payer.setter
    def Payer(self, Payer):
        self._Payer = Payer

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
    def Creator(self):
        r"""Creator
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def RealTotalCost(self):
        r"""Actual payment amount (pent)
        :rtype: int
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def VoucherDecline(self):
        r"""Voucher offset amount (pent)
        :rtype: int
        """
        return self._VoucherDecline

    @VoucherDecline.setter
    def VoucherDecline(self, VoucherDecline):
        self._VoucherDecline = VoucherDecline

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def GoodsCategoryId(self):
        r"""Product category ID
        :rtype: int
        """
        return self._GoodsCategoryId

    @GoodsCategoryId.setter
    def GoodsCategoryId(self, GoodsCategoryId):
        self._GoodsCategoryId = GoodsCategoryId

    @property
    def ProductInfo(self):
        r"""Product details
        :rtype: list of ProductInfo
        """
        return self._ProductInfo

    @ProductInfo.setter
    def ProductInfo(self, ProductInfo):
        self._ProductInfo = ProductInfo

    @property
    def TimeSpan(self):
        r"""Duration
        :rtype: float
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        r"""Time unit
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def Currency(self):
        r"""Currency unit
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def Policy(self):
        r"""Discount rate
        :rtype: float
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Price(self):
        r"""Unit price (cents)
        :rtype: float
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def TotalCost(self):
        r"""Original price (cents)
        :rtype: float
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def ProductCode(self):
        r"""Product code
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def SubProductCode(self):
        r"""Subproduct code
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def BigDealId(self):
        r"""Large order number.
        :rtype: str
        """
        return self._BigDealId

    @BigDealId.setter
    def BigDealId(self, BigDealId):
        self._BigDealId = BigDealId

    @property
    def Formula(self):
        r"""Refund formula.
        :rtype: str
        """
        return self._Formula

    @Formula.setter
    def Formula(self, Formula):
        self._Formula = Formula

    @property
    def RefReturnDeals(self):
        r"""Refund involves order information.
        :rtype: str
        """
        return self._RefReturnDeals

    @RefReturnDeals.setter
    def RefReturnDeals(self, RefReturnDeals):
        self._RefReturnDeals = RefReturnDeals

    @property
    def PayMode(self):
        r"""Billing mode: `prePay` (prepaid), `postPay` (pay-as-you-go), `riPay` (reserved instance)
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Action(self):
        r"""Transaction type

Modify network mode adjust bandwidth mode.
Adjust bandwidth size.
`Refund`: refund.
downgrade.
upgrade configuration.
renew.
purchase.
preMoveOut monthly subscription resource migration out.
preMoveIn specifies the monthly subscription resources to migrate.
preToPost specifies the prepaid to postpaid conversion.
postMoveOut specifies the pay-as-you-go resources to be migrated out.
postMoveIn specifies the pay-as-you-go resources for inbound migration.
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ProductName(self):
        r"""Product code chinese name.
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def SubProductName(self):
        r"""Sub-Product code chinese name.
        :rtype: str
        """
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName

    @property
    def ResourceId(self):
        r"""The resource ID corresponding to the order. If the query parameter `Limit` exceeds 200, null will be returned.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ZoneCode(self):
        r"""Availability zone Id corresponding to the order
        :rtype: str
        """
        return self._ZoneCode

    @ZoneCode.setter
    def ZoneCode(self, ZoneCode):
        self._ZoneCode = ZoneCode


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._Status = params.get("Status")
        self._Payer = params.get("Payer")
        self._CreateTime = params.get("CreateTime")
        self._Creator = params.get("Creator")
        self._RealTotalCost = params.get("RealTotalCost")
        self._VoucherDecline = params.get("VoucherDecline")
        self._ProjectId = params.get("ProjectId")
        self._GoodsCategoryId = params.get("GoodsCategoryId")
        if params.get("ProductInfo") is not None:
            self._ProductInfo = []
            for item in params.get("ProductInfo"):
                obj = ProductInfo()
                obj._deserialize(item)
                self._ProductInfo.append(obj)
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._Currency = params.get("Currency")
        self._Policy = params.get("Policy")
        self._Price = params.get("Price")
        self._TotalCost = params.get("TotalCost")
        self._ProductCode = params.get("ProductCode")
        self._SubProductCode = params.get("SubProductCode")
        self._BigDealId = params.get("BigDealId")
        self._Formula = params.get("Formula")
        self._RefReturnDeals = params.get("RefReturnDeals")
        self._PayMode = params.get("PayMode")
        self._Action = params.get("Action")
        self._ProductName = params.get("ProductName")
        self._SubProductName = params.get("SubProductName")
        self._ResourceId = params.get("ResourceId")
        self._ZoneCode = params.get("ZoneCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAllocationRuleRequest(AbstractModel):
    r"""DeleteAllocationRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: The deleted sharing rule ID.
        :type RuleId: int
        :param _Month: Month, which is the current month by default if not provided.
        :type Month: str
        """
        self._RuleId = None
        self._Month = None

    @property
    def RuleId(self):
        r"""The deleted sharing rule ID.
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Month(self):
        r"""Month, which is the current month by default if not provided.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Month = params.get("Month")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAllocationRuleResponse(AbstractModel):
    r"""DeleteAllocationRule response structure.

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


class DeleteAllocationTagRequest(AbstractModel):
    r"""DeleteAllocationTag request structure.

    """

    def __init__(self):
        r"""
        :param _TagKey: Cost allocation tag key
        :type TagKey: list of str
        """
        self._TagKey = None

    @property
    def TagKey(self):
        r"""Cost allocation tag key
        :rtype: list of str
        """
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
    r"""DeleteAllocationTag response structure.

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


class DeleteAllocationUnitRequest(AbstractModel):
    r"""DeleteAllocationUnit request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Specifies the deleted cost allocation unit ID.
        :type Id: int
        :param _Month: Month, which is the current month by default if not provided.
        :type Month: str
        """
        self._Id = None
        self._Month = None

    @property
    def Id(self):
        r"""Specifies the deleted cost allocation unit ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Month(self):
        r"""Month, which is the current month by default if not provided.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Month = params.get("Month")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAllocationUnitResponse(AbstractModel):
    r"""DeleteAllocationUnit response structure.

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


class DeleteGatherRuleRequest(AbstractModel):
    r"""DeleteGatherRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: The deleted collection rule ID.
        :type RuleId: int
        :param _Month: Month, which is the current month by default if not provided.
        :type Month: str
        """
        self._RuleId = None
        self._Month = None

    @property
    def RuleId(self):
        r"""The deleted collection rule ID.
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Month(self):
        r"""Month, which is the current month by default if not provided.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Month = params.get("Month")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGatherRuleResponse(AbstractModel):
    r"""DeleteGatherRule response structure.

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


class DescribeAccountBalanceRequest(AbstractModel):
    r"""DescribeAccountBalance request structure.

    """

    def __init__(self):
        r"""
        :param _TempCredit: Query the temporary limit
        :type TempCredit: bool
        """
        self._TempCredit = None

    @property
    def TempCredit(self):
        r"""Query the temporary limit
        :rtype: bool
        """
        return self._TempCredit

    @TempCredit.setter
    def TempCredit(self, TempCredit):
        self._TempCredit = TempCredit


    def _deserialize(self, params):
        self._TempCredit = params.get("TempCredit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountBalanceResponse(AbstractModel):
    r"""DescribeAccountBalance response structure.

    """

    def __init__(self):
        r"""
        :param _Balance: Available account balance in cents, which takes the same calculation rules as `RealBalance`, `CreditBalance`, and `RealCreditBalance`.
        :type Balance: int
        :param _Uin: The user Uin for the query
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
        :param _TempCredit: Temporary limit, unit cent
        :type TempCredit: float
        :param _TempAmountInfoList: Temporary limit details
        :type TempAmountInfoList: list of UinTempAmountModel
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
        self._TempCredit = None
        self._TempAmountInfoList = None
        self._RequestId = None

    @property
    def Balance(self):
        r"""Available account balance in cents, which takes the same calculation rules as `RealBalance`, `CreditBalance`, and `RealCreditBalance`.
        :rtype: int
        """
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def Uin(self):
        r"""The user Uin for the query
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def RealBalance(self):
        r"""Available account balance in cents, which takes the same calculation rules as `Balance`, `CreditBalance`, and `RealCreditBalance`.
        :rtype: float
        """
        return self._RealBalance

    @RealBalance.setter
    def RealBalance(self, RealBalance):
        self._RealBalance = RealBalance

    @property
    def CashAccountBalance(self):
        r"""Cash account balance in cents. Currently, this field is not applied.
        :rtype: float
        """
        return self._CashAccountBalance

    @CashAccountBalance.setter
    def CashAccountBalance(self, CashAccountBalance):
        self._CashAccountBalance = CashAccountBalance

    @property
    def IncomeIntoAccountBalance(self):
        r"""Income account balance in cents. Currently, this field is not applied.
        :rtype: float
        """
        return self._IncomeIntoAccountBalance

    @IncomeIntoAccountBalance.setter
    def IncomeIntoAccountBalance(self, IncomeIntoAccountBalance):
        self._IncomeIntoAccountBalance = IncomeIntoAccountBalance

    @property
    def PresentAccountBalance(self):
        r"""Present account balance in cents. Currently, this field is not applied.
        :rtype: float
        """
        return self._PresentAccountBalance

    @PresentAccountBalance.setter
    def PresentAccountBalance(self, PresentAccountBalance):
        self._PresentAccountBalance = PresentAccountBalance

    @property
    def FreezeAmount(self):
        r"""Frozen amount in cents.
        :rtype: float
        """
        return self._FreezeAmount

    @FreezeAmount.setter
    def FreezeAmount(self, FreezeAmount):
        self._FreezeAmount = FreezeAmount

    @property
    def OweAmount(self):
        r"""Overdue amount in cents, which is when the available credit balance is negative.
        :rtype: float
        """
        return self._OweAmount

    @OweAmount.setter
    def OweAmount(self, OweAmount):
        self._OweAmount = OweAmount

    @property
    def IsAllowArrears(self):
        warnings.warn("parameter `IsAllowArrears` is deprecated", DeprecationWarning) 

        r"""Whether overdue payments are allowed. Currently, this field is not applied.
        :rtype: bool
        """
        return self._IsAllowArrears

    @IsAllowArrears.setter
    def IsAllowArrears(self, IsAllowArrears):
        warnings.warn("parameter `IsAllowArrears` is deprecated", DeprecationWarning) 

        self._IsAllowArrears = IsAllowArrears

    @property
    def IsCreditLimited(self):
        warnings.warn("parameter `IsCreditLimited` is deprecated", DeprecationWarning) 

        r"""Whether you have a credit limit. Currently, this field is not applied.
        :rtype: bool
        """
        return self._IsCreditLimited

    @IsCreditLimited.setter
    def IsCreditLimited(self, IsCreditLimited):
        warnings.warn("parameter `IsCreditLimited` is deprecated", DeprecationWarning) 

        self._IsCreditLimited = IsCreditLimited

    @property
    def CreditAmount(self):
        r"""Credit limit in cents. Credit limit－available credit balance = consumption amount
        :rtype: float
        """
        return self._CreditAmount

    @CreditAmount.setter
    def CreditAmount(self, CreditAmount):
        self._CreditAmount = CreditAmount

    @property
    def CreditBalance(self):
        r"""Available credit balance in cents, which takes the same calculation rules as `Balance`, `RealBalance`, and `RealCreditBalance`.
        :rtype: float
        """
        return self._CreditBalance

    @CreditBalance.setter
    def CreditBalance(self, CreditBalance):
        self._CreditBalance = CreditBalance

    @property
    def RealCreditBalance(self):
        r"""Available account balance in cents, which takes the same calculation rules as `Balance`, `RealBalance`, and `CreditBalance`.
        :rtype: float
        """
        return self._RealCreditBalance

    @RealCreditBalance.setter
    def RealCreditBalance(self, RealCreditBalance):
        self._RealCreditBalance = RealCreditBalance

    @property
    def TempCredit(self):
        r"""Temporary limit, unit cent
        :rtype: float
        """
        return self._TempCredit

    @TempCredit.setter
    def TempCredit(self, TempCredit):
        self._TempCredit = TempCredit

    @property
    def TempAmountInfoList(self):
        r"""Temporary limit details
        :rtype: list of UinTempAmountModel
        """
        return self._TempAmountInfoList

    @TempAmountInfoList.setter
    def TempAmountInfoList(self, TempAmountInfoList):
        self._TempAmountInfoList = TempAmountInfoList

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
        self._TempCredit = params.get("TempCredit")
        if params.get("TempAmountInfoList") is not None:
            self._TempAmountInfoList = []
            for item in params.get("TempAmountInfoList"):
                obj = UinTempAmountModel()
                obj._deserialize(item)
                self._TempAmountInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllocateConditionsRequest(AbstractModel):
    r"""DescribeAllocateConditions request structure.

    """

    def __init__(self):
        r"""
        :param _Month: Bill month, in the format of 2024-02, which is the current month by default if not provided
        :type Month: str
        """
        self._Month = None

    @property
    def Month(self):
        r"""Bill month, in the format of 2024-02, which is the current month by default if not provided
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month


    def _deserialize(self, params):
        self._Month = params.get("Month")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocateConditionsResponse(AbstractModel):
    r"""DescribeAllocateConditions response structure.

    """

    def __init__(self):
        r"""
        :param _Business: Product filter list
        :type Business: list of BillBusinessLink
        :param _Product: Subproduct filter list
        :type Product: list of BillProduct
        :param _Item: Component name filter list
        :type Item: list of BillItem
        :param _Region: Region filter list
        :type Region: list of BillRegion
        :param _InstanceType: Instance type filter list
        :type InstanceType: list of BillInstanceType
        :param _PayMode: Billing mode filter list
        :type PayMode: list of BillPayMode
        :param _Project: Project filter list
        :type Project: list of BillProject
        :param _Tag: Tag filter list
        :type Tag: list of BillTag
        :param _OwnerUin: User UIN filter list
        :type OwnerUin: list of BillOwnerUin
        :param _OperateUin: Operator UIN filter list
        :type OperateUin: list of BillOperateUin
        :param _ActionType: Transaction type filter list
        :type ActionType: list of BillActionType
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Business = None
        self._Product = None
        self._Item = None
        self._Region = None
        self._InstanceType = None
        self._PayMode = None
        self._Project = None
        self._Tag = None
        self._OwnerUin = None
        self._OperateUin = None
        self._ActionType = None
        self._RequestId = None

    @property
    def Business(self):
        r"""Product filter list
        :rtype: list of BillBusinessLink
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Product(self):
        r"""Subproduct filter list
        :rtype: list of BillProduct
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Item(self):
        r"""Component name filter list
        :rtype: list of BillItem
        """
        return self._Item

    @Item.setter
    def Item(self, Item):
        self._Item = Item

    @property
    def Region(self):
        r"""Region filter list
        :rtype: list of BillRegion
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceType(self):
        r"""Instance type filter list
        :rtype: list of BillInstanceType
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def PayMode(self):
        r"""Billing mode filter list
        :rtype: list of BillPayMode
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Project(self):
        r"""Project filter list
        :rtype: list of BillProject
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Tag(self):
        r"""Tag filter list
        :rtype: list of BillTag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def OwnerUin(self):
        r"""User UIN filter list
        :rtype: list of BillOwnerUin
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        r"""Operator UIN filter list
        :rtype: list of BillOperateUin
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def ActionType(self):
        r"""Transaction type filter list
        :rtype: list of BillActionType
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

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
        if params.get("Business") is not None:
            self._Business = []
            for item in params.get("Business"):
                obj = BillBusinessLink()
                obj._deserialize(item)
                self._Business.append(obj)
        if params.get("Product") is not None:
            self._Product = []
            for item in params.get("Product"):
                obj = BillProduct()
                obj._deserialize(item)
                self._Product.append(obj)
        if params.get("Item") is not None:
            self._Item = []
            for item in params.get("Item"):
                obj = BillItem()
                obj._deserialize(item)
                self._Item.append(obj)
        if params.get("Region") is not None:
            self._Region = []
            for item in params.get("Region"):
                obj = BillRegion()
                obj._deserialize(item)
                self._Region.append(obj)
        if params.get("InstanceType") is not None:
            self._InstanceType = []
            for item in params.get("InstanceType"):
                obj = BillInstanceType()
                obj._deserialize(item)
                self._InstanceType.append(obj)
        if params.get("PayMode") is not None:
            self._PayMode = []
            for item in params.get("PayMode"):
                obj = BillPayMode()
                obj._deserialize(item)
                self._PayMode.append(obj)
        if params.get("Project") is not None:
            self._Project = []
            for item in params.get("Project"):
                obj = BillProject()
                obj._deserialize(item)
                self._Project.append(obj)
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = BillTag()
                obj._deserialize(item)
                self._Tag.append(obj)
        if params.get("OwnerUin") is not None:
            self._OwnerUin = []
            for item in params.get("OwnerUin"):
                obj = BillOwnerUin()
                obj._deserialize(item)
                self._OwnerUin.append(obj)
        if params.get("OperateUin") is not None:
            self._OperateUin = []
            for item in params.get("OperateUin"):
                obj = BillOperateUin()
                obj._deserialize(item)
                self._OperateUin.append(obj)
        if params.get("ActionType") is not None:
            self._ActionType = []
            for item in params.get("ActionType"):
                obj = BillActionType()
                obj._deserialize(item)
                self._ActionType.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllocationBillConditionsRequest(AbstractModel):
    r"""DescribeAllocationBillConditions request structure.

    """

    def __init__(self):
        r"""
        :param _Month: Bill month, in the format of 2024-02, which is the current month by default if not provided
        :type Month: str
        :param _TreeNodeUniqKeys: Unique identifier of a billing unit, used for filtering
        :type TreeNodeUniqKeys: list of str
        :param _BillDates: Date
        :type BillDates: list of str
        :param _BusinessCodes: Product code
        :type BusinessCodes: list of str
        :param _OwnerUins: User UIN
        :type OwnerUins: list of str
        :param _OperateUins: Operator UIN
        :type OperateUins: list of str
        :param _PayModes: Billing mode code
        :type PayModes: list of str
        :param _ActionTypes: Transaction type code
        :type ActionTypes: list of str
        :param _ProductCodes: Subproduct code
        :type ProductCodes: list of str
        :param _RegionIds: Region ID
        :type RegionIds: list of str
        :param _ZoneIds: AZ ID
        :type ZoneIds: list of str
        :param _InstanceTypes: Instance type code
        :type InstanceTypes: list of str
        :param _Tag: Tag
        :type Tag: list of str
        :param _ComponentCodes: Component type code
        :type ComponentCodes: list of str
        :param _ItemCodes: Component name code
        :type ItemCodes: list of str
        :param _SearchKey: Fuzzy search criteria
        :type SearchKey: str
        :param _ProjectIds: Project ID
        :type ProjectIds: list of int non-negative
        :param _AllocationType: Cost collection type
        :type AllocationType: list of int
        """
        self._Month = None
        self._TreeNodeUniqKeys = None
        self._BillDates = None
        self._BusinessCodes = None
        self._OwnerUins = None
        self._OperateUins = None
        self._PayModes = None
        self._ActionTypes = None
        self._ProductCodes = None
        self._RegionIds = None
        self._ZoneIds = None
        self._InstanceTypes = None
        self._Tag = None
        self._ComponentCodes = None
        self._ItemCodes = None
        self._SearchKey = None
        self._ProjectIds = None
        self._AllocationType = None

    @property
    def Month(self):
        r"""Bill month, in the format of 2024-02, which is the current month by default if not provided
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def TreeNodeUniqKeys(self):
        r"""Unique identifier of a billing unit, used for filtering
        :rtype: list of str
        """
        return self._TreeNodeUniqKeys

    @TreeNodeUniqKeys.setter
    def TreeNodeUniqKeys(self, TreeNodeUniqKeys):
        self._TreeNodeUniqKeys = TreeNodeUniqKeys

    @property
    def BillDates(self):
        r"""Date
        :rtype: list of str
        """
        return self._BillDates

    @BillDates.setter
    def BillDates(self, BillDates):
        self._BillDates = BillDates

    @property
    def BusinessCodes(self):
        r"""Product code
        :rtype: list of str
        """
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def OwnerUins(self):
        r"""User UIN
        :rtype: list of str
        """
        return self._OwnerUins

    @OwnerUins.setter
    def OwnerUins(self, OwnerUins):
        self._OwnerUins = OwnerUins

    @property
    def OperateUins(self):
        r"""Operator UIN
        :rtype: list of str
        """
        return self._OperateUins

    @OperateUins.setter
    def OperateUins(self, OperateUins):
        self._OperateUins = OperateUins

    @property
    def PayModes(self):
        r"""Billing mode code
        :rtype: list of str
        """
        return self._PayModes

    @PayModes.setter
    def PayModes(self, PayModes):
        self._PayModes = PayModes

    @property
    def ActionTypes(self):
        r"""Transaction type code
        :rtype: list of str
        """
        return self._ActionTypes

    @ActionTypes.setter
    def ActionTypes(self, ActionTypes):
        self._ActionTypes = ActionTypes

    @property
    def ProductCodes(self):
        r"""Subproduct code
        :rtype: list of str
        """
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes

    @property
    def RegionIds(self):
        r"""Region ID
        :rtype: list of str
        """
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def ZoneIds(self):
        r"""AZ ID
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def InstanceTypes(self):
        r"""Instance type code
        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def Tag(self):
        r"""Tag
        :rtype: list of str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ComponentCodes(self):
        r"""Component type code
        :rtype: list of str
        """
        return self._ComponentCodes

    @ComponentCodes.setter
    def ComponentCodes(self, ComponentCodes):
        self._ComponentCodes = ComponentCodes

    @property
    def ItemCodes(self):
        r"""Component name code
        :rtype: list of str
        """
        return self._ItemCodes

    @ItemCodes.setter
    def ItemCodes(self, ItemCodes):
        self._ItemCodes = ItemCodes

    @property
    def SearchKey(self):
        r"""Fuzzy search criteria
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ProjectIds(self):
        r"""Project ID
        :rtype: list of int non-negative
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def AllocationType(self):
        r"""Cost collection type
        :rtype: list of int
        """
        return self._AllocationType

    @AllocationType.setter
    def AllocationType(self, AllocationType):
        self._AllocationType = AllocationType


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._TreeNodeUniqKeys = params.get("TreeNodeUniqKeys")
        self._BillDates = params.get("BillDates")
        self._BusinessCodes = params.get("BusinessCodes")
        self._OwnerUins = params.get("OwnerUins")
        self._OperateUins = params.get("OperateUins")
        self._PayModes = params.get("PayModes")
        self._ActionTypes = params.get("ActionTypes")
        self._ProductCodes = params.get("ProductCodes")
        self._RegionIds = params.get("RegionIds")
        self._ZoneIds = params.get("ZoneIds")
        self._InstanceTypes = params.get("InstanceTypes")
        self._Tag = params.get("Tag")
        self._ComponentCodes = params.get("ComponentCodes")
        self._ItemCodes = params.get("ItemCodes")
        self._SearchKey = params.get("SearchKey")
        self._ProjectIds = params.get("ProjectIds")
        self._AllocationType = params.get("AllocationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationBillConditionsResponse(AbstractModel):
    r"""DescribeAllocationBillConditions response structure.

    """

    def __init__(self):
        r"""
        :param _Business: Product filter list
        :type Business: list of BillBusiness
        :param _Product: Subproduct filter list
        :type Product: list of BillProduct
        :param _Item: Component name filter list
        :type Item: list of BillItem
        :param _Region: Region filter list
        :type Region: list of BillRegion
        :param _InstanceType: Instance type filter list
        :type InstanceType: list of BillInstanceType
        :param _PayMode: Billing mode filter list
        :type PayMode: list of BillPayMode
        :param _Project: Project filter list
        :type Project: list of BillProject
        :param _Tag: Tag filter list
        :type Tag: list of BillTag
        :param _OwnerUin: User UIN filter list
        :type OwnerUin: list of BillOwnerUin
        :param _OperateUin: Operator UIN filter list
        :type OperateUin: list of BillOperateUin
        :param _BillDay: Date filter list
        :type BillDay: list of BillDays
        :param _ActionType: Transaction type filter list
        :type ActionType: list of BillActionType
        :param _Component: Component type filter list
        :type Component: list of BillComponent
        :param _Zone: Availability zone filter list
        :type Zone: list of BillZoneId
        :param _AllocationTreeNode: Cost allocation unit filter list
        :type AllocationTreeNode: list of AllocationTreeNode
        :param _TagKey: Cost allocation tag key
        :type TagKey: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Business = None
        self._Product = None
        self._Item = None
        self._Region = None
        self._InstanceType = None
        self._PayMode = None
        self._Project = None
        self._Tag = None
        self._OwnerUin = None
        self._OperateUin = None
        self._BillDay = None
        self._ActionType = None
        self._Component = None
        self._Zone = None
        self._AllocationTreeNode = None
        self._TagKey = None
        self._RequestId = None

    @property
    def Business(self):
        r"""Product filter list
        :rtype: list of BillBusiness
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Product(self):
        r"""Subproduct filter list
        :rtype: list of BillProduct
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Item(self):
        r"""Component name filter list
        :rtype: list of BillItem
        """
        return self._Item

    @Item.setter
    def Item(self, Item):
        self._Item = Item

    @property
    def Region(self):
        r"""Region filter list
        :rtype: list of BillRegion
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceType(self):
        r"""Instance type filter list
        :rtype: list of BillInstanceType
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def PayMode(self):
        r"""Billing mode filter list
        :rtype: list of BillPayMode
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Project(self):
        r"""Project filter list
        :rtype: list of BillProject
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Tag(self):
        r"""Tag filter list
        :rtype: list of BillTag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def OwnerUin(self):
        r"""User UIN filter list
        :rtype: list of BillOwnerUin
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        r"""Operator UIN filter list
        :rtype: list of BillOperateUin
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def BillDay(self):
        r"""Date filter list
        :rtype: list of BillDays
        """
        return self._BillDay

    @BillDay.setter
    def BillDay(self, BillDay):
        self._BillDay = BillDay

    @property
    def ActionType(self):
        r"""Transaction type filter list
        :rtype: list of BillActionType
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def Component(self):
        r"""Component type filter list
        :rtype: list of BillComponent
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Zone(self):
        r"""Availability zone filter list
        :rtype: list of BillZoneId
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def AllocationTreeNode(self):
        r"""Cost allocation unit filter list
        :rtype: list of AllocationTreeNode
        """
        return self._AllocationTreeNode

    @AllocationTreeNode.setter
    def AllocationTreeNode(self, AllocationTreeNode):
        self._AllocationTreeNode = AllocationTreeNode

    @property
    def TagKey(self):
        r"""Cost allocation tag key
        :rtype: list of str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

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
        if params.get("Business") is not None:
            self._Business = []
            for item in params.get("Business"):
                obj = BillBusiness()
                obj._deserialize(item)
                self._Business.append(obj)
        if params.get("Product") is not None:
            self._Product = []
            for item in params.get("Product"):
                obj = BillProduct()
                obj._deserialize(item)
                self._Product.append(obj)
        if params.get("Item") is not None:
            self._Item = []
            for item in params.get("Item"):
                obj = BillItem()
                obj._deserialize(item)
                self._Item.append(obj)
        if params.get("Region") is not None:
            self._Region = []
            for item in params.get("Region"):
                obj = BillRegion()
                obj._deserialize(item)
                self._Region.append(obj)
        if params.get("InstanceType") is not None:
            self._InstanceType = []
            for item in params.get("InstanceType"):
                obj = BillInstanceType()
                obj._deserialize(item)
                self._InstanceType.append(obj)
        if params.get("PayMode") is not None:
            self._PayMode = []
            for item in params.get("PayMode"):
                obj = BillPayMode()
                obj._deserialize(item)
                self._PayMode.append(obj)
        if params.get("Project") is not None:
            self._Project = []
            for item in params.get("Project"):
                obj = BillProject()
                obj._deserialize(item)
                self._Project.append(obj)
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = BillTag()
                obj._deserialize(item)
                self._Tag.append(obj)
        if params.get("OwnerUin") is not None:
            self._OwnerUin = []
            for item in params.get("OwnerUin"):
                obj = BillOwnerUin()
                obj._deserialize(item)
                self._OwnerUin.append(obj)
        if params.get("OperateUin") is not None:
            self._OperateUin = []
            for item in params.get("OperateUin"):
                obj = BillOperateUin()
                obj._deserialize(item)
                self._OperateUin.append(obj)
        if params.get("BillDay") is not None:
            self._BillDay = []
            for item in params.get("BillDay"):
                obj = BillDays()
                obj._deserialize(item)
                self._BillDay.append(obj)
        if params.get("ActionType") is not None:
            self._ActionType = []
            for item in params.get("ActionType"):
                obj = BillActionType()
                obj._deserialize(item)
                self._ActionType.append(obj)
        if params.get("Component") is not None:
            self._Component = []
            for item in params.get("Component"):
                obj = BillComponent()
                obj._deserialize(item)
                self._Component.append(obj)
        if params.get("Zone") is not None:
            self._Zone = []
            for item in params.get("Zone"):
                obj = BillZoneId()
                obj._deserialize(item)
                self._Zone.append(obj)
        if params.get("AllocationTreeNode") is not None:
            self._AllocationTreeNode = []
            for item in params.get("AllocationTreeNode"):
                obj = AllocationTreeNode()
                obj._deserialize(item)
                self._AllocationTreeNode.append(obj)
        self._TagKey = params.get("TagKey")
        self._RequestId = params.get("RequestId")


class DescribeAllocationBillDetailRequest(AbstractModel):
    r"""DescribeAllocationBillDetail request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Quantity, with the maximum value of 1,000
        :type Limit: int
        :param _Offset: Pagination offset. If Offset is 0, it indicates the first page. If Limit is 100, then Offset is 100, and it indicates the second page. If Offset is 200, it indicates the third page, and so on.
        :type Offset: int
        :param _Month: Bill month, in the format of 2024-02, which is the current month by default if not provided
        :type Month: str
        :param _TreeNodeUniqKeys: Unique identifier of a billing unit, used for filtering
        :type TreeNodeUniqKeys: list of str
        :param _Sort: Sorting field, with the enumerated values as follows:
RiTimeSpan - Deduction duration of a reserved instance
ExtendPayAmount1 - Original price for the deduction duration of a reserved instance
RealCost - Discounted total
CashPayAmount - Cash amount
VoucherPayAmount - Amount of promo voucher
IncentivePayAmount - Amount of free credit
TransferPayAmount - Royalty amount
Cost - Original price of a component
        :type Sort: str
        :param _SortType: Sorting type, with the enumerated values as follows:
asc - Ascending
desc - Descending
        :type SortType: str
        :param _BusinessCodes: Product code, used for filtering
        :type BusinessCodes: list of str
        :param _OwnerUins: User UIN, used for filtering
        :type OwnerUins: list of str
        :param _OperateUins: Operator UIN, used for filtering
        :type OperateUins: list of str
        :param _PayModes: Billing mode code, used for filtering
        :type PayModes: list of str
        :param _ActionTypes: Transaction type code, used for filtering
        :type ActionTypes: list of str
        :param _ProductCodes: Subproduct code, used for filtering
        :type ProductCodes: list of str
        :param _RegionIds: Region ID, used for filtering
        :type RegionIds: list of str
        :param _ZoneIds: AZ ID, used for filtering
        :type ZoneIds: list of str
        :param _InstanceTypes: Instance type code, used for filtering
        :type InstanceTypes: list of str
        :param _Tag: Tag, used for filtering
        :type Tag: list of str
        :param _ComponentCodes: Component type code, used for filtering
        :type ComponentCodes: list of str
        :param _ItemCodes: Component name code, used for filtering
        :type ItemCodes: list of str
        :param _SearchKey: Fuzzy search: supports tag, resource ID, and resource alias.
        :type SearchKey: str
        :param _ProjectIds: Project ID, used for filtering
        :type ProjectIds: list of int non-negative
        """
        self._Limit = None
        self._Offset = None
        self._Month = None
        self._TreeNodeUniqKeys = None
        self._Sort = None
        self._SortType = None
        self._BusinessCodes = None
        self._OwnerUins = None
        self._OperateUins = None
        self._PayModes = None
        self._ActionTypes = None
        self._ProductCodes = None
        self._RegionIds = None
        self._ZoneIds = None
        self._InstanceTypes = None
        self._Tag = None
        self._ComponentCodes = None
        self._ItemCodes = None
        self._SearchKey = None
        self._ProjectIds = None

    @property
    def Limit(self):
        r"""Quantity, with the maximum value of 1,000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Pagination offset. If Offset is 0, it indicates the first page. If Limit is 100, then Offset is 100, and it indicates the second page. If Offset is 200, it indicates the third page, and so on.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Month(self):
        r"""Bill month, in the format of 2024-02, which is the current month by default if not provided
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def TreeNodeUniqKeys(self):
        r"""Unique identifier of a billing unit, used for filtering
        :rtype: list of str
        """
        return self._TreeNodeUniqKeys

    @TreeNodeUniqKeys.setter
    def TreeNodeUniqKeys(self, TreeNodeUniqKeys):
        self._TreeNodeUniqKeys = TreeNodeUniqKeys

    @property
    def Sort(self):
        r"""Sorting field, with the enumerated values as follows:
RiTimeSpan - Deduction duration of a reserved instance
ExtendPayAmount1 - Original price for the deduction duration of a reserved instance
RealCost - Discounted total
CashPayAmount - Cash amount
VoucherPayAmount - Amount of promo voucher
IncentivePayAmount - Amount of free credit
TransferPayAmount - Royalty amount
Cost - Original price of a component
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def SortType(self):
        r"""Sorting type, with the enumerated values as follows:
asc - Ascending
desc - Descending
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def BusinessCodes(self):
        r"""Product code, used for filtering
        :rtype: list of str
        """
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def OwnerUins(self):
        r"""User UIN, used for filtering
        :rtype: list of str
        """
        return self._OwnerUins

    @OwnerUins.setter
    def OwnerUins(self, OwnerUins):
        self._OwnerUins = OwnerUins

    @property
    def OperateUins(self):
        r"""Operator UIN, used for filtering
        :rtype: list of str
        """
        return self._OperateUins

    @OperateUins.setter
    def OperateUins(self, OperateUins):
        self._OperateUins = OperateUins

    @property
    def PayModes(self):
        r"""Billing mode code, used for filtering
        :rtype: list of str
        """
        return self._PayModes

    @PayModes.setter
    def PayModes(self, PayModes):
        self._PayModes = PayModes

    @property
    def ActionTypes(self):
        r"""Transaction type code, used for filtering
        :rtype: list of str
        """
        return self._ActionTypes

    @ActionTypes.setter
    def ActionTypes(self, ActionTypes):
        self._ActionTypes = ActionTypes

    @property
    def ProductCodes(self):
        r"""Subproduct code, used for filtering
        :rtype: list of str
        """
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes

    @property
    def RegionIds(self):
        r"""Region ID, used for filtering
        :rtype: list of str
        """
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def ZoneIds(self):
        r"""AZ ID, used for filtering
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def InstanceTypes(self):
        r"""Instance type code, used for filtering
        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def Tag(self):
        r"""Tag, used for filtering
        :rtype: list of str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ComponentCodes(self):
        r"""Component type code, used for filtering
        :rtype: list of str
        """
        return self._ComponentCodes

    @ComponentCodes.setter
    def ComponentCodes(self, ComponentCodes):
        self._ComponentCodes = ComponentCodes

    @property
    def ItemCodes(self):
        r"""Component name code, used for filtering
        :rtype: list of str
        """
        return self._ItemCodes

    @ItemCodes.setter
    def ItemCodes(self, ItemCodes):
        self._ItemCodes = ItemCodes

    @property
    def SearchKey(self):
        r"""Fuzzy search: supports tag, resource ID, and resource alias.
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ProjectIds(self):
        r"""Project ID, used for filtering
        :rtype: list of int non-negative
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Month = params.get("Month")
        self._TreeNodeUniqKeys = params.get("TreeNodeUniqKeys")
        self._Sort = params.get("Sort")
        self._SortType = params.get("SortType")
        self._BusinessCodes = params.get("BusinessCodes")
        self._OwnerUins = params.get("OwnerUins")
        self._OperateUins = params.get("OperateUins")
        self._PayModes = params.get("PayModes")
        self._ActionTypes = params.get("ActionTypes")
        self._ProductCodes = params.get("ProductCodes")
        self._RegionIds = params.get("RegionIds")
        self._ZoneIds = params.get("ZoneIds")
        self._InstanceTypes = params.get("InstanceTypes")
        self._Tag = params.get("Tag")
        self._ComponentCodes = params.get("ComponentCodes")
        self._ItemCodes = params.get("ItemCodes")
        self._SearchKey = params.get("SearchKey")
        self._ProjectIds = params.get("ProjectIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationBillDetailResponse(AbstractModel):
    r"""DescribeAllocationBillDetail response structure.

    """

    def __init__(self):
        r"""
        :param _RecordNum: Total quantity.
        :type RecordNum: int
        :param _Total: Total amount of a cost allocation bill
        :type Total: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        :param _Detail: Details of a cost allocation bill
        :type Detail: list of AllocationDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecordNum = None
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def RecordNum(self):
        r"""Total quantity.
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def Total(self):
        r"""Total amount of a cost allocation bill
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        r"""Details of a cost allocation bill
        :rtype: list of AllocationDetail
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

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
        self._RecordNum = params.get("RecordNum")
        if params.get("Total") is not None:
            self._Total = AllocationOverviewTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = AllocationDetail()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllocationMonthOverviewRequest(AbstractModel):
    r"""DescribeAllocationMonthOverview request structure.

    """

    def __init__(self):
        r"""
        :param _Month: Bill month, in the format of 2024-02, which is the current month by default if not provided
        :type Month: str
        """
        self._Month = None

    @property
    def Month(self):
        r"""Bill month, in the format of 2024-02, which is the current month by default if not provided
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month


    def _deserialize(self, params):
        self._Month = params.get("Month")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationMonthOverviewResponse(AbstractModel):
    r"""DescribeAllocationMonthOverview response structure.

    """

    def __init__(self):
        r"""
        :param _Detail: Monthly overview of a cost allocation bill
        :type Detail: list of AllocationOverviewNode
        :param _Total: Total amount of a cost allocation bill
        :type Total: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Detail = None
        self._Total = None
        self._RequestId = None

    @property
    def Detail(self):
        r"""Monthly overview of a cost allocation bill
        :rtype: list of AllocationOverviewNode
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Total(self):
        r"""Total amount of a cost allocation bill
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = AllocationOverviewNode()
                obj._deserialize(item)
                self._Detail.append(obj)
        if params.get("Total") is not None:
            self._Total = AllocationOverviewTotal()
            self._Total._deserialize(params.get("Total"))
        self._RequestId = params.get("RequestId")


class DescribeAllocationOverviewRequest(AbstractModel):
    r"""DescribeAllocationOverview request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Quantity, with the maximum value of 1,000
        :type Limit: int
        :param _Offset: Pagination offset. If offset is 0, it indicates the first page. If limit is 100, then offset is 100, it indicates the second page; if offset is 200, it indicates the third page, and so on
        :type Offset: int
        :param _Month: Bill month, in the format of 2024-02, which is the current month by default if not provided
        :type Month: str
        :param _PeriodType: Statistical period, with the enumerated values as follows:
month - Month
day - Day
        :type PeriodType: str
        :param _TreeNodeUniqKeys: Unique identifier of a billing unit, used for filtering
        :type TreeNodeUniqKeys: list of str
        :param _Sort: Sorting field, with the enumerated values as follows: 
GatherCashPayAmount - Collected fees (cash)
GatherVoucherPayAmount - Collected fees (voucher)
GatherIncentivePayAmount - Collected fees (free credit)
GatherTransferPayAmount - Collected fees (royalty amount)
AllocateCashPayAmount - Allocated fees (cash)
AllocateVoucherPayAmount - Allocated fees (voucher)
AllocateIncentivePayAmount - Allocated fees (free credit)
AllocateTransferPayAmount - Allocated fees (royalty amount)
TotalCashPayAmount - Total fees (cash)
TotalVoucherPayAmount - Total fees (voucher)
TotalIncentivePayAmount - Total fees (free credit)
TotalTransferPayAmount - Total fees (royalty amount)
GatherRealCost - Collected fees (discounted total)
AllocateRealCost - Allocated fees (discounted total)
RealTotalCost - Total fees (discounted total)
Ratio - Proportion (discounted total)
        :type Sort: str
        :param _SortType: Sorting type, with the enumerated values as follows:
asc - Ascending
desc - Descending
        :type SortType: str
        :param _BillDates: Date, used for filtering
        :type BillDates: list of str
        """
        self._Limit = None
        self._Offset = None
        self._Month = None
        self._PeriodType = None
        self._TreeNodeUniqKeys = None
        self._Sort = None
        self._SortType = None
        self._BillDates = None

    @property
    def Limit(self):
        r"""Quantity, with the maximum value of 1,000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Pagination offset. If offset is 0, it indicates the first page. If limit is 100, then offset is 100, it indicates the second page; if offset is 200, it indicates the third page, and so on
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Month(self):
        r"""Bill month, in the format of 2024-02, which is the current month by default if not provided
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PeriodType(self):
        r"""Statistical period, with the enumerated values as follows:
month - Month
day - Day
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType

    @property
    def TreeNodeUniqKeys(self):
        r"""Unique identifier of a billing unit, used for filtering
        :rtype: list of str
        """
        return self._TreeNodeUniqKeys

    @TreeNodeUniqKeys.setter
    def TreeNodeUniqKeys(self, TreeNodeUniqKeys):
        self._TreeNodeUniqKeys = TreeNodeUniqKeys

    @property
    def Sort(self):
        r"""Sorting field, with the enumerated values as follows: 
GatherCashPayAmount - Collected fees (cash)
GatherVoucherPayAmount - Collected fees (voucher)
GatherIncentivePayAmount - Collected fees (free credit)
GatherTransferPayAmount - Collected fees (royalty amount)
AllocateCashPayAmount - Allocated fees (cash)
AllocateVoucherPayAmount - Allocated fees (voucher)
AllocateIncentivePayAmount - Allocated fees (free credit)
AllocateTransferPayAmount - Allocated fees (royalty amount)
TotalCashPayAmount - Total fees (cash)
TotalVoucherPayAmount - Total fees (voucher)
TotalIncentivePayAmount - Total fees (free credit)
TotalTransferPayAmount - Total fees (royalty amount)
GatherRealCost - Collected fees (discounted total)
AllocateRealCost - Allocated fees (discounted total)
RealTotalCost - Total fees (discounted total)
Ratio - Proportion (discounted total)
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def SortType(self):
        r"""Sorting type, with the enumerated values as follows:
asc - Ascending
desc - Descending
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def BillDates(self):
        r"""Date, used for filtering
        :rtype: list of str
        """
        return self._BillDates

    @BillDates.setter
    def BillDates(self, BillDates):
        self._BillDates = BillDates


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Month = params.get("Month")
        self._PeriodType = params.get("PeriodType")
        self._TreeNodeUniqKeys = params.get("TreeNodeUniqKeys")
        self._Sort = params.get("Sort")
        self._SortType = params.get("SortType")
        self._BillDates = params.get("BillDates")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationOverviewResponse(AbstractModel):
    r"""DescribeAllocationOverview response structure.

    """

    def __init__(self):
        r"""
        :param _RecordNum: Total quantity.
        :type RecordNum: int
        :param _Total: Total amount of a cost allocation bill
        :type Total: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        :param _Detail: Details of the cost allocation overview
        :type Detail: list of AllocationOverviewDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecordNum = None
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def RecordNum(self):
        r"""Total quantity.
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def Total(self):
        r"""Total amount of a cost allocation bill
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        r"""Details of the cost allocation overview
        :rtype: list of AllocationOverviewDetail
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

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
        self._RecordNum = params.get("RecordNum")
        if params.get("Total") is not None:
            self._Total = AllocationOverviewTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = AllocationOverviewDetail()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllocationRuleDetailRequest(AbstractModel):
    r"""DescribeAllocationRuleDetail request structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: The queried sharing rule ID.
        :type RuleId: int
        :param _Month: Month, which is the current month by default if not provided.
        :type Month: str
        """
        self._RuleId = None
        self._Month = None

    @property
    def RuleId(self):
        r"""The queried sharing rule ID.
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Month(self):
        r"""Month, which is the current month by default if not provided.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Month = params.get("Month")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationRuleDetailResponse(AbstractModel):
    r"""DescribeAllocationRuleDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Sharing rule ID.
        :type Id: int
        :param _Uin: Sharing rule ownership UIN.
        :type Uin: str
        :param _Name: Sharing rule name.
        :type Name: str
        :param _Type: Specifies the public area policy type. the enumeration values are as follows:.
1 - custom sharing proportion. 
2 - proportional allocation. 
3 - allocation by proportion.
        :type Type: int
        :param _RuleDetail: Public sharing rule expression.
        :type RuleDetail: :class:`tencentcloud.billing.v20180709.models.AllocationRuleExpression`
        :param _RatioDetail: Sharing proportion expression. returns when Type is 1 or 2.
        :type RatioDetail: list of AllocationRationExpression
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._Uin = None
        self._Name = None
        self._Type = None
        self._RuleDetail = None
        self._RatioDetail = None
        self._RequestId = None

    @property
    def Id(self):
        r"""Sharing rule ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uin(self):
        r"""Sharing rule ownership UIN.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Name(self):
        r"""Sharing rule name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""Specifies the public area policy type. the enumeration values are as follows:.
1 - custom sharing proportion. 
2 - proportional allocation. 
3 - allocation by proportion.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RuleDetail(self):
        r"""Public sharing rule expression.
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationRuleExpression`
        """
        return self._RuleDetail

    @RuleDetail.setter
    def RuleDetail(self, RuleDetail):
        self._RuleDetail = RuleDetail

    @property
    def RatioDetail(self):
        r"""Sharing proportion expression. returns when Type is 1 or 2.
        :rtype: list of AllocationRationExpression
        """
        return self._RatioDetail

    @RatioDetail.setter
    def RatioDetail(self, RatioDetail):
        self._RatioDetail = RatioDetail

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
        self._Id = params.get("Id")
        self._Uin = params.get("Uin")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("RuleDetail") is not None:
            self._RuleDetail = AllocationRuleExpression()
            self._RuleDetail._deserialize(params.get("RuleDetail"))
        if params.get("RatioDetail") is not None:
            self._RatioDetail = []
            for item in params.get("RatioDetail"):
                obj = AllocationRationExpression()
                obj._deserialize(item)
                self._RatioDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllocationRuleSummaryRequest(AbstractModel):
    r"""DescribeAllocationRuleSummary request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Specifies the data quantity per fetch. the maximum value is 1000.
        :type Limit: int
        :param _Offset: Pagination offset
        :type Offset: int
        :param _Month: Month, which is the current month by default if not provided.
        :type Month: str
        :param _Type: Public area policy type, for filtering.
Enumeration values are as follows:. 
1 - custom sharing proportion. 
2 - proportional allocation. 
3 - allocation by proportion.
        :type Type: int
        :param _Name: Sharing rule name or cost allocation unit name, used for fuzzy filter criteria.
        :type Name: str
        """
        self._Limit = None
        self._Offset = None
        self._Month = None
        self._Type = None
        self._Name = None

    @property
    def Limit(self):
        r"""Specifies the data quantity per fetch. the maximum value is 1000.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

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
    def Month(self):
        r"""Month, which is the current month by default if not provided.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def Type(self):
        r"""Public area policy type, for filtering.
Enumeration values are as follows:. 
1 - custom sharing proportion. 
2 - proportional allocation. 
3 - allocation by proportion.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        r"""Sharing rule name or cost allocation unit name, used for fuzzy filter criteria.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Month = params.get("Month")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationRuleSummaryResponse(AbstractModel):
    r"""DescribeAllocationRuleSummary response structure.

    """

    def __init__(self):
        r"""
        :param _RuleList: Sharing rule expression.
        :type RuleList: list of AllocationRuleOverview
        :param _Total: Total number of rules.
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleList = None
        self._Total = None
        self._RequestId = None

    @property
    def RuleList(self):
        r"""Sharing rule expression.
        :rtype: list of AllocationRuleOverview
        """
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def Total(self):
        r"""Total number of rules.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = AllocationRuleOverview()
                obj._deserialize(item)
                self._RuleList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeAllocationSummaryByBusinessRequest(AbstractModel):
    r"""DescribeAllocationSummaryByBusiness request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Quantity, with the maximum value of 1,000
        :type Limit: int
        :param _Offset: Pagination offset. If Offset is 0, it indicates the first page. If Limit is 100, then Offset is 100, and it indicates the second page. If Offset is 200, it indicates the third page, and so on.
        :type Offset: int
        :param _Month: Bill month, in the format of 2024-02, which is the current month by default if not provided


        :type Month: str
        :param _PeriodType: Statistical period, with the enumerated values as follows:
month - Month
day - Day
        :type PeriodType: str
        :param _TreeNodeUniqKeys: Unique identifier of a billing unit, used for filtering


        :type TreeNodeUniqKeys: list of str
        :param _SortType: Sorting type, with the enumerated values as follows:
asc - Ascending
desc - Descending
        :type SortType: str
        :param _Sort: Sorting field, with the enumerated values as follows:
GatherCashPayAmount - Collected fees (cash)
GatherVoucherPayAmount - Collected fees (voucher)
GatherIncentivePayAmount - Collected fees (free credit)
GatherTransferPayAmount - Collected fees (royalty amount)
AllocateCashPayAmount - Allocated fees (cash)
AllocateVoucherPayAmount - Allocated fees (voucher)
AllocateIncentivePayAmount - Allocated fees (free credit)
AllocateTransferPayAmount - Allocated fees (royalty amount)
TotalCashPayAmount - Total fees (cash)
TotalVoucherPayAmount - Total fees (voucher)
TotalIncentivePayAmount - Total fees (free credit)
TotalTransferPayAmount - Total fees (royalty amount)
GatherRealCost - Collected fees (discounted total)
AllocateRealCost - Allocated fees (discounted total)
RealTotalCost - Total fees (discounted total)
BusinessCode - Product code
Ratio - Proportion (discounted total)
Trend - Month-on-month ratio (discounted total)
        :type Sort: str
        :param _BillDates: Date, used for filtering and provided when PeriodType is set to day

        :type BillDates: list of str
        :param _BusinessCodes: Product code, used for filtering
        :type BusinessCodes: list of str
        :param _SearchKey: Fuzzy search criteria
        :type SearchKey: str
        """
        self._Limit = None
        self._Offset = None
        self._Month = None
        self._PeriodType = None
        self._TreeNodeUniqKeys = None
        self._SortType = None
        self._Sort = None
        self._BillDates = None
        self._BusinessCodes = None
        self._SearchKey = None

    @property
    def Limit(self):
        r"""Quantity, with the maximum value of 1,000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Pagination offset. If Offset is 0, it indicates the first page. If Limit is 100, then Offset is 100, and it indicates the second page. If Offset is 200, it indicates the third page, and so on.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Month(self):
        r"""Bill month, in the format of 2024-02, which is the current month by default if not provided


        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PeriodType(self):
        r"""Statistical period, with the enumerated values as follows:
month - Month
day - Day
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType

    @property
    def TreeNodeUniqKeys(self):
        r"""Unique identifier of a billing unit, used for filtering


        :rtype: list of str
        """
        return self._TreeNodeUniqKeys

    @TreeNodeUniqKeys.setter
    def TreeNodeUniqKeys(self, TreeNodeUniqKeys):
        self._TreeNodeUniqKeys = TreeNodeUniqKeys

    @property
    def SortType(self):
        r"""Sorting type, with the enumerated values as follows:
asc - Ascending
desc - Descending
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def Sort(self):
        r"""Sorting field, with the enumerated values as follows:
GatherCashPayAmount - Collected fees (cash)
GatherVoucherPayAmount - Collected fees (voucher)
GatherIncentivePayAmount - Collected fees (free credit)
GatherTransferPayAmount - Collected fees (royalty amount)
AllocateCashPayAmount - Allocated fees (cash)
AllocateVoucherPayAmount - Allocated fees (voucher)
AllocateIncentivePayAmount - Allocated fees (free credit)
AllocateTransferPayAmount - Allocated fees (royalty amount)
TotalCashPayAmount - Total fees (cash)
TotalVoucherPayAmount - Total fees (voucher)
TotalIncentivePayAmount - Total fees (free credit)
TotalTransferPayAmount - Total fees (royalty amount)
GatherRealCost - Collected fees (discounted total)
AllocateRealCost - Allocated fees (discounted total)
RealTotalCost - Total fees (discounted total)
BusinessCode - Product code
Ratio - Proportion (discounted total)
Trend - Month-on-month ratio (discounted total)
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def BillDates(self):
        r"""Date, used for filtering and provided when PeriodType is set to day

        :rtype: list of str
        """
        return self._BillDates

    @BillDates.setter
    def BillDates(self, BillDates):
        self._BillDates = BillDates

    @property
    def BusinessCodes(self):
        r"""Product code, used for filtering
        :rtype: list of str
        """
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def SearchKey(self):
        warnings.warn("parameter `SearchKey` is deprecated", DeprecationWarning) 

        r"""Fuzzy search criteria
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        warnings.warn("parameter `SearchKey` is deprecated", DeprecationWarning) 

        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Month = params.get("Month")
        self._PeriodType = params.get("PeriodType")
        self._TreeNodeUniqKeys = params.get("TreeNodeUniqKeys")
        self._SortType = params.get("SortType")
        self._Sort = params.get("Sort")
        self._BillDates = params.get("BillDates")
        self._BusinessCodes = params.get("BusinessCodes")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationSummaryByBusinessResponse(AbstractModel):
    r"""DescribeAllocationSummaryByBusiness response structure.

    """

    def __init__(self):
        r"""
        :param _RecordNum: Total quantity.
        :type RecordNum: int
        :param _Total: Total amount of a cost allocation bill

        :type Total: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        :param _Detail: Detailed summary of the cost allocation bill by business
        :type Detail: list of AllocationSummaryByBusiness
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecordNum = None
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def RecordNum(self):
        r"""Total quantity.
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def Total(self):
        r"""Total amount of a cost allocation bill

        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        r"""Detailed summary of the cost allocation bill by business
        :rtype: list of AllocationSummaryByBusiness
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

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
        self._RecordNum = params.get("RecordNum")
        if params.get("Total") is not None:
            self._Total = AllocationOverviewTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = AllocationSummaryByBusiness()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllocationSummaryByItemRequest(AbstractModel):
    r"""DescribeAllocationSummaryByItem request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Quantity, with the maximum value of 1,000


        :type Limit: int
        :param _Offset: Pagination offset. If Offset is 0, it indicates the first page. If Limit is 100, then Offset is 100, and it indicates the second page. If Offset is 200, it indicates the third page, and so on.
        :type Offset: int
        :param _Month: Bill month, in the format of 2024-02, which is the current month by default if not provided


        :type Month: str
        :param _PeriodType: Statistical period, with the enumerated values as follows:
month - Month
day - Day
        :type PeriodType: str
        :param _TreeNodeUniqKeys: Unique identifier of a billing unit, used for filtering


        :type TreeNodeUniqKeys: list of str
        :param _Sort: Sorting field, with the enumerated values as follows:
RiTimeSpan - Deduction duration of a reserved instance
ExtendPayAmount1 - Original price for the deduction duration of a reserved instance
RealCost - Discounted total
CashPayAmount - Cash amount
VoucherPayAmount - Amount of promo voucher
IncentivePayAmount - Amount of free credit
TransferPayAmount - Royalty amount
Cost - Original price of a component
        :type Sort: str
        :param _SortType: Sorting type, with the enumerated values as follows:
asc - Ascending
desc - Descending
        :type SortType: str
        :param _BillDates: Date, used for filtering


        :type BillDates: list of str
        :param _BusinessCodes: Product code, used for filtering


        :type BusinessCodes: list of str
        :param _OwnerUins: User UIN, used for filtering


        :type OwnerUins: list of str
        :param _OperateUins: Operator UIN, used for filtering


        :type OperateUins: list of str
        :param _PayModes: Billing mode code, used for filtering


        :type PayModes: list of str
        :param _ActionTypes: Transaction type code, used for filtering


        :type ActionTypes: list of str
        :param _ProductCodes: Subproduct code, used for filtering


        :type ProductCodes: list of str
        :param _RegionIds: Region ID, used for filtering


        :type RegionIds: list of str
        :param _ZoneIds: Availability Zone (AZ) ID, used for filtering


        :type ZoneIds: list of str
        :param _InstanceTypes: Instance type code, used for filtering


        :type InstanceTypes: list of str
        :param _Tag: Tag, used for filtering


        :type Tag: list of str
        :param _ComponentCodes: Component type code, used for filtering
        :type ComponentCodes: list of str
        :param _ItemCodes: Component name code, used for filtering
        :type ItemCodes: list of str
        :param _SearchKey: Fuzzy search: supports tag, resource ID, and resource alias.
        :type SearchKey: str
        :param _ProjectIds: Project ID, used for filtering


        :type ProjectIds: list of int non-negative
        :param _AllocationType: Cost collection type, with the enumerated values as follows:
0 - Allocation
1 - Collection
-1 - Unallocated
        :type AllocationType: list of int
        """
        self._Limit = None
        self._Offset = None
        self._Month = None
        self._PeriodType = None
        self._TreeNodeUniqKeys = None
        self._Sort = None
        self._SortType = None
        self._BillDates = None
        self._BusinessCodes = None
        self._OwnerUins = None
        self._OperateUins = None
        self._PayModes = None
        self._ActionTypes = None
        self._ProductCodes = None
        self._RegionIds = None
        self._ZoneIds = None
        self._InstanceTypes = None
        self._Tag = None
        self._ComponentCodes = None
        self._ItemCodes = None
        self._SearchKey = None
        self._ProjectIds = None
        self._AllocationType = None

    @property
    def Limit(self):
        r"""Quantity, with the maximum value of 1,000


        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Pagination offset. If Offset is 0, it indicates the first page. If Limit is 100, then Offset is 100, and it indicates the second page. If Offset is 200, it indicates the third page, and so on.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Month(self):
        r"""Bill month, in the format of 2024-02, which is the current month by default if not provided


        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PeriodType(self):
        r"""Statistical period, with the enumerated values as follows:
month - Month
day - Day
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType

    @property
    def TreeNodeUniqKeys(self):
        r"""Unique identifier of a billing unit, used for filtering


        :rtype: list of str
        """
        return self._TreeNodeUniqKeys

    @TreeNodeUniqKeys.setter
    def TreeNodeUniqKeys(self, TreeNodeUniqKeys):
        self._TreeNodeUniqKeys = TreeNodeUniqKeys

    @property
    def Sort(self):
        r"""Sorting field, with the enumerated values as follows:
RiTimeSpan - Deduction duration of a reserved instance
ExtendPayAmount1 - Original price for the deduction duration of a reserved instance
RealCost - Discounted total
CashPayAmount - Cash amount
VoucherPayAmount - Amount of promo voucher
IncentivePayAmount - Amount of free credit
TransferPayAmount - Royalty amount
Cost - Original price of a component
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def SortType(self):
        r"""Sorting type, with the enumerated values as follows:
asc - Ascending
desc - Descending
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def BillDates(self):
        r"""Date, used for filtering


        :rtype: list of str
        """
        return self._BillDates

    @BillDates.setter
    def BillDates(self, BillDates):
        self._BillDates = BillDates

    @property
    def BusinessCodes(self):
        r"""Product code, used for filtering


        :rtype: list of str
        """
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def OwnerUins(self):
        r"""User UIN, used for filtering


        :rtype: list of str
        """
        return self._OwnerUins

    @OwnerUins.setter
    def OwnerUins(self, OwnerUins):
        self._OwnerUins = OwnerUins

    @property
    def OperateUins(self):
        r"""Operator UIN, used for filtering


        :rtype: list of str
        """
        return self._OperateUins

    @OperateUins.setter
    def OperateUins(self, OperateUins):
        self._OperateUins = OperateUins

    @property
    def PayModes(self):
        r"""Billing mode code, used for filtering


        :rtype: list of str
        """
        return self._PayModes

    @PayModes.setter
    def PayModes(self, PayModes):
        self._PayModes = PayModes

    @property
    def ActionTypes(self):
        r"""Transaction type code, used for filtering


        :rtype: list of str
        """
        return self._ActionTypes

    @ActionTypes.setter
    def ActionTypes(self, ActionTypes):
        self._ActionTypes = ActionTypes

    @property
    def ProductCodes(self):
        r"""Subproduct code, used for filtering


        :rtype: list of str
        """
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes

    @property
    def RegionIds(self):
        r"""Region ID, used for filtering


        :rtype: list of str
        """
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def ZoneIds(self):
        r"""Availability Zone (AZ) ID, used for filtering


        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def InstanceTypes(self):
        r"""Instance type code, used for filtering


        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def Tag(self):
        r"""Tag, used for filtering


        :rtype: list of str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ComponentCodes(self):
        r"""Component type code, used for filtering
        :rtype: list of str
        """
        return self._ComponentCodes

    @ComponentCodes.setter
    def ComponentCodes(self, ComponentCodes):
        self._ComponentCodes = ComponentCodes

    @property
    def ItemCodes(self):
        r"""Component name code, used for filtering
        :rtype: list of str
        """
        return self._ItemCodes

    @ItemCodes.setter
    def ItemCodes(self, ItemCodes):
        self._ItemCodes = ItemCodes

    @property
    def SearchKey(self):
        r"""Fuzzy search: supports tag, resource ID, and resource alias.
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ProjectIds(self):
        r"""Project ID, used for filtering


        :rtype: list of int non-negative
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def AllocationType(self):
        r"""Cost collection type, with the enumerated values as follows:
0 - Allocation
1 - Collection
-1 - Unallocated
        :rtype: list of int
        """
        return self._AllocationType

    @AllocationType.setter
    def AllocationType(self, AllocationType):
        self._AllocationType = AllocationType


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Month = params.get("Month")
        self._PeriodType = params.get("PeriodType")
        self._TreeNodeUniqKeys = params.get("TreeNodeUniqKeys")
        self._Sort = params.get("Sort")
        self._SortType = params.get("SortType")
        self._BillDates = params.get("BillDates")
        self._BusinessCodes = params.get("BusinessCodes")
        self._OwnerUins = params.get("OwnerUins")
        self._OperateUins = params.get("OperateUins")
        self._PayModes = params.get("PayModes")
        self._ActionTypes = params.get("ActionTypes")
        self._ProductCodes = params.get("ProductCodes")
        self._RegionIds = params.get("RegionIds")
        self._ZoneIds = params.get("ZoneIds")
        self._InstanceTypes = params.get("InstanceTypes")
        self._Tag = params.get("Tag")
        self._ComponentCodes = params.get("ComponentCodes")
        self._ItemCodes = params.get("ItemCodes")
        self._SearchKey = params.get("SearchKey")
        self._ProjectIds = params.get("ProjectIds")
        self._AllocationType = params.get("AllocationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationSummaryByItemResponse(AbstractModel):
    r"""DescribeAllocationSummaryByItem response structure.

    """

    def __init__(self):
        r"""
        :param _RecordNum: Total quantity.

        :type RecordNum: int
        :param _Total: Total amount of a cost allocation bill
        :type Total: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        :param _Detail: Details of a Cost Allocation Bill by item

        :type Detail: list of AllocationSummaryByItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecordNum = None
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def RecordNum(self):
        r"""Total quantity.

        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def Total(self):
        r"""Total amount of a cost allocation bill
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        r"""Details of a Cost Allocation Bill by item

        :rtype: list of AllocationSummaryByItem
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

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
        self._RecordNum = params.get("RecordNum")
        if params.get("Total") is not None:
            self._Total = AllocationOverviewTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = AllocationSummaryByItem()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllocationSummaryByResourceRequest(AbstractModel):
    r"""DescribeAllocationSummaryByResource request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Quantity, with the maximum value of 1,000


        :type Limit: int
        :param _Offset: Pagination offset. If Offset is 0, it indicates the first page. If Limit is 100, then Offset is 100, and it indicates the second page. If Offset is 200, it indicates the third page, and so on.
        :type Offset: int
        :param _Month: Bill month, in the format of 2024-02, which is the current month by default if not provided


        :type Month: str
        :param _PeriodType: Statistical period, with the enumerated values as follows:
month - Month
day - Day
        :type PeriodType: str
        :param _TreeNodeUniqKeys: Unique identifier of a billing unit, used for filtering
        :type TreeNodeUniqKeys: list of str
        :param _Sort: Sorting field, with the enumerated values as follows:
RiTimeSpan - Deduction duration of a reserved instance
ExtendPayAmount1 - Original price for the deduction duration of a reserved instance
RealCost - Discounted total
CashPayAmount - Cash amount
VoucherPayAmount - Amount of promo voucher
IncentivePayAmount - Amount of free credit
TransferPayAmount - Royalty amount
Cost - Original price of a component
        :type Sort: str
        :param _SortType: Sorting type, with the enumerated values as follows:
asc - Ascending
desc - Descending
        :type SortType: str
        :param _BillDates: Date, used for filtering
        :type BillDates: list of str
        :param _BusinessCodes: Product code, used for filtering
        :type BusinessCodes: list of str
        :param _OwnerUins: User UIN, used for filtering
        :type OwnerUins: list of str
        :param _OperateUins: Operator UIN, used for filtering
        :type OperateUins: list of str
        :param _PayModes: Billing mode code, used for filtering
        :type PayModes: list of str
        :param _ActionTypes: Transaction type code, used for filtering
        :type ActionTypes: list of str
        :param _ProductCodes: Subproduct code, used for filtering
        :type ProductCodes: list of str
        :param _RegionIds: Region ID, used for filtering
        :type RegionIds: list of str
        :param _ZoneIds: Availability zone (AZ) ID, used for filtering
        :type ZoneIds: list of str
        :param _InstanceTypes: Instance type code, used for filtering
        :type InstanceTypes: list of str
        :param _Tag: Tag, used for filtering
        :type Tag: list of str
        :param _SearchKey: Fuzzy search: supports tag, resource ID, and resource alias
        :type SearchKey: str
        :param _ProjectIds: Project ID, used for filtering
        :type ProjectIds: list of int non-negative
        :param _AllocationType: Cost collection type, with the enumerated values as follows:
0 - Allocation 
1 - Collection 
-1 - Unallocated
        :type AllocationType: list of int
        """
        self._Limit = None
        self._Offset = None
        self._Month = None
        self._PeriodType = None
        self._TreeNodeUniqKeys = None
        self._Sort = None
        self._SortType = None
        self._BillDates = None
        self._BusinessCodes = None
        self._OwnerUins = None
        self._OperateUins = None
        self._PayModes = None
        self._ActionTypes = None
        self._ProductCodes = None
        self._RegionIds = None
        self._ZoneIds = None
        self._InstanceTypes = None
        self._Tag = None
        self._SearchKey = None
        self._ProjectIds = None
        self._AllocationType = None

    @property
    def Limit(self):
        r"""Quantity, with the maximum value of 1,000


        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Pagination offset. If Offset is 0, it indicates the first page. If Limit is 100, then Offset is 100, and it indicates the second page. If Offset is 200, it indicates the third page, and so on.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Month(self):
        r"""Bill month, in the format of 2024-02, which is the current month by default if not provided


        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PeriodType(self):
        r"""Statistical period, with the enumerated values as follows:
month - Month
day - Day
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType

    @property
    def TreeNodeUniqKeys(self):
        r"""Unique identifier of a billing unit, used for filtering
        :rtype: list of str
        """
        return self._TreeNodeUniqKeys

    @TreeNodeUniqKeys.setter
    def TreeNodeUniqKeys(self, TreeNodeUniqKeys):
        self._TreeNodeUniqKeys = TreeNodeUniqKeys

    @property
    def Sort(self):
        r"""Sorting field, with the enumerated values as follows:
RiTimeSpan - Deduction duration of a reserved instance
ExtendPayAmount1 - Original price for the deduction duration of a reserved instance
RealCost - Discounted total
CashPayAmount - Cash amount
VoucherPayAmount - Amount of promo voucher
IncentivePayAmount - Amount of free credit
TransferPayAmount - Royalty amount
Cost - Original price of a component
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def SortType(self):
        r"""Sorting type, with the enumerated values as follows:
asc - Ascending
desc - Descending
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def BillDates(self):
        r"""Date, used for filtering
        :rtype: list of str
        """
        return self._BillDates

    @BillDates.setter
    def BillDates(self, BillDates):
        self._BillDates = BillDates

    @property
    def BusinessCodes(self):
        r"""Product code, used for filtering
        :rtype: list of str
        """
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def OwnerUins(self):
        r"""User UIN, used for filtering
        :rtype: list of str
        """
        return self._OwnerUins

    @OwnerUins.setter
    def OwnerUins(self, OwnerUins):
        self._OwnerUins = OwnerUins

    @property
    def OperateUins(self):
        r"""Operator UIN, used for filtering
        :rtype: list of str
        """
        return self._OperateUins

    @OperateUins.setter
    def OperateUins(self, OperateUins):
        self._OperateUins = OperateUins

    @property
    def PayModes(self):
        r"""Billing mode code, used for filtering
        :rtype: list of str
        """
        return self._PayModes

    @PayModes.setter
    def PayModes(self, PayModes):
        self._PayModes = PayModes

    @property
    def ActionTypes(self):
        r"""Transaction type code, used for filtering
        :rtype: list of str
        """
        return self._ActionTypes

    @ActionTypes.setter
    def ActionTypes(self, ActionTypes):
        self._ActionTypes = ActionTypes

    @property
    def ProductCodes(self):
        r"""Subproduct code, used for filtering
        :rtype: list of str
        """
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes

    @property
    def RegionIds(self):
        r"""Region ID, used for filtering
        :rtype: list of str
        """
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def ZoneIds(self):
        r"""Availability zone (AZ) ID, used for filtering
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def InstanceTypes(self):
        r"""Instance type code, used for filtering
        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def Tag(self):
        r"""Tag, used for filtering
        :rtype: list of str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def SearchKey(self):
        r"""Fuzzy search: supports tag, resource ID, and resource alias
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ProjectIds(self):
        r"""Project ID, used for filtering
        :rtype: list of int non-negative
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def AllocationType(self):
        r"""Cost collection type, with the enumerated values as follows:
0 - Allocation 
1 - Collection 
-1 - Unallocated
        :rtype: list of int
        """
        return self._AllocationType

    @AllocationType.setter
    def AllocationType(self, AllocationType):
        self._AllocationType = AllocationType


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Month = params.get("Month")
        self._PeriodType = params.get("PeriodType")
        self._TreeNodeUniqKeys = params.get("TreeNodeUniqKeys")
        self._Sort = params.get("Sort")
        self._SortType = params.get("SortType")
        self._BillDates = params.get("BillDates")
        self._BusinessCodes = params.get("BusinessCodes")
        self._OwnerUins = params.get("OwnerUins")
        self._OperateUins = params.get("OperateUins")
        self._PayModes = params.get("PayModes")
        self._ActionTypes = params.get("ActionTypes")
        self._ProductCodes = params.get("ProductCodes")
        self._RegionIds = params.get("RegionIds")
        self._ZoneIds = params.get("ZoneIds")
        self._InstanceTypes = params.get("InstanceTypes")
        self._Tag = params.get("Tag")
        self._SearchKey = params.get("SearchKey")
        self._ProjectIds = params.get("ProjectIds")
        self._AllocationType = params.get("AllocationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationSummaryByResourceResponse(AbstractModel):
    r"""DescribeAllocationSummaryByResource response structure.

    """

    def __init__(self):
        r"""
        :param _RecordNum: Total quantity.

        :type RecordNum: int
        :param _Total: Total amount of a cost allocation bill

        :type Total: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        :param _Detail: Detailed summary of the cost allocation bill by resource

        :type Detail: list of AllocationSummaryByResource
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecordNum = None
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def RecordNum(self):
        r"""Total quantity.

        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def Total(self):
        r"""Total amount of a cost allocation bill

        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        r"""Detailed summary of the cost allocation bill by resource

        :rtype: list of AllocationSummaryByResource
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

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
        self._RecordNum = params.get("RecordNum")
        if params.get("Total") is not None:
            self._Total = AllocationOverviewTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = AllocationSummaryByResource()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllocationTreeRequest(AbstractModel):
    r"""DescribeAllocationTree request structure.

    """

    def __init__(self):
        r"""
        :param _Month: Month, the current month by default if not provided.
        :type Month: str
        """
        self._Month = None

    @property
    def Month(self):
        r"""Month, the current month by default if not provided.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month


    def _deserialize(self, params):
        self._Month = params.get("Month")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationTreeResponse(AbstractModel):
    r"""DescribeAllocationTree response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Cost allocation unit ID.
        :type Id: int
        :param _Name: Specifies the name of a cost allocation unit.
        :type Name: str
        :param _TreeNodeUniqKey: Unique identifier of a cost allocation unit
        :type TreeNodeUniqKey: str
        :param _Children: Specifies a subtree.
        :type Children: list of AllocationTree
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._Name = None
        self._TreeNodeUniqKey = None
        self._Children = None
        self._RequestId = None

    @property
    def Id(self):
        r"""Cost allocation unit ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""Specifies the name of a cost allocation unit.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TreeNodeUniqKey(self):
        r"""Unique identifier of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def Children(self):
        r"""Specifies a subtree.
        :rtype: list of AllocationTree
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children

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
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = AllocationTree()
                obj._deserialize(item)
                self._Children.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllocationTrendByMonthRequest(AbstractModel):
    r"""DescribeAllocationTrendByMonth request structure.

    """

    def __init__(self):
        r"""
        :param _Month: Bill month, in the format of 2024-02, which is the current month by default if not provided
        :type Month: str
        :param _TreeNodeUniqKey: Unique identifier of a cost allocation unit
        :type TreeNodeUniqKey: str
        :param _BusinessCode: Product code, used for filtering
        :type BusinessCode: str
        """
        self._Month = None
        self._TreeNodeUniqKey = None
        self._BusinessCode = None

    @property
    def Month(self):
        r"""Bill month, in the format of 2024-02, which is the current month by default if not provided
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def TreeNodeUniqKey(self):
        r"""Unique identifier of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def BusinessCode(self):
        r"""Product code, used for filtering
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._BusinessCode = params.get("BusinessCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationTrendByMonthResponse(AbstractModel):
    r"""DescribeAllocationTrendByMonth response structure.

    """

    def __init__(self):
        r"""
        :param _Current: Current month's expense information
        :type Current: :class:`tencentcloud.billing.v20180709.models.AllocationBillTrendDetail`
        :param _Previous: Previous months' expense information
        :type Previous: list of AllocationBillTrendDetail
        :param _Stat: Expense statistical information
        :type Stat: :class:`tencentcloud.billing.v20180709.models.AllocationStat`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Current = None
        self._Previous = None
        self._Stat = None
        self._RequestId = None

    @property
    def Current(self):
        r"""Current month's expense information
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationBillTrendDetail`
        """
        return self._Current

    @Current.setter
    def Current(self, Current):
        self._Current = Current

    @property
    def Previous(self):
        r"""Previous months' expense information
        :rtype: list of AllocationBillTrendDetail
        """
        return self._Previous

    @Previous.setter
    def Previous(self, Previous):
        self._Previous = Previous

    @property
    def Stat(self):
        r"""Expense statistical information
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationStat`
        """
        return self._Stat

    @Stat.setter
    def Stat(self, Stat):
        self._Stat = Stat

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
        if params.get("Current") is not None:
            self._Current = AllocationBillTrendDetail()
            self._Current._deserialize(params.get("Current"))
        if params.get("Previous") is not None:
            self._Previous = []
            for item in params.get("Previous"):
                obj = AllocationBillTrendDetail()
                obj._deserialize(item)
                self._Previous.append(obj)
        if params.get("Stat") is not None:
            self._Stat = AllocationStat()
            self._Stat._deserialize(params.get("Stat"))
        self._RequestId = params.get("RequestId")


class DescribeAllocationUnitDetailRequest(AbstractModel):
    r"""DescribeAllocationUnitDetail request structure.

    """

    def __init__(self):
        r"""
        :param _Id: ID of the queried cost allocation unit.
        :type Id: int
        :param _Month: Month, the current month by default if not provided.
        :type Month: str
        """
        self._Id = None
        self._Month = None

    @property
    def Id(self):
        r"""ID of the queried cost allocation unit.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Month(self):
        r"""Month, the current month by default if not provided.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Month = params.get("Month")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationUnitDetailResponse(AbstractModel):
    r"""DescribeAllocationUnitDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Id: ID of a cost allocation unit.
        :type Id: int
        :param _Uin: Associated UIN of the cost allocation unit.
        :type Uin: str
        :param _Name: Specifies the name of a cost allocation unit.
        :type Name: str
        :param _ParentId: Cost allocation unit parent node ID.
        :type ParentId: int
        :param _SourceName: Source organization name.
        :type SourceName: str
        :param _SourceId: Source organization ID.
        :type SourceId: str
        :param _Remark: Specifies remark description.
        :type Remark: str
        :param _TreeNodeUniqKey: Cost allocation unit identifier.
        :type TreeNodeUniqKey: str
        :param _RuleId: If a cost allocation unit is set with an collection rule, return the collection rule ID. if no collection rule is set, do not return.
        :type RuleId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._Uin = None
        self._Name = None
        self._ParentId = None
        self._SourceName = None
        self._SourceId = None
        self._Remark = None
        self._TreeNodeUniqKey = None
        self._RuleId = None
        self._RequestId = None

    @property
    def Id(self):
        r"""ID of a cost allocation unit.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uin(self):
        r"""Associated UIN of the cost allocation unit.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Name(self):
        r"""Specifies the name of a cost allocation unit.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParentId(self):
        r"""Cost allocation unit parent node ID.
        :rtype: int
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def SourceName(self):
        r"""Source organization name.
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def SourceId(self):
        r"""Source organization ID.
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def Remark(self):
        r"""Specifies remark description.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TreeNodeUniqKey(self):
        r"""Cost allocation unit identifier.
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def RuleId(self):
        r"""If a cost allocation unit is set with an collection rule, return the collection rule ID. if no collection rule is set, do not return.
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

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
        self._Id = params.get("Id")
        self._Uin = params.get("Uin")
        self._Name = params.get("Name")
        self._ParentId = params.get("ParentId")
        self._SourceName = params.get("SourceName")
        self._SourceId = params.get("SourceId")
        self._Remark = params.get("Remark")
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class DescribeBillAdjustInfoRequest(AbstractModel):
    r"""DescribeBillAdjustInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Month: <p>Format: yyyy-MM<br>Bill month. Either month or timeFrom&amp;timeTo must be specified. If timeFrom&amp;timeTo is specified, the month field is invalid.</p>
        :type Month: str
        :param _TimeFrom: <p>Format: yyyy-MM-dd<br>Start time. Either month or timeFrom&amp;timeTo must be specified. If timeFrom&amp;timeTo is specified, the month field is invalid. timeFrom and timeTo must be specified together and must be in the same month. Cross-month queries are not supported and the query results are data for the entire month.</p>
        :type TimeFrom: str
        :param _TimeTo: <p>Format: yyyy-MM-dd<br>End time. Either month or timeFrom&amp;timeTo must be specified. If this field is specified, the month field is invalid. timeFrom and timeTo must be passed together and be in the same month. Cross-month queries are not supported. The query result is data of the entire month.</p>
        :type TimeTo: str
        :param _PayerUin: <p>Account ID of the payer (Account ID is the unique account identifier for the user in Tencent Cloud). By default, the query returns the account statement of the current account. If the group management account needs to query the self-pay bills of member accounts, enter the member account UIN in this field.</p>
        :type PayerUin: str
        """
        self._Month = None
        self._TimeFrom = None
        self._TimeTo = None
        self._PayerUin = None

    @property
    def Month(self):
        r"""<p>Format: yyyy-MM<br>Bill month. Either month or timeFrom&amp;timeTo must be specified. If timeFrom&amp;timeTo is specified, the month field is invalid.</p>
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def TimeFrom(self):
        r"""<p>Format: yyyy-MM-dd<br>Start time. Either month or timeFrom&amp;timeTo must be specified. If timeFrom&amp;timeTo is specified, the month field is invalid. timeFrom and timeTo must be specified together and must be in the same month. Cross-month queries are not supported and the query results are data for the entire month.</p>
        :rtype: str
        """
        return self._TimeFrom

    @TimeFrom.setter
    def TimeFrom(self, TimeFrom):
        self._TimeFrom = TimeFrom

    @property
    def TimeTo(self):
        r"""<p>Format: yyyy-MM-dd<br>End time. Either month or timeFrom&amp;timeTo must be specified. If this field is specified, the month field is invalid. timeFrom and timeTo must be passed together and be in the same month. Cross-month queries are not supported. The query result is data of the entire month.</p>
        :rtype: str
        """
        return self._TimeTo

    @TimeTo.setter
    def TimeTo(self, TimeTo):
        self._TimeTo = TimeTo

    @property
    def PayerUin(self):
        r"""<p>Account ID of the payer (Account ID is the unique account identifier for the user in Tencent Cloud). By default, the query returns the account statement of the current account. If the group management account needs to query the self-pay bills of member accounts, enter the member account UIN in this field.</p>
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._TimeFrom = params.get("TimeFrom")
        self._TimeTo = params.get("TimeTo")
        self._PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillAdjustInfoResponse(AbstractModel):
    r"""DescribeBillAdjustInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Total: <p>Total data</p>
        :type Total: int
        :param _Data: <p>Detailed data</p>
        :type Data: list of AdjustInfoDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        r"""<p>Total data</p>
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        r"""<p>Detailed data</p>
        :rtype: list of AdjustInfoDetail
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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AdjustInfoDetail()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillDetailForOrganizationRequest(AbstractModel):
    r"""DescribeBillDetailForOrganization request structure.

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
        :param _PayMode: Billing mode, which can be `prePay` (yearly/monthly subscription) or `postPay` (pay-as-you-go).
        :type PayMode: str
        :param _ResourceId: ID of the instance to be queried.
        :type ResourceId: str
        :param _ActionType: Transaction type. This parameter needs to be input using the `ActionTypeName` value. Valid values:
Yearly/monthly subscription purchase
Yearly/monthly subscription renewal
Yearly/monthly subscription upgrade/downgrade
Yearly/monthly subscription refund 
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
Yearly/monthly subscription resource migration in 
Yearly/monthly subscription resource migration out 
Prepaid 
Hourly 
RI refund 
Pay-as-you-go reversal 
Yearly/monthly subscription to pay-as-you-go 
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
        r"""Pagination offset. If `Offset` is `0`, it indicates the first page. When `Limit` is `100`, if `Offset` is `100`, it indicates the second page; if `Offset` is `200`, it indicates the third page, and so on.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""The number of entries returned at a time. The maximum value is `100`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PeriodType(self):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        r"""Cycle type, which can be `byUsedTime` (by billing cycle) or `byPayTime` (by deduction time). This value must be the same as the billing period type in Billing Center for that particular month. You can check your billing cycle at the top of the [Bill Overview](https://console.cloud.tencent.com/expense/bill/overview) page.
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        self._PeriodType = PeriodType

    @property
    def Month(self):
        r"""The month is in the format of yyyy-mm. Either Month or BeginTime&EndTime must be specified. If BeginTime&EndTime is specified, the Month field is invalid. Data within the last 18 months can be pulled at most.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def BeginTime(self):
        r"""The start time of the period in the format of yyyy-mm-dd hh:ii:ss. Either Month or BeginTime&EndTime must be specified. If BeginTime&EndTime is specified, the Month field is invalid. BeginTime and EndTime must be specified together and must be in the same month. Cross-month queries are not supported and the query results are data for the entire month. Data within the last 18 months can be pulled at most.
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""The end time of the period in the format of yyyy-mm-dd hh:ii:ss. Either Month or BeginTime&EndTime must be specified. If BeginTime&EndTime is specified, the Month field is invalid. BeginTime and EndTime must be specified together and must be in the same month. Cross-month queries are not supported and the query results are data for the entire month. Data within the last 18 months can be pulled at most.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NeedRecordNum(self):
        r"""Indicates whether the total number of records is required, used for pagination.
Valid values: `1` (required), `0` (not required).
        :rtype: int
        """
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def PayMode(self):
        r"""Billing mode, which can be `prePay` (yearly/monthly subscription) or `postPay` (pay-as-you-go).
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResourceId(self):
        r"""ID of the instance to be queried.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ActionType(self):
        r"""Transaction type. This parameter needs to be input using the `ActionTypeName` value. Valid values:
Yearly/monthly subscription purchase
Yearly/monthly subscription renewal
Yearly/monthly subscription upgrade/downgrade
Yearly/monthly subscription refund 
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
Yearly/monthly subscription resource migration in 
Yearly/monthly subscription resource migration out 
Prepaid 
Hourly 
RI refund 
Pay-as-you-go reversal 
Yearly/monthly subscription to pay-as-you-go 
Minimum spend deduction 
Hourly savings plan fee
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ProjectId(self):
        r"""Project ID: The ID of the project to which the resource belongs.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def BusinessCode(self):
        r"""Product code.
Note: To query the product codes used in the current month, call <a href="https://intl.cloud.tencent.com/document/product/555/35761?from_cn_redirect=1">DescribeBillSummaryByProduct</a>.
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def Context(self):
        r"""Context information returned by the last response. You can view multiple pages when querying for data after May 2023 to speed up the query. We recommend you use this query method if your data volume is above 100 thousand entries, which can improve query speed by 2-10 times.
        :rtype: str
        """
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
    r"""DescribeBillDetailForOrganization response structure.

    """

    def __init__(self):
        r"""
        :param _DetailSet: Details list.
        :type DetailSet: list of DistributionBillDetail
        :param _Total: Total number of records, which is cached every 24 hours and may be less than the actual total number of records.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _Context: Context information of this request can be used in the request parameter of the next request to accelerate query speed.
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
        r"""Details list.
        :rtype: list of DistributionBillDetail
        """
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet

    @property
    def Total(self):
        r"""Total number of records, which is cached every 24 hours and may be less than the actual total number of records.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Context(self):
        r"""Context information of this request can be used in the request parameter of the next request to accelerate query speed.
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

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
    r"""DescribeBillDetail request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination offset. Offset=0 indicates the first page. If Limit=100, Offset=100 indicates the second page, Offset=200 indicates the third page, and so on.
        :type Offset: int
        :param _Limit: The number of entries returned at a time. The maximum value is `300`.
        :type Limit: int
        :param _PeriodType: Period type, byUsedTime by billing period/byPayTime by fee deduction cycle. It should be consistent with the billing cycle for the month in the expense center. You can go to the top of the [bill overview](https://console.cloud.tencent.com/expense/bill/overview) page to view and confirm your billing cycle type.
        :type PeriodType: str
        :param _Month: The month is in the format of yyyy-mm. Either Month or BeginTime&EndTime must be specified. If BeginTime&EndTime is specified, the Month field is invalid. Data within the last 18 months can be pulled at most.
        :type Month: str
        :param _BeginTime: The start time of the period in the format of yyyy-mm-dd hh:ii:ss. Either Month or BeginTime&EndTime must be specified. If BeginTime&EndTime is specified, the Month field is invalid. BeginTime and EndTime must be specified together and must be in the same month. Cross-month queries are not supported and the query results are data for the entire month. Data within the last 18 months can be pulled at most.
        :type BeginTime: str
        :param _EndTime: The end time of the period in the format of yyyy-mm-dd hh:ii:ss. Either Month or BeginTime&EndTime must be specified. If BeginTime&EndTime is specified, the Month field is invalid. BeginTime and EndTime must be specified together and must be in the same month. Cross-month queries are not supported and the query results are data for the entire month. Data within the last 18 months can be pulled at most.
        :type EndTime: str
        :param _NeedRecordNum: Total number of records for access list needed for frontend pagination
1: needed, 0: not needed
        :type NeedRecordNum: int
        :param _ProductCode: Queries information on a specified product
        :type ProductCode: str
        :param _PayMode: Billing mode: prePay/postPay
        :type PayMode: str
        :param _ResourceId: Queries information on a specified resource
        :type ResourceId: str
        :param _ActionType: Hourly settlement
Daily settlement
Yearly/monthly subscription
Spot
New yearly/monthly subscription
Yearly/monthly subscription renewal
Yearly/monthly subscription specification adjustment
Yearly/monthly subscription refund
Adjustment - deduction
Adjustment - refund
Hourly RI fee
One-off RI Fee
Hourly Savings Plan fee
Offline project deduction
Offline product deduction
        :type ActionType: str
        :param _ProjectId: Project ID: Project ID of the resource
        :type ProjectId: int
        :param _BusinessCode: Product name code
Remark: If needed to obtain BusinessCode used in current month, invoke API: <a href="https://www.tencentcloud.com/document/product/555/35761?from_cn_redirect=1">Get fee distribution by product</a>
        :type BusinessCode: str
        :param _Context: Context information returned from the last request. Paginated query of data for months with Month>=2023-05 can speed up query speed. Recommended for users with data volume at tens of thousands level. Query speed can be improved by 2-10x.
        :type Context: str
        :param _PayerUin: Account ID of the payer (Account ID is the unique account identifier for the user in Tencent Cloud). By default, the query returns the account statement of the current account. If the group management account needs to query the self-pay bills of member accounts, enter the member account UIN in this field.
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
        r"""Pagination offset. Offset=0 indicates the first page. If Limit=100, Offset=100 indicates the second page, Offset=200 indicates the third page, and so on.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""The number of entries returned at a time. The maximum value is `300`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PeriodType(self):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        r"""Period type, byUsedTime by billing period/byPayTime by fee deduction cycle. It should be consistent with the billing cycle for the month in the expense center. You can go to the top of the [bill overview](https://console.cloud.tencent.com/expense/bill/overview) page to view and confirm your billing cycle type.
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        self._PeriodType = PeriodType

    @property
    def Month(self):
        r"""The month is in the format of yyyy-mm. Either Month or BeginTime&EndTime must be specified. If BeginTime&EndTime is specified, the Month field is invalid. Data within the last 18 months can be pulled at most.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def BeginTime(self):
        r"""The start time of the period in the format of yyyy-mm-dd hh:ii:ss. Either Month or BeginTime&EndTime must be specified. If BeginTime&EndTime is specified, the Month field is invalid. BeginTime and EndTime must be specified together and must be in the same month. Cross-month queries are not supported and the query results are data for the entire month. Data within the last 18 months can be pulled at most.
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""The end time of the period in the format of yyyy-mm-dd hh:ii:ss. Either Month or BeginTime&EndTime must be specified. If BeginTime&EndTime is specified, the Month field is invalid. BeginTime and EndTime must be specified together and must be in the same month. Cross-month queries are not supported and the query results are data for the entire month. Data within the last 18 months can be pulled at most.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NeedRecordNum(self):
        r"""Total number of records for access list needed for frontend pagination
1: needed, 0: not needed
        :rtype: int
        """
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def ProductCode(self):
        warnings.warn("parameter `ProductCode` is deprecated", DeprecationWarning) 

        r"""Queries information on a specified product
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        warnings.warn("parameter `ProductCode` is deprecated", DeprecationWarning) 

        self._ProductCode = ProductCode

    @property
    def PayMode(self):
        r"""Billing mode: prePay/postPay
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResourceId(self):
        r"""Queries information on a specified resource
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ActionType(self):
        r"""Hourly settlement
Daily settlement
Yearly/monthly subscription
Spot
New yearly/monthly subscription
Yearly/monthly subscription renewal
Yearly/monthly subscription specification adjustment
Yearly/monthly subscription refund
Adjustment - deduction
Adjustment - refund
Hourly RI fee
One-off RI Fee
Hourly Savings Plan fee
Offline project deduction
Offline product deduction
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ProjectId(self):
        r"""Project ID: Project ID of the resource
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def BusinessCode(self):
        r"""Product name code
Remark: If needed to obtain BusinessCode used in current month, invoke API: <a href="https://www.tencentcloud.com/document/product/555/35761?from_cn_redirect=1">Get fee distribution by product</a>
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def Context(self):
        r"""Context information returned from the last request. Paginated query of data for months with Month>=2023-05 can speed up query speed. Recommended for users with data volume at tens of thousands level. Query speed can be improved by 2-10x.
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def PayerUin(self):
        r"""Account ID of the payer (Account ID is the unique account identifier for the user in Tencent Cloud). By default, the query returns the account statement of the current account. If the group management account needs to query the self-pay bills of member accounts, enter the member account UIN in this field.
        :rtype: str
        """
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
    r"""DescribeBillDetail response structure.

    """

    def __init__(self):
        r"""
        :param _DetailSet: Detail list
        :type DetailSet: list of BillDetail
        :param _Total: Total record count, cached once every 24 hours, may be less than the actual total record count
        :type Total: int
        :param _Context: Context information of this request can be used in the request parameter of the next request to accelerate query speed.
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
        r"""Detail list
        :rtype: list of BillDetail
        """
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet

    @property
    def Total(self):
        r"""Total record count, cached once every 24 hours, may be less than the actual total record count
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Context(self):
        r"""Context information of this request can be used in the request parameter of the next request to accelerate query speed.
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

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
    r"""DescribeBillDownloadUrl request structure.

    """

    def __init__(self):
        r"""
        :param _FileType: Billing mode. Enumeration values
billOverview=L0-PDF Bill
Bill Summary=L1-Summary Bill	
billResource=L2-Resource bill	
billDetail=L3-Detailed Bill	
billPack
        :type FileType: str
        :param _Month: Billing month
Earliest start month supported is 2021-01
L0-PDF&bill package does not support download for the current month. Please download the monthly bill after billing on the 1st of next month at 19:00.
        :type Month: str
        :param _ChildUin: Downloaded account ID list. By default, the query returns the account statement of the current account. If the group management account needs to download the self-pay bills of member accounts, enter the member account UIN in this field.
        :type ChildUin: list of str
        """
        self._FileType = None
        self._Month = None
        self._ChildUin = None

    @property
    def FileType(self):
        r"""Billing mode. Enumeration values
billOverview=L0-PDF Bill
Bill Summary=L1-Summary Bill	
billResource=L2-Resource bill	
billDetail=L3-Detailed Bill	
billPack
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Month(self):
        r"""Billing month
Earliest start month supported is 2021-01
L0-PDF&bill package does not support download for the current month. Please download the monthly bill after billing on the 1st of next month at 19:00.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def ChildUin(self):
        r"""Downloaded account ID list. By default, the query returns the account statement of the current account. If the group management account needs to download the self-pay bills of member accounts, enter the member account UIN in this field.
        :rtype: list of str
        """
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
    r"""DescribeBillDownloadUrl response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: Whether the bill file is ready. 0: file generating, 1: file generated
        :type Ready: int
        :param _DownloadUrl: Billing file download link, valid for 1 day
Note: This field may return null, indicating that no valid values can be obtained.
        :type DownloadUrl: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ready = None
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def Ready(self):
        r"""Whether the bill file is ready. 0: file generating, 1: file generated
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def DownloadUrl(self):
        r"""Billing file download link, valid for 1 day
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

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
        self._Ready = params.get("Ready")
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class DescribeBillResourceSummaryForOrganizationRequest(AbstractModel):
    r"""DescribeBillResourceSummaryForOrganization request structure.

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
Yearly/monthly subscription purchase
Yearly/monthly subscription renewal
Yearly/monthly subscription upgrade/downgrade
Yearly/monthly subscription refund 
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
Yearly/monthly subscription resource migration in 
Yearly/monthly subscription resource migration out 
Prepaid 
Hourly 
RI refund 
Pay-as-you-go reversal 
Yearly/monthly subscription to pay-as-you-go 
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
        r"""Pagination offset. If `Offset` is `0`, it indicates the first page. When `Limit` is `100`, if `Offset` is `100`, it indicates the second page; if `Offset` is `200`, it indicates the third page, and so on.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""The number of entries returned at a time. The maximum value is `1000`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Month(self):
        r"""Bill month in the format of "yyyy-mm". This value must be no earlier than the month when Bill 2.0 is activated.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PeriodType(self):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        r"""Cycle type, which can be `byUsedTime` (by billing cycle) or `byPayTime` (by deduction time). This value must be the same as the billing period type in Billing Center for that particular month. You can check your billing cycle at the top of the [Bill Overview](https://console.cloud.tencent.com/expense/bill/overview) page.
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        self._PeriodType = PeriodType

    @property
    def NeedRecordNum(self):
        r"""Indicates whether the total number of records is required, used for pagination.
Valid values: `1` (required), `0` (not required).
        :rtype: int
        """
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def ActionType(self):
        r"""Transaction type. This parameter needs to be input using the `ActionTypeName` value. Valid values:
Yearly/monthly subscription purchase
Yearly/monthly subscription renewal
Yearly/monthly subscription upgrade/downgrade
Yearly/monthly subscription refund 
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
Yearly/monthly subscription resource migration in 
Yearly/monthly subscription resource migration out 
Prepaid 
Hourly 
RI refund 
Pay-as-you-go reversal 
Yearly/monthly subscription to pay-as-you-go 
Minimum spend deduction 
Hourly savings plan fee
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ResourceId(self):
        r"""ID of the instance to be queried.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def PayMode(self):
        r"""Billing mode. Valid values: `prePay`, `postPay`.
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def BusinessCode(self):
        r"""Product code
Note: To query the product codes (`BusinessCode`) used in the current month, call <a href="https://intl.cloud.tencent.com/document/product/555/35761?from_cn_redirect=1">DescribeBillSummaryByProduct</a>.
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def TagKey(self):
        r"""Cost allocation tag key, which can be customized. This parameter can be used for querying bills after January 2021.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Resource tag value. If it is left empty, there are no records with tag values set under this tag key.
This parameter can be used for querying bills after January 2021.
        :rtype: str
        """
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
    r"""DescribeBillResourceSummaryForOrganization response structure.

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
        r"""Resource summary list.
        :rtype: list of BillDistributionResourceSummary
        """
        return self._ResourceSummarySet

    @ResourceSummarySet.setter
    def ResourceSummarySet(self, ResourceSummarySet):
        self._ResourceSummarySet = ResourceSummarySet

    @property
    def Total(self):
        r"""Total number of resource summary lists. It will not be returned if `NeedRecordNum` is `0`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
                obj = BillDistributionResourceSummary()
                obj._deserialize(item)
                self._ResourceSummarySet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeBillResourceSummaryRequest(AbstractModel):
    r"""DescribeBillResourceSummary request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination offset. If `Offset` is `0`, it indicates the first page. If `Limit` is `100`, "`Offset` = `100`" indicates the second page, then "`Offset` = `200`" indicates the third page, and so on.
        :type Offset: int
        :param _Limit: Quantity, maximum is 1000
        :type Limit: int
        :param _Month: Bill month in the format of "yyyy-mm". This value must be no earlier than March 2019, when Bill 2.0 was launched.
        :type Month: str
        :param _PeriodType: The period type. byUsedTime
        :type PeriodType: str
        :param _NeedRecordNum: Indicates whether or not the total number of records of accessing the list is required, used for frontend pages.
1 = yes, 0 = no
        :type NeedRecordNum: int
        :param _ActionType: Hourly settlement
Daily settlement
Yearly/monthly subscription
Spot
New yearly/monthly subscription
Yearly/monthly subscription renewal
Yearly/monthly subscription specification adjustment
Yearly/monthly subscription refund
Adjustment - deduction
Adjustment - refund
Hourly RI fee
One-off RI Fee
Hourly Savings Plan fee
Offline project deduction
Offline product deduction
        :type ActionType: str
        :param _ResourceId: ID of the instance to be queried
        :type ResourceId: str
        :param _PayMode: Billing mode: prePay/postPay
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
        r"""Pagination offset. If `Offset` is `0`, it indicates the first page. If `Limit` is `100`, "`Offset` = `100`" indicates the second page, then "`Offset` = `200`" indicates the third page, and so on.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Quantity, maximum is 1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Month(self):
        r"""Bill month in the format of "yyyy-mm". This value must be no earlier than March 2019, when Bill 2.0 was launched.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PeriodType(self):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        r"""The period type. byUsedTime
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        self._PeriodType = PeriodType

    @property
    def NeedRecordNum(self):
        r"""Indicates whether or not the total number of records of accessing the list is required, used for frontend pages.
1 = yes, 0 = no
        :rtype: int
        """
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def ActionType(self):
        r"""Hourly settlement
Daily settlement
Yearly/monthly subscription
Spot
New yearly/monthly subscription
Yearly/monthly subscription renewal
Yearly/monthly subscription specification adjustment
Yearly/monthly subscription refund
Adjustment - deduction
Adjustment - refund
Hourly RI fee
One-off RI Fee
Hourly Savings Plan fee
Offline project deduction
Offline product deduction
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ResourceId(self):
        r"""ID of the instance to be queried
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def PayMode(self):
        r"""Billing mode: prePay/postPay
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def BusinessCode(self):
        r"""Product code
Note: To query the product codes used in the current month, call <a href="https://intl.cloud.tencent.com/document/product/555/35761?from_cn_redirect=1">DescribeBillSummaryByProduct</a>.
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def PayerUin(self):
        r"""The account ID of the payer, which is the unique identifier of a Tencent Cloud user. This account is allowed to query its own bills by default. If an organization admin account needs to query the self-pay bills of members, this field should be specified as the member account ID.
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def TagKey(self):
        r"""Cost allocation tag key, which can be customized. This parameter can be used for querying bills after January 2021.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Resource tag value. If it is left empty, there are no records with tag values set under this tag key.
This parameter can be used for querying bills after January 2021.
        :rtype: str
        """
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
    r"""DescribeBillResourceSummary response structure.

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
        r"""Resource summary list
        :rtype: list of BillResourceSummary
        """
        return self._ResourceSummarySet

    @ResourceSummarySet.setter
    def ResourceSummarySet(self, ResourceSummarySet):
        self._ResourceSummarySet = ResourceSummarySet

    @property
    def Total(self):
        r"""Total number of resource summary lists, which will not be returned when `NeedRecordNum` is `0`. This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
                obj = BillResourceSummary()
                obj._deserialize(item)
                self._ResourceSummarySet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryByPayModeRequest(AbstractModel):
    r"""DescribeBillSummaryByPayMode request structure.

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
        r"""The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PayerUin(self):
        r"""Query bill data user's UIN
        :rtype: str
        """
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
    r"""DescribeBillSummaryByPayMode response structure.

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
        r"""Indicates whether the data is ready. `0`: Not ready. `1`: Ready. If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first time. Wait for 5-10 minutes and try again.
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryOverview(self):
        r"""Detailed cost distribution for all billing modes
Note: This field may return null, indicating that no valid value was found.
        :rtype: list of PayModeSummaryOverviewItem
        """
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

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
        self._Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self._SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = PayModeSummaryOverviewItem()
                obj._deserialize(item)
                self._SummaryOverview.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryByProductRequest(AbstractModel):
    r"""DescribeBillSummaryByProduct request structure.

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
        r"""The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PayerUin(self):
        r"""Queries bill data user's UIN
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def PayType(self):
        r"""A bill type, which corresponds to a subtotal type of L0 bills.
This parameter has become valid since v3.0 bills took effect in May 2021.
Valid values:
`consume`: consumption
`refund`: refund
`adjustment`: bill adjustment
        :rtype: str
        """
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
    r"""DescribeBillSummaryByProduct response structure.

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
        r"""Indicates whether the data is ready. `0`: Not ready. `1`: Ready. If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first time. Wait for 5-10 minutes and try again.
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryTotal(self):
        r"""Total cost details
Note: This field may return null, indicating that no valid value was found.
        :rtype: :class:`tencentcloud.billing.v20180709.models.BusinessSummaryTotal`
        """
        return self._SummaryTotal

    @SummaryTotal.setter
    def SummaryTotal(self, SummaryTotal):
        self._SummaryTotal = SummaryTotal

    @property
    def SummaryOverview(self):
        r"""Cost distribution of all products
Note: This field may return null, indicating that no valid value was found.
        :rtype: list of BusinessSummaryOverviewItem
        """
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

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
    r"""DescribeBillSummaryByProject request structure.

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
        r"""The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PayerUin(self):
        r"""Queries bill data user's UIN
        :rtype: str
        """
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
    r"""DescribeBillSummaryByProject response structure.

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
        r"""Indicates whether the data is ready. `0`: Not ready. `1`: Ready. If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first time. Wait for 5-10 minutes and try again.
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryOverview(self):
        r"""Detailed cost distribution for all projects
Note: This field may return null, indicating that no valid value was found.
        :rtype: list of ProjectSummaryOverviewItem
        """
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

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
        self._Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self._SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = ProjectSummaryOverviewItem()
                obj._deserialize(item)
                self._SummaryOverview.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryByRegionRequest(AbstractModel):
    r"""DescribeBillSummaryByRegion request structure.

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
        r"""The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PayerUin(self):
        r"""Queries bill data user's UIN
        :rtype: str
        """
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
    r"""DescribeBillSummaryByRegion response structure.

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
        r"""Indicates whether the data is ready. `0`: Not ready. `1`: Ready. If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first time. Wait for 5-10 minutes and try again.
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryOverview(self):
        r"""Detailed cost distribution for all regions
Note: This field may return null, indicating that no valid value was found.
        :rtype: list of RegionSummaryOverviewItem
        """
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

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
        self._Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self._SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = RegionSummaryOverviewItem()
                obj._deserialize(item)
                self._SummaryOverview.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryByTagRequest(AbstractModel):
    r"""DescribeBillSummaryByTag request structure.

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
        r"""The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TagKey(self):
        r"""Cost allocation tag key, which can be customized.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def PayerUin(self):
        r"""Payer UIN
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def TagValue(self):
        r"""Resource tag value
        :rtype: str
        """
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
    r"""DescribeBillSummaryByTag response structure.

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
        r"""Indicates whether the data is ready. `0`: Not ready. `1`: Ready. If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first time. Wait for 5-10 minutes and try again.
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryOverview(self):
        r"""Details about cost distribution over different tags
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TagSummaryOverviewItem
        """
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

    @property
    def SummaryTotal(self):
        r"""Total cost
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.billing.v20180709.models.SummaryTotal`
        """
        return self._SummaryTotal

    @SummaryTotal.setter
    def SummaryTotal(self, SummaryTotal):
        self._SummaryTotal = SummaryTotal

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
    r"""DescribeBillSummaryForOrganization request structure.

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
        r"""Bill month in the format of "yyyy-mm".
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def GroupType(self):
        r"""Bill dimension. Valid values: `business`, `project`, `region`, `payMode`, and `tag`.
        :rtype: str
        """
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def TagKey(self):
        r"""Tag key. Pass in it when `GroupType` is `tag`.
        :rtype: list of str
        """
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
    r"""DescribeBillSummaryForOrganization response structure.

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
        r"""Indicates whether the data is ready. Valid values: `0` (not ready), `1` (ready). If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first time. Wait for 5-10 minutes and try again.
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryDetail(self):
        r"""Bills summarized by multiple dimensions.
        :rtype: list of SummaryDetail
        """
        return self._SummaryDetail

    @SummaryDetail.setter
    def SummaryDetail(self, SummaryDetail):
        self._SummaryDetail = SummaryDetail

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
        self._Ready = params.get("Ready")
        if params.get("SummaryDetail") is not None:
            self._SummaryDetail = []
            for item in params.get("SummaryDetail"):
                obj = SummaryDetail()
                obj._deserialize(item)
                self._SummaryDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryRequest(AbstractModel):
    r"""DescribeBillSummary request structure.

    """

    def __init__(self):
        r"""
        :param _Month: <p>Bill month, formatted as 2023-04</p>
        :type Month: str
        :param _GroupType: <p>Billing dimension type. Enumeration values as follows: business, project, region, payMode, tag</p>
        :type GroupType: str
        :param _TagKey: <p>Tag key. Pass GroupType=tag when obtaining dimensional billing by tag.</p>
        :type TagKey: list of str
        :param _OperateUin: <p>Operator UIN: Operator account ID (ID of the prepaid resource order or postpaid operation, activate postpaid resource account or role ID)</p>
        :type OperateUin: str
        :param _PayerUin: <p>Account ID of the payer (Account ID is the unique account identifier for the user in Tencent Cloud). By default, the query returns the account statement of the current account. If the group management account needs to query the self-pay bills of member accounts, enter the member account UIN in this field.</p>
        :type PayerUin: str
        """
        self._Month = None
        self._GroupType = None
        self._TagKey = None
        self._OperateUin = None
        self._PayerUin = None

    @property
    def Month(self):
        r"""<p>Bill month, formatted as 2023-04</p>
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def GroupType(self):
        r"""<p>Billing dimension type. Enumeration values as follows: business, project, region, payMode, tag</p>
        :rtype: str
        """
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def TagKey(self):
        r"""<p>Tag key. Pass GroupType=tag when obtaining dimensional billing by tag.</p>
        :rtype: list of str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def OperateUin(self):
        r"""<p>Operator UIN: Operator account ID (ID of the prepaid resource order or postpaid operation, activate postpaid resource account or role ID)</p>
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def PayerUin(self):
        r"""<p>Account ID of the payer (Account ID is the unique account identifier for the user in Tencent Cloud). By default, the query returns the account statement of the current account. If the group management account needs to query the self-pay bills of member accounts, enter the member account UIN in this field.</p>
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._GroupType = params.get("GroupType")
        self._TagKey = params.get("TagKey")
        self._OperateUin = params.get("OperateUin")
        self._PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryResponse(AbstractModel):
    r"""DescribeBillSummary response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: <p>Data readiness, 0 preparing, 1 ready. (Ready=0 indicates the first time initialization billing is in progress for the present UIN, is expected to take 5-10 minutes. Just retry after 10 minutes.)</p>
        :type Ready: int
        :param _SummaryDetail: <p>Multidimensional bill summary of consumption detail</p>
        :type SummaryDetail: list of SummaryDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryDetail = None
        self._RequestId = None

    @property
    def Ready(self):
        r"""<p>Data readiness, 0 preparing, 1 ready. (Ready=0 indicates the first time initialization billing is in progress for the present UIN, is expected to take 5-10 minutes. Just retry after 10 minutes.)</p>
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryDetail(self):
        r"""<p>Multidimensional bill summary of consumption detail</p>
        :rtype: list of SummaryDetail
        """
        return self._SummaryDetail

    @SummaryDetail.setter
    def SummaryDetail(self, SummaryDetail):
        self._SummaryDetail = SummaryDetail

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
        self._Ready = params.get("Ready")
        if params.get("SummaryDetail") is not None:
            self._SummaryDetail = []
            for item in params.get("SummaryDetail"):
                obj = SummaryDetail()
                obj._deserialize(item)
                self._SummaryDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCPQBillingMappingRequest(AbstractModel):
    r"""DescribeCPQBillingMapping request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset
        :type Offset: str
        :param _Limit: The number of entries returned at a time. The maximum value is `100`.	
        :type Limit: str
        :param _SpuName: Quoted subproduct name
        :type SpuName: str
        :param _CategoryName: Quoted product name
        :type CategoryName: str
        :param _BusinessName: Product name
        :type BusinessName: str
        :param _ProductName: Subproduct name
        :type ProductName: str
        :param _ComponentName: Component type name
        :type ComponentName: str
        :param _ItemName: Component name
        :type ItemName: str
        :param _BusinessCode: Product code
        :type BusinessCode: str
        :param _ProductCode: Subproduct code
        :type ProductCode: str
        :param _ComponentCode: Component type code
        :type ComponentCode: str
        :param _ItemCode: Component code
        :type ItemCode: str
        """
        self._Offset = None
        self._Limit = None
        self._SpuName = None
        self._CategoryName = None
        self._BusinessName = None
        self._ProductName = None
        self._ComponentName = None
        self._ItemName = None
        self._BusinessCode = None
        self._ProductCode = None
        self._ComponentCode = None
        self._ItemCode = None

    @property
    def Offset(self):
        r"""Offset
        :rtype: str
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""The number of entries returned at a time. The maximum value is `100`.	
        :rtype: str
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SpuName(self):
        r"""Quoted subproduct name
        :rtype: str
        """
        return self._SpuName

    @SpuName.setter
    def SpuName(self, SpuName):
        self._SpuName = SpuName

    @property
    def CategoryName(self):
        r"""Quoted product name
        :rtype: str
        """
        return self._CategoryName

    @CategoryName.setter
    def CategoryName(self, CategoryName):
        self._CategoryName = CategoryName

    @property
    def BusinessName(self):
        r"""Product name
        :rtype: str
        """
        return self._BusinessName

    @BusinessName.setter
    def BusinessName(self, BusinessName):
        self._BusinessName = BusinessName

    @property
    def ProductName(self):
        r"""Subproduct name
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ComponentName(self):
        r"""Component type name
        :rtype: str
        """
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def ItemName(self):
        r"""Component name
        :rtype: str
        """
        return self._ItemName

    @ItemName.setter
    def ItemName(self, ItemName):
        self._ItemName = ItemName

    @property
    def BusinessCode(self):
        r"""Product code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProductCode(self):
        r"""Subproduct code
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ComponentCode(self):
        r"""Component type code
        :rtype: str
        """
        return self._ComponentCode

    @ComponentCode.setter
    def ComponentCode(self, ComponentCode):
        self._ComponentCode = ComponentCode

    @property
    def ItemCode(self):
        r"""Component code
        :rtype: str
        """
        return self._ItemCode

    @ItemCode.setter
    def ItemCode(self, ItemCode):
        self._ItemCode = ItemCode


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SpuName = params.get("SpuName")
        self._CategoryName = params.get("CategoryName")
        self._BusinessName = params.get("BusinessName")
        self._ProductName = params.get("ProductName")
        self._ComponentName = params.get("ComponentName")
        self._ItemName = params.get("ItemName")
        self._BusinessCode = params.get("BusinessCode")
        self._ProductCode = params.get("ProductCode")
        self._ComponentCode = params.get("ComponentCode")
        self._ItemCode = params.get("ItemCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCPQBillingMappingResponse(AbstractModel):
    r"""DescribeCPQBillingMapping response structure.

    """

    def __init__(self):
        r"""
        :param _ResourceSpuSet: Return data details
        :type ResourceSpuSet: list of ResourceSpuSet
        :param _Total: 10
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ResourceSpuSet = None
        self._Total = None
        self._RequestId = None

    @property
    def ResourceSpuSet(self):
        r"""Return data details
        :rtype: list of ResourceSpuSet
        """
        return self._ResourceSpuSet

    @ResourceSpuSet.setter
    def ResourceSpuSet(self, ResourceSpuSet):
        self._ResourceSpuSet = ResourceSpuSet

    @property
    def Total(self):
        r"""10
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("ResourceSpuSet") is not None:
            self._ResourceSpuSet = []
            for item in params.get("ResourceSpuSet"):
                obj = ResourceSpuSet()
                obj._deserialize(item)
                self._ResourceSpuSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeCostDetailRequest(AbstractModel):
    r"""DescribeCostDetail request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: The number of entries returned at a time. The maximum value is `100`.
        :type Limit: int
        :param _Offset: Offset
        :type Offset: int
        :param _BeginTime: Cycle start time. The query granularity is daily. The hour/minute/second parameter must be input in the format of yyyy-mm-dd hh:ii:ss. Either Month or BeginTime&EndTime must be entered, and if this field is present, Month becomes invalid. BeginTime and EndTime must be entered together, and must be in the same month. Cross-month retrieval is not currently supported. Data retrievable is the data after consumption bill is enabled and within the past 18 months.
        :type BeginTime: str
        :param _EndTime: Cycle end time. The query granularity is daily. The hour-minute-second parameter must be imported in the format of yyyy-mm-dd hh:ii:ss. Either Month or BeginTime&EndTime must be specified. If this field is present, Month becomes invalid. BeginTime and EndTime must be specified together and must be in the same month. Cross-month retrieval is not currently supported. Data retrievable is the data after consumption bill is enabled and within the past 18 months.
        :type EndTime: str
        :param _NeedRecordNum: Whether the total number of records in the list is needed, for frontend pagination1: needed, 0: not needed
        :type NeedRecordNum: int
        :param _Month: The month is in the format of yyyy-mm. Either Month or BeginTime&EndTime must be specified. If BeginTime&EndTime is specified, the Month field is invalid. It cannot be earlier than the month when the consumption bill was enabled. Data within the last 18 months can be pulled at most.
        :type Month: str
        :param _ProductCode: Query information of a specified product
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
        r"""The number of entries returned at a time. The maximum value is `100`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def BeginTime(self):
        r"""Cycle start time. The query granularity is daily. The hour/minute/second parameter must be input in the format of yyyy-mm-dd hh:ii:ss. Either Month or BeginTime&EndTime must be entered, and if this field is present, Month becomes invalid. BeginTime and EndTime must be entered together, and must be in the same month. Cross-month retrieval is not currently supported. Data retrievable is the data after consumption bill is enabled and within the past 18 months.
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""Cycle end time. The query granularity is daily. The hour-minute-second parameter must be imported in the format of yyyy-mm-dd hh:ii:ss. Either Month or BeginTime&EndTime must be specified. If this field is present, Month becomes invalid. BeginTime and EndTime must be specified together and must be in the same month. Cross-month retrieval is not currently supported. Data retrievable is the data after consumption bill is enabled and within the past 18 months.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NeedRecordNum(self):
        r"""Whether the total number of records in the list is needed, for frontend pagination1: needed, 0: not needed
        :rtype: int
        """
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def Month(self):
        r"""The month is in the format of yyyy-mm. Either Month or BeginTime&EndTime must be specified. If BeginTime&EndTime is specified, the Month field is invalid. It cannot be earlier than the month when the consumption bill was enabled. Data within the last 18 months can be pulled at most.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def ProductCode(self):
        r"""Query information of a specified product
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def PayMode(self):
        r"""Payment mode. Options include prePay and postPay.
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResourceId(self):
        r"""Used to query information of a specified resource
        :rtype: str
        """
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
    r"""DescribeCostDetail response structure.

    """

    def __init__(self):
        r"""
        :param _DetailSet: Consumption details
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
        r"""Consumption details
        :rtype: list of CostDetail
        """
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet

    @property
    def Total(self):
        r"""Record countNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("DetailSet") is not None:
            self._DetailSet = []
            for item in params.get("DetailSet"):
                obj = CostDetail()
                obj._deserialize(item)
                self._DetailSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeCostExplorerSummaryRequest(AbstractModel):
    r"""DescribeCostExplorerSummary request structure.

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
        :param _FeeType: Fee type: cost-discounted total cost, totalCost-original price cost
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
        r"""The start time of the period in the format of yyyy-mm-dd hh:ii:ss.
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""The end time of the period in the format of yyyy-mm-dd hh:ii:ss.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def BillType(self):
        r"""Bill type: 1-cost bill, 2-consumption bill
        :rtype: str
        """
        return self._BillType

    @BillType.setter
    def BillType(self, BillType):
        self._BillType = BillType

    @property
    def PeriodType(self):
        r"""Statistical period: day-day, month-month;
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType

    @property
    def Dimensions(self):
        r"""Classification dimension (data aggregation dimension). Query classification dimension. (Use classification dimension code input parameter.) Input parameter enumeration value:default = Total only
feeType = Fee typebillType = Bill typebusiness = Product
product = Sub-productregion=Region
zone = Availability zoneactionType = Transaction typepayMode = Billing modetags = Tagproject = ProjectpayerUin = Payer accountownerUin = User account
        :rtype: str
        """
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def FeeType(self):
        r"""Fee type: cost-discounted total cost, totalCost-original price cost
        :rtype: str
        """
        return self._FeeType

    @FeeType.setter
    def FeeType(self, FeeType):
        self._FeeType = FeeType

    @property
    def PageSize(self):
        r"""Quantity. The maximum value per page is 100.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNo(self):
        r"""Starting page, where PageNo=1 indicates the first page, PageNo=2 indicates the second page, and so on.
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def TagKeyStr(self):
        r"""Cost allocation tag value
        :rtype: str
        """
        return self._TagKeyStr

    @TagKeyStr.setter
    def TagKeyStr(self, TagKeyStr):
        self._TagKeyStr = TagKeyStr

    @property
    def NeedConditionValue(self):
        r"""Whether the filter box is needed: 1- indicates it is needed, 0- indicates it is not needed. If it is not specified, it is not required by default.
        :rtype: str
        """
        return self._NeedConditionValue

    @NeedConditionValue.setter
    def NeedConditionValue(self, NeedConditionValue):
        self._NeedConditionValue = NeedConditionValue

    @property
    def Conditions(self):
        r"""Filter parameters
        :rtype: :class:`tencentcloud.billing.v20180709.models.AnalyseConditions`
        """
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
    r"""DescribeCostExplorerSummary response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Number of data records
        :type Total: int
        :param _Header: Header information.
        :type Header: :class:`tencentcloud.billing.v20180709.models.AnalyseHeaderDetail`
        :param _Detail: Data details
        :type Detail: list of AnalyseDetail
        :param _TotalDetail: data total
        :type TotalDetail: :class:`tencentcloud.billing.v20180709.models.AnalyseDetail`
        :param _ConditionValue: filtering box
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
        r"""Number of data records
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Header(self):
        r"""Header information.
        :rtype: :class:`tencentcloud.billing.v20180709.models.AnalyseHeaderDetail`
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def Detail(self):
        r"""Data details
        :rtype: list of AnalyseDetail
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def TotalDetail(self):
        r"""data total
        :rtype: :class:`tencentcloud.billing.v20180709.models.AnalyseDetail`
        """
        return self._TotalDetail

    @TotalDetail.setter
    def TotalDetail(self, TotalDetail):
        self._TotalDetail = TotalDetail

    @property
    def ConditionValue(self):
        r"""filtering box
        :rtype: :class:`tencentcloud.billing.v20180709.models.AnalyseConditionDetail`
        """
        return self._ConditionValue

    @ConditionValue.setter
    def ConditionValue(self, ConditionValue):
        self._ConditionValue = ConditionValue

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
    r"""DescribeCostSummaryByProduct request structure.

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
        r"""The value must be of the same month as `EndTime`. The query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""The value must be of the same month as `BeginTime`. The query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        r"""Data quantity per fetch. The maximum value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset, which starts from 0 by default
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PayerUin(self):
        r"""UIN of the user querying the bill data
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def NeedRecordNum(self):
        r"""Whether to return the record count. 0 for no, 1 for yes. Default is no.
        :rtype: int
        """
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
    r"""DescribeCostSummaryByProduct response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: Data readiness, 0 for not ready, 1 for ready
        :type Ready: int
        :param _Total: Consumption details
        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param _Data: Consumption details summarized by product
        :type Data: list of ConsumptionBusinessSummaryDataItem
        :param _RecordNum: Record count. If NeedRecordNum is 0, null is returned.
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
        r"""Data readiness, 0 for not ready, 1 for ready
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Total(self):
        r"""Consumption details
        :rtype: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        r"""Consumption details summarized by product
        :rtype: list of ConsumptionBusinessSummaryDataItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RecordNum(self):
        r"""Record count. If NeedRecordNum is 0, null is returned.
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

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
    r"""DescribeCostSummaryByProject request structure.

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
        r"""The value must be of the same month as `EndTime`. The query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""The value must be of the same month as `BeginTime`. The query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        r"""Data quantity per fetch. The maximum value is `100`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset, which starts from 0 by default
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PayerUin(self):
        r"""UIN of the user querying the bill data
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def NeedRecordNum(self):
        r"""Whether to return the record count. 0 for no, 1 for yes. Default is no.
        :rtype: int
        """
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
    r"""DescribeCostSummaryByProject response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: Data readiness, 0 for not ready, 1 for ready
        :type Ready: int
        :param _Total: Consumption details
        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param _Data: Consumption details summarized by business
        :type Data: list of ConsumptionProjectSummaryDataItem
        :param _RecordNum: Record count. If NeedRecordNum is 0, null is returned.
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
        r"""Data readiness, 0 for not ready, 1 for ready
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Total(self):
        r"""Consumption details
        :rtype: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        r"""Consumption details summarized by business
        :rtype: list of ConsumptionProjectSummaryDataItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RecordNum(self):
        r"""Record count. If NeedRecordNum is 0, null is returned.
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

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
    r"""DescribeCostSummaryByRegion request structure.

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
        r"""The value must be of the same month as `EndTime`. The query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""The value must be of the same month as `BeginTime`. The query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        r"""Data quantity per fetch. The maximum value is `100`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset, which starts from 0 by default
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PayerUin(self):
        r"""UIN of the user querying the bill data
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def NeedRecordNum(self):
        r"""Whether to return the record count. 0 for no, 1 for yes. Default is no.
        :rtype: int
        """
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
    r"""DescribeCostSummaryByRegion response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: Data readiness, 0 for not ready, 1 for ready
        :type Ready: int
        :param _Total: Consumption details
        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param _Data: Consumption details summarized by region
        :type Data: list of ConsumptionRegionSummaryDataItem
        :param _RecordNum: Record count. If NeedRecordNum is 0, null is returned.
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
        r"""Data readiness, 0 for not ready, 1 for ready
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Total(self):
        r"""Consumption details
        :rtype: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        r"""Consumption details summarized by region
        :rtype: list of ConsumptionRegionSummaryDataItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RecordNum(self):
        r"""Record count. If NeedRecordNum is 0, null is returned.
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

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
    r"""DescribeCostSummaryByResource request structure.

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
        r"""The value must be of the same month as EndTime. The query period must start and end on the same month and the query result returned will be of the entire month. For example, if both BeginTime and EndTime are 2018-09, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""The value must be of the same month as BeginTime. The query period must start and end on the same month and the query result returned will be of the entire month. For example, if both BeginTime and EndTime are 2018-09, the data returned will be for the entire month of September 2018.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        r"""Data quantity per fetch. The maximum value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset, which starts from 0 by default
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PayerUin(self):
        r"""UIN of the user querying the bill data
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def NeedRecordNum(self):
        r"""Whether to return the record count. 0 for no, 1 for yes. Default is no.
        :rtype: int
        """
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def NeedConditionValue(self):
        r"""Whether to return filter criteria. 0 for no, 1 for yes. Default is no.
        :rtype: int
        """
        return self._NeedConditionValue

    @NeedConditionValue.setter
    def NeedConditionValue(self, NeedConditionValue):
        self._NeedConditionValue = NeedConditionValue

    @property
    def Conditions(self):
        r"""Filter criteria. It only supports ResourceKeyword (resource keyword, which supports fuzzy query by resource ID or resource name), ProjectIds (project ID), RegionIds (region ID), PayModes (payment mode, prePay or postPay), HideFreeCost (whether to hide zero-amount transactions, 0 or 1), and OrderByCost (sorting rule by fees, desc or asc).
        :rtype: :class:`tencentcloud.billing.v20180709.models.Conditions`
        """
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
    r"""DescribeCostSummaryByResource response structure.

    """

    def __init__(self):
        r"""
        :param _Ready: Data readiness, 0 for not ready, 1 for ready
        :type Ready: int
        :param _Total: Consumption details
        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param _ConditionValue: Filter criteria
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConditionValue: :class:`tencentcloud.billing.v20180709.models.ConsumptionResourceSummaryConditionValue`
        :param _RecordNum: Record countNote: This field may return null, indicating that no valid values can be obtained.
        :type RecordNum: int
        :param _Data: Resource consumption details
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
        r"""Data readiness, 0 for not ready, 1 for ready
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Total(self):
        r"""Consumption details
        :rtype: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConditionValue(self):
        r"""Filter criteria
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.billing.v20180709.models.ConsumptionResourceSummaryConditionValue`
        """
        return self._ConditionValue

    @ConditionValue.setter
    def ConditionValue(self, ConditionValue):
        self._ConditionValue = ConditionValue

    @property
    def RecordNum(self):
        r"""Record countNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def Data(self):
        r"""Resource consumption details
        :rtype: list of ConsumptionResourceSummaryDataItem
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


class DescribeDealsByCondRequest(AbstractModel):
    r"""DescribeDealsByCond request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time 
Example :2016-01-01 00:00:00
        :type StartTime: str
        :param _EndTime: End time 
Example:2016-02-01 00:00:00. 
It is recommended that the span does not exceed 3 months.
        :type EndTime: str
        :param _Limit: The number of records per page. The default is 20, and the maximum is 1,000.
        :type Limit: int
        :param _Offset: The page number the records start from, starting from 0. The default is 0.
        :type Offset: int
        :param _Status: Order status, default is 4 (successful order)
Status of the order
1: unpaid
2: paid 
3: shipment in progress
4: shipped
5`: Shipment Failed
6`: Refunded
7`: Ticket closed
8`: Order expired
9`: Order invalid
10: product invalidated
11: third-party payment refused
12: payment in process
        :type Status: int
        :param _OrderId: Sub-order number
Example: 202202021234567
        :type OrderId: str
        :param _BigDealId: Large order number.
Example: 202202021234566
        :type BigDealId: str
        :param _ResourceId: Resource ID
Example:ins-a2bb34
        :type ResourceId: str
        :param _StatusSet: Order status
        :type StatusSet: list of int
        """
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._OrderId = None
        self._BigDealId = None
        self._ResourceId = None
        self._StatusSet = None

    @property
    def StartTime(self):
        r"""Start time 
Example :2016-01-01 00:00:00
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time 
Example:2016-02-01 00:00:00. 
It is recommended that the span does not exceed 3 months.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        r"""The number of records per page. The default is 20, and the maximum is 1,000.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""The page number the records start from, starting from 0. The default is 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        r"""Order status, default is 4 (successful order)
Status of the order
1: unpaid
2: paid 
3: shipment in progress
4: shipped
5`: Shipment Failed
6`: Refunded
7`: Ticket closed
8`: Order expired
9`: Order invalid
10: product invalidated
11: third-party payment refused
12: payment in process
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrderId(self):
        r"""Sub-order number
Example: 202202021234567
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def BigDealId(self):
        r"""Large order number.
Example: 202202021234566
        :rtype: str
        """
        return self._BigDealId

    @BigDealId.setter
    def BigDealId(self, BigDealId):
        self._BigDealId = BigDealId

    @property
    def ResourceId(self):
        r"""Resource ID
Example:ins-a2bb34
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def StatusSet(self):
        r"""Order status
        :rtype: list of int
        """
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Status = params.get("Status")
        self._OrderId = params.get("OrderId")
        self._BigDealId = params.get("BigDealId")
        self._ResourceId = params.get("ResourceId")
        self._StatusSet = params.get("StatusSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDealsByCondResponse(AbstractModel):
    r"""DescribeDealsByCond response structure.

    """

    def __init__(self):
        r"""
        :param _Deals: Order list
        :type Deals: list of Deal
        :param _TotalCount: Total number of orders
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Deals = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Deals(self):
        r"""Order list
        :rtype: list of Deal
        """
        return self._Deals

    @Deals.setter
    def Deals(self, Deals):
        self._Deals = Deals

    @property
    def TotalCount(self):
        r"""Total number of orders
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Deals") is not None:
            self._Deals = []
            for item in params.get("Deals"):
                obj = Deal()
                obj._deserialize(item)
                self._Deals.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDosageCosDetailByDateRequest(AbstractModel):
    r"""DescribeDosageCosDetailByDate request structure.

    """

    def __init__(self):
        r"""
        :param _StartDate: The start date of the usage query in the format of yyyy-mm-dd, such as `2020-09-01`.
        :type StartDate: str
        :param _EndDate: The end date of the usage query in the format of yyyy-mm-dd, such as `2020-09-30`. (The end date must be in the same month as the start date. Cross-month queries are not supported.)
        :type EndDate: str
        :param _BucketName: Bucket name. You can use `Get Service` to query the list of all buckets under a requester account. For details, see [GET Service (List Buckets)](https://www.tencentcloud.com/document/product/436/8291).
        :type BucketName: str
        """
        self._StartDate = None
        self._EndDate = None
        self._BucketName = None

    @property
    def StartDate(self):
        r"""The start date of the usage query in the format of yyyy-mm-dd, such as `2020-09-01`.
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        r"""The end date of the usage query in the format of yyyy-mm-dd, such as `2020-09-30`. (The end date must be in the same month as the start date. Cross-month queries are not supported.)
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def BucketName(self):
        r"""Bucket name. You can use `Get Service` to query the list of all buckets under a requester account. For details, see [GET Service (List Buckets)](https://www.tencentcloud.com/document/product/436/8291).
        :rtype: str
        """
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
    r"""DescribeDosageCosDetailByDate response structure.

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
        r"""Array of usage
        :rtype: list of CosDetailSets
        """
        return self._DetailSets

    @DetailSets.setter
    def DetailSets(self, DetailSets):
        self._DetailSets = DetailSets

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
        if params.get("DetailSets") is not None:
            self._DetailSets = []
            for item in params.get("DetailSets"):
                obj = CosDetailSets()
                obj._deserialize(item)
                self._DetailSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGatherResourceRequest(AbstractModel):
    r"""DescribeGatherResource request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Quantity, with the maximum value of 1,000
        :type Limit: int
        :param _Offset: Pagination offset. If Offset is 0, it indicates the first page. If Limit is 100, then Offset is 100, and it indicates the second page. If Offset is 200, it indicates the third page, and so on.
        :type Offset: int
        :param _Month: Bill month, in the format of 2024-02, which is the current month by default if not provided.
        :type Month: str
        :param _TreeNodeUniqKey: Unique identifier of a billing unit, used for filtering
        :type TreeNodeUniqKey: str
        :param _GatherType: Resource directory category, with the enumerated values as follows:
all - All 
none - Not collected
        :type GatherType: str
        :param _Sort: Sorting field, with the enumerated values as follows:
realCost - Discounted total
cashPayAmount - Cash amount
voucherPayAmount - Amount of promo voucher
incentivePayAmount - Amount of free credit
transferPayAmount - Royalty amount
        :type Sort: str
        :param _SortType: Sorting type, with the enumerated values as follows:
asc - Ascending
desc - Descending
        :type SortType: str
        :param _BusinessCodes: Product code, used for filtering
        :type BusinessCodes: list of str
        :param _ProductCodes: Subproduct code, used for filtering
        :type ProductCodes: list of str
        :param _ItemCodes: Component name code, used for filtering
        :type ItemCodes: list of str
        :param _RegionIds: Region ID, used for filtering
        :type RegionIds: list of int non-negative
        :param _InstanceTypes: Instance type code, used for filtering
        :type InstanceTypes: list of str
        :param _PayModes: Billing mode code, used for filtering
        :type PayModes: list of str
        :param _OperateUins: Operator UIN, used for filtering
        :type OperateUins: list of str
        :param _OwnerUins: User UIN, used for filtering
        :type OwnerUins: list of str
        :param _SearchKey: Fuzzy search: supports tag, resource ID, and resource alias.
        :type SearchKey: str
        :param _Tag: Tag, used for filtering
        :type Tag: list of str
        :param _ProjectIds: Project ID, used for filtering
        :type ProjectIds: list of str
        :param _ActionTypes: Transaction type code, used for filtering
        :type ActionTypes: list of str
        """
        self._Limit = None
        self._Offset = None
        self._Month = None
        self._TreeNodeUniqKey = None
        self._GatherType = None
        self._Sort = None
        self._SortType = None
        self._BusinessCodes = None
        self._ProductCodes = None
        self._ItemCodes = None
        self._RegionIds = None
        self._InstanceTypes = None
        self._PayModes = None
        self._OperateUins = None
        self._OwnerUins = None
        self._SearchKey = None
        self._Tag = None
        self._ProjectIds = None
        self._ActionTypes = None

    @property
    def Limit(self):
        r"""Quantity, with the maximum value of 1,000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Pagination offset. If Offset is 0, it indicates the first page. If Limit is 100, then Offset is 100, and it indicates the second page. If Offset is 200, it indicates the third page, and so on.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Month(self):
        r"""Bill month, in the format of 2024-02, which is the current month by default if not provided.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def TreeNodeUniqKey(self):
        r"""Unique identifier of a billing unit, used for filtering
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def GatherType(self):
        r"""Resource directory category, with the enumerated values as follows:
all - All 
none - Not collected
        :rtype: str
        """
        return self._GatherType

    @GatherType.setter
    def GatherType(self, GatherType):
        self._GatherType = GatherType

    @property
    def Sort(self):
        r"""Sorting field, with the enumerated values as follows:
realCost - Discounted total
cashPayAmount - Cash amount
voucherPayAmount - Amount of promo voucher
incentivePayAmount - Amount of free credit
transferPayAmount - Royalty amount
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def SortType(self):
        r"""Sorting type, with the enumerated values as follows:
asc - Ascending
desc - Descending
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def BusinessCodes(self):
        r"""Product code, used for filtering
        :rtype: list of str
        """
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def ProductCodes(self):
        r"""Subproduct code, used for filtering
        :rtype: list of str
        """
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes

    @property
    def ItemCodes(self):
        r"""Component name code, used for filtering
        :rtype: list of str
        """
        return self._ItemCodes

    @ItemCodes.setter
    def ItemCodes(self, ItemCodes):
        self._ItemCodes = ItemCodes

    @property
    def RegionIds(self):
        r"""Region ID, used for filtering
        :rtype: list of int non-negative
        """
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def InstanceTypes(self):
        r"""Instance type code, used for filtering
        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def PayModes(self):
        r"""Billing mode code, used for filtering
        :rtype: list of str
        """
        return self._PayModes

    @PayModes.setter
    def PayModes(self, PayModes):
        self._PayModes = PayModes

    @property
    def OperateUins(self):
        r"""Operator UIN, used for filtering
        :rtype: list of str
        """
        return self._OperateUins

    @OperateUins.setter
    def OperateUins(self, OperateUins):
        self._OperateUins = OperateUins

    @property
    def OwnerUins(self):
        r"""User UIN, used for filtering
        :rtype: list of str
        """
        return self._OwnerUins

    @OwnerUins.setter
    def OwnerUins(self, OwnerUins):
        self._OwnerUins = OwnerUins

    @property
    def SearchKey(self):
        r"""Fuzzy search: supports tag, resource ID, and resource alias.
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def Tag(self):
        r"""Tag, used for filtering
        :rtype: list of str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ProjectIds(self):
        r"""Project ID, used for filtering
        :rtype: list of str
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def ActionTypes(self):
        r"""Transaction type code, used for filtering
        :rtype: list of str
        """
        return self._ActionTypes

    @ActionTypes.setter
    def ActionTypes(self, ActionTypes):
        self._ActionTypes = ActionTypes


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Month = params.get("Month")
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._GatherType = params.get("GatherType")
        self._Sort = params.get("Sort")
        self._SortType = params.get("SortType")
        self._BusinessCodes = params.get("BusinessCodes")
        self._ProductCodes = params.get("ProductCodes")
        self._ItemCodes = params.get("ItemCodes")
        self._RegionIds = params.get("RegionIds")
        self._InstanceTypes = params.get("InstanceTypes")
        self._PayModes = params.get("PayModes")
        self._OperateUins = params.get("OperateUins")
        self._OwnerUins = params.get("OwnerUins")
        self._SearchKey = params.get("SearchKey")
        self._Tag = params.get("Tag")
        self._ProjectIds = params.get("ProjectIds")
        self._ActionTypes = params.get("ActionTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatherResourceResponse(AbstractModel):
    r"""DescribeGatherResource response structure.

    """

    def __init__(self):
        r"""
        :param _RecordNum: Total quantity.
        :type RecordNum: int
        :param _GatherResourceSummary: Resource collection summary

Note: This field may return null, indicating that no valid values can be obtained.
        :type GatherResourceSummary: list of GatherResourceSummary
        :param _LastUpdateTime: Data update time

Note: This field may return null, indicating that no valid values can be obtained.
        :type LastUpdateTime: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecordNum = None
        self._GatherResourceSummary = None
        self._LastUpdateTime = None
        self._RequestId = None

    @property
    def RecordNum(self):
        r"""Total quantity.
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def GatherResourceSummary(self):
        r"""Resource collection summary

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of GatherResourceSummary
        """
        return self._GatherResourceSummary

    @GatherResourceSummary.setter
    def GatherResourceSummary(self, GatherResourceSummary):
        self._GatherResourceSummary = GatherResourceSummary

    @property
    def LastUpdateTime(self):
        r"""Data update time

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

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
        self._RecordNum = params.get("RecordNum")
        if params.get("GatherResourceSummary") is not None:
            self._GatherResourceSummary = []
            for item in params.get("GatherResourceSummary"):
                obj = GatherResourceSummary()
                obj._deserialize(item)
                self._GatherResourceSummary.append(obj)
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._RequestId = params.get("RequestId")


class DescribeGatherRuleDetailRequest(AbstractModel):
    r"""DescribeGatherRuleDetail request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Specifies the ID of the queried collection rule.
        :type Id: int
        :param _Month: Month, the current month by default if not provided.
        :type Month: str
        """
        self._Id = None
        self._Month = None

    @property
    def Id(self):
        r"""Specifies the ID of the queried collection rule.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Month(self):
        r"""Month, the current month by default if not provided.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Month = params.get("Month")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatherRuleDetailResponse(AbstractModel):
    r"""DescribeGatherRuleDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Specifies the collection rule ID.
        :type Id: int
        :param _Uin: Associated UIN of the collection rule.
        :type Uin: str
        :param _UpdateTime: Collection rule last update time.
        :type UpdateTime: str
        :param _RuleDetail: Collection rule details.
        :type RuleDetail: :class:`tencentcloud.billing.v20180709.models.AllocationRuleExpression`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._Uin = None
        self._UpdateTime = None
        self._RuleDetail = None
        self._RequestId = None

    @property
    def Id(self):
        r"""Specifies the collection rule ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uin(self):
        r"""Associated UIN of the collection rule.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def UpdateTime(self):
        r"""Collection rule last update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def RuleDetail(self):
        r"""Collection rule details.
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationRuleExpression`
        """
        return self._RuleDetail

    @RuleDetail.setter
    def RuleDetail(self, RuleDetail):
        self._RuleDetail = RuleDetail

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
        self._Id = params.get("Id")
        self._Uin = params.get("Uin")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("RuleDetail") is not None:
            self._RuleDetail = AllocationRuleExpression()
            self._RuleDetail._deserialize(params.get("RuleDetail"))
        self._RequestId = params.get("RequestId")


class DescribeRenewInstancesRequest(AbstractModel):
    r"""DescribeRenewInstances request structure.

    """

    def __init__(self):
        r"""
        :param _MaxResults: Maximum number of instances per page. Value range: 1-100.
        :type MaxResults: int
        :param _NextToken: Token for querying the next page of returned results. NextToken is not needed when calling the API for the first time.
        :type NextToken: str
        :param _Reverse: Get the sorting order of the instance. The enumerated values are as follows:
false = Ascending (default)
true=Descending
        :type Reverse: bool
        :param _RenewFlagList: Renewal flag. Multiple values separated by commas. Enumeration value as follows:
NOTIFY_AND_MANUAL_RENEW: manual renewal.
NOTIFY_AND_AUTO_RENEW: automatic renewal.
DISABLE_NOTIFY_AND_MANUAL_RENEW: non-renewal upon expiration.
        :type RenewFlagList: list of str
        :param _InstanceIdList: Instance ID. Multiple IDs separated by commas, with a maximum of 100.
        :type InstanceIdList: list of str
        :param _ExpireTimeStart: Expiry time start, format yyyy-MM-dd HH:mm:ss.
        :type ExpireTimeStart: str
        :param _ExpireTimeEnd: Expiry time in the format of yyyy-MM-dd HH:mm:ss.
        :type ExpireTimeEnd: str
        """
        self._MaxResults = None
        self._NextToken = None
        self._Reverse = None
        self._RenewFlagList = None
        self._InstanceIdList = None
        self._ExpireTimeStart = None
        self._ExpireTimeEnd = None

    @property
    def MaxResults(self):
        r"""Maximum number of instances per page. Value range: 1-100.
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""Token for querying the next page of returned results. NextToken is not needed when calling the API for the first time.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def Reverse(self):
        r"""Get the sorting order of the instance. The enumerated values are as follows:
false = Ascending (default)
true=Descending
        :rtype: bool
        """
        return self._Reverse

    @Reverse.setter
    def Reverse(self, Reverse):
        self._Reverse = Reverse

    @property
    def RenewFlagList(self):
        r"""Renewal flag. Multiple values separated by commas. Enumeration value as follows:
NOTIFY_AND_MANUAL_RENEW: manual renewal.
NOTIFY_AND_AUTO_RENEW: automatic renewal.
DISABLE_NOTIFY_AND_MANUAL_RENEW: non-renewal upon expiration.
        :rtype: list of str
        """
        return self._RenewFlagList

    @RenewFlagList.setter
    def RenewFlagList(self, RenewFlagList):
        self._RenewFlagList = RenewFlagList

    @property
    def InstanceIdList(self):
        r"""Instance ID. Multiple IDs separated by commas, with a maximum of 100.
        :rtype: list of str
        """
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

    @property
    def ExpireTimeStart(self):
        r"""Expiry time start, format yyyy-MM-dd HH:mm:ss.
        :rtype: str
        """
        return self._ExpireTimeStart

    @ExpireTimeStart.setter
    def ExpireTimeStart(self, ExpireTimeStart):
        self._ExpireTimeStart = ExpireTimeStart

    @property
    def ExpireTimeEnd(self):
        r"""Expiry time in the format of yyyy-MM-dd HH:mm:ss.
        :rtype: str
        """
        return self._ExpireTimeEnd

    @ExpireTimeEnd.setter
    def ExpireTimeEnd(self, ExpireTimeEnd):
        self._ExpireTimeEnd = ExpireTimeEnd


    def _deserialize(self, params):
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._Reverse = params.get("Reverse")
        self._RenewFlagList = params.get("RenewFlagList")
        self._InstanceIdList = params.get("InstanceIdList")
        self._ExpireTimeStart = params.get("ExpireTimeStart")
        self._ExpireTimeEnd = params.get("ExpireTimeEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRenewInstancesResponse(AbstractModel):
    r"""DescribeRenewInstances response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceList: Instance summary list.
        :type InstanceList: list of RenewInstance
        :param _NextToken: Token for querying the next page of returned results.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NextToken: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceList = None
        self._NextToken = None
        self._RequestId = None

    @property
    def InstanceList(self):
        r"""Instance summary list.
        :rtype: list of RenewInstance
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def NextToken(self):
        r"""Token for querying the next page of returned results.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

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
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = RenewInstance()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._NextToken = params.get("NextToken")
        self._RequestId = params.get("RequestId")


class DescribeTagListRequest(AbstractModel):
    r"""DescribeTagList request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Quantity, with the maximum value of 1,000
        :type Limit: int
        :param _Offset: Pagination offset. Offset=0 indicates the first page. If Limit=100, Offset=100 indicates the second page, Offset=200 indicates the third page, and so on.
        :type Offset: int
        :param _TagKey: Cost allocation tag key, used as fuzzy search
        :type TagKey: str
        :param _Status: Tag type, enumeration value: 0 ordinary tag, 1 allocation tag, used for filtering. If not passed, get all tag keys.
        :type Status: int
        :param _OrderType: Sorting method, enumeration value: asc for ascending order, desc for descending order.
        :type OrderType: str
        """
        self._Limit = None
        self._Offset = None
        self._TagKey = None
        self._Status = None
        self._OrderType = None

    @property
    def Limit(self):
        r"""Quantity, with the maximum value of 1,000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Pagination offset. Offset=0 indicates the first page. If Limit=100, Offset=100 indicates the second page, Offset=200 indicates the third page, and so on.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def TagKey(self):
        r"""Cost allocation tag key, used as fuzzy search
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def Status(self):
        r"""Tag type, enumeration value: 0 ordinary tag, 1 allocation tag, used for filtering. If not passed, get all tag keys.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrderType(self):
        r"""Sorting method, enumeration value: asc for ascending order, desc for descending order.
        :rtype: str
        """
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
    r"""DescribeTagList response structure.

    """

    def __init__(self):
        r"""
        :param _RecordNum: Total number of records
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
        r"""Total number of records
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def Data(self):
        r"""Tag information.
        :rtype: list of TagDataInfo
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
        self._RecordNum = params.get("RecordNum")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TagDataInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVoucherInfoRequest(AbstractModel):
    r"""DescribeVoucherInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: <p>How many data entries per page, 20 is selected by default, maximum not exceeding 1000</p>
        :type Limit: int
        :param _Offset: <p>Page number, starts from 1 by default</p>
        :type Offset: int
        :param _Status: <p>Voucher status: pending use: unUsed, Used: used, delivered: delivered, discarded: cancel, expired: overdue</p>
        :type Status: str
        :param _VoucherId: <p>Voucher id</p>
        :type VoucherId: str
        :param _CodeId: <p>Voucher order id</p>
        :type CodeId: str
        :param _ProductCode: <p>product code</p>
        :type ProductCode: str
        :param _ActivityId: <p>Activity id</p>
        :type ActivityId: str
        :param _VoucherName: <p>Voucher name</p>
        :type VoucherName: str
        :param _TimeFrom: <p>Start time of delivery. Example: 2021-01-01</p>
        :type TimeFrom: str
        :param _TimeTo: <p>Delivery end time. Example: 2021-01-01</p>
        :type TimeTo: str
        :param _SortField: <p>Specified sorting field: BeginTime start time, EndTime expiry time, CreateTime creation time</p>
        :type SortField: str
        :param _SortOrder: <p>Specify ascending/descending order: desc, asc</p>
        :type SortOrder: str
        :param _PayMode: <p>Payment mode, postPay (postpaid)/prePay (prepaid)/riPay (reserved instance)/"" or "*" means all modes. If payMode is "" or "*", productCode and subProductCode must be empty.</p>
        :type PayMode: str
        :param _PayScene: <p>Payment scenario PayMode=postPay: spotpay - spot instance, "settle account" - standard post-paid. PayMode=prePay: purchase - monthly subscription new purchase, renew - annual and monthly renewal (auto renewal), modify - monthly subscription configuration change. PayMode=riPay: oneOffFee - prepayment of reserved instance, hourlyFee - hourly charge for reserved instance, * - support all payment scenarios.</p>
        :type PayScene: str
        :param _Operator: <p>Operator is used by default as user uin</p>
        :type Operator: str
        :param _VoucherMainType: <p>The primary types of vouchers are has_price and no_price, which represent the cash voucher with a price and the cash voucher without a price respectively.</p>
        :type VoucherMainType: str
        :param _VoucherSubType: <p>Voucher subtype: Discount is a discount voucher, and deduct is a deduction voucher.</p>
        :type VoucherSubType: str
        :param _StartTimeFrom: <p>Voucher validity start time</p>
        :type StartTimeFrom: str
        :param _StartTimeTo: <p>Voucher validity time end time</p>
        :type StartTimeTo: str
        :param _EndTimeFrom: <p>Voucher expiration time start time</p>
        :type EndTimeFrom: str
        :param _EndTimeTo: <p>Voucher expiration time end time</p>
        :type EndTimeTo: str
        :param _CreateTimeFrom: <p>Voucher issuance start time</p>
        :type CreateTimeFrom: str
        :param _CreateTimeTo: <p>Voucher issuance time end time</p>
        :type CreateTimeTo: str
        :param _Lang: <p>Language parameter</p><p>Default value: zh</p><p>Expect the product name to return in Chinese or other languages. Currently only support Chinese and English. Return in Chinese when "zh" is entered or left blank; return in English in other cases.</p>
        :type Lang: str
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
        self._StartTimeFrom = None
        self._StartTimeTo = None
        self._EndTimeFrom = None
        self._EndTimeTo = None
        self._CreateTimeFrom = None
        self._CreateTimeTo = None
        self._Lang = None

    @property
    def Limit(self):
        r"""<p>How many data entries per page, 20 is selected by default, maximum not exceeding 1000</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>Page number, starts from 1 by default</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        r"""<p>Voucher status: pending use: unUsed, Used: used, delivered: delivered, discarded: cancel, expired: overdue</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VoucherId(self):
        r"""<p>Voucher id</p>
        :rtype: str
        """
        return self._VoucherId

    @VoucherId.setter
    def VoucherId(self, VoucherId):
        self._VoucherId = VoucherId

    @property
    def CodeId(self):
        r"""<p>Voucher order id</p>
        :rtype: str
        """
        return self._CodeId

    @CodeId.setter
    def CodeId(self, CodeId):
        self._CodeId = CodeId

    @property
    def ProductCode(self):
        r"""<p>product code</p>
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ActivityId(self):
        r"""<p>Activity id</p>
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def VoucherName(self):
        r"""<p>Voucher name</p>
        :rtype: str
        """
        return self._VoucherName

    @VoucherName.setter
    def VoucherName(self, VoucherName):
        self._VoucherName = VoucherName

    @property
    def TimeFrom(self):
        r"""<p>Start time of delivery. Example: 2021-01-01</p>
        :rtype: str
        """
        return self._TimeFrom

    @TimeFrom.setter
    def TimeFrom(self, TimeFrom):
        self._TimeFrom = TimeFrom

    @property
    def TimeTo(self):
        r"""<p>Delivery end time. Example: 2021-01-01</p>
        :rtype: str
        """
        return self._TimeTo

    @TimeTo.setter
    def TimeTo(self, TimeTo):
        self._TimeTo = TimeTo

    @property
    def SortField(self):
        r"""<p>Specified sorting field: BeginTime start time, EndTime expiry time, CreateTime creation time</p>
        :rtype: str
        """
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortOrder(self):
        r"""<p>Specify ascending/descending order: desc, asc</p>
        :rtype: str
        """
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder

    @property
    def PayMode(self):
        r"""<p>Payment mode, postPay (postpaid)/prePay (prepaid)/riPay (reserved instance)/"" or "*" means all modes. If payMode is "" or "*", productCode and subProductCode must be empty.</p>
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayScene(self):
        r"""<p>Payment scenario PayMode=postPay: spotpay - spot instance, "settle account" - standard post-paid. PayMode=prePay: purchase - monthly subscription new purchase, renew - annual and monthly renewal (auto renewal), modify - monthly subscription configuration change. PayMode=riPay: oneOffFee - prepayment of reserved instance, hourlyFee - hourly charge for reserved instance, * - support all payment scenarios.</p>
        :rtype: str
        """
        return self._PayScene

    @PayScene.setter
    def PayScene(self, PayScene):
        self._PayScene = PayScene

    @property
    def Operator(self):
        r"""<p>Operator is used by default as user uin</p>
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def VoucherMainType(self):
        r"""<p>The primary types of vouchers are has_price and no_price, which represent the cash voucher with a price and the cash voucher without a price respectively.</p>
        :rtype: str
        """
        return self._VoucherMainType

    @VoucherMainType.setter
    def VoucherMainType(self, VoucherMainType):
        self._VoucherMainType = VoucherMainType

    @property
    def VoucherSubType(self):
        r"""<p>Voucher subtype: Discount is a discount voucher, and deduct is a deduction voucher.</p>
        :rtype: str
        """
        return self._VoucherSubType

    @VoucherSubType.setter
    def VoucherSubType(self, VoucherSubType):
        self._VoucherSubType = VoucherSubType

    @property
    def StartTimeFrom(self):
        r"""<p>Voucher validity start time</p>
        :rtype: str
        """
        return self._StartTimeFrom

    @StartTimeFrom.setter
    def StartTimeFrom(self, StartTimeFrom):
        self._StartTimeFrom = StartTimeFrom

    @property
    def StartTimeTo(self):
        r"""<p>Voucher validity time end time</p>
        :rtype: str
        """
        return self._StartTimeTo

    @StartTimeTo.setter
    def StartTimeTo(self, StartTimeTo):
        self._StartTimeTo = StartTimeTo

    @property
    def EndTimeFrom(self):
        r"""<p>Voucher expiration time start time</p>
        :rtype: str
        """
        return self._EndTimeFrom

    @EndTimeFrom.setter
    def EndTimeFrom(self, EndTimeFrom):
        self._EndTimeFrom = EndTimeFrom

    @property
    def EndTimeTo(self):
        r"""<p>Voucher expiration time end time</p>
        :rtype: str
        """
        return self._EndTimeTo

    @EndTimeTo.setter
    def EndTimeTo(self, EndTimeTo):
        self._EndTimeTo = EndTimeTo

    @property
    def CreateTimeFrom(self):
        r"""<p>Voucher issuance start time</p>
        :rtype: str
        """
        return self._CreateTimeFrom

    @CreateTimeFrom.setter
    def CreateTimeFrom(self, CreateTimeFrom):
        self._CreateTimeFrom = CreateTimeFrom

    @property
    def CreateTimeTo(self):
        r"""<p>Voucher issuance time end time</p>
        :rtype: str
        """
        return self._CreateTimeTo

    @CreateTimeTo.setter
    def CreateTimeTo(self, CreateTimeTo):
        self._CreateTimeTo = CreateTimeTo

    @property
    def Lang(self):
        r"""<p>Language parameter</p><p>Default value: zh</p><p>Expect the product name to return in Chinese or other languages. Currently only support Chinese and English. Return in Chinese when "zh" is entered or left blank; return in English in other cases.</p>
        :rtype: str
        """
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang


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
        self._StartTimeFrom = params.get("StartTimeFrom")
        self._StartTimeTo = params.get("StartTimeTo")
        self._EndTimeFrom = params.get("EndTimeFrom")
        self._EndTimeTo = params.get("EndTimeTo")
        self._CreateTimeFrom = params.get("CreateTimeFrom")
        self._CreateTimeTo = params.get("CreateTimeTo")
        self._Lang = params.get("Lang")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVoucherInfoResponse(AbstractModel):
    r"""DescribeVoucherInfo response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>Total count</p>
        :type TotalCount: int
        :param _TotalBalance: <p>Total balance (differential)</p>
        :type TotalBalance: int
        :param _VoucherInfos: <p>Voucher information related to</p>
        :type VoucherInfos: list of VoucherInfos
        :param _Unit: <p>Unit of the amount field in the API response</p><p>Default value: micro</p><p>Currency unit: micro (microcent)<br>Voucher issuance and use are processed with 8-digit high-precision, so the currency unit defaults to micro (microcent). If CNY or USD is needed, convert using the following formula:<br>CNY: 1 micro = 0.00000001  yuan<br>USD: 1 micro = 0.00000001  USD</p>
        :type Unit: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TotalBalance = None
        self._VoucherInfos = None
        self._Unit = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>Total count</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalBalance(self):
        r"""<p>Total balance (differential)</p>
        :rtype: int
        """
        return self._TotalBalance

    @TotalBalance.setter
    def TotalBalance(self, TotalBalance):
        self._TotalBalance = TotalBalance

    @property
    def VoucherInfos(self):
        r"""<p>Voucher information related to</p>
        :rtype: list of VoucherInfos
        """
        return self._VoucherInfos

    @VoucherInfos.setter
    def VoucherInfos(self, VoucherInfos):
        self._VoucherInfos = VoucherInfos

    @property
    def Unit(self):
        r"""<p>Unit of the amount field in the API response</p><p>Default value: micro</p><p>Currency unit: micro (microcent)<br>Voucher issuance and use are processed with 8-digit high-precision, so the currency unit defaults to micro (microcent). If CNY or USD is needed, convert using the following formula:<br>CNY: 1 micro = 0.00000001  yuan<br>USD: 1 micro = 0.00000001  USD</p>
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

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
        self._TotalBalance = params.get("TotalBalance")
        if params.get("VoucherInfos") is not None:
            self._VoucherInfos = []
            for item in params.get("VoucherInfos"):
                obj = VoucherInfos()
                obj._deserialize(item)
                self._VoucherInfos.append(obj)
        self._Unit = params.get("Unit")
        self._RequestId = params.get("RequestId")


class DescribeVoucherUsageDetailsRequest(AbstractModel):
    r"""DescribeVoucherUsageDetails request structure.

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
        r"""The number of records per page. The default is 20, and the maximum is 1,000.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""The page number the records start from. The default is 1.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def VoucherId(self):
        r"""The voucher ID.
        :rtype: str
        """
        return self._VoucherId

    @VoucherId.setter
    def VoucherId(self, VoucherId):
        self._VoucherId = VoucherId

    @property
    def Operator(self):
        r"""The operator. The default is the UIN of the current.
        :rtype: str
        """
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
    r"""DescribeVoucherUsageDetails response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total number of vouchers.
        :type TotalCount: int
        :param _TotalUsedAmount: The total amount used. The value of this parameter is the total amount used (USD, rounded to 8 decimal places) multiplied by 100,000,000.
        :type TotalUsedAmount: int
        :param _UsageRecords: Voucher usage record details
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
        r"""The total number of vouchers.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalUsedAmount(self):
        r"""The total amount used. The value of this parameter is the total amount used (USD, rounded to 8 decimal places) multiplied by 100,000,000.
        :rtype: int
        """
        return self._TotalUsedAmount

    @TotalUsedAmount.setter
    def TotalUsedAmount(self, TotalUsedAmount):
        self._TotalUsedAmount = TotalUsedAmount

    @property
    def UsageRecords(self):
        r"""Voucher usage record details
        :rtype: list of UsageRecords
        """
        return self._UsageRecords

    @UsageRecords.setter
    def UsageRecords(self, UsageRecords):
        self._UsageRecords = UsageRecords

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
        self._TotalUsedAmount = params.get("TotalUsedAmount")
        if params.get("UsageRecords") is not None:
            self._UsageRecords = []
            for item in params.get("UsageRecords"):
                obj = UsageRecords()
                obj._deserialize(item)
                self._UsageRecords.append(obj)
        self._RequestId = params.get("RequestId")


class DistributionBillDetail(AbstractModel):
    r"""Objects of reseller bill details

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
        :type Tags: list of BillTagInfo
        :param _BusinessCode: Product code
        :type BusinessCode: str
        :param _ProductCode: Subproduct code
        :type ProductCode: str
        :param _ActionType: Transaction type code
        :type ActionType: str
        :param _RegionId: Region ID
        :type RegionId: str
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _PriceInfo: Price attribute: Other attributes of the component that affect discount pricing besides unit price and duration
        :type PriceInfo: list of str
        :param _AssociatedOrder: Associated transaction document ID: Document ID associated with this transaction, such as a write-off order, the original order, a resettlement order, or the original purchase order number recorded in a refund order.
        :type AssociatedOrder: :class:`tencentcloud.billing.v20180709.models.BillDetailAssociatedOrder`
        :param _Formula: Calculation explanation: A detailed explanation to calculations of billing settlement for special transaction types, such as refund and configuration changes.
        :type Formula: str
        :param _FormulaUrl: Billing Rules: The detailed billing rules for each product shown in the portal explanation link
        :type FormulaUrl: str
        :param _BillMonth: Billing month
        :type BillMonth: str
        :param _BillDay: Billing day
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
        r"""Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        r"""Subproduct name: The subcategory of a Tencent Cloud product purchased by the user, such as CVM - Standard S1.
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        r"""Billing mode: The billing mode, which can be monthly subscription or pay-as-you-go.
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        r"""Project Name: The project to which a resource belongs, which is user-designated. If a resource has not been assigned to a project, it will automatically belong to the default project.
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        r"""Region: The region of a resource, e.g. South China (Guangzhou).
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        r"""Availability zone: availability zone of a resource, e.g. Guangzhou Zone 3.
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        r"""Instance ID: The object ID of a billed resource, such as a CVM instance ID. This object ID may vary due to various forms and contents of resources in different products.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        r"""Instance name: The resource name set by the user in the console. If it is not set, it will be empty by default.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        r"""Transaction type, which can be monthly subscription purchase, monthly subscription renewal, pay-as-you-go deduction, etc.
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        r"""Order ID: The ID of a monthly subscription order.
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def BillId(self):
        r"""Transaction ID: The ID of a settlement bill.
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def PayTime(self):
        r"""Deduction time: The settlement cost deduction time.
        :rtype: str
        """
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def FeeBeginTime(self):
        r"""Usage start time: The time at which product or service usage starts.
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        r"""Usage end time: The time at which product or service usage ends.
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ComponentSet(self):
        r"""List of components.
        :rtype: list of BillDetailComponent
        """
        return self._ComponentSet

    @ComponentSet.setter
    def ComponentSet(self, ComponentSet):
        self._ComponentSet = ComponentSet

    @property
    def OwnerUin(self):
        r"""Owner account ID: The account ID of the actual resource user.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        r"""Operator account ID: The account or role ID of the operator who purchases or activates a resource.
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def Tags(self):
        r"""Tag information.
        :rtype: list of BillTagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def BusinessCode(self):
        r"""Product code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProductCode(self):
        r"""Subproduct code
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ActionType(self):
        r"""Transaction type code
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def RegionId(self):
        r"""Region ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PriceInfo(self):
        r"""Price attribute: Other attributes of the component that affect discount pricing besides unit price and duration
        :rtype: list of str
        """
        return self._PriceInfo

    @PriceInfo.setter
    def PriceInfo(self, PriceInfo):
        self._PriceInfo = PriceInfo

    @property
    def AssociatedOrder(self):
        r"""Associated transaction document ID: Document ID associated with this transaction, such as a write-off order, the original order, a resettlement order, or the original purchase order number recorded in a refund order.
        :rtype: :class:`tencentcloud.billing.v20180709.models.BillDetailAssociatedOrder`
        """
        return self._AssociatedOrder

    @AssociatedOrder.setter
    def AssociatedOrder(self, AssociatedOrder):
        self._AssociatedOrder = AssociatedOrder

    @property
    def Formula(self):
        r"""Calculation explanation: A detailed explanation to calculations of billing settlement for special transaction types, such as refund and configuration changes.
        :rtype: str
        """
        return self._Formula

    @Formula.setter
    def Formula(self, Formula):
        self._Formula = Formula

    @property
    def FormulaUrl(self):
        r"""Billing Rules: The detailed billing rules for each product shown in the portal explanation link
        :rtype: str
        """
        return self._FormulaUrl

    @FormulaUrl.setter
    def FormulaUrl(self, FormulaUrl):
        self._FormulaUrl = FormulaUrl

    @property
    def BillMonth(self):
        r"""Billing month
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def BillDay(self):
        r"""Billing day
        :rtype: str
        """
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
    r"""The products that are not applicable.

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
        r"""The names of non-applicable products.
        :rtype: str
        """
        return self._GoodsName

    @GoodsName.setter
    def GoodsName(self, GoodsName):
        self._GoodsName = GoodsName

    @property
    def PayMode(self):
        r"""`postPay`: pay-as-you-go; `prePay`: prepaid; `riPay`: reserved instance; empty or `*`: all.
        :rtype: str
        """
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
        


class GatherResourceSummary(AbstractModel):
    r"""Resource collection summary

    """

    def __init__(self):
        r"""
        :param _PayerUin: Payer UIN: Account ID of the payer, which is the unique account identifier for the user in Tencent Cloud.
        :type PayerUin: str
        :param _OwnerUin: User UIN: Account ID of the actual resource user
        :type OwnerUin: str
        :param _OperateUin: Operator account ID (the resource account ID or role ID opened by prepaid resource ordering or postpaid operation)
        :type OperateUin: str
        :param _InstanceType: Instance type code
        :type InstanceType: str
        :param _InstanceTypeName: Instance type: The type of an instance corresponding to the product service purchased, including resource packages, RI, SP, and spot instances. It is displayed as "-" by default for regular instances.
        :type InstanceTypeName: str
        :param _ResourceId: Resource ID: Resources vary by product, and the content is not identical. For example, Cloud Virtual Machine (CVM) corresponds to the instance ID. If the product is split, it shows the split item ID, such as COS bucket ID and CDN domain name.
        :type ResourceId: str
        :param _ResourceName: Instance name: The name set by the user for the resource in the console, which is empty by default if not set. If the product is split, it shows the split resource alias.
        :type ResourceName: str
        :param _TreeNodeUniqKey: Unique identifier of a cost allocation unit
        :type TreeNodeUniqKey: str
        :param _TreeNodeUniqKeyName: Name of a cost allocation unit
        :type TreeNodeUniqKeyName: str
        :param _RuleId: Allocation rule ID hit by the resource
        :type RuleId: int
        :param _RuleName: Allocation rule name hit by the resource
        :type RuleName: str
        :param _BusinessCode: Product code
        :type BusinessCode: str
        :param _BusinessCodeName: Product name: Various cloud products purchased by users
        :type BusinessCodeName: str
        :param _ItemCode: Component name code
        :type ItemCode: str
        :param _ItemCodeName: Component name: The specific component of a product or service purchased by the user
        :type ItemCodeName: str
        :param _RegionId: Region ID
        :type RegionId: int
        :param _RegionName: Region name: The region where the resource is located
        :type RegionName: str
        :param _Tag: Allocation tag: The resource-bound tag
        :type Tag: list of BillTag
        :param _RealTotalCost: Discounted total: discounted total = (Original Price - Original Price Deducted by a Reserved Instance - Savings Plan Deduction from Original Price) * Discount Rate
        :type RealTotalCost: str
        :param _CashPayAmount: Cash account expenditure (CNY): The amount paid through the cash account
        :type CashPayAmount: str
        :param _VoucherPayAmount: Promo voucher expenditure (CNY): The amount paid using various vouchers (such as promo vouchers and cash vouchers)
        :type VoucherPayAmount: str
        :param _IncentivePayAmount: Gift account expenditure (CNY): The amount paid using free credits
        :type IncentivePayAmount: str
        :param _TransferPayAmount: Royalty account expenditure (CNY): The amount paid through the royalty account
        :type TransferPayAmount: str
        :param _AllocationType: Cost collection type: The source types of fees, including allocated, collection and unallocated.
0 - Allocation
1 - Collection
-1 - Unallocated
        :type AllocationType: int
        :param _BelongTreeNodeUniqKey: Information of the current allocation unit
        :type BelongTreeNodeUniqKey: :class:`tencentcloud.billing.v20180709.models.AllocationTreeNode`
        :param _BelongRule: Information on allocation rules hit by the current resource
        :type BelongRule: :class:`tencentcloud.billing.v20180709.models.AllocationRule`
        :param _OtherTreeNodeUniqKeys: Information on other allocation units
        :type OtherTreeNodeUniqKeys: list of AllocationTreeNode
        :param _OtherRules: Information on other hit rules
        :type OtherRules: list of AllocationRule
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _ProjectName: Project name: The Project to which a resource belongs, which is independently allocated by the user for the resource in the console. If a resource has not been allocated to an Project, it will be a default Project.
        :type ProjectName: str
        :param _ProductCode: Subproduct code
        :type ProductCode: str
        :param _ProductCodeName: Subproduct name: Product subdivision type purchased by the user
        :type ProductCodeName: str
        :param _PayMode: Billing mode code
        :type PayMode: str
        :param _PayModeName: Billing mode: Resource billing mode, which can be monthly subscription or pay-as-you-go.
        :type PayModeName: str
        :param _ActionType: Transaction type code
        :type ActionType: str
        :param _ActionTypeName: Transaction type: Detailed transaction type
        :type ActionTypeName: str
        :param _SplitItemId: Split item ID: The ID of the split item involved in the split product, such as COS bucket ID and CDN domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SplitItemId: str
        :param _SplitItemName: Split item name: The split item involved in the split product
Note: This field may return null, indicating that no valid values can be obtained.
        :type SplitItemName: str
        """
        self._PayerUin = None
        self._OwnerUin = None
        self._OperateUin = None
        self._InstanceType = None
        self._InstanceTypeName = None
        self._ResourceId = None
        self._ResourceName = None
        self._TreeNodeUniqKey = None
        self._TreeNodeUniqKeyName = None
        self._RuleId = None
        self._RuleName = None
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._ItemCode = None
        self._ItemCodeName = None
        self._RegionId = None
        self._RegionName = None
        self._Tag = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._VoucherPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None
        self._AllocationType = None
        self._BelongTreeNodeUniqKey = None
        self._BelongRule = None
        self._OtherTreeNodeUniqKeys = None
        self._OtherRules = None
        self._ProjectId = None
        self._ProjectName = None
        self._ProductCode = None
        self._ProductCodeName = None
        self._PayMode = None
        self._PayModeName = None
        self._ActionType = None
        self._ActionTypeName = None
        self._SplitItemId = None
        self._SplitItemName = None

    @property
    def PayerUin(self):
        r"""Payer UIN: Account ID of the payer, which is the unique account identifier for the user in Tencent Cloud.
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        r"""User UIN: Account ID of the actual resource user
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        r"""Operator account ID (the resource account ID or role ID opened by prepaid resource ordering or postpaid operation)
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def InstanceType(self):
        r"""Instance type code
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceTypeName(self):
        r"""Instance type: The type of an instance corresponding to the product service purchased, including resource packages, RI, SP, and spot instances. It is displayed as "-" by default for regular instances.
        :rtype: str
        """
        return self._InstanceTypeName

    @InstanceTypeName.setter
    def InstanceTypeName(self, InstanceTypeName):
        self._InstanceTypeName = InstanceTypeName

    @property
    def ResourceId(self):
        r"""Resource ID: Resources vary by product, and the content is not identical. For example, Cloud Virtual Machine (CVM) corresponds to the instance ID. If the product is split, it shows the split item ID, such as COS bucket ID and CDN domain name.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        r"""Instance name: The name set by the user for the resource in the console, which is empty by default if not set. If the product is split, it shows the split resource alias.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def TreeNodeUniqKey(self):
        r"""Unique identifier of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def TreeNodeUniqKeyName(self):
        r"""Name of a cost allocation unit
        :rtype: str
        """
        return self._TreeNodeUniqKeyName

    @TreeNodeUniqKeyName.setter
    def TreeNodeUniqKeyName(self, TreeNodeUniqKeyName):
        self._TreeNodeUniqKeyName = TreeNodeUniqKeyName

    @property
    def RuleId(self):
        r"""Allocation rule ID hit by the resource
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        r"""Allocation rule name hit by the resource
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def BusinessCode(self):
        r"""Product code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        r"""Product name: Various cloud products purchased by users
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ItemCode(self):
        r"""Component name code
        :rtype: str
        """
        return self._ItemCode

    @ItemCode.setter
    def ItemCode(self, ItemCode):
        self._ItemCode = ItemCode

    @property
    def ItemCodeName(self):
        r"""Component name: The specific component of a product or service purchased by the user
        :rtype: str
        """
        return self._ItemCodeName

    @ItemCodeName.setter
    def ItemCodeName(self, ItemCodeName):
        self._ItemCodeName = ItemCodeName

    @property
    def RegionId(self):
        r"""Region ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        r"""Region name: The region where the resource is located
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def Tag(self):
        r"""Allocation tag: The resource-bound tag
        :rtype: list of BillTag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def RealTotalCost(self):
        r"""Discounted total: discounted total = (Original Price - Original Price Deducted by a Reserved Instance - Savings Plan Deduction from Original Price) * Discount Rate
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        r"""Cash account expenditure (CNY): The amount paid through the cash account
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def VoucherPayAmount(self):
        r"""Promo voucher expenditure (CNY): The amount paid using various vouchers (such as promo vouchers and cash vouchers)
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Gift account expenditure (CNY): The amount paid using free credits
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        r"""Royalty account expenditure (CNY): The amount paid through the royalty account
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def AllocationType(self):
        r"""Cost collection type: The source types of fees, including allocated, collection and unallocated.
0 - Allocation
1 - Collection
-1 - Unallocated
        :rtype: int
        """
        return self._AllocationType

    @AllocationType.setter
    def AllocationType(self, AllocationType):
        self._AllocationType = AllocationType

    @property
    def BelongTreeNodeUniqKey(self):
        r"""Information of the current allocation unit
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationTreeNode`
        """
        return self._BelongTreeNodeUniqKey

    @BelongTreeNodeUniqKey.setter
    def BelongTreeNodeUniqKey(self, BelongTreeNodeUniqKey):
        self._BelongTreeNodeUniqKey = BelongTreeNodeUniqKey

    @property
    def BelongRule(self):
        r"""Information on allocation rules hit by the current resource
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationRule`
        """
        return self._BelongRule

    @BelongRule.setter
    def BelongRule(self, BelongRule):
        self._BelongRule = BelongRule

    @property
    def OtherTreeNodeUniqKeys(self):
        r"""Information on other allocation units
        :rtype: list of AllocationTreeNode
        """
        return self._OtherTreeNodeUniqKeys

    @OtherTreeNodeUniqKeys.setter
    def OtherTreeNodeUniqKeys(self, OtherTreeNodeUniqKeys):
        self._OtherTreeNodeUniqKeys = OtherTreeNodeUniqKeys

    @property
    def OtherRules(self):
        r"""Information on other hit rules
        :rtype: list of AllocationRule
        """
        return self._OtherRules

    @OtherRules.setter
    def OtherRules(self, OtherRules):
        self._OtherRules = OtherRules

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""Project name: The Project to which a resource belongs, which is independently allocated by the user for the resource in the console. If a resource has not been allocated to an Project, it will be a default Project.
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProductCode(self):
        r"""Subproduct code
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductCodeName(self):
        r"""Subproduct name: Product subdivision type purchased by the user
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayMode(self):
        r"""Billing mode code
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        r"""Billing mode: Resource billing mode, which can be monthly subscription or pay-as-you-go.
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ActionType(self):
        r"""Transaction type code
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        r"""Transaction type: Detailed transaction type
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def SplitItemId(self):
        warnings.warn("parameter `SplitItemId` is deprecated", DeprecationWarning) 

        r"""Split item ID: The ID of the split item involved in the split product, such as COS bucket ID and CDN domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SplitItemId

    @SplitItemId.setter
    def SplitItemId(self, SplitItemId):
        warnings.warn("parameter `SplitItemId` is deprecated", DeprecationWarning) 

        self._SplitItemId = SplitItemId

    @property
    def SplitItemName(self):
        warnings.warn("parameter `SplitItemName` is deprecated", DeprecationWarning) 

        r"""Split item name: The split item involved in the split product
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SplitItemName

    @SplitItemName.setter
    def SplitItemName(self, SplitItemName):
        warnings.warn("parameter `SplitItemName` is deprecated", DeprecationWarning) 

        self._SplitItemName = SplitItemName


    def _deserialize(self, params):
        self._PayerUin = params.get("PayerUin")
        self._OwnerUin = params.get("OwnerUin")
        self._OperateUin = params.get("OperateUin")
        self._InstanceType = params.get("InstanceType")
        self._InstanceTypeName = params.get("InstanceTypeName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._TreeNodeUniqKeyName = params.get("TreeNodeUniqKeyName")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._ItemCode = params.get("ItemCode")
        self._ItemCodeName = params.get("ItemCodeName")
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = BillTag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._AllocationType = params.get("AllocationType")
        if params.get("BelongTreeNodeUniqKey") is not None:
            self._BelongTreeNodeUniqKey = AllocationTreeNode()
            self._BelongTreeNodeUniqKey._deserialize(params.get("BelongTreeNodeUniqKey"))
        if params.get("BelongRule") is not None:
            self._BelongRule = AllocationRule()
            self._BelongRule._deserialize(params.get("BelongRule"))
        if params.get("OtherTreeNodeUniqKeys") is not None:
            self._OtherTreeNodeUniqKeys = []
            for item in params.get("OtherTreeNodeUniqKeys"):
                obj = AllocationTreeNode()
                obj._deserialize(item)
                self._OtherTreeNodeUniqKeys.append(obj)
        if params.get("OtherRules") is not None:
            self._OtherRules = []
            for item in params.get("OtherRules"):
                obj = AllocationRule()
                obj._deserialize(item)
                self._OtherRules.append(obj)
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._ProductCode = params.get("ProductCode")
        self._ProductCodeName = params.get("ProductCodeName")
        self._PayMode = params.get("PayMode")
        self._PayModeName = params.get("PayModeName")
        self._ActionType = params.get("ActionType")
        self._ActionTypeName = params.get("ActionTypeName")
        self._SplitItemId = params.get("SplitItemId")
        self._SplitItemName = params.get("SplitItemName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatherRuleSummary(AbstractModel):
    r"""List of collection rules.

    """

    def __init__(self):
        r"""
        :param _RuleDetail: Cost allocation regular expression.
        :type RuleDetail: :class:`tencentcloud.billing.v20180709.models.AllocationRuleExpression`
        """
        self._RuleDetail = None

    @property
    def RuleDetail(self):
        r"""Cost allocation regular expression.
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationRuleExpression`
        """
        return self._RuleDetail

    @RuleDetail.setter
    def RuleDetail(self, RuleDetail):
        self._RuleDetail = RuleDetail


    def _deserialize(self, params):
        if params.get("RuleDetail") is not None:
            self._RuleDetail = AllocationRuleExpression()
            self._RuleDetail._deserialize(params.get("RuleDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAllocationRuleRequest(AbstractModel):
    r"""ModifyAllocationRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: The edited sharing rule ID.
        :type RuleId: int
        :param _Name: Edited sharing rule name.
        :type Name: str
        :param _Type: Public sharing policy types, enumeration values are as follows: 1 - custom sharing proportion 2 - proportional allocation 3 - allocation by proportion.
        :type Type: int
        :param _RuleDetail: Edited share rules expression.
        :type RuleDetail: :class:`tencentcloud.billing.v20180709.models.AllocationRuleExpression`
        :param _RatioDetail: Edited sharing proportion expression.
        :type RatioDetail: list of AllocationRationExpression
        :param _Month: Month, which is the current month by default if not provided.
        :type Month: str
        """
        self._RuleId = None
        self._Name = None
        self._Type = None
        self._RuleDetail = None
        self._RatioDetail = None
        self._Month = None

    @property
    def RuleId(self):
        r"""The edited sharing rule ID.
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Name(self):
        r"""Edited sharing rule name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""Public sharing policy types, enumeration values are as follows: 1 - custom sharing proportion 2 - proportional allocation 3 - allocation by proportion.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RuleDetail(self):
        r"""Edited share rules expression.
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationRuleExpression`
        """
        return self._RuleDetail

    @RuleDetail.setter
    def RuleDetail(self, RuleDetail):
        self._RuleDetail = RuleDetail

    @property
    def RatioDetail(self):
        r"""Edited sharing proportion expression.
        :rtype: list of AllocationRationExpression
        """
        return self._RatioDetail

    @RatioDetail.setter
    def RatioDetail(self, RatioDetail):
        self._RatioDetail = RatioDetail

    @property
    def Month(self):
        r"""Month, which is the current month by default if not provided.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("RuleDetail") is not None:
            self._RuleDetail = AllocationRuleExpression()
            self._RuleDetail._deserialize(params.get("RuleDetail"))
        if params.get("RatioDetail") is not None:
            self._RatioDetail = []
            for item in params.get("RatioDetail"):
                obj = AllocationRationExpression()
                obj._deserialize(item)
                self._RatioDetail.append(obj)
        self._Month = params.get("Month")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAllocationRuleResponse(AbstractModel):
    r"""ModifyAllocationRule response structure.

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


class ModifyAllocationUnitRequest(AbstractModel):
    r"""ModifyAllocationUnit request structure.

    """

    def __init__(self):
        r"""
        :param _Id: ID of the modified cost allocation unit.
        :type Id: int
        :param _Name: Modified cost allocation unit name.
        :type Name: str
        :param _SourceName: Modified cost allocation unit source organization name.
        :type SourceName: str
        :param _SourceId: Modified allocation unit source organization ID.
        :type SourceId: str
        :param _Remark: Cost allocation unit remark description.
        :type Remark: str
        :param _Month: Month, the current month by default if not provided.
        :type Month: str
        """
        self._Id = None
        self._Name = None
        self._SourceName = None
        self._SourceId = None
        self._Remark = None
        self._Month = None

    @property
    def Id(self):
        r"""ID of the modified cost allocation unit.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""Modified cost allocation unit name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SourceName(self):
        r"""Modified cost allocation unit source organization name.
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def SourceId(self):
        r"""Modified allocation unit source organization ID.
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def Remark(self):
        r"""Cost allocation unit remark description.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Month(self):
        r"""Month, the current month by default if not provided.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._SourceName = params.get("SourceName")
        self._SourceId = params.get("SourceId")
        self._Remark = params.get("Remark")
        self._Month = params.get("Month")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAllocationUnitResponse(AbstractModel):
    r"""ModifyAllocationUnit response structure.

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


class ModifyGatherRuleRequest(AbstractModel):
    r"""ModifyGatherRule request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Edit collection rule ID.
        :type Id: int
        :param _RuleDetail: Rule detail of the edited collection rule.
        :type RuleDetail: :class:`tencentcloud.billing.v20180709.models.AllocationRuleExpression`
        :param _Month: Month, which is the current month by default if not provided.
        :type Month: str
        """
        self._Id = None
        self._RuleDetail = None
        self._Month = None

    @property
    def Id(self):
        r"""Edit collection rule ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleDetail(self):
        r"""Rule detail of the edited collection rule.
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationRuleExpression`
        """
        return self._RuleDetail

    @RuleDetail.setter
    def RuleDetail(self, RuleDetail):
        self._RuleDetail = RuleDetail

    @property
    def Month(self):
        r"""Month, which is the current month by default if not provided.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("RuleDetail") is not None:
            self._RuleDetail = AllocationRuleExpression()
            self._RuleDetail._deserialize(params.get("RuleDetail"))
        self._Month = params.get("Month")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGatherRuleResponse(AbstractModel):
    r"""ModifyGatherRule response structure.

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


class OperateRsp(AbstractModel):
    r"""Operate related resources return detail

    """

    def __init__(self):
        r"""
        :param _Code: Operation failure code at the instance dimension
Note: This field may return null, indicating that no valid values can be obtained.
        :type Code: int
        :param _Message: Failure reason for operating related resources
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _InstanceId: Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        """
        self._Code = None
        self._Message = None
        self._InstanceId = None

    @property
    def Code(self):
        r"""Operation failure code at the instance dimension
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""Failure reason for operating related resources
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def InstanceId(self):
        r"""Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayDealsRequest(AbstractModel):
    r"""PayDeals request structure.

    """

    def __init__(self):
        r"""
        :param _OrderIds: Specifies one or more Sub-order No. that need to pay. must pass either this parameter or the BigDealIds field, but not both.
        :type OrderIds: list of str
        :param _AutoVoucher: Whether to automatically use a voucher. valid values: 1 (yes), 0 (no). default: 0.
        :type AutoVoucher: int
        :param _VoucherIds: Voucher ID list. currently only supports specifying one voucher.
        :type VoucherIds: list of str
        :param _BigDealIds: Specifies one or more Order No. that need to pay. must pass either this parameter or the OrderIds field.
        :type BigDealIds: list of str
        :param _AgentPay: 0 self pay, 3 group agent, 4 reseller places a product-level payment order for customers. default 0.
        :type AgentPay: int
        :param _CpsUin: Disregard it.
        :type CpsUin: str
        """
        self._OrderIds = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._BigDealIds = None
        self._AgentPay = None
        self._CpsUin = None

    @property
    def OrderIds(self):
        r"""Specifies one or more Sub-order No. that need to pay. must pass either this parameter or the BigDealIds field, but not both.
        :rtype: list of str
        """
        return self._OrderIds

    @OrderIds.setter
    def OrderIds(self, OrderIds):
        self._OrderIds = OrderIds

    @property
    def AutoVoucher(self):
        r"""Whether to automatically use a voucher. valid values: 1 (yes), 0 (no). default: 0.
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""Voucher ID list. currently only supports specifying one voucher.
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def BigDealIds(self):
        r"""Specifies one or more Order No. that need to pay. must pass either this parameter or the OrderIds field.
        :rtype: list of str
        """
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def AgentPay(self):
        r"""0 self pay, 3 group agent, 4 reseller places a product-level payment order for customers. default 0.
        :rtype: int
        """
        return self._AgentPay

    @AgentPay.setter
    def AgentPay(self, AgentPay):
        self._AgentPay = AgentPay

    @property
    def CpsUin(self):
        r"""Disregard it.
        :rtype: str
        """
        return self._CpsUin

    @CpsUin.setter
    def CpsUin(self, CpsUin):
        self._CpsUin = CpsUin


    def _deserialize(self, params):
        self._OrderIds = params.get("OrderIds")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._BigDealIds = params.get("BigDealIds")
        self._AgentPay = params.get("AgentPay")
        self._CpsUin = params.get("CpsUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayDealsResponse(AbstractModel):
    r"""PayDeals response structure.

    """

    def __init__(self):
        r"""
        :param _OrderIds: Specifies the array of Sub-order No. with payment successful.
        :type OrderIds: list of str
        :param _ResourceIds: Specifies the Id array of resources with payment successful.
        :type ResourceIds: list of str
        :param _BigDealIds: Specifies the array of Order No. with payment successful.
        :type BigDealIds: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OrderIds = None
        self._ResourceIds = None
        self._BigDealIds = None
        self._RequestId = None

    @property
    def OrderIds(self):
        r"""Specifies the array of Sub-order No. with payment successful.
        :rtype: list of str
        """
        return self._OrderIds

    @OrderIds.setter
    def OrderIds(self, OrderIds):
        self._OrderIds = OrderIds

    @property
    def ResourceIds(self):
        r"""Specifies the Id array of resources with payment successful.
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def BigDealIds(self):
        r"""Specifies the array of Order No. with payment successful.
        :rtype: list of str
        """
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

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
        self._OrderIds = params.get("OrderIds")
        self._ResourceIds = params.get("ResourceIds")
        self._BigDealIds = params.get("BigDealIds")
        self._RequestId = params.get("RequestId")


class PayModeSummaryOverviewItem(AbstractModel):
    r"""Detailed summary of costs by billing mode

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
        r"""Billing mode code
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        r"""Billing mode, which can be monthly subscription or pay-as-you-go.
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def RealTotalCostRatio(self):
        r"""Cost ratio, to two decimal points
        :rtype: str
        """
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        r"""Total amount after discount
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        r"""Cash credit: The amount paid from the user’s cash balance
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Free credit: The amount paid with the user’s free credit
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        r"""Voucher payment: The voucher deduction amount
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        r"""Commission credit: The amount paid with the user’s commission credit.
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def TotalCost(self):
        r"""The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Detail(self):
        r"""Detailed summary of costs by transaction type
        :rtype: list of ActionSummaryOverviewItem
        """
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
        


class ProductInfo(AbstractModel):
    r"""Product details

    """

    def __init__(self):
        r"""
        :param _Name: Product detail name identifier
        :type Name: str
        :param _Value: Product details
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""Product detail name identifier
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""Product details
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
        


class ProjectSummaryOverviewItem(AbstractModel):
    r"""Detailed summary of purchases by project

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
        r"""Project ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""Project name: The project to which a resource belongs, which is user-designated. If a resource has not been assigned to a project, it will automatically belong to the default project.
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RealTotalCostRatio(self):
        r"""Cost ratio, to two decimal points
        :rtype: str
        """
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        r"""Total amount after discount
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        r"""Cash credit: The amount paid from the user’s cash account
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Free credit: The amount paid with the user’s free credit
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        r"""Voucher payment: The voucher deduction amount
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        r"""Commission credit: The amount paid with the user’s commission credit.
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def BillMonth(self):
        r"""Billing month, e.g. `2019-08`
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def TotalCost(self):
        r"""The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :rtype: str
        """
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
        


class RefundInstanceRequest(AbstractModel):
    r"""RefundInstance request structure.

    """

    def __init__(self):
        r"""
        :param _ClientToken: ClientToken is a unique, case-sensitive string generated by the client, no more than 64 ASCII characters. for example, ClientToken=123e4567-e89b-12d3-a456-42665544****.
        :type ClientToken: str
        :param _ProductCode: Product code.
        :type ProductCode: str
        :param _SubProductCode: Sub-product code.
        :type SubProductCode: str
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _RegionCode: Region code.
        :type RegionCode: str
        """
        self._ClientToken = None
        self._ProductCode = None
        self._SubProductCode = None
        self._InstanceId = None
        self._RegionCode = None

    @property
    def ClientToken(self):
        r"""ClientToken is a unique, case-sensitive string generated by the client, no more than 64 ASCII characters. for example, ClientToken=123e4567-e89b-12d3-a456-42665544****.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ProductCode(self):
        r"""Product code.
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def SubProductCode(self):
        r"""Sub-product code.
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RegionCode(self):
        r"""Region code.
        :rtype: str
        """
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode


    def _deserialize(self, params):
        self._ClientToken = params.get("ClientToken")
        self._ProductCode = params.get("ProductCode")
        self._SubProductCode = params.get("SubProductCode")
        self._InstanceId = params.get("InstanceId")
        self._RegionCode = params.get("RegionCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundInstanceResponse(AbstractModel):
    r"""RefundInstance response structure.

    """

    def __init__(self):
        r"""
        :param _OrderIdList: Order ID list
        :type OrderIdList: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OrderIdList = None
        self._RequestId = None

    @property
    def OrderIdList(self):
        r"""Order ID list
        :rtype: list of str
        """
        return self._OrderIdList

    @OrderIdList.setter
    def OrderIdList(self, OrderIdList):
        self._OrderIdList = OrderIdList

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
        self._OrderIdList = params.get("OrderIdList")
        self._RequestId = params.get("RequestId")


class RegionSummaryOverviewItem(AbstractModel):
    r"""Detailed summary of purchases by region

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID
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
        r"""Region ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        r"""Region: The region to which a resource belongs, such as South China (Guangzhou).
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RealTotalCostRatio(self):
        r"""Cost ratio, to two decimal points
        :rtype: str
        """
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        r"""Total amount after discount
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        r"""Cash credit: The amount paid from the user’s cash account
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Free credit: The amount paid with the user’s free credit
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        r"""Voucher payment: The voucher deduction amount
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        r"""Commission credit: The amount paid with the user’s commission credit.
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def BillMonth(self):
        r"""Billing month, e.g. `2019-08`
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def TotalCost(self):
        r"""The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :rtype: str
        """
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
        


class RenewInstance(AbstractModel):
    r"""Resource instance information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _ProductCode: Product code
        :type ProductCode: str
        :param _SubProductCode: Subproduct code
        :type SubProductCode: str
        :param _RegionCode: Region encoding
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionCode: str
        :param _Status: Instance status:
NORMAL
ISOLATED Isolated
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _RenewFlag: Renewal flag:
NOTIFY_AND_MANUAL_RENEW: manual renewal
NOTIFY_AND_AUTO_RENEW: auto-renewal.
DISABLE_NOTIFY_AND_MANUAL_RENEW: non-renewal upon expiration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: str
        :param _ExpireTime: Instance expiration time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _InstanceName: Instance alias: The name set by the user for the instance in the console, which is empty by default if not set.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _ProductName: Product name: Cloud products purchased by users, such as Cloud Virtual Machine (CVM)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProductName: str
        :param _ProjectName: Project name: Instance Ownership of the project. User can autonomously assign project to the instance on the console. Default project if not allocated.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectName: str
        :param _RenewPeriod: Automatic renewal cycle length
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewPeriod: int
        :param _RenewPeriodUnit: Automatic renewal cycle unit: y year, m month
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewPeriodUnit: str
        """
        self._InstanceId = None
        self._ProductCode = None
        self._SubProductCode = None
        self._RegionCode = None
        self._Status = None
        self._RenewFlag = None
        self._ExpireTime = None
        self._InstanceName = None
        self._ProductName = None
        self._ProjectName = None
        self._RenewPeriod = None
        self._RenewPeriodUnit = None

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProductCode(self):
        r"""Product code
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def SubProductCode(self):
        r"""Subproduct code
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def RegionCode(self):
        r"""Region encoding
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode

    @property
    def Status(self):
        r"""Instance status:
NORMAL
ISOLATED Isolated
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RenewFlag(self):
        r"""Renewal flag:
NOTIFY_AND_MANUAL_RENEW: manual renewal
NOTIFY_AND_AUTO_RENEW: auto-renewal.
DISABLE_NOTIFY_AND_MANUAL_RENEW: non-renewal upon expiration.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ExpireTime(self):
        r"""Instance expiration time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def InstanceName(self):
        r"""Instance alias: The name set by the user for the instance in the console, which is empty by default if not set.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ProductName(self):
        r"""Product name: Cloud products purchased by users, such as Cloud Virtual Machine (CVM)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProjectName(self):
        r"""Project name: Instance Ownership of the project. User can autonomously assign project to the instance on the console. Default project if not allocated.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RenewPeriod(self):
        r"""Automatic renewal cycle length
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RenewPeriod

    @RenewPeriod.setter
    def RenewPeriod(self, RenewPeriod):
        self._RenewPeriod = RenewPeriod

    @property
    def RenewPeriodUnit(self):
        r"""Automatic renewal cycle unit: y year, m month
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RenewPeriodUnit

    @RenewPeriodUnit.setter
    def RenewPeriodUnit(self, RenewPeriodUnit):
        self._RenewPeriodUnit = RenewPeriodUnit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProductCode = params.get("ProductCode")
        self._SubProductCode = params.get("SubProductCode")
        self._RegionCode = params.get("RegionCode")
        self._Status = params.get("Status")
        self._RenewFlag = params.get("RenewFlag")
        self._ExpireTime = params.get("ExpireTime")
        self._InstanceName = params.get("InstanceName")
        self._ProductName = params.get("ProductName")
        self._ProjectName = params.get("ProjectName")
        self._RenewPeriod = params.get("RenewPeriod")
        self._RenewPeriodUnit = params.get("RenewPeriodUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceRequest(AbstractModel):
    r"""RenewInstance request structure.

    """

    def __init__(self):
        r"""
        :param _ClientToken: ClientToken is a unique, case-sensitive string generated by the client, with no more than 64 ASCII characters. for example, ClientToken=123e4567-e89b-12d3-a456-42665544.
        :type ClientToken: str
        :param _ProductCode: Product code.
        :type ProductCode: str
        :param _SubProductCode: Sub-product code.
        :type SubProductCode: str
        :param _RegionCode: Region code.
        :type RegionCode: str
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Period: Manual renewal duration, upper limit: 36, default value is 1.
        :type Period: int
        :param _PeriodUnit: Manual renewal duration unit. available values: 
m: renew monthly, 
y: renew annually. 
default value is m.
        :type PeriodUnit: str
        """
        self._ClientToken = None
        self._ProductCode = None
        self._SubProductCode = None
        self._RegionCode = None
        self._InstanceId = None
        self._Period = None
        self._PeriodUnit = None

    @property
    def ClientToken(self):
        r"""ClientToken is a unique, case-sensitive string generated by the client, with no more than 64 ASCII characters. for example, ClientToken=123e4567-e89b-12d3-a456-42665544.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ProductCode(self):
        r"""Product code.
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def SubProductCode(self):
        r"""Sub-product code.
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def RegionCode(self):
        r"""Region code.
        :rtype: str
        """
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Period(self):
        r"""Manual renewal duration, upper limit: 36, default value is 1.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def PeriodUnit(self):
        r"""Manual renewal duration unit. available values: 
m: renew monthly, 
y: renew annually. 
default value is m.
        :rtype: str
        """
        return self._PeriodUnit

    @PeriodUnit.setter
    def PeriodUnit(self, PeriodUnit):
        self._PeriodUnit = PeriodUnit


    def _deserialize(self, params):
        self._ClientToken = params.get("ClientToken")
        self._ProductCode = params.get("ProductCode")
        self._SubProductCode = params.get("SubProductCode")
        self._RegionCode = params.get("RegionCode")
        self._InstanceId = params.get("InstanceId")
        self._Period = params.get("Period")
        self._PeriodUnit = params.get("PeriodUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceResponse(AbstractModel):
    r"""RenewInstance response structure.

    """

    def __init__(self):
        r"""
        :param _OrderIdList: Order ID list
        :type OrderIdList: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OrderIdList = None
        self._RequestId = None

    @property
    def OrderIdList(self):
        r"""Order ID list
        :rtype: list of str
        """
        return self._OrderIdList

    @OrderIdList.setter
    def OrderIdList(self, OrderIdList):
        self._OrderIdList = OrderIdList

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
        self._OrderIdList = params.get("OrderIdList")
        self._RequestId = params.get("RequestId")


class ResourceSpuSet(AbstractModel):
    r"""Quotation for 4-tier product details

    """

    def __init__(self):
        r"""
        :param _SpuNameZh: Quoted subproduct (Chinese)
        :type SpuNameZh: str
        :param _SpuNameEn: Quoted subproduct (English)
        :type SpuNameEn: str
        :param _CategoryNameZh: Quoted product (Chinese)
        :type CategoryNameZh: str
        :param _CategoryNameEn: Quoted product (English)
        :type CategoryNameEn: str
        :param _BusinessCode: Product code
        :type BusinessCode: str
        :param _BusinessNameZh: Product name (Chinese)
        :type BusinessNameZh: str
        :param _BusinessNameEn: Product name (English)
        :type BusinessNameEn: str
        :param _ProductCode: Subproduct code
        :type ProductCode: str
        :param _ProductNameZh: Subproduct name (Chinese)
        :type ProductNameZh: str
        :param _ProductNameEn: Subproduct name (English)
        :type ProductNameEn: str
        :param _ComponentCode: Component type code
        :type ComponentCode: str
        :param _ComponentNameZh: Component type name (Chinese)
        :type ComponentNameZh: str
        :param _ComponentNameEn: Component type name (English)
        :type ComponentNameEn: str
        :param _ItemCode: Component code
        :type ItemCode: str
        :param _ItemNameZh: Component name (Chinese)
        :type ItemNameZh: str
        :param _ItemNameEn: Component name (English)
        :type ItemNameEn: str
        """
        self._SpuNameZh = None
        self._SpuNameEn = None
        self._CategoryNameZh = None
        self._CategoryNameEn = None
        self._BusinessCode = None
        self._BusinessNameZh = None
        self._BusinessNameEn = None
        self._ProductCode = None
        self._ProductNameZh = None
        self._ProductNameEn = None
        self._ComponentCode = None
        self._ComponentNameZh = None
        self._ComponentNameEn = None
        self._ItemCode = None
        self._ItemNameZh = None
        self._ItemNameEn = None

    @property
    def SpuNameZh(self):
        r"""Quoted subproduct (Chinese)
        :rtype: str
        """
        return self._SpuNameZh

    @SpuNameZh.setter
    def SpuNameZh(self, SpuNameZh):
        self._SpuNameZh = SpuNameZh

    @property
    def SpuNameEn(self):
        r"""Quoted subproduct (English)
        :rtype: str
        """
        return self._SpuNameEn

    @SpuNameEn.setter
    def SpuNameEn(self, SpuNameEn):
        self._SpuNameEn = SpuNameEn

    @property
    def CategoryNameZh(self):
        r"""Quoted product (Chinese)
        :rtype: str
        """
        return self._CategoryNameZh

    @CategoryNameZh.setter
    def CategoryNameZh(self, CategoryNameZh):
        self._CategoryNameZh = CategoryNameZh

    @property
    def CategoryNameEn(self):
        r"""Quoted product (English)
        :rtype: str
        """
        return self._CategoryNameEn

    @CategoryNameEn.setter
    def CategoryNameEn(self, CategoryNameEn):
        self._CategoryNameEn = CategoryNameEn

    @property
    def BusinessCode(self):
        r"""Product code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessNameZh(self):
        r"""Product name (Chinese)
        :rtype: str
        """
        return self._BusinessNameZh

    @BusinessNameZh.setter
    def BusinessNameZh(self, BusinessNameZh):
        self._BusinessNameZh = BusinessNameZh

    @property
    def BusinessNameEn(self):
        r"""Product name (English)
        :rtype: str
        """
        return self._BusinessNameEn

    @BusinessNameEn.setter
    def BusinessNameEn(self, BusinessNameEn):
        self._BusinessNameEn = BusinessNameEn

    @property
    def ProductCode(self):
        r"""Subproduct code
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductNameZh(self):
        r"""Subproduct name (Chinese)
        :rtype: str
        """
        return self._ProductNameZh

    @ProductNameZh.setter
    def ProductNameZh(self, ProductNameZh):
        self._ProductNameZh = ProductNameZh

    @property
    def ProductNameEn(self):
        r"""Subproduct name (English)
        :rtype: str
        """
        return self._ProductNameEn

    @ProductNameEn.setter
    def ProductNameEn(self, ProductNameEn):
        self._ProductNameEn = ProductNameEn

    @property
    def ComponentCode(self):
        r"""Component type code
        :rtype: str
        """
        return self._ComponentCode

    @ComponentCode.setter
    def ComponentCode(self, ComponentCode):
        self._ComponentCode = ComponentCode

    @property
    def ComponentNameZh(self):
        r"""Component type name (Chinese)
        :rtype: str
        """
        return self._ComponentNameZh

    @ComponentNameZh.setter
    def ComponentNameZh(self, ComponentNameZh):
        self._ComponentNameZh = ComponentNameZh

    @property
    def ComponentNameEn(self):
        r"""Component type name (English)
        :rtype: str
        """
        return self._ComponentNameEn

    @ComponentNameEn.setter
    def ComponentNameEn(self, ComponentNameEn):
        self._ComponentNameEn = ComponentNameEn

    @property
    def ItemCode(self):
        r"""Component code
        :rtype: str
        """
        return self._ItemCode

    @ItemCode.setter
    def ItemCode(self, ItemCode):
        self._ItemCode = ItemCode

    @property
    def ItemNameZh(self):
        r"""Component name (Chinese)
        :rtype: str
        """
        return self._ItemNameZh

    @ItemNameZh.setter
    def ItemNameZh(self, ItemNameZh):
        self._ItemNameZh = ItemNameZh

    @property
    def ItemNameEn(self):
        r"""Component name (English)
        :rtype: str
        """
        return self._ItemNameEn

    @ItemNameEn.setter
    def ItemNameEn(self, ItemNameEn):
        self._ItemNameEn = ItemNameEn


    def _deserialize(self, params):
        self._SpuNameZh = params.get("SpuNameZh")
        self._SpuNameEn = params.get("SpuNameEn")
        self._CategoryNameZh = params.get("CategoryNameZh")
        self._CategoryNameEn = params.get("CategoryNameEn")
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessNameZh = params.get("BusinessNameZh")
        self._BusinessNameEn = params.get("BusinessNameEn")
        self._ProductCode = params.get("ProductCode")
        self._ProductNameZh = params.get("ProductNameZh")
        self._ProductNameEn = params.get("ProductNameEn")
        self._ComponentCode = params.get("ComponentCode")
        self._ComponentNameZh = params.get("ComponentNameZh")
        self._ComponentNameEn = params.get("ComponentNameEn")
        self._ItemCode = params.get("ItemCode")
        self._ItemNameZh = params.get("ItemNameZh")
        self._ItemNameEn = params.get("ItemNameEn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetRenewalRequest(AbstractModel):
    r"""SetRenewal request structure.

    """

    def __init__(self):
        r"""
        :param _ProductCode: Product code.
        :type ProductCode: str
        :param _RegionCode: Region code.
        :type RegionCode: str
        :param _InstanceId: Instance ID. Only one can be specified.
        :type InstanceId: str
        :param _RenewFlag: Renewal flag. Enumeration values are as follows:
NOTIFY_AND_MANUAL_RENEW: manual renewal.
NOTIFY_AND_AUTO_RENEW: automatic renewal.
DISABLE_NOTIFY_AND_MANUAL_RENEW: non-renewal upon expiration.
        :type RenewFlag: str
        :param _RenewPeriod: Automatic renewal cycle length. If left empty, the default value set by product is used.
If it is month, support: 1-11
If it is year, support: 1-5.
Supported range mainly depends on the product side.
        :type RenewPeriod: str
        :param _RenewPeriodUnit: Automatic renewal cycle unit. If left empty, the default value set by the product is used.
Year y, month m
Supported range mainly depends on the product side.
        :type RenewPeriodUnit: str
        """
        self._ProductCode = None
        self._RegionCode = None
        self._InstanceId = None
        self._RenewFlag = None
        self._RenewPeriod = None
        self._RenewPeriodUnit = None

    @property
    def ProductCode(self):
        r"""Product code.
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def RegionCode(self):
        r"""Region code.
        :rtype: str
        """
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode

    @property
    def InstanceId(self):
        r"""Instance ID. Only one can be specified.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RenewFlag(self):
        r"""Renewal flag. Enumeration values are as follows:
NOTIFY_AND_MANUAL_RENEW: manual renewal.
NOTIFY_AND_AUTO_RENEW: automatic renewal.
DISABLE_NOTIFY_AND_MANUAL_RENEW: non-renewal upon expiration.
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def RenewPeriod(self):
        r"""Automatic renewal cycle length. If left empty, the default value set by product is used.
If it is month, support: 1-11
If it is year, support: 1-5.
Supported range mainly depends on the product side.
        :rtype: str
        """
        return self._RenewPeriod

    @RenewPeriod.setter
    def RenewPeriod(self, RenewPeriod):
        self._RenewPeriod = RenewPeriod

    @property
    def RenewPeriodUnit(self):
        r"""Automatic renewal cycle unit. If left empty, the default value set by the product is used.
Year y, month m
Supported range mainly depends on the product side.
        :rtype: str
        """
        return self._RenewPeriodUnit

    @RenewPeriodUnit.setter
    def RenewPeriodUnit(self, RenewPeriodUnit):
        self._RenewPeriodUnit = RenewPeriodUnit


    def _deserialize(self, params):
        self._ProductCode = params.get("ProductCode")
        self._RegionCode = params.get("RegionCode")
        self._InstanceId = params.get("InstanceId")
        self._RenewFlag = params.get("RenewFlag")
        self._RenewPeriod = params.get("RenewPeriod")
        self._RenewPeriodUnit = params.get("RenewPeriodUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetRenewalResponse(AbstractModel):
    r"""SetRenewal response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceList: Instance list when the operation fails.
        :type InstanceList: list of OperateRsp
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceList = None
        self._RequestId = None

    @property
    def InstanceList(self):
        r"""Instance list when the operation fails.
        :rtype: list of OperateRsp
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

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
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = OperateRsp()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._RequestId = params.get("RequestId")


class SummaryDetail(AbstractModel):
    r"""Detailed summary of costs by multiple dimensions

    """

    def __init__(self):
        r"""
        :param _GroupKey: Bill dimension code
        :type GroupKey: str
        :param _GroupValue: Billing dimension value
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
        :param _TransferPayAmount: Royalty account expenditure: The amount paid through the royalty account
        :type TransferPayAmount: str
        :param _Business: Product summary information
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
        r"""Bill dimension code
        :rtype: str
        """
        return self._GroupKey

    @GroupKey.setter
    def GroupKey(self, GroupKey):
        self._GroupKey = GroupKey

    @property
    def GroupValue(self):
        r"""Billing dimension value
        :rtype: str
        """
        return self._GroupValue

    @GroupValue.setter
    def GroupValue(self, GroupValue):
        self._GroupValue = GroupValue

    @property
    def TotalCost(self):
        r"""Original cost in USD. This parameter has become valid since Bill 3.0 took effect in May 2021, and before that `-` was returned for this parameter. If a customer has applied for a contract price different from the prices listed on the official website, `-` will also be returned for this parameter.
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RealTotalCost(self):
        r"""Total amount after discount
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        r"""Cash credit: The amount paid from the user’s cash account
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Free credit: The amount paid with the user’s free credit
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        r"""Voucher payment: The voucher deduction amount
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        r"""Royalty account expenditure: The amount paid through the royalty account
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def Business(self):
        r"""Product summary information
        :rtype: list of BusinessSummaryInfo
        """
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
    r"""Total cost

    """

    def __init__(self):
        r"""
        :param _RealTotalCost: discounted total price
        :type RealTotalCost: str
        :param _TotalCost: Original price in CNY. The TotalCost field comes into effect after bill 3.0 (May 2021) and returns "-" before bill 3.0. In the current situation of contract price, the TotalCost field returns "-" if a price difference exists with the official website price.
        :type TotalCost: str
        """
        self._RealTotalCost = None
        self._TotalCost = None

    @property
    def RealTotalCost(self):
        r"""discounted total price
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def TotalCost(self):
        r"""Original price in CNY. The TotalCost field comes into effect after bill 3.0 (May 2021) and returns "-" before bill 3.0. In the current situation of contract price, the TotalCost field returns "-" if a price difference exists with the official website price.
        :rtype: str
        """
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
    r"""Tag information.

    """

    def __init__(self):
        r"""
        :param _TagKey: Cost allocation tag key.
        :type TagKey: str
        :param _Status: Tag type. Valid values: `0` (general tags), `1` (cost allocation tags).
        :type Status: int
        :param _UpdateTime: Set the allocation tag time. Ordinary tags do not return.
        :type UpdateTime: str
        """
        self._TagKey = None
        self._Status = None
        self._UpdateTime = None

    @property
    def TagKey(self):
        r"""Cost allocation tag key.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def Status(self):
        r"""Tag type. Valid values: `0` (general tags), `1` (cost allocation tags).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpdateTime(self):
        r"""Set the allocation tag time. Ordinary tags do not return.
        :rtype: str
        """
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
    r"""Details about cost distribution over different tags.

    """

    def __init__(self):
        r"""
        :param _TagValue: Tag value
        :type TagValue: str
        :param _RealTotalCostRatio: Percentage of the fee, with 2 decimal places.
        :type RealTotalCostRatio: str
        :param _RealTotalCost: discounted total price
        :type RealTotalCost: str
        :param _CashPayAmount: Cash account expenditure: The amount paid through the cash account
        :type CashPayAmount: str
        :param _IncentivePayAmount: Gift account expenditure: The amount paid using free credits
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: Coupon expenditure: The amount paid using various vouchers (such as vouchers and cash vouchers)
        :type VoucherPayAmount: str
        :param _TransferPayAmount: Royalty account expenditure: The amount paid through the royalty account
        :type TransferPayAmount: str
        :param _TotalCost: Original price in CNY. The TotalCost field comes into effect after bill 3.0 (May 2021) and returns "-" before bill 3.0. In the current situation of contract price, the TotalCost field returns "-" if a price difference exists with the official website price.
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
        r"""Tag value
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def RealTotalCostRatio(self):
        r"""Percentage of the fee, with 2 decimal places.
        :rtype: str
        """
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        r"""discounted total price
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        r"""Cash account expenditure: The amount paid through the cash account
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        r"""Gift account expenditure: The amount paid using free credits
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        r"""Coupon expenditure: The amount paid using various vouchers (such as vouchers and cash vouchers)
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        r"""Royalty account expenditure: The amount paid through the royalty account
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def TotalCost(self):
        r"""Original price in CNY. The TotalCost field comes into effect after bill 3.0 (May 2021) and returns "-" before bill 3.0. In the current situation of contract price, the TotalCost field returns "-" if a price difference exists with the official website price.
        :rtype: str
        """
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
        


class UinTempAmountModel(AbstractModel):
    r"""Temporary limit details

    """

    def __init__(self):
        r"""
        :param _Uin: User UIN
        :type Uin: str
        :param _TempAmount: temporary limit
        :type TempAmount: float
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EndTime: End time.
        :type EndTime: str
        """
        self._Uin = None
        self._TempAmount = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Uin(self):
        r"""User UIN
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def TempAmount(self):
        r"""temporary limit
        :rtype: float
        """
        return self._TempAmount

    @TempAmount.setter
    def TempAmount(self, TempAmount):
        self._TempAmount = TempAmount

    @property
    def StartTime(self):
        r"""Start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._TempAmount = params.get("TempAmount")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageDetails(AbstractModel):
    r"""The product purchased.

    """

    def __init__(self):
        r"""
        :param _ProductName: Product name
        :type ProductName: str
        :param _SubProductName: product details
        :type SubProductName: str
        :param _ProductCode: Product code	
        :type ProductCode: str
        :param _SubProductCode: Sub-product code	
        :type SubProductCode: str
        :param _BillingItemCode: Billing item code.	
        :type BillingItemCode: str
        :param _SubBillingItemCode: Billing sub-item code.	
        :type SubBillingItemCode: str
        :param _ProductEnName: Product English Name	
        :type ProductEnName: str
        :param _SubProductEnName: English name of the sub-product.	
        :type SubProductEnName: str
        :param _CalcUnit: billing cycle	
        :type CalcUnit: str
        :param _Action: payMode is prepay and payScene is common in the current situation
        :type Action: str
        """
        self._ProductName = None
        self._SubProductName = None
        self._ProductCode = None
        self._SubProductCode = None
        self._BillingItemCode = None
        self._SubBillingItemCode = None
        self._ProductEnName = None
        self._SubProductEnName = None
        self._CalcUnit = None
        self._Action = None

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
        r"""product details
        :rtype: str
        """
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName

    @property
    def ProductCode(self):
        r"""Product code	
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def SubProductCode(self):
        r"""Sub-product code	
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def BillingItemCode(self):
        r"""Billing item code.	
        :rtype: str
        """
        return self._BillingItemCode

    @BillingItemCode.setter
    def BillingItemCode(self, BillingItemCode):
        self._BillingItemCode = BillingItemCode

    @property
    def SubBillingItemCode(self):
        r"""Billing sub-item code.	
        :rtype: str
        """
        return self._SubBillingItemCode

    @SubBillingItemCode.setter
    def SubBillingItemCode(self, SubBillingItemCode):
        self._SubBillingItemCode = SubBillingItemCode

    @property
    def ProductEnName(self):
        r"""Product English Name	
        :rtype: str
        """
        return self._ProductEnName

    @ProductEnName.setter
    def ProductEnName(self, ProductEnName):
        self._ProductEnName = ProductEnName

    @property
    def SubProductEnName(self):
        r"""English name of the sub-product.	
        :rtype: str
        """
        return self._SubProductEnName

    @SubProductEnName.setter
    def SubProductEnName(self, SubProductEnName):
        self._SubProductEnName = SubProductEnName

    @property
    def CalcUnit(self):
        r"""billing cycle	
        :rtype: str
        """
        return self._CalcUnit

    @CalcUnit.setter
    def CalcUnit(self, CalcUnit):
        self._CalcUnit = CalcUnit

    @property
    def Action(self):
        r"""payMode is prepay and payScene is common in the current situation
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._SubProductName = params.get("SubProductName")
        self._ProductCode = params.get("ProductCode")
        self._SubProductCode = params.get("SubProductCode")
        self._BillingItemCode = params.get("BillingItemCode")
        self._SubBillingItemCode = params.get("SubBillingItemCode")
        self._ProductEnName = params.get("ProductEnName")
        self._SubProductEnName = params.get("SubProductEnName")
        self._CalcUnit = params.get("CalcUnit")
        self._Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageRecords(AbstractModel):
    r"""The usage records.

    """

    def __init__(self):
        r"""
        :param _UsedAmount: The amount used. The value of this parameter is the amount used (USD, rounded to 8 decimal places) multiplied by 100,000,000.
        :type UsedAmount: int
        :param _UsedTime: The time when the voucher was used.
        :type UsedTime: str
        :param _UsageDetails: Usage record details
        :type UsageDetails: list of UsageDetails
        :param _PayMode: Payment mode
        :type PayMode: str
        :param _VoucherId: Queried coupon id
        :type VoucherId: str
        :param _PayScene: Transaction scene: (adjust: adjust accounts, common: normal transaction scene)
        :type PayScene: str
        :param _SeqId: Unique ID, corresponding to transaction: prepaid dealName, bill adjustment/postpaid outTradeNo
        :type SeqId: str
        """
        self._UsedAmount = None
        self._UsedTime = None
        self._UsageDetails = None
        self._PayMode = None
        self._VoucherId = None
        self._PayScene = None
        self._SeqId = None

    @property
    def UsedAmount(self):
        r"""The amount used. The value of this parameter is the amount used (USD, rounded to 8 decimal places) multiplied by 100,000,000.
        :rtype: int
        """
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

    @property
    def UsedTime(self):
        r"""The time when the voucher was used.
        :rtype: str
        """
        return self._UsedTime

    @UsedTime.setter
    def UsedTime(self, UsedTime):
        self._UsedTime = UsedTime

    @property
    def UsageDetails(self):
        r"""Usage record details
        :rtype: list of UsageDetails
        """
        return self._UsageDetails

    @UsageDetails.setter
    def UsageDetails(self, UsageDetails):
        self._UsageDetails = UsageDetails

    @property
    def PayMode(self):
        r"""Payment mode
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def VoucherId(self):
        r"""Queried coupon id
        :rtype: str
        """
        return self._VoucherId

    @VoucherId.setter
    def VoucherId(self, VoucherId):
        self._VoucherId = VoucherId

    @property
    def PayScene(self):
        r"""Transaction scene: (adjust: adjust accounts, common: normal transaction scene)
        :rtype: str
        """
        return self._PayScene

    @PayScene.setter
    def PayScene(self, PayScene):
        self._PayScene = PayScene

    @property
    def SeqId(self):
        r"""Unique ID, corresponding to transaction: prepaid dealName, bill adjustment/postpaid outTradeNo
        :rtype: str
        """
        return self._SeqId

    @SeqId.setter
    def SeqId(self, SeqId):
        self._SeqId = SeqId


    def _deserialize(self, params):
        self._UsedAmount = params.get("UsedAmount")
        self._UsedTime = params.get("UsedTime")
        if params.get("UsageDetails") is not None:
            self._UsageDetails = []
            for item in params.get("UsageDetails"):
                obj = UsageDetails()
                obj._deserialize(item)
                self._UsageDetails.append(obj)
        self._PayMode = params.get("PayMode")
        self._VoucherId = params.get("VoucherId")
        self._PayScene = params.get("PayScene")
        self._SeqId = params.get("SeqId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoucherInfos(AbstractModel):
    r"""Voucher information.

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
        :param _ApplicableProducts: Product information applies to
        :type ApplicableProducts: :class:`tencentcloud.billing.v20180709.models.ApplicableProducts`
        :param _ExcludedProducts: Product information not applicable
        :type ExcludedProducts: list of ExcludedProducts
        :param _PolicyRemark: Instructions/Batch Remarks
        :type PolicyRemark: str
        :param _CreateTime: Coupon issuance time
        :type CreateTime: str
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
        self._PolicyRemark = None
        self._CreateTime = None

    @property
    def OwnerUin(self):
        r"""The owner of the voucher.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Status(self):
        r"""The status of the voucher: `unUsed`, `used`, `delivered`, `cancel`, `overdue`
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NominalValue(self):
        r"""The value of the voucher. The value of this parameter is the voucher value (USD, rounded to 8 decimal places) multiplied by 100,000,000.
        :rtype: int
        """
        return self._NominalValue

    @NominalValue.setter
    def NominalValue(self, NominalValue):
        self._NominalValue = NominalValue

    @property
    def Balance(self):
        r"""The balance left. The value of this parameter is the balance left (USD, rounded to 8 decimal places) multiplied by 100,000,000.
        :rtype: int
        """
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def VoucherId(self):
        r"""The voucher ID.
        :rtype: str
        """
        return self._VoucherId

    @VoucherId.setter
    def VoucherId(self, VoucherId):
        self._VoucherId = VoucherId

    @property
    def PayMode(self):
        r"""`postPay`: pay-as-you-go; `prePay`: prepaid; `riPay`: reserved instance; empty or `*`: all.
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayScene(self):
        r"""If `PayMode` is `postPay`, this parameter may be `spotpay` (spot instance) or `settle account` (regular pay-as-you-go). If `PayMode` is `prePay`, this parameter may be `purchase`, `renew`, or `modify` (downgrade/upgrade). If `PayMode` is `riPay`, this parameter may be `oneOffFee` (prepayment of reserved instance) or `hourlyFee` (hourly billing of reserved instance). `*` means to query vouchers that support all billing scenarios.
        :rtype: str
        """
        return self._PayScene

    @PayScene.setter
    def PayScene(self, PayScene):
        self._PayScene = PayScene

    @property
    def BeginTime(self):
        r"""The start time of the validity period.
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""The end time of the validity period.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ApplicableProducts(self):
        r"""Product information applies to
        :rtype: :class:`tencentcloud.billing.v20180709.models.ApplicableProducts`
        """
        return self._ApplicableProducts

    @ApplicableProducts.setter
    def ApplicableProducts(self, ApplicableProducts):
        self._ApplicableProducts = ApplicableProducts

    @property
    def ExcludedProducts(self):
        r"""Product information not applicable
        :rtype: list of ExcludedProducts
        """
        return self._ExcludedProducts

    @ExcludedProducts.setter
    def ExcludedProducts(self, ExcludedProducts):
        self._ExcludedProducts = ExcludedProducts

    @property
    def PolicyRemark(self):
        r"""Instructions/Batch Remarks
        :rtype: str
        """
        return self._PolicyRemark

    @PolicyRemark.setter
    def PolicyRemark(self, PolicyRemark):
        self._PolicyRemark = PolicyRemark

    @property
    def CreateTime(self):
        r"""Coupon issuance time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


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
        self._PolicyRemark = params.get("PolicyRemark")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        