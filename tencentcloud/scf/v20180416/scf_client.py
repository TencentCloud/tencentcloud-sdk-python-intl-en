# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.scf.v20180416 import models


class ScfClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'scf.tencentcloudapi.com'
    _service = 'scf'


    def CopyFunction(self, request):
        """This API is used to replicate a function. You can store the replicated function in a specified Region and Namespace.
        Note: This API **does not** replicate the following objects or attributes of the function:
        1. Function trigger
        2. Versions other than $LATEST
        3. CLS target of the logs configured in the function

        You can manually configure the function after replication as required.

        :param request: Request instance for CopyFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.CopyFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CopyFunctionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CopyFunction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CopyFunctionResponse()
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


    def CreateAlias(self, request):
        """This API is used to create an alias for a function version. You can use the alias to mark a specific function version such as DEV/RELEASE. You can also modify the version pointed to by the alias at any time.
        An alias must point to a master version and can point to an additional version at the same time. If you specify an alias when invoking a function, the request will be sent to the versions pointed to by the alias. You can configure the ratio between the master version and additional version during request sending.

        :param request: Request instance for CreateAlias.
        :type request: :class:`tencentcloud.scf.v20180416.models.CreateAliasRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CreateAliasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAlias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAliasResponse()
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


    def CreateFunction(self, request):
        """This API is used to create a function based on the input parameters.

        :param request: Request instance for CreateFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.CreateFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CreateFunctionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFunction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFunctionResponse()
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


    def CreateNamespace(self, request):
        """This API is used to create a namespace based on the input parameters.

        :param request: Request instance for CreateNamespace.
        :type request: :class:`tencentcloud.scf.v20180416.models.CreateNamespaceRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CreateNamespaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNamespace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNamespaceResponse()
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


    def CreateTrigger(self, request):
        """This API is used to create a trigger based on the input parameters.

        :param request: Request instance for CreateTrigger.
        :type request: :class:`tencentcloud.scf.v20180416.models.CreateTriggerRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CreateTriggerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTrigger", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTriggerResponse()
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


    def DeleteAlias(self, request):
        """This API is used to delete an alias of a function version.

        :param request: Request instance for DeleteAlias.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteAliasRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteAliasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAlias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAliasResponse()
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


    def DeleteFunction(self, request):
        """This API is used to delete a function based on the input parameters.

        :param request: Request instance for DeleteFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteFunctionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFunction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFunctionResponse()
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


    def DeleteLayerVersion(self, request):
        """This API is used to delete a specified version of a specified layer. The deleted version cannot be associated with a function, but the deletion does not affect functions that are referencing this layer.

        :param request: Request instance for DeleteLayerVersion.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteLayerVersionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteLayerVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLayerVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLayerVersionResponse()
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


    def DeleteNamespace(self, request):
        """This API is used to create a namespace based on the input parameters.

        :param request: Request instance for DeleteNamespace.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteNamespaceRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteNamespaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNamespace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNamespaceResponse()
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


    def DeleteProvisionedConcurrencyConfig(self, request):
        """This API is used to delete the provisioned concurrency configuration of a function version.

        :param request: Request instance for DeleteProvisionedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteProvisionedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteProvisionedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteProvisionedConcurrencyConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProvisionedConcurrencyConfigResponse()
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


    def DeleteReservedConcurrencyConfig(self, request):
        """This API is used to delete the reserved concurrency configuration of a function.

        :param request: Request instance for DeleteReservedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteReservedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteReservedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteReservedConcurrencyConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteReservedConcurrencyConfigResponse()
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


    def DeleteTrigger(self, request):
        """This API is used to delete an existing trigger based on the input parameters.

        :param request: Request instance for DeleteTrigger.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteTriggerRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteTriggerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTrigger", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTriggerResponse()
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


    def GetAccount(self, request):
        """This API is used to get the account information.

        :param request: Request instance for GetAccount.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetAccountRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetAccountResponse()
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


    def GetAlias(self, request):
        """This API is used to get the alias details such as the name, description, version, and routing information.

        :param request: Request instance for GetAlias.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetAliasRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetAliasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetAlias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetAliasResponse()
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


    def GetFunction(self, request):
        """This API is used to obtain function details, such as name, code, handler, associated trigger, and timeout.

        :param request: Request instance for GetFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetFunctionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetFunction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetFunctionResponse()
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


    def GetFunctionAddress(self, request):
        """This API is used to obtain the download address of the function code package.

        :param request: Request instance for GetFunctionAddress.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetFunctionAddressRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetFunctionAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetFunctionAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetFunctionAddressResponse()
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


    def GetFunctionEventInvokeConfig(self, request):
        """This API is used to get the async retry configuration of a function, including the number of retry attempts and message retention period.

        :param request: Request instance for GetFunctionEventInvokeConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetFunctionEventInvokeConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetFunctionEventInvokeConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetFunctionEventInvokeConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetFunctionEventInvokeConfigResponse()
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


    def GetFunctionLogs(self, request):
        """This API is used to return function running logs according to the specified log query criteria.

        :param request: Request instance for GetFunctionLogs.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetFunctionLogsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetFunctionLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetFunctionLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetFunctionLogsResponse()
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


    def GetLayerVersion(self, request):
        """This API is used to get the layer version details, including links used to download files in the layer.

        :param request: Request instance for GetLayerVersion.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetLayerVersionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetLayerVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetLayerVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetLayerVersionResponse()
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


    def GetProvisionedConcurrencyConfig(self, request):
        """This API is used to get the provisioned concurrency details of a function or its specified version.

        :param request: Request instance for GetProvisionedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetProvisionedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetProvisionedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetProvisionedConcurrencyConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetProvisionedConcurrencyConfigResponse()
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


    def GetReservedConcurrencyConfig(self, request):
        """This API is used to get the reserved concurrency details of a function.

        :param request: Request instance for GetReservedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetReservedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetReservedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetReservedConcurrencyConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetReservedConcurrencyConfigResponse()
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


    def Invoke(self, request):
        """This API is used to run a function.

        :param request: Request instance for Invoke.
        :type request: :class:`tencentcloud.scf.v20180416.models.InvokeRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.InvokeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Invoke", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InvokeResponse()
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


    def ListAliases(self, request):
        """This API is used to return the list of all aliases under a function. You can filter them by the specific function version.

        :param request: Request instance for ListAliases.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListAliasesRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListAliasesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListAliases", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAliasesResponse()
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


    def ListAsyncEvents(self, request):
        """This API is used to pull the list of async function events.

        :param request: Request instance for ListAsyncEvents.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListAsyncEventsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListAsyncEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListAsyncEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAsyncEventsResponse()
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


    def ListFunctions(self, request):
        """This API is used to return relevant function information based on the input query parameters.

        :param request: Request instance for ListFunctions.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListFunctionsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListFunctionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListFunctions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListFunctionsResponse()
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


    def ListLayerVersions(self, request):
        """This API is used to get the information of all versions of a specified layer.

        :param request: Request instance for ListLayerVersions.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListLayerVersionsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListLayerVersionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListLayerVersions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListLayerVersionsResponse()
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


    def ListLayers(self, request):
        """This API is used to return the list of all layers, including the information of the latest version of each layer. You can filter them by the compatible runtime.

        :param request: Request instance for ListLayers.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListLayersRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListLayersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListLayers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListLayersResponse()
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


    def ListNamespaces(self, request):
        """This API is used to display a namespace list.

        :param request: Request instance for ListNamespaces.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListNamespacesRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListNamespacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListNamespaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListNamespacesResponse()
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


    def ListTriggers(self, request):
        """This API is used to get the function trigger list.

        :param request: Request instance for ListTriggers.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListTriggersRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListTriggersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListTriggers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListTriggersResponse()
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


    def ListVersionByFunction(self, request):
        """This API is used to query the function version based on the input parameters.

        :param request: Request instance for ListVersionByFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListVersionByFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListVersionByFunctionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListVersionByFunction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListVersionByFunctionResponse()
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


    def PublishLayerVersion(self, request):
        """This API is used to create a version for a layer by using the given .zip file or COS object. Each time this API is called with the same layer name, a new version will be generated.

        :param request: Request instance for PublishLayerVersion.
        :type request: :class:`tencentcloud.scf.v20180416.models.PublishLayerVersionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.PublishLayerVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PublishLayerVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PublishLayerVersionResponse()
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


    def PublishVersion(self, request):
        """This API is used for users to release a new version of the function.

        :param request: Request instance for PublishVersion.
        :type request: :class:`tencentcloud.scf.v20180416.models.PublishVersionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.PublishVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PublishVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PublishVersionResponse()
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


    def PutProvisionedConcurrencyConfig(self, request):
        """This API is used to set the provisioned concurrency of a non-$LATEST version of a function.

        :param request: Request instance for PutProvisionedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.PutProvisionedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.PutProvisionedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PutProvisionedConcurrencyConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PutProvisionedConcurrencyConfigResponse()
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


    def PutReservedConcurrencyConfig(self, request):
        """This API is used to set the reserved concurrency of a function.

        :param request: Request instance for PutReservedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.PutReservedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.PutReservedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PutReservedConcurrencyConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PutReservedConcurrencyConfigResponse()
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


    def PutTotalConcurrencyConfig(self, request):
        """This API is used to modify the account concurrency quota.

        :param request: Request instance for PutTotalConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.PutTotalConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.PutTotalConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PutTotalConcurrencyConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PutTotalConcurrencyConfigResponse()
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


    def TerminateAsyncEvent(self, request):
        """This API is used to terminate a running async function event.

        :param request: Request instance for TerminateAsyncEvent.
        :type request: :class:`tencentcloud.scf.v20180416.models.TerminateAsyncEventRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.TerminateAsyncEventResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateAsyncEvent", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateAsyncEventResponse()
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


    def UpdateAlias(self, request):
        """This API is used to update the configuration of an alias.

        :param request: Request instance for UpdateAlias.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateAliasRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateAliasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateAlias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAliasResponse()
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


    def UpdateFunctionCode(self, request):
        """This API is used to update the function code based on the input parameters.

        :param request: Request instance for UpdateFunctionCode.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionCodeRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionCodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateFunctionCode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateFunctionCodeResponse()
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


    def UpdateFunctionConfiguration(self, request):
        """This API is used to update the function configuration based on the input parameters.

        :param request: Request instance for UpdateFunctionConfiguration.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionConfigurationRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateFunctionConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateFunctionConfigurationResponse()
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


    def UpdateFunctionEventInvokeConfig(self, request):
        """This API is used to update the async retry configuration of a function, including the number of retry attempts and message retention period.

        :param request: Request instance for UpdateFunctionEventInvokeConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionEventInvokeConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionEventInvokeConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateFunctionEventInvokeConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateFunctionEventInvokeConfigResponse()
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


    def UpdateNamespace(self, request):
        """This API is used to update a namespace.

        :param request: Request instance for UpdateNamespace.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateNamespaceRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateNamespaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateNamespace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateNamespaceResponse()
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