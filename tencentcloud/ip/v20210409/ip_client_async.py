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
from tencentcloud.ip.v20210409 import models
from typing import Dict


class IpClient(AbstractClient):
    _apiVersion = '2021-04-09'
    _endpoint = 'ip.intl.tencentcloudapi.com'
    _service = 'ip'

    async def AllocateCustomerCredit(
            self,
            request: models.AllocateCustomerCreditRequest,
            opts: Dict = None,
    ) -> models.AllocateCustomerCreditResponse:
        """
        This API is used for a partner to set credit for a customer, such as increasing or lowering the credit and setting it to 0.
        1. The credit is valid permanently and will not be zeroed regularly.
        2. The customer's service will be suspended when its available credit sets to 0, so caution should be exercised with this operation.
        3. To prevent the customer from making new purchases without affecting their use of previously purchased products, the partner can set their available credit to 0 after obtaining the non-stop feature privilege from the channel manager.
        4. The set credit is an increase to the current available credit and cannot exceed the remaining allocable credit. Setting the credit to a negative value indicates to repossess it. The available credit can be set to 0 at the minimum.
        """
        
        kwargs = {}
        kwargs["action"] = "AllocateCustomerCredit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AllocateCustomerCreditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccount(
            self,
            request: models.CreateAccountRequest,
            opts: Dict = None,
    ) -> models.CreateAccountResponse:
        """
        This API is used to create a Tencent Cloud account in the International Partner platform for a customer. After registration, the customer will be automatically bound to the partner account.

        Notes:<br>
        1. To create the Tencent Cloud account, the partner should enter and verify the customer’s email address and mobile number.<br>
        2. The customer needs to complete personal information after the first login.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCountryCodes(
            self,
            request: models.GetCountryCodesRequest,
            opts: Dict = None,
    ) -> models.GetCountryCodesResponse:
        """
        This API is used to obtain country and region codes.
        """
        
        kwargs = {}
        kwargs["action"] = "GetCountryCodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCountryCodesResponse
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
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCreditAllocationHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCreditAllocationHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryCustomersCredit(
            self,
            request: models.QueryCustomersCreditRequest,
            opts: Dict = None,
    ) -> models.QueryCustomersCreditResponse:
        """
        This API is used for a partner to query a customer's credit and basic information.
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCustomersCredit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCustomersCreditResponse
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
        """
        
        kwargs = {}
        kwargs["action"] = "QueryPartnerCredit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryPartnerCreditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)