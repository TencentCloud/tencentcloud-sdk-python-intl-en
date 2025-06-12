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
        :param _ActionType: Transaction type code.
        :type ActionType: str
        :param _ActionTypeName: Transaction type name.
        :type ActionTypeName: str
        :param _OriginalCost: Actual total consumption, up to 8 decimal places.
        :type OriginalCost: str
        :param _VoucherPayAmount: Voucher payment amount, up to 8 decimal places.
        :type VoucherPayAmount: str
        :param _TotalCost: Total consumption, up to 8 decimal places.
        :type TotalCost: str
        """
        self._ActionType = None
        self._ActionTypeName = None
        self._OriginalCost = None
        self._VoucherPayAmount = None
        self._TotalCost = None

    @property
    def ActionType(self):
        """Transaction type code.
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        """Transaction type name.
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OriginalCost(self):
        """Actual total consumption, up to 8 decimal places.
        :rtype: str
        """
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def VoucherPayAmount(self):
        """Voucher payment amount, up to 8 decimal places.
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TotalCost(self):
        """Total consumption, up to 8 decimal places.
        :rtype: str
        """
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
        


class AllocateCreditPoolRequest(AbstractModel):
    """AllocateCreditPool request structure.

    """

    def __init__(self):
        r"""
        :param _SubAgentUin: Second-level reseller UIN.
        :type SubAgentUin: int
        :param _Credit: Allocated amount.
        :type Credit: float
        """
        self._SubAgentUin = None
        self._Credit = None

    @property
    def SubAgentUin(self):
        """Second-level reseller UIN.
        :rtype: int
        """
        return self._SubAgentUin

    @SubAgentUin.setter
    def SubAgentUin(self, SubAgentUin):
        self._SubAgentUin = SubAgentUin

    @property
    def Credit(self):
        """Allocated amount.
        :rtype: float
        """
        return self._Credit

    @Credit.setter
    def Credit(self, Credit):
        self._Credit = Credit


    def _deserialize(self, params):
        self._SubAgentUin = params.get("SubAgentUin")
        self._Credit = params.get("Credit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateCreditPoolResponse(AbstractModel):
    """AllocateCreditPool response structure.

    """

    def __init__(self):
        r"""
        :param _RemainingCredit: Current total remaining quota.
        :type RemainingCredit: float
        :param _TotalCredit: Total allocated quota.
        :type TotalCredit: float
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RemainingCredit = None
        self._TotalCredit = None
        self._RequestId = None

    @property
    def RemainingCredit(self):
        """Current total remaining quota.
        :rtype: float
        """
        return self._RemainingCredit

    @RemainingCredit.setter
    def RemainingCredit(self, RemainingCredit):
        self._RemainingCredit = RemainingCredit

    @property
    def TotalCredit(self):
        """Total allocated quota.
        :rtype: float
        """
        return self._TotalCredit

    @TotalCredit.setter
    def TotalCredit(self, TotalCredit):
        self._TotalCredit = TotalCredit

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RemainingCredit = params.get("RemainingCredit")
        self._TotalCredit = params.get("TotalCredit")
        self._RequestId = params.get("RequestId")


class AllocateCustomerCreditRequest(AbstractModel):
    """AllocateCustomerCredit request structure.

    """

    def __init__(self):
        r"""
        :param _AddedCredit: Specific value of the credit allocated to the customer
        :type AddedCredit: float
        :param _ClientUin: Customer UIN
        :type ClientUin: int
        :param _Remark: Remark
        :type Remark: str
        """
        self._AddedCredit = None
        self._ClientUin = None
        self._Remark = None

    @property
    def AddedCredit(self):
        """Specific value of the credit allocated to the customer
        :rtype: float
        """
        return self._AddedCredit

    @AddedCredit.setter
    def AddedCredit(self, AddedCredit):
        self._AddedCredit = AddedCredit

    @property
    def ClientUin(self):
        """Customer UIN
        :rtype: int
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def Remark(self):
        """Remark
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._AddedCredit = params.get("AddedCredit")
        self._ClientUin = params.get("ClientUin")
        self._Remark = params.get("Remark")
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCredit = None
        self._RemainingCredit = None
        self._RequestId = None

    @property
    def TotalCredit(self):
        """The updated total credit
        :rtype: float
        """
        return self._TotalCredit

    @TotalCredit.setter
    def TotalCredit(self, TotalCredit):
        self._TotalCredit = TotalCredit

    @property
    def RemainingCredit(self):
        """The updated available credit
        :rtype: float
        """
        return self._RemainingCredit

    @RemainingCredit.setter
    def RemainingCredit(self, RemainingCredit):
        self._RemainingCredit = RemainingCredit

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCredit = params.get("TotalCredit")
        self._RemainingCredit = params.get("RemainingCredit")
        self._RequestId = params.get("RequestId")


class ApproveClientApplyRequest(AbstractModel):
    """ApproveClientApply request structure.

    """

    def __init__(self):
        r"""
        :param _ClientUin: Sub-customer uin.
        :type ClientUin: int
        :param _ApproveType: Approval type. only supports pass and reject.
        :type ApproveType: str
        :param _RejectReason: Reason for rejection. required only when approvetype is reject.
        :type RejectReason: str
        """
        self._ClientUin = None
        self._ApproveType = None
        self._RejectReason = None

    @property
    def ClientUin(self):
        """Sub-customer uin.
        :rtype: int
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def ApproveType(self):
        """Approval type. only supports pass and reject.
        :rtype: str
        """
        return self._ApproveType

    @ApproveType.setter
    def ApproveType(self, ApproveType):
        self._ApproveType = ApproveType

    @property
    def RejectReason(self):
        """Reason for rejection. required only when approvetype is reject.
        :rtype: str
        """
        return self._RejectReason

    @RejectReason.setter
    def RejectReason(self, RejectReason):
        self._RejectReason = RejectReason


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        self._ApproveType = params.get("ApproveType")
        self._RejectReason = params.get("RejectReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApproveClientApplyResponse(AbstractModel):
    """ApproveClientApply response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ApproveSubAgentApplyRequest(AbstractModel):
    """ApproveSubAgentApply request structure.

    """

    def __init__(self):
        r"""
        :param _SubAgentUin: Second-level reseller UIN.
        :type SubAgentUin: int
        :param _ApproveType: Approval type. Only pass and reject are supported.
        :type ApproveType: str
        :param _RejectReason: Reason for rejection. Fill in only when ApproveType is reject.
        :type RejectReason: str
        """
        self._SubAgentUin = None
        self._ApproveType = None
        self._RejectReason = None

    @property
    def SubAgentUin(self):
        """Second-level reseller UIN.
        :rtype: int
        """
        return self._SubAgentUin

    @SubAgentUin.setter
    def SubAgentUin(self, SubAgentUin):
        self._SubAgentUin = SubAgentUin

    @property
    def ApproveType(self):
        """Approval type. Only pass and reject are supported.
        :rtype: str
        """
        return self._ApproveType

    @ApproveType.setter
    def ApproveType(self, ApproveType):
        self._ApproveType = ApproveType

    @property
    def RejectReason(self):
        """Reason for rejection. Fill in only when ApproveType is reject.
        :rtype: str
        """
        return self._RejectReason

    @RejectReason.setter
    def RejectReason(self, RejectReason):
        self._RejectReason = RejectReason


    def _deserialize(self, params):
        self._SubAgentUin = params.get("SubAgentUin")
        self._ApproveType = params.get("ApproveType")
        self._RejectReason = params.get("RejectReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApproveSubAgentApplyResponse(AbstractModel):
    """ApproveSubAgentApply response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BillDetailData(AbstractModel):
    """Customer bill details

    """

    def __init__(self):
        r"""
        :param _PayerAccountId: reseller account.
        :type PayerAccountId: int
        :param _OwnerAccountId: Subaccount.
        :type OwnerAccountId: int
        :param _OperatorAccountId: Operator account.
        :type OperatorAccountId: int
        :param _ProductName: Product name.
        :type ProductName: str
        :param _BillingMode: Billing mode
.
Monthly subscription (annual and monthly).
Pay-As-You-Go resources.
Standard ri reserved instance.
        :type BillingMode: str
        :param _ProjectName: Project name.
.

        :type ProjectName: str
        :param _Region: Resource region.
        :type Region: str
        :param _AvailabilityZone: Resource available zone.
        :type AvailabilityZone: str
        :param _InstanceId: Instance id.
        :type InstanceId: str
        :param _InstanceName: Instance name.
        :type InstanceName: str
        :param _SubProductName: Sub-Product name
.

        :type SubProductName: str
        :param _TransactionType: Settlement type.
        :type TransactionType: str
        :param _TransactionId: <Transaction id>.
        :type TransactionId: str
        :param _TransactionTime: Settlement time.

        :type TransactionTime: str
        :param _UsageStartTime: <Resource start time>.
        :type UsageStartTime: str
        :param _UsageEndTime: <Resource end usage time>.
        :type UsageEndTime: str
        :param _ComponentType: Component.
        :type ComponentType: str
        :param _ComponentName: Component name.
        :type ComponentName: str
        :param _ComponentListPrice: Component list price.
        :type ComponentListPrice: str
        :param _ComponentPriceMeasurementUnit: Price unit.
        :type ComponentPriceMeasurementUnit: str
        :param _ComponentUsage: Component usage.
        :type ComponentUsage: str
        :param _ComponentUsageUnit: Component usage unit.
        :type ComponentUsageUnit: str
        :param _UsageDuration: Resource usage duration.
        :type UsageDuration: str
        :param _DurationUnit: duration unit.
        :type DurationUnit: str
        :param _OriginalCost: Total original price.
Original cost = component list price * component usage * usage duration.
        :type OriginalCost: str
        :param _DiscountRate: Discount (default is 1).
        :type DiscountRate: str
        :param _Currency: Currency.
        :type Currency: str
        :param _TotalAmountAfterDiscount: Total cost after discount.
        :type TotalAmountAfterDiscount: str
        :param _VoucherDeduction: Voucher deduction amount.
        :type VoucherDeduction: str
        :param _TotalCost: = Total Amount After Discount - Voucher Deduction
        :type TotalCost: str
        :param _Id: Identifier (id).
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
        """reseller account.
        :rtype: int
        """
        return self._PayerAccountId

    @PayerAccountId.setter
    def PayerAccountId(self, PayerAccountId):
        self._PayerAccountId = PayerAccountId

    @property
    def OwnerAccountId(self):
        """Subaccount.
        :rtype: int
        """
        return self._OwnerAccountId

    @OwnerAccountId.setter
    def OwnerAccountId(self, OwnerAccountId):
        self._OwnerAccountId = OwnerAccountId

    @property
    def OperatorAccountId(self):
        """Operator account.
        :rtype: int
        """
        return self._OperatorAccountId

    @OperatorAccountId.setter
    def OperatorAccountId(self, OperatorAccountId):
        self._OperatorAccountId = OperatorAccountId

    @property
    def ProductName(self):
        """Product name.
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def BillingMode(self):
        """Billing mode
.
Monthly subscription (annual and monthly).
Pay-As-You-Go resources.
Standard ri reserved instance.
        :rtype: str
        """
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def ProjectName(self):
        """Project name.
.

        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def Region(self):
        """Resource region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AvailabilityZone(self):
        """Resource available zone.
        :rtype: str
        """
        return self._AvailabilityZone

    @AvailabilityZone.setter
    def AvailabilityZone(self, AvailabilityZone):
        self._AvailabilityZone = AvailabilityZone

    @property
    def InstanceId(self):
        """Instance id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Instance name.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def SubProductName(self):
        """Sub-Product name
.

        :rtype: str
        """
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName

    @property
    def TransactionType(self):
        """Settlement type.
        :rtype: str
        """
        return self._TransactionType

    @TransactionType.setter
    def TransactionType(self, TransactionType):
        self._TransactionType = TransactionType

    @property
    def TransactionId(self):
        """<Transaction id>.
        :rtype: str
        """
        return self._TransactionId

    @TransactionId.setter
    def TransactionId(self, TransactionId):
        self._TransactionId = TransactionId

    @property
    def TransactionTime(self):
        """Settlement time.

        :rtype: str
        """
        return self._TransactionTime

    @TransactionTime.setter
    def TransactionTime(self, TransactionTime):
        self._TransactionTime = TransactionTime

    @property
    def UsageStartTime(self):
        """<Resource start time>.
        :rtype: str
        """
        return self._UsageStartTime

    @UsageStartTime.setter
    def UsageStartTime(self, UsageStartTime):
        self._UsageStartTime = UsageStartTime

    @property
    def UsageEndTime(self):
        """<Resource end usage time>.
        :rtype: str
        """
        return self._UsageEndTime

    @UsageEndTime.setter
    def UsageEndTime(self, UsageEndTime):
        self._UsageEndTime = UsageEndTime

    @property
    def ComponentType(self):
        """Component.
        :rtype: str
        """
        return self._ComponentType

    @ComponentType.setter
    def ComponentType(self, ComponentType):
        self._ComponentType = ComponentType

    @property
    def ComponentName(self):
        """Component name.
        :rtype: str
        """
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def ComponentListPrice(self):
        """Component list price.
        :rtype: str
        """
        return self._ComponentListPrice

    @ComponentListPrice.setter
    def ComponentListPrice(self, ComponentListPrice):
        self._ComponentListPrice = ComponentListPrice

    @property
    def ComponentPriceMeasurementUnit(self):
        """Price unit.
        :rtype: str
        """
        return self._ComponentPriceMeasurementUnit

    @ComponentPriceMeasurementUnit.setter
    def ComponentPriceMeasurementUnit(self, ComponentPriceMeasurementUnit):
        self._ComponentPriceMeasurementUnit = ComponentPriceMeasurementUnit

    @property
    def ComponentUsage(self):
        """Component usage.
        :rtype: str
        """
        return self._ComponentUsage

    @ComponentUsage.setter
    def ComponentUsage(self, ComponentUsage):
        self._ComponentUsage = ComponentUsage

    @property
    def ComponentUsageUnit(self):
        """Component usage unit.
        :rtype: str
        """
        return self._ComponentUsageUnit

    @ComponentUsageUnit.setter
    def ComponentUsageUnit(self, ComponentUsageUnit):
        self._ComponentUsageUnit = ComponentUsageUnit

    @property
    def UsageDuration(self):
        """Resource usage duration.
        :rtype: str
        """
        return self._UsageDuration

    @UsageDuration.setter
    def UsageDuration(self, UsageDuration):
        self._UsageDuration = UsageDuration

    @property
    def DurationUnit(self):
        """duration unit.
        :rtype: str
        """
        return self._DurationUnit

    @DurationUnit.setter
    def DurationUnit(self, DurationUnit):
        self._DurationUnit = DurationUnit

    @property
    def OriginalCost(self):
        """Total original price.
Original cost = component list price * component usage * usage duration.
        :rtype: str
        """
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountRate(self):
        """Discount (default is 1).
        :rtype: str
        """
        return self._DiscountRate

    @DiscountRate.setter
    def DiscountRate(self, DiscountRate):
        self._DiscountRate = DiscountRate

    @property
    def Currency(self):
        """Currency.
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def TotalAmountAfterDiscount(self):
        """Total cost after discount.
        :rtype: str
        """
        return self._TotalAmountAfterDiscount

    @TotalAmountAfterDiscount.setter
    def TotalAmountAfterDiscount(self, TotalAmountAfterDiscount):
        self._TotalAmountAfterDiscount = TotalAmountAfterDiscount

    @property
    def VoucherDeduction(self):
        """Voucher deduction amount.
        :rtype: str
        """
        return self._VoucherDeduction

    @VoucherDeduction.setter
    def VoucherDeduction(self, VoucherDeduction):
        self._VoucherDeduction = VoucherDeduction

    @property
    def TotalCost(self):
        """= Total Amount After Discount - Voucher Deduction
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Id(self):
        """Identifier (id).
        :rtype: str
        """
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
        :param _BusinessCodeName: Product name.
        :type BusinessCodeName: str
        :param _BusinessCode: Product code.
        :type BusinessCode: str
        :param _OriginalCost: Original price.
        :type OriginalCost: str
        :param _VoucherPayAmount: Voucher amount.
        :type VoucherPayAmount: str
        :param _RICost: RI deduction.
        :type RICost: str
        :param _TotalCost: Total amount.
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
        """Product name.
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def BusinessCode(self):
        """Product code.
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def OriginalCost(self):
        """Original price.
        :rtype: str
        """
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def VoucherPayAmount(self):
        """Voucher amount.
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def RICost(self):
        """RI deduction.
        :rtype: str
        """
        return self._RICost

    @RICost.setter
    def RICost(self, RICost):
        self._RICost = RICost

    @property
    def TotalCost(self):
        """Total amount.
        :rtype: str
        """
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
        :param _BusinessCode: Product code.
        :type BusinessCode: str
        :param _BusinessCodeName: Product name.
        :type BusinessCodeName: str
        :param _OriginalCost: List price, keep 8 decimal places.
        :type OriginalCost: str
        :param _VoucherPayAmount: Voucher payment amount, keep 8 decimal places.
        :type VoucherPayAmount: str
        :param _TotalCost: Consumption amount, keep 8 decimal places.
        :type TotalCost: str
        """
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._OriginalCost = None
        self._VoucherPayAmount = None
        self._TotalCost = None

    @property
    def BusinessCode(self):
        """Product code.
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        """Product name.
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def OriginalCost(self):
        """List price, keep 8 decimal places.
        :rtype: str
        """
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def VoucherPayAmount(self):
        """Voucher payment amount, keep 8 decimal places.
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TotalCost(self):
        """Consumption amount, keep 8 decimal places.
        :rtype: str
        """
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
        """Country/region name in English
        :rtype: str
        """
        return self._EnName

    @EnName.setter
    def EnName(self, EnName):
        self._EnName = EnName

    @property
    def Name(self):
        """Country/region name in Chinese
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IOS2(self):
        """
        :rtype: str
        """
        return self._IOS2

    @IOS2.setter
    def IOS2(self, IOS2):
        self._IOS2 = IOS2

    @property
    def IOS3(self):
        """
        :rtype: str
        """
        return self._IOS3

    @IOS3.setter
    def IOS3(self, IOS3):
        self._IOS3 = IOS3

    @property
    def Code(self):
        """International dialing code
        :rtype: str
        """
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
        :param _AccountType: Account type of a new customer.
Valid values: `personal`, `company`.
        :type AccountType: str
        :param _Mail: Registered email address, which should be valid and correct.
such as "account@qq.com"
        :type Mail: str
        :param _Password: Account password.
Length limit: 8-20 characters
A password must contain numbers, letters, and symbols (!@#$%^&*()). Space is not allowed.
        :type Password: str
        :param _ConfirmPassword: The confirmed password, which must be the same as that entered in the `Password` field.
        :type ConfirmPassword: str
        :param _PhoneNum: Customer's mobile number.
The caller needs to ensure the validity and correctness of the mobile number. A global mobile number within a range of 1-32 digits is allowed.
The system will perform binding limit verification of the mobile number you provide, allowing a maximum of 5 accounts per mobile number.
        :type PhoneNum: str
        :param _CountryCode: Customer's country/region code, which can be obtained via the  [GetCountryCodes API](https://www.tencentcloud.com/document/product/1085/51416), such as "852".
Parameter value is not allowed to be 7,380,86.
        :type CountryCode: str
        :param _Area: Customer's ISO2 standard country/region code, which can be obtained via the [GetCountryCodes API](https://www.tencentcloud.com/document/product/1085/51416). It should correspond to the `CountryCode` field, such as `HK`.
        :type Area: str
        :param _VerifyCode: VerifyCode. This parameter is required. 
Use the [SendVerifyCode API](https://www.tencentcloud.com/document/product/1085/65907) to obtain the verifycode.The SendVerifyCode API sends a 6-digit verifycode to your specified mobile number via SMS. After receiving it, you need to pass it along with other parameters.
        :type VerifyCode: str
        :param _Extended: Extension field, which is left empty by default.
        :type Extended: str
        :param _TradeOne: Layer-1 industry id. This is a required item and can be obtained via the [ GetTradeConfigList  API](https://www.tencentcloud.com/zh/document/product/1085/68181),
such as "kghy_01".
        :type TradeOne: str
        :param _TradeTwo: Layer-2 industry id. This is a required item and can be obtained via the [ GetTradeConfigList API](https://www.tencentcloud.com/zh/document/product/1085/68181),
such as "kghy_0101"
        :type TradeTwo: str
        """
        self._AccountType = None
        self._Mail = None
        self._Password = None
        self._ConfirmPassword = None
        self._PhoneNum = None
        self._CountryCode = None
        self._Area = None
        self._VerifyCode = None
        self._Extended = None
        self._TradeOne = None
        self._TradeTwo = None

    @property
    def AccountType(self):
        """Account type of a new customer.
Valid values: `personal`, `company`.
        :rtype: str
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Mail(self):
        """Registered email address, which should be valid and correct.
such as "account@qq.com"
        :rtype: str
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def Password(self):
        """Account password.
Length limit: 8-20 characters
A password must contain numbers, letters, and symbols (!@#$%^&*()). Space is not allowed.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ConfirmPassword(self):
        """The confirmed password, which must be the same as that entered in the `Password` field.
        :rtype: str
        """
        return self._ConfirmPassword

    @ConfirmPassword.setter
    def ConfirmPassword(self, ConfirmPassword):
        self._ConfirmPassword = ConfirmPassword

    @property
    def PhoneNum(self):
        """Customer's mobile number.
The caller needs to ensure the validity and correctness of the mobile number. A global mobile number within a range of 1-32 digits is allowed.
The system will perform binding limit verification of the mobile number you provide, allowing a maximum of 5 accounts per mobile number.
        :rtype: str
        """
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def CountryCode(self):
        """Customer's country/region code, which can be obtained via the  [GetCountryCodes API](https://www.tencentcloud.com/document/product/1085/51416), such as "852".
Parameter value is not allowed to be 7,380,86.
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def Area(self):
        """Customer's ISO2 standard country/region code, which can be obtained via the [GetCountryCodes API](https://www.tencentcloud.com/document/product/1085/51416). It should correspond to the `CountryCode` field, such as `HK`.
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VerifyCode(self):
        """VerifyCode. This parameter is required. 
Use the [SendVerifyCode API](https://www.tencentcloud.com/document/product/1085/65907) to obtain the verifycode.The SendVerifyCode API sends a 6-digit verifycode to your specified mobile number via SMS. After receiving it, you need to pass it along with other parameters.
        :rtype: str
        """
        return self._VerifyCode

    @VerifyCode.setter
    def VerifyCode(self, VerifyCode):
        self._VerifyCode = VerifyCode

    @property
    def Extended(self):
        """Extension field, which is left empty by default.
        :rtype: str
        """
        return self._Extended

    @Extended.setter
    def Extended(self, Extended):
        self._Extended = Extended

    @property
    def TradeOne(self):
        """Layer-1 industry id. This is a required item and can be obtained via the [ GetTradeConfigList  API](https://www.tencentcloud.com/zh/document/product/1085/68181),
such as "kghy_01".
        :rtype: str
        """
        return self._TradeOne

    @TradeOne.setter
    def TradeOne(self, TradeOne):
        self._TradeOne = TradeOne

    @property
    def TradeTwo(self):
        """Layer-2 industry id. This is a required item and can be obtained via the [ GetTradeConfigList API](https://www.tencentcloud.com/zh/document/product/1085/68181),
such as "kghy_0101"
        :rtype: str
        """
        return self._TradeTwo

    @TradeTwo.setter
    def TradeTwo(self, TradeTwo):
        self._TradeTwo = TradeTwo


    def _deserialize(self, params):
        self._AccountType = params.get("AccountType")
        self._Mail = params.get("Mail")
        self._Password = params.get("Password")
        self._ConfirmPassword = params.get("ConfirmPassword")
        self._PhoneNum = params.get("PhoneNum")
        self._CountryCode = params.get("CountryCode")
        self._Area = params.get("Area")
        self._VerifyCode = params.get("VerifyCode")
        self._Extended = params.get("Extended")
        self._TradeOne = params.get("TradeOne")
        self._TradeTwo = params.get("TradeTwo")
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Uin = None
        self._RequestId = None

    @property
    def Uin(self):
        """Account UIN
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._RequestId = params.get("RequestId")


class CreateAndSendClientInvitationMailRequest(AbstractModel):
    """CreateAndSendClientInvitationMail request structure.

    """

    def __init__(self):
        r"""
        :param _Email: Email address that receives the customer invitation link.
        :type Email: str
        :param _InvitationRole: Invite a role.
Note: if no value is passed, it defaults to the sub - customer.
Client: customer.
SubAgent: second-level reseller.
        :type InvitationRole: str
        :param _MaterialUrl: Specifies the application material.
Note: this field takes effect only in the scenario of inviting a second-level reseller.
        :type MaterialUrl: str
        """
        self._Email = None
        self._InvitationRole = None
        self._MaterialUrl = None

    @property
    def Email(self):
        """Email address that receives the customer invitation link.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def InvitationRole(self):
        """Invite a role.
Note: if no value is passed, it defaults to the sub - customer.
Client: customer.
SubAgent: second-level reseller.
        :rtype: str
        """
        return self._InvitationRole

    @InvitationRole.setter
    def InvitationRole(self, InvitationRole):
        self._InvitationRole = InvitationRole

    @property
    def MaterialUrl(self):
        """Specifies the application material.
Note: this field takes effect only in the scenario of inviting a second-level reseller.
        :rtype: str
        """
        return self._MaterialUrl

    @MaterialUrl.setter
    def MaterialUrl(self, MaterialUrl):
        self._MaterialUrl = MaterialUrl


    def _deserialize(self, params):
        self._Email = params.get("Email")
        self._InvitationRole = params.get("InvitationRole")
        self._MaterialUrl = params.get("MaterialUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAndSendClientInvitationMailResponse(AbstractModel):
    """CreateAndSendClientInvitationMail response structure.

    """

    def __init__(self):
        r"""
        :param _InvitationLink: Specifies the invitation link for the customer.
        :type InvitationLink: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InvitationLink = None
        self._RequestId = None

    @property
    def InvitationLink(self):
        """Specifies the invitation link for the customer.
        :rtype: str
        """
        return self._InvitationLink

    @InvitationLink.setter
    def InvitationLink(self, InvitationLink):
        self._InvitationLink = InvitationLink

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InvitationLink = params.get("InvitationLink")
        self._RequestId = params.get("RequestId")


class CustomerBillDetailData(AbstractModel):
    """Customer bill details

    """

    def __init__(self):
        r"""
        :param _PayerAccountId: Distributor account.
        :type PayerAccountId: int
        :param _OwnerAccountId: Sub-Customer account.
        :type OwnerAccountId: int
        :param _OperatorAccountId: Operator account.
        :type OperatorAccountId: int
        :param _ProductName: Product name.
        :type ProductName: str
        :param _BillingMode: Billing mode
.
Monthly subscription.
Pay-As-You-Go resources.
Standard ri reserved instances.
        :type BillingMode: str
        :param _ProjectName: Project name.
.

        :type ProjectName: str
        :param _Region: Resource region.
        :type Region: str
        :param _AvailabilityZone: Resource availability zone.
        :type AvailabilityZone: str
        :param _InstanceId: Instance id.
        :type InstanceId: str
        :param _InstanceName: Instance name.
        :type InstanceName: str
        :param _SubProductName: Sub-Product name
.

        :type SubProductName: str
        :param _TransactionType: Settlement type.
        :type TransactionType: str
        :param _TransactionId: Transaction flow id.
        :type TransactionId: str
        :param _TransactionTime: Settlement time.

        :type TransactionTime: str
        :param _UsageStartTime: Resource start time.
        :type UsageStartTime: str
        :param _UsageEndTime: Resource end time.
        :type UsageEndTime: str
        :param _ComponentType: Component.
        :type ComponentType: str
        :param _ComponentName: Component name.
        :type ComponentName: str
        :param _ComponentListPrice: Component list price.
        :type ComponentListPrice: str
        :param _ComponentPriceMeasurementUnit: Price unit.
        :type ComponentPriceMeasurementUnit: str
        :param _ComponentUsage: Component usage.
        :type ComponentUsage: str
        :param _ComponentUsageUnit: Component usage unit.
        :type ComponentUsageUnit: str
        :param _UsageDuration: Resource usage duration.
        :type UsageDuration: str
        :param _DurationUnit: duration unit.
        :type DurationUnit: str
        :param _OriginalCost: Total original price.
Original cost = component list price * component usage * usage duration.
        :type OriginalCost: str
        :param _Currency: Currency.
        :type Currency: str
        :param _TotalCost: = Total Amount After Discount - Voucher Deduction
        :type TotalCost: str
        :param _Id: Id identifier.
        :type Id: str
        :param _Tags: Tag information.
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
        """Distributor account.
        :rtype: int
        """
        return self._PayerAccountId

    @PayerAccountId.setter
    def PayerAccountId(self, PayerAccountId):
        self._PayerAccountId = PayerAccountId

    @property
    def OwnerAccountId(self):
        """Sub-Customer account.
        :rtype: int
        """
        return self._OwnerAccountId

    @OwnerAccountId.setter
    def OwnerAccountId(self, OwnerAccountId):
        self._OwnerAccountId = OwnerAccountId

    @property
    def OperatorAccountId(self):
        """Operator account.
        :rtype: int
        """
        return self._OperatorAccountId

    @OperatorAccountId.setter
    def OperatorAccountId(self, OperatorAccountId):
        self._OperatorAccountId = OperatorAccountId

    @property
    def ProductName(self):
        """Product name.
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def BillingMode(self):
        """Billing mode
.
Monthly subscription.
Pay-As-You-Go resources.
Standard ri reserved instances.
        :rtype: str
        """
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def ProjectName(self):
        """Project name.
.

        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def Region(self):
        """Resource region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AvailabilityZone(self):
        """Resource availability zone.
        :rtype: str
        """
        return self._AvailabilityZone

    @AvailabilityZone.setter
    def AvailabilityZone(self, AvailabilityZone):
        self._AvailabilityZone = AvailabilityZone

    @property
    def InstanceId(self):
        """Instance id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Instance name.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def SubProductName(self):
        """Sub-Product name
.

        :rtype: str
        """
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName

    @property
    def TransactionType(self):
        """Settlement type.
        :rtype: str
        """
        return self._TransactionType

    @TransactionType.setter
    def TransactionType(self, TransactionType):
        self._TransactionType = TransactionType

    @property
    def TransactionId(self):
        """Transaction flow id.
        :rtype: str
        """
        return self._TransactionId

    @TransactionId.setter
    def TransactionId(self, TransactionId):
        self._TransactionId = TransactionId

    @property
    def TransactionTime(self):
        """Settlement time.

        :rtype: str
        """
        return self._TransactionTime

    @TransactionTime.setter
    def TransactionTime(self, TransactionTime):
        self._TransactionTime = TransactionTime

    @property
    def UsageStartTime(self):
        """Resource start time.
        :rtype: str
        """
        return self._UsageStartTime

    @UsageStartTime.setter
    def UsageStartTime(self, UsageStartTime):
        self._UsageStartTime = UsageStartTime

    @property
    def UsageEndTime(self):
        """Resource end time.
        :rtype: str
        """
        return self._UsageEndTime

    @UsageEndTime.setter
    def UsageEndTime(self, UsageEndTime):
        self._UsageEndTime = UsageEndTime

    @property
    def ComponentType(self):
        """Component.
        :rtype: str
        """
        return self._ComponentType

    @ComponentType.setter
    def ComponentType(self, ComponentType):
        self._ComponentType = ComponentType

    @property
    def ComponentName(self):
        """Component name.
        :rtype: str
        """
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def ComponentListPrice(self):
        """Component list price.
        :rtype: str
        """
        return self._ComponentListPrice

    @ComponentListPrice.setter
    def ComponentListPrice(self, ComponentListPrice):
        self._ComponentListPrice = ComponentListPrice

    @property
    def ComponentPriceMeasurementUnit(self):
        """Price unit.
        :rtype: str
        """
        return self._ComponentPriceMeasurementUnit

    @ComponentPriceMeasurementUnit.setter
    def ComponentPriceMeasurementUnit(self, ComponentPriceMeasurementUnit):
        self._ComponentPriceMeasurementUnit = ComponentPriceMeasurementUnit

    @property
    def ComponentUsage(self):
        """Component usage.
        :rtype: str
        """
        return self._ComponentUsage

    @ComponentUsage.setter
    def ComponentUsage(self, ComponentUsage):
        self._ComponentUsage = ComponentUsage

    @property
    def ComponentUsageUnit(self):
        """Component usage unit.
        :rtype: str
        """
        return self._ComponentUsageUnit

    @ComponentUsageUnit.setter
    def ComponentUsageUnit(self, ComponentUsageUnit):
        self._ComponentUsageUnit = ComponentUsageUnit

    @property
    def UsageDuration(self):
        """Resource usage duration.
        :rtype: str
        """
        return self._UsageDuration

    @UsageDuration.setter
    def UsageDuration(self, UsageDuration):
        self._UsageDuration = UsageDuration

    @property
    def DurationUnit(self):
        """duration unit.
        :rtype: str
        """
        return self._DurationUnit

    @DurationUnit.setter
    def DurationUnit(self, DurationUnit):
        self._DurationUnit = DurationUnit

    @property
    def OriginalCost(self):
        """Total original price.
Original cost = component list price * component usage * usage duration.
        :rtype: str
        """
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def Currency(self):
        """Currency.
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def TotalCost(self):
        """= Total Amount After Discount - Voucher Deduction
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Id(self):
        """Id identifier.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Tags(self):
        """Tag information.
        :rtype: list of TagInfo
        """
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
        :param _Month: Inquiry month, in the format of YYYY-MM, such as 2023-01
        :type Month: str
        :param _PageSize: Page parameter: number of entries per page. Value range: [1, 200]
        :type PageSize: int
        :param _Page: Page parameter: current page number. The minimum value is 1.
        :type Page: int
        :param _PayMode: Billing mode. Valid values: prePay (Monthly subscription) and postPay (Pay-As-You-Go resources)
        :type PayMode: str
        :param _ActionType: Transaction type. Valid values: prepay_purchase (Purchase), prepay_renew (Renewal), prepay_modify (Upgrade/Downgrade), prepay_return ( Monthly subscription refund), postpay_deduct (Pay-as-you-go), postpay_deduct_h (Hourly settlement), postpay_deduct_d (Daily settlement), postpay_deduct_m (Monthly settlement), offline_deduct (Offline project deduction), online_deduct (Offline product deduction), recon_deduct (Adjustment - deduction), recon_increase (Adjustment - compensation), ripay_purchase (One-off RI Fee), postpay_deduct_s (Spot), ri_hour_pay (Hourly RI fee), prePurchase (New monthly subscription), preRenew (Monthly subscription renewal), preUpgrade (Upgrade/Downgrade), preDowngrade (Upgrade/Downgrade), svp_hour_pay (Hourly Savings Plan fee), recon_guarantee (Minimum spend deduction), pre_purchase (New monthly subscription), pre_renew (Monthly subscription renewal), pre_upgrade (Upgrade/Downgrade), pre_downgrade (Upgrade/Downgrade)
        :type ActionType: str
        """
        self._Month = None
        self._PageSize = None
        self._Page = None
        self._PayMode = None
        self._ActionType = None

    @property
    def Month(self):
        """Inquiry month, in the format of YYYY-MM, such as 2023-01
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PageSize(self):
        """Page parameter: number of entries per page. Value range: [1, 200]
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Page(self):
        """Page parameter: current page number. The minimum value is 1.
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PayMode(self):
        """Billing mode. Valid values: prePay (Monthly subscription) and postPay (Pay-As-You-Go resources)
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ActionType(self):
        """Transaction type. Valid values: prepay_purchase (Purchase), prepay_renew (Renewal), prepay_modify (Upgrade/Downgrade), prepay_return ( Monthly subscription refund), postpay_deduct (Pay-as-you-go), postpay_deduct_h (Hourly settlement), postpay_deduct_d (Daily settlement), postpay_deduct_m (Monthly settlement), offline_deduct (Offline project deduction), online_deduct (Offline product deduction), recon_deduct (Adjustment - deduction), recon_increase (Adjustment - compensation), ripay_purchase (One-off RI Fee), postpay_deduct_s (Spot), ri_hour_pay (Hourly RI fee), prePurchase (New monthly subscription), preRenew (Monthly subscription renewal), preUpgrade (Upgrade/Downgrade), preDowngrade (Upgrade/Downgrade), svp_hour_pay (Hourly Savings Plan fee), recon_guarantee (Minimum spend deduction), pre_purchase (New monthly subscription), pre_renew (Monthly subscription renewal), pre_upgrade (Upgrade/Downgrade), pre_downgrade (Upgrade/Downgrade)
        :rtype: str
        """
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
        :param _DetailSet: Data details.
        :type DetailSet: list of CustomerBillDetailData
        :param _Total: Total number of entries.
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DetailSet = None
        self._Total = None
        self._RequestId = None

    @property
    def DetailSet(self):
        """Data details.
        :rtype: list of CustomerBillDetailData
        """
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet

    @property
    def Total(self):
        """Total number of entries.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        :param _Month: The month to which the bill belongs, formatted as YYYY-MM; the earliest month available for query is June, 2022. Current month's billing data may be inaccurate; please download the current month's bill after it is generated at 1:00 on the 5th of the next month.
        :type Month: str
        :param _FileType: Type of bill. Valid values: L2 or L3
        :type FileType: str
        """
        self._Month = None
        self._FileType = None

    @property
    def Month(self):
        """The month to which the bill belongs, formatted as YYYY-MM; the earliest month available for query is June, 2022. Current month's billing data may be inaccurate; please download the current month's bill after it is generated at 1:00 on the 5th of the next month.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def FileType(self):
        """Type of bill. Valid values: L2 or L3
        :rtype: str
        """
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
        :param _DownloadUrl: File download link, with a file validity period of 1 hour
        :type DownloadUrl: str
        :param _Ready: File generation status. 0: generating; 1: generated.
        :type Ready: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._Ready = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        """File download link, with a file validity period of 1 hour
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def Ready(self):
        """File generation status. 0: generating; 1: generated.
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._Ready = params.get("Ready")
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
        """Bill month in the format of "yyyy-MM"
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def CustomerUin(self):
        """Customer UIN
        :rtype: int
        """
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
        :param _SummaryOverview: Get the payment mode details of the sub-customer bill summary through the api.
        :type SummaryOverview: list of PayModeSummaryOverviewItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SummaryOverview = None
        self._RequestId = None

    @property
    def SummaryOverview(self):
        """Get the payment mode details of the sub-customer bill summary through the api.
        :rtype: list of PayModeSummaryOverviewItem
        """
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Bill month in the format of "yyyy-MM"
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def CustomerUin(self):
        """Customer UIN
        :rtype: int
        """
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
        :param _SummaryOverview: Detailed information of product dimension.
        :type SummaryOverview: list of BusinessSummaryOverviewItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SummaryOverview = None
        self._RequestId = None

    @property
    def SummaryOverview(self):
        """Detailed information of product dimension.
        :rtype: list of BusinessSummaryOverviewItem
        """
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Bill month in the format of "yyyy-MM"
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def CustomerUin(self):
        """Customer UIN
        :rtype: int
        """
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
        :param _SummaryOverview: Get the region details of the customer bill data totaled by region through the api.
        :type SummaryOverview: list of RegionSummaryOverviewItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SummaryOverview = None
        self._RequestId = None

    @property
    def SummaryOverview(self):
        """Get the region details of the customer bill data totaled by region through the api.
        :rtype: list of RegionSummaryOverviewItem
        """
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _Month: The month to which the bill belongs, formatted as YYYY-MM.
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
        """The month to which the bill belongs, formatted as YYYY-MM.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def GroupType(self):
        """Billing dimension. Optional parameters: product, project, tag
        :rtype: str
        """
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def TagKey(self):
        """Tag value list
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
        


class DescribeBillSummaryResponse(AbstractModel):
    """DescribeBillSummary response structure.

    """

    def __init__(self):
        r"""
        :param _SummaryDetail: Detailed summary by billing dimension.
        :type SummaryDetail: list of SummaryDetails
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SummaryDetail = None
        self._RequestId = None

    @property
    def SummaryDetail(self):
        """Detailed summary by billing dimension.
        :rtype: list of SummaryDetails
        """
        return self._SummaryDetail

    @SummaryDetail.setter
    def SummaryDetail(self, SummaryDetail):
        self._SummaryDetail = SummaryDetail

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _CustomerUin: Sub-account UIN
        :type CustomerUin: int
        :param _Month: Inquiry month, in the format of YYYY-MM, such as 2023-01.
        :type Month: str
        :param _PageSize: Page parameter: number of entries per page. Value range: [1, 200]
        :type PageSize: int
        :param _Page: Page parameter: current page number. The minimum value is 1.
        :type Page: int
        :param _PayMode: Billing mode. Valid values:
prePay (Monthly subscription)
postPay (Pay-As-You-Go resources)
        :type PayMode: str
        :param _ActionType: Transaction type. Valid values:
prepay_purchase (Purchase)
prepay_renew (Renewal)
prepay_modify (Upgrade/Downgrade)
prepay_return ( Monthly subscription refund)
postpay_deduct (Pay-as-you-go)
postpay_deduct_h (Hourly settlement)
postpay_deduct_d (Daily settlement)
postpay_deduct_m (Monthly settlement)
offline_deduct (Offline project deduction)
online_deduct (Offline product deduction)
recon_deduct (Adjustment - deduction)
recon_increase (Adjustment - compensation)
ripay_purchase (One-off RI Fee)
postpay_deduct_s (Spot)
ri_hour_pay (Hourly RI fee)
prePurchase (New monthly subscription)
preRenew (Monthly subscription renewal)
preUpgrade (Upgrade/Downgrade)
preDowngrade (Upgrade/Downgrade)
svp_hour_pay (Hourly Savings Plan fee)
recon_guarantee (Minimum spend deduction)
pre_purchase (New monthly subscription)
pre_renew (Monthly subscription renewal)
pre_upgrade (Upgrade/Downgrade)
pre_downgrade (Upgrade/Downgrade)
        :type ActionType: str
        :param _IsConfirmed: Payment status
0: not distinguished
1: paid
2: unpaid
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
        """Sub-account UIN
        :rtype: int
        """
        return self._CustomerUin

    @CustomerUin.setter
    def CustomerUin(self, CustomerUin):
        self._CustomerUin = CustomerUin

    @property
    def Month(self):
        """Inquiry month, in the format of YYYY-MM, such as 2023-01.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PageSize(self):
        """Page parameter: number of entries per page. Value range: [1, 200]
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Page(self):
        """Page parameter: current page number. The minimum value is 1.
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PayMode(self):
        """Billing mode. Valid values:
prePay (Monthly subscription)
postPay (Pay-As-You-Go resources)
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ActionType(self):
        """Transaction type. Valid values:
prepay_purchase (Purchase)
prepay_renew (Renewal)
prepay_modify (Upgrade/Downgrade)
prepay_return ( Monthly subscription refund)
postpay_deduct (Pay-as-you-go)
postpay_deduct_h (Hourly settlement)
postpay_deduct_d (Daily settlement)
postpay_deduct_m (Monthly settlement)
offline_deduct (Offline project deduction)
online_deduct (Offline product deduction)
recon_deduct (Adjustment - deduction)
recon_increase (Adjustment - compensation)
ripay_purchase (One-off RI Fee)
postpay_deduct_s (Spot)
ri_hour_pay (Hourly RI fee)
prePurchase (New monthly subscription)
preRenew (Monthly subscription renewal)
preUpgrade (Upgrade/Downgrade)
preDowngrade (Upgrade/Downgrade)
svp_hour_pay (Hourly Savings Plan fee)
recon_guarantee (Minimum spend deduction)
pre_purchase (New monthly subscription)
pre_renew (Monthly subscription renewal)
pre_upgrade (Upgrade/Downgrade)
pre_downgrade (Upgrade/Downgrade)
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def IsConfirmed(self):
        """Payment status
0: not distinguished
1: paid
2: unpaid
        :rtype: str
        """
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
        :param _DetailSet: Data detailsNote: This field may return null, indicating that no valid values can be obtained.
        :type DetailSet: list of BillDetailData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._DetailSet = None
        self._RequestId = None

    @property
    def Total(self):
        """Total number of data entries
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def DetailSet(self):
        """Data detailsNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of BillDetailData
        """
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class DescribeCustomerBillDownloadUrlRequest(AbstractModel):
    """DescribeCustomerBillDownloadUrl request structure.

    """

    def __init__(self):
        r"""
        :param _Month: The month to which the bill belongs, formatted as yyyy-mm; the earliest month available for query is june, 2022. current month's billing data may be inaccurate; please download the current month's bill after it is generated at 1:00 on the 5th of the next month.
        :type Month: str
        :param _FileType: Bill type. valid values: [billResource, billDetail, billResourcePack, billDetailPack]. `billResource`: resource bill; `billDetail`: detailed bill; `billResourcePack`: resource bill package; `billDetailPack`: detailed bill package.
        :type FileType: str
        :param _CustomerUinType: Customer type. valid values: [Customer, Reseller, ResellerCustomer]. `Customer`: direct customer; `Reseller`: secondary reseller; `ResellerCustomer`: reseller's customers
        :type CustomerUinType: str
        :param _FileLanguage: Language. valid values: [zh_cn, en]. default is `en` (english).
        :type FileLanguage: str
        :param _CustomerUin: Customer uin. when downloading the bill package (FileType is billResourcePack or billDetailPack), CustomerUin is not passed
        :type CustomerUin: int
        """
        self._Month = None
        self._FileType = None
        self._CustomerUinType = None
        self._FileLanguage = None
        self._CustomerUin = None

    @property
    def Month(self):
        """The month to which the bill belongs, formatted as yyyy-mm; the earliest month available for query is june, 2022. current month's billing data may be inaccurate; please download the current month's bill after it is generated at 1:00 on the 5th of the next month.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def FileType(self):
        """Bill type. valid values: [billResource, billDetail, billResourcePack, billDetailPack]. `billResource`: resource bill; `billDetail`: detailed bill; `billResourcePack`: resource bill package; `billDetailPack`: detailed bill package.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CustomerUinType(self):
        """Customer type. valid values: [Customer, Reseller, ResellerCustomer]. `Customer`: direct customer; `Reseller`: secondary reseller; `ResellerCustomer`: reseller's customers
        :rtype: str
        """
        return self._CustomerUinType

    @CustomerUinType.setter
    def CustomerUinType(self, CustomerUinType):
        self._CustomerUinType = CustomerUinType

    @property
    def FileLanguage(self):
        """Language. valid values: [zh_cn, en]. default is `en` (english).
        :rtype: str
        """
        return self._FileLanguage

    @FileLanguage.setter
    def FileLanguage(self, FileLanguage):
        self._FileLanguage = FileLanguage

    @property
    def CustomerUin(self):
        """Customer uin. when downloading the bill package (FileType is billResourcePack or billDetailPack), CustomerUin is not passed
        :rtype: int
        """
        return self._CustomerUin

    @CustomerUin.setter
    def CustomerUin(self, CustomerUin):
        self._CustomerUin = CustomerUin


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._FileType = params.get("FileType")
        self._CustomerUinType = params.get("CustomerUinType")
        self._FileLanguage = params.get("FileLanguage")
        self._CustomerUin = params.get("CustomerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomerBillDownloadUrlResponse(AbstractModel):
    """DescribeCustomerBillDownloadUrl response structure.

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: File download link, with a file validity period of 1 hour.
        :type DownloadUrl: str
        :param _Ready: File generation status. 0: generating; 1: generated.
        :type Ready: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._Ready = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        """File download link, with a file validity period of 1 hour.
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def Ready(self):
        """File generation status. 0: generating; 1: generated.
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._Ready = params.get("Ready")
        self._RequestId = params.get("RequestId")


class DescribeCustomerBillSummaryRequest(AbstractModel):
    """DescribeCustomerBillSummary request structure.

    """

    def __init__(self):
        r"""
        :param _CustomerUin: Customer UIN
        :type CustomerUin: int
        :param _Month: The queried month in "YYYY-MM" format, such as 2023-01.
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
        """Customer UIN
        :rtype: int
        """
        return self._CustomerUin

    @CustomerUin.setter
    def CustomerUin(self, CustomerUin):
        self._CustomerUin = CustomerUin

    @property
    def Month(self):
        """The queried month in "YYYY-MM" format, such as 2023-01.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PayMode(self):
        """Billing mode. Valid values:
`prePay` (Monthly subscription)
`postPay` (Pay-as-you-go)
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ActionType(self):
        """Transaction type. Valid values:
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
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def IsConfirmed(self):
        """Payment status
`0`: N/A
`1`: Paid
`2`: Unpaid
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCost = None
        self._RequestId = None

    @property
    def TotalCost(self):
        """Total amount
        :rtype: float
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _CustomerUin: Sub-Account uin.
        :type CustomerUin: str
        :param _Email: Contact email.
        :type Email: str
        :param _Phone: Contact phone number.
        :type Phone: str
        :param _Mark: Remarks.
        :type Mark: str
        :param _Name: Display name.
        :type Name: str
        :param _BindTime: Binding time.
        :type BindTime: str
        :param _AccountStatus: Account status.
0: normal.
1: forcibly mandatory (this function is not supported yet).
2: mandatory arrears. 
        :type AccountStatus: str
        :param _AuthStatus: Specifies the identity verification status.
-999: account information not found.
-1: file not uploaded.
0: pending review.
Under review.
Error in review: 2.
3: pass review.
        :type AuthStatus: str
        :param _AuthType: Real-Name type.
-1: default value. no such information. 
0: personal type. 
1: enterprise type.
        :type AuthType: int
        :param _CidRegisterTime: Specifies the registration time of the cid.
        :type CidRegisterTime: str
        :param _UinRegisterTime: Specifies the registration time of the uin.
        :type UinRegisterTime: str
        :param _AuthPassTime: Time when real-name authentication passed.
        :type AuthPassTime: str
        :param _HasExpense: Whether there is consumption.
0: no consumption; 1: consumption.
        :type HasExpense: int
        """
        self._CustomerUin = None
        self._Email = None
        self._Phone = None
        self._Mark = None
        self._Name = None
        self._BindTime = None
        self._AccountStatus = None
        self._AuthStatus = None
        self._AuthType = None
        self._CidRegisterTime = None
        self._UinRegisterTime = None
        self._AuthPassTime = None
        self._HasExpense = None

    @property
    def CustomerUin(self):
        """Sub-Account uin.
        :rtype: str
        """
        return self._CustomerUin

    @CustomerUin.setter
    def CustomerUin(self, CustomerUin):
        self._CustomerUin = CustomerUin

    @property
    def Email(self):
        """Contact email.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Phone(self):
        """Contact phone number.
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Mark(self):
        """Remarks.
        :rtype: str
        """
        return self._Mark

    @Mark.setter
    def Mark(self, Mark):
        self._Mark = Mark

    @property
    def Name(self):
        """Display name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BindTime(self):
        """Binding time.
        :rtype: str
        """
        return self._BindTime

    @BindTime.setter
    def BindTime(self, BindTime):
        self._BindTime = BindTime

    @property
    def AccountStatus(self):
        """Account status.
0: normal.
1: forcibly mandatory (this function is not supported yet).
2: mandatory arrears. 
        :rtype: str
        """
        return self._AccountStatus

    @AccountStatus.setter
    def AccountStatus(self, AccountStatus):
        self._AccountStatus = AccountStatus

    @property
    def AuthStatus(self):
        """Specifies the identity verification status.
-999: account information not found.
-1: file not uploaded.
0: pending review.
Under review.
Error in review: 2.
3: pass review.
        :rtype: str
        """
        return self._AuthStatus

    @AuthStatus.setter
    def AuthStatus(self, AuthStatus):
        self._AuthStatus = AuthStatus

    @property
    def AuthType(self):
        """Real-Name type.
-1: default value. no such information. 
0: personal type. 
1: enterprise type.
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def CidRegisterTime(self):
        """Specifies the registration time of the cid.
        :rtype: str
        """
        return self._CidRegisterTime

    @CidRegisterTime.setter
    def CidRegisterTime(self, CidRegisterTime):
        self._CidRegisterTime = CidRegisterTime

    @property
    def UinRegisterTime(self):
        """Specifies the registration time of the uin.
        :rtype: str
        """
        return self._UinRegisterTime

    @UinRegisterTime.setter
    def UinRegisterTime(self, UinRegisterTime):
        self._UinRegisterTime = UinRegisterTime

    @property
    def AuthPassTime(self):
        """Time when real-name authentication passed.
        :rtype: str
        """
        return self._AuthPassTime

    @AuthPassTime.setter
    def AuthPassTime(self, AuthPassTime):
        self._AuthPassTime = AuthPassTime

    @property
    def HasExpense(self):
        """Whether there is consumption.
0: no consumption; 1: consumption.
        :rtype: int
        """
        return self._HasExpense

    @HasExpense.setter
    def HasExpense(self, HasExpense):
        self._HasExpense = HasExpense


    def _deserialize(self, params):
        self._CustomerUin = params.get("CustomerUin")
        self._Email = params.get("Email")
        self._Phone = params.get("Phone")
        self._Mark = params.get("Mark")
        self._Name = params.get("Name")
        self._BindTime = params.get("BindTime")
        self._AccountStatus = params.get("AccountStatus")
        self._AuthStatus = params.get("AuthStatus")
        self._AuthType = params.get("AuthType")
        self._CidRegisterTime = params.get("CidRegisterTime")
        self._UinRegisterTime = params.get("UinRegisterTime")
        self._AuthPassTime = params.get("AuthPassTime")
        self._HasExpense = params.get("HasExpense")
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
        """List of customer UIN. Array length value: 1-20.
        :rtype: list of int
        """
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
        :param _Data: Sub-Customer information.
        :type Data: list of DescribeCustomerInfoData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """Sub-Customer information.
        :rtype: list of DescribeCustomerInfoData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """Customer UIN Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        """Page number
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        """Number of data entries per page
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        """List of customer UINs Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DescribeCustomerUinData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        """The number of customers
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
                obj = DescribeCustomerUinData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeRebateDownloadUrlRequest(AbstractModel):
    """DescribeRebateDownloadUrl request structure.

    """

    def __init__(self):
        r"""
        :param _Month: Month of the commission bill. Format: YYYY-MM.
        :type Month: str
        :param _FileType: Bill file type. Valid value: CommissionDetail.
        :type FileType: str
        """
        self._Month = None
        self._FileType = None

    @property
    def Month(self):
        """Month of the commission bill. Format: YYYY-MM.
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def FileType(self):
        """Bill file type. Valid value: CommissionDetail.
        :rtype: str
        """
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
        


class DescribeRebateDownloadUrlResponse(AbstractModel):
    """DescribeRebateDownloadUrl response structure.

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: File download link, with a file validity period of 1 hour.
        :type DownloadUrl: str
        :param _Ready: File generation status. 0: generating; 1: generated.
        :type Ready: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._Ready = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        """File download link, with a file validity period of 1 hour.
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def Ready(self):
        """File generation status. 0: generating; 1: generated.
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._Ready = params.get("Ready")
        self._RequestId = params.get("RequestId")


class ForceQNRequest(AbstractModel):
    """ForceQN request structure.

    """

    def __init__(self):
        r"""
        :param _ClientUin: Sub-account UIN
        :type ClientUin: int
        :param _Type: 0: Normal  2: Forced service suspension
        :type Type: int
        """
        self._ClientUin = None
        self._Type = None

    @property
    def ClientUin(self):
        """Sub-account UIN
        :rtype: int
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def Type(self):
        """0: Normal  2: Forced service suspension
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceQNResponse(AbstractModel):
    """ForceQN response structure.

    """

    def __init__(self):
        r"""
        :param _C: Status (deprecated).
        :type C: int
        :param _M: Msg (deprecated).
        :type M: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._C = None
        self._M = None
        self._RequestId = None

    @property
    def C(self):
        warnings.warn("parameter `C` is deprecated", DeprecationWarning) 

        """Status (deprecated).
        :rtype: int
        """
        return self._C

    @C.setter
    def C(self, C):
        warnings.warn("parameter `C` is deprecated", DeprecationWarning) 

        self._C = C

    @property
    def M(self):
        warnings.warn("parameter `M` is deprecated", DeprecationWarning) 

        """Msg (deprecated).
        :rtype: str
        """
        return self._M

    @M.setter
    def M(self, M):
        warnings.warn("parameter `M` is deprecated", DeprecationWarning) 

        self._M = M

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._C = params.get("C")
        self._M = params.get("M")
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """List of country/region codes
        :rtype: list of CountryCodeItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
                obj = CountryCodeItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class GetTradeConfigListRequest(AbstractModel):
    """GetTradeConfigList request structure.

    """


class GetTradeConfigListResponse(AbstractModel):
    """GetTradeConfigList response structure.

    """

    def __init__(self):
        r"""
        :param _TradeList: Industry information.
        :type TradeList: list of TradeOneNode
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TradeList = None
        self._RequestId = None

    @property
    def TradeList(self):
        """Industry information.
        :rtype: list of TradeOneNode
        """
        return self._TradeList

    @TradeList.setter
    def TradeList(self, TradeList):
        self._TradeList = TradeList

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TradeList") is not None:
            self._TradeList = []
            for item in params.get("TradeList"):
                obj = TradeOneNode()
                obj._deserialize(item)
                self._TradeList.append(obj)
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
        """Customer UIN
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def Remark(self):
        """New customer remarks
        :rtype: str
        """
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
        """If successful, returns the new customer remarks
        :rtype: str
        """
        return self._ClientRemark

    @ClientRemark.setter
    def ClientRemark(self, ClientRemark):
        self._ClientRemark = ClientRemark

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _PayMode: Payment mode.
        :type PayMode: str
        :param _PayModeName: Payment mode name.
        :type PayModeName: str
        :param _OriginalCost: Actual total consumption, up to 8 decimal places.
        :type OriginalCost: str
        :param _Detail: Bill details in each payment mode.
        :type Detail: list of ActionSummaryOverviewItem
        :param _VoucherPayAmount: Voucher payment amount, up to 8 decimal places.
        :type VoucherPayAmount: str
        :param _TotalCost: Total consumption, up to 8 decimal places.
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
        """Payment mode.
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        """Payment mode name.
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def OriginalCost(self):
        """Actual total consumption, up to 8 decimal places.
        :rtype: str
        """
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def Detail(self):
        """Bill details in each payment mode.
        :rtype: list of ActionSummaryOverviewItem
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def VoucherPayAmount(self):
        """Voucher payment amount, up to 8 decimal places.
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TotalCost(self):
        """Total consumption, up to 8 decimal places.
        :rtype: str
        """
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
        


class PolicyProductList(AbstractModel):
    """Policy product list entity response parameters structure.

    """

    def __init__(self):
        r"""
        :param _PolicyCode:  Policy code.
        :type PolicyCode: str
        :param _ProductCode: The code of the ProductName field in the  bill data. If the return value is *, any item at this level is included in the policy product range.
        :type ProductCode: str
        :param _ProductName: The ProductName field value in the billing data. If the return value is *, any item at this level is included in the policy product range.
        :type ProductName: str
        :param _SubProductCode: The code of the SubProduct field in the  bill data. If the return value is *, any item at this level is included in the policy product range.
        :type SubProductCode: str
        :param _SubProductName: The SubProduct field value in the billing data. If the return value is *, any item at this level is included in the policy product range.
        :type SubProductName: str
        :param _ComponentTypeCode: The code of the ComponentType field in the  bill data. If the return value is *, any item at this level is included in the policy product range.
        :type ComponentTypeCode: str
        :param _ComponentTypeName: The ComponentType field value in the billing data. If the return value is *, any item at this level is included in the policy product range.
        :type ComponentTypeName: str
        :param _ComponentCode: The code of the Component field in the  bill data. If the return value is *, any item at this level is included in the policy product range.
        :type ComponentCode: str
        :param _ComponentName: The Component field value in the billing data. If the return value is *, any item at this level is included in the policy product range.
        :type ComponentName: str
        :param _StartDate: Policy effective time.
        :type StartDate: str
        :param _EndDate: Policy expiration time.
        :type EndDate: str
        """
        self._PolicyCode = None
        self._ProductCode = None
        self._ProductName = None
        self._SubProductCode = None
        self._SubProductName = None
        self._ComponentTypeCode = None
        self._ComponentTypeName = None
        self._ComponentCode = None
        self._ComponentName = None
        self._StartDate = None
        self._EndDate = None

    @property
    def PolicyCode(self):
        """ Policy code.
        :rtype: str
        """
        return self._PolicyCode

    @PolicyCode.setter
    def PolicyCode(self, PolicyCode):
        self._PolicyCode = PolicyCode

    @property
    def ProductCode(self):
        """The code of the ProductName field in the  bill data. If the return value is *, any item at this level is included in the policy product range.
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductName(self):
        """The ProductName field value in the billing data. If the return value is *, any item at this level is included in the policy product range.
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def SubProductCode(self):
        """The code of the SubProduct field in the  bill data. If the return value is *, any item at this level is included in the policy product range.
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def SubProductName(self):
        """The SubProduct field value in the billing data. If the return value is *, any item at this level is included in the policy product range.
        :rtype: str
        """
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName

    @property
    def ComponentTypeCode(self):
        """The code of the ComponentType field in the  bill data. If the return value is *, any item at this level is included in the policy product range.
        :rtype: str
        """
        return self._ComponentTypeCode

    @ComponentTypeCode.setter
    def ComponentTypeCode(self, ComponentTypeCode):
        self._ComponentTypeCode = ComponentTypeCode

    @property
    def ComponentTypeName(self):
        """The ComponentType field value in the billing data. If the return value is *, any item at this level is included in the policy product range.
        :rtype: str
        """
        return self._ComponentTypeName

    @ComponentTypeName.setter
    def ComponentTypeName(self, ComponentTypeName):
        self._ComponentTypeName = ComponentTypeName

    @property
    def ComponentCode(self):
        """The code of the Component field in the  bill data. If the return value is *, any item at this level is included in the policy product range.
        :rtype: str
        """
        return self._ComponentCode

    @ComponentCode.setter
    def ComponentCode(self, ComponentCode):
        self._ComponentCode = ComponentCode

    @property
    def ComponentName(self):
        """The Component field value in the billing data. If the return value is *, any item at this level is included in the policy product range.
        :rtype: str
        """
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def StartDate(self):
        """Policy effective time.
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """Policy expiration time.
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._PolicyCode = params.get("PolicyCode")
        self._ProductCode = params.get("ProductCode")
        self._ProductName = params.get("ProductName")
        self._SubProductCode = params.get("SubProductCode")
        self._SubProductName = params.get("SubProductName")
        self._ComponentTypeCode = params.get("ComponentTypeCode")
        self._ComponentTypeName = params.get("ComponentTypeName")
        self._ComponentCode = params.get("ComponentCode")
        self._ComponentName = params.get("ComponentName")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
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
        """Customer UIN
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccountStatus = None
        self._RequestId = None

    @property
    def AccountStatus(self):
        """Account verification status
        :rtype: bool
        """
        return self._AccountStatus

    @AccountStatus.setter
    def AccountStatus(self, AccountStatus):
        self._AccountStatus = AccountStatus

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _ClientCreditAfter: Available credits after allocation.
        :type ClientCreditAfter: float
        :param _Remark: Remark
        :type Remark: str
        """
        self._AllocatedTime = None
        self._Operator = None
        self._Credit = None
        self._AllocatedCredit = None
        self._ClientCreditAfter = None
        self._Remark = None

    @property
    def AllocatedTime(self):
        """Allocation time
        :rtype: str
        """
        return self._AllocatedTime

    @AllocatedTime.setter
    def AllocatedTime(self, AllocatedTime):
        self._AllocatedTime = AllocatedTime

    @property
    def Operator(self):
        """Operator
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Credit(self):
        """Allocated credit value
        :rtype: float
        """
        return self._Credit

    @Credit.setter
    def Credit(self, Credit):
        self._Credit = Credit

    @property
    def AllocatedCredit(self):
        """The allocated total credit
        :rtype: float
        """
        return self._AllocatedCredit

    @AllocatedCredit.setter
    def AllocatedCredit(self, AllocatedCredit):
        self._AllocatedCredit = AllocatedCredit

    @property
    def ClientCreditAfter(self):
        """Available credits after allocation.
        :rtype: float
        """
        return self._ClientCreditAfter

    @ClientCreditAfter.setter
    def ClientCreditAfter(self, ClientCreditAfter):
        self._ClientCreditAfter = ClientCreditAfter

    @property
    def Remark(self):
        """Remark
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._AllocatedTime = params.get("AllocatedTime")
        self._Operator = params.get("Operator")
        self._Credit = params.get("Credit")
        self._AllocatedCredit = params.get("AllocatedCredit")
        self._ClientCreditAfter = params.get("ClientCreditAfter")
        self._Remark = params.get("Remark")
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
        """Customer UIN
        :rtype: int
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def Page(self):
        """Page number
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        """Number of data entries per page
        :rtype: int
        """
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
        :param _Total: Total number of historical records.
        :type Total: int
        :param _History: Detailed list of historical information.
        :type History: list of QueryCreditAllocationHistoryData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._History = None
        self._RequestId = None

    @property
    def Total(self):
        """Total number of historical records.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def History(self):
        """Detailed list of historical information.
        :rtype: list of QueryCreditAllocationHistoryData
        """
        return self._History

    @History.setter
    def History(self, History):
        self._History = History

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """List of user. Array length value: 1-50.
        :rtype: list of int non-negative
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """User information list
        :rtype: list of QueryDirectCustomersCreditData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
                obj = QueryDirectCustomersCreditData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class QueryCustomerBillingQuotaData(AbstractModel):
    """Sub-customer credit balance data

    """

    def __init__(self):
        r"""
        :param _TotalCredit: Total credit limit (unit: cny), accurate down to two decimal places.
        :type TotalCredit: float
        :param _RemainingCredit: Remaining credit limit (unit: cny), accurate down to two decimal places.
        :type RemainingCredit: float
        :param _RemainingVoucher: Remaining total voucher amount (unit: cny), accurate down to two decimal places.
        :type RemainingVoucher: float
        :param _Force: Forced status
.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Force: int
        :param _PrepayFrozen: Prepaid frozen amount.
        :type PrepayFrozen: float
        :param _PostpayFrozen: Postpaid frozen amount.
        :type PostpayFrozen: float
        """
        self._TotalCredit = None
        self._RemainingCredit = None
        self._RemainingVoucher = None
        self._Force = None
        self._PrepayFrozen = None
        self._PostpayFrozen = None

    @property
    def TotalCredit(self):
        """Total credit limit (unit: cny), accurate down to two decimal places.
        :rtype: float
        """
        return self._TotalCredit

    @TotalCredit.setter
    def TotalCredit(self, TotalCredit):
        self._TotalCredit = TotalCredit

    @property
    def RemainingCredit(self):
        """Remaining credit limit (unit: cny), accurate down to two decimal places.
        :rtype: float
        """
        return self._RemainingCredit

    @RemainingCredit.setter
    def RemainingCredit(self, RemainingCredit):
        self._RemainingCredit = RemainingCredit

    @property
    def RemainingVoucher(self):
        """Remaining total voucher amount (unit: cny), accurate down to two decimal places.
        :rtype: float
        """
        return self._RemainingVoucher

    @RemainingVoucher.setter
    def RemainingVoucher(self, RemainingVoucher):
        self._RemainingVoucher = RemainingVoucher

    @property
    def Force(self):
        """Forced status
.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force

    @property
    def PrepayFrozen(self):
        """Prepaid frozen amount.
        :rtype: float
        """
        return self._PrepayFrozen

    @PrepayFrozen.setter
    def PrepayFrozen(self, PrepayFrozen):
        self._PrepayFrozen = PrepayFrozen

    @property
    def PostpayFrozen(self):
        """Postpaid frozen amount.
        :rtype: float
        """
        return self._PostpayFrozen

    @PostpayFrozen.setter
    def PostpayFrozen(self, PostpayFrozen):
        self._PostpayFrozen = PostpayFrozen


    def _deserialize(self, params):
        self._TotalCredit = params.get("TotalCredit")
        self._RemainingCredit = params.get("RemainingCredit")
        self._RemainingVoucher = params.get("RemainingVoucher")
        self._Force = params.get("Force")
        self._PrepayFrozen = params.get("PrepayFrozen")
        self._PostpayFrozen = params.get("PostpayFrozen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCustomerBillingQuotaRequest(AbstractModel):
    """QueryCustomerBillingQuota request structure.

    """

    def __init__(self):
        r"""
        :param _EventId: Event id, used to tag the request event, usually a random number.
        :type EventId: int
        :param _ComponentName: Source of the request.
        :type ComponentName: str
        """
        self._EventId = None
        self._ComponentName = None

    @property
    def EventId(self):
        warnings.warn("parameter `EventId` is deprecated", DeprecationWarning) 

        """Event id, used to tag the request event, usually a random number.
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        warnings.warn("parameter `EventId` is deprecated", DeprecationWarning) 

        self._EventId = EventId

    @property
    def ComponentName(self):
        warnings.warn("parameter `ComponentName` is deprecated", DeprecationWarning) 

        """Source of the request.
        :rtype: str
        """
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        warnings.warn("parameter `ComponentName` is deprecated", DeprecationWarning) 

        self._ComponentName = ComponentName


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._ComponentName = params.get("ComponentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCustomerBillingQuotaResponse(AbstractModel):
    """QueryCustomerBillingQuota response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Limit data.
        :type Data: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCustomerBillingQuotaData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """Limit data.
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCustomerBillingQuotaData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = QueryCustomerBillingQuotaData()
            self._Data._deserialize(params.get("Data"))
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
        """Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """Type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Mobile(self):
        """Mobile number
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Email(self):
        """Email
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Arrears(self):
        """Overdue payment flag
        :rtype: str
        """
        return self._Arrears

    @Arrears.setter
    def Arrears(self, Arrears):
        self._Arrears = Arrears

    @property
    def AssociationTime(self):
        """Binding time
        :rtype: str
        """
        return self._AssociationTime

    @AssociationTime.setter
    def AssociationTime(self, AssociationTime):
        self._AssociationTime = AssociationTime

    @property
    def RecentExpiry(self):
        """Expiration time
        :rtype: str
        """
        return self._RecentExpiry

    @RecentExpiry.setter
    def RecentExpiry(self, RecentExpiry):
        self._RecentExpiry = RecentExpiry

    @property
    def ClientUin(self):
        """Customer UIN
        :rtype: int
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def Credit(self):
        """Credit allocated to a customer
        :rtype: float
        """
        return self._Credit

    @Credit.setter
    def Credit(self, Credit):
        self._Credit = Credit

    @property
    def RemainingCredit(self):
        """The remaining credit of a customer
        :rtype: float
        """
        return self._RemainingCredit

    @RemainingCredit.setter
    def RemainingCredit(self, RemainingCredit):
        self._RemainingCredit = RemainingCredit

    @property
    def IdentifyType(self):
        """`0`: Identity not verified; `1`: Individual identity verified; `2`: Enterprise identity verified.
        :rtype: int
        """
        return self._IdentifyType

    @IdentifyType.setter
    def IdentifyType(self, IdentifyType):
        self._IdentifyType = IdentifyType

    @property
    def Remark(self):
        """Customer remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Force(self):
        """Forced status
        :rtype: int
        """
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
        """Search condition type. You can only search by customer ID, name, remarks, or email.
        :rtype: str
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def Filter(self):
        """Search condition
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Page(self):
        """A pagination parameter that specifies the current page number, with a value starting from 1.
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        """A pagination parameter that specifies the number of entries per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Order(self):
        """A sort parameter that specifies the sort order. Valid values: `desc` (descending order), or `asc` (ascending order) based on `AssociationTime`. The value will be `desc` if left empty.
        :rtype: str
        """
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
        :param _Data: Queries the list of customers.
        :type Data: list of QueryCustomersCreditData
        :param _Total: Number of customers
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        """Queries the list of customers.
        :rtype: list of QueryCustomersCreditData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        """Number of customers
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """User UIN
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def TotalCredit(self):
        """Total credit
        :rtype: float
        """
        return self._TotalCredit

    @TotalCredit.setter
    def TotalCredit(self, TotalCredit):
        self._TotalCredit = TotalCredit

    @property
    def RemainingCredit(self):
        """Remaining credit
        :rtype: float
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """Direct customer information list
        :rtype: list of QueryDirectCustomersCreditData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
                obj = QueryDirectCustomersCreditData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class QueryInvitationInfoData(AbstractModel):
    """Invitation link information.

    """

    def __init__(self):
        r"""
        :param _InvitationToken: Invitation link token.
        :type InvitationToken: str
        :param _CreateTime: Creation time of the invitation link.
        :type CreateTime: str
        :param _Status: Invite link status.
1: Unused.
2: Used.
        :type Status: int
        :param _UseTime: Indicates the usage time of the invitation link.
        :type UseTime: str
        :param _ClientUin: Customer uin.
        :type ClientUin: int
        :param _ClientMail: Customer mailbox.
        :type ClientMail: str
        :param _ClientType: Customer type.
1: Second-Level reseller.
2: Sub-Customer.
        :type ClientType: int
        :param _BindTime: The binding time of the customer.
        :type BindTime: str
        """
        self._InvitationToken = None
        self._CreateTime = None
        self._Status = None
        self._UseTime = None
        self._ClientUin = None
        self._ClientMail = None
        self._ClientType = None
        self._BindTime = None

    @property
    def InvitationToken(self):
        """Invitation link token.
        :rtype: str
        """
        return self._InvitationToken

    @InvitationToken.setter
    def InvitationToken(self, InvitationToken):
        self._InvitationToken = InvitationToken

    @property
    def CreateTime(self):
        """Creation time of the invitation link.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        """Invite link status.
1: Unused.
2: Used.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UseTime(self):
        """Indicates the usage time of the invitation link.
        :rtype: str
        """
        return self._UseTime

    @UseTime.setter
    def UseTime(self, UseTime):
        self._UseTime = UseTime

    @property
    def ClientUin(self):
        """Customer uin.
        :rtype: int
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def ClientMail(self):
        """Customer mailbox.
        :rtype: str
        """
        return self._ClientMail

    @ClientMail.setter
    def ClientMail(self, ClientMail):
        self._ClientMail = ClientMail

    @property
    def ClientType(self):
        """Customer type.
1: Second-Level reseller.
2: Sub-Customer.
        :rtype: int
        """
        return self._ClientType

    @ClientType.setter
    def ClientType(self, ClientType):
        self._ClientType = ClientType

    @property
    def BindTime(self):
        """The binding time of the customer.
        :rtype: str
        """
        return self._BindTime

    @BindTime.setter
    def BindTime(self, BindTime):
        self._BindTime = BindTime


    def _deserialize(self, params):
        self._InvitationToken = params.get("InvitationToken")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        self._UseTime = params.get("UseTime")
        self._ClientUin = params.get("ClientUin")
        self._ClientMail = params.get("ClientMail")
        self._ClientType = params.get("ClientType")
        self._BindTime = params.get("BindTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryInvitationInfoRequest(AbstractModel):
    """QueryInvitationInfo request structure.

    """

    def __init__(self):
        r"""
        :param _InvitationToken: Invite token. array member quantity value: [1, 100].
        :type InvitationToken: list of str
        """
        self._InvitationToken = None

    @property
    def InvitationToken(self):
        """Invite token. array member quantity value: [1, 100].
        :rtype: list of str
        """
        return self._InvitationToken

    @InvitationToken.setter
    def InvitationToken(self, InvitationToken):
        self._InvitationToken = InvitationToken


    def _deserialize(self, params):
        self._InvitationToken = params.get("InvitationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryInvitationInfoResponse(AbstractModel):
    """QueryInvitationInfo response structure.

    """

    def __init__(self):
        r"""
        :param _InvitationInfo: Invitation link information.
        :type InvitationInfo: list of QueryInvitationInfoData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InvitationInfo = None
        self._RequestId = None

    @property
    def InvitationInfo(self):
        """Invitation link information.
        :rtype: list of QueryInvitationInfoData
        """
        return self._InvitationInfo

    @InvitationInfo.setter
    def InvitationInfo(self, InvitationInfo):
        self._InvitationInfo = InvitationInfo

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InvitationInfo") is not None:
            self._InvitationInfo = []
            for item in params.get("InvitationInfo"):
                obj = QueryInvitationInfoData()
                obj._deserialize(item)
                self._InvitationInfo.append(obj)
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """Allocated credit
        :rtype: float
        """
        return self._AllocatedCredit

    @AllocatedCredit.setter
    def AllocatedCredit(self, AllocatedCredit):
        self._AllocatedCredit = AllocatedCredit

    @property
    def TotalCredit(self):
        """Total credit
        :rtype: float
        """
        return self._TotalCredit

    @TotalCredit.setter
    def TotalCredit(self, TotalCredit):
        self._TotalCredit = TotalCredit

    @property
    def RemainingCredit(self):
        """Remaining credit
        :rtype: float
        """
        return self._RemainingCredit

    @RemainingCredit.setter
    def RemainingCredit(self, RemainingCredit):
        self._RemainingCredit = RemainingCredit

    @property
    def CustomerTotalCredit(self):
        """Allocated quota for the client
        :rtype: float
        """
        return self._CustomerTotalCredit

    @CustomerTotalCredit.setter
    def CustomerTotalCredit(self, CustomerTotalCredit):
        self._CustomerTotalCredit = CustomerTotalCredit

    @property
    def CustomerRemainingCredit(self):
        """Remaining quota for the client
        :rtype: float
        """
        return self._CustomerRemainingCredit

    @CustomerRemainingCredit.setter
    def CustomerRemainingCredit(self, CustomerRemainingCredit):
        self._CustomerRemainingCredit = CustomerRemainingCredit

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class QueryPendingClientsV2Request(AbstractModel):
    """QueryPendingClientsV2 request structure.

    """

    def __init__(self):
        r"""
        :param _Page: Page number, starting from 1.
        :type Page: int
        :param _PageSize: Quantity. page size [1-100].
        :type PageSize: int
        """
        self._Page = None
        self._PageSize = None

    @property
    def Page(self):
        """Page number, starting from 1.
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        """Quantity. page size [1-100].
        :rtype: int
        """
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
        


class QueryPendingClientsV2Response(AbstractModel):
    """QueryPendingClientsV2 response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Details of customers in application.
        :type Data: list of QueryPendingCustomersItem
        :param _Total: Total number of customers in application.
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        """Details of customers in application.
        :rtype: list of QueryPendingCustomersItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        """Total number of customers in application.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
                obj = QueryPendingCustomersItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class QueryPendingCustomersItem(AbstractModel):
    """Pending review sub-customer

    """

    def __init__(self):
        r"""
        :param _ApplyTime: Application time.
        :type ApplyTime: str
        :param _ClientUin: Sub-Account uin.
        :type ClientUin: int
        :param _Email: Email.
        :type Email: str
        :param _Mobile: Mobile number.
        :type Mobile: str
        :param _Name: Name.
        :type Name: str
        :param _Status: Approval status.
        :type Status: str
        :param _Type: Sub-Customer type.
        :type Type: str
        """
        self._ApplyTime = None
        self._ClientUin = None
        self._Email = None
        self._Mobile = None
        self._Name = None
        self._Status = None
        self._Type = None

    @property
    def ApplyTime(self):
        """Application time.
        :rtype: str
        """
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def ClientUin(self):
        """Sub-Account uin.
        :rtype: int
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def Email(self):
        """Email.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Mobile(self):
        """Mobile number.
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Name(self):
        """Name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        """Approval status.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        """Sub-Customer type.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._ApplyTime = params.get("ApplyTime")
        self._ClientUin = params.get("ClientUin")
        self._Email = params.get("Email")
        self._Mobile = params.get("Mobile")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryPendingSubAgentsV2Request(AbstractModel):
    """QueryPendingSubAgentsV2 request structure.

    """

    def __init__(self):
        r"""
        :param _Page: Page number. starts from 1.
        :type Page: int
        :param _PageSize: Specifies the number of items per page. value range: supports up to 100.
        :type PageSize: int
        """
        self._Page = None
        self._PageSize = None

    @property
    def Page(self):
        """Page number. starts from 1.
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        """Specifies the number of items per page. value range: supports up to 100.
        :rtype: int
        """
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
        


class QueryPendingSubAgentsV2Response(AbstractModel):
    """QueryPendingSubAgentsV2 response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Application in progress second-level reseller information.
        :type Data: list of QueryPendingSubAgentsV2ResponseData
        :param _Total: Number of second-level resellers in application.
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        """Application in progress second-level reseller information.
        :rtype: list of QueryPendingSubAgentsV2ResponseData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        """Number of second-level resellers in application.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
                obj = QueryPendingSubAgentsV2ResponseData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class QueryPendingSubAgentsV2ResponseData(AbstractModel):
    """Information of second-level reseller application in progress.

    """

    def __init__(self):
        r"""
        :param _SubAgentUin: Second-level reseller UIN.
        :type SubAgentUin: int
        :param _Name: Name
        :type Name: str
        :param _Mobile: Mobile number.
        :type Mobile: str
        :param _Email: Specifies the mailbox.
        :type Email: str
        :param _ApplyTime: Application time
        :type ApplyTime: str
        :param _Status: Approval status

{Reviewing: pending review}.
        :type Status: str
        :param _MaterialUrl: Application material.
        :type MaterialUrl: str
        :param _AuthState: Identity verification status -1: file not uploaded 0: pending review 1: under review; 2: review error; 3: approved.
        :type AuthState: int
        """
        self._SubAgentUin = None
        self._Name = None
        self._Mobile = None
        self._Email = None
        self._ApplyTime = None
        self._Status = None
        self._MaterialUrl = None
        self._AuthState = None

    @property
    def SubAgentUin(self):
        """Second-level reseller UIN.
        :rtype: int
        """
        return self._SubAgentUin

    @SubAgentUin.setter
    def SubAgentUin(self, SubAgentUin):
        self._SubAgentUin = SubAgentUin

    @property
    def Name(self):
        """Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mobile(self):
        """Mobile number.
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Email(self):
        """Specifies the mailbox.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def ApplyTime(self):
        """Application time
        :rtype: str
        """
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def Status(self):
        """Approval status

{Reviewing: pending review}.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MaterialUrl(self):
        """Application material.
        :rtype: str
        """
        return self._MaterialUrl

    @MaterialUrl.setter
    def MaterialUrl(self, MaterialUrl):
        self._MaterialUrl = MaterialUrl

    @property
    def AuthState(self):
        """Identity verification status -1: file not uploaded 0: pending review 1: under review; 2: review error; 3: approved.
        :rtype: int
        """
        return self._AuthState

    @AuthState.setter
    def AuthState(self, AuthState):
        self._AuthState = AuthState


    def _deserialize(self, params):
        self._SubAgentUin = params.get("SubAgentUin")
        self._Name = params.get("Name")
        self._Mobile = params.get("Mobile")
        self._Email = params.get("Email")
        self._ApplyTime = params.get("ApplyTime")
        self._Status = params.get("Status")
        self._MaterialUrl = params.get("MaterialUrl")
        self._AuthState = params.get("AuthState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryPolicyProductListByCodeRequest(AbstractModel):
    """QueryPolicyProductListByCode request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyCode: Policy code.
        :type PolicyCode: str
        :param _ProductCode: The code of the ProductName field in the  bill data.
        :type ProductCode: str
        :param _ProductName: The ProductName field value in the billing data.
        :type ProductName: str
        :param _SubProductCode: The code of the SubProductName field in the  bill data.
        :type SubProductCode: str
        :param _SubProductName: The SubProductName field value in the billing data.
        :type SubProductName: str
        :param _Page: Page parameter: current page number. The minimum value is 1.
        :type Page: int
        :param _PageSize: Page parameter: Indicates the number of entries per page. Value range: [1, 200], default is 200.
        :type PageSize: int
        """
        self._PolicyCode = None
        self._ProductCode = None
        self._ProductName = None
        self._SubProductCode = None
        self._SubProductName = None
        self._Page = None
        self._PageSize = None

    @property
    def PolicyCode(self):
        """Policy code.
        :rtype: str
        """
        return self._PolicyCode

    @PolicyCode.setter
    def PolicyCode(self, PolicyCode):
        self._PolicyCode = PolicyCode

    @property
    def ProductCode(self):
        """The code of the ProductName field in the  bill data.
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductName(self):
        """The ProductName field value in the billing data.
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def SubProductCode(self):
        """The code of the SubProductName field in the  bill data.
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def SubProductName(self):
        """The SubProductName field value in the billing data.
        :rtype: str
        """
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName

    @property
    def Page(self):
        """Page parameter: current page number. The minimum value is 1.
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        """Page parameter: Indicates the number of entries per page. Value range: [1, 200], default is 200.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._PolicyCode = params.get("PolicyCode")
        self._ProductCode = params.get("ProductCode")
        self._ProductName = params.get("ProductName")
        self._SubProductCode = params.get("SubProductCode")
        self._SubProductName = params.get("SubProductName")
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryPolicyProductListByCodeResponse(AbstractModel):
    """QueryPolicyProductListByCode response structure.

    """

    def __init__(self):
        r"""
        :param _ProductList: policy product list.
        :type ProductList: list of PolicyProductList
        :param _Total: Total number of data entries
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProductList = None
        self._Total = None
        self._RequestId = None

    @property
    def ProductList(self):
        """policy product list.
        :rtype: list of PolicyProductList
        """
        return self._ProductList

    @ProductList.setter
    def ProductList(self, ProductList):
        self._ProductList = ProductList

    @property
    def Total(self):
        """Total number of data entries
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProductList") is not None:
            self._ProductList = []
            for item in params.get("ProductList"):
                obj = PolicyProductList()
                obj._deserialize(item)
                self._ProductList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class QuerySubAgentsDetailV2Request(AbstractModel):
    """QuerySubAgentsDetailV2 request structure.

    """

    def __init__(self):
        r"""
        :param _Page: Page number. starts from 1.
        :type Page: int
        :param _PageSize: Number of items per page. supports up to 100.
        :type PageSize: int
        :param _FilterType: Filter criteria, support the following filter parameters.
Note: Email, SubAgentUin, and ClientUin only support exact search. other conditions support fuzzy retrieval.The following are the definitions of filtering  items:

Name: specifies second-level reseller name.
SubAgentUin: specifies the uin of the second-level reseller.
Remark: specifies remark.
Mobile: specifies the mobile number.
Email: specifies email address.
ClientUin: specifies the Indirect customer uin.
        :type FilterType: str
        :param _Filter: Filter value
        :type Filter: str
        :param _Order: Sorting method. sorts by binding time in ascending or descending order. defaults to descending order if not specified.
Desc: descending order.
acs: ascending.
        :type Order: str
        """
        self._Page = None
        self._PageSize = None
        self._FilterType = None
        self._Filter = None
        self._Order = None

    @property
    def Page(self):
        """Page number. starts from 1.
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        """Number of items per page. supports up to 100.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def FilterType(self):
        """Filter criteria, support the following filter parameters.
Note: Email, SubAgentUin, and ClientUin only support exact search. other conditions support fuzzy retrieval.The following are the definitions of filtering  items:

Name: specifies second-level reseller name.
SubAgentUin: specifies the uin of the second-level reseller.
Remark: specifies remark.
Mobile: specifies the mobile number.
Email: specifies email address.
ClientUin: specifies the Indirect customer uin.
        :rtype: str
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def Filter(self):
        """Filter value
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Order(self):
        """Sorting method. sorts by binding time in ascending or descending order. defaults to descending order if not specified.
Desc: descending order.
acs: ascending.
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        self._FilterType = params.get("FilterType")
        self._Filter = params.get("Filter")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuerySubAgentsDetailV2Response(AbstractModel):
    """QuerySubAgentsDetailV2 response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Number of second-level resellers.
        :type Total: int
        :param _Data: Second-Level reseller information.
        :type Data: list of QuerySubAgentsDetailV2ResponseData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        """Number of second-level resellers.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """Second-Level reseller information.
        :rtype: list of QuerySubAgentsDetailV2ResponseData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
                obj = QuerySubAgentsDetailV2ResponseData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class QuerySubAgentsDetailV2ResponseData(AbstractModel):
    """Second-Level reseller information.

    """

    def __init__(self):
        r"""
        :param _SubAgentUin: Second-level reseller UIN.
        :type SubAgentUin: int
        :param _Name: Name
        :type Name: str
        :param _Remark: Remarks
        :type Remark: str
        :param _Mobile: Mobile number.
        :type Mobile: str
        :param _Email: Specifies the mailbox.
        :type Email: str
        :param _CountOfCustomers: Number of secondary dealer sub-customers.
        :type CountOfCustomers: int
        :param _BindTime: Binding time.
        :type BindTime: str
        :param _Credit: Credit limit pool of second-level reseller.
        :type Credit: float
        :param _RemainingCredit: Value pool of unconsumed credit limit for second-level reseller.
        :type RemainingCredit: float
        :param _Voucher: Cash coupon quota pool for second-level reseller.
        :type Voucher: float
        :param _RemainingVoucher: Balance of cash coupon quota pool for second-level reseller.
        :type RemainingVoucher: float
        """
        self._SubAgentUin = None
        self._Name = None
        self._Remark = None
        self._Mobile = None
        self._Email = None
        self._CountOfCustomers = None
        self._BindTime = None
        self._Credit = None
        self._RemainingCredit = None
        self._Voucher = None
        self._RemainingVoucher = None

    @property
    def SubAgentUin(self):
        """Second-level reseller UIN.
        :rtype: int
        """
        return self._SubAgentUin

    @SubAgentUin.setter
    def SubAgentUin(self, SubAgentUin):
        self._SubAgentUin = SubAgentUin

    @property
    def Name(self):
        """Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        """Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Mobile(self):
        """Mobile number.
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Email(self):
        """Specifies the mailbox.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def CountOfCustomers(self):
        """Number of secondary dealer sub-customers.
        :rtype: int
        """
        return self._CountOfCustomers

    @CountOfCustomers.setter
    def CountOfCustomers(self, CountOfCustomers):
        self._CountOfCustomers = CountOfCustomers

    @property
    def BindTime(self):
        """Binding time.
        :rtype: str
        """
        return self._BindTime

    @BindTime.setter
    def BindTime(self, BindTime):
        self._BindTime = BindTime

    @property
    def Credit(self):
        """Credit limit pool of second-level reseller.
        :rtype: float
        """
        return self._Credit

    @Credit.setter
    def Credit(self, Credit):
        self._Credit = Credit

    @property
    def RemainingCredit(self):
        """Value pool of unconsumed credit limit for second-level reseller.
        :rtype: float
        """
        return self._RemainingCredit

    @RemainingCredit.setter
    def RemainingCredit(self, RemainingCredit):
        self._RemainingCredit = RemainingCredit

    @property
    def Voucher(self):
        """Cash coupon quota pool for second-level reseller.
        :rtype: float
        """
        return self._Voucher

    @Voucher.setter
    def Voucher(self, Voucher):
        self._Voucher = Voucher

    @property
    def RemainingVoucher(self):
        """Balance of cash coupon quota pool for second-level reseller.
        :rtype: float
        """
        return self._RemainingVoucher

    @RemainingVoucher.setter
    def RemainingVoucher(self, RemainingVoucher):
        self._RemainingVoucher = RemainingVoucher


    def _deserialize(self, params):
        self._SubAgentUin = params.get("SubAgentUin")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._Mobile = params.get("Mobile")
        self._Email = params.get("Email")
        self._CountOfCustomers = params.get("CountOfCustomers")
        self._BindTime = params.get("BindTime")
        self._Credit = params.get("Credit")
        self._RemainingCredit = params.get("RemainingCredit")
        self._Voucher = params.get("Voucher")
        self._RemainingVoucher = params.get("RemainingVoucher")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryT1IndirectCustomersDetailRequest(AbstractModel):
    """QueryT1IndirectCustomersDetail request structure.

    """

    def __init__(self):
        r"""
        :param _SubAgentUin: Second-level reseller UIN.
        :type SubAgentUin: int
        :param _Page: Pagination parameter: current page number. it starts from 1.
        :type Page: int
        :param _PageSize: Pagination parameter, indicates the number of entries per page. supports [1, 100] data entries per request.
        :type PageSize: int
        """
        self._SubAgentUin = None
        self._Page = None
        self._PageSize = None

    @property
    def SubAgentUin(self):
        """Second-level reseller UIN.
        :rtype: int
        """
        return self._SubAgentUin

    @SubAgentUin.setter
    def SubAgentUin(self, SubAgentUin):
        self._SubAgentUin = SubAgentUin

    @property
    def Page(self):
        """Pagination parameter: current page number. it starts from 1.
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        """Pagination parameter, indicates the number of entries per page. supports [1, 100] data entries per request.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._SubAgentUin = params.get("SubAgentUin")
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryT1IndirectCustomersDetailResponse(AbstractModel):
    """QueryT1IndirectCustomersDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The number of indirect sub-customers of a distributor.
        :type Total: int
        :param _SubAgentUin: Second-level reseller UIN.
        :type SubAgentUin: int
        :param _SubAgentName: Second-Level reseller name.
        :type SubAgentName: str
        :param _Data: Indirect sub-customer information.
        :type Data: list of QueryT1IndirectCustomersDetailResponseData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._SubAgentUin = None
        self._SubAgentName = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        """The number of indirect sub-customers of a distributor.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def SubAgentUin(self):
        """Second-level reseller UIN.
        :rtype: int
        """
        return self._SubAgentUin

    @SubAgentUin.setter
    def SubAgentUin(self, SubAgentUin):
        self._SubAgentUin = SubAgentUin

    @property
    def SubAgentName(self):
        """Second-Level reseller name.
        :rtype: str
        """
        return self._SubAgentName

    @SubAgentName.setter
    def SubAgentName(self, SubAgentName):
        self._SubAgentName = SubAgentName

    @property
    def Data(self):
        """Indirect sub-customer information.
        :rtype: list of QueryT1IndirectCustomersDetailResponseData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._SubAgentUin = params.get("SubAgentUin")
        self._SubAgentName = params.get("SubAgentName")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = QueryT1IndirectCustomersDetailResponseData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class QueryT1IndirectCustomersDetailResponseData(AbstractModel):
    """Query data of indirect sub-customers of a first-level distributor.

    Callable roles: Distributor

    """

    def __init__(self):
        r"""
        :param _ClientUin: Customer uin.
        :type ClientUin: int
        :param _ClientName: Customer name.
        :type ClientName: str
        :param _ClientBindTime: The time when a sub-customer binds a second-level reseller, time zone: UTC+08:00.
        :type ClientBindTime: str
        """
        self._ClientUin = None
        self._ClientName = None
        self._ClientBindTime = None

    @property
    def ClientUin(self):
        """Customer uin.
        :rtype: int
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def ClientName(self):
        """Customer name.
        :rtype: str
        """
        return self._ClientName

    @ClientName.setter
    def ClientName(self, ClientName):
        self._ClientName = ClientName

    @property
    def ClientBindTime(self):
        """The time when a sub-customer binds a second-level reseller, time zone: UTC+08:00.
        :rtype: str
        """
        return self._ClientBindTime

    @ClientBindTime.setter
    def ClientBindTime(self, ClientBindTime):
        self._ClientBindTime = ClientBindTime


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        self._ClientName = params.get("ClientName")
        self._ClientBindTime = params.get("ClientBindTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        """Customer UIN
        :rtype: int
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def TotalAmount(self):
        """Voucher quota
        :rtype: float
        """
        return self._TotalAmount

    @TotalAmount.setter
    def TotalAmount(self, TotalAmount):
        self._TotalAmount = TotalAmount

    @property
    def RemainAmount(self):
        """Voucher amount
        :rtype: float
        """
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
        """Customer UIN list. Array length value: 1-20.
        :rtype: list of int non-negative
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """Customer voucher quota information
        :rtype: list of QueryVoucherAmountByUinItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """Customer UIN
        :rtype: int
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def TotalCount(self):
        """The total number of vouchers
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        """Voucher details
        :rtype: list of QueryVoucherListByUinVoucherItem
        """
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
        """Customer UIN list. Array length value: 1-20.
        :rtype: list of int non-negative
        """
        return self._ClientUins

    @ClientUins.setter
    def ClientUins(self, ClientUins):
        self._ClientUins = ClientUins

    @property
    def Status(self):
        """Voucher status. If this parameter is not passed in, all status will be queried by default. Valid values: `Unused`, `Used`, `Expired`.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """Customer voucher information
        :rtype: list of QueryVoucherListByUinItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """Voucher ID
        :rtype: str
        """
        return self._VoucherId

    @VoucherId.setter
    def VoucherId(self, VoucherId):
        self._VoucherId = VoucherId

    @property
    def VoucherStatus(self):
        """Voucher status
        :rtype: str
        """
        return self._VoucherStatus

    @VoucherStatus.setter
    def VoucherStatus(self, VoucherStatus):
        self._VoucherStatus = VoucherStatus

    @property
    def TotalAmount(self):
        """Voucher value
        :rtype: float
        """
        return self._TotalAmount

    @TotalAmount.setter
    def TotalAmount(self, TotalAmount):
        self._TotalAmount = TotalAmount

    @property
    def RemainAmount(self):
        """Balance
        :rtype: float
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """Reseller name
        :rtype: str
        """
        return self._AgentName

    @AgentName.setter
    def AgentName(self, AgentName):
        self._AgentName = AgentName

    @property
    def AccountType(self):
        """Reseller role type (1: Reseller; 2: Distributor; 3: Second-level reseller)
        :rtype: int
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def TotalQuota(self):
        """Total quota
        :rtype: float
        """
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def RemainingQuota(self):
        """Remaining quota
        :rtype: float
        """
        return self._RemainingQuota

    @RemainingQuota.setter
    def RemainingQuota(self, RemainingQuota):
        self._RemainingQuota = RemainingQuota

    @property
    def IssuedNum(self):
        """The number of issued vouchers
        :rtype: int
        """
        return self._IssuedNum

    @IssuedNum.setter
    def IssuedNum(self, IssuedNum):
        self._IssuedNum = IssuedNum

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _RegionId: Region id.
        :type RegionId: str
        :param _RegionName: Region name.
        :type RegionName: str
        :param _OriginalCost: Actual total consumption, up to 8 decimal places.
        :type OriginalCost: str
        :param _VoucherPayAmount: Voucher payment amount, up to 8 decimal places.
        :type VoucherPayAmount: str
        :param _TotalCost: Total consumption, up to 8 decimal places.
        :type TotalCost: str
        """
        self._RegionId = None
        self._RegionName = None
        self._OriginalCost = None
        self._VoucherPayAmount = None
        self._TotalCost = None

    @property
    def RegionId(self):
        """Region id.
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """Region name.
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def OriginalCost(self):
        """Actual total consumption, up to 8 decimal places.
        :rtype: str
        """
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def VoucherPayAmount(self):
        """Voucher payment amount, up to 8 decimal places.
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TotalCost(self):
        """Total consumption, up to 8 decimal places.
        :rtype: str
        """
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
        


class SendVerifyCodeRequest(AbstractModel):
    """SendVerifyCode request structure.

    """

    def __init__(self):
        r"""
        :param _CountryCode: Country code.
Parameter value is not allowed to be 7,380,86.
        :type CountryCode: str
        :param _PhoneNum: Mobile number.
The caller needs to ensure the validity and correctness of the mobile number. A global mobile number within a range of 1-32 digits is allowed.No need to add CountryCode before mobile number.
        :type PhoneNum: str
        """
        self._CountryCode = None
        self._PhoneNum = None

    @property
    def CountryCode(self):
        """Country code.
Parameter value is not allowed to be 7,380,86.
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def PhoneNum(self):
        """Mobile number.
The caller needs to ensure the validity and correctness of the mobile number. A global mobile number within a range of 1-32 digits is allowed.No need to add CountryCode before mobile number.
        :rtype: str
        """
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum


    def _deserialize(self, params):
        self._CountryCode = params.get("CountryCode")
        self._PhoneNum = params.get("PhoneNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendVerifyCodeResponse(AbstractModel):
    """SendVerifyCode response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SummaryDetails(AbstractModel):
    """Detailed summary by billing dimension

    """

    def __init__(self):
        r"""
        :param _Business: Product information list.
        :type Business: list of BusinessInfo
        :param _OriginalCost: Original price.
        :type OriginalCost: str
        :param _VoucherPayAmount: Voucher amount.
        :type VoucherPayAmount: str
        :param _RICost: RI deduction.
        :type RICost: str
        :param _TotalCost: <TOTAL_AMOUNT>.
        :type TotalCost: str
        :param _GroupKey: Classification dimension summary key.
        :type GroupKey: str
        :param _GroupValue: Summary value by classification dimension.
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
        """Product information list.
        :rtype: list of BusinessInfo
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def OriginalCost(self):
        """Original price.
        :rtype: str
        """
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def VoucherPayAmount(self):
        """Voucher amount.
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def RICost(self):
        """RI deduction.
        :rtype: str
        """
        return self._RICost

    @RICost.setter
    def RICost(self, RICost):
        self._RICost = RICost

    @property
    def TotalCost(self):
        """<TOTAL_AMOUNT>.
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def GroupKey(self):
        """Classification dimension summary key.
        :rtype: str
        """
        return self._GroupKey

    @GroupKey.setter
    def GroupKey(self, GroupKey):
        self._GroupKey = GroupKey

    @property
    def GroupValue(self):
        """Summary value by classification dimension.
        :rtype: str
        """
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
        :param _TagKey: Tag key.
        :type TagKey: str
        :param _TagValue: Tag value.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """Tag key.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value.
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
        


class TradeOneNode(AbstractModel):
    """Primary Industry Information

    """

    def __init__(self):
        r"""
        :param _Id: Layer-1 industry id.
        :type Id: str
        :param _Name: Layer-1 industry name.
        :type Name: str
        :param _Children: Layer-2 industries corresponding to the layer-1 industry.
        :type Children: list of TradeTwoNode
        """
        self._Id = None
        self._Name = None
        self._Children = None

    @property
    def Id(self):
        """Layer-1 industry id.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Layer-1 industry name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Children(self):
        """Layer-2 industries corresponding to the layer-1 industry.
        :rtype: list of TradeTwoNode
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = TradeTwoNode()
                obj._deserialize(item)
                self._Children.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TradeTwoNode(AbstractModel):
    """Secondary Industry Information

    """

    def __init__(self):
        r"""
        :param _Id: Secondary industry id.
        :type Id: str
        :param _Name: Secondary industry name.
        :type Name: str
        :param _TradeInfo: Industry information.
        :type TradeInfo: str
        """
        self._Id = None
        self._Name = None
        self._TradeInfo = None

    @property
    def Id(self):
        """Secondary industry id.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Secondary industry name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TradeInfo(self):
        """Industry information.
        :rtype: str
        """
        return self._TradeInfo

    @TradeInfo.setter
    def TradeInfo(self, TradeInfo):
        self._TradeInfo = TradeInfo


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._TradeInfo = params.get("TradeInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        