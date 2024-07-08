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
from tencentcloud.apigateway.v20180808 import models


class ApigatewayClient(AbstractClient):
    _apiVersion = '2018-08-08'
    _endpoint = 'apigateway.tencentcloudapi.com'
    _service = 'apigateway'


    def AttachPlugin(self, request):
        """This API is used to bind a plugin to an API.

        :param request: Request instance for AttachPlugin.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.AttachPluginRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.AttachPluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachPlugin", params, headers=headers)
            response = json.loads(body)
            model = models.AttachPluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindApiApp(self, request):
        """This API is used to bind an application to an API.

        :param request: Request instance for BindApiApp.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.BindApiAppRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.BindApiAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindApiApp", params, headers=headers)
            response = json.loads(body)
            model = models.BindApiAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindEnvironment(self, request):
        """This API is used to bind a usage plan to a service or API.
        After you publish a service to an environment, if the API requires authentication and can be called only when it is bound to a usage plan, you can use this API to bind a usage plan to the specified environment.
        Currently, a usage plan can be bound to an API; however, under the same service, usage plans bound to a service and usage plans bound to an API cannot coexist. Therefore, in an environment to which a service-level usage plan has already been bound, please use the `DemoteServiceUsagePlan` API to degrade it.

        :param request: Request instance for BindEnvironment.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.BindEnvironmentRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.BindEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.BindEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindIPStrategy(self, request):
        """This API is used to bind an IP policy to an API.

        :param request: Request instance for BindIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.BindIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.BindIPStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindIPStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.BindIPStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindSecretIds(self, request):
        """This API is used to bind a key to a usage plan.
        You can bind a key to a usage plan and bind the usage plan to an environment where a service is published, so that callers can use the key to call APIs in the service. You can use this API to bind a key to a usage plan.

        :param request: Request instance for BindSecretIds.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.BindSecretIdsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.BindSecretIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindSecretIds", params, headers=headers)
            response = json.loads(body)
            model = models.BindSecretIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindSubDomain(self, request):
        """This API is used to bind a custom domain name to a service.
        Each service in API Gateway provides a default domain name for users to call. If you want to use your own domain name, you can bind a custom domain name to the target service. After getting the ICP filing and configuring the CNAME record between the custom and default domain names, you can directly call the custom domain name.

        :param request: Request instance for BindSubDomain.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.BindSubDomainRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.BindSubDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindSubDomain", params, headers=headers)
            response = json.loads(body)
            model = models.BindSubDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BuildAPIDoc(self, request):
        """This API is used to build an API document.

        :param request: Request instance for BuildAPIDoc.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.BuildAPIDocRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.BuildAPIDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BuildAPIDoc", params, headers=headers)
            response = json.loads(body)
            model = models.BuildAPIDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAPIDoc(self, request):
        """This API is used to create an API document.

        :param request: Request instance for CreateAPIDoc.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateAPIDocRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateAPIDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAPIDoc", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAPIDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApi(self, request):
        """This API is used to create an API. Before creating an API, you need to create a service, as each API belongs to a certain service.

        :param request: Request instance for CreateApi.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateApiRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApi", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApiApp(self, request):
        """This API is used to create an application.

        :param request: Request instance for CreateApiApp.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateApiAppRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateApiAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApiApp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApiAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApiKey(self, request):
        """This API is used to create an API key pair.

        :param request: Request instance for CreateApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIPStrategy(self, request):
        """This API is used to create a service IP policy.

        :param request: Request instance for CreateIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateIPStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIPStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIPStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePlugin(self, request):
        """This API is used to create an API Gateway plugin.

        :param request: Request instance for CreatePlugin.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreatePluginRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreatePluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePlugin", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateService(self, request):
        """This API is used to create a service.
        A service is the biggest usage unit in API Gateway. Each service can contain multiple APIs and one default domain name for invocation. You can also bind your own custom domain name to a service.

        :param request: Request instance for CreateService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUpstream(self, request):
        """This API is used to create an upstream.

        :param request: Request instance for CreateUpstream.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateUpstreamRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateUpstreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUpstream", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUpstreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUsagePlan(self, request):
        """This API is used to create a usage plan.
        To use API Gateway, you need to create a usage plan and bind it to a service environment.

        :param request: Request instance for CreateUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateUsagePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUsagePlan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUsagePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAPIDoc(self, request):
        """This API is used to delete an API document.

        :param request: Request instance for DeleteAPIDoc.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteAPIDocRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteAPIDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAPIDoc", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAPIDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApi(self, request):
        """This API is used to delete a created API.

        :param request: Request instance for DeleteApi.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteApiRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApi", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApiApp(self, request):
        """This API is used to delete a created application.

        :param request: Request instance for DeleteApiApp.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteApiAppRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteApiAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApiApp", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApiAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApiKey(self, request):
        """This API is used to delete an API key pair.

        :param request: Request instance for DeleteApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIPStrategy(self, request):
        """This API is used to delete a service IP policy.

        :param request: Request instance for DeleteIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteIPStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIPStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIPStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePlugin(self, request):
        """This API is used to delete an API Gateway plugin.

        :param request: Request instance for DeletePlugin.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeletePluginRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeletePluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePlugin", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteService(self, request):
        """This API is used to delete a service in API Gateway.

        :param request: Request instance for DeleteService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteService", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteServiceSubDomainMapping(self, request):
        """This API is used to delete a custom domain name mapping in a service environment.
        You can use this API if you use a custom domain name and custom mapping. Please note that if you delete all mappings in all environments, a failure will be returned when this API is called.

        :param request: Request instance for DeleteServiceSubDomainMapping.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteServiceSubDomainMappingRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteServiceSubDomainMappingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteServiceSubDomainMapping", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServiceSubDomainMappingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUpstream(self, request):
        """This API is used to delete an upstream. Note that you can only delete an upstream when it’s not bound with any APIs.

        :param request: Request instance for DeleteUpstream.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteUpstreamRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteUpstreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUpstream", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUpstreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUsagePlan(self, request):
        """This API is used to delete a usage plan.

        :param request: Request instance for DeleteUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteUsagePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUsagePlan", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUsagePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DemoteServiceUsagePlan(self, request):
        """This API is used to degrade a usage plan of a service in an environment to the API level.
        This operation will be denied if there are no APIs under the service.
        This operation will also be denied if the current environment has not been published.

        :param request: Request instance for DemoteServiceUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DemoteServiceUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DemoteServiceUsagePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DemoteServiceUsagePlan", params, headers=headers)
            response = json.loads(body)
            model = models.DemoteServiceUsagePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAPIDocDetail(self, request):
        """This API is used to query the details of an API document.

        :param request: Request instance for DescribeAPIDocDetail.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeAPIDocDetailRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeAPIDocDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAPIDocDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAPIDocDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAPIDocs(self, request):
        """This API is used to query the list of API documents.

        :param request: Request instance for DescribeAPIDocs.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeAPIDocsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeAPIDocsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAPIDocs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAPIDocsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllPluginApis(self, request):
        """This API is used to list all APIs that can use this plugin, no matter whether the API is bound with the plugin.

        :param request: Request instance for DescribeAllPluginApis.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeAllPluginApisRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeAllPluginApisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllPluginApis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllPluginApisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApi(self, request):
        """This API (`DescribeApi`) is used to query the details of the APIs users manage via Tencent Cloud API Gateway.

        :param request: Request instance for DescribeApi.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApi", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiApp(self, request):
        """This API is used to search for an application by application ID.

        :param request: Request instance for DescribeApiApp.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiAppRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiApp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiAppBindApisStatus(self, request):
        """This API is used to query the list of APIs bound to an application.

        :param request: Request instance for DescribeApiAppBindApisStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiAppBindApisStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiAppBindApisStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiAppBindApisStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiAppBindApisStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiAppsStatus(self, request):
        """This API is used to query the application list.

        :param request: Request instance for DescribeApiAppsStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiAppsStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiAppsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiAppsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiAppsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiBindApiAppsStatus(self, request):
        """This API is used to query the list of applications bound to an API.

        :param request: Request instance for DescribeApiBindApiAppsStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiBindApiAppsStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiBindApiAppsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiBindApiAppsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiBindApiAppsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiEnvironmentStrategy(self, request):
        """This API is used to display the throttling policies bound to an API.

        :param request: Request instance for DescribeApiEnvironmentStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiEnvironmentStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiEnvironmentStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiEnvironmentStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiEnvironmentStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiForApiApp(self, request):
        """This API is used to query the details of an API deployed at API Gateway.

        :param request: Request instance for DescribeApiForApiApp.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiForApiAppRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiForApiAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiForApiApp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiForApiAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiKey(self, request):
        """This API is used to query the details of a key.
        After creating an API key, you can query its details by using this API.

        :param request: Request instance for DescribeApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiKeysStatus(self, request):
        """This API is used to query the information of one or more API keys.


        :param request: Request instance for DescribeApiKeysStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiKeysStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiKeysStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiKeysStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiKeysStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiUsagePlan(self, request):
        """This API is used to query the details of API usage plans in a service.
        To make authentication and throttling for a service take effect, you need to bind a usage plan to it. This API is used to query all usage plans bound to a service and APIs under it.

        :param request: Request instance for DescribeApiUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiUsagePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiUsagePlan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiUsagePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApisStatus(self, request):
        """This API is used to view a certain API or the list of all APIs under a service and relevant information.

        :param request: Request instance for DescribeApisStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApisStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApisStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApisStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApisStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIPStrategy(self, request):
        """This API is used to query IP policy details.

        :param request: Request instance for DescribeIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIPStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIPStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIPStrategyApisStatus(self, request):
        """This API is used to query the list of APIs to which an IP policy can be bound, i.e., the difference set between all APIs under the service and the APIs already bound to the policy.

        :param request: Request instance for DescribeIPStrategyApisStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategyApisStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategyApisStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIPStrategyApisStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIPStrategyApisStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIPStrategysStatus(self, request):
        """This API is used to query the list of service IP policies.

        :param request: Request instance for DescribeIPStrategysStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategysStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategysStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIPStrategysStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIPStrategysStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogSearch(self, request):
        """This API is used to search for logs.

        :param request: Request instance for DescribeLogSearch.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeLogSearchRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeLogSearchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogSearch", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogSearchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePlugin(self, request):
        """This API is used to query the plugin details by plugin ID.

        :param request: Request instance for DescribePlugin.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribePluginRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribePluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlugin", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePluginApis(self, request):
        """This API is used to query APIs bound with a specified plugin.

        :param request: Request instance for DescribePluginApis.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribePluginApisRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribePluginApisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePluginApis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePluginApisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePluginsByApi(self, request):
        """This API is used to query all plug-ins bound with the API.

        :param request: Request instance for DescribePluginsByApi.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribePluginsByApiRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribePluginsByApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePluginsByApi", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePluginsByApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeService(self, request):
        """This API is used to query the details of a service, such as its description, domain name, protocol, creation time, and releases.

        :param request: Request instance for DescribeService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceEnvironmentList(self, request):
        """This API is used to query the list of environments under a service. All environments and their statuses under the queried service will be returned.

        :param request: Request instance for DescribeServiceEnvironmentList.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentListRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceEnvironmentList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceEnvironmentListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceEnvironmentReleaseHistory(self, request):
        """This API is used to query the release history in a service environment.
        A service can only be used when it is published to an environment after creation. This API is used to query the release history in an environment under a service.

        :param request: Request instance for DescribeServiceEnvironmentReleaseHistory.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentReleaseHistoryRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentReleaseHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceEnvironmentReleaseHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceEnvironmentReleaseHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceEnvironmentStrategy(self, request):
        """This API is used to display a service throttling policy.

        :param request: Request instance for DescribeServiceEnvironmentStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceEnvironmentStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceEnvironmentStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceForApiApp(self, request):
        """This API is used to query the details of a service, such as its description, domain name, and protocol.

        :param request: Request instance for DescribeServiceForApiApp.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceForApiAppRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceForApiAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceForApiApp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceForApiAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceReleaseVersion(self, request):
        """This API is used to query the list of all published versions under a service.
        A service is generally published on several versions. This API can be used to query the published versions.

        :param request: Request instance for DescribeServiceReleaseVersion.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceReleaseVersionRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceReleaseVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceReleaseVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceReleaseVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceSubDomainMappings(self, request):
        """This API is used to query the path mappings of a custom domain name.
        In API Gateway, you can bind a custom domain name to a service and map its paths. You can customize different path mappings to up to 3 environments under the service. This API is used to query the list of path mappings of a custom domain name bound to a service.

        :param request: Request instance for DescribeServiceSubDomainMappings.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceSubDomainMappingsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceSubDomainMappingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceSubDomainMappings", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceSubDomainMappingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceSubDomains(self, request):
        """This API is used to query the list of custom domain names.
        In API Gateway, you can bind custom domain names to a service for service call. This API is used to query the list of custom domain names bound to a service.

        :param request: Request instance for DescribeServiceSubDomains.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceSubDomainsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceSubDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceSubDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceSubDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceUsagePlan(self, request):
        """This API is used to query the details of usage plans in a service.
        To make authentication and throttling for a service take effect, you need to bind a usage plan to it. This API is used to query all usage plans bound to a service.

        :param request: Request instance for DescribeServiceUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceUsagePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceUsagePlan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceUsagePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServicesStatus(self, request):
        """This API is used to query the list of one or more services and return relevant domain name, time, and other information.

        :param request: Request instance for DescribeServicesStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServicesStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServicesStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServicesStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServicesStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUpstreamBindApis(self, request):
        """This API is used to query APIs bound with an upstream.

        :param request: Request instance for DescribeUpstreamBindApis.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeUpstreamBindApisRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeUpstreamBindApisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUpstreamBindApis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUpstreamBindApisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUpstreams(self, request):
        """This API is used to query details of upstreams under the current account.

        :param request: Request instance for DescribeUpstreams.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeUpstreamsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeUpstreamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUpstreams", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUpstreamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsagePlan(self, request):
        """This API is used to query the details of a usage plan, such as its name, QPS, creation time, and bound environment.

        :param request: Request instance for DescribeUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsagePlan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsagePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsagePlanEnvironments(self, request):
        """This API is used to query the list of environments bound to a usage plan.
        After binding a usage plan to environments, you can use this API to query all service environments bound to the usage plan.

        :param request: Request instance for DescribeUsagePlanEnvironments.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanEnvironmentsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsagePlanEnvironments", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsagePlanEnvironmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsagePlanSecretIds(self, request):
        """This API is used to query the list of keys bound to a usage plan.
        In API Gateway, a usage plan can be bound to multiple key pairs. You can use this API to query the list of keys bound to it.

        :param request: Request instance for DescribeUsagePlanSecretIds.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanSecretIdsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanSecretIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsagePlanSecretIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsagePlanSecretIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsagePlansStatus(self, request):
        """This API is used to query the list of usage plans.

        :param request: Request instance for DescribeUsagePlansStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlansStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlansStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsagePlansStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsagePlansStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachPlugin(self, request):
        """This API is used to unbind an API from the plugin.

        :param request: Request instance for DetachPlugin.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DetachPluginRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DetachPluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachPlugin", params, headers=headers)
            response = json.loads(body)
            model = models.DetachPluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableApiKey(self, request):
        """This API is used to disable an API key.

        :param request: Request instance for DisableApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DisableApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DisableApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.DisableApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableApiKey(self, request):
        """This API is used to enable a disabled API key.

        :param request: Request instance for EnableApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.EnableApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.EnableApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.EnableApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportOpenApi(self, request):
        """This API is used to import an OpenAPI to API gateway.

        :param request: Request instance for ImportOpenApi.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ImportOpenApiRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ImportOpenApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportOpenApi", params, headers=headers)
            response = json.loads(body)
            model = models.ImportOpenApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAPIDoc(self, request):
        """This API is used to modify an API document.

        :param request: Request instance for ModifyAPIDoc.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyAPIDocRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyAPIDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAPIDoc", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAPIDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApi(self, request):
        """This API is used to modify an API. You can call this API to edit/modify a configured API. The modified API takes effect only after its service is published to the corresponding environment again.

        :param request: Request instance for ModifyApi.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApi", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApiApp(self, request):
        """This API is used to modify a created API.

        :param request: Request instance for ModifyApiApp.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiAppRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApiApp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApiAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApiEnvironmentStrategy(self, request):
        """This API is used to modify an API throttling policy.

        :param request: Request instance for ModifyApiEnvironmentStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiEnvironmentStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiEnvironmentStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApiEnvironmentStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApiEnvironmentStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApiIncrement(self, request):
        """This API is used to incrementally update an API and mainly called by programs (different from `ModifyApi`, which requires that full API parameters be passed in and is suitable for use in the console).

        :param request: Request instance for ModifyApiIncrement.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiIncrementRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiIncrementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApiIncrement", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApiIncrementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIPStrategy(self, request):
        """This API is used to modify a service IP policy.

        :param request: Request instance for ModifyIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyIPStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIPStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIPStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPlugin(self, request):
        """This API is used to modify a plugin.

        :param request: Request instance for ModifyPlugin.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyPluginRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyPluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPlugin", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyService(self, request):
        """This API is used to modify the relevant information of a service. After a service is created, its name, description, and service type can be modified.

        :param request: Request instance for ModifyService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyServiceEnvironmentStrategy(self, request):
        """This API is used to modify a service throttling policy.

        :param request: Request instance for ModifyServiceEnvironmentStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyServiceEnvironmentStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyServiceEnvironmentStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyServiceEnvironmentStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyServiceEnvironmentStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySubDomain(self, request):
        """This API is used to modify the path mapping in the custom domain name settings of a service. The path mapping rule can be modified before it is bound to the custom domain name.

        :param request: Request instance for ModifySubDomain.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifySubDomainRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifySubDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUpstream(self, request):
        """This API is used to modify an upstream.

        :param request: Request instance for ModifyUpstream.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyUpstreamRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyUpstreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUpstream", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUpstreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUsagePlan(self, request):
        """This API is used to modify the name, description, and QPS of a usage plan.

        :param request: Request instance for ModifyUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyUsagePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUsagePlan", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUsagePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseService(self, request):
        """This API is used to publish a service.
        An API Gateway service can only be called when it is published to an environment and takes effect after creation. This API is used to publish a service to an environment such as the `release` environment.

        :param request: Request instance for ReleaseService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ReleaseServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ReleaseServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseService", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetAPIDocPassword(self, request):
        """This API is used to reset the password of an API document.

        :param request: Request instance for ResetAPIDocPassword.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ResetAPIDocPasswordRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ResetAPIDocPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetAPIDocPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetAPIDocPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnBindEnvironment(self, request):
        """This API is used to unbind a usage plan from a specified environment.

        :param request: Request instance for UnBindEnvironment.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UnBindEnvironmentRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UnBindEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnBindEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.UnBindEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnBindIPStrategy(self, request):
        """This API is used to unbind an IP policy from a service.

        :param request: Request instance for UnBindIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UnBindIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UnBindIPStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnBindIPStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.UnBindIPStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnBindSecretIds(self, request):
        """This API is used to unbind a key from a usage plan.

        :param request: Request instance for UnBindSecretIds.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UnBindSecretIdsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UnBindSecretIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnBindSecretIds", params, headers=headers)
            response = json.loads(body)
            model = models.UnBindSecretIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnBindSubDomain(self, request):
        """This API is used to unbind a custom domain name.
        After binding a custom domain name to a service by using API Gateway, you can use this API to unbind it.

        :param request: Request instance for UnBindSubDomain.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UnBindSubDomainRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UnBindSubDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnBindSubDomain", params, headers=headers)
            response = json.loads(body)
            model = models.UnBindSubDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnReleaseService(self, request):
        """This API is used to deactivate a service.
        Only after a service is published to an environment can its APIs be called. You can call this API to deactivate a service in the release environment. Once deactivated, the service cannot be called.

        :param request: Request instance for UnReleaseService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UnReleaseServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UnReleaseServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnReleaseService", params, headers=headers)
            response = json.loads(body)
            model = models.UnReleaseServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindApiApp(self, request):
        """This API is used to unbind an application from an API.

        :param request: Request instance for UnbindApiApp.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UnbindApiAppRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UnbindApiAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindApiApp", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindApiAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateApiAppKey(self, request):
        """This API is used to update an application key.

        :param request: Request instance for UpdateApiAppKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UpdateApiAppKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UpdateApiAppKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateApiAppKey", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateApiAppKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateApiKey(self, request):
        """This API is used to update a created API key pair.

        :param request: Request instance for UpdateApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UpdateApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UpdateApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateService(self, request):
        """This API is used to switch the running version of a service published in an environment to a specified version. After you create a service by using API Gateway and publish it to an environment, multiple versions will be generated during development. In this case, you can call this API to switch versions.

        :param request: Request instance for UpdateService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UpdateServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UpdateServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateService", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))