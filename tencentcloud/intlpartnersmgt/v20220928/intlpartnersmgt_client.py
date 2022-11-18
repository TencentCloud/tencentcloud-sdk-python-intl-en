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
    _endpoint = 'intlpartnersmgt.tencentcloudapi.com'
    _service = 'intlpartnersmgt'


    def AllocateCustomerCredit(self, request):
        """This API is used for a partner to set credit for a customer, such as increasing or lowering the credit and setting it to 0.
        1. The credit is valid permanently and will not be zeroed regularly.
        2. The customer's service will be suspended when its available credit is set to 0, so caution should be exercised with this operation.
        3. To prevent the customer from making new purchases without affecting their use of previously purchased products, the partner can set their available credit to 0 after obtaining the non-stop feature privilege from the channel manager.
        4. The set credit is an increment of the current available credit and cannot exceed the remaining allocable credit. Setting the credit to a negative value indicates that it will be repossessed. The available credit can be set to 0 at the minimum.

        :param request: Request instance for AllocateCustomerCredit.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.AllocateCustomerCreditRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.AllocateCustomerCreditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AllocateCustomerCredit", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AllocateCustomerCreditResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAccount(self, request):
        """This API is used to create a Tencent Cloud account on the partner platform for a customer. After registration, the customer will be automatically bound to the partner account.

        Notes:<br>
        1. The partner should verify the entered email address and mobile number for creating a Tencent Cloud account.<br>
        2. The customer needs to complete personal information after the first login.

        :param request: Request instance for CreateAccount.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.CreateAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccount", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.GetCountryCodesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryCreditAllocationHistory(self, request):
        """This API is used to query all the credit allocation records of a single customer.

        :param request: Request instance for QueryCreditAllocationHistory.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCreditAllocationHistoryRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCreditAllocationHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCreditAllocationHistory", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryCreditAllocationHistoryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryCreditByUinList(self, request):
        """This API is used to query the credit of users in the list.

        :param request: Request instance for QueryCreditByUinList.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCreditByUinListRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCreditByUinListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCreditByUinList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryCreditByUinListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryCustomersCredit(self, request):
        """This API is used for a partner to the credits and basic information of cutomers.

        :param request: Request instance for QueryCustomersCredit.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCustomersCreditRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCustomersCreditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCustomersCredit", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryCustomersCreditResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryDirectCustomersCredit(self, request):
        """This API is used to query the credits of direct customers.

        :param request: Request instance for QueryDirectCustomersCredit.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryDirectCustomersCreditRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryDirectCustomersCreditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryDirectCustomersCredit", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryDirectCustomersCreditResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryPartnerCredit(self, request):
        """This API is used for a partner to query its own total credit, available credit, and used credit in USD.

        :param request: Request instance for QueryPartnerCredit.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryPartnerCreditRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryPartnerCreditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryPartnerCredit", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryPartnerCreditResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)