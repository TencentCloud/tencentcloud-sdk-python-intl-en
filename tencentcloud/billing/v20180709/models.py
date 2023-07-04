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
        :param ActionType: Transaction type code
        :type ActionType: str
        :param ActionTypeName: Transaction type, which can be monthly subscription purchase, monthly subscription renewal, or pay-as-you-go deduction.
        :type ActionTypeName: str
        :param RealTotalCostRatio: Cost ratio, to two decimal points
        :type RealTotalCostRatio: str
        :param RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param TransferPayAmount: Commission credit: The amount paid with the user’s commission credit. Note: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        :param BillMonth: Billing month, e.g. `2019-08`
        :type BillMonth: str
        :param TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        """
        self.ActionType = None
        self.ActionTypeName = None
        self.RealTotalCostRatio = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None
        self.BillMonth = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.ActionType = params.get("ActionType")
        self.ActionTypeName = params.get("ActionTypeName")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.RealTotalCost = params.get("RealTotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
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
        :param BusinessCodeName: Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :type BusinessCodeName: str
        :param ProductCodeName: Subproduct name: The subcategory of a Tencent Cloud product purchased by the user, such as CVM – Standard S1.
        :type ProductCodeName: str
        :param PayModeName: Billing mode, which can be monthly subscription or pay-as-you-go.
        :type PayModeName: str
        :param ProjectName: Project name: The project to which a resource belongs, which is user-designated. If a resource has not been assigned to a project, it will automatically belong to the default project.
        :type ProjectName: str
        :param RegionName: Region: The region to which a resource belongs, such as South China (Guangzhou).
        :type RegionName: str
        :param ZoneName: Availability zone: availability zone of a resource, e.g. Guangzhou Zone 3
        :type ZoneName: str
        :param ResourceId: Instance ID: The object ID of a billed resource, such as a CVM instance ID. This object ID may vary due to various forms and contents of resources in different products.
        :type ResourceId: str
        :param ResourceName: Instance name: The resource name set by the user in the console. If it is not set, it will be empty by default.
        :type ResourceName: str
        :param ActionTypeName: Transaction type, which can be monthly subscription purchase, monthly subscription renewal, or pay-as-you-go deduction.
        :type ActionTypeName: str
        :param OrderId: Order ID: The order number for a monthly subscription purchase
        :type OrderId: str
        :param BillId: Transaction ID: The bill number for a deducted payment
        :type BillId: str
        :param PayTime: Transaction time: The time at which a payment was deducted
        :type PayTime: str
        :param FeeBeginTime: Usage start time: The time at which product or service usage starts
        :type FeeBeginTime: str
        :param FeeEndTime: Usage end time: The time at which product or service usage ends
        :type FeeEndTime: str
        :param ComponentSet: Component list
        :type ComponentSet: list of BillDetailComponent
        :param PayerUin: Payer account ID: The account ID of the payer, which is the unique identifier of a Tencent Cloud user.
        :type PayerUin: str
        :param OwnerUin: Owner account ID: The account ID of the actual resource user
        :type OwnerUin: str
        :param OperateUin: Operator account ID: The account or role ID of the operator who purchases or activates a resource
        :type OperateUin: str
        :param Tags: Tag information. Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of BillTagInfo
        :param BusinessCode: Product code. Note: This field may return null, indicating that no valid values can be obtained.
        :type BusinessCode: str
        :param ProductCode: Subproduct code. Note: This field may return null, indicating that no valid values can be obtained.
        :type ProductCode: str
        :param ActionType: Transaction type code. Note: This field may return null, indicating that no valid values can be obtained.
        :type ActionType: str
        :param RegionId: Region ID. Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionId: str
        :param ProjectId: Project ID
        :type ProjectId: int
        :param PriceInfo: Price attribute
Note: This field may return null, indicating that no valid values can be obtained.
        :type PriceInfo: list of str
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
        self.PriceInfo = None


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
        self.PriceInfo = params.get("PriceInfo")
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
        :param ComponentCodeName: Component type: The component type of a product or service purchased, such as CVM instance components including CPU and memory.
        :type ComponentCodeName: str
        :param ItemCodeName: Component name: The specific component of a product or service purchased
        :type ItemCodeName: str
        :param SinglePrice: Component list price: The listed unit price of a component. If a customer has applied for a fixed preferential price or contract price, this parameter will not be displayed by default.
        :type SinglePrice: str
        :param SpecifiedPrice: Specified price of a component. This parameter has been deprecated.
        :type SpecifiedPrice: str
        :param PriceUnit: Component price measurement unit: The unit of measurement for a component price, which is composed of USD, usage unit, and duration unit.
        :type PriceUnit: str
        :param UsedAmount: Component usage: The actually settled usage of a component, which is "Raw usage - Deducted usage (including packages)".
        :type UsedAmount: str
        :param UsedAmountUnit: Component usage unit: The unit of measurement for component usage
        :type UsedAmountUnit: str
        :param RealTotalMeasure: 
        :type RealTotalMeasure: str
        :param DeductedMeasure: 
        :type DeductedMeasure: str
        :param TimeSpan: Usage duration: The resource usage duration
        :type TimeSpan: str
        :param TimeUnitName: Duration unit: The unit of measurement for usage duration
        :type TimeUnitName: str
        :param Cost: Original cost: The original cost of a resource, which is "List price x Usage x Usage duration". If a customer has applied for a fixed preferential price or contract price or is in a refund scenario, this parameter will not be displayed by default.
        :type Cost: str
        :param Discount: Discount multiplier: The discount multiplier applied to the cost of the resource. If a customer has applied for a fixed preferential price or contract price or is in a refund scenario, this parameter will not be displayed by default.
        :type Discount: str
        :param ReduceType: Offer type
        :type ReduceType: str
        :param RealCost: Total amount after discount: Total amount after discount = (Original cost - RI deduction (cost) - SP deduction (cost)) x Discount multiplier
        :type RealCost: str
        :param VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param TransferPayAmount: Commission credit: The amount paid with the user’s commission credit. Note: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        :param ItemCode: Component type code. Note: This field may return null, indicating that no valid values can be obtained.
        :type ItemCode: str
        :param ComponentCode: Component name code. Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentCode: str
        :param ContractPrice: Component contracted price: The contracted unit price of a component, which is "List price x Discount". Note: This field may return null, indicating that no valid values can be obtained.
        :type ContractPrice: str
        :param InstanceType: Instance type: The instance type of a product or service purchased, which can be resource package, RI, SP, or spot instance. Other instance types are not displayed by default. Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param RiTimeSpan: RI deduction (duration): The usage duration deducted by RI. Note: This field may return null, indicating that no valid values can be obtained.
        :type RiTimeSpan: str
        :param OriginalCostWithRI: RI deduction (cost): The amount deducted from the original cost by RI. Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalCostWithRI: str
        :param SPDeductionRate: Savings plan deduction rate: The discount multiplier that applies to the component based on the remaining commitment of the savings plan. Note: This field may return null, indicating that no valid values can be obtained.
        :type SPDeductionRate: str
        :param SPDeduction: Cost deduction by SP. This parameter has been deprecated. Note: This field may return null, indicating that no valid values can be obtained.
        :type SPDeduction: str
        :param OriginalCostWithSP: SP deduction (cost): SP deduction (cost) = Cost deduction by SP / SP deduction rate. Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalCostWithSP: str
        :param BlendedDiscount: Blended discount multiplier: The final discount multiplier that is applied after combining multiple discount types, which is "Total amount after discount / Original cost". Note: This field may return null, indicating that no valid values can be obtained.
        :type BlendedDiscount: str
        """
        self.ComponentCodeName = None
        self.ItemCodeName = None
        self.SinglePrice = None
        self.SpecifiedPrice = None
        self.PriceUnit = None
        self.UsedAmount = None
        self.UsedAmountUnit = None
        self.RealTotalMeasure = None
        self.DeductedMeasure = None
        self.TimeSpan = None
        self.TimeUnitName = None
        self.Cost = None
        self.Discount = None
        self.ReduceType = None
        self.RealCost = None
        self.VoucherPayAmount = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.TransferPayAmount = None
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
        self.RealTotalMeasure = params.get("RealTotalMeasure")
        self.DeductedMeasure = params.get("DeductedMeasure")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnitName = params.get("TimeUnitName")
        self.Cost = params.get("Cost")
        self.Discount = params.get("Discount")
        self.ReduceType = params.get("ReduceType")
        self.RealCost = params.get("RealCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
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
        :param BusinessCodeName: Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :type BusinessCodeName: str
        :param ProductCodeName: Subproduct name: The subcategory of a Tencent Cloud product purchased by the user, such as CVM – Standard S1.
        :type ProductCodeName: str
        :param PayModeName: Billing mode, which can be monthly subscription or pay-as-you-go.
        :type PayModeName: str
        :param ProjectName: Project name: The project to which a resource belongs, which is user-designated. If a resource has not been assigned to a project, it will automatically belong to the default project.
        :type ProjectName: str
        :param RegionName: Region: The region to which a resource belongs, such as South China (Guangzhou).
        :type RegionName: str
        :param ZoneName: Availability zone: The availability zone to which a resource belongs, such as Guangzhou Zone 3.
        :type ZoneName: str
        :param ResourceId: Instance ID: The object ID of a billed resource, such as a CVM instance ID. This object ID may vary due to various forms and contents of resources in different products.	
        :type ResourceId: str
        :param ResourceName: Instance name: The resource name set by the user in the console. If it is not set, it will be empty by default.
        :type ResourceName: str
        :param ActionTypeName: Transaction type, which can be monthly subscription purchase, monthly subscription renewal, or pay-as-you-go deduction.
        :type ActionTypeName: str
        :param OrderId: Order ID: The order number for a monthly subscription purchase
        :type OrderId: str
        :param PayTime: Transaction time: The time at which a payment was deducted
        :type PayTime: str
        :param FeeBeginTime: Usage start time: The time at which product or service usage starts
        :type FeeBeginTime: str
        :param FeeEndTime: Usage end time: The time at which product or service usage ends
        :type FeeEndTime: str
        :param ConfigDesc: Configuration description: The billable item names and usage of a resource, which are displayed on the resource bill only.
        :type ConfigDesc: str
        :param ExtendField1: Extended field 1: Extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField1: str
        :param ExtendField2: Extended field 2: Extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField2: str
        :param TotalCost: Original cost: The original cost of a resource, which is "List price x Usage x Usage duration". If a customer has applied for a fixed preferential price or contract price or applied for a refund, this parameter will not be displayed by default.
        :type TotalCost: str
        :param Discount: Discount multiplier: The discount multiplier applied to the cost of the resource. If a customer has applied for a fixed preferential price or contract price or applied for a refund, this parameter will not be displayed by default.
        :type Discount: str
        :param ReduceType: Offer type
        :type ReduceType: str
        :param RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param TransferPayAmount: Commission credit: The amount paid with the user’s commission credit. Note: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        :param ExtendField3: Extended field 3: Extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField3: str
        :param ExtendField4: Extended field 4: Extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField4: str
        :param ExtendField5: Extended field 5: Extended attribute information of a product, which is displayed on the resource bill only.
        :type ExtendField5: str
        :param Tags: Tag information. Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of BillTagInfo
        :param PayerUin: Payer account ID: The account ID of the payer, which is the unique identifier of a Tencent Cloud user.
        :type PayerUin: str
        :param OwnerUin: Owner account ID: The account ID of the actual resource user
        :type OwnerUin: str
        :param OperateUin: Operator account ID: The account or role ID of the operator who purchases or activates a resource.
        :type OperateUin: str
        :param BusinessCode: Product code
        :type BusinessCode: str
        :param ProductCode: Subproduct code
        :type ProductCode: str
        :param RegionId: Region ID
        :type RegionId: int
        :param InstanceType: Instance type: The instance type of a product or service purchased, which can be resource package, RI, SP, or spot instance. Other instance types are not displayed by default.
        :type InstanceType: str
        :param OriginalCostWithRI: RI deduction (cost): The amount deducted from the original cost by RI	
        :type OriginalCostWithRI: str
        :param SPDeduction: Cost deduction by SP. This parameter has been deprecated.
        :type SPDeduction: str
        :param OriginalCostWithSP: SP deduction (cost): SP deduction (cost) = Cost deduction by SP / SP deduction rate	
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
        self.TransferPayAmount = None
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
        self.TransferPayAmount = params.get("TransferPayAmount")
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
        


class BusinessSummaryInfo(AbstractModel):
    """Detailed summary of products

    """

    def __init__(self):
        r"""
        :param BusinessCode: Product code
        :type BusinessCode: str
        :param BusinessCodeName: Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :type BusinessCodeName: str
        :param TotalCost: Original cost in USD. This parameter became valid when Bill 3.0 took effect in May 2021. Before that, `-` was returned for this parameter. If a customer has applied for a contract price different from the prices listed on the official website, `-` will also be returned for this parameter. 
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCost: str
        :param RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param TransferPayAmount: Commission credit: The amount paid with the user’s commission credit. Note: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        """
        self.BusinessCode = None
        self.BusinessCodeName = None
        self.TotalCost = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.TotalCost = params.get("TotalCost")
        self.RealTotalCost = params.get("RealTotalCost")
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
        


class BusinessSummaryOverviewItem(AbstractModel):
    """Summarize product details by product

    """

    def __init__(self):
        r"""
        :param BusinessCode: Product code. Note: This field may return null, indicating that no valid values can be obtained.
        :type BusinessCode: str
        :param BusinessCodeName: Product name: The name of a Tencent Cloud product purchased by the user, such as CVM.
        :type BusinessCodeName: str
        :param RealTotalCostRatio: Cost ratio, to two decimal points
        :type RealTotalCostRatio: str
        :param RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param TransferPayAmount: Commission credit: The amount paid with the user’s commission credit.
        :type TransferPayAmount: str
        :param BillMonth: Billing month, e.g. `2019-08`
        :type BillMonth: str
        :param TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        """
        self.BusinessCode = None
        self.BusinessCodeName = None
        self.RealTotalCostRatio = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None
        self.BillMonth = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.RealTotalCost = params.get("RealTotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
        self.BillMonth = params.get("BillMonth")
        self.TotalCost = params.get("TotalCost")
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
        :param RealTotalCost: Total amount after discount

        :type RealTotalCost: str
        :param VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param TransferPayAmount: Commission credit: The amount paid with the user’s commission credit.
        :type TransferPayAmount: str
        :param TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        """
        self.RealTotalCost = None
        self.VoucherPayAmount = None
        self.IncentivePayAmount = None
        self.CashPayAmount = None
        self.TransferPayAmount = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.CashPayAmount = params.get("CashPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
        self.TotalCost = params.get("TotalCost")
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
        :param SubProductCodeName: Subproduct name
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
        :param CreditAmount: Credit limit in cents. Credit limit－available credit balance = consumption amount
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
        :param BeginTime: The start time of the query range, which should be in the format Y-m-d H:i:s . The query range must be in the last 18 months and cannot be earlier than May 2018 (when Bill 2.0 was introduced). The start time and end time must be in the same month.

Example: tccli billing DescribeBillDetail --cli-unfold-argument --Offset 1 --Limit 100 --BeginTime '2023-04-01 12:05:15' --EndTime '2023-04-18 12:00:10' --ProjectId 1000000731  --version "2018-07-09"

Alternatively, you can use Month to query the billing details of a month.
Example:
ccli billing DescribeBillDetail --cli-unfold-argument --Offset 1 --Limit 100 --Month 2023-04  --version "2018-07-09" --ResourceId "disk-oj9okstm"
        :type BeginTime: str
        :param EndTime: The end time of the query range, which should be in the format `Y-m-d H:i:s `. The query range must be in the last 18 months and cannot be earlier than May 2018 (when Bill 2.0 was introduced). The start time and end time must be in the same month.

Example: tccli billing DescribeBillDetail --cli-unfold-argument --Offset 1 --Limit 100 --BeginTime '2023-04-01 12:05:15' --EndTime '2023-04-18 12:00:10' --ProjectId 1000000731  --version "2018-07-09"

Alternatively, you can use `Month` to query the billing details of a month. 
Example:
ccli billing DescribeBillDetail --cli-unfold-argument --Offset 1 --Limit 100 --Month 2023-04  --version "2018-07-09" --ResourceId "disk-oj9okstm"
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
        :param Context: Context information returned by the last request. You can set `Month` to `2023-05` or later to accelerate queries. We recommend users whose data volume is over 100 thousand entries use the paginated query feature, which can help greatly speed up your queries.
        :type Context: str
        :param PayerUin: 
        :type PayerUin: str
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
        self.Context = None
        self.PayerUin = None


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
        self.Context = params.get("Context")
        self.PayerUin = params.get("PayerUin")
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
        :param Total: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param Context: Context information returned by this request. The value can be passed in as the value of parameters in the next request to accelerate queries. Note: This field may return null, indicating that no valid values can be obtained.
        :type Context: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DetailSet = None
        self.Total = None
        self.Context = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailSet") is not None:
            self.DetailSet = []
            for item in params.get("DetailSet"):
                obj = BillDetail()
                obj._deserialize(item)
                self.DetailSet.append(obj)
        self.Total = params.get("Total")
        self.Context = params.get("Context")
        self.RequestId = params.get("RequestId")


class DescribeBillResourceSummaryRequest(AbstractModel):
    """DescribeBillResourceSummary request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Pagination offset. If `Offset` is `0`, it indicates the first page. If `Limit` is `100`, "`Offset` = `100`" indicates the second page, then "`Offset` = `200`" indicates the third page, and so on.
        :type Offset: int
        :param Limit: Quantity, maximum is 1000
        :type Limit: int
        :param Month: Bill month in the format of "yyyy-mm". This value must be no earlier than March 2019, when Bill 2.0 was launched.
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
        :param PayerUin: 
        :type PayerUin: str
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
        self.PayerUin = None


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
        self.PayerUin = params.get("PayerUin")
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
        :param Total: Total number of resource summary lists, which will not be returned when `NeedRecordNum` is `0`. This field may return null, indicating that no valid values can be obtained.
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
        :param Ready: Indicates whether the data is ready. `0`: Not ready. `1`: Ready. If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first. Wait for 5-10 minutes and try again.
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
        :param Ready: Indicates whether the data is ready. `0`: Not ready. `1`: Ready. If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first. Wait for 5-10 minutes and try again.
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
        :param Ready: Indicates whether the data is ready. `0`: Not ready. `1`: Ready. If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first. Wait for 5-10 minutes and try again.
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
        :param Ready: Indicates whether the data is ready. `0`: Not ready. `1`: Ready. If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first. Wait for 5-10 minutes and try again.
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
        :param TagKey: Cost allocation tag key, which can be customized.
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
        :param Ready: Indicates whether the data is ready. `0`: Not ready. `1`: Ready. If `Ready` is `0`, it indicates that the current UIN is initializing billing for the first. Wait for 5-10 minutes and try again.
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


class DescribeBillSummaryRequest(AbstractModel):
    """DescribeBillSummary request structure.

    """

    def __init__(self):
        r"""
        :param Month: Bill month in the format of "yyyy-mm"
        :type Month: str
        :param GroupType: Bill dimension. Valid values: `business`, `project`, `region`, `payMode`, and `tag`
        :type GroupType: str
        :param TagKey: Tag key, which is used when `GroupType` is `tag`.
        :type TagKey: list of str
        """
        self.Month = None
        self.GroupType = None
        self.TagKey = None


    def _deserialize(self, params):
        self.Month = params.get("Month")
        self.GroupType = params.get("GroupType")
        self.TagKey = params.get("TagKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryResponse(AbstractModel):
    """DescribeBillSummary response structure.

    """

    def __init__(self):
        r"""
        :param Ready: Indicates whether the data is ready. `0`: Not ready. `1`: Ready. If `Ready` is `0`, it indicates the current UIN is initializing for the first billing. Wait for 5-10 minutes and try again.
        :type Ready: int
        :param SummaryDetail: Detailed summary of costs by multiple dimensions
        :type SummaryDetail: list of SummaryDetail
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryDetail") is not None:
            self.SummaryDetail = []
            for item in params.get("SummaryDetail"):
                obj = SummaryDetail()
                obj._deserialize(item)
                self.SummaryDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDosageCosDetailByDateRequest(AbstractModel):
    """DescribeDosageCosDetailByDate request structure.

    """

    def __init__(self):
        r"""
        :param StartDate: The start date of the usage query, such as `2020-09-01`.
        :type StartDate: str
        :param EndDate: The end date of the usage query (end date must be in the same month as the start date), such as `2020-09-30`.
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
        :param TimeFrom: The start date of the voucher issuance, such as `2021-01-01`.
        :type TimeFrom: str
        :param TimeTo: The end date of the voucher issuance, such as `2021-01-01`.
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
    """Detailed summary of costs by billing mode

    """

    def __init__(self):
        r"""
        :param PayMode: Billing mode code
        :type PayMode: str
        :param PayModeName: Billing mode, which can be monthly subscription or pay-as-you-go.
        :type PayModeName: str
        :param RealTotalCostRatio: Cost ratio, to two decimal points
        :type RealTotalCostRatio: str
        :param RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param CashPayAmount: Cash credit: The amount paid from the user’s cash balance
        :type CashPayAmount: str
        :param IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param TransferPayAmount: Commission credit: The amount paid with the user’s commission credit.
        :type TransferPayAmount: str
        :param TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        :param Detail: Detailed summary of costs by transaction type
        :type Detail: list of ActionSummaryOverviewItem
        """
        self.PayMode = None
        self.PayModeName = None
        self.RealTotalCostRatio = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None
        self.TotalCost = None
        self.Detail = None


    def _deserialize(self, params):
        self.PayMode = params.get("PayMode")
        self.PayModeName = params.get("PayModeName")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.RealTotalCost = params.get("RealTotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
        self.TotalCost = params.get("TotalCost")
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = ActionSummaryOverviewItem()
                obj._deserialize(item)
                self.Detail.append(obj)
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
        :param ProjectName: Project name: The project to which a resource belongs, which is user-designated. If a resource has not been assigned to a project, it will automatically belong to the default project.
        :type ProjectName: str
        :param RealTotalCostRatio: Cost ratio, to two decimal points
        :type RealTotalCostRatio: str
        :param RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param TransferPayAmount: Commission credit: The amount paid with the user’s commission credit.
        :type TransferPayAmount: str
        :param BillMonth: Billing month, e.g. `2019-08`
        :type BillMonth: str
        :param TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        """
        self.ProjectId = None
        self.ProjectName = None
        self.RealTotalCostRatio = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None
        self.BillMonth = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.RealTotalCost = params.get("RealTotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
        self.BillMonth = params.get("BillMonth")
        self.TotalCost = params.get("TotalCost")
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
        :param RegionName: Region: The region to which a resource belongs, such as South China (Guangzhou).
        :type RegionName: str
        :param RealTotalCostRatio: Cost ratio, to two decimal points
        :type RealTotalCostRatio: str
        :param RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param TransferPayAmount: Commission credit: The amount paid with the user’s commission credit.
        :type TransferPayAmount: str
        :param BillMonth: Billing month, e.g. `2019-08`
        :type BillMonth: str
        :param TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
        :type TotalCost: str
        """
        self.RegionId = None
        self.RegionName = None
        self.RealTotalCostRatio = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None
        self.BillMonth = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.RealTotalCost = params.get("RealTotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
        self.BillMonth = params.get("BillMonth")
        self.TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SummaryDetail(AbstractModel):
    """Detailed summary of costs by multiple dimensions

    """

    def __init__(self):
        r"""
        :param GroupKey: Bill dimension code. Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupKey: str
        :param GroupValue: Bill dimension value. Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupValue: str
        :param TotalCost: Original cost in USD. This parameter has become valid since Bill 3.0 took effect in May 2021, and before that `-` was returned for this parameter. If a customer has applied for a contract price different from the prices listed on the official website, `-` will also be returned for this parameter.
        :type TotalCost: str
        :param RealTotalCost: Total amount after discount
        :type RealTotalCost: str
        :param CashPayAmount: Cash credit: The amount paid from the user’s cash account
        :type CashPayAmount: str
        :param IncentivePayAmount: Free credit: The amount paid with the user’s free credit
        :type IncentivePayAmount: str
        :param VoucherPayAmount: Voucher payment: The voucher deduction amount
        :type VoucherPayAmount: str
        :param TransferPayAmount: Commission credit: The amount paid with the user’s commission credit. Note: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        :param Business: Detailed summary of products. Note: This field may return null, indicating that no valid values can be obtained.
        :type Business: list of BusinessSummaryInfo
        """
        self.GroupKey = None
        self.GroupValue = None
        self.TotalCost = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None
        self.Business = None


    def _deserialize(self, params):
        self.GroupKey = params.get("GroupKey")
        self.GroupValue = params.get("GroupValue")
        self.TotalCost = params.get("TotalCost")
        self.RealTotalCost = params.get("RealTotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
        if params.get("Business") is not None:
            self.Business = []
            for item in params.get("Business"):
                obj = BusinessSummaryInfo()
                obj._deserialize(item)
                self.Business.append(obj)
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
        :param RealTotalCost: Total amount after discount. Note: This field may return null, indicating that no valid values can be obtained.
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
        :param RealTotalCostRatio: Cost percentage rounded to two decimal places
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealTotalCostRatio: str
        :param RealTotalCost: Total amount after discount. Note: This field may return null, indicating that no valid values can be obtained.
        :type RealTotalCost: str
        :param CashPayAmount: Cash credit: The amount paid from the user’s cash account. Note: This field may return null, indicating that no valid values can be obtained.
        :type CashPayAmount: str
        :param IncentivePayAmount: Free credit: The amount paid with the user’s free credit. Note: This field may return null, indicating that no valid values can be obtained.
        :type IncentivePayAmount: str
        :param VoucherPayAmount: Voucher payment: The amount deducted by using vouchers. Note: This field may return null, indicating that no valid values can be obtained.
        :type VoucherPayAmount: str
        :param TransferPayAmount: Commission credit: The amount paid with the user’s commission credit. Note: This field may return null, indicating that no valid values can be obtained.
        :type TransferPayAmount: str
        :param TotalCost: The original cost in USD. This parameter has become valid since v3.0 bills took effect in May 2021, and before that `-` was returned for this parameter. If a customer uses a contract price different from the published price, `-` will also be returned for this parameter.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TotalCost: str
        """
        self.TagValue = None
        self.RealTotalCostRatio = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.TagValue = params.get("TagValue")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.RealTotalCost = params.get("RealTotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
        self.TotalCost = params.get("TotalCost")
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
        