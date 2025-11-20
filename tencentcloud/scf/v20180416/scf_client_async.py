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
from tencentcloud.scf.v20180416 import models
from typing import Dict


class ScfClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'scf.intl.tencentcloudapi.com'
    _service = 'scf'

    async def CopyFunction(
            self,
            request: models.CopyFunctionRequest,
            opts: Dict = None,
    ) -> models.CopyFunctionResponse:
        """
        This API is used to replicate a function. You can store the replicated function in a specified Region and Namespace.
        Note: This API **does not** replicate the following objects or attributes of the function:
        1. Function trigger
        2. Versions other than $LATEST
        3. CLS target of the logs configured in the function

        You can manually configure the function after replication as required.
        """
        
        kwargs = {}
        kwargs["action"] = "CopyFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlias(
            self,
            request: models.CreateAliasRequest,
            opts: Dict = None,
    ) -> models.CreateAliasResponse:
        """
        This API is used to create an alias for a function version. You can use the alias to mark a specific function version such as DEV/RELEASE. You can also modify the version pointed to by the alias at any time.
        An alias must point to a master version and can point to an additional version at the same time. If you specify an alias when invoking a function, the request will be sent to the versions pointed to by the alias. You can configure the ratio between the master version and additional version during request sending.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNamespace(
            self,
            request: models.CreateNamespaceRequest,
            opts: Dict = None,
    ) -> models.CreateNamespaceResponse:
        """
        This API is used to create a namespace based on the input parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTrigger(
            self,
            request: models.CreateTriggerRequest,
            opts: Dict = None,
    ) -> models.CreateTriggerResponse:
        """
        This API is used to create a trigger based on the input parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlias(
            self,
            request: models.DeleteAliasRequest,
            opts: Dict = None,
    ) -> models.DeleteAliasResponse:
        """
        This API is used to delete an alias of a function version.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFunction(
            self,
            request: models.DeleteFunctionRequest,
            opts: Dict = None,
    ) -> models.DeleteFunctionResponse:
        """
        This API is used to delete a function based on the input parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLayerVersion(
            self,
            request: models.DeleteLayerVersionRequest,
            opts: Dict = None,
    ) -> models.DeleteLayerVersionResponse:
        """
        This API is used to delete a specified version of a specified layer. The deleted version cannot be associated with a function, but the deletion does not affect functions that are referencing this layer.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLayerVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLayerVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNamespace(
            self,
            request: models.DeleteNamespaceRequest,
            opts: Dict = None,
    ) -> models.DeleteNamespaceResponse:
        """
        This API is used to delete the specific namespace according to the parameters passed in.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProvisionedConcurrencyConfig(
            self,
            request: models.DeleteProvisionedConcurrencyConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteProvisionedConcurrencyConfigResponse:
        """
        This API is used to delete the provisioned concurrency configuration of a function version.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProvisionedConcurrencyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProvisionedConcurrencyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReservedConcurrencyConfig(
            self,
            request: models.DeleteReservedConcurrencyConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteReservedConcurrencyConfigResponse:
        """
        This API is used to delete the configuration of reserved quota.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReservedConcurrencyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReservedConcurrencyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTrigger(
            self,
            request: models.DeleteTriggerRequest,
            opts: Dict = None,
    ) -> models.DeleteTriggerResponse:
        """
        This API is used to delete an existing trigger based on the input parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAccount(
            self,
            request: models.GetAccountRequest,
            opts: Dict = None,
    ) -> models.GetAccountResponse:
        """
        This API is used to get the account information.
        """
        
        kwargs = {}
        kwargs["action"] = "GetAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAlias(
            self,
            request: models.GetAliasRequest,
            opts: Dict = None,
    ) -> models.GetAliasResponse:
        """
        This API is used to get the alias details such as the name, description, version, and routing information.
        """
        
        kwargs = {}
        kwargs["action"] = "GetAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAsyncEventStatus(
            self,
            request: models.GetAsyncEventStatusRequest,
            opts: Dict = None,
    ) -> models.GetAsyncEventStatusResponse:
        """
        This API is used to get the status of an async function execution event. The event status is retained for 3*24 hours, counting from the completion of the event.
        """
        
        kwargs = {}
        kwargs["action"] = "GetAsyncEventStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAsyncEventStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFunctionAddress(
            self,
            request: models.GetFunctionAddressRequest,
            opts: Dict = None,
    ) -> models.GetFunctionAddressResponse:
        """
        This API is used to obtain the download address of the function code package.
        """
        
        kwargs = {}
        kwargs["action"] = "GetFunctionAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFunctionAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFunctionEventInvokeConfig(
            self,
            request: models.GetFunctionEventInvokeConfigRequest,
            opts: Dict = None,
    ) -> models.GetFunctionEventInvokeConfigResponse:
        """
        This API is used to get the async retry configuration of a function, including the number of retry attempts and message retention period.
        """
        
        kwargs = {}
        kwargs["action"] = "GetFunctionEventInvokeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFunctionEventInvokeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFunctionLogs(
            self,
            request: models.GetFunctionLogsRequest,
            opts: Dict = None,
    ) -> models.GetFunctionLogsResponse:
        """
        This API returns function running logs according to the specified conditions. Note that this API has been disused. You can use [GetRequestStatus](https://intl.cloud.tencent.com/document/product/583/65348?from_cn_redirect=1) instead. See also [Retrieving Logs](https://intl.cloud.tencent.com/document/product/583/52637?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "GetFunctionLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFunctionLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLayerVersion(
            self,
            request: models.GetLayerVersionRequest,
            opts: Dict = None,
    ) -> models.GetLayerVersionResponse:
        """
        This API is used to get the layer version details, including links used to download files in the layer.
        """
        
        kwargs = {}
        kwargs["action"] = "GetLayerVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLayerVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetProvisionedConcurrencyConfig(
            self,
            request: models.GetProvisionedConcurrencyConfigRequest,
            opts: Dict = None,
    ) -> models.GetProvisionedConcurrencyConfigResponse:
        """
        This API is used to get the provisioned concurrency details of a function or its specified version.
        """
        
        kwargs = {}
        kwargs["action"] = "GetProvisionedConcurrencyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetProvisionedConcurrencyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRequestStatus(
            self,
            request: models.GetRequestStatusRequest,
            opts: Dict = None,
    ) -> models.GetRequestStatusResponse:
        """
        This API is used to query the status of a single function request.
        """
        
        kwargs = {}
        kwargs["action"] = "GetRequestStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRequestStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetReservedConcurrencyConfig(
            self,
            request: models.GetReservedConcurrencyConfigRequest,
            opts: Dict = None,
    ) -> models.GetReservedConcurrencyConfigResponse:
        """
        This API is used to obtain the reserved quota details of a function.
        """
        
        kwargs = {}
        kwargs["action"] = "GetReservedConcurrencyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetReservedConcurrencyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def Invoke(
            self,
            request: models.InvokeRequest,
            opts: Dict = None,
    ) -> models.InvokeResponse:
        """
        This API is used to run a function.
        """
        
        kwargs = {}
        kwargs["action"] = "Invoke"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvokeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InvokeFunction(
            self,
            request: models.InvokeFunctionRequest,
            opts: Dict = None,
    ) -> models.InvokeFunctionResponse:
        """
        This API is used to invoke functions synchronously.
        """
        
        kwargs = {}
        kwargs["action"] = "InvokeFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvokeFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAliases(
            self,
            request: models.ListAliasesRequest,
            opts: Dict = None,
    ) -> models.ListAliasesResponse:
        """
        This API is used to return the list of all aliases under a function. You can filter them by the specific function version.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAliases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAliasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAsyncEvents(
            self,
            request: models.ListAsyncEventsRequest,
            opts: Dict = None,
    ) -> models.ListAsyncEventsResponse:
        """
        This API is used to pull the list of async function events.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAsyncEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAsyncEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListFunctions(
            self,
            request: models.ListFunctionsRequest,
            opts: Dict = None,
    ) -> models.ListFunctionsResponse:
        """
        This API is used to return relevant function information based on the input query parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "ListFunctions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListFunctionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListLayerVersions(
            self,
            request: models.ListLayerVersionsRequest,
            opts: Dict = None,
    ) -> models.ListLayerVersionsResponse:
        """
        This API is used to get the information of all versions of a specified layer.
        """
        
        kwargs = {}
        kwargs["action"] = "ListLayerVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListLayerVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListLayers(
            self,
            request: models.ListLayersRequest,
            opts: Dict = None,
    ) -> models.ListLayersResponse:
        """
        This API is used to return the list of all layers, including the information of the latest version of each layer. You can filter them by the compatible runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "ListLayers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListLayersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListNamespaces(
            self,
            request: models.ListNamespacesRequest,
            opts: Dict = None,
    ) -> models.ListNamespacesResponse:
        """
        This API is used to display a namespace list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTriggers(
            self,
            request: models.ListTriggersRequest,
            opts: Dict = None,
    ) -> models.ListTriggersResponse:
        """
        This API is used to get the function trigger list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListTriggers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTriggersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListVersionByFunction(
            self,
            request: models.ListVersionByFunctionRequest,
            opts: Dict = None,
    ) -> models.ListVersionByFunctionResponse:
        """
        This API is used to query the function version based on the input parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "ListVersionByFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListVersionByFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PublishLayerVersion(
            self,
            request: models.PublishLayerVersionRequest,
            opts: Dict = None,
    ) -> models.PublishLayerVersionResponse:
        """
        This API is used to create a version for a layer by using the given .zip file or COS object. Each time this API is called with the same layer name, a new version will be generated.
        """
        
        kwargs = {}
        kwargs["action"] = "PublishLayerVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PublishLayerVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PublishVersion(
            self,
            request: models.PublishVersionRequest,
            opts: Dict = None,
    ) -> models.PublishVersionResponse:
        """
        This API is used for users to release a new version of the function.
        """
        
        kwargs = {}
        kwargs["action"] = "PublishVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PublishVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutProvisionedConcurrencyConfig(
            self,
            request: models.PutProvisionedConcurrencyConfigRequest,
            opts: Dict = None,
    ) -> models.PutProvisionedConcurrencyConfigResponse:
        """
        This API is used to set the provisioned concurrency of a non-$LATEST version of a function.
        """
        
        kwargs = {}
        kwargs["action"] = "PutProvisionedConcurrencyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutProvisionedConcurrencyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutReservedConcurrencyConfig(
            self,
            request: models.PutReservedConcurrencyConfigRequest,
            opts: Dict = None,
    ) -> models.PutReservedConcurrencyConfigResponse:
        """
        This API is used to configure the reserved quota of a function.
        """
        
        kwargs = {}
        kwargs["action"] = "PutReservedConcurrencyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutReservedConcurrencyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutTotalConcurrencyConfig(
            self,
            request: models.PutTotalConcurrencyConfigRequest,
            opts: Dict = None,
    ) -> models.PutTotalConcurrencyConfigResponse:
        """
        This API is used to modify the account concurrency quota.
        """
        
        kwargs = {}
        kwargs["action"] = "PutTotalConcurrencyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutTotalConcurrencyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateAsyncEvent(
            self,
            request: models.TerminateAsyncEventRequest,
            opts: Dict = None,
    ) -> models.TerminateAsyncEventResponse:
        """
        This API is used to terminate a running async function event.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateAsyncEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateAsyncEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAlias(
            self,
            request: models.UpdateAliasRequest,
            opts: Dict = None,
    ) -> models.UpdateAliasResponse:
        """
        This API is used to update the configuration of an alias.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateFunctionCode(
            self,
            request: models.UpdateFunctionCodeRequest,
            opts: Dict = None,
    ) -> models.UpdateFunctionCodeResponse:
        """
        This API is used to update the function code based on the input parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateFunctionCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateFunctionCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateFunctionEventInvokeConfig(
            self,
            request: models.UpdateFunctionEventInvokeConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateFunctionEventInvokeConfigResponse:
        """
        This API is used to update the async retry configuration of a function, including the number of retry attempts and message retention period.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateFunctionEventInvokeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateFunctionEventInvokeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateNamespace(
            self,
            request: models.UpdateNamespaceRequest,
            opts: Dict = None,
    ) -> models.UpdateNamespaceResponse:
        """
        This API is used to update a namespace.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTriggerStatus(
            self,
            request: models.UpdateTriggerStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateTriggerStatusResponse:
        """
        This API is used to update the trigger status.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTriggerStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTriggerStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)