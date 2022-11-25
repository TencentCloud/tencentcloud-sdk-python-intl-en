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
        r"""
        :param ApiDocId: API document ID
        :type ApiDocId: str
        :param ApiDocName: API document name
        :type ApiDocName: str
        :param ApiDocStatus: API document build status
        :type ApiDocStatus: str
        """
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
        r"""
        :param ApiDocId: API document ID
        :type ApiDocId: str
        :param ApiDocName: API document name
        :type ApiDocName: str
        :param ApiDocStatus: API document build status
        :type ApiDocStatus: str
        :param ApiCount: Number of APIs with API documents
        :type ApiCount: int
        :param ViewCount: Number of views of API document
        :type ViewCount: int
        :param ReleaseCount: Number of releases of API document
        :type ReleaseCount: int
        :param ApiDocUri: API document access URI
        :type ApiDocUri: str
        :param SharePassword: API document password for sharing
        :type SharePassword: str
        :param UpdatedTime: API document update time
        :type UpdatedTime: str
        :param ServiceId: Service ID
        :type ServiceId: str
        :param Environment: Environment information
        :type Environment: str
        :param ApiIds: ID of the API for which to generate the API document
        :type ApiIds: list of str
        :param ServiceName: Service name
        :type ServiceName: str
        :param ApiNames: Name of the API for which to generate the API document
        :type ApiNames: list of str
        """
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
        r"""
        :param TotalCount: Number of API documents
        :type TotalCount: int
        :param APIDocSet: Basic information of API document
        :type APIDocSet: list of APIDoc
        """
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
        


class ApiAppApiInfo(AbstractModel):
    """Information of the API bound to the application

    """

    def __init__(self):
        r"""
        :param ApiAppName: Application name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAppName: str
        :param ApiAppId: Application ID
        :type ApiAppId: str
        :param ApiId: API ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiId: str
        :param ApiName: API name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiName: str
        :param ServiceId: Service ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceId: str
        :param AuthorizedTime: Binding authorization time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthorizedTime: str
        :param ApiRegion: API region
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiRegion: str
        :param EnvironmentName: Authorized binding environment
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnvironmentName: str
        """
        self.ApiAppName = None
        self.ApiAppId = None
        self.ApiId = None
        self.ApiName = None
        self.ServiceId = None
        self.AuthorizedTime = None
        self.ApiRegion = None
        self.EnvironmentName = None


    def _deserialize(self, params):
        self.ApiAppName = params.get("ApiAppName")
        self.ApiAppId = params.get("ApiAppId")
        self.ApiId = params.get("ApiId")
        self.ApiName = params.get("ApiName")
        self.ServiceId = params.get("ServiceId")
        self.AuthorizedTime = params.get("AuthorizedTime")
        self.ApiRegion = params.get("ApiRegion")
        self.EnvironmentName = params.get("EnvironmentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiAppApiInfos(AbstractModel):
    """Application information set

    """

    def __init__(self):
        r"""
        :param TotalCount: Quantity
        :type TotalCount: int
        :param ApiAppApiSet: Information array of the API bound to the application
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAppApiSet: list of ApiAppApiInfo
        """
        self.TotalCount = None
        self.ApiAppApiSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiAppApiSet") is not None:
            self.ApiAppApiSet = []
            for item in params.get("ApiAppApiSet"):
                obj = ApiAppApiInfo()
                obj._deserialize(item)
                self.ApiAppApiSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiAppInfo(AbstractModel):
    """Application information

    """

    def __init__(self):
        r"""
        :param ApiAppName: Application name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAppName: str
        :param ApiAppId: Application ID
        :type ApiAppId: str
        :param ApiAppSecret: Application SECRET
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAppSecret: str
        :param ApiAppDesc: Application description
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAppDesc: str
        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param ModifiedTime: Modification time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param ApiAppKey: Application KEY
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAppKey: str
        """
        self.ApiAppName = None
        self.ApiAppId = None
        self.ApiAppSecret = None
        self.ApiAppDesc = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ApiAppKey = None


    def _deserialize(self, params):
        self.ApiAppName = params.get("ApiAppName")
        self.ApiAppId = params.get("ApiAppId")
        self.ApiAppSecret = params.get("ApiAppSecret")
        self.ApiAppDesc = params.get("ApiAppDesc")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ApiAppKey = params.get("ApiAppKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiAppInfos(AbstractModel):
    """Application information set

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of applications
        :type TotalCount: int
        :param ApiAppSet: Application information array
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAppSet: list of ApiAppInfo
        """
        self.TotalCount = None
        self.ApiAppSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiAppSet") is not None:
            self.ApiAppSet = []
            for item in params.get("ApiAppSet"):
                obj = ApiAppInfo()
                obj._deserialize(item)
                self.ApiAppSet.append(obj)
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
        r"""
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
        r"""
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
        r"""
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
        :param IsDebugAfterCharge: Whether to enable debugging after purchase.
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
        r"""
        :param ServiceId: Unique service ID of API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceId: str
        :param ServiceName: Service name of API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceName: str
        :param ServiceDesc: Service description of API.
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
        :param IsDebugAfterCharge: Whether to enable debugging after purchase (reserved field for the marketplace).
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDebugAfterCharge: bool
        :param RequestConfig: Request frontend configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.RequestConfig`
        :param ResponseType: Return type.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseType: str
        :param ResponseSuccessExample: Sample response for successful custom response configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseSuccessExample: str
        :param ResponseFailExample: Sample response for failed custom response configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseFailExample: str
        :param ResponseErrorCodes: Custom error code configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseErrorCodes: list of ErrorCodes
        :param RequestParameters: Frontend request parameter.
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
        :param ServiceParameters: API backend service parameter.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceParameters: list of ServiceParameter
        :param ConstantParameters: Constant parameter.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ConstantParameters: list of ConstantParameter
        :param ServiceMockReturnMessage: Returned message of API backend Mock, which is required if `ServiceType` is `Mock`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceMockReturnMessage: str
        :param ServiceScfFunctionName: SCF function name, which takes effect if the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceScfFunctionName: str
        :param ServiceScfFunctionNamespace: SCF function namespace, which takes effect if the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceScfFunctionNamespace: str
        :param ServiceScfFunctionQualifier: SCF function version, which takes effect if the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceScfFunctionQualifier: str
        :param ServiceScfIsIntegratedResponse: Whether integrated response is enabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceScfIsIntegratedResponse: bool
        :param ServiceWebsocketRegisterFunctionName: SCF WebSocket registration function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketRegisterFunctionName: str
        :param ServiceWebsocketRegisterFunctionNamespace: SCF WebSocket registration function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketRegisterFunctionNamespace: str
        :param ServiceWebsocketRegisterFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketRegisterFunctionQualifier: str
        :param ServiceWebsocketCleanupFunctionName: SCF WebSocket cleanup function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketCleanupFunctionName: str
        :param ServiceWebsocketCleanupFunctionNamespace: SCF WebSocket cleanup function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketCleanupFunctionNamespace: str
        :param ServiceWebsocketCleanupFunctionQualifier: SCF WebSocket cleanup function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketCleanupFunctionQualifier: str
        :param InternalDomain: WebSocket callback address.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InternalDomain: str
        :param ServiceWebsocketTransportFunctionName: SCF WebSocket transfer function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketTransportFunctionName: str
        :param ServiceWebsocketTransportFunctionNamespace: SCF WebSocket transfer function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketTransportFunctionNamespace: str
        :param ServiceWebsocketTransportFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketTransportFunctionQualifier: str
        :param MicroServices: List of microservices bound to API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MicroServices: list of MicroService
        :param MicroServicesInfo: Microservice details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MicroServicesInfo: list of int
        :param ServiceTsfLoadBalanceConf: Load balancing configuration of microservice.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`
        :param ServiceTsfHealthCheckConf: Health check configuration of microservice.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param EnableCORS: Whether to enable CORS.
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnableCORS: bool
        :param Tags: Information of tags bound to API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param Environments: Environment information published for API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Environments: list of str
        :param IsBase64Encoded: Whether to enable Base64 encoding. This parameter takes effect only when the backend is SCF.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsBase64Encoded: bool
        :param IsBase64Trigger: Whether to trigger Base64 encoding by header. This parameter takes effect only when the backend is SCF.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsBase64Trigger: bool
        :param Base64EncodedTriggerRules: Header trigger rules. The number of rules cannot exceed 10.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Base64EncodedTriggerRules: list of Base64EncodedTriggerRule
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
        


class ApiInfoSummary(AbstractModel):
    """Information of the APIs that can use this plugin

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of APIs that can use this plugin
        :type TotalCount: int
        :param ApiSet: Information of the APIs that can use this plugin
        :type ApiSet: list of AvailableApiInfo
        """
        self.TotalCount = None
        self.ApiSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiSet") is not None:
            self.ApiSet = []
            for item in params.get("ApiSet"):
                obj = AvailableApiInfo()
                obj._deserialize(item)
                self.ApiSet.append(obj)
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
        r"""
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
        r"""
        :param TotalCount: Number of eligible API keys.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param ApiKeySet: API key list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiKeySet: list of ApiKey
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param TotalCount: Number of eligible APIs.
        :type TotalCount: int
        :param ApiIdStatusSet: API list.
        :type ApiIdStatusSet: list of DesApisStatus
        """
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
        


class AttachPluginRequest(AbstractModel):
    """AttachPlugin request structure.

    """

    def __init__(self):
        r"""
        :param PluginId: ID of the plugin to be bound
        :type PluginId: str
        :param ServiceId: Service ID
        :type ServiceId: str
        :param EnvironmentName: API environment
        :type EnvironmentName: str
        :param ApiIds: List of APIs bound with the plugin
        :type ApiIds: list of str
        """
        self.PluginId = None
        self.ServiceId = None
        self.EnvironmentName = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachPluginResponse(AbstractModel):
    """AttachPlugin response structure.

    """

    def __init__(self):
        r"""
        :param Result: Whether binding succeeded.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class AttachedApiInfo(AbstractModel):
    """Information of the API bound with the plugin

    """

    def __init__(self):
        r"""
        :param ServiceId: ID of the service to which the API belongs
        :type ServiceId: str
        :param ServiceName: Name of the service to which the API belongs
        :type ServiceName: str
        :param ServiceDesc: Description of the service to which the API belongs
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceDesc: str
        :param ApiId: API ID
        :type ApiId: str
        :param ApiName: API name
        :type ApiName: str
        :param ApiDesc: API description
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiDesc: str
        :param Environment: Environment of the API bound with the plugin
        :type Environment: str
        :param AttachedTime: Time when the plugin was bound to the API
        :type AttachedTime: str
        """
        self.ServiceId = None
        self.ServiceName = None
        self.ServiceDesc = None
        self.ApiId = None
        self.ApiName = None
        self.ApiDesc = None
        self.Environment = None
        self.AttachedTime = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceName = params.get("ServiceName")
        self.ServiceDesc = params.get("ServiceDesc")
        self.ApiId = params.get("ApiId")
        self.ApiName = params.get("ApiName")
        self.ApiDesc = params.get("ApiDesc")
        self.Environment = params.get("Environment")
        self.AttachedTime = params.get("AttachedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedApiSummary(AbstractModel):
    """List of APIs bound with the plugin

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of APIs bound with the plugin
        :type TotalCount: int
        :param AttachedApis: Information of the API bound with the plugin
        :type AttachedApis: list of AttachedApiInfo
        """
        self.TotalCount = None
        self.AttachedApis = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AttachedApis") is not None:
            self.AttachedApis = []
            for item in params.get("AttachedApis"):
                obj = AttachedApiInfo()
                obj._deserialize(item)
                self.AttachedApis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedPluginInfo(AbstractModel):
    """Information of bound plug-ins

    """

    def __init__(self):
        r"""
        :param PluginId: Plugin ID
        :type PluginId: str
        :param Environment: Environment information
        :type Environment: str
        :param AttachedTime: Binding time
        :type AttachedTime: str
        :param PluginName: Plugin name
        :type PluginName: str
        :param PluginType: Plugin type
        :type PluginType: str
        :param Description: Plugin description
        :type Description: str
        :param PluginData: Plugin definition statement
        :type PluginData: str
        """
        self.PluginId = None
        self.Environment = None
        self.AttachedTime = None
        self.PluginName = None
        self.PluginType = None
        self.Description = None
        self.PluginData = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        self.Environment = params.get("Environment")
        self.AttachedTime = params.get("AttachedTime")
        self.PluginName = params.get("PluginName")
        self.PluginType = params.get("PluginType")
        self.Description = params.get("Description")
        self.PluginData = params.get("PluginData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedPluginSummary(AbstractModel):
    """Information of bound plug-ins

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of bound plug-ins
        :type TotalCount: int
        :param PluginSummary: Information of bound plug-ins
        :type PluginSummary: list of AttachedPluginInfo
        """
        self.TotalCount = None
        self.PluginSummary = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PluginSummary") is not None:
            self.PluginSummary = []
            for item in params.get("PluginSummary"):
                obj = AttachedPluginInfo()
                obj._deserialize(item)
                self.PluginSummary.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableApiInfo(AbstractModel):
    """Information of the APIs that can use this plugin

    """

    def __init__(self):
        r"""
        :param ApiId: API ID
        :type ApiId: str
        :param ApiName: API name
        :type ApiName: str
        :param ApiType: API type
        :type ApiType: str
        :param Path: API path
        :type Path: str
        :param Method: API method
        :type Method: str
        :param AttachedOtherPlugin: Whether the API is bound with another plugin
Note: this field may return null, indicating that no valid values can be obtained.
        :type AttachedOtherPlugin: bool
        :param IsAttached: Whether the API is bound with the current plugin
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsAttached: bool
        """
        self.ApiId = None
        self.ApiName = None
        self.ApiType = None
        self.Path = None
        self.Method = None
        self.AttachedOtherPlugin = None
        self.IsAttached = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.ApiName = params.get("ApiName")
        self.ApiType = params.get("ApiType")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.AttachedOtherPlugin = params.get("AttachedOtherPlugin")
        self.IsAttached = params.get("IsAttached")
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
        r"""
        :param Name: Header for triggering encoding. Valid values are `Accept` and `Content_Type`, corresponding to the `Accept` and `Content-Type` headers in the data stream request, respectively.
        :type Name: str
        :param Value: Array of header values that can trigger the encoding. Each element in the array can be up to 40 characters, including digits, letters, and special characters (`.`, `+`, `*`, `-`, `/`, and `_`). 

For example, [
    "application/x-vpeg005",
    "application/xhtml+xml",
    "application/vnd.ms-project",
    "application/vnd.rn-rn_music_package"
] are valid.
        :type Value: list of str
        """
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
        


class BindApiAppRequest(AbstractModel):
    """BindApiApp request structure.

    """

    def __init__(self):
        r"""
        :param ApiAppId: Unique ID of the application to be bound.
        :type ApiAppId: str
        :param Environment: Environment to be bound.
        :type Environment: str
        :param ServiceId: Unique ID of the service to be bound.
        :type ServiceId: str
        :param ApiId: Unique ID of the API to be bound.
        :type ApiId: str
        """
        self.ApiAppId = None
        self.Environment = None
        self.ServiceId = None
        self.ApiId = None


    def _deserialize(self, params):
        self.ApiAppId = params.get("ApiAppId")
        self.Environment = params.get("Environment")
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindApiAppResponse(AbstractModel):
    """BindApiApp response structure.

    """

    def __init__(self):
        r"""
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


class BindApiInfo(AbstractModel):
    """Information of the API bound with the upstream

    """

    def __init__(self):
        r"""
        :param ApiId: Unique API ID.
        :type ApiId: str
        :param ServiceId: Unique ID of the service
        :type ServiceId: str
        :param ApiName: API name
Note: This field may return `null`, indicating that no valid value was found.
        :type ApiName: str
        :param ServiceName: Service name
Note: This field may return `null`, indicating that no valid value was found.
        :type ServiceName: str
        :param BindTime: Bound At
        :type BindTime: str
        """
        self.ApiId = None
        self.ServiceId = None
        self.ApiName = None
        self.ServiceName = None
        self.BindTime = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.ServiceId = params.get("ServiceId")
        self.ApiName = params.get("ApiName")
        self.ServiceName = params.get("ServiceName")
        self.BindTime = params.get("BindTime")
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
        r"""
        :param UsagePlanIds: List of unique IDs of the usage plans to be bound.
        :type UsagePlanIds: list of str
        :param BindType: Binding type. Valid values: API, SERVICE. Default value: SERVICE.
        :type BindType: str
        :param Environment: Environment to be bound.
        :type Environment: str
        :param ServiceId: Unique ID of the service to be bound.
        :type ServiceId: str
        :param ApiIds: Unique API ID array, which is required if `bindType` is `API`.
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
        r"""
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
        r"""
        :param ServiceId: Unique service ID of the IP policy to be bound.
        :type ServiceId: str
        :param StrategyId: Unique ID of the IP policy to be bound.
        :type StrategyId: str
        :param EnvironmentName: Environment to be bound to IP policy.
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param SubDomain: Custom domain name to be bound.
        :type SubDomain: str
        :param Protocol: Protocol supported by service. Valid values: http, https, http&https.
        :type Protocol: str
        :param NetType: Network type. Valid values: OUTER, INNER.
        :type NetType: str
        :param IsDefaultMapping: Whether the default path mapping is used. The default value is `true`. If the value is `false`, the custom path mapping will be used and `PathMappingSet` will be required in this case.
        :type IsDefaultMapping: bool
        :param NetSubDomain: Default domain name.
        :type NetSubDomain: str
        :param CertificateId: Unique certificate ID of the custom domain name to be bound. The certificate can be uploaded if `Protocol` is `https` or `http&https`.
        :type CertificateId: str
        :param PathMappingSet: Custom domain name path mapping. It can contain up to 3 `Environment` values which can be set to only `test`, `prepub`, and `release`, respectively.
        :type PathMappingSet: list of PathMapping
        :param IsForcedHttps: Whether to force HTTP requests to redirect to HTTPS. Default value: `false`. When this parameter is `true`, API Gateway will redirect all requests using the custom domain name over the HTTP protocol to the HTTPS protocol for forwarding.
        :type IsForcedHttps: bool
        """
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
        r"""
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


class BuildAPIDocRequest(AbstractModel):
    """BuildAPIDoc request structure.

    """

    def __init__(self):
        r"""
        :param ApiDocId: API document ID
        :type ApiDocId: str
        """
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
        r"""
        :param Result: Whether the operation succeeded
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ConstantParameter(AbstractModel):
    """Constant parameter

    """

    def __init__(self):
        r"""
        :param Name: Constant parameter name, which is used only if `ServiceType` is `HTTP`.
        :type Name: str
        :param Desc: Constant parameter description, which is used only if `ServiceType` is `HTTP`.
        :type Desc: str
        :param Position: Constant parameter position, which is used only if `ServiceType` is `HTTP`.
        :type Position: str
        :param DefaultValue: Default value of constant parameter, which is used only if `ServiceType` is `HTTP`.
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosConfig(AbstractModel):
    """COS-type API configuration

    """

    def __init__(self):
        r"""
        :param Action: Specifies how the backend COS bucket is called by the API. The frontend request method and Action can be:
GET：GetObject
PUT：PutObject
POST：PostObject、AppendObject
HEAD： HeadObject
DELETE： DeleteObject
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Action: str
        :param BucketName: Backend COS bucket of the API
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BucketName: str
        :param Authorization: Whether to enable the backend COS signature for the API. It defaults to `false`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Authorization: bool
        :param PathMatchMode: The path matching mode of the backend COS service
`BackEndPath`: Match the backend path
`FullPath`: Match the full path

Default: `BackEndPath`
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PathMatchMode: str
        """
        self.Action = None
        self.BucketName = None
        self.Authorization = None
        self.PathMatchMode = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.BucketName = params.get("BucketName")
        self.Authorization = params.get("Authorization")
        self.PathMatchMode = params.get("PathMatchMode")
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
        r"""
        :param ApiDocName: API document name
        :type ApiDocName: str
        :param ServiceId: Service name
        :type ServiceId: str
        :param Environment: Environment name
        :type Environment: str
        :param ApiIds: List of APIs for which to generate documents
        :type ApiIds: list of str
        """
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
        r"""
        :param Result: Basic information of API document
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = APIDoc()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateApiAppRequest(AbstractModel):
    """CreateApiApp request structure.

    """

    def __init__(self):
        r"""
        :param ApiAppName: Custom application name.
        :type ApiAppName: str
        :param ApiAppDesc: Application description
        :type ApiAppDesc: str
        """
        self.ApiAppName = None
        self.ApiAppDesc = None


    def _deserialize(self, params):
        self.ApiAppName = params.get("ApiAppName")
        self.ApiAppDesc = params.get("ApiAppDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiAppResponse(AbstractModel):
    """CreateApiApp response structure.

    """

    def __init__(self):
        r"""
        :param Result: New application details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiAppInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateApiKeyRequest(AbstractModel):
    """CreateApiKey request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Custom key name.
        :type SecretName: str
        :param AccessKeyType: Key type. Valid values: auto, manual (custom key). Default value: auto.
        :type AccessKeyType: str
        :param AccessKeyId: Custom key ID, which is required if `AccessKeyType` is `manual`. It can contain 5–50 letters, digits, and underscores.
        :type AccessKeyId: str
        :param AccessKeySecret: Custom key, which is required if `AccessKeyType` is `manual`. It can contain 10–50 letters, digits, and underscores.
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
        r"""
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
        r"""
        :param ServiceId: Unique service ID of API.
        :type ServiceId: str
        :param ServiceType: API backend service type. Valid values: HTTP, MOCK, TSF, SCF, WEBSOCKET, TARGET (in beta test).
        :type ServiceType: str
        :param ServiceTimeout: API backend service timeout period in seconds.
        :type ServiceTimeout: int
        :param Protocol: API frontend request protocol. Valid values: HTTPS, WEBSOCKET.
        :type Protocol: str
        :param RequestConfig: Request frontend configuration.
        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.ApiRequestConfig`
        :param ApiName: Custom API name.
        :type ApiName: str
        :param ApiDesc: Custom API description.
        :type ApiDesc: str
        :param ApiType: API type. Valid values: NORMAL (general API), TSF (microservice API). Default value: NORMAL.
        :type ApiType: str
        :param AuthType: API authentication type. Valid values: SECRET (key pair authentication), NONE (no authentication), OAUTH, APP (application authentication). Default value: NONE.
        :type AuthType: str
        :param EnableCORS: Whether to enable CORS.
        :type EnableCORS: bool
        :param ConstantParameters: Constant parameter.
        :type ConstantParameters: list of ConstantParameter
        :param RequestParameters: Frontend request parameter.
        :type RequestParameters: list of RequestParameter
        :param ApiBusinessType: This field is valid if `AuthType` is `OAUTH`. NORMAL: business API; OAUTH: authorization API.
        :type ApiBusinessType: str
        :param ServiceMockReturnMessage: Returned message of API backend Mock, which is required if `ServiceType` is `Mock`.
        :type ServiceMockReturnMessage: str
        :param MicroServices: List of microservices bound to API.
        :type MicroServices: list of MicroServiceReq
        :param ServiceTsfLoadBalanceConf: Load balancing configuration of microservice.
        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`
        :param ServiceTsfHealthCheckConf: Health check configuration of microservice.
        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param TargetServices: `target` type backend resource information (in beta test).
        :type TargetServices: list of TargetServicesReq
        :param TargetServicesLoadBalanceConf: `target` type load balancing configuration (in beta test).
        :type TargetServicesLoadBalanceConf: int
        :param TargetServicesHealthCheckConf: `target` health check configuration (in beta test).
        :type TargetServicesHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param ServiceScfFunctionName: SCF function name, which takes effect if the backend type is `SCF`.
        :type ServiceScfFunctionName: str
        :param ServiceWebsocketRegisterFunctionName: SCF WebSocket registration function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionName: str
        :param ServiceWebsocketCleanupFunctionName: SCF WebSocket cleanup function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionName: str
        :param ServiceWebsocketTransportFunctionName: SCF WebSocket transfer function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionName: str
        :param ServiceScfFunctionNamespace: SCF function namespace, which takes effect if the backend type is `SCF`.
        :type ServiceScfFunctionNamespace: str
        :param ServiceScfFunctionQualifier: SCF function version, which takes effect if the backend type is `SCF`.
        :type ServiceScfFunctionQualifier: str
        :param ServiceWebsocketRegisterFunctionNamespace: SCF WebSocket registration function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionNamespace: str
        :param ServiceWebsocketRegisterFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionQualifier: str
        :param ServiceWebsocketTransportFunctionNamespace: SCF WebSocket transfer function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionNamespace: str
        :param ServiceWebsocketTransportFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionQualifier: str
        :param ServiceWebsocketCleanupFunctionNamespace: SCF WebSocket cleanup function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionNamespace: str
        :param ServiceWebsocketCleanupFunctionQualifier: SCF WebSocket cleanup function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionQualifier: str
        :param ServiceScfIsIntegratedResponse: Whether to enable response integration, which takes effect if the backend type is `SCF`.
        :type ServiceScfIsIntegratedResponse: bool
        :param IsDebugAfterCharge: Billing after debugging starts (reserved field for marketplace).
        :type IsDebugAfterCharge: bool
        :param IsDeleteResponseErrorCodes: Whether to delete the error codes for custom response configuration. If the value is left empty or `False`, the error codes will not be deleted. If the value is `True`, all custom response configuration error codes of the API will be deleted.
        :type IsDeleteResponseErrorCodes: bool
        :param ResponseType: Return type.
        :type ResponseType: str
        :param ResponseSuccessExample: Sample response for successful custom response configuration.
        :type ResponseSuccessExample: str
        :param ResponseFailExample: Sample response for failed custom response configuration.
        :type ResponseFailExample: str
        :param ServiceConfig: API backend service configuration.
        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`
        :param AuthRelationApiId: Unique ID of associated authorization API, which takes effect only if `AuthType` is `OAUTH` and `ApiBusinessType` is `NORMAL`. It is the unique ID of the OAuth 2.0 authorization API bound to the business API.
        :type AuthRelationApiId: str
        :param ServiceParameters: API backend service parameter.
        :type ServiceParameters: list of ServiceParameter
        :param OauthConfig: OAuth configuration, which takes effect if `AuthType` is `OAUTH`.
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param ResponseErrorCodes: Custom error code configuration.
        :type ResponseErrorCodes: list of ResponseErrorCodeReq
        :param TargetNamespaceId: TSF Serverless namespace ID (in beta test).
        :type TargetNamespaceId: str
        :param UserType: User type.
        :type UserType: str
        :param IsBase64Encoded: Whether to enable Base64 encoding. This parameter takes effect only when the backend is SCF.
        :type IsBase64Encoded: bool
        :param EventBusId: Event bus ID.
        :type EventBusId: str
        :param ServiceScfFunctionType: SCF function type, which takes effect if the backend type is `SCF`. Valid values: `EVENT` and `HTTP`.
        :type ServiceScfFunctionType: str
        :param EIAMAppType: EIAM application type.
        :type EIAMAppType: str
        :param EIAMAuthType: EIAM application authentication type. Valid values: `AuthenticationOnly`, `Authentication`, `Authorization`.
        :type EIAMAuthType: str
        :param TokenTimeout: Validity of the EIAM application token. Unit: second. Default value: `7200`.
        :type TokenTimeout: int
        :param EIAMAppId: EIAM application ID.
        :type EIAMAppId: str
        :param Owner: Owner of the resource
        :type Owner: str
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
        self.IsBase64Encoded = None
        self.EventBusId = None
        self.ServiceScfFunctionType = None
        self.EIAMAppType = None
        self.EIAMAuthType = None
        self.TokenTimeout = None
        self.EIAMAppId = None
        self.Owner = None


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
        self.EventBusId = params.get("EventBusId")
        self.ServiceScfFunctionType = params.get("ServiceScfFunctionType")
        self.EIAMAppType = params.get("EIAMAppType")
        self.EIAMAuthType = params.get("EIAMAuthType")
        self.TokenTimeout = params.get("TokenTimeout")
        self.EIAMAppId = params.get("EIAMAppId")
        self.Owner = params.get("Owner")
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
        r"""
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
    """Return of API creation

    """

    def __init__(self):
        r"""
        :param ApiId: API ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiId: str
        :param Path: Path
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Path: str
        :param Method: Request method
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Method: str
        :param CreatedTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param Status: Status of the import task
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Status: str
        :param ErrMsg: Details of the error
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ErrMsg: str
        :param ApiName: API name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApiName: str
        """
        self.ApiId = None
        self.Path = None
        self.Method = None
        self.CreatedTime = None
        self.Status = None
        self.ErrMsg = None
        self.ApiName = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.CreatedTime = params.get("CreatedTime")
        self.Status = params.get("Status")
        self.ErrMsg = params.get("ErrMsg")
        self.ApiName = params.get("ApiName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiRspSet(AbstractModel):
    """Information of the APIs created

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of APIs
        :type TotalCount: int
        :param ApiSet: Information of created APIs
        :type ApiSet: list of CreateApiRsp
        """
        self.TotalCount = None
        self.ApiSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiSet") is not None:
            self.ApiSet = []
            for item in params.get("ApiSet"):
                obj = CreateApiRsp()
                obj._deserialize(item)
                self.ApiSet.append(obj)
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
        r"""
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param StrategyName: Custom policy name.
        :type StrategyName: str
        :param StrategyType: Policy type. Valid values: WHITE (allowlist), BLACK (blocklist).
        :type StrategyType: str
        :param StrategyData: Policy details. Multiple IPs are separated with \n.
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
        r"""
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


class CreatePluginRequest(AbstractModel):
    """CreatePlugin request structure.

    """

    def __init__(self):
        r"""
        :param PluginName: Custom plugin name. A plugin name should contain 2-50 characters out of a-z, A-Z, 0-9, and _, which must begin with a letter and end with a letter or a number.
        :type PluginName: str
        :param PluginType: Plugin type. Valid values: `IPControl`, `TrafficControl`, `Cors`, `CustomReq`, `CustomAuth`, `Routing`, `TrafficControlByParameter`, `CircuitBreaker`, `ProxyCache`
        :type PluginType: str
        :param PluginData: Plugin definition statement in json format
        :type PluginData: str
        :param Description: Plugin description within 200 characters
        :type Description: str
        :param Tags: Label
        :type Tags: list of Tag
        """
        self.PluginName = None
        self.PluginType = None
        self.PluginData = None
        self.Description = None
        self.Tags = None


    def _deserialize(self, params):
        self.PluginName = params.get("PluginName")
        self.PluginType = params.get("PluginType")
        self.PluginData = params.get("PluginData")
        self.Description = params.get("Description")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePluginResponse(AbstractModel):
    """CreatePlugin response structure.

    """

    def __init__(self):
        r"""
        :param Result: Details of the new plugin
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.Plugin`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = Plugin()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateServiceRequest(AbstractModel):
    """CreateService request structure.

    """

    def __init__(self):
        r"""
        :param ServiceName: Custom service name.
        :type ServiceName: str
        :param Protocol: Service frontend request type, such as `http`, `https`, and `http&https`.
        :type Protocol: str
        :param ServiceDesc: Custom service description.
        :type ServiceDesc: str
        :param ExclusiveSetName: Dedicated cluster name, which is used to specify the dedicated cluster where the service is to be created.
        :type ExclusiveSetName: str
        :param NetTypes: Network type list, which is used to specify the supported network types. INNER: private network access; OUTER: public network access. Default value: OUTER.
        :type NetTypes: list of str
        :param IpVersion: IP version number. Valid values: IPv4, IPv6. Default value: IPv4.
        :type IpVersion: str
        :param SetServerName: Cluster name, which is reserved and used by the `tsf serverless` type.
        :type SetServerName: str
        :param AppIdType: User type, which is reserved and can be used by `serverless` users.
        :type AppIdType: str
        :param Tags: Tag information.
        :type Tags: list of Tag
        :param InstanceId: Dedicated instance ID
        :type InstanceId: str
        :param UniqVpcId: VPC attribute
        :type UniqVpcId: str
        """
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
        self.UniqVpcId = None


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
        self.UniqVpcId = params.get("UniqVpcId")
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
        r"""
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param ServiceName: Custom service name.
        :type ServiceName: str
        :param ServiceDesc: Custom service description.
        :type ServiceDesc: str
        :param OuterSubDomain: Default public domain name.
        :type OuterSubDomain: str
        :param InnerSubDomain: Default VPC domain name.
        :type InnerSubDomain: str
        :param CreatedTime: Service creation time in the format of `YYYY-MM-DDThh:mm:ssZ` according to ISO 8601 standard. UTC time is used.
        :type CreatedTime: str
        :param NetTypes: Network type list. INNER: private network access; OUTER: public network access.
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


class CreateUpstreamRequest(AbstractModel):
    """CreateUpstream request structure.

    """

    def __init__(self):
        r"""
        :param Scheme: Backend protocol. Valid values: `HTTP`, `HTTPS`
        :type Scheme: str
        :param Algorithm: Load balancing algorithm. Valid value: `ROUND-ROBIN`
        :type Algorithm: str
        :param UniqVpcId: Unique VPC ID
        :type UniqVpcId: str
        :param UpstreamName: Upstream name
        :type UpstreamName: str
        :param UpstreamDescription: Upstream description
        :type UpstreamDescription: str
        :param UpstreamType: Upstream access type. Valid values: `IP_PORT`, `K8S`
        :type UpstreamType: str
        :param Retries: Retry attempts. It defaults to `3`.
        :type Retries: int
        :param UpstreamHost: The Host request header that forwarded from the gateway to backend
        :type UpstreamHost: str
        :param Nodes: Backend nodes
        :type Nodes: list of UpstreamNode
        :param Tags: Label
        :type Tags: list of Tag
        :param HealthChecker: Health check configuration
        :type HealthChecker: :class:`tencentcloud.apigateway.v20180808.models.UpstreamHealthChecker`
        :param K8sService: Configuration of TKE service
        :type K8sService: list of K8sService
        """
        self.Scheme = None
        self.Algorithm = None
        self.UniqVpcId = None
        self.UpstreamName = None
        self.UpstreamDescription = None
        self.UpstreamType = None
        self.Retries = None
        self.UpstreamHost = None
        self.Nodes = None
        self.Tags = None
        self.HealthChecker = None
        self.K8sService = None


    def _deserialize(self, params):
        self.Scheme = params.get("Scheme")
        self.Algorithm = params.get("Algorithm")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UpstreamName = params.get("UpstreamName")
        self.UpstreamDescription = params.get("UpstreamDescription")
        self.UpstreamType = params.get("UpstreamType")
        self.Retries = params.get("Retries")
        self.UpstreamHost = params.get("UpstreamHost")
        if params.get("Nodes") is not None:
            self.Nodes = []
            for item in params.get("Nodes"):
                obj = UpstreamNode()
                obj._deserialize(item)
                self.Nodes.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("HealthChecker") is not None:
            self.HealthChecker = UpstreamHealthChecker()
            self.HealthChecker._deserialize(params.get("HealthChecker"))
        if params.get("K8sService") is not None:
            self.K8sService = []
            for item in params.get("K8sService"):
                obj = K8sService()
                obj._deserialize(item)
                self.K8sService.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUpstreamResponse(AbstractModel):
    """CreateUpstream response structure.

    """

    def __init__(self):
        r"""
        :param UpstreamId: The unique upstream ID returned
Note: This field may return `NULL`, indicating that no valid value was found.
        :type UpstreamId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UpstreamId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UpstreamId = params.get("UpstreamId")
        self.RequestId = params.get("RequestId")


class CreateUsagePlanRequest(AbstractModel):
    """CreateUsagePlan request structure.

    """

    def __init__(self):
        r"""
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
        r"""
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


class DeleteAPIDocRequest(AbstractModel):
    """DeleteAPIDoc request structure.

    """

    def __init__(self):
        r"""
        :param ApiDocId: API document ID
        :type ApiDocId: str
        """
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
        r"""
        :param Result: Whether the operation succeeded
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteApiAppRequest(AbstractModel):
    """DeleteApiApp request structure.

    """

    def __init__(self):
        r"""
        :param ApiAppId: Unique application ID.
        :type ApiAppId: str
        """
        self.ApiAppId = None


    def _deserialize(self, params):
        self.ApiAppId = params.get("ApiAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApiAppResponse(AbstractModel):
    """DeleteApiApp response structure.

    """

    def __init__(self):
        r"""
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


class DeleteApiKeyRequest(AbstractModel):
    """DeleteApiKey request structure.

    """

    def __init__(self):
        r"""
        :param AccessKeyId: ID of the key to be deleted.
        :type AccessKeyId: str
        """
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
        r"""
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
        r"""
        :param ServiceId: Unique service ID of API.
        :type ServiceId: str
        :param ApiId: Unique API ID.
        :type ApiId: str
        """
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
        r"""
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
        r"""
        :param ServiceId: Unique service ID of the IP policy to be deleted.
        :type ServiceId: str
        :param StrategyId: Unique ID of the IP policy to be deleted.
        :type StrategyId: str
        """
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
        r"""
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


class DeletePluginRequest(AbstractModel):
    """DeletePlugin request structure.

    """

    def __init__(self):
        r"""
        :param PluginId: ID of the plugin to be deleted
        :type PluginId: str
        """
        self.PluginId = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePluginResponse(AbstractModel):
    """DeletePlugin response structure.

    """

    def __init__(self):
        r"""
        :param Result: Result of the deletion action
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
        r"""
        :param ServiceId: Unique ID of the service to be deleted.
        :type ServiceId: str
        :param SkipVerification: A parameter used to set to skip the deletion precondition verification (only supported for services on dedicated instances).
        :type SkipVerification: int
        """
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
        r"""
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
        r"""
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param SubDomain: Custom domain name bound to service.
        :type SubDomain: str
        :param Environment: Name of the environment whose mapping is to be deleted. Valid values: test (test environment), prepub (pre-release environment), release (release environment).
        :type Environment: str
        """
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
        r"""
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


class DeleteUpstreamRequest(AbstractModel):
    """DeleteUpstream request structure.

    """

    def __init__(self):
        r"""
        :param UpstreamId: ID of the upstream to be deleted
        :type UpstreamId: str
        """
        self.UpstreamId = None


    def _deserialize(self, params):
        self.UpstreamId = params.get("UpstreamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUpstreamResponse(AbstractModel):
    """DeleteUpstream response structure.

    """

    def __init__(self):
        r"""
        :param UpstreamId: ID of the deleted upstream
Note: This field may return `NULL`, indicating that no valid value was found.
        :type UpstreamId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UpstreamId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UpstreamId = params.get("UpstreamId")
        self.RequestId = params.get("RequestId")


class DeleteUsagePlanRequest(AbstractModel):
    """DeleteUsagePlan request structure.

    """

    def __init__(self):
        r"""
        :param UsagePlanId: Unique ID of the usage plan to be deleted.
        :type UsagePlanId: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param ApiType: API type. Valid values: NORMAL (general API), TSF (microservice API).
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiType: str
        :param Protocol: API protocol.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param IsDebugAfterCharge: Whether to enable debugging after purchase (reserved field for the marketplace)
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDebugAfterCharge: bool
        :param AuthType: API authentication type. Valid values: `SECRET` (key pair authentication), `NONE` (no authentication), `OAUTH`, and `EIAM`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AuthType: str
        :param ApiBusinessType: OAuth API type, which is valid if `AuthType` is `OAUTH`. Valid values: NORMAL (business API), OAUTH (authorization API).
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiBusinessType: str
        :param AuthRelationApiId: Unique ID of associated authorization API, which takes effect only if `AuthType` is `OAUTH` and `ApiBusinessType` is `NORMAL`. It is the unique ID of the OAuth 2.0 authorization API bound to the business API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthRelationApiId: str
        :param OauthConfig: OAuth configuration information, which takes effect if `AuthType` is `OAUTH`.
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
        r"""
        :param ApiDocId: API document ID
        :type ApiDocId: str
        """
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
        r"""
        :param Result: API document details
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDocInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
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
        r"""
        :param Result: API document list information
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDocs`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = APIDocs()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeAllPluginApisRequest(AbstractModel):
    """DescribeAllPluginApis request structure.

    """

    def __init__(self):
        r"""
        :param ServiceId: ID of the service to be queried
        :type ServiceId: str
        :param PluginId: ID of the plugin to be queried
        :type PluginId: str
        :param EnvironmentName: Environment information
        :type EnvironmentName: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100
        :type Limit: int
        :param Offset: Offset. Default value: 0
        :type Offset: int
        """
        self.ServiceId = None
        self.PluginId = None
        self.EnvironmentName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.PluginId = params.get("PluginId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllPluginApisResponse(AbstractModel):
    """DescribeAllPluginApis response structure.

    """

    def __init__(self):
        r"""
        :param Result: List of APIs that ca use this plugin
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiInfoSummary`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiInfoSummary()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiAppBindApisStatusRequest(AbstractModel):
    """DescribeApiAppBindApisStatus request structure.

    """

    def __init__(self):
        r"""
        :param ApiAppId: Application ID
        :type ApiAppId: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter. Valid values: ApiId, ApiName, ServiceId, Environment, KeyWord (match with `name` or ID).
        :type Filters: list of Filter
        """
        self.ApiAppId = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.ApiAppId = params.get("ApiAppId")
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
        


class DescribeApiAppBindApisStatusResponse(AbstractModel):
    """DescribeApiAppBindApisStatus response structure.

    """

    def __init__(self):
        r"""
        :param Result: List of APIs bound to the application.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppApiInfos`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiAppApiInfos()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiAppRequest(AbstractModel):
    """DescribeApiApp request structure.

    """

    def __init__(self):
        r"""
        :param ApiAppId: Application ID.
        :type ApiAppId: str
        """
        self.ApiAppId = None


    def _deserialize(self, params):
        self.ApiAppId = params.get("ApiAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiAppResponse(AbstractModel):
    """DescribeApiApp response structure.

    """

    def __init__(self):
        r"""
        :param Result: Application details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppInfos`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiAppInfos()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiAppsStatusRequest(AbstractModel):
    """DescribeApiAppsStatus request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter. Valid values: ApiAppId, ApiAppName, KeyWord (match with `name` or ID).
        :type Filters: list of Filter
        """
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
        


class DescribeApiAppsStatusResponse(AbstractModel):
    """DescribeApiAppsStatus response structure.

    """

    def __init__(self):
        r"""
        :param Result: Application list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppInfos`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiAppInfos()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiBindApiAppsStatusRequest(AbstractModel):
    """DescribeApiBindApiAppsStatus request structure.

    """

    def __init__(self):
        r"""
        :param ServiceId: Service ID
        :type ServiceId: str
        :param ApiIds: Array of API IDs
        :type ApiIds: list of str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter. Valid values: ApiAppId, Environment, KeyWord (match with `name` or ID).
        :type Filters: list of Filter
        """
        self.ServiceId = None
        self.ApiIds = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiIds = params.get("ApiIds")
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
        


class DescribeApiBindApiAppsStatusResponse(AbstractModel):
    """DescribeApiBindApiAppsStatus response structure.

    """

    def __init__(self):
        r"""
        :param Result: List of APIs bound to the application.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppApiInfos`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiAppApiInfos()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiEnvironmentStrategyRequest(AbstractModel):
    """DescribeApiEnvironmentStrategy request structure.

    """

    def __init__(self):
        r"""
        :param ServiceId: Unique service ID of API.
        :type ServiceId: str
        :param EnvironmentNames: Environment list.
        :type EnvironmentNames: list of str
        :param ApiId: Unique API ID.
        :type ApiId: str
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
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
        r"""
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


class DescribeApiForApiAppRequest(AbstractModel):
    """DescribeApiForApiApp request structure.

    """

    def __init__(self):
        r"""
        :param ServiceId: Unique service ID of the API
        :type ServiceId: str
        :param ApiId: Unique API ID
        :type ApiId: str
        :param ApiRegion: API region
        :type ApiRegion: str
        """
        self.ServiceId = None
        self.ApiId = None
        self.ApiRegion = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        self.ApiRegion = params.get("ApiRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiForApiAppResponse(AbstractModel):
    """DescribeApiForApiApp response structure.

    """

    def __init__(self):
        r"""
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


class DescribeApiKeyRequest(AbstractModel):
    """DescribeApiKey request structure.

    """

    def __init__(self):
        r"""
        :param AccessKeyId: API key ID.
        :type AccessKeyId: str
        """
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
        r"""
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


class DescribeApiKeysStatusRequest(AbstractModel):
    """DescribeApiKeysStatus request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter. Valid values: AccessKeyId, AccessKeySecret, SecretName, NotUsagePlanId, Status, KeyWord (match with `name` or `path`).
        :type Filters: list of Filter
        """
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
        r"""
        :param Result: Key list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKeysStatus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param ServiceId: Unique service ID of API.
        :type ServiceId: str
        :param ApiId: Unique API ID.
        :type ApiId: str
        """
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
        r"""
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
        r"""
        :param ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
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
        r"""
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


class DescribeApisStatusRequest(AbstractModel):
    """DescribeApisStatus request structure.

    """

    def __init__(self):
        r"""
        :param ServiceId: Unique service ID of API.
        :type ServiceId: str
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Filters: API filter. Valid values: `ApiId`, `ApiName`, `ApiPath`, `ApiType`, `AuthRelationApiId`, `AuthType`, `ApiBuniessType`, `NotUsagePlanId`, `Environment`, `Tags` (whose values are the list of `$tag_key:tag_value`), `TagKeys` (whose values are the list of tag keys). Note that `NotUsagePlanId` and `Environment` must be used in the same time.
        :type Filters: list of Filter
        """
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
        r"""
        :param Result: List of API details.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApisStatus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param StrategyId: Unique policy ID.
        :type StrategyId: str
        :param EnvironmentName: Policy environment.
        :type EnvironmentName: str
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter. Valid values: ApiPath, ApiName, KeyWord (fuzzy search by `Path` and `Name`).
        :type Filters: list of Filter
        """
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
        r"""
        :param Result: List of APIs bound to environment.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategyApiStatus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param StrategyId: Unique IP policy ID.
        :type StrategyId: str
        :param EnvironmentName: Environment associated with policy.
        :type EnvironmentName: str
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter, which is a reserved field. Filtering is not supported currently.
        :type Filters: list of Filter
        """
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
        r"""
        :param Result: IP policy details.
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


class DescribeIPStrategysStatusRequest(AbstractModel):
    """DescribeIPStrategysStatus request structure.

    """

    def __init__(self):
        r"""
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param Filters: Filter. Valid values: StrategyName.
        :type Filters: list of Filter
        """
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
        r"""
        :param Result: List of eligible policies.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategysStatus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param StartTime: Log start time
        :type StartTime: str
        :param EndTime: Log end time
        :type EndTime: str
        :param ServiceId: Service ID
        :type ServiceId: str
        :param Filters: Reserved field
        :type Filters: list of Filter
        :param Limit: Number of logs to be returned at a time. Maximum value: 100
        :type Limit: int
        :param ConText: Subsequent content can be obtained based on the `ConText` returned last time. Up to 10,000 data entries can be obtained
        :type ConText: str
        :param Sort: Sorting by time. Valid values: asc (ascending), desc (descending). Default value: desc
        :type Sort: str
        :param Query: Reserved field
        :type Query: str
        :param LogQuerys: Search criterion. Valid values:
req_id: "="
api_id: "="
cip: "="
uip: ":"
err_msg: ":"
rsp_st: "=", "!=", ":", ">", "<"
req_t: ">=", "<="

Note:
":" indicates included, and "!=" indicates not equal to. For the meanings of fields, please see the `LogSet` description of the output parameter
        :type LogQuerys: list of LogQuery
        """
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
        r"""
        :param ConText: Cursor for getting more search results. If the value is `""`, there will be no subsequent results
        :type ConText: str
        :param LogSet: The returned result contains any number of logs, which are in the following format:
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
req_id: request ID.
        :type LogSet: list of str
        :param TotalCount: Number of logs returned for one search (`TotalCount <= Limit`)
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


class DescribePluginApisRequest(AbstractModel):
    """DescribePluginApis request structure.

    """

    def __init__(self):
        r"""
        :param PluginId: ID of the plugin to be queried
        :type PluginId: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100
        :type Limit: int
        :param Offset: Offset. Default value: 0
        :type Offset: int
        """
        self.PluginId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePluginApisResponse(AbstractModel):
    """DescribePluginApis response structure.

    """

    def __init__(self):
        r"""
        :param Result: List of APIs bound with the plugin
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.AttachedApiSummary`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = AttachedApiSummary()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePluginRequest(AbstractModel):
    """DescribePlugin request structure.

    """

    def __init__(self):
        r"""
        :param PluginId: ID of the plugin to be queried
        :type PluginId: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100
        :type Limit: int
        :param Offset: Offset. Default value: 0
        :type Offset: int
        """
        self.PluginId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePluginResponse(AbstractModel):
    """DescribePlugin response structure.

    """

    def __init__(self):
        r"""
        :param Result: Plugin details
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.Plugin`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = Plugin()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePluginsByApiRequest(AbstractModel):
    """DescribePluginsByApi request structure.

    """

    def __init__(self):
        r"""
        :param ApiId: ID of the API to query
        :type ApiId: str
        :param ServiceId: ID of the service to query
        :type ServiceId: str
        :param EnvironmentName: Environment information
        :type EnvironmentName: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100
        :type Limit: int
        :param Offset: Offset. Default value: 0
        :type Offset: int
        """
        self.ApiId = None
        self.ServiceId = None
        self.EnvironmentName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
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
        


class DescribePluginsByApiResponse(AbstractModel):
    """DescribePluginsByApi response structure.

    """

    def __init__(self):
        r"""
        :param Result: List of plug-ins bound with the API
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.AttachedPluginSummary`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = AttachedPluginSummary()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServiceEnvironmentListRequest(AbstractModel):
    """DescribeServiceEnvironmentList request structure.

    """

    def __init__(self):
        r"""
        :param ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
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
        r"""
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
        r"""
        :param ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        :param EnvironmentName: Environment name.
        :type EnvironmentName: str
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
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
        r"""
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
        r"""
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
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
        r"""
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


class DescribeServiceForApiAppRequest(AbstractModel):
    """DescribeServiceForApiApp request structure.

    """

    def __init__(self):
        r"""
        :param ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        :param ApiRegion: Service region.
        :type ApiRegion: str
        """
        self.ServiceId = None
        self.ApiRegion = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiRegion = params.get("ApiRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceForApiAppResponse(AbstractModel):
    """DescribeServiceForApiApp response structure.

    """

    def __init__(self):
        r"""
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param AvailableEnvironments: Service environment list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AvailableEnvironments: list of str
        :param ServiceName: Service name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceName: str
        :param ServiceDesc: Service description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceDesc: str
        :param Protocol: Protocol supported by service. Valid values: http, https, http&https.
        :type Protocol: str
        :param CreatedTime: Service creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param ModifiedTime: Service modification time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param ExclusiveSetName: Self-Deployed cluster name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExclusiveSetName: str
        :param NetTypes: Network type list. INNER: private network access; OUTER: public network access.
        :type NetTypes: list of str
        :param InternalSubDomain: Subdomain name for private network access.
        :type InternalSubDomain: str
        :param OuterSubDomain: Subdomain name for public network access.
        :type OuterSubDomain: str
        :param InnerHttpPort: Service port number for HTTP access over private network.
        :type InnerHttpPort: int
        :param InnerHttpsPort: Port number for HTTPS access over private network.
        :type InnerHttpsPort: int
        :param ApiTotalCount: Total number of APIs.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiTotalCount: int
        :param ApiIdStatusSet: API list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiIdStatusSet: list of ApiIdStatus
        :param UsagePlanTotalCount: Total number of usage plans.
Note: this field may return null, indicating that no valid values can be obtained.
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
        :param Tags: Tag bound to the service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
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
        self.Tags = None
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
        self.RequestId = params.get("RequestId")


class DescribeServiceReleaseVersionRequest(AbstractModel):
    """DescribeServiceReleaseVersion request structure.

    """

    def __init__(self):
        r"""
        :param ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
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
        r"""
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
        r"""
        :param ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        """
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
        r"""
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param AvailableEnvironments: Service environment list.
        :type AvailableEnvironments: list of str
        :param ServiceName: Service name.
        :type ServiceName: str
        :param ServiceDesc: Service description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceDesc: str
        :param Protocol: Protocol supported by service. Valid values: http, https, http&https.
        :type Protocol: str
        :param CreatedTime: Service creation time.
        :type CreatedTime: str
        :param ModifiedTime: Service modification time.
        :type ModifiedTime: str
        :param ExclusiveSetName: Dedicated cluster name.
        :type ExclusiveSetName: str
        :param NetTypes: Network type list. INNER: private network access; OUTER: public network access.
        :type NetTypes: list of str
        :param InternalSubDomain: Subdomain name for private network access.
        :type InternalSubDomain: str
        :param OuterSubDomain: Subdomain name for public network access.
        :type OuterSubDomain: str
        :param InnerHttpPort: Service port number for HTTP access over private network.
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
        :param Tags: Tags bound to a service.
Note: this field may return null, indicating that no valid values found.
        :type Tags: list of Tag
        :param InstanceId: Dedicated instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param InstanceName: Dedicated instance name
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param SetType: Cluster type
Note: this field may return null, indicating that no valid values can be obtained.
        :type SetType: str
        :param DeploymentType: Cluster type for service deployment
Note: this field may return null, indicating that no valid values found.
        :type DeploymentType: str
        :param SpecialUse: Whether the service if for special usage. Valid values: `DEFAULT` (general usage), `HTTP_DNS`.
Note: This field may return `NULL`, indicating that no valid value was found.
        :type SpecialUse: str
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
        self.Tags = None
        self.InstanceId = None
        self.InstanceName = None
        self.SetType = None
        self.DeploymentType = None
        self.SpecialUse = None
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
        self.DeploymentType = params.get("DeploymentType")
        self.SpecialUse = params.get("SpecialUse")
        self.RequestId = params.get("RequestId")


class DescribeServiceSubDomainMappingsRequest(AbstractModel):
    """DescribeServiceSubDomainMappings request structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
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
        r"""
        :param Result: Custom service domain name query.
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
        r"""
        :param ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
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
        r"""
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


class DescribeServicesStatusRequest(AbstractModel):
    """DescribeServicesStatus request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter. Valid values: `ServiceId`, `ServiceName`, `NotUsagePlanId`, `Environment`, `IpVersion`, `InstanceId`, `NetType`, `EIAMAppId`.
        :type Filters: list of Filter
        """
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
        r"""
        :param Result: Service list query result.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServicesStatus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServicesStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUpstreamBindApis(AbstractModel):
    """Queries APIs bound with an upstream

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number
        :type TotalCount: int
        :param BindApiSet: Information of bound APIs
        :type BindApiSet: list of BindApiInfo
        """
        self.TotalCount = None
        self.BindApiSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BindApiSet") is not None:
            self.BindApiSet = []
            for item in params.get("BindApiSet"):
                obj = BindApiInfo()
                obj._deserialize(item)
                self.BindApiSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpstreamBindApisRequest(AbstractModel):
    """DescribeUpstreamBindApis request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Number of entries per page
        :type Limit: int
        :param Offset: The starting position of paging
        :type Offset: int
        :param UpstreamId: Upstream ID
        :type UpstreamId: str
        :param Filters: Filters the results by `ServiceId` and `ApiId`
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.UpstreamId = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.UpstreamId = params.get("UpstreamId")
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
        


class DescribeUpstreamBindApisResponse(AbstractModel):
    """DescribeUpstreamBindApis response structure.

    """

    def __init__(self):
        r"""
        :param Result: Query results
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DescribeUpstreamBindApis`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = DescribeUpstreamBindApis()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUpstreamInfo(AbstractModel):
    """The returned result of upstream query

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of results
        :type TotalCount: int
        :param UpstreamSet: List of query result
        :type UpstreamSet: list of UpstreamInfo
        """
        self.TotalCount = None
        self.UpstreamSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UpstreamSet") is not None:
            self.UpstreamSet = []
            for item in params.get("UpstreamSet"):
                obj = UpstreamInfo()
                obj._deserialize(item)
                self.UpstreamSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpstreamsRequest(AbstractModel):
    """DescribeUpstreams request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Number of entries per page
        :type Limit: int
        :param Offset: The starting position of paging
        :type Offset: int
        :param Filters: Filters. Valid values: `UpstreamId` and `UpstreamName`
        :type Filters: list of Filter
        """
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
        


class DescribeUpstreamsResponse(AbstractModel):
    """DescribeUpstreams response structure.

    """

    def __init__(self):
        r"""
        :param Result: Query results
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DescribeUpstreamInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = DescribeUpstreamInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUsagePlanEnvironmentsRequest(AbstractModel):
    """DescribeUsagePlanEnvironments request structure.

    """

    def __init__(self):
        r"""
        :param UsagePlanId: Unique ID of the usage plan to be queried.
        :type UsagePlanId: str
        :param BindType: Binding type. Valid values: API, SERVICE. Default value: SERVICE.
        :type BindType: str
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
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
        r"""
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
        r"""
        :param UsagePlanId: Unique ID of the usage plan to be queried.
        :type UsagePlanId: str
        """
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
        r"""
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
        r"""
        :param UsagePlanId: Unique ID of bound usage plan.
        :type UsagePlanId: str
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
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
        r"""
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


class DescribeUsagePlansStatusRequest(AbstractModel):
    """DescribeUsagePlansStatus request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Usage plan filter. Valid values: UsagePlanId, UsagePlanName, NotServiceId, NotApiId, Environment.
        :type Filters: list of Filter
        """
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
        r"""
        :param Result: Usage plan list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlansStatus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UsagePlansStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DetachPluginRequest(AbstractModel):
    """DetachPlugin request structure.

    """

    def __init__(self):
        r"""
        :param PluginId: ID of the plugin to be unbound
        :type PluginId: str
        :param ServiceId: Service ID
        :type ServiceId: str
        :param EnvironmentName: API environment
        :type EnvironmentName: str
        :param ApiId: ID of the API to unbind from the plugin
        :type ApiId: str
        """
        self.PluginId = None
        self.ServiceId = None
        self.EnvironmentName = None
        self.ApiId = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachPluginResponse(AbstractModel):
    """DetachPlugin response structure.

    """

    def __init__(self):
        r"""
        :param Result: Whether unbinding succeeded.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DisableApiKeyRequest(AbstractModel):
    """DisableApiKey request structure.

    """

    def __init__(self):
        r"""
        :param AccessKeyId: ID of the key to be disabled.
        :type AccessKeyId: str
        """
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
        r"""
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
    """API document download

    """

    def __init__(self):
        r"""
        :param DocumentURL: Download link of generated file. Generated documents will be stored in COS.
        :type DocumentURL: str
        :param SdkURL: Download link of generated SDK file. Generated SDK files will be stored in COS.
        :type SdkURL: str
        """
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
        r"""
        :param DomainName: Domain name.
        :type DomainName: str
        :param Status: Domain name resolution status. `1`: normal, `0`: failed
        :type Status: int
        :param CertificateId: Certificate ID.
        :type CertificateId: str
        :param IsDefaultMapping: Whether the default path mapping is used.
        :type IsDefaultMapping: bool
        :param Protocol: Custom domain name protocol type.
        :type Protocol: str
        :param NetType: Network type. Valid values: INNER, OUTER.
        :type NetType: str
        :param IsForcedHttps: Whether to force HTTP requests to redirect to HTTPS. Default value: `false`. When this parameter is `true`, API Gateway will redirect all requests using the custom domain name over the HTTP protocol to the HTTPS protocol for forwarding.
        :type IsForcedHttps: bool
        :param RegistrationStatus: ICP filing status
        :type RegistrationStatus: bool
        """
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
        r"""
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
        r"""
        :param AccessKeyId: ID of the key to be enabled.
        :type AccessKeyId: str
        """
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
        r"""
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
    """Information of service release environment.

    """

    def __init__(self):
        r"""
        :param EnvironmentName: Environment name.
        :type EnvironmentName: str
        :param Url: Access path.
        :type Url: str
        :param Status: Release status. 1: published. 0: not published.
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
        r"""
        :param EnvironmentName: Environment name
        :type EnvironmentName: str
        :param Quota: Throttling value
        :type Quota: int
        :param MaxQuota: Maximum quota value
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxQuota: int
        """
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
        r"""
        :param Code: Custom response configuration error code.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Code: int
        :param Msg: Custom response configuration error message.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param Desc: Custom response configuration error code remarks.
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
        r"""
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
        r"""
        :param ServiceId: Unique service ID of the document to be created.
        :type ServiceId: str
        :param GenEnvironment: Environment of the service for which to create an SDK.
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
        r"""
        :param Result: API document and SDK link.
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
        r"""
        :param IsHealthCheck: Whether health check is enabled.
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
        r"""
        :param StrategyId: Unique policy ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StrategyId: str
        :param StrategyName: Custom policy name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StrategyName: str
        :param StrategyType: Policy type. Valid values: WHITE (allowlist), BLACK (blocklist).
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
        r"""
        :param ApiId: Unique API ID.
        :type ApiId: str
        :param ApiName: Custom API name.
        :type ApiName: str
        :param ApiType: API type. Valid values: NORMAL (general API), TSF (microservice API).
        :type ApiType: str
        :param Path: API path, such as `/path`.
        :type Path: str
        :param Method: API request method, such as `GET`.
        :type Method: str
        :param OtherIPStrategyId: Unique ID of another policy bound to API.
        :type OtherIPStrategyId: str
        :param OtherEnvironmentName: Environment bound to API.
        :type OtherEnvironmentName: str
        """
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
        r"""
        :param TotalCount: Number of APIs bound to environment.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param ApiIdStatusSet: Details of APIs bound to environment.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiIdStatusSet: list of IPStrategyApi
        """
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
        r"""
        :param TotalCount: Number of policies.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param StrategySet: Policy list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StrategySet: list of IPStrategy
        """
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
        


class ImportOpenApiRequest(AbstractModel):
    """ImportOpenApi request structure.

    """

    def __init__(self):
        r"""
        :param ServiceId: The unique ID of the service associated with the API
        :type ServiceId: str
        :param Content: Content of the openAPI
        :type Content: str
        :param EncodeType: Format of the content. Values: `YAML` (default), `JSON`
        :type EncodeType: str
        :param ContentVersion: Version of the content. It can only be `openAPI` for now.
        :type ContentVersion: str
        """
        self.ServiceId = None
        self.Content = None
        self.EncodeType = None
        self.ContentVersion = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Content = params.get("Content")
        self.EncodeType = params.get("EncodeType")
        self.ContentVersion = params.get("ContentVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportOpenApiResponse(AbstractModel):
    """ImportOpenApi response structure.

    """

    def __init__(self):
        r"""
        :param Result: The result of importing the OpenAPI
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.CreateApiRspSet`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateApiRspSet()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class K8sLabel(AbstractModel):
    """K8s Label

    """

    def __init__(self):
        r"""
        :param Key: Key of the label
        :type Key: str
        :param Value: Value of the label
        :type Value: str
        """
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
        


class K8sService(AbstractModel):
    """Configuration of K8s service

    """

    def __init__(self):
        r"""
        :param Weight: Weight
        :type Weight: int
        :param ClusterId: K8s cluster ID
        :type ClusterId: str
        :param Namespace: Namespace of the container
        :type Namespace: str
        :param ServiceName: Name of the service
        :type ServiceName: str
        :param Port: Service port
        :type Port: int
        :param ExtraLabels: The additional Label of the Pod
        :type ExtraLabels: list of K8sLabel
        :param Name: (Optional) Custom name of the service
        :type Name: str
        """
        self.Weight = None
        self.ClusterId = None
        self.Namespace = None
        self.ServiceName = None
        self.Port = None
        self.ExtraLabels = None
        self.Name = None


    def _deserialize(self, params):
        self.Weight = params.get("Weight")
        self.ClusterId = params.get("ClusterId")
        self.Namespace = params.get("Namespace")
        self.ServiceName = params.get("ServiceName")
        self.Port = params.get("Port")
        if params.get("ExtraLabels") is not None:
            self.ExtraLabels = []
            for item in params.get("ExtraLabels"):
                obj = K8sLabel()
                obj._deserialize(item)
                self.ExtraLabels.append(obj)
        self.Name = params.get("Name")
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
        r"""
        :param Name: Search field
        :type Name: str
        :param Operator: Operator
        :type Operator: str
        :param Value: Search value
        :type Value: str
        """
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
        r"""
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
        r"""
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
        r"""
        :param ApiDocId: API document ID
        :type ApiDocId: str
        :param ApiDocName: API document name
        :type ApiDocName: str
        :param ServiceId: Service name
        :type ServiceId: str
        :param Environment: Environment name
        :type Environment: str
        :param ApiIds: List of APIs for which to generate documents
        :type ApiIds: list of str
        """
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
        r"""
        :param Result: Basic information of API document
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = APIDoc()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyApiAppRequest(AbstractModel):
    """ModifyApiApp request structure.

    """

    def __init__(self):
        r"""
        :param ApiAppId: Unique application ID.
        :type ApiAppId: str
        :param ApiAppName: Modified application name
        :type ApiAppName: str
        :param ApiAppDesc: Modified application description
        :type ApiAppDesc: str
        """
        self.ApiAppId = None
        self.ApiAppName = None
        self.ApiAppDesc = None


    def _deserialize(self, params):
        self.ApiAppId = params.get("ApiAppId")
        self.ApiAppName = params.get("ApiAppName")
        self.ApiAppDesc = params.get("ApiAppDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiAppResponse(AbstractModel):
    """ModifyApiApp response structure.

    """

    def __init__(self):
        r"""
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


class ModifyApiEnvironmentStrategyRequest(AbstractModel):
    """ModifyApiEnvironmentStrategy request structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
        :param ServiceId: Service ID
        :type ServiceId: str
        :param ApiId: API ID
        :type ApiId: str
        :param BusinessType: Authorization type of the API to be modified (you can select `OAUTH`, i.e., authorization API)
        :type BusinessType: str
        :param PublicKey: Public key value to be modified by OAuth API
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
        r"""
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
        r"""
        :param ServiceId: Unique service ID of API.
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
        :param ApiType: API type. Valid values: NORMAL, TSF. Default value: NORMAL.
        :type ApiType: str
        :param AuthType: API authentication type. Valid values: SECRET, NONE, OAUTH, APP. Default value: NONE.
        :type AuthType: str
        :param AuthRequired: Whether signature authentication is required. True: yes; False: no. This parameter is to be disused.
        :type AuthRequired: bool
        :param ServiceTimeout: API backend service timeout period in seconds.
        :type ServiceTimeout: int
        :param Protocol: API frontend request type, such as HTTP, HTTPS, or HTTP and HTTPS.
        :type Protocol: str
        :param EnableCORS: Whether to enable CORS. True: yes; False: no.
        :type EnableCORS: bool
        :param ConstantParameters: Constant parameter.
        :type ConstantParameters: list of ConstantParameter
        :param RequestParameters: Frontend request parameter.
        :type RequestParameters: list of ReqParameter
        :param ApiBusinessType: This field is valid if `AuthType` is `OAUTH`. NORMAL: business API; OAUTH: authorization API.
        :type ApiBusinessType: str
        :param ServiceMockReturnMessage: Returned message of API backend Mock, which is required if `ServiceType` is `Mock`.
        :type ServiceMockReturnMessage: str
        :param MicroServices: List of microservices bound to API.
        :type MicroServices: list of MicroServiceReq
        :param ServiceTsfLoadBalanceConf: Load balancing configuration of microservice.
        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`
        :param ServiceTsfHealthCheckConf: Health check configuration of microservice.
        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param TargetServicesLoadBalanceConf: `target` type load balancing configuration (in beta test).
        :type TargetServicesLoadBalanceConf: int
        :param TargetServicesHealthCheckConf: `target` health check configuration (in beta test).
        :type TargetServicesHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param ServiceScfFunctionName: SCF function name, which takes effect if the backend type is `SCF`.
        :type ServiceScfFunctionName: str
        :param ServiceWebsocketRegisterFunctionName: SCF WebSocket registration function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionName: str
        :param ServiceWebsocketCleanupFunctionName: SCF WebSocket cleanup function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionName: str
        :param ServiceWebsocketTransportFunctionName: SCF WebSocket transfer function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionName: str
        :param ServiceScfFunctionNamespace: SCF function namespace, which takes effect if the backend type is `SCF`.
        :type ServiceScfFunctionNamespace: str
        :param ServiceScfFunctionQualifier: SCF function version, which takes effect if the backend type is `SCF`.
        :type ServiceScfFunctionQualifier: str
        :param ServiceWebsocketRegisterFunctionNamespace: SCF WebSocket registration function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionNamespace: str
        :param ServiceWebsocketRegisterFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionQualifier: str
        :param ServiceWebsocketTransportFunctionNamespace: SCF WebSocket transfer function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionNamespace: str
        :param ServiceWebsocketTransportFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionQualifier: str
        :param ServiceWebsocketCleanupFunctionNamespace: SCF WebSocket cleanup function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionNamespace: str
        :param ServiceWebsocketCleanupFunctionQualifier: SCF WebSocket cleanup function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionQualifier: str
        :param ServiceScfIsIntegratedResponse: Whether to enable response integration, which takes effect if the backend type is `SCF`.
        :type ServiceScfIsIntegratedResponse: bool
        :param IsDebugAfterCharge: Billing after debugging starts (reserved field for marketplace).
        :type IsDebugAfterCharge: bool
        :param TagSpecifications: Tag.
        :type TagSpecifications: :class:`tencentcloud.apigateway.v20180808.models.Tag`
        :param IsDeleteResponseErrorCodes: Whether to delete the error codes for custom response configuration. If the value is left empty or `False`, the error codes will not be deleted. If the value is `True`, all custom response configuration error codes of the API will be deleted.
        :type IsDeleteResponseErrorCodes: bool
        :param ResponseType: Return type.
        :type ResponseType: str
        :param ResponseSuccessExample: Sample response for successful custom response configuration.
        :type ResponseSuccessExample: str
        :param ResponseFailExample: Sample response for failed custom response configuration.
        :type ResponseFailExample: str
        :param ServiceConfig: API backend service configuration.
        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`
        :param AuthRelationApiId: Unique ID of associated authorization API, which takes effect only if `AuthType` is `OAUTH` and `ApiBusinessType` is `NORMAL`. It is the unique ID of the OAuth 2.0 authorization API bound to the business API.
        :type AuthRelationApiId: str
        :param ServiceParameters: API backend service parameter.
        :type ServiceParameters: list of ServiceParameter
        :param OauthConfig: OAuth configuration, which takes effect if `AuthType` is `OAUTH`.
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param ResponseErrorCodes: Custom error code configuration.
        :type ResponseErrorCodes: list of ResponseErrorCodeReq
        :param IsBase64Encoded: Whether to enable Base64 encoding. This parameter takes effect only when the backend is SCF.
        :type IsBase64Encoded: bool
        :param IsBase64Trigger: Whether to trigger Base64 encoding by header. This parameter takes effect only when the backend is SCF.
        :type IsBase64Trigger: bool
        :param Base64EncodedTriggerRules: Header trigger rules. The number of rules cannot exceed 10.
        :type Base64EncodedTriggerRules: list of Base64EncodedTriggerRule
        :param EventBusId: Event bus ID.
        :type EventBusId: str
        :param ServiceScfFunctionType: SCF function type, which takes effect when the backend type is `SCF`. Valid values: `EVENT` and `HTTP`.
        :type ServiceScfFunctionType: str
        :param EIAMAppType: EIAM application type.
        :type EIAMAppType: str
        :param EIAMAuthType: EIAM application authentication type. Valid values: `AuthenticationOnly`, `Authentication`, `Authorization`.
        :type EIAMAuthType: str
        :param EIAMAppId: Validity of the EIAM application token. Unit: second. Default value: `7200`.
        :type EIAMAppId: str
        :param TokenTimeout: EIAM application ID.
        :type TokenTimeout: int
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
        self.IsBase64Encoded = None
        self.IsBase64Trigger = None
        self.Base64EncodedTriggerRules = None
        self.EventBusId = None
        self.ServiceScfFunctionType = None
        self.EIAMAppType = None
        self.EIAMAuthType = None
        self.EIAMAppId = None
        self.TokenTimeout = None


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
        self.EventBusId = params.get("EventBusId")
        self.ServiceScfFunctionType = params.get("ServiceScfFunctionType")
        self.EIAMAppType = params.get("EIAMAppType")
        self.EIAMAuthType = params.get("EIAMAuthType")
        self.EIAMAppId = params.get("EIAMAppId")
        self.TokenTimeout = params.get("TokenTimeout")
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
        r"""
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
        r"""
        :param ServiceId: Unique service ID of the policy to be modified.
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
        r"""
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


class ModifyPluginRequest(AbstractModel):
    """ModifyPlugin request structure.

    """

    def __init__(self):
        r"""
        :param PluginId: ID of the plugin to be modified
        :type PluginId: str
        :param PluginName: Plugin name to be modified. A plugin name can contain up to 50 characters out of `a-z`, `A-Z`, `0-9`, and `_`, which must begin with a letter and end with a letter or a number.
        :type PluginName: str
        :param Description: Plugin description to be modified. A description is within 200 characters.
        :type Description: str
        :param PluginData: Plugin definition statement to be modified. The json format is supported.
        :type PluginData: str
        """
        self.PluginId = None
        self.PluginName = None
        self.Description = None
        self.PluginData = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        self.PluginName = params.get("PluginName")
        self.Description = params.get("Description")
        self.PluginData = params.get("PluginData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPluginResponse(AbstractModel):
    """ModifyPlugin response structure.

    """

    def __init__(self):
        r"""
        :param Result: Whether modification succeeded.
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
        r"""
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
        r"""
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
        r"""
        :param ServiceId: Unique ID of the service to be modified.
        :type ServiceId: str
        :param ServiceName: Service name after modification.
        :type ServiceName: str
        :param ServiceDesc: Service description after modification.
        :type ServiceDesc: str
        :param Protocol: Service frontend request type after modification, such as `http`, `https`, and `http&https`.
        :type Protocol: str
        :param NetTypes: Network type list, which is used to specify the supported network types. INNER: private network access; OUTER: public network access. Default value: OUTER.
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
        r"""
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
        r"""
        :param ServiceId: Unique service ID.
        :type ServiceId: str
        :param SubDomain: Custom domain name whose path mapping is to be modified.
        :type SubDomain: str
        :param IsDefaultMapping: Whether to change to the default path mapping. true: use the default path mapping; false: use the custom path mapping.
        :type IsDefaultMapping: bool
        :param CertificateId: Certificate ID, which is required if the HTTPS protocol is included.
        :type CertificateId: str
        :param Protocol: Custom domain name protocol type after modification. Valid values: http, https, http&https.
        :type Protocol: str
        :param PathMappingSet: Path mapping list after modification.
        :type PathMappingSet: list of PathMapping
        :param NetType: Network type. Valid values: INNER, OUTER.
        :type NetType: str
        :param IsForcedHttps: Whether to force HTTP requests to redirect to HTTPS. Default value: `false`. When this parameter is `true`, API Gateway will redirect all requests using the custom domain name over the HTTP protocol to the HTTPS protocol for forwarding.
        :type IsForcedHttps: bool
        """
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
        r"""
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


class ModifyUpstreamRequest(AbstractModel):
    """ModifyUpstream request structure.

    """

    def __init__(self):
        r"""
        :param UpstreamId: Unique upstream ID
        :type UpstreamId: str
        :param UpstreamName: Upstream name
        :type UpstreamName: str
        :param UpstreamDescription: Upstream description
        :type UpstreamDescription: str
        :param Scheme: Backend protocol. Valid values: `HTTP`, `HTTPS`
        :type Scheme: str
        :param UpstreamType: Upstream access type. Valid values: `IP_PORT`, `K8S`
        :type UpstreamType: str
        :param Algorithm: Load balancing algorithm. Valid value: `ROUND_ROBIN`
        :type Algorithm: str
        :param UniqVpcId: Unique VPC ID.
        :type UniqVpcId: str
        :param Retries: Retry attempts. It defaults to `3`.
        :type Retries: int
        :param UpstreamHost: Gateway forwarding to the upstream Host request header
        :type UpstreamHost: str
        :param Nodes: List of backend nodes
        :type Nodes: list of UpstreamNode
        :param HealthChecker: Health check configuration
        :type HealthChecker: :class:`tencentcloud.apigateway.v20180808.models.UpstreamHealthChecker`
        :param K8sService: Configuration of TKE service
        :type K8sService: list of K8sService
        """
        self.UpstreamId = None
        self.UpstreamName = None
        self.UpstreamDescription = None
        self.Scheme = None
        self.UpstreamType = None
        self.Algorithm = None
        self.UniqVpcId = None
        self.Retries = None
        self.UpstreamHost = None
        self.Nodes = None
        self.HealthChecker = None
        self.K8sService = None


    def _deserialize(self, params):
        self.UpstreamId = params.get("UpstreamId")
        self.UpstreamName = params.get("UpstreamName")
        self.UpstreamDescription = params.get("UpstreamDescription")
        self.Scheme = params.get("Scheme")
        self.UpstreamType = params.get("UpstreamType")
        self.Algorithm = params.get("Algorithm")
        self.UniqVpcId = params.get("UniqVpcId")
        self.Retries = params.get("Retries")
        self.UpstreamHost = params.get("UpstreamHost")
        if params.get("Nodes") is not None:
            self.Nodes = []
            for item in params.get("Nodes"):
                obj = UpstreamNode()
                obj._deserialize(item)
                self.Nodes.append(obj)
        if params.get("HealthChecker") is not None:
            self.HealthChecker = UpstreamHealthChecker()
            self.HealthChecker._deserialize(params.get("HealthChecker"))
        if params.get("K8sService") is not None:
            self.K8sService = []
            for item in params.get("K8sService"):
                obj = K8sService()
                obj._deserialize(item)
                self.K8sService.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUpstreamResponse(AbstractModel):
    """ModifyUpstream response structure.

    """

    def __init__(self):
        r"""
        :param Result: Return modified upstream information
Note: This field may return `NULL`, indicating that no valid value was found.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UpstreamInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UpstreamInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyUsagePlanRequest(AbstractModel):
    """ModifyUsagePlan request structure.

    """

    def __init__(self):
        r"""
        :param UsagePlanId: Unique usage plan ID.
        :type UsagePlanId: str
        :param UsagePlanName: Custom usage plan name after modification.
        :type UsagePlanName: str
        :param UsagePlanDesc: Custom usage plan description after modification.
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
        r"""
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
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Plugin(AbstractModel):
    """Details of the API Gateway plugin

    """

    def __init__(self):
        r"""
        :param PluginId: Plugin ID
        :type PluginId: str
        :param PluginName: Plugin name
        :type PluginName: str
        :param PluginType: Plugin type
        :type PluginType: str
        :param PluginData: Plugin definition statement
        :type PluginData: str
        :param Description: Plugin description
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param CreatedTime: Plugin creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
        :type CreatedTime: str
        :param ModifiedTime: Plugin modification time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used
        :type ModifiedTime: str
        :param AttachedApiTotalCount: Total number of APIs bound with the plugin
Note: this field may return null, indicating that no valid values can be obtained.
        :type AttachedApiTotalCount: int
        :param AttachedApis: Information of the API bound with the plugin
Note: this field may return null, indicating that no valid values can be obtained.
        :type AttachedApis: list of AttachedApiInfo
        """
        self.PluginId = None
        self.PluginName = None
        self.PluginType = None
        self.PluginData = None
        self.Description = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.AttachedApiTotalCount = None
        self.AttachedApis = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        self.PluginName = params.get("PluginName")
        self.PluginType = params.get("PluginType")
        self.PluginData = params.get("PluginData")
        self.Description = params.get("Description")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.AttachedApiTotalCount = params.get("AttachedApiTotalCount")
        if params.get("AttachedApis") is not None:
            self.AttachedApis = []
            for item in params.get("AttachedApis"):
                obj = AttachedApiInfo()
                obj._deserialize(item)
                self.AttachedApis.append(obj)
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
        r"""
        :param ReleaseDesc: Release remarks.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReleaseDesc: str
        :param ReleaseVersion: Published version ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReleaseVersion: str
        """
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
        r"""
        :param ServiceId: Unique ID of the service to be published.
        :type ServiceId: str
        :param EnvironmentName: Name of the environment to be published. Valid values: test (test environment), prepub (pre-release environment), release (release environment).
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
        r"""
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


class ReqParameter(AbstractModel):
    """Request parameter

    """

    def __init__(self):
        r"""
        :param Name: API frontend parameter name.
        :type Name: str
        :param Position: Position of the API frontend parameter, such as the header. Supported values: `header`, `query`, and `path`.
        :type Position: str
        :param Type: API frontend parameter type, such as `String` and `int`.
        :type Type: str
        :param DefaultValue: Default value of API frontend parameter.
        :type DefaultValue: str
        :param Required: Whether the API frontend parameter is required. True: yes; False: no.
        :type Required: bool
        :param Desc: API frontend parameter remarks.
        :type Desc: str
        """
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
        r"""
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
        r"""
        :param Name: Request parameter name
        :type Name: str
        :param Desc: Description
        :type Desc: str
        :param Position: Parameter position
        :type Position: str
        :param Type: Parameter type
        :type Type: str
        :param DefaultValue: Default value
        :type DefaultValue: str
        :param Required: Whether it is required
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
        r"""
        :param ApiDocId: API document ID
        :type ApiDocId: str
        """
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
        r"""
        :param Result: Basic information of API document
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Code: Custom response configuration error code.
        :type Code: int
        :param Msg: Custom response configuration error message.
        :type Msg: str
        :param Desc: Custom response configuration error code remarks.
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
        r"""
        :param InnerHttpsPort: Port for HTTPS access over private network.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InnerHttpsPort: int
        :param ServiceDesc: Custom service description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceDesc: str
        :param Protocol: Service frontend request type, such as `http`, `https`, and `http&https`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param NetTypes: Network types supported by service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NetTypes: list of str
        :param ExclusiveSetName: Dedicated cluster name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExclusiveSetName: str
        :param ServiceId: Unique service ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceId: str
        :param IpVersion: IP version.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpVersion: str
        :param AvailableEnvironments: List of published environments, such as test, prepub, and release.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AvailableEnvironments: list of str
        :param ServiceName: Custom service name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceName: str
        :param OuterSubDomain: Public domain name assigned by the system for this service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OuterSubDomain: str
        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param InnerHttpPort: Port for HTTP access over private network.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InnerHttpPort: int
        :param InnerSubDomain: Private domain name automatically assigned by the system for this service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InnerSubDomain: str
        :param TradeIsolateStatus: Billing status of service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TradeIsolateStatus: int
        :param Tags: Tags bound to a service.
Note: this field may return null, indicating that no valid values found.
        :type Tags: list of Tag
        :param InstanceId: Dedicated instance
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param SetType: Cluster type
Note: this field may return null, indicating that no valid values can be obtained.
        :type SetType: str
        :param DeploymentType: Cluster type for service deployment
Note: this field may return null, indicating that no valid values found.
        :type DeploymentType: str
        """
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
        self.DeploymentType = None


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
        self.DeploymentType = params.get("DeploymentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceConfig(AbstractModel):
    """ServiceConfig information

    """

    def __init__(self):
        r"""
        :param Product: The backend type. It’s available when `vpc` is enabled. Values: `clb`, `cvm` and `upstream`.
        :type Product: str
        :param UniqVpcId: Unique VPC ID.
        :type UniqVpcId: str
        :param Url: API backend service URL, which is required if `ServiceType` is `HTTP`.
        :type Url: str
        :param Path: API backend service path, such as `/path`, which is required if `ServiceType` is `HTTP`. The frontend and backend paths can be different.
        :type Path: str
        :param Method: API backend service request method, such as `GET`, which is required if `ServiceType` is `HTTP`. The frontend and backend methods can be different
        :type Method: str
        :param UpstreamId: It’s required for `upstream`.
Note: This field may return `NULL`, indicating that no valid value was found.
        :type UpstreamId: str
        :param CosConfig: API backend COS configuration. It’s required if the `ServiceType` is ·`COS`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CosConfig: :class:`tencentcloud.apigateway.v20180808.models.CosConfig`
        """
        self.Product = None
        self.UniqVpcId = None
        self.Url = None
        self.Path = None
        self.Method = None
        self.UpstreamId = None
        self.CosConfig = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.UniqVpcId = params.get("UniqVpcId")
        self.Url = params.get("Url")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.UpstreamId = params.get("UpstreamId")
        if params.get("CosConfig") is not None:
            self.CosConfig = CosConfig()
            self.CosConfig._deserialize(params.get("CosConfig"))
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
        r"""
        :param TotalCount: Total number of environments bound to service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param EnvironmentList: List of environments bound to service.
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
        r"""
        :param EnvironmentName: Environment name.
        :type EnvironmentName: str
        :param Url: Access service environment URL.
        :type Url: str
        :param Status: Release status.
        :type Status: int
        :param VersionName: Published version number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VersionName: str
        :param Strategy: Throttling value.
        :type Strategy: int
        :param MaxStrategy: Maximum quota value
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxStrategy: int
        """
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
        r"""
        :param TotalCount: Number of throttling policies.
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
        r"""
        :param Name: API backend service parameter name, which is used only if `ServiceType` is `HTTP`. The frontend and backend parameter names can be different.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param Position: Position of API backend service parameter, such as `head`, which is used only if `ServiceType` is `HTTP`. The positions of frontend and backend parameters can be different.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Position: str
        :param RelevantRequestParameterPosition: Position of the API frontend parameter corresponding to the backend service parameter, such as `head`, which is used only if `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RelevantRequestParameterPosition: str
        :param RelevantRequestParameterName: Name of the API frontend parameter corresponding to the backend service parameter, which is used only if `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RelevantRequestParameterName: str
        :param DefaultValue: Default value of API backend service parameter, which is used only if `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DefaultValue: str
        :param RelevantRequestParameterDesc: API backend service parameter remarks, which is used only if `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RelevantRequestParameterDesc: str
        :param RelevantRequestParameterType: API backend service parameter type, which is used only if `ServiceType` is `HTTP`.
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
        r"""
        :param TotalCount: Total number of published versions.
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
        r"""
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
        r"""
        :param TotalCount: Total number of published versions.
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
        r"""
        :param IsDefaultMapping: Whether the default path mapping is used. true: use the default path mapping; false: use the custom path mapping (`PathMappingSet` is required in this case).
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
        r"""
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
        r"""
        :param TotalCount: Total number of services in list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param ServiceSet: Service list details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceSet: list of Service
        """
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
        r"""
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
        r"""
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
        r"""
        :param IsLoadBalance: Whether load balancing is enabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsLoadBalance: bool
        :param Method: Load balancing method.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Method: str
        :param SessionStickRequired: Whether session persistence is enabled.
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
        r"""
        :param BindType: Binding type. Valid values: API, SERVICE. Default value: SERVICE.
        :type BindType: str
        :param UsagePlanIds: List of unique IDs of the usage plans to be bound.
        :type UsagePlanIds: list of str
        :param Environment: Service environment to be unbound.
        :type Environment: str
        :param ServiceId: Unique ID of the service to be unbound.
        :type ServiceId: str
        :param ApiIds: Unique API ID array, which is required if `BindType` is `API`.
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param ServiceId: Unique ID of the service to be deactivated.
        :type ServiceId: str
        :param EnvironmentName: Name of the environment to be deactivated. Valid values: test (test environment), prepub (pre-release environment), release (release environment).
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
        r"""
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


class UnbindApiAppRequest(AbstractModel):
    """UnbindApiApp request structure.

    """

    def __init__(self):
        r"""
        :param ApiAppId: Unique ID of the application to be bound.
        :type ApiAppId: str
        :param Environment: Environment to be bound.
        :type Environment: str
        :param ServiceId: Unique ID of the service to be bound.
        :type ServiceId: str
        :param ApiId: Unique ID of the API to be bound.
        :type ApiId: str
        """
        self.ApiAppId = None
        self.Environment = None
        self.ServiceId = None
        self.ApiId = None


    def _deserialize(self, params):
        self.ApiAppId = params.get("ApiAppId")
        self.Environment = params.get("Environment")
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindApiAppResponse(AbstractModel):
    """UnbindApiApp response structure.

    """

    def __init__(self):
        r"""
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


class UpdateApiAppKeyRequest(AbstractModel):
    """UpdateApiAppKey request structure.

    """

    def __init__(self):
        r"""
        :param ApiAppId: Unique application ID.
        :type ApiAppId: str
        :param ApiAppKey: Application Key.
        :type ApiAppKey: str
        :param ApiAppSecret: Application Secret.
        :type ApiAppSecret: str
        """
        self.ApiAppId = None
        self.ApiAppKey = None
        self.ApiAppSecret = None


    def _deserialize(self, params):
        self.ApiAppId = params.get("ApiAppId")
        self.ApiAppKey = params.get("ApiAppKey")
        self.ApiAppSecret = params.get("ApiAppSecret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApiAppKeyResponse(AbstractModel):
    """UpdateApiAppKey response structure.

    """

    def __init__(self):
        r"""
        :param Result: Whether update succeeded.
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
        r"""
        :param AccessKeyId: ID of the key to be changed.
        :type AccessKeyId: str
        :param AccessKeySecret: Key to be updated, which is required when a custom key is updated. It can contain 10–50 letters, digits, and underscores.
        :type AccessKeySecret: str
        """
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
        r"""
        :param Result: Key details after change.
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
        r"""
        :param ServiceId: Unique ID of the service to be switch.
        :type ServiceId: str
        :param EnvironmentName: Name of the environment to be switched to. Valid values: test (test environment), prepub (pre-release environment), release (release environment).
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
        r"""
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


class UpstreamHealthChecker(AbstractModel):
    """Upstream health check parameter configuration

    """

    def __init__(self):
        r"""
        :param EnableActiveCheck: Specifies whether to enable active health check
        :type EnableActiveCheck: bool
        :param EnablePassiveCheck: Specifies whether the enable passive health check
        :type EnablePassiveCheck: bool
        :param HealthyHttpStatus: The HTTP status code that indicates that the upstream is healthy
        :type HealthyHttpStatus: str
        :param UnhealthyHttpStatus: The HTTP status code that indicates that the upstream is unhealthy
        :type UnhealthyHttpStatus: str
        :param TcpFailureThreshold: The threshold on consecutive TCP errors. Range: [0, 254]. `0` indicates not to check TCP.
        :type TcpFailureThreshold: int
        :param TimeoutThreshold: The threshold on consecutive timeouts. Range: [0, 254]. `0` indicates not to check TCP.
        :type TimeoutThreshold: int
        :param HttpFailureThreshold: The threshold on consecutive HTTP errors. Range: [0, 254]. `0` indicates not to check HTTP.
        :type HttpFailureThreshold: int
        :param ActiveCheckHttpPath: The path for active health check. It defaults to `/`.
        :type ActiveCheckHttpPath: str
        :param ActiveCheckTimeout: The timeout period for active health check in seconds. Default: `5`. 
        :type ActiveCheckTimeout: int
        :param ActiveCheckInterval: The interval for active health check in seconds. Default: `5`. 
        :type ActiveCheckInterval: int
        :param ActiveRequestHeader: Header of the active health check request
        :type ActiveRequestHeader: list of UpstreamHealthCheckerReqHeaders
        :param UnhealthyTimeout: The period for an abnormal to recover automatically in seconds. If only the passive health check is enabled, it must be greater than 0. Otherwise the abnormal nodes can not recovered automatically. The default value is 30 seconds. 
        :type UnhealthyTimeout: int
        """
        self.EnableActiveCheck = None
        self.EnablePassiveCheck = None
        self.HealthyHttpStatus = None
        self.UnhealthyHttpStatus = None
        self.TcpFailureThreshold = None
        self.TimeoutThreshold = None
        self.HttpFailureThreshold = None
        self.ActiveCheckHttpPath = None
        self.ActiveCheckTimeout = None
        self.ActiveCheckInterval = None
        self.ActiveRequestHeader = None
        self.UnhealthyTimeout = None


    def _deserialize(self, params):
        self.EnableActiveCheck = params.get("EnableActiveCheck")
        self.EnablePassiveCheck = params.get("EnablePassiveCheck")
        self.HealthyHttpStatus = params.get("HealthyHttpStatus")
        self.UnhealthyHttpStatus = params.get("UnhealthyHttpStatus")
        self.TcpFailureThreshold = params.get("TcpFailureThreshold")
        self.TimeoutThreshold = params.get("TimeoutThreshold")
        self.HttpFailureThreshold = params.get("HttpFailureThreshold")
        self.ActiveCheckHttpPath = params.get("ActiveCheckHttpPath")
        self.ActiveCheckTimeout = params.get("ActiveCheckTimeout")
        self.ActiveCheckInterval = params.get("ActiveCheckInterval")
        if params.get("ActiveRequestHeader") is not None:
            self.ActiveRequestHeader = []
            for item in params.get("ActiveRequestHeader"):
                obj = UpstreamHealthCheckerReqHeaders()
                obj._deserialize(item)
                self.ActiveRequestHeader.append(obj)
        self.UnhealthyTimeout = params.get("UnhealthyTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpstreamHealthCheckerReqHeaders(AbstractModel):
    """The request header configuration of active upstream health check requests

    """


class UpstreamInfo(AbstractModel):
    """Upstream details

    """

    def __init__(self):
        r"""
        :param UpstreamId: Unique upstream ID
        :type UpstreamId: str
        :param UpstreamName: Upstream name
        :type UpstreamName: str
        :param UpstreamDescription: Upstream description
        :type UpstreamDescription: str
        :param Scheme: Backend protocol. Valid values: `HTTP`, `HTTPS`
        :type Scheme: str
        :param Algorithm: Load balancing algorithm. Valid value: `ROUND_ROBIN`
        :type Algorithm: str
        :param UniqVpcId: Unique VPC ID
        :type UniqVpcId: str
        :param Retries: Number of retry attempts
        :type Retries: int
        :param Nodes: Backend nodes
        :type Nodes: list of UpstreamNode
        :param CreatedTime: Creation time.
        :type CreatedTime: str
        :param Tags: Label
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        :param HealthChecker: Health check configuration
Note: This field may return `null`, indicating that no valid value was found.
        :type HealthChecker: :class:`tencentcloud.apigateway.v20180808.models.UpstreamHealthChecker`
        :param UpstreamType: Upstream type. Valid values: `IP_PORT`, `K8S`
        :type UpstreamType: str
        :param K8sServices: Configuration of TKE service
Note: This field may return `NULL`, indicating that no valid value was found.
        :type K8sServices: list of K8sService
        :param UpstreamHost: The Host header that the gateway forwards to the upstream
Note: This field may return `NULL`, indicating that no valid value was found.
        :type UpstreamHost: str
        """
        self.UpstreamId = None
        self.UpstreamName = None
        self.UpstreamDescription = None
        self.Scheme = None
        self.Algorithm = None
        self.UniqVpcId = None
        self.Retries = None
        self.Nodes = None
        self.CreatedTime = None
        self.Tags = None
        self.HealthChecker = None
        self.UpstreamType = None
        self.K8sServices = None
        self.UpstreamHost = None


    def _deserialize(self, params):
        self.UpstreamId = params.get("UpstreamId")
        self.UpstreamName = params.get("UpstreamName")
        self.UpstreamDescription = params.get("UpstreamDescription")
        self.Scheme = params.get("Scheme")
        self.Algorithm = params.get("Algorithm")
        self.UniqVpcId = params.get("UniqVpcId")
        self.Retries = params.get("Retries")
        if params.get("Nodes") is not None:
            self.Nodes = []
            for item in params.get("Nodes"):
                obj = UpstreamNode()
                obj._deserialize(item)
                self.Nodes.append(obj)
        self.CreatedTime = params.get("CreatedTime")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("HealthChecker") is not None:
            self.HealthChecker = UpstreamHealthChecker()
            self.HealthChecker._deserialize(params.get("HealthChecker"))
        self.UpstreamType = params.get("UpstreamType")
        if params.get("K8sServices") is not None:
            self.K8sServices = []
            for item in params.get("K8sServices"):
                obj = K8sService()
                obj._deserialize(item)
                self.K8sServices.append(obj)
        self.UpstreamHost = params.get("UpstreamHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpstreamNode(AbstractModel):
    """Upstream node metadata

    """

    def __init__(self):
        r"""
        :param Host: IP or domain name
        :type Host: str
        :param Port: The port number. Range: [0, 65535]
        :type Port: int
        :param Weight: Value range: [0, 100]. `0` refers to disable it.
        :type Weight: int
        :param VmInstanceId: CVM Instance ID
Note: This field may return `NULL`, indicating that no valid value was found.
        :type VmInstanceId: str
        :param Tags: Tag
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of str
        :param Healthy: Health status of the node. Values: `OFF`, `HEALTHY`, `UNHEALTHY` and `NO_DATA`. It’s not required for creating and editing actions. It only supports VPC upstreams.
Note: This field may return `NULL`, indicating that no valid value was found.
        :type Healthy: str
        :param ServiceName: TKE container name
Note: This field may return `NULL`, indicating that no valid value was found.
        :type ServiceName: str
        :param NameSpace: TKE namespace
Note: This field may return `NULL`, indicating that no valid value was found.
        :type NameSpace: str
        :param ClusterId: ID of the TKE cluster
Note: This field may return `null`, indicating that no valid value was found.
        :type ClusterId: str
        :param Source: Node source. Valid value: `K8S`
Note: This field may return `NULL`, indicating that no valid value was found.
        :type Source: str
        :param UniqueServiceName: The unique service name in API Gateway
Note: This field may return `null`, indicating that no valid value was found.
        :type UniqueServiceName: str
        """
        self.Host = None
        self.Port = None
        self.Weight = None
        self.VmInstanceId = None
        self.Tags = None
        self.Healthy = None
        self.ServiceName = None
        self.NameSpace = None
        self.ClusterId = None
        self.Source = None
        self.UniqueServiceName = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.VmInstanceId = params.get("VmInstanceId")
        self.Tags = params.get("Tags")
        self.Healthy = params.get("Healthy")
        self.ServiceName = params.get("ServiceName")
        self.NameSpace = params.get("NameSpace")
        self.ClusterId = params.get("ClusterId")
        self.Source = params.get("Source")
        self.UniqueServiceName = params.get("UniqueServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlan(AbstractModel):
    """`usagePlan` details

    """

    def __init__(self):
        r"""
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
        r"""
        :param EnvironmentName: Environment name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnvironmentName: str
        :param ServiceId: Unique service ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceId: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        :param Environment: Name of bound environment.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Environment: str
        :param InUseRequestNum: Used quota.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InUseRequestNum: int
        :param MaxRequestNum: Maximum number of requests.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxRequestNum: int
        :param MaxRequestNumPreSec: Maximum number of requests per second.
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
        r"""
        :param TotalCount: Number of environments of the service bound to usage plan.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param EnvironmentList: Environment status of services bound to usage plan.
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
        r"""
        :param UsagePlanId: Unique usage plan ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanId: str
        :param UsagePlanName: Usage plan name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanName: str
        :param UsagePlanDesc: Usage plan description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanDesc: str
        :param InitQuota: Number of initialization calls.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InitQuota: int
        :param MaxRequestNumPreSec: Limit of requests per second.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxRequestNumPreSec: int
        :param MaxRequestNum: Maximum number of calls.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxRequestNum: int
        :param IsHide: Whether to hide.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsHide: int
        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param BindSecretIdTotalCount: Number of bound keys.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BindSecretIdTotalCount: int
        :param BindSecretIds: Details of bound keys.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BindSecretIds: list of str
        :param BindEnvironmentTotalCount: Number of bound environments.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BindEnvironmentTotalCount: int
        :param BindEnvironments: Details of bound environments.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BindEnvironments: list of UsagePlanBindEnvironment
        """
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
        r"""
        :param UsagePlanId: Unique usage plan ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanId: str
        :param UsagePlanName: Custom usage plan name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanName: str
        :param UsagePlanDesc: Custom usage plan description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanDesc: str
        :param MaxRequestNumPreSec: Maximum number of requests per second.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxRequestNumPreSec: int
        :param MaxRequestNum: Total number of requests allowed. `-1` indicates no limit.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxRequestNum: int
        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        """
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
        r"""
        :param TotalCount: Number of eligible usage plans.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param UsagePlanStatusSet: Usage plan list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanStatusSet: list of UsagePlanStatusInfo
        """
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
        