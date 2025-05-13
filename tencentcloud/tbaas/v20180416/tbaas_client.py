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
from tencentcloud.tbaas.v20180416 import models


class TbaasClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'tbaas.intl.tencentcloudapi.com'
    _service = 'tbaas'


    def DescribeFabricBlock(self, request):
        """This API is used to retrieve the detailed information of a block in Fabric.

        :param request: Request instance for DescribeFabricBlock.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.DescribeFabricBlockRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.DescribeFabricBlockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFabricBlock", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFabricBlockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFabricTransaction(self, request):
        """This API is used to obtain detailed information of Fabric transactions.

        :param request: Request instance for DescribeFabricTransaction.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.DescribeFabricTransactionRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.DescribeFabricTransactionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFabricTransaction", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFabricTransactionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InvokeFabricChaincode(self, request):
        """This API is used to call a Fabric user contract to execute a transaction.

        :param request: Request instance for InvokeFabricChaincode.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.InvokeFabricChaincodeRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.InvokeFabricChaincodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InvokeFabricChaincode", params, headers=headers)
            response = json.loads(body)
            model = models.InvokeFabricChaincodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryFabricChaincode(self, request):
        """This API is used to make a user contract call in Fabric for querying.

        :param request: Request instance for QueryFabricChaincode.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.QueryFabricChaincodeRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.QueryFabricChaincodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFabricChaincode", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFabricChaincodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))