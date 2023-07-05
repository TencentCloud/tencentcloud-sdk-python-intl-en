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
        :param _ApiDocId: API document ID
        :type ApiDocId: str
        :param _ApiDocName: API document name
        :type ApiDocName: str
        :param _ApiDocStatus: API document build status
        :type ApiDocStatus: str
        """
        self._ApiDocId = None
        self._ApiDocName = None
        self._ApiDocStatus = None

    @property
    def ApiDocId(self):
        return self._ApiDocId

    @ApiDocId.setter
    def ApiDocId(self, ApiDocId):
        self._ApiDocId = ApiDocId

    @property
    def ApiDocName(self):
        return self._ApiDocName

    @ApiDocName.setter
    def ApiDocName(self, ApiDocName):
        self._ApiDocName = ApiDocName

    @property
    def ApiDocStatus(self):
        return self._ApiDocStatus

    @ApiDocStatus.setter
    def ApiDocStatus(self, ApiDocStatus):
        self._ApiDocStatus = ApiDocStatus


    def _deserialize(self, params):
        self._ApiDocId = params.get("ApiDocId")
        self._ApiDocName = params.get("ApiDocName")
        self._ApiDocStatus = params.get("ApiDocStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class APIDocInfo(AbstractModel):
    """API document details

    """

    def __init__(self):
        r"""
        :param _ApiDocId: API document ID
        :type ApiDocId: str
        :param _ApiDocName: API document name
        :type ApiDocName: str
        :param _ApiDocStatus: API document build status
        :type ApiDocStatus: str
        :param _ApiCount: Number of APIs with API documents
        :type ApiCount: int
        :param _ViewCount: Number of views of API document
        :type ViewCount: int
        :param _ReleaseCount: Number of releases of API document
        :type ReleaseCount: int
        :param _ApiDocUri: API document access URI
        :type ApiDocUri: str
        :param _SharePassword: API document password for sharing
        :type SharePassword: str
        :param _UpdatedTime: API document update time
        :type UpdatedTime: str
        :param _ServiceId: Service ID
        :type ServiceId: str
        :param _Environment: Environment information
        :type Environment: str
        :param _ApiIds: ID of the API for which to generate the API document
        :type ApiIds: list of str
        :param _ServiceName: Service name
        :type ServiceName: str
        :param _ApiNames: Name of the API for which to generate the API document
        :type ApiNames: list of str
        """
        self._ApiDocId = None
        self._ApiDocName = None
        self._ApiDocStatus = None
        self._ApiCount = None
        self._ViewCount = None
        self._ReleaseCount = None
        self._ApiDocUri = None
        self._SharePassword = None
        self._UpdatedTime = None
        self._ServiceId = None
        self._Environment = None
        self._ApiIds = None
        self._ServiceName = None
        self._ApiNames = None

    @property
    def ApiDocId(self):
        return self._ApiDocId

    @ApiDocId.setter
    def ApiDocId(self, ApiDocId):
        self._ApiDocId = ApiDocId

    @property
    def ApiDocName(self):
        return self._ApiDocName

    @ApiDocName.setter
    def ApiDocName(self, ApiDocName):
        self._ApiDocName = ApiDocName

    @property
    def ApiDocStatus(self):
        return self._ApiDocStatus

    @ApiDocStatus.setter
    def ApiDocStatus(self, ApiDocStatus):
        self._ApiDocStatus = ApiDocStatus

    @property
    def ApiCount(self):
        return self._ApiCount

    @ApiCount.setter
    def ApiCount(self, ApiCount):
        self._ApiCount = ApiCount

    @property
    def ViewCount(self):
        return self._ViewCount

    @ViewCount.setter
    def ViewCount(self, ViewCount):
        self._ViewCount = ViewCount

    @property
    def ReleaseCount(self):
        return self._ReleaseCount

    @ReleaseCount.setter
    def ReleaseCount(self, ReleaseCount):
        self._ReleaseCount = ReleaseCount

    @property
    def ApiDocUri(self):
        return self._ApiDocUri

    @ApiDocUri.setter
    def ApiDocUri(self, ApiDocUri):
        self._ApiDocUri = ApiDocUri

    @property
    def SharePassword(self):
        return self._SharePassword

    @SharePassword.setter
    def SharePassword(self, SharePassword):
        self._SharePassword = SharePassword

    @property
    def UpdatedTime(self):
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ApiNames(self):
        return self._ApiNames

    @ApiNames.setter
    def ApiNames(self, ApiNames):
        self._ApiNames = ApiNames


    def _deserialize(self, params):
        self._ApiDocId = params.get("ApiDocId")
        self._ApiDocName = params.get("ApiDocName")
        self._ApiDocStatus = params.get("ApiDocStatus")
        self._ApiCount = params.get("ApiCount")
        self._ViewCount = params.get("ViewCount")
        self._ReleaseCount = params.get("ReleaseCount")
        self._ApiDocUri = params.get("ApiDocUri")
        self._SharePassword = params.get("SharePassword")
        self._UpdatedTime = params.get("UpdatedTime")
        self._ServiceId = params.get("ServiceId")
        self._Environment = params.get("Environment")
        self._ApiIds = params.get("ApiIds")
        self._ServiceName = params.get("ServiceName")
        self._ApiNames = params.get("ApiNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class APIDocs(AbstractModel):
    """API document list

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of API documents
        :type TotalCount: int
        :param _APIDocSet: Basic information of API document
        :type APIDocSet: list of APIDoc
        """
        self._TotalCount = None
        self._APIDocSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def APIDocSet(self):
        return self._APIDocSet

    @APIDocSet.setter
    def APIDocSet(self, APIDocSet):
        self._APIDocSet = APIDocSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("APIDocSet") is not None:
            self._APIDocSet = []
            for item in params.get("APIDocSet"):
                obj = APIDoc()
                obj._deserialize(item)
                self._APIDocSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiAppApiInfo(AbstractModel):
    """Information of the API bound to the application

    """

    def __init__(self):
        r"""
        :param _ApiAppName: Application name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAppName: str
        :param _ApiAppId: Application ID
        :type ApiAppId: str
        :param _ApiId: API ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiId: str
        :param _ApiName: API name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiName: str
        :param _ServiceId: Service ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceId: str
        :param _AuthorizedTime: Binding authorization time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthorizedTime: str
        :param _ApiRegion: API region
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiRegion: str
        :param _EnvironmentName: Authorized binding environment
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnvironmentName: str
        """
        self._ApiAppName = None
        self._ApiAppId = None
        self._ApiId = None
        self._ApiName = None
        self._ServiceId = None
        self._AuthorizedTime = None
        self._ApiRegion = None
        self._EnvironmentName = None

    @property
    def ApiAppName(self):
        return self._ApiAppName

    @ApiAppName.setter
    def ApiAppName(self, ApiAppName):
        self._ApiAppName = ApiAppName

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def AuthorizedTime(self):
        return self._AuthorizedTime

    @AuthorizedTime.setter
    def AuthorizedTime(self, AuthorizedTime):
        self._AuthorizedTime = AuthorizedTime

    @property
    def ApiRegion(self):
        return self._ApiRegion

    @ApiRegion.setter
    def ApiRegion(self, ApiRegion):
        self._ApiRegion = ApiRegion

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName


    def _deserialize(self, params):
        self._ApiAppName = params.get("ApiAppName")
        self._ApiAppId = params.get("ApiAppId")
        self._ApiId = params.get("ApiId")
        self._ApiName = params.get("ApiName")
        self._ServiceId = params.get("ServiceId")
        self._AuthorizedTime = params.get("AuthorizedTime")
        self._ApiRegion = params.get("ApiRegion")
        self._EnvironmentName = params.get("EnvironmentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiAppApiInfos(AbstractModel):
    """Application information set

    """

    def __init__(self):
        r"""
        :param _TotalCount: Quantity
        :type TotalCount: int
        :param _ApiAppApiSet: Information array of the API bound to the application
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAppApiSet: list of ApiAppApiInfo
        """
        self._TotalCount = None
        self._ApiAppApiSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiAppApiSet(self):
        return self._ApiAppApiSet

    @ApiAppApiSet.setter
    def ApiAppApiSet(self, ApiAppApiSet):
        self._ApiAppApiSet = ApiAppApiSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiAppApiSet") is not None:
            self._ApiAppApiSet = []
            for item in params.get("ApiAppApiSet"):
                obj = ApiAppApiInfo()
                obj._deserialize(item)
                self._ApiAppApiSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiAppInfo(AbstractModel):
    """Application information

    """

    def __init__(self):
        r"""
        :param _ApiAppName: Application name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAppName: str
        :param _ApiAppId: Application ID
        :type ApiAppId: str
        :param _ApiAppSecret: Application SECRET
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAppSecret: str
        :param _ApiAppDesc: Application description
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAppDesc: str
        :param _CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _ModifiedTime: Modification time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param _ApiAppKey: Application KEY
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAppKey: str
        """
        self._ApiAppName = None
        self._ApiAppId = None
        self._ApiAppSecret = None
        self._ApiAppDesc = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ApiAppKey = None

    @property
    def ApiAppName(self):
        return self._ApiAppName

    @ApiAppName.setter
    def ApiAppName(self, ApiAppName):
        self._ApiAppName = ApiAppName

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId

    @property
    def ApiAppSecret(self):
        return self._ApiAppSecret

    @ApiAppSecret.setter
    def ApiAppSecret(self, ApiAppSecret):
        self._ApiAppSecret = ApiAppSecret

    @property
    def ApiAppDesc(self):
        return self._ApiAppDesc

    @ApiAppDesc.setter
    def ApiAppDesc(self, ApiAppDesc):
        self._ApiAppDesc = ApiAppDesc

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ApiAppKey(self):
        return self._ApiAppKey

    @ApiAppKey.setter
    def ApiAppKey(self, ApiAppKey):
        self._ApiAppKey = ApiAppKey


    def _deserialize(self, params):
        self._ApiAppName = params.get("ApiAppName")
        self._ApiAppId = params.get("ApiAppId")
        self._ApiAppSecret = params.get("ApiAppSecret")
        self._ApiAppDesc = params.get("ApiAppDesc")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ApiAppKey = params.get("ApiAppKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiAppInfos(AbstractModel):
    """Application information set

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of applications
        :type TotalCount: int
        :param _ApiAppSet: Application information array
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAppSet: list of ApiAppInfo
        """
        self._TotalCount = None
        self._ApiAppSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiAppSet(self):
        return self._ApiAppSet

    @ApiAppSet.setter
    def ApiAppSet(self, ApiAppSet):
        self._ApiAppSet = ApiAppSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiAppSet") is not None:
            self._ApiAppSet = []
            for item in params.get("ApiAppSet"):
                obj = ApiAppInfo()
                obj._deserialize(item)
                self._ApiAppSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiEnvironmentStrategy(AbstractModel):
    """API environment binding policy

    """

    def __init__(self):
        r"""
        :param _ApiId: Unique API ID.
        :type ApiId: str
        :param _ApiName: Custom API name.
        :type ApiName: str
        :param _Path: API path, such as `/path`.
        :type Path: str
        :param _Method: API method, such as `GET`.
        :type Method: str
        :param _EnvironmentStrategySet: Environment throttling information.
        :type EnvironmentStrategySet: list of EnvironmentStrategy
        """
        self._ApiId = None
        self._ApiName = None
        self._Path = None
        self._Method = None
        self._EnvironmentStrategySet = None

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def EnvironmentStrategySet(self):
        return self._EnvironmentStrategySet

    @EnvironmentStrategySet.setter
    def EnvironmentStrategySet(self, EnvironmentStrategySet):
        self._EnvironmentStrategySet = EnvironmentStrategySet


    def _deserialize(self, params):
        self._ApiId = params.get("ApiId")
        self._ApiName = params.get("ApiName")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        if params.get("EnvironmentStrategySet") is not None:
            self._EnvironmentStrategySet = []
            for item in params.get("EnvironmentStrategySet"):
                obj = EnvironmentStrategy()
                obj._deserialize(item)
                self._EnvironmentStrategySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiEnvironmentStrategyStataus(AbstractModel):
    """List of policies bound to API

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of throttling policies bound to API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _ApiEnvironmentStrategySet: List of throttling policies bound to API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiEnvironmentStrategySet: list of ApiEnvironmentStrategy
        """
        self._TotalCount = None
        self._ApiEnvironmentStrategySet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiEnvironmentStrategySet(self):
        return self._ApiEnvironmentStrategySet

    @ApiEnvironmentStrategySet.setter
    def ApiEnvironmentStrategySet(self, ApiEnvironmentStrategySet):
        self._ApiEnvironmentStrategySet = ApiEnvironmentStrategySet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiEnvironmentStrategySet") is not None:
            self._ApiEnvironmentStrategySet = []
            for item in params.get("ApiEnvironmentStrategySet"):
                obj = ApiEnvironmentStrategy()
                obj._deserialize(item)
                self._ApiEnvironmentStrategySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiIdStatus(AbstractModel):
    """API status

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _ApiId: Unique API ID.
        :type ApiId: str
        :param _ApiDesc: API description
        :type ApiDesc: str
        :param _Path: API path.
        :type Path: str
        :param _Method: API method.
        :type Method: str
        :param _CreatedTime: Service creation time.
        :type CreatedTime: str
        :param _ModifiedTime: Service modification time.
        :type ModifiedTime: str
        :param _ApiName: API name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiName: str
        :param _UniqVpcId: Unique VPC ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UniqVpcId: str
        :param _ApiType: API type.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiType: str
        :param _Protocol: API protocol.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _IsDebugAfterCharge: Whether to enable debugging after purchase.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDebugAfterCharge: bool
        :param _AuthType: Authorization type.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthType: str
        :param _ApiBusinessType: API business type.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiBusinessType: str
        :param _AuthRelationApiId: Unique ID of associated authorization API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthRelationApiId: str
        :param _RelationBuniessApiIds: List of business APIs associated with authorization API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RelationBuniessApiIds: list of str
        :param _OauthConfig: OAuth configuration information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param _TokenLocation: Token storage position, which is an OAuth 2.0 API request.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TokenLocation: str
        """
        self._ServiceId = None
        self._ApiId = None
        self._ApiDesc = None
        self._Path = None
        self._Method = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ApiName = None
        self._UniqVpcId = None
        self._ApiType = None
        self._Protocol = None
        self._IsDebugAfterCharge = None
        self._AuthType = None
        self._ApiBusinessType = None
        self._AuthRelationApiId = None
        self._RelationBuniessApiIds = None
        self._OauthConfig = None
        self._TokenLocation = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiDesc(self):
        return self._ApiDesc

    @ApiDesc.setter
    def ApiDesc(self, ApiDesc):
        self._ApiDesc = ApiDesc

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def ApiType(self):
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def IsDebugAfterCharge(self):
        return self._IsDebugAfterCharge

    @IsDebugAfterCharge.setter
    def IsDebugAfterCharge(self, IsDebugAfterCharge):
        self._IsDebugAfterCharge = IsDebugAfterCharge

    @property
    def AuthType(self):
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ApiBusinessType(self):
        return self._ApiBusinessType

    @ApiBusinessType.setter
    def ApiBusinessType(self, ApiBusinessType):
        self._ApiBusinessType = ApiBusinessType

    @property
    def AuthRelationApiId(self):
        return self._AuthRelationApiId

    @AuthRelationApiId.setter
    def AuthRelationApiId(self, AuthRelationApiId):
        self._AuthRelationApiId = AuthRelationApiId

    @property
    def RelationBuniessApiIds(self):
        return self._RelationBuniessApiIds

    @RelationBuniessApiIds.setter
    def RelationBuniessApiIds(self, RelationBuniessApiIds):
        self._RelationBuniessApiIds = RelationBuniessApiIds

    @property
    def OauthConfig(self):
        return self._OauthConfig

    @OauthConfig.setter
    def OauthConfig(self, OauthConfig):
        self._OauthConfig = OauthConfig

    @property
    def TokenLocation(self):
        return self._TokenLocation

    @TokenLocation.setter
    def TokenLocation(self, TokenLocation):
        self._TokenLocation = TokenLocation


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        self._ApiDesc = params.get("ApiDesc")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ApiName = params.get("ApiName")
        self._UniqVpcId = params.get("UniqVpcId")
        self._ApiType = params.get("ApiType")
        self._Protocol = params.get("Protocol")
        self._IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        self._AuthType = params.get("AuthType")
        self._ApiBusinessType = params.get("ApiBusinessType")
        self._AuthRelationApiId = params.get("AuthRelationApiId")
        self._RelationBuniessApiIds = params.get("RelationBuniessApiIds")
        if params.get("OauthConfig") is not None:
            self._OauthConfig = OauthConfig()
            self._OauthConfig._deserialize(params.get("OauthConfig"))
        self._TokenLocation = params.get("TokenLocation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiInfo(AbstractModel):
    """API information

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID of API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceId: str
        :param _ServiceName: Service name of API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceName: str
        :param _ServiceDesc: Service description of API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceDesc: str
        :param _ApiId: Unique API ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiId: str
        :param _ApiDesc: API description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiDesc: str
        :param _CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param _ApiName: API name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiName: str
        :param _ApiType: API type. Valid values: NORMAL (general API), TSF (microservice API).
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiType: str
        :param _Protocol: API frontend request type, such as HTTP, HTTPS, or HTTP and HTTPS.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _AuthType: API authentication type. Valid values: SECRET (key pair authentication), NONE (no authentication), OAUTH.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthType: str
        :param _ApiBusinessType: OAuth API type. Valid values: NORMAL (business API), OAUTH (authorization API).
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiBusinessType: str
        :param _AuthRelationApiId: Unique ID of the authorization API associated with OAuth business API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthRelationApiId: str
        :param _OauthConfig: OAuth configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param _IsDebugAfterCharge: Whether to enable debugging after purchase (reserved field for the marketplace).
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDebugAfterCharge: bool
        :param _RequestConfig: Request frontend configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.RequestConfig`
        :param _ResponseType: Return type.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseType: str
        :param _ResponseSuccessExample: Sample response for successful custom response configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseSuccessExample: str
        :param _ResponseFailExample: Sample response for failed custom response configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseFailExample: str
        :param _ResponseErrorCodes: Custom error code configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseErrorCodes: list of ErrorCodes
        :param _RequestParameters: Frontend request parameter.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RequestParameters: list of ReqParameter
        :param _ServiceTimeout: API backend service timeout period in seconds.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceTimeout: int
        :param _ServiceType: API backend service type. Valid values: HTTP, MOCK, TSF, CLB, SCF, WEBSOCKET, TARGET (in beta test).
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceType: str
        :param _ServiceConfig: API backend service configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`
        :param _ServiceParameters: API backend service parameter.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceParameters: list of ServiceParameter
        :param _ConstantParameters: Constant parameter.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ConstantParameters: list of ConstantParameter
        :param _ServiceMockReturnMessage: Returned message of API backend Mock, which is required if `ServiceType` is `Mock`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceMockReturnMessage: str
        :param _ServiceScfFunctionName: SCF function name, which takes effect if the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceScfFunctionName: str
        :param _ServiceScfFunctionNamespace: SCF function namespace, which takes effect if the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceScfFunctionNamespace: str
        :param _ServiceScfFunctionQualifier: SCF function version, which takes effect if the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceScfFunctionQualifier: str
        :param _ServiceScfIsIntegratedResponse: Whether integrated response is enabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceScfIsIntegratedResponse: bool
        :param _ServiceWebsocketRegisterFunctionName: SCF WebSocket registration function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketRegisterFunctionName: str
        :param _ServiceWebsocketRegisterFunctionNamespace: SCF WebSocket registration function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketRegisterFunctionNamespace: str
        :param _ServiceWebsocketRegisterFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketRegisterFunctionQualifier: str
        :param _ServiceWebsocketCleanupFunctionName: SCF WebSocket cleanup function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketCleanupFunctionName: str
        :param _ServiceWebsocketCleanupFunctionNamespace: SCF WebSocket cleanup function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketCleanupFunctionNamespace: str
        :param _ServiceWebsocketCleanupFunctionQualifier: SCF WebSocket cleanup function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketCleanupFunctionQualifier: str
        :param _InternalDomain: WebSocket callback address.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InternalDomain: str
        :param _ServiceWebsocketTransportFunctionName: SCF WebSocket transfer function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketTransportFunctionName: str
        :param _ServiceWebsocketTransportFunctionNamespace: SCF WebSocket transfer function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketTransportFunctionNamespace: str
        :param _ServiceWebsocketTransportFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceWebsocketTransportFunctionQualifier: str
        :param _MicroServices: List of microservices bound to API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MicroServices: list of MicroService
        :param _MicroServicesInfo: Microservice details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MicroServicesInfo: list of int
        :param _ServiceTsfLoadBalanceConf: Load balancing configuration of microservice.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`
        :param _ServiceTsfHealthCheckConf: Health check configuration of microservice.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param _EnableCORS: Whether to enable CORS.
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnableCORS: bool
        :param _Tags: Information of tags bound to API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _Environments: Environment information published for API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Environments: list of str
        :param _IsBase64Encoded: Whether to enable Base64 encoding. This parameter takes effect only when the backend is SCF.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsBase64Encoded: bool
        :param _IsBase64Trigger: Whether to trigger Base64 encoding by header. This parameter takes effect only when the backend is SCF.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsBase64Trigger: bool
        :param _Base64EncodedTriggerRules: Header trigger rules. The number of rules cannot exceed 10.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Base64EncodedTriggerRules: list of Base64EncodedTriggerRule
        """
        self._ServiceId = None
        self._ServiceName = None
        self._ServiceDesc = None
        self._ApiId = None
        self._ApiDesc = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ApiName = None
        self._ApiType = None
        self._Protocol = None
        self._AuthType = None
        self._ApiBusinessType = None
        self._AuthRelationApiId = None
        self._OauthConfig = None
        self._IsDebugAfterCharge = None
        self._RequestConfig = None
        self._ResponseType = None
        self._ResponseSuccessExample = None
        self._ResponseFailExample = None
        self._ResponseErrorCodes = None
        self._RequestParameters = None
        self._ServiceTimeout = None
        self._ServiceType = None
        self._ServiceConfig = None
        self._ServiceParameters = None
        self._ConstantParameters = None
        self._ServiceMockReturnMessage = None
        self._ServiceScfFunctionName = None
        self._ServiceScfFunctionNamespace = None
        self._ServiceScfFunctionQualifier = None
        self._ServiceScfIsIntegratedResponse = None
        self._ServiceWebsocketRegisterFunctionName = None
        self._ServiceWebsocketRegisterFunctionNamespace = None
        self._ServiceWebsocketRegisterFunctionQualifier = None
        self._ServiceWebsocketCleanupFunctionName = None
        self._ServiceWebsocketCleanupFunctionNamespace = None
        self._ServiceWebsocketCleanupFunctionQualifier = None
        self._InternalDomain = None
        self._ServiceWebsocketTransportFunctionName = None
        self._ServiceWebsocketTransportFunctionNamespace = None
        self._ServiceWebsocketTransportFunctionQualifier = None
        self._MicroServices = None
        self._MicroServicesInfo = None
        self._ServiceTsfLoadBalanceConf = None
        self._ServiceTsfHealthCheckConf = None
        self._EnableCORS = None
        self._Tags = None
        self._Environments = None
        self._IsBase64Encoded = None
        self._IsBase64Trigger = None
        self._Base64EncodedTriggerRules = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceDesc(self):
        return self._ServiceDesc

    @ServiceDesc.setter
    def ServiceDesc(self, ServiceDesc):
        self._ServiceDesc = ServiceDesc

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiDesc(self):
        return self._ApiDesc

    @ApiDesc.setter
    def ApiDesc(self, ApiDesc):
        self._ApiDesc = ApiDesc

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def ApiType(self):
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def AuthType(self):
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ApiBusinessType(self):
        return self._ApiBusinessType

    @ApiBusinessType.setter
    def ApiBusinessType(self, ApiBusinessType):
        self._ApiBusinessType = ApiBusinessType

    @property
    def AuthRelationApiId(self):
        return self._AuthRelationApiId

    @AuthRelationApiId.setter
    def AuthRelationApiId(self, AuthRelationApiId):
        self._AuthRelationApiId = AuthRelationApiId

    @property
    def OauthConfig(self):
        return self._OauthConfig

    @OauthConfig.setter
    def OauthConfig(self, OauthConfig):
        self._OauthConfig = OauthConfig

    @property
    def IsDebugAfterCharge(self):
        return self._IsDebugAfterCharge

    @IsDebugAfterCharge.setter
    def IsDebugAfterCharge(self, IsDebugAfterCharge):
        self._IsDebugAfterCharge = IsDebugAfterCharge

    @property
    def RequestConfig(self):
        return self._RequestConfig

    @RequestConfig.setter
    def RequestConfig(self, RequestConfig):
        self._RequestConfig = RequestConfig

    @property
    def ResponseType(self):
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseSuccessExample(self):
        return self._ResponseSuccessExample

    @ResponseSuccessExample.setter
    def ResponseSuccessExample(self, ResponseSuccessExample):
        self._ResponseSuccessExample = ResponseSuccessExample

    @property
    def ResponseFailExample(self):
        return self._ResponseFailExample

    @ResponseFailExample.setter
    def ResponseFailExample(self, ResponseFailExample):
        self._ResponseFailExample = ResponseFailExample

    @property
    def ResponseErrorCodes(self):
        return self._ResponseErrorCodes

    @ResponseErrorCodes.setter
    def ResponseErrorCodes(self, ResponseErrorCodes):
        self._ResponseErrorCodes = ResponseErrorCodes

    @property
    def RequestParameters(self):
        return self._RequestParameters

    @RequestParameters.setter
    def RequestParameters(self, RequestParameters):
        self._RequestParameters = RequestParameters

    @property
    def ServiceTimeout(self):
        return self._ServiceTimeout

    @ServiceTimeout.setter
    def ServiceTimeout(self, ServiceTimeout):
        self._ServiceTimeout = ServiceTimeout

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ServiceConfig(self):
        return self._ServiceConfig

    @ServiceConfig.setter
    def ServiceConfig(self, ServiceConfig):
        self._ServiceConfig = ServiceConfig

    @property
    def ServiceParameters(self):
        return self._ServiceParameters

    @ServiceParameters.setter
    def ServiceParameters(self, ServiceParameters):
        self._ServiceParameters = ServiceParameters

    @property
    def ConstantParameters(self):
        return self._ConstantParameters

    @ConstantParameters.setter
    def ConstantParameters(self, ConstantParameters):
        self._ConstantParameters = ConstantParameters

    @property
    def ServiceMockReturnMessage(self):
        return self._ServiceMockReturnMessage

    @ServiceMockReturnMessage.setter
    def ServiceMockReturnMessage(self, ServiceMockReturnMessage):
        self._ServiceMockReturnMessage = ServiceMockReturnMessage

    @property
    def ServiceScfFunctionName(self):
        return self._ServiceScfFunctionName

    @ServiceScfFunctionName.setter
    def ServiceScfFunctionName(self, ServiceScfFunctionName):
        self._ServiceScfFunctionName = ServiceScfFunctionName

    @property
    def ServiceScfFunctionNamespace(self):
        return self._ServiceScfFunctionNamespace

    @ServiceScfFunctionNamespace.setter
    def ServiceScfFunctionNamespace(self, ServiceScfFunctionNamespace):
        self._ServiceScfFunctionNamespace = ServiceScfFunctionNamespace

    @property
    def ServiceScfFunctionQualifier(self):
        return self._ServiceScfFunctionQualifier

    @ServiceScfFunctionQualifier.setter
    def ServiceScfFunctionQualifier(self, ServiceScfFunctionQualifier):
        self._ServiceScfFunctionQualifier = ServiceScfFunctionQualifier

    @property
    def ServiceScfIsIntegratedResponse(self):
        return self._ServiceScfIsIntegratedResponse

    @ServiceScfIsIntegratedResponse.setter
    def ServiceScfIsIntegratedResponse(self, ServiceScfIsIntegratedResponse):
        self._ServiceScfIsIntegratedResponse = ServiceScfIsIntegratedResponse

    @property
    def ServiceWebsocketRegisterFunctionName(self):
        return self._ServiceWebsocketRegisterFunctionName

    @ServiceWebsocketRegisterFunctionName.setter
    def ServiceWebsocketRegisterFunctionName(self, ServiceWebsocketRegisterFunctionName):
        self._ServiceWebsocketRegisterFunctionName = ServiceWebsocketRegisterFunctionName

    @property
    def ServiceWebsocketRegisterFunctionNamespace(self):
        return self._ServiceWebsocketRegisterFunctionNamespace

    @ServiceWebsocketRegisterFunctionNamespace.setter
    def ServiceWebsocketRegisterFunctionNamespace(self, ServiceWebsocketRegisterFunctionNamespace):
        self._ServiceWebsocketRegisterFunctionNamespace = ServiceWebsocketRegisterFunctionNamespace

    @property
    def ServiceWebsocketRegisterFunctionQualifier(self):
        return self._ServiceWebsocketRegisterFunctionQualifier

    @ServiceWebsocketRegisterFunctionQualifier.setter
    def ServiceWebsocketRegisterFunctionQualifier(self, ServiceWebsocketRegisterFunctionQualifier):
        self._ServiceWebsocketRegisterFunctionQualifier = ServiceWebsocketRegisterFunctionQualifier

    @property
    def ServiceWebsocketCleanupFunctionName(self):
        return self._ServiceWebsocketCleanupFunctionName

    @ServiceWebsocketCleanupFunctionName.setter
    def ServiceWebsocketCleanupFunctionName(self, ServiceWebsocketCleanupFunctionName):
        self._ServiceWebsocketCleanupFunctionName = ServiceWebsocketCleanupFunctionName

    @property
    def ServiceWebsocketCleanupFunctionNamespace(self):
        return self._ServiceWebsocketCleanupFunctionNamespace

    @ServiceWebsocketCleanupFunctionNamespace.setter
    def ServiceWebsocketCleanupFunctionNamespace(self, ServiceWebsocketCleanupFunctionNamespace):
        self._ServiceWebsocketCleanupFunctionNamespace = ServiceWebsocketCleanupFunctionNamespace

    @property
    def ServiceWebsocketCleanupFunctionQualifier(self):
        return self._ServiceWebsocketCleanupFunctionQualifier

    @ServiceWebsocketCleanupFunctionQualifier.setter
    def ServiceWebsocketCleanupFunctionQualifier(self, ServiceWebsocketCleanupFunctionQualifier):
        self._ServiceWebsocketCleanupFunctionQualifier = ServiceWebsocketCleanupFunctionQualifier

    @property
    def InternalDomain(self):
        return self._InternalDomain

    @InternalDomain.setter
    def InternalDomain(self, InternalDomain):
        self._InternalDomain = InternalDomain

    @property
    def ServiceWebsocketTransportFunctionName(self):
        return self._ServiceWebsocketTransportFunctionName

    @ServiceWebsocketTransportFunctionName.setter
    def ServiceWebsocketTransportFunctionName(self, ServiceWebsocketTransportFunctionName):
        self._ServiceWebsocketTransportFunctionName = ServiceWebsocketTransportFunctionName

    @property
    def ServiceWebsocketTransportFunctionNamespace(self):
        return self._ServiceWebsocketTransportFunctionNamespace

    @ServiceWebsocketTransportFunctionNamespace.setter
    def ServiceWebsocketTransportFunctionNamespace(self, ServiceWebsocketTransportFunctionNamespace):
        self._ServiceWebsocketTransportFunctionNamespace = ServiceWebsocketTransportFunctionNamespace

    @property
    def ServiceWebsocketTransportFunctionQualifier(self):
        return self._ServiceWebsocketTransportFunctionQualifier

    @ServiceWebsocketTransportFunctionQualifier.setter
    def ServiceWebsocketTransportFunctionQualifier(self, ServiceWebsocketTransportFunctionQualifier):
        self._ServiceWebsocketTransportFunctionQualifier = ServiceWebsocketTransportFunctionQualifier

    @property
    def MicroServices(self):
        return self._MicroServices

    @MicroServices.setter
    def MicroServices(self, MicroServices):
        self._MicroServices = MicroServices

    @property
    def MicroServicesInfo(self):
        return self._MicroServicesInfo

    @MicroServicesInfo.setter
    def MicroServicesInfo(self, MicroServicesInfo):
        self._MicroServicesInfo = MicroServicesInfo

    @property
    def ServiceTsfLoadBalanceConf(self):
        return self._ServiceTsfLoadBalanceConf

    @ServiceTsfLoadBalanceConf.setter
    def ServiceTsfLoadBalanceConf(self, ServiceTsfLoadBalanceConf):
        self._ServiceTsfLoadBalanceConf = ServiceTsfLoadBalanceConf

    @property
    def ServiceTsfHealthCheckConf(self):
        return self._ServiceTsfHealthCheckConf

    @ServiceTsfHealthCheckConf.setter
    def ServiceTsfHealthCheckConf(self, ServiceTsfHealthCheckConf):
        self._ServiceTsfHealthCheckConf = ServiceTsfHealthCheckConf

    @property
    def EnableCORS(self):
        return self._EnableCORS

    @EnableCORS.setter
    def EnableCORS(self, EnableCORS):
        self._EnableCORS = EnableCORS

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Environments(self):
        return self._Environments

    @Environments.setter
    def Environments(self, Environments):
        self._Environments = Environments

    @property
    def IsBase64Encoded(self):
        return self._IsBase64Encoded

    @IsBase64Encoded.setter
    def IsBase64Encoded(self, IsBase64Encoded):
        self._IsBase64Encoded = IsBase64Encoded

    @property
    def IsBase64Trigger(self):
        return self._IsBase64Trigger

    @IsBase64Trigger.setter
    def IsBase64Trigger(self, IsBase64Trigger):
        self._IsBase64Trigger = IsBase64Trigger

    @property
    def Base64EncodedTriggerRules(self):
        return self._Base64EncodedTriggerRules

    @Base64EncodedTriggerRules.setter
    def Base64EncodedTriggerRules(self, Base64EncodedTriggerRules):
        self._Base64EncodedTriggerRules = Base64EncodedTriggerRules


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceName = params.get("ServiceName")
        self._ServiceDesc = params.get("ServiceDesc")
        self._ApiId = params.get("ApiId")
        self._ApiDesc = params.get("ApiDesc")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ApiName = params.get("ApiName")
        self._ApiType = params.get("ApiType")
        self._Protocol = params.get("Protocol")
        self._AuthType = params.get("AuthType")
        self._ApiBusinessType = params.get("ApiBusinessType")
        self._AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("OauthConfig") is not None:
            self._OauthConfig = OauthConfig()
            self._OauthConfig._deserialize(params.get("OauthConfig"))
        self._IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        if params.get("RequestConfig") is not None:
            self._RequestConfig = RequestConfig()
            self._RequestConfig._deserialize(params.get("RequestConfig"))
        self._ResponseType = params.get("ResponseType")
        self._ResponseSuccessExample = params.get("ResponseSuccessExample")
        self._ResponseFailExample = params.get("ResponseFailExample")
        if params.get("ResponseErrorCodes") is not None:
            self._ResponseErrorCodes = []
            for item in params.get("ResponseErrorCodes"):
                obj = ErrorCodes()
                obj._deserialize(item)
                self._ResponseErrorCodes.append(obj)
        if params.get("RequestParameters") is not None:
            self._RequestParameters = []
            for item in params.get("RequestParameters"):
                obj = ReqParameter()
                obj._deserialize(item)
                self._RequestParameters.append(obj)
        self._ServiceTimeout = params.get("ServiceTimeout")
        self._ServiceType = params.get("ServiceType")
        if params.get("ServiceConfig") is not None:
            self._ServiceConfig = ServiceConfig()
            self._ServiceConfig._deserialize(params.get("ServiceConfig"))
        if params.get("ServiceParameters") is not None:
            self._ServiceParameters = []
            for item in params.get("ServiceParameters"):
                obj = ServiceParameter()
                obj._deserialize(item)
                self._ServiceParameters.append(obj)
        if params.get("ConstantParameters") is not None:
            self._ConstantParameters = []
            for item in params.get("ConstantParameters"):
                obj = ConstantParameter()
                obj._deserialize(item)
                self._ConstantParameters.append(obj)
        self._ServiceMockReturnMessage = params.get("ServiceMockReturnMessage")
        self._ServiceScfFunctionName = params.get("ServiceScfFunctionName")
        self._ServiceScfFunctionNamespace = params.get("ServiceScfFunctionNamespace")
        self._ServiceScfFunctionQualifier = params.get("ServiceScfFunctionQualifier")
        self._ServiceScfIsIntegratedResponse = params.get("ServiceScfIsIntegratedResponse")
        self._ServiceWebsocketRegisterFunctionName = params.get("ServiceWebsocketRegisterFunctionName")
        self._ServiceWebsocketRegisterFunctionNamespace = params.get("ServiceWebsocketRegisterFunctionNamespace")
        self._ServiceWebsocketRegisterFunctionQualifier = params.get("ServiceWebsocketRegisterFunctionQualifier")
        self._ServiceWebsocketCleanupFunctionName = params.get("ServiceWebsocketCleanupFunctionName")
        self._ServiceWebsocketCleanupFunctionNamespace = params.get("ServiceWebsocketCleanupFunctionNamespace")
        self._ServiceWebsocketCleanupFunctionQualifier = params.get("ServiceWebsocketCleanupFunctionQualifier")
        self._InternalDomain = params.get("InternalDomain")
        self._ServiceWebsocketTransportFunctionName = params.get("ServiceWebsocketTransportFunctionName")
        self._ServiceWebsocketTransportFunctionNamespace = params.get("ServiceWebsocketTransportFunctionNamespace")
        self._ServiceWebsocketTransportFunctionQualifier = params.get("ServiceWebsocketTransportFunctionQualifier")
        if params.get("MicroServices") is not None:
            self._MicroServices = []
            for item in params.get("MicroServices"):
                obj = MicroService()
                obj._deserialize(item)
                self._MicroServices.append(obj)
        self._MicroServicesInfo = params.get("MicroServicesInfo")
        if params.get("ServiceTsfLoadBalanceConf") is not None:
            self._ServiceTsfLoadBalanceConf = TsfLoadBalanceConfResp()
            self._ServiceTsfLoadBalanceConf._deserialize(params.get("ServiceTsfLoadBalanceConf"))
        if params.get("ServiceTsfHealthCheckConf") is not None:
            self._ServiceTsfHealthCheckConf = HealthCheckConf()
            self._ServiceTsfHealthCheckConf._deserialize(params.get("ServiceTsfHealthCheckConf"))
        self._EnableCORS = params.get("EnableCORS")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Environments = params.get("Environments")
        self._IsBase64Encoded = params.get("IsBase64Encoded")
        self._IsBase64Trigger = params.get("IsBase64Trigger")
        if params.get("Base64EncodedTriggerRules") is not None:
            self._Base64EncodedTriggerRules = []
            for item in params.get("Base64EncodedTriggerRules"):
                obj = Base64EncodedTriggerRule()
                obj._deserialize(item)
                self._Base64EncodedTriggerRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiInfoSummary(AbstractModel):
    """Information of the APIs that can use this plugin

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of APIs that can use this plugin
        :type TotalCount: int
        :param _ApiSet: Information of the APIs that can use this plugin
        :type ApiSet: list of AvailableApiInfo
        """
        self._TotalCount = None
        self._ApiSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiSet(self):
        return self._ApiSet

    @ApiSet.setter
    def ApiSet(self, ApiSet):
        self._ApiSet = ApiSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiSet") is not None:
            self._ApiSet = []
            for item in params.get("ApiSet"):
                obj = AvailableApiInfo()
                obj._deserialize(item)
                self._ApiSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiKey(AbstractModel):
    """Key details

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: Created API key ID.
        :type AccessKeyId: str
        :param _AccessKeySecret: Created API key.
        :type AccessKeySecret: str
        :param _AccessKeyType: Key type. Valid values: auto, manual.
        :type AccessKeyType: str
        :param _SecretName: Custom key name.
        :type SecretName: str
        :param _ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
        :type ModifiedTime: str
        :param _Status: Key status. 0: disabled. 1: enabled.
        :type Status: int
        :param _CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
        :type CreatedTime: str
        """
        self._AccessKeyId = None
        self._AccessKeySecret = None
        self._AccessKeyType = None
        self._SecretName = None
        self._ModifiedTime = None
        self._Status = None
        self._CreatedTime = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def AccessKeySecret(self):
        return self._AccessKeySecret

    @AccessKeySecret.setter
    def AccessKeySecret(self, AccessKeySecret):
        self._AccessKeySecret = AccessKeySecret

    @property
    def AccessKeyType(self):
        return self._AccessKeyType

    @AccessKeyType.setter
    def AccessKeyType(self, AccessKeyType):
        self._AccessKeyType = AccessKeyType

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        self._AccessKeySecret = params.get("AccessKeySecret")
        self._AccessKeyType = params.get("AccessKeyType")
        self._SecretName = params.get("SecretName")
        self._ModifiedTime = params.get("ModifiedTime")
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiKeysStatus(AbstractModel):
    """Key list

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible API keys.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _ApiKeySet: API key list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiKeySet: list of ApiKey
        """
        self._TotalCount = None
        self._ApiKeySet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiKeySet(self):
        return self._ApiKeySet

    @ApiKeySet.setter
    def ApiKeySet(self, ApiKeySet):
        self._ApiKeySet = ApiKeySet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiKeySet") is not None:
            self._ApiKeySet = []
            for item in params.get("ApiKeySet"):
                obj = ApiKey()
                obj._deserialize(item)
                self._ApiKeySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiRequestConfig(AbstractModel):
    """API request configuration

    """

    def __init__(self):
        r"""
        :param _Path: path
        :type Path: str
        :param _Method: Method
        :type Method: str
        """
        self._Path = None
        self._Method = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiUsagePlan(AbstractModel):
    """Details of usage plans bound to API or service

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceId: str
        :param _ApiId: Unique API ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiId: str
        :param _ApiName: API name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiName: str
        :param _Path: API path.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Path: str
        :param _Method: API method.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Method: str
        :param _UsagePlanId: Unique usage plan ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanId: str
        :param _UsagePlanName: Usage plan name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanName: str
        :param _UsagePlanDesc: Usage plan description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanDesc: str
        :param _Environment: Service environment bound to usage plan.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Environment: str
        :param _InUseRequestNum: Used quota.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InUseRequestNum: int
        :param _MaxRequestNum: Total number of requests allowed. `-1` indicates no limit.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxRequestNum: int
        :param _MaxRequestNumPreSec: Request QPS upper limit. `-1` indicates no limit.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxRequestNumPreSec: int
        :param _CreatedTime: Usage plan creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _ModifiedTime: Last modified time of usage plan.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param _ServiceName: Service name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceName: str
        """
        self._ServiceId = None
        self._ApiId = None
        self._ApiName = None
        self._Path = None
        self._Method = None
        self._UsagePlanId = None
        self._UsagePlanName = None
        self._UsagePlanDesc = None
        self._Environment = None
        self._InUseRequestNum = None
        self._MaxRequestNum = None
        self._MaxRequestNumPreSec = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ServiceName = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def UsagePlanName(self):
        return self._UsagePlanName

    @UsagePlanName.setter
    def UsagePlanName(self, UsagePlanName):
        self._UsagePlanName = UsagePlanName

    @property
    def UsagePlanDesc(self):
        return self._UsagePlanDesc

    @UsagePlanDesc.setter
    def UsagePlanDesc(self, UsagePlanDesc):
        self._UsagePlanDesc = UsagePlanDesc

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def InUseRequestNum(self):
        return self._InUseRequestNum

    @InUseRequestNum.setter
    def InUseRequestNum(self, InUseRequestNum):
        self._InUseRequestNum = InUseRequestNum

    @property
    def MaxRequestNum(self):
        return self._MaxRequestNum

    @MaxRequestNum.setter
    def MaxRequestNum(self, MaxRequestNum):
        self._MaxRequestNum = MaxRequestNum

    @property
    def MaxRequestNumPreSec(self):
        return self._MaxRequestNumPreSec

    @MaxRequestNumPreSec.setter
    def MaxRequestNumPreSec(self, MaxRequestNumPreSec):
        self._MaxRequestNumPreSec = MaxRequestNumPreSec

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        self._ApiName = params.get("ApiName")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        self._UsagePlanId = params.get("UsagePlanId")
        self._UsagePlanName = params.get("UsagePlanName")
        self._UsagePlanDesc = params.get("UsagePlanDesc")
        self._Environment = params.get("Environment")
        self._InUseRequestNum = params.get("InUseRequestNum")
        self._MaxRequestNum = params.get("MaxRequestNum")
        self._MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiUsagePlanSet(AbstractModel):
    """List of usage plans bound to API

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of usage plans bound to API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _ApiUsagePlanList: List of usage plans bound to API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiUsagePlanList: list of ApiUsagePlan
        """
        self._TotalCount = None
        self._ApiUsagePlanList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiUsagePlanList(self):
        return self._ApiUsagePlanList

    @ApiUsagePlanList.setter
    def ApiUsagePlanList(self, ApiUsagePlanList):
        self._ApiUsagePlanList = ApiUsagePlanList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiUsagePlanList") is not None:
            self._ApiUsagePlanList = []
            for item in params.get("ApiUsagePlanList"):
                obj = ApiUsagePlan()
                obj._deserialize(item)
                self._ApiUsagePlanList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApisStatus(AbstractModel):
    """API list status description

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible APIs.
        :type TotalCount: int
        :param _ApiIdStatusSet: API list.
        :type ApiIdStatusSet: list of DesApisStatus
        """
        self._TotalCount = None
        self._ApiIdStatusSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiIdStatusSet(self):
        return self._ApiIdStatusSet

    @ApiIdStatusSet.setter
    def ApiIdStatusSet(self, ApiIdStatusSet):
        self._ApiIdStatusSet = ApiIdStatusSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiIdStatusSet") is not None:
            self._ApiIdStatusSet = []
            for item in params.get("ApiIdStatusSet"):
                obj = DesApisStatus()
                obj._deserialize(item)
                self._ApiIdStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachPluginRequest(AbstractModel):
    """AttachPlugin request structure.

    """

    def __init__(self):
        r"""
        :param _PluginId: ID of the plugin to be bound
        :type PluginId: str
        :param _ServiceId: Service ID
        :type ServiceId: str
        :param _EnvironmentName: API environment
        :type EnvironmentName: str
        :param _ApiIds: List of APIs bound with the plugin
        :type ApiIds: list of str
        """
        self._PluginId = None
        self._ServiceId = None
        self._EnvironmentName = None
        self._ApiIds = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._ServiceId = params.get("ServiceId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachPluginResponse(AbstractModel):
    """AttachPlugin response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether binding succeeded.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class AttachedApiInfo(AbstractModel):
    """Information of the API bound with the plugin

    """

    def __init__(self):
        r"""
        :param _ServiceId: ID of the service to which the API belongs
        :type ServiceId: str
        :param _ServiceName: Name of the service to which the API belongs
        :type ServiceName: str
        :param _ServiceDesc: Description of the service to which the API belongs
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceDesc: str
        :param _ApiId: API ID
        :type ApiId: str
        :param _ApiName: API name
        :type ApiName: str
        :param _ApiDesc: API description
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiDesc: str
        :param _Environment: Environment of the API bound with the plugin
        :type Environment: str
        :param _AttachedTime: Time when the plugin was bound to the API
        :type AttachedTime: str
        """
        self._ServiceId = None
        self._ServiceName = None
        self._ServiceDesc = None
        self._ApiId = None
        self._ApiName = None
        self._ApiDesc = None
        self._Environment = None
        self._AttachedTime = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceDesc(self):
        return self._ServiceDesc

    @ServiceDesc.setter
    def ServiceDesc(self, ServiceDesc):
        self._ServiceDesc = ServiceDesc

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def ApiDesc(self):
        return self._ApiDesc

    @ApiDesc.setter
    def ApiDesc(self, ApiDesc):
        self._ApiDesc = ApiDesc

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def AttachedTime(self):
        return self._AttachedTime

    @AttachedTime.setter
    def AttachedTime(self, AttachedTime):
        self._AttachedTime = AttachedTime


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceName = params.get("ServiceName")
        self._ServiceDesc = params.get("ServiceDesc")
        self._ApiId = params.get("ApiId")
        self._ApiName = params.get("ApiName")
        self._ApiDesc = params.get("ApiDesc")
        self._Environment = params.get("Environment")
        self._AttachedTime = params.get("AttachedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedApiSummary(AbstractModel):
    """List of APIs bound with the plugin

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of APIs bound with the plugin
        :type TotalCount: int
        :param _AttachedApis: Information of the API bound with the plugin
        :type AttachedApis: list of AttachedApiInfo
        """
        self._TotalCount = None
        self._AttachedApis = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AttachedApis(self):
        return self._AttachedApis

    @AttachedApis.setter
    def AttachedApis(self, AttachedApis):
        self._AttachedApis = AttachedApis


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AttachedApis") is not None:
            self._AttachedApis = []
            for item in params.get("AttachedApis"):
                obj = AttachedApiInfo()
                obj._deserialize(item)
                self._AttachedApis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedPluginInfo(AbstractModel):
    """Information of bound plug-ins

    """

    def __init__(self):
        r"""
        :param _PluginId: Plugin ID
        :type PluginId: str
        :param _Environment: Environment information
        :type Environment: str
        :param _AttachedTime: Binding time
        :type AttachedTime: str
        :param _PluginName: Plugin name
        :type PluginName: str
        :param _PluginType: Plugin type
        :type PluginType: str
        :param _Description: Plugin description
        :type Description: str
        :param _PluginData: Plugin definition statement
        :type PluginData: str
        """
        self._PluginId = None
        self._Environment = None
        self._AttachedTime = None
        self._PluginName = None
        self._PluginType = None
        self._Description = None
        self._PluginData = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def AttachedTime(self):
        return self._AttachedTime

    @AttachedTime.setter
    def AttachedTime(self, AttachedTime):
        self._AttachedTime = AttachedTime

    @property
    def PluginName(self):
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def PluginType(self):
        return self._PluginType

    @PluginType.setter
    def PluginType(self, PluginType):
        self._PluginType = PluginType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PluginData(self):
        return self._PluginData

    @PluginData.setter
    def PluginData(self, PluginData):
        self._PluginData = PluginData


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._Environment = params.get("Environment")
        self._AttachedTime = params.get("AttachedTime")
        self._PluginName = params.get("PluginName")
        self._PluginType = params.get("PluginType")
        self._Description = params.get("Description")
        self._PluginData = params.get("PluginData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedPluginSummary(AbstractModel):
    """Information of bound plug-ins

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of bound plug-ins
        :type TotalCount: int
        :param _PluginSummary: Information of bound plug-ins
        :type PluginSummary: list of AttachedPluginInfo
        """
        self._TotalCount = None
        self._PluginSummary = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PluginSummary(self):
        return self._PluginSummary

    @PluginSummary.setter
    def PluginSummary(self, PluginSummary):
        self._PluginSummary = PluginSummary


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("PluginSummary") is not None:
            self._PluginSummary = []
            for item in params.get("PluginSummary"):
                obj = AttachedPluginInfo()
                obj._deserialize(item)
                self._PluginSummary.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableApiInfo(AbstractModel):
    """Information of the APIs that can use this plugin

    """

    def __init__(self):
        r"""
        :param _ApiId: API ID
        :type ApiId: str
        :param _ApiName: API name
        :type ApiName: str
        :param _ApiType: API type
        :type ApiType: str
        :param _Path: API path
        :type Path: str
        :param _Method: API method
        :type Method: str
        :param _AttachedOtherPlugin: Whether the API is bound with another plugin
Note: this field may return null, indicating that no valid values can be obtained.
        :type AttachedOtherPlugin: bool
        :param _IsAttached: Whether the API is bound with the current plugin
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsAttached: bool
        """
        self._ApiId = None
        self._ApiName = None
        self._ApiType = None
        self._Path = None
        self._Method = None
        self._AttachedOtherPlugin = None
        self._IsAttached = None

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def ApiType(self):
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def AttachedOtherPlugin(self):
        return self._AttachedOtherPlugin

    @AttachedOtherPlugin.setter
    def AttachedOtherPlugin(self, AttachedOtherPlugin):
        self._AttachedOtherPlugin = AttachedOtherPlugin

    @property
    def IsAttached(self):
        return self._IsAttached

    @IsAttached.setter
    def IsAttached(self, IsAttached):
        self._IsAttached = IsAttached


    def _deserialize(self, params):
        self._ApiId = params.get("ApiId")
        self._ApiName = params.get("ApiName")
        self._ApiType = params.get("ApiType")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        self._AttachedOtherPlugin = params.get("AttachedOtherPlugin")
        self._IsAttached = params.get("IsAttached")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Base64EncodedTriggerRule(AbstractModel):
    """Header trigger rule for Base64 encoding.

    """

    def __init__(self):
        r"""
        :param _Name: Header for triggering encoding. Valid values are `Accept` and `Content_Type`, corresponding to the `Accept` and `Content-Type` headers in the data stream request, respectively.
        :type Name: str
        :param _Value: Array of header values that can trigger the encoding. Each element in the array can be up to 40 characters, including digits, letters, and special characters (`.`, `+`, `*`, `-`, `/`, and `_`). 

For example, [
    "application/x-vpeg005",
    "application/xhtml+xml",
    "application/vnd.ms-project",
    "application/vnd.rn-rn_music_package"
] are valid.
        :type Value: list of str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindApiAppRequest(AbstractModel):
    """BindApiApp request structure.

    """

    def __init__(self):
        r"""
        :param _ApiAppId: Unique ID of the application to be bound.
        :type ApiAppId: str
        :param _Environment: Environment to be bound.
        :type Environment: str
        :param _ServiceId: Unique ID of the service to be bound.
        :type ServiceId: str
        :param _ApiId: Unique ID of the API to be bound.
        :type ApiId: str
        """
        self._ApiAppId = None
        self._Environment = None
        self._ServiceId = None
        self._ApiId = None

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId


    def _deserialize(self, params):
        self._ApiAppId = params.get("ApiAppId")
        self._Environment = params.get("Environment")
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindApiAppResponse(AbstractModel):
    """BindApiApp response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether binding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class BindApiInfo(AbstractModel):
    """Information of the API bound with the upstream

    """

    def __init__(self):
        r"""
        :param _ApiId: Unique API ID.
        :type ApiId: str
        :param _ServiceId: Unique ID of the service
        :type ServiceId: str
        :param _ApiName: API name
Note: This field may return `null`, indicating that no valid value was found.
        :type ApiName: str
        :param _ServiceName: Service name
Note: This field may return `null`, indicating that no valid value was found.
        :type ServiceName: str
        :param _BindTime: Bound At
        :type BindTime: str
        """
        self._ApiId = None
        self._ServiceId = None
        self._ApiName = None
        self._ServiceName = None
        self._BindTime = None

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def BindTime(self):
        return self._BindTime

    @BindTime.setter
    def BindTime(self, BindTime):
        self._BindTime = BindTime


    def _deserialize(self, params):
        self._ApiId = params.get("ApiId")
        self._ServiceId = params.get("ServiceId")
        self._ApiName = params.get("ApiName")
        self._ServiceName = params.get("ServiceName")
        self._BindTime = params.get("BindTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindEnvironmentRequest(AbstractModel):
    """BindEnvironment request structure.

    """

    def __init__(self):
        r"""
        :param _UsagePlanIds: List of unique IDs of the usage plans to be bound.
        :type UsagePlanIds: list of str
        :param _BindType: Binding type. Valid values: API, SERVICE. Default value: SERVICE.
        :type BindType: str
        :param _Environment: Environment to be bound.
        :type Environment: str
        :param _ServiceId: Unique ID of the service to be bound.
        :type ServiceId: str
        :param _ApiIds: Unique API ID array, which is required if `bindType` is `API`.
        :type ApiIds: list of str
        """
        self._UsagePlanIds = None
        self._BindType = None
        self._Environment = None
        self._ServiceId = None
        self._ApiIds = None

    @property
    def UsagePlanIds(self):
        return self._UsagePlanIds

    @UsagePlanIds.setter
    def UsagePlanIds(self, UsagePlanIds):
        self._UsagePlanIds = UsagePlanIds

    @property
    def BindType(self):
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds


    def _deserialize(self, params):
        self._UsagePlanIds = params.get("UsagePlanIds")
        self._BindType = params.get("BindType")
        self._Environment = params.get("Environment")
        self._ServiceId = params.get("ServiceId")
        self._ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindEnvironmentResponse(AbstractModel):
    """BindEnvironment response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether binding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class BindIPStrategyRequest(AbstractModel):
    """BindIPStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID of the IP policy to be bound.
        :type ServiceId: str
        :param _StrategyId: Unique ID of the IP policy to be bound.
        :type StrategyId: str
        :param _EnvironmentName: Environment to be bound to IP policy.
        :type EnvironmentName: str
        :param _BindApiIds: List of APIs to be bound to IP policy.
        :type BindApiIds: list of str
        """
        self._ServiceId = None
        self._StrategyId = None
        self._EnvironmentName = None
        self._BindApiIds = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def BindApiIds(self):
        return self._BindApiIds

    @BindApiIds.setter
    def BindApiIds(self, BindApiIds):
        self._BindApiIds = BindApiIds


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._StrategyId = params.get("StrategyId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._BindApiIds = params.get("BindApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindIPStrategyResponse(AbstractModel):
    """BindIPStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether binding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class BindSecretIdsRequest(AbstractModel):
    """BindSecretIds request structure.

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: Unique ID of the usage plan to be bound.
        :type UsagePlanId: str
        :param _AccessKeyIds: Array of IDs of the keys to be bound.
        :type AccessKeyIds: list of str
        """
        self._UsagePlanId = None
        self._AccessKeyIds = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def AccessKeyIds(self):
        return self._AccessKeyIds

    @AccessKeyIds.setter
    def AccessKeyIds(self, AccessKeyIds):
        self._AccessKeyIds = AccessKeyIds


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        self._AccessKeyIds = params.get("AccessKeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindSecretIdsResponse(AbstractModel):
    """BindSecretIds response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether binding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class BindSubDomainRequest(AbstractModel):
    """BindSubDomain request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _SubDomain: Custom domain name to be bound.
        :type SubDomain: str
        :param _Protocol: Protocol supported by service. Valid values: http, https, http&https.
        :type Protocol: str
        :param _NetType: Network type. Valid values: OUTER, INNER.
        :type NetType: str
        :param _IsDefaultMapping: Whether the default path mapping is used. The default value is `true`. If the value is `false`, the custom path mapping will be used and `PathMappingSet` will be required in this case.
        :type IsDefaultMapping: bool
        :param _NetSubDomain: Default domain name.
        :type NetSubDomain: str
        :param _CertificateId: Unique certificate ID of the custom domain name to be bound. The certificate can be uploaded if `Protocol` is `https` or `http&https`.
        :type CertificateId: str
        :param _PathMappingSet: Custom domain name path mapping. It can contain up to 3 `Environment` values which can be set to only `test`, `prepub`, and `release`, respectively.
        :type PathMappingSet: list of PathMapping
        :param _IsForcedHttps: Whether to force HTTP requests to redirect to HTTPS. Default value: `false`. When this parameter is `true`, API Gateway will redirect all requests using the custom domain name over the HTTP protocol to the HTTPS protocol for forwarding.
        :type IsForcedHttps: bool
        """
        self._ServiceId = None
        self._SubDomain = None
        self._Protocol = None
        self._NetType = None
        self._IsDefaultMapping = None
        self._NetSubDomain = None
        self._CertificateId = None
        self._PathMappingSet = None
        self._IsForcedHttps = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def IsDefaultMapping(self):
        return self._IsDefaultMapping

    @IsDefaultMapping.setter
    def IsDefaultMapping(self, IsDefaultMapping):
        self._IsDefaultMapping = IsDefaultMapping

    @property
    def NetSubDomain(self):
        return self._NetSubDomain

    @NetSubDomain.setter
    def NetSubDomain(self, NetSubDomain):
        self._NetSubDomain = NetSubDomain

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def PathMappingSet(self):
        return self._PathMappingSet

    @PathMappingSet.setter
    def PathMappingSet(self, PathMappingSet):
        self._PathMappingSet = PathMappingSet

    @property
    def IsForcedHttps(self):
        return self._IsForcedHttps

    @IsForcedHttps.setter
    def IsForcedHttps(self, IsForcedHttps):
        self._IsForcedHttps = IsForcedHttps


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._SubDomain = params.get("SubDomain")
        self._Protocol = params.get("Protocol")
        self._NetType = params.get("NetType")
        self._IsDefaultMapping = params.get("IsDefaultMapping")
        self._NetSubDomain = params.get("NetSubDomain")
        self._CertificateId = params.get("CertificateId")
        if params.get("PathMappingSet") is not None:
            self._PathMappingSet = []
            for item in params.get("PathMappingSet"):
                obj = PathMapping()
                obj._deserialize(item)
                self._PathMappingSet.append(obj)
        self._IsForcedHttps = params.get("IsForcedHttps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindSubDomainResponse(AbstractModel):
    """BindSubDomain response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether binding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class BuildAPIDocRequest(AbstractModel):
    """BuildAPIDoc request structure.

    """

    def __init__(self):
        r"""
        :param _ApiDocId: API document ID
        :type ApiDocId: str
        """
        self._ApiDocId = None

    @property
    def ApiDocId(self):
        return self._ApiDocId

    @ApiDocId.setter
    def ApiDocId(self, ApiDocId):
        self._ApiDocId = ApiDocId


    def _deserialize(self, params):
        self._ApiDocId = params.get("ApiDocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BuildAPIDocResponse(AbstractModel):
    """BuildAPIDoc response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the operation succeeded
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ConstantParameter(AbstractModel):
    """Constant parameter

    """

    def __init__(self):
        r"""
        :param _Name: Constant parameter name, which is used only if `ServiceType` is `HTTP`.
        :type Name: str
        :param _Desc: Constant parameter description, which is used only if `ServiceType` is `HTTP`.
        :type Desc: str
        :param _Position: Constant parameter position, which is used only if `ServiceType` is `HTTP`.
        :type Position: str
        :param _DefaultValue: Default value of constant parameter, which is used only if `ServiceType` is `HTTP`.
        :type DefaultValue: str
        """
        self._Name = None
        self._Desc = None
        self._Position = None
        self._DefaultValue = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._Position = params.get("Position")
        self._DefaultValue = params.get("DefaultValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosConfig(AbstractModel):
    """COS-type API configuration

    """

    def __init__(self):
        r"""
        :param _Action: Specifies how the backend COS bucket is called by the API. The frontend request method and Action can be:
GET：GetObject
PUT：PutObject
POST：PostObject、AppendObject
HEAD： HeadObject
DELETE： DeleteObject
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Action: str
        :param _BucketName: Backend COS bucket of the API
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BucketName: str
        :param _Authorization: Whether to enable the backend COS signature for the API. It defaults to `false`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Authorization: bool
        :param _PathMatchMode: The path matching mode of the backend COS service
`BackEndPath`: Match the backend path
`FullPath`: Match the full path

Default: `BackEndPath`
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PathMatchMode: str
        """
        self._Action = None
        self._BucketName = None
        self._Authorization = None
        self._PathMatchMode = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def Authorization(self):
        return self._Authorization

    @Authorization.setter
    def Authorization(self, Authorization):
        self._Authorization = Authorization

    @property
    def PathMatchMode(self):
        return self._PathMatchMode

    @PathMatchMode.setter
    def PathMatchMode(self, PathMatchMode):
        self._PathMatchMode = PathMatchMode


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._BucketName = params.get("BucketName")
        self._Authorization = params.get("Authorization")
        self._PathMatchMode = params.get("PathMatchMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAPIDocRequest(AbstractModel):
    """CreateAPIDoc request structure.

    """

    def __init__(self):
        r"""
        :param _ApiDocName: API document name
        :type ApiDocName: str
        :param _ServiceId: Service name
        :type ServiceId: str
        :param _Environment: Environment name
        :type Environment: str
        :param _ApiIds: List of APIs for which to generate documents
        :type ApiIds: list of str
        """
        self._ApiDocName = None
        self._ServiceId = None
        self._Environment = None
        self._ApiIds = None

    @property
    def ApiDocName(self):
        return self._ApiDocName

    @ApiDocName.setter
    def ApiDocName(self, ApiDocName):
        self._ApiDocName = ApiDocName

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds


    def _deserialize(self, params):
        self._ApiDocName = params.get("ApiDocName")
        self._ServiceId = params.get("ServiceId")
        self._Environment = params.get("Environment")
        self._ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAPIDocResponse(AbstractModel):
    """CreateAPIDoc response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Basic information of API document
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = APIDoc()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateApiAppRequest(AbstractModel):
    """CreateApiApp request structure.

    """

    def __init__(self):
        r"""
        :param _ApiAppName: Custom application name.
        :type ApiAppName: str
        :param _ApiAppDesc: Application description
        :type ApiAppDesc: str
        """
        self._ApiAppName = None
        self._ApiAppDesc = None

    @property
    def ApiAppName(self):
        return self._ApiAppName

    @ApiAppName.setter
    def ApiAppName(self, ApiAppName):
        self._ApiAppName = ApiAppName

    @property
    def ApiAppDesc(self):
        return self._ApiAppDesc

    @ApiAppDesc.setter
    def ApiAppDesc(self, ApiAppDesc):
        self._ApiAppDesc = ApiAppDesc


    def _deserialize(self, params):
        self._ApiAppName = params.get("ApiAppName")
        self._ApiAppDesc = params.get("ApiAppDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiAppResponse(AbstractModel):
    """CreateApiApp response structure.

    """

    def __init__(self):
        r"""
        :param _Result: New application details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiAppInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateApiKeyRequest(AbstractModel):
    """CreateApiKey request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Custom key name.
        :type SecretName: str
        :param _AccessKeyType: Key type. Valid values: auto, manual (custom key). Default value: auto.
        :type AccessKeyType: str
        :param _AccessKeyId: Custom key ID, which is required if `AccessKeyType` is `manual`. It can contain 5–50 letters, digits, and underscores.
        :type AccessKeyId: str
        :param _AccessKeySecret: Custom key, which is required if `AccessKeyType` is `manual`. It can contain 10–50 letters, digits, and underscores.
        :type AccessKeySecret: str
        """
        self._SecretName = None
        self._AccessKeyType = None
        self._AccessKeyId = None
        self._AccessKeySecret = None

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def AccessKeyType(self):
        return self._AccessKeyType

    @AccessKeyType.setter
    def AccessKeyType(self, AccessKeyType):
        self._AccessKeyType = AccessKeyType

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def AccessKeySecret(self):
        return self._AccessKeySecret

    @AccessKeySecret.setter
    def AccessKeySecret(self, AccessKeySecret):
        self._AccessKeySecret = AccessKeySecret


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._AccessKeyType = params.get("AccessKeyType")
        self._AccessKeyId = params.get("AccessKeyId")
        self._AccessKeySecret = params.get("AccessKeySecret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiKeyResponse(AbstractModel):
    """CreateApiKey response structure.

    """

    def __init__(self):
        r"""
        :param _Result: New key details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiKey()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateApiRequest(AbstractModel):
    """CreateApi request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID of API.
        :type ServiceId: str
        :param _ServiceType: API backend service type. Valid values: HTTP, MOCK, TSF, SCF, WEBSOCKET, TARGET (in beta test).
        :type ServiceType: str
        :param _ServiceTimeout: API backend service timeout period in seconds.
        :type ServiceTimeout: int
        :param _Protocol: API frontend request protocol. Valid values: HTTPS, WEBSOCKET.
        :type Protocol: str
        :param _RequestConfig: Request frontend configuration.
        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.ApiRequestConfig`
        :param _ApiName: Custom API name.
        :type ApiName: str
        :param _ApiDesc: Custom API description.
        :type ApiDesc: str
        :param _ApiType: API type. Valid values: NORMAL (general API), TSF (microservice API). Default value: NORMAL.
        :type ApiType: str
        :param _AuthType: API authentication type. Valid values: SECRET (key pair authentication), NONE (no authentication), OAUTH, APP (application authentication). Default value: NONE.
        :type AuthType: str
        :param _EnableCORS: Whether to enable CORS.
        :type EnableCORS: bool
        :param _ConstantParameters: Constant parameter.
        :type ConstantParameters: list of ConstantParameter
        :param _RequestParameters: Frontend request parameter.
        :type RequestParameters: list of RequestParameter
        :param _ApiBusinessType: This field is valid if `AuthType` is `OAUTH`. NORMAL: business API; OAUTH: authorization API.
        :type ApiBusinessType: str
        :param _ServiceMockReturnMessage: Returned message of API backend Mock, which is required if `ServiceType` is `Mock`.
        :type ServiceMockReturnMessage: str
        :param _MicroServices: List of microservices bound to API.
        :type MicroServices: list of MicroServiceReq
        :param _ServiceTsfLoadBalanceConf: Load balancing configuration of microservice.
        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`
        :param _ServiceTsfHealthCheckConf: Health check configuration of microservice.
        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param _TargetServices: `target` type backend resource information (in beta test).
        :type TargetServices: list of TargetServicesReq
        :param _TargetServicesLoadBalanceConf: `target` type load balancing configuration (in beta test).
        :type TargetServicesLoadBalanceConf: int
        :param _TargetServicesHealthCheckConf: `target` health check configuration (in beta test).
        :type TargetServicesHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param _ServiceScfFunctionName: SCF function name, which takes effect if the backend type is `SCF`.
        :type ServiceScfFunctionName: str
        :param _ServiceWebsocketRegisterFunctionName: SCF WebSocket registration function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionName: str
        :param _ServiceWebsocketCleanupFunctionName: SCF WebSocket cleanup function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionName: str
        :param _ServiceWebsocketTransportFunctionName: SCF WebSocket transfer function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionName: str
        :param _ServiceScfFunctionNamespace: SCF function namespace, which takes effect if the backend type is `SCF`.
        :type ServiceScfFunctionNamespace: str
        :param _ServiceScfFunctionQualifier: SCF function version, which takes effect if the backend type is `SCF`.
        :type ServiceScfFunctionQualifier: str
        :param _ServiceWebsocketRegisterFunctionNamespace: SCF WebSocket registration function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionNamespace: str
        :param _ServiceWebsocketRegisterFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionQualifier: str
        :param _ServiceWebsocketTransportFunctionNamespace: SCF WebSocket transfer function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionNamespace: str
        :param _ServiceWebsocketTransportFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionQualifier: str
        :param _ServiceWebsocketCleanupFunctionNamespace: SCF WebSocket cleanup function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionNamespace: str
        :param _ServiceWebsocketCleanupFunctionQualifier: SCF WebSocket cleanup function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionQualifier: str
        :param _ServiceScfIsIntegratedResponse: Whether to enable response integration, which takes effect if the backend type is `SCF`.
        :type ServiceScfIsIntegratedResponse: bool
        :param _IsDebugAfterCharge: Billing after debugging starts (reserved field for marketplace).
        :type IsDebugAfterCharge: bool
        :param _IsDeleteResponseErrorCodes: Whether to delete the error codes for custom response configuration. If the value is left empty or `False`, the error codes will not be deleted. If the value is `True`, all custom response configuration error codes of the API will be deleted.
        :type IsDeleteResponseErrorCodes: bool
        :param _ResponseType: Return type.
        :type ResponseType: str
        :param _ResponseSuccessExample: Sample response for successful custom response configuration.
        :type ResponseSuccessExample: str
        :param _ResponseFailExample: Sample response for failed custom response configuration.
        :type ResponseFailExample: str
        :param _ServiceConfig: API backend service configuration.
        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`
        :param _AuthRelationApiId: Unique ID of associated authorization API, which takes effect only if `AuthType` is `OAUTH` and `ApiBusinessType` is `NORMAL`. It is the unique ID of the OAuth 2.0 authorization API bound to the business API.
        :type AuthRelationApiId: str
        :param _ServiceParameters: API backend service parameter.
        :type ServiceParameters: list of ServiceParameter
        :param _OauthConfig: OAuth configuration, which takes effect if `AuthType` is `OAUTH`.
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param _ResponseErrorCodes: Custom error code configuration.
        :type ResponseErrorCodes: list of ResponseErrorCodeReq
        :param _TargetNamespaceId: TSF Serverless namespace ID (in beta test).
        :type TargetNamespaceId: str
        :param _UserType: User type.
        :type UserType: str
        :param _IsBase64Encoded: Whether to enable Base64 encoding. This parameter takes effect only when the backend is SCF.
        :type IsBase64Encoded: bool
        :param _EventBusId: Event bus ID.
        :type EventBusId: str
        :param _ServiceScfFunctionType: SCF function type, which takes effect if the backend type is `SCF`. Valid values: `EVENT` and `HTTP`.
        :type ServiceScfFunctionType: str
        :param _EIAMAppType: EIAM application type.
        :type EIAMAppType: str
        :param _EIAMAuthType: EIAM application authentication type. Valid values: `AuthenticationOnly`, `Authentication`, `Authorization`.
        :type EIAMAuthType: str
        :param _TokenTimeout: Validity of the EIAM application token. Unit: second. Default value: `7200`.
        :type TokenTimeout: int
        :param _EIAMAppId: EIAM application ID.
        :type EIAMAppId: str
        :param _Owner: Owner of the resource
        :type Owner: str
        """
        self._ServiceId = None
        self._ServiceType = None
        self._ServiceTimeout = None
        self._Protocol = None
        self._RequestConfig = None
        self._ApiName = None
        self._ApiDesc = None
        self._ApiType = None
        self._AuthType = None
        self._EnableCORS = None
        self._ConstantParameters = None
        self._RequestParameters = None
        self._ApiBusinessType = None
        self._ServiceMockReturnMessage = None
        self._MicroServices = None
        self._ServiceTsfLoadBalanceConf = None
        self._ServiceTsfHealthCheckConf = None
        self._TargetServices = None
        self._TargetServicesLoadBalanceConf = None
        self._TargetServicesHealthCheckConf = None
        self._ServiceScfFunctionName = None
        self._ServiceWebsocketRegisterFunctionName = None
        self._ServiceWebsocketCleanupFunctionName = None
        self._ServiceWebsocketTransportFunctionName = None
        self._ServiceScfFunctionNamespace = None
        self._ServiceScfFunctionQualifier = None
        self._ServiceWebsocketRegisterFunctionNamespace = None
        self._ServiceWebsocketRegisterFunctionQualifier = None
        self._ServiceWebsocketTransportFunctionNamespace = None
        self._ServiceWebsocketTransportFunctionQualifier = None
        self._ServiceWebsocketCleanupFunctionNamespace = None
        self._ServiceWebsocketCleanupFunctionQualifier = None
        self._ServiceScfIsIntegratedResponse = None
        self._IsDebugAfterCharge = None
        self._IsDeleteResponseErrorCodes = None
        self._ResponseType = None
        self._ResponseSuccessExample = None
        self._ResponseFailExample = None
        self._ServiceConfig = None
        self._AuthRelationApiId = None
        self._ServiceParameters = None
        self._OauthConfig = None
        self._ResponseErrorCodes = None
        self._TargetNamespaceId = None
        self._UserType = None
        self._IsBase64Encoded = None
        self._EventBusId = None
        self._ServiceScfFunctionType = None
        self._EIAMAppType = None
        self._EIAMAuthType = None
        self._TokenTimeout = None
        self._EIAMAppId = None
        self._Owner = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ServiceTimeout(self):
        return self._ServiceTimeout

    @ServiceTimeout.setter
    def ServiceTimeout(self, ServiceTimeout):
        self._ServiceTimeout = ServiceTimeout

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RequestConfig(self):
        return self._RequestConfig

    @RequestConfig.setter
    def RequestConfig(self, RequestConfig):
        self._RequestConfig = RequestConfig

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def ApiDesc(self):
        return self._ApiDesc

    @ApiDesc.setter
    def ApiDesc(self, ApiDesc):
        self._ApiDesc = ApiDesc

    @property
    def ApiType(self):
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def AuthType(self):
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def EnableCORS(self):
        return self._EnableCORS

    @EnableCORS.setter
    def EnableCORS(self, EnableCORS):
        self._EnableCORS = EnableCORS

    @property
    def ConstantParameters(self):
        return self._ConstantParameters

    @ConstantParameters.setter
    def ConstantParameters(self, ConstantParameters):
        self._ConstantParameters = ConstantParameters

    @property
    def RequestParameters(self):
        return self._RequestParameters

    @RequestParameters.setter
    def RequestParameters(self, RequestParameters):
        self._RequestParameters = RequestParameters

    @property
    def ApiBusinessType(self):
        return self._ApiBusinessType

    @ApiBusinessType.setter
    def ApiBusinessType(self, ApiBusinessType):
        self._ApiBusinessType = ApiBusinessType

    @property
    def ServiceMockReturnMessage(self):
        return self._ServiceMockReturnMessage

    @ServiceMockReturnMessage.setter
    def ServiceMockReturnMessage(self, ServiceMockReturnMessage):
        self._ServiceMockReturnMessage = ServiceMockReturnMessage

    @property
    def MicroServices(self):
        return self._MicroServices

    @MicroServices.setter
    def MicroServices(self, MicroServices):
        self._MicroServices = MicroServices

    @property
    def ServiceTsfLoadBalanceConf(self):
        return self._ServiceTsfLoadBalanceConf

    @ServiceTsfLoadBalanceConf.setter
    def ServiceTsfLoadBalanceConf(self, ServiceTsfLoadBalanceConf):
        self._ServiceTsfLoadBalanceConf = ServiceTsfLoadBalanceConf

    @property
    def ServiceTsfHealthCheckConf(self):
        return self._ServiceTsfHealthCheckConf

    @ServiceTsfHealthCheckConf.setter
    def ServiceTsfHealthCheckConf(self, ServiceTsfHealthCheckConf):
        self._ServiceTsfHealthCheckConf = ServiceTsfHealthCheckConf

    @property
    def TargetServices(self):
        return self._TargetServices

    @TargetServices.setter
    def TargetServices(self, TargetServices):
        self._TargetServices = TargetServices

    @property
    def TargetServicesLoadBalanceConf(self):
        return self._TargetServicesLoadBalanceConf

    @TargetServicesLoadBalanceConf.setter
    def TargetServicesLoadBalanceConf(self, TargetServicesLoadBalanceConf):
        self._TargetServicesLoadBalanceConf = TargetServicesLoadBalanceConf

    @property
    def TargetServicesHealthCheckConf(self):
        return self._TargetServicesHealthCheckConf

    @TargetServicesHealthCheckConf.setter
    def TargetServicesHealthCheckConf(self, TargetServicesHealthCheckConf):
        self._TargetServicesHealthCheckConf = TargetServicesHealthCheckConf

    @property
    def ServiceScfFunctionName(self):
        return self._ServiceScfFunctionName

    @ServiceScfFunctionName.setter
    def ServiceScfFunctionName(self, ServiceScfFunctionName):
        self._ServiceScfFunctionName = ServiceScfFunctionName

    @property
    def ServiceWebsocketRegisterFunctionName(self):
        return self._ServiceWebsocketRegisterFunctionName

    @ServiceWebsocketRegisterFunctionName.setter
    def ServiceWebsocketRegisterFunctionName(self, ServiceWebsocketRegisterFunctionName):
        self._ServiceWebsocketRegisterFunctionName = ServiceWebsocketRegisterFunctionName

    @property
    def ServiceWebsocketCleanupFunctionName(self):
        return self._ServiceWebsocketCleanupFunctionName

    @ServiceWebsocketCleanupFunctionName.setter
    def ServiceWebsocketCleanupFunctionName(self, ServiceWebsocketCleanupFunctionName):
        self._ServiceWebsocketCleanupFunctionName = ServiceWebsocketCleanupFunctionName

    @property
    def ServiceWebsocketTransportFunctionName(self):
        return self._ServiceWebsocketTransportFunctionName

    @ServiceWebsocketTransportFunctionName.setter
    def ServiceWebsocketTransportFunctionName(self, ServiceWebsocketTransportFunctionName):
        self._ServiceWebsocketTransportFunctionName = ServiceWebsocketTransportFunctionName

    @property
    def ServiceScfFunctionNamespace(self):
        return self._ServiceScfFunctionNamespace

    @ServiceScfFunctionNamespace.setter
    def ServiceScfFunctionNamespace(self, ServiceScfFunctionNamespace):
        self._ServiceScfFunctionNamespace = ServiceScfFunctionNamespace

    @property
    def ServiceScfFunctionQualifier(self):
        return self._ServiceScfFunctionQualifier

    @ServiceScfFunctionQualifier.setter
    def ServiceScfFunctionQualifier(self, ServiceScfFunctionQualifier):
        self._ServiceScfFunctionQualifier = ServiceScfFunctionQualifier

    @property
    def ServiceWebsocketRegisterFunctionNamespace(self):
        return self._ServiceWebsocketRegisterFunctionNamespace

    @ServiceWebsocketRegisterFunctionNamespace.setter
    def ServiceWebsocketRegisterFunctionNamespace(self, ServiceWebsocketRegisterFunctionNamespace):
        self._ServiceWebsocketRegisterFunctionNamespace = ServiceWebsocketRegisterFunctionNamespace

    @property
    def ServiceWebsocketRegisterFunctionQualifier(self):
        return self._ServiceWebsocketRegisterFunctionQualifier

    @ServiceWebsocketRegisterFunctionQualifier.setter
    def ServiceWebsocketRegisterFunctionQualifier(self, ServiceWebsocketRegisterFunctionQualifier):
        self._ServiceWebsocketRegisterFunctionQualifier = ServiceWebsocketRegisterFunctionQualifier

    @property
    def ServiceWebsocketTransportFunctionNamespace(self):
        return self._ServiceWebsocketTransportFunctionNamespace

    @ServiceWebsocketTransportFunctionNamespace.setter
    def ServiceWebsocketTransportFunctionNamespace(self, ServiceWebsocketTransportFunctionNamespace):
        self._ServiceWebsocketTransportFunctionNamespace = ServiceWebsocketTransportFunctionNamespace

    @property
    def ServiceWebsocketTransportFunctionQualifier(self):
        return self._ServiceWebsocketTransportFunctionQualifier

    @ServiceWebsocketTransportFunctionQualifier.setter
    def ServiceWebsocketTransportFunctionQualifier(self, ServiceWebsocketTransportFunctionQualifier):
        self._ServiceWebsocketTransportFunctionQualifier = ServiceWebsocketTransportFunctionQualifier

    @property
    def ServiceWebsocketCleanupFunctionNamespace(self):
        return self._ServiceWebsocketCleanupFunctionNamespace

    @ServiceWebsocketCleanupFunctionNamespace.setter
    def ServiceWebsocketCleanupFunctionNamespace(self, ServiceWebsocketCleanupFunctionNamespace):
        self._ServiceWebsocketCleanupFunctionNamespace = ServiceWebsocketCleanupFunctionNamespace

    @property
    def ServiceWebsocketCleanupFunctionQualifier(self):
        return self._ServiceWebsocketCleanupFunctionQualifier

    @ServiceWebsocketCleanupFunctionQualifier.setter
    def ServiceWebsocketCleanupFunctionQualifier(self, ServiceWebsocketCleanupFunctionQualifier):
        self._ServiceWebsocketCleanupFunctionQualifier = ServiceWebsocketCleanupFunctionQualifier

    @property
    def ServiceScfIsIntegratedResponse(self):
        return self._ServiceScfIsIntegratedResponse

    @ServiceScfIsIntegratedResponse.setter
    def ServiceScfIsIntegratedResponse(self, ServiceScfIsIntegratedResponse):
        self._ServiceScfIsIntegratedResponse = ServiceScfIsIntegratedResponse

    @property
    def IsDebugAfterCharge(self):
        return self._IsDebugAfterCharge

    @IsDebugAfterCharge.setter
    def IsDebugAfterCharge(self, IsDebugAfterCharge):
        self._IsDebugAfterCharge = IsDebugAfterCharge

    @property
    def IsDeleteResponseErrorCodes(self):
        return self._IsDeleteResponseErrorCodes

    @IsDeleteResponseErrorCodes.setter
    def IsDeleteResponseErrorCodes(self, IsDeleteResponseErrorCodes):
        self._IsDeleteResponseErrorCodes = IsDeleteResponseErrorCodes

    @property
    def ResponseType(self):
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseSuccessExample(self):
        return self._ResponseSuccessExample

    @ResponseSuccessExample.setter
    def ResponseSuccessExample(self, ResponseSuccessExample):
        self._ResponseSuccessExample = ResponseSuccessExample

    @property
    def ResponseFailExample(self):
        return self._ResponseFailExample

    @ResponseFailExample.setter
    def ResponseFailExample(self, ResponseFailExample):
        self._ResponseFailExample = ResponseFailExample

    @property
    def ServiceConfig(self):
        return self._ServiceConfig

    @ServiceConfig.setter
    def ServiceConfig(self, ServiceConfig):
        self._ServiceConfig = ServiceConfig

    @property
    def AuthRelationApiId(self):
        return self._AuthRelationApiId

    @AuthRelationApiId.setter
    def AuthRelationApiId(self, AuthRelationApiId):
        self._AuthRelationApiId = AuthRelationApiId

    @property
    def ServiceParameters(self):
        return self._ServiceParameters

    @ServiceParameters.setter
    def ServiceParameters(self, ServiceParameters):
        self._ServiceParameters = ServiceParameters

    @property
    def OauthConfig(self):
        return self._OauthConfig

    @OauthConfig.setter
    def OauthConfig(self, OauthConfig):
        self._OauthConfig = OauthConfig

    @property
    def ResponseErrorCodes(self):
        return self._ResponseErrorCodes

    @ResponseErrorCodes.setter
    def ResponseErrorCodes(self, ResponseErrorCodes):
        self._ResponseErrorCodes = ResponseErrorCodes

    @property
    def TargetNamespaceId(self):
        return self._TargetNamespaceId

    @TargetNamespaceId.setter
    def TargetNamespaceId(self, TargetNamespaceId):
        self._TargetNamespaceId = TargetNamespaceId

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def IsBase64Encoded(self):
        return self._IsBase64Encoded

    @IsBase64Encoded.setter
    def IsBase64Encoded(self, IsBase64Encoded):
        self._IsBase64Encoded = IsBase64Encoded

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def ServiceScfFunctionType(self):
        return self._ServiceScfFunctionType

    @ServiceScfFunctionType.setter
    def ServiceScfFunctionType(self, ServiceScfFunctionType):
        self._ServiceScfFunctionType = ServiceScfFunctionType

    @property
    def EIAMAppType(self):
        return self._EIAMAppType

    @EIAMAppType.setter
    def EIAMAppType(self, EIAMAppType):
        self._EIAMAppType = EIAMAppType

    @property
    def EIAMAuthType(self):
        return self._EIAMAuthType

    @EIAMAuthType.setter
    def EIAMAuthType(self, EIAMAuthType):
        self._EIAMAuthType = EIAMAuthType

    @property
    def TokenTimeout(self):
        return self._TokenTimeout

    @TokenTimeout.setter
    def TokenTimeout(self, TokenTimeout):
        self._TokenTimeout = TokenTimeout

    @property
    def EIAMAppId(self):
        return self._EIAMAppId

    @EIAMAppId.setter
    def EIAMAppId(self, EIAMAppId):
        self._EIAMAppId = EIAMAppId

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceType = params.get("ServiceType")
        self._ServiceTimeout = params.get("ServiceTimeout")
        self._Protocol = params.get("Protocol")
        if params.get("RequestConfig") is not None:
            self._RequestConfig = ApiRequestConfig()
            self._RequestConfig._deserialize(params.get("RequestConfig"))
        self._ApiName = params.get("ApiName")
        self._ApiDesc = params.get("ApiDesc")
        self._ApiType = params.get("ApiType")
        self._AuthType = params.get("AuthType")
        self._EnableCORS = params.get("EnableCORS")
        if params.get("ConstantParameters") is not None:
            self._ConstantParameters = []
            for item in params.get("ConstantParameters"):
                obj = ConstantParameter()
                obj._deserialize(item)
                self._ConstantParameters.append(obj)
        if params.get("RequestParameters") is not None:
            self._RequestParameters = []
            for item in params.get("RequestParameters"):
                obj = RequestParameter()
                obj._deserialize(item)
                self._RequestParameters.append(obj)
        self._ApiBusinessType = params.get("ApiBusinessType")
        self._ServiceMockReturnMessage = params.get("ServiceMockReturnMessage")
        if params.get("MicroServices") is not None:
            self._MicroServices = []
            for item in params.get("MicroServices"):
                obj = MicroServiceReq()
                obj._deserialize(item)
                self._MicroServices.append(obj)
        if params.get("ServiceTsfLoadBalanceConf") is not None:
            self._ServiceTsfLoadBalanceConf = TsfLoadBalanceConfResp()
            self._ServiceTsfLoadBalanceConf._deserialize(params.get("ServiceTsfLoadBalanceConf"))
        if params.get("ServiceTsfHealthCheckConf") is not None:
            self._ServiceTsfHealthCheckConf = HealthCheckConf()
            self._ServiceTsfHealthCheckConf._deserialize(params.get("ServiceTsfHealthCheckConf"))
        if params.get("TargetServices") is not None:
            self._TargetServices = []
            for item in params.get("TargetServices"):
                obj = TargetServicesReq()
                obj._deserialize(item)
                self._TargetServices.append(obj)
        self._TargetServicesLoadBalanceConf = params.get("TargetServicesLoadBalanceConf")
        if params.get("TargetServicesHealthCheckConf") is not None:
            self._TargetServicesHealthCheckConf = HealthCheckConf()
            self._TargetServicesHealthCheckConf._deserialize(params.get("TargetServicesHealthCheckConf"))
        self._ServiceScfFunctionName = params.get("ServiceScfFunctionName")
        self._ServiceWebsocketRegisterFunctionName = params.get("ServiceWebsocketRegisterFunctionName")
        self._ServiceWebsocketCleanupFunctionName = params.get("ServiceWebsocketCleanupFunctionName")
        self._ServiceWebsocketTransportFunctionName = params.get("ServiceWebsocketTransportFunctionName")
        self._ServiceScfFunctionNamespace = params.get("ServiceScfFunctionNamespace")
        self._ServiceScfFunctionQualifier = params.get("ServiceScfFunctionQualifier")
        self._ServiceWebsocketRegisterFunctionNamespace = params.get("ServiceWebsocketRegisterFunctionNamespace")
        self._ServiceWebsocketRegisterFunctionQualifier = params.get("ServiceWebsocketRegisterFunctionQualifier")
        self._ServiceWebsocketTransportFunctionNamespace = params.get("ServiceWebsocketTransportFunctionNamespace")
        self._ServiceWebsocketTransportFunctionQualifier = params.get("ServiceWebsocketTransportFunctionQualifier")
        self._ServiceWebsocketCleanupFunctionNamespace = params.get("ServiceWebsocketCleanupFunctionNamespace")
        self._ServiceWebsocketCleanupFunctionQualifier = params.get("ServiceWebsocketCleanupFunctionQualifier")
        self._ServiceScfIsIntegratedResponse = params.get("ServiceScfIsIntegratedResponse")
        self._IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        self._IsDeleteResponseErrorCodes = params.get("IsDeleteResponseErrorCodes")
        self._ResponseType = params.get("ResponseType")
        self._ResponseSuccessExample = params.get("ResponseSuccessExample")
        self._ResponseFailExample = params.get("ResponseFailExample")
        if params.get("ServiceConfig") is not None:
            self._ServiceConfig = ServiceConfig()
            self._ServiceConfig._deserialize(params.get("ServiceConfig"))
        self._AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("ServiceParameters") is not None:
            self._ServiceParameters = []
            for item in params.get("ServiceParameters"):
                obj = ServiceParameter()
                obj._deserialize(item)
                self._ServiceParameters.append(obj)
        if params.get("OauthConfig") is not None:
            self._OauthConfig = OauthConfig()
            self._OauthConfig._deserialize(params.get("OauthConfig"))
        if params.get("ResponseErrorCodes") is not None:
            self._ResponseErrorCodes = []
            for item in params.get("ResponseErrorCodes"):
                obj = ResponseErrorCodeReq()
                obj._deserialize(item)
                self._ResponseErrorCodes.append(obj)
        self._TargetNamespaceId = params.get("TargetNamespaceId")
        self._UserType = params.get("UserType")
        self._IsBase64Encoded = params.get("IsBase64Encoded")
        self._EventBusId = params.get("EventBusId")
        self._ServiceScfFunctionType = params.get("ServiceScfFunctionType")
        self._EIAMAppType = params.get("EIAMAppType")
        self._EIAMAuthType = params.get("EIAMAuthType")
        self._TokenTimeout = params.get("TokenTimeout")
        self._EIAMAppId = params.get("EIAMAppId")
        self._Owner = params.get("Owner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiResponse(AbstractModel):
    """CreateApi response structure.

    """

    def __init__(self):
        r"""
        :param _Result: API information
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.CreateApiRsp`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CreateApiRsp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateApiRsp(AbstractModel):
    """Return of API creation

    """

    def __init__(self):
        r"""
        :param _ApiId: API ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiId: str
        :param _Path: Path
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Path: str
        :param _Method: Request method
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Method: str
        :param _CreatedTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _Status: Status of the import task
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Status: str
        :param _ErrMsg: Details of the error
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ErrMsg: str
        :param _ApiName: API name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApiName: str
        """
        self._ApiId = None
        self._Path = None
        self._Method = None
        self._CreatedTime = None
        self._Status = None
        self._ErrMsg = None
        self._ApiName = None

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName


    def _deserialize(self, params):
        self._ApiId = params.get("ApiId")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        self._CreatedTime = params.get("CreatedTime")
        self._Status = params.get("Status")
        self._ErrMsg = params.get("ErrMsg")
        self._ApiName = params.get("ApiName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiRspSet(AbstractModel):
    """Information of the APIs created

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of APIs
        :type TotalCount: int
        :param _ApiSet: Information of created APIs
        :type ApiSet: list of CreateApiRsp
        """
        self._TotalCount = None
        self._ApiSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiSet(self):
        return self._ApiSet

    @ApiSet.setter
    def ApiSet(self, ApiSet):
        self._ApiSet = ApiSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiSet") is not None:
            self._ApiSet = []
            for item in params.get("ApiSet"):
                obj = CreateApiRsp()
                obj._deserialize(item)
                self._ApiSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIPStrategyRequest(AbstractModel):
    """CreateIPStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _StrategyName: Custom policy name.
        :type StrategyName: str
        :param _StrategyType: Policy type. Valid values: WHITE (allowlist), BLACK (blocklist).
        :type StrategyType: str
        :param _StrategyData: Policy details. Multiple IPs are separated with \n.
        :type StrategyData: str
        """
        self._ServiceId = None
        self._StrategyName = None
        self._StrategyType = None
        self._StrategyData = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StrategyName(self):
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def StrategyType(self):
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def StrategyData(self):
        return self._StrategyData

    @StrategyData.setter
    def StrategyData(self, StrategyData):
        self._StrategyData = StrategyData


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._StrategyName = params.get("StrategyName")
        self._StrategyType = params.get("StrategyType")
        self._StrategyData = params.get("StrategyData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIPStrategyResponse(AbstractModel):
    """CreateIPStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Result: New IP policy details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategy`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = IPStrategy()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreatePluginRequest(AbstractModel):
    """CreatePlugin request structure.

    """

    def __init__(self):
        r"""
        :param _PluginName: Custom plugin name. A plugin name should contain 2-50 characters out of a-z, A-Z, 0-9, and _, which must begin with a letter and end with a letter or a number.
        :type PluginName: str
        :param _PluginType: Plugin type. Valid values: `IPControl`, `TrafficControl`, `Cors`, `CustomReq`, `CustomAuth`, `Routing`, `TrafficControlByParameter`, `CircuitBreaker`, `ProxyCache`
        :type PluginType: str
        :param _PluginData: Plugin definition statement in json format
        :type PluginData: str
        :param _Description: Plugin description within 200 characters
        :type Description: str
        :param _Tags: Label
        :type Tags: list of Tag
        """
        self._PluginName = None
        self._PluginType = None
        self._PluginData = None
        self._Description = None
        self._Tags = None

    @property
    def PluginName(self):
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def PluginType(self):
        return self._PluginType

    @PluginType.setter
    def PluginType(self, PluginType):
        self._PluginType = PluginType

    @property
    def PluginData(self):
        return self._PluginData

    @PluginData.setter
    def PluginData(self, PluginData):
        self._PluginData = PluginData

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._PluginName = params.get("PluginName")
        self._PluginType = params.get("PluginType")
        self._PluginData = params.get("PluginData")
        self._Description = params.get("Description")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePluginResponse(AbstractModel):
    """CreatePlugin response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Details of the new plugin
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.Plugin`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = Plugin()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateServiceRequest(AbstractModel):
    """CreateService request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceName: Custom service name.
        :type ServiceName: str
        :param _Protocol: Service frontend request type, such as `http`, `https`, and `http&https`.
        :type Protocol: str
        :param _ServiceDesc: Custom service description.
        :type ServiceDesc: str
        :param _ExclusiveSetName: Dedicated cluster name, which is used to specify the dedicated cluster where the service is to be created.
        :type ExclusiveSetName: str
        :param _NetTypes: Network type list, which is used to specify the supported network types. INNER: private network access; OUTER: public network access. Default value: OUTER.
        :type NetTypes: list of str
        :param _IpVersion: IP version number. Valid values: IPv4, IPv6. Default value: IPv4.
        :type IpVersion: str
        :param _SetServerName: Cluster name, which is reserved and used by the `tsf serverless` type.
        :type SetServerName: str
        :param _AppIdType: User type, which is reserved and can be used by `serverless` users.
        :type AppIdType: str
        :param _Tags: Tag information.
        :type Tags: list of Tag
        :param _InstanceId: Dedicated instance ID
        :type InstanceId: str
        :param _UniqVpcId: VPC attribute
        :type UniqVpcId: str
        """
        self._ServiceName = None
        self._Protocol = None
        self._ServiceDesc = None
        self._ExclusiveSetName = None
        self._NetTypes = None
        self._IpVersion = None
        self._SetServerName = None
        self._AppIdType = None
        self._Tags = None
        self._InstanceId = None
        self._UniqVpcId = None

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ServiceDesc(self):
        return self._ServiceDesc

    @ServiceDesc.setter
    def ServiceDesc(self, ServiceDesc):
        self._ServiceDesc = ServiceDesc

    @property
    def ExclusiveSetName(self):
        return self._ExclusiveSetName

    @ExclusiveSetName.setter
    def ExclusiveSetName(self, ExclusiveSetName):
        self._ExclusiveSetName = ExclusiveSetName

    @property
    def NetTypes(self):
        return self._NetTypes

    @NetTypes.setter
    def NetTypes(self, NetTypes):
        self._NetTypes = NetTypes

    @property
    def IpVersion(self):
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def SetServerName(self):
        return self._SetServerName

    @SetServerName.setter
    def SetServerName(self, SetServerName):
        self._SetServerName = SetServerName

    @property
    def AppIdType(self):
        return self._AppIdType

    @AppIdType.setter
    def AppIdType(self, AppIdType):
        self._AppIdType = AppIdType

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._Protocol = params.get("Protocol")
        self._ServiceDesc = params.get("ServiceDesc")
        self._ExclusiveSetName = params.get("ExclusiveSetName")
        self._NetTypes = params.get("NetTypes")
        self._IpVersion = params.get("IpVersion")
        self._SetServerName = params.get("SetServerName")
        self._AppIdType = params.get("AppIdType")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._UniqVpcId = params.get("UniqVpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceResponse(AbstractModel):
    """CreateService response structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _ServiceName: Custom service name.
        :type ServiceName: str
        :param _ServiceDesc: Custom service description.
        :type ServiceDesc: str
        :param _OuterSubDomain: Default public domain name.
        :type OuterSubDomain: str
        :param _InnerSubDomain: Default VPC domain name.
        :type InnerSubDomain: str
        :param _CreatedTime: Service creation time in the format of `YYYY-MM-DDThh:mm:ssZ` according to ISO 8601 standard. UTC time is used.
        :type CreatedTime: str
        :param _NetTypes: Network type list. INNER: private network access; OUTER: public network access.
        :type NetTypes: list of str
        :param _IpVersion: IP version number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ServiceId = None
        self._ServiceName = None
        self._ServiceDesc = None
        self._OuterSubDomain = None
        self._InnerSubDomain = None
        self._CreatedTime = None
        self._NetTypes = None
        self._IpVersion = None
        self._RequestId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceDesc(self):
        return self._ServiceDesc

    @ServiceDesc.setter
    def ServiceDesc(self, ServiceDesc):
        self._ServiceDesc = ServiceDesc

    @property
    def OuterSubDomain(self):
        return self._OuterSubDomain

    @OuterSubDomain.setter
    def OuterSubDomain(self, OuterSubDomain):
        self._OuterSubDomain = OuterSubDomain

    @property
    def InnerSubDomain(self):
        return self._InnerSubDomain

    @InnerSubDomain.setter
    def InnerSubDomain(self, InnerSubDomain):
        self._InnerSubDomain = InnerSubDomain

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def NetTypes(self):
        return self._NetTypes

    @NetTypes.setter
    def NetTypes(self, NetTypes):
        self._NetTypes = NetTypes

    @property
    def IpVersion(self):
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceName = params.get("ServiceName")
        self._ServiceDesc = params.get("ServiceDesc")
        self._OuterSubDomain = params.get("OuterSubDomain")
        self._InnerSubDomain = params.get("InnerSubDomain")
        self._CreatedTime = params.get("CreatedTime")
        self._NetTypes = params.get("NetTypes")
        self._IpVersion = params.get("IpVersion")
        self._RequestId = params.get("RequestId")


class CreateUpstreamRequest(AbstractModel):
    """CreateUpstream request structure.

    """

    def __init__(self):
        r"""
        :param _Scheme: Backend protocol. Valid values: `HTTP`, `HTTPS`
        :type Scheme: str
        :param _Algorithm: Load balancing algorithm. Valid value: `ROUND-ROBIN`
        :type Algorithm: str
        :param _UniqVpcId: Unique VPC ID
        :type UniqVpcId: str
        :param _UpstreamName: Upstream name
        :type UpstreamName: str
        :param _UpstreamDescription: Upstream description
        :type UpstreamDescription: str
        :param _UpstreamType: Upstream access type. Valid values: `IP_PORT`, `K8S`
        :type UpstreamType: str
        :param _Retries: Retry attempts. It defaults to `3`.
        :type Retries: int
        :param _UpstreamHost: The Host request header that forwarded from the gateway to backend
        :type UpstreamHost: str
        :param _Nodes: Backend nodes
        :type Nodes: list of UpstreamNode
        :param _Tags: Label
        :type Tags: list of Tag
        :param _HealthChecker: Health check configuration
        :type HealthChecker: :class:`tencentcloud.apigateway.v20180808.models.UpstreamHealthChecker`
        :param _K8sService: Configuration of TKE service
        :type K8sService: list of K8sService
        """
        self._Scheme = None
        self._Algorithm = None
        self._UniqVpcId = None
        self._UpstreamName = None
        self._UpstreamDescription = None
        self._UpstreamType = None
        self._Retries = None
        self._UpstreamHost = None
        self._Nodes = None
        self._Tags = None
        self._HealthChecker = None
        self._K8sService = None

    @property
    def Scheme(self):
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UpstreamName(self):
        return self._UpstreamName

    @UpstreamName.setter
    def UpstreamName(self, UpstreamName):
        self._UpstreamName = UpstreamName

    @property
    def UpstreamDescription(self):
        return self._UpstreamDescription

    @UpstreamDescription.setter
    def UpstreamDescription(self, UpstreamDescription):
        self._UpstreamDescription = UpstreamDescription

    @property
    def UpstreamType(self):
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def Retries(self):
        return self._Retries

    @Retries.setter
    def Retries(self, Retries):
        self._Retries = Retries

    @property
    def UpstreamHost(self):
        return self._UpstreamHost

    @UpstreamHost.setter
    def UpstreamHost(self, UpstreamHost):
        self._UpstreamHost = UpstreamHost

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HealthChecker(self):
        return self._HealthChecker

    @HealthChecker.setter
    def HealthChecker(self, HealthChecker):
        self._HealthChecker = HealthChecker

    @property
    def K8sService(self):
        return self._K8sService

    @K8sService.setter
    def K8sService(self, K8sService):
        self._K8sService = K8sService


    def _deserialize(self, params):
        self._Scheme = params.get("Scheme")
        self._Algorithm = params.get("Algorithm")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UpstreamName = params.get("UpstreamName")
        self._UpstreamDescription = params.get("UpstreamDescription")
        self._UpstreamType = params.get("UpstreamType")
        self._Retries = params.get("Retries")
        self._UpstreamHost = params.get("UpstreamHost")
        if params.get("Nodes") is not None:
            self._Nodes = []
            for item in params.get("Nodes"):
                obj = UpstreamNode()
                obj._deserialize(item)
                self._Nodes.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("HealthChecker") is not None:
            self._HealthChecker = UpstreamHealthChecker()
            self._HealthChecker._deserialize(params.get("HealthChecker"))
        if params.get("K8sService") is not None:
            self._K8sService = []
            for item in params.get("K8sService"):
                obj = K8sService()
                obj._deserialize(item)
                self._K8sService.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUpstreamResponse(AbstractModel):
    """CreateUpstream response structure.

    """

    def __init__(self):
        r"""
        :param _UpstreamId: The unique upstream ID returned
Note: This field may return `NULL`, indicating that no valid value was found.
        :type UpstreamId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UpstreamId = None
        self._RequestId = None

    @property
    def UpstreamId(self):
        return self._UpstreamId

    @UpstreamId.setter
    def UpstreamId(self, UpstreamId):
        self._UpstreamId = UpstreamId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UpstreamId = params.get("UpstreamId")
        self._RequestId = params.get("RequestId")


class CreateUsagePlanRequest(AbstractModel):
    """CreateUsagePlan request structure.

    """

    def __init__(self):
        r"""
        :param _UsagePlanName: Custom usage plan name.
        :type UsagePlanName: str
        :param _UsagePlanDesc: Custom usage plan description.
        :type UsagePlanDesc: str
        :param _MaxRequestNum: Total number of requests allowed. Valid values: -1, [1,99999999]. The default value is `-1`, which indicates no limit.
        :type MaxRequestNum: int
        :param _MaxRequestNumPreSec: Limit of requests per second. Valid values: -1, [1,2000]. The default value is `-1`, which indicates no limit.
        :type MaxRequestNumPreSec: int
        """
        self._UsagePlanName = None
        self._UsagePlanDesc = None
        self._MaxRequestNum = None
        self._MaxRequestNumPreSec = None

    @property
    def UsagePlanName(self):
        return self._UsagePlanName

    @UsagePlanName.setter
    def UsagePlanName(self, UsagePlanName):
        self._UsagePlanName = UsagePlanName

    @property
    def UsagePlanDesc(self):
        return self._UsagePlanDesc

    @UsagePlanDesc.setter
    def UsagePlanDesc(self, UsagePlanDesc):
        self._UsagePlanDesc = UsagePlanDesc

    @property
    def MaxRequestNum(self):
        return self._MaxRequestNum

    @MaxRequestNum.setter
    def MaxRequestNum(self, MaxRequestNum):
        self._MaxRequestNum = MaxRequestNum

    @property
    def MaxRequestNumPreSec(self):
        return self._MaxRequestNumPreSec

    @MaxRequestNumPreSec.setter
    def MaxRequestNumPreSec(self, MaxRequestNumPreSec):
        self._MaxRequestNumPreSec = MaxRequestNumPreSec


    def _deserialize(self, params):
        self._UsagePlanName = params.get("UsagePlanName")
        self._UsagePlanDesc = params.get("UsagePlanDesc")
        self._MaxRequestNum = params.get("MaxRequestNum")
        self._MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUsagePlanResponse(AbstractModel):
    """CreateUsagePlan response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Usage plan details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UsagePlanInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteAPIDocRequest(AbstractModel):
    """DeleteAPIDoc request structure.

    """

    def __init__(self):
        r"""
        :param _ApiDocId: API document ID
        :type ApiDocId: str
        """
        self._ApiDocId = None

    @property
    def ApiDocId(self):
        return self._ApiDocId

    @ApiDocId.setter
    def ApiDocId(self, ApiDocId):
        self._ApiDocId = ApiDocId


    def _deserialize(self, params):
        self._ApiDocId = params.get("ApiDocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAPIDocResponse(AbstractModel):
    """DeleteAPIDoc response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the operation succeeded
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteApiAppRequest(AbstractModel):
    """DeleteApiApp request structure.

    """

    def __init__(self):
        r"""
        :param _ApiAppId: Unique application ID.
        :type ApiAppId: str
        """
        self._ApiAppId = None

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId


    def _deserialize(self, params):
        self._ApiAppId = params.get("ApiAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApiAppResponse(AbstractModel):
    """DeleteApiApp response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether deletion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteApiKeyRequest(AbstractModel):
    """DeleteApiKey request structure.

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: ID of the key to be deleted.
        :type AccessKeyId: str
        """
        self._AccessKeyId = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApiKeyResponse(AbstractModel):
    """DeleteApiKey response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether deletion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteApiRequest(AbstractModel):
    """DeleteApi request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID of API.
        :type ServiceId: str
        :param _ApiId: Unique API ID.
        :type ApiId: str
        """
        self._ServiceId = None
        self._ApiId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApiResponse(AbstractModel):
    """DeleteApi response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether deletion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteIPStrategyRequest(AbstractModel):
    """DeleteIPStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID of the IP policy to be deleted.
        :type ServiceId: str
        :param _StrategyId: Unique ID of the IP policy to be deleted.
        :type StrategyId: str
        """
        self._ServiceId = None
        self._StrategyId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIPStrategyResponse(AbstractModel):
    """DeleteIPStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether deletion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeletePluginRequest(AbstractModel):
    """DeletePlugin request structure.

    """

    def __init__(self):
        r"""
        :param _PluginId: ID of the plugin to be deleted
        :type PluginId: str
        """
        self._PluginId = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePluginResponse(AbstractModel):
    """DeletePlugin response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Result of the deletion action
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteServiceRequest(AbstractModel):
    """DeleteService request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique ID of the service to be deleted.
        :type ServiceId: str
        :param _SkipVerification: A parameter used to set to skip the deletion precondition verification (only supported for services on dedicated instances).
        :type SkipVerification: int
        """
        self._ServiceId = None
        self._SkipVerification = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def SkipVerification(self):
        return self._SkipVerification

    @SkipVerification.setter
    def SkipVerification(self, SkipVerification):
        self._SkipVerification = SkipVerification


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._SkipVerification = params.get("SkipVerification")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceResponse(AbstractModel):
    """DeleteService response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether deletion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteServiceSubDomainMappingRequest(AbstractModel):
    """DeleteServiceSubDomainMapping request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _SubDomain: Custom domain name bound to service.
        :type SubDomain: str
        :param _Environment: Name of the environment whose mapping is to be deleted. Valid values: test (test environment), prepub (pre-release environment), release (release environment).
        :type Environment: str
        """
        self._ServiceId = None
        self._SubDomain = None
        self._Environment = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._SubDomain = params.get("SubDomain")
        self._Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceSubDomainMappingResponse(AbstractModel):
    """DeleteServiceSubDomainMapping response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the path mapping of the custom domain name is successfully deleted.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteUpstreamRequest(AbstractModel):
    """DeleteUpstream request structure.

    """

    def __init__(self):
        r"""
        :param _UpstreamId: ID of the upstream to be deleted
        :type UpstreamId: str
        """
        self._UpstreamId = None

    @property
    def UpstreamId(self):
        return self._UpstreamId

    @UpstreamId.setter
    def UpstreamId(self, UpstreamId):
        self._UpstreamId = UpstreamId


    def _deserialize(self, params):
        self._UpstreamId = params.get("UpstreamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUpstreamResponse(AbstractModel):
    """DeleteUpstream response structure.

    """

    def __init__(self):
        r"""
        :param _UpstreamId: ID of the deleted upstream
Note: This field may return `NULL`, indicating that no valid value was found.
        :type UpstreamId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UpstreamId = None
        self._RequestId = None

    @property
    def UpstreamId(self):
        return self._UpstreamId

    @UpstreamId.setter
    def UpstreamId(self, UpstreamId):
        self._UpstreamId = UpstreamId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UpstreamId = params.get("UpstreamId")
        self._RequestId = params.get("RequestId")


class DeleteUsagePlanRequest(AbstractModel):
    """DeleteUsagePlan request structure.

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: Unique ID of the usage plan to be deleted.
        :type UsagePlanId: str
        """
        self._UsagePlanId = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsagePlanResponse(AbstractModel):
    """DeleteUsagePlan response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether deletion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DemoteServiceUsagePlanRequest(AbstractModel):
    """DemoteServiceUsagePlan request structure.

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: Usage plan ID.
        :type UsagePlanId: str
        :param _ServiceId: Unique ID of the service to be demoted.
        :type ServiceId: str
        :param _Environment: Environment name.
        :type Environment: str
        """
        self._UsagePlanId = None
        self._ServiceId = None
        self._Environment = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        self._ServiceId = params.get("ServiceId")
        self._Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DemoteServiceUsagePlanResponse(AbstractModel):
    """DemoteServiceUsagePlan response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether demotion succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DesApisStatus(AbstractModel):
    """API status details

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _ApiId: Unique API ID.
        :type ApiId: str
        :param _ApiDesc: Custom API description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiDesc: str
        :param _CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param _ApiName: API name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiName: str
        :param _VpcId: VPC ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcId: int
        :param _UniqVpcId: Unique VPC ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UniqVpcId: str
        :param _ApiType: API type. Valid values: NORMAL (general API), TSF (microservice API).
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiType: str
        :param _Protocol: API protocol.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _IsDebugAfterCharge: Whether to enable debugging after purchase (reserved field for the marketplace)
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDebugAfterCharge: bool
        :param _AuthType: API authentication type. Valid values: `SECRET` (key pair authentication), `NONE` (no authentication), `OAUTH`, and `EIAM`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AuthType: str
        :param _ApiBusinessType: OAuth API type, which is valid if `AuthType` is `OAUTH`. Valid values: NORMAL (business API), OAUTH (authorization API).
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiBusinessType: str
        :param _AuthRelationApiId: Unique ID of associated authorization API, which takes effect only if `AuthType` is `OAUTH` and `ApiBusinessType` is `NORMAL`. It is the unique ID of the OAuth 2.0 authorization API bound to the business API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthRelationApiId: str
        :param _OauthConfig: OAuth configuration information, which takes effect if `AuthType` is `OAUTH`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param _RelationBuniessApiIds: List of business APIs associated with authorization API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RelationBuniessApiIds: list of str
        :param _Tags: Information of tags associated with API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of str
        :param _Path: API path, such as `/path`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Path: str
        :param _Method: API request method, such as `GET`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Method: str
        """
        self._ServiceId = None
        self._ApiId = None
        self._ApiDesc = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ApiName = None
        self._VpcId = None
        self._UniqVpcId = None
        self._ApiType = None
        self._Protocol = None
        self._IsDebugAfterCharge = None
        self._AuthType = None
        self._ApiBusinessType = None
        self._AuthRelationApiId = None
        self._OauthConfig = None
        self._RelationBuniessApiIds = None
        self._Tags = None
        self._Path = None
        self._Method = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiDesc(self):
        return self._ApiDesc

    @ApiDesc.setter
    def ApiDesc(self, ApiDesc):
        self._ApiDesc = ApiDesc

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def ApiType(self):
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def IsDebugAfterCharge(self):
        return self._IsDebugAfterCharge

    @IsDebugAfterCharge.setter
    def IsDebugAfterCharge(self, IsDebugAfterCharge):
        self._IsDebugAfterCharge = IsDebugAfterCharge

    @property
    def AuthType(self):
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ApiBusinessType(self):
        return self._ApiBusinessType

    @ApiBusinessType.setter
    def ApiBusinessType(self, ApiBusinessType):
        self._ApiBusinessType = ApiBusinessType

    @property
    def AuthRelationApiId(self):
        return self._AuthRelationApiId

    @AuthRelationApiId.setter
    def AuthRelationApiId(self, AuthRelationApiId):
        self._AuthRelationApiId = AuthRelationApiId

    @property
    def OauthConfig(self):
        return self._OauthConfig

    @OauthConfig.setter
    def OauthConfig(self, OauthConfig):
        self._OauthConfig = OauthConfig

    @property
    def RelationBuniessApiIds(self):
        return self._RelationBuniessApiIds

    @RelationBuniessApiIds.setter
    def RelationBuniessApiIds(self, RelationBuniessApiIds):
        self._RelationBuniessApiIds = RelationBuniessApiIds

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        self._ApiDesc = params.get("ApiDesc")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ApiName = params.get("ApiName")
        self._VpcId = params.get("VpcId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._ApiType = params.get("ApiType")
        self._Protocol = params.get("Protocol")
        self._IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        self._AuthType = params.get("AuthType")
        self._ApiBusinessType = params.get("ApiBusinessType")
        self._AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("OauthConfig") is not None:
            self._OauthConfig = OauthConfig()
            self._OauthConfig._deserialize(params.get("OauthConfig"))
        self._RelationBuniessApiIds = params.get("RelationBuniessApiIds")
        self._Tags = params.get("Tags")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIDocDetailRequest(AbstractModel):
    """DescribeAPIDocDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ApiDocId: API document ID
        :type ApiDocId: str
        """
        self._ApiDocId = None

    @property
    def ApiDocId(self):
        return self._ApiDocId

    @ApiDocId.setter
    def ApiDocId(self, ApiDocId):
        self._ApiDocId = ApiDocId


    def _deserialize(self, params):
        self._ApiDocId = params.get("ApiDocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIDocDetailResponse(AbstractModel):
    """DescribeAPIDocDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Result: API document details
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDocInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = APIDocInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeAPIDocsRequest(AbstractModel):
    """DescribeAPIDocs request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIDocsResponse(AbstractModel):
    """DescribeAPIDocs response structure.

    """

    def __init__(self):
        r"""
        :param _Result: API document list information
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDocs`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = APIDocs()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeAllPluginApisRequest(AbstractModel):
    """DescribeAllPluginApis request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: ID of the service to be queried
        :type ServiceId: str
        :param _PluginId: ID of the plugin to be queried
        :type PluginId: str
        :param _EnvironmentName: Environment information
        :type EnvironmentName: str
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100
        :type Limit: int
        :param _Offset: Offset. Default value: 0
        :type Offset: int
        """
        self._ServiceId = None
        self._PluginId = None
        self._EnvironmentName = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._PluginId = params.get("PluginId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllPluginApisResponse(AbstractModel):
    """DescribeAllPluginApis response structure.

    """

    def __init__(self):
        r"""
        :param _Result: List of APIs that ca use this plugin
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiInfoSummary`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiInfoSummary()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiAppBindApisStatusRequest(AbstractModel):
    """DescribeApiAppBindApisStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ApiAppId: Application ID
        :type ApiAppId: str
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter. Valid values: ApiId, ApiName, ServiceId, Environment, KeyWord (match with `name` or ID).
        :type Filters: list of Filter
        """
        self._ApiAppId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ApiAppId = params.get("ApiAppId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiAppBindApisStatusResponse(AbstractModel):
    """DescribeApiAppBindApisStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Result: List of APIs bound to the application.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppApiInfos`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiAppApiInfos()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiAppRequest(AbstractModel):
    """DescribeApiApp request structure.

    """

    def __init__(self):
        r"""
        :param _ApiAppId: Application ID.
        :type ApiAppId: str
        """
        self._ApiAppId = None

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId


    def _deserialize(self, params):
        self._ApiAppId = params.get("ApiAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiAppResponse(AbstractModel):
    """DescribeApiApp response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Application details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppInfos`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiAppInfos()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiAppsStatusRequest(AbstractModel):
    """DescribeApiAppsStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter. Valid values: ApiAppId, ApiAppName, KeyWord (match with `name` or ID).
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiAppsStatusResponse(AbstractModel):
    """DescribeApiAppsStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Application list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppInfos`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiAppInfos()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiBindApiAppsStatusRequest(AbstractModel):
    """DescribeApiBindApiAppsStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Service ID
        :type ServiceId: str
        :param _ApiIds: Array of API IDs
        :type ApiIds: list of str
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter. Valid values: ApiAppId, Environment, KeyWord (match with `name` or ID).
        :type Filters: list of Filter
        """
        self._ServiceId = None
        self._ApiIds = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiIds = params.get("ApiIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiBindApiAppsStatusResponse(AbstractModel):
    """DescribeApiBindApiAppsStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Result: List of APIs bound to the application.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppApiInfos`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiAppApiInfos()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiEnvironmentStrategyRequest(AbstractModel):
    """DescribeApiEnvironmentStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID of API.
        :type ServiceId: str
        :param _EnvironmentNames: Environment list.
        :type EnvironmentNames: list of str
        :param _ApiId: Unique API ID.
        :type ApiId: str
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._ServiceId = None
        self._EnvironmentNames = None
        self._ApiId = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def EnvironmentNames(self):
        return self._EnvironmentNames

    @EnvironmentNames.setter
    def EnvironmentNames(self, EnvironmentNames):
        self._EnvironmentNames = EnvironmentNames

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._EnvironmentNames = params.get("EnvironmentNames")
        self._ApiId = params.get("ApiId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiEnvironmentStrategyResponse(AbstractModel):
    """DescribeApiEnvironmentStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Details of policies bound to API
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiEnvironmentStrategyStataus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiEnvironmentStrategyStataus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiForApiAppRequest(AbstractModel):
    """DescribeApiForApiApp request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID of the API
        :type ServiceId: str
        :param _ApiId: Unique API ID
        :type ApiId: str
        :param _ApiRegion: API region
        :type ApiRegion: str
        """
        self._ServiceId = None
        self._ApiId = None
        self._ApiRegion = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiRegion(self):
        return self._ApiRegion

    @ApiRegion.setter
    def ApiRegion(self, ApiRegion):
        self._ApiRegion = ApiRegion


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        self._ApiRegion = params.get("ApiRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiForApiAppResponse(AbstractModel):
    """DescribeApiForApiApp response structure.

    """

    def __init__(self):
        r"""
        :param _Result: API details.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiKeyRequest(AbstractModel):
    """DescribeApiKey request structure.

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: API key ID.
        :type AccessKeyId: str
        """
        self._AccessKeyId = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiKeyResponse(AbstractModel):
    """DescribeApiKey response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Key details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiKey()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiKeysStatusRequest(AbstractModel):
    """DescribeApiKeysStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter. Valid values: AccessKeyId, AccessKeySecret, SecretName, NotUsagePlanId, Status, KeyWord (match with `name` or `path`).
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiKeysStatusResponse(AbstractModel):
    """DescribeApiKeysStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Key list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKeysStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiKeysStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiRequest(AbstractModel):
    """DescribeApi request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID of API.
        :type ServiceId: str
        :param _ApiId: Unique API ID.
        :type ApiId: str
        """
        self._ServiceId = None
        self._ApiId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiResponse(AbstractModel):
    """DescribeApi response structure.

    """

    def __init__(self):
        r"""
        :param _Result: API details.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiUsagePlanRequest(AbstractModel):
    """DescribeApiUsagePlan request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._ServiceId = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiUsagePlanResponse(AbstractModel):
    """DescribeApiUsagePlan response structure.

    """

    def __init__(self):
        r"""
        :param _Result: List of usage plans bound to API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiUsagePlanSet`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiUsagePlanSet()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApisStatusRequest(AbstractModel):
    """DescribeApisStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID of API.
        :type ServiceId: str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Filters: API filter. Valid values: `ApiId`, `ApiName`, `ApiPath`, `ApiType`, `AuthRelationApiId`, `AuthType`, `ApiBuniessType`, `NotUsagePlanId`, `Environment`, `Tags` (whose values are the list of `$tag_key:tag_value`), `TagKeys` (whose values are the list of tag keys). Note that `NotUsagePlanId` and `Environment` must be used in the same time.
        :type Filters: list of Filter
        """
        self._ServiceId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApisStatusResponse(AbstractModel):
    """DescribeApisStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Result: List of API details.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApisStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApisStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeIPStrategyApisStatusRequest(AbstractModel):
    """DescribeIPStrategyApisStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _StrategyId: Unique policy ID.
        :type StrategyId: str
        :param _EnvironmentName: Policy environment.
        :type EnvironmentName: str
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter. Valid values: ApiPath, ApiName, KeyWord (fuzzy search by `Path` and `Name`).
        :type Filters: list of Filter
        """
        self._ServiceId = None
        self._StrategyId = None
        self._EnvironmentName = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._StrategyId = params.get("StrategyId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPStrategyApisStatusResponse(AbstractModel):
    """DescribeIPStrategyApisStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Result: List of APIs bound to environment.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategyApiStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = IPStrategyApiStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeIPStrategyRequest(AbstractModel):
    """DescribeIPStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _StrategyId: Unique IP policy ID.
        :type StrategyId: str
        :param _EnvironmentName: Environment associated with policy.
        :type EnvironmentName: str
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter, which is a reserved field. Filtering is not supported currently.
        :type Filters: list of Filter
        """
        self._ServiceId = None
        self._StrategyId = None
        self._EnvironmentName = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._StrategyId = params.get("StrategyId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPStrategyResponse(AbstractModel):
    """DescribeIPStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Result: IP policy details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategy`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = IPStrategy()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeIPStrategysStatusRequest(AbstractModel):
    """DescribeIPStrategysStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _Filters: Filter. Valid values: StrategyName.
        :type Filters: list of Filter
        """
        self._ServiceId = None
        self._Filters = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPStrategysStatusResponse(AbstractModel):
    """DescribeIPStrategysStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Result: List of eligible policies.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategysStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = IPStrategysStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeLogSearchRequest(AbstractModel):
    """DescribeLogSearch request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Log start time
        :type StartTime: str
        :param _EndTime: Log end time
        :type EndTime: str
        :param _ServiceId: Service ID
        :type ServiceId: str
        :param _Filters: Reserved field
        :type Filters: list of Filter
        :param _Limit: Number of logs to be returned at a time. Maximum value: 100
        :type Limit: int
        :param _ConText: Subsequent content can be obtained based on the `ConText` returned last time. Up to 10,000 data entries can be obtained
        :type ConText: str
        :param _Sort: Sorting by time. Valid values: asc (ascending), desc (descending). Default value: desc
        :type Sort: str
        :param _Query: Reserved field
        :type Query: str
        :param _LogQuerys: Search criterion. Valid values:
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
        self._StartTime = None
        self._EndTime = None
        self._ServiceId = None
        self._Filters = None
        self._Limit = None
        self._ConText = None
        self._Sort = None
        self._Query = None
        self._LogQuerys = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ConText(self):
        return self._ConText

    @ConText.setter
    def ConText(self, ConText):
        self._ConText = ConText

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def LogQuerys(self):
        return self._LogQuerys

    @LogQuerys.setter
    def LogQuerys(self, LogQuerys):
        self._LogQuerys = LogQuerys


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ServiceId = params.get("ServiceId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._ConText = params.get("ConText")
        self._Sort = params.get("Sort")
        self._Query = params.get("Query")
        if params.get("LogQuerys") is not None:
            self._LogQuerys = []
            for item in params.get("LogQuerys"):
                obj = LogQuery()
                obj._deserialize(item)
                self._LogQuerys.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogSearchResponse(AbstractModel):
    """DescribeLogSearch response structure.

    """

    def __init__(self):
        r"""
        :param _ConText: Cursor for getting more search results. If the value is `""`, there will be no subsequent results
        :type ConText: str
        :param _LogSet: The returned result contains any number of logs, which are in the following format:
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
        :param _TotalCount: Number of logs returned for one search (`TotalCount <= Limit`)
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ConText = None
        self._LogSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ConText(self):
        return self._ConText

    @ConText.setter
    def ConText(self, ConText):
        self._ConText = ConText

    @property
    def LogSet(self):
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ConText = params.get("ConText")
        self._LogSet = params.get("LogSet")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePluginApisRequest(AbstractModel):
    """DescribePluginApis request structure.

    """

    def __init__(self):
        r"""
        :param _PluginId: ID of the plugin to be queried
        :type PluginId: str
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100
        :type Limit: int
        :param _Offset: Offset. Default value: 0
        :type Offset: int
        """
        self._PluginId = None
        self._Limit = None
        self._Offset = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePluginApisResponse(AbstractModel):
    """DescribePluginApis response structure.

    """

    def __init__(self):
        r"""
        :param _Result: List of APIs bound with the plugin
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.AttachedApiSummary`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = AttachedApiSummary()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribePluginRequest(AbstractModel):
    """DescribePlugin request structure.

    """

    def __init__(self):
        r"""
        :param _PluginId: ID of the plugin to be queried
        :type PluginId: str
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100
        :type Limit: int
        :param _Offset: Offset. Default value: 0
        :type Offset: int
        """
        self._PluginId = None
        self._Limit = None
        self._Offset = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePluginResponse(AbstractModel):
    """DescribePlugin response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Plugin details
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.Plugin`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = Plugin()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribePluginsByApiRequest(AbstractModel):
    """DescribePluginsByApi request structure.

    """

    def __init__(self):
        r"""
        :param _ApiId: ID of the API to query
        :type ApiId: str
        :param _ServiceId: ID of the service to query
        :type ServiceId: str
        :param _EnvironmentName: Environment information
        :type EnvironmentName: str
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100
        :type Limit: int
        :param _Offset: Offset. Default value: 0
        :type Offset: int
        """
        self._ApiId = None
        self._ServiceId = None
        self._EnvironmentName = None
        self._Limit = None
        self._Offset = None

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ApiId = params.get("ApiId")
        self._ServiceId = params.get("ServiceId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePluginsByApiResponse(AbstractModel):
    """DescribePluginsByApi response structure.

    """

    def __init__(self):
        r"""
        :param _Result: List of plug-ins bound with the API
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.AttachedPluginSummary`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = AttachedPluginSummary()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeServiceEnvironmentListRequest(AbstractModel):
    """DescribeServiceEnvironmentList request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._ServiceId = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceEnvironmentListResponse(AbstractModel):
    """DescribeServiceEnvironmentList response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Details of environments bound to service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceEnvironmentSet`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ServiceEnvironmentSet()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeServiceEnvironmentReleaseHistoryRequest(AbstractModel):
    """DescribeServiceEnvironmentReleaseHistory request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        :param _EnvironmentName: Environment name.
        :type EnvironmentName: str
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._ServiceId = None
        self._EnvironmentName = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceEnvironmentReleaseHistoryResponse(AbstractModel):
    """DescribeServiceEnvironmentReleaseHistory response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Service release history.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceReleaseHistory`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ServiceReleaseHistory()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeServiceEnvironmentStrategyRequest(AbstractModel):
    """DescribeServiceEnvironmentStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._ServiceId = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceEnvironmentStrategyResponse(AbstractModel):
    """DescribeServiceEnvironmentStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Throttling policy list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceEnvironmentStrategyStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ServiceEnvironmentStrategyStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeServiceForApiAppRequest(AbstractModel):
    """DescribeServiceForApiApp request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        :param _ApiRegion: Service region.
        :type ApiRegion: str
        """
        self._ServiceId = None
        self._ApiRegion = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiRegion(self):
        return self._ApiRegion

    @ApiRegion.setter
    def ApiRegion(self, ApiRegion):
        self._ApiRegion = ApiRegion


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiRegion = params.get("ApiRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceForApiAppResponse(AbstractModel):
    """DescribeServiceForApiApp response structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _AvailableEnvironments: Service environment list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AvailableEnvironments: list of str
        :param _ServiceName: Service name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceName: str
        :param _ServiceDesc: Service description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceDesc: str
        :param _Protocol: Protocol supported by service. Valid values: http, https, http&https.
        :type Protocol: str
        :param _CreatedTime: Service creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _ModifiedTime: Service modification time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param _ExclusiveSetName: Self-Deployed cluster name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExclusiveSetName: str
        :param _NetTypes: Network type list. INNER: private network access; OUTER: public network access.
        :type NetTypes: list of str
        :param _InternalSubDomain: Subdomain name for private network access.
        :type InternalSubDomain: str
        :param _OuterSubDomain: Subdomain name for public network access.
        :type OuterSubDomain: str
        :param _InnerHttpPort: Service port number for HTTP access over private network.
        :type InnerHttpPort: int
        :param _InnerHttpsPort: Port number for HTTPS access over private network.
        :type InnerHttpsPort: int
        :param _ApiTotalCount: Total number of APIs.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiTotalCount: int
        :param _ApiIdStatusSet: API list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiIdStatusSet: list of ApiIdStatus
        :param _UsagePlanTotalCount: Total number of usage plans.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanTotalCount: int
        :param _UsagePlanList: Usage plan array.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanList: list of UsagePlan
        :param _IpVersion: IP version.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpVersion: str
        :param _UserType: Service user type.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserType: str
        :param _SetId: Reserved field.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SetId: int
        :param _Tags: Tag bound to the service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ServiceId = None
        self._AvailableEnvironments = None
        self._ServiceName = None
        self._ServiceDesc = None
        self._Protocol = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ExclusiveSetName = None
        self._NetTypes = None
        self._InternalSubDomain = None
        self._OuterSubDomain = None
        self._InnerHttpPort = None
        self._InnerHttpsPort = None
        self._ApiTotalCount = None
        self._ApiIdStatusSet = None
        self._UsagePlanTotalCount = None
        self._UsagePlanList = None
        self._IpVersion = None
        self._UserType = None
        self._SetId = None
        self._Tags = None
        self._RequestId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def AvailableEnvironments(self):
        return self._AvailableEnvironments

    @AvailableEnvironments.setter
    def AvailableEnvironments(self, AvailableEnvironments):
        self._AvailableEnvironments = AvailableEnvironments

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceDesc(self):
        return self._ServiceDesc

    @ServiceDesc.setter
    def ServiceDesc(self, ServiceDesc):
        self._ServiceDesc = ServiceDesc

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ExclusiveSetName(self):
        return self._ExclusiveSetName

    @ExclusiveSetName.setter
    def ExclusiveSetName(self, ExclusiveSetName):
        self._ExclusiveSetName = ExclusiveSetName

    @property
    def NetTypes(self):
        return self._NetTypes

    @NetTypes.setter
    def NetTypes(self, NetTypes):
        self._NetTypes = NetTypes

    @property
    def InternalSubDomain(self):
        return self._InternalSubDomain

    @InternalSubDomain.setter
    def InternalSubDomain(self, InternalSubDomain):
        self._InternalSubDomain = InternalSubDomain

    @property
    def OuterSubDomain(self):
        return self._OuterSubDomain

    @OuterSubDomain.setter
    def OuterSubDomain(self, OuterSubDomain):
        self._OuterSubDomain = OuterSubDomain

    @property
    def InnerHttpPort(self):
        return self._InnerHttpPort

    @InnerHttpPort.setter
    def InnerHttpPort(self, InnerHttpPort):
        self._InnerHttpPort = InnerHttpPort

    @property
    def InnerHttpsPort(self):
        return self._InnerHttpsPort

    @InnerHttpsPort.setter
    def InnerHttpsPort(self, InnerHttpsPort):
        self._InnerHttpsPort = InnerHttpsPort

    @property
    def ApiTotalCount(self):
        return self._ApiTotalCount

    @ApiTotalCount.setter
    def ApiTotalCount(self, ApiTotalCount):
        self._ApiTotalCount = ApiTotalCount

    @property
    def ApiIdStatusSet(self):
        return self._ApiIdStatusSet

    @ApiIdStatusSet.setter
    def ApiIdStatusSet(self, ApiIdStatusSet):
        self._ApiIdStatusSet = ApiIdStatusSet

    @property
    def UsagePlanTotalCount(self):
        return self._UsagePlanTotalCount

    @UsagePlanTotalCount.setter
    def UsagePlanTotalCount(self, UsagePlanTotalCount):
        self._UsagePlanTotalCount = UsagePlanTotalCount

    @property
    def UsagePlanList(self):
        return self._UsagePlanList

    @UsagePlanList.setter
    def UsagePlanList(self, UsagePlanList):
        self._UsagePlanList = UsagePlanList

    @property
    def IpVersion(self):
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def SetId(self):
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._AvailableEnvironments = params.get("AvailableEnvironments")
        self._ServiceName = params.get("ServiceName")
        self._ServiceDesc = params.get("ServiceDesc")
        self._Protocol = params.get("Protocol")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ExclusiveSetName = params.get("ExclusiveSetName")
        self._NetTypes = params.get("NetTypes")
        self._InternalSubDomain = params.get("InternalSubDomain")
        self._OuterSubDomain = params.get("OuterSubDomain")
        self._InnerHttpPort = params.get("InnerHttpPort")
        self._InnerHttpsPort = params.get("InnerHttpsPort")
        self._ApiTotalCount = params.get("ApiTotalCount")
        if params.get("ApiIdStatusSet") is not None:
            self._ApiIdStatusSet = []
            for item in params.get("ApiIdStatusSet"):
                obj = ApiIdStatus()
                obj._deserialize(item)
                self._ApiIdStatusSet.append(obj)
        self._UsagePlanTotalCount = params.get("UsagePlanTotalCount")
        if params.get("UsagePlanList") is not None:
            self._UsagePlanList = []
            for item in params.get("UsagePlanList"):
                obj = UsagePlan()
                obj._deserialize(item)
                self._UsagePlanList.append(obj)
        self._IpVersion = params.get("IpVersion")
        self._UserType = params.get("UserType")
        self._SetId = params.get("SetId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeServiceReleaseVersionRequest(AbstractModel):
    """DescribeServiceReleaseVersion request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._ServiceId = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceReleaseVersionResponse(AbstractModel):
    """DescribeServiceReleaseVersion response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Service release version list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceReleaseVersion`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ServiceReleaseVersion()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeServiceRequest(AbstractModel):
    """DescribeService request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        """
        self._ServiceId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceResponse(AbstractModel):
    """DescribeService response structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _AvailableEnvironments: Service environment list.
        :type AvailableEnvironments: list of str
        :param _ServiceName: Service name.
        :type ServiceName: str
        :param _ServiceDesc: Service description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceDesc: str
        :param _Protocol: Protocol supported by service. Valid values: http, https, http&https.
        :type Protocol: str
        :param _CreatedTime: Service creation time.
        :type CreatedTime: str
        :param _ModifiedTime: Service modification time.
        :type ModifiedTime: str
        :param _ExclusiveSetName: Dedicated cluster name.
        :type ExclusiveSetName: str
        :param _NetTypes: Network type list. INNER: private network access; OUTER: public network access.
        :type NetTypes: list of str
        :param _InternalSubDomain: Subdomain name for private network access.
        :type InternalSubDomain: str
        :param _OuterSubDomain: Subdomain name for public network access.
        :type OuterSubDomain: str
        :param _InnerHttpPort: Service port number for HTTP access over private network.
        :type InnerHttpPort: int
        :param _InnerHttpsPort: Port number for HTTPS access over private network.
        :type InnerHttpsPort: int
        :param _ApiTotalCount: Total number of APIs.
        :type ApiTotalCount: int
        :param _ApiIdStatusSet: API list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiIdStatusSet: list of ApiIdStatus
        :param _UsagePlanTotalCount: Total number of usage plans.
        :type UsagePlanTotalCount: int
        :param _UsagePlanList: Usage plan array.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanList: list of UsagePlan
        :param _IpVersion: IP version.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpVersion: str
        :param _UserType: Service user type.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserType: str
        :param _SetId: Reserved field.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SetId: int
        :param _Tags: Tags bound to a service.
Note: this field may return null, indicating that no valid values found.
        :type Tags: list of Tag
        :param _InstanceId: Dedicated instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _InstanceName: Dedicated instance name
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _SetType: Cluster type
Note: this field may return null, indicating that no valid values can be obtained.
        :type SetType: str
        :param _DeploymentType: Cluster type for service deployment
Note: this field may return null, indicating that no valid values found.
        :type DeploymentType: str
        :param _SpecialUse: Whether the service if for special usage. Valid values: `DEFAULT` (general usage), `HTTP_DNS`.
Note: This field may return `NULL`, indicating that no valid value was found.
        :type SpecialUse: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ServiceId = None
        self._AvailableEnvironments = None
        self._ServiceName = None
        self._ServiceDesc = None
        self._Protocol = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ExclusiveSetName = None
        self._NetTypes = None
        self._InternalSubDomain = None
        self._OuterSubDomain = None
        self._InnerHttpPort = None
        self._InnerHttpsPort = None
        self._ApiTotalCount = None
        self._ApiIdStatusSet = None
        self._UsagePlanTotalCount = None
        self._UsagePlanList = None
        self._IpVersion = None
        self._UserType = None
        self._SetId = None
        self._Tags = None
        self._InstanceId = None
        self._InstanceName = None
        self._SetType = None
        self._DeploymentType = None
        self._SpecialUse = None
        self._RequestId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def AvailableEnvironments(self):
        return self._AvailableEnvironments

    @AvailableEnvironments.setter
    def AvailableEnvironments(self, AvailableEnvironments):
        self._AvailableEnvironments = AvailableEnvironments

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceDesc(self):
        return self._ServiceDesc

    @ServiceDesc.setter
    def ServiceDesc(self, ServiceDesc):
        self._ServiceDesc = ServiceDesc

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ExclusiveSetName(self):
        return self._ExclusiveSetName

    @ExclusiveSetName.setter
    def ExclusiveSetName(self, ExclusiveSetName):
        self._ExclusiveSetName = ExclusiveSetName

    @property
    def NetTypes(self):
        return self._NetTypes

    @NetTypes.setter
    def NetTypes(self, NetTypes):
        self._NetTypes = NetTypes

    @property
    def InternalSubDomain(self):
        return self._InternalSubDomain

    @InternalSubDomain.setter
    def InternalSubDomain(self, InternalSubDomain):
        self._InternalSubDomain = InternalSubDomain

    @property
    def OuterSubDomain(self):
        return self._OuterSubDomain

    @OuterSubDomain.setter
    def OuterSubDomain(self, OuterSubDomain):
        self._OuterSubDomain = OuterSubDomain

    @property
    def InnerHttpPort(self):
        return self._InnerHttpPort

    @InnerHttpPort.setter
    def InnerHttpPort(self, InnerHttpPort):
        self._InnerHttpPort = InnerHttpPort

    @property
    def InnerHttpsPort(self):
        return self._InnerHttpsPort

    @InnerHttpsPort.setter
    def InnerHttpsPort(self, InnerHttpsPort):
        self._InnerHttpsPort = InnerHttpsPort

    @property
    def ApiTotalCount(self):
        return self._ApiTotalCount

    @ApiTotalCount.setter
    def ApiTotalCount(self, ApiTotalCount):
        self._ApiTotalCount = ApiTotalCount

    @property
    def ApiIdStatusSet(self):
        return self._ApiIdStatusSet

    @ApiIdStatusSet.setter
    def ApiIdStatusSet(self, ApiIdStatusSet):
        self._ApiIdStatusSet = ApiIdStatusSet

    @property
    def UsagePlanTotalCount(self):
        return self._UsagePlanTotalCount

    @UsagePlanTotalCount.setter
    def UsagePlanTotalCount(self, UsagePlanTotalCount):
        self._UsagePlanTotalCount = UsagePlanTotalCount

    @property
    def UsagePlanList(self):
        return self._UsagePlanList

    @UsagePlanList.setter
    def UsagePlanList(self, UsagePlanList):
        self._UsagePlanList = UsagePlanList

    @property
    def IpVersion(self):
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def SetId(self):
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def SetType(self):
        return self._SetType

    @SetType.setter
    def SetType(self, SetType):
        self._SetType = SetType

    @property
    def DeploymentType(self):
        return self._DeploymentType

    @DeploymentType.setter
    def DeploymentType(self, DeploymentType):
        self._DeploymentType = DeploymentType

    @property
    def SpecialUse(self):
        return self._SpecialUse

    @SpecialUse.setter
    def SpecialUse(self, SpecialUse):
        self._SpecialUse = SpecialUse

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._AvailableEnvironments = params.get("AvailableEnvironments")
        self._ServiceName = params.get("ServiceName")
        self._ServiceDesc = params.get("ServiceDesc")
        self._Protocol = params.get("Protocol")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ExclusiveSetName = params.get("ExclusiveSetName")
        self._NetTypes = params.get("NetTypes")
        self._InternalSubDomain = params.get("InternalSubDomain")
        self._OuterSubDomain = params.get("OuterSubDomain")
        self._InnerHttpPort = params.get("InnerHttpPort")
        self._InnerHttpsPort = params.get("InnerHttpsPort")
        self._ApiTotalCount = params.get("ApiTotalCount")
        if params.get("ApiIdStatusSet") is not None:
            self._ApiIdStatusSet = []
            for item in params.get("ApiIdStatusSet"):
                obj = ApiIdStatus()
                obj._deserialize(item)
                self._ApiIdStatusSet.append(obj)
        self._UsagePlanTotalCount = params.get("UsagePlanTotalCount")
        if params.get("UsagePlanList") is not None:
            self._UsagePlanList = []
            for item in params.get("UsagePlanList"):
                obj = UsagePlan()
                obj._deserialize(item)
                self._UsagePlanList.append(obj)
        self._IpVersion = params.get("IpVersion")
        self._UserType = params.get("UserType")
        self._SetId = params.get("SetId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._SetType = params.get("SetType")
        self._DeploymentType = params.get("DeploymentType")
        self._SpecialUse = params.get("SpecialUse")
        self._RequestId = params.get("RequestId")


class DescribeServiceSubDomainMappingsRequest(AbstractModel):
    """DescribeServiceSubDomainMappings request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _SubDomain: Custom domain name bound to service.
        :type SubDomain: str
        """
        self._ServiceId = None
        self._SubDomain = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._SubDomain = params.get("SubDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceSubDomainMappingsResponse(AbstractModel):
    """DescribeServiceSubDomainMappings response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Custom path mapping list.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceSubDomainMappings`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ServiceSubDomainMappings()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeServiceSubDomainsRequest(AbstractModel):
    """DescribeServiceSubDomains request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._ServiceId = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceSubDomainsResponse(AbstractModel):
    """DescribeServiceSubDomains response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Custom service domain name query.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DomainSets`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DomainSets()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeServiceUsagePlanRequest(AbstractModel):
    """DescribeServiceUsagePlan request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique ID of the service to be queried.
        :type ServiceId: str
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._ServiceId = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceUsagePlanResponse(AbstractModel):
    """DescribeServiceUsagePlan response structure.

    """

    def __init__(self):
        r"""
        :param _Result: List of usage plans bound to service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceUsagePlanSet`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ServiceUsagePlanSet()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeServicesStatusRequest(AbstractModel):
    """DescribeServicesStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter. Valid values: `ServiceId`, `ServiceName`, `NotUsagePlanId`, `Environment`, `IpVersion`, `InstanceId`, `NetType`, `EIAMAppId`.
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServicesStatusResponse(AbstractModel):
    """DescribeServicesStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Service list query result.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServicesStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ServicesStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeUpstreamBindApis(AbstractModel):
    """Queries APIs bound with an upstream

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _BindApiSet: Information of bound APIs
        :type BindApiSet: list of BindApiInfo
        """
        self._TotalCount = None
        self._BindApiSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BindApiSet(self):
        return self._BindApiSet

    @BindApiSet.setter
    def BindApiSet(self, BindApiSet):
        self._BindApiSet = BindApiSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BindApiSet") is not None:
            self._BindApiSet = []
            for item in params.get("BindApiSet"):
                obj = BindApiInfo()
                obj._deserialize(item)
                self._BindApiSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpstreamBindApisRequest(AbstractModel):
    """DescribeUpstreamBindApis request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of entries per page
        :type Limit: int
        :param _Offset: The starting position of paging
        :type Offset: int
        :param _UpstreamId: Upstream ID
        :type UpstreamId: str
        :param _Filters: Filters the results by `ServiceId` and `ApiId`
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._UpstreamId = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def UpstreamId(self):
        return self._UpstreamId

    @UpstreamId.setter
    def UpstreamId(self, UpstreamId):
        self._UpstreamId = UpstreamId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._UpstreamId = params.get("UpstreamId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpstreamBindApisResponse(AbstractModel):
    """DescribeUpstreamBindApis response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Query results
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DescribeUpstreamBindApis`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeUpstreamBindApis()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeUpstreamInfo(AbstractModel):
    """The returned result of upstream query

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results
        :type TotalCount: int
        :param _UpstreamSet: List of query result
        :type UpstreamSet: list of UpstreamInfo
        """
        self._TotalCount = None
        self._UpstreamSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UpstreamSet(self):
        return self._UpstreamSet

    @UpstreamSet.setter
    def UpstreamSet(self, UpstreamSet):
        self._UpstreamSet = UpstreamSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("UpstreamSet") is not None:
            self._UpstreamSet = []
            for item in params.get("UpstreamSet"):
                obj = UpstreamInfo()
                obj._deserialize(item)
                self._UpstreamSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpstreamsRequest(AbstractModel):
    """DescribeUpstreams request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of entries per page
        :type Limit: int
        :param _Offset: The starting position of paging
        :type Offset: int
        :param _Filters: Filters. Valid values: `UpstreamId` and `UpstreamName`
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpstreamsResponse(AbstractModel):
    """DescribeUpstreams response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Query results
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DescribeUpstreamInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeUpstreamInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeUsagePlanEnvironmentsRequest(AbstractModel):
    """DescribeUsagePlanEnvironments request structure.

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: Unique ID of the usage plan to be queried.
        :type UsagePlanId: str
        :param _BindType: Binding type. Valid values: API, SERVICE. Default value: SERVICE.
        :type BindType: str
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._UsagePlanId = None
        self._BindType = None
        self._Limit = None
        self._Offset = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def BindType(self):
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        self._BindType = params.get("BindType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsagePlanEnvironmentsResponse(AbstractModel):
    """DescribeUsagePlanEnvironments response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Usage plan binding details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanEnvironmentStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UsagePlanEnvironmentStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeUsagePlanRequest(AbstractModel):
    """DescribeUsagePlan request structure.

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: Unique ID of the usage plan to be queried.
        :type UsagePlanId: str
        """
        self._UsagePlanId = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsagePlanResponse(AbstractModel):
    """DescribeUsagePlan response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Usage plan details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UsagePlanInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeUsagePlanSecretIdsRequest(AbstractModel):
    """DescribeUsagePlanSecretIds request structure.

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: Unique ID of bound usage plan.
        :type UsagePlanId: str
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._UsagePlanId = None
        self._Limit = None
        self._Offset = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsagePlanSecretIdsResponse(AbstractModel):
    """DescribeUsagePlanSecretIds response structure.

    """

    def __init__(self):
        r"""
        :param _Result: List of keys bound to usage plan.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanBindSecretStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UsagePlanBindSecretStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeUsagePlansStatusRequest(AbstractModel):
    """DescribeUsagePlansStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Usage plan filter. Valid values: UsagePlanId, UsagePlanName, NotServiceId, NotApiId, Environment.
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsagePlansStatusResponse(AbstractModel):
    """DescribeUsagePlansStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Usage plan list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlansStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UsagePlansStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DetachPluginRequest(AbstractModel):
    """DetachPlugin request structure.

    """

    def __init__(self):
        r"""
        :param _PluginId: ID of the plugin to be unbound
        :type PluginId: str
        :param _ServiceId: Service ID
        :type ServiceId: str
        :param _EnvironmentName: API environment
        :type EnvironmentName: str
        :param _ApiId: ID of the API to unbind from the plugin
        :type ApiId: str
        """
        self._PluginId = None
        self._ServiceId = None
        self._EnvironmentName = None
        self._ApiId = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._ServiceId = params.get("ServiceId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachPluginResponse(AbstractModel):
    """DetachPlugin response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether unbinding succeeded.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DisableApiKeyRequest(AbstractModel):
    """DisableApiKey request structure.

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: ID of the key to be disabled.
        :type AccessKeyId: str
        """
        self._AccessKeyId = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableApiKeyResponse(AbstractModel):
    """DisableApiKey response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the key is successfully disabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DocumentSDK(AbstractModel):
    """API document download

    """

    def __init__(self):
        r"""
        :param _DocumentURL: Download link of generated file. Generated documents will be stored in COS.
        :type DocumentURL: str
        :param _SdkURL: Download link of generated SDK file. Generated SDK files will be stored in COS.
        :type SdkURL: str
        """
        self._DocumentURL = None
        self._SdkURL = None

    @property
    def DocumentURL(self):
        return self._DocumentURL

    @DocumentURL.setter
    def DocumentURL(self, DocumentURL):
        self._DocumentURL = DocumentURL

    @property
    def SdkURL(self):
        return self._SdkURL

    @SdkURL.setter
    def SdkURL(self, SdkURL):
        self._SdkURL = SdkURL


    def _deserialize(self, params):
        self._DocumentURL = params.get("DocumentURL")
        self._SdkURL = params.get("SdkURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainSetList(AbstractModel):
    """Custom service domain name list

    """

    def __init__(self):
        r"""
        :param _DomainName: Domain name.
        :type DomainName: str
        :param _Status: Domain name resolution status. `1`: normal, `0`: failed
        :type Status: int
        :param _CertificateId: Certificate ID.
        :type CertificateId: str
        :param _IsDefaultMapping: Whether the default path mapping is used.
        :type IsDefaultMapping: bool
        :param _Protocol: Custom domain name protocol type.
        :type Protocol: str
        :param _NetType: Network type. Valid values: INNER, OUTER.
        :type NetType: str
        :param _IsForcedHttps: Whether to force HTTP requests to redirect to HTTPS. Default value: `false`. When this parameter is `true`, API Gateway will redirect all requests using the custom domain name over the HTTP protocol to the HTTPS protocol for forwarding.
        :type IsForcedHttps: bool
        :param _RegistrationStatus: ICP filing status
        :type RegistrationStatus: bool
        """
        self._DomainName = None
        self._Status = None
        self._CertificateId = None
        self._IsDefaultMapping = None
        self._Protocol = None
        self._NetType = None
        self._IsForcedHttps = None
        self._RegistrationStatus = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsDefaultMapping(self):
        return self._IsDefaultMapping

    @IsDefaultMapping.setter
    def IsDefaultMapping(self, IsDefaultMapping):
        self._IsDefaultMapping = IsDefaultMapping

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def IsForcedHttps(self):
        return self._IsForcedHttps

    @IsForcedHttps.setter
    def IsForcedHttps(self, IsForcedHttps):
        self._IsForcedHttps = IsForcedHttps

    @property
    def RegistrationStatus(self):
        return self._RegistrationStatus

    @RegistrationStatus.setter
    def RegistrationStatus(self, RegistrationStatus):
        self._RegistrationStatus = RegistrationStatus


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._Status = params.get("Status")
        self._CertificateId = params.get("CertificateId")
        self._IsDefaultMapping = params.get("IsDefaultMapping")
        self._Protocol = params.get("Protocol")
        self._NetType = params.get("NetType")
        self._IsForcedHttps = params.get("IsForcedHttps")
        self._RegistrationStatus = params.get("RegistrationStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainSets(AbstractModel):
    """Custom service domain name information

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of custom domain names under service
        :type TotalCount: int
        :param _DomainSet: Custom service domain name list.
        :type DomainSet: list of DomainSetList
        """
        self._TotalCount = None
        self._DomainSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DomainSet(self):
        return self._DomainSet

    @DomainSet.setter
    def DomainSet(self, DomainSet):
        self._DomainSet = DomainSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DomainSet") is not None:
            self._DomainSet = []
            for item in params.get("DomainSet"):
                obj = DomainSetList()
                obj._deserialize(item)
                self._DomainSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApiKeyRequest(AbstractModel):
    """EnableApiKey request structure.

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: ID of the key to be enabled.
        :type AccessKeyId: str
        """
        self._AccessKeyId = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApiKeyResponse(AbstractModel):
    """EnableApiKey response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the key is successfully enabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class Environment(AbstractModel):
    """Information of service release environment.

    """

    def __init__(self):
        r"""
        :param _EnvironmentName: Environment name.
        :type EnvironmentName: str
        :param _Url: Access path.
        :type Url: str
        :param _Status: Release status. 1: published. 0: not published.
        :type Status: int
        :param _VersionName: Running version.
        :type VersionName: str
        """
        self._EnvironmentName = None
        self._Url = None
        self._Status = None
        self._VersionName = None

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName


    def _deserialize(self, params):
        self._EnvironmentName = params.get("EnvironmentName")
        self._Url = params.get("Url")
        self._Status = params.get("Status")
        self._VersionName = params.get("VersionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvironmentStrategy(AbstractModel):
    """Environment throttling

    """

    def __init__(self):
        r"""
        :param _EnvironmentName: Environment name
        :type EnvironmentName: str
        :param _Quota: Throttling value
        :type Quota: int
        :param _MaxQuota: Maximum quota value
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxQuota: int
        """
        self._EnvironmentName = None
        self._Quota = None
        self._MaxQuota = None

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Quota(self):
        return self._Quota

    @Quota.setter
    def Quota(self, Quota):
        self._Quota = Quota

    @property
    def MaxQuota(self):
        return self._MaxQuota

    @MaxQuota.setter
    def MaxQuota(self, MaxQuota):
        self._MaxQuota = MaxQuota


    def _deserialize(self, params):
        self._EnvironmentName = params.get("EnvironmentName")
        self._Quota = params.get("Quota")
        self._MaxQuota = params.get("MaxQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorCodes(AbstractModel):
    """Custom error code

    """

    def __init__(self):
        r"""
        :param _Code: Custom response configuration error code.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Code: int
        :param _Msg: Custom response configuration error message.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _Desc: Custom response configuration error code remarks.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Desc: str
        :param _ConvertedCode: Custom error code conversion.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ConvertedCode: int
        :param _NeedConvert: Whether to enable error code conversion.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NeedConvert: bool
        """
        self._Code = None
        self._Msg = None
        self._Desc = None
        self._ConvertedCode = None
        self._NeedConvert = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ConvertedCode(self):
        return self._ConvertedCode

    @ConvertedCode.setter
    def ConvertedCode(self, ConvertedCode):
        self._ConvertedCode = ConvertedCode

    @property
    def NeedConvert(self):
        return self._NeedConvert

    @NeedConvert.setter
    def NeedConvert(self, NeedConvert):
        self._NeedConvert = NeedConvert


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._Desc = params.get("Desc")
        self._ConvertedCode = params.get("ConvertedCode")
        self._NeedConvert = params.get("NeedConvert")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
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
        :param _Name: Field to be filtered.
        :type Name: str
        :param _Values: Filter value of field.
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateApiDocumentRequest(AbstractModel):
    """GenerateApiDocument request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID of the document to be created.
        :type ServiceId: str
        :param _GenEnvironment: Environment of the service for which to create an SDK.
        :type GenEnvironment: str
        :param _GenLanguage: Programming language of the SDK to be created. Currently, only Python and JavaScript are supported.
        :type GenLanguage: str
        """
        self._ServiceId = None
        self._GenEnvironment = None
        self._GenLanguage = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def GenEnvironment(self):
        return self._GenEnvironment

    @GenEnvironment.setter
    def GenEnvironment(self, GenEnvironment):
        self._GenEnvironment = GenEnvironment

    @property
    def GenLanguage(self):
        return self._GenLanguage

    @GenLanguage.setter
    def GenLanguage(self, GenLanguage):
        self._GenLanguage = GenLanguage


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._GenEnvironment = params.get("GenEnvironment")
        self._GenLanguage = params.get("GenLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateApiDocumentResponse(AbstractModel):
    """GenerateApiDocument response structure.

    """

    def __init__(self):
        r"""
        :param _Result: API document and SDK link.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DocumentSDK`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DocumentSDK()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class HealthCheckConf(AbstractModel):
    """Health check configuration, including `TsfHealthCheckConf` and `TargetServicesHealthCheckConf`

    """

    def __init__(self):
        r"""
        :param _IsHealthCheck: Whether health check is enabled.
        :type IsHealthCheck: bool
        :param _RequestVolumeThreshold: Health check threshold.
        :type RequestVolumeThreshold: int
        :param _SleepWindowInMilliseconds: Window size.
        :type SleepWindowInMilliseconds: int
        :param _ErrorThresholdPercentage: Threshold percentage.
        :type ErrorThresholdPercentage: int
        """
        self._IsHealthCheck = None
        self._RequestVolumeThreshold = None
        self._SleepWindowInMilliseconds = None
        self._ErrorThresholdPercentage = None

    @property
    def IsHealthCheck(self):
        return self._IsHealthCheck

    @IsHealthCheck.setter
    def IsHealthCheck(self, IsHealthCheck):
        self._IsHealthCheck = IsHealthCheck

    @property
    def RequestVolumeThreshold(self):
        return self._RequestVolumeThreshold

    @RequestVolumeThreshold.setter
    def RequestVolumeThreshold(self, RequestVolumeThreshold):
        self._RequestVolumeThreshold = RequestVolumeThreshold

    @property
    def SleepWindowInMilliseconds(self):
        return self._SleepWindowInMilliseconds

    @SleepWindowInMilliseconds.setter
    def SleepWindowInMilliseconds(self, SleepWindowInMilliseconds):
        self._SleepWindowInMilliseconds = SleepWindowInMilliseconds

    @property
    def ErrorThresholdPercentage(self):
        return self._ErrorThresholdPercentage

    @ErrorThresholdPercentage.setter
    def ErrorThresholdPercentage(self, ErrorThresholdPercentage):
        self._ErrorThresholdPercentage = ErrorThresholdPercentage


    def _deserialize(self, params):
        self._IsHealthCheck = params.get("IsHealthCheck")
        self._RequestVolumeThreshold = params.get("RequestVolumeThreshold")
        self._SleepWindowInMilliseconds = params.get("SleepWindowInMilliseconds")
        self._ErrorThresholdPercentage = params.get("ErrorThresholdPercentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPStrategy(AbstractModel):
    """IP policy

    """

    def __init__(self):
        r"""
        :param _StrategyId: Unique policy ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StrategyId: str
        :param _StrategyName: Custom policy name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StrategyName: str
        :param _StrategyType: Policy type. Valid values: WHITE (allowlist), BLACK (blocklist).
Note: this field may return null, indicating that no valid values can be obtained.
        :type StrategyType: str
        :param _StrategyData: IP list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StrategyData: str
        :param _CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _ModifiedTime: Modification time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param _ServiceId: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceId: str
        :param _BindApiTotalCount: Number of APIs bound to policy.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BindApiTotalCount: int
        :param _BindApis: Bound API details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BindApis: list of DesApisStatus
        """
        self._StrategyId = None
        self._StrategyName = None
        self._StrategyType = None
        self._StrategyData = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ServiceId = None
        self._BindApiTotalCount = None
        self._BindApis = None

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def StrategyName(self):
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def StrategyType(self):
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def StrategyData(self):
        return self._StrategyData

    @StrategyData.setter
    def StrategyData(self, StrategyData):
        self._StrategyData = StrategyData

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def BindApiTotalCount(self):
        return self._BindApiTotalCount

    @BindApiTotalCount.setter
    def BindApiTotalCount(self, BindApiTotalCount):
        self._BindApiTotalCount = BindApiTotalCount

    @property
    def BindApis(self):
        return self._BindApis

    @BindApis.setter
    def BindApis(self, BindApis):
        self._BindApis = BindApis


    def _deserialize(self, params):
        self._StrategyId = params.get("StrategyId")
        self._StrategyName = params.get("StrategyName")
        self._StrategyType = params.get("StrategyType")
        self._StrategyData = params.get("StrategyData")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ServiceId = params.get("ServiceId")
        self._BindApiTotalCount = params.get("BindApiTotalCount")
        if params.get("BindApis") is not None:
            self._BindApis = []
            for item in params.get("BindApis"):
                obj = DesApisStatus()
                obj._deserialize(item)
                self._BindApis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPStrategyApi(AbstractModel):
    """List of APIs bound to policy

    """

    def __init__(self):
        r"""
        :param _ApiId: Unique API ID.
        :type ApiId: str
        :param _ApiName: Custom API name.
        :type ApiName: str
        :param _ApiType: API type. Valid values: NORMAL (general API), TSF (microservice API).
        :type ApiType: str
        :param _Path: API path, such as `/path`.
        :type Path: str
        :param _Method: API request method, such as `GET`.
        :type Method: str
        :param _OtherIPStrategyId: Unique ID of another policy bound to API.
        :type OtherIPStrategyId: str
        :param _OtherEnvironmentName: Environment bound to API.
        :type OtherEnvironmentName: str
        """
        self._ApiId = None
        self._ApiName = None
        self._ApiType = None
        self._Path = None
        self._Method = None
        self._OtherIPStrategyId = None
        self._OtherEnvironmentName = None

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def ApiType(self):
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def OtherIPStrategyId(self):
        return self._OtherIPStrategyId

    @OtherIPStrategyId.setter
    def OtherIPStrategyId(self, OtherIPStrategyId):
        self._OtherIPStrategyId = OtherIPStrategyId

    @property
    def OtherEnvironmentName(self):
        return self._OtherEnvironmentName

    @OtherEnvironmentName.setter
    def OtherEnvironmentName(self, OtherEnvironmentName):
        self._OtherEnvironmentName = OtherEnvironmentName


    def _deserialize(self, params):
        self._ApiId = params.get("ApiId")
        self._ApiName = params.get("ApiName")
        self._ApiType = params.get("ApiType")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        self._OtherIPStrategyId = params.get("OtherIPStrategyId")
        self._OtherEnvironmentName = params.get("OtherEnvironmentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPStrategyApiStatus(AbstractModel):
    """Details of API bound to IP policy

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of APIs bound to environment.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _ApiIdStatusSet: Details of APIs bound to environment.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiIdStatusSet: list of IPStrategyApi
        """
        self._TotalCount = None
        self._ApiIdStatusSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiIdStatusSet(self):
        return self._ApiIdStatusSet

    @ApiIdStatusSet.setter
    def ApiIdStatusSet(self, ApiIdStatusSet):
        self._ApiIdStatusSet = ApiIdStatusSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiIdStatusSet") is not None:
            self._ApiIdStatusSet = []
            for item in params.get("ApiIdStatusSet"):
                obj = IPStrategyApi()
                obj._deserialize(item)
                self._ApiIdStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPStrategysStatus(AbstractModel):
    """Policy list

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of policies.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _StrategySet: Policy list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StrategySet: list of IPStrategy
        """
        self._TotalCount = None
        self._StrategySet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def StrategySet(self):
        return self._StrategySet

    @StrategySet.setter
    def StrategySet(self, StrategySet):
        self._StrategySet = StrategySet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("StrategySet") is not None:
            self._StrategySet = []
            for item in params.get("StrategySet"):
                obj = IPStrategy()
                obj._deserialize(item)
                self._StrategySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportOpenApiRequest(AbstractModel):
    """ImportOpenApi request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: The unique ID of the service associated with the API
        :type ServiceId: str
        :param _Content: Content of the openAPI
        :type Content: str
        :param _EncodeType: Format of the content. Values: `YAML` (default), `JSON`
        :type EncodeType: str
        :param _ContentVersion: Version of the content. It can only be `openAPI` for now.
        :type ContentVersion: str
        """
        self._ServiceId = None
        self._Content = None
        self._EncodeType = None
        self._ContentVersion = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def EncodeType(self):
        return self._EncodeType

    @EncodeType.setter
    def EncodeType(self, EncodeType):
        self._EncodeType = EncodeType

    @property
    def ContentVersion(self):
        return self._ContentVersion

    @ContentVersion.setter
    def ContentVersion(self, ContentVersion):
        self._ContentVersion = ContentVersion


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Content = params.get("Content")
        self._EncodeType = params.get("EncodeType")
        self._ContentVersion = params.get("ContentVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportOpenApiResponse(AbstractModel):
    """ImportOpenApi response structure.

    """

    def __init__(self):
        r"""
        :param _Result: The result of importing the OpenAPI
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.CreateApiRspSet`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CreateApiRspSet()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class K8sLabel(AbstractModel):
    """K8s Label

    """

    def __init__(self):
        r"""
        :param _Key: Key of the label
        :type Key: str
        :param _Value: Value of the label
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class K8sService(AbstractModel):
    """Configuration of K8s service

    """

    def __init__(self):
        r"""
        :param _Weight: Weight
        :type Weight: int
        :param _ClusterId: K8s cluster ID
        :type ClusterId: str
        :param _Namespace: Namespace of the container
        :type Namespace: str
        :param _ServiceName: Name of the service
        :type ServiceName: str
        :param _Port: Service port
        :type Port: int
        :param _ExtraLabels: The additional Label of the Pod
        :type ExtraLabels: list of K8sLabel
        :param _Name: (Optional) Custom name of the service
        :type Name: str
        """
        self._Weight = None
        self._ClusterId = None
        self._Namespace = None
        self._ServiceName = None
        self._Port = None
        self._ExtraLabels = None
        self._Name = None

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ExtraLabels(self):
        return self._ExtraLabels

    @ExtraLabels.setter
    def ExtraLabels(self, ExtraLabels):
        self._ExtraLabels = ExtraLabels

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Weight = params.get("Weight")
        self._ClusterId = params.get("ClusterId")
        self._Namespace = params.get("Namespace")
        self._ServiceName = params.get("ServiceName")
        self._Port = params.get("Port")
        if params.get("ExtraLabels") is not None:
            self._ExtraLabels = []
            for item in params.get("ExtraLabels"):
                obj = K8sLabel()
                obj._deserialize(item)
                self._ExtraLabels.append(obj)
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogQuery(AbstractModel):
    """Search criterion input parameter

    """

    def __init__(self):
        r"""
        :param _Name: Search field
        :type Name: str
        :param _Operator: Operator
        :type Operator: str
        :param _Value: Search value
        :type Value: str
        """
        self._Name = None
        self._Operator = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MicroService(AbstractModel):
    """Information of microservice bound to API.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Microservice cluster ID.
        :type ClusterId: str
        :param _NamespaceId: Microservice namespace ID.
        :type NamespaceId: str
        :param _MicroServiceName: Microservice name.
        :type MicroServiceName: str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._MicroServiceName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def MicroServiceName(self):
        return self._MicroServiceName

    @MicroServiceName.setter
    def MicroServiceName(self, MicroServiceName):
        self._MicroServiceName = MicroServiceName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._MicroServiceName = params.get("MicroServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MicroServiceReq(AbstractModel):
    """TSF type input parameters

    """

    def __init__(self):
        r"""
        :param _ClusterId: Microservice cluster.
        :type ClusterId: str
        :param _NamespaceId: Microservice namespace.
        :type NamespaceId: str
        :param _MicroServiceName: Microservice name.
        :type MicroServiceName: str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._MicroServiceName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def MicroServiceName(self):
        return self._MicroServiceName

    @MicroServiceName.setter
    def MicroServiceName(self, MicroServiceName):
        self._MicroServiceName = MicroServiceName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._MicroServiceName = params.get("MicroServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAPIDocRequest(AbstractModel):
    """ModifyAPIDoc request structure.

    """

    def __init__(self):
        r"""
        :param _ApiDocId: API document ID
        :type ApiDocId: str
        :param _ApiDocName: API document name
        :type ApiDocName: str
        :param _ServiceId: Service name
        :type ServiceId: str
        :param _Environment: Environment name
        :type Environment: str
        :param _ApiIds: List of APIs for which to generate documents
        :type ApiIds: list of str
        """
        self._ApiDocId = None
        self._ApiDocName = None
        self._ServiceId = None
        self._Environment = None
        self._ApiIds = None

    @property
    def ApiDocId(self):
        return self._ApiDocId

    @ApiDocId.setter
    def ApiDocId(self, ApiDocId):
        self._ApiDocId = ApiDocId

    @property
    def ApiDocName(self):
        return self._ApiDocName

    @ApiDocName.setter
    def ApiDocName(self, ApiDocName):
        self._ApiDocName = ApiDocName

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds


    def _deserialize(self, params):
        self._ApiDocId = params.get("ApiDocId")
        self._ApiDocName = params.get("ApiDocName")
        self._ServiceId = params.get("ServiceId")
        self._Environment = params.get("Environment")
        self._ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAPIDocResponse(AbstractModel):
    """ModifyAPIDoc response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Basic information of API document
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = APIDoc()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyApiAppRequest(AbstractModel):
    """ModifyApiApp request structure.

    """

    def __init__(self):
        r"""
        :param _ApiAppId: Unique application ID.
        :type ApiAppId: str
        :param _ApiAppName: Modified application name
        :type ApiAppName: str
        :param _ApiAppDesc: Modified application description
        :type ApiAppDesc: str
        """
        self._ApiAppId = None
        self._ApiAppName = None
        self._ApiAppDesc = None

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId

    @property
    def ApiAppName(self):
        return self._ApiAppName

    @ApiAppName.setter
    def ApiAppName(self, ApiAppName):
        self._ApiAppName = ApiAppName

    @property
    def ApiAppDesc(self):
        return self._ApiAppDesc

    @ApiAppDesc.setter
    def ApiAppDesc(self, ApiAppDesc):
        self._ApiAppDesc = ApiAppDesc


    def _deserialize(self, params):
        self._ApiAppId = params.get("ApiAppId")
        self._ApiAppName = params.get("ApiAppName")
        self._ApiAppDesc = params.get("ApiAppDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiAppResponse(AbstractModel):
    """ModifyApiApp response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether modification succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyApiEnvironmentStrategyRequest(AbstractModel):
    """ModifyApiEnvironmentStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _Strategy: Throttling value.
        :type Strategy: int
        :param _EnvironmentName: Environment name.
        :type EnvironmentName: str
        :param _ApiIds: API list.
        :type ApiIds: list of str
        """
        self._ServiceId = None
        self._Strategy = None
        self._EnvironmentName = None
        self._ApiIds = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Strategy(self):
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Strategy = params.get("Strategy")
        self._EnvironmentName = params.get("EnvironmentName")
        self._ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiEnvironmentStrategyResponse(AbstractModel):
    """ModifyApiEnvironmentStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether modification succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyApiIncrementRequest(AbstractModel):
    """ModifyApiIncrement request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Service ID
        :type ServiceId: str
        :param _ApiId: API ID
        :type ApiId: str
        :param _BusinessType: Authorization type of the API to be modified (you can select `OAUTH`, i.e., authorization API)
        :type BusinessType: str
        :param _PublicKey: Public key value to be modified by OAuth API
        :type PublicKey: str
        :param _LoginRedirectUrl: OAuth API redirect address
        :type LoginRedirectUrl: str
        """
        self._ServiceId = None
        self._ApiId = None
        self._BusinessType = None
        self._PublicKey = None
        self._LoginRedirectUrl = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def BusinessType(self):
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def LoginRedirectUrl(self):
        return self._LoginRedirectUrl

    @LoginRedirectUrl.setter
    def LoginRedirectUrl(self, LoginRedirectUrl):
        self._LoginRedirectUrl = LoginRedirectUrl


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        self._BusinessType = params.get("BusinessType")
        self._PublicKey = params.get("PublicKey")
        self._LoginRedirectUrl = params.get("LoginRedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiIncrementResponse(AbstractModel):
    """ModifyApiIncrement response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyApiRequest(AbstractModel):
    """ModifyApi request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID of API.
        :type ServiceId: str
        :param _ServiceType: API backend service type. Valid values: HTTP, MOCK, TSF, CLB, SCF, WEBSOCKET, TARGET (in beta test).
        :type ServiceType: str
        :param _RequestConfig: Request frontend configuration.
        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.RequestConfig`
        :param _ApiId: Unique API ID.
        :type ApiId: str
        :param _ApiName: Custom API name.
        :type ApiName: str
        :param _ApiDesc: Custom API description.
        :type ApiDesc: str
        :param _ApiType: API type. Valid values: NORMAL, TSF. Default value: NORMAL.
        :type ApiType: str
        :param _AuthType: API authentication type. Valid values: SECRET, NONE, OAUTH, APP. Default value: NONE.
        :type AuthType: str
        :param _AuthRequired: Whether signature authentication is required. True: yes; False: no. This parameter is to be disused.
        :type AuthRequired: bool
        :param _ServiceTimeout: API backend service timeout period in seconds.
        :type ServiceTimeout: int
        :param _Protocol: API frontend request type, such as HTTP, HTTPS, or HTTP and HTTPS.
        :type Protocol: str
        :param _EnableCORS: Whether to enable CORS. True: yes; False: no.
        :type EnableCORS: bool
        :param _ConstantParameters: Constant parameter.
        :type ConstantParameters: list of ConstantParameter
        :param _RequestParameters: Frontend request parameter.
        :type RequestParameters: list of ReqParameter
        :param _ApiBusinessType: This field is valid if `AuthType` is `OAUTH`. NORMAL: business API; OAUTH: authorization API.
        :type ApiBusinessType: str
        :param _ServiceMockReturnMessage: Returned message of API backend Mock, which is required if `ServiceType` is `Mock`.
        :type ServiceMockReturnMessage: str
        :param _MicroServices: List of microservices bound to API.
        :type MicroServices: list of MicroServiceReq
        :param _ServiceTsfLoadBalanceConf: Load balancing configuration of microservice.
        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`
        :param _ServiceTsfHealthCheckConf: Health check configuration of microservice.
        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param _TargetServicesLoadBalanceConf: `target` type load balancing configuration (in beta test).
        :type TargetServicesLoadBalanceConf: int
        :param _TargetServicesHealthCheckConf: `target` health check configuration (in beta test).
        :type TargetServicesHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param _ServiceScfFunctionName: SCF function name, which takes effect if the backend type is `SCF`.
        :type ServiceScfFunctionName: str
        :param _ServiceWebsocketRegisterFunctionName: SCF WebSocket registration function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionName: str
        :param _ServiceWebsocketCleanupFunctionName: SCF WebSocket cleanup function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionName: str
        :param _ServiceWebsocketTransportFunctionName: SCF WebSocket transfer function, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionName: str
        :param _ServiceScfFunctionNamespace: SCF function namespace, which takes effect if the backend type is `SCF`.
        :type ServiceScfFunctionNamespace: str
        :param _ServiceScfFunctionQualifier: SCF function version, which takes effect if the backend type is `SCF`.
        :type ServiceScfFunctionQualifier: str
        :param _ServiceWebsocketRegisterFunctionNamespace: SCF WebSocket registration function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionNamespace: str
        :param _ServiceWebsocketRegisterFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketRegisterFunctionQualifier: str
        :param _ServiceWebsocketTransportFunctionNamespace: SCF WebSocket transfer function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionNamespace: str
        :param _ServiceWebsocketTransportFunctionQualifier: SCF WebSocket transfer function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketTransportFunctionQualifier: str
        :param _ServiceWebsocketCleanupFunctionNamespace: SCF WebSocket cleanup function namespace, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionNamespace: str
        :param _ServiceWebsocketCleanupFunctionQualifier: SCF WebSocket cleanup function version, which takes effect if the frontend type is `WEBSOCKET` and the backend type is `SCF`.
        :type ServiceWebsocketCleanupFunctionQualifier: str
        :param _ServiceScfIsIntegratedResponse: Whether to enable response integration, which takes effect if the backend type is `SCF`.
        :type ServiceScfIsIntegratedResponse: bool
        :param _IsDebugAfterCharge: Billing after debugging starts (reserved field for marketplace).
        :type IsDebugAfterCharge: bool
        :param _TagSpecifications: Tag.
        :type TagSpecifications: :class:`tencentcloud.apigateway.v20180808.models.Tag`
        :param _IsDeleteResponseErrorCodes: Whether to delete the error codes for custom response configuration. If the value is left empty or `False`, the error codes will not be deleted. If the value is `True`, all custom response configuration error codes of the API will be deleted.
        :type IsDeleteResponseErrorCodes: bool
        :param _ResponseType: Return type.
        :type ResponseType: str
        :param _ResponseSuccessExample: Sample response for successful custom response configuration.
        :type ResponseSuccessExample: str
        :param _ResponseFailExample: Sample response for failed custom response configuration.
        :type ResponseFailExample: str
        :param _ServiceConfig: API backend service configuration.
        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`
        :param _AuthRelationApiId: Unique ID of associated authorization API, which takes effect only if `AuthType` is `OAUTH` and `ApiBusinessType` is `NORMAL`. It is the unique ID of the OAuth 2.0 authorization API bound to the business API.
        :type AuthRelationApiId: str
        :param _ServiceParameters: API backend service parameter.
        :type ServiceParameters: list of ServiceParameter
        :param _OauthConfig: OAuth configuration, which takes effect if `AuthType` is `OAUTH`.
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param _ResponseErrorCodes: Custom error code configuration.
        :type ResponseErrorCodes: list of ResponseErrorCodeReq
        :param _IsBase64Encoded: Whether to enable Base64 encoding. This parameter takes effect only when the backend is SCF.
        :type IsBase64Encoded: bool
        :param _IsBase64Trigger: Whether to trigger Base64 encoding by header. This parameter takes effect only when the backend is SCF.
        :type IsBase64Trigger: bool
        :param _Base64EncodedTriggerRules: Header trigger rules. The number of rules cannot exceed 10.
        :type Base64EncodedTriggerRules: list of Base64EncodedTriggerRule
        :param _EventBusId: Event bus ID.
        :type EventBusId: str
        :param _ServiceScfFunctionType: SCF function type, which takes effect when the backend type is `SCF`. Valid values: `EVENT` and `HTTP`.
        :type ServiceScfFunctionType: str
        :param _EIAMAppType: EIAM application type.
        :type EIAMAppType: str
        :param _EIAMAuthType: EIAM application authentication type. Valid values: `AuthenticationOnly`, `Authentication`, `Authorization`.
        :type EIAMAuthType: str
        :param _EIAMAppId: Validity of the EIAM application token. Unit: second. Default value: `7200`.
        :type EIAMAppId: str
        :param _TokenTimeout: EIAM application ID.
        :type TokenTimeout: int
        """
        self._ServiceId = None
        self._ServiceType = None
        self._RequestConfig = None
        self._ApiId = None
        self._ApiName = None
        self._ApiDesc = None
        self._ApiType = None
        self._AuthType = None
        self._AuthRequired = None
        self._ServiceTimeout = None
        self._Protocol = None
        self._EnableCORS = None
        self._ConstantParameters = None
        self._RequestParameters = None
        self._ApiBusinessType = None
        self._ServiceMockReturnMessage = None
        self._MicroServices = None
        self._ServiceTsfLoadBalanceConf = None
        self._ServiceTsfHealthCheckConf = None
        self._TargetServicesLoadBalanceConf = None
        self._TargetServicesHealthCheckConf = None
        self._ServiceScfFunctionName = None
        self._ServiceWebsocketRegisterFunctionName = None
        self._ServiceWebsocketCleanupFunctionName = None
        self._ServiceWebsocketTransportFunctionName = None
        self._ServiceScfFunctionNamespace = None
        self._ServiceScfFunctionQualifier = None
        self._ServiceWebsocketRegisterFunctionNamespace = None
        self._ServiceWebsocketRegisterFunctionQualifier = None
        self._ServiceWebsocketTransportFunctionNamespace = None
        self._ServiceWebsocketTransportFunctionQualifier = None
        self._ServiceWebsocketCleanupFunctionNamespace = None
        self._ServiceWebsocketCleanupFunctionQualifier = None
        self._ServiceScfIsIntegratedResponse = None
        self._IsDebugAfterCharge = None
        self._TagSpecifications = None
        self._IsDeleteResponseErrorCodes = None
        self._ResponseType = None
        self._ResponseSuccessExample = None
        self._ResponseFailExample = None
        self._ServiceConfig = None
        self._AuthRelationApiId = None
        self._ServiceParameters = None
        self._OauthConfig = None
        self._ResponseErrorCodes = None
        self._IsBase64Encoded = None
        self._IsBase64Trigger = None
        self._Base64EncodedTriggerRules = None
        self._EventBusId = None
        self._ServiceScfFunctionType = None
        self._EIAMAppType = None
        self._EIAMAuthType = None
        self._EIAMAppId = None
        self._TokenTimeout = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def RequestConfig(self):
        return self._RequestConfig

    @RequestConfig.setter
    def RequestConfig(self, RequestConfig):
        self._RequestConfig = RequestConfig

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def ApiDesc(self):
        return self._ApiDesc

    @ApiDesc.setter
    def ApiDesc(self, ApiDesc):
        self._ApiDesc = ApiDesc

    @property
    def ApiType(self):
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def AuthType(self):
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def AuthRequired(self):
        return self._AuthRequired

    @AuthRequired.setter
    def AuthRequired(self, AuthRequired):
        self._AuthRequired = AuthRequired

    @property
    def ServiceTimeout(self):
        return self._ServiceTimeout

    @ServiceTimeout.setter
    def ServiceTimeout(self, ServiceTimeout):
        self._ServiceTimeout = ServiceTimeout

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def EnableCORS(self):
        return self._EnableCORS

    @EnableCORS.setter
    def EnableCORS(self, EnableCORS):
        self._EnableCORS = EnableCORS

    @property
    def ConstantParameters(self):
        return self._ConstantParameters

    @ConstantParameters.setter
    def ConstantParameters(self, ConstantParameters):
        self._ConstantParameters = ConstantParameters

    @property
    def RequestParameters(self):
        return self._RequestParameters

    @RequestParameters.setter
    def RequestParameters(self, RequestParameters):
        self._RequestParameters = RequestParameters

    @property
    def ApiBusinessType(self):
        return self._ApiBusinessType

    @ApiBusinessType.setter
    def ApiBusinessType(self, ApiBusinessType):
        self._ApiBusinessType = ApiBusinessType

    @property
    def ServiceMockReturnMessage(self):
        return self._ServiceMockReturnMessage

    @ServiceMockReturnMessage.setter
    def ServiceMockReturnMessage(self, ServiceMockReturnMessage):
        self._ServiceMockReturnMessage = ServiceMockReturnMessage

    @property
    def MicroServices(self):
        return self._MicroServices

    @MicroServices.setter
    def MicroServices(self, MicroServices):
        self._MicroServices = MicroServices

    @property
    def ServiceTsfLoadBalanceConf(self):
        return self._ServiceTsfLoadBalanceConf

    @ServiceTsfLoadBalanceConf.setter
    def ServiceTsfLoadBalanceConf(self, ServiceTsfLoadBalanceConf):
        self._ServiceTsfLoadBalanceConf = ServiceTsfLoadBalanceConf

    @property
    def ServiceTsfHealthCheckConf(self):
        return self._ServiceTsfHealthCheckConf

    @ServiceTsfHealthCheckConf.setter
    def ServiceTsfHealthCheckConf(self, ServiceTsfHealthCheckConf):
        self._ServiceTsfHealthCheckConf = ServiceTsfHealthCheckConf

    @property
    def TargetServicesLoadBalanceConf(self):
        return self._TargetServicesLoadBalanceConf

    @TargetServicesLoadBalanceConf.setter
    def TargetServicesLoadBalanceConf(self, TargetServicesLoadBalanceConf):
        self._TargetServicesLoadBalanceConf = TargetServicesLoadBalanceConf

    @property
    def TargetServicesHealthCheckConf(self):
        return self._TargetServicesHealthCheckConf

    @TargetServicesHealthCheckConf.setter
    def TargetServicesHealthCheckConf(self, TargetServicesHealthCheckConf):
        self._TargetServicesHealthCheckConf = TargetServicesHealthCheckConf

    @property
    def ServiceScfFunctionName(self):
        return self._ServiceScfFunctionName

    @ServiceScfFunctionName.setter
    def ServiceScfFunctionName(self, ServiceScfFunctionName):
        self._ServiceScfFunctionName = ServiceScfFunctionName

    @property
    def ServiceWebsocketRegisterFunctionName(self):
        return self._ServiceWebsocketRegisterFunctionName

    @ServiceWebsocketRegisterFunctionName.setter
    def ServiceWebsocketRegisterFunctionName(self, ServiceWebsocketRegisterFunctionName):
        self._ServiceWebsocketRegisterFunctionName = ServiceWebsocketRegisterFunctionName

    @property
    def ServiceWebsocketCleanupFunctionName(self):
        return self._ServiceWebsocketCleanupFunctionName

    @ServiceWebsocketCleanupFunctionName.setter
    def ServiceWebsocketCleanupFunctionName(self, ServiceWebsocketCleanupFunctionName):
        self._ServiceWebsocketCleanupFunctionName = ServiceWebsocketCleanupFunctionName

    @property
    def ServiceWebsocketTransportFunctionName(self):
        return self._ServiceWebsocketTransportFunctionName

    @ServiceWebsocketTransportFunctionName.setter
    def ServiceWebsocketTransportFunctionName(self, ServiceWebsocketTransportFunctionName):
        self._ServiceWebsocketTransportFunctionName = ServiceWebsocketTransportFunctionName

    @property
    def ServiceScfFunctionNamespace(self):
        return self._ServiceScfFunctionNamespace

    @ServiceScfFunctionNamespace.setter
    def ServiceScfFunctionNamespace(self, ServiceScfFunctionNamespace):
        self._ServiceScfFunctionNamespace = ServiceScfFunctionNamespace

    @property
    def ServiceScfFunctionQualifier(self):
        return self._ServiceScfFunctionQualifier

    @ServiceScfFunctionQualifier.setter
    def ServiceScfFunctionQualifier(self, ServiceScfFunctionQualifier):
        self._ServiceScfFunctionQualifier = ServiceScfFunctionQualifier

    @property
    def ServiceWebsocketRegisterFunctionNamespace(self):
        return self._ServiceWebsocketRegisterFunctionNamespace

    @ServiceWebsocketRegisterFunctionNamespace.setter
    def ServiceWebsocketRegisterFunctionNamespace(self, ServiceWebsocketRegisterFunctionNamespace):
        self._ServiceWebsocketRegisterFunctionNamespace = ServiceWebsocketRegisterFunctionNamespace

    @property
    def ServiceWebsocketRegisterFunctionQualifier(self):
        return self._ServiceWebsocketRegisterFunctionQualifier

    @ServiceWebsocketRegisterFunctionQualifier.setter
    def ServiceWebsocketRegisterFunctionQualifier(self, ServiceWebsocketRegisterFunctionQualifier):
        self._ServiceWebsocketRegisterFunctionQualifier = ServiceWebsocketRegisterFunctionQualifier

    @property
    def ServiceWebsocketTransportFunctionNamespace(self):
        return self._ServiceWebsocketTransportFunctionNamespace

    @ServiceWebsocketTransportFunctionNamespace.setter
    def ServiceWebsocketTransportFunctionNamespace(self, ServiceWebsocketTransportFunctionNamespace):
        self._ServiceWebsocketTransportFunctionNamespace = ServiceWebsocketTransportFunctionNamespace

    @property
    def ServiceWebsocketTransportFunctionQualifier(self):
        return self._ServiceWebsocketTransportFunctionQualifier

    @ServiceWebsocketTransportFunctionQualifier.setter
    def ServiceWebsocketTransportFunctionQualifier(self, ServiceWebsocketTransportFunctionQualifier):
        self._ServiceWebsocketTransportFunctionQualifier = ServiceWebsocketTransportFunctionQualifier

    @property
    def ServiceWebsocketCleanupFunctionNamespace(self):
        return self._ServiceWebsocketCleanupFunctionNamespace

    @ServiceWebsocketCleanupFunctionNamespace.setter
    def ServiceWebsocketCleanupFunctionNamespace(self, ServiceWebsocketCleanupFunctionNamespace):
        self._ServiceWebsocketCleanupFunctionNamespace = ServiceWebsocketCleanupFunctionNamespace

    @property
    def ServiceWebsocketCleanupFunctionQualifier(self):
        return self._ServiceWebsocketCleanupFunctionQualifier

    @ServiceWebsocketCleanupFunctionQualifier.setter
    def ServiceWebsocketCleanupFunctionQualifier(self, ServiceWebsocketCleanupFunctionQualifier):
        self._ServiceWebsocketCleanupFunctionQualifier = ServiceWebsocketCleanupFunctionQualifier

    @property
    def ServiceScfIsIntegratedResponse(self):
        return self._ServiceScfIsIntegratedResponse

    @ServiceScfIsIntegratedResponse.setter
    def ServiceScfIsIntegratedResponse(self, ServiceScfIsIntegratedResponse):
        self._ServiceScfIsIntegratedResponse = ServiceScfIsIntegratedResponse

    @property
    def IsDebugAfterCharge(self):
        return self._IsDebugAfterCharge

    @IsDebugAfterCharge.setter
    def IsDebugAfterCharge(self, IsDebugAfterCharge):
        self._IsDebugAfterCharge = IsDebugAfterCharge

    @property
    def TagSpecifications(self):
        return self._TagSpecifications

    @TagSpecifications.setter
    def TagSpecifications(self, TagSpecifications):
        self._TagSpecifications = TagSpecifications

    @property
    def IsDeleteResponseErrorCodes(self):
        return self._IsDeleteResponseErrorCodes

    @IsDeleteResponseErrorCodes.setter
    def IsDeleteResponseErrorCodes(self, IsDeleteResponseErrorCodes):
        self._IsDeleteResponseErrorCodes = IsDeleteResponseErrorCodes

    @property
    def ResponseType(self):
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseSuccessExample(self):
        return self._ResponseSuccessExample

    @ResponseSuccessExample.setter
    def ResponseSuccessExample(self, ResponseSuccessExample):
        self._ResponseSuccessExample = ResponseSuccessExample

    @property
    def ResponseFailExample(self):
        return self._ResponseFailExample

    @ResponseFailExample.setter
    def ResponseFailExample(self, ResponseFailExample):
        self._ResponseFailExample = ResponseFailExample

    @property
    def ServiceConfig(self):
        return self._ServiceConfig

    @ServiceConfig.setter
    def ServiceConfig(self, ServiceConfig):
        self._ServiceConfig = ServiceConfig

    @property
    def AuthRelationApiId(self):
        return self._AuthRelationApiId

    @AuthRelationApiId.setter
    def AuthRelationApiId(self, AuthRelationApiId):
        self._AuthRelationApiId = AuthRelationApiId

    @property
    def ServiceParameters(self):
        return self._ServiceParameters

    @ServiceParameters.setter
    def ServiceParameters(self, ServiceParameters):
        self._ServiceParameters = ServiceParameters

    @property
    def OauthConfig(self):
        return self._OauthConfig

    @OauthConfig.setter
    def OauthConfig(self, OauthConfig):
        self._OauthConfig = OauthConfig

    @property
    def ResponseErrorCodes(self):
        return self._ResponseErrorCodes

    @ResponseErrorCodes.setter
    def ResponseErrorCodes(self, ResponseErrorCodes):
        self._ResponseErrorCodes = ResponseErrorCodes

    @property
    def IsBase64Encoded(self):
        return self._IsBase64Encoded

    @IsBase64Encoded.setter
    def IsBase64Encoded(self, IsBase64Encoded):
        self._IsBase64Encoded = IsBase64Encoded

    @property
    def IsBase64Trigger(self):
        return self._IsBase64Trigger

    @IsBase64Trigger.setter
    def IsBase64Trigger(self, IsBase64Trigger):
        self._IsBase64Trigger = IsBase64Trigger

    @property
    def Base64EncodedTriggerRules(self):
        return self._Base64EncodedTriggerRules

    @Base64EncodedTriggerRules.setter
    def Base64EncodedTriggerRules(self, Base64EncodedTriggerRules):
        self._Base64EncodedTriggerRules = Base64EncodedTriggerRules

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def ServiceScfFunctionType(self):
        return self._ServiceScfFunctionType

    @ServiceScfFunctionType.setter
    def ServiceScfFunctionType(self, ServiceScfFunctionType):
        self._ServiceScfFunctionType = ServiceScfFunctionType

    @property
    def EIAMAppType(self):
        return self._EIAMAppType

    @EIAMAppType.setter
    def EIAMAppType(self, EIAMAppType):
        self._EIAMAppType = EIAMAppType

    @property
    def EIAMAuthType(self):
        return self._EIAMAuthType

    @EIAMAuthType.setter
    def EIAMAuthType(self, EIAMAuthType):
        self._EIAMAuthType = EIAMAuthType

    @property
    def EIAMAppId(self):
        return self._EIAMAppId

    @EIAMAppId.setter
    def EIAMAppId(self, EIAMAppId):
        self._EIAMAppId = EIAMAppId

    @property
    def TokenTimeout(self):
        return self._TokenTimeout

    @TokenTimeout.setter
    def TokenTimeout(self, TokenTimeout):
        self._TokenTimeout = TokenTimeout


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceType = params.get("ServiceType")
        if params.get("RequestConfig") is not None:
            self._RequestConfig = RequestConfig()
            self._RequestConfig._deserialize(params.get("RequestConfig"))
        self._ApiId = params.get("ApiId")
        self._ApiName = params.get("ApiName")
        self._ApiDesc = params.get("ApiDesc")
        self._ApiType = params.get("ApiType")
        self._AuthType = params.get("AuthType")
        self._AuthRequired = params.get("AuthRequired")
        self._ServiceTimeout = params.get("ServiceTimeout")
        self._Protocol = params.get("Protocol")
        self._EnableCORS = params.get("EnableCORS")
        if params.get("ConstantParameters") is not None:
            self._ConstantParameters = []
            for item in params.get("ConstantParameters"):
                obj = ConstantParameter()
                obj._deserialize(item)
                self._ConstantParameters.append(obj)
        if params.get("RequestParameters") is not None:
            self._RequestParameters = []
            for item in params.get("RequestParameters"):
                obj = ReqParameter()
                obj._deserialize(item)
                self._RequestParameters.append(obj)
        self._ApiBusinessType = params.get("ApiBusinessType")
        self._ServiceMockReturnMessage = params.get("ServiceMockReturnMessage")
        if params.get("MicroServices") is not None:
            self._MicroServices = []
            for item in params.get("MicroServices"):
                obj = MicroServiceReq()
                obj._deserialize(item)
                self._MicroServices.append(obj)
        if params.get("ServiceTsfLoadBalanceConf") is not None:
            self._ServiceTsfLoadBalanceConf = TsfLoadBalanceConfResp()
            self._ServiceTsfLoadBalanceConf._deserialize(params.get("ServiceTsfLoadBalanceConf"))
        if params.get("ServiceTsfHealthCheckConf") is not None:
            self._ServiceTsfHealthCheckConf = HealthCheckConf()
            self._ServiceTsfHealthCheckConf._deserialize(params.get("ServiceTsfHealthCheckConf"))
        self._TargetServicesLoadBalanceConf = params.get("TargetServicesLoadBalanceConf")
        if params.get("TargetServicesHealthCheckConf") is not None:
            self._TargetServicesHealthCheckConf = HealthCheckConf()
            self._TargetServicesHealthCheckConf._deserialize(params.get("TargetServicesHealthCheckConf"))
        self._ServiceScfFunctionName = params.get("ServiceScfFunctionName")
        self._ServiceWebsocketRegisterFunctionName = params.get("ServiceWebsocketRegisterFunctionName")
        self._ServiceWebsocketCleanupFunctionName = params.get("ServiceWebsocketCleanupFunctionName")
        self._ServiceWebsocketTransportFunctionName = params.get("ServiceWebsocketTransportFunctionName")
        self._ServiceScfFunctionNamespace = params.get("ServiceScfFunctionNamespace")
        self._ServiceScfFunctionQualifier = params.get("ServiceScfFunctionQualifier")
        self._ServiceWebsocketRegisterFunctionNamespace = params.get("ServiceWebsocketRegisterFunctionNamespace")
        self._ServiceWebsocketRegisterFunctionQualifier = params.get("ServiceWebsocketRegisterFunctionQualifier")
        self._ServiceWebsocketTransportFunctionNamespace = params.get("ServiceWebsocketTransportFunctionNamespace")
        self._ServiceWebsocketTransportFunctionQualifier = params.get("ServiceWebsocketTransportFunctionQualifier")
        self._ServiceWebsocketCleanupFunctionNamespace = params.get("ServiceWebsocketCleanupFunctionNamespace")
        self._ServiceWebsocketCleanupFunctionQualifier = params.get("ServiceWebsocketCleanupFunctionQualifier")
        self._ServiceScfIsIntegratedResponse = params.get("ServiceScfIsIntegratedResponse")
        self._IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        if params.get("TagSpecifications") is not None:
            self._TagSpecifications = Tag()
            self._TagSpecifications._deserialize(params.get("TagSpecifications"))
        self._IsDeleteResponseErrorCodes = params.get("IsDeleteResponseErrorCodes")
        self._ResponseType = params.get("ResponseType")
        self._ResponseSuccessExample = params.get("ResponseSuccessExample")
        self._ResponseFailExample = params.get("ResponseFailExample")
        if params.get("ServiceConfig") is not None:
            self._ServiceConfig = ServiceConfig()
            self._ServiceConfig._deserialize(params.get("ServiceConfig"))
        self._AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("ServiceParameters") is not None:
            self._ServiceParameters = []
            for item in params.get("ServiceParameters"):
                obj = ServiceParameter()
                obj._deserialize(item)
                self._ServiceParameters.append(obj)
        if params.get("OauthConfig") is not None:
            self._OauthConfig = OauthConfig()
            self._OauthConfig._deserialize(params.get("OauthConfig"))
        if params.get("ResponseErrorCodes") is not None:
            self._ResponseErrorCodes = []
            for item in params.get("ResponseErrorCodes"):
                obj = ResponseErrorCodeReq()
                obj._deserialize(item)
                self._ResponseErrorCodes.append(obj)
        self._IsBase64Encoded = params.get("IsBase64Encoded")
        self._IsBase64Trigger = params.get("IsBase64Trigger")
        if params.get("Base64EncodedTriggerRules") is not None:
            self._Base64EncodedTriggerRules = []
            for item in params.get("Base64EncodedTriggerRules"):
                obj = Base64EncodedTriggerRule()
                obj._deserialize(item)
                self._Base64EncodedTriggerRules.append(obj)
        self._EventBusId = params.get("EventBusId")
        self._ServiceScfFunctionType = params.get("ServiceScfFunctionType")
        self._EIAMAppType = params.get("EIAMAppType")
        self._EIAMAuthType = params.get("EIAMAuthType")
        self._EIAMAppId = params.get("EIAMAppId")
        self._TokenTimeout = params.get("TokenTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiResponse(AbstractModel):
    """ModifyApi response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyIPStrategyRequest(AbstractModel):
    """ModifyIPStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID of the policy to be modified.
        :type ServiceId: str
        :param _StrategyId: Unique ID of the policy to be modified.
        :type StrategyId: str
        :param _StrategyData: Details of the policy to be modified.
        :type StrategyData: str
        """
        self._ServiceId = None
        self._StrategyId = None
        self._StrategyData = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def StrategyData(self):
        return self._StrategyData

    @StrategyData.setter
    def StrategyData(self, StrategyData):
        self._StrategyData = StrategyData


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._StrategyId = params.get("StrategyId")
        self._StrategyData = params.get("StrategyData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIPStrategyResponse(AbstractModel):
    """ModifyIPStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether modification succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyPluginRequest(AbstractModel):
    """ModifyPlugin request structure.

    """

    def __init__(self):
        r"""
        :param _PluginId: ID of the plugin to be modified
        :type PluginId: str
        :param _PluginName: Plugin name to be modified. A plugin name can contain up to 50 characters out of `a-z`, `A-Z`, `0-9`, and `_`, which must begin with a letter and end with a letter or a number.
        :type PluginName: str
        :param _Description: Plugin description to be modified. A description is within 200 characters.
        :type Description: str
        :param _PluginData: Plugin definition statement to be modified. The json format is supported.
        :type PluginData: str
        """
        self._PluginId = None
        self._PluginName = None
        self._Description = None
        self._PluginData = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def PluginName(self):
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PluginData(self):
        return self._PluginData

    @PluginData.setter
    def PluginData(self, PluginData):
        self._PluginData = PluginData


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._PluginName = params.get("PluginName")
        self._Description = params.get("Description")
        self._PluginData = params.get("PluginData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPluginResponse(AbstractModel):
    """ModifyPlugin response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether modification succeeded.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyServiceEnvironmentStrategyRequest(AbstractModel):
    """ModifyServiceEnvironmentStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _Strategy: Throttling value.
        :type Strategy: int
        :param _EnvironmentNames: Environment list.
        :type EnvironmentNames: list of str
        """
        self._ServiceId = None
        self._Strategy = None
        self._EnvironmentNames = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Strategy(self):
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def EnvironmentNames(self):
        return self._EnvironmentNames

    @EnvironmentNames.setter
    def EnvironmentNames(self, EnvironmentNames):
        self._EnvironmentNames = EnvironmentNames


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Strategy = params.get("Strategy")
        self._EnvironmentNames = params.get("EnvironmentNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceEnvironmentStrategyResponse(AbstractModel):
    """ModifyServiceEnvironmentStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether modification succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyServiceRequest(AbstractModel):
    """ModifyService request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique ID of the service to be modified.
        :type ServiceId: str
        :param _ServiceName: Service name after modification.
        :type ServiceName: str
        :param _ServiceDesc: Service description after modification.
        :type ServiceDesc: str
        :param _Protocol: Service frontend request type after modification, such as `http`, `https`, and `http&https`.
        :type Protocol: str
        :param _NetTypes: Network type list, which is used to specify the supported network types. INNER: private network access; OUTER: public network access. Default value: OUTER.
        :type NetTypes: list of str
        """
        self._ServiceId = None
        self._ServiceName = None
        self._ServiceDesc = None
        self._Protocol = None
        self._NetTypes = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceDesc(self):
        return self._ServiceDesc

    @ServiceDesc.setter
    def ServiceDesc(self, ServiceDesc):
        self._ServiceDesc = ServiceDesc

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def NetTypes(self):
        return self._NetTypes

    @NetTypes.setter
    def NetTypes(self, NetTypes):
        self._NetTypes = NetTypes


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceName = params.get("ServiceName")
        self._ServiceDesc = params.get("ServiceDesc")
        self._Protocol = params.get("Protocol")
        self._NetTypes = params.get("NetTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceResponse(AbstractModel):
    """ModifyService response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySubDomainRequest(AbstractModel):
    """ModifySubDomain request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _SubDomain: Custom domain name whose path mapping is to be modified.
        :type SubDomain: str
        :param _IsDefaultMapping: Whether to change to the default path mapping. true: use the default path mapping; false: use the custom path mapping.
        :type IsDefaultMapping: bool
        :param _CertificateId: Certificate ID, which is required if the HTTPS protocol is included.
        :type CertificateId: str
        :param _Protocol: Custom domain name protocol type after modification. Valid values: http, https, http&https.
        :type Protocol: str
        :param _PathMappingSet: Path mapping list after modification.
        :type PathMappingSet: list of PathMapping
        :param _NetType: Network type. Valid values: INNER, OUTER.
        :type NetType: str
        :param _IsForcedHttps: Whether to force HTTP requests to redirect to HTTPS. Default value: `false`. When this parameter is `true`, API Gateway will redirect all requests using the custom domain name over the HTTP protocol to the HTTPS protocol for forwarding.
        :type IsForcedHttps: bool
        """
        self._ServiceId = None
        self._SubDomain = None
        self._IsDefaultMapping = None
        self._CertificateId = None
        self._Protocol = None
        self._PathMappingSet = None
        self._NetType = None
        self._IsForcedHttps = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def IsDefaultMapping(self):
        return self._IsDefaultMapping

    @IsDefaultMapping.setter
    def IsDefaultMapping(self, IsDefaultMapping):
        self._IsDefaultMapping = IsDefaultMapping

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def PathMappingSet(self):
        return self._PathMappingSet

    @PathMappingSet.setter
    def PathMappingSet(self, PathMappingSet):
        self._PathMappingSet = PathMappingSet

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def IsForcedHttps(self):
        return self._IsForcedHttps

    @IsForcedHttps.setter
    def IsForcedHttps(self, IsForcedHttps):
        self._IsForcedHttps = IsForcedHttps


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._SubDomain = params.get("SubDomain")
        self._IsDefaultMapping = params.get("IsDefaultMapping")
        self._CertificateId = params.get("CertificateId")
        self._Protocol = params.get("Protocol")
        if params.get("PathMappingSet") is not None:
            self._PathMappingSet = []
            for item in params.get("PathMappingSet"):
                obj = PathMapping()
                obj._deserialize(item)
                self._PathMappingSet.append(obj)
        self._NetType = params.get("NetType")
        self._IsForcedHttps = params.get("IsForcedHttps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubDomainResponse(AbstractModel):
    """ModifySubDomain response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the custom domain name is successfully modified.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyUpstreamRequest(AbstractModel):
    """ModifyUpstream request structure.

    """

    def __init__(self):
        r"""
        :param _UpstreamId: Unique upstream ID
        :type UpstreamId: str
        :param _UpstreamName: Upstream name
        :type UpstreamName: str
        :param _UpstreamDescription: Upstream description
        :type UpstreamDescription: str
        :param _Scheme: Backend protocol. Valid values: `HTTP`, `HTTPS`
        :type Scheme: str
        :param _UpstreamType: Upstream access type. Valid values: `IP_PORT`, `K8S`
        :type UpstreamType: str
        :param _Algorithm: Load balancing algorithm. Valid value: `ROUND_ROBIN`
        :type Algorithm: str
        :param _UniqVpcId: Unique VPC ID.
        :type UniqVpcId: str
        :param _Retries: Retry attempts. It defaults to `3`.
        :type Retries: int
        :param _UpstreamHost: Gateway forwarding to the upstream Host request header
        :type UpstreamHost: str
        :param _Nodes: List of backend nodes
        :type Nodes: list of UpstreamNode
        :param _HealthChecker: Health check configuration
        :type HealthChecker: :class:`tencentcloud.apigateway.v20180808.models.UpstreamHealthChecker`
        :param _K8sService: Configuration of TKE service
        :type K8sService: list of K8sService
        """
        self._UpstreamId = None
        self._UpstreamName = None
        self._UpstreamDescription = None
        self._Scheme = None
        self._UpstreamType = None
        self._Algorithm = None
        self._UniqVpcId = None
        self._Retries = None
        self._UpstreamHost = None
        self._Nodes = None
        self._HealthChecker = None
        self._K8sService = None

    @property
    def UpstreamId(self):
        return self._UpstreamId

    @UpstreamId.setter
    def UpstreamId(self, UpstreamId):
        self._UpstreamId = UpstreamId

    @property
    def UpstreamName(self):
        return self._UpstreamName

    @UpstreamName.setter
    def UpstreamName(self, UpstreamName):
        self._UpstreamName = UpstreamName

    @property
    def UpstreamDescription(self):
        return self._UpstreamDescription

    @UpstreamDescription.setter
    def UpstreamDescription(self, UpstreamDescription):
        self._UpstreamDescription = UpstreamDescription

    @property
    def Scheme(self):
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme

    @property
    def UpstreamType(self):
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Retries(self):
        return self._Retries

    @Retries.setter
    def Retries(self, Retries):
        self._Retries = Retries

    @property
    def UpstreamHost(self):
        return self._UpstreamHost

    @UpstreamHost.setter
    def UpstreamHost(self, UpstreamHost):
        self._UpstreamHost = UpstreamHost

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def HealthChecker(self):
        return self._HealthChecker

    @HealthChecker.setter
    def HealthChecker(self, HealthChecker):
        self._HealthChecker = HealthChecker

    @property
    def K8sService(self):
        return self._K8sService

    @K8sService.setter
    def K8sService(self, K8sService):
        self._K8sService = K8sService


    def _deserialize(self, params):
        self._UpstreamId = params.get("UpstreamId")
        self._UpstreamName = params.get("UpstreamName")
        self._UpstreamDescription = params.get("UpstreamDescription")
        self._Scheme = params.get("Scheme")
        self._UpstreamType = params.get("UpstreamType")
        self._Algorithm = params.get("Algorithm")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Retries = params.get("Retries")
        self._UpstreamHost = params.get("UpstreamHost")
        if params.get("Nodes") is not None:
            self._Nodes = []
            for item in params.get("Nodes"):
                obj = UpstreamNode()
                obj._deserialize(item)
                self._Nodes.append(obj)
        if params.get("HealthChecker") is not None:
            self._HealthChecker = UpstreamHealthChecker()
            self._HealthChecker._deserialize(params.get("HealthChecker"))
        if params.get("K8sService") is not None:
            self._K8sService = []
            for item in params.get("K8sService"):
                obj = K8sService()
                obj._deserialize(item)
                self._K8sService.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUpstreamResponse(AbstractModel):
    """ModifyUpstream response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Return modified upstream information
Note: This field may return `NULL`, indicating that no valid value was found.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UpstreamInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UpstreamInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyUsagePlanRequest(AbstractModel):
    """ModifyUsagePlan request structure.

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: Unique usage plan ID.
        :type UsagePlanId: str
        :param _UsagePlanName: Custom usage plan name after modification.
        :type UsagePlanName: str
        :param _UsagePlanDesc: Custom usage plan description after modification.
        :type UsagePlanDesc: str
        :param _MaxRequestNum: Total number of requests allowed. Valid values: -1, [1,99999999]. The default value is `-1`, which indicates no limit.
        :type MaxRequestNum: int
        :param _MaxRequestNumPreSec: Limit of requests per second. Valid values: -1, [1,2000]. The default value is `-1`, which indicates no limit.
        :type MaxRequestNumPreSec: int
        """
        self._UsagePlanId = None
        self._UsagePlanName = None
        self._UsagePlanDesc = None
        self._MaxRequestNum = None
        self._MaxRequestNumPreSec = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def UsagePlanName(self):
        return self._UsagePlanName

    @UsagePlanName.setter
    def UsagePlanName(self, UsagePlanName):
        self._UsagePlanName = UsagePlanName

    @property
    def UsagePlanDesc(self):
        return self._UsagePlanDesc

    @UsagePlanDesc.setter
    def UsagePlanDesc(self, UsagePlanDesc):
        self._UsagePlanDesc = UsagePlanDesc

    @property
    def MaxRequestNum(self):
        return self._MaxRequestNum

    @MaxRequestNum.setter
    def MaxRequestNum(self, MaxRequestNum):
        self._MaxRequestNum = MaxRequestNum

    @property
    def MaxRequestNumPreSec(self):
        return self._MaxRequestNumPreSec

    @MaxRequestNumPreSec.setter
    def MaxRequestNumPreSec(self, MaxRequestNumPreSec):
        self._MaxRequestNumPreSec = MaxRequestNumPreSec


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        self._UsagePlanName = params.get("UsagePlanName")
        self._UsagePlanDesc = params.get("UsagePlanDesc")
        self._MaxRequestNum = params.get("MaxRequestNum")
        self._MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUsagePlanResponse(AbstractModel):
    """ModifyUsagePlan response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Usage plan details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UsagePlanInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class OauthConfig(AbstractModel):
    """OAuth authorization configuration information

    """

    def __init__(self):
        r"""
        :param _PublicKey: Public key for user token verification.
        :type PublicKey: str
        :param _TokenLocation: Token delivery location.
        :type TokenLocation: str
        :param _LoginRedirectUrl: Redirect address, which is used to guide user logins.
        :type LoginRedirectUrl: str
        """
        self._PublicKey = None
        self._TokenLocation = None
        self._LoginRedirectUrl = None

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def TokenLocation(self):
        return self._TokenLocation

    @TokenLocation.setter
    def TokenLocation(self, TokenLocation):
        self._TokenLocation = TokenLocation

    @property
    def LoginRedirectUrl(self):
        return self._LoginRedirectUrl

    @LoginRedirectUrl.setter
    def LoginRedirectUrl(self, LoginRedirectUrl):
        self._LoginRedirectUrl = LoginRedirectUrl


    def _deserialize(self, params):
        self._PublicKey = params.get("PublicKey")
        self._TokenLocation = params.get("TokenLocation")
        self._LoginRedirectUrl = params.get("LoginRedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathMapping(AbstractModel):
    """Custom domain name path mapping.

    """

    def __init__(self):
        r"""
        :param _Path: Path.
        :type Path: str
        :param _Environment: Release environment. Valid values: test, prepub, release.
        :type Environment: str
        """
        self._Path = None
        self._Environment = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Plugin(AbstractModel):
    """Details of the API Gateway plugin

    """

    def __init__(self):
        r"""
        :param _PluginId: Plugin ID
        :type PluginId: str
        :param _PluginName: Plugin name
        :type PluginName: str
        :param _PluginType: Plugin type
        :type PluginType: str
        :param _PluginData: Plugin definition statement
        :type PluginData: str
        :param _Description: Plugin description
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _CreatedTime: Plugin creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
        :type CreatedTime: str
        :param _ModifiedTime: Plugin modification time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used
        :type ModifiedTime: str
        :param _AttachedApiTotalCount: Total number of APIs bound with the plugin
Note: this field may return null, indicating that no valid values can be obtained.
        :type AttachedApiTotalCount: int
        :param _AttachedApis: Information of the API bound with the plugin
Note: this field may return null, indicating that no valid values can be obtained.
        :type AttachedApis: list of AttachedApiInfo
        """
        self._PluginId = None
        self._PluginName = None
        self._PluginType = None
        self._PluginData = None
        self._Description = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._AttachedApiTotalCount = None
        self._AttachedApis = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def PluginName(self):
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def PluginType(self):
        return self._PluginType

    @PluginType.setter
    def PluginType(self, PluginType):
        self._PluginType = PluginType

    @property
    def PluginData(self):
        return self._PluginData

    @PluginData.setter
    def PluginData(self, PluginData):
        self._PluginData = PluginData

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def AttachedApiTotalCount(self):
        return self._AttachedApiTotalCount

    @AttachedApiTotalCount.setter
    def AttachedApiTotalCount(self, AttachedApiTotalCount):
        self._AttachedApiTotalCount = AttachedApiTotalCount

    @property
    def AttachedApis(self):
        return self._AttachedApis

    @AttachedApis.setter
    def AttachedApis(self, AttachedApis):
        self._AttachedApis = AttachedApis


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._PluginName = params.get("PluginName")
        self._PluginType = params.get("PluginType")
        self._PluginData = params.get("PluginData")
        self._Description = params.get("Description")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._AttachedApiTotalCount = params.get("AttachedApiTotalCount")
        if params.get("AttachedApis") is not None:
            self._AttachedApis = []
            for item in params.get("AttachedApis"):
                obj = AttachedApiInfo()
                obj._deserialize(item)
                self._AttachedApis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseService(AbstractModel):
    """Returned result of service publishing

    """

    def __init__(self):
        r"""
        :param _ReleaseDesc: Release remarks.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReleaseDesc: str
        :param _ReleaseVersion: Published version ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReleaseVersion: str
        """
        self._ReleaseDesc = None
        self._ReleaseVersion = None

    @property
    def ReleaseDesc(self):
        return self._ReleaseDesc

    @ReleaseDesc.setter
    def ReleaseDesc(self, ReleaseDesc):
        self._ReleaseDesc = ReleaseDesc

    @property
    def ReleaseVersion(self):
        return self._ReleaseVersion

    @ReleaseVersion.setter
    def ReleaseVersion(self, ReleaseVersion):
        self._ReleaseVersion = ReleaseVersion


    def _deserialize(self, params):
        self._ReleaseDesc = params.get("ReleaseDesc")
        self._ReleaseVersion = params.get("ReleaseVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseServiceRequest(AbstractModel):
    """ReleaseService request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique ID of the service to be published.
        :type ServiceId: str
        :param _EnvironmentName: Name of the environment to be published. Valid values: test (test environment), prepub (pre-release environment), release (release environment).
        :type EnvironmentName: str
        :param _ReleaseDesc: Release description.
        :type ReleaseDesc: str
        :param _ApiIds: `apiId` list, which is reserved. Full API release is used by default.
        :type ApiIds: list of str
        """
        self._ServiceId = None
        self._EnvironmentName = None
        self._ReleaseDesc = None
        self._ApiIds = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ReleaseDesc(self):
        return self._ReleaseDesc

    @ReleaseDesc.setter
    def ReleaseDesc(self, ReleaseDesc):
        self._ReleaseDesc = ReleaseDesc

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._ReleaseDesc = params.get("ReleaseDesc")
        self._ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseServiceResponse(AbstractModel):
    """ReleaseService response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Release information.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ReleaseService`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ReleaseService()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ReqParameter(AbstractModel):
    """Request parameter

    """

    def __init__(self):
        r"""
        :param _Name: API frontend parameter name.
        :type Name: str
        :param _Position: Position of the API frontend parameter, such as the header. Supported values: `header`, `query`, and `path`.
        :type Position: str
        :param _Type: API frontend parameter type, such as `String` and `int`.
        :type Type: str
        :param _DefaultValue: Default value of API frontend parameter.
        :type DefaultValue: str
        :param _Required: Whether the API frontend parameter is required. True: yes; False: no.
        :type Required: bool
        :param _Desc: API frontend parameter remarks.
        :type Desc: str
        """
        self._Name = None
        self._Position = None
        self._Type = None
        self._DefaultValue = None
        self._Required = None
        self._Desc = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def Required(self):
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Position = params.get("Position")
        self._Type = params.get("Type")
        self._DefaultValue = params.get("DefaultValue")
        self._Required = params.get("Required")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestConfig(AbstractModel):
    """Frontend path configuration

    """

    def __init__(self):
        r"""
        :param _Path: API path, such as `/path`.
        :type Path: str
        :param _Method: API request method, such as `GET`.
        :type Method: str
        """
        self._Path = None
        self._Method = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestParameter(AbstractModel):
    """Request parameter

    """

    def __init__(self):
        r"""
        :param _Name: Request parameter name
        :type Name: str
        :param _Desc: Description
        :type Desc: str
        :param _Position: Parameter position
        :type Position: str
        :param _Type: Parameter type
        :type Type: str
        :param _DefaultValue: Default value
        :type DefaultValue: str
        :param _Required: Whether it is required
        :type Required: bool
        """
        self._Name = None
        self._Desc = None
        self._Position = None
        self._Type = None
        self._DefaultValue = None
        self._Required = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def Required(self):
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._Position = params.get("Position")
        self._Type = params.get("Type")
        self._DefaultValue = params.get("DefaultValue")
        self._Required = params.get("Required")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAPIDocPasswordRequest(AbstractModel):
    """ResetAPIDocPassword request structure.

    """

    def __init__(self):
        r"""
        :param _ApiDocId: API document ID
        :type ApiDocId: str
        """
        self._ApiDocId = None

    @property
    def ApiDocId(self):
        return self._ApiDocId

    @ApiDocId.setter
    def ApiDocId(self, ApiDocId):
        self._ApiDocId = ApiDocId


    def _deserialize(self, params):
        self._ApiDocId = params.get("ApiDocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAPIDocPasswordResponse(AbstractModel):
    """ResetAPIDocPassword response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Basic information of API document
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = APIDoc()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ResponseErrorCodeReq(AbstractModel):
    """Error code input parameter

    """

    def __init__(self):
        r"""
        :param _Code: Custom response configuration error code.
        :type Code: int
        :param _Msg: Custom response configuration error message.
        :type Msg: str
        :param _Desc: Custom response configuration error code remarks.
        :type Desc: str
        :param _ConvertedCode: Custom error code conversion.
        :type ConvertedCode: int
        :param _NeedConvert: Whether to enable error code conversion.
        :type NeedConvert: bool
        """
        self._Code = None
        self._Msg = None
        self._Desc = None
        self._ConvertedCode = None
        self._NeedConvert = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ConvertedCode(self):
        return self._ConvertedCode

    @ConvertedCode.setter
    def ConvertedCode(self, ConvertedCode):
        self._ConvertedCode = ConvertedCode

    @property
    def NeedConvert(self):
        return self._NeedConvert

    @NeedConvert.setter
    def NeedConvert(self, NeedConvert):
        self._NeedConvert = NeedConvert


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._Desc = params.get("Desc")
        self._ConvertedCode = params.get("ConvertedCode")
        self._NeedConvert = params.get("NeedConvert")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Service(AbstractModel):
    """Service list display

    """

    def __init__(self):
        r"""
        :param _InnerHttpsPort: Port for HTTPS access over private network.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InnerHttpsPort: int
        :param _ServiceDesc: Custom service description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceDesc: str
        :param _Protocol: Service frontend request type, such as `http`, `https`, and `http&https`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param _NetTypes: Network types supported by service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NetTypes: list of str
        :param _ExclusiveSetName: Dedicated cluster name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExclusiveSetName: str
        :param _ServiceId: Unique service ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceId: str
        :param _IpVersion: IP version.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpVersion: str
        :param _AvailableEnvironments: List of published environments, such as test, prepub, and release.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AvailableEnvironments: list of str
        :param _ServiceName: Custom service name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceName: str
        :param _OuterSubDomain: Public domain name assigned by the system for this service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OuterSubDomain: str
        :param _CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _InnerHttpPort: Port for HTTP access over private network.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InnerHttpPort: int
        :param _InnerSubDomain: Private domain name automatically assigned by the system for this service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InnerSubDomain: str
        :param _TradeIsolateStatus: Billing status of service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TradeIsolateStatus: int
        :param _Tags: Tags bound to a service.
Note: this field may return null, indicating that no valid values found.
        :type Tags: list of Tag
        :param _InstanceId: Dedicated instance
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _SetType: Cluster type
Note: this field may return null, indicating that no valid values can be obtained.
        :type SetType: str
        :param _DeploymentType: Cluster type for service deployment
Note: this field may return null, indicating that no valid values found.
        :type DeploymentType: str
        """
        self._InnerHttpsPort = None
        self._ServiceDesc = None
        self._Protocol = None
        self._ModifiedTime = None
        self._NetTypes = None
        self._ExclusiveSetName = None
        self._ServiceId = None
        self._IpVersion = None
        self._AvailableEnvironments = None
        self._ServiceName = None
        self._OuterSubDomain = None
        self._CreatedTime = None
        self._InnerHttpPort = None
        self._InnerSubDomain = None
        self._TradeIsolateStatus = None
        self._Tags = None
        self._InstanceId = None
        self._SetType = None
        self._DeploymentType = None

    @property
    def InnerHttpsPort(self):
        return self._InnerHttpsPort

    @InnerHttpsPort.setter
    def InnerHttpsPort(self, InnerHttpsPort):
        self._InnerHttpsPort = InnerHttpsPort

    @property
    def ServiceDesc(self):
        return self._ServiceDesc

    @ServiceDesc.setter
    def ServiceDesc(self, ServiceDesc):
        self._ServiceDesc = ServiceDesc

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def NetTypes(self):
        return self._NetTypes

    @NetTypes.setter
    def NetTypes(self, NetTypes):
        self._NetTypes = NetTypes

    @property
    def ExclusiveSetName(self):
        return self._ExclusiveSetName

    @ExclusiveSetName.setter
    def ExclusiveSetName(self, ExclusiveSetName):
        self._ExclusiveSetName = ExclusiveSetName

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def IpVersion(self):
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def AvailableEnvironments(self):
        return self._AvailableEnvironments

    @AvailableEnvironments.setter
    def AvailableEnvironments(self, AvailableEnvironments):
        self._AvailableEnvironments = AvailableEnvironments

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def OuterSubDomain(self):
        return self._OuterSubDomain

    @OuterSubDomain.setter
    def OuterSubDomain(self, OuterSubDomain):
        self._OuterSubDomain = OuterSubDomain

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def InnerHttpPort(self):
        return self._InnerHttpPort

    @InnerHttpPort.setter
    def InnerHttpPort(self, InnerHttpPort):
        self._InnerHttpPort = InnerHttpPort

    @property
    def InnerSubDomain(self):
        return self._InnerSubDomain

    @InnerSubDomain.setter
    def InnerSubDomain(self, InnerSubDomain):
        self._InnerSubDomain = InnerSubDomain

    @property
    def TradeIsolateStatus(self):
        return self._TradeIsolateStatus

    @TradeIsolateStatus.setter
    def TradeIsolateStatus(self, TradeIsolateStatus):
        self._TradeIsolateStatus = TradeIsolateStatus

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SetType(self):
        return self._SetType

    @SetType.setter
    def SetType(self, SetType):
        self._SetType = SetType

    @property
    def DeploymentType(self):
        return self._DeploymentType

    @DeploymentType.setter
    def DeploymentType(self, DeploymentType):
        self._DeploymentType = DeploymentType


    def _deserialize(self, params):
        self._InnerHttpsPort = params.get("InnerHttpsPort")
        self._ServiceDesc = params.get("ServiceDesc")
        self._Protocol = params.get("Protocol")
        self._ModifiedTime = params.get("ModifiedTime")
        self._NetTypes = params.get("NetTypes")
        self._ExclusiveSetName = params.get("ExclusiveSetName")
        self._ServiceId = params.get("ServiceId")
        self._IpVersion = params.get("IpVersion")
        self._AvailableEnvironments = params.get("AvailableEnvironments")
        self._ServiceName = params.get("ServiceName")
        self._OuterSubDomain = params.get("OuterSubDomain")
        self._CreatedTime = params.get("CreatedTime")
        self._InnerHttpPort = params.get("InnerHttpPort")
        self._InnerSubDomain = params.get("InnerSubDomain")
        self._TradeIsolateStatus = params.get("TradeIsolateStatus")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._SetType = params.get("SetType")
        self._DeploymentType = params.get("DeploymentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceConfig(AbstractModel):
    """ServiceConfig information

    """

    def __init__(self):
        r"""
        :param _Product: The backend type. It’s available when `vpc` is enabled. Values: `clb`, `cvm` and `upstream`.
        :type Product: str
        :param _UniqVpcId: Unique VPC ID.
        :type UniqVpcId: str
        :param _Url: API backend service URL, which is required if `ServiceType` is `HTTP`.
        :type Url: str
        :param _Path: API backend service path, such as `/path`, which is required if `ServiceType` is `HTTP`. The frontend and backend paths can be different.
        :type Path: str
        :param _Method: API backend service request method, such as `GET`, which is required if `ServiceType` is `HTTP`. The frontend and backend methods can be different
        :type Method: str
        :param _UpstreamId: It’s required for `upstream`.
Note: This field may return `NULL`, indicating that no valid value was found.
        :type UpstreamId: str
        :param _CosConfig: API backend COS configuration. It’s required if the `ServiceType` is ·`COS`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CosConfig: :class:`tencentcloud.apigateway.v20180808.models.CosConfig`
        """
        self._Product = None
        self._UniqVpcId = None
        self._Url = None
        self._Path = None
        self._Method = None
        self._UpstreamId = None
        self._CosConfig = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def UpstreamId(self):
        return self._UpstreamId

    @UpstreamId.setter
    def UpstreamId(self, UpstreamId):
        self._UpstreamId = UpstreamId

    @property
    def CosConfig(self):
        return self._CosConfig

    @CosConfig.setter
    def CosConfig(self, CosConfig):
        self._CosConfig = CosConfig


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Url = params.get("Url")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        self._UpstreamId = params.get("UpstreamId")
        if params.get("CosConfig") is not None:
            self._CosConfig = CosConfig()
            self._CosConfig._deserialize(params.get("CosConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceEnvironmentSet(AbstractModel):
    """Details of environments bound to service

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of environments bound to service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _EnvironmentList: List of environments bound to service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnvironmentList: list of Environment
        """
        self._TotalCount = None
        self._EnvironmentList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EnvironmentList(self):
        return self._EnvironmentList

    @EnvironmentList.setter
    def EnvironmentList(self, EnvironmentList):
        self._EnvironmentList = EnvironmentList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("EnvironmentList") is not None:
            self._EnvironmentList = []
            for item in params.get("EnvironmentList"):
                obj = Environment()
                obj._deserialize(item)
                self._EnvironmentList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceEnvironmentStrategy(AbstractModel):
    """Service environment policy

    """

    def __init__(self):
        r"""
        :param _EnvironmentName: Environment name.
        :type EnvironmentName: str
        :param _Url: Access service environment URL.
        :type Url: str
        :param _Status: Release status.
        :type Status: int
        :param _VersionName: Published version number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VersionName: str
        :param _Strategy: Throttling value.
        :type Strategy: int
        :param _MaxStrategy: Maximum quota value
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxStrategy: int
        """
        self._EnvironmentName = None
        self._Url = None
        self._Status = None
        self._VersionName = None
        self._Strategy = None
        self._MaxStrategy = None

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Strategy(self):
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def MaxStrategy(self):
        return self._MaxStrategy

    @MaxStrategy.setter
    def MaxStrategy(self, MaxStrategy):
        self._MaxStrategy = MaxStrategy


    def _deserialize(self, params):
        self._EnvironmentName = params.get("EnvironmentName")
        self._Url = params.get("Url")
        self._Status = params.get("Status")
        self._VersionName = params.get("VersionName")
        self._Strategy = params.get("Strategy")
        self._MaxStrategy = params.get("MaxStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceEnvironmentStrategyStatus(AbstractModel):
    """List of policies bound to environment

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of throttling policies.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _EnvironmentList: Throttling policy list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnvironmentList: list of ServiceEnvironmentStrategy
        """
        self._TotalCount = None
        self._EnvironmentList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EnvironmentList(self):
        return self._EnvironmentList

    @EnvironmentList.setter
    def EnvironmentList(self, EnvironmentList):
        self._EnvironmentList = EnvironmentList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("EnvironmentList") is not None:
            self._EnvironmentList = []
            for item in params.get("EnvironmentList"):
                obj = ServiceEnvironmentStrategy()
                obj._deserialize(item)
                self._EnvironmentList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceParameter(AbstractModel):
    """ServiceParameter

    """

    def __init__(self):
        r"""
        :param _Name: API backend service parameter name, which is used only if `ServiceType` is `HTTP`. The frontend and backend parameter names can be different.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Position: Position of API backend service parameter, such as `head`, which is used only if `ServiceType` is `HTTP`. The positions of frontend and backend parameters can be different.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Position: str
        :param _RelevantRequestParameterPosition: Position of the API frontend parameter corresponding to the backend service parameter, such as `head`, which is used only if `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RelevantRequestParameterPosition: str
        :param _RelevantRequestParameterName: Name of the API frontend parameter corresponding to the backend service parameter, which is used only if `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RelevantRequestParameterName: str
        :param _DefaultValue: Default value of API backend service parameter, which is used only if `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DefaultValue: str
        :param _RelevantRequestParameterDesc: API backend service parameter remarks, which is used only if `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RelevantRequestParameterDesc: str
        :param _RelevantRequestParameterType: API backend service parameter type, which is used only if `ServiceType` is `HTTP`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RelevantRequestParameterType: str
        """
        self._Name = None
        self._Position = None
        self._RelevantRequestParameterPosition = None
        self._RelevantRequestParameterName = None
        self._DefaultValue = None
        self._RelevantRequestParameterDesc = None
        self._RelevantRequestParameterType = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def RelevantRequestParameterPosition(self):
        return self._RelevantRequestParameterPosition

    @RelevantRequestParameterPosition.setter
    def RelevantRequestParameterPosition(self, RelevantRequestParameterPosition):
        self._RelevantRequestParameterPosition = RelevantRequestParameterPosition

    @property
    def RelevantRequestParameterName(self):
        return self._RelevantRequestParameterName

    @RelevantRequestParameterName.setter
    def RelevantRequestParameterName(self, RelevantRequestParameterName):
        self._RelevantRequestParameterName = RelevantRequestParameterName

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def RelevantRequestParameterDesc(self):
        return self._RelevantRequestParameterDesc

    @RelevantRequestParameterDesc.setter
    def RelevantRequestParameterDesc(self, RelevantRequestParameterDesc):
        self._RelevantRequestParameterDesc = RelevantRequestParameterDesc

    @property
    def RelevantRequestParameterType(self):
        return self._RelevantRequestParameterType

    @RelevantRequestParameterType.setter
    def RelevantRequestParameterType(self, RelevantRequestParameterType):
        self._RelevantRequestParameterType = RelevantRequestParameterType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Position = params.get("Position")
        self._RelevantRequestParameterPosition = params.get("RelevantRequestParameterPosition")
        self._RelevantRequestParameterName = params.get("RelevantRequestParameterName")
        self._DefaultValue = params.get("DefaultValue")
        self._RelevantRequestParameterDesc = params.get("RelevantRequestParameterDesc")
        self._RelevantRequestParameterType = params.get("RelevantRequestParameterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceReleaseHistory(AbstractModel):
    """Service release history

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of published versions.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _VersionList: Historical version list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VersionList: list of ServiceReleaseHistoryInfo
        """
        self._TotalCount = None
        self._VersionList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VersionList(self):
        return self._VersionList

    @VersionList.setter
    def VersionList(self, VersionList):
        self._VersionList = VersionList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("VersionList") is not None:
            self._VersionList = []
            for item in params.get("VersionList"):
                obj = ServiceReleaseHistoryInfo()
                obj._deserialize(item)
                self._VersionList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceReleaseHistoryInfo(AbstractModel):
    """Service release list details

    """

    def __init__(self):
        r"""
        :param _VersionName: Version ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VersionName: str
        :param _VersionDesc: Version description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VersionDesc: str
        :param _ReleaseTime: Version release time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReleaseTime: str
        """
        self._VersionName = None
        self._VersionDesc = None
        self._ReleaseTime = None

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def VersionDesc(self):
        return self._VersionDesc

    @VersionDesc.setter
    def VersionDesc(self, VersionDesc):
        self._VersionDesc = VersionDesc

    @property
    def ReleaseTime(self):
        return self._ReleaseTime

    @ReleaseTime.setter
    def ReleaseTime(self, ReleaseTime):
        self._ReleaseTime = ReleaseTime


    def _deserialize(self, params):
        self._VersionName = params.get("VersionName")
        self._VersionDesc = params.get("VersionDesc")
        self._ReleaseTime = params.get("ReleaseTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceReleaseVersion(AbstractModel):
    """Service release version

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of published versions.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _VersionList: Release version list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VersionList: list of ServiceReleaseHistoryInfo
        """
        self._TotalCount = None
        self._VersionList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VersionList(self):
        return self._VersionList

    @VersionList.setter
    def VersionList(self, VersionList):
        self._VersionList = VersionList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("VersionList") is not None:
            self._VersionList = []
            for item in params.get("VersionList"):
                obj = ServiceReleaseHistoryInfo()
                obj._deserialize(item)
                self._VersionList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceSubDomainMappings(AbstractModel):
    """Custom service domain name path mapping

    """

    def __init__(self):
        r"""
        :param _IsDefaultMapping: Whether the default path mapping is used. true: use the default path mapping; false: use the custom path mapping (`PathMappingSet` is required in this case).
        :type IsDefaultMapping: bool
        :param _PathMappingSet: Custom path mapping list.
        :type PathMappingSet: list of PathMapping
        """
        self._IsDefaultMapping = None
        self._PathMappingSet = None

    @property
    def IsDefaultMapping(self):
        return self._IsDefaultMapping

    @IsDefaultMapping.setter
    def IsDefaultMapping(self, IsDefaultMapping):
        self._IsDefaultMapping = IsDefaultMapping

    @property
    def PathMappingSet(self):
        return self._PathMappingSet

    @PathMappingSet.setter
    def PathMappingSet(self, PathMappingSet):
        self._PathMappingSet = PathMappingSet


    def _deserialize(self, params):
        self._IsDefaultMapping = params.get("IsDefaultMapping")
        if params.get("PathMappingSet") is not None:
            self._PathMappingSet = []
            for item in params.get("PathMappingSet"):
                obj = PathMapping()
                obj._deserialize(item)
                self._PathMappingSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceUsagePlanSet(AbstractModel):
    """List of usage plans bound to service

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of usage plans bound to service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _ServiceUsagePlanList: List of usage plans bound to service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceUsagePlanList: list of ApiUsagePlan
        """
        self._TotalCount = None
        self._ServiceUsagePlanList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ServiceUsagePlanList(self):
        return self._ServiceUsagePlanList

    @ServiceUsagePlanList.setter
    def ServiceUsagePlanList(self, ServiceUsagePlanList):
        self._ServiceUsagePlanList = ServiceUsagePlanList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ServiceUsagePlanList") is not None:
            self._ServiceUsagePlanList = []
            for item in params.get("ServiceUsagePlanList"):
                obj = ApiUsagePlan()
                obj._deserialize(item)
                self._ServiceUsagePlanList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServicesStatus(AbstractModel):
    """Service list display

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of services in list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _ServiceSet: Service list details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceSet: list of Service
        """
        self._TotalCount = None
        self._ServiceSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ServiceSet(self):
        return self._ServiceSet

    @ServiceSet.setter
    def ServiceSet(self, ServiceSet):
        self._ServiceSet = ServiceSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ServiceSet") is not None:
            self._ServiceSet = []
            for item in params.get("ServiceSet"):
                obj = Service()
                obj._deserialize(item)
                self._ServiceSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Information of tag bound to API.

    """

    def __init__(self):
        r"""
        :param _Key: Tag key.
        :type Key: str
        :param _Value: Tag value.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetServicesReq(AbstractModel):
    """TSF Serverless input parameters

    """

    def __init__(self):
        r"""
        :param _VmIp: VM IP
        :type VmIp: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _VmPort: VM Port
        :type VmPort: int
        :param _HostIp: IP of the host where the CVM instance resides
        :type HostIp: str
        :param _DockerIp: Docker IP
        :type DockerIp: str
        """
        self._VmIp = None
        self._VpcId = None
        self._VmPort = None
        self._HostIp = None
        self._DockerIp = None

    @property
    def VmIp(self):
        return self._VmIp

    @VmIp.setter
    def VmIp(self, VmIp):
        self._VmIp = VmIp

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VmPort(self):
        return self._VmPort

    @VmPort.setter
    def VmPort(self, VmPort):
        self._VmPort = VmPort

    @property
    def HostIp(self):
        return self._HostIp

    @HostIp.setter
    def HostIp(self, HostIp):
        self._HostIp = HostIp

    @property
    def DockerIp(self):
        return self._DockerIp

    @DockerIp.setter
    def DockerIp(self, DockerIp):
        self._DockerIp = DockerIp


    def _deserialize(self, params):
        self._VmIp = params.get("VmIp")
        self._VpcId = params.get("VpcId")
        self._VmPort = params.get("VmPort")
        self._HostIp = params.get("HostIp")
        self._DockerIp = params.get("DockerIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfLoadBalanceConfResp(AbstractModel):
    """`TsfLoadBalanceConf` output parameter usage

    """

    def __init__(self):
        r"""
        :param _IsLoadBalance: Whether load balancing is enabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsLoadBalance: bool
        :param _Method: Load balancing method.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Method: str
        :param _SessionStickRequired: Whether session persistence is enabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SessionStickRequired: bool
        :param _SessionStickTimeout: Session persistence timeout period.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SessionStickTimeout: int
        """
        self._IsLoadBalance = None
        self._Method = None
        self._SessionStickRequired = None
        self._SessionStickTimeout = None

    @property
    def IsLoadBalance(self):
        return self._IsLoadBalance

    @IsLoadBalance.setter
    def IsLoadBalance(self, IsLoadBalance):
        self._IsLoadBalance = IsLoadBalance

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def SessionStickRequired(self):
        return self._SessionStickRequired

    @SessionStickRequired.setter
    def SessionStickRequired(self, SessionStickRequired):
        self._SessionStickRequired = SessionStickRequired

    @property
    def SessionStickTimeout(self):
        return self._SessionStickTimeout

    @SessionStickTimeout.setter
    def SessionStickTimeout(self, SessionStickTimeout):
        self._SessionStickTimeout = SessionStickTimeout


    def _deserialize(self, params):
        self._IsLoadBalance = params.get("IsLoadBalance")
        self._Method = params.get("Method")
        self._SessionStickRequired = params.get("SessionStickRequired")
        self._SessionStickTimeout = params.get("SessionStickTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindEnvironmentRequest(AbstractModel):
    """UnBindEnvironment request structure.

    """

    def __init__(self):
        r"""
        :param _BindType: Binding type. Valid values: API, SERVICE. Default value: SERVICE.
        :type BindType: str
        :param _UsagePlanIds: List of unique IDs of the usage plans to be bound.
        :type UsagePlanIds: list of str
        :param _Environment: Service environment to be unbound.
        :type Environment: str
        :param _ServiceId: Unique ID of the service to be unbound.
        :type ServiceId: str
        :param _ApiIds: Unique API ID array, which is required if `BindType` is `API`.
        :type ApiIds: list of str
        """
        self._BindType = None
        self._UsagePlanIds = None
        self._Environment = None
        self._ServiceId = None
        self._ApiIds = None

    @property
    def BindType(self):
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType

    @property
    def UsagePlanIds(self):
        return self._UsagePlanIds

    @UsagePlanIds.setter
    def UsagePlanIds(self, UsagePlanIds):
        self._UsagePlanIds = UsagePlanIds

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds


    def _deserialize(self, params):
        self._BindType = params.get("BindType")
        self._UsagePlanIds = params.get("UsagePlanIds")
        self._Environment = params.get("Environment")
        self._ServiceId = params.get("ServiceId")
        self._ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindEnvironmentResponse(AbstractModel):
    """UnBindEnvironment response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether unbinding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UnBindIPStrategyRequest(AbstractModel):
    """UnBindIPStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique ID of the service to be unbound.
        :type ServiceId: str
        :param _StrategyId: Unique ID of the IP policy to be unbound.
        :type StrategyId: str
        :param _EnvironmentName: Environment to be unbound.
        :type EnvironmentName: str
        :param _UnBindApiIds: List of APIs to be unbound.
        :type UnBindApiIds: list of str
        """
        self._ServiceId = None
        self._StrategyId = None
        self._EnvironmentName = None
        self._UnBindApiIds = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def UnBindApiIds(self):
        return self._UnBindApiIds

    @UnBindApiIds.setter
    def UnBindApiIds(self, UnBindApiIds):
        self._UnBindApiIds = UnBindApiIds


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._StrategyId = params.get("StrategyId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._UnBindApiIds = params.get("UnBindApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindIPStrategyResponse(AbstractModel):
    """UnBindIPStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether unbinding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UnBindSecretIdsRequest(AbstractModel):
    """UnBindSecretIds request structure.

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: Unique ID of the usage plan to be unbound.
        :type UsagePlanId: str
        :param _AccessKeyIds: Array of IDs of the keys to be unbound.
        :type AccessKeyIds: list of str
        """
        self._UsagePlanId = None
        self._AccessKeyIds = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def AccessKeyIds(self):
        return self._AccessKeyIds

    @AccessKeyIds.setter
    def AccessKeyIds(self, AccessKeyIds):
        self._AccessKeyIds = AccessKeyIds


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        self._AccessKeyIds = params.get("AccessKeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindSecretIdsResponse(AbstractModel):
    """UnBindSecretIds response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether unbinding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UnBindSubDomainRequest(AbstractModel):
    """UnBindSubDomain request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique service ID.
        :type ServiceId: str
        :param _SubDomain: Custom domain name to be unbound.
        :type SubDomain: str
        """
        self._ServiceId = None
        self._SubDomain = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._SubDomain = params.get("SubDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindSubDomainResponse(AbstractModel):
    """UnBindSubDomain response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the custom domain name is successfully unbound.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UnReleaseServiceRequest(AbstractModel):
    """UnReleaseService request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique ID of the service to be deactivated.
        :type ServiceId: str
        :param _EnvironmentName: Name of the environment to be deactivated. Valid values: test (test environment), prepub (pre-release environment), release (release environment).
        :type EnvironmentName: str
        :param _ApiIds: List of APIs to be deactivated, which is a reserved field.
        :type ApiIds: list of str
        """
        self._ServiceId = None
        self._EnvironmentName = None
        self._ApiIds = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnReleaseServiceResponse(AbstractModel):
    """UnReleaseService response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether deactivation succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UnbindApiAppRequest(AbstractModel):
    """UnbindApiApp request structure.

    """

    def __init__(self):
        r"""
        :param _ApiAppId: Unique ID of the application to be bound.
        :type ApiAppId: str
        :param _Environment: Environment to be bound.
        :type Environment: str
        :param _ServiceId: Unique ID of the service to be bound.
        :type ServiceId: str
        :param _ApiId: Unique ID of the API to be bound.
        :type ApiId: str
        """
        self._ApiAppId = None
        self._Environment = None
        self._ServiceId = None
        self._ApiId = None

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId


    def _deserialize(self, params):
        self._ApiAppId = params.get("ApiAppId")
        self._Environment = params.get("Environment")
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindApiAppResponse(AbstractModel):
    """UnbindApiApp response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether unbinding succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UpdateApiAppKeyRequest(AbstractModel):
    """UpdateApiAppKey request structure.

    """

    def __init__(self):
        r"""
        :param _ApiAppId: Unique application ID.
        :type ApiAppId: str
        :param _ApiAppKey: Application Key.
        :type ApiAppKey: str
        :param _ApiAppSecret: Application Secret.
        :type ApiAppSecret: str
        """
        self._ApiAppId = None
        self._ApiAppKey = None
        self._ApiAppSecret = None

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId

    @property
    def ApiAppKey(self):
        return self._ApiAppKey

    @ApiAppKey.setter
    def ApiAppKey(self, ApiAppKey):
        self._ApiAppKey = ApiAppKey

    @property
    def ApiAppSecret(self):
        return self._ApiAppSecret

    @ApiAppSecret.setter
    def ApiAppSecret(self, ApiAppSecret):
        self._ApiAppSecret = ApiAppSecret


    def _deserialize(self, params):
        self._ApiAppId = params.get("ApiAppId")
        self._ApiAppKey = params.get("ApiAppKey")
        self._ApiAppSecret = params.get("ApiAppSecret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApiAppKeyResponse(AbstractModel):
    """UpdateApiAppKey response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether update succeeded.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UpdateApiKeyRequest(AbstractModel):
    """UpdateApiKey request structure.

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: ID of the key to be changed.
        :type AccessKeyId: str
        :param _AccessKeySecret: Key to be updated, which is required when a custom key is updated. It can contain 10–50 letters, digits, and underscores.
        :type AccessKeySecret: str
        """
        self._AccessKeyId = None
        self._AccessKeySecret = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def AccessKeySecret(self):
        return self._AccessKeySecret

    @AccessKeySecret.setter
    def AccessKeySecret(self, AccessKeySecret):
        self._AccessKeySecret = AccessKeySecret


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        self._AccessKeySecret = params.get("AccessKeySecret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApiKeyResponse(AbstractModel):
    """UpdateApiKey response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Key details after change.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiKey()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class UpdateServiceRequest(AbstractModel):
    """UpdateService request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique ID of the service to be switch.
        :type ServiceId: str
        :param _EnvironmentName: Name of the environment to be switched to. Valid values: test (test environment), prepub (pre-release environment), release (release environment).
        :type EnvironmentName: str
        :param _VersionName: Number of the version to be switched to.
        :type VersionName: str
        :param _UpdateDesc: Switch description.
        :type UpdateDesc: str
        """
        self._ServiceId = None
        self._EnvironmentName = None
        self._VersionName = None
        self._UpdateDesc = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def UpdateDesc(self):
        return self._UpdateDesc

    @UpdateDesc.setter
    def UpdateDesc(self, UpdateDesc):
        self._UpdateDesc = UpdateDesc


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._VersionName = params.get("VersionName")
        self._UpdateDesc = params.get("UpdateDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateServiceResponse(AbstractModel):
    """UpdateService response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the version is successfully switched.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UpstreamHealthChecker(AbstractModel):
    """Upstream health check parameter configuration

    """

    def __init__(self):
        r"""
        :param _EnableActiveCheck: Specifies whether to enable active health check
        :type EnableActiveCheck: bool
        :param _EnablePassiveCheck: Specifies whether the enable passive health check
        :type EnablePassiveCheck: bool
        :param _HealthyHttpStatus: The HTTP status code that indicates that the upstream is healthy
        :type HealthyHttpStatus: str
        :param _UnhealthyHttpStatus: The HTTP status code that indicates that the upstream is unhealthy
        :type UnhealthyHttpStatus: str
        :param _TcpFailureThreshold: The threshold on consecutive TCP errors. Range: [0, 254]. `0` indicates not to check TCP.
        :type TcpFailureThreshold: int
        :param _TimeoutThreshold: The threshold on consecutive timeouts. Range: [0, 254]. `0` indicates not to check TCP.
        :type TimeoutThreshold: int
        :param _HttpFailureThreshold: The threshold on consecutive HTTP errors. Range: [0, 254]. `0` indicates not to check HTTP.
        :type HttpFailureThreshold: int
        :param _ActiveCheckHttpPath: The path for active health check. It defaults to `/`.
        :type ActiveCheckHttpPath: str
        :param _ActiveCheckTimeout: The timeout period for active health check in seconds. Default: `5`. 
        :type ActiveCheckTimeout: int
        :param _ActiveCheckInterval: The interval for active health check in seconds. Default: `5`. 
        :type ActiveCheckInterval: int
        :param _ActiveRequestHeader: Header of the active health check request
        :type ActiveRequestHeader: list of UpstreamHealthCheckerReqHeaders
        :param _UnhealthyTimeout: The period for an abnormal to recover automatically in seconds. If only the passive health check is enabled, it must be greater than 0. Otherwise the abnormal nodes can not recovered automatically. The default value is 30 seconds. 
        :type UnhealthyTimeout: int
        """
        self._EnableActiveCheck = None
        self._EnablePassiveCheck = None
        self._HealthyHttpStatus = None
        self._UnhealthyHttpStatus = None
        self._TcpFailureThreshold = None
        self._TimeoutThreshold = None
        self._HttpFailureThreshold = None
        self._ActiveCheckHttpPath = None
        self._ActiveCheckTimeout = None
        self._ActiveCheckInterval = None
        self._ActiveRequestHeader = None
        self._UnhealthyTimeout = None

    @property
    def EnableActiveCheck(self):
        return self._EnableActiveCheck

    @EnableActiveCheck.setter
    def EnableActiveCheck(self, EnableActiveCheck):
        self._EnableActiveCheck = EnableActiveCheck

    @property
    def EnablePassiveCheck(self):
        return self._EnablePassiveCheck

    @EnablePassiveCheck.setter
    def EnablePassiveCheck(self, EnablePassiveCheck):
        self._EnablePassiveCheck = EnablePassiveCheck

    @property
    def HealthyHttpStatus(self):
        return self._HealthyHttpStatus

    @HealthyHttpStatus.setter
    def HealthyHttpStatus(self, HealthyHttpStatus):
        self._HealthyHttpStatus = HealthyHttpStatus

    @property
    def UnhealthyHttpStatus(self):
        return self._UnhealthyHttpStatus

    @UnhealthyHttpStatus.setter
    def UnhealthyHttpStatus(self, UnhealthyHttpStatus):
        self._UnhealthyHttpStatus = UnhealthyHttpStatus

    @property
    def TcpFailureThreshold(self):
        return self._TcpFailureThreshold

    @TcpFailureThreshold.setter
    def TcpFailureThreshold(self, TcpFailureThreshold):
        self._TcpFailureThreshold = TcpFailureThreshold

    @property
    def TimeoutThreshold(self):
        return self._TimeoutThreshold

    @TimeoutThreshold.setter
    def TimeoutThreshold(self, TimeoutThreshold):
        self._TimeoutThreshold = TimeoutThreshold

    @property
    def HttpFailureThreshold(self):
        return self._HttpFailureThreshold

    @HttpFailureThreshold.setter
    def HttpFailureThreshold(self, HttpFailureThreshold):
        self._HttpFailureThreshold = HttpFailureThreshold

    @property
    def ActiveCheckHttpPath(self):
        return self._ActiveCheckHttpPath

    @ActiveCheckHttpPath.setter
    def ActiveCheckHttpPath(self, ActiveCheckHttpPath):
        self._ActiveCheckHttpPath = ActiveCheckHttpPath

    @property
    def ActiveCheckTimeout(self):
        return self._ActiveCheckTimeout

    @ActiveCheckTimeout.setter
    def ActiveCheckTimeout(self, ActiveCheckTimeout):
        self._ActiveCheckTimeout = ActiveCheckTimeout

    @property
    def ActiveCheckInterval(self):
        return self._ActiveCheckInterval

    @ActiveCheckInterval.setter
    def ActiveCheckInterval(self, ActiveCheckInterval):
        self._ActiveCheckInterval = ActiveCheckInterval

    @property
    def ActiveRequestHeader(self):
        return self._ActiveRequestHeader

    @ActiveRequestHeader.setter
    def ActiveRequestHeader(self, ActiveRequestHeader):
        self._ActiveRequestHeader = ActiveRequestHeader

    @property
    def UnhealthyTimeout(self):
        return self._UnhealthyTimeout

    @UnhealthyTimeout.setter
    def UnhealthyTimeout(self, UnhealthyTimeout):
        self._UnhealthyTimeout = UnhealthyTimeout


    def _deserialize(self, params):
        self._EnableActiveCheck = params.get("EnableActiveCheck")
        self._EnablePassiveCheck = params.get("EnablePassiveCheck")
        self._HealthyHttpStatus = params.get("HealthyHttpStatus")
        self._UnhealthyHttpStatus = params.get("UnhealthyHttpStatus")
        self._TcpFailureThreshold = params.get("TcpFailureThreshold")
        self._TimeoutThreshold = params.get("TimeoutThreshold")
        self._HttpFailureThreshold = params.get("HttpFailureThreshold")
        self._ActiveCheckHttpPath = params.get("ActiveCheckHttpPath")
        self._ActiveCheckTimeout = params.get("ActiveCheckTimeout")
        self._ActiveCheckInterval = params.get("ActiveCheckInterval")
        if params.get("ActiveRequestHeader") is not None:
            self._ActiveRequestHeader = []
            for item in params.get("ActiveRequestHeader"):
                obj = UpstreamHealthCheckerReqHeaders()
                obj._deserialize(item)
                self._ActiveRequestHeader.append(obj)
        self._UnhealthyTimeout = params.get("UnhealthyTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
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
        :param _UpstreamId: Unique upstream ID
        :type UpstreamId: str
        :param _UpstreamName: Upstream name
        :type UpstreamName: str
        :param _UpstreamDescription: Upstream description
        :type UpstreamDescription: str
        :param _Scheme: Backend protocol. Valid values: `HTTP`, `HTTPS`
        :type Scheme: str
        :param _Algorithm: Load balancing algorithm. Valid value: `ROUND_ROBIN`
        :type Algorithm: str
        :param _UniqVpcId: Unique VPC ID
        :type UniqVpcId: str
        :param _Retries: Number of retry attempts
        :type Retries: int
        :param _Nodes: Backend nodes
        :type Nodes: list of UpstreamNode
        :param _CreatedTime: Creation time.
        :type CreatedTime: str
        :param _Tags: Label
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        :param _HealthChecker: Health check configuration
Note: This field may return `null`, indicating that no valid value was found.
        :type HealthChecker: :class:`tencentcloud.apigateway.v20180808.models.UpstreamHealthChecker`
        :param _UpstreamType: Upstream type. Valid values: `IP_PORT`, `K8S`
        :type UpstreamType: str
        :param _K8sServices: Configuration of TKE service
Note: This field may return `NULL`, indicating that no valid value was found.
        :type K8sServices: list of K8sService
        :param _UpstreamHost: The Host header that the gateway forwards to the upstream
Note: This field may return `NULL`, indicating that no valid value was found.
        :type UpstreamHost: str
        """
        self._UpstreamId = None
        self._UpstreamName = None
        self._UpstreamDescription = None
        self._Scheme = None
        self._Algorithm = None
        self._UniqVpcId = None
        self._Retries = None
        self._Nodes = None
        self._CreatedTime = None
        self._Tags = None
        self._HealthChecker = None
        self._UpstreamType = None
        self._K8sServices = None
        self._UpstreamHost = None

    @property
    def UpstreamId(self):
        return self._UpstreamId

    @UpstreamId.setter
    def UpstreamId(self, UpstreamId):
        self._UpstreamId = UpstreamId

    @property
    def UpstreamName(self):
        return self._UpstreamName

    @UpstreamName.setter
    def UpstreamName(self, UpstreamName):
        self._UpstreamName = UpstreamName

    @property
    def UpstreamDescription(self):
        return self._UpstreamDescription

    @UpstreamDescription.setter
    def UpstreamDescription(self, UpstreamDescription):
        self._UpstreamDescription = UpstreamDescription

    @property
    def Scheme(self):
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Retries(self):
        return self._Retries

    @Retries.setter
    def Retries(self, Retries):
        self._Retries = Retries

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HealthChecker(self):
        return self._HealthChecker

    @HealthChecker.setter
    def HealthChecker(self, HealthChecker):
        self._HealthChecker = HealthChecker

    @property
    def UpstreamType(self):
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def K8sServices(self):
        return self._K8sServices

    @K8sServices.setter
    def K8sServices(self, K8sServices):
        self._K8sServices = K8sServices

    @property
    def UpstreamHost(self):
        return self._UpstreamHost

    @UpstreamHost.setter
    def UpstreamHost(self, UpstreamHost):
        self._UpstreamHost = UpstreamHost


    def _deserialize(self, params):
        self._UpstreamId = params.get("UpstreamId")
        self._UpstreamName = params.get("UpstreamName")
        self._UpstreamDescription = params.get("UpstreamDescription")
        self._Scheme = params.get("Scheme")
        self._Algorithm = params.get("Algorithm")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Retries = params.get("Retries")
        if params.get("Nodes") is not None:
            self._Nodes = []
            for item in params.get("Nodes"):
                obj = UpstreamNode()
                obj._deserialize(item)
                self._Nodes.append(obj)
        self._CreatedTime = params.get("CreatedTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("HealthChecker") is not None:
            self._HealthChecker = UpstreamHealthChecker()
            self._HealthChecker._deserialize(params.get("HealthChecker"))
        self._UpstreamType = params.get("UpstreamType")
        if params.get("K8sServices") is not None:
            self._K8sServices = []
            for item in params.get("K8sServices"):
                obj = K8sService()
                obj._deserialize(item)
                self._K8sServices.append(obj)
        self._UpstreamHost = params.get("UpstreamHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpstreamNode(AbstractModel):
    """Upstream node metadata

    """

    def __init__(self):
        r"""
        :param _Host: IP or domain name
        :type Host: str
        :param _Port: The port number. Range: [0, 65535]
        :type Port: int
        :param _Weight: Value range: [0, 100]. `0` refers to disable it.
        :type Weight: int
        :param _VmInstanceId: CVM Instance ID
Note: This field may return `NULL`, indicating that no valid value was found.
        :type VmInstanceId: str
        :param _Tags: Tag
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of str
        :param _Healthy: Health status of the node. Values: `OFF`, `HEALTHY`, `UNHEALTHY` and `NO_DATA`. It’s not required for creating and editing actions. It only supports VPC upstreams.
Note: This field may return `NULL`, indicating that no valid value was found.
        :type Healthy: str
        :param _ServiceName: TKE container name
Note: This field may return `NULL`, indicating that no valid value was found.
        :type ServiceName: str
        :param _NameSpace: TKE namespace
Note: This field may return `NULL`, indicating that no valid value was found.
        :type NameSpace: str
        :param _ClusterId: ID of the TKE cluster
Note: This field may return `null`, indicating that no valid value was found.
        :type ClusterId: str
        :param _Source: Node source. Valid value: `K8S`
Note: This field may return `NULL`, indicating that no valid value was found.
        :type Source: str
        :param _UniqueServiceName: The unique service name in API Gateway
Note: This field may return `null`, indicating that no valid value was found.
        :type UniqueServiceName: str
        """
        self._Host = None
        self._Port = None
        self._Weight = None
        self._VmInstanceId = None
        self._Tags = None
        self._Healthy = None
        self._ServiceName = None
        self._NameSpace = None
        self._ClusterId = None
        self._Source = None
        self._UniqueServiceName = None

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def VmInstanceId(self):
        return self._VmInstanceId

    @VmInstanceId.setter
    def VmInstanceId(self, VmInstanceId):
        self._VmInstanceId = VmInstanceId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Healthy(self):
        return self._Healthy

    @Healthy.setter
    def Healthy(self, Healthy):
        self._Healthy = Healthy

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def NameSpace(self):
        return self._NameSpace

    @NameSpace.setter
    def NameSpace(self, NameSpace):
        self._NameSpace = NameSpace

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def UniqueServiceName(self):
        return self._UniqueServiceName

    @UniqueServiceName.setter
    def UniqueServiceName(self, UniqueServiceName):
        self._UniqueServiceName = UniqueServiceName


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._VmInstanceId = params.get("VmInstanceId")
        self._Tags = params.get("Tags")
        self._Healthy = params.get("Healthy")
        self._ServiceName = params.get("ServiceName")
        self._NameSpace = params.get("NameSpace")
        self._ClusterId = params.get("ClusterId")
        self._Source = params.get("Source")
        self._UniqueServiceName = params.get("UniqueServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlan(AbstractModel):
    """`usagePlan` details

    """

    def __init__(self):
        r"""
        :param _Environment: Environment name.
        :type Environment: str
        :param _UsagePlanId: Unique usage plan ID.
        :type UsagePlanId: str
        :param _UsagePlanName: Usage plan name.
        :type UsagePlanName: str
        :param _UsagePlanDesc: Usage plan description.
        :type UsagePlanDesc: str
        :param _MaxRequestNumPreSec: Usage plan QPS. `-1` indicates no limit.
        :type MaxRequestNumPreSec: int
        :param _CreatedTime: Usage plan time.
        :type CreatedTime: str
        :param _ModifiedTime: Usage plan modification time.
        :type ModifiedTime: str
        """
        self._Environment = None
        self._UsagePlanId = None
        self._UsagePlanName = None
        self._UsagePlanDesc = None
        self._MaxRequestNumPreSec = None
        self._CreatedTime = None
        self._ModifiedTime = None

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def UsagePlanName(self):
        return self._UsagePlanName

    @UsagePlanName.setter
    def UsagePlanName(self, UsagePlanName):
        self._UsagePlanName = UsagePlanName

    @property
    def UsagePlanDesc(self):
        return self._UsagePlanDesc

    @UsagePlanDesc.setter
    def UsagePlanDesc(self, UsagePlanDesc):
        self._UsagePlanDesc = UsagePlanDesc

    @property
    def MaxRequestNumPreSec(self):
        return self._MaxRequestNumPreSec

    @MaxRequestNumPreSec.setter
    def MaxRequestNumPreSec(self, MaxRequestNumPreSec):
        self._MaxRequestNumPreSec = MaxRequestNumPreSec

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime


    def _deserialize(self, params):
        self._Environment = params.get("Environment")
        self._UsagePlanId = params.get("UsagePlanId")
        self._UsagePlanName = params.get("UsagePlanName")
        self._UsagePlanDesc = params.get("UsagePlanDesc")
        self._MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanBindEnvironment(AbstractModel):
    """Information of environment bound to usage plan

    """

    def __init__(self):
        r"""
        :param _EnvironmentName: Environment name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnvironmentName: str
        :param _ServiceId: Unique service ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceId: str
        """
        self._EnvironmentName = None
        self._ServiceId = None

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId


    def _deserialize(self, params):
        self._EnvironmentName = params.get("EnvironmentName")
        self._ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanBindSecret(AbstractModel):
    """Key bound to usage plan

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: Key ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccessKeyId: str
        :param _SecretName: Key name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecretName: str
        :param _Status: Key status. 0: disabled. 1: enabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        """
        self._AccessKeyId = None
        self._SecretName = None
        self._Status = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        self._SecretName = params.get("SecretName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanBindSecretStatus(AbstractModel):
    """List of keys bound to usage plan.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of keys bound to usage plan.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _AccessKeyList: List of key details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccessKeyList: list of UsagePlanBindSecret
        """
        self._TotalCount = None
        self._AccessKeyList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccessKeyList(self):
        return self._AccessKeyList

    @AccessKeyList.setter
    def AccessKeyList(self, AccessKeyList):
        self._AccessKeyList = AccessKeyList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AccessKeyList") is not None:
            self._AccessKeyList = []
            for item in params.get("AccessKeyList"):
                obj = UsagePlanBindSecret()
                obj._deserialize(item)
                self._AccessKeyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanEnvironment(AbstractModel):
    """Details of environments bound to usage plan.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Unique ID of bound service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceId: str
        :param _ApiId: Unique API ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiId: str
        :param _ApiName: API name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiName: str
        :param _Path: API path.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Path: str
        :param _Method: API method.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Method: str
        :param _Environment: Name of bound environment.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Environment: str
        :param _InUseRequestNum: Used quota.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InUseRequestNum: int
        :param _MaxRequestNum: Maximum number of requests.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxRequestNum: int
        :param _MaxRequestNumPreSec: Maximum number of requests per second.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxRequestNumPreSec: int
        :param _CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param _ServiceName: Service name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceName: str
        """
        self._ServiceId = None
        self._ApiId = None
        self._ApiName = None
        self._Path = None
        self._Method = None
        self._Environment = None
        self._InUseRequestNum = None
        self._MaxRequestNum = None
        self._MaxRequestNumPreSec = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ServiceName = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def InUseRequestNum(self):
        return self._InUseRequestNum

    @InUseRequestNum.setter
    def InUseRequestNum(self, InUseRequestNum):
        self._InUseRequestNum = InUseRequestNum

    @property
    def MaxRequestNum(self):
        return self._MaxRequestNum

    @MaxRequestNum.setter
    def MaxRequestNum(self, MaxRequestNum):
        self._MaxRequestNum = MaxRequestNum

    @property
    def MaxRequestNumPreSec(self):
        return self._MaxRequestNumPreSec

    @MaxRequestNumPreSec.setter
    def MaxRequestNumPreSec(self, MaxRequestNumPreSec):
        self._MaxRequestNumPreSec = MaxRequestNumPreSec

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        self._ApiName = params.get("ApiName")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        self._Environment = params.get("Environment")
        self._InUseRequestNum = params.get("InUseRequestNum")
        self._MaxRequestNum = params.get("MaxRequestNum")
        self._MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanEnvironmentStatus(AbstractModel):
    """List of environments bound to usage plan.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of environments of the service bound to usage plan.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _EnvironmentList: Environment status of services bound to usage plan.
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnvironmentList: list of UsagePlanEnvironment
        """
        self._TotalCount = None
        self._EnvironmentList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EnvironmentList(self):
        return self._EnvironmentList

    @EnvironmentList.setter
    def EnvironmentList(self, EnvironmentList):
        self._EnvironmentList = EnvironmentList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("EnvironmentList") is not None:
            self._EnvironmentList = []
            for item in params.get("EnvironmentList"):
                obj = UsagePlanEnvironment()
                obj._deserialize(item)
                self._EnvironmentList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanInfo(AbstractModel):
    """Usage plan details.

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: Unique usage plan ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanId: str
        :param _UsagePlanName: Usage plan name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanName: str
        :param _UsagePlanDesc: Usage plan description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanDesc: str
        :param _InitQuota: Number of initialization calls.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InitQuota: int
        :param _MaxRequestNumPreSec: Limit of requests per second.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxRequestNumPreSec: int
        :param _MaxRequestNum: Maximum number of calls.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxRequestNum: int
        :param _IsHide: Whether to hide.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsHide: int
        :param _CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param _BindSecretIdTotalCount: Number of bound keys.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BindSecretIdTotalCount: int
        :param _BindSecretIds: Details of bound keys.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BindSecretIds: list of str
        :param _BindEnvironmentTotalCount: Number of bound environments.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BindEnvironmentTotalCount: int
        :param _BindEnvironments: Details of bound environments.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BindEnvironments: list of UsagePlanBindEnvironment
        """
        self._UsagePlanId = None
        self._UsagePlanName = None
        self._UsagePlanDesc = None
        self._InitQuota = None
        self._MaxRequestNumPreSec = None
        self._MaxRequestNum = None
        self._IsHide = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._BindSecretIdTotalCount = None
        self._BindSecretIds = None
        self._BindEnvironmentTotalCount = None
        self._BindEnvironments = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def UsagePlanName(self):
        return self._UsagePlanName

    @UsagePlanName.setter
    def UsagePlanName(self, UsagePlanName):
        self._UsagePlanName = UsagePlanName

    @property
    def UsagePlanDesc(self):
        return self._UsagePlanDesc

    @UsagePlanDesc.setter
    def UsagePlanDesc(self, UsagePlanDesc):
        self._UsagePlanDesc = UsagePlanDesc

    @property
    def InitQuota(self):
        return self._InitQuota

    @InitQuota.setter
    def InitQuota(self, InitQuota):
        self._InitQuota = InitQuota

    @property
    def MaxRequestNumPreSec(self):
        return self._MaxRequestNumPreSec

    @MaxRequestNumPreSec.setter
    def MaxRequestNumPreSec(self, MaxRequestNumPreSec):
        self._MaxRequestNumPreSec = MaxRequestNumPreSec

    @property
    def MaxRequestNum(self):
        return self._MaxRequestNum

    @MaxRequestNum.setter
    def MaxRequestNum(self, MaxRequestNum):
        self._MaxRequestNum = MaxRequestNum

    @property
    def IsHide(self):
        return self._IsHide

    @IsHide.setter
    def IsHide(self, IsHide):
        self._IsHide = IsHide

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def BindSecretIdTotalCount(self):
        return self._BindSecretIdTotalCount

    @BindSecretIdTotalCount.setter
    def BindSecretIdTotalCount(self, BindSecretIdTotalCount):
        self._BindSecretIdTotalCount = BindSecretIdTotalCount

    @property
    def BindSecretIds(self):
        return self._BindSecretIds

    @BindSecretIds.setter
    def BindSecretIds(self, BindSecretIds):
        self._BindSecretIds = BindSecretIds

    @property
    def BindEnvironmentTotalCount(self):
        return self._BindEnvironmentTotalCount

    @BindEnvironmentTotalCount.setter
    def BindEnvironmentTotalCount(self, BindEnvironmentTotalCount):
        self._BindEnvironmentTotalCount = BindEnvironmentTotalCount

    @property
    def BindEnvironments(self):
        return self._BindEnvironments

    @BindEnvironments.setter
    def BindEnvironments(self, BindEnvironments):
        self._BindEnvironments = BindEnvironments


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        self._UsagePlanName = params.get("UsagePlanName")
        self._UsagePlanDesc = params.get("UsagePlanDesc")
        self._InitQuota = params.get("InitQuota")
        self._MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self._MaxRequestNum = params.get("MaxRequestNum")
        self._IsHide = params.get("IsHide")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._BindSecretIdTotalCount = params.get("BindSecretIdTotalCount")
        self._BindSecretIds = params.get("BindSecretIds")
        self._BindEnvironmentTotalCount = params.get("BindEnvironmentTotalCount")
        if params.get("BindEnvironments") is not None:
            self._BindEnvironments = []
            for item in params.get("BindEnvironments"):
                obj = UsagePlanBindEnvironment()
                obj._deserialize(item)
                self._BindEnvironments.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanStatusInfo(AbstractModel):
    """Usage plan list display.

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: Unique usage plan ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanId: str
        :param _UsagePlanName: Custom usage plan name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanName: str
        :param _UsagePlanDesc: Custom usage plan description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanDesc: str
        :param _MaxRequestNumPreSec: Maximum number of requests per second.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxRequestNumPreSec: int
        :param _MaxRequestNum: Total number of requests allowed. `-1` indicates no limit.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxRequestNum: int
        :param _CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _ModifiedTime: Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        """
        self._UsagePlanId = None
        self._UsagePlanName = None
        self._UsagePlanDesc = None
        self._MaxRequestNumPreSec = None
        self._MaxRequestNum = None
        self._CreatedTime = None
        self._ModifiedTime = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def UsagePlanName(self):
        return self._UsagePlanName

    @UsagePlanName.setter
    def UsagePlanName(self, UsagePlanName):
        self._UsagePlanName = UsagePlanName

    @property
    def UsagePlanDesc(self):
        return self._UsagePlanDesc

    @UsagePlanDesc.setter
    def UsagePlanDesc(self, UsagePlanDesc):
        self._UsagePlanDesc = UsagePlanDesc

    @property
    def MaxRequestNumPreSec(self):
        return self._MaxRequestNumPreSec

    @MaxRequestNumPreSec.setter
    def MaxRequestNumPreSec(self, MaxRequestNumPreSec):
        self._MaxRequestNumPreSec = MaxRequestNumPreSec

    @property
    def MaxRequestNum(self):
        return self._MaxRequestNum

    @MaxRequestNum.setter
    def MaxRequestNum(self, MaxRequestNum):
        self._MaxRequestNum = MaxRequestNum

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        self._UsagePlanName = params.get("UsagePlanName")
        self._UsagePlanDesc = params.get("UsagePlanDesc")
        self._MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self._MaxRequestNum = params.get("MaxRequestNum")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlansStatus(AbstractModel):
    """Usage plan list

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible usage plans.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _UsagePlanStatusSet: Usage plan list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsagePlanStatusSet: list of UsagePlanStatusInfo
        """
        self._TotalCount = None
        self._UsagePlanStatusSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UsagePlanStatusSet(self):
        return self._UsagePlanStatusSet

    @UsagePlanStatusSet.setter
    def UsagePlanStatusSet(self, UsagePlanStatusSet):
        self._UsagePlanStatusSet = UsagePlanStatusSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("UsagePlanStatusSet") is not None:
            self._UsagePlanStatusSet = []
            for item in params.get("UsagePlanStatusSet"):
                obj = UsagePlanStatusInfo()
                obj._deserialize(item)
                self._UsagePlanStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        