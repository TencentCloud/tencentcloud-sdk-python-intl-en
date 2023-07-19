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
            headers = request.headers
            body = self.call("CopyFunction", params, headers=headers)
            response = json.loads(body)
            model = models.CopyFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAlias(self, request):
        """This API is used to create an alias for a function version. You can use the alias to mark a specific function version such as DEV/RELEASE. You can also modify the version pointed to by the alias at any time.
        An alias must point to a master version and can point to an additional version at the same time. If you specify an alias when invoking a function, the request will be sent to the versions pointed to by the alias. You can configure the ratio between the master version and additional version during request sending.

        :param request: Request instance for CreateAlias.
        :type request: :class:`tencentcloud.scf.v20180416.models.CreateAliasRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CreateAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlias", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNamespace(self, request):
        """This API is used to create a namespace based on the input parameters.

        :param request: Request instance for CreateNamespace.
        :type request: :class:`tencentcloud.scf.v20180416.models.CreateNamespaceRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CreateNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTrigger(self, request):
        """This API is used to create a trigger based on the input parameters.

        :param request: Request instance for CreateTrigger.
        :type request: :class:`tencentcloud.scf.v20180416.models.CreateTriggerRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CreateTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAlias(self, request):
        """This API is used to delete an alias of a function version.

        :param request: Request instance for DeleteAlias.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteAliasRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlias", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFunction(self, request):
        """This API is used to delete a function based on the input parameters.

        :param request: Request instance for DeleteFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFunction", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLayerVersion(self, request):
        """This API is used to delete a specified version of a specified layer. The deleted version cannot be associated with a function, but the deletion does not affect functions that are referencing this layer.

        :param request: Request instance for DeleteLayerVersion.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteLayerVersionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteLayerVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLayerVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLayerVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNamespace(self, request):
        """This API is used to delete the specific namespace according to the parameters passed in.

        :param request: Request instance for DeleteNamespace.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteNamespaceRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProvisionedConcurrencyConfig(self, request):
        """This API is used to delete the provisioned concurrency configuration of a function version.

        :param request: Request instance for DeleteProvisionedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteProvisionedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteProvisionedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProvisionedConcurrencyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProvisionedConcurrencyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReservedConcurrencyConfig(self, request):
        """This API is used to delete the configuration of reserved quota.

        :param request: Request instance for DeleteReservedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteReservedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteReservedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReservedConcurrencyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReservedConcurrencyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTrigger(self, request):
        """This API is used to delete an existing trigger based on the input parameters.

        :param request: Request instance for DeleteTrigger.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteTriggerRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAccount(self, request):
        """This API is used to get the account information.

        :param request: Request instance for GetAccount.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetAccountRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAccount", params, headers=headers)
            response = json.loads(body)
            model = models.GetAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAlias(self, request):
        """This API is used to get the alias details such as the name, description, version, and routing information.

        :param request: Request instance for GetAlias.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetAliasRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAlias", params, headers=headers)
            response = json.loads(body)
            model = models.GetAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAsyncEventStatus(self, request):
        """This API is used to get the status of an async function execution event. The event status is retained for 3*24 hours, counting from the completion of the event.

        :param request: Request instance for GetAsyncEventStatus.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetAsyncEventStatusRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetAsyncEventStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAsyncEventStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetAsyncEventStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFunctionAddress(self, request):
        """This API is used to obtain the download address of the function code package.

        :param request: Request instance for GetFunctionAddress.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetFunctionAddressRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetFunctionAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFunctionAddress", params, headers=headers)
            response = json.loads(body)
            model = models.GetFunctionAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFunctionEventInvokeConfig(self, request):
        """This API is used to get the async retry configuration of a function, including the number of retry attempts and message retention period.

        :param request: Request instance for GetFunctionEventInvokeConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetFunctionEventInvokeConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetFunctionEventInvokeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFunctionEventInvokeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.GetFunctionEventInvokeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFunctionLogs(self, request):
        """This API returns function running logs according to the specified conditions. Note that this API has been disused. You can use [GetRequestStatus](https://intl.cloud.tencent.com/document/product/583/65348?from_cn_redirect=1) instead. See also [Retrieving Logs](https://intl.cloud.tencent.com/document/product/583/52637?from_cn_redirect=1).

        :param request: Request instance for GetFunctionLogs.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetFunctionLogsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetFunctionLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFunctionLogs", params, headers=headers)
            response = json.loads(body)
            model = models.GetFunctionLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLayerVersion(self, request):
        """This API is used to get the layer version details, including links used to download files in the layer.

        :param request: Request instance for GetLayerVersion.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetLayerVersionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetLayerVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLayerVersion", params, headers=headers)
            response = json.loads(body)
            model = models.GetLayerVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetProvisionedConcurrencyConfig(self, request):
        """This API is used to get the provisioned concurrency details of a function or its specified version.

        :param request: Request instance for GetProvisionedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetProvisionedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetProvisionedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetProvisionedConcurrencyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.GetProvisionedConcurrencyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRequestStatus(self, request):
        """This API is used to query the status of a single function request.

        :param request: Request instance for GetRequestStatus.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetRequestStatusRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetRequestStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRequestStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetRequestStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetReservedConcurrencyConfig(self, request):
        """This API is used to obtain the reserved quota details of a function.

        :param request: Request instance for GetReservedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetReservedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetReservedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetReservedConcurrencyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.GetReservedConcurrencyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def Invoke(self, request):
        """This API is used to run a function.

        :param request: Request instance for Invoke.
        :type request: :class:`tencentcloud.scf.v20180416.models.InvokeRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.InvokeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Invoke", params, headers=headers)
            response = json.loads(body)
            model = models.InvokeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InvokeFunction(self, request):
        """This API is used to invoke functions synchronously.

        :param request: Request instance for InvokeFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.InvokeFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.InvokeFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InvokeFunction", params, headers=headers)
            response = json.loads(body)
            model = models.InvokeFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAliases(self, request):
        """This API is used to return the list of all aliases under a function. You can filter them by the specific function version.

        :param request: Request instance for ListAliases.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListAliasesRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListAliasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAliases", params, headers=headers)
            response = json.loads(body)
            model = models.ListAliasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAsyncEvents(self, request):
        """This API is used to pull the list of async function events.

        :param request: Request instance for ListAsyncEvents.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListAsyncEventsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListAsyncEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAsyncEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ListAsyncEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListFunctions(self, request):
        """This API is used to return relevant function information based on the input query parameters.

        :param request: Request instance for ListFunctions.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListFunctionsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListFunctionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListFunctions", params, headers=headers)
            response = json.loads(body)
            model = models.ListFunctionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListLayerVersions(self, request):
        """This API is used to get the information of all versions of a specified layer.

        :param request: Request instance for ListLayerVersions.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListLayerVersionsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListLayerVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListLayerVersions", params, headers=headers)
            response = json.loads(body)
            model = models.ListLayerVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListLayers(self, request):
        """This API is used to return the list of all layers, including the information of the latest version of each layer. You can filter them by the compatible runtime.

        :param request: Request instance for ListLayers.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListLayersRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListLayersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListLayers", params, headers=headers)
            response = json.loads(body)
            model = models.ListLayersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListNamespaces(self, request):
        """This API is used to display a namespace list.

        :param request: Request instance for ListNamespaces.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListNamespacesRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.ListNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTriggers(self, request):
        """This API is used to get the function trigger list.

        :param request: Request instance for ListTriggers.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListTriggersRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListTriggersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTriggers", params, headers=headers)
            response = json.loads(body)
            model = models.ListTriggersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListVersionByFunction(self, request):
        """This API is used to query the function version based on the input parameters.

        :param request: Request instance for ListVersionByFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListVersionByFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListVersionByFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListVersionByFunction", params, headers=headers)
            response = json.loads(body)
            model = models.ListVersionByFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PublishLayerVersion(self, request):
        """This API is used to create a version for a layer by using the given .zip file or COS object. Each time this API is called with the same layer name, a new version will be generated.

        :param request: Request instance for PublishLayerVersion.
        :type request: :class:`tencentcloud.scf.v20180416.models.PublishLayerVersionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.PublishLayerVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PublishLayerVersion", params, headers=headers)
            response = json.loads(body)
            model = models.PublishLayerVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PublishVersion(self, request):
        """This API is used for users to release a new version of the function.

        :param request: Request instance for PublishVersion.
        :type request: :class:`tencentcloud.scf.v20180416.models.PublishVersionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.PublishVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PublishVersion", params, headers=headers)
            response = json.loads(body)
            model = models.PublishVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PutProvisionedConcurrencyConfig(self, request):
        """This API is used to set the provisioned concurrency of a non-$LATEST version of a function.

        :param request: Request instance for PutProvisionedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.PutProvisionedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.PutProvisionedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutProvisionedConcurrencyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.PutProvisionedConcurrencyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PutReservedConcurrencyConfig(self, request):
        """This API is used to configure the reserved quota of a function.

        :param request: Request instance for PutReservedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.PutReservedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.PutReservedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutReservedConcurrencyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.PutReservedConcurrencyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PutTotalConcurrencyConfig(self, request):
        """This API is used to modify the account concurrency quota.

        :param request: Request instance for PutTotalConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.PutTotalConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.PutTotalConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutTotalConcurrencyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.PutTotalConcurrencyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateAsyncEvent(self, request):
        """This API is used to terminate a running async function event.

        :param request: Request instance for TerminateAsyncEvent.
        :type request: :class:`tencentcloud.scf.v20180416.models.TerminateAsyncEventRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.TerminateAsyncEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateAsyncEvent", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateAsyncEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAlias(self, request):
        """This API is used to update the configuration of an alias.

        :param request: Request instance for UpdateAlias.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateAliasRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAlias", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateFunctionCode(self, request):
        """This API is used to update the function code based on the input parameters.

        :param request: Request instance for UpdateFunctionCode.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionCodeRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateFunctionCode", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateFunctionCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateFunctionEventInvokeConfig(self, request):
        """This API is used to update the async retry configuration of a function, including the number of retry attempts and message retention period.

        :param request: Request instance for UpdateFunctionEventInvokeConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionEventInvokeConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionEventInvokeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateFunctionEventInvokeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateFunctionEventInvokeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateNamespace(self, request):
        """This API is used to update a namespace.

        :param request: Request instance for UpdateNamespace.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateNamespaceRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTriggerStatus(self, request):
        """This API is used to update the trigger status.

        :param request: Request instance for UpdateTriggerStatus.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateTriggerStatusRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateTriggerStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTriggerStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTriggerStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))