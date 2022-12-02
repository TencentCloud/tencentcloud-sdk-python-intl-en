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
        :param ActionType: Transaction type
        :type ActionType: str
        :param ActionTypeName: Transaction type name
        :type ActionTypeName: str
        :param RealTotalCost: Actual cost
        :type RealTotalCost: str
        :param RealTotalCostRatio: Cost ratio, to two decimal points
        :type RealTotalCostRatio: str
        :param CashPayAmount: Cash amount
        :type CashPayAmount: str
        :param IncentivePayAmount: Trial credit amount
        :type IncentivePayAmount: str
        :param VoucherPayAmount: Voucher amount
        :type VoucherPayAmount: str
        :param BillMonth: Billing month, e.g. `2019-08`
        :type BillMonth: str
        :param TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        """
        self.ActionType = None
        self.ActionTypeName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.BillMonth = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.ActionType = params.get("ActionType")
        self.ActionTypeName = params.get("ActionTypeName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.BillMonth = params.get("BillMonth")
        self.TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicableProducts(AbstractModel):
    """The products that are applicable.

    """

    def __init__(self):
        r"""
        :param GoodsName: Valid values: `all products` or names of the applicable products (string). Multiple names are separated by commas.
        :type GoodsName: str
        :param PayMode: Valid values: `postPay`: pay-as-you-go; `prePay`: prepaid; `riPay`: reserved instance; empty or `*`: all. If `GoodsName` contains multiple product names and `PayMode` is `*`, it indicates that the voucher can be used in all billing modes for each of the products.
        :type PayMode: str
        """
        self.GoodsName = None
        self.PayMode = None


    def _deserialize(self, params):
        self.GoodsName = params.get("GoodsName")
        self.PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDetail(AbstractModel):
    """Bill details

    """

    def __init__(self):
        r"""
        :param BusinessCodeName: Product name: major categories of Tencent Cloud services, e.g. CVM and TencentDB for MySQL
        :type BusinessCodeName: str
        :param ProductCodeName: Sub-product name: sub-categories of Tencent Cloud services, such as CVM-Standard S1
        :type ProductCodeName: str
        :param PayModeName: Billing mode
        :type PayModeName: str
        :param ProjectName: Project: project of a resource
        :type ProjectName: str
        :param RegionName: Region: region of a resource, e.g. South China (Guangzhou)
        :type RegionName: str
        :param ZoneName: Availability zone: availability zone of a resource, e.g. Guangzhou Zone 3
        :type ZoneName: str
        :param ResourceId: Instance ID
        :type ResourceId: str
        :param ResourceName: Instance name
        :type ResourceName: str
        :param ActionTypeName: Transaction type
        :type ActionTypeName: str
        :param OrderId: Order ID
        :type OrderId: str
        :param BillId: Transaction ID
        :type BillId: str
        :param PayTime: Payment time
        :type PayTime: str
        :param FeeBeginTime: Service start time
        :type FeeBeginTime: str
        :param FeeEndTime: Service end time
        :type FeeEndTime: str
        :param ComponentSet: Component list
        :type ComponentSet: list of BillDetailComponent
        :param PayerUin: Payer's UIN
        :type PayerUin: str
        :param OwnerUin: User's UIN
        :type OwnerUin: str
        :param OperateUin: Operator's UIN
        :type OperateUin: str
        :param Tags: Tag information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of BillTagInfo
        :param BusinessCode: Product code
Note: This field may return `null`, indicating that no valid value can be found.
        :type BusinessCode: str
        :param ProductCode: Subproduct code
Note: This field may return `null`, indicating that no valid value can be found.
        :type ProductCode: str
        :param ActionType: Transaction type
Note: This field may return `null`, indicating that no valid value can be found.
        :type ActionType: str
        :param RegionId: 
        :type RegionId: str
        :param ProjectId: Project ID: ID of the project to which the resource belongs
        :type ProjectId: int
        """
        self.BusinessCodeName = None
        self.ProductCodeName = None
        self.PayModeName = None
        self.ProjectName = None
        self.RegionName = None
        self.ZoneName = None
        self.ResourceId = None
        self.ResourceName = None
        self.ActionTypeName = None
        self.OrderId = None
        self.BillId = None
        self.PayTime = None
        self.FeeBeginTime = None
        self.FeeEndTime = None
        self.ComponentSet = None
        self.PayerUin = None
        self.OwnerUin = None
        self.OperateUin = None
        self.Tags = None
        self.BusinessCode = None
        self.ProductCode = None
        self.ActionType = None
        self.RegionId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.ProductCodeName = params.get("ProductCodeName")
        self.PayModeName = params.get("PayModeName")
        self.ProjectName = params.get("ProjectName")
        self.RegionName = params.get("RegionName")
        self.ZoneName = params.get("ZoneName")
        self.ResourceId = params.get("ResourceId")
        self.ResourceName = params.get("ResourceName")
        self.ActionTypeName = params.get("ActionTypeName")
        self.OrderId = params.get("OrderId")
        self.BillId = params.get("BillId")
        self.PayTime = params.get("PayTime")
        self.FeeBeginTime = params.get("FeeBeginTime")
        self.FeeEndTime = params.get("FeeEndTime")
        if params.get("ComponentSet") is not None:
            self.ComponentSet = []
            for item in params.get("ComponentSet"):
                obj = BillDetailComponent()
                obj._deserialize(item)
                self.ComponentSet.append(obj)
        self.PayerUin = params.get("PayerUin")
        self.OwnerUin = params.get("OwnerUin")
        self.OperateUin = params.get("OperateUin")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = BillTagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.BusinessCode = params.get("BusinessCode")
        self.ProductCode = params.get("ProductCode")
        self.ActionType = params.get("ActionType")
        self.RegionId = params.get("RegionId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDetailComponent(AbstractModel):
    """Information about components charged in the bill

    """

    def __init__(self):
        r"""
        :param ComponentCodeName: Component type: type of a resource component, e.g. memory, disk, etc.
        :type ComponentCodeName: str
        :param ItemCodeName: Component name: name of a resource component, e.g. TencentDB for MySQL-memory
        :type ItemCodeName: str
        :param SinglePrice: Component published price: original price of a resource component with the original granularity
        :type SinglePrice: str
        :param SpecifiedPrice: Specified price of the component
        :type SpecifiedPrice: str
        :param PriceUnit: Price unit
        :type PriceUnit: str
        :param UsedAmount: Component usage
        :type UsedAmount: str
        :param UsedAmountUnit: Component usage unit
        :type UsedAmountUnit: str
        :param TimeSpan: Usage period
        :type TimeSpan: str
        :param TimeUnitName: Time unit
        :type TimeUnitName: str
        :param Cost: Original price of the component
        :type Cost: str
        :param Discount: Discount rate
        :type Discount: str
        :param ReduceType: Offer type
        :type ReduceType: str
        :param RealCost: Total discounted price
        :type RealCost: str
        :param VoucherPayAmount: Amount paid in voucher
        :type VoucherPayAmount: str
        :param CashPayAmount: Amount paid in cash
        :type CashPayAmount: str
        :param IncentivePayAmount: Amount paid in trial credit
        :type IncentivePayAmount: str
        :param ItemCode: Component type code
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ItemCode: str
        :param ComponentCode: Component code
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ComponentCode: str
        :param ContractPrice: Contract price
        :type ContractPrice: str
        :param InstanceType: The special instance (resource pack, reserved instance, savings plan, or spot instance) that is applied to deduction. Valid values:
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type InstanceType: str
        :param RiTimeSpan: The usage duration deducted by a reserved instance. The unit of measurement for deduction is the same as that for usage duration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RiTimeSpan: str
        :param OriginalCostWithRI: The amount deducted by a reserved instance based on the original component cost.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginalCostWithRI: str
        :param SPDeductionRate: The discount multiplier that applies to the component based on the remaining commitment of the savings plan.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SPDeductionRate: str
        :param SPDeduction: The savings plan deduction amount.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SPDeduction: str
        :param OriginalCostWithSP: The amount deducted by a savings plan based on the original component cost.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginalCostWithSP: str
        :param BlendedDiscount: The blended discount multiplier that combines the official website discount, reserved instance discount, and savings plan discount. If no reserved instance and savings plan discounts are available, the blended discount multiplier equals the discount multiplier.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type BlendedDiscount: str
        """
        self.ComponentCodeName = None
        self.ItemCodeName = None
        self.SinglePrice = None
        self.SpecifiedPrice = None
        self.PriceUnit = None
        self.UsedAmount = None
        self.UsedAmountUnit = None
        self.TimeSpan = None
        self.TimeUnitName = None
        self.Cost = None
        self.Discount = None
        self.ReduceType = None
        self.RealCost = None
        self.VoucherPayAmount = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.ItemCode = None
        self.ComponentCode = None
        self.ContractPrice = None
        self.InstanceType = None
        self.RiTimeSpan = None
        self.OriginalCostWithRI = None
        self.SPDeductionRate = None
        self.SPDeduction = None
        self.OriginalCostWithSP = None
        self.BlendedDiscount = None


    def _deserialize(self, params):
        self.ComponentCodeName = params.get("ComponentCodeName")
        self.ItemCodeName = params.get("ItemCodeName")
        self.SinglePrice = params.get("SinglePrice")
        self.SpecifiedPrice = params.get("SpecifiedPrice")
        self.PriceUnit = params.get("PriceUnit")
        self.UsedAmount = params.get("UsedAmount")
        self.UsedAmountUnit = params.get("UsedAmountUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnitName = params.get("TimeUnitName")
        self.Cost = params.get("Cost")
        self.Discount = params.get("Discount")
        self.ReduceType = params.get("ReduceType")
        self.RealCost = params.get("RealCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.ItemCode = params.get("ItemCode")
        self.ComponentCode = params.get("ComponentCode")
        self.ContractPrice = params.get("ContractPrice")
        self.InstanceType = params.get("InstanceType")
        self.RiTimeSpan = params.get("RiTimeSpan")
        self.OriginalCostWithRI = params.get("OriginalCostWithRI")
        self.SPDeductionRate = params.get("SPDeductionRate")
        self.SPDeduction = params.get("SPDeduction")
        self.OriginalCostWithSP = params.get("OriginalCostWithSP")
        self.BlendedDiscount = params.get("BlendedDiscount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillResourceSummary(AbstractModel):
    """Information about resources charged in the bill

    """

    def __init__(self):
        r"""
        :param BusinessCodeName: Product name: major categories of Tencent Cloud services, e.g. CVM and TencentDB for MySQL
        :type BusinessCodeName: str
        :param ProductCodeName: Subproduct name, which is the subcategory of a Tencent Cloud product, such as CVM-Standard S1. If no subproduct name can be obtained, `-` is returned.
        :type ProductCodeName: str
        :param PayModeName: Billing mode
        :type PayModeName: str
        :param ProjectName: Project
        :type ProjectName: str
        :param RegionName: Region
        :type RegionName: str
        :param ZoneName: Availability zone
        :type ZoneName: str
        :param ResourceId: Instance ID
        :type ResourceId: str
        :param ResourceName: Resource instance namDeduction timee
        :type ResourceName: str
        :param ActionTypeName: Transaction type
        :type ActionTypeName: str
        :param OrderId: Order ID
        :type OrderId: str
        :param PayTime: Payment time
        :type PayTime: str
        :param FeeBeginTime: Service start time
        :type FeeBeginTime: str
        :param FeeEndTime: Service end time
        :type FeeEndTime: str
        :param ConfigDesc: Configuration description
        :type ConfigDesc: str
        :param ExtendField1: Extension field 1
        :type ExtendField1: str
        :param ExtendField2: Extension field 2
        :type ExtendField2: str
        :param TotalCost: Cost, in USD
        :type TotalCost: str
        :param Discount: Discount
If different discounts or contract prices are applied, `-` will be returned for this parameter.
        :type Discount: str
        :param ReduceType: Offer type
        :type ReduceType: str
        :param RealTotalCost: Total cost after discount, in USD
        :type RealTotalCost: str
        :param VoucherPayAmount: Amount paid in voucher, in USD
        :type VoucherPayAmount: str
        :param CashPayAmount: Amount paid in cash, in USD
        :type CashPayAmount: str
        :param IncentivePayAmount: Amount paid in trial credit, in USD
        :type IncentivePayAmount: str
        :param ExtendField3: Extension field 3
        :type ExtendField3: str
        :param ExtendField4: Extension field 4
        :type ExtendField4: str
        :param ExtendField5: Extension field 5
        :type ExtendField5: str
        :param Tags: Tag information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of BillTagInfo
        :param PayerUin: Payer UIN
        :type PayerUin: str
        :param OwnerUin: Resource owner UIN; '-' is returned if no value is obtained
        :type OwnerUin: str
        :param OperateUin: Operator UIN; '-' is returned if no value is obtained
        :type OperateUin: str
        :param BusinessCode: Product code
        :type BusinessCode: str
        :param ProductCode: Subproduct code
        :type ProductCode: str
        :param RegionId: 
        :type RegionId: int
        :param InstanceType: The special instance (resource pack, reserved instance, savings plan, or spot instance) that is applied to deduction. Valid values:

ri=Standard RI

svp=Savings Plan

si=Spot Instances

rp=Resource Pack
        :type InstanceType: str
        :param OriginalCostWithRI: The amount deducted by a reserved instance based on the original component cost.
        :type OriginalCostWithRI: str
        :param SPDeduction: The savings plan deduction amount.
        :type SPDeduction: str
        :param OriginalCostWithSP: The amount deducted by a savings plan based on the original component cost.
        :type OriginalCostWithSP: str
        """
        self.BusinessCodeName = None
        self.ProductCodeName = None
        self.PayModeName = None
        self.ProjectName = None
        self.RegionName = None
        self.ZoneName = None
        self.ResourceId = None
        self.ResourceName = None
        self.ActionTypeName = None
        self.OrderId = None
        self.PayTime = None
        self.FeeBeginTime = None
        self.FeeEndTime = None
        self.ConfigDesc = None
        self.ExtendField1 = None
        self.ExtendField2 = None
        self.TotalCost = None
        self.Discount = None
        self.ReduceType = None
        self.RealTotalCost = None
        self.VoucherPayAmount = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.ExtendField3 = None
        self.ExtendField4 = None
        self.ExtendField5 = None
        self.Tags = None
        self.PayerUin = None
        self.OwnerUin = None
        self.OperateUin = None
        self.BusinessCode = None
        self.ProductCode = None
        self.RegionId = None
        self.InstanceType = None
        self.OriginalCostWithRI = None
        self.SPDeduction = None
        self.OriginalCostWithSP = None


    def _deserialize(self, params):
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.ProductCodeName = params.get("ProductCodeName")
        self.PayModeName = params.get("PayModeName")
        self.ProjectName = params.get("ProjectName")
        self.RegionName = params.get("RegionName")
        self.ZoneName = params.get("ZoneName")
        self.ResourceId = params.get("ResourceId")
        self.ResourceName = params.get("ResourceName")
        self.ActionTypeName = params.get("ActionTypeName")
        self.OrderId = params.get("OrderId")
        self.PayTime = params.get("PayTime")
        self.FeeBeginTime = params.get("FeeBeginTime")
        self.FeeEndTime = params.get("FeeEndTime")
        self.ConfigDesc = params.get("ConfigDesc")
        self.ExtendField1 = params.get("ExtendField1")
        self.ExtendField2 = params.get("ExtendField2")
        self.TotalCost = params.get("TotalCost")
        self.Discount = params.get("Discount")
        self.ReduceType = params.get("ReduceType")
        self.RealTotalCost = params.get("RealTotalCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.ExtendField3 = params.get("ExtendField3")
        self.ExtendField4 = params.get("ExtendField4")
        self.ExtendField5 = params.get("ExtendField5")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = BillTagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.PayerUin = params.get("PayerUin")
        self.OwnerUin = params.get("OwnerUin")
        self.OperateUin = params.get("OperateUin")
        self.BusinessCode = params.get("BusinessCode")
        self.ProductCode = params.get("ProductCode")
        self.RegionId = params.get("RegionId")
        self.InstanceType = params.get("InstanceType")
        self.OriginalCostWithRI = params.get("OriginalCostWithRI")
        self.SPDeduction = params.get("SPDeduction")
        self.OriginalCostWithSP = params.get("OriginalCostWithSP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillTagInfo(AbstractModel):
    """Bill tag information.

    """

    def __init__(self):
        r"""
        :param TagKey: Cost allocation tag key
        :type TagKey: str
        :param TagValue: Tag value
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusinessSummaryOverviewItem(AbstractModel):
    """Summarize product details by product

    """

    def __init__(self):
        r"""
        :param BusinessCode: Product code
Note: This field may return `null`, indicating that no valid value can be found.
        :type BusinessCode: str
        :param BusinessCodeName: Product name: major categories of Tencent Cloud services, e.g. CVM and TencentDB for MySQL
        :type BusinessCodeName: str
        :param RealTotalCost: Actual cost
        :type RealTotalCost: str
        :param RealTotalCostRatio: Cost ratio, to two decimal points
        :type RealTotalCostRatio: str
        :param CashPayAmount: Cash amount
        :type CashPayAmount: str
        :param IncentivePayAmount: Trial credit amount
        :type IncentivePayAmount: str
        :param VoucherPayAmount: Voucher amount
        :type VoucherPayAmount: str
        :param BillMonth: Billing month, e.g. `2019-08`
        :type BillMonth: str
        :param TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        :param TransferPayAmount: Payment by commission credits
        :type TransferPayAmount: str
        """
        self.BusinessCode = None
        self.BusinessCodeName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.BillMonth = None
        self.TotalCost = None
        self.TransferPayAmount = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.BillMonth = params.get("BillMonth")
        self.TotalCost = params.get("TotalCost")
        self.TransferPayAmount = params.get("TransferPayAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusinessSummaryTotal(AbstractModel):
    """Summarize total cost by product

    """

    def __init__(self):
        r"""
        :param RealTotalCost: Total cost
        :type RealTotalCost: str
        :param VoucherPayAmount: Voucher amount
        :type VoucherPayAmount: str
        :param IncentivePayAmount: Trial credit amount
        :type IncentivePayAmount: str
        :param CashPayAmount: Cash amount
        :type CashPayAmount: str
        :param TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        :param TransferPayAmount: Payment by commission credits
        :type TransferPayAmount: str
        """
        self.RealTotalCost = None
        self.VoucherPayAmount = None
        self.IncentivePayAmount = None
        self.CashPayAmount = None
        self.TotalCost = None
        self.TransferPayAmount = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.CashPayAmount = params.get("CashPayAmount")
        self.TotalCost = params.get("TotalCost")
        self.TransferPayAmount = params.get("TransferPayAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosDetailSets(AbstractModel):
    """Information about the data structure of the returned COS usage details

    """

    def __init__(self):
        r"""
        :param BucketName: Bucket name
        :type BucketName: str
        :param DosageBeginTime: The start time of the usage
        :type DosageBeginTime: str
        :param DosageEndTime: The end time of the usage
        :type DosageEndTime: str
        :param SubProductCodeName: Sub-product name
        :type SubProductCodeName: str
        :param BillingItemCodeName: Billable item name
        :type BillingItemCodeName: str
        :param DosageValue: Usage
        :type DosageValue: str
        :param Unit: Unit of the billable item
        :type Unit: str
        """
        self.BucketName = None
        self.DosageBeginTime = None
        self.DosageEndTime = None
        self.SubProductCodeName = None
        self.BillingItemCodeName = None
        self.DosageValue = None
        self.Unit = None


    def _deserialize(self, params):
        self.BucketName = params.get("BucketName")
        self.DosageBeginTime = params.get("DosageBeginTime")
        self.DosageEndTime = params.get("DosageEndTime")
        self.SubProductCodeName = params.get("SubProductCodeName")
        self.BillingItemCodeName = params.get("BillingItemCodeName")
        self.DosageValue = params.get("DosageValue")
        self.Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountBalanceRequest(AbstractModel):
    """DescribeAccountBalance request structure.

    """


class DescribeAccountBalanceResponse(AbstractModel):
    """DescribeAccountBalance response structure.

    """

    def __init__(self):
        r"""
        :param Balance: Available account balance in cents, which takes the same calculation rules as `RealBalance`, `CreditBalance`, and `RealCreditBalance`.
        :type Balance: int
        :param Uin: The UIN to query.
        :type Uin: int
        :param RealBalance: Available account balance in cents, which takes the same calculation rules as `Balance`, `CreditBalance`, and `RealCreditBalance`.
        :type RealBalance: float
        :param CashAccountBalance: Cash account balance in cents. Currently, this field is not applied.
        :type CashAccountBalance: float
        :param IncomeIntoAccountBalance: Income account balance in cents. Currently, this field is not applied.
        :type IncomeIntoAccountBalance: float
        :param PresentAccountBalance: Present account balance in cents. Currently, this field is not applied.
        :type PresentAccountBalance: float
        :param FreezeAmount: Frozen amount in cents.
        :type FreezeAmount: float
        :param OweAmount: Overdue amount in cents, which is when the available credit balance is negative.
        :type OweAmount: float
        :param IsAllowArrears: Whether overdue payments are allowed. Currently, this field is not applied.
        :type IsAllowArrears: bool
        :param IsCreditLimited: Whether you have a credit limit. Currently, this field is not applied.
        :type IsCreditLimited: bool
        :param CreditAmount: Credit limit. Credit limit－available credit balance = consumption amount
        :type CreditAmount: float
        :param CreditBalance: Available credit balance in cents, which takes the same calculation rules as `Balance`, `RealBalance`, and `RealCreditBalance`.
        :type CreditBalance: float
        :param RealCreditBalance: Available account balance in cents, which takes the same calculation rules as `Balance`, `RealBalance`, and `CreditBalance`.
        :type RealCreditBalance: float
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Balance = None
        self.Uin = None
        self.RealBalance = None
        self.CashAccountBalance = None
        self.IncomeIntoAccountBalance = None
        self.PresentAccountBalance = None
        self.FreezeAmount = None
        self.OweAmount = None
        self.IsAllowArrears = None
        self.IsCreditLimited = None
        self.CreditAmount = None
        self.CreditBalance = None
        self.RealCreditBalance = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Balance = params.get("Balance")
        self.Uin = params.get("Uin")
        self.RealBalance = params.get("RealBalance")
        self.CashAccountBalance = params.get("CashAccountBalance")
        self.IncomeIntoAccountBalance = params.get("IncomeIntoAccountBalance")
        self.PresentAccountBalance = params.get("PresentAccountBalance")
        self.FreezeAmount = params.get("FreezeAmount")
        self.OweAmount = params.get("OweAmount")
        self.IsAllowArrears = params.get("IsAllowArrears")
        self.IsCreditLimited = params.get("IsCreditLimited")
        self.CreditAmount = params.get("CreditAmount")
        self.CreditBalance = params.get("CreditBalance")
        self.RealCreditBalance = params.get("RealCreditBalance")
        self.RequestId = params.get("RequestId")


class DescribeBillDetailRequest(AbstractModel):
    """DescribeBillDetail request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset
        :type Offset: int
        :param Limit: Quantity, maximum is 100
        :type Limit: int
        :param PeriodType: The period type. byUsedTime: By usage period; byPayTime: By payment period. Must be the same as the period of the current monthly bill of the Billing Center. You can check your bill statistics period type at the top of the [Bill Overview](https://console.cloud.tencent.com/expense/bill/overview) page. 
        :type PeriodType: str
        :param Month: Month; format: yyyy-mm. You only have to enter either Month or BeginTime and EndTime. When you enter values for BeginTime and EndTime, Month becomes invalid. This value must be no earlier than the month when Bill 2.0 is activated; last 24 months data are available.
        :type Month: str
        :param BeginTime: The start time of the period; format: Y-m-d H:i:s. You only have to enter either Month or BeginTime and EndTime. When you enter values for BeginTime and EndTime, Month becomes invalid. BeginTime and EndTime must be inputted as a pair. This value must be no earlier than the month when Bill 2.0 is activated; last 24 months data are available.
        :type BeginTime: str
        :param EndTime: The end time of the period; format: Y-m-d H:i:s. You only have to enter either Month or BeginTime and EndTime. When you enter values for BeginTime and EndTime, Month becomes invalid. BeginTime and EndTime must be inputted as a pair. This value must be no earlier than the month when Bill 2.0 is activated; last 24 months data are available.
        :type EndTime: str
        :param NeedRecordNum: Indicates whether or not the total number of records of accessing the list is required, used for frontend pages.
1 = yes, 0 = no
        :type NeedRecordNum: int
        :param ProductCode: Queries information on a specified product
        :type ProductCode: str
        :param PayMode: Billing mode: prePay/postPay
        :type PayMode: str
        :param ResourceId: Queries information on a specified resource
        :type ResourceId: str
        :param ActionType: Action type to query. Valid values:
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
        :param ProjectId: Project ID: ID of the project to which the resource belongs
        :type ProjectId: int
        :param BusinessCode: Product code
Note: To query the product codes used in the current month, call <a href="https://intl.cloud.tencent.com/document/product/555/35761?from_cn_redirect=1">DescribeBillSummaryByProduct</a>.
        :type BusinessCode: str
        """
        self.Offset = None
        self.Limit = None
        self.PeriodType = None
        self.Month = None
        self.BeginTime = None
        self.EndTime = None
        self.NeedRecordNum = None
        self.ProductCode = None
        self.PayMode = None
        self.ResourceId = None
        self.ActionType = None
        self.ProjectId = None
        self.BusinessCode = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PeriodType = params.get("PeriodType")
        self.Month = params.get("Month")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.NeedRecordNum = params.get("NeedRecordNum")
        self.ProductCode = params.get("ProductCode")
        self.PayMode = params.get("PayMode")
        self.ResourceId = params.get("ResourceId")
        self.ActionType = params.get("ActionType")
        self.ProjectId = params.get("ProjectId")
        self.BusinessCode = params.get("BusinessCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillDetailResponse(AbstractModel):
    """DescribeBillDetail response structure.

    """

    def __init__(self):
        r"""
        :param DetailSet: Details list
        :type DetailSet: list of BillDetail
        :param Total: Total number of records
Note: This field may return null, indicating that no valid value was found.
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DetailSet = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailSet") is not None:
            self.DetailSet = []
            for item in params.get("DetailSet"):
                obj = BillDetail()
                obj._deserialize(item)
                self.DetailSet.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeBillResourceSummaryRequest(AbstractModel):
    """DescribeBillResourceSummary request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset
        :type Offset: int
        :param Limit: Quantity, maximum is 1000
        :type Limit: int
        :param Month: Month; format: yyyy-mm. This value cannot be earlier than the month when Bill 2.0 is enabled. Last 24 months data are available.
        :type Month: str
        :param PeriodType: The period type. byUsedTime: By usage period; byPayTime: by payment period. Must be the same as the period of the current monthly bill of the Billing Center. You can check your bill statistics period type at the top of the [Bill Overview](https://console.cloud.tencent.com/expense/bill/overview) page.
        :type PeriodType: str
        :param NeedRecordNum: Indicates whether or not the total number of records of accessing the list is required, used for frontend pages.
1 = yes, 0 = no
        :type NeedRecordNum: int
        :param ActionType: Action type to query. Valid values:
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
        :param ResourceId: ID of the instance to be queried
        :type ResourceId: str
        :param PayMode: Billing mode. Valid values: `prePay` (prepaid), `postPay` (postpaid)
        :type PayMode: str
        :param BusinessCode: Product code
Note: To query the product codes used in the current month, call <a href="https://intl.cloud.tencent.com/document/product/555/35761?from_cn_redirect=1">DescribeBillSummaryByProduct</a>.
        :type BusinessCode: str
        """
        self.Offset = None
        self.Limit = None
        self.Month = None
        self.PeriodType = None
        self.NeedRecordNum = None
        self.ActionType = None
        self.ResourceId = None
        self.PayMode = None
        self.BusinessCode = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Month = params.get("Month")
        self.PeriodType = params.get("PeriodType")
        self.NeedRecordNum = params.get("NeedRecordNum")
        self.ActionType = params.get("ActionType")
        self.ResourceId = params.get("ResourceId")
        self.PayMode = params.get("PayMode")
        self.BusinessCode = params.get("BusinessCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillResourceSummaryResponse(AbstractModel):
    """DescribeBillResourceSummary response structure.

    """

    def __init__(self):
        r"""
        :param ResourceSummarySet: Resource summary list
        :type ResourceSummarySet: list of BillResourceSummary
        :param Total: Total number of resource summary lists
Note: This field may return null, indicating that no valid value was found.
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ResourceSummarySet = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResourceSummarySet") is not None:
            self.ResourceSummarySet = []
            for item in params.get("ResourceSummarySet"):
                obj = BillResourceSummary()
                obj._deserialize(item)
                self.ResourceSummarySet.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeBillSummaryByPayModeRequest(AbstractModel):
    """DescribeBillSummaryByPayMode request structure.

    """

    def __init__(self):
        r"""
        :param BeginTime: The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type BeginTime: str
        :param EndTime: The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type EndTime: str
        :param PayerUin: Query bill data user's UIN
        :type PayerUin: str
        """
        self.BeginTime = None
        self.EndTime = None
        self.PayerUin = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByPayModeResponse(AbstractModel):
    """DescribeBillSummaryByPayMode response structure.

    """

    def __init__(self):
        r"""
        :param Ready: Indicates whether or not the data is ready. 0 = not ready, 1 = ready.
        :type Ready: int
        :param SummaryOverview: Detailed cost distribution for all billing modes
Note: This field may return null, indicating that no valid value was found.
        :type SummaryOverview: list of PayModeSummaryOverviewItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self.SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = PayModeSummaryOverviewItem()
                obj._deserialize(item)
                self.SummaryOverview.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillSummaryByProductRequest(AbstractModel):
    """DescribeBillSummaryByProduct request structure.

    """

    def __init__(self):
        r"""
        :param BeginTime: The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type BeginTime: str
        :param EndTime: The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type EndTime: str
        :param PayerUin: Queries bill data user's UIN
        :type PayerUin: str
        :param PayType: A bill type, which corresponds to a subtotal type of L0 bills.
This parameter has become valid since v3.0 bills took effect in May 2021.
Valid values:
`consume`: consumption
`refund`: refund
`adjustment`: bill adjustment
        :type PayType: str
        """
        self.BeginTime = None
        self.EndTime = None
        self.PayerUin = None
        self.PayType = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.PayerUin = params.get("PayerUin")
        self.PayType = params.get("PayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByProductResponse(AbstractModel):
    """DescribeBillSummaryByProduct response structure.

    """

    def __init__(self):
        r"""
        :param Ready: Indicates whether or not the data is ready. 0 = not ready, 1 = ready.
        :type Ready: int
        :param SummaryTotal: Total cost details
Note: This field may return null, indicating that no valid value was found.
        :type SummaryTotal: :class:`tencentcloud.billing.v20180709.models.BusinessSummaryTotal`
        :param SummaryOverview: Cost distribution of all products
Note: This field may return null, indicating that no valid value was found.
        :type SummaryOverview: list of BusinessSummaryOverviewItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryTotal = None
        self.SummaryOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryTotal") is not None:
            self.SummaryTotal = BusinessSummaryTotal()
            self.SummaryTotal._deserialize(params.get("SummaryTotal"))
        if params.get("SummaryOverview") is not None:
            self.SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = BusinessSummaryOverviewItem()
                obj._deserialize(item)
                self.SummaryOverview.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillSummaryByProjectRequest(AbstractModel):
    """DescribeBillSummaryByProject request structure.

    """

    def __init__(self):
        r"""
        :param BeginTime: The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type BeginTime: str
        :param EndTime: The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type EndTime: str
        :param PayerUin: Queries bill data user's UIN
        :type PayerUin: str
        """
        self.BeginTime = None
        self.EndTime = None
        self.PayerUin = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByProjectResponse(AbstractModel):
    """DescribeBillSummaryByProject response structure.

    """

    def __init__(self):
        r"""
        :param Ready: Indicates whether or not the data is ready. 0 = not ready, 1 = ready.
        :type Ready: int
        :param SummaryOverview: Detailed cost distribution for all projects
Note: This field may return null, indicating that no valid value was found.
        :type SummaryOverview: list of ProjectSummaryOverviewItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self.SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = ProjectSummaryOverviewItem()
                obj._deserialize(item)
                self.SummaryOverview.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillSummaryByRegionRequest(AbstractModel):
    """DescribeBillSummaryByRegion request structure.

    """

    def __init__(self):
        r"""
        :param BeginTime: The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type BeginTime: str
        :param EndTime: The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type EndTime: str
        :param PayerUin: Queries bill data user's UIN
        :type PayerUin: str
        """
        self.BeginTime = None
        self.EndTime = None
        self.PayerUin = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByRegionResponse(AbstractModel):
    """DescribeBillSummaryByRegion response structure.

    """

    def __init__(self):
        r"""
        :param Ready: Indicates whether or not the data is ready. 0 = not ready, 1 = ready.
        :type Ready: int
        :param SummaryOverview: Detailed cost distribution for all regions
Note: This field may return null, indicating that no valid value was found.
        :type SummaryOverview: list of RegionSummaryOverviewItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self.SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = RegionSummaryOverviewItem()
                obj._deserialize(item)
                self.SummaryOverview.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillSummaryByTagRequest(AbstractModel):
    """DescribeBillSummaryByTag request structure.

    """

    def __init__(self):
        r"""
        :param BeginTime: The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type BeginTime: str
        :param EndTime: The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.
        :type EndTime: str
        :param TagKey: Cost allocation tag key
        :type TagKey: str
        :param PayerUin: Payer UIN
        :type PayerUin: str
        :param TagValue: Resource tag value
        :type TagValue: str
        """
        self.BeginTime = None
        self.EndTime = None
        self.TagKey = None
        self.PayerUin = None
        self.TagValue = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.TagKey = params.get("TagKey")
        self.PayerUin = params.get("PayerUin")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByTagResponse(AbstractModel):
    """DescribeBillSummaryByTag response structure.

    """

    def __init__(self):
        r"""
        :param Ready: Indicates whether or not the data is ready. `0`: not ready; `1`: ready.
        :type Ready: int
        :param SummaryOverview: Details about cost distribution over different tags
Note: This field may return null, indicating that no valid values can be obtained.
        :type SummaryOverview: list of TagSummaryOverviewItem
        :param SummaryTotal: Total cost
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SummaryTotal: :class:`tencentcloud.billing.v20180709.models.SummaryTotal`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryOverview = None
        self.SummaryTotal = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self.SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = TagSummaryOverviewItem()
                obj._deserialize(item)
                self.SummaryOverview.append(obj)
        if params.get("SummaryTotal") is not None:
            self.SummaryTotal = SummaryTotal()
            self.SummaryTotal._deserialize(params.get("SummaryTotal"))
        self.RequestId = params.get("RequestId")


class DescribeDosageCosDetailByDateRequest(AbstractModel):
    """DescribeDosageCosDetailByDate request structure.

    """

    def __init__(self):
        r"""
        :param StartDate: The start date of the usage query
        :type StartDate: str
        :param EndDate: The end date of the usage query (end date must be in the same month as the start date)
        :type EndDate: str
        :param BucketName: Bucket name. You can use `Get Service` to query the list of all buckets under a requester account. For details, see [GET Service (List Buckets)](https://www.tencentcloud.com/document/product/436/8291).
        :type BucketName: str
        """
        self.StartDate = None
        self.EndDate = None
        self.BucketName = None


    def _deserialize(self, params):
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.BucketName = params.get("BucketName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDosageCosDetailByDateResponse(AbstractModel):
    """DescribeDosageCosDetailByDate response structure.

    """

    def __init__(self):
        r"""
        :param DetailSets: Array of usage
        :type DetailSets: list of CosDetailSets
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DetailSets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailSets") is not None:
            self.DetailSets = []
            for item in params.get("DetailSets"):
                obj = CosDetailSets()
                obj._deserialize(item)
                self.DetailSets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVoucherInfoRequest(AbstractModel):
    """DescribeVoucherInfo request structure.

    """

    def __init__(self):
        r"""
        :param Limit: The number of records per page. The default is 20, and the maximum is 1,000.
        :type Limit: int
        :param Offset: The page number the records start from. The default is 1.
        :type Offset: int
        :param Status: The voucher status. Valid values: `unUsed`, `used`, `delivered`, `cancel`, `overdue`.
        :type Status: str
        :param VoucherId: The voucher ID.
        :type VoucherId: str
        :param CodeId: The voucher order ID.
        :type CodeId: str
        :param ProductCode: The product code.
        :type ProductCode: str
        :param ActivityId: The campaign ID.
        :type ActivityId: str
        :param VoucherName: The voucher name.
        :type VoucherName: str
        :param TimeFrom: The start time of the promotional campaign.
        :type TimeFrom: str
        :param TimeTo: The end time of the promotional campaign.
        :type TimeTo: str
        :param SortField: The field used to sort the records. Valid values: BeginTime, EndTime, CreateTime.
        :type SortField: str
        :param SortOrder: Whether to sort the records in ascending or descending order. Valid values: desc, asc.
        :type SortOrder: str
        :param PayMode: The payment mode. Valid values: `postPay`: pay-as-you-go; `prePay`: prepaid; `riPay`: reserved instance; empty or `*`: all. If this parameter is empty or `*`, `productCode` and `subProductCode` must also be empty.
        :type PayMode: str
        :param PayScene: If `PayMode` is `postPay`, this parameter may be `spotpay` (spot instance) or `settle account` (regular pay-as-you-go). If `PayMode` is `prePay`, this parameter may be `purchase`, `renew`, or `modify` (downgrade/upgrade). If `PayMode` is `riPay`, this parameter may be `oneOffFee` (prepayment of reserved instance) or `hourlyFee` (hourly billing of reserved instance). `*` means to query vouchers that support all billing scenarios.
        :type PayScene: str
        :param Operator: The operator. The default is the UIN of the current user.
        :type Operator: str
        """
        self.Limit = None
        self.Offset = None
        self.Status = None
        self.VoucherId = None
        self.CodeId = None
        self.ProductCode = None
        self.ActivityId = None
        self.VoucherName = None
        self.TimeFrom = None
        self.TimeTo = None
        self.SortField = None
        self.SortOrder = None
        self.PayMode = None
        self.PayScene = None
        self.Operator = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Status = params.get("Status")
        self.VoucherId = params.get("VoucherId")
        self.CodeId = params.get("CodeId")
        self.ProductCode = params.get("ProductCode")
        self.ActivityId = params.get("ActivityId")
        self.VoucherName = params.get("VoucherName")
        self.TimeFrom = params.get("TimeFrom")
        self.TimeTo = params.get("TimeTo")
        self.SortField = params.get("SortField")
        self.SortOrder = params.get("SortOrder")
        self.PayMode = params.get("PayMode")
        self.PayScene = params.get("PayScene")
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVoucherInfoResponse(AbstractModel):
    """DescribeVoucherInfo response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The total number of vouchers.
        :type TotalCount: int
        :param TotalBalance: The total voucher balance. The value of this parameter is the total balance (USD, rounded to 8 decimal places) multiplied by 100,000,000.
        :type TotalBalance: int
        :param VoucherInfos: The voucher information.
Note: This field may return `null`, indicating that no valid value was found.
        :type VoucherInfos: list of VoucherInfos
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TotalBalance = None
        self.VoucherInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.TotalBalance = params.get("TotalBalance")
        if params.get("VoucherInfos") is not None:
            self.VoucherInfos = []
            for item in params.get("VoucherInfos"):
                obj = VoucherInfos()
                obj._deserialize(item)
                self.VoucherInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVoucherUsageDetailsRequest(AbstractModel):
    """DescribeVoucherUsageDetails request structure.

    """

    def __init__(self):
        r"""
        :param Limit: The number of records per page. The default is 20, and the maximum is 1,000.
        :type Limit: int
        :param Offset: The page number the records start from. The default is 1.
        :type Offset: int
        :param VoucherId: The voucher ID.
        :type VoucherId: str
        :param Operator: The operator. The default is the UIN of the current.
        :type Operator: str
        """
        self.Limit = None
        self.Offset = None
        self.VoucherId = None
        self.Operator = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.VoucherId = params.get("VoucherId")
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVoucherUsageDetailsResponse(AbstractModel):
    """DescribeVoucherUsageDetails response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The total number of vouchers.
        :type TotalCount: int
        :param TotalUsedAmount: The total amount used. The value of this parameter is the total amount used (USD, rounded to 8 decimal places) multiplied by 100,000,000.
        :type TotalUsedAmount: int
        :param UsageRecords: The usage details.
Note: This field may return `null`, indicating that no valid value was found.
        :type UsageRecords: list of UsageRecords
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TotalUsedAmount = None
        self.UsageRecords = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.TotalUsedAmount = params.get("TotalUsedAmount")
        if params.get("UsageRecords") is not None:
            self.UsageRecords = []
            for item in params.get("UsageRecords"):
                obj = UsageRecords()
                obj._deserialize(item)
                self.UsageRecords.append(obj)
        self.RequestId = params.get("RequestId")


class ExcludedProducts(AbstractModel):
    """The products that are not applicable.

    """

    def __init__(self):
        r"""
        :param GoodsName: The names of non-applicable products.
        :type GoodsName: str
        :param PayMode: `postPay`: pay-as-you-go; `prePay`: prepaid; `riPay`: reserved instance; empty or `*`: all.
        :type PayMode: str
        """
        self.GoodsName = None
        self.PayMode = None


    def _deserialize(self, params):
        self.GoodsName = params.get("GoodsName")
        self.PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayModeSummaryOverviewItem(AbstractModel):
    """Detailed summary of purchases by billing mode

    """

    def __init__(self):
        r"""
        :param PayMode: Billing mode
        :type PayMode: str
        :param PayModeName: Billing mode name
        :type PayModeName: str
        :param RealTotalCost: Actual cost
        :type RealTotalCost: str
        :param RealTotalCostRatio: Cost ratio, to two decimal points
        :type RealTotalCostRatio: str
        :param Detail: Detailed summary of purchases by transaction type
        :type Detail: list of ActionSummaryOverviewItem
        :param CashPayAmount: Cash amount
        :type CashPayAmount: str
        :param IncentivePayAmount: Trial credit amount
        :type IncentivePayAmount: str
        :param VoucherPayAmount: Voucher amount
        :type VoucherPayAmount: str
        :param TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        :param TransferPayAmount: Payment by commission credits
        :type TransferPayAmount: str
        """
        self.PayMode = None
        self.PayModeName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.Detail = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TotalCost = None
        self.TransferPayAmount = None


    def _deserialize(self, params):
        self.PayMode = params.get("PayMode")
        self.PayModeName = params.get("PayModeName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = ActionSummaryOverviewItem()
                obj._deserialize(item)
                self.Detail.append(obj)
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TotalCost = params.get("TotalCost")
        self.TransferPayAmount = params.get("TransferPayAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectSummaryOverviewItem(AbstractModel):
    """Detailed summary of purchases by project

    """

    def __init__(self):
        r"""
        :param ProjectId: Project ID
        :type ProjectId: str
        :param ProjectName: Project name
        :type ProjectName: str
        :param RealTotalCost: Actual cost
        :type RealTotalCost: str
        :param RealTotalCostRatio: Cost ratio, to two decimal points
        :type RealTotalCostRatio: str
        :param CashPayAmount: Cash amount
        :type CashPayAmount: str
        :param IncentivePayAmount: Trial credit amount
        :type IncentivePayAmount: str
        :param VoucherPayAmount: Voucher amount
        :type VoucherPayAmount: str
        :param BillMonth: Billing month, e.g. `2019-08`
        :type BillMonth: str
        :param TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        :param TransferPayAmount: Payment by commission credits
        :type TransferPayAmount: str
        """
        self.ProjectId = None
        self.ProjectName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.BillMonth = None
        self.TotalCost = None
        self.TransferPayAmount = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.BillMonth = params.get("BillMonth")
        self.TotalCost = params.get("TotalCost")
        self.TransferPayAmount = params.get("TransferPayAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionSummaryOverviewItem(AbstractModel):
    """Detailed summary of purchases by region

    """

    def __init__(self):
        r"""
        :param RegionId: Region ID
Note: This field may return null, indicating that no valid value was found.
        :type RegionId: str
        :param RegionName: Region name
        :type RegionName: str
        :param RealTotalCost: Actual cost
        :type RealTotalCost: str
        :param RealTotalCostRatio: Cost ratio, to two decimal points
        :type RealTotalCostRatio: str
        :param CashPayAmount: Cash amount
        :type CashPayAmount: str
        :param IncentivePayAmount: Trial credit amount
        :type IncentivePayAmount: str
        :param VoucherPayAmount: Voucher amount
        :type VoucherPayAmount: str
        :param BillMonth: Billing month, e.g. `2019-08`
        :type BillMonth: str
        :param TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        :param TransferPayAmount: Payment by commission credits
        :type TransferPayAmount: str
        """
        self.RegionId = None
        self.RegionName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.BillMonth = None
        self.TotalCost = None
        self.TransferPayAmount = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.BillMonth = params.get("BillMonth")
        self.TotalCost = params.get("TotalCost")
        self.TransferPayAmount = params.get("TransferPayAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SummaryTotal(AbstractModel):
    """Total cost

    """

    def __init__(self):
        r"""
        :param RealTotalCost: Total cost
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RealTotalCost: str
        :param TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TotalCost: str
        """
        self.RealTotalCost = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")
        self.TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagSummaryOverviewItem(AbstractModel):
    """Details about cost distribution over different tags.

    """

    def __init__(self):
        r"""
        :param TagValue: Tag value
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagValue: str
        :param RealTotalCost: Actual cost
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealTotalCost: str
        :param RealTotalCostRatio: Cost percentage rounded to two decimal places
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealTotalCostRatio: str
        :param TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TotalCost: str
        :param CashPayAmount: Payment by cash credits
Note: This field may return null, indicating that no valid values can be obtained.
        :type CashPayAmount: str
        :param IncentivePayAmount: Payment by free credits
Note: This field may return null, indicating that no valid values can be obtained.
        :type IncentivePayAmount: str
        :param VoucherPayAmount: Payment by vouchers
Note: This field may return null, indicating that no valid values can be obtained.
        :type VoucherPayAmount: str
        :param TransferPayAmount: Payment by commission credits
Note: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        """
        self.TagValue = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.TotalCost = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None


    def _deserialize(self, params):
        self.TagValue = params.get("TagValue")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.TotalCost = params.get("TotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageDetails(AbstractModel):
    """The product purchased.

    """

    def __init__(self):
        r"""
        :param ProductName: The name of the product.
Note: This field may return `null`, indicating that no valid value was found.
        :type ProductName: str
        :param SubProductName: 
        :type SubProductName: str
        """
        self.ProductName = None
        self.SubProductName = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        self.SubProductName = params.get("SubProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageRecords(AbstractModel):
    """The usage records.

    """

    def __init__(self):
        r"""
        :param UsedAmount: The amount used. The value of this parameter is the amount used (USD, rounded to 8 decimal places) multiplied by 100,000,000.
        :type UsedAmount: int
        :param UsedTime: The time when the voucher was used.
        :type UsedTime: str
        :param UsageDetails: The details of the product purchased.
Note: This field may return `null`, indicating that no valid value was found.
        :type UsageDetails: list of UsageDetails
        """
        self.UsedAmount = None
        self.UsedTime = None
        self.UsageDetails = None


    def _deserialize(self, params):
        self.UsedAmount = params.get("UsedAmount")
        self.UsedTime = params.get("UsedTime")
        if params.get("UsageDetails") is not None:
            self.UsageDetails = []
            for item in params.get("UsageDetails"):
                obj = UsageDetails()
                obj._deserialize(item)
                self.UsageDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoucherInfos(AbstractModel):
    """Voucher information.

    """

    def __init__(self):
        r"""
        :param OwnerUin: The owner of the voucher.
        :type OwnerUin: str
        :param Status: The status of the voucher: `unUsed`, `used`, `delivered`, `cancel`, `overdue`
        :type Status: str
        :param NominalValue: The value of the voucher. The value of this parameter is the voucher value (USD, rounded to 8 decimal places) multiplied by 100,000,000.
        :type NominalValue: int
        :param Balance: The balance left. The value of this parameter is the balance left (USD, rounded to 8 decimal places) multiplied by 100,000,000.
        :type Balance: int
        :param VoucherId: The voucher ID.
        :type VoucherId: str
        :param PayMode: `postPay`: pay-as-you-go; `prePay`: prepaid; `riPay`: reserved instance; empty or `*`: all.
        :type PayMode: str
        :param PayScene: If `PayMode` is `postPay`, this parameter may be `spotpay` (spot instance) or `settle account` (regular pay-as-you-go). If `PayMode` is `prePay`, this parameter may be `purchase`, `renew`, or `modify` (downgrade/upgrade). If `PayMode` is `riPay`, this parameter may be `oneOffFee` (prepayment of reserved instance) or `hourlyFee` (hourly billing of reserved instance). `*` means to query vouchers that support all billing scenarios.
        :type PayScene: str
        :param BeginTime: The start time of the validity period.
        :type BeginTime: str
        :param EndTime: The end time of the validity period.
        :type EndTime: str
        :param ApplicableProducts: The products that are applicable.
Note: This field may return `null`, indicating that no valid value was found.
        :type ApplicableProducts: :class:`tencentcloud.billing.v20180709.models.ApplicableProducts`
        :param ExcludedProducts: The products that are not applicable.
Note: This field may return `null`, indicating that no valid value was found.
        :type ExcludedProducts: list of ExcludedProducts
        """
        self.OwnerUin = None
        self.Status = None
        self.NominalValue = None
        self.Balance = None
        self.VoucherId = None
        self.PayMode = None
        self.PayScene = None
        self.BeginTime = None
        self.EndTime = None
        self.ApplicableProducts = None
        self.ExcludedProducts = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.Status = params.get("Status")
        self.NominalValue = params.get("NominalValue")
        self.Balance = params.get("Balance")
        self.VoucherId = params.get("VoucherId")
        self.PayMode = params.get("PayMode")
        self.PayScene = params.get("PayScene")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        if params.get("ApplicableProducts") is not None:
            self.ApplicableProducts = ApplicableProducts()
            self.ApplicableProducts._deserialize(params.get("ApplicableProducts"))
        if params.get("ExcludedProducts") is not None:
            self.ExcludedProducts = []
            for item in params.get("ExcludedProducts"):
                obj = ExcludedProducts()
                obj._deserialize(item)
                self.ExcludedProducts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        