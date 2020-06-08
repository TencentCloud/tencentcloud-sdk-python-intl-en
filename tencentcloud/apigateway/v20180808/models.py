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

from tencentcloud.common.abstract_model import AbstractModel


class ApiEnvironmentStrategy(AbstractModel):
    """API environment binding policy

    """

    def __init__(self):
        """
        :param ApiId: Unique API ID.
        :type ApiId: str
        :param ApiName: Custom API name.
        :type ApiName: str
        :param Path: API path, such as `/path`.
        :type Path: str
        :param Method: API method, such as `GET`.
        :type Method: str
        :param EnvironmentStrategySet: Environment throttling information.
        :type EnvironmentStrategySet: list of EnvironmentStrategy
        """
        self.ApiId = None
        self.ApiName = None
        self.Path = None
        self.Method = None
        self.EnvironmentStrategySet = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.ApiName = params.get("ApiName")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        if params.get("EnvironmentStrategySet") is not None:
            self.EnvironmentStrategySet = []
            for item in params.get("EnvironmentStrategySet"):
                obj = EnvironmentStrategy()
                obj._deserialize(item)
                self.EnvironmentStrategySet.append(obj)


class ApiEnvironmentStrategyStataus(AbstractModel):
    """List of policies bound to API

    """

    def __init__(self):
        """
        :param TotalCount: Number of throttling policies bound to API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param ApiEnvironmentStrategySet: List of throttling policies bound to API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiEnvironmentStrategySet: list of ApiEnvironmentStrategy
        """
        self.TotalCount = None
        self.ApiEnvironmentStrategySet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiEnvironmentStrategySet") is not None:
            self.ApiEnvironmentStrategySet = []
            for item in params.get("ApiEnvironmentStrategySet"):
                obj = ApiEnvironmentStrategy()
                obj._deserialize(item)
                self.ApiEnvironmentStrategySet.append(obj)


class ApiIdStatus(AbstractModel):
    """API status

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param ApiId: Unique API ID.
        :type ApiId: str
        :param ApiDesc: API description
        :type ApiDesc: str
        :param Path: API path.
        :type Path: str
        :param Method: API method.
        :type Method: str
        :param CreatedTime: Service creation time.
        :type CreatedTime: str
        :param ModifiedTime: Service modification time.
        :type ModifiedTime: str
        :param ApiName: API name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiName: str
        :param UniqVpcId: Unique VPC ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UniqVpcId: str
        :param ApiType: API type.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiType: str
        :param Protocol: API protocol.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param IsDebugAfterCharge: Whether to enable debugging on purchase.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDebugAfterCharge: bool
        :param AuthType: Authorization type.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthType: str
        :param ApiBusinessType: API business type.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiBusinessType: str
        :param AuthRelationApiId: Unique ID of associated authorization API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthRelationApiId: str
        :param RelationBuniessApiIds: List of business APIs associated with authorization API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RelationBuniessApiIds: list of str
        :param OauthConfig: OAuth configuration information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param TokenLocation: Token storage position, which is an OAuth 2.0 API request.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TokenLocation: str
        """
        self.ServiceId = None
        self.ApiId = None
        self.ApiDesc = None
        self.Path = None
        self.Method = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ApiName = None
        self.UniqVpcId = None
        self.ApiType = None
        self.Protocol = None
        self.IsDebugAfterCharge = None
        self.AuthType = None
        self.ApiBusinessType = None
        self.AuthRelationApiId = None
        self.RelationBuniessApiIds = None
        self.OauthConfig = None
        self.TokenLocation = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        self.ApiDesc = params.get("ApiDesc")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ApiName = params.get("ApiName")
        self.UniqVpcId = params.get("UniqVpcId")
        self.ApiType = params.get("ApiType")
        self.Protocol = params.get("Protocol")
        self.IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        self.AuthType = params.get("AuthType")
        self.ApiBusinessType = params.get("ApiBusinessType")
        self.AuthRelationApiId = params.get("AuthRelationApiId")
        self.RelationBuniessApiIds = params.get("RelationBuniessApiIds")
        if params.get("OauthConfig") is not None:
            self.OauthConfig = OauthConfig()
            self.OauthConfig._deserialize(params.get("OauthConfig"))
        self.TokenLocation = params.get("TokenLocation")


class ApiInfo(AbstractModel):
    """API information

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of API's service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceId: str
        :param ServiceName: Name of API's service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceName: str
        :param ServiceDesc: Description of API's service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceDesc: str
        :param ApiId: Unique API ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiId: str
        :param ApiDesc: API description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiDesc: str
        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param ApiName: API name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiName: str
        :param ApiType: API type. Valid values: NORMAL (general API), TSF (microservice API).
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiType: str
        :param Protocol: API frontend request type, such as HTTP, HTTPS, or HTTP and HTTPS.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param AuthType: API authentication type. Valid values: SECRET (key pair authentication), NONE (no authentication), OAUTH.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthType: str
        :param ApiBusinessType: OAuth API type. Valid values: NORMAL (business API), OAUTH (authorization API).
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiBusinessType: str
        :param AuthRelationApiId: Unique ID of the authorization API associated with OAuth business API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthRelationApiId: str
        :param OauthConfig: OAuth configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param IsDebugAfterCharge: Whether to enable debugging on purchase (reserved for the marketplace).
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDebugAfterCharge: bool
        :param RequestConfig: Request frontend configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.RequestConfig`
        :param ResponseType: Return type.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseType: str
        :param ResponseSuccessExample: Successful response sample of custom response configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseSuccessExample: str
        :param ResponseFailExample: Response failure sample of custom response configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseFailExample: str
        :param ResponseErrorCodes: Custom error code configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseErrorCodes: list of ErrorCodes
        :param RequestParameters: Frontend request parameters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RequestParameters: list of ReqParameter
        :param ServiceTimeout: API backend service timeout period in seconds.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceTimeout: int
        :param ServiceType: API backend service type. Valid values: HTTP, MOCK, TSF, CLB, SCF, WEBSOCKET, TARGET (in beta test).
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceType: str
        :param ServiceConfig: API backend service configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`
        :param ServiceParameters: API backend service parameters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceParameters: list of ServiceParameter
        :param ConstantParameters: Constant parameters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ConstantParameters: list of ConstantParameter
        :param ServiceMockReturnMessage: Returned information of API backend mocking. This parameter is required when `ServiceType` is `Mock`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceMockReturnMessage: str
        :param ServiceScfFunctionName: SCF function name. This parameter takes effect when the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceScfFunctionName: str
        :param ServiceScfFunctionNamespace: SCF function namespace. This parameter takes effect when the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceScfFunctionNamespace: str
        :param ServiceScfFunctionQualifier: SCF function version. This parameter takes effect when the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceScfFunctionQualifier: str
        :param ServiceScfIsIntegratedResponse: Whether to enable integrated response.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceScfIsIntegratedResponse: bool
        :param ServiceWebsocketRegisterFunctionName: SCF WebSocket registration function namespace. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketRegisterFunctionName: str
        :param ServiceWebsocketRegisterFunctionNamespace: SCF WebSocket registration function namespace. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketRegisterFunctionNamespace: str
        :param ServiceWebsocketRegisterFunctionQualifier: SCF WebSocket transfer function version. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketRegisterFunctionQualifier: str
        :param ServiceWebsocketCleanupFunctionName: SCF WebSocket cleanup function. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketCleanupFunctionName: str
        :param ServiceWebsocketCleanupFunctionNamespace: SCF WebSocket cleanup function namespace. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketCleanupFunctionNamespace: str
        :param ServiceWebsocketCleanupFunctionQualifier: SCF WebSocket cleanup function version. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketCleanupFunctionQualifier: str
        :param InternalDomain: WebSocket pushback address.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InternalDomain: str
        :param ServiceWebsocketTransportFunctionName: SCF WebSocket transfer function. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketTransportFunctionName: str
        :param ServiceWebsocketTransportFunctionNamespace: SCF WebSocket transfer function namespace. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketTransportFunctionNamespace: str
        :param ServiceWebsocketTransportFunctionQualifier: SCF WebSocket transfer function version. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketTransportFunctionQualifier: str
        :param MicroServices: List of microservices bound to API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MicroServices: list of MicroService
        :param MicroServicesInfo: Microservice detailed information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MicroServicesInfo: list of int
        :param ServiceTsfLoadBalanceConf: Microservice load balancing configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`
        :param ServiceTsfHealthCheckConf: Microservice health check configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param EnableCORS: Whether to enable CORS.
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnableCORS: bool
        :param Tags: Information of tags bound to API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        """
        self.ServiceId = None
        self.ServiceName = None
        self.ServiceDesc = None
        self.ApiId = None
        self.ApiDesc = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ApiName = None
        self.ApiType = None
        self.Protocol = None
        self.AuthType = None
        self.ApiBusinessType = None
        self.AuthRelationApiId = None
        self.OauthConfig = None
        self.IsDebugAfterCharge = None
        self.RequestConfig = None
        self.ResponseType = None
        self.ResponseSuccessExample = None
        self.ResponseFailExample = None
        self.ResponseErrorCodes = None
        self.RequestParameters = None
        self.ServiceTimeout = None
        self.ServiceType = None
        self.ServiceConfig = None
        self.ServiceParameters = None
        self.ConstantParameters = None
        self.ServiceMockReturnMessage = None
        self.ServiceScfFunctionName = None
        self.ServiceScfFunctionNamespace = None
        self.ServiceScfFunctionQualifier = None
        self.ServiceScfIsIntegratedResponse = None
        self.ServiceWebsocketRegisterFunctionName = None
        self.ServiceWebsocketRegisterFunctionNamespace = None
        self.ServiceWebsocketRegisterFunctionQualifier = None
        self.ServiceWebsocketCleanupFunctionName = None
        self.ServiceWebsocketCleanupFunctionNamespace = None
        self.ServiceWebsocketCleanupFunctionQualifier = None
        self.InternalDomain = None
        self.ServiceWebsocketTransportFunctionName = None
        self.ServiceWebsocketTransportFunctionNamespace = None
        self.ServiceWebsocketTransportFunctionQualifier = None
        self.MicroServices = None
        self.MicroServicesInfo = None
        self.ServiceTsfLoadBalanceConf = None
        self.ServiceTsfHealthCheckConf = None
        self.EnableCORS = None
        self.Tags = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceName = params.get("ServiceName")
        self.ServiceDesc = params.get("ServiceDesc")
        self.ApiId = params.get("ApiId")
        self.ApiDesc = params.get("ApiDesc")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ApiName = params.get("ApiName")
        self.ApiType = params.get("ApiType")
        self.Protocol = params.get("Protocol")
        self.AuthType = params.get("AuthType")
        self.ApiBusinessType = params.get("ApiBusinessType")
        self.AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("OauthConfig") is not None:
            self.OauthConfig = OauthConfig()
            self.OauthConfig._deserialize(params.get("OauthConfig"))
        self.IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        if params.get("RequestConfig") is not None:
            self.RequestConfig = RequestConfig()
            self.RequestConfig._deserialize(params.get("RequestConfig"))
        self.ResponseType = params.get("ResponseType")
        self.ResponseSuccessExample = params.get("ResponseSuccessExample")
        self.ResponseFailExample = params.get("ResponseFailExample")
        if params.get("ResponseErrorCodes") is not None:
            self.ResponseErrorCodes = []
            for item in params.get("ResponseErrorCodes"):
                obj = ErrorCodes()
                obj._deserialize(item)
                self.ResponseErrorCodes.append(obj)
        if params.get("RequestParameters") is not None:
            self.RequestParameters = []
            for item in params.get("RequestParameters"):
                obj = ReqParameter()
                obj._deserialize(item)
                self.RequestParameters.append(obj)
        self.ServiceTimeout = params.get("ServiceTimeout")
        self.ServiceType = params.get("ServiceType")
        if params.get("ServiceConfig") is not None:
            self.ServiceConfig = ServiceConfig()
            self.ServiceConfig._deserialize(params.get("ServiceConfig"))
        if params.get("ServiceParameters") is not None:
            self.ServiceParameters = []
            for item in params.get("ServiceParameters"):
                obj = ServiceParameter()
                obj._deserialize(item)
                self.ServiceParameters.append(obj)
        if params.get("ConstantParameters") is not None:
            self.ConstantParameters = []
            for item in params.get("ConstantParameters"):
                obj = ConstantParameter()
                obj._deserialize(item)
                self.ConstantParameters.append(obj)
        self.ServiceMockReturnMessage = params.get("ServiceMockReturnMessage")
        self.ServiceScfFunctionName = params.get("ServiceScfFunctionName")
        self.ServiceScfFunctionNamespace = params.get("ServiceScfFunctionNamespace")
        self.ServiceScfFunctionQualifier = params.get("ServiceScfFunctionQualifier")
        self.ServiceScfIsIntegratedResponse = params.get("ServiceScfIsIntegratedResponse")
        self.ServiceWebsocketRegisterFunctionName = params.get("ServiceWebsocketRegisterFunctionName")
        self.ServiceWebsocketRegisterFunctionNamespace = params.get("ServiceWebsocketRegisterFunctionNamespace")
        self.ServiceWebsocketRegisterFunctionQualifier = params.get("ServiceWebsocketRegisterFunctionQualifier")
        self.ServiceWebsocketCleanupFunctionName = params.get("ServiceWebsocketCleanupFunctionName")
        self.ServiceWebsocketCleanupFunctionNamespace = params.get("ServiceWebsocketCleanupFunctionNamespace")
        self.ServiceWebsocketCleanupFunctionQualifier = params.get("ServiceWebsocketCleanupFunctionQualifier")
        self.InternalDomain = params.get("InternalDomain")
        self.ServiceWebsocketTransportFunctionName = params.get("ServiceWebsocketTransportFunctionName")
        self.ServiceWebsocketTransportFunctionNamespace = params.get("ServiceWebsocketTransportFunctionNamespace")
        self.ServiceWebsocketTransportFunctionQualifier = params.get("ServiceWebsocketTransportFunctionQualifier")
        if params.get("MicroServices") is not None:
            self.MicroServices = []
            for item in params.get("MicroServices"):
                obj = MicroService()
                obj._deserialize(item)
                self.MicroServices.append(obj)
        self.MicroServicesInfo = params.get("MicroServicesInfo")
        if params.get("ServiceTsfLoadBalanceConf") is not None:
            self.ServiceTsfLoadBalanceConf = TsfLoadBalanceConfResp()
            self.ServiceTsfLoadBalanceConf._deserialize(params.get("ServiceTsfLoadBalanceConf"))
        if params.get("ServiceTsfHealthCheckConf") is not None:
            self.ServiceTsfHealthCheckConf = HealthCheckConf()
            self.ServiceTsfHealthCheckConf._deserialize(params.get("ServiceTsfHealthCheckConf"))
        self.EnableCORS = params.get("EnableCORS")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class ApiKey(AbstractModel):
    """Key details

    """

    def __init__(self):
        """
        :param AccessKeyId: Created API key ID.
        :type AccessKeyId: str
        :param AccessKeySecret: Created API key.
        :type AccessKeySecret: str
        :param AccessKeyType: Key type. Valid values: auto, manual.
        :type AccessKeyType: str
        :param SecretName: Custom key name.
        :type SecretName: str
        :param ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
        :type ModifiedTime: str
        :param Status: Key status. 0: disabled. 1: enabled.
        :type Status: int
        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
        :type CreatedTime: str
        """
        self.AccessKeyId = None
        self.AccessKeySecret = None
        self.AccessKeyType = None
        self.SecretName = None
        self.ModifiedTime = None
        self.Status = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        self.AccessKeySecret = params.get("AccessKeySecret")
        self.AccessKeyType = params.get("AccessKeyType")
        self.SecretName = params.get("SecretName")
        self.ModifiedTime = params.get("ModifiedTime")
        self.Status = params.get("Status")
        self.CreatedTime = params.get("CreatedTime")


class ApiRequestConfig(AbstractModel):
    """API request configuration

    """

    def __init__(self):
        """
        :param Path: path
        :type Path: str
        :param Method: Method
        :type Method: str
        """
        self.Path = None
        self.Method = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Method = params.get("Method")


class ApiUsagePlan(AbstractModel):
    """Details of the usage plans bound to API or service

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceId: str
        :param ApiId: Unique API ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiId: str
        :param ApiName: API name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiName: str
        :param Path: API path.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Path: str
        :param Method: API method.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Method: str
        :param UsagePlanId: Unique usage plan ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanId: str
        :param UsagePlanName: Usage plan name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanName: str
        :param UsagePlanDesc: Usage plan description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanDesc: str
        :param Environment: Service environment bound to usage plan.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Environment: str
        :param InUseRequestNum: Used quota.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InUseRequestNum: int
        :param MaxRequestNum: Total number of requests allowed. `-1` indicates no limit.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxRequestNum: int
        :param MaxRequestNumPreSec: Request QPS upper limit. `-1` indicates no limit.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxRequestNumPreSec: int
        :param CreatedTime: Usage plan creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param ModifiedTime: Last modified time of usage plan.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param ServiceName: Service name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceName: str
        """
        self.ServiceId = None
        self.ApiId = None
        self.ApiName = None
        self.Path = None
        self.Method = None
        self.UsagePlanId = None
        self.UsagePlanName = None
        self.UsagePlanDesc = None
        self.Environment = None
        self.InUseRequestNum = None
        self.MaxRequestNum = None
        self.MaxRequestNumPreSec = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        self.ApiName = params.get("ApiName")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.UsagePlanId = params.get("UsagePlanId")
        self.UsagePlanName = params.get("UsagePlanName")
        self.UsagePlanDesc = params.get("UsagePlanDesc")
        self.Environment = params.get("Environment")
        self.InUseRequestNum = params.get("InUseRequestNum")
        self.MaxRequestNum = params.get("MaxRequestNum")
        self.MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ServiceName = params.get("ServiceName")


class ApiUsagePlanSet(AbstractModel):
    """List of usage plans bound to API

    """

    def __init__(self):
        """
        :param TotalCount: Total number of usage plans bound to API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param ApiUsagePlanList: List of usage plans bound to API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiUsagePlanList: list of ApiUsagePlan
        """
        self.TotalCount = None
        self.ApiUsagePlanList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiUsagePlanList") is not None:
            self.ApiUsagePlanList = []
            for item in params.get("ApiUsagePlanList"):
                obj = ApiUsagePlan()
                obj._deserialize(item)
                self.ApiUsagePlanList.append(obj)


class BindEnvironmentRequest(AbstractModel):
    """BindEnvironment request structure.

    """

    def __init__(self):
        """
        :param UsagePlanIds: List of unique IDs of the usage plans to be bound.
        :type UsagePlanIds: list of str
        :param BindType: Binding type. Valid values: API, SERVICE (default value).
        :type BindType: str
        :param Environment: Environment to be bound.
        :type Environment: str
        :param ServiceId: Unique ID of the service to be bound.
        :type ServiceId: str
        :param ApiIds: Unique API ID array. This parameter will be required when `bindType` is `API`.
        :type ApiIds: list of str
        """
        self.UsagePlanIds = None
        self.BindType = None
        self.Environment = None
        self.ServiceId = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.UsagePlanIds = params.get("UsagePlanIds")
        self.BindType = params.get("BindType")
        self.Environment = params.get("Environment")
        self.ServiceId = params.get("ServiceId")
        self.ApiIds = params.get("ApiIds")


class BindEnvironmentResponse(AbstractModel):
    """BindEnvironment response structure.

    """

    def __init__(self):
        """
        :param Result: Whether binding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BindIPStrategyRequest(AbstractModel):
    """BindIPStrategy request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of the service of the IP policy to be bound.
        :type ServiceId: str
        :param StrategyId: Unique ID of the IP policy to be bound.
        :type StrategyId: str
        :param EnvironmentName: Environment to be bound to IP policy
        :type EnvironmentName: str
        :param BindApiIds: List of APIs to be bound to IP policy.
        :type BindApiIds: list of str
        """
        self.ServiceId = None
        self.StrategyId = None
        self.EnvironmentName = None
        self.BindApiIds = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyId = params.get("StrategyId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.BindApiIds = params.get("BindApiIds")


class BindIPStrategyResponse(AbstractModel):
    """BindIPStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: Whether binding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BindSecretIdsRequest(AbstractModel):
    """BindSecretIds request structure.

    """

    def __init__(self):
        """
        :param UsagePlanId: Unique ID of the usage plan to be bound.
        :type UsagePlanId: str
        :param AccessKeyIds: Array of IDs of the keys to be bound.
        :type AccessKeyIds: list of str
        """
        self.UsagePlanId = None
        self.AccessKeyIds = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.AccessKeyIds = params.get("AccessKeyIds")


class BindSecretIdsResponse(AbstractModel):
    """BindSecretIds response structure.

    """

    def __init__(self):
        """
        :param Result: Whether binding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BindSubDomainRequest(AbstractModel):
    """BindSubDomain request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param SubDomain: Custom domain name to be bound.
        :type SubDomain: str
        :param Protocol: Protocols supported by service. Valid values: http, https, http&https.
        :type Protocol: str
        :param NetType: Network type. Valid values: INNER, OUTER.
        :type NetType: str
        :param IsDefaultMapping: Whether to use the default path mapping. The default value is `true`. If the value is `false`, the custom path mapping will be used and `PathMappingSet` is required.
        :type IsDefaultMapping: bool
        :param NetSubDomain: Default domain name.
        :type NetSubDomain: str
        :param CertificateId: Unique ID of the certificate of the custom domain name to be bound. The certificate can be uploaded only when `Protocol` is `https` or `http&https`.
        :type CertificateId: str
        :param PathMappingSet: Custom domain name path mapping. It can contain up to 3 `Environment` parameters which can be set to only `test`, `prepub`, or `release`.
        :type PathMappingSet: list of PathMapping
        """
        self.ServiceId = None
        self.SubDomain = None
        self.Protocol = None
        self.NetType = None
        self.IsDefaultMapping = None
        self.NetSubDomain = None
        self.CertificateId = None
        self.PathMappingSet = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.SubDomain = params.get("SubDomain")
        self.Protocol = params.get("Protocol")
        self.NetType = params.get("NetType")
        self.IsDefaultMapping = params.get("IsDefaultMapping")
        self.NetSubDomain = params.get("NetSubDomain")
        self.CertificateId = params.get("CertificateId")
        if params.get("PathMappingSet") is not None:
            self.PathMappingSet = []
            for item in params.get("PathMappingSet"):
                obj = PathMapping()
                obj._deserialize(item)
                self.PathMappingSet.append(obj)


class BindSubDomainResponse(AbstractModel):
    """BindSubDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ConstantParameter(AbstractModel):
    """Constant parameters

    """

    def __init__(self):
        """
        :param Name: Constant parameter name. This parameter takes effect only when `ServiceType` is `HTTP`.
        :type Name: str
        :param Desc: Constant parameter description. This parameter takes effect only when `ServiceType` is `HTTP`.
        :type Desc: str
        :param Position: Constant parameter location. This parameter takes effect only when `ServiceType` is `HTTP`.
        :type Position: str
        :param DefaultValue: Constant parameter default value. This parameter takes effect only when `ServiceType` is `HTTP`.
        :type DefaultValue: str
        """
        self.Name = None
        self.Desc = None
        self.Position = None
        self.DefaultValue = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Position = params.get("Position")
        self.DefaultValue = params.get("DefaultValue")


class CreateApiKeyRequest(AbstractModel):
    """CreateApiKey request structure.

    """

    def __init__(self):
        """
        :param SecretName: Custom key name.
        :type SecretName: str
        :param AccessKeyType: Key type. Valid values: auto, manual (custom key). Default value: auto.
        :type AccessKeyType: str
        :param AccessKeyId: Custom key ID, which is required when `AccessKeyType` is `manual`. It can contain 5 to 50 letters, digits, and underscores.
        :type AccessKeyId: str
        :param AccessKeySecret: Custom key, which is required when `AccessKeyType` is `manual`. It can contain 10 to 50 letters, digits, and underscores.
        :type AccessKeySecret: str
        """
        self.SecretName = None
        self.AccessKeyType = None
        self.AccessKeyId = None
        self.AccessKeySecret = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.AccessKeyType = params.get("AccessKeyType")
        self.AccessKeyId = params.get("AccessKeyId")
        self.AccessKeySecret = params.get("AccessKeySecret")


class CreateApiKeyResponse(AbstractModel):
    """CreateApiKey response structure.

    """

    def __init__(self):
        """
        :param Result: New key details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiKey()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateApiRequest(AbstractModel):
    """CreateApi request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of API's service.
        :type ServiceId: str
        :param ServiceType: API backend service type. Valid values: HTTP, MOCK, TSF, CLB, SCF, WEBSOCKET, TARGET (in beta test).
        :type ServiceType: str
        :param ServiceTimeout: API backend service timeout period in seconds.
        :type ServiceTimeout: int
        :param Protocol: API frontend request type, such as HTTP, HTTPS, or HTTP and HTTPS.
        :type Protocol: str
        :param RequestConfig: Request frontend configuration.
        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.ApiRequestConfig`
        :param ApiName: Custom API name.
        :type ApiName: str
        :param ApiDesc: Custom API description.
        :type ApiDesc: str
        :param ApiType: API type. Valid values: NORMAL (general API), TSF (microservice API). Default value: NORMAL.
        :type ApiType: str
        :param AuthType: API authentication type. Valid values: SECRET (key pair authentication), NONE (no authentication), OAUTH. Default value: NONE.
        :type AuthType: str
        :param EnableCORS: Whether to enable CORS.
        :type EnableCORS: bool
        :param ConstantParameters: Constant parameters.
        :type ConstantParameters: list of ConstantParameter
        :param RequestParameters: Frontend request parameters.
        :type RequestParameters: list of RequestParameter
        :param ApiBusinessType: This field takes effect when `AuthType` is `OAUTH`. NORMAL: business API. OAUTH: authorization API.
        :type ApiBusinessType: str
        :param ServiceMockReturnMessage: Returned information of API backend mocking. This parameter is required when `ServiceType` is `Mock`.
        :type ServiceMockReturnMessage: str
        :param MicroServices: List of microservices bound to API.
        :type MicroServices: list of MicroServiceReq
        :param ServiceTsfLoadBalanceConf: Microservice load balancing configuration.
        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`
        :param ServiceTsfHealthCheckConf: Microservice health check configuration.
        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param TargetServices: `target` type backend resource information (in beta test).
        :type TargetServices: list of TargetServicesReq
        :param TargetServicesLoadBalanceConf: `target` type load balancing configuration (in beta test).
        :type TargetServicesLoadBalanceConf: int
        :param TargetServicesHealthCheckConf: `target` health check configuration (in beta test).
        :type TargetServicesHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param ServiceScfFunctionName: SCF function name. This parameter takes effect when the backend type is `SCF`.
        :type ServiceScfFunctionName: str
        :param ServiceWebsocketRegisterFunctionName: SCF WebSocket registration function. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionName: str
        :param ServiceWebsocketCleanupFunctionName: SCF WebSocket cleanup function. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionName: str
        :param ServiceWebsocketTransportFunctionName: SCF WebSocket transfer function. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionName: str
        :param ServiceScfFunctionNamespace: SCF function namespace. This parameter takes effect when the backend type is `SCF`.
        :type ServiceScfFunctionNamespace: str
        :param ServiceScfFunctionQualifier: SCF function version. This parameter takes effect when the backend type is `SCF`.
        :type ServiceScfFunctionQualifier: str
        :param ServiceWebsocketRegisterFunctionNamespace: SCF WebSocket registration function namespace. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionNamespace: str
        :param ServiceWebsocketRegisterFunctionQualifier: SCF WebSocket transfer function version. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionQualifier: str
        :param ServiceWebsocketTransportFunctionNamespace: SCF WebSocket transfer function namespace. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionNamespace: str
        :param ServiceWebsocketTransportFunctionQualifier: SCF WebSocket transfer function version. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionQualifier: str
        :param ServiceWebsocketCleanupFunctionNamespace: SCF WebSocket cleanup function namespace. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionNamespace: str
        :param ServiceWebsocketCleanupFunctionQualifier: SCF WebSocket cleanup function version. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionQualifier: str
        :param ServiceScfIsIntegratedResponse: Whether to enable response integration. This parameter takes effect when the backend type is `SCF`.
        :type ServiceScfIsIntegratedResponse: bool
        :param IsDebugAfterCharge: Billing after debugging starts (reserved for marketplace).
        :type IsDebugAfterCharge: bool
        :param IsDeleteResponseErrorCodes: Whether to delete the custom response configuration error codes. If the value is left empty or `False`, the error codes will not be deleted. If the value is `True`, all custom response configuration error codes of the API will be deleted.
        :type IsDeleteResponseErrorCodes: bool
        :param ResponseType: Return type.
        :type ResponseType: str
        :param ResponseSuccessExample: Successful response sample of custom response configuration.
        :type ResponseSuccessExample: str
        :param ResponseFailExample: Response failure sample of custom response configuration.
        :type ResponseFailExample: str
        :param ServiceConfig: API backend service configuration.
        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`
        :param AuthRelationApiId: Unique ID of associated authorization API. This parameter takes effect only when `AuthType` is `OAUTH` and `ApiBusinessType` is `NORMAL`. It is the unique ID of the OAuth 2.0 authorization API bound to the business API.
        :type AuthRelationApiId: str
        :param ServiceParameters: API backend service parameters.
        :type ServiceParameters: list of ServiceParameter
        :param OauthConfig: OAuth configuration. This parameter takes effect when `AuthType` is `OAUTH`.
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param ResponseErrorCodes: Custom error code configuration.
        :type ResponseErrorCodes: list of ResponseErrorCodeReq
        :param TargetNamespaceId: TSF Serverless namespace ID (in beta test).
        :type TargetNamespaceId: str
        :param UserType: User type.
        :type UserType: str
        """
        self.ServiceId = None
        self.ServiceType = None
        self.ServiceTimeout = None
        self.Protocol = None
        self.RequestConfig = None
        self.ApiName = None
        self.ApiDesc = None
        self.ApiType = None
        self.AuthType = None
        self.EnableCORS = None
        self.ConstantParameters = None
        self.RequestParameters = None
        self.ApiBusinessType = None
        self.ServiceMockReturnMessage = None
        self.MicroServices = None
        self.ServiceTsfLoadBalanceConf = None
        self.ServiceTsfHealthCheckConf = None
        self.TargetServices = None
        self.TargetServicesLoadBalanceConf = None
        self.TargetServicesHealthCheckConf = None
        self.ServiceScfFunctionName = None
        self.ServiceWebsocketRegisterFunctionName = None
        self.ServiceWebsocketCleanupFunctionName = None
        self.ServiceWebsocketTransportFunctionName = None
        self.ServiceScfFunctionNamespace = None
        self.ServiceScfFunctionQualifier = None
        self.ServiceWebsocketRegisterFunctionNamespace = None
        self.ServiceWebsocketRegisterFunctionQualifier = None
        self.ServiceWebsocketTransportFunctionNamespace = None
        self.ServiceWebsocketTransportFunctionQualifier = None
        self.ServiceWebsocketCleanupFunctionNamespace = None
        self.ServiceWebsocketCleanupFunctionQualifier = None
        self.ServiceScfIsIntegratedResponse = None
        self.IsDebugAfterCharge = None
        self.IsDeleteResponseErrorCodes = None
        self.ResponseType = None
        self.ResponseSuccessExample = None
        self.ResponseFailExample = None
        self.ServiceConfig = None
        self.AuthRelationApiId = None
        self.ServiceParameters = None
        self.OauthConfig = None
        self.ResponseErrorCodes = None
        self.TargetNamespaceId = None
        self.UserType = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceType = params.get("ServiceType")
        self.ServiceTimeout = params.get("ServiceTimeout")
        self.Protocol = params.get("Protocol")
        if params.get("RequestConfig") is not None:
            self.RequestConfig = ApiRequestConfig()
            self.RequestConfig._deserialize(params.get("RequestConfig"))
        self.ApiName = params.get("ApiName")
        self.ApiDesc = params.get("ApiDesc")
        self.ApiType = params.get("ApiType")
        self.AuthType = params.get("AuthType")
        self.EnableCORS = params.get("EnableCORS")
        if params.get("ConstantParameters") is not None:
            self.ConstantParameters = []
            for item in params.get("ConstantParameters"):
                obj = ConstantParameter()
                obj._deserialize(item)
                self.ConstantParameters.append(obj)
        if params.get("RequestParameters") is not None:
            self.RequestParameters = []
            for item in params.get("RequestParameters"):
                obj = RequestParameter()
                obj._deserialize(item)
                self.RequestParameters.append(obj)
        self.ApiBusinessType = params.get("ApiBusinessType")
        self.ServiceMockReturnMessage = params.get("ServiceMockReturnMessage")
        if params.get("MicroServices") is not None:
            self.MicroServices = []
            for item in params.get("MicroServices"):
                obj = MicroServiceReq()
                obj._deserialize(item)
                self.MicroServices.append(obj)
        if params.get("ServiceTsfLoadBalanceConf") is not None:
            self.ServiceTsfLoadBalanceConf = TsfLoadBalanceConfResp()
            self.ServiceTsfLoadBalanceConf._deserialize(params.get("ServiceTsfLoadBalanceConf"))
        if params.get("ServiceTsfHealthCheckConf") is not None:
            self.ServiceTsfHealthCheckConf = HealthCheckConf()
            self.ServiceTsfHealthCheckConf._deserialize(params.get("ServiceTsfHealthCheckConf"))
        if params.get("TargetServices") is not None:
            self.TargetServices = []
            for item in params.get("TargetServices"):
                obj = TargetServicesReq()
                obj._deserialize(item)
                self.TargetServices.append(obj)
        self.TargetServicesLoadBalanceConf = params.get("TargetServicesLoadBalanceConf")
        if params.get("TargetServicesHealthCheckConf") is not None:
            self.TargetServicesHealthCheckConf = HealthCheckConf()
            self.TargetServicesHealthCheckConf._deserialize(params.get("TargetServicesHealthCheckConf"))
        self.ServiceScfFunctionName = params.get("ServiceScfFunctionName")
        self.ServiceWebsocketRegisterFunctionName = params.get("ServiceWebsocketRegisterFunctionName")
        self.ServiceWebsocketCleanupFunctionName = params.get("ServiceWebsocketCleanupFunctionName")
        self.ServiceWebsocketTransportFunctionName = params.get("ServiceWebsocketTransportFunctionName")
        self.ServiceScfFunctionNamespace = params.get("ServiceScfFunctionNamespace")
        self.ServiceScfFunctionQualifier = params.get("ServiceScfFunctionQualifier")
        self.ServiceWebsocketRegisterFunctionNamespace = params.get("ServiceWebsocketRegisterFunctionNamespace")
        self.ServiceWebsocketRegisterFunctionQualifier = params.get("ServiceWebsocketRegisterFunctionQualifier")
        self.ServiceWebsocketTransportFunctionNamespace = params.get("ServiceWebsocketTransportFunctionNamespace")
        self.ServiceWebsocketTransportFunctionQualifier = params.get("ServiceWebsocketTransportFunctionQualifier")
        self.ServiceWebsocketCleanupFunctionNamespace = params.get("ServiceWebsocketCleanupFunctionNamespace")
        self.ServiceWebsocketCleanupFunctionQualifier = params.get("ServiceWebsocketCleanupFunctionQualifier")
        self.ServiceScfIsIntegratedResponse = params.get("ServiceScfIsIntegratedResponse")
        self.IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        self.IsDeleteResponseErrorCodes = params.get("IsDeleteResponseErrorCodes")
        self.ResponseType = params.get("ResponseType")
        self.ResponseSuccessExample = params.get("ResponseSuccessExample")
        self.ResponseFailExample = params.get("ResponseFailExample")
        if params.get("ServiceConfig") is not None:
            self.ServiceConfig = ServiceConfig()
            self.ServiceConfig._deserialize(params.get("ServiceConfig"))
        self.AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("ServiceParameters") is not None:
            self.ServiceParameters = []
            for item in params.get("ServiceParameters"):
                obj = ServiceParameter()
                obj._deserialize(item)
                self.ServiceParameters.append(obj)
        if params.get("OauthConfig") is not None:
            self.OauthConfig = OauthConfig()
            self.OauthConfig._deserialize(params.get("OauthConfig"))
        if params.get("ResponseErrorCodes") is not None:
            self.ResponseErrorCodes = []
            for item in params.get("ResponseErrorCodes"):
                obj = ResponseErrorCodeReq()
                obj._deserialize(item)
                self.ResponseErrorCodes.append(obj)
        self.TargetNamespaceId = params.get("TargetNamespaceId")
        self.UserType = params.get("UserType")


class CreateApiResponse(AbstractModel):
    """CreateApi response structure.

    """

    def __init__(self):
        """
        :param Result: API information
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.CreateApiRsp`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateApiRsp()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateApiRsp(AbstractModel):
    """Returned parameters for API creation

    """

    def __init__(self):
        """
        :param ApiId: API ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiId: str
        :param Path: path
Note: this field may return null, indicating that no valid values can be obtained.
        :type Path: str
        :param Method: method
Note: this field may return null, indicating that no valid values can be obtained.
        :type Method: str
        :param CreatedTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        """
        self.ApiId = None
        self.Path = None
        self.Method = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.CreatedTime = params.get("CreatedTime")


class CreateIPStrategyRequest(AbstractModel):
    """CreateIPStrategy request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param StrategyName: Custom policy name.
        :type StrategyName: str
        :param StrategyType: Policy type. Valid values: WHITE (whitelist), BLACK (blacklist).
        :type StrategyType: str
        :param StrategyData: Policy details.
        :type StrategyData: str
        """
        self.ServiceId = None
        self.StrategyName = None
        self.StrategyType = None
        self.StrategyData = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyName = params.get("StrategyName")
        self.StrategyType = params.get("StrategyType")
        self.StrategyData = params.get("StrategyData")


class CreateIPStrategyResponse(AbstractModel):
    """CreateIPStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: New IP policy details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategy`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = IPStrategy()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateServiceRequest(AbstractModel):
    """CreateService request structure.

    """

    def __init__(self):
        """
        :param ServiceName: Custom service name. If this parameter is left empty, the system will automatically generate a unique name.
        :type ServiceName: str
        :param Protocol: Service frontend request type, such as `http`, `https`, and `http&https`.
        :type Protocol: str
        :param ServiceDesc: Custom service description.
        :type ServiceDesc: str
        :param ExclusiveSetName: Self-deployed cluster name, which is used to specify the self-deployed cluster where the service is to be created.
        :type ExclusiveSetName: str
        :param NetTypes: Network type list, which is used to specify the supported network types. `INNER` indicates access over private network, and `OUTER` indicates access over public network. The default value is `OUTER`.
        :type NetTypes: list of str
        :param IpVersion: IP version number. Valid values: IPv4 (default value), IPv6
        :type IpVersion: str
        :param SetServerName: Cluster name, which is reserved and used by the `tsf serverless` type.
        :type SetServerName: str
        :param AppIdType: User type, which is reserved and can be used by `serverless` users.
        :type AppIdType: str
        """
        self.ServiceName = None
        self.Protocol = None
        self.ServiceDesc = None
        self.ExclusiveSetName = None
        self.NetTypes = None
        self.IpVersion = None
        self.SetServerName = None
        self.AppIdType = None


    def _deserialize(self, params):
        self.ServiceName = params.get("ServiceName")
        self.Protocol = params.get("Protocol")
        self.ServiceDesc = params.get("ServiceDesc")
        self.ExclusiveSetName = params.get("ExclusiveSetName")
        self.NetTypes = params.get("NetTypes")
        self.IpVersion = params.get("IpVersion")
        self.SetServerName = params.get("SetServerName")
        self.AppIdType = params.get("AppIdType")


class CreateServiceResponse(AbstractModel):
    """CreateService response structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param ServiceName: Custom service name.
        :type ServiceName: str
        :param ServiceDesc: Custom service description.
        :type ServiceDesc: str
        :param OuterSubDomain: Default public network domain name.
        :type OuterSubDomain: str
        :param InnerSubDomain: Default domain name of VPC private network
        :type InnerSubDomain: str
        :param CreatedTime: Service creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
        :type CreatedTime: str
        :param NetTypes: Network type list. `INNER` indicates access over private network, and `OUTER` indicates access over public network.
        :type NetTypes: list of str
        :param IpVersion: IP version number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpVersion: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ServiceId = None
        self.ServiceName = None
        self.ServiceDesc = None
        self.OuterSubDomain = None
        self.InnerSubDomain = None
        self.CreatedTime = None
        self.NetTypes = None
        self.IpVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceName = params.get("ServiceName")
        self.ServiceDesc = params.get("ServiceDesc")
        self.OuterSubDomain = params.get("OuterSubDomain")
        self.InnerSubDomain = params.get("InnerSubDomain")
        self.CreatedTime = params.get("CreatedTime")
        self.NetTypes = params.get("NetTypes")
        self.IpVersion = params.get("IpVersion")
        self.RequestId = params.get("RequestId")


class CreateUsagePlanRequest(AbstractModel):
    """CreateUsagePlan request structure.

    """

    def __init__(self):
        """
        :param UsagePlanName: Custom usage plan name.
        :type UsagePlanName: str
        :param UsagePlanDesc: Custom usage plan description.
        :type UsagePlanDesc: str
        :param MaxRequestNum: Total number of requests allowed. Valid values: -1, [1,99999999]. The default value is `-1`, which indicates no limit.
        :type MaxRequestNum: int
        :param MaxRequestNumPreSec: Limit of requests per second. Valid values: -1, [1,2000]. The default value is `-1`, which indicates no limit.
        :type MaxRequestNumPreSec: int
        """
        self.UsagePlanName = None
        self.UsagePlanDesc = None
        self.MaxRequestNum = None
        self.MaxRequestNumPreSec = None


    def _deserialize(self, params):
        self.UsagePlanName = params.get("UsagePlanName")
        self.UsagePlanDesc = params.get("UsagePlanDesc")
        self.MaxRequestNum = params.get("MaxRequestNum")
        self.MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")


class CreateUsagePlanResponse(AbstractModel):
    """CreateUsagePlan response structure.

    """

    def __init__(self):
        """
        :param Result: Usage plan details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UsagePlanInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteApiKeyRequest(AbstractModel):
    """DeleteApiKey request structure.

    """

    def __init__(self):
        """
        :param AccessKeyId: ID of the key to be deleted.
        :type AccessKeyId: str
        """
        self.AccessKeyId = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")


class DeleteApiKeyResponse(AbstractModel):
    """DeleteApiKey response structure.

    """

    def __init__(self):
        """
        :param Result: Whether deletion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteApiRequest(AbstractModel):
    """DeleteApi request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of API's service.
        :type ServiceId: str
        :param ApiId: Unique API ID.
        :type ApiId: str
        """
        self.ServiceId = None
        self.ApiId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")


class DeleteApiResponse(AbstractModel):
    """DeleteApi response structure.

    """

    def __init__(self):
        """
        :param Result: Whether deletion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteIPStrategyRequest(AbstractModel):
    """DeleteIPStrategy request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of the service of the IP policy to be deleted.
        :type ServiceId: str
        :param StrategyId: Unique ID of the IP policy to be deleted.
        :type StrategyId: str
        """
        self.ServiceId = None
        self.StrategyId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyId = params.get("StrategyId")


class DeleteIPStrategyResponse(AbstractModel):
    """DeleteIPStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: Whether deletion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteServiceRequest(AbstractModel):
    """DeleteService request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of the service to be deleted.
        :type ServiceId: str
        """
        self.ServiceId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")


class DeleteServiceResponse(AbstractModel):
    """DeleteService response structure.

    """

    def __init__(self):
        """
        :param Result: Whether deletion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteServiceSubDomainMappingRequest(AbstractModel):
    """DeleteServiceSubDomainMapping request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param SubDomain: Custom domain name bound to service.
        :type SubDomain: str
        :param Environment: Name of the environment whose mapping is to be deleted. Valid values: test (testing environment), prepub (pre-publish environment), release (release environment).
        :type Environment: str
        """
        self.ServiceId = None
        self.SubDomain = None
        self.Environment = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.SubDomain = params.get("SubDomain")
        self.Environment = params.get("Environment")


class DeleteServiceSubDomainMappingResponse(AbstractModel):
    """DeleteServiceSubDomainMapping response structure.

    """

    def __init__(self):
        """
        :param Result: Whether the path mapping of the custom domain name is successfully deleted.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteUsagePlanRequest(AbstractModel):
    """DeleteUsagePlan request structure.

    """

    def __init__(self):
        """
        :param UsagePlanId: Unique ID of the usage plan to be deleted.
        :type UsagePlanId: str
        """
        self.UsagePlanId = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")


class DeleteUsagePlanResponse(AbstractModel):
    """DeleteUsagePlan response structure.

    """

    def __init__(self):
        """
        :param Result: Whether deletion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DemoteServiceUsagePlanRequest(AbstractModel):
    """DemoteServiceUsagePlan request structure.

    """

    def __init__(self):
        """
        :param UsagePlanId: Usage plan ID.
        :type UsagePlanId: str
        :param ServiceId: Unique ID of the service to be demoted.
        :type ServiceId: str
        :param Environment: Environment name.
        :type Environment: str
        """
        self.UsagePlanId = None
        self.ServiceId = None
        self.Environment = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.ServiceId = params.get("ServiceId")
        self.Environment = params.get("Environment")


class DemoteServiceUsagePlanResponse(AbstractModel):
    """DemoteServiceUsagePlan response structure.

    """

    def __init__(self):
        """
        :param Result: Whether demotion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DesApisStatus(AbstractModel):
    """API status details

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param ApiId: Unique API ID.
        :type ApiId: str
        :param ApiDesc: Custom API description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiDesc: str
        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param ApiName: API name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiName: str
        :param VpcId: VPC ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcId: int
        :param UniqVpcId: Unique VPC ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UniqVpcId: str
        :param ApiType: API type. Valid values (general API), TSF (microservice API).
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiType: str
        :param Protocol: API protocol.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param IsDebugAfterCharge: Whether to enable debugging on purchase (reserved for the marketplace)
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDebugAfterCharge: bool
        :param AuthType: API authentication type. Valid values: SECRET (key pair authentication), NONE (no authentication), OAUTH.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthType: str
        :param ApiBusinessType: OAuth API type. This parameter takes effect when `AuthType` is `OAUTH`. Valid values: NORMAL (business API), OAUTH (authorization API).
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiBusinessType: str
        :param AuthRelationApiId: Unique ID of associated authorization API. This parameter takes effect only when `AuthType` is `OAUTH` and `ApiBusinessType` is `NORMAL`. It is the unique ID of the OAuth 2.0 authorization API bound to the business API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthRelationApiId: str
        :param OauthConfig: OAuth configuration information. This parameter takes effect when `AuthType` is `OAUTH`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param RelationBuniessApiIds: List of business APIs associated with authorization API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RelationBuniessApiIds: list of str
        :param Tags: Information of tags associated with API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of str
        :param Path: API path, such as `/path`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Path: str
        :param Method: API request method, such as `GET`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Method: str
        """
        self.ServiceId = None
        self.ApiId = None
        self.ApiDesc = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ApiName = None
        self.VpcId = None
        self.UniqVpcId = None
        self.ApiType = None
        self.Protocol = None
        self.IsDebugAfterCharge = None
        self.AuthType = None
        self.ApiBusinessType = None
        self.AuthRelationApiId = None
        self.OauthConfig = None
        self.RelationBuniessApiIds = None
        self.Tags = None
        self.Path = None
        self.Method = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        self.ApiDesc = params.get("ApiDesc")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ApiName = params.get("ApiName")
        self.VpcId = params.get("VpcId")
        self.UniqVpcId = params.get("UniqVpcId")
        self.ApiType = params.get("ApiType")
        self.Protocol = params.get("Protocol")
        self.IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        self.AuthType = params.get("AuthType")
        self.ApiBusinessType = params.get("ApiBusinessType")
        self.AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("OauthConfig") is not None:
            self.OauthConfig = OauthConfig()
            self.OauthConfig._deserialize(params.get("OauthConfig"))
        self.RelationBuniessApiIds = params.get("RelationBuniessApiIds")
        self.Tags = params.get("Tags")
        self.Path = params.get("Path")
        self.Method = params.get("Method")


class DescribeApiEnvironmentStrategyRequest(AbstractModel):
    """DescribeApiEnvironmentStrategy request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of the service of API.
        :type ServiceId: str
        :param EnvironmentNames: Environment list.
        :type EnvironmentNames: list of str
        :param ApiId: Unique API ID.
        :type ApiId: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.ServiceId = None
        self.EnvironmentNames = None
        self.ApiId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentNames = params.get("EnvironmentNames")
        self.ApiId = params.get("ApiId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeApiEnvironmentStrategyResponse(AbstractModel):
    """DescribeApiEnvironmentStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: Details of policies bound to API
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiEnvironmentStrategyStataus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiEnvironmentStrategyStataus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiKeyRequest(AbstractModel):
    """DescribeApiKey request structure.

    """

    def __init__(self):
        """
        :param AccessKeyId: API key ID.
        :type AccessKeyId: str
        """
        self.AccessKeyId = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")


class DescribeApiKeyResponse(AbstractModel):
    """DescribeApiKey response structure.

    """

    def __init__(self):
        """
        :param Result: Key details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiKey()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiRequest(AbstractModel):
    """DescribeApi request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of API's service.
        :type ServiceId: str
        :param ApiId: Unique API ID.
        :type ApiId: str
        """
        self.ServiceId = None
        self.ApiId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")


class DescribeApiResponse(AbstractModel):
    """DescribeApi response structure.

    """

    def __init__(self):
        """
        :param Result: API details.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiUsagePlanRequest(AbstractModel):
    """DescribeApiUsagePlan request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeApiUsagePlanResponse(AbstractModel):
    """DescribeApiUsagePlan response structure.

    """

    def __init__(self):
        """
        :param Result: List of usage plans bound to API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiUsagePlanSet`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiUsagePlanSet()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeLogSearchRequest(AbstractModel):
    """DescribeLogSearch request structure.

    """

    def __init__(self):
        """
        :param StartTime: Log start time
        :type StartTime: str
        :param EndTime: Log end time
        :type EndTime: str
        :param ServiceId: Service ID
        :type ServiceId: str
        :param Filters: Exact search by `apiid` or `reqid`
        :type Filters: list of Filter
        :param Limit: Number of logs returned at a time. Up to 100 logs can be returned at a time
        :type Limit: int
        :param ConText: Subsequent content can be obtained based on the `ConText` returned last time. Up to 10,000 data entries can be obtained
        :type ConText: str
        :param Sort: Log sorting by time in ascending order (asc) or descending order (desc). The default value is `desc`
        :type Sort: str
        :param Query: Fuzzy search of logs by keyword
        :type Query: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ServiceId = None
        self.Filters = None
        self.Limit = None
        self.ConText = None
        self.Sort = None
        self.Query = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ServiceId = params.get("ServiceId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.ConText = params.get("ConText")
        self.Sort = params.get("Sort")
        self.Query = params.get("Query")


class DescribeLogSearchResponse(AbstractModel):
    """DescribeLogSearch response structure.

    """

    def __init__(self):
        """
        :param ConText: Cursor for getting more search results. If the value is `""`, there will be no subsequent results
        :type ConText: str
        :param LogSet: The returned result contains zero or multiple logs, which are in the following format:
'[$app_id][$env_name][$service_id][$http_host][$api_id][$uri][$scheme][rsp_st:$status][ups_st:$upstream_status]'
'[cip:$remote_addr][uip:$upstream_addr][vip:$server_addr][rsp_len:$bytes_sent][req_len:$request_length]'
'[req_t:$request_time][ups_rsp_t:$upstream_response_time][ups_conn_t:$upstream_connect_time][ups_head_t:$upstream_header_time]’
'[err_msg:$err_msg][tcp_rtt:$tcpinfo_rtt][$pid][$time_local][req_id:$request_id]';

Note:
app_id: user ID.
env_name: environment name.
service_id: service ID.
http_host: domain name.
api_id: API ID.
uri: request path.
scheme: HTTP/HTTPS protocol.
rsp_st: request response status code.
ups_st: backend business server response status code (if the request is passed through to the backend, this variable will not be empty. If the request is blocked in API Gateway, this variable will be `-`).
cip: client IP.
uip: backend business service (upstream) IP.
vip: VIP requested to be accessed.
rsp_len: response length.
req_len: request length.
req_t: total request response time.
ups_rsp_t: total backend response time (time between connection establishment by API Gateway and backend response reception).
ups_conn_t: time when the backend business server is successfully connected.
ups_head_t: time when the backend response head arrives.
err_msg: error message.
tcp_rtt: client TCP connection information. RTT (Round Trip Time) consists of three parts: link propagation delay, end system processing delay, queuing and processing delay in router cache.
req_id: request ID.
        :type LogSet: list of str
        :param TotalCount: Number of logs returned for a search (`TotalCount <= Limit`)
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ConText = None
        self.LogSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ConText = params.get("ConText")
        self.LogSet = params.get("LogSet")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeServiceEnvironmentListRequest(AbstractModel):
    """DescribeServiceEnvironmentList request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeServiceEnvironmentListResponse(AbstractModel):
    """DescribeServiceEnvironmentList response structure.

    """

    def __init__(self):
        """
        :param Result: Details of environments bound to service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceEnvironmentSet`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServiceEnvironmentSet()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServiceEnvironmentReleaseHistoryRequest(AbstractModel):
    """DescribeServiceEnvironmentReleaseHistory request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        :param EnvironmentName: Environment name.
        :type EnvironmentName: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.ServiceId = None
        self.EnvironmentName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeServiceEnvironmentReleaseHistoryResponse(AbstractModel):
    """DescribeServiceEnvironmentReleaseHistory response structure.

    """

    def __init__(self):
        """
        :param Result: Service release history.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceReleaseHistory`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServiceReleaseHistory()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServiceEnvironmentStrategyRequest(AbstractModel):
    """DescribeServiceEnvironmentStrategy request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeServiceEnvironmentStrategyResponse(AbstractModel):
    """DescribeServiceEnvironmentStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: Throttling policy list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceEnvironmentStrategyStatus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServiceEnvironmentStrategyStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServiceReleaseVersionRequest(AbstractModel):
    """DescribeServiceReleaseVersion request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeServiceReleaseVersionResponse(AbstractModel):
    """DescribeServiceReleaseVersion response structure.

    """

    def __init__(self):
        """
        :param Result: Service release version list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceReleaseVersion`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServiceReleaseVersion()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServiceRequest(AbstractModel):
    """DescribeService request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        """
        self.ServiceId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")


class DescribeServiceResponse(AbstractModel):
    """DescribeService response structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param AvailableEnvironments: Service environment list.
        :type AvailableEnvironments: list of str
        :param ServiceName: Service name.
        :type ServiceName: str
        :param ServiceDesc: Service description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceDesc: str
        :param Protocol: Protocols supported by service. Valid values: http, https, http&https.
        :type Protocol: str
        :param CreatedTime: Service creation time.
        :type CreatedTime: str
        :param ModifiedTime: Service modification time.
        :type ModifiedTime: str
        :param ExclusiveSetName: Self-deployed cluster name.
        :type ExclusiveSetName: str
        :param NetTypes: Network type list. `INNER` indicates access over private network, and `OUTER` indicates access over public network.
        :type NetTypes: list of str
        :param InternalSubDomain: Private network access subdomain name.
        :type InternalSubDomain: str
        :param OuterSubDomain: Public network access subdomain name.
        :type OuterSubDomain: str
        :param InnerHttpPort: Port number for HTTP access over private network.
        :type InnerHttpPort: int
        :param InnerHttpsPort: Port number for HTTPS access over private network.
        :type InnerHttpsPort: int
        :param ApiTotalCount: Total number of APIs.
        :type ApiTotalCount: int
        :param ApiIdStatusSet: API list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiIdStatusSet: list of ApiIdStatus
        :param UsagePlanTotalCount: Total number of usage plans.
        :type UsagePlanTotalCount: int
        :param UsagePlanList: Usage plan array.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanList: list of UsagePlan
        :param IpVersion: IP version.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpVersion: str
        :param UserType: Service user type.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserType: str
        :param SetId: Reserved field.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SetId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ServiceId = None
        self.AvailableEnvironments = None
        self.ServiceName = None
        self.ServiceDesc = None
        self.Protocol = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ExclusiveSetName = None
        self.NetTypes = None
        self.InternalSubDomain = None
        self.OuterSubDomain = None
        self.InnerHttpPort = None
        self.InnerHttpsPort = None
        self.ApiTotalCount = None
        self.ApiIdStatusSet = None
        self.UsagePlanTotalCount = None
        self.UsagePlanList = None
        self.IpVersion = None
        self.UserType = None
        self.SetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.AvailableEnvironments = params.get("AvailableEnvironments")
        self.ServiceName = params.get("ServiceName")
        self.ServiceDesc = params.get("ServiceDesc")
        self.Protocol = params.get("Protocol")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ExclusiveSetName = params.get("ExclusiveSetName")
        self.NetTypes = params.get("NetTypes")
        self.InternalSubDomain = params.get("InternalSubDomain")
        self.OuterSubDomain = params.get("OuterSubDomain")
        self.InnerHttpPort = params.get("InnerHttpPort")
        self.InnerHttpsPort = params.get("InnerHttpsPort")
        self.ApiTotalCount = params.get("ApiTotalCount")
        if params.get("ApiIdStatusSet") is not None:
            self.ApiIdStatusSet = []
            for item in params.get("ApiIdStatusSet"):
                obj = ApiIdStatus()
                obj._deserialize(item)
                self.ApiIdStatusSet.append(obj)
        self.UsagePlanTotalCount = params.get("UsagePlanTotalCount")
        if params.get("UsagePlanList") is not None:
            self.UsagePlanList = []
            for item in params.get("UsagePlanList"):
                obj = UsagePlan()
                obj._deserialize(item)
                self.UsagePlanList.append(obj)
        self.IpVersion = params.get("IpVersion")
        self.UserType = params.get("UserType")
        self.SetId = params.get("SetId")
        self.RequestId = params.get("RequestId")


class DescribeServiceSubDomainMappingsRequest(AbstractModel):
    """DescribeServiceSubDomainMappings request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param SubDomain: Custom domain name bound to service.
        :type SubDomain: str
        """
        self.ServiceId = None
        self.SubDomain = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.SubDomain = params.get("SubDomain")


class DescribeServiceSubDomainMappingsResponse(AbstractModel):
    """DescribeServiceSubDomainMappings response structure.

    """

    def __init__(self):
        """
        :param Result: Custom path mapping list.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceSubDomainMappings`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServiceSubDomainMappings()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServiceSubDomainsRequest(AbstractModel):
    """DescribeServiceSubDomains request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeServiceSubDomainsResponse(AbstractModel):
    """DescribeServiceSubDomains response structure.

    """

    def __init__(self):
        """
        :param Result: Custom service domain names.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DomainSets`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = DomainSets()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServiceUsagePlanRequest(AbstractModel):
    """DescribeServiceUsagePlan request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeServiceUsagePlanResponse(AbstractModel):
    """DescribeServiceUsagePlan response structure.

    """

    def __init__(self):
        """
        :param Result: List of usage plans bound to service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceUsagePlanSet`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServiceUsagePlanSet()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUsagePlanEnvironmentsRequest(AbstractModel):
    """DescribeUsagePlanEnvironments request structure.

    """

    def __init__(self):
        """
        :param UsagePlanId: Unique ID of the usage plan to be queried.
        :type UsagePlanId: str
        :param BindType: Binding type. Valid values: API, SERVICE (default value).
        :type BindType: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.UsagePlanId = None
        self.BindType = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.BindType = params.get("BindType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeUsagePlanEnvironmentsResponse(AbstractModel):
    """DescribeUsagePlanEnvironments response structure.

    """

    def __init__(self):
        """
        :param Result: Usage plan binding details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanEnvironmentStatus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UsagePlanEnvironmentStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUsagePlanRequest(AbstractModel):
    """DescribeUsagePlan request structure.

    """

    def __init__(self):
        """
        :param UsagePlanId: Unique ID of the usage plan to be queried.
        :type UsagePlanId: str
        """
        self.UsagePlanId = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")


class DescribeUsagePlanResponse(AbstractModel):
    """DescribeUsagePlan response structure.

    """

    def __init__(self):
        """
        :param Result: Usage plan details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UsagePlanInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUsagePlanSecretIdsRequest(AbstractModel):
    """DescribeUsagePlanSecretIds request structure.

    """

    def __init__(self):
        """
        :param UsagePlanId: Unique ID of bound usage plan.
        :type UsagePlanId: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.UsagePlanId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeUsagePlanSecretIdsResponse(AbstractModel):
    """DescribeUsagePlanSecretIds response structure.

    """

    def __init__(self):
        """
        :param Result: List of keys bound to usage plan.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanBindSecretStatus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UsagePlanBindSecretStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DisableApiKeyRequest(AbstractModel):
    """DisableApiKey request structure.

    """

    def __init__(self):
        """
        :param AccessKeyId: ID of the key to be disabled.
        :type AccessKeyId: str
        """
        self.AccessKeyId = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")


class DisableApiKeyResponse(AbstractModel):
    """DisableApiKey response structure.

    """

    def __init__(self):
        """
        :param Result: Whether the key is successfully disabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DocumentSDK(AbstractModel):
    """API documentation download

    """

    def __init__(self):
        """
        :param DocumentURL: Download link of generated file. Generated documents are stored in COS.
        :type DocumentURL: str
        :param SdkURL: Download link of generated SDK file. Generated SDKs are stored in COS.
        :type SdkURL: str
        """
        self.DocumentURL = None
        self.SdkURL = None


    def _deserialize(self, params):
        self.DocumentURL = params.get("DocumentURL")
        self.SdkURL = params.get("SdkURL")


class DomainSets(AbstractModel):
    """Custom service domain name information

    """

    def __init__(self):
        """
        :param TotalCount: Number of custom domain names under service
        :type TotalCount: int
        :param DomainSet: Custom service domain name list.
        :type DomainSet: list of DomainSetList
        """
        self.TotalCount = None
        self.DomainSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DomainSet") is not None:
            self.DomainSet = []
            for item in params.get("DomainSet"):
                obj = DomainSetList()
                obj._deserialize(item)
                self.DomainSet.append(obj)


class EnableApiKeyRequest(AbstractModel):
    """EnableApiKey request structure.

    """

    def __init__(self):
        """
        :param AccessKeyId: ID of the key to be enabled.
        :type AccessKeyId: str
        """
        self.AccessKeyId = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")


class EnableApiKeyResponse(AbstractModel):
    """EnableApiKey response structure.

    """

    def __init__(self):
        """
        :param Result: Whether the key is successfully enabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class Environment(AbstractModel):
    """Environment

    """

    def __init__(self):
        """
        :param EnvironmentName: Environment name.
        :type EnvironmentName: str
        :param Url: Access path.
        :type Url: str
        :param Status: Release status. 1: released. 0: not released.
        :type Status: int
        :param VersionName: Running version.
        :type VersionName: str
        """
        self.EnvironmentName = None
        self.Url = None
        self.Status = None
        self.VersionName = None


    def _deserialize(self, params):
        self.EnvironmentName = params.get("EnvironmentName")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.VersionName = params.get("VersionName")


class EnvironmentStrategy(AbstractModel):
    """Environment throttling

    """

    def __init__(self):
        """
        :param EnvironmentName: Environment name
        :type EnvironmentName: str
        :param Quota: Throttling value
        :type Quota: int
        """
        self.EnvironmentName = None
        self.Quota = None


    def _deserialize(self, params):
        self.EnvironmentName = params.get("EnvironmentName")
        self.Quota = params.get("Quota")


class ErrorCodes(AbstractModel):
    """ErrorCodes

    """

    def __init__(self):
        """
        :param Code: Custom response configuration error code.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Code: int
        :param Msg: Custom response configuration error message.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param Desc: Remarks of the custom response configuration error code.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Desc: str
        :param ConvertedCode: Custom error code conversion.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ConvertedCode: int
        :param NeedConvert: Whether to enable error code conversion.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NeedConvert: bool
        """
        self.Code = None
        self.Msg = None
        self.Desc = None
        self.ConvertedCode = None
        self.NeedConvert = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Desc = params.get("Desc")
        self.ConvertedCode = params.get("ConvertedCode")
        self.NeedConvert = params.get("NeedConvert")


class Filter(AbstractModel):
    """>Key-value pair filters for conditional filtering queries, such as filter ID, name, and status
    > * If there are multiple `Filter`, the relationship among them is logical `AND`.
    > * If there are multiple `Values` in the same `Filter`, the relationship among them is logical `OR`.
    >

    """

    def __init__(self):
        """
        :param Name: Field to be filtered.
        :type Name: str
        :param Values: Filter value of field.
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class GenerateApiDocumentRequest(AbstractModel):
    """GenerateApiDocument request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID of the document to be created.
        :type ServiceId: str
        :param GenEnvironment: Environment of the service for which the SDK is to be created.
        :type GenEnvironment: str
        :param GenLanguage: Programming language of the SDK to be created. Currently, only Python and JavaScript are supported.
        :type GenLanguage: str
        """
        self.ServiceId = None
        self.GenEnvironment = None
        self.GenLanguage = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.GenEnvironment = params.get("GenEnvironment")
        self.GenLanguage = params.get("GenLanguage")


class GenerateApiDocumentResponse(AbstractModel):
    """GenerateApiDocument response structure.

    """

    def __init__(self):
        """
        :param Result: API documentation and SDK link.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DocumentSDK`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = DocumentSDK()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class HealthCheckConf(AbstractModel):
    """Health check configuration, including `TsfHealthCheckConf` and `TargetServicesHealthCheckConf`

    """

    def __init__(self):
        """
        :param IsHealthCheck: Whether to enable health check.
        :type IsHealthCheck: bool
        :param RequestVolumeThreshold: Health check threshold.
        :type RequestVolumeThreshold: int
        :param SleepWindowInMilliseconds: Window size.
        :type SleepWindowInMilliseconds: int
        :param ErrorThresholdPercentage: Threshold percentage.
        :type ErrorThresholdPercentage: int
        """
        self.IsHealthCheck = None
        self.RequestVolumeThreshold = None
        self.SleepWindowInMilliseconds = None
        self.ErrorThresholdPercentage = None


    def _deserialize(self, params):
        self.IsHealthCheck = params.get("IsHealthCheck")
        self.RequestVolumeThreshold = params.get("RequestVolumeThreshold")
        self.SleepWindowInMilliseconds = params.get("SleepWindowInMilliseconds")
        self.ErrorThresholdPercentage = params.get("ErrorThresholdPercentage")


class IPStrategy(AbstractModel):
    """IP policy

    """

    def __init__(self):
        """
        :param StrategyId: Unique policy ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StrategyId: str
        :param StrategyName: Custom policy name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StrategyName: str
        :param StrategyType: Policy type. Valid values: WHITE (whitelist), BLACK (blacklist).
Note: this field may return null, indicating that no valid values can be obtained.
        :type StrategyType: str
        :param StrategyData: IP list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StrategyData: str
        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param ModifiedTime: Modification time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param ServiceId: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceId: str
        :param BindApiTotalCount: Number of APIs bound to policy.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BindApiTotalCount: int
        :param BindApis: Bound API details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BindApis: list of DesApisStatus
        """
        self.StrategyId = None
        self.StrategyName = None
        self.StrategyType = None
        self.StrategyData = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ServiceId = None
        self.BindApiTotalCount = None
        self.BindApis = None


    def _deserialize(self, params):
        self.StrategyId = params.get("StrategyId")
        self.StrategyName = params.get("StrategyName")
        self.StrategyType = params.get("StrategyType")
        self.StrategyData = params.get("StrategyData")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ServiceId = params.get("ServiceId")
        self.BindApiTotalCount = params.get("BindApiTotalCount")
        if params.get("BindApis") is not None:
            self.BindApis = []
            for item in params.get("BindApis"):
                obj = DesApisStatus()
                obj._deserialize(item)
                self.BindApis.append(obj)


class MicroService(AbstractModel):
    """MicroService

    """

    def __init__(self):
        """
        :param ClusterId: Microservice cluster ID.
        :type ClusterId: str
        :param NamespaceId: Microservice namespace ID.
        :type NamespaceId: str
        :param MicroServiceName: Microservice name.
        :type MicroServiceName: str
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.MicroServiceName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.MicroServiceName = params.get("MicroServiceName")


class MicroServiceReq(AbstractModel):
    """TSF type input parameters

    """

    def __init__(self):
        """
        :param ClusterId: Microservice cluster.
        :type ClusterId: str
        :param NamespaceId: Microservice namespace.
        :type NamespaceId: str
        :param MicroServiceName: Microservice name.
        :type MicroServiceName: str
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.MicroServiceName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.MicroServiceName = params.get("MicroServiceName")


class ModifyApiEnvironmentStrategyRequest(AbstractModel):
    """ModifyApiEnvironmentStrategy request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param Strategy: Throttling value.
        :type Strategy: int
        :param EnvironmentName: Environment name.
        :type EnvironmentName: str
        :param ApiIds: API list.
        :type ApiIds: list of str
        """
        self.ServiceId = None
        self.Strategy = None
        self.EnvironmentName = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Strategy = params.get("Strategy")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ApiIds = params.get("ApiIds")


class ModifyApiEnvironmentStrategyResponse(AbstractModel):
    """ModifyApiEnvironmentStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: Whether modification succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyApiIncrementRequest(AbstractModel):
    """ModifyApiIncrement request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Service ID
        :type ServiceId: str
        :param ApiId: API ID
        :type ApiId: str
        :param BusinessType: Authorization type of the API to be modified (you can select `OAUTH`, i.e., authorization API)
        :type BusinessType: str
        :param PublicKey: Public key value to be modified of OAuth API
        :type PublicKey: str
        :param LoginRedirectUrl: OAuth API redirect address
        :type LoginRedirectUrl: str
        """
        self.ServiceId = None
        self.ApiId = None
        self.BusinessType = None
        self.PublicKey = None
        self.LoginRedirectUrl = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        self.BusinessType = params.get("BusinessType")
        self.PublicKey = params.get("PublicKey")
        self.LoginRedirectUrl = params.get("LoginRedirectUrl")


class ModifyApiIncrementResponse(AbstractModel):
    """ModifyApiIncrement response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApiRequest(AbstractModel):
    """ModifyApi request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of API's service.
        :type ServiceId: str
        :param ServiceType: API backend service type. Valid values: HTTP, MOCK, TSF, CLB, SCF, WEBSOCKET, TARGET (in beta test).
        :type ServiceType: str
        :param RequestConfig: Request frontend configuration.
        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.RequestConfig`
        :param ApiId: Unique API ID.
        :type ApiId: str
        :param ApiName: Custom API name.
        :type ApiName: str
        :param ApiDesc: Custom API description.
        :type ApiDesc: str
        :param ApiType: API type. Valid values: NORMAL (default value), TSF.
        :type ApiType: str
        :param AuthType: API authentication type. Valid values: SECRET, NONE (default), OAUTH.
        :type AuthType: str
        :param AuthRequired: Whether signature authentication is required. `True` indicates yes while `False` indicates no. This parameter is to be disused.
        :type AuthRequired: bool
        :param ServiceTimeout: API backend service timeout period in seconds.
        :type ServiceTimeout: int
        :param Protocol: API frontend request type, such as HTTP, HTTPS, or HTTP and HTTPS.
        :type Protocol: str
        :param EnableCORS: Whether to enable CORS. `True` indicates yes while `False` indicates no.
        :type EnableCORS: bool
        :param ConstantParameters: Constant parameters.
        :type ConstantParameters: list of ConstantParameter
        :param RequestParameters: Frontend request parameters.
        :type RequestParameters: list of ReqParameter
        :param ApiBusinessType: This field takes effect when `AuthType` is `OAUTH`. NORMAL: business API. OAUTH: authorization API.
        :type ApiBusinessType: str
        :param ServiceMockReturnMessage: Returned information of API backend mocking. This parameter is required when `ServiceType` is `Mock`.
        :type ServiceMockReturnMessage: str
        :param MicroServices: List of microservices bound to API.
        :type MicroServices: list of MicroServiceReq
        :param ServiceTsfLoadBalanceConf: Microservice load balancing configuration.
        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`
        :param ServiceTsfHealthCheckConf: Microservice health check configuration.
        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param TargetServicesLoadBalanceConf: `target` type load balancing configuration (in beta test).
        :type TargetServicesLoadBalanceConf: int
        :param TargetServicesHealthCheckConf: `target` health check configuration (in beta test).
        :type TargetServicesHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param ServiceScfFunctionName: SCF function name. This parameter takes effect when the backend type is `SCF`.
        :type ServiceScfFunctionName: str
        :param ServiceWebsocketRegisterFunctionName: SCF WebSocket registration function. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionName: str
        :param ServiceWebsocketCleanupFunctionName: SCF WebSocket cleanup function. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionName: str
        :param ServiceWebsocketTransportFunctionName: SCF WebSocket transfer function. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionName: str
        :param ServiceScfFunctionNamespace: SCF function namespace. This parameter takes effect when the backend type is `SCF`.
        :type ServiceScfFunctionNamespace: str
        :param ServiceScfFunctionQualifier: SCF function version. This parameter takes effect when the backend type is `SCF`.
        :type ServiceScfFunctionQualifier: str
        :param ServiceWebsocketRegisterFunctionNamespace: SCF WebSocket registration function namespace. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionNamespace: str
        :param ServiceWebsocketRegisterFunctionQualifier: SCF WebSocket transfer function version. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionQualifier: str
        :param ServiceWebsocketTransportFunctionNamespace: SCF WebSocket transfer function namespace. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionNamespace: str
        :param ServiceWebsocketTransportFunctionQualifier: SCF WebSocket transfer function version. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionQualifier: str
        :param ServiceWebsocketCleanupFunctionNamespace: SCF WebSocket cleanup function namespace. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionNamespace: str
        :param ServiceWebsocketCleanupFunctionQualifier: SCF WebSocket cleanup function version. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionQualifier: str
        :param ServiceScfIsIntegratedResponse: Whether to enable response integration. This parameter takes effect when the backend type is `SCF`.
        :type ServiceScfIsIntegratedResponse: bool
        :param IsDebugAfterCharge: Billing after debugging starts (reserved for marketplace).
        :type IsDebugAfterCharge: bool
        :param TagSpecifications: Tag.
        :type TagSpecifications: :class:`tencentcloud.apigateway.v20180808.models.Tag`
        :param IsDeleteResponseErrorCodes: Whether to delete the custom response configuration error codes. If the value is left empty or `False`, the error codes will not be deleted. If the value is `True`, all custom response configuration error codes of the API will be deleted.
        :type IsDeleteResponseErrorCodes: bool
        :param ResponseType: Return type.
        :type ResponseType: str
        :param ResponseSuccessExample: Successful response sample of custom response configuration.
        :type ResponseSuccessExample: str
        :param ResponseFailExample: Response failure sample of custom response configuration.
        :type ResponseFailExample: str
        :param ServiceConfig: API backend service configuration.
        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`
        :param AuthRelationApiId: Unique ID of associated authorization API. This parameter takes effect only when `AuthType` is `OAUTH` and `ApiBusinessType` is `NORMAL`. It is the unique ID of the OAuth 2.0 authorization API bound to the business API.
        :type AuthRelationApiId: str
        :param ServiceParameters: API backend service parameters.
        :type ServiceParameters: list of ServiceParameter
        :param OauthConfig: OAuth configuration. This parameter takes effect when `AuthType` is `OAUTH`.
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param ResponseErrorCodes: Custom error code configuration.
        :type ResponseErrorCodes: list of ResponseErrorCodeReq
        """
        self.ServiceId = None
        self.ServiceType = None
        self.RequestConfig = None
        self.ApiId = None
        self.ApiName = None
        self.ApiDesc = None
        self.ApiType = None
        self.AuthType = None
        self.AuthRequired = None
        self.ServiceTimeout = None
        self.Protocol = None
        self.EnableCORS = None
        self.ConstantParameters = None
        self.RequestParameters = None
        self.ApiBusinessType = None
        self.ServiceMockReturnMessage = None
        self.MicroServices = None
        self.ServiceTsfLoadBalanceConf = None
        self.ServiceTsfHealthCheckConf = None
        self.TargetServicesLoadBalanceConf = None
        self.TargetServicesHealthCheckConf = None
        self.ServiceScfFunctionName = None
        self.ServiceWebsocketRegisterFunctionName = None
        self.ServiceWebsocketCleanupFunctionName = None
        self.ServiceWebsocketTransportFunctionName = None
        self.ServiceScfFunctionNamespace = None
        self.ServiceScfFunctionQualifier = None
        self.ServiceWebsocketRegisterFunctionNamespace = None
        self.ServiceWebsocketRegisterFunctionQualifier = None
        self.ServiceWebsocketTransportFunctionNamespace = None
        self.ServiceWebsocketTransportFunctionQualifier = None
        self.ServiceWebsocketCleanupFunctionNamespace = None
        self.ServiceWebsocketCleanupFunctionQualifier = None
        self.ServiceScfIsIntegratedResponse = None
        self.IsDebugAfterCharge = None
        self.TagSpecifications = None
        self.IsDeleteResponseErrorCodes = None
        self.ResponseType = None
        self.ResponseSuccessExample = None
        self.ResponseFailExample = None
        self.ServiceConfig = None
        self.AuthRelationApiId = None
        self.ServiceParameters = None
        self.OauthConfig = None
        self.ResponseErrorCodes = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceType = params.get("ServiceType")
        if params.get("RequestConfig") is not None:
            self.RequestConfig = RequestConfig()
            self.RequestConfig._deserialize(params.get("RequestConfig"))
        self.ApiId = params.get("ApiId")
        self.ApiName = params.get("ApiName")
        self.ApiDesc = params.get("ApiDesc")
        self.ApiType = params.get("ApiType")
        self.AuthType = params.get("AuthType")
        self.AuthRequired = params.get("AuthRequired")
        self.ServiceTimeout = params.get("ServiceTimeout")
        self.Protocol = params.get("Protocol")
        self.EnableCORS = params.get("EnableCORS")
        if params.get("ConstantParameters") is not None:
            self.ConstantParameters = []
            for item in params.get("ConstantParameters"):
                obj = ConstantParameter()
                obj._deserialize(item)
                self.ConstantParameters.append(obj)
        if params.get("RequestParameters") is not None:
            self.RequestParameters = []
            for item in params.get("RequestParameters"):
                obj = ReqParameter()
                obj._deserialize(item)
                self.RequestParameters.append(obj)
        self.ApiBusinessType = params.get("ApiBusinessType")
        self.ServiceMockReturnMessage = params.get("ServiceMockReturnMessage")
        if params.get("MicroServices") is not None:
            self.MicroServices = []
            for item in params.get("MicroServices"):
                obj = MicroServiceReq()
                obj._deserialize(item)
                self.MicroServices.append(obj)
        if params.get("ServiceTsfLoadBalanceConf") is not None:
            self.ServiceTsfLoadBalanceConf = TsfLoadBalanceConfResp()
            self.ServiceTsfLoadBalanceConf._deserialize(params.get("ServiceTsfLoadBalanceConf"))
        if params.get("ServiceTsfHealthCheckConf") is not None:
            self.ServiceTsfHealthCheckConf = HealthCheckConf()
            self.ServiceTsfHealthCheckConf._deserialize(params.get("ServiceTsfHealthCheckConf"))
        self.TargetServicesLoadBalanceConf = params.get("TargetServicesLoadBalanceConf")
        if params.get("TargetServicesHealthCheckConf") is not None:
            self.TargetServicesHealthCheckConf = HealthCheckConf()
            self.TargetServicesHealthCheckConf._deserialize(params.get("TargetServicesHealthCheckConf"))
        self.ServiceScfFunctionName = params.get("ServiceScfFunctionName")
        self.ServiceWebsocketRegisterFunctionName = params.get("ServiceWebsocketRegisterFunctionName")
        self.ServiceWebsocketCleanupFunctionName = params.get("ServiceWebsocketCleanupFunctionName")
        self.ServiceWebsocketTransportFunctionName = params.get("ServiceWebsocketTransportFunctionName")
        self.ServiceScfFunctionNamespace = params.get("ServiceScfFunctionNamespace")
        self.ServiceScfFunctionQualifier = params.get("ServiceScfFunctionQualifier")
        self.ServiceWebsocketRegisterFunctionNamespace = params.get("ServiceWebsocketRegisterFunctionNamespace")
        self.ServiceWebsocketRegisterFunctionQualifier = params.get("ServiceWebsocketRegisterFunctionQualifier")
        self.ServiceWebsocketTransportFunctionNamespace = params.get("ServiceWebsocketTransportFunctionNamespace")
        self.ServiceWebsocketTransportFunctionQualifier = params.get("ServiceWebsocketTransportFunctionQualifier")
        self.ServiceWebsocketCleanupFunctionNamespace = params.get("ServiceWebsocketCleanupFunctionNamespace")
        self.ServiceWebsocketCleanupFunctionQualifier = params.get("ServiceWebsocketCleanupFunctionQualifier")
        self.ServiceScfIsIntegratedResponse = params.get("ServiceScfIsIntegratedResponse")
        self.IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        if params.get("TagSpecifications") is not None:
            self.TagSpecifications = Tag()
            self.TagSpecifications._deserialize(params.get("TagSpecifications"))
        self.IsDeleteResponseErrorCodes = params.get("IsDeleteResponseErrorCodes")
        self.ResponseType = params.get("ResponseType")
        self.ResponseSuccessExample = params.get("ResponseSuccessExample")
        self.ResponseFailExample = params.get("ResponseFailExample")
        if params.get("ServiceConfig") is not None:
            self.ServiceConfig = ServiceConfig()
            self.ServiceConfig._deserialize(params.get("ServiceConfig"))
        self.AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("ServiceParameters") is not None:
            self.ServiceParameters = []
            for item in params.get("ServiceParameters"):
                obj = ServiceParameter()
                obj._deserialize(item)
                self.ServiceParameters.append(obj)
        if params.get("OauthConfig") is not None:
            self.OauthConfig = OauthConfig()
            self.OauthConfig._deserialize(params.get("OauthConfig"))
        if params.get("ResponseErrorCodes") is not None:
            self.ResponseErrorCodes = []
            for item in params.get("ResponseErrorCodes"):
                obj = ResponseErrorCodeReq()
                obj._deserialize(item)
                self.ResponseErrorCodes.append(obj)


class ModifyApiResponse(AbstractModel):
    """ModifyApi response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIPStrategyRequest(AbstractModel):
    """ModifyIPStrategy request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of the service of the policy to be modified.
        :type ServiceId: str
        :param StrategyId: Unique ID of the policy to be modified.
        :type StrategyId: str
        :param StrategyData: Details of the policy to be modified.
        :type StrategyData: str
        """
        self.ServiceId = None
        self.StrategyId = None
        self.StrategyData = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyId = params.get("StrategyId")
        self.StrategyData = params.get("StrategyData")


class ModifyIPStrategyResponse(AbstractModel):
    """ModifyIPStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: Whether modification succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyServiceEnvironmentStrategyRequest(AbstractModel):
    """ModifyServiceEnvironmentStrategy request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param Strategy: Throttling value.
        :type Strategy: int
        :param EnvironmentNames: Environment list.
        :type EnvironmentNames: list of str
        """
        self.ServiceId = None
        self.Strategy = None
        self.EnvironmentNames = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Strategy = params.get("Strategy")
        self.EnvironmentNames = params.get("EnvironmentNames")


class ModifyServiceEnvironmentStrategyResponse(AbstractModel):
    """ModifyServiceEnvironmentStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: Whether modification succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyServiceRequest(AbstractModel):
    """ModifyService request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of the service to be modified.
        :type ServiceId: str
        :param ServiceName: Modified service name.
        :type ServiceName: str
        :param ServiceDesc: Modified service description.
        :type ServiceDesc: str
        :param Protocol: Modified service frontend request type, such as `http`, `https`, and `http&https`.
        :type Protocol: str
        :param NetTypes: Network type list, which is used to specify the supported network types. `INNER` indicates access over private network, and `OUTER` indicates access over public network. The default value is `OUTER`.
        :type NetTypes: list of str
        """
        self.ServiceId = None
        self.ServiceName = None
        self.ServiceDesc = None
        self.Protocol = None
        self.NetTypes = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceName = params.get("ServiceName")
        self.ServiceDesc = params.get("ServiceDesc")
        self.Protocol = params.get("Protocol")
        self.NetTypes = params.get("NetTypes")


class ModifyServiceResponse(AbstractModel):
    """ModifyService response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubDomainRequest(AbstractModel):
    """ModifySubDomain request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param SubDomain: Custom domain name for which the path mapping is to be modified.
        :type SubDomain: str
        :param IsDefaultMapping: Whether to change to the default path mapping. true: use the default path mapping. false: use the custom path mapping.
        :type IsDefaultMapping: bool
        :param CertificateId: Certificate ID, which is required when the HTTPS protocol is included.
        :type CertificateId: str
        :param Protocol: Modified custom domain name protocol type. Valid values: http, https, http&https.
        :type Protocol: str
        :param PathMappingSet: Modified path mapping list.
        :type PathMappingSet: list of PathMapping
        :param NetType: Network type. Valid values: INNER, OUTER.
        :type NetType: str
        """
        self.ServiceId = None
        self.SubDomain = None
        self.IsDefaultMapping = None
        self.CertificateId = None
        self.Protocol = None
        self.PathMappingSet = None
        self.NetType = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.SubDomain = params.get("SubDomain")
        self.IsDefaultMapping = params.get("IsDefaultMapping")
        self.CertificateId = params.get("CertificateId")
        self.Protocol = params.get("Protocol")
        if params.get("PathMappingSet") is not None:
            self.PathMappingSet = []
            for item in params.get("PathMappingSet"):
                obj = PathMapping()
                obj._deserialize(item)
                self.PathMappingSet.append(obj)
        self.NetType = params.get("NetType")


class ModifySubDomainResponse(AbstractModel):
    """ModifySubDomain response structure.

    """

    def __init__(self):
        """
        :param Result: Whether the custom domain name is successfully modified.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyUsagePlanRequest(AbstractModel):
    """ModifyUsagePlan request structure.

    """

    def __init__(self):
        """
        :param UsagePlanId: Unique usage plan ID.
        :type UsagePlanId: str
        :param UsagePlanName: Modified custom usage plan name.
        :type UsagePlanName: str
        :param UsagePlanDesc: Modified custom usage plan description.
        :type UsagePlanDesc: str
        :param MaxRequestNum: Total number of requests allowed. Valid values: -1, [1,99999999]. The default value is `-1`, which indicates no limit.
        :type MaxRequestNum: int
        :param MaxRequestNumPreSec: Limit of requests per second. Valid values: -1, [1,2000]. The default value is `-1`, which indicates no limit.
        :type MaxRequestNumPreSec: int
        """
        self.UsagePlanId = None
        self.UsagePlanName = None
        self.UsagePlanDesc = None
        self.MaxRequestNum = None
        self.MaxRequestNumPreSec = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.UsagePlanName = params.get("UsagePlanName")
        self.UsagePlanDesc = params.get("UsagePlanDesc")
        self.MaxRequestNum = params.get("MaxRequestNum")
        self.MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")


class ModifyUsagePlanResponse(AbstractModel):
    """ModifyUsagePlan response structure.

    """

    def __init__(self):
        """
        :param Result: Usage plan details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UsagePlanInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class OauthConfig(AbstractModel):
    """OAuth authorization configuration information

    """

    def __init__(self):
        """
        :param PublicKey: Public key for user token verification.
        :type PublicKey: str
        :param TokenLocation: Token delivery location.
        :type TokenLocation: str
        :param LoginRedirectUrl: Redirect address, which is used to guide user logins.
        :type LoginRedirectUrl: str
        """
        self.PublicKey = None
        self.TokenLocation = None
        self.LoginRedirectUrl = None


    def _deserialize(self, params):
        self.PublicKey = params.get("PublicKey")
        self.TokenLocation = params.get("TokenLocation")
        self.LoginRedirectUrl = params.get("LoginRedirectUrl")


class PathMapping(AbstractModel):
    """Custom domain name path mapping.

    """

    def __init__(self):
        """
        :param Path: Path.
        :type Path: str
        :param Environment: Release environment. Valid values: test, prepub, release.
        :type Environment: str
        """
        self.Path = None
        self.Environment = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Environment = params.get("Environment")


class ReleaseService(AbstractModel):
    """Service publishing returned result

    """

    def __init__(self):
        """
        :param ReleaseDesc: Release remarks.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReleaseDesc: str
        :param ReleaseVersion: Release version ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReleaseVersion: str
        """
        self.ReleaseDesc = None
        self.ReleaseVersion = None


    def _deserialize(self, params):
        self.ReleaseDesc = params.get("ReleaseDesc")
        self.ReleaseVersion = params.get("ReleaseVersion")


class ReleaseServiceRequest(AbstractModel):
    """ReleaseService request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of the service to be published.
        :type ServiceId: str
        :param EnvironmentName: Name of the environment to be published. Valid values: test (testing environment), prepub (pre-publish environment), release (release environment).
        :type EnvironmentName: str
        :param ReleaseDesc: Release description.
        :type ReleaseDesc: str
        :param ApiIds: `apiId` list, which is reserved. Full API release is used by default.
        :type ApiIds: list of str
        """
        self.ServiceId = None
        self.EnvironmentName = None
        self.ReleaseDesc = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ReleaseDesc = params.get("ReleaseDesc")
        self.ApiIds = params.get("ApiIds")


class ReleaseServiceResponse(AbstractModel):
    """ReleaseService response structure.

    """

    def __init__(self):
        """
        :param Result: Release information.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ReleaseService`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ReleaseService()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class RequestConfig(AbstractModel):
    """Frontend path configuration

    """

    def __init__(self):
        """
        :param Path: API path, such as `/path`.
        :type Path: str
        :param Method: API request method, such as `GET`.
        :type Method: str
        """
        self.Path = None
        self.Method = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Method = params.get("Method")


class RequestParameter(AbstractModel):
    """Request parameter

    """

    def __init__(self):
        """
        :param Name: Request parameter name
        :type Name: str
        :param Desc: Description
        :type Desc: str
        :param Position: Parameter location
        :type Position: str
        :param Type: Parameter type
        :type Type: str
        :param DefaultValue: Default value
        :type DefaultValue: str
        :param Required: Required
        :type Required: bool
        """
        self.Name = None
        self.Desc = None
        self.Position = None
        self.Type = None
        self.DefaultValue = None
        self.Required = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Position = params.get("Position")
        self.Type = params.get("Type")
        self.DefaultValue = params.get("DefaultValue")
        self.Required = params.get("Required")


class ResponseErrorCodeReq(AbstractModel):
    """Error code input parameters

    """

    def __init__(self):
        """
        :param Code: Custom response configuration error code.
        :type Code: int
        :param Msg: Custom response configuration error message.
        :type Msg: str
        :param Desc: Remarks of the custom response configuration error code.
        :type Desc: str
        :param ConvertedCode: Custom error code conversion.
        :type ConvertedCode: int
        :param NeedConvert: Whether to enable error code conversion.
        :type NeedConvert: bool
        """
        self.Code = None
        self.Msg = None
        self.Desc = None
        self.ConvertedCode = None
        self.NeedConvert = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Desc = params.get("Desc")
        self.ConvertedCode = params.get("ConvertedCode")
        self.NeedConvert = params.get("NeedConvert")


class ServiceConfig(AbstractModel):
    """ServiceConfig

    """

    def __init__(self):
        """
        :param Product: Backend type. This parameter takes effect when VPC is enabled. Currently, only `clb` is supported.
        :type Product: str
        :param UniqVpcId: Unique VPC ID.
        :type UniqVpcId: str
        :param Url: API backend service URL. This parameter is required when `ServiceType` is `HTTP`.
        :type Url: str
        :param Path: API backend service path, such as `/path`. If `ServiceType` is `HTTP`, this parameter will be required. The frontend and backend paths can be different.
        :type Path: str
        :param Method: API backend service request method, such as `GET`. If `ServiceType` is `HTTP`, this parameter will be required. The frontend and backend methods can be different
        :type Method: str
        """
        self.Product = None
        self.UniqVpcId = None
        self.Url = None
        self.Path = None
        self.Method = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.UniqVpcId = params.get("UniqVpcId")
        self.Url = params.get("Url")
        self.Path = params.get("Path")
        self.Method = params.get("Method")


class ServiceEnvironmentSet(AbstractModel):
    """Details of environments bound to service

    """

    def __init__(self):
        """
        :param TotalCount: Total number of environments bound to service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param EnvironmentList: List of environments bound to service
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnvironmentList: list of Environment
        """
        self.TotalCount = None
        self.EnvironmentList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EnvironmentList") is not None:
            self.EnvironmentList = []
            for item in params.get("EnvironmentList"):
                obj = Environment()
                obj._deserialize(item)
                self.EnvironmentList.append(obj)


class ServiceEnvironmentStrategy(AbstractModel):
    """Service environment policy

    """

    def __init__(self):
        """
        :param EnvironmentName: Environment name.
        :type EnvironmentName: str
        :param Url: Access service environment URL.
        :type Url: str
        :param Status: Release status.
        :type Status: int
        :param VersionName: Release version ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VersionName: str
        :param Strategy: Throttling value.
        :type Strategy: int
        """
        self.EnvironmentName = None
        self.Url = None
        self.Status = None
        self.VersionName = None
        self.Strategy = None


    def _deserialize(self, params):
        self.EnvironmentName = params.get("EnvironmentName")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.VersionName = params.get("VersionName")
        self.Strategy = params.get("Strategy")


class ServiceEnvironmentStrategyStatus(AbstractModel):
    """List of policies bound to environment.

    """

    def __init__(self):
        """
        :param TotalCount: Throttling policy number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param EnvironmentList: Throttling policy list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnvironmentList: list of ServiceEnvironmentStrategy
        """
        self.TotalCount = None
        self.EnvironmentList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EnvironmentList") is not None:
            self.EnvironmentList = []
            for item in params.get("EnvironmentList"):
                obj = ServiceEnvironmentStrategy()
                obj._deserialize(item)
                self.EnvironmentList.append(obj)


class ServiceParameter(AbstractModel):
    """ServiceParameter

    """

    def __init__(self):
        """
        :param Name: API backend service parameter name. This parameter takes effect only when `ServiceType` is `HTTP`. Frontend and backend parameter names can be different.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param Position: API backend service parameter position, such as `head`. This parameter takes effect only when `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Position: str
        :param RelevantRequestParameterPosition: Position of the API frontend parameter corresponding to backend service parameter, such as `head`. This parameter takes effect only when `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RelevantRequestParameterPosition: str
        :param RelevantRequestParameterName: Name of the API frontend parameter corresponding to backend service parameter. This parameter takes effect only when `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RelevantRequestParameterName: str
        :param DefaultValue: API backend service parameter default value. This parameter takes effect only when `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DefaultValue: str
        :param RelevantRequestParameterDesc: API backend service parameter remarks. This parameter takes effect only when `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RelevantRequestParameterDesc: str
        :param RelevantRequestParameterType: API backend service parameter type. This parameter takes effect only when `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RelevantRequestParameterType: str
        """
        self.Name = None
        self.Position = None
        self.RelevantRequestParameterPosition = None
        self.RelevantRequestParameterName = None
        self.DefaultValue = None
        self.RelevantRequestParameterDesc = None
        self.RelevantRequestParameterType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Position = params.get("Position")
        self.RelevantRequestParameterPosition = params.get("RelevantRequestParameterPosition")
        self.RelevantRequestParameterName = params.get("RelevantRequestParameterName")
        self.DefaultValue = params.get("DefaultValue")
        self.RelevantRequestParameterDesc = params.get("RelevantRequestParameterDesc")
        self.RelevantRequestParameterType = params.get("RelevantRequestParameterType")


class ServiceReleaseHistory(AbstractModel):
    """Service release history

    """

    def __init__(self):
        """
        :param TotalCount: Total number of release versions.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param VersionList: Historical version list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VersionList: list of ServiceReleaseHistoryInfo
        """
        self.TotalCount = None
        self.VersionList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VersionList") is not None:
            self.VersionList = []
            for item in params.get("VersionList"):
                obj = ServiceReleaseHistoryInfo()
                obj._deserialize(item)
                self.VersionList.append(obj)


class ServiceReleaseHistoryInfo(AbstractModel):
    """Service release list details

    """

    def __init__(self):
        """
        :param VersionName: Version ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VersionName: str
        :param VersionDesc: Version description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VersionDesc: str
        :param ReleaseTime: Version release time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReleaseTime: str
        """
        self.VersionName = None
        self.VersionDesc = None
        self.ReleaseTime = None


    def _deserialize(self, params):
        self.VersionName = params.get("VersionName")
        self.VersionDesc = params.get("VersionDesc")
        self.ReleaseTime = params.get("ReleaseTime")


class ServiceReleaseVersion(AbstractModel):
    """Service release version

    """

    def __init__(self):
        """
        :param TotalCount: Total number of release versions.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param VersionList: Release version list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VersionList: list of ServiceReleaseHistoryInfo
        """
        self.TotalCount = None
        self.VersionList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VersionList") is not None:
            self.VersionList = []
            for item in params.get("VersionList"):
                obj = ServiceReleaseHistoryInfo()
                obj._deserialize(item)
                self.VersionList.append(obj)


class ServiceSubDomainMappings(AbstractModel):
    """Custom service domain name path mapping

    """

    def __init__(self):
        """
        :param IsDefaultMapping: Whether to use the default path mapping. true: use the default path mapping. false: use the custom path mapping (`PathMappingSet` is required).
        :type IsDefaultMapping: bool
        :param PathMappingSet: Custom path mapping list.
        :type PathMappingSet: list of PathMapping
        """
        self.IsDefaultMapping = None
        self.PathMappingSet = None


    def _deserialize(self, params):
        self.IsDefaultMapping = params.get("IsDefaultMapping")
        if params.get("PathMappingSet") is not None:
            self.PathMappingSet = []
            for item in params.get("PathMappingSet"):
                obj = PathMapping()
                obj._deserialize(item)
                self.PathMappingSet.append(obj)


class ServiceUsagePlanSet(AbstractModel):
    """List of usage plans bound to service

    """

    def __init__(self):
        """
        :param TotalCount: Total number of usage plans bound to service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param ServiceUsagePlanList: List of usage plans bound to service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceUsagePlanList: list of ApiUsagePlan
        """
        self.TotalCount = None
        self.ServiceUsagePlanList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ServiceUsagePlanList") is not None:
            self.ServiceUsagePlanList = []
            for item in params.get("ServiceUsagePlanList"):
                obj = ApiUsagePlan()
                obj._deserialize(item)
                self.ServiceUsagePlanList.append(obj)


class Tag(AbstractModel):
    """API tag

    """

    def __init__(self):
        """
        :param Key: Tag key.
        :type Key: str
        :param Value: Tag value.
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class TargetServicesReq(AbstractModel):
    """TSF Serverless input parameters

    """

    def __init__(self):
        """
        :param VmIp: VM IP
        :type VmIp: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param VmPort: VM Port
        :type VmPort: int
        :param HostIp: IP of the host where the CVM instance resides
        :type HostIp: str
        :param DockerIp: Docker IP
        :type DockerIp: str
        """
        self.VmIp = None
        self.VpcId = None
        self.VmPort = None
        self.HostIp = None
        self.DockerIp = None


    def _deserialize(self, params):
        self.VmIp = params.get("VmIp")
        self.VpcId = params.get("VpcId")
        self.VmPort = params.get("VmPort")
        self.HostIp = params.get("HostIp")
        self.DockerIp = params.get("DockerIp")


class TsfLoadBalanceConfResp(AbstractModel):
    """`TsfLoadBalanceConf` output parameter usage

    """

    def __init__(self):
        """
        :param IsLoadBalance: Whether to enable load balancing.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsLoadBalance: bool
        :param Method: Load balancing method.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Method: str
        :param SessionStickRequired: Whether to enable session persistence.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SessionStickRequired: bool
        :param SessionStickTimeout: Session persistence timeout period.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SessionStickTimeout: int
        """
        self.IsLoadBalance = None
        self.Method = None
        self.SessionStickRequired = None
        self.SessionStickTimeout = None


    def _deserialize(self, params):
        self.IsLoadBalance = params.get("IsLoadBalance")
        self.Method = params.get("Method")
        self.SessionStickRequired = params.get("SessionStickRequired")
        self.SessionStickTimeout = params.get("SessionStickTimeout")


class UnBindEnvironmentRequest(AbstractModel):
    """UnBindEnvironment request structure.

    """

    def __init__(self):
        """
        :param BindType: Binding type. Valid values: API, SERVICE (default value).
        :type BindType: str
        :param UsagePlanIds: List of unique IDs of the usage plans to be bound.
        :type UsagePlanIds: list of str
        :param Environment: Service environment to be unbound.
        :type Environment: str
        :param ServiceId: Unique ID of the service to be unbound.
        :type ServiceId: str
        :param ApiIds: Unique API ID array. This parameter will be required when `BindType` is `API`.
        :type ApiIds: list of str
        """
        self.BindType = None
        self.UsagePlanIds = None
        self.Environment = None
        self.ServiceId = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.BindType = params.get("BindType")
        self.UsagePlanIds = params.get("UsagePlanIds")
        self.Environment = params.get("Environment")
        self.ServiceId = params.get("ServiceId")
        self.ApiIds = params.get("ApiIds")


class UnBindEnvironmentResponse(AbstractModel):
    """UnBindEnvironment response structure.

    """

    def __init__(self):
        """
        :param Result: Whether unbinding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UnBindIPStrategyRequest(AbstractModel):
    """UnBindIPStrategy request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of the service to be unbound.
        :type ServiceId: str
        :param StrategyId: Unique ID of the IP policy to be unbound.
        :type StrategyId: str
        :param EnvironmentName: Environment to be unbound.
        :type EnvironmentName: str
        :param UnBindApiIds: List of APIs to be unbound.
        :type UnBindApiIds: list of str
        """
        self.ServiceId = None
        self.StrategyId = None
        self.EnvironmentName = None
        self.UnBindApiIds = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyId = params.get("StrategyId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.UnBindApiIds = params.get("UnBindApiIds")


class UnBindIPStrategyResponse(AbstractModel):
    """UnBindIPStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: Whether unbinding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UnBindSecretIdsRequest(AbstractModel):
    """UnBindSecretIds request structure.

    """

    def __init__(self):
        """
        :param UsagePlanId: Unique ID of the usage plan to be unbound.
        :type UsagePlanId: str
        :param AccessKeyIds: Array of IDs of the keys to be unbound.
        :type AccessKeyIds: list of str
        """
        self.UsagePlanId = None
        self.AccessKeyIds = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.AccessKeyIds = params.get("AccessKeyIds")


class UnBindSecretIdsResponse(AbstractModel):
    """UnBindSecretIds response structure.

    """

    def __init__(self):
        """
        :param Result: Whether unbinding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UnBindSubDomainRequest(AbstractModel):
    """UnBindSubDomain request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param SubDomain: Custom domain name to be unbound.
        :type SubDomain: str
        """
        self.ServiceId = None
        self.SubDomain = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.SubDomain = params.get("SubDomain")


class UnBindSubDomainResponse(AbstractModel):
    """UnBindSubDomain response structure.

    """

    def __init__(self):
        """
        :param Result: Whether the custom domain name is successfully unbound.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UnReleaseServiceRequest(AbstractModel):
    """UnReleaseService request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of the service to be deactivated.
        :type ServiceId: str
        :param EnvironmentName: Name of the environment to be deactivated. Valid values: test (testing environment), prepub (pre-publish environment), release (release environment).
        :type EnvironmentName: str
        :param ApiIds: List of APIs to be deactivated, which is a reserved field.
        :type ApiIds: list of str
        """
        self.ServiceId = None
        self.EnvironmentName = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ApiIds = params.get("ApiIds")


class UnReleaseServiceResponse(AbstractModel):
    """UnReleaseService response structure.

    """

    def __init__(self):
        """
        :param Result: Whether deactivation succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UpdateApiKeyRequest(AbstractModel):
    """UpdateApiKey request structure.

    """

    def __init__(self):
        """
        :param AccessKeyId: ID of the key to be updated.
        :type AccessKeyId: str
        :param AccessKeySecret: Key to be updated, which is required when a custom key is updated. It can contain 10 to 50 letters, digits, and underscores.
        :type AccessKeySecret: str
        """
        self.AccessKeyId = None
        self.AccessKeySecret = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        self.AccessKeySecret = params.get("AccessKeySecret")


class UpdateApiKeyResponse(AbstractModel):
    """UpdateApiKey response structure.

    """

    def __init__(self):
        """
        :param Result: Changed key details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiKey()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class UpdateServiceRequest(AbstractModel):
    """UpdateService request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of the service to be switch to.
        :type ServiceId: str
        :param EnvironmentName: Name of the environment to be switched to. Valid values: test (testing environment), prepub (pre-publish environment), release (release environment).
        :type EnvironmentName: str
        :param VersionName: Number of the version to be switched to.
        :type VersionName: str
        :param UpdateDesc: Switch description.
        :type UpdateDesc: str
        """
        self.ServiceId = None
        self.EnvironmentName = None
        self.VersionName = None
        self.UpdateDesc = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.VersionName = params.get("VersionName")
        self.UpdateDesc = params.get("UpdateDesc")


class UpdateServiceResponse(AbstractModel):
    """UpdateService response structure.

    """

    def __init__(self):
        """
        :param Result: Whether the version is successfully switched.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UsagePlan(AbstractModel):
    """`usagePlan` details

    """

    def __init__(self):
        """
        :param Environment: Environment name.
        :type Environment: str
        :param UsagePlanId: Unique usage plan ID.
        :type UsagePlanId: str
        :param UsagePlanName: Usage plan name.
        :type UsagePlanName: str
        :param UsagePlanDesc: Usage plan description.
        :type UsagePlanDesc: str
        :param MaxRequestNumPreSec: Usage plan QPS. `-1` indicates no limit.
        :type MaxRequestNumPreSec: int
        :param CreatedTime: Usage plan time.
        :type CreatedTime: str
        :param ModifiedTime: Usage plan modification time.
        :type ModifiedTime: str
        """
        self.Environment = None
        self.UsagePlanId = None
        self.UsagePlanName = None
        self.UsagePlanDesc = None
        self.MaxRequestNumPreSec = None
        self.CreatedTime = None
        self.ModifiedTime = None


    def _deserialize(self, params):
        self.Environment = params.get("Environment")
        self.UsagePlanId = params.get("UsagePlanId")
        self.UsagePlanName = params.get("UsagePlanName")
        self.UsagePlanDesc = params.get("UsagePlanDesc")
        self.MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")


class UsagePlanBindSecret(AbstractModel):
    """Key bound to usage plan

    """

    def __init__(self):
        """
        :param AccessKeyId: Key ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccessKeyId: str
        :param SecretName: Key name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecretName: str
        :param Status: Key status. 0: disabled. 1: enabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        """
        self.AccessKeyId = None
        self.SecretName = None
        self.Status = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        self.SecretName = params.get("SecretName")
        self.Status = params.get("Status")


class UsagePlanBindSecretStatus(AbstractModel):
    """List of keys bound to usage plan.

    """

    def __init__(self):
        """
        :param TotalCount: Number of keys bound to usage plan.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param AccessKeyList: List of key details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccessKeyList: list of UsagePlanBindSecret
        """
        self.TotalCount = None
        self.AccessKeyList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AccessKeyList") is not None:
            self.AccessKeyList = []
            for item in params.get("AccessKeyList"):
                obj = UsagePlanBindSecret()
                obj._deserialize(item)
                self.AccessKeyList.append(obj)


class UsagePlanEnvironment(AbstractModel):
    """Usage plan binding details

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of bound service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceId: str
        :param ApiId: Unique API ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiId: str
        :param ApiName: API name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiName: str
        :param Path: API path.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Path: str
        :param Method: API method.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Method: str
        :param Environment: Name of the bound environment.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Environment: str
        :param InUseRequestNum: Used quota.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InUseRequestNum: int
        :param MaxRequestNum: Maximum number of requests.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxRequestNum: int
        :param MaxRequestNumPreSec: Maximum requests per second.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxRequestNumPreSec: int
        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param ServiceName: Service name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceName: str
        """
        self.ServiceId = None
        self.ApiId = None
        self.ApiName = None
        self.Path = None
        self.Method = None
        self.Environment = None
        self.InUseRequestNum = None
        self.MaxRequestNum = None
        self.MaxRequestNumPreSec = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        self.ApiName = params.get("ApiName")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.Environment = params.get("Environment")
        self.InUseRequestNum = params.get("InUseRequestNum")
        self.MaxRequestNum = params.get("MaxRequestNum")
        self.MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ServiceName = params.get("ServiceName")


class UsagePlanEnvironmentStatus(AbstractModel):
    """Usage plan binding details

    """

    def __init__(self):
        """
        :param TotalCount: Number of environments of the service bound to usage plan.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param EnvironmentList: Environment status of the services bound to usage plan.
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnvironmentList: list of UsagePlanEnvironment
        """
        self.TotalCount = None
        self.EnvironmentList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EnvironmentList") is not None:
            self.EnvironmentList = []
            for item in params.get("EnvironmentList"):
                obj = UsagePlanEnvironment()
                obj._deserialize(item)
                self.EnvironmentList.append(obj)