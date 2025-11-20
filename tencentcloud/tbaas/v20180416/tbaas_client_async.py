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
from tencentcloud.tbaas.v20180416 import models
from typing import Dict


class TbaasClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'tbaas.intl.tencentcloudapi.com'
    _service = 'tbaas'

    async def DescribeFabricBlock(
            self,
            request: models.DescribeFabricBlockRequest,
            opts: Dict = None,
    ) -> models.DescribeFabricBlockResponse:
        """
        This API is used to retrieve the detailed information of a block in Fabric.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFabricBlock"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFabricBlockResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFabricTransaction(
            self,
            request: models.DescribeFabricTransactionRequest,
            opts: Dict = None,
    ) -> models.DescribeFabricTransactionResponse:
        """
        This API is used to obtain detailed information of Fabric transactions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFabricTransaction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFabricTransactionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InvokeFabricChaincode(
            self,
            request: models.InvokeFabricChaincodeRequest,
            opts: Dict = None,
    ) -> models.InvokeFabricChaincodeResponse:
        """
        This API is used to call a Fabric user contract to execute a transaction.
        """
        
        kwargs = {}
        kwargs["action"] = "InvokeFabricChaincode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvokeFabricChaincodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFabricChaincode(
            self,
            request: models.QueryFabricChaincodeRequest,
            opts: Dict = None,
    ) -> models.QueryFabricChaincodeResponse:
        """
        This API is used to make a user contract call in Fabric for querying.
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFabricChaincode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFabricChaincodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)