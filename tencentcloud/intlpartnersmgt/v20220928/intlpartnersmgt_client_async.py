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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.intlpartnersmgt.v20220928 import models
from typing import Dict


class IntlpartnersmgtClient(AbstractClient):
    _apiVersion = '2022-09-28'
    _endpoint = 'intlpartnersmgt.intl.tencentcloudapi.com'
    _service = 'intlpartnersmgt'

    async def AllocateCreditPool(
            self,
            request: models.AllocateCreditPoolRequest,
            opts: Dict = None,
    ) -> models.AllocateCreditPoolResponse:
        """
        This API is used to allocate credit pools to second-level resellers by distributors.
        Callable roles: Distributor
        """
        
        kwargs = {}
        kwargs["action"] = "AllocateCreditPool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AllocateCreditPoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AllocateCustomerCredit(
            self,
            request: models.AllocateCustomerCreditRequest,
            opts: Dict = None,
    ) -> models.AllocateCustomerCreditResponse:
        """
        This API is used for a partner to set credit for a customer, such as increasing or lowering the credit and setting it to 0.
        1. The credit is valid permanently and will not be zeroed regularly.
        2. The customer's service will be suspended when its available credit is set to 0, so caution should be exercised with this operation.
        3. To prevent the customer from making new purchases without affecting their use of previously purchased products, the partner can set their available credit to 0 after obtaining the non-stop feature privilege from the channel manager.
        4. The set credit is an increment of the current available credit and cannot exceed the remaining allocable credit. Setting the credit to a negative value indicates that it will be repossessed. The available credit can be set to 0 at the minimum.

        Callable roles: Distributor, Second-level reseller, Reseller
        """
        
        kwargs = {}
        kwargs["action"] = "AllocateCustomerCredit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AllocateCustomerCreditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApproveClientApply(
            self,
            request: models.ApproveClientApplyRequest,
            opts: Dict = None,
    ) -> models.ApproveClientApplyResponse:
        """
        Description: This API is used by resellers to review applications to become sub-customers. Note: This API is used to apply for the allowlist. If needed, please contact your business representative.

        Callable roles: Reseller, Distributer, Second-level reseller
        """
        
        kwargs = {}
        kwargs["action"] = "ApproveClientApply"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApproveClientApplyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApproveSubAgentApply(
            self,
            request: models.ApproveSubAgentApplyRequest,
            opts: Dict = None,
    ) -> models.ApproveSubAgentApplyResponse:
        """
        This API is used to approve applications for second-level resellers.
        Invocation Role: Distributor.
        """
        
        kwargs = {}
        kwargs["action"] = "ApproveSubAgentApply"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApproveSubAgentApplyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccount(
            self,
            request: models.CreateAccountRequest,
            opts: Dict = None,
    ) -> models.CreateAccountResponse:
        """
        This API is used to create Tencent Cloud customer accounts for distributor/second-level resellers.After the account is created, it will be automatically bound to the partner account.Note:
        1. Create a Tencent Cloud account. The entered email address and mobile phone number need to be verified by the partner for validity.
        2. Customers need to add personal information when logging in for the first time.
        3. This interface needs to be applied for allowlist usage. Please contact the channel manager to initiate the application process.

        Callable roles: Distributor, Second-level reseller, Reseller
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAndSendClientInvitationMail(
            self,
            request: models.CreateAndSendClientInvitationMailRequest,
            opts: Dict = None,
    ) -> models.CreateAndSendClientInvitationMailResponse:
        """
        This API is used to perform operations. Application for allowlist is required before usage. If needed, contact your business representative to request allowlisting. The specific usage process is as follows;.
        This API is used to create an invitation link. You can send the invitation link to your designated email address.
        2. Customers need to click the invitation link in the mailbox, fill in and submit relevant information.
        3. After customer submission, you can view the application of this sub-customer on the customer management page and review it.

        This API is used to handle cases where if the designated mailbox does not receive the invitation link, you can send the invitation link returned by the API to the customer manually.
        Invocation roles: resellers, distributors, second-level reseller.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAndSendClientInvitationMail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAndSendClientInvitationMailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillDetail(
            self,
            request: models.DescribeBillDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBillDetailResponse:
        """
        Description: End-customer queries its own bill details.
        Callable role: End-customer.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillDownloadUrl(
            self,
            request: models.DescribeBillDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeBillDownloadUrlResponse:
        """
        Description: This API is used to download billing files and return billing file URLs for sub-customers.
        Callable role: Enb-customer.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummary(
            self,
            request: models.DescribeBillSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryResponse:
        """
        Description: External API for L1 billing of Sub-customer billing center.
        Callable role: End-customer.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummaryByPayMode(
            self,
            request: models.DescribeBillSummaryByPayModeRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryByPayModeResponse:
        """
        This API is used to obtain the total amount of customer bills by payment mode.
        Callable roles: Distributor, Second-level reseller, Reseller
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummaryByPayMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryByPayModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummaryByProduct(
            self,
            request: models.DescribeBillSummaryByProductRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryByProductResponse:
        """
        Description: Obtain the summarized value of sub - account bills by product dimension.
        Callable roles: Distributor, Second-level reseller, Reseller
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummaryByProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryByProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummaryByRegion(
            self,
            request: models.DescribeBillSummaryByRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryByRegionResponse:
        """
        Description: Obtain the summarized value of sub - account bills by region through API.
        Callable roles: Distributor, Second-level reseller, Reseller
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummaryByRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryByRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomerBillDetail(
            self,
            request: models.DescribeCustomerBillDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomerBillDetailResponse:
        """
        This API is used to query the customer bill details by resellers.
        Callable roles: Distributor, Second-level reseller, Reseller.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomerBillDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomerBillDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomerBillDetailByDay(
            self,
            request: models.DescribeCustomerBillDetailByDayRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomerBillDetailByDayResponse:
        """
        This API is used to query the daily bill expenditure of customer by resellers.
        Invocation Role: first-level reseller, second-level reseller, reseller.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomerBillDetailByDay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomerBillDetailByDayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomerBillDownloadUrl(
            self,
            request: models.DescribeCustomerBillDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomerBillDownloadUrlResponse:
        """
        This API is used to get the URL for downloading the customer bill file by reseller. The download conditions are as follows:
        1. Detailed bills (billDetail and billDetailPack) can be downloaded starting from June 2022; resource bills (billResource and billResourcePack) can be downloaded starting from November 2023.
        2. Bill packages (billDetailPack and billResourcePack) can only be downloaded after billing.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomerBillDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomerBillDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomerBillSummary(
            self,
            request: models.DescribeCustomerBillSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomerBillSummaryResponse:
        """
        This API is used to query the total amount of customer bills.
        Callable roles: Distributor, Second-level reseller, Reseller
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomerBillSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomerBillSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomerInfo(
            self,
            request: models.DescribeCustomerInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomerInfoResponse:
        """
        This API is used to query sub-customer information.
        Invocation roles: reseller, first-level distributor.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomerInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomerInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomerOwnVoucherList(
            self,
            request: models.DescribeCustomerOwnVoucherListRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomerOwnVoucherListResponse:
        """
        This API is used to query the voucher list by Customer.
        Callable roles: Customer.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomerOwnVoucherList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomerOwnVoucherListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomerUin(
            self,
            request: models.DescribeCustomerUinRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomerUinResponse:
        """
        This API is used to query the list of customer UINs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomerUin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomerUinResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomerVoucherList(
            self,
            request: models.DescribeCustomerVoucherListRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomerVoucherListResponse:
        """
        This API is used to query the customer voucher list by Reseller, Second-level Reseller or Distributor.
        Callable roles: Reseller, Second-level Reseller or Distributor.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomerVoucherList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomerVoucherListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRebateDownloadUrl(
            self,
            request: models.DescribeRebateDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeRebateDownloadUrlResponse:
        """
        This API is used to download the commission bill file by resellers/agents. The file URL is returned.
        Resellers/Agents can call this API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRebateDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRebateDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ForceQN(
            self,
            request: models.ForceQNRequest,
            opts: Dict = None,
    ) -> models.ForceQNResponse:
        """
        Forced Service Suspension settings and cancellation can be used only after the reseller is whitelisted.

        Callable roles: Distributor, Second-level reseller, Reseller
        """
        
        kwargs = {}
        kwargs["action"] = "ForceQN"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ForceQNResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCountryCodes(
            self,
            request: models.GetCountryCodesRequest,
            opts: Dict = None,
    ) -> models.GetCountryCodesResponse:
        """
        This API is used to obtain country/region codes.
        """
        
        kwargs = {}
        kwargs["action"] = "GetCountryCodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCountryCodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTradeConfigList(
            self,
            request: models.GetTradeConfigListRequest,
            opts: Dict = None,
    ) -> models.GetTradeConfigListResponse:
        """
        This API is used to query industry information, including layer-1 industry and layer-2 industry.

        Callable roles: Distributor, Second-level reseller, Reseller,End-customer
        """
        
        kwargs = {}
        kwargs["action"] = "GetTradeConfigList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTradeConfigListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClientRemark(
            self,
            request: models.ModifyClientRemarkRequest,
            opts: Dict = None,
    ) -> models.ModifyClientRemarkResponse:
        """
        This API is used to modify customer remarks.

        Callable roles: Distributor, Second-level reseller, Reseller
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClientRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClientRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryAccountVerificationStatus(
            self,
            request: models.QueryAccountVerificationStatusRequest,
            opts: Dict = None,
    ) -> models.QueryAccountVerificationStatusResponse:
        """
        This API is used to query the account verification status.
        Callable roles: Distributor, Reseller
        """
        
        kwargs = {}
        kwargs["action"] = "QueryAccountVerificationStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryAccountVerificationStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryCreditAllocationHistory(
            self,
            request: models.QueryCreditAllocationHistoryRequest,
            opts: Dict = None,
    ) -> models.QueryCreditAllocationHistoryResponse:
        """
        This API is used to query all the credit allocation records of a single customer.
        Callable roles: Distributor, Second-level reseller, Reseller
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCreditAllocationHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCreditAllocationHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryCreditByUinList(
            self,
            request: models.QueryCreditByUinListRequest,
            opts: Dict = None,
    ) -> models.QueryCreditByUinListResponse:
        """
        This API is used to query the credit of users in the list.
        Callable roles: Distributor, Second-level reseller, Reseller
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCreditByUinList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCreditByUinListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryCustomerBillingQuota(
            self,
            request: models.QueryCustomerBillingQuotaRequest,
            opts: Dict = None,
    ) -> models.QueryCustomerBillingQuotaResponse:
        """
        Description: This API is used for a sub-customer to real-time query its own total credit and remaining credit in USD.

        Callable roles: Sub-customer
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCustomerBillingQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCustomerBillingQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryCustomersCredit(
            self,
            request: models.QueryCustomersCreditRequest,
            opts: Dict = None,
    ) -> models.QueryCustomersCreditResponse:
        """
        This API is used for a partner to the credits and basic information of cutomers.

        Callable roles: Distributor, Second-level reseller, Reseller
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCustomersCredit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCustomersCreditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryDirectCustomersCredit(
            self,
            request: models.QueryDirectCustomersCreditRequest,
            opts: Dict = None,
    ) -> models.QueryDirectCustomersCreditResponse:
        """
        This API is used to query the credits of direct customers.
        Callable roles: Distributor, Second-level reseller, Reseller
        """
        
        kwargs = {}
        kwargs["action"] = "QueryDirectCustomersCredit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryDirectCustomersCreditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryInvitationInfo(
            self,
            request: models.QueryInvitationInfoRequest,
            opts: Dict = None,
    ) -> models.QueryInvitationInfoResponse:
        """
        Query usage information of invitation link. Invitation link is valid for 30 days.And once created, the data will only be retained for 60 days, and the system will automatically delete the invitation link after 60 days.
        Invokable role types: Distributor, Second-level reseller, Reseller.
        """
        
        kwargs = {}
        kwargs["action"] = "QueryInvitationInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryInvitationInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryPartnerCredit(
            self,
            request: models.QueryPartnerCreditRequest,
            opts: Dict = None,
    ) -> models.QueryPartnerCreditResponse:
        """
        This API is used for a partner to query its own total credit, available credit, and used credit in USD.

        Callable roles: Distributor, Second-level reseller, Reseller
        """
        
        kwargs = {}
        kwargs["action"] = "QueryPartnerCredit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryPartnerCreditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryPendingClientsV2(
            self,
            request: models.QueryPendingClientsV2Request,
            opts: Dict = None,
    ) -> models.QueryPendingClientsV2Response:
        """
        Description: This API is used by resellers to query the list of sub-customers pending review. Note: This API is used to apply for the allowlist. If needed, please contact your business representative.

        Callable roles: Reseller, Distributer, Second-level reseller
        """
        
        kwargs = {}
        kwargs["action"] = "QueryPendingClientsV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryPendingClientsV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryPendingSubAgentsV2(
            self,
            request: models.QueryPendingSubAgentsV2Request,
            opts: Dict = None,
    ) -> models.QueryPendingSubAgentsV2Response:
        """
        This API is used to query information of second-level resellers in application.
        Invocation Role: Distributor.
        """
        
        kwargs = {}
        kwargs["action"] = "QueryPendingSubAgentsV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryPendingSubAgentsV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryPolicyProductListByCode(
            self,
            request: models.QueryPolicyProductListByCodeRequest,
            opts: Dict = None,
    ) -> models.QueryPolicyProductListByCodeResponse:
        """
        This API is used to query the product list information within the specified policy range. To call this API, contact your business manager to apply for adding it to the allowlist.
        Callable roles: Distributor, Second-level reseller, Reseller
        """
        
        kwargs = {}
        kwargs["action"] = "QueryPolicyProductListByCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryPolicyProductListByCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QuerySubAgentsDetailV2(
            self,
            request: models.QuerySubAgentsDetailV2Request,
            opts: Dict = None,
    ) -> models.QuerySubAgentsDetailV2Response:
        """
        This API is used to query information of second-level resellers.
        Invocation Role:Distributor.
        """
        
        kwargs = {}
        kwargs["action"] = "QuerySubAgentsDetailV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QuerySubAgentsDetailV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryT1IndirectCustomersDetail(
            self,
            request: models.QueryT1IndirectCustomersDetailRequest,
            opts: Dict = None,
    ) -> models.QueryT1IndirectCustomersDetailResponse:
        """
        This API is used to query the indirect sub-customers of a distributor.
        Invokable role type: Distributor
        """
        
        kwargs = {}
        kwargs["action"] = "QueryT1IndirectCustomersDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryT1IndirectCustomersDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryVoucherAmountByUin(
            self,
            request: models.QueryVoucherAmountByUinRequest,
            opts: Dict = None,
    ) -> models.QueryVoucherAmountByUinResponse:
        """
        This API is used by primary/secondary resellers to query the voucher quota based on the customer UIN.
        Callable roles: Reseller, Distributor, Second-level reseller
        """
        
        kwargs = {}
        kwargs["action"] = "QueryVoucherAmountByUin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryVoucherAmountByUinResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryVoucherListByUin(
            self,
            request: models.QueryVoucherListByUinRequest,
            opts: Dict = None,
    ) -> models.QueryVoucherListByUinResponse:
        """
        This API is used by primary/secondary resellers to query the voucher list based on the customer UIN.
        Callable roles: Reseller, Distributor, Second-level reseller
        """
        
        kwargs = {}
        kwargs["action"] = "QueryVoucherListByUin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryVoucherListByUinResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryVoucherPool(
            self,
            request: models.QueryVoucherPoolRequest,
            opts: Dict = None,
    ) -> models.QueryVoucherPoolResponse:
        """
        This API is used by primary/secondary resellers to query the voucher quota pool.
        Callable roles: Distributor, First-level reseller, Second-level reseller
        """
        
        kwargs = {}
        kwargs["action"] = "QueryVoucherPool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryVoucherPoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendVerifyCode(
            self,
            request: models.SendVerifyCodeRequest,
            opts: Dict = None,
    ) -> models.SendVerifyCodeResponse:
        """
        This API is used to send a verification code for account registration.

        Callable roles: Distributor, Second-level reseller, Reseller,End-customer
        """
        
        kwargs = {}
        kwargs["action"] = "SendVerifyCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendVerifyCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)