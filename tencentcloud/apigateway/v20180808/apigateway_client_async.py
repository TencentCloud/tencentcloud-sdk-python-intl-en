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
from tencentcloud.apigateway.v20180808 import models
from typing import Dict


class ApigatewayClient(AbstractClient):
    _apiVersion = '2018-08-08'
    _endpoint = 'apigateway.intl.tencentcloudapi.com'
    _service = 'apigateway'

    async def AttachPlugin(
            self,
            request: models.AttachPluginRequest,
            opts: Dict = None,
    ) -> models.AttachPluginResponse:
        """
        This API is used to bind a plugin to an API.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachPlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachPluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindApiApp(
            self,
            request: models.BindApiAppRequest,
            opts: Dict = None,
    ) -> models.BindApiAppResponse:
        """
        This API is used to bind an application to an API.
        """
        
        kwargs = {}
        kwargs["action"] = "BindApiApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindApiAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindEnvironment(
            self,
            request: models.BindEnvironmentRequest,
            opts: Dict = None,
    ) -> models.BindEnvironmentResponse:
        """
        This API is used to bind a usage plan to a service or API.
        After you publish a service to an environment, if the API requires authentication and can be called only when it is bound to a usage plan, you can use this API to bind a usage plan to the specified environment.
        Currently, a usage plan can be bound to an API; however, under the same service, usage plans bound to a service and usage plans bound to an API cannot coexist. Therefore, in an environment to which a service-level usage plan has already been bound, please use the `DemoteServiceUsagePlan` API to degrade it.
        """
        
        kwargs = {}
        kwargs["action"] = "BindEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindIPStrategy(
            self,
            request: models.BindIPStrategyRequest,
            opts: Dict = None,
    ) -> models.BindIPStrategyResponse:
        """
        This API is used to bind an IP policy to an API.
        """
        
        kwargs = {}
        kwargs["action"] = "BindIPStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindIPStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindSecretIds(
            self,
            request: models.BindSecretIdsRequest,
            opts: Dict = None,
    ) -> models.BindSecretIdsResponse:
        """
        This API is used to bind a key to a usage plan.
        You can bind a key to a usage plan and bind the usage plan to an environment where a service is published, so that callers can use the key to call APIs in the service. You can use this API to bind a key to a usage plan.
        """
        
        kwargs = {}
        kwargs["action"] = "BindSecretIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindSecretIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindSubDomain(
            self,
            request: models.BindSubDomainRequest,
            opts: Dict = None,
    ) -> models.BindSubDomainResponse:
        """
        This API is used to bind a custom domain name to a service.
        Each service in API Gateway provides a default domain name for users to call. If you want to use your own domain name, you can bind a custom domain name to the target service. After getting the ICP filing and configuring the CNAME record between the custom and default domain names, you can directly call the custom domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "BindSubDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindSubDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BuildAPIDoc(
            self,
            request: models.BuildAPIDocRequest,
            opts: Dict = None,
    ) -> models.BuildAPIDocResponse:
        """
        This API is used to build an API document.
        """
        
        kwargs = {}
        kwargs["action"] = "BuildAPIDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BuildAPIDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAPIDoc(
            self,
            request: models.CreateAPIDocRequest,
            opts: Dict = None,
    ) -> models.CreateAPIDocResponse:
        """
        This API is used to create an API document.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAPIDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAPIDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApi(
            self,
            request: models.CreateApiRequest,
            opts: Dict = None,
    ) -> models.CreateApiResponse:
        """
        This API is used to create an API. Before creating an API, you need to create a service, as each API belongs to a certain service.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApiApp(
            self,
            request: models.CreateApiAppRequest,
            opts: Dict = None,
    ) -> models.CreateApiAppResponse:
        """
        This API is used to create an application.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApiApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApiAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApiKey(
            self,
            request: models.CreateApiKeyRequest,
            opts: Dict = None,
    ) -> models.CreateApiKeyResponse:
        """
        This API is used to create an API key pair.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIPStrategy(
            self,
            request: models.CreateIPStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateIPStrategyResponse:
        """
        This API is used to create a service IP policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIPStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIPStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePlugin(
            self,
            request: models.CreatePluginRequest,
            opts: Dict = None,
    ) -> models.CreatePluginResponse:
        """
        This API is used to create an API Gateway plugin.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateService(
            self,
            request: models.CreateServiceRequest,
            opts: Dict = None,
    ) -> models.CreateServiceResponse:
        """
        This API is used to create a service.
        A service is the biggest usage unit in API Gateway. Each service can contain multiple APIs and one default domain name for invocation. You can also bind your own custom domain name to a service.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUpstream(
            self,
            request: models.CreateUpstreamRequest,
            opts: Dict = None,
    ) -> models.CreateUpstreamResponse:
        """
        This API is used to create an upstream.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUpstream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUpstreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUsagePlan(
            self,
            request: models.CreateUsagePlanRequest,
            opts: Dict = None,
    ) -> models.CreateUsagePlanResponse:
        """
        This API is used to create a usage plan.
        To use API Gateway, you need to create a usage plan and bind it to a service environment.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUsagePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUsagePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAPIDoc(
            self,
            request: models.DeleteAPIDocRequest,
            opts: Dict = None,
    ) -> models.DeleteAPIDocResponse:
        """
        This API is used to delete an API document.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAPIDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAPIDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApi(
            self,
            request: models.DeleteApiRequest,
            opts: Dict = None,
    ) -> models.DeleteApiResponse:
        """
        This API is used to delete a created API.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApiApp(
            self,
            request: models.DeleteApiAppRequest,
            opts: Dict = None,
    ) -> models.DeleteApiAppResponse:
        """
        This API is used to delete a created application.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApiApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApiAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApiKey(
            self,
            request: models.DeleteApiKeyRequest,
            opts: Dict = None,
    ) -> models.DeleteApiKeyResponse:
        """
        This API is used to delete an API key pair.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIPStrategy(
            self,
            request: models.DeleteIPStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteIPStrategyResponse:
        """
        This API is used to delete a service IP policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIPStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIPStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePlugin(
            self,
            request: models.DeletePluginRequest,
            opts: Dict = None,
    ) -> models.DeletePluginResponse:
        """
        This API is used to delete an API Gateway plugin.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteService(
            self,
            request: models.DeleteServiceRequest,
            opts: Dict = None,
    ) -> models.DeleteServiceResponse:
        """
        This API is used to delete a service in API Gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteServiceSubDomainMapping(
            self,
            request: models.DeleteServiceSubDomainMappingRequest,
            opts: Dict = None,
    ) -> models.DeleteServiceSubDomainMappingResponse:
        """
        This API is used to delete a custom domain name mapping in a service environment.
        You can use this API if you use a custom domain name and custom mapping. Please note that if you delete all mappings in all environments, a failure will be returned when this API is called.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteServiceSubDomainMapping"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServiceSubDomainMappingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUpstream(
            self,
            request: models.DeleteUpstreamRequest,
            opts: Dict = None,
    ) -> models.DeleteUpstreamResponse:
        """
        This API is used to delete an upstream. Note that you can only delete an upstream when it’s not bound with any APIs.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUpstream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUpstreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUsagePlan(
            self,
            request: models.DeleteUsagePlanRequest,
            opts: Dict = None,
    ) -> models.DeleteUsagePlanResponse:
        """
        This API is used to delete a usage plan.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUsagePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUsagePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DemoteServiceUsagePlan(
            self,
            request: models.DemoteServiceUsagePlanRequest,
            opts: Dict = None,
    ) -> models.DemoteServiceUsagePlanResponse:
        """
        This API is used to degrade a usage plan of a service in an environment to the API level.
        This operation will be denied if there are no APIs under the service.
        This operation will also be denied if the current environment has not been published.
        """
        
        kwargs = {}
        kwargs["action"] = "DemoteServiceUsagePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DemoteServiceUsagePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAPIDocDetail(
            self,
            request: models.DescribeAPIDocDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAPIDocDetailResponse:
        """
        This API is used to query the details of an API document.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAPIDocDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAPIDocDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAPIDocs(
            self,
            request: models.DescribeAPIDocsRequest,
            opts: Dict = None,
    ) -> models.DescribeAPIDocsResponse:
        """
        This API is used to query the list of API documents.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAPIDocs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAPIDocsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllPluginApis(
            self,
            request: models.DescribeAllPluginApisRequest,
            opts: Dict = None,
    ) -> models.DescribeAllPluginApisResponse:
        """
        This API is used to list all APIs that can use this plugin, no matter whether the API is bound with the plugin.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllPluginApis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllPluginApisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApi(
            self,
            request: models.DescribeApiRequest,
            opts: Dict = None,
    ) -> models.DescribeApiResponse:
        """
        This API (`DescribeApi`) is used to query the details of the APIs users manage via Tencent Cloud API Gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiApp(
            self,
            request: models.DescribeApiAppRequest,
            opts: Dict = None,
    ) -> models.DescribeApiAppResponse:
        """
        This API is used to search for an application by application ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiAppBindApisStatus(
            self,
            request: models.DescribeApiAppBindApisStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeApiAppBindApisStatusResponse:
        """
        This API is used to query the list of APIs bound to an application.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiAppBindApisStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiAppBindApisStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiAppsStatus(
            self,
            request: models.DescribeApiAppsStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeApiAppsStatusResponse:
        """
        This API is used to query the application list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiAppsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiAppsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiBindApiAppsStatus(
            self,
            request: models.DescribeApiBindApiAppsStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeApiBindApiAppsStatusResponse:
        """
        This API is used to query the list of applications bound to an API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiBindApiAppsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiBindApiAppsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiEnvironmentStrategy(
            self,
            request: models.DescribeApiEnvironmentStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeApiEnvironmentStrategyResponse:
        """
        This API is used to display the throttling policies bound to an API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiEnvironmentStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiEnvironmentStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiForApiApp(
            self,
            request: models.DescribeApiForApiAppRequest,
            opts: Dict = None,
    ) -> models.DescribeApiForApiAppResponse:
        """
        This API is used to query the details of an API deployed at API Gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiForApiApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiForApiAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiKey(
            self,
            request: models.DescribeApiKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeApiKeyResponse:
        """
        This API is used to query the details of a key.
        After creating an API key, you can query its details by using this API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiKeysStatus(
            self,
            request: models.DescribeApiKeysStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeApiKeysStatusResponse:
        """
        This API is used to query the information of one or more API keys.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiKeysStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiKeysStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiUsagePlan(
            self,
            request: models.DescribeApiUsagePlanRequest,
            opts: Dict = None,
    ) -> models.DescribeApiUsagePlanResponse:
        """
        This API is used to query the details of API usage plans in a service.
        To make authentication and throttling for a service take effect, you need to bind a usage plan to it. This API is used to query all usage plans bound to a service and APIs under it.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiUsagePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiUsagePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApisStatus(
            self,
            request: models.DescribeApisStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeApisStatusResponse:
        """
        This API is used to view a certain API or the list of all APIs under a service and relevant information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApisStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApisStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExclusiveInstanceRegions(
            self,
            request: models.DescribeExclusiveInstanceRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeExclusiveInstanceRegionsResponse:
        """
        Get the list of supported regions for dedicated instances
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExclusiveInstanceRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExclusiveInstanceRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPStrategy(
            self,
            request: models.DescribeIPStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeIPStrategyResponse:
        """
        This API is used to query IP policy details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPStrategyApisStatus(
            self,
            request: models.DescribeIPStrategyApisStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeIPStrategyApisStatusResponse:
        """
        This API is used to query the list of APIs to which an IP policy can be bound, i.e., the difference set between all APIs under the service and the APIs already bound to the policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPStrategyApisStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPStrategyApisStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPStrategysStatus(
            self,
            request: models.DescribeIPStrategysStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeIPStrategysStatusResponse:
        """
        This API is used to query the list of service IP policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPStrategysStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPStrategysStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesNetworkConfig(
            self,
            request: models.DescribeInstancesNetworkConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesNetworkConfigResponse:
        """
        This API is used to obtain the network configuration list of a dedicated instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesNetworkConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesNetworkConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogSearch(
            self,
            request: models.DescribeLogSearchRequest,
            opts: Dict = None,
    ) -> models.DescribeLogSearchResponse:
        """
        This API is used to search for logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogSearch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogSearchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePlugin(
            self,
            request: models.DescribePluginRequest,
            opts: Dict = None,
    ) -> models.DescribePluginResponse:
        """
        This API is used to query the plugin details by plugin ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePluginApis(
            self,
            request: models.DescribePluginApisRequest,
            opts: Dict = None,
    ) -> models.DescribePluginApisResponse:
        """
        This API is used to query APIs bound with a specified plugin.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePluginApis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePluginApisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePluginsByApi(
            self,
            request: models.DescribePluginsByApiRequest,
            opts: Dict = None,
    ) -> models.DescribePluginsByApiResponse:
        """
        This API is used to query all plug-ins bound with the API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePluginsByApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePluginsByApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeService(
            self,
            request: models.DescribeServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceResponse:
        """
        This API is used to query the details of a service, such as its description, domain name, protocol, creation time, and releases.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceEnvironmentList(
            self,
            request: models.DescribeServiceEnvironmentListRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceEnvironmentListResponse:
        """
        This API is used to query the list of environments under a service. All environments and their statuses under the queried service will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceEnvironmentList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceEnvironmentListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceEnvironmentReleaseHistory(
            self,
            request: models.DescribeServiceEnvironmentReleaseHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceEnvironmentReleaseHistoryResponse:
        """
        This API is used to query the release history in a service environment.
        A service can only be used when it is published to an environment after creation. This API is used to query the release history in an environment under a service.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceEnvironmentReleaseHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceEnvironmentReleaseHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceEnvironmentStrategy(
            self,
            request: models.DescribeServiceEnvironmentStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceEnvironmentStrategyResponse:
        """
        This API is used to display a service throttling policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceEnvironmentStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceEnvironmentStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceForApiApp(
            self,
            request: models.DescribeServiceForApiAppRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceForApiAppResponse:
        """
        This API is used to query the details of a service, such as its description, domain name, and protocol.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceForApiApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceForApiAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceReleaseVersion(
            self,
            request: models.DescribeServiceReleaseVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceReleaseVersionResponse:
        """
        This API is used to query the list of all published versions under a service.
        A service is generally published on several versions. This API can be used to query the published versions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceReleaseVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceReleaseVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceSubDomainMappings(
            self,
            request: models.DescribeServiceSubDomainMappingsRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceSubDomainMappingsResponse:
        """
        This API is used to query the path mappings of a custom domain name.
        In API Gateway, you can bind a custom domain name to a service and map its paths. You can customize different path mappings to up to 3 environments under the service. This API is used to query the list of path mappings of a custom domain name bound to a service.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceSubDomainMappings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceSubDomainMappingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceSubDomains(
            self,
            request: models.DescribeServiceSubDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceSubDomainsResponse:
        """
        This API is used to query the list of custom domain names.
        In API Gateway, you can bind custom domain names to a service for service call. This API is used to query the list of custom domain names bound to a service.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceSubDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceSubDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceUsagePlan(
            self,
            request: models.DescribeServiceUsagePlanRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceUsagePlanResponse:
        """
        This API is used to query the details of usage plans in a service.
        To make authentication and throttling for a service take effect, you need to bind a usage plan to it. This API is used to query all usage plans bound to a service.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceUsagePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceUsagePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServicesStatus(
            self,
            request: models.DescribeServicesStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeServicesStatusResponse:
        """
        This API is used to query the list of one or more services and return relevant domain name, time, and other information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServicesStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServicesStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUpstreamBindApis(
            self,
            request: models.DescribeUpstreamBindApisRequest,
            opts: Dict = None,
    ) -> models.DescribeUpstreamBindApisResponse:
        """
        This API is used to query APIs bound with an upstream.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUpstreamBindApis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUpstreamBindApisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUpstreams(
            self,
            request: models.DescribeUpstreamsRequest,
            opts: Dict = None,
    ) -> models.DescribeUpstreamsResponse:
        """
        This API is used to query details of upstreams under the current account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUpstreams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUpstreamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsagePlan(
            self,
            request: models.DescribeUsagePlanRequest,
            opts: Dict = None,
    ) -> models.DescribeUsagePlanResponse:
        """
        This API is used to query the details of a usage plan, such as its name, QPS, creation time, and bound environment.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsagePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsagePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsagePlanEnvironments(
            self,
            request: models.DescribeUsagePlanEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeUsagePlanEnvironmentsResponse:
        """
        This API is used to query the list of environments bound to a usage plan.
        After binding a usage plan to environments, you can use this API to query all service environments bound to the usage plan.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsagePlanEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsagePlanEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsagePlanSecretIds(
            self,
            request: models.DescribeUsagePlanSecretIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeUsagePlanSecretIdsResponse:
        """
        This API is used to query the list of keys bound to a usage plan.
        In API Gateway, a usage plan can be bound to multiple key pairs. You can use this API to query the list of keys bound to it.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsagePlanSecretIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsagePlanSecretIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsagePlansStatus(
            self,
            request: models.DescribeUsagePlansStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeUsagePlansStatusResponse:
        """
        This API is used to query the list of usage plans.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsagePlansStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsagePlansStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachPlugin(
            self,
            request: models.DetachPluginRequest,
            opts: Dict = None,
    ) -> models.DetachPluginResponse:
        """
        This API is used to unbind an API from the plugin.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachPlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachPluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableApiKey(
            self,
            request: models.DisableApiKeyRequest,
            opts: Dict = None,
    ) -> models.DisableApiKeyResponse:
        """
        This API is used to disable an API key.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableApiKey(
            self,
            request: models.EnableApiKeyRequest,
            opts: Dict = None,
    ) -> models.EnableApiKeyResponse:
        """
        This API is used to enable a disabled API key.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportOpenApi(
            self,
            request: models.ImportOpenApiRequest,
            opts: Dict = None,
    ) -> models.ImportOpenApiResponse:
        """
        This API is used to import an OpenAPI to API gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "ImportOpenApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportOpenApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAPIDoc(
            self,
            request: models.ModifyAPIDocRequest,
            opts: Dict = None,
    ) -> models.ModifyAPIDocResponse:
        """
        This API is used to modify an API document.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAPIDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAPIDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApi(
            self,
            request: models.ModifyApiRequest,
            opts: Dict = None,
    ) -> models.ModifyApiResponse:
        """
        This API is used to modify an API. You can call this API to edit/modify a configured API. The modified API takes effect only after its service is published to the corresponding environment again.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApiApp(
            self,
            request: models.ModifyApiAppRequest,
            opts: Dict = None,
    ) -> models.ModifyApiAppResponse:
        """
        This API is used to modify a created API.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApiApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApiAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApiEnvironmentStrategy(
            self,
            request: models.ModifyApiEnvironmentStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyApiEnvironmentStrategyResponse:
        """
        This API is used to modify an API throttling policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApiEnvironmentStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApiEnvironmentStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApiIncrement(
            self,
            request: models.ModifyApiIncrementRequest,
            opts: Dict = None,
    ) -> models.ModifyApiIncrementResponse:
        """
        This API is used to incrementally update an API and mainly called by programs (different from `ModifyApi`, which requires that full API parameters be passed in and is suitable for use in the console).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApiIncrement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApiIncrementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIPStrategy(
            self,
            request: models.ModifyIPStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyIPStrategyResponse:
        """
        This API is used to modify a service IP policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIPStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIPStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPlugin(
            self,
            request: models.ModifyPluginRequest,
            opts: Dict = None,
    ) -> models.ModifyPluginResponse:
        """
        This API is used to modify a plugin.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyService(
            self,
            request: models.ModifyServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyServiceResponse:
        """
        This API is used to modify the relevant information of a service. After a service is created, its name, description, and service type can be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyServiceEnvironmentStrategy(
            self,
            request: models.ModifyServiceEnvironmentStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyServiceEnvironmentStrategyResponse:
        """
        This API is used to modify a service throttling policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyServiceEnvironmentStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyServiceEnvironmentStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubDomain(
            self,
            request: models.ModifySubDomainRequest,
            opts: Dict = None,
    ) -> models.ModifySubDomainResponse:
        """
        This API is used to modify the path mapping in the custom domain name settings of a service. The path mapping rule can be modified before it is bound to the custom domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUpstream(
            self,
            request: models.ModifyUpstreamRequest,
            opts: Dict = None,
    ) -> models.ModifyUpstreamResponse:
        """
        This API is used to modify an upstream.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUpstream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUpstreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUsagePlan(
            self,
            request: models.ModifyUsagePlanRequest,
            opts: Dict = None,
    ) -> models.ModifyUsagePlanResponse:
        """
        This API is used to modify the name, description, and QPS of a usage plan.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUsagePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUsagePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseService(
            self,
            request: models.ReleaseServiceRequest,
            opts: Dict = None,
    ) -> models.ReleaseServiceResponse:
        """
        This API is used to publish a service.
        An API Gateway service can only be called when it is published to an environment and takes effect after creation. This API is used to publish a service to an environment such as the `release` environment.
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetAPIDocPassword(
            self,
            request: models.ResetAPIDocPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetAPIDocPasswordResponse:
        """
        This API is used to reset the password of an API document.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetAPIDocPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetAPIDocPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnBindEnvironment(
            self,
            request: models.UnBindEnvironmentRequest,
            opts: Dict = None,
    ) -> models.UnBindEnvironmentResponse:
        """
        This API is used to unbind a usage plan from a specified environment.
        """
        
        kwargs = {}
        kwargs["action"] = "UnBindEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnBindEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnBindIPStrategy(
            self,
            request: models.UnBindIPStrategyRequest,
            opts: Dict = None,
    ) -> models.UnBindIPStrategyResponse:
        """
        This API is used to unbind an IP policy from a service.
        """
        
        kwargs = {}
        kwargs["action"] = "UnBindIPStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnBindIPStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnBindSecretIds(
            self,
            request: models.UnBindSecretIdsRequest,
            opts: Dict = None,
    ) -> models.UnBindSecretIdsResponse:
        """
        This API is used to unbind a key from a usage plan.
        """
        
        kwargs = {}
        kwargs["action"] = "UnBindSecretIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnBindSecretIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnBindSubDomain(
            self,
            request: models.UnBindSubDomainRequest,
            opts: Dict = None,
    ) -> models.UnBindSubDomainResponse:
        """
        This API is used to unbind a custom domain name.
        After binding a custom domain name to a service by using API Gateway, you can use this API to unbind it.
        """
        
        kwargs = {}
        kwargs["action"] = "UnBindSubDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnBindSubDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnReleaseService(
            self,
            request: models.UnReleaseServiceRequest,
            opts: Dict = None,
    ) -> models.UnReleaseServiceResponse:
        """
        This API is used to deactivate a service.
        Only after a service is published to an environment can its APIs be called. You can call this API to deactivate a service in the release environment. Once deactivated, the service cannot be called.
        """
        
        kwargs = {}
        kwargs["action"] = "UnReleaseService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnReleaseServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindApiApp(
            self,
            request: models.UnbindApiAppRequest,
            opts: Dict = None,
    ) -> models.UnbindApiAppResponse:
        """
        This API is used to unbind an application from an API.
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindApiApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindApiAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateApiAppKey(
            self,
            request: models.UpdateApiAppKeyRequest,
            opts: Dict = None,
    ) -> models.UpdateApiAppKeyResponse:
        """
        This API is used to update an application key.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateApiAppKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateApiAppKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateApiKey(
            self,
            request: models.UpdateApiKeyRequest,
            opts: Dict = None,
    ) -> models.UpdateApiKeyResponse:
        """
        This API is used to update a created API key pair.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateService(
            self,
            request: models.UpdateServiceRequest,
            opts: Dict = None,
    ) -> models.UpdateServiceResponse:
        """
        This API is used to switch the running version of a service published in an environment to a specified version. After you create a service by using API Gateway and publish it to an environment, multiple versions will be generated during development. In this case, you can call this API to switch versions.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)