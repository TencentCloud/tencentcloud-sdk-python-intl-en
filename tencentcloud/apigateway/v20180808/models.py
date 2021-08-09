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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class APIDoc(AbstractModel):
    """Basic information of API document

    """

    def __init__(self):
        """
        :param ApiDocId: API document ID\n        :type ApiDocId: str\n        :param ApiDocName: API document name\n        :type ApiDocName: str\n        :param ApiDocStatus: API document build status\n        :type ApiDocStatus: str\n        """
        self.ApiDocId = None
        self.ApiDocName = None
        self.ApiDocStatus = None


    def _deserialize(self, params):
        self.ApiDocId = params.get("ApiDocId")
        self.ApiDocName = params.get("ApiDocName")
        self.ApiDocStatus = params.get("ApiDocStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class APIDocInfo(AbstractModel):
    """API document details

    """

    def __init__(self):
        """
        :param ApiDocId: API document ID\n        :type ApiDocId: str\n        :param ApiDocName: API document name\n        :type ApiDocName: str\n        :param ApiDocStatus: API document build status\n        :type ApiDocStatus: str\n        :param ApiCount: Number of APIs with API documents\n        :type ApiCount: int\n        :param ViewCount: Number of views of API document\n        :type ViewCount: int\n        :param ReleaseCount: Number of releases of API document\n        :type ReleaseCount: int\n        :param ApiDocUri: API document access URI\n        :type ApiDocUri: str\n        :param SharePassword: API document password for sharing\n        :type SharePassword: str\n        :param UpdatedTime: API document update time\n        :type UpdatedTime: str\n        :param ServiceId: Service ID\n        :type ServiceId: str\n        :param Environment: Environment information\n        :type Environment: str\n        :param ApiIds: ID of the API for which to generate the API document\n        :type ApiIds: list of str\n        :param ServiceName: Service name\n        :type ServiceName: str\n        :param ApiNames: Name of the API for which to generate the API document\n        :type ApiNames: list of str\n        """
        self.ApiDocId = None
        self.ApiDocName = None
        self.ApiDocStatus = None
        self.ApiCount = None
        self.ViewCount = None
        self.ReleaseCount = None
        self.ApiDocUri = None
        self.SharePassword = None
        self.UpdatedTime = None
        self.ServiceId = None
        self.Environment = None
        self.ApiIds = None
        self.ServiceName = None
        self.ApiNames = None


    def _deserialize(self, params):
        self.ApiDocId = params.get("ApiDocId")
        self.ApiDocName = params.get("ApiDocName")
        self.ApiDocStatus = params.get("ApiDocStatus")
        self.ApiCount = params.get("ApiCount")
        self.ViewCount = params.get("ViewCount")
        self.ReleaseCount = params.get("ReleaseCount")
        self.ApiDocUri = params.get("ApiDocUri")
        self.SharePassword = params.get("SharePassword")
        self.UpdatedTime = params.get("UpdatedTime")
        self.ServiceId = params.get("ServiceId")
        self.Environment = params.get("Environment")
        self.ApiIds = params.get("ApiIds")
        self.ServiceName = params.get("ServiceName")
        self.ApiNames = params.get("ApiNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class APIDocs(AbstractModel):
    """API document list

    """

    def __init__(self):
        """
        :param TotalCount: Number of API documents\n        :type TotalCount: int\n        :param APIDocSet: Basic information of API document\n        :type APIDocSet: list of APIDoc\n        """
        self.TotalCount = None
        self.APIDocSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("APIDocSet") is not None:
            self.APIDocSet = []
            for item in params.get("APIDocSet"):
                obj = APIDoc()
                obj._deserialize(item)
                self.APIDocSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiEnvironmentStrategy(AbstractModel):
    """API environment binding policy

    """

    def __init__(self):
        """
        :param ApiId: Unique API ID.\n        :type ApiId: str\n        :param ApiName: Custom API name.\n        :type ApiName: str\n        :param Path: API path, such as `/path`.\n        :type Path: str\n        :param Method: API method, such as `GET`.\n        :type Method: str\n        :param EnvironmentStrategySet: Environment throttling information.\n        :type EnvironmentStrategySet: list of EnvironmentStrategy\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiEnvironmentStrategyStataus(AbstractModel):
    """List of policies bound to API

    """

    def __init__(self):
        """
        :param TotalCount: Number of throttling policies bound to API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param ApiEnvironmentStrategySet: List of throttling policies bound to API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiEnvironmentStrategySet: list of ApiEnvironmentStrategy\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiIdStatus(AbstractModel):
    """API status

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.\n        :type ServiceId: str\n        :param ApiId: Unique API ID.\n        :type ApiId: str\n        :param ApiDesc: API description\n        :type ApiDesc: str\n        :param Path: API path.\n        :type Path: str\n        :param Method: API method.\n        :type Method: str\n        :param CreatedTime: Service creation time.\n        :type CreatedTime: str\n        :param ModifiedTime: Service modification time.\n        :type ModifiedTime: str\n        :param ApiName: API name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiName: str\n        :param UniqVpcId: Unique VPC ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UniqVpcId: str\n        :param ApiType: API type.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiType: str\n        :param Protocol: API protocol.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Protocol: str\n        :param IsDebugAfterCharge: Whether to enable debugging after purchase.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsDebugAfterCharge: bool\n        :param AuthType: Authorization type.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AuthType: str\n        :param ApiBusinessType: API business type.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiBusinessType: str\n        :param AuthRelationApiId: Unique ID of associated authorization API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AuthRelationApiId: str\n        :param RelationBuniessApiIds: List of business APIs associated with authorization API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RelationBuniessApiIds: list of str\n        :param OauthConfig: OAuth configuration information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`\n        :param TokenLocation: Token storage position, which is an OAuth 2.0 API request.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TokenLocation: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiInfo(AbstractModel):
    """API information

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID of API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceId: str\n        :param ServiceName: Service name of API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceName: str\n        :param ServiceDesc: Service description of API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceDesc: str\n        :param ApiId: Unique API ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiId: str\n        :param ApiDesc: API description.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiDesc: str\n        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreatedTime: str\n        :param ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ModifiedTime: str\n        :param ApiName: API name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiName: str\n        :param ApiType: API type. Valid values: NORMAL (general API), TSF (microservice API).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiType: str\n        :param Protocol: API frontend request type, such as HTTP, HTTPS, or HTTP and HTTPS.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Protocol: str\n        :param AuthType: API authentication type. Valid values: SECRET (key pair authentication), NONE (no authentication), OAUTH.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AuthType: str\n        :param ApiBusinessType: OAuth API type. Valid values: NORMAL (business API), OAUTH (authorization API).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiBusinessType: str\n        :param AuthRelationApiId: Unique ID of the authorization API associated with OAuth business API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AuthRelationApiId: str\n        :param OauthConfig: OAuth configuration.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`\n        :param IsDebugAfterCharge: Whether to enable debugging after purchase (reserved field for the marketplace).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsDebugAfterCharge: bool\n        :param RequestConfig: Request frontend configuration.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.RequestConfig`\n        :param ResponseType: Return type.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ResponseType: str\n        :param ResponseSuccessExample: Sample response for successful custom response configuration.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ResponseSuccessExample: str\n        :param ResponseFailExample: Sample response for failed custom response configuration.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ResponseFailExample: str\n        :param ResponseErrorCodes: Custom error code configuration.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ResponseErrorCodes: list of ErrorCodes\n        :param RequestParameters: Frontend request parameter.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RequestParameters: list of ReqParameter\n        :param ServiceTimeout: API backend service timeout period in seconds.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceTimeout: int\n        :param ServiceType: API backend service type. Valid values: HTTP, MOCK, TSF, CLB, SCF, WEBSOCKET, TARGET (in beta test).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceType: str\n        :param ServiceConfig: API backend service configuration.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`\n        :param ServiceParameters: API backend service parameter.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceParameters: list of ServiceParameter\n        :param ConstantParameters: Constant parameter.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ConstantParameters: list of ConstantParameter\n        :param ServiceMockReturnMessage: Returned message of API backend Mock, which is required if `ServiceType` is `Mock`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceMockReturnMessage: str\n        :param ServiceScfFunctionName: SCF function name, which takes effect if the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceScfFunctionName: str\n        :param ServiceScfFunctionNamespace: SCF function namespace, which takes effect if the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceScfFunctionNamespace: str\n        :param ServiceScfFunctionQualifier: SCF function version, which takes effect if the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceScfFunctionQualifier: str\n        :param ServiceScfIsIntegratedResponse: Whether integrated response is enabled.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceScfIsIntegratedResponse: bool\n        :param ServiceWebsocketRegisterFunctionName: SCF WebSocket registration function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceWebsocketRegisterFunctionName: str\n        :param ServiceWebsocketRegisterFunctionNamespace: SCF WebSocket registration function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceWebsocketRegisterFunctionNamespace: str\n        :param ServiceWebsocketRegisterFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceWebsocketRegisterFunctionQualifier: str\n        :param ServiceWebsocketCleanupFunctionName: SCF WebSocket cleanup function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceWebsocketCleanupFunctionName: str\n        :param ServiceWebsocketCleanupFunctionNamespace: SCF WebSocket cleanup function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceWebsocketCleanupFunctionNamespace: str\n        :param ServiceWebsocketCleanupFunctionQualifier: SCF WebSocket cleanup function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceWebsocketCleanupFunctionQualifier: str\n        :param InternalDomain: WebSocket callback address.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InternalDomain: str\n        :param ServiceWebsocketTransportFunctionName: SCF WebSocket transfer function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceWebsocketTransportFunctionName: str\n        :param ServiceWebsocketTransportFunctionNamespace: SCF WebSocket transfer function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceWebsocketTransportFunctionNamespace: str\n        :param ServiceWebsocketTransportFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceWebsocketTransportFunctionQualifier: str\n        :param MicroServices: List of microservices bound to API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MicroServices: list of MicroService\n        :param MicroServicesInfo: Microservice details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MicroServicesInfo: list of int\n        :param ServiceTsfLoadBalanceConf: Load balancing configuration of microservice.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`\n        :param ServiceTsfHealthCheckConf: Health check configuration of microservice.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`\n        :param EnableCORS: Whether to enable CORS.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EnableCORS: bool\n        :param Tags: Information of tags bound to API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Tags: list of Tag\n        :param Environments: Environment information published for API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Environments: list of str\n        :param IsBase64Encoded: Whether to enable Base64 encoding. This parameter takes effect only when the backend is SCF.
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type IsBase64Encoded: bool\n        :param IsBase64Trigger: Whether to trigger Base64 encoding by header. This parameter takes effect only when the backend is SCF.
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type IsBase64Trigger: bool\n        :param Base64EncodedTriggerRules: Header trigger rules. The number of rules cannot exceed 10.
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type Base64EncodedTriggerRules: list of Base64EncodedTriggerRule\n        """
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
        self.Environments = None
        self.IsBase64Encoded = None
        self.IsBase64Trigger = None
        self.Base64EncodedTriggerRules = None


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
        self.Environments = params.get("Environments")
        self.IsBase64Encoded = params.get("IsBase64Encoded")
        self.IsBase64Trigger = params.get("IsBase64Trigger")
        if params.get("Base64EncodedTriggerRules") is not None:
            self.Base64EncodedTriggerRules = []
            for item in params.get("Base64EncodedTriggerRules"):
                obj = Base64EncodedTriggerRule()
                obj._deserialize(item)
                self.Base64EncodedTriggerRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiKey(AbstractModel):
    """Key details

    """

    def __init__(self):
        """
        :param AccessKeyId: Created API key ID.\n        :type AccessKeyId: str\n        :param AccessKeySecret: Created API key.\n        :type AccessKeySecret: str\n        :param AccessKeyType: Key type. Valid values: auto, manual.\n        :type AccessKeyType: str\n        :param SecretName: Custom key name.\n        :type SecretName: str\n        :param ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.\n        :type ModifiedTime: str\n        :param Status: Key status. 0: disabled. 1: enabled.\n        :type Status: int\n        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.\n        :type CreatedTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiKeysStatus(AbstractModel):
    """Key list

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible API keys.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param ApiKeySet: API key list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiKeySet: list of ApiKey\n        """
        self.TotalCount = None
        self.ApiKeySet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiKeySet") is not None:
            self.ApiKeySet = []
            for item in params.get("ApiKeySet"):
                obj = ApiKey()
                obj._deserialize(item)
                self.ApiKeySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiRequestConfig(AbstractModel):
    """API request configuration

    """

    def __init__(self):
        """
        :param Path: path\n        :type Path: str\n        :param Method: Method\n        :type Method: str\n        """
        self.Path = None
        self.Method = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiUsagePlan(AbstractModel):
    """Details of usage plans bound to API or service

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceId: str\n        :param ApiId: Unique API ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiId: str\n        :param ApiName: API name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiName: str\n        :param Path: API path.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Path: str\n        :param Method: API method.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Method: str\n        :param UsagePlanId: Unique usage plan ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UsagePlanId: str\n        :param UsagePlanName: Usage plan name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UsagePlanName: str\n        :param UsagePlanDesc: Usage plan description.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UsagePlanDesc: str\n        :param Environment: Service environment bound to usage plan.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Environment: str\n        :param InUseRequestNum: Used quota.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InUseRequestNum: int\n        :param MaxRequestNum: Total number of requests allowed. `-1` indicates no limit.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxRequestNum: int\n        :param MaxRequestNumPreSec: Request QPS upper limit. `-1` indicates no limit.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxRequestNumPreSec: int\n        :param CreatedTime: Usage plan creation time.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreatedTime: str\n        :param ModifiedTime: Last modified time of usage plan.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ModifiedTime: str\n        :param ServiceName: Service name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiUsagePlanSet(AbstractModel):
    """List of usage plans bound to API

    """

    def __init__(self):
        """
        :param TotalCount: Total number of usage plans bound to API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param ApiUsagePlanList: List of usage plans bound to API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiUsagePlanList: list of ApiUsagePlan\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApisStatus(AbstractModel):
    """API list status description

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible APIs.\n        :type TotalCount: int\n        :param ApiIdStatusSet: API list.\n        :type ApiIdStatusSet: list of DesApisStatus\n        """
        self.TotalCount = None
        self.ApiIdStatusSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiIdStatusSet") is not None:
            self.ApiIdStatusSet = []
            for item in params.get("ApiIdStatusSet"):
                obj = DesApisStatus()
                obj._deserialize(item)
                self.ApiIdStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Base64EncodedTriggerRule(AbstractModel):
    """Header trigger rule for Base64 encoding.

    """

    def __init__(self):
        """
        :param Name: Header for triggering encoding. Valid values are `Accept` and `Content_Type`, corresponding to the `Accept` and `Content-Type` headers in the data stream request, respectively.\n        :type Name: str\n        :param Value: Array of header values that can trigger the encoding. Each element in the array can be up to 40 characters, including digits, letters, and special characters (`.`, `+`, `*`, `-`, `/`, and `_`). 

For example, [
    "application/x-vpeg005",
    "application/xhtml+xml",
    "application/vnd.ms-project",
    "application/vnd.rn-rn_music_package"
] are valid.\n        :type Value: list of str\n        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindEnvironmentRequest(AbstractModel):
    """BindEnvironment request structure.

    """

    def __init__(self):
        """
        :param UsagePlanIds: List of unique IDs of the usage plans to be bound.\n        :type UsagePlanIds: list of str\n        :param BindType: Binding type. Valid values: API, SERVICE. Default value: SERVICE.\n        :type BindType: str\n        :param Environment: Environment to be bound.\n        :type Environment: str\n        :param ServiceId: Unique ID of the service to be bound.\n        :type ServiceId: str\n        :param ApiIds: Unique API ID array, which is required if `bindType` is `API`.\n        :type ApiIds: list of str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindEnvironmentResponse(AbstractModel):
    """BindEnvironment response structure.

    """

    def __init__(self):
        """
        :param Result: Whether binding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique service ID of the IP policy to be bound.\n        :type ServiceId: str\n        :param StrategyId: Unique ID of the IP policy to be bound.\n        :type StrategyId: str\n        :param EnvironmentName: Environment to be bound to IP policy.\n        :type EnvironmentName: str\n        :param BindApiIds: List of APIs to be bound to IP policy.\n        :type BindApiIds: list of str\n        """
        self.ServiceId = None
        self.StrategyId = None
        self.EnvironmentName = None
        self.BindApiIds = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyId = params.get("StrategyId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.BindApiIds = params.get("BindApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindIPStrategyResponse(AbstractModel):
    """BindIPStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: Whether binding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param UsagePlanId: Unique ID of the usage plan to be bound.\n        :type UsagePlanId: str\n        :param AccessKeyIds: Array of IDs of the keys to be bound.\n        :type AccessKeyIds: list of str\n        """
        self.UsagePlanId = None
        self.AccessKeyIds = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.AccessKeyIds = params.get("AccessKeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindSecretIdsResponse(AbstractModel):
    """BindSecretIds response structure.

    """

    def __init__(self):
        """
        :param Result: Whether binding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique service ID.\n        :type ServiceId: str\n        :param SubDomain: Custom domain name to be bound.\n        :type SubDomain: str\n        :param Protocol: Protocol supported by service. Valid values: http, https, http&https.\n        :type Protocol: str\n        :param NetType: Network type. Valid values: OUTER, INNER.\n        :type NetType: str\n        :param IsDefaultMapping: Whether the default path mapping is used. The default value is `true`. If the value is `false`, the custom path mapping will be used and `PathMappingSet` will be required in this case.\n        :type IsDefaultMapping: bool\n        :param NetSubDomain: Default domain name.\n        :type NetSubDomain: str\n        :param CertificateId: Unique certificate ID of the custom domain name to be bound. The certificate can be uploaded if `Protocol` is `https` or `http&https`.\n        :type CertificateId: str\n        :param PathMappingSet: Custom domain name path mapping. It can contain up to 3 `Environment` values which can be set to only `test`, `prepub`, and `release`, respectively.\n        :type PathMappingSet: list of PathMapping\n        :param IsForcedHttps: Whether to force HTTP requests to redirect to HTTPS. Default value: `false`. When this parameter is `true`, API Gateway will redirect all requests using the custom domain name over the HTTP protocol to the HTTPS protocol for forwarding.\n        :type IsForcedHttps: bool\n        """
        self.ServiceId = None
        self.SubDomain = None
        self.Protocol = None
        self.NetType = None
        self.IsDefaultMapping = None
        self.NetSubDomain = None
        self.CertificateId = None
        self.PathMappingSet = None
        self.IsForcedHttps = None


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
        self.IsForcedHttps = params.get("IsForcedHttps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindSubDomainResponse(AbstractModel):
    """BindSubDomain response structure.

    """

    def __init__(self):
        """
        :param Result: Whether binding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BuildAPIDocRequest(AbstractModel):
    """BuildAPIDoc request structure.

    """

    def __init__(self):
        """
        :param ApiDocId: API document ID\n        :type ApiDocId: str\n        """
        self.ApiDocId = None


    def _deserialize(self, params):
        self.ApiDocId = params.get("ApiDocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BuildAPIDocResponse(AbstractModel):
    """BuildAPIDoc response structure.

    """

    def __init__(self):
        """
        :param Result: Whether the operation succeeded\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ConstantParameter(AbstractModel):
    """Constant parameter

    """

    def __init__(self):
        """
        :param Name: Constant parameter name, which is used only if `ServiceType` is `HTTP`.\n        :type Name: str\n        :param Desc: Constant parameter description, which is used only if `ServiceType` is `HTTP`.\n        :type Desc: str\n        :param Position: Constant parameter position, which is used only if `ServiceType` is `HTTP`.\n        :type Position: str\n        :param DefaultValue: Default value of constant parameter, which is used only if `ServiceType` is `HTTP`.\n        :type DefaultValue: str\n        """
        self.Name = None
        self.Desc = None
        self.Position = None
        self.DefaultValue = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Position = params.get("Position")
        self.DefaultValue = params.get("DefaultValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAPIDocRequest(AbstractModel):
    """CreateAPIDoc request structure.

    """

    def __init__(self):
        """
        :param ApiDocName: API document name\n        :type ApiDocName: str\n        :param ServiceId: Service name\n        :type ServiceId: str\n        :param Environment: Environment name\n        :type Environment: str\n        :param ApiIds: List of APIs for which to generate documents\n        :type ApiIds: list of str\n        """
        self.ApiDocName = None
        self.ServiceId = None
        self.Environment = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.ApiDocName = params.get("ApiDocName")
        self.ServiceId = params.get("ServiceId")
        self.Environment = params.get("Environment")
        self.ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAPIDocResponse(AbstractModel):
    """CreateAPIDoc response structure.

    """

    def __init__(self):
        """
        :param Result: Basic information of API document\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = APIDoc()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateApiKeyRequest(AbstractModel):
    """CreateApiKey request structure.

    """

    def __init__(self):
        """
        :param SecretName: Custom key name.\n        :type SecretName: str\n        :param AccessKeyType: Key type. Valid values: auto, manual (custom key). Default value: auto.\n        :type AccessKeyType: str\n        :param AccessKeyId: Custom key ID, which is required if `AccessKeyType` is `manual`. It can contain 5–50 letters, digits, and underscores.\n        :type AccessKeyId: str\n        :param AccessKeySecret: Custom key, which is required if `AccessKeyType` is `manual`. It can contain 10–50 letters, digits, and underscores.\n        :type AccessKeySecret: str\n        """
        self.SecretName = None
        self.AccessKeyType = None
        self.AccessKeyId = None
        self.AccessKeySecret = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.AccessKeyType = params.get("AccessKeyType")
        self.AccessKeyId = params.get("AccessKeyId")
        self.AccessKeySecret = params.get("AccessKeySecret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiKeyResponse(AbstractModel):
    """CreateApiKey response structure.

    """

    def __init__(self):
        """
        :param Result: New key details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique service ID of API.\n        :type ServiceId: str\n        :param ServiceType: API backend service type. Valid values: HTTP, MOCK, TSF, SCF, WEBSOCKET, TARGET (in beta test).\n        :type ServiceType: str\n        :param ServiceTimeout: API backend service timeout period in seconds.\n        :type ServiceTimeout: int\n        :param Protocol: API frontend request protocol. Valid values: HTTPS, WEBSOCKET.\n        :type Protocol: str\n        :param RequestConfig: Request frontend configuration.\n        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.ApiRequestConfig`\n        :param ApiName: Custom API name.\n        :type ApiName: str\n        :param ApiDesc: Custom API description.\n        :type ApiDesc: str\n        :param ApiType: API type. Valid values: NORMAL (general API), TSF (microservice API). Default value: NORMAL.\n        :type ApiType: str\n        :param AuthType: API authentication type. Valid values: SECRET (key pair authentication), NONE (no authentication), OAUTH, APP (application authentication). Default value: NONE.\n        :type AuthType: str\n        :param EnableCORS: Whether to enable CORS.\n        :type EnableCORS: bool\n        :param ConstantParameters: Constant parameter.\n        :type ConstantParameters: list of ConstantParameter\n        :param RequestParameters: Frontend request parameter.\n        :type RequestParameters: list of RequestParameter\n        :param ApiBusinessType: This field is valid if `AuthType` is `OAUTH`. NORMAL: business API; OAUTH: authorization API.\n        :type ApiBusinessType: str\n        :param ServiceMockReturnMessage: Returned message of API backend Mock, which is required if `ServiceType` is `Mock`.\n        :type ServiceMockReturnMessage: str\n        :param MicroServices: List of microservices bound to API.\n        :type MicroServices: list of MicroServiceReq\n        :param ServiceTsfLoadBalanceConf: Load balancing configuration of microservice.\n        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`\n        :param ServiceTsfHealthCheckConf: Health check configuration of microservice.\n        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`\n        :param TargetServices: `target` type backend resource information (in beta test).\n        :type TargetServices: list of TargetServicesReq\n        :param TargetServicesLoadBalanceConf: `target` type load balancing configuration (in beta test).\n        :type TargetServicesLoadBalanceConf: int\n        :param TargetServicesHealthCheckConf: `target` health check configuration (in beta test).\n        :type TargetServicesHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`\n        :param ServiceScfFunctionName: SCF function name, which takes effect if the backend type is `SCF`.\n        :type ServiceScfFunctionName: str\n        :param ServiceWebsocketRegisterFunctionName: SCF WebSocket registration function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketRegisterFunctionName: str\n        :param ServiceWebsocketCleanupFunctionName: SCF WebSocket cleanup function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketCleanupFunctionName: str\n        :param ServiceWebsocketTransportFunctionName: SCF WebSocket transfer function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketTransportFunctionName: str\n        :param ServiceScfFunctionNamespace: SCF function namespace, which takes effect if the backend type is `SCF`.\n        :type ServiceScfFunctionNamespace: str\n        :param ServiceScfFunctionQualifier: SCF function version, which takes effect if the backend type is `SCF`.\n        :type ServiceScfFunctionQualifier: str\n        :param ServiceWebsocketRegisterFunctionNamespace: SCF WebSocket registration function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketRegisterFunctionNamespace: str\n        :param ServiceWebsocketRegisterFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketRegisterFunctionQualifier: str\n        :param ServiceWebsocketTransportFunctionNamespace: SCF WebSocket transfer function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketTransportFunctionNamespace: str\n        :param ServiceWebsocketTransportFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketTransportFunctionQualifier: str\n        :param ServiceWebsocketCleanupFunctionNamespace: SCF WebSocket cleanup function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketCleanupFunctionNamespace: str\n        :param ServiceWebsocketCleanupFunctionQualifier: SCF WebSocket cleanup function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketCleanupFunctionQualifier: str\n        :param ServiceScfIsIntegratedResponse: Whether to enable response integration, which takes effect if the backend type is `SCF`.\n        :type ServiceScfIsIntegratedResponse: bool\n        :param IsDebugAfterCharge: Billing after debugging starts (reserved field for marketplace).\n        :type IsDebugAfterCharge: bool\n        :param IsDeleteResponseErrorCodes: Whether to delete the error codes for custom response configuration. If the value is left empty or `False`, the error codes will not be deleted. If the value is `True`, all custom response configuration error codes of the API will be deleted.\n        :type IsDeleteResponseErrorCodes: bool\n        :param ResponseType: Return type.\n        :type ResponseType: str\n        :param ResponseSuccessExample: Sample response for successful custom response configuration.\n        :type ResponseSuccessExample: str\n        :param ResponseFailExample: Sample response for failed custom response configuration.\n        :type ResponseFailExample: str\n        :param ServiceConfig: API backend service configuration.\n        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`\n        :param AuthRelationApiId: Unique ID of associated authorization API, which takes effect only if `AuthType` is `OAUTH` and `ApiBusinessType` is `NORMAL`. It is the unique ID of the OAuth 2.0 authorization API bound to the business API.\n        :type AuthRelationApiId: str\n        :param ServiceParameters: API backend service parameter.\n        :type ServiceParameters: list of ServiceParameter\n        :param OauthConfig: OAuth configuration, which takes effect if `AuthType` is `OAUTH`.\n        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`\n        :param ResponseErrorCodes: Custom error code configuration.\n        :type ResponseErrorCodes: list of ResponseErrorCodeReq\n        :param TargetNamespaceId: TSF Serverless namespace ID (in beta test).\n        :type TargetNamespaceId: str\n        :param UserType: User type.\n        :type UserType: str\n        :param IsBase64Encoded: Whether to enable Base64 encoding. This parameter takes effect only when the backend is SCF.\n        :type IsBase64Encoded: bool\n        """
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
        self.IsBase64Encoded = None


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
        self.IsBase64Encoded = params.get("IsBase64Encoded")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiResponse(AbstractModel):
    """CreateApi response structure.

    """

    def __init__(self):
        """
        :param Result: API information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.CreateApiRsp`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateApiRsp()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateApiRsp(AbstractModel):
    """Return of API creation

    """

    def __init__(self):
        """
        :param ApiId: API ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiId: str\n        :param Path: path
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Path: str\n        :param Method: method
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Method: str\n        :param CreatedTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreatedTime: str\n        """
        self.ApiId = None
        self.Path = None
        self.Method = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIPStrategyRequest(AbstractModel):
    """CreateIPStrategy request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.\n        :type ServiceId: str\n        :param StrategyName: Custom policy name.\n        :type StrategyName: str\n        :param StrategyType: Policy type. Valid values: WHITE (allowlist), BLACK (blocklist).\n        :type StrategyType: str\n        :param StrategyData: Policy details. Multiple IPs are separated with \n.\n        :type StrategyData: str\n        """
        self.ServiceId = None
        self.StrategyName = None
        self.StrategyType = None
        self.StrategyData = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyName = params.get("StrategyName")
        self.StrategyType = params.get("StrategyType")
        self.StrategyData = params.get("StrategyData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIPStrategyResponse(AbstractModel):
    """CreateIPStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: New IP policy details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategy`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceName: Custom service name.\n        :type ServiceName: str\n        :param Protocol: Service frontend request type, such as `http`, `https`, and `http&https`.\n        :type Protocol: str\n        :param ServiceDesc: Custom service description.\n        :type ServiceDesc: str\n        :param ExclusiveSetName: Dedicated cluster name, which is used to specify the dedicated cluster where the service is to be created.\n        :type ExclusiveSetName: str\n        :param NetTypes: Network type list, which is used to specify the supported network types. INNER: private network access; OUTER: public network access. Default value: OUTER.\n        :type NetTypes: list of str\n        :param IpVersion: IP version number. Valid values: IPv4, IPv6. Default value: IPv4.\n        :type IpVersion: str\n        :param SetServerName: Cluster name, which is reserved and used by the `tsf serverless` type.\n        :type SetServerName: str\n        :param AppIdType: User type, which is reserved and can be used by `serverless` users.\n        :type AppIdType: str\n        :param Tags: Tag information.\n        :type Tags: list of Tag\n        :param InstanceId: Dedicated instance ID\n        :type InstanceId: str\n        """
        self.ServiceName = None
        self.Protocol = None
        self.ServiceDesc = None
        self.ExclusiveSetName = None
        self.NetTypes = None
        self.IpVersion = None
        self.SetServerName = None
        self.AppIdType = None
        self.Tags = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.ServiceName = params.get("ServiceName")
        self.Protocol = params.get("Protocol")
        self.ServiceDesc = params.get("ServiceDesc")
        self.ExclusiveSetName = params.get("ExclusiveSetName")
        self.NetTypes = params.get("NetTypes")
        self.IpVersion = params.get("IpVersion")
        self.SetServerName = params.get("SetServerName")
        self.AppIdType = params.get("AppIdType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceResponse(AbstractModel):
    """CreateService response structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.\n        :type ServiceId: str\n        :param ServiceName: Custom service name.\n        :type ServiceName: str\n        :param ServiceDesc: Custom service description.\n        :type ServiceDesc: str\n        :param OuterSubDomain: Default public domain name.\n        :type OuterSubDomain: str\n        :param InnerSubDomain: Default VPC domain name.\n        :type InnerSubDomain: str\n        :param CreatedTime: Service creation time in the format of `YYYY-MM-DDThh:mm:ssZ` according to ISO 8601 standard. UTC time is used.\n        :type CreatedTime: str\n        :param NetTypes: Network type list. INNER: private network access; OUTER: public network access.\n        :type NetTypes: list of str\n        :param IpVersion: IP version number.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IpVersion: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param UsagePlanName: Custom usage plan name.\n        :type UsagePlanName: str\n        :param UsagePlanDesc: Custom usage plan description.\n        :type UsagePlanDesc: str\n        :param MaxRequestNum: Total number of requests allowed. Valid values: -1, [1,99999999]. The default value is `-1`, which indicates no limit.\n        :type MaxRequestNum: int\n        :param MaxRequestNumPreSec: Limit of requests per second. Valid values: -1, [1,2000]. The default value is `-1`, which indicates no limit.\n        :type MaxRequestNumPreSec: int\n        """
        self.UsagePlanName = None
        self.UsagePlanDesc = None
        self.MaxRequestNum = None
        self.MaxRequestNumPreSec = None


    def _deserialize(self, params):
        self.UsagePlanName = params.get("UsagePlanName")
        self.UsagePlanDesc = params.get("UsagePlanDesc")
        self.MaxRequestNum = params.get("MaxRequestNum")
        self.MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUsagePlanResponse(AbstractModel):
    """CreateUsagePlan response structure.

    """

    def __init__(self):
        """
        :param Result: Usage plan details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UsagePlanInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteAPIDocRequest(AbstractModel):
    """DeleteAPIDoc request structure.

    """

    def __init__(self):
        """
        :param ApiDocId: API document ID\n        :type ApiDocId: str\n        """
        self.ApiDocId = None


    def _deserialize(self, params):
        self.ApiDocId = params.get("ApiDocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAPIDocResponse(AbstractModel):
    """DeleteAPIDoc response structure.

    """

    def __init__(self):
        """
        :param Result: Whether the operation succeeded\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteApiKeyRequest(AbstractModel):
    """DeleteApiKey request structure.

    """

    def __init__(self):
        """
        :param AccessKeyId: ID of the key to be deleted.\n        :type AccessKeyId: str\n        """
        self.AccessKeyId = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApiKeyResponse(AbstractModel):
    """DeleteApiKey response structure.

    """

    def __init__(self):
        """
        :param Result: Whether deletion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique service ID of API.\n        :type ServiceId: str\n        :param ApiId: Unique API ID.\n        :type ApiId: str\n        """
        self.ServiceId = None
        self.ApiId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApiResponse(AbstractModel):
    """DeleteApi response structure.

    """

    def __init__(self):
        """
        :param Result: Whether deletion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique service ID of the IP policy to be deleted.\n        :type ServiceId: str\n        :param StrategyId: Unique ID of the IP policy to be deleted.\n        :type StrategyId: str\n        """
        self.ServiceId = None
        self.StrategyId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIPStrategyResponse(AbstractModel):
    """DeleteIPStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: Whether deletion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique ID of the service to be deleted.\n        :type ServiceId: str\n        :param SkipVerification: A parameter used to set to skip the deletion precondition verification (only supported for services on dedicated instances).\n        :type SkipVerification: int\n        """
        self.ServiceId = None
        self.SkipVerification = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.SkipVerification = params.get("SkipVerification")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceResponse(AbstractModel):
    """DeleteService response structure.

    """

    def __init__(self):
        """
        :param Result: Whether deletion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique service ID.\n        :type ServiceId: str\n        :param SubDomain: Custom domain name bound to service.\n        :type SubDomain: str\n        :param Environment: Name of the environment whose mapping is to be deleted. Valid values: test (test environment), prepub (pre-release environment), release (release environment).\n        :type Environment: str\n        """
        self.ServiceId = None
        self.SubDomain = None
        self.Environment = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.SubDomain = params.get("SubDomain")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceSubDomainMappingResponse(AbstractModel):
    """DeleteServiceSubDomainMapping response structure.

    """

    def __init__(self):
        """
        :param Result: Whether the path mapping of the custom domain name is successfully deleted.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param UsagePlanId: Unique ID of the usage plan to be deleted.\n        :type UsagePlanId: str\n        """
        self.UsagePlanId = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsagePlanResponse(AbstractModel):
    """DeleteUsagePlan response structure.

    """

    def __init__(self):
        """
        :param Result: Whether deletion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param UsagePlanId: Usage plan ID.\n        :type UsagePlanId: str\n        :param ServiceId: Unique ID of the service to be demoted.\n        :type ServiceId: str\n        :param Environment: Environment name.\n        :type Environment: str\n        """
        self.UsagePlanId = None
        self.ServiceId = None
        self.Environment = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.ServiceId = params.get("ServiceId")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DemoteServiceUsagePlanResponse(AbstractModel):
    """DemoteServiceUsagePlan response structure.

    """

    def __init__(self):
        """
        :param Result: Whether demotion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique service ID.\n        :type ServiceId: str\n        :param ApiId: Unique API ID.\n        :type ApiId: str\n        :param ApiDesc: Custom API description.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiDesc: str\n        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreatedTime: str\n        :param ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ModifiedTime: str\n        :param ApiName: API name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiName: str\n        :param VpcId: VPC ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VpcId: int\n        :param UniqVpcId: Unique VPC ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UniqVpcId: str\n        :param ApiType: API type. Valid values: NORMAL (general API), TSF (microservice API).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiType: str\n        :param Protocol: API protocol.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Protocol: str\n        :param IsDebugAfterCharge: Whether to enable debugging after purchase (reserved field for the marketplace)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsDebugAfterCharge: bool\n        :param AuthType: API authentication type. Valid values: SECRET (key pair authentication), NONE (no authentication), OAUTH.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AuthType: str\n        :param ApiBusinessType: OAuth API type, which is valid if `AuthType` is `OAUTH`. Valid values: NORMAL (business API), OAUTH (authorization API).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiBusinessType: str\n        :param AuthRelationApiId: Unique ID of associated authorization API, which takes effect only if `AuthType` is `OAUTH` and `ApiBusinessType` is `NORMAL`. It is the unique ID of the OAuth 2.0 authorization API bound to the business API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AuthRelationApiId: str\n        :param OauthConfig: OAuth configuration information, which takes effect if `AuthType` is `OAUTH`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`\n        :param RelationBuniessApiIds: List of business APIs associated with authorization API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RelationBuniessApiIds: list of str\n        :param Tags: Information of tags associated with API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Tags: list of str\n        :param Path: API path, such as `/path`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Path: str\n        :param Method: API request method, such as `GET`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Method: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIDocDetailRequest(AbstractModel):
    """DescribeAPIDocDetail request structure.

    """

    def __init__(self):
        """
        :param ApiDocId: API document ID\n        :type ApiDocId: str\n        """
        self.ApiDocId = None


    def _deserialize(self, params):
        self.ApiDocId = params.get("ApiDocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIDocDetailResponse(AbstractModel):
    """DescribeAPIDocDetail response structure.

    """

    def __init__(self):
        """
        :param Result: API document details\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDocInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = APIDocInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeAPIDocsRequest(AbstractModel):
    """DescribeAPIDocs request structure.

    """

    def __init__(self):
        """
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIDocsResponse(AbstractModel):
    """DescribeAPIDocs response structure.

    """

    def __init__(self):
        """
        :param Result: API document list information\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDocs`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = APIDocs()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiEnvironmentStrategyRequest(AbstractModel):
    """DescribeApiEnvironmentStrategy request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID of API.\n        :type ServiceId: str\n        :param EnvironmentNames: Environment list.\n        :type EnvironmentNames: list of str\n        :param ApiId: Unique API ID.\n        :type ApiId: str\n        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiEnvironmentStrategyResponse(AbstractModel):
    """DescribeApiEnvironmentStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: Details of policies bound to API
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiEnvironmentStrategyStataus`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param AccessKeyId: API key ID.\n        :type AccessKeyId: str\n        """
        self.AccessKeyId = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiKeyResponse(AbstractModel):
    """DescribeApiKey response structure.

    """

    def __init__(self):
        """
        :param Result: Key details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiKey()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiKeysStatusRequest(AbstractModel):
    """DescribeApiKeysStatus request structure.

    """

    def __init__(self):
        """
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter. Valid values: AccessKeyId, AccessKeySecret, SecretName, NotUsagePlanId, Status, KeyWord (match with `name` or `path`).\n        :type Filters: list of Filter\n        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiKeysStatusResponse(AbstractModel):
    """DescribeApiKeysStatus response structure.

    """

    def __init__(self):
        """
        :param Result: Key list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKeysStatus`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiKeysStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiRequest(AbstractModel):
    """DescribeApi request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID of API.\n        :type ServiceId: str\n        :param ApiId: Unique API ID.\n        :type ApiId: str\n        """
        self.ServiceId = None
        self.ApiId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiResponse(AbstractModel):
    """DescribeApi response structure.

    """

    def __init__(self):
        """
        :param Result: API details.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique ID of the service to be queried.\n        :type ServiceId: str\n        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiUsagePlanResponse(AbstractModel):
    """DescribeApiUsagePlan response structure.

    """

    def __init__(self):
        """
        :param Result: List of usage plans bound to API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiUsagePlanSet`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiUsagePlanSet()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApisStatusRequest(AbstractModel):
    """DescribeApisStatus request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID of API.\n        :type ServiceId: str\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Filters: API filter. Valid values: ApiId, ApiName, ApiPath, ApiType, AuthRelationApiId, AuthType, ApiBuniessType, NotUsagePlanId, Environment, Tags (whose values are the list of `$tag_key:tag_value`), TagKeys (whose values are the list of tag keys).\n        :type Filters: list of Filter\n        """
        self.ServiceId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApisStatusResponse(AbstractModel):
    """DescribeApisStatus response structure.

    """

    def __init__(self):
        """
        :param Result: List of API details.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApisStatus`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApisStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeIPStrategyApisStatusRequest(AbstractModel):
    """DescribeIPStrategyApisStatus request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.\n        :type ServiceId: str\n        :param StrategyId: Unique policy ID.\n        :type StrategyId: str\n        :param EnvironmentName: Policy environment.\n        :type EnvironmentName: str\n        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter. Valid values: ApiPath, ApiName, KeyWord (fuzzy search by `Path` and `Name`).\n        :type Filters: list of Filter\n        """
        self.ServiceId = None
        self.StrategyId = None
        self.EnvironmentName = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyId = params.get("StrategyId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPStrategyApisStatusResponse(AbstractModel):
    """DescribeIPStrategyApisStatus response structure.

    """

    def __init__(self):
        """
        :param Result: List of APIs bound to environment.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategyApiStatus`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = IPStrategyApiStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeIPStrategyRequest(AbstractModel):
    """DescribeIPStrategy request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.\n        :type ServiceId: str\n        :param StrategyId: Unique IP policy ID.\n        :type StrategyId: str\n        :param EnvironmentName: Environment associated with policy.\n        :type EnvironmentName: str\n        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter, which is a reserved field. Filtering is not supported currently.\n        :type Filters: list of Filter\n        """
        self.ServiceId = None
        self.StrategyId = None
        self.EnvironmentName = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyId = params.get("StrategyId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPStrategyResponse(AbstractModel):
    """DescribeIPStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: IP policy details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategy`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = IPStrategy()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeIPStrategysStatusRequest(AbstractModel):
    """DescribeIPStrategysStatus request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.\n        :type ServiceId: str\n        :param Filters: Filter. Valid values: StrategyName.\n        :type Filters: list of Filter\n        """
        self.ServiceId = None
        self.Filters = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPStrategysStatusResponse(AbstractModel):
    """DescribeIPStrategysStatus response structure.

    """

    def __init__(self):
        """
        :param Result: List of eligible policies.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategysStatus`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = IPStrategysStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeLogSearchRequest(AbstractModel):
    """DescribeLogSearch request structure.

    """

    def __init__(self):
        """
        :param StartTime: Log start time\n        :type StartTime: str\n        :param EndTime: Log end time\n        :type EndTime: str\n        :param ServiceId: Service ID\n        :type ServiceId: str\n        :param Filters: Reserved field\n        :type Filters: list of Filter\n        :param Limit: Number of logs to be returned at a time. Maximum value: 100\n        :type Limit: int\n        :param ConText: Subsequent content can be obtained based on the `ConText` returned last time. Up to 10,000 data entries can be obtained\n        :type ConText: str\n        :param Sort: Sorting by time. Valid values: asc (ascending), desc (descending). Default value: desc\n        :type Sort: str\n        :param Query: Reserved field\n        :type Query: str\n        :param LogQuerys: Search criterion. Valid values:
req_id: "="
api_id: "="
cip: "="
uip: ":"
err_msg: ":"
rsp_st: "=", "!=", ":", ">", "<"
req_t: ">=", "<="

Note:
":" indicates included, and "!=" indicates not equal to. For the meanings of fields, please see the `LogSet` description of the output parameter\n        :type LogQuerys: list of LogQuery\n        """
        self.StartTime = None
        self.EndTime = None
        self.ServiceId = None
        self.Filters = None
        self.Limit = None
        self.ConText = None
        self.Sort = None
        self.Query = None
        self.LogQuerys = None


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
        if params.get("LogQuerys") is not None:
            self.LogQuerys = []
            for item in params.get("LogQuerys"):
                obj = LogQuery()
                obj._deserialize(item)
                self.LogQuerys.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogSearchResponse(AbstractModel):
    """DescribeLogSearch response structure.

    """

    def __init__(self):
        """
        :param ConText: Cursor for getting more search results. If the value is `""`, there will be no subsequent results\n        :type ConText: str\n        :param LogSet: The returned result contains any number of logs, which are in the following format:
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
ups_st: backend business server response status code (if the request is passed through to the backend, this variable will not be empty. If the request is blocked in API Gateway, this variable will be displayed as `-`).
cip: client IP.
uip: backend business service (upstream) IP.
vip: VIP requested to be accessed.
rsp_len: response length.
req_len: request length.
req_t: total request response time.
ups_rsp_t: total backend response time (time between connection establishment by API Gateway and backend response receipt).
ups_conn_t: time when the backend business server is successfully connected to.
ups_head_t: time when the backend response header arrives.
err_msg: error message.
tcp_rtt: client TCP connection information. RTT (Round Trip Time) consists of three parts: link propagation delay, end system processing delay, and queuing delay in router cache.
req_id: request ID.\n        :type LogSet: list of str\n        :param TotalCount: Number of logs returned for one search (`TotalCount <= Limit`)\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique ID of the service to be queried.\n        :type ServiceId: str\n        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceEnvironmentListResponse(AbstractModel):
    """DescribeServiceEnvironmentList response structure.

    """

    def __init__(self):
        """
        :param Result: Details of environments bound to service.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceEnvironmentSet`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique ID of the service to be queried.\n        :type ServiceId: str\n        :param EnvironmentName: Environment name.\n        :type EnvironmentName: str\n        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
        self.ServiceId = None
        self.EnvironmentName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceEnvironmentReleaseHistoryResponse(AbstractModel):
    """DescribeServiceEnvironmentReleaseHistory response structure.

    """

    def __init__(self):
        """
        :param Result: Service release history.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceReleaseHistory`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique service ID.\n        :type ServiceId: str\n        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceEnvironmentStrategyResponse(AbstractModel):
    """DescribeServiceEnvironmentStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: Throttling policy list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceEnvironmentStrategyStatus`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique ID of the service to be queried.\n        :type ServiceId: str\n        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceReleaseVersionResponse(AbstractModel):
    """DescribeServiceReleaseVersion response structure.

    """

    def __init__(self):
        """
        :param Result: Service release version list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceReleaseVersion`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique ID of the service to be queried.\n        :type ServiceId: str\n        """
        self.ServiceId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceResponse(AbstractModel):
    """DescribeService response structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.\n        :type ServiceId: str\n        :param AvailableEnvironments: Service environment list.\n        :type AvailableEnvironments: list of str\n        :param ServiceName: Service name.\n        :type ServiceName: str\n        :param ServiceDesc: Service description.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceDesc: str\n        :param Protocol: Protocol supported by service. Valid values: http, https, http&https.\n        :type Protocol: str\n        :param CreatedTime: Service creation time.\n        :type CreatedTime: str\n        :param ModifiedTime: Service modification time.\n        :type ModifiedTime: str\n        :param ExclusiveSetName: Dedicated cluster name.\n        :type ExclusiveSetName: str\n        :param NetTypes: Network type list. INNER: private network access; OUTER: public network access.\n        :type NetTypes: list of str\n        :param InternalSubDomain: Subdomain name for private network access.\n        :type InternalSubDomain: str\n        :param OuterSubDomain: Subdomain name for public network access.\n        :type OuterSubDomain: str\n        :param InnerHttpPort: Service port number for HTTP access over private network.\n        :type InnerHttpPort: int\n        :param InnerHttpsPort: Port number for HTTPS access over private network.\n        :type InnerHttpsPort: int\n        :param ApiTotalCount: Total number of APIs.\n        :type ApiTotalCount: int\n        :param ApiIdStatusSet: API list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiIdStatusSet: list of ApiIdStatus\n        :param UsagePlanTotalCount: Total number of usage plans.\n        :type UsagePlanTotalCount: int\n        :param UsagePlanList: Usage plan array.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UsagePlanList: list of UsagePlan\n        :param IpVersion: IP version.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IpVersion: str\n        :param UserType: Service user type.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UserType: str\n        :param SetId: Reserved field.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SetId: int\n        :param Tags: Tags bound to a service.
Note: this field may return null, indicating that no valid values found.\n        :type Tags: list of Tag\n        :param InstanceId: Dedicated instance ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InstanceId: str\n        :param InstanceName: Dedicated instance name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InstanceName: str\n        :param SetType: Cluster type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SetType: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        self.Tags = None
        self.InstanceId = None
        self.InstanceName = None
        self.SetType = None
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
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.SetType = params.get("SetType")
        self.RequestId = params.get("RequestId")


class DescribeServiceSubDomainMappingsRequest(AbstractModel):
    """DescribeServiceSubDomainMappings request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.\n        :type ServiceId: str\n        :param SubDomain: Custom domain name bound to service.\n        :type SubDomain: str\n        """
        self.ServiceId = None
        self.SubDomain = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.SubDomain = params.get("SubDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceSubDomainMappingsResponse(AbstractModel):
    """DescribeServiceSubDomainMappings response structure.

    """

    def __init__(self):
        """
        :param Result: Custom path mapping list.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceSubDomainMappings`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique service ID.\n        :type ServiceId: str\n        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceSubDomainsResponse(AbstractModel):
    """DescribeServiceSubDomains response structure.

    """

    def __init__(self):
        """
        :param Result: Custom service domain name query.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DomainSets`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique ID of the service to be queried.\n        :type ServiceId: str\n        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceUsagePlanResponse(AbstractModel):
    """DescribeServiceUsagePlan response structure.

    """

    def __init__(self):
        """
        :param Result: List of usage plans bound to service.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceUsagePlanSet`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServiceUsagePlanSet()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServicesStatusRequest(AbstractModel):
    """DescribeServicesStatus request structure.

    """

    def __init__(self):
        """
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter. Valid values: ServiceId, ServiceName, NotUsagePlanId, Environment, IpVersion, InstanceId\n        :type Filters: list of Filter\n        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServicesStatusResponse(AbstractModel):
    """DescribeServicesStatus response structure.

    """

    def __init__(self):
        """
        :param Result: Service list query result.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServicesStatus`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServicesStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUsagePlanEnvironmentsRequest(AbstractModel):
    """DescribeUsagePlanEnvironments request structure.

    """

    def __init__(self):
        """
        :param UsagePlanId: Unique ID of the usage plan to be queried.\n        :type UsagePlanId: str\n        :param BindType: Binding type. Valid values: API, SERVICE. Default value: SERVICE.\n        :type BindType: str\n        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
        self.UsagePlanId = None
        self.BindType = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.BindType = params.get("BindType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsagePlanEnvironmentsResponse(AbstractModel):
    """DescribeUsagePlanEnvironments response structure.

    """

    def __init__(self):
        """
        :param Result: Usage plan binding details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanEnvironmentStatus`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param UsagePlanId: Unique ID of the usage plan to be queried.\n        :type UsagePlanId: str\n        """
        self.UsagePlanId = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsagePlanResponse(AbstractModel):
    """DescribeUsagePlan response structure.

    """

    def __init__(self):
        """
        :param Result: Usage plan details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param UsagePlanId: Unique ID of bound usage plan.\n        :type UsagePlanId: str\n        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
        self.UsagePlanId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsagePlanSecretIdsResponse(AbstractModel):
    """DescribeUsagePlanSecretIds response structure.

    """

    def __init__(self):
        """
        :param Result: List of keys bound to usage plan.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanBindSecretStatus`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UsagePlanBindSecretStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUsagePlansStatusRequest(AbstractModel):
    """DescribeUsagePlansStatus request structure.

    """

    def __init__(self):
        """
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Usage plan filter. Valid values: UsagePlanId, UsagePlanName, NotServiceId, NotApiId, Environment.\n        :type Filters: list of Filter\n        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsagePlansStatusResponse(AbstractModel):
    """DescribeUsagePlansStatus response structure.

    """

    def __init__(self):
        """
        :param Result: Usage plan list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlansStatus`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UsagePlansStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DisableApiKeyRequest(AbstractModel):
    """DisableApiKey request structure.

    """

    def __init__(self):
        """
        :param AccessKeyId: ID of the key to be disabled.\n        :type AccessKeyId: str\n        """
        self.AccessKeyId = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableApiKeyResponse(AbstractModel):
    """DisableApiKey response structure.

    """

    def __init__(self):
        """
        :param Result: Whether the key is successfully disabled.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DocumentSDK(AbstractModel):
    """API document download

    """

    def __init__(self):
        """
        :param DocumentURL: Download link of generated file. Generated documents will be stored in COS.\n        :type DocumentURL: str\n        :param SdkURL: Download link of generated SDK file. Generated SDK files will be stored in COS.\n        :type SdkURL: str\n        """
        self.DocumentURL = None
        self.SdkURL = None


    def _deserialize(self, params):
        self.DocumentURL = params.get("DocumentURL")
        self.SdkURL = params.get("SdkURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainSetList(AbstractModel):
    """Custom service domain name list

    """

    def __init__(self):
        """
        :param DomainName: Domain name.\n        :type DomainName: str\n        :param Status: Domain name resolution status. True: success; False: failure.\n        :type Status: int\n        :param CertificateId: Certificate ID.\n        :type CertificateId: str\n        :param IsDefaultMapping: Whether the default path mapping is used.\n        :type IsDefaultMapping: bool\n        :param Protocol: Custom domain name protocol type.\n        :type Protocol: str\n        :param NetType: Network type. Valid values: INNER, OUTER.\n        :type NetType: str\n        :param IsForcedHttps: Whether to force HTTP requests to redirect to HTTPS. Default value: `false`. When this parameter is `true`, API Gateway will redirect all requests using the custom domain name over the HTTP protocol to the HTTPS protocol for forwarding.\n        :type IsForcedHttps: bool\n        :param RegistrationStatus: ICP filing status\n        :type RegistrationStatus: bool\n        """
        self.DomainName = None
        self.Status = None
        self.CertificateId = None
        self.IsDefaultMapping = None
        self.Protocol = None
        self.NetType = None
        self.IsForcedHttps = None
        self.RegistrationStatus = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Status = params.get("Status")
        self.CertificateId = params.get("CertificateId")
        self.IsDefaultMapping = params.get("IsDefaultMapping")
        self.Protocol = params.get("Protocol")
        self.NetType = params.get("NetType")
        self.IsForcedHttps = params.get("IsForcedHttps")
        self.RegistrationStatus = params.get("RegistrationStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainSets(AbstractModel):
    """Custom service domain name information

    """

    def __init__(self):
        """
        :param TotalCount: Number of custom domain names under service\n        :type TotalCount: int\n        :param DomainSet: Custom service domain name list.\n        :type DomainSet: list of DomainSetList\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApiKeyRequest(AbstractModel):
    """EnableApiKey request structure.

    """

    def __init__(self):
        """
        :param AccessKeyId: ID of the key to be enabled.\n        :type AccessKeyId: str\n        """
        self.AccessKeyId = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApiKeyResponse(AbstractModel):
    """EnableApiKey response structure.

    """

    def __init__(self):
        """
        :param Result: Whether the key is successfully enabled.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class Environment(AbstractModel):
    """Information of service release environment.

    """

    def __init__(self):
        """
        :param EnvironmentName: Environment name.\n        :type EnvironmentName: str\n        :param Url: Access path.\n        :type Url: str\n        :param Status: Release status. 1: published. 0: not published.\n        :type Status: int\n        :param VersionName: Running version.\n        :type VersionName: str\n        """
        self.EnvironmentName = None
        self.Url = None
        self.Status = None
        self.VersionName = None


    def _deserialize(self, params):
        self.EnvironmentName = params.get("EnvironmentName")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.VersionName = params.get("VersionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvironmentStrategy(AbstractModel):
    """Environment throttling

    """

    def __init__(self):
        """
        :param EnvironmentName: Environment name\n        :type EnvironmentName: str\n        :param Quota: Throttling value\n        :type Quota: int\n        :param MaxQuota: Maximum quota value
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxQuota: int\n        """
        self.EnvironmentName = None
        self.Quota = None
        self.MaxQuota = None


    def _deserialize(self, params):
        self.EnvironmentName = params.get("EnvironmentName")
        self.Quota = params.get("Quota")
        self.MaxQuota = params.get("MaxQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorCodes(AbstractModel):
    """Custom error code

    """

    def __init__(self):
        """
        :param Code: Custom response configuration error code.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Code: int\n        :param Msg: Custom response configuration error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Msg: str\n        :param Desc: Custom response configuration error code remarks.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Desc: str\n        :param ConvertedCode: Custom error code conversion.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ConvertedCode: int\n        :param NeedConvert: Whether to enable error code conversion.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NeedConvert: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """>Key-value pair filter for conditional filtering queries, such as filtering ID, name, status, etc.
    > * If there are multiple `Filter`, the relationship among them is logical `AND`.
    > * If there are multiple `Values` in the same `Filter`, the relationship among them is logical `OR`.
    >

    """

    def __init__(self):
        """
        :param Name: Field to be filtered.\n        :type Name: str\n        :param Values: Filter value of field.\n        :type Values: list of str\n        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateApiDocumentRequest(AbstractModel):
    """GenerateApiDocument request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID of the document to be created.\n        :type ServiceId: str\n        :param GenEnvironment: Environment of the service for which to create an SDK.\n        :type GenEnvironment: str\n        :param GenLanguage: Programming language of the SDK to be created. Currently, only Python and JavaScript are supported.\n        :type GenLanguage: str\n        """
        self.ServiceId = None
        self.GenEnvironment = None
        self.GenLanguage = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.GenEnvironment = params.get("GenEnvironment")
        self.GenLanguage = params.get("GenLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateApiDocumentResponse(AbstractModel):
    """GenerateApiDocument response structure.

    """

    def __init__(self):
        """
        :param Result: API document and SDK link.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DocumentSDK`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param IsHealthCheck: Whether health check is enabled.\n        :type IsHealthCheck: bool\n        :param RequestVolumeThreshold: Health check threshold.\n        :type RequestVolumeThreshold: int\n        :param SleepWindowInMilliseconds: Window size.\n        :type SleepWindowInMilliseconds: int\n        :param ErrorThresholdPercentage: Threshold percentage.\n        :type ErrorThresholdPercentage: int\n        """
        self.IsHealthCheck = None
        self.RequestVolumeThreshold = None
        self.SleepWindowInMilliseconds = None
        self.ErrorThresholdPercentage = None


    def _deserialize(self, params):
        self.IsHealthCheck = params.get("IsHealthCheck")
        self.RequestVolumeThreshold = params.get("RequestVolumeThreshold")
        self.SleepWindowInMilliseconds = params.get("SleepWindowInMilliseconds")
        self.ErrorThresholdPercentage = params.get("ErrorThresholdPercentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPStrategy(AbstractModel):
    """IP policy

    """

    def __init__(self):
        """
        :param StrategyId: Unique policy ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StrategyId: str\n        :param StrategyName: Custom policy name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StrategyName: str\n        :param StrategyType: Policy type. Valid values: WHITE (allowlist), BLACK (blocklist).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StrategyType: str\n        :param StrategyData: IP list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StrategyData: str\n        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreatedTime: str\n        :param ModifiedTime: Modification time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ModifiedTime: str\n        :param ServiceId: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceId: str\n        :param BindApiTotalCount: Number of APIs bound to policy.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BindApiTotalCount: int\n        :param BindApis: Bound API details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BindApis: list of DesApisStatus\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPStrategyApi(AbstractModel):
    """List of APIs bound to policy

    """

    def __init__(self):
        """
        :param ApiId: Unique API ID.\n        :type ApiId: str\n        :param ApiName: Custom API name.\n        :type ApiName: str\n        :param ApiType: API type. Valid values: NORMAL (general API), TSF (microservice API).\n        :type ApiType: str\n        :param Path: API path, such as `/path`.\n        :type Path: str\n        :param Method: API request method, such as `GET`.\n        :type Method: str\n        :param OtherIPStrategyId: Unique ID of another policy bound to API.\n        :type OtherIPStrategyId: str\n        :param OtherEnvironmentName: Environment bound to API.\n        :type OtherEnvironmentName: str\n        """
        self.ApiId = None
        self.ApiName = None
        self.ApiType = None
        self.Path = None
        self.Method = None
        self.OtherIPStrategyId = None
        self.OtherEnvironmentName = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.ApiName = params.get("ApiName")
        self.ApiType = params.get("ApiType")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.OtherIPStrategyId = params.get("OtherIPStrategyId")
        self.OtherEnvironmentName = params.get("OtherEnvironmentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPStrategyApiStatus(AbstractModel):
    """Details of API bound to IP policy

    """

    def __init__(self):
        """
        :param TotalCount: Number of APIs bound to environment.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param ApiIdStatusSet: Details of APIs bound to environment.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiIdStatusSet: list of IPStrategyApi\n        """
        self.TotalCount = None
        self.ApiIdStatusSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiIdStatusSet") is not None:
            self.ApiIdStatusSet = []
            for item in params.get("ApiIdStatusSet"):
                obj = IPStrategyApi()
                obj._deserialize(item)
                self.ApiIdStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPStrategysStatus(AbstractModel):
    """Policy list

    """

    def __init__(self):
        """
        :param TotalCount: Number of policies.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param StrategySet: Policy list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StrategySet: list of IPStrategy\n        """
        self.TotalCount = None
        self.StrategySet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("StrategySet") is not None:
            self.StrategySet = []
            for item in params.get("StrategySet"):
                obj = IPStrategy()
                obj._deserialize(item)
                self.StrategySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogQuery(AbstractModel):
    """Search criterion input parameter

    """

    def __init__(self):
        """
        :param Name: Search field\n        :type Name: str\n        :param Operator: Operator\n        :type Operator: str\n        :param Value: Search value\n        :type Value: str\n        """
        self.Name = None
        self.Operator = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Operator = params.get("Operator")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MicroService(AbstractModel):
    """Information of microservice bound to API.

    """

    def __init__(self):
        """
        :param ClusterId: Microservice cluster ID.\n        :type ClusterId: str\n        :param NamespaceId: Microservice namespace ID.\n        :type NamespaceId: str\n        :param MicroServiceName: Microservice name.\n        :type MicroServiceName: str\n        """
        self.ClusterId = None
        self.NamespaceId = None
        self.MicroServiceName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.MicroServiceName = params.get("MicroServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MicroServiceReq(AbstractModel):
    """TSF type input parameters

    """

    def __init__(self):
        """
        :param ClusterId: Microservice cluster.\n        :type ClusterId: str\n        :param NamespaceId: Microservice namespace.\n        :type NamespaceId: str\n        :param MicroServiceName: Microservice name.\n        :type MicroServiceName: str\n        """
        self.ClusterId = None
        self.NamespaceId = None
        self.MicroServiceName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.MicroServiceName = params.get("MicroServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAPIDocRequest(AbstractModel):
    """ModifyAPIDoc request structure.

    """

    def __init__(self):
        """
        :param ApiDocId: API document ID\n        :type ApiDocId: str\n        :param ApiDocName: API document name\n        :type ApiDocName: str\n        :param ServiceId: Service name\n        :type ServiceId: str\n        :param Environment: Environment name\n        :type Environment: str\n        :param ApiIds: List of APIs for which to generate documents\n        :type ApiIds: list of str\n        """
        self.ApiDocId = None
        self.ApiDocName = None
        self.ServiceId = None
        self.Environment = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.ApiDocId = params.get("ApiDocId")
        self.ApiDocName = params.get("ApiDocName")
        self.ServiceId = params.get("ServiceId")
        self.Environment = params.get("Environment")
        self.ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAPIDocResponse(AbstractModel):
    """ModifyAPIDoc response structure.

    """

    def __init__(self):
        """
        :param Result: Basic information of API document\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = APIDoc()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyApiEnvironmentStrategyRequest(AbstractModel):
    """ModifyApiEnvironmentStrategy request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.\n        :type ServiceId: str\n        :param Strategy: Throttling value.\n        :type Strategy: int\n        :param EnvironmentName: Environment name.\n        :type EnvironmentName: str\n        :param ApiIds: API list.\n        :type ApiIds: list of str\n        """
        self.ServiceId = None
        self.Strategy = None
        self.EnvironmentName = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Strategy = params.get("Strategy")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiEnvironmentStrategyResponse(AbstractModel):
    """ModifyApiEnvironmentStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: Whether modification succeeded.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Service ID\n        :type ServiceId: str\n        :param ApiId: API ID\n        :type ApiId: str\n        :param BusinessType: Authorization type of the API to be modified (you can select `OAUTH`, i.e., authorization API)\n        :type BusinessType: str\n        :param PublicKey: Public key value to be modified by OAuth API\n        :type PublicKey: str\n        :param LoginRedirectUrl: OAuth API redirect address\n        :type LoginRedirectUrl: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiIncrementResponse(AbstractModel):
    """ModifyApiIncrement response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApiRequest(AbstractModel):
    """ModifyApi request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID of API.\n        :type ServiceId: str\n        :param ServiceType: API backend service type. Valid values: HTTP, MOCK, TSF, CLB, SCF, WEBSOCKET, TARGET (in beta test).\n        :type ServiceType: str\n        :param RequestConfig: Request frontend configuration.\n        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.RequestConfig`\n        :param ApiId: Unique API ID.\n        :type ApiId: str\n        :param ApiName: Custom API name.\n        :type ApiName: str\n        :param ApiDesc: Custom API description.\n        :type ApiDesc: str\n        :param ApiType: API type. Valid values: NORMAL, TSF. Default value: NORMAL.\n        :type ApiType: str\n        :param AuthType: API authentication type. Valid values: SECRET, NONE, OAUTH, APP. Default value: NONE.\n        :type AuthType: str\n        :param AuthRequired: Whether signature authentication is required. True: yes; False: no. This parameter is to be disused.\n        :type AuthRequired: bool\n        :param ServiceTimeout: API backend service timeout period in seconds.\n        :type ServiceTimeout: int\n        :param Protocol: API frontend request type, such as HTTP, HTTPS, or HTTP and HTTPS.\n        :type Protocol: str\n        :param EnableCORS: Whether to enable CORS. True: yes; False: no.\n        :type EnableCORS: bool\n        :param ConstantParameters: Constant parameter.\n        :type ConstantParameters: list of ConstantParameter\n        :param RequestParameters: Frontend request parameter.\n        :type RequestParameters: list of ReqParameter\n        :param ApiBusinessType: This field is valid if `AuthType` is `OAUTH`. NORMAL: business API; OAUTH: authorization API.\n        :type ApiBusinessType: str\n        :param ServiceMockReturnMessage: Returned message of API backend Mock, which is required if `ServiceType` is `Mock`.\n        :type ServiceMockReturnMessage: str\n        :param MicroServices: List of microservices bound to API.\n        :type MicroServices: list of MicroServiceReq\n        :param ServiceTsfLoadBalanceConf: Load balancing configuration of microservice.\n        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`\n        :param ServiceTsfHealthCheckConf: Health check configuration of microservice.\n        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`\n        :param TargetServicesLoadBalanceConf: `target` type load balancing configuration (in beta test).\n        :type TargetServicesLoadBalanceConf: int\n        :param TargetServicesHealthCheckConf: `target` health check configuration (in beta test).\n        :type TargetServicesHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`\n        :param ServiceScfFunctionName: SCF function name, which takes effect if the backend type is `SCF`.\n        :type ServiceScfFunctionName: str\n        :param ServiceWebsocketRegisterFunctionName: SCF WebSocket registration function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketRegisterFunctionName: str\n        :param ServiceWebsocketCleanupFunctionName: SCF WebSocket cleanup function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketCleanupFunctionName: str\n        :param ServiceWebsocketTransportFunctionName: SCF WebSocket transfer function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketTransportFunctionName: str\n        :param ServiceScfFunctionNamespace: SCF function namespace, which takes effect if the backend type is `SCF`.\n        :type ServiceScfFunctionNamespace: str\n        :param ServiceScfFunctionQualifier: SCF function version, which takes effect if the backend type is `SCF`.\n        :type ServiceScfFunctionQualifier: str\n        :param ServiceWebsocketRegisterFunctionNamespace: SCF WebSocket registration function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketRegisterFunctionNamespace: str\n        :param ServiceWebsocketRegisterFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketRegisterFunctionQualifier: str\n        :param ServiceWebsocketTransportFunctionNamespace: SCF WebSocket transfer function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketTransportFunctionNamespace: str\n        :param ServiceWebsocketTransportFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketTransportFunctionQualifier: str\n        :param ServiceWebsocketCleanupFunctionNamespace: SCF WebSocket cleanup function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketCleanupFunctionNamespace: str\n        :param ServiceWebsocketCleanupFunctionQualifier: SCF WebSocket cleanup function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.\n        :type ServiceWebsocketCleanupFunctionQualifier: str\n        :param ServiceScfIsIntegratedResponse: Whether to enable response integration, which takes effect if the backend type is `SCF`.\n        :type ServiceScfIsIntegratedResponse: bool\n        :param IsDebugAfterCharge: Billing after debugging starts (reserved field for marketplace).\n        :type IsDebugAfterCharge: bool\n        :param TagSpecifications: Tag.\n        :type TagSpecifications: :class:`tencentcloud.apigateway.v20180808.models.Tag`\n        :param IsDeleteResponseErrorCodes: Whether to delete the error codes for custom response configuration. If the value is left empty or `False`, the error codes will not be deleted. If the value is `True`, all custom response configuration error codes of the API will be deleted.\n        :type IsDeleteResponseErrorCodes: bool\n        :param ResponseType: Return type.\n        :type ResponseType: str\n        :param ResponseSuccessExample: Sample response for successful custom response configuration.\n        :type ResponseSuccessExample: str\n        :param ResponseFailExample: Sample response for failed custom response configuration.\n        :type ResponseFailExample: str\n        :param ServiceConfig: API backend service configuration.\n        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`\n        :param AuthRelationApiId: Unique ID of associated authorization API, which takes effect only if `AuthType` is `OAUTH` and `ApiBusinessType` is `NORMAL`. It is the unique ID of the OAuth 2.0 authorization API bound to the business API.\n        :type AuthRelationApiId: str\n        :param ServiceParameters: API backend service parameter.\n        :type ServiceParameters: list of ServiceParameter\n        :param OauthConfig: OAuth configuration, which takes effect if `AuthType` is `OAUTH`.\n        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`\n        :param ResponseErrorCodes: Custom error code configuration.\n        :type ResponseErrorCodes: list of ResponseErrorCodeReq\n        :param IsBase64Encoded: Whether to enable Base64 encoding. This parameter takes effect only when the backend is SCF.\n        :type IsBase64Encoded: bool\n        :param IsBase64Trigger: Whether to trigger Base64 encoding by header. This parameter takes effect only when the backend is SCF.\n        :type IsBase64Trigger: bool\n        :param Base64EncodedTriggerRules: Header trigger rules. The number of rules cannot exceed 10.\n        :type Base64EncodedTriggerRules: list of Base64EncodedTriggerRule\n        """
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
        self.IsBase64Encoded = None
        self.IsBase64Trigger = None
        self.Base64EncodedTriggerRules = None


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
        self.IsBase64Encoded = params.get("IsBase64Encoded")
        self.IsBase64Trigger = params.get("IsBase64Trigger")
        if params.get("Base64EncodedTriggerRules") is not None:
            self.Base64EncodedTriggerRules = []
            for item in params.get("Base64EncodedTriggerRules"):
                obj = Base64EncodedTriggerRule()
                obj._deserialize(item)
                self.Base64EncodedTriggerRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiResponse(AbstractModel):
    """ModifyApi response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIPStrategyRequest(AbstractModel):
    """ModifyIPStrategy request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID of the policy to be modified.\n        :type ServiceId: str\n        :param StrategyId: Unique ID of the policy to be modified.\n        :type StrategyId: str\n        :param StrategyData: Details of the policy to be modified.\n        :type StrategyData: str\n        """
        self.ServiceId = None
        self.StrategyId = None
        self.StrategyData = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyId = params.get("StrategyId")
        self.StrategyData = params.get("StrategyData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIPStrategyResponse(AbstractModel):
    """ModifyIPStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: Whether modification succeeded.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique service ID.\n        :type ServiceId: str\n        :param Strategy: Throttling value.\n        :type Strategy: int\n        :param EnvironmentNames: Environment list.\n        :type EnvironmentNames: list of str\n        """
        self.ServiceId = None
        self.Strategy = None
        self.EnvironmentNames = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Strategy = params.get("Strategy")
        self.EnvironmentNames = params.get("EnvironmentNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceEnvironmentStrategyResponse(AbstractModel):
    """ModifyServiceEnvironmentStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: Whether modification succeeded.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique ID of the service to be modified.\n        :type ServiceId: str\n        :param ServiceName: Service name after modification.\n        :type ServiceName: str\n        :param ServiceDesc: Service description after modification.\n        :type ServiceDesc: str\n        :param Protocol: Service frontend request type after modification, such as `http`, `https`, and `http&https`.\n        :type Protocol: str\n        :param NetTypes: Network type list, which is used to specify the supported network types. INNER: private network access; OUTER: public network access. Default value: OUTER.\n        :type NetTypes: list of str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceResponse(AbstractModel):
    """ModifyService response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubDomainRequest(AbstractModel):
    """ModifySubDomain request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique service ID.\n        :type ServiceId: str\n        :param SubDomain: Custom domain name whose path mapping is to be modified.\n        :type SubDomain: str\n        :param IsDefaultMapping: Whether to change to the default path mapping. true: use the default path mapping; false: use the custom path mapping.\n        :type IsDefaultMapping: bool\n        :param CertificateId: Certificate ID, which is required if the HTTPS protocol is included.\n        :type CertificateId: str\n        :param Protocol: Custom domain name protocol type after modification. Valid values: http, https, http&https.\n        :type Protocol: str\n        :param PathMappingSet: Path mapping list after modification.\n        :type PathMappingSet: list of PathMapping\n        :param NetType: Network type. Valid values: INNER, OUTER.\n        :type NetType: str\n        :param IsForcedHttps: Whether to force HTTP requests to redirect to HTTPS. Default value: `false`. When this parameter is `true`, API Gateway will redirect all requests using the custom domain name over the HTTP protocol to the HTTPS protocol for forwarding.\n        :type IsForcedHttps: bool\n        """
        self.ServiceId = None
        self.SubDomain = None
        self.IsDefaultMapping = None
        self.CertificateId = None
        self.Protocol = None
        self.PathMappingSet = None
        self.NetType = None
        self.IsForcedHttps = None


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
        self.IsForcedHttps = params.get("IsForcedHttps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubDomainResponse(AbstractModel):
    """ModifySubDomain response structure.

    """

    def __init__(self):
        """
        :param Result: Whether the custom domain name is successfully modified.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param UsagePlanId: Unique usage plan ID.\n        :type UsagePlanId: str\n        :param UsagePlanName: Custom usage plan name after modification.\n        :type UsagePlanName: str\n        :param UsagePlanDesc: Custom usage plan description after modification.\n        :type UsagePlanDesc: str\n        :param MaxRequestNum: Total number of requests allowed. Valid values: -1, [1,99999999]. The default value is `-1`, which indicates no limit.\n        :type MaxRequestNum: int\n        :param MaxRequestNumPreSec: Limit of requests per second. Valid values: -1, [1,2000]. The default value is `-1`, which indicates no limit.\n        :type MaxRequestNumPreSec: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUsagePlanResponse(AbstractModel):
    """ModifyUsagePlan response structure.

    """

    def __init__(self):
        """
        :param Result: Usage plan details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param PublicKey: Public key for user token verification.\n        :type PublicKey: str\n        :param TokenLocation: Token delivery location.\n        :type TokenLocation: str\n        :param LoginRedirectUrl: Redirect address, which is used to guide user logins.\n        :type LoginRedirectUrl: str\n        """
        self.PublicKey = None
        self.TokenLocation = None
        self.LoginRedirectUrl = None


    def _deserialize(self, params):
        self.PublicKey = params.get("PublicKey")
        self.TokenLocation = params.get("TokenLocation")
        self.LoginRedirectUrl = params.get("LoginRedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathMapping(AbstractModel):
    """Custom domain name path mapping.

    """

    def __init__(self):
        """
        :param Path: Path.\n        :type Path: str\n        :param Environment: Release environment. Valid values: test, prepub, release.\n        :type Environment: str\n        """
        self.Path = None
        self.Environment = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseService(AbstractModel):
    """Returned result of service publishing

    """

    def __init__(self):
        """
        :param ReleaseDesc: Release remarks.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ReleaseDesc: str\n        :param ReleaseVersion: Published version ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ReleaseVersion: str\n        """
        self.ReleaseDesc = None
        self.ReleaseVersion = None


    def _deserialize(self, params):
        self.ReleaseDesc = params.get("ReleaseDesc")
        self.ReleaseVersion = params.get("ReleaseVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseServiceRequest(AbstractModel):
    """ReleaseService request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of the service to be published.\n        :type ServiceId: str\n        :param EnvironmentName: Name of the environment to be published. Valid values: test (test environment), prepub (pre-release environment), release (release environment).\n        :type EnvironmentName: str\n        :param ReleaseDesc: Release description.\n        :type ReleaseDesc: str\n        :param ApiIds: `apiId` list, which is reserved. Full API release is used by default.\n        :type ApiIds: list of str\n        """
        self.ServiceId = None
        self.EnvironmentName = None
        self.ReleaseDesc = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ReleaseDesc = params.get("ReleaseDesc")
        self.ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseServiceResponse(AbstractModel):
    """ReleaseService response structure.

    """

    def __init__(self):
        """
        :param Result: Release information.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ReleaseService`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ReleaseService()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ReqParameter(AbstractModel):
    """Request parameter

    """

    def __init__(self):
        """
        :param Name: API frontend parameter name.\n        :type Name: str\n        :param Position: Position of the API frontend parameter, such as the header. Supported values: `header`, `query`, and `path`.\n        :type Position: str\n        :param Type: API frontend parameter type, such as `String` and `int`.\n        :type Type: str\n        :param DefaultValue: Default value of API frontend parameter.\n        :type DefaultValue: str\n        :param Required: Whether the API frontend parameter is required. True: yes; False: no.\n        :type Required: bool\n        :param Desc: API frontend parameter remarks.\n        :type Desc: str\n        """
        self.Name = None
        self.Position = None
        self.Type = None
        self.DefaultValue = None
        self.Required = None
        self.Desc = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Position = params.get("Position")
        self.Type = params.get("Type")
        self.DefaultValue = params.get("DefaultValue")
        self.Required = params.get("Required")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestConfig(AbstractModel):
    """Frontend path configuration

    """

    def __init__(self):
        """
        :param Path: API path, such as `/path`.\n        :type Path: str\n        :param Method: API request method, such as `GET`.\n        :type Method: str\n        """
        self.Path = None
        self.Method = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestParameter(AbstractModel):
    """Request parameter

    """

    def __init__(self):
        """
        :param Name: Request parameter name\n        :type Name: str\n        :param Desc: Description\n        :type Desc: str\n        :param Position: Parameter position\n        :type Position: str\n        :param Type: Parameter type\n        :type Type: str\n        :param DefaultValue: Default value\n        :type DefaultValue: str\n        :param Required: Whether it is required\n        :type Required: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAPIDocPasswordRequest(AbstractModel):
    """ResetAPIDocPassword request structure.

    """

    def __init__(self):
        """
        :param ApiDocId: API document ID\n        :type ApiDocId: str\n        """
        self.ApiDocId = None


    def _deserialize(self, params):
        self.ApiDocId = params.get("ApiDocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAPIDocPasswordResponse(AbstractModel):
    """ResetAPIDocPassword response structure.

    """

    def __init__(self):
        """
        :param Result: Basic information of API document\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = APIDoc()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ResponseErrorCodeReq(AbstractModel):
    """Error code input parameter

    """

    def __init__(self):
        """
        :param Code: Custom response configuration error code.\n        :type Code: int\n        :param Msg: Custom response configuration error message.\n        :type Msg: str\n        :param Desc: Custom response configuration error code remarks.\n        :type Desc: str\n        :param ConvertedCode: Custom error code conversion.\n        :type ConvertedCode: int\n        :param NeedConvert: Whether to enable error code conversion.\n        :type NeedConvert: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Service(AbstractModel):
    """Service list display

    """

    def __init__(self):
        """
        :param InnerHttpsPort: Port for HTTPS access over private network.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InnerHttpsPort: int\n        :param ServiceDesc: Custom service description.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceDesc: str\n        :param Protocol: Service frontend request type, such as `http`, `https`, and `http&https`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Protocol: str\n        :param ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ModifiedTime: str\n        :param NetTypes: Network types supported by service.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NetTypes: list of str\n        :param ExclusiveSetName: Dedicated cluster name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ExclusiveSetName: str\n        :param ServiceId: Unique service ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceId: str\n        :param IpVersion: IP version.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IpVersion: str\n        :param AvailableEnvironments: List of published environments, such as test, prepub, and release.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AvailableEnvironments: list of str\n        :param ServiceName: Custom service name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceName: str\n        :param OuterSubDomain: Public domain name assigned by the system for this service.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OuterSubDomain: str\n        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreatedTime: str\n        :param InnerHttpPort: Port for HTTP access over private network.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InnerHttpPort: int\n        :param InnerSubDomain: Private domain name automatically assigned by the system for this service.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InnerSubDomain: str\n        :param TradeIsolateStatus: Billing status of service.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TradeIsolateStatus: int\n        :param Tags: Tags bound to a service.
Note: this field may return null, indicating that no valid values found.\n        :type Tags: list of Tag\n        :param InstanceId: Dedicated instance
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InstanceId: str\n        :param SetType: Cluster type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SetType: str\n        """
        self.InnerHttpsPort = None
        self.ServiceDesc = None
        self.Protocol = None
        self.ModifiedTime = None
        self.NetTypes = None
        self.ExclusiveSetName = None
        self.ServiceId = None
        self.IpVersion = None
        self.AvailableEnvironments = None
        self.ServiceName = None
        self.OuterSubDomain = None
        self.CreatedTime = None
        self.InnerHttpPort = None
        self.InnerSubDomain = None
        self.TradeIsolateStatus = None
        self.Tags = None
        self.InstanceId = None
        self.SetType = None


    def _deserialize(self, params):
        self.InnerHttpsPort = params.get("InnerHttpsPort")
        self.ServiceDesc = params.get("ServiceDesc")
        self.Protocol = params.get("Protocol")
        self.ModifiedTime = params.get("ModifiedTime")
        self.NetTypes = params.get("NetTypes")
        self.ExclusiveSetName = params.get("ExclusiveSetName")
        self.ServiceId = params.get("ServiceId")
        self.IpVersion = params.get("IpVersion")
        self.AvailableEnvironments = params.get("AvailableEnvironments")
        self.ServiceName = params.get("ServiceName")
        self.OuterSubDomain = params.get("OuterSubDomain")
        self.CreatedTime = params.get("CreatedTime")
        self.InnerHttpPort = params.get("InnerHttpPort")
        self.InnerSubDomain = params.get("InnerSubDomain")
        self.TradeIsolateStatus = params.get("TradeIsolateStatus")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.SetType = params.get("SetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceConfig(AbstractModel):
    """ServiceConfig

    """

    def __init__(self):
        """
        :param Product: Backend type, which takes effect when VPC is enabled. Currently, only `clb` is supported.\n        :type Product: str\n        :param UniqVpcId: Unique VPC ID.\n        :type UniqVpcId: str\n        :param Url: API backend service URL, which is required if `ServiceType` is `HTTP`.\n        :type Url: str\n        :param Path: API backend service path, such as `/path`, which is required if `ServiceType` is `HTTP`. The frontend and backend paths can be different.\n        :type Path: str\n        :param Method: API backend service request method, such as `GET`, which is required if `ServiceType` is `HTTP`. The frontend and backend methods can be different\n        :type Method: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceEnvironmentSet(AbstractModel):
    """Details of environments bound to service

    """

    def __init__(self):
        """
        :param TotalCount: Total number of environments bound to service.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param EnvironmentList: List of environments bound to service.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EnvironmentList: list of Environment\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceEnvironmentStrategy(AbstractModel):
    """Service environment policy

    """

    def __init__(self):
        """
        :param EnvironmentName: Environment name.\n        :type EnvironmentName: str\n        :param Url: Access service environment URL.\n        :type Url: str\n        :param Status: Release status.\n        :type Status: int\n        :param VersionName: Published version number.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VersionName: str\n        :param Strategy: Throttling value.\n        :type Strategy: int\n        :param MaxStrategy: Maximum quota value
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxStrategy: int\n        """
        self.EnvironmentName = None
        self.Url = None
        self.Status = None
        self.VersionName = None
        self.Strategy = None
        self.MaxStrategy = None


    def _deserialize(self, params):
        self.EnvironmentName = params.get("EnvironmentName")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.VersionName = params.get("VersionName")
        self.Strategy = params.get("Strategy")
        self.MaxStrategy = params.get("MaxStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceEnvironmentStrategyStatus(AbstractModel):
    """List of policies bound to environment

    """

    def __init__(self):
        """
        :param TotalCount: Number of throttling policies.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param EnvironmentList: Throttling policy list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EnvironmentList: list of ServiceEnvironmentStrategy\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceParameter(AbstractModel):
    """ServiceParameter

    """

    def __init__(self):
        """
        :param Name: API backend service parameter name, which is used only if `ServiceType` is `HTTP`. The frontend and backend parameter names can be different.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Name: str\n        :param Position: Position of API backend service parameter, such as `head`, which is used only if `ServiceType` is `HTTP`. The positions of frontend and backend parameters can be different.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Position: str\n        :param RelevantRequestParameterPosition: Position of the API frontend parameter corresponding to the backend service parameter, such as `head`, which is used only if `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RelevantRequestParameterPosition: str\n        :param RelevantRequestParameterName: Name of the API frontend parameter corresponding to the backend service parameter, which is used only if `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RelevantRequestParameterName: str\n        :param DefaultValue: Default value of API backend service parameter, which is used only if `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DefaultValue: str\n        :param RelevantRequestParameterDesc: API backend service parameter remarks, which is used only if `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RelevantRequestParameterDesc: str\n        :param RelevantRequestParameterType: API backend service parameter type, which is used only if `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RelevantRequestParameterType: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceReleaseHistory(AbstractModel):
    """Service release history

    """

    def __init__(self):
        """
        :param TotalCount: Total number of published versions.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param VersionList: Historical version list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VersionList: list of ServiceReleaseHistoryInfo\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceReleaseHistoryInfo(AbstractModel):
    """Service release list details

    """

    def __init__(self):
        """
        :param VersionName: Version ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VersionName: str\n        :param VersionDesc: Version description.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VersionDesc: str\n        :param ReleaseTime: Version release time.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ReleaseTime: str\n        """
        self.VersionName = None
        self.VersionDesc = None
        self.ReleaseTime = None


    def _deserialize(self, params):
        self.VersionName = params.get("VersionName")
        self.VersionDesc = params.get("VersionDesc")
        self.ReleaseTime = params.get("ReleaseTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceReleaseVersion(AbstractModel):
    """Service release version

    """

    def __init__(self):
        """
        :param TotalCount: Total number of published versions.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param VersionList: Release version list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VersionList: list of ServiceReleaseHistoryInfo\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceSubDomainMappings(AbstractModel):
    """Custom service domain name path mapping

    """

    def __init__(self):
        """
        :param IsDefaultMapping: Whether the default path mapping is used. true: use the default path mapping; false: use the custom path mapping (`PathMappingSet` is required in this case).\n        :type IsDefaultMapping: bool\n        :param PathMappingSet: Custom path mapping list.\n        :type PathMappingSet: list of PathMapping\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceUsagePlanSet(AbstractModel):
    """List of usage plans bound to service

    """

    def __init__(self):
        """
        :param TotalCount: Total number of usage plans bound to service.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param ServiceUsagePlanList: List of usage plans bound to service.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceUsagePlanList: list of ApiUsagePlan\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServicesStatus(AbstractModel):
    """Service list display

    """

    def __init__(self):
        """
        :param TotalCount: Total number of services in list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param ServiceSet: Service list details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceSet: list of Service\n        """
        self.TotalCount = None
        self.ServiceSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ServiceSet") is not None:
            self.ServiceSet = []
            for item in params.get("ServiceSet"):
                obj = Service()
                obj._deserialize(item)
                self.ServiceSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Information of tag bound to API.

    """

    def __init__(self):
        """
        :param Key: Tag key.\n        :type Key: str\n        :param Value: Tag value.\n        :type Value: str\n        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetServicesReq(AbstractModel):
    """TSF Serverless input parameters

    """

    def __init__(self):
        """
        :param VmIp: VM IP\n        :type VmIp: str\n        :param VpcId: VPC ID\n        :type VpcId: str\n        :param VmPort: VM Port\n        :type VmPort: int\n        :param HostIp: IP of the host where the CVM instance resides\n        :type HostIp: str\n        :param DockerIp: Docker IP\n        :type DockerIp: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfLoadBalanceConfResp(AbstractModel):
    """`TsfLoadBalanceConf` output parameter usage

    """

    def __init__(self):
        """
        :param IsLoadBalance: Whether load balancing is enabled.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsLoadBalance: bool\n        :param Method: Load balancing method.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Method: str\n        :param SessionStickRequired: Whether session persistence is enabled.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SessionStickRequired: bool\n        :param SessionStickTimeout: Session persistence timeout period.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SessionStickTimeout: int\n        """
        self.IsLoadBalance = None
        self.Method = None
        self.SessionStickRequired = None
        self.SessionStickTimeout = None


    def _deserialize(self, params):
        self.IsLoadBalance = params.get("IsLoadBalance")
        self.Method = params.get("Method")
        self.SessionStickRequired = params.get("SessionStickRequired")
        self.SessionStickTimeout = params.get("SessionStickTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindEnvironmentRequest(AbstractModel):
    """UnBindEnvironment request structure.

    """

    def __init__(self):
        """
        :param BindType: Binding type. Valid values: API, SERVICE. Default value: SERVICE.\n        :type BindType: str\n        :param UsagePlanIds: List of unique IDs of the usage plans to be bound.\n        :type UsagePlanIds: list of str\n        :param Environment: Service environment to be unbound.\n        :type Environment: str\n        :param ServiceId: Unique ID of the service to be unbound.\n        :type ServiceId: str\n        :param ApiIds: Unique API ID array, which is required if `BindType` is `API`.\n        :type ApiIds: list of str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindEnvironmentResponse(AbstractModel):
    """UnBindEnvironment response structure.

    """

    def __init__(self):
        """
        :param Result: Whether unbinding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique ID of the service to be unbound.\n        :type ServiceId: str\n        :param StrategyId: Unique ID of the IP policy to be unbound.\n        :type StrategyId: str\n        :param EnvironmentName: Environment to be unbound.\n        :type EnvironmentName: str\n        :param UnBindApiIds: List of APIs to be unbound.\n        :type UnBindApiIds: list of str\n        """
        self.ServiceId = None
        self.StrategyId = None
        self.EnvironmentName = None
        self.UnBindApiIds = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyId = params.get("StrategyId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.UnBindApiIds = params.get("UnBindApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindIPStrategyResponse(AbstractModel):
    """UnBindIPStrategy response structure.

    """

    def __init__(self):
        """
        :param Result: Whether unbinding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param UsagePlanId: Unique ID of the usage plan to be unbound.\n        :type UsagePlanId: str\n        :param AccessKeyIds: Array of IDs of the keys to be unbound.\n        :type AccessKeyIds: list of str\n        """
        self.UsagePlanId = None
        self.AccessKeyIds = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.AccessKeyIds = params.get("AccessKeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindSecretIdsResponse(AbstractModel):
    """UnBindSecretIds response structure.

    """

    def __init__(self):
        """
        :param Result: Whether unbinding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique service ID.\n        :type ServiceId: str\n        :param SubDomain: Custom domain name to be unbound.\n        :type SubDomain: str\n        """
        self.ServiceId = None
        self.SubDomain = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.SubDomain = params.get("SubDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindSubDomainResponse(AbstractModel):
    """UnBindSubDomain response structure.

    """

    def __init__(self):
        """
        :param Result: Whether the custom domain name is successfully unbound.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique ID of the service to be deactivated.\n        :type ServiceId: str\n        :param EnvironmentName: Name of the environment to be deactivated. Valid values: test (test environment), prepub (pre-release environment), release (release environment).\n        :type EnvironmentName: str\n        :param ApiIds: List of APIs to be deactivated, which is a reserved field.\n        :type ApiIds: list of str\n        """
        self.ServiceId = None
        self.EnvironmentName = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnReleaseServiceResponse(AbstractModel):
    """UnReleaseService response structure.

    """

    def __init__(self):
        """
        :param Result: Whether deactivation succeeded.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param AccessKeyId: ID of the key to be changed.\n        :type AccessKeyId: str\n        :param AccessKeySecret: Key to be updated, which is required when a custom key is updated. It can contain 10–50 letters, digits, and underscores.\n        :type AccessKeySecret: str\n        """
        self.AccessKeyId = None
        self.AccessKeySecret = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        self.AccessKeySecret = params.get("AccessKeySecret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApiKeyResponse(AbstractModel):
    """UpdateApiKey response structure.

    """

    def __init__(self):
        """
        :param Result: Key details after change.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceId: Unique ID of the service to be switch.\n        :type ServiceId: str\n        :param EnvironmentName: Name of the environment to be switched to. Valid values: test (test environment), prepub (pre-release environment), release (release environment).\n        :type EnvironmentName: str\n        :param VersionName: Number of the version to be switched to.\n        :type VersionName: str\n        :param UpdateDesc: Switch description.\n        :type UpdateDesc: str\n        """
        self.ServiceId = None
        self.EnvironmentName = None
        self.VersionName = None
        self.UpdateDesc = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.VersionName = params.get("VersionName")
        self.UpdateDesc = params.get("UpdateDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateServiceResponse(AbstractModel):
    """UpdateService response structure.

    """

    def __init__(self):
        """
        :param Result: Whether the version is successfully switched.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Environment: Environment name.\n        :type Environment: str\n        :param UsagePlanId: Unique usage plan ID.\n        :type UsagePlanId: str\n        :param UsagePlanName: Usage plan name.\n        :type UsagePlanName: str\n        :param UsagePlanDesc: Usage plan description.\n        :type UsagePlanDesc: str\n        :param MaxRequestNumPreSec: Usage plan QPS. `-1` indicates no limit.\n        :type MaxRequestNumPreSec: int\n        :param CreatedTime: Usage plan time.\n        :type CreatedTime: str\n        :param ModifiedTime: Usage plan modification time.\n        :type ModifiedTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanBindEnvironment(AbstractModel):
    """Information of environment bound to usage plan

    """

    def __init__(self):
        """
        :param EnvironmentName: Environment name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EnvironmentName: str\n        :param ServiceId: Unique service ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceId: str\n        """
        self.EnvironmentName = None
        self.ServiceId = None


    def _deserialize(self, params):
        self.EnvironmentName = params.get("EnvironmentName")
        self.ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanBindSecret(AbstractModel):
    """Key bound to usage plan

    """

    def __init__(self):
        """
        :param AccessKeyId: Key ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AccessKeyId: str\n        :param SecretName: Key name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SecretName: str\n        :param Status: Key status. 0: disabled. 1: enabled.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Status: int\n        """
        self.AccessKeyId = None
        self.SecretName = None
        self.Status = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        self.SecretName = params.get("SecretName")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanBindSecretStatus(AbstractModel):
    """List of keys bound to usage plan.

    """

    def __init__(self):
        """
        :param TotalCount: Number of keys bound to usage plan.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param AccessKeyList: List of key details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AccessKeyList: list of UsagePlanBindSecret\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanEnvironment(AbstractModel):
    """Details of environments bound to usage plan.

    """

    def __init__(self):
        """
        :param ServiceId: Unique ID of bound service.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceId: str\n        :param ApiId: Unique API ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiId: str\n        :param ApiName: API name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiName: str\n        :param Path: API path.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Path: str\n        :param Method: API method.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Method: str\n        :param Environment: Name of bound environment.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Environment: str\n        :param InUseRequestNum: Used quota.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InUseRequestNum: int\n        :param MaxRequestNum: Maximum number of requests.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxRequestNum: int\n        :param MaxRequestNumPreSec: Maximum number of requests per second.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxRequestNumPreSec: int\n        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreatedTime: str\n        :param ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ModifiedTime: str\n        :param ServiceName: Service name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanEnvironmentStatus(AbstractModel):
    """List of environments bound to usage plan.

    """

    def __init__(self):
        """
        :param TotalCount: Number of environments of the service bound to usage plan.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param EnvironmentList: Environment status of services bound to usage plan.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EnvironmentList: list of UsagePlanEnvironment\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanInfo(AbstractModel):
    """Usage plan details.

    """

    def __init__(self):
        """
        :param UsagePlanId: Unique usage plan ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UsagePlanId: str\n        :param UsagePlanName: Usage plan name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UsagePlanName: str\n        :param UsagePlanDesc: Usage plan description.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UsagePlanDesc: str\n        :param InitQuota: Number of initialization calls.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InitQuota: int\n        :param MaxRequestNumPreSec: Limit of requests per second.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxRequestNumPreSec: int\n        :param MaxRequestNum: Maximum number of calls.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxRequestNum: int\n        :param IsHide: Whether to hide.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsHide: int\n        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreatedTime: str\n        :param ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ModifiedTime: str\n        :param BindSecretIdTotalCount: Number of bound keys.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BindSecretIdTotalCount: int\n        :param BindSecretIds: Details of bound keys.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BindSecretIds: list of str\n        :param BindEnvironmentTotalCount: Number of bound environments.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BindEnvironmentTotalCount: int\n        :param BindEnvironments: Details of bound environments.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BindEnvironments: list of UsagePlanBindEnvironment\n        """
        self.UsagePlanId = None
        self.UsagePlanName = None
        self.UsagePlanDesc = None
        self.InitQuota = None
        self.MaxRequestNumPreSec = None
        self.MaxRequestNum = None
        self.IsHide = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.BindSecretIdTotalCount = None
        self.BindSecretIds = None
        self.BindEnvironmentTotalCount = None
        self.BindEnvironments = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.UsagePlanName = params.get("UsagePlanName")
        self.UsagePlanDesc = params.get("UsagePlanDesc")
        self.InitQuota = params.get("InitQuota")
        self.MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self.MaxRequestNum = params.get("MaxRequestNum")
        self.IsHide = params.get("IsHide")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.BindSecretIdTotalCount = params.get("BindSecretIdTotalCount")
        self.BindSecretIds = params.get("BindSecretIds")
        self.BindEnvironmentTotalCount = params.get("BindEnvironmentTotalCount")
        if params.get("BindEnvironments") is not None:
            self.BindEnvironments = []
            for item in params.get("BindEnvironments"):
                obj = UsagePlanBindEnvironment()
                obj._deserialize(item)
                self.BindEnvironments.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanStatusInfo(AbstractModel):
    """Usage plan list display.

    """

    def __init__(self):
        """
        :param UsagePlanId: Unique usage plan ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UsagePlanId: str\n        :param UsagePlanName: Custom usage plan name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UsagePlanName: str\n        :param UsagePlanDesc: Custom usage plan description.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UsagePlanDesc: str\n        :param MaxRequestNumPreSec: Maximum number of requests per second.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxRequestNumPreSec: int\n        :param MaxRequestNum: Total number of requests allowed. `-1` indicates no limit.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxRequestNum: int\n        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreatedTime: str\n        :param ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ModifiedTime: str\n        """
        self.UsagePlanId = None
        self.UsagePlanName = None
        self.UsagePlanDesc = None
        self.MaxRequestNumPreSec = None
        self.MaxRequestNum = None
        self.CreatedTime = None
        self.ModifiedTime = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.UsagePlanName = params.get("UsagePlanName")
        self.UsagePlanDesc = params.get("UsagePlanDesc")
        self.MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self.MaxRequestNum = params.get("MaxRequestNum")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlansStatus(AbstractModel):
    """Usage plan list

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible usage plans.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param UsagePlanStatusSet: Usage plan list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UsagePlanStatusSet: list of UsagePlanStatusInfo\n        """
        self.TotalCount = None
        self.UsagePlanStatusSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UsagePlanStatusSet") is not None:
            self.UsagePlanStatusSet = []
            for item in params.get("UsagePlanStatusSet"):
                obj = UsagePlanStatusInfo()
                obj._deserialize(item)
                self.UsagePlanStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        