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
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BusinessCode: str
        :param ProductCode: Subproduct code
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ProductCode: str
        :param ActionType: Transaction type/code (optional)
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
        :param ProductCodeName: Sub-product name: sub-categories of Tencent Cloud services, such as CVM-Standard S1; if no subproduct name is obtained, '-' is returned.
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
        :param BusinessCode: 
        :type BusinessCode: str
        :param ProductCode: 
        :type ProductCode: str
        :param RegionId: 
        :type RegionId: int
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
Note: This field may return null, indicating that no valid value was found.
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
        """
        self.RealTotalCost = None
        self.VoucherPayAmount = None
        self.IncentivePayAmount = None
        self.CashPayAmount = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.CashPayAmount = params.get("CashPayAmount")
        self.TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param BusinessCode: Business code
Note: To query business codes used in the current month, call <a href="https://intl.cloud.tencent.com/document/product/555/35761?from_cn_redirect=1">DescribeBillSummaryByProduct</a>.
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
        :param BusinessCode: Business code
Note: To query business codes used in the current month, call <a href="https://intl.cloud.tencent.com/document/product/555/35761?from_cn_redirect=1">DescribeBillSummaryByProduct</a>.
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
        """
        self.TagValue = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.TagValue = params.get("TagValue")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        