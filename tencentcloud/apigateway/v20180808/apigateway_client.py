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
from tencentcloud.apigateway.v20180808 import models


class ApigatewayClient(AbstractClient):
    _apiVersion = '2018-08-08'
    _endpoint = 'apigateway.tencentcloudapi.com'
    _service = 'apigateway'


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
            body = self.call("BindEnvironment", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindEnvironmentResponse()
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


    def BindIPStrategy(self, request):
        """This API is used to bind an IP policy to an API.

        :param request: Request instance for BindIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.BindIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.BindIPStrategyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindIPStrategy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindIPStrategyResponse()
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


    def BindSecretIds(self, request):
        """This API is used to bind a key to a usage plan.
        You can bind a key to a usage plan and bind the usage plan to an environment where a service is published, so that callers can use the key to call APIs in the service. You can use this API to bind a key to a usage plan.

        :param request: Request instance for BindSecretIds.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.BindSecretIdsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.BindSecretIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindSecretIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindSecretIdsResponse()
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


    def BindSubDomain(self, request):
        """This API is used to bind a custom domain name to a service.
        Each service in API Gateway provides a default domain name for users to call. If you want to use your own domain name, you can bind a custom domain name to the target service. After getting the ICP filing and configuring the CNAME record between the custom and default domain names, you can directly call the custom domain name.

        :param request: Request instance for BindSubDomain.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.BindSubDomainRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.BindSubDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindSubDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindSubDomainResponse()
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


    def CreateApi(self, request):
        """This API is used to create an API. Before creating an API, you need to create a service, as each API belongs to a certain service.

        :param request: Request instance for CreateApi.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateApiRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateApiResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateApi", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateApiResponse()
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


    def CreateApiKey(self, request):
        """This API is used to create an API key pair.

        :param request: Request instance for CreateApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateApiKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateApiKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateApiKeyResponse()
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


    def CreateIPStrategy(self, request):
        """This API is used to create a service IP policy.

        :param request: Request instance for CreateIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateIPStrategyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateIPStrategy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateIPStrategyResponse()
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


    def CreateService(self, request):
        """This API is used to create a service.
        The maximum unit in API Gateway is service. Multiple APIs can be created in one service, and each service has a default domain name for users to call. You can also bind your own custom domain name to a service.

        :param request: Request instance for CreateService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServiceResponse()
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


    def CreateUsagePlan(self, request):
        """This API is used to create a usage plan.
        To use API Gateway, you need to create a usage plan and bind it to a service environment.

        :param request: Request instance for CreateUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateUsagePlanResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateUsagePlan", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUsagePlanResponse()
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


    def DeleteApi(self, request):
        """This API is used to delete a created API.

        :param request: Request instance for DeleteApi.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteApiRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteApiResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteApi", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteApiResponse()
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


    def DeleteApiKey(self, request):
        """This API is used to delete an API key pair.

        :param request: Request instance for DeleteApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteApiKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteApiKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteApiKeyResponse()
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


    def DeleteIPStrategy(self, request):
        """This API is used to delete a service IP policy.

        :param request: Request instance for DeleteIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteIPStrategyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteIPStrategy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteIPStrategyResponse()
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


    def DeleteService(self, request):
        """This API is used to delete a service in API Gateway.

        :param request: Request instance for DeleteService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteServiceResponse()
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


    def DeleteServiceSubDomainMapping(self, request):
        """This API is used to delete a custom domain name mapping in a service environment.
        You can use this API if you use a custom domain name and custom mapping. Please note that if you delete all mappings in all environments, a failure will be returned when this API is called.

        :param request: Request instance for DeleteServiceSubDomainMapping.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteServiceSubDomainMappingRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteServiceSubDomainMappingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteServiceSubDomainMapping", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteServiceSubDomainMappingResponse()
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


    def DeleteUsagePlan(self, request):
        """This API is used to delete a usage plan.

        :param request: Request instance for DeleteUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteUsagePlanResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteUsagePlan", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUsagePlanResponse()
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
            body = self.call("DemoteServiceUsagePlan", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DemoteServiceUsagePlanResponse()
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


    def DescribeApi(self, request):
        """This API (`DescribeApi`) is used to query the details of the APIs users manage via Tencent Cloud API Gateway.

        :param request: Request instance for DescribeApi.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApi", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApiResponse()
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


    def DescribeApiEnvironmentStrategy(self, request):
        """This API is used to display the throttling policies bound to an API.

        :param request: Request instance for DescribeApiEnvironmentStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiEnvironmentStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiEnvironmentStrategyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApiEnvironmentStrategy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApiEnvironmentStrategyResponse()
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


    def DescribeApiKey(self, request):
        """This API is used to query the details of a key.
        After creating an API key, you can query its details by using this API.

        :param request: Request instance for DescribeApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApiKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApiKeyResponse()
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


    def DescribeApiKeysStatus(self, request):
        """This API is used to query the list of keys.
        If you have created multiple API key pairs, you can use this API to query the information of one or more keys. This API does not display the `secretKey`.

        :param request: Request instance for DescribeApiKeysStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiKeysStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiKeysStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApiKeysStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApiKeysStatusResponse()
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


    def DescribeApiUsagePlan(self, request):
        """This API is used to query the details of API usage plans in a service.
        To make authentication and throttling for a service take effect, you need to bind a usage plan to it. This API is used to query all usage plans bound to a service and APIs under it.

        :param request: Request instance for DescribeApiUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiUsagePlanResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApiUsagePlan", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApiUsagePlanResponse()
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


    def DescribeApisStatus(self, request):
        """This API is used to view a certain API or the list of all APIs under a service and relevant information.

        :param request: Request instance for DescribeApisStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApisStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApisStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApisStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApisStatusResponse()
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


    def DescribeIPStrategy(self, request):
        """This API is used to query IP policy details.

        :param request: Request instance for DescribeIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIPStrategy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIPStrategyResponse()
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


    def DescribeIPStrategyApisStatus(self, request):
        """This API is used to query the list of APIs to which an IP policy can be bound, i.e., the difference set between all APIs under the service and the APIs already bound to the policy.

        :param request: Request instance for DescribeIPStrategyApisStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategyApisStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategyApisStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIPStrategyApisStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIPStrategyApisStatusResponse()
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


    def DescribeIPStrategysStatus(self, request):
        """This API is used to query the list of service IP policies.

        :param request: Request instance for DescribeIPStrategysStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategysStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategysStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIPStrategysStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIPStrategysStatusResponse()
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


    def DescribeLogSearch(self, request):
        """This API is used to search for logs.

        :param request: Request instance for DescribeLogSearch.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeLogSearchRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeLogSearchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLogSearch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogSearchResponse()
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


    def DescribeService(self, request):
        """This API is used to query the details of a service, such as its description, domain name, protocol, creation time, and releases.

        :param request: Request instance for DescribeService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceResponse()
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


    def DescribeServiceEnvironmentList(self, request):
        """This API is used to query the list of environments under a service. All environments and their statuses under the queried service will be returned.

        :param request: Request instance for DescribeServiceEnvironmentList.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentListRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServiceEnvironmentList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceEnvironmentListResponse()
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


    def DescribeServiceEnvironmentReleaseHistory(self, request):
        """This API is used to query the release history in a service environment.
        A service can only be used when it is published to an environment after creation. This API is used to query the release history in an environment under a service.

        :param request: Request instance for DescribeServiceEnvironmentReleaseHistory.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentReleaseHistoryRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentReleaseHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServiceEnvironmentReleaseHistory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceEnvironmentReleaseHistoryResponse()
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


    def DescribeServiceEnvironmentStrategy(self, request):
        """This API is used to display a service throttling policy.

        :param request: Request instance for DescribeServiceEnvironmentStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentStrategyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServiceEnvironmentStrategy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceEnvironmentStrategyResponse()
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


    def DescribeServiceReleaseVersion(self, request):
        """This API is used to query the list of all published versions under a service.
        A service is generally published on several versions. This API can be used to query the published versions.

        :param request: Request instance for DescribeServiceReleaseVersion.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceReleaseVersionRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceReleaseVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServiceReleaseVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceReleaseVersionResponse()
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


    def DescribeServiceSubDomainMappings(self, request):
        """This API is used to query the path mappings of a custom domain name.
        In API Gateway, you can bind a custom domain name to a service and map its paths. You can customize different path mappings to up to 3 environments under the service. This API is used to query the list of path mappings of a custom domain name bound to a service.

        :param request: Request instance for DescribeServiceSubDomainMappings.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceSubDomainMappingsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceSubDomainMappingsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServiceSubDomainMappings", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceSubDomainMappingsResponse()
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


    def DescribeServiceSubDomains(self, request):
        """This API is used to query the list of custom domain names.
        In API Gateway, you can bind custom domain names to a service for service call. This API is used to query the list of custom domain names bound to a service.

        :param request: Request instance for DescribeServiceSubDomains.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceSubDomainsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceSubDomainsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServiceSubDomains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceSubDomainsResponse()
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


    def DescribeServiceUsagePlan(self, request):
        """This API is used to query the details of usage plans in a service.
        To make authentication and throttling for a service take effect, you need to bind a usage plan to it. This API is used to query all usage plans bound to a service.

        :param request: Request instance for DescribeServiceUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceUsagePlanResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServiceUsagePlan", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceUsagePlanResponse()
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


    def DescribeServicesStatus(self, request):
        """This API is used to query the list of one or more services and return relevant domain name, time, and other information.

        :param request: Request instance for DescribeServicesStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServicesStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServicesStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServicesStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServicesStatusResponse()
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


    def DescribeUsagePlan(self, request):
        """This API is used to query the details of a usage plan, such as its name, QPS, creation time, and bound environment.

        :param request: Request instance for DescribeUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUsagePlan", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUsagePlanResponse()
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


    def DescribeUsagePlanEnvironments(self, request):
        """This API is used to query the list of environments bound to a usage plan.
        After binding a usage plan to environments, you can use this API to query all service environments bound to the usage plan.

        :param request: Request instance for DescribeUsagePlanEnvironments.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanEnvironmentsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUsagePlanEnvironments", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUsagePlanEnvironmentsResponse()
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


    def DescribeUsagePlanSecretIds(self, request):
        """This API is used to query the list of keys bound to a usage plan.
        In API Gateway, a usage plan can be bound to multiple key pairs. You can use this API to query the list of keys bound to it.

        :param request: Request instance for DescribeUsagePlanSecretIds.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanSecretIdsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanSecretIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUsagePlanSecretIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUsagePlanSecretIdsResponse()
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


    def DescribeUsagePlansStatus(self, request):
        """This API is used to query the list of usage plans.

        :param request: Request instance for DescribeUsagePlansStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlansStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlansStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUsagePlansStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUsagePlansStatusResponse()
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


    def DisableApiKey(self, request):
        """This API is used to disable an API key.

        :param request: Request instance for DisableApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DisableApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DisableApiKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableApiKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableApiKeyResponse()
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


    def EnableApiKey(self, request):
        """This API is used to enable a disabled API key.

        :param request: Request instance for EnableApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.EnableApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.EnableApiKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableApiKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableApiKeyResponse()
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


    def GenerateApiDocument(self, request):
        """This API is used to automatically generate API documents and SDKs. One document and one SDK will be generated for each environment under each service, respectively.

        :param request: Request instance for GenerateApiDocument.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.GenerateApiDocumentRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.GenerateApiDocumentResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GenerateApiDocument", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GenerateApiDocumentResponse()
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


    def ModifyApi(self, request):
        """This API is used to modify an API. You can call this API to edit/modify a configured API. The modified API takes effect only after its service is published to the corresponding environment again.

        :param request: Request instance for ModifyApi.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyApi", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyApiResponse()
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


    def ModifyApiEnvironmentStrategy(self, request):
        """This API is used to modify an API throttling policy.

        :param request: Request instance for ModifyApiEnvironmentStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiEnvironmentStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiEnvironmentStrategyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyApiEnvironmentStrategy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyApiEnvironmentStrategyResponse()
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


    def ModifyApiIncrement(self, request):
        """This API is used to incrementally update an API and mainly called by programs (different from `ModifyApi`, which requires that full API parameters be passed in and is suitable for use in the console).

        :param request: Request instance for ModifyApiIncrement.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiIncrementRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiIncrementResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyApiIncrement", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyApiIncrementResponse()
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


    def ModifyIPStrategy(self, request):
        """This API is used to modify a service IP policy.

        :param request: Request instance for ModifyIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyIPStrategyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyIPStrategy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyIPStrategyResponse()
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


    def ModifyService(self, request):
        """This API is used to modify the relevant information of a service. After a service is created, its name, description, and service type can be modified.

        :param request: Request instance for ModifyService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyServiceResponse()
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


    def ModifyServiceEnvironmentStrategy(self, request):
        """This API is used to modify a service throttling policy.

        :param request: Request instance for ModifyServiceEnvironmentStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyServiceEnvironmentStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyServiceEnvironmentStrategyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyServiceEnvironmentStrategy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyServiceEnvironmentStrategyResponse()
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


    def ModifySubDomain(self, request):
        """This API is used to modify the path mapping in the custom domain name settings of a service. The path mapping rule can be modified before it is bound to the custom domain name.

        :param request: Request instance for ModifySubDomain.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifySubDomainRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifySubDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySubDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubDomainResponse()
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


    def ModifyUsagePlan(self, request):
        """This API is used to modify the name, description, and QPS of a usage plan.

        :param request: Request instance for ModifyUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyUsagePlanResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyUsagePlan", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyUsagePlanResponse()
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


    def ReleaseService(self, request):
        """This API is used to publish a service.
        An API Gateway service can only be called when it is published to an environment and takes effect after creation. This API is used to publish a service to an environment such as the `release` environment.

        :param request: Request instance for ReleaseService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ReleaseServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ReleaseServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReleaseService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReleaseServiceResponse()
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


    def UnBindEnvironment(self, request):
        """This API is used to unbind a usage plan from a specified environment.

        :param request: Request instance for UnBindEnvironment.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UnBindEnvironmentRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UnBindEnvironmentResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnBindEnvironment", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnBindEnvironmentResponse()
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


    def UnBindIPStrategy(self, request):
        """This API is used to unbind an IP policy from a service.

        :param request: Request instance for UnBindIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UnBindIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UnBindIPStrategyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnBindIPStrategy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnBindIPStrategyResponse()
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


    def UnBindSecretIds(self, request):
        """This API is used to unbind a key from a usage plan.

        :param request: Request instance for UnBindSecretIds.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UnBindSecretIdsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UnBindSecretIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnBindSecretIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnBindSecretIdsResponse()
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


    def UnBindSubDomain(self, request):
        """This API is used to unbind a custom domain name.
        After binding a custom domain name to a service by using API Gateway, you can use this API to unbind it.

        :param request: Request instance for UnBindSubDomain.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UnBindSubDomainRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UnBindSubDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnBindSubDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnBindSubDomainResponse()
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


    def UnReleaseService(self, request):
        """This API is used to deactivate a service.
        Only after a service is published to an environment can its APIs be called. You can call this API to deactivate a service in the release environment. Once deactivated, the service cannot be called.

        :param request: Request instance for UnReleaseService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UnReleaseServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UnReleaseServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnReleaseService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnReleaseServiceResponse()
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


    def UpdateApiKey(self, request):
        """This API is used to update a created API key pair.

        :param request: Request instance for UpdateApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UpdateApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UpdateApiKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateApiKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateApiKeyResponse()
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


    def UpdateService(self, request):
        """This API is used to switch the running version of a service published in an environment to a specified version. After you create a service by using API Gateway and publish it to an environment, multiple versions will be generated during development. In this case, you can call this API to switch versions.

        :param request: Request instance for UpdateService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UpdateServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UpdateServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateServiceResponse()
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