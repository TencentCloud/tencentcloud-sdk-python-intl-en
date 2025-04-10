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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.intlpartnersmgt.v20220928 import models


class IntlpartnersmgtClient(AbstractClient):
    _apiVersion = '2022-09-28'
    _endpoint = 'intlpartnersmgt.intl.tencentcloudapi.com'
    _service = 'intlpartnersmgt'


    def AllocateCreditPool(self, request):
        """This API is used to allocate credit pools to second-level resellers by distributors.
        Callable roles: Distributor

        :param request: Request instance for AllocateCreditPool.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.AllocateCreditPoolRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.AllocateCreditPoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AllocateCreditPool", params, headers=headers)
            response = json.loads(body)
            model = models.AllocateCreditPoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AllocateCustomerCredit(self, request):
        """This API is used for a partner to set credit for a customer, such as increasing or lowering the credit and setting it to 0.
        1. The credit is valid permanently and will not be zeroed regularly.
        2. The customer's service will be suspended when its available credit is set to 0, so caution should be exercised with this operation.
        3. To prevent the customer from making new purchases without affecting their use of previously purchased products, the partner can set their available credit to 0 after obtaining the non-stop feature privilege from the channel manager.
        4. The set credit is an increment of the current available credit and cannot exceed the remaining allocable credit. Setting the credit to a negative value indicates that it will be repossessed. The available credit can be set to 0 at the minimum.

        Callable roles: Distributor, Second-level reseller, Reseller

        :param request: Request instance for AllocateCustomerCredit.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.AllocateCustomerCreditRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.AllocateCustomerCreditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AllocateCustomerCredit", params, headers=headers)
            response = json.loads(body)
            model = models.AllocateCustomerCreditResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ApproveClientApply(self, request):
        """Description: This API is used by resellers to review applications to become sub-customers. Note: This API is used to apply for the allowlist. If needed, please contact your business representative.

        Callable roles: Reseller, Distributer, Second-level reseller

        :param request: Request instance for ApproveClientApply.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.ApproveClientApplyRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.ApproveClientApplyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApproveClientApply", params, headers=headers)
            response = json.loads(body)
            model = models.ApproveClientApplyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccount(self, request):
        """This API is used to create Tencent Cloud customer accounts for distributor/second-level resellers.After the account is created, it will be automatically bound to the partner account.Note:
        1. Create a Tencent Cloud account. The entered email address and mobile phone number need to be verified by the partner for validity.
        2. Customers need to add personal information when logging in for the first time.
        3. This interface needs to be applied for allowlist usage. Please contact the channel manager to initiate the application process.

        Callable roles: Distributor, Second-level reseller, Reseller

        :param request: Request instance for CreateAccount.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.CreateAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAndSendClientInvitationMail(self, request):
        """This API is used to apply for the allowlist. If needed, please contact your business representative.Directions:
        1.This API is used to create an invitation link, which you can send to a specified email address.
        2.Customer need to click the invitation link in the email, fill in and submit the required information.
        3.You can review the customer's application in customer management  after submission.

        Note:This API is used to manually send the invitation link to the customer if the specified email does not receive it.

        Callable roles: Distributor, Second-level reseller, Reseller

        :param request: Request instance for CreateAndSendClientInvitationMail.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.CreateAndSendClientInvitationMailRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.CreateAndSendClientInvitationMailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAndSendClientInvitationMail", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAndSendClientInvitationMailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillDetail(self, request):
        """Description: End-customer queries its own bill details.
        Callable role: End-customer.

        :param request: Request instance for DescribeBillDetail.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeBillDetailRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeBillDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillDownloadUrl(self, request):
        """Description: This API is used to download billing files and return billing file URLs for sub-customers.
        Callable role: Enb-customer.

        :param request: Request instance for DescribeBillDownloadUrl.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeBillDownloadUrlRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeBillDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummary(self, request):
        """Description: External API for L1 billing of Sub-customer billing center.
        Callable role: End-customer.

        :param request: Request instance for DescribeBillSummary.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeBillSummaryRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeBillSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummaryByPayMode(self, request):
        """This API is used to obtain the total amount of customer bills by payment mode.
        Callable roles: Distributor, Second-level reseller, Reseller

        :param request: Request instance for DescribeBillSummaryByPayMode.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeBillSummaryByPayModeRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeBillSummaryByPayModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummaryByPayMode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryByPayModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummaryByProduct(self, request):
        """Description: Obtain the summarized value of sub - account bills by product dimension.
        Callable roles: Distributor, Second-level reseller, Reseller

        :param request: Request instance for DescribeBillSummaryByProduct.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeBillSummaryByProductRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeBillSummaryByProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummaryByProduct", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryByProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummaryByRegion(self, request):
        """Description: Obtain the summarized value of sub - account bills by region through API.
        Callable roles: Distributor, Second-level reseller, Reseller

        :param request: Request instance for DescribeBillSummaryByRegion.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeBillSummaryByRegionRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeBillSummaryByRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummaryByRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryByRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomerBillDetail(self, request):
        """This API is used to query the customer bill details by resellers.
        Callable roles: Distributor, Second-level reseller, Reseller

        :param request: Request instance for DescribeCustomerBillDetail.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeCustomerBillDetailRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeCustomerBillDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomerBillDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomerBillDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomerBillDownloadUrl(self, request):
        """This API is used to get the URL for downloading the customer bill file by reseller. The download conditions are as follows:
        1. Detailed bills (billDetail and billDetailPack) can be downloaded starting from June 2022; resource bills (billResource and billResourcePack) can be downloaded starting from November 2023.
        2. Bill packages (billDetailPack and billResourcePack) can only be downloaded after billing.

        :param request: Request instance for DescribeCustomerBillDownloadUrl.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeCustomerBillDownloadUrlRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeCustomerBillDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomerBillDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomerBillDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomerBillSummary(self, request):
        """This API is used to query the total amount of customer bills.
        Callable roles: Distributor, Second-level reseller, Reseller

        :param request: Request instance for DescribeCustomerBillSummary.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeCustomerBillSummaryRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeCustomerBillSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomerBillSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomerBillSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomerInfo(self, request):
        """This API is used to query the customer information.

        Callable roles: Distributor, Reseller

        :param request: Request instance for DescribeCustomerInfo.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeCustomerInfoRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeCustomerInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomerInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomerInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomerUin(self, request):
        """This API is used to query the list of customer UINs.

        :param request: Request instance for DescribeCustomerUin.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeCustomerUinRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.DescribeCustomerUinResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomerUin", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomerUinResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ForceQN(self, request):
        """Forced Service Suspension settings and cancellation can be used only after the reseller is whitelisted.

        Callable roles: Distributor, Second-level reseller, Reseller

        :param request: Request instance for ForceQN.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.ForceQNRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.ForceQNResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ForceQN", params, headers=headers)
            response = json.loads(body)
            model = models.ForceQNResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCountryCodes(self, request):
        """This API is used to obtain country/region codes.

        :param request: Request instance for GetCountryCodes.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.GetCountryCodesRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.GetCountryCodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCountryCodes", params, headers=headers)
            response = json.loads(body)
            model = models.GetCountryCodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTradeConfigList(self, request):
        """This API is used to query industry information, including layer-1 industry and layer-2 industry.

        Callable roles: Distributor, Second-level reseller, Reseller,End-customer

        :param request: Request instance for GetTradeConfigList.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.GetTradeConfigListRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.GetTradeConfigListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTradeConfigList", params, headers=headers)
            response = json.loads(body)
            model = models.GetTradeConfigListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClientRemark(self, request):
        """This API is used to modify customer remarks.

        Callable roles: Distributor, Second-level reseller, Reseller

        :param request: Request instance for ModifyClientRemark.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.ModifyClientRemarkRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.ModifyClientRemarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClientRemark", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClientRemarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryAccountVerificationStatus(self, request):
        """This API is used to query the account verification status.
        Callable roles: Distributor, Reseller

        :param request: Request instance for QueryAccountVerificationStatus.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryAccountVerificationStatusRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryAccountVerificationStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryAccountVerificationStatus", params, headers=headers)
            response = json.loads(body)
            model = models.QueryAccountVerificationStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryCreditAllocationHistory(self, request):
        """This API is used to query all the credit allocation records of a single customer.
        Callable roles: Distributor, Second-level reseller, Reseller

        :param request: Request instance for QueryCreditAllocationHistory.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCreditAllocationHistoryRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCreditAllocationHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCreditAllocationHistory", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCreditAllocationHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryCreditByUinList(self, request):
        """This API is used to query the credit of users in the list.
        Callable roles: Distributor, Second-level reseller, Reseller

        :param request: Request instance for QueryCreditByUinList.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCreditByUinListRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCreditByUinListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCreditByUinList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCreditByUinListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryCustomerBillingQuota(self, request):
        """Description: This API is used for a sub-customer to real-time query its own total credit and remaining credit in USD.

        Callable roles: Sub-customer

        :param request: Request instance for QueryCustomerBillingQuota.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCustomerBillingQuotaRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCustomerBillingQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCustomerBillingQuota", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCustomerBillingQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryCustomersCredit(self, request):
        """This API is used for a partner to the credits and basic information of cutomers.

        Callable roles: Distributor, Second-level reseller, Reseller

        :param request: Request instance for QueryCustomersCredit.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCustomersCreditRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCustomersCreditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCustomersCredit", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCustomersCreditResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryDirectCustomersCredit(self, request):
        """This API is used to query the credits of direct customers.
        Callable roles: Distributor, Second-level reseller, Reseller

        :param request: Request instance for QueryDirectCustomersCredit.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryDirectCustomersCreditRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryDirectCustomersCreditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryDirectCustomersCredit", params, headers=headers)
            response = json.loads(body)
            model = models.QueryDirectCustomersCreditResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryInvitationInfo(self, request):
        """Query usage information of invitation link. Once created, the data will only be retained for 60 days, and the system will automatically delete the invitation link after 60 days.
        Invokable role types: Distributor, Second-level reseller, Reseller.

        :param request: Request instance for QueryInvitationInfo.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryInvitationInfoRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryInvitationInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryInvitationInfo", params, headers=headers)
            response = json.loads(body)
            model = models.QueryInvitationInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryPartnerCredit(self, request):
        """This API is used for a partner to query its own total credit, available credit, and used credit in USD.

        Callable roles: Distributor, Second-level reseller, Reseller

        :param request: Request instance for QueryPartnerCredit.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryPartnerCreditRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryPartnerCreditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryPartnerCredit", params, headers=headers)
            response = json.loads(body)
            model = models.QueryPartnerCreditResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryPendingClientsV2(self, request):
        """Description: This API is used by resellers to query the list of sub-customers pending review. Note: This API is used to apply for the allowlist. If needed, please contact your business representative.

        Callable roles: Reseller, Distributer, Second-level reseller

        :param request: Request instance for QueryPendingClientsV2.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryPendingClientsV2Request`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryPendingClientsV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryPendingClientsV2", params, headers=headers)
            response = json.loads(body)
            model = models.QueryPendingClientsV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryPolicyProductListByCode(self, request):
        """This API is used to query the product list information within the specified policy range. To call this API, contact your business manager to apply for adding it to the allowlist.
        Callable roles: Distributor, Second-level reseller, Reseller

        :param request: Request instance for QueryPolicyProductListByCode.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryPolicyProductListByCodeRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryPolicyProductListByCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryPolicyProductListByCode", params, headers=headers)
            response = json.loads(body)
            model = models.QueryPolicyProductListByCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryT1IndirectCustomersDetail(self, request):
        """This API is used to query the indirect sub-customers of a first-level distributor.
        Invokable role type: first-level reseller.

        :param request: Request instance for QueryT1IndirectCustomersDetail.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryT1IndirectCustomersDetailRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryT1IndirectCustomersDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryT1IndirectCustomersDetail", params, headers=headers)
            response = json.loads(body)
            model = models.QueryT1IndirectCustomersDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryVoucherAmountByUin(self, request):
        """This API is used by primary/secondary resellers to query the voucher quota based on the customer UIN.
        Callable roles: Reseller, Distributor, Second-level reseller

        :param request: Request instance for QueryVoucherAmountByUin.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryVoucherAmountByUinRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryVoucherAmountByUinResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryVoucherAmountByUin", params, headers=headers)
            response = json.loads(body)
            model = models.QueryVoucherAmountByUinResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryVoucherListByUin(self, request):
        """This API is used by primary/secondary resellers to query the voucher list based on the customer UIN.
        Callable roles: Reseller, Distributor, Second-level reseller

        :param request: Request instance for QueryVoucherListByUin.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryVoucherListByUinRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryVoucherListByUinResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryVoucherListByUin", params, headers=headers)
            response = json.loads(body)
            model = models.QueryVoucherListByUinResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryVoucherPool(self, request):
        """This API is used by primary/secondary resellers to query the voucher quota pool.
        Callable roles: Distributor, First-level reseller, Second-level reseller

        :param request: Request instance for QueryVoucherPool.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryVoucherPoolRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryVoucherPoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryVoucherPool", params, headers=headers)
            response = json.loads(body)
            model = models.QueryVoucherPoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendVerifyCode(self, request):
        """This API is used to send a verification code for account registration.

        Callable roles: Distributor, Second-level reseller, Reseller,End-customer

        :param request: Request instance for SendVerifyCode.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.SendVerifyCodeRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.SendVerifyCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendVerifyCode", params, headers=headers)
            response = json.loads(body)
            model = models.SendVerifyCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))