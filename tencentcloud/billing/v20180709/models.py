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
        """
        :param ActionType: Transaction type\n        :type ActionType: str\n        :param ActionTypeName: Transaction type name\n        :type ActionTypeName: str\n        :param RealTotalCost: Actual cost\n        :type RealTotalCost: str\n        :param RealTotalCostRatio: Cost ratio, to two decimal points\n        :type RealTotalCostRatio: str\n        :param CashPayAmount: Cash amount\n        :type CashPayAmount: str\n        :param IncentivePayAmount: Trial credit amount\n        :type IncentivePayAmount: str\n        :param VoucherPayAmount: Voucher amount\n        :type VoucherPayAmount: str\n        :param BillMonth: Billing month, e.g. `2019-08`\n        :type BillMonth: str\n        """
        self.ActionType = None
        self.ActionTypeName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.BillMonth = None


    def _deserialize(self, params):
        self.ActionType = params.get("ActionType")
        self.ActionTypeName = params.get("ActionTypeName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.BillMonth = params.get("BillMonth")
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
        """
        :param BusinessCodeName: Product name: major categories of Tencent Cloud services, e.g. CVM and TencentDB for MySQL\n        :type BusinessCodeName: str\n        :param ProductCodeName: Sub-product name: sub-categories of Tencent Cloud services, such as CVM-Standard S1\n        :type ProductCodeName: str\n        :param PayModeName: Billing mode\n        :type PayModeName: str\n        :param ProjectName: Project: project of a resource\n        :type ProjectName: str\n        :param RegionName: Region: region of a resource, e.g. South China (Guangzhou)\n        :type RegionName: str\n        :param ZoneName: Availability zone: availability zone of a resource, e.g. Guangzhou Zone 3\n        :type ZoneName: str\n        :param ResourceId: Instance ID\n        :type ResourceId: str\n        :param ResourceName: Instance name\n        :type ResourceName: str\n        :param ActionTypeName: Transaction type\n        :type ActionTypeName: str\n        :param OrderId: Order ID\n        :type OrderId: str\n        :param BillId: Transaction ID\n        :type BillId: str\n        :param PayTime: Payment time\n        :type PayTime: str\n        :param FeeBeginTime: Service start time\n        :type FeeBeginTime: str\n        :param FeeEndTime: Service end time\n        :type FeeEndTime: str\n        :param ComponentSet: Component list\n        :type ComponentSet: list of BillDetailComponent\n        :param PayerUin: Payer's UIN\n        :type PayerUin: str\n        :param OwnerUin: User's UIN\n        :type OwnerUin: str\n        :param OperateUin: Operator's UIN\n        :type OperateUin: str\n        :param Tags: Tag information
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Tags: list of BillTagInfo\n        :param BusinessCode: Product code
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type BusinessCode: str\n        :param ProductCode: Subproduct code
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ProductCode: str\n        :param ActionType: Transaction type/code (optional)\n        :type ActionType: str\n        :param RegionId: \n        :type RegionId: str\n        :param ProjectId: Project ID: ID of the project to which the resource belongs\n        :type ProjectId: int\n        """
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
        """
        :param ComponentCodeName: Component type: type of a resource component, e.g. memory, disk, etc.\n        :type ComponentCodeName: str\n        :param ItemCodeName: Component name: name of a resource component, e.g. TencentDB for MySQL-memory\n        :type ItemCodeName: str\n        :param SinglePrice: Component published price: original price of a resource component with the original granularity\n        :type SinglePrice: str\n        :param SpecifiedPrice: Specified price of the component\n        :type SpecifiedPrice: str\n        :param PriceUnit: Price unit\n        :type PriceUnit: str\n        :param UsedAmount: Component usage\n        :type UsedAmount: str\n        :param UsedAmountUnit: Component usage unit\n        :type UsedAmountUnit: str\n        :param TimeSpan: Usage period\n        :type TimeSpan: str\n        :param TimeUnitName: Time unit\n        :type TimeUnitName: str\n        :param Cost: Original price of the component\n        :type Cost: str\n        :param Discount: Discount rate\n        :type Discount: str\n        :param ReduceType: Offer type\n        :type ReduceType: str\n        :param RealCost: Total discounted price\n        :type RealCost: str\n        :param VoucherPayAmount: Amount paid in voucher\n        :type VoucherPayAmount: str\n        :param CashPayAmount: Amount paid in cash\n        :type CashPayAmount: str\n        :param IncentivePayAmount: Amount paid in trial credit\n        :type IncentivePayAmount: str\n        :param ItemCode: Component type code
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ItemCode: str\n        :param ComponentCode: Component code
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ComponentCode: str\n        :param ContractPrice: Contract price\n        :type ContractPrice: str\n        """
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
        """
        :param BusinessCodeName: Product name: major categories of Tencent Cloud services, e.g. CVM and TencentDB for MySQL\n        :type BusinessCodeName: str\n        :param ProductCodeName: Sub-product name: sub-categories of Tencent Cloud services, such as CVM-Standard S1; if no subproduct name is obtained, '-' is returned.\n        :type ProductCodeName: str\n        :param PayModeName: Billing mode\n        :type PayModeName: str\n        :param ProjectName: Project\n        :type ProjectName: str\n        :param RegionName: Region\n        :type RegionName: str\n        :param ZoneName: Availability zone\n        :type ZoneName: str\n        :param ResourceId: Instance ID\n        :type ResourceId: str\n        :param ResourceName: Resource instance namDeduction timee\n        :type ResourceName: str\n        :param ActionTypeName: Transaction type\n        :type ActionTypeName: str\n        :param OrderId: Order ID\n        :type OrderId: str\n        :param PayTime: Payment time\n        :type PayTime: str\n        :param FeeBeginTime: Service start time\n        :type FeeBeginTime: str\n        :param FeeEndTime: Service end time\n        :type FeeEndTime: str\n        :param ConfigDesc: Configuration description\n        :type ConfigDesc: str\n        :param ExtendField1: Extension field 1\n        :type ExtendField1: str\n        :param ExtendField2: Extension field 2\n        :type ExtendField2: str\n        :param TotalCost: Cost, in USD\n        :type TotalCost: str\n        :param Discount: Discount rate\n        :type Discount: str\n        :param ReduceType: Offer type\n        :type ReduceType: str\n        :param RealTotalCost: Total cost after discount, in USD\n        :type RealTotalCost: str\n        :param VoucherPayAmount: Amount paid in voucher, in USD\n        :type VoucherPayAmount: str\n        :param CashPayAmount: Amount paid in cash, in USD\n        :type CashPayAmount: str\n        :param IncentivePayAmount: Amount paid in trial credit, in USD\n        :type IncentivePayAmount: str\n        :param ExtendField3: Extension field 3\n        :type ExtendField3: str\n        :param ExtendField4: Extension field 4\n        :type ExtendField4: str\n        :param ExtendField5: Extension field 5\n        :type ExtendField5: str\n        :param Tags: Tag information
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Tags: list of BillTagInfo\n        :param PayerUin: Payer UIN\n        :type PayerUin: str\n        :param OwnerUin: Resource owner UIN; '-' is returned if no value is obtained\n        :type OwnerUin: str\n        :param OperateUin: Operator UIN; '-' is returned if no value is obtained\n        :type OperateUin: str\n        :param BusinessCode: \n        :type BusinessCode: str\n        :param ProductCode: \n        :type ProductCode: str\n        :param RegionId: \n        :type RegionId: int\n        """
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
        """
        :param TagKey: Cost allocation tag key\n        :type TagKey: str\n        :param TagValue: Tag value\n        :type TagValue: str\n        """
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
        """
        :param BusinessCode: Product code
Note: This field may return null, indicating that no valid value was found.\n        :type BusinessCode: str\n        :param BusinessCodeName: Product name: major categories of Tencent Cloud services, e.g. CVM and TencentDB for MySQL\n        :type BusinessCodeName: str\n        :param RealTotalCost: Actual cost\n        :type RealTotalCost: str\n        :param RealTotalCostRatio: Cost ratio, to two decimal points\n        :type RealTotalCostRatio: str\n        :param CashPayAmount: Cash amount\n        :type CashPayAmount: str\n        :param IncentivePayAmount: Trial credit amount\n        :type IncentivePayAmount: str\n        :param VoucherPayAmount: Voucher amount\n        :type VoucherPayAmount: str\n        :param BillMonth: Billing month, e.g. `2019-08`\n        :type BillMonth: str\n        """
        self.BusinessCode = None
        self.BusinessCodeName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.BillMonth = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.BillMonth = params.get("BillMonth")
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
        """
        :param RealTotalCost: Total cost\n        :type RealTotalCost: str\n        :param VoucherPayAmount: Voucher amount\n        :type VoucherPayAmount: str\n        :param IncentivePayAmount: Trial credit amount\n        :type IncentivePayAmount: str\n        :param CashPayAmount: Cash amount\n        :type CashPayAmount: str\n        """
        self.RealTotalCost = None
        self.VoucherPayAmount = None
        self.IncentivePayAmount = None
        self.CashPayAmount = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.CashPayAmount = params.get("CashPayAmount")
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
        """
        :param Offset: Offset\n        :type Offset: int\n        :param Limit: Quantity, maximum is 100\n        :type Limit: int\n        :param PeriodType: The period type. byUsedTime: By usage period; byPayTime: By payment period. Must be the same as the period of the current monthly bill of the Billing Center. You can check your bill statistics period type at the top of the [Bill Overview](https://console.cloud.tencent.com/expense/bill/overview) page. \n        :type PeriodType: str\n        :param Month: Month; format: yyyy-mm. You only have to enter either Month or BeginTime and EndTime. When you enter values for BeginTime and EndTime, Month becomes invalid. This value must be no earlier than the month when Bill 2.0 is activated; last 24 months data are available.\n        :type Month: str\n        :param BeginTime: The start time of the period; format: Y-m-d H:i:s. You only have to enter either Month or BeginTime and EndTime. When you enter values for BeginTime and EndTime, Month becomes invalid. BeginTime and EndTime must be inputted as a pair. This value must be no earlier than the month when Bill 2.0 is activated; last 24 months data are available.\n        :type BeginTime: str\n        :param EndTime: The end time of the period; format: Y-m-d H:i:s. You only have to enter either Month or BeginTime and EndTime. When you enter values for BeginTime and EndTime, Month becomes invalid. BeginTime and EndTime must be inputted as a pair. This value must be no earlier than the month when Bill 2.0 is activated; last 24 months data are available.\n        :type EndTime: str\n        :param NeedRecordNum: Indicates whether or not the total number of records of accessing the list is required, used for frontend pages.
1 = yes, 0 = no\n        :type NeedRecordNum: int\n        :param ProductCode: Queries information on a specified product\n        :type ProductCode: str\n        :param PayMode: Billing mode: prePay/postPay\n        :type PayMode: str\n        :param ResourceId: Queries information on a specified resource\n        :type ResourceId: str\n        :param ActionType: \n        :type ActionType: str\n        :param ProjectId: Project ID: ID of the project to which the resource belongs\n        :type ProjectId: int\n        """
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
        """
        :param DetailSet: Details list\n        :type DetailSet: list of BillDetail\n        :param Total: Total number of records
Note: This field may return null, indicating that no valid value was found.\n        :type Total: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Offset: Offset\n        :type Offset: int\n        :param Limit: Quantity, maximum is 1000\n        :type Limit: int\n        :param PeriodType: The period type. byUsedTime: By usage period; byPayTime: by payment period. Must be the same as the period of the current monthly bill of the Billing Center. You can check your bill statistics period type at the top of the [Bill Overview](https://console.cloud.tencent.com/expense/bill/overview) page.\n        :type PeriodType: str\n        :param Month: Month; format: yyyy-mm. This value cannot be earlier than the month when Bill 2.0 is enabled. Last 24 months data are available.\n        :type Month: str\n        :param NeedRecordNum: Indicates whether or not the total number of records of accessing the list is required, used for frontend pages.
1 = yes, 0 = no\n        :type NeedRecordNum: int\n        :param ActionType: \n        :type ActionType: str\n        :param ResourceId: ID of the instance to be queried\n        :type ResourceId: str\n        :param PayMode: Billing mode. Valid values: `prePay` (prepaid), `postPay` (postpaid)\n        :type PayMode: str\n        """
        self.Offset = None
        self.Limit = None
        self.PeriodType = None
        self.Month = None
        self.NeedRecordNum = None
        self.ActionType = None
        self.ResourceId = None
        self.PayMode = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PeriodType = params.get("PeriodType")
        self.Month = params.get("Month")
        self.NeedRecordNum = params.get("NeedRecordNum")
        self.ActionType = params.get("ActionType")
        self.ResourceId = params.get("ResourceId")
        self.PayMode = params.get("PayMode")
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
        """
        :param ResourceSummarySet: Resource summary list\n        :type ResourceSummarySet: list of BillResourceSummary\n        :param Total: Total number of resource summary lists
Note: This field may return null, indicating that no valid value was found.\n        :type Total: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param BeginTime: The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.\n        :type BeginTime: str\n        :param EndTime: The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.\n        :type EndTime: str\n        :param PayerUin: Query bill data user's UIN\n        :type PayerUin: str\n        """
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
        """
        :param Ready: Indicates whether or not the data is ready. 0 = not ready, 1 = ready.\n        :type Ready: int\n        :param SummaryOverview: Detailed cost distribution for all billing modes
Note: This field may return null, indicating that no valid value was found.\n        :type SummaryOverview: list of PayModeSummaryOverviewItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param BeginTime: The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.\n        :type BeginTime: str\n        :param EndTime: The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.\n        :type EndTime: str\n        :param PayerUin: Queries bill data user's UIN\n        :type PayerUin: str\n        """
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
        


class DescribeBillSummaryByProductResponse(AbstractModel):
    """DescribeBillSummaryByProduct response structure.

    """

    def __init__(self):
        """
        :param Ready: Indicates whether or not the data is ready. 0 = not ready, 1 = ready.\n        :type Ready: int\n        :param SummaryTotal: Total cost details
Note: This field may return null, indicating that no valid value was found.\n        :type SummaryTotal: :class:`tencentcloud.billing.v20180709.models.BusinessSummaryTotal`\n        :param SummaryOverview: Cost distribution of all products
Note: This field may return null, indicating that no valid value was found.\n        :type SummaryOverview: list of BusinessSummaryOverviewItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param BeginTime: The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.\n        :type BeginTime: str\n        :param EndTime: The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.\n        :type EndTime: str\n        :param PayerUin: Queries bill data user's UIN\n        :type PayerUin: str\n        """
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
        """
        :param Ready: Indicates whether or not the data is ready. 0 = not ready, 1 = ready.\n        :type Ready: int\n        :param SummaryOverview: Detailed cost distribution for all projects
Note: This field may return null, indicating that no valid value was found.\n        :type SummaryOverview: list of ProjectSummaryOverviewItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param BeginTime: The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.\n        :type BeginTime: str\n        :param EndTime: The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.\n        :type EndTime: str\n        :param PayerUin: Queries bill data user's UIN\n        :type PayerUin: str\n        """
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
        """
        :param Ready: Indicates whether or not the data is ready. 0 = not ready, 1 = ready.\n        :type Ready: int\n        :param SummaryOverview: Detailed cost distribution for all regions
Note: This field may return null, indicating that no valid value was found.\n        :type SummaryOverview: list of RegionSummaryOverviewItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param BeginTime: The value must be of the same month as `EndTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.\n        :type BeginTime: str\n        :param EndTime: The value must be of the same month as `BeginTime`. Query period must start and end on the same month and the query result returned will be of the entire month. For example, if both `BeginTime` and `EndTime` are `2018-09`, the data returned will be for the entire month of September 2018.\n        :type EndTime: str\n        :param TagKey: Cost allocation tag key\n        :type TagKey: str\n        :param PayerUin: Payer UIN\n        :type PayerUin: str\n        """
        self.BeginTime = None
        self.EndTime = None
        self.TagKey = None
        self.PayerUin = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.TagKey = params.get("TagKey")
        self.PayerUin = params.get("PayerUin")
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
        """
        :param Ready: Indicates whether or not the data is ready. `0`: not ready; `1`: ready.\n        :type Ready: int\n        :param SummaryOverview: Details about cost distribution over different tags
Note: This field may return null, indicating that no valid values can be obtained.\n        :type SummaryOverview: list of TagSummaryOverviewItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Ready = None
        self.SummaryOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self.SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = TagSummaryOverviewItem()
                obj._deserialize(item)
                self.SummaryOverview.append(obj)
        self.RequestId = params.get("RequestId")


class PayModeSummaryOverviewItem(AbstractModel):
    """Detailed summary of purchases by billing mode

    """

    def __init__(self):
        """
        :param PayMode: Billing mode\n        :type PayMode: str\n        :param PayModeName: Billing mode name\n        :type PayModeName: str\n        :param RealTotalCost: Actual cost\n        :type RealTotalCost: str\n        :param RealTotalCostRatio: Cost ratio, to two decimal points\n        :type RealTotalCostRatio: str\n        :param Detail: Detailed summary of purchases by transaction type\n        :type Detail: list of ActionSummaryOverviewItem\n        :param CashPayAmount: Cash amount\n        :type CashPayAmount: str\n        :param IncentivePayAmount: Trial credit amount\n        :type IncentivePayAmount: str\n        :param VoucherPayAmount: Voucher amount\n        :type VoucherPayAmount: str\n        """
        self.PayMode = None
        self.PayModeName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.Detail = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None


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
        """
        :param ProjectId: Project ID\n        :type ProjectId: str\n        :param ProjectName: Project name\n        :type ProjectName: str\n        :param RealTotalCost: Actual cost\n        :type RealTotalCost: str\n        :param RealTotalCostRatio: Cost ratio, to two decimal points\n        :type RealTotalCostRatio: str\n        :param CashPayAmount: Cash amount\n        :type CashPayAmount: str\n        :param IncentivePayAmount: Trial credit amount\n        :type IncentivePayAmount: str\n        :param VoucherPayAmount: Voucher amount\n        :type VoucherPayAmount: str\n        :param BillMonth: Billing month, e.g. `2019-08`\n        :type BillMonth: str\n        """
        self.ProjectId = None
        self.ProjectName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.BillMonth = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.BillMonth = params.get("BillMonth")
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
        """
        :param RegionId: Region ID
Note: This field may return null, indicating that no valid value was found.\n        :type RegionId: str\n        :param RegionName: Region name\n        :type RegionName: str\n        :param RealTotalCost: Actual cost\n        :type RealTotalCost: str\n        :param RealTotalCostRatio: Cost ratio, to two decimal points\n        :type RealTotalCostRatio: str\n        :param CashPayAmount: Cash amount\n        :type CashPayAmount: str\n        :param IncentivePayAmount: Trial credit amount\n        :type IncentivePayAmount: str\n        :param VoucherPayAmount: Voucher amount\n        :type VoucherPayAmount: str\n        :param BillMonth: Billing month, e.g. `2019-08`\n        :type BillMonth: str\n        """
        self.RegionId = None
        self.RegionName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.BillMonth = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.BillMonth = params.get("BillMonth")
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
        """
        :param TagValue: Tag value
Note: This field may return null, indicating that no valid values can be obtained.\n        :type TagValue: str\n        :param RealTotalCost: Actual cost
Note: This field may return null, indicating that no valid values can be obtained.\n        :type RealTotalCost: str\n        :param RealTotalCostRatio: Cost percentage rounded to two decimal places
Note: This field may return null, indicating that no valid values can be obtained.\n        :type RealTotalCostRatio: str\n        """
        self.TagValue = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None


    def _deserialize(self, params):
        self.TagValue = params.get("TagValue")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        