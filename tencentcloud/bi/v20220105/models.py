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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class ApiDatasourceConfig(AbstractModel):
    r"""API data source connection configuration

    """

    def __init__(self):
        r"""
        :param _FieldsJsonData: API data source parsing result
Note: This field may return null, indicating that no valid values can be obtained.
        :type FieldsJsonData: str
        :param _ConnectionType: Connection Type 1: Direct Connection 2: Extraction
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConnectionType: int
        :param _FrequencyConfig: Extraction frequency configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type FrequencyConfig: :class:`tencentcloud.bi.v20220105.models.FrequencyConfig`
        :param _Url: Request URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type Url: str
        :param _RequestMethod: 1:GET 2:POST
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestMethod: int
        :param _RequestHeader: Request headers
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestHeader: str
        :param _RequestParams: Request parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestParams: str
        :param _RequestBody: request body
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestBody: str
        :param _UserName: Username.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _Password: Password.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Password: str
        :param _AuthorizationType: Valid values: 1: no authentication; 2: BASIC_AUTH.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuthorizationType: int
        :param _TableId: Table ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableId: int
        :param _JsonPathDbNameMap: Mapping path DbName
Note: This field may return null, indicating that no valid values can be obtained.
        :type JsonPathDbNameMap: str
        :param _AuthApi: Authentication API
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuthApi: str
        :param _AppKey: Application Key
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppKey: str
        :param _AppSecret: application key
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppSecret: str
        :param _SecretKey: Data Key
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param _SecretIv: Data key initialization vector
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecretIv: str
        """
        self._FieldsJsonData = None
        self._ConnectionType = None
        self._FrequencyConfig = None
        self._Url = None
        self._RequestMethod = None
        self._RequestHeader = None
        self._RequestParams = None
        self._RequestBody = None
        self._UserName = None
        self._Password = None
        self._AuthorizationType = None
        self._TableId = None
        self._JsonPathDbNameMap = None
        self._AuthApi = None
        self._AppKey = None
        self._AppSecret = None
        self._SecretKey = None
        self._SecretIv = None

    @property
    def FieldsJsonData(self):
        r"""API data source parsing result
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FieldsJsonData

    @FieldsJsonData.setter
    def FieldsJsonData(self, FieldsJsonData):
        self._FieldsJsonData = FieldsJsonData

    @property
    def ConnectionType(self):
        r"""Connection Type 1: Direct Connection 2: Extraction
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ConnectionType

    @ConnectionType.setter
    def ConnectionType(self, ConnectionType):
        self._ConnectionType = ConnectionType

    @property
    def FrequencyConfig(self):
        r"""Extraction frequency configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.FrequencyConfig`
        """
        return self._FrequencyConfig

    @FrequencyConfig.setter
    def FrequencyConfig(self, FrequencyConfig):
        self._FrequencyConfig = FrequencyConfig

    @property
    def Url(self):
        r"""Request URL
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RequestMethod(self):
        r"""1:GET 2:POST
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RequestMethod

    @RequestMethod.setter
    def RequestMethod(self, RequestMethod):
        self._RequestMethod = RequestMethod

    @property
    def RequestHeader(self):
        r"""Request headers
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader

    @property
    def RequestParams(self):
        r"""Request parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RequestParams

    @RequestParams.setter
    def RequestParams(self, RequestParams):
        self._RequestParams = RequestParams

    @property
    def RequestBody(self):
        r"""request body
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RequestBody

    @RequestBody.setter
    def RequestBody(self, RequestBody):
        self._RequestBody = RequestBody

    @property
    def UserName(self):
        r"""Username.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""Password.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def AuthorizationType(self):
        r"""Valid values: 1: no authentication; 2: BASIC_AUTH.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AuthorizationType

    @AuthorizationType.setter
    def AuthorizationType(self, AuthorizationType):
        self._AuthorizationType = AuthorizationType

    @property
    def TableId(self):
        r"""Table ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def JsonPathDbNameMap(self):
        r"""Mapping path DbName
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JsonPathDbNameMap

    @JsonPathDbNameMap.setter
    def JsonPathDbNameMap(self, JsonPathDbNameMap):
        self._JsonPathDbNameMap = JsonPathDbNameMap

    @property
    def AuthApi(self):
        r"""Authentication API
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AuthApi

    @AuthApi.setter
    def AuthApi(self, AuthApi):
        self._AuthApi = AuthApi

    @property
    def AppKey(self):
        r"""Application Key
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def AppSecret(self):
        r"""application key
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppSecret

    @AppSecret.setter
    def AppSecret(self, AppSecret):
        self._AppSecret = AppSecret

    @property
    def SecretKey(self):
        r"""Data Key
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def SecretIv(self):
        r"""Data key initialization vector
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SecretIv

    @SecretIv.setter
    def SecretIv(self, SecretIv):
        self._SecretIv = SecretIv


    def _deserialize(self, params):
        self._FieldsJsonData = params.get("FieldsJsonData")
        self._ConnectionType = params.get("ConnectionType")
        if params.get("FrequencyConfig") is not None:
            self._FrequencyConfig = FrequencyConfig()
            self._FrequencyConfig._deserialize(params.get("FrequencyConfig"))
        self._Url = params.get("Url")
        self._RequestMethod = params.get("RequestMethod")
        self._RequestHeader = params.get("RequestHeader")
        self._RequestParams = params.get("RequestParams")
        self._RequestBody = params.get("RequestBody")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._AuthorizationType = params.get("AuthorizationType")
        self._TableId = params.get("TableId")
        self._JsonPathDbNameMap = params.get("JsonPathDbNameMap")
        self._AuthApi = params.get("AuthApi")
        self._AppKey = params.get("AppKey")
        self._AppSecret = params.get("AppSecret")
        self._SecretKey = params.get("SecretKey")
        self._SecretIv = params.get("SecretIv")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyEmbedIntervalRequest(AbstractModel):
    r"""ApplyEmbedInterval request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Shares the project ID.
        :type ProjectId: int
        :param _PageId: Shares the page ID. This field is empty (0) for embedding a dashboard and is not passed for embedding ChatBI.

        :type PageId: int
        :param _BIToken: Token requiring extension.
        :type BIToken: str
        :param _ExtraParam: Alternate field.
        :type ExtraParam: str
        :param _Intention: embed: page/dashboard embedding.
chatBIEmbed: ChatBI embedding.
        :type Intention: str
        :param _Scope: panel: dashboard; page: page.
project, during ChatBI embedding.
        :type Scope: str
        """
        self._ProjectId = None
        self._PageId = None
        self._BIToken = None
        self._ExtraParam = None
        self._Intention = None
        self._Scope = None

    @property
    def ProjectId(self):
        r"""Shares the project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageId(self):
        r"""Shares the page ID. This field is empty (0) for embedding a dashboard and is not passed for embedding ChatBI.

        :rtype: int
        """
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def BIToken(self):
        r"""Token requiring extension.
        :rtype: str
        """
        return self._BIToken

    @BIToken.setter
    def BIToken(self, BIToken):
        self._BIToken = BIToken

    @property
    def ExtraParam(self):
        r"""Alternate field.
        :rtype: str
        """
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def Intention(self):
        r"""embed: page/dashboard embedding.
chatBIEmbed: ChatBI embedding.
        :rtype: str
        """
        return self._Intention

    @Intention.setter
    def Intention(self, Intention):
        self._Intention = Intention

    @property
    def Scope(self):
        r"""panel: dashboard; page: page.
project, during ChatBI embedding.
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageId = params.get("PageId")
        self._BIToken = params.get("BIToken")
        self._ExtraParam = params.get("ExtraParam")
        self._Intention = params.get("Intention")
        self._Scope = params.get("Scope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyEmbedIntervalResponse(AbstractModel):
    r"""ApplyEmbedInterval response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Additional parameters.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Data: Result data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.ApplyEmbedTokenInfo`
        :param _Msg: Result description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Additional parameters.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        r"""Result data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ApplyEmbedTokenInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Msg(self):
        r"""Result description.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = ApplyEmbedTokenInfo()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ApplyEmbedTokenInfo(AbstractModel):
    r"""Token deferral request

    """

    def __init__(self):
        r"""
        :param _Result: Request result.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        """
        self._Result = None

    @property
    def Result(self):
        r"""Request result.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaseStateAction(AbstractModel):
    r"""Operation attributes of every record returned by a list query

    """

    def __init__(self):
        r"""
        :param _ShowEdit: Whether the edit button is visible.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ShowEdit: bool
        :param _IsEdit: Whether the edit button is clickable.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsEdit: bool
        :param _EditText: Edit button text.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EditText: str
        :param _EditTips: Edit-disabled hint.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EditTips: str
        :param _ShowDel: Whether the deletion button is visible.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ShowDel: bool
        :param _IsDel: Whether the deletion button is clickable.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDel: bool
        :param _DelText: Delete button text.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DelText: str
        :param _DelTips: Delete-disabled hint.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DelTips: str
        :param _ShowCopy: Whether the copy button is visible.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ShowCopy: bool
        :param _ShowView: Whether it is visible.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ShowView: bool
        :param _ShowRename: Whether renaming is allowed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ShowRename: bool
        """
        self._ShowEdit = None
        self._IsEdit = None
        self._EditText = None
        self._EditTips = None
        self._ShowDel = None
        self._IsDel = None
        self._DelText = None
        self._DelTips = None
        self._ShowCopy = None
        self._ShowView = None
        self._ShowRename = None

    @property
    def ShowEdit(self):
        r"""Whether the edit button is visible.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._ShowEdit

    @ShowEdit.setter
    def ShowEdit(self, ShowEdit):
        self._ShowEdit = ShowEdit

    @property
    def IsEdit(self):
        r"""Whether the edit button is clickable.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsEdit

    @IsEdit.setter
    def IsEdit(self, IsEdit):
        self._IsEdit = IsEdit

    @property
    def EditText(self):
        r"""Edit button text.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EditText

    @EditText.setter
    def EditText(self, EditText):
        self._EditText = EditText

    @property
    def EditTips(self):
        r"""Edit-disabled hint.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EditTips

    @EditTips.setter
    def EditTips(self, EditTips):
        self._EditTips = EditTips

    @property
    def ShowDel(self):
        r"""Whether the deletion button is visible.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._ShowDel

    @ShowDel.setter
    def ShowDel(self, ShowDel):
        self._ShowDel = ShowDel

    @property
    def IsDel(self):
        r"""Whether the deletion button is clickable.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsDel

    @IsDel.setter
    def IsDel(self, IsDel):
        self._IsDel = IsDel

    @property
    def DelText(self):
        r"""Delete button text.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DelText

    @DelText.setter
    def DelText(self, DelText):
        self._DelText = DelText

    @property
    def DelTips(self):
        r"""Delete-disabled hint.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DelTips

    @DelTips.setter
    def DelTips(self, DelTips):
        self._DelTips = DelTips

    @property
    def ShowCopy(self):
        r"""Whether the copy button is visible.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._ShowCopy

    @ShowCopy.setter
    def ShowCopy(self, ShowCopy):
        self._ShowCopy = ShowCopy

    @property
    def ShowView(self):
        r"""Whether it is visible.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._ShowView

    @ShowView.setter
    def ShowView(self, ShowView):
        self._ShowView = ShowView

    @property
    def ShowRename(self):
        r"""Whether renaming is allowed.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._ShowRename

    @ShowRename.setter
    def ShowRename(self, ShowRename):
        self._ShowRename = ShowRename


    def _deserialize(self, params):
        self._ShowEdit = params.get("ShowEdit")
        self._IsEdit = params.get("IsEdit")
        self._EditText = params.get("EditText")
        self._EditTips = params.get("EditTips")
        self._ShowDel = params.get("ShowDel")
        self._IsDel = params.get("IsDel")
        self._DelText = params.get("DelText")
        self._DelTips = params.get("DelTips")
        self._ShowCopy = params.get("ShowCopy")
        self._ShowView = params.get("ShowView")
        self._ShowRename = params.get("ShowRename")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearEmbedTokenRequest(AbstractModel):
    r"""ClearEmbedToken request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _UserCorpId: Host Account ID
        :type UserCorpId: str
        :param _Scope: panel , page
        :type Scope: str
        :param _PageId: page id
        :type PageId: str
        """
        self._ProjectId = None
        self._UserCorpId = None
        self._Scope = None
        self._PageId = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def UserCorpId(self):
        r"""Host Account ID
        :rtype: str
        """
        return self._UserCorpId

    @UserCorpId.setter
    def UserCorpId(self, UserCorpId):
        self._UserCorpId = UserCorpId

    @property
    def Scope(self):
        r"""panel , page
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def PageId(self):
        r"""page id
        :rtype: str
        """
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._UserCorpId = params.get("UserCorpId")
        self._Scope = params.get("Scope")
        self._PageId = params.get("PageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearEmbedTokenResponse(AbstractModel):
    r"""ClearEmbedToken response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Additional message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: Prompt message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _Data: Result
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Msg = None
        self._Data = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Additional message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Prompt message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Data(self):
        r"""Result
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class CorpUserListData(AbstractModel):
    r"""Enterprise user list

    """

    def __init__(self):
        r"""
        :param _List: List.
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of UserIdAndUserName
        :param _Total: Total number.
        :type Total: int
        :param _TotalPages: Number of pages.
        :type TotalPages: int
        """
        self._List = None
        self._Total = None
        self._TotalPages = None

    @property
    def List(self):
        r"""List.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of UserIdAndUserName
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        r"""Total number.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalPages(self):
        r"""Number of pages.
        :rtype: int
        """
        return self._TotalPages

    @TotalPages.setter
    def TotalPages(self, TotalPages):
        self._TotalPages = TotalPages


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = UserIdAndUserName()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._TotalPages = params.get("TotalPages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCorpTagRequest(AbstractModel):
    r"""CreateCorpTag request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Tag name
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        r"""Tag name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCorpTagResponse(AbstractModel):
    r"""CreateCorpTag response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _Data: Data.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.DataId`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Msg = None
        self._Data = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Data(self):
        r"""Data.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.DataId`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        if params.get("Data") is not None:
            self._Data = DataId()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateDataTableRequest(AbstractModel):
    r"""CreateDataTable request structure.

    """

    def __init__(self):
        r"""
        :param _Type: The backend provides a dictionary: table type, 1. database table creation, 2. SQL table creation, 3. Excel upload, 4. API connection, 5. Tencent documentation, 6. cloud database, 7. manually enter, 8. join query.
        :type Type: int
        :param _Name: Data table name
        :type Name: str
        :param _ProjectId: None.
        :type ProjectId: int
        :param _FoldId: folder
        :type FoldId: int
        :param _DatasourceId: data source Id
        :type DatasourceId: str
        :param _TableName: physical table name
        :type TableName: str
        :param _Sql: sql statement
        :type Sql: str
        :param _ExcelUrl: excel address
        :type ExcelUrl: str
        :param _Fields: configure field
        :type Fields: list of TableField
        :param _TableNodeType: Multi-table join usage: 1: Data source original table, 2: Local table, 3: Excel table, 4: API table
        :type TableNodeType: int
        :param _Tables: Original table information for multi-table join
        :type Tables: list of JoinSourceTable
        :param _Joins: Multi-table join association information
        :type Joins: list of JoinRelation
        :param _ExtInfo: Additional info, such as api data source info and Tencent document access info
        :type ExtInfo: str
        :param _AsyncRequest: whether
        :type AsyncRequest: bool
        :param _ParentTranId: dependent async transaction id
        :type ParentTranId: str
        :param _ApiDatasourceConfig: API data source configuration
        :type ApiDatasourceConfig: :class:`tencentcloud.bi.v20220105.models.ApiDatasourceConfig`
        :param _ParamList: 1
        :type ParamList: list of ParamCreateDTO
        :param _DlcExtInfo: dlc advanced parameter
        :type DlcExtInfo: str
        :param _QueryDbData: Query database required or not
        :type QueryDbData: str
        :param _TableComment: Table remark
        :type TableComment: str
        :param _QueryFieldRemark: Whether to query field remarks
        :type QueryFieldRemark: int
        :param _FieldRemarkList: Field remarks list
        :type FieldRemarkList: list of FieldRemarkDTO
        """
        self._Type = None
        self._Name = None
        self._ProjectId = None
        self._FoldId = None
        self._DatasourceId = None
        self._TableName = None
        self._Sql = None
        self._ExcelUrl = None
        self._Fields = None
        self._TableNodeType = None
        self._Tables = None
        self._Joins = None
        self._ExtInfo = None
        self._AsyncRequest = None
        self._ParentTranId = None
        self._ApiDatasourceConfig = None
        self._ParamList = None
        self._DlcExtInfo = None
        self._QueryDbData = None
        self._TableComment = None
        self._QueryFieldRemark = None
        self._FieldRemarkList = None

    @property
    def Type(self):
        r"""The backend provides a dictionary: table type, 1. database table creation, 2. SQL table creation, 3. Excel upload, 4. API connection, 5. Tencent documentation, 6. cloud database, 7. manually enter, 8. join query.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        r"""Data table name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProjectId(self):
        r"""None.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FoldId(self):
        r"""folder
        :rtype: int
        """
        return self._FoldId

    @FoldId.setter
    def FoldId(self, FoldId):
        self._FoldId = FoldId

    @property
    def DatasourceId(self):
        r"""data source Id
        :rtype: str
        """
        return self._DatasourceId

    @DatasourceId.setter
    def DatasourceId(self, DatasourceId):
        self._DatasourceId = DatasourceId

    @property
    def TableName(self):
        r"""physical table name
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Sql(self):
        r"""sql statement
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def ExcelUrl(self):
        r"""excel address
        :rtype: str
        """
        return self._ExcelUrl

    @ExcelUrl.setter
    def ExcelUrl(self, ExcelUrl):
        self._ExcelUrl = ExcelUrl

    @property
    def Fields(self):
        r"""configure field
        :rtype: list of TableField
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def TableNodeType(self):
        r"""Multi-table join usage: 1: Data source original table, 2: Local table, 3: Excel table, 4: API table
        :rtype: int
        """
        return self._TableNodeType

    @TableNodeType.setter
    def TableNodeType(self, TableNodeType):
        self._TableNodeType = TableNodeType

    @property
    def Tables(self):
        r"""Original table information for multi-table join
        :rtype: list of JoinSourceTable
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def Joins(self):
        r"""Multi-table join association information
        :rtype: list of JoinRelation
        """
        return self._Joins

    @Joins.setter
    def Joins(self, Joins):
        self._Joins = Joins

    @property
    def ExtInfo(self):
        r"""Additional info, such as api data source info and Tencent document access info
        :rtype: str
        """
        return self._ExtInfo

    @ExtInfo.setter
    def ExtInfo(self, ExtInfo):
        self._ExtInfo = ExtInfo

    @property
    def AsyncRequest(self):
        r"""whether
        :rtype: bool
        """
        return self._AsyncRequest

    @AsyncRequest.setter
    def AsyncRequest(self, AsyncRequest):
        self._AsyncRequest = AsyncRequest

    @property
    def ParentTranId(self):
        r"""dependent async transaction id
        :rtype: str
        """
        return self._ParentTranId

    @ParentTranId.setter
    def ParentTranId(self, ParentTranId):
        self._ParentTranId = ParentTranId

    @property
    def ApiDatasourceConfig(self):
        r"""API data source configuration
        :rtype: :class:`tencentcloud.bi.v20220105.models.ApiDatasourceConfig`
        """
        return self._ApiDatasourceConfig

    @ApiDatasourceConfig.setter
    def ApiDatasourceConfig(self, ApiDatasourceConfig):
        self._ApiDatasourceConfig = ApiDatasourceConfig

    @property
    def ParamList(self):
        r"""1
        :rtype: list of ParamCreateDTO
        """
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def DlcExtInfo(self):
        r"""dlc advanced parameter
        :rtype: str
        """
        return self._DlcExtInfo

    @DlcExtInfo.setter
    def DlcExtInfo(self, DlcExtInfo):
        self._DlcExtInfo = DlcExtInfo

    @property
    def QueryDbData(self):
        r"""Query database required or not
        :rtype: str
        """
        return self._QueryDbData

    @QueryDbData.setter
    def QueryDbData(self, QueryDbData):
        self._QueryDbData = QueryDbData

    @property
    def TableComment(self):
        r"""Table remark
        :rtype: str
        """
        return self._TableComment

    @TableComment.setter
    def TableComment(self, TableComment):
        self._TableComment = TableComment

    @property
    def QueryFieldRemark(self):
        r"""Whether to query field remarks
        :rtype: int
        """
        return self._QueryFieldRemark

    @QueryFieldRemark.setter
    def QueryFieldRemark(self, QueryFieldRemark):
        self._QueryFieldRemark = QueryFieldRemark

    @property
    def FieldRemarkList(self):
        r"""Field remarks list
        :rtype: list of FieldRemarkDTO
        """
        return self._FieldRemarkList

    @FieldRemarkList.setter
    def FieldRemarkList(self, FieldRemarkList):
        self._FieldRemarkList = FieldRemarkList


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._ProjectId = params.get("ProjectId")
        self._FoldId = params.get("FoldId")
        self._DatasourceId = params.get("DatasourceId")
        self._TableName = params.get("TableName")
        self._Sql = params.get("Sql")
        self._ExcelUrl = params.get("ExcelUrl")
        if params.get("Fields") is not None:
            self._Fields = []
            for item in params.get("Fields"):
                obj = TableField()
                obj._deserialize(item)
                self._Fields.append(obj)
        self._TableNodeType = params.get("TableNodeType")
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = JoinSourceTable()
                obj._deserialize(item)
                self._Tables.append(obj)
        if params.get("Joins") is not None:
            self._Joins = []
            for item in params.get("Joins"):
                obj = JoinRelation()
                obj._deserialize(item)
                self._Joins.append(obj)
        self._ExtInfo = params.get("ExtInfo")
        self._AsyncRequest = params.get("AsyncRequest")
        self._ParentTranId = params.get("ParentTranId")
        if params.get("ApiDatasourceConfig") is not None:
            self._ApiDatasourceConfig = ApiDatasourceConfig()
            self._ApiDatasourceConfig._deserialize(params.get("ApiDatasourceConfig"))
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ParamCreateDTO()
                obj._deserialize(item)
                self._ParamList.append(obj)
        self._DlcExtInfo = params.get("DlcExtInfo")
        self._QueryDbData = params.get("QueryDbData")
        self._TableComment = params.get("TableComment")
        self._QueryFieldRemark = params.get("QueryFieldRemark")
        if params.get("FieldRemarkList") is not None:
            self._FieldRemarkList = []
            for item in params.get("FieldRemarkList"):
                obj = FieldRemarkDTO()
                obj._deserialize(item)
                self._FieldRemarkList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataTableResponse(AbstractModel):
    r"""CreateDataTable response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Data: Returned data table id on success
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.IdDTO`
        :param _Extra: Additional Information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: Error prompt
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Data = None
        self._Extra = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Data(self):
        r"""Returned data table id on success
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.IdDTO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Extra(self):
        r"""Additional Information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Error prompt
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        if params.get("Data") is not None:
            self._Data = IdDTO()
            self._Data._deserialize(params.get("Data"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateDatasourceCloudRequest(AbstractModel):
    r"""CreateDatasourceCloud request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceType: The backend provides dictionaries: domain type. 1. Tencent Cloud, 2. local.
        :type ServiceType: str
        :param _DbType: Drive.
Value range:.
MYSQL: MYSQL database.
PRESTO: presto database.
POSTGRE: PostgreSQL database.
DLC: dlc database.
MSSQL: microsoft SQL Server database.
        :type DbType: str
        :param _Charset: Database encoding.
        :type Charset: str
        :param _DbUser: Username.
        :type DbUser: str
        :param _DbPwd: Password.
        :type DbPwd: str
        :param _DbName: Database name.
        :type DbName: str
        :param _SourceName: Database alias.
        :type SourceName: str
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _Vip: Private network IP address of the public cloud.
        :type Vip: str
        :param _Vport: Private network port of the public cloud.
        :type Vport: str
        :param _VpcId: VPC identifier.
        :type VpcId: str
        :param _UniqVpcId: Unified VPC identifier.
        :type UniqVpcId: str
        :param _RegionId: Region identifier (gz, bj).
        :type RegionId: str
        :param _ExtraParam: Extension parameter.
        :type ExtraParam: str
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _ProdDbName: Product name of the data source.
        :type ProdDbName: str
        :param _DataOrigin: Third-party data source identifier.
        :type DataOrigin: str
        :param _DataOriginProjectId: Third-party project ID.
        :type DataOriginProjectId: str
        :param _DataOriginDatasourceId: Third-party data source ID.
        :type DataOriginDatasourceId: str
        :param _ClusterId: Cluster ID.
        :type ClusterId: str
        :param _Schema: Database schema.
        :type Schema: str
        :param _DbVersion: Database version.
        :type DbVersion: str
        """
        self._ServiceType = None
        self._DbType = None
        self._Charset = None
        self._DbUser = None
        self._DbPwd = None
        self._DbName = None
        self._SourceName = None
        self._ProjectId = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None
        self._UniqVpcId = None
        self._RegionId = None
        self._ExtraParam = None
        self._InstanceId = None
        self._ProdDbName = None
        self._DataOrigin = None
        self._DataOriginProjectId = None
        self._DataOriginDatasourceId = None
        self._ClusterId = None
        self._Schema = None
        self._DbVersion = None

    @property
    def ServiceType(self):
        r"""The backend provides dictionaries: domain type. 1. Tencent Cloud, 2. local.
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def DbType(self):
        r"""Drive.
Value range:.
MYSQL: MYSQL database.
PRESTO: presto database.
POSTGRE: PostgreSQL database.
DLC: dlc database.
MSSQL: microsoft SQL Server database.
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Charset(self):
        r"""Database encoding.
        :rtype: str
        """
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def DbUser(self):
        r"""Username.
        :rtype: str
        """
        return self._DbUser

    @DbUser.setter
    def DbUser(self, DbUser):
        self._DbUser = DbUser

    @property
    def DbPwd(self):
        r"""Password.
        :rtype: str
        """
        return self._DbPwd

    @DbPwd.setter
    def DbPwd(self, DbPwd):
        self._DbPwd = DbPwd

    @property
    def DbName(self):
        r"""Database name.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SourceName(self):
        r"""Database alias.
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Vip(self):
        r"""Private network IP address of the public cloud.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""Private network port of the public cloud.
        :rtype: str
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        r"""VPC identifier.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def UniqVpcId(self):
        r"""Unified VPC identifier.
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def RegionId(self):
        r"""Region identifier (gz, bj).
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ExtraParam(self):
        r"""Extension parameter.
        :rtype: str
        """
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProdDbName(self):
        r"""Product name of the data source.
        :rtype: str
        """
        return self._ProdDbName

    @ProdDbName.setter
    def ProdDbName(self, ProdDbName):
        self._ProdDbName = ProdDbName

    @property
    def DataOrigin(self):
        r"""Third-party data source identifier.
        :rtype: str
        """
        return self._DataOrigin

    @DataOrigin.setter
    def DataOrigin(self, DataOrigin):
        self._DataOrigin = DataOrigin

    @property
    def DataOriginProjectId(self):
        r"""Third-party project ID.
        :rtype: str
        """
        return self._DataOriginProjectId

    @DataOriginProjectId.setter
    def DataOriginProjectId(self, DataOriginProjectId):
        self._DataOriginProjectId = DataOriginProjectId

    @property
    def DataOriginDatasourceId(self):
        r"""Third-party data source ID.
        :rtype: str
        """
        return self._DataOriginDatasourceId

    @DataOriginDatasourceId.setter
    def DataOriginDatasourceId(self, DataOriginDatasourceId):
        self._DataOriginDatasourceId = DataOriginDatasourceId

    @property
    def ClusterId(self):
        r"""Cluster ID.
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Schema(self):
        r"""Database schema.
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def DbVersion(self):
        r"""Database version.
        :rtype: str
        """
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._DbType = params.get("DbType")
        self._Charset = params.get("Charset")
        self._DbUser = params.get("DbUser")
        self._DbPwd = params.get("DbPwd")
        self._DbName = params.get("DbName")
        self._SourceName = params.get("SourceName")
        self._ProjectId = params.get("ProjectId")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._RegionId = params.get("RegionId")
        self._ExtraParam = params.get("ExtraParam")
        self._InstanceId = params.get("InstanceId")
        self._ProdDbName = params.get("ProdDbName")
        self._DataOrigin = params.get("DataOrigin")
        self._DataOriginProjectId = params.get("DataOriginProjectId")
        self._DataOriginDatasourceId = params.get("DataOriginDatasourceId")
        self._ClusterId = params.get("ClusterId")
        self._Schema = params.get("Schema")
        self._DbVersion = params.get("DbVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatasourceCloudResponse(AbstractModel):
    r"""CreateDatasourceCloud response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Data: Success No.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.IdDTO`
        :param _Extra: Additional information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: Prompt.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Data = None
        self._Extra = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Data(self):
        r"""Success No.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.IdDTO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Extra(self):
        r"""Additional information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Prompt.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        if params.get("Data") is not None:
            self._Data = IdDTO()
            self._Data._deserialize(params.get("Data"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateDatasourceRequest(AbstractModel):
    r"""CreateDatasource request structure.

    """

    def __init__(self):
        r"""
        :param _DbHost: HOST
        :type DbHost: str
        :param _DbPort: Port.
        :type DbPort: int
        :param _ServiceType: The backend provides dictionaries: domain type. 1. Tencent Cloud, 2. local.
        :type ServiceType: str
        :param _DbType: Drive.
Value range:.
MYSQL: MYSQL database.
PRESTO: presto database.
POSTGRE: PostgreSQL database.
DLC: dlc database.
MSSQL: microsoft SQL Server database.
        :type DbType: str
        :param _Charset: Database encoding.
        :type Charset: str
        :param _DbUser: Username.
        :type DbUser: str
        :param _DbPwd: Password.
        :type DbPwd: str
        :param _DbName: Database name.
        :type DbName: str
        :param _SourceName: Database alias.
        :type SourceName: str
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _Catalog: Catalog value.
        :type Catalog: str
        :param _DataOrigin: Third-party data source identifier.
        :type DataOrigin: str
        :param _DataOriginProjectId: Third-party project ID.
        :type DataOriginProjectId: str
        :param _DataOriginDatasourceId: Third-party data source ID.
        :type DataOriginDatasourceId: str
        :param _ExtraParam: Extension parameter.
        :type ExtraParam: str
        :param _UniqVpcId: Unified identifier of the Tencent Cloud VPC.
        :type UniqVpcId: str
        :param _Vip: VPC IP address.
        :type Vip: str
        :param _Vport: VPC port.
        :type Vport: str
        :param _VpcId: Tencent Cloud VPC identifier.
        :type VpcId: str
        :param _OperationAuthLimit: Operation permission limitation.
        :type OperationAuthLimit: list of str
        :param _UseVPC: Enables VPC.
        :type UseVPC: bool
        :param _RegionId: Region.
        :type RegionId: str
        :param _Schema: Database schema.
        :type Schema: str
        :param _DbVersion: Database version.
        :type DbVersion: str
        """
        self._DbHost = None
        self._DbPort = None
        self._ServiceType = None
        self._DbType = None
        self._Charset = None
        self._DbUser = None
        self._DbPwd = None
        self._DbName = None
        self._SourceName = None
        self._ProjectId = None
        self._Catalog = None
        self._DataOrigin = None
        self._DataOriginProjectId = None
        self._DataOriginDatasourceId = None
        self._ExtraParam = None
        self._UniqVpcId = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None
        self._OperationAuthLimit = None
        self._UseVPC = None
        self._RegionId = None
        self._Schema = None
        self._DbVersion = None

    @property
    def DbHost(self):
        r"""HOST
        :rtype: str
        """
        return self._DbHost

    @DbHost.setter
    def DbHost(self, DbHost):
        self._DbHost = DbHost

    @property
    def DbPort(self):
        r"""Port.
        :rtype: int
        """
        return self._DbPort

    @DbPort.setter
    def DbPort(self, DbPort):
        self._DbPort = DbPort

    @property
    def ServiceType(self):
        r"""The backend provides dictionaries: domain type. 1. Tencent Cloud, 2. local.
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def DbType(self):
        r"""Drive.
Value range:.
MYSQL: MYSQL database.
PRESTO: presto database.
POSTGRE: PostgreSQL database.
DLC: dlc database.
MSSQL: microsoft SQL Server database.
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Charset(self):
        r"""Database encoding.
        :rtype: str
        """
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def DbUser(self):
        r"""Username.
        :rtype: str
        """
        return self._DbUser

    @DbUser.setter
    def DbUser(self, DbUser):
        self._DbUser = DbUser

    @property
    def DbPwd(self):
        r"""Password.
        :rtype: str
        """
        return self._DbPwd

    @DbPwd.setter
    def DbPwd(self, DbPwd):
        self._DbPwd = DbPwd

    @property
    def DbName(self):
        r"""Database name.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SourceName(self):
        r"""Database alias.
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Catalog(self):
        r"""Catalog value.
        :rtype: str
        """
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def DataOrigin(self):
        r"""Third-party data source identifier.
        :rtype: str
        """
        return self._DataOrigin

    @DataOrigin.setter
    def DataOrigin(self, DataOrigin):
        self._DataOrigin = DataOrigin

    @property
    def DataOriginProjectId(self):
        r"""Third-party project ID.
        :rtype: str
        """
        return self._DataOriginProjectId

    @DataOriginProjectId.setter
    def DataOriginProjectId(self, DataOriginProjectId):
        self._DataOriginProjectId = DataOriginProjectId

    @property
    def DataOriginDatasourceId(self):
        r"""Third-party data source ID.
        :rtype: str
        """
        return self._DataOriginDatasourceId

    @DataOriginDatasourceId.setter
    def DataOriginDatasourceId(self, DataOriginDatasourceId):
        self._DataOriginDatasourceId = DataOriginDatasourceId

    @property
    def ExtraParam(self):
        r"""Extension parameter.
        :rtype: str
        """
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def UniqVpcId(self):
        r"""Unified identifier of the Tencent Cloud VPC.
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Vip(self):
        r"""VPC IP address.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""VPC port.
        :rtype: str
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        r"""Tencent Cloud VPC identifier.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def OperationAuthLimit(self):
        r"""Operation permission limitation.
        :rtype: list of str
        """
        return self._OperationAuthLimit

    @OperationAuthLimit.setter
    def OperationAuthLimit(self, OperationAuthLimit):
        self._OperationAuthLimit = OperationAuthLimit

    @property
    def UseVPC(self):
        r"""Enables VPC.
        :rtype: bool
        """
        return self._UseVPC

    @UseVPC.setter
    def UseVPC(self, UseVPC):
        self._UseVPC = UseVPC

    @property
    def RegionId(self):
        r"""Region.
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Schema(self):
        r"""Database schema.
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def DbVersion(self):
        r"""Database version.
        :rtype: str
        """
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion


    def _deserialize(self, params):
        self._DbHost = params.get("DbHost")
        self._DbPort = params.get("DbPort")
        self._ServiceType = params.get("ServiceType")
        self._DbType = params.get("DbType")
        self._Charset = params.get("Charset")
        self._DbUser = params.get("DbUser")
        self._DbPwd = params.get("DbPwd")
        self._DbName = params.get("DbName")
        self._SourceName = params.get("SourceName")
        self._ProjectId = params.get("ProjectId")
        self._Catalog = params.get("Catalog")
        self._DataOrigin = params.get("DataOrigin")
        self._DataOriginProjectId = params.get("DataOriginProjectId")
        self._DataOriginDatasourceId = params.get("DataOriginDatasourceId")
        self._ExtraParam = params.get("ExtraParam")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        self._OperationAuthLimit = params.get("OperationAuthLimit")
        self._UseVPC = params.get("UseVPC")
        self._RegionId = params.get("RegionId")
        self._Schema = params.get("Schema")
        self._DbVersion = params.get("DbVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatasourceResponse(AbstractModel):
    r"""CreateDatasource response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Data: Data source ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.IdDTO`
        :param _Extra: Additional information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: Prompt.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Data = None
        self._Extra = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Data(self):
        r"""Data source ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.IdDTO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Extra(self):
        r"""Additional information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Prompt.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        if params.get("Data") is not None:
            self._Data = IdDTO()
            self._Data._deserialize(params.get("Data"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateEmbedTokenRequest(AbstractModel):
    r"""CreateEmbedToken request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Shares the project ID.
        :type ProjectId: int
        :param _PageId: Shares the page ID. This field is empty (0) for embedding a dashboard and is not passed for embedding ChatBI.
        :type PageId: int
        :param _Intention: "embed" indicates page dashboard embedding, and "chatBIEmbed" indicates ChatBI embedding.
        :type Intention: str
        :param _Scope: "page" indicates embedding a page, "panel" indicates embedding the entire dashboard, and "project" is used for ChatBI embedding.
        :type Scope: str
        :param _ExpireTime: Expiration time. Unit: minutes. Maximum value: 240 (namely, 4 hours). Default value: 240.
        :type ExpireTime: str
        :param _ExtraParam: Alternate field.
        :type ExtraParam: str
        :param _UserCorpId: User enterprise ID (only used for multi-user).
        :type UserCorpId: str
        :param _UserId: User ID (only used for multi-user).
        :type UserId: str
        :param _TicketNum: Access count limit (range: 1-99999). Leave empty to disable access restrictions.
        :type TicketNum: int
        :param _GlobalParam: Global filter parameters: Applies to all report filter criteria. Should be formatted as a JSON string.
** Currently, only character-type page parameters can be bound to global parameters.
**
[
    {
"ParamKey": "name", page parameter name.
"JoinType": "AND", // connection method. Currently, only AND is supported.
        "WhereList": [
            {
"Operator": "-neq", // operator. Refer to the following instructions.
"Value": [ action value. For a single-value array, only one value is passed.
                    "zZWJMD",
                    "ZzVGHX",
"Hunan province".
"Hebei province".
                ]
            }
        ]
    },
    {
        "ParamKey": "genderParam",
        "JoinType": "AND",
        "WhereList": [
            {
                "Operator": "-neq",
                "Value": [
"Male".
                ]
            }
        ]
    }
]



Currently supported operators.
 -neq not equal to != operator.
 -eq equal to = operator.
 -is in operator.

        :type GlobalParam: str
        :param _TokenType: 100: no user bound. Create 1 token at a time. UserCorpId and UserId are optional. ChatBI embedding is not supported.
200: single token per user. Create 1 token at a time. UserCorpId and UserId required.
300: multiple tokens per user. Create multiple tokens at a time. UserCorpId and UserId required.
        :type TokenType: int
        :param _TokenNum: The number of tokens created at one time.
        :type TokenNum: int
        :param _ConfigParam: Embedded display configurations: Currently for ChatBI embedding scenarios; TableFilter represents data table list filtering, SqlView represents SQL view feature.
        :type ConfigParam: str
        """
        self._ProjectId = None
        self._PageId = None
        self._Intention = None
        self._Scope = None
        self._ExpireTime = None
        self._ExtraParam = None
        self._UserCorpId = None
        self._UserId = None
        self._TicketNum = None
        self._GlobalParam = None
        self._TokenType = None
        self._TokenNum = None
        self._ConfigParam = None

    @property
    def ProjectId(self):
        r"""Shares the project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageId(self):
        r"""Shares the page ID. This field is empty (0) for embedding a dashboard and is not passed for embedding ChatBI.
        :rtype: int
        """
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def Intention(self):
        r""""embed" indicates page dashboard embedding, and "chatBIEmbed" indicates ChatBI embedding.
        :rtype: str
        """
        return self._Intention

    @Intention.setter
    def Intention(self, Intention):
        self._Intention = Intention

    @property
    def Scope(self):
        r""""page" indicates embedding a page, "panel" indicates embedding the entire dashboard, and "project" is used for ChatBI embedding.
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def ExpireTime(self):
        r"""Expiration time. Unit: minutes. Maximum value: 240 (namely, 4 hours). Default value: 240.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ExtraParam(self):
        r"""Alternate field.
        :rtype: str
        """
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def UserCorpId(self):
        r"""User enterprise ID (only used for multi-user).
        :rtype: str
        """
        return self._UserCorpId

    @UserCorpId.setter
    def UserCorpId(self, UserCorpId):
        self._UserCorpId = UserCorpId

    @property
    def UserId(self):
        r"""User ID (only used for multi-user).
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def TicketNum(self):
        r"""Access count limit (range: 1-99999). Leave empty to disable access restrictions.
        :rtype: int
        """
        return self._TicketNum

    @TicketNum.setter
    def TicketNum(self, TicketNum):
        self._TicketNum = TicketNum

    @property
    def GlobalParam(self):
        r"""Global filter parameters: Applies to all report filter criteria. Should be formatted as a JSON string.
** Currently, only character-type page parameters can be bound to global parameters.
**
[
    {
"ParamKey": "name", page parameter name.
"JoinType": "AND", // connection method. Currently, only AND is supported.
        "WhereList": [
            {
"Operator": "-neq", // operator. Refer to the following instructions.
"Value": [ action value. For a single-value array, only one value is passed.
                    "zZWJMD",
                    "ZzVGHX",
"Hunan province".
"Hebei province".
                ]
            }
        ]
    },
    {
        "ParamKey": "genderParam",
        "JoinType": "AND",
        "WhereList": [
            {
                "Operator": "-neq",
                "Value": [
"Male".
                ]
            }
        ]
    }
]



Currently supported operators.
 -neq not equal to != operator.
 -eq equal to = operator.
 -is in operator.

        :rtype: str
        """
        return self._GlobalParam

    @GlobalParam.setter
    def GlobalParam(self, GlobalParam):
        self._GlobalParam = GlobalParam

    @property
    def TokenType(self):
        r"""100: no user bound. Create 1 token at a time. UserCorpId and UserId are optional. ChatBI embedding is not supported.
200: single token per user. Create 1 token at a time. UserCorpId and UserId required.
300: multiple tokens per user. Create multiple tokens at a time. UserCorpId and UserId required.
        :rtype: int
        """
        return self._TokenType

    @TokenType.setter
    def TokenType(self, TokenType):
        self._TokenType = TokenType

    @property
    def TokenNum(self):
        r"""The number of tokens created at one time.
        :rtype: int
        """
        return self._TokenNum

    @TokenNum.setter
    def TokenNum(self, TokenNum):
        self._TokenNum = TokenNum

    @property
    def ConfigParam(self):
        r"""Embedded display configurations: Currently for ChatBI embedding scenarios; TableFilter represents data table list filtering, SqlView represents SQL view feature.
        :rtype: str
        """
        return self._ConfigParam

    @ConfigParam.setter
    def ConfigParam(self, ConfigParam):
        self._ConfigParam = ConfigParam


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageId = params.get("PageId")
        self._Intention = params.get("Intention")
        self._Scope = params.get("Scope")
        self._ExpireTime = params.get("ExpireTime")
        self._ExtraParam = params.get("ExtraParam")
        self._UserCorpId = params.get("UserCorpId")
        self._UserId = params.get("UserId")
        self._TicketNum = params.get("TicketNum")
        self._GlobalParam = params.get("GlobalParam")
        self._TokenType = params.get("TokenType")
        self._TokenNum = params.get("TokenNum")
        self._ConfigParam = params.get("ConfigParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmbedTokenResponse(AbstractModel):
    r"""CreateEmbedToken response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Additional information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Data: Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.EmbedTokenInfo`
        :param _Msg: Result description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Additional information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        r"""Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.EmbedTokenInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Msg(self):
        r"""Result description.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = EmbedTokenInfo()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreatePermissionRanksRequest(AbstractModel):
    r"""CreatePermissionRanks request structure.

    """

    def __init__(self):
        r"""
        :param _TableId: <p>page number</p>
        :type TableId: int
        :param _Mode: <p>Mode</p><p>Enumeration value:</p><ul><li>ALL: All</li><li>Specify: Specify</li><li>TAG: Tag</li></ul><p>Default value: ALL</p>
        :type Mode: str
        :param _RoleType: <p>Role type</p><p>Enumeration value:</p><ul><li>ROLES: By role</li><li>Others: Other</li></ul><p>Default value: Others</p>
        :type RoleType: str
        :param _RoleId: <p>All page numbers</p>
        :type RoleId: int
        :param _RulerInfo: <p>Rule information</p>
        :type RulerInfo: str
        :param _Type: <p>Type</p><p>Enumeration value:</p><ul><li>ROW: row permission</li><li>COLUMN: column permission</li></ul><p>Default value: ROW</p>
        :type Type: str
        :param _OpenStatus: <p>Enabled status</p><p>Enumeration value:</p><ul><li>Open: Turn on</li><li>Close: Turn off</li></ul><p>Default value: Close</p>
        :type OpenStatus: str
        :param _ProjectId: <p>Project ID.</p>
        :type ProjectId: int
        :param _RowColumnConfigList: <p>Row/column permission configuration</p>
        :type RowColumnConfigList: list of RowColumnConfig
        """
        self._TableId = None
        self._Mode = None
        self._RoleType = None
        self._RoleId = None
        self._RulerInfo = None
        self._Type = None
        self._OpenStatus = None
        self._ProjectId = None
        self._RowColumnConfigList = None

    @property
    def TableId(self):
        r"""<p>page number</p>
        :rtype: int
        """
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def Mode(self):
        r"""<p>Mode</p><p>Enumeration value:</p><ul><li>ALL: All</li><li>Specify: Specify</li><li>TAG: Tag</li></ul><p>Default value: ALL</p>
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def RoleType(self):
        r"""<p>Role type</p><p>Enumeration value:</p><ul><li>ROLES: By role</li><li>Others: Other</li></ul><p>Default value: Others</p>
        :rtype: str
        """
        return self._RoleType

    @RoleType.setter
    def RoleType(self, RoleType):
        self._RoleType = RoleType

    @property
    def RoleId(self):
        r"""<p>All page numbers</p>
        :rtype: int
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RulerInfo(self):
        r"""<p>Rule information</p>
        :rtype: str
        """
        return self._RulerInfo

    @RulerInfo.setter
    def RulerInfo(self, RulerInfo):
        self._RulerInfo = RulerInfo

    @property
    def Type(self):
        r"""<p>Type</p><p>Enumeration value:</p><ul><li>ROW: row permission</li><li>COLUMN: column permission</li></ul><p>Default value: ROW</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def OpenStatus(self):
        r"""<p>Enabled status</p><p>Enumeration value:</p><ul><li>Open: Turn on</li><li>Close: Turn off</li></ul><p>Default value: Close</p>
        :rtype: str
        """
        return self._OpenStatus

    @OpenStatus.setter
    def OpenStatus(self, OpenStatus):
        self._OpenStatus = OpenStatus

    @property
    def ProjectId(self):
        r"""<p>Project ID.</p>
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RowColumnConfigList(self):
        r"""<p>Row/column permission configuration</p>
        :rtype: list of RowColumnConfig
        """
        return self._RowColumnConfigList

    @RowColumnConfigList.setter
    def RowColumnConfigList(self, RowColumnConfigList):
        self._RowColumnConfigList = RowColumnConfigList


    def _deserialize(self, params):
        self._TableId = params.get("TableId")
        self._Mode = params.get("Mode")
        self._RoleType = params.get("RoleType")
        self._RoleId = params.get("RoleId")
        self._RulerInfo = params.get("RulerInfo")
        self._Type = params.get("Type")
        self._OpenStatus = params.get("OpenStatus")
        self._ProjectId = params.get("ProjectId")
        if params.get("RowColumnConfigList") is not None:
            self._RowColumnConfigList = []
            for item in params.get("RowColumnConfigList"):
                obj = RowColumnConfig()
                obj._deserialize(item)
                self._RowColumnConfigList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePermissionRanksResponse(AbstractModel):
    r"""CreatePermissionRanks response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Msg: <p>Message</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _Extra: <p>112</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Data: <p>1</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Msg = None
        self._Extra = None
        self._Data = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Msg(self):
        r"""<p>Message</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Extra(self):
        r"""<p>112</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        r"""<p>1</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Msg = params.get("Msg")
        self._Extra = params.get("Extra")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    r"""CreateProject request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Project name.
        :type Name: str
        :param _ColorCode: Background color of the logo.
        :type ColorCode: str
        :param _Logo: Project logo.
        :type Logo: str
        :param _Mark: Remarks.
        :type Mark: str
        :param _IsApply: Whether to allow user requests.
        :type IsApply: bool
        :param _DefaultPanelType: Default dashboard.
Value range:.
1: project dashboard. 
2: my dashboard.
        :type DefaultPanelType: int
        :param _ManagePlatform: Management platform.
        :type ManagePlatform: str
        """
        self._Name = None
        self._ColorCode = None
        self._Logo = None
        self._Mark = None
        self._IsApply = None
        self._DefaultPanelType = None
        self._ManagePlatform = None

    @property
    def Name(self):
        r"""Project name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ColorCode(self):
        r"""Background color of the logo.
        :rtype: str
        """
        return self._ColorCode

    @ColorCode.setter
    def ColorCode(self, ColorCode):
        self._ColorCode = ColorCode

    @property
    def Logo(self):
        r"""Project logo.
        :rtype: str
        """
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def Mark(self):
        r"""Remarks.
        :rtype: str
        """
        return self._Mark

    @Mark.setter
    def Mark(self, Mark):
        self._Mark = Mark

    @property
    def IsApply(self):
        r"""Whether to allow user requests.
        :rtype: bool
        """
        return self._IsApply

    @IsApply.setter
    def IsApply(self, IsApply):
        self._IsApply = IsApply

    @property
    def DefaultPanelType(self):
        r"""Default dashboard.
Value range:.
1: project dashboard. 
2: my dashboard.
        :rtype: int
        """
        return self._DefaultPanelType

    @DefaultPanelType.setter
    def DefaultPanelType(self, DefaultPanelType):
        self._DefaultPanelType = DefaultPanelType

    @property
    def ManagePlatform(self):
        r"""Management platform.
        :rtype: str
        """
        return self._ManagePlatform

    @ManagePlatform.setter
    def ManagePlatform(self, ManagePlatform):
        self._ManagePlatform = ManagePlatform


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ColorCode = params.get("ColorCode")
        self._Logo = params.get("Logo")
        self._Mark = params.get("Mark")
        self._IsApply = params.get("IsApply")
        self._DefaultPanelType = params.get("DefaultPanelType")
        self._ManagePlatform = params.get("ManagePlatform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProjectResponse(AbstractModel):
    r"""CreateProject response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Extra data.
        :type Extra: str
        :param _Data: Data.

        :type Data: :class:`tencentcloud.bi.v20220105.models.Data`
        :param _Msg: Returned information.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Extra data.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        r"""Data.

        :rtype: :class:`tencentcloud.bi.v20220105.models.Data`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Msg(self):
        r"""Returned information.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = Data()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateTagTableRequest(AbstractModel):
    r"""CreateTagTable request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Tag table name
        :type Name: str
        :param _AutoImportProjectId: Project id associated with the tag table
        :type AutoImportProjectId: int
        :param _AutoImportTableId: id of the data table associated with the tag table
        :type AutoImportTableId: int
        :param _AutoImportUinField: Corresponding field of uin
        :type AutoImportUinField: str
        """
        self._Name = None
        self._AutoImportProjectId = None
        self._AutoImportTableId = None
        self._AutoImportUinField = None

    @property
    def Name(self):
        r"""Tag table name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AutoImportProjectId(self):
        r"""Project id associated with the tag table
        :rtype: int
        """
        return self._AutoImportProjectId

    @AutoImportProjectId.setter
    def AutoImportProjectId(self, AutoImportProjectId):
        self._AutoImportProjectId = AutoImportProjectId

    @property
    def AutoImportTableId(self):
        r"""id of the data table associated with the tag table
        :rtype: int
        """
        return self._AutoImportTableId

    @AutoImportTableId.setter
    def AutoImportTableId(self, AutoImportTableId):
        self._AutoImportTableId = AutoImportTableId

    @property
    def AutoImportUinField(self):
        r"""Corresponding field of uin
        :rtype: str
        """
        return self._AutoImportUinField

    @AutoImportUinField.setter
    def AutoImportUinField(self, AutoImportUinField):
        self._AutoImportUinField = AutoImportUinField


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AutoImportProjectId = params.get("AutoImportProjectId")
        self._AutoImportTableId = params.get("AutoImportTableId")
        self._AutoImportUinField = params.get("AutoImportUinField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTagTableResponse(AbstractModel):
    r"""CreateTagTable response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Data: Data.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.CreateTagTableVO`
        :param _Extra: Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: Information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Data = None
        self._Extra = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Data(self):
        r"""Data.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateTagTableVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Extra(self):
        r"""Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        if params.get("Data") is not None:
            self._Data = CreateTagTableVO()
            self._Data._deserialize(params.get("Data"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateTagTableVO(AbstractModel):
    r"""Create tag output parameters

    """

    def __init__(self):
        r"""
        :param _Id: Tag table id
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        r"""Tag table id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserRoleProjectRequest(AbstractModel):
    r"""CreateUserRoleProject request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _RoleIdList: Role ID list.
        :type RoleIdList: list of int
        :param _UserList: User list (deprecated).
        :type UserList: list of UserIdAndUserName
        :param _UserInfoList: User list (new).
        :type UserInfoList: list of UserInfo
        """
        self._ProjectId = None
        self._RoleIdList = None
        self._UserList = None
        self._UserInfoList = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RoleIdList(self):
        r"""Role ID list.
        :rtype: list of int
        """
        return self._RoleIdList

    @RoleIdList.setter
    def RoleIdList(self, RoleIdList):
        self._RoleIdList = RoleIdList

    @property
    def UserList(self):
        warnings.warn("parameter `UserList` is deprecated", DeprecationWarning) 

        r"""User list (deprecated).
        :rtype: list of UserIdAndUserName
        """
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        warnings.warn("parameter `UserList` is deprecated", DeprecationWarning) 

        self._UserList = UserList

    @property
    def UserInfoList(self):
        r"""User list (new).
        :rtype: list of UserInfo
        """
        return self._UserInfoList

    @UserInfoList.setter
    def UserInfoList(self, UserInfoList):
        self._UserInfoList = UserInfoList


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._RoleIdList = params.get("RoleIdList")
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = UserIdAndUserName()
                obj._deserialize(item)
                self._UserList.append(obj)
        if params.get("UserInfoList") is not None:
            self._UserInfoList = []
            for item in params.get("UserInfoList"):
                obj = UserInfo()
                obj._deserialize(item)
                self._UserInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserRoleProjectResponse(AbstractModel):
    r"""CreateUserRoleProject response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Data: Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.DataId`
        :param _Msg: Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        r"""Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.DataId`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Msg(self):
        r"""Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = DataId()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateUserRoleRequest(AbstractModel):
    r"""CreateUserRole request structure.

    """

    def __init__(self):
        r"""
        :param _RoleIdList: Role ID list.
        :type RoleIdList: list of int
        :param _UserList: User list (deprecated).
        :type UserList: list of UserIdAndUserName
        :param _UserInfoList: User list (new).
        :type UserInfoList: list of UserInfo
        :param _UserGroups: User group ID list.
        :type UserGroups: list of int non-negative
        """
        self._RoleIdList = None
        self._UserList = None
        self._UserInfoList = None
        self._UserGroups = None

    @property
    def RoleIdList(self):
        r"""Role ID list.
        :rtype: list of int
        """
        return self._RoleIdList

    @RoleIdList.setter
    def RoleIdList(self, RoleIdList):
        self._RoleIdList = RoleIdList

    @property
    def UserList(self):
        warnings.warn("parameter `UserList` is deprecated", DeprecationWarning) 

        r"""User list (deprecated).
        :rtype: list of UserIdAndUserName
        """
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        warnings.warn("parameter `UserList` is deprecated", DeprecationWarning) 

        self._UserList = UserList

    @property
    def UserInfoList(self):
        r"""User list (new).
        :rtype: list of UserInfo
        """
        return self._UserInfoList

    @UserInfoList.setter
    def UserInfoList(self, UserInfoList):
        self._UserInfoList = UserInfoList

    @property
    def UserGroups(self):
        r"""User group ID list.
        :rtype: list of int non-negative
        """
        return self._UserGroups

    @UserGroups.setter
    def UserGroups(self, UserGroups):
        self._UserGroups = UserGroups


    def _deserialize(self, params):
        self._RoleIdList = params.get("RoleIdList")
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = UserIdAndUserName()
                obj._deserialize(item)
                self._UserList.append(obj)
        if params.get("UserInfoList") is not None:
            self._UserInfoList = []
            for item in params.get("UserInfoList"):
                obj = UserInfo()
                obj._deserialize(item)
                self._UserInfoList.append(obj)
        self._UserGroups = params.get("UserGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserRoleResponse(AbstractModel):
    r"""CreateUserRole response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Data: Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.DataId`
        :param _Msg: Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        r"""Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.DataId`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Msg(self):
        r"""Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = DataId()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class Data(AbstractModel):
    r"""Data

    """

    def __init__(self):
        r"""
        :param _Id: Project ID.

        :type Id: int
        :param _EditUrl: url
Note: This field may return null, indicating that no valid values can be obtained.
        :type EditUrl: str
        """
        self._Id = None
        self._EditUrl = None

    @property
    def Id(self):
        r"""Project ID.

        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def EditUrl(self):
        r"""url
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EditUrl

    @EditUrl.setter
    def EditUrl(self, EditUrl):
        self._EditUrl = EditUrl


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._EditUrl = params.get("EditUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataId(AbstractModel):
    r"""Data ID

    """

    def __init__(self):
        r"""
        :param _Id: Data ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        r"""Data ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatasourceInfo(AbstractModel):
    r"""Data source details

    """

    def __init__(self):
        r"""
        :param _Id: Database ID.
        :type Id: int
        :param _DbName: Database name.
        :type DbName: str
        :param _ServiceType: Domain type. Valid values: 1: Tencent Cloud; 2: local.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceType: str
        :param _SourceName: Database alias.
        :type SourceName: str
        :param _DbType: Database driver.
        :type DbType: str
        :param _DbHost: HOST
        :type DbHost: str
        :param _DbPort: Port.
        :type DbPort: int
        :param _DbUser: Username.
        :type DbUser: str
        :param _Charset: Database encoding.
        :type Charset: str
        :param _CreatedAt: Creation time.

        :type CreatedAt: str
        :param _UpdatedAt: Modification time.
        :type UpdatedAt: str
        :param _CreatedUser: Creator.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedUser: str
        :param _Catalog: Catalog value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Catalog: str
        :param _ConnectType: Connection type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConnectType: str
        :param _ProjectId: Project ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectId: str
        :param _Desc: Data source description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Desc: str
        :param _Status: Data source status.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _SourcePlat: Source platform.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SourcePlat: str
        :param _ExtraParam: Extension parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtraParam: str
        :param _AddInfo: Additional information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AddInfo: str
        :param _ProjectName: Project name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectName: str
        :param _EngineType: Engine type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EngineType: str
        :param _Manager: Data source owner.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Manager: str
        :param _OperatorWhitelist: Operation personnel allowlist.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OperatorWhitelist: str
        :param _VpcId: VPC information of the data source.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _UniqVpcId: uniqVpc information of the data source.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqVpcId: str
        :param _RegionId: Data source region information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionId: str
        :param _StateAction: Operation attributes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StateAction: :class:`tencentcloud.bi.v20220105.models.BaseStateAction`
        :param _UpdatedUser: Updater.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdatedUser: str
        :param _PermissionList: Permission list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PermissionList: list of PermissionGroup
        :param _AuthList: Permission value list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuthList: list of str
        :param _DataOrigin: Third-party data source identifier.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataOrigin: str
        :param _DataOriginProjectId: Third-party project ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataOriginProjectId: str
        :param _DataOriginDatasourceId: Third-party data source ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataOriginDatasourceId: str
        :param _ClusterId: Cluster ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param _DbTypeName: Data source name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbTypeName: str
        :param _UseVPC: Enable VPC.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UseVPC: bool
        :param _Owner: Associated person ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Owner: str
        :param _OwnerName: Associated person name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OwnerName: str
        :param _Schema: Database schema.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Schema: str
        :param _DbVersion: Database version.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbVersion: str
        """
        self._Id = None
        self._DbName = None
        self._ServiceType = None
        self._SourceName = None
        self._DbType = None
        self._DbHost = None
        self._DbPort = None
        self._DbUser = None
        self._Charset = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._CreatedUser = None
        self._Catalog = None
        self._ConnectType = None
        self._ProjectId = None
        self._Desc = None
        self._Status = None
        self._SourcePlat = None
        self._ExtraParam = None
        self._AddInfo = None
        self._ProjectName = None
        self._EngineType = None
        self._Manager = None
        self._OperatorWhitelist = None
        self._VpcId = None
        self._UniqVpcId = None
        self._RegionId = None
        self._StateAction = None
        self._UpdatedUser = None
        self._PermissionList = None
        self._AuthList = None
        self._DataOrigin = None
        self._DataOriginProjectId = None
        self._DataOriginDatasourceId = None
        self._ClusterId = None
        self._DbTypeName = None
        self._UseVPC = None
        self._Owner = None
        self._OwnerName = None
        self._Schema = None
        self._DbVersion = None

    @property
    def Id(self):
        r"""Database ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DbName(self):
        r"""Database name.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def ServiceType(self):
        r"""Domain type. Valid values: 1: Tencent Cloud; 2: local.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def SourceName(self):
        r"""Database alias.
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def DbType(self):
        r"""Database driver.
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DbHost(self):
        r"""HOST
        :rtype: str
        """
        return self._DbHost

    @DbHost.setter
    def DbHost(self, DbHost):
        self._DbHost = DbHost

    @property
    def DbPort(self):
        r"""Port.
        :rtype: int
        """
        return self._DbPort

    @DbPort.setter
    def DbPort(self, DbPort):
        self._DbPort = DbPort

    @property
    def DbUser(self):
        r"""Username.
        :rtype: str
        """
        return self._DbUser

    @DbUser.setter
    def DbUser(self, DbUser):
        self._DbUser = DbUser

    @property
    def Charset(self):
        r"""Database encoding.
        :rtype: str
        """
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def CreatedAt(self):
        r"""Creation time.

        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""Modification time.
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def CreatedUser(self):
        r"""Creator.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatedUser

    @CreatedUser.setter
    def CreatedUser(self, CreatedUser):
        self._CreatedUser = CreatedUser

    @property
    def Catalog(self):
        r"""Catalog value.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def ConnectType(self):
        r"""Connection type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ConnectType

    @ConnectType.setter
    def ConnectType(self, ConnectType):
        self._ConnectType = ConnectType

    @property
    def ProjectId(self):
        r"""Project ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Desc(self):
        r"""Data source description.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Status(self):
        r"""Data source status.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SourcePlat(self):
        r"""Source platform.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SourcePlat

    @SourcePlat.setter
    def SourcePlat(self, SourcePlat):
        self._SourcePlat = SourcePlat

    @property
    def ExtraParam(self):
        r"""Extension parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def AddInfo(self):
        r"""Additional information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AddInfo

    @AddInfo.setter
    def AddInfo(self, AddInfo):
        self._AddInfo = AddInfo

    @property
    def ProjectName(self):
        r"""Project name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def EngineType(self):
        r"""Engine type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def Manager(self):
        r"""Data source owner.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Manager

    @Manager.setter
    def Manager(self, Manager):
        self._Manager = Manager

    @property
    def OperatorWhitelist(self):
        r"""Operation personnel allowlist.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OperatorWhitelist

    @OperatorWhitelist.setter
    def OperatorWhitelist(self, OperatorWhitelist):
        self._OperatorWhitelist = OperatorWhitelist

    @property
    def VpcId(self):
        r"""VPC information of the data source.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def UniqVpcId(self):
        r"""uniqVpc information of the data source.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def RegionId(self):
        r"""Data source region information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def StateAction(self):
        r"""Operation attributes.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.BaseStateAction`
        """
        return self._StateAction

    @StateAction.setter
    def StateAction(self, StateAction):
        self._StateAction = StateAction

    @property
    def UpdatedUser(self):
        r"""Updater.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdatedUser

    @UpdatedUser.setter
    def UpdatedUser(self, UpdatedUser):
        self._UpdatedUser = UpdatedUser

    @property
    def PermissionList(self):
        r"""Permission list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of PermissionGroup
        """
        return self._PermissionList

    @PermissionList.setter
    def PermissionList(self, PermissionList):
        self._PermissionList = PermissionList

    @property
    def AuthList(self):
        r"""Permission value list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AuthList

    @AuthList.setter
    def AuthList(self, AuthList):
        self._AuthList = AuthList

    @property
    def DataOrigin(self):
        r"""Third-party data source identifier.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DataOrigin

    @DataOrigin.setter
    def DataOrigin(self, DataOrigin):
        self._DataOrigin = DataOrigin

    @property
    def DataOriginProjectId(self):
        r"""Third-party project ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DataOriginProjectId

    @DataOriginProjectId.setter
    def DataOriginProjectId(self, DataOriginProjectId):
        self._DataOriginProjectId = DataOriginProjectId

    @property
    def DataOriginDatasourceId(self):
        r"""Third-party data source ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DataOriginDatasourceId

    @DataOriginDatasourceId.setter
    def DataOriginDatasourceId(self, DataOriginDatasourceId):
        self._DataOriginDatasourceId = DataOriginDatasourceId

    @property
    def ClusterId(self):
        r"""Cluster ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DbTypeName(self):
        r"""Data source name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbTypeName

    @DbTypeName.setter
    def DbTypeName(self, DbTypeName):
        self._DbTypeName = DbTypeName

    @property
    def UseVPC(self):
        r"""Enable VPC.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._UseVPC

    @UseVPC.setter
    def UseVPC(self, UseVPC):
        self._UseVPC = UseVPC

    @property
    def Owner(self):
        r"""Associated person ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def OwnerName(self):
        r"""Associated person name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OwnerName

    @OwnerName.setter
    def OwnerName(self, OwnerName):
        self._OwnerName = OwnerName

    @property
    def Schema(self):
        r"""Database schema.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def DbVersion(self):
        r"""Database version.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DbName = params.get("DbName")
        self._ServiceType = params.get("ServiceType")
        self._SourceName = params.get("SourceName")
        self._DbType = params.get("DbType")
        self._DbHost = params.get("DbHost")
        self._DbPort = params.get("DbPort")
        self._DbUser = params.get("DbUser")
        self._Charset = params.get("Charset")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._CreatedUser = params.get("CreatedUser")
        self._Catalog = params.get("Catalog")
        self._ConnectType = params.get("ConnectType")
        self._ProjectId = params.get("ProjectId")
        self._Desc = params.get("Desc")
        self._Status = params.get("Status")
        self._SourcePlat = params.get("SourcePlat")
        self._ExtraParam = params.get("ExtraParam")
        self._AddInfo = params.get("AddInfo")
        self._ProjectName = params.get("ProjectName")
        self._EngineType = params.get("EngineType")
        self._Manager = params.get("Manager")
        self._OperatorWhitelist = params.get("OperatorWhitelist")
        self._VpcId = params.get("VpcId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._RegionId = params.get("RegionId")
        if params.get("StateAction") is not None:
            self._StateAction = BaseStateAction()
            self._StateAction._deserialize(params.get("StateAction"))
        self._UpdatedUser = params.get("UpdatedUser")
        if params.get("PermissionList") is not None:
            self._PermissionList = []
            for item in params.get("PermissionList"):
                obj = PermissionGroup()
                obj._deserialize(item)
                self._PermissionList.append(obj)
        self._AuthList = params.get("AuthList")
        self._DataOrigin = params.get("DataOrigin")
        self._DataOriginProjectId = params.get("DataOriginProjectId")
        self._DataOriginDatasourceId = params.get("DataOriginDatasourceId")
        self._ClusterId = params.get("ClusterId")
        self._DbTypeName = params.get("DbTypeName")
        self._UseVPC = params.get("UseVPC")
        self._Owner = params.get("Owner")
        self._OwnerName = params.get("OwnerName")
        self._Schema = params.get("Schema")
        self._DbVersion = params.get("DbVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatasourceInfoData(AbstractModel):
    r"""Data source details list

    """

    def __init__(self):
        r"""
        :param _List: Data source details list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of DatasourceInfo
        :param _Total: Total number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _TotalPages: Total number of pages.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalPages: int
        """
        self._List = None
        self._Total = None
        self._TotalPages = None

    @property
    def List(self):
        r"""Data source details list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DatasourceInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        r"""Total number.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalPages(self):
        r"""Total number of pages.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalPages

    @TotalPages.setter
    def TotalPages(self, TotalPages):
        self._TotalPages = TotalPages


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DatasourceInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._TotalPages = params.get("TotalPages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDatasourceRequest(AbstractModel):
    r"""DeleteDatasource request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Data source ID.
        :type Id: int
        :param _ProjectId: Project ID.
        :type ProjectId: int
        """
        self._Id = None
        self._ProjectId = None

    @property
    def Id(self):
        r"""Data source ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDatasourceResponse(AbstractModel):
    r"""DeleteDatasource response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Data: Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: str
        :param _Extra: Expansion.
        :type Extra: str
        :param _Msg: Information.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Data = None
        self._Extra = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Data(self):
        r"""Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Extra(self):
        r"""Expansion.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Information.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Data = params.get("Data")
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteProjectRequest(AbstractModel):
    r"""DeleteProject request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Project ID.
        :type Id: int
        :param _Seed: Random number.
        :type Seed: str
        :param _DefaultPanelType: Default dashboard.
Value range:.
1: project dashboard. 
2: my dashboard.
        :type DefaultPanelType: int
        """
        self._Id = None
        self._Seed = None
        self._DefaultPanelType = None

    @property
    def Id(self):
        r"""Project ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Seed(self):
        r"""Random number.
        :rtype: str
        """
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def DefaultPanelType(self):
        r"""Default dashboard.
Value range:.
1: project dashboard. 
2: my dashboard.
        :rtype: int
        """
        return self._DefaultPanelType

    @DefaultPanelType.setter
    def DefaultPanelType(self, DefaultPanelType):
        self._DefaultPanelType = DefaultPanelType


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Seed = params.get("Seed")
        self._DefaultPanelType = params.get("DefaultPanelType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectResponse(AbstractModel):
    r"""DeleteProject response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: "".
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Data: ""
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: str
        :param _Msg: ""
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r""""".
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        r"""""
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Msg(self):
        r"""""
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Data = params.get("Data")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteUserRoleProjectRequest(AbstractModel):
    r"""DeleteUserRoleProject request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _UserId: User ID.
        :type UserId: str
        """
        self._ProjectId = None
        self._UserId = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def UserId(self):
        r"""User ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserRoleProjectResponse(AbstractModel):
    r"""DeleteUserRoleProject response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Data: Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: str
        :param _Msg: Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        r"""Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Msg(self):
        r"""Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Data = params.get("Data")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteUserRoleRequest(AbstractModel):
    r"""DeleteUserRole request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID.
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        r"""User ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserRoleResponse(AbstractModel):
    r"""DeleteUserRole response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Data: Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: str
        :param _Msg: Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        r"""Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Msg(self):
        r"""Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Data = params.get("Data")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeDatasourceListRequest(AbstractModel):
    r"""DescribeDatasourceList request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: None.
        :type ProjectId: int
        :param _AllPage: Returns all pages and defaults to false.
        :type AllPage: bool
        :param _DbName: Database name search.
        :type DbName: str
        :param _PageNo: None.
        :type PageNo: int
        :param _PageSize: None.
        :type PageSize: int
        :param _Keyword: Search keywords.
        :type Keyword: str
        :param _PermissionType: Permission filter (0: all permissions, 1: access permission, 2: edit permission).
        :type PermissionType: int
        """
        self._ProjectId = None
        self._AllPage = None
        self._DbName = None
        self._PageNo = None
        self._PageSize = None
        self._Keyword = None
        self._PermissionType = None

    @property
    def ProjectId(self):
        r"""None.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AllPage(self):
        r"""Returns all pages and defaults to false.
        :rtype: bool
        """
        return self._AllPage

    @AllPage.setter
    def AllPage(self, AllPage):
        self._AllPage = AllPage

    @property
    def DbName(self):
        r"""Database name search.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def PageNo(self):
        r"""None.
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        r"""None.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Keyword(self):
        r"""Search keywords.
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def PermissionType(self):
        r"""Permission filter (0: all permissions, 1: access permission, 2: edit permission).
        :rtype: int
        """
        return self._PermissionType

    @PermissionType.setter
    def PermissionType(self, PermissionType):
        self._PermissionType = PermissionType


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AllPage = params.get("AllPage")
        self._DbName = params.get("DbName")
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._Keyword = params.get("Keyword")
        self._PermissionType = params.get("PermissionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatasourceListResponse(AbstractModel):
    r"""DescribeDatasourceList response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Data: List details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.DatasourceInfoData`
        :param _Extra: Information.
        :type Extra: str
        :param _Msg: Information.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Data = None
        self._Extra = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Data(self):
        r"""List details.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.DatasourceInfoData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Extra(self):
        r"""Information.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Information.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        if params.get("Data") is not None:
            self._Data = DatasourceInfoData()
            self._Data._deserialize(params.get("Data"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribePageWidgetListRequest(AbstractModel):
    r"""DescribePageWidgetList request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _PageId: Page ID.
        :type PageId: str
        """
        self._ProjectId = None
        self._PageId = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageId(self):
        r"""Page ID.
        :rtype: str
        """
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageId = params.get("PageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePageWidgetListResponse(AbstractModel):
    r"""DescribePageWidgetList response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Extension parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Data: Returned data results.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.WidgetListVO`
        :param _Msg: Response message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Extension parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        r"""Returned data results.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.WidgetListVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Msg(self):
        r"""Response message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = WidgetListVO()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeProjectInfoRequest(AbstractModel):
    r"""DescribeProjectInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Project ID.
        :type Id: int
        :param _DefaultPanelType: Default dashboard.
Value range:.
1: project dashboard. 
2: my dashboard.
        :type DefaultPanelType: int
        """
        self._Id = None
        self._DefaultPanelType = None

    @property
    def Id(self):
        r"""Project ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DefaultPanelType(self):
        r"""Default dashboard.
Value range:.
1: project dashboard. 
2: my dashboard.
        :rtype: int
        """
        return self._DefaultPanelType

    @DefaultPanelType.setter
    def DefaultPanelType(self, DefaultPanelType):
        self._DefaultPanelType = DefaultPanelType


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DefaultPanelType = params.get("DefaultPanelType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectInfoResponse(AbstractModel):
    r"""DescribeProjectInfo response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: ""
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: ""
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _Data: Project details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.Project`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Msg = None
        self._Data = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""""
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""""
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Data(self):
        r"""Project details.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.Project`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        if params.get("Data") is not None:
            self._Data = Project()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeProjectListRequest(AbstractModel):
    r"""DescribeProjectList request structure.

    """

    def __init__(self):
        r"""
        :param _PageSize: Page capacity. The initial version defaults to 20 and may change dynamically based on screen width in the future.
        :type PageSize: int
        :param _PageNo: Page marker.
        :type PageNo: int
        :param _Keyword: Fuzzy search field.
        :type Keyword: str
        :param _AllPage: Whether to display all. If true, ignore pagination.
        :type AllPage: bool
        :param _ModuleCollection: Role information.
        :type ModuleCollection: str
        :param _ModuleIdList: moduleId set.
        :type ModuleIdList: list of str
        """
        self._PageSize = None
        self._PageNo = None
        self._Keyword = None
        self._AllPage = None
        self._ModuleCollection = None
        self._ModuleIdList = None

    @property
    def PageSize(self):
        r"""Page capacity. The initial version defaults to 20 and may change dynamically based on screen width in the future.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNo(self):
        r"""Page marker.
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def Keyword(self):
        r"""Fuzzy search field.
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def AllPage(self):
        r"""Whether to display all. If true, ignore pagination.
        :rtype: bool
        """
        return self._AllPage

    @AllPage.setter
    def AllPage(self, AllPage):
        self._AllPage = AllPage

    @property
    def ModuleCollection(self):
        r"""Role information.
        :rtype: str
        """
        return self._ModuleCollection

    @ModuleCollection.setter
    def ModuleCollection(self, ModuleCollection):
        self._ModuleCollection = ModuleCollection

    @property
    def ModuleIdList(self):
        r"""moduleId set.
        :rtype: list of str
        """
        return self._ModuleIdList

    @ModuleIdList.setter
    def ModuleIdList(self, ModuleIdList):
        self._ModuleIdList = ModuleIdList


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNo = params.get("PageNo")
        self._Keyword = params.get("Keyword")
        self._AllPage = params.get("AllPage")
        self._ModuleCollection = params.get("ModuleCollection")
        self._ModuleIdList = params.get("ModuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectListResponse(AbstractModel):
    r"""DescribeProjectList response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Additional information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: API information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _Data: Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.ProjectListData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Msg = None
        self._Data = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Additional information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""API information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Data(self):
        r"""Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ProjectListData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        if params.get("Data") is not None:
            self._Data = ProjectListData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeSourceFieldListRequest(AbstractModel):
    r"""DescribeSourceFieldList request structure.

    """

    def __init__(self):
        r"""
        :param _DataSourceId: data source Id
        :type DataSourceId: int
        :param _TableName: Table name
        :type TableName: str
        :param _Sql: sql content
        :type Sql: str
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _AsyncRequest: whether
        :type AsyncRequest: bool
        :param _TranId: async transaction id
        :type TranId: str
        :param _ParamList: 11
        :type ParamList: list of ParamCreateDTO
        :param _DlcExtInfo: DLC extension parameter
        :type DlcExtInfo: str
        :param _QueryDbData: Query database required or not
        :type QueryDbData: str
        :param _TableId: Data table Id
        :type TableId: str
        :param _TableType: The backend provides a dictionary: table type, 1. database table creation, 2. SQL table creation, 3. Excel upload, 4. API connection, 5. Tencent documentation, 6. cloud database, 7. manually enter, 8. join query.
        :type TableType: int
        """
        self._DataSourceId = None
        self._TableName = None
        self._Sql = None
        self._ProjectId = None
        self._AsyncRequest = None
        self._TranId = None
        self._ParamList = None
        self._DlcExtInfo = None
        self._QueryDbData = None
        self._TableId = None
        self._TableType = None

    @property
    def DataSourceId(self):
        r"""data source Id
        :rtype: int
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def TableName(self):
        r"""Table name
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Sql(self):
        r"""sql content
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AsyncRequest(self):
        r"""whether
        :rtype: bool
        """
        return self._AsyncRequest

    @AsyncRequest.setter
    def AsyncRequest(self, AsyncRequest):
        self._AsyncRequest = AsyncRequest

    @property
    def TranId(self):
        r"""async transaction id
        :rtype: str
        """
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def ParamList(self):
        r"""11
        :rtype: list of ParamCreateDTO
        """
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def DlcExtInfo(self):
        r"""DLC extension parameter
        :rtype: str
        """
        return self._DlcExtInfo

    @DlcExtInfo.setter
    def DlcExtInfo(self, DlcExtInfo):
        self._DlcExtInfo = DlcExtInfo

    @property
    def QueryDbData(self):
        r"""Query database required or not
        :rtype: str
        """
        return self._QueryDbData

    @QueryDbData.setter
    def QueryDbData(self, QueryDbData):
        self._QueryDbData = QueryDbData

    @property
    def TableId(self):
        r"""Data table Id
        :rtype: str
        """
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def TableType(self):
        r"""The backend provides a dictionary: table type, 1. database table creation, 2. SQL table creation, 3. Excel upload, 4. API connection, 5. Tencent documentation, 6. cloud database, 7. manually enter, 8. join query.
        :rtype: int
        """
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType


    def _deserialize(self, params):
        self._DataSourceId = params.get("DataSourceId")
        self._TableName = params.get("TableName")
        self._Sql = params.get("Sql")
        self._ProjectId = params.get("ProjectId")
        self._AsyncRequest = params.get("AsyncRequest")
        self._TranId = params.get("TranId")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ParamCreateDTO()
                obj._deserialize(item)
                self._ParamList.append(obj)
        self._DlcExtInfo = params.get("DlcExtInfo")
        self._QueryDbData = params.get("QueryDbData")
        self._TableId = params.get("TableId")
        self._TableType = params.get("TableType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSourceFieldListResponse(AbstractModel):
    r"""DescribeSourceFieldList response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Additional Information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: Information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _Data: List of fields in the table
        :type Data: :class:`tencentcloud.bi.v20220105.models.TableColumnListData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Msg = None
        self._Data = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Additional Information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Data(self):
        r"""List of fields in the table
        :rtype: :class:`tencentcloud.bi.v20220105.models.TableColumnListData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        if params.get("Data") is not None:
            self._Data = TableColumnListData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeUserProjectListRequest(AbstractModel):
    r"""DescribeUserProjectList request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _AllPage: None.
        :type AllPage: bool
        :param _PageNo: None.
        :type PageNo: int
        :param _PageSize: None.
        :type PageSize: int
        :param _IsFilterPerAuthUser: Whether to filter out enterprise administrators.
        :type IsFilterPerAuthUser: bool
        :param _IsFilterCurrentUser: Whether to filter out the current user.
        :type IsFilterCurrentUser: bool
        :param _Keyword: Keyword.
        :type Keyword: str
        """
        self._ProjectId = None
        self._AllPage = None
        self._PageNo = None
        self._PageSize = None
        self._IsFilterPerAuthUser = None
        self._IsFilterCurrentUser = None
        self._Keyword = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AllPage(self):
        r"""None.
        :rtype: bool
        """
        return self._AllPage

    @AllPage.setter
    def AllPage(self, AllPage):
        self._AllPage = AllPage

    @property
    def PageNo(self):
        r"""None.
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        r"""None.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def IsFilterPerAuthUser(self):
        r"""Whether to filter out enterprise administrators.
        :rtype: bool
        """
        return self._IsFilterPerAuthUser

    @IsFilterPerAuthUser.setter
    def IsFilterPerAuthUser(self, IsFilterPerAuthUser):
        self._IsFilterPerAuthUser = IsFilterPerAuthUser

    @property
    def IsFilterCurrentUser(self):
        r"""Whether to filter out the current user.
        :rtype: bool
        """
        return self._IsFilterCurrentUser

    @IsFilterCurrentUser.setter
    def IsFilterCurrentUser(self, IsFilterCurrentUser):
        self._IsFilterCurrentUser = IsFilterCurrentUser

    @property
    def Keyword(self):
        r"""Keyword.
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AllPage = params.get("AllPage")
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._IsFilterPerAuthUser = params.get("IsFilterPerAuthUser")
        self._IsFilterCurrentUser = params.get("IsFilterCurrentUser")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserProjectListResponse(AbstractModel):
    r"""DescribeUserProjectList response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Data: Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.CorpUserListData`
        :param _Extra: Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Data = None
        self._Extra = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Data(self):
        r"""Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.CorpUserListData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Extra(self):
        r"""Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        if params.get("Data") is not None:
            self._Data = CorpUserListData()
            self._Data._deserialize(params.get("Data"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeUserRoleListRequest(AbstractModel):
    r"""DescribeUserRoleList request structure.

    """

    def __init__(self):
        r"""
        :param _PageNo: Page number.
        :type PageNo: int
        :param _PageSize: Number of pages.
        :type PageSize: int
        :param _AllPage: All page numbers.
        :type AllPage: bool
        :param _UserType: 0: enterprise user. 1: visitor. If left blank, it indicates all users.
        :type UserType: str
        :param _Keyword: Keyword for fuzzy search.
        :type Keyword: str
        :param _ProjectId: Project ID.

        :type ProjectId: str
        :param _IsOnlyBindAppUser: Whether to only obtain users bound to the WeCom app.
        :type IsOnlyBindAppUser: bool
        """
        self._PageNo = None
        self._PageSize = None
        self._AllPage = None
        self._UserType = None
        self._Keyword = None
        self._ProjectId = None
        self._IsOnlyBindAppUser = None

    @property
    def PageNo(self):
        r"""Page number.
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        r"""Number of pages.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def AllPage(self):
        r"""All page numbers.
        :rtype: bool
        """
        return self._AllPage

    @AllPage.setter
    def AllPage(self, AllPage):
        self._AllPage = AllPage

    @property
    def UserType(self):
        r"""0: enterprise user. 1: visitor. If left blank, it indicates all users.
        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def Keyword(self):
        r"""Keyword for fuzzy search.
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def IsOnlyBindAppUser(self):
        r"""Whether to only obtain users bound to the WeCom app.
        :rtype: bool
        """
        return self._IsOnlyBindAppUser

    @IsOnlyBindAppUser.setter
    def IsOnlyBindAppUser(self, IsOnlyBindAppUser):
        self._IsOnlyBindAppUser = IsOnlyBindAppUser


    def _deserialize(self, params):
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._AllPage = params.get("AllPage")
        self._UserType = params.get("UserType")
        self._Keyword = params.get("Keyword")
        self._ProjectId = params.get("ProjectId")
        self._IsOnlyBindAppUser = params.get("IsOnlyBindAppUser")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserRoleListResponse(AbstractModel):
    r"""DescribeUserRoleList response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Extension description information (providing more exception messages for auxiliary judgment).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Data: Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.UserRoleListData`
        :param _Msg: Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Extension description information (providing more exception messages for auxiliary judgment).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        r"""Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.UserRoleListData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Msg(self):
        r"""Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = UserRoleListData()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeUserRoleProjectListRequest(AbstractModel):
    r"""DescribeUserRoleProjectList request structure.

    """

    def __init__(self):
        r"""
        :param _PageNo: Page number.
        :type PageNo: int
        :param _PageSize: Number of pages.
        :type PageSize: int
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _IsOnlyBindAppUser: Whether to only obtain users bound to the WeCom app.
        :type IsOnlyBindAppUser: bool
        :param _AllPage: Whether to obtain all the data.
        :type AllPage: bool
        :param _RoleCode: Role code.
        :type RoleCode: str
        :param _UserIdList: User ID list.
        :type UserIdList: list of str
        :param _Keyword: Search keywords.
        :type Keyword: str
        """
        self._PageNo = None
        self._PageSize = None
        self._ProjectId = None
        self._IsOnlyBindAppUser = None
        self._AllPage = None
        self._RoleCode = None
        self._UserIdList = None
        self._Keyword = None

    @property
    def PageNo(self):
        r"""Page number.
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        r"""Number of pages.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def IsOnlyBindAppUser(self):
        r"""Whether to only obtain users bound to the WeCom app.
        :rtype: bool
        """
        return self._IsOnlyBindAppUser

    @IsOnlyBindAppUser.setter
    def IsOnlyBindAppUser(self, IsOnlyBindAppUser):
        self._IsOnlyBindAppUser = IsOnlyBindAppUser

    @property
    def AllPage(self):
        r"""Whether to obtain all the data.
        :rtype: bool
        """
        return self._AllPage

    @AllPage.setter
    def AllPage(self, AllPage):
        self._AllPage = AllPage

    @property
    def RoleCode(self):
        r"""Role code.
        :rtype: str
        """
        return self._RoleCode

    @RoleCode.setter
    def RoleCode(self, RoleCode):
        self._RoleCode = RoleCode

    @property
    def UserIdList(self):
        r"""User ID list.
        :rtype: list of str
        """
        return self._UserIdList

    @UserIdList.setter
    def UserIdList(self, UserIdList):
        self._UserIdList = UserIdList

    @property
    def Keyword(self):
        r"""Search keywords.
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._ProjectId = params.get("ProjectId")
        self._IsOnlyBindAppUser = params.get("IsOnlyBindAppUser")
        self._AllPage = params.get("AllPage")
        self._RoleCode = params.get("RoleCode")
        self._UserIdList = params.get("UserIdList")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserRoleProjectListResponse(AbstractModel):
    r"""DescribeUserRoleProjectList response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Data: Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.UserRoleListData`
        :param _Msg: Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        r"""Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.UserRoleListData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Msg(self):
        r"""Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = UserRoleListData()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class EditCorpTagRequest(AbstractModel):
    r"""EditCorpTag request structure.

    """

    def __init__(self):
        r"""
        :param _Id: tag ID
        :type Id: int
        :param _Name: Tag name.
        :type Name: str
        :param _ImportType: Import tag mode (manual/auto)
        :type ImportType: str
        :param _AutoImportTagTableId: id of the tag table for automatic import
        :type AutoImportTagTableId: int
        :param _AutoImportField: Automatic import of associated tag fields
        :type AutoImportField: str
        :param _AsyncRequest: Whether it is an async request.
        :type AsyncRequest: bool
        :param _AutoImportTagTableName: Name of the tag table for automatic import
        :type AutoImportTagTableName: str
        :param _TranId: Transaction ID.
        :type TranId: str
        """
        self._Id = None
        self._Name = None
        self._ImportType = None
        self._AutoImportTagTableId = None
        self._AutoImportField = None
        self._AsyncRequest = None
        self._AutoImportTagTableName = None
        self._TranId = None

    @property
    def Id(self):
        r"""tag ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""Tag name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ImportType(self):
        r"""Import tag mode (manual/auto)
        :rtype: str
        """
        return self._ImportType

    @ImportType.setter
    def ImportType(self, ImportType):
        self._ImportType = ImportType

    @property
    def AutoImportTagTableId(self):
        r"""id of the tag table for automatic import
        :rtype: int
        """
        return self._AutoImportTagTableId

    @AutoImportTagTableId.setter
    def AutoImportTagTableId(self, AutoImportTagTableId):
        self._AutoImportTagTableId = AutoImportTagTableId

    @property
    def AutoImportField(self):
        r"""Automatic import of associated tag fields
        :rtype: str
        """
        return self._AutoImportField

    @AutoImportField.setter
    def AutoImportField(self, AutoImportField):
        self._AutoImportField = AutoImportField

    @property
    def AsyncRequest(self):
        r"""Whether it is an async request.
        :rtype: bool
        """
        return self._AsyncRequest

    @AsyncRequest.setter
    def AsyncRequest(self, AsyncRequest):
        self._AsyncRequest = AsyncRequest

    @property
    def AutoImportTagTableName(self):
        r"""Name of the tag table for automatic import
        :rtype: str
        """
        return self._AutoImportTagTableName

    @AutoImportTagTableName.setter
    def AutoImportTagTableName(self, AutoImportTagTableName):
        self._AutoImportTagTableName = AutoImportTagTableName

    @property
    def TranId(self):
        r"""Transaction ID.
        :rtype: str
        """
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._ImportType = params.get("ImportType")
        self._AutoImportTagTableId = params.get("AutoImportTagTableId")
        self._AutoImportField = params.get("AutoImportField")
        self._AsyncRequest = params.get("AsyncRequest")
        self._AutoImportTagTableName = params.get("AutoImportTagTableName")
        self._TranId = params.get("TranId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditCorpTagResponse(AbstractModel):
    r"""EditCorpTag response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _Data: Data.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.EditTagVO`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Msg = None
        self._Data = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Data(self):
        r"""Data.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.EditTagVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        if params.get("Data") is not None:
            self._Data = EditTagVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class EditTagVO(AbstractModel):
    r"""Sync tag data output parameters

    """

    def __init__(self):
        r"""
        :param _TranId: Transaction ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TranId: str
        :param _TranStatus: Transaction status
Note: This field may return null, indicating that no valid values can be obtained.
        :type TranStatus: int
        :param _Id: Tag information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: int
        """
        self._TranId = None
        self._TranStatus = None
        self._Id = None

    @property
    def TranId(self):
        r"""Transaction ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def TranStatus(self):
        r"""Transaction status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TranStatus

    @TranStatus.setter
    def TranStatus(self, TranStatus):
        self._TranStatus = TranStatus

    @property
    def Id(self):
        r"""Tag information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._TranId = params.get("TranId")
        self._TranStatus = params.get("TranStatus")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmbedTokenInfo(AbstractModel):
    r"""Report embedding data structure with strong authentication

    """

    def __init__(self):
        r"""
        :param _Id: Information identifier.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: int
        :param _BIToken: Token.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BIToken: str
        :param _ProjectId: Project ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectId: str
        :param _CreatedUser: Creator.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedUser: str
        :param _CreatedAt: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedAt: str
        :param _UpdatedUser: Updater.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdatedUser: str
        :param _UpdatedAt: Update time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdatedAt: str
        :param _PageId: Page ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageId: str
        :param _ExtraParam: Backup.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtraParam: str
        :param _Scope: Embedding type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Scope: str
        :param _ExpireTime: Expiration time (in minutes), with a maximum value of 240.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: int
        :param _UserCorpId: User enterprise ID (only used for multi-user).
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserCorpId: str
        :param _UserId: User ID (only used for multi-user).
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param _TicketNum: Access count limit (range: 1–99999). Leave empty to disable access restrictions.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TicketNum: int
        :param _GlobalParam: Global parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GlobalParam: str
        :param _Intention: "embed" indicates page dashboard embedding, and "chatBIEmbed" indicates ChatBI embedding.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Intention: str
        :param _TokenType: 100: no bound user.
200: single token per user.
300: multiple tokens per user.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TokenType: int
        :param _TokenNum: Number of tokens.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TokenNum: int
        :param _SingleUserMultiToken: Whether it is multiple tokens per user.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SingleUserMultiToken: bool
        :param _ConfigParam: Embedded display configurations: Currently for ChatBI embedding scenarios; TableFilter represents data table list filtering, SqlView represents SQL view feature.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConfigParam: str
        """
        self._Id = None
        self._BIToken = None
        self._ProjectId = None
        self._CreatedUser = None
        self._CreatedAt = None
        self._UpdatedUser = None
        self._UpdatedAt = None
        self._PageId = None
        self._ExtraParam = None
        self._Scope = None
        self._ExpireTime = None
        self._UserCorpId = None
        self._UserId = None
        self._TicketNum = None
        self._GlobalParam = None
        self._Intention = None
        self._TokenType = None
        self._TokenNum = None
        self._SingleUserMultiToken = None
        self._ConfigParam = None

    @property
    def Id(self):
        r"""Information identifier.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def BIToken(self):
        r"""Token.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BIToken

    @BIToken.setter
    def BIToken(self, BIToken):
        self._BIToken = BIToken

    @property
    def ProjectId(self):
        r"""Project ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreatedUser(self):
        r"""Creator.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatedUser

    @CreatedUser.setter
    def CreatedUser(self, CreatedUser):
        self._CreatedUser = CreatedUser

    @property
    def CreatedAt(self):
        r"""Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedUser(self):
        r"""Updater.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdatedUser

    @UpdatedUser.setter
    def UpdatedUser(self, UpdatedUser):
        self._UpdatedUser = UpdatedUser

    @property
    def UpdatedAt(self):
        r"""Update time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def PageId(self):
        r"""Page ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def ExtraParam(self):
        r"""Backup.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def Scope(self):
        r"""Embedding type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def ExpireTime(self):
        r"""Expiration time (in minutes), with a maximum value of 240.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def UserCorpId(self):
        r"""User enterprise ID (only used for multi-user).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserCorpId

    @UserCorpId.setter
    def UserCorpId(self, UserCorpId):
        self._UserCorpId = UserCorpId

    @property
    def UserId(self):
        r"""User ID (only used for multi-user).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def TicketNum(self):
        r"""Access count limit (range: 1–99999). Leave empty to disable access restrictions.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TicketNum

    @TicketNum.setter
    def TicketNum(self, TicketNum):
        self._TicketNum = TicketNum

    @property
    def GlobalParam(self):
        r"""Global parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._GlobalParam

    @GlobalParam.setter
    def GlobalParam(self, GlobalParam):
        self._GlobalParam = GlobalParam

    @property
    def Intention(self):
        r""""embed" indicates page dashboard embedding, and "chatBIEmbed" indicates ChatBI embedding.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Intention

    @Intention.setter
    def Intention(self, Intention):
        self._Intention = Intention

    @property
    def TokenType(self):
        r"""100: no bound user.
200: single token per user.
300: multiple tokens per user.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TokenType

    @TokenType.setter
    def TokenType(self, TokenType):
        self._TokenType = TokenType

    @property
    def TokenNum(self):
        r"""Number of tokens.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TokenNum

    @TokenNum.setter
    def TokenNum(self, TokenNum):
        self._TokenNum = TokenNum

    @property
    def SingleUserMultiToken(self):
        r"""Whether it is multiple tokens per user.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._SingleUserMultiToken

    @SingleUserMultiToken.setter
    def SingleUserMultiToken(self, SingleUserMultiToken):
        self._SingleUserMultiToken = SingleUserMultiToken

    @property
    def ConfigParam(self):
        r"""Embedded display configurations: Currently for ChatBI embedding scenarios; TableFilter represents data table list filtering, SqlView represents SQL view feature.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ConfigParam

    @ConfigParam.setter
    def ConfigParam(self, ConfigParam):
        self._ConfigParam = ConfigParam


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._BIToken = params.get("BIToken")
        self._ProjectId = params.get("ProjectId")
        self._CreatedUser = params.get("CreatedUser")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedUser = params.get("UpdatedUser")
        self._UpdatedAt = params.get("UpdatedAt")
        self._PageId = params.get("PageId")
        self._ExtraParam = params.get("ExtraParam")
        self._Scope = params.get("Scope")
        self._ExpireTime = params.get("ExpireTime")
        self._UserCorpId = params.get("UserCorpId")
        self._UserId = params.get("UserId")
        self._TicketNum = params.get("TicketNum")
        self._GlobalParam = params.get("GlobalParam")
        self._Intention = params.get("Intention")
        self._TokenType = params.get("TokenType")
        self._TokenNum = params.get("TokenNum")
        self._SingleUserMultiToken = params.get("SingleUserMultiToken")
        self._ConfigParam = params.get("ConfigParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmptyValue(AbstractModel):
    r"""Empty value display style configuration value structure

    """

    def __init__(self):
        r"""
        :param _Type: Empty value display style type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _Custom: Display style type for null values corresponds to specific display string
Note: This field may return null, indicating that no valid values can be obtained.
        :type Custom: str
        """
        self._Type = None
        self._Custom = None

    @property
    def Type(self):
        r"""Empty value display style type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Custom(self):
        r"""Display style type for null values corresponds to specific display string
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Custom

    @Custom.setter
    def Custom(self, Custom):
        self._Custom = Custom


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Custom = params.get("Custom")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmptyValueConfig(AbstractModel):
    r"""Empty value display style configuration structure

    """

    def __init__(self):
        r"""
        :param _Number: Numeric value field null style configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Number: :class:`tencentcloud.bi.v20220105.models.EmptyValue`
        :param _String: Style configuration for empty string fields
Note: This field may return null, indicating that no valid values can be obtained.
        :type String: :class:`tencentcloud.bi.v20220105.models.EmptyValue`
        """
        self._Number = None
        self._String = None

    @property
    def Number(self):
        r"""Numeric value field null style configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.EmptyValue`
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def String(self):
        r"""Style configuration for empty string fields
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.EmptyValue`
        """
        return self._String

    @String.setter
    def String(self, String):
        self._String = String


    def _deserialize(self, params):
        if params.get("Number") is not None:
            self._Number = EmptyValue()
            self._Number._deserialize(params.get("Number"))
        if params.get("String") is not None:
            self._String = EmptyValue()
            self._String._deserialize(params.get("String"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorInfo(AbstractModel):
    r"""Custom error information object

    """

    def __init__(self):
        r"""
        :param _ErrorTip: Error description field.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorTip: str
        :param _ErrorMessage: Original exception message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMessage: str
        :param _ErrorLevel: Error level field.
ERROR
WARN
INFO
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorLevel: str
        :param _DocLink: Documentation link.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DocLink: str
        :param _FAQ: Quick start guide.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FAQ: str
        :param _ReservedField: Reserved field 1.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReservedField: str
        """
        self._ErrorTip = None
        self._ErrorMessage = None
        self._ErrorLevel = None
        self._DocLink = None
        self._FAQ = None
        self._ReservedField = None

    @property
    def ErrorTip(self):
        r"""Error description field.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorTip

    @ErrorTip.setter
    def ErrorTip(self, ErrorTip):
        self._ErrorTip = ErrorTip

    @property
    def ErrorMessage(self):
        r"""Original exception message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ErrorLevel(self):
        r"""Error level field.
ERROR
WARN
INFO
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorLevel

    @ErrorLevel.setter
    def ErrorLevel(self, ErrorLevel):
        self._ErrorLevel = ErrorLevel

    @property
    def DocLink(self):
        r"""Documentation link.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DocLink

    @DocLink.setter
    def DocLink(self, DocLink):
        self._DocLink = DocLink

    @property
    def FAQ(self):
        r"""Quick start guide.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FAQ

    @FAQ.setter
    def FAQ(self, FAQ):
        self._FAQ = FAQ

    @property
    def ReservedField(self):
        r"""Reserved field 1.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ReservedField

    @ReservedField.setter
    def ReservedField(self, ReservedField):
        self._ReservedField = ReservedField


    def _deserialize(self, params):
        self._ErrorTip = params.get("ErrorTip")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ErrorLevel = params.get("ErrorLevel")
        self._DocLink = params.get("DocLink")
        self._FAQ = params.get("FAQ")
        self._ReservedField = params.get("ReservedField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportScreenPageRequest(AbstractModel):
    r"""ExportScreenPage request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _PageId: Page ID.
        :type PageId: str
        :param _CanvasType: Canvas type. Grid canvas: GRID; Free canvas: FREE.
        :type CanvasType: str
        :param _PicType: Image export type. Valid values: Base64, and URL (valid period: 1 day).
        :type PicType: str
        :param _WidgetIds: Component IDs. When empty, export the entire page.
        :type WidgetIds: list of str
        :param _AsyncRequest: Whether it is an async request.
        :type AsyncRequest: bool
        :param _TranId: Transaction ID.
        :type TranId: str
        """
        self._ProjectId = None
        self._PageId = None
        self._CanvasType = None
        self._PicType = None
        self._WidgetIds = None
        self._AsyncRequest = None
        self._TranId = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageId(self):
        r"""Page ID.
        :rtype: str
        """
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def CanvasType(self):
        r"""Canvas type. Grid canvas: GRID; Free canvas: FREE.
        :rtype: str
        """
        return self._CanvasType

    @CanvasType.setter
    def CanvasType(self, CanvasType):
        self._CanvasType = CanvasType

    @property
    def PicType(self):
        r"""Image export type. Valid values: Base64, and URL (valid period: 1 day).
        :rtype: str
        """
        return self._PicType

    @PicType.setter
    def PicType(self, PicType):
        self._PicType = PicType

    @property
    def WidgetIds(self):
        r"""Component IDs. When empty, export the entire page.
        :rtype: list of str
        """
        return self._WidgetIds

    @WidgetIds.setter
    def WidgetIds(self, WidgetIds):
        self._WidgetIds = WidgetIds

    @property
    def AsyncRequest(self):
        r"""Whether it is an async request.
        :rtype: bool
        """
        return self._AsyncRequest

    @AsyncRequest.setter
    def AsyncRequest(self, AsyncRequest):
        self._AsyncRequest = AsyncRequest

    @property
    def TranId(self):
        r"""Transaction ID.
        :rtype: str
        """
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageId = params.get("PageId")
        self._CanvasType = params.get("CanvasType")
        self._PicType = params.get("PicType")
        self._WidgetIds = params.get("WidgetIds")
        self._AsyncRequest = params.get("AsyncRequest")
        self._TranId = params.get("TranId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportScreenPageResponse(AbstractModel):
    r"""ExportScreenPage response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Extension parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Data: Returned data results.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.PageScreenListVO`
        :param _Msg: Response message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Extension parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        r"""Returned data results.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.PageScreenListVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Msg(self):
        r"""Response message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = PageScreenListVO()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class FieldRemarkDTO(AbstractModel):
    r"""Field remarks

    """

    def __init__(self):
        r"""
        :param _FieldName: field name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FieldName: str
        :param _Comment: Field remarks list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Comment: list of str
        """
        self._FieldName = None
        self._Comment = None

    @property
    def FieldName(self):
        r"""field name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def Comment(self):
        r"""Field remarks list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._FieldName = params.get("FieldName")
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrequencyConfig(AbstractModel):
    r"""Scheduled task execution frequency configuration

    """

    def __init__(self):
        r"""
        :param _Frequency: Cycle
Note: This field may return null, indicating that no valid values can be obtained.
        :type Frequency: str
        :param _Dates: Date
Note: This field may return null, indicating that no valid values can be obtained.
        :type Dates: list of int
        :param _Time: Time
Note: This field may return null, indicating that no valid values can be obtained.
        :type Time: str
        :param _IntervalTime: Interval
Note: This field may return null, indicating that no valid values can be obtained.
        :type IntervalTime: int
        :param _IntervalTimeUnit: 1:SECOND,2:MINUTE,3:HOUR,4:DAY
Note: This field may return null, indicating that no valid values can be obtained.
        :type IntervalTimeUnit: int
        :param _Hours: hourly list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Hours: list of int
        :param _Minute: Minute list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Minute: list of int
        """
        self._Frequency = None
        self._Dates = None
        self._Time = None
        self._IntervalTime = None
        self._IntervalTimeUnit = None
        self._Hours = None
        self._Minute = None

    @property
    def Frequency(self):
        r"""Cycle
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def Dates(self):
        r"""Date
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._Dates

    @Dates.setter
    def Dates(self, Dates):
        self._Dates = Dates

    @property
    def Time(self):
        r"""Time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def IntervalTime(self):
        r"""Interval
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def IntervalTimeUnit(self):
        r"""1:SECOND,2:MINUTE,3:HOUR,4:DAY
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IntervalTimeUnit

    @IntervalTimeUnit.setter
    def IntervalTimeUnit(self, IntervalTimeUnit):
        self._IntervalTimeUnit = IntervalTimeUnit

    @property
    def Hours(self):
        r"""hourly list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._Hours

    @Hours.setter
    def Hours(self, Hours):
        self._Hours = Hours

    @property
    def Minute(self):
        r"""Minute list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._Minute

    @Minute.setter
    def Minute(self, Minute):
        self._Minute = Minute


    def _deserialize(self, params):
        self._Frequency = params.get("Frequency")
        self._Dates = params.get("Dates")
        self._Time = params.get("Time")
        self._IntervalTime = params.get("IntervalTime")
        self._IntervalTimeUnit = params.get("IntervalTimeUnit")
        self._Hours = params.get("Hours")
        self._Minute = params.get("Minute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdDTO(AbstractModel):
    r"""Object containing only ID

    """

    def __init__(self):
        r"""
        :param _Id: Request ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: int
        :param _AccessKey: key
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessKey: str
        :param _ProjectId: id
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param _TranId: Transaction ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TranId: str
        :param _TranStatus: Transaction status.
Value range:.
Processing.
2: processing is successful.
3: processing failure.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TranStatus: int
        """
        self._Id = None
        self._AccessKey = None
        self._ProjectId = None
        self._TranId = None
        self._TranStatus = None

    @property
    def Id(self):
        r"""Request ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AccessKey(self):
        r"""key
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def ProjectId(self):
        r"""id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TranId(self):
        r"""Transaction ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def TranStatus(self):
        r"""Transaction status.
Value range:.
Processing.
2: processing is successful.
3: processing failure.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TranStatus

    @TranStatus.setter
    def TranStatus(self, TranStatus):
        self._TranStatus = TranStatus


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._AccessKey = params.get("AccessKey")
        self._ProjectId = params.get("ProjectId")
        self._TranId = params.get("TranId")
        self._TranStatus = params.get("TranStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinRelation(AbstractModel):
    r"""Join tables and view association information between original tables

    """

    def __init__(self):
        r"""
        :param _JoinId: Association relationship id, used by the frontend
Note: This field may return null, indicating that no valid values can be obtained.
        :type JoinId: str
        :param _SourceTableNodeId: Original table node id
Note: This field may return null, indicating that no valid values can be obtained.
        :type SourceTableNodeId: str
        :param _TargetTableNodeId: Target table node id
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetTableNodeId: str
        :param _JoinType: Association type of multi-table join
Note: This field may return null, indicating that no valid values can be obtained.
        :type JoinType: str
        :param _Fields: Field list for joined tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type Fields: list of JoinRelationField
        """
        self._JoinId = None
        self._SourceTableNodeId = None
        self._TargetTableNodeId = None
        self._JoinType = None
        self._Fields = None

    @property
    def JoinId(self):
        r"""Association relationship id, used by the frontend
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JoinId

    @JoinId.setter
    def JoinId(self, JoinId):
        self._JoinId = JoinId

    @property
    def SourceTableNodeId(self):
        r"""Original table node id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SourceTableNodeId

    @SourceTableNodeId.setter
    def SourceTableNodeId(self, SourceTableNodeId):
        self._SourceTableNodeId = SourceTableNodeId

    @property
    def TargetTableNodeId(self):
        r"""Target table node id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TargetTableNodeId

    @TargetTableNodeId.setter
    def TargetTableNodeId(self, TargetTableNodeId):
        self._TargetTableNodeId = TargetTableNodeId

    @property
    def JoinType(self):
        r"""Association type of multi-table join
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JoinType

    @JoinType.setter
    def JoinType(self, JoinType):
        self._JoinType = JoinType

    @property
    def Fields(self):
        r"""Field list for joined tables
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of JoinRelationField
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields


    def _deserialize(self, params):
        self._JoinId = params.get("JoinId")
        self._SourceTableNodeId = params.get("SourceTableNodeId")
        self._TargetTableNodeId = params.get("TargetTableNodeId")
        self._JoinType = params.get("JoinType")
        if params.get("Fields") is not None:
            self._Fields = []
            for item in params.get("Fields"):
                obj = JoinRelationField()
                obj._deserialize(item)
                self._Fields.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinRelationField(AbstractModel):
    r"""Join tables and view association information between original tables

    """

    def __init__(self):
        r"""
        :param _FieldJoinId: Field association id, frontend usage
Note: This field may return null, indicating that no valid values can be obtained.
        :type FieldJoinId: str
        :param _SourceField: Original table field
Note: This field may return null, indicating that no valid values can be obtained.
        :type SourceField: :class:`tencentcloud.bi.v20220105.models.TableField`
        :param _TargetField: Target table field
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetField: :class:`tencentcloud.bi.v20220105.models.TableField`
        """
        self._FieldJoinId = None
        self._SourceField = None
        self._TargetField = None

    @property
    def FieldJoinId(self):
        r"""Field association id, frontend usage
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FieldJoinId

    @FieldJoinId.setter
    def FieldJoinId(self, FieldJoinId):
        self._FieldJoinId = FieldJoinId

    @property
    def SourceField(self):
        r"""Original table field
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.TableField`
        """
        return self._SourceField

    @SourceField.setter
    def SourceField(self, SourceField):
        self._SourceField = SourceField

    @property
    def TargetField(self):
        r"""Target table field
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.TableField`
        """
        return self._TargetField

    @TargetField.setter
    def TargetField(self, TargetField):
        self._TargetField = TargetField


    def _deserialize(self, params):
        self._FieldJoinId = params.get("FieldJoinId")
        if params.get("SourceField") is not None:
            self._SourceField = TableField()
            self._SourceField._deserialize(params.get("SourceField"))
        if params.get("TargetField") is not None:
            self._TargetField = TableField()
            self._TargetField._deserialize(params.get("TargetField"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinSourceTable(AbstractModel):
    r"""Join tables and view original table information

    """

    def __init__(self):
        r"""
        :param _TableNodeType: 1: Data source original table, 2: Local table, 3: Excel table, 4: API table
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableNodeType: int
        :param _TableNodeId: Base Table Node Id
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableNodeId: str
        :param _ParentId: Parent node ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ParentId: str
        :param _TableId: Optional, the data source has no ID in the original table.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableId: str
        :param _TableName: Required. Use the original table name for the data source. Use the logical table name for other types.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param _Fields: Field list to display in the base table
Note: This field may return null, indicating that no valid values can be obtained.
        :type Fields: list of TableField
        :param _DatasourceId: Data source ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DatasourceId: int
        :param _TableAlias: Optional, alias of the data source displayed on the front-end, excel table creation is required
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableAlias: str
        """
        self._TableNodeType = None
        self._TableNodeId = None
        self._ParentId = None
        self._TableId = None
        self._TableName = None
        self._Fields = None
        self._DatasourceId = None
        self._TableAlias = None

    @property
    def TableNodeType(self):
        r"""1: Data source original table, 2: Local table, 3: Excel table, 4: API table
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TableNodeType

    @TableNodeType.setter
    def TableNodeType(self, TableNodeType):
        self._TableNodeType = TableNodeType

    @property
    def TableNodeId(self):
        r"""Base Table Node Id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableNodeId

    @TableNodeId.setter
    def TableNodeId(self, TableNodeId):
        self._TableNodeId = TableNodeId

    @property
    def ParentId(self):
        r"""Parent node ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def TableId(self):
        r"""Optional, the data source has no ID in the original table.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def TableName(self):
        r"""Required. Use the original table name for the data source. Use the logical table name for other types.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Fields(self):
        r"""Field list to display in the base table
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TableField
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def DatasourceId(self):
        r"""Data source ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DatasourceId

    @DatasourceId.setter
    def DatasourceId(self, DatasourceId):
        self._DatasourceId = DatasourceId

    @property
    def TableAlias(self):
        r"""Optional, alias of the data source displayed on the front-end, excel table creation is required
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableAlias

    @TableAlias.setter
    def TableAlias(self, TableAlias):
        self._TableAlias = TableAlias


    def _deserialize(self, params):
        self._TableNodeType = params.get("TableNodeType")
        self._TableNodeId = params.get("TableNodeId")
        self._ParentId = params.get("ParentId")
        self._TableId = params.get("TableId")
        self._TableName = params.get("TableName")
        if params.get("Fields") is not None:
            self._Fields = []
            for item in params.get("Fields"):
                obj = TableField()
                obj._deserialize(item)
                self._Fields.append(obj)
        self._DatasourceId = params.get("DatasourceId")
        self._TableAlias = params.get("TableAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatasourceCloudRequest(AbstractModel):
    r"""ModifyDatasourceCloud request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceType: The backend provides dictionaries: domain type. 1: Tencent Cloud; 2: local.
        :type ServiceType: str
        :param _DbType: Drive.
Value range:.
MYSQL: MYSQL database.
PRESTO: presto database.
POSTGRE: PostgreSQL database.
DLC: dlc database.
MSSQL: microsoft SQL Server database.
        :type DbType: str
        :param _Charset: Database encoding.
        :type Charset: str
        :param _DbUser: Username.
        :type DbUser: str
        :param _DbPwd: Password.
        :type DbPwd: str
        :param _DbName: Database name.
        :type DbName: str
        :param _SourceName: Database alias.
        :type SourceName: str
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _Id: Primary key.
        :type Id: int
        :param _Vip: Private network IP address of the public cloud.
        :type Vip: str
        :param _Vport: Private network port of the public cloud.
        :type Vport: str
        :param _VpcId: VPC identifier.
        :type VpcId: str
        :param _UniqVpcId: Unified VPC identifier.
        :type UniqVpcId: str
        :param _RegionId: Region identifier (gz, bj).
        :type RegionId: str
        :param _ExtraParam: Extension parameter.
        :type ExtraParam: str
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _ProdDbName: Product name of the data source.
        :type ProdDbName: str
        :param _DataOrigin: Third-party data source identifier.
        :type DataOrigin: str
        :param _DataOriginProjectId: Third-party project ID.
        :type DataOriginProjectId: str
        :param _DataOriginDatasourceId: Third-party data source ID.
        :type DataOriginDatasourceId: str
        :param _ClusterId: Cluster ID.
        :type ClusterId: str
        :param _Schema: Database schema.
        :type Schema: str
        :param _DbVersion: Database version.
        :type DbVersion: str
        """
        self._ServiceType = None
        self._DbType = None
        self._Charset = None
        self._DbUser = None
        self._DbPwd = None
        self._DbName = None
        self._SourceName = None
        self._ProjectId = None
        self._Id = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None
        self._UniqVpcId = None
        self._RegionId = None
        self._ExtraParam = None
        self._InstanceId = None
        self._ProdDbName = None
        self._DataOrigin = None
        self._DataOriginProjectId = None
        self._DataOriginDatasourceId = None
        self._ClusterId = None
        self._Schema = None
        self._DbVersion = None

    @property
    def ServiceType(self):
        r"""The backend provides dictionaries: domain type. 1: Tencent Cloud; 2: local.
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def DbType(self):
        r"""Drive.
Value range:.
MYSQL: MYSQL database.
PRESTO: presto database.
POSTGRE: PostgreSQL database.
DLC: dlc database.
MSSQL: microsoft SQL Server database.
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Charset(self):
        r"""Database encoding.
        :rtype: str
        """
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def DbUser(self):
        r"""Username.
        :rtype: str
        """
        return self._DbUser

    @DbUser.setter
    def DbUser(self, DbUser):
        self._DbUser = DbUser

    @property
    def DbPwd(self):
        r"""Password.
        :rtype: str
        """
        return self._DbPwd

    @DbPwd.setter
    def DbPwd(self, DbPwd):
        self._DbPwd = DbPwd

    @property
    def DbName(self):
        r"""Database name.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SourceName(self):
        r"""Database alias.
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Id(self):
        r"""Primary key.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Vip(self):
        r"""Private network IP address of the public cloud.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""Private network port of the public cloud.
        :rtype: str
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        r"""VPC identifier.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def UniqVpcId(self):
        r"""Unified VPC identifier.
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def RegionId(self):
        r"""Region identifier (gz, bj).
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ExtraParam(self):
        r"""Extension parameter.
        :rtype: str
        """
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProdDbName(self):
        r"""Product name of the data source.
        :rtype: str
        """
        return self._ProdDbName

    @ProdDbName.setter
    def ProdDbName(self, ProdDbName):
        self._ProdDbName = ProdDbName

    @property
    def DataOrigin(self):
        r"""Third-party data source identifier.
        :rtype: str
        """
        return self._DataOrigin

    @DataOrigin.setter
    def DataOrigin(self, DataOrigin):
        self._DataOrigin = DataOrigin

    @property
    def DataOriginProjectId(self):
        r"""Third-party project ID.
        :rtype: str
        """
        return self._DataOriginProjectId

    @DataOriginProjectId.setter
    def DataOriginProjectId(self, DataOriginProjectId):
        self._DataOriginProjectId = DataOriginProjectId

    @property
    def DataOriginDatasourceId(self):
        r"""Third-party data source ID.
        :rtype: str
        """
        return self._DataOriginDatasourceId

    @DataOriginDatasourceId.setter
    def DataOriginDatasourceId(self, DataOriginDatasourceId):
        self._DataOriginDatasourceId = DataOriginDatasourceId

    @property
    def ClusterId(self):
        r"""Cluster ID.
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Schema(self):
        r"""Database schema.
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def DbVersion(self):
        r"""Database version.
        :rtype: str
        """
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._DbType = params.get("DbType")
        self._Charset = params.get("Charset")
        self._DbUser = params.get("DbUser")
        self._DbPwd = params.get("DbPwd")
        self._DbName = params.get("DbName")
        self._SourceName = params.get("SourceName")
        self._ProjectId = params.get("ProjectId")
        self._Id = params.get("Id")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._RegionId = params.get("RegionId")
        self._ExtraParam = params.get("ExtraParam")
        self._InstanceId = params.get("InstanceId")
        self._ProdDbName = params.get("ProdDbName")
        self._DataOrigin = params.get("DataOrigin")
        self._DataOriginProjectId = params.get("DataOriginProjectId")
        self._DataOriginDatasourceId = params.get("DataOriginDatasourceId")
        self._ClusterId = params.get("ClusterId")
        self._Schema = params.get("Schema")
        self._DbVersion = params.get("DbVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatasourceCloudResponse(AbstractModel):
    r"""ModifyDatasourceCloud response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Data: None.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: str
        :param _Extra: Additional information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: Prompt.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Data = None
        self._Extra = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Data(self):
        r"""None.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Extra(self):
        r"""Additional information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Prompt.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Data = params.get("Data")
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ModifyDatasourceRequest(AbstractModel):
    r"""ModifyDatasource request structure.

    """

    def __init__(self):
        r"""
        :param _DbHost: HOST
        :type DbHost: str
        :param _DbPort: Port.
        :type DbPort: int
        :param _ServiceType: The backend provides dictionaries: domain type. 1: Tencent Cloud; 2: local.
        :type ServiceType: str
        :param _DbType: Drive.
Value range:.
MYSQL: MYSQL database.
PRESTO: presto database.
POSTGRE: PostgreSQL database.
DLC: dlc database.
MSSQL: microsoft SQL Server database.
        :type DbType: str
        :param _Charset: Database encoding.
        :type Charset: str
        :param _DbUser: Username.
        :type DbUser: str
        :param _DbPwd: Password.
        :type DbPwd: str
        :param _DbName: Database name.
        :type DbName: str
        :param _SourceName: Database alias.
        :type SourceName: str
        :param _Id: Data source ID.
        :type Id: int
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _Catalog: Catalog value.
        :type Catalog: str
        :param _DataOrigin: Third-party data source identifier.
        :type DataOrigin: str
        :param _DataOriginProjectId: Third-party project ID.
        :type DataOriginProjectId: str
        :param _DataOriginDatasourceId: Third-party data source ID.
        :type DataOriginDatasourceId: str
        :param _ExtraParam: Extension parameter.
        :type ExtraParam: str
        :param _UniqVpcId: Unified identifier of the Tencent Cloud VPC.
        :type UniqVpcId: str
        :param _Vip: VPC IP address.
        :type Vip: str
        :param _Vport: VPC port.
        :type Vport: str
        :param _VpcId: Tencent Cloud VPC identifier.
        :type VpcId: str
        :param _UseVPC: Enable VPC.  
        :type UseVPC: bool
        :param _RegionId: Region.
        :type RegionId: str
        :param _Schema: Database schema.
        :type Schema: str
        :param _DbVersion: Database version.
        :type DbVersion: str
        """
        self._DbHost = None
        self._DbPort = None
        self._ServiceType = None
        self._DbType = None
        self._Charset = None
        self._DbUser = None
        self._DbPwd = None
        self._DbName = None
        self._SourceName = None
        self._Id = None
        self._ProjectId = None
        self._Catalog = None
        self._DataOrigin = None
        self._DataOriginProjectId = None
        self._DataOriginDatasourceId = None
        self._ExtraParam = None
        self._UniqVpcId = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None
        self._UseVPC = None
        self._RegionId = None
        self._Schema = None
        self._DbVersion = None

    @property
    def DbHost(self):
        r"""HOST
        :rtype: str
        """
        return self._DbHost

    @DbHost.setter
    def DbHost(self, DbHost):
        self._DbHost = DbHost

    @property
    def DbPort(self):
        r"""Port.
        :rtype: int
        """
        return self._DbPort

    @DbPort.setter
    def DbPort(self, DbPort):
        self._DbPort = DbPort

    @property
    def ServiceType(self):
        r"""The backend provides dictionaries: domain type. 1: Tencent Cloud; 2: local.
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def DbType(self):
        r"""Drive.
Value range:.
MYSQL: MYSQL database.
PRESTO: presto database.
POSTGRE: PostgreSQL database.
DLC: dlc database.
MSSQL: microsoft SQL Server database.
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Charset(self):
        r"""Database encoding.
        :rtype: str
        """
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def DbUser(self):
        r"""Username.
        :rtype: str
        """
        return self._DbUser

    @DbUser.setter
    def DbUser(self, DbUser):
        self._DbUser = DbUser

    @property
    def DbPwd(self):
        r"""Password.
        :rtype: str
        """
        return self._DbPwd

    @DbPwd.setter
    def DbPwd(self, DbPwd):
        self._DbPwd = DbPwd

    @property
    def DbName(self):
        r"""Database name.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SourceName(self):
        r"""Database alias.
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def Id(self):
        r"""Data source ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Catalog(self):
        r"""Catalog value.
        :rtype: str
        """
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def DataOrigin(self):
        r"""Third-party data source identifier.
        :rtype: str
        """
        return self._DataOrigin

    @DataOrigin.setter
    def DataOrigin(self, DataOrigin):
        self._DataOrigin = DataOrigin

    @property
    def DataOriginProjectId(self):
        r"""Third-party project ID.
        :rtype: str
        """
        return self._DataOriginProjectId

    @DataOriginProjectId.setter
    def DataOriginProjectId(self, DataOriginProjectId):
        self._DataOriginProjectId = DataOriginProjectId

    @property
    def DataOriginDatasourceId(self):
        r"""Third-party data source ID.
        :rtype: str
        """
        return self._DataOriginDatasourceId

    @DataOriginDatasourceId.setter
    def DataOriginDatasourceId(self, DataOriginDatasourceId):
        self._DataOriginDatasourceId = DataOriginDatasourceId

    @property
    def ExtraParam(self):
        r"""Extension parameter.
        :rtype: str
        """
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def UniqVpcId(self):
        r"""Unified identifier of the Tencent Cloud VPC.
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Vip(self):
        r"""VPC IP address.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""VPC port.
        :rtype: str
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        r"""Tencent Cloud VPC identifier.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def UseVPC(self):
        r"""Enable VPC.  
        :rtype: bool
        """
        return self._UseVPC

    @UseVPC.setter
    def UseVPC(self, UseVPC):
        self._UseVPC = UseVPC

    @property
    def RegionId(self):
        r"""Region.
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Schema(self):
        r"""Database schema.
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def DbVersion(self):
        r"""Database version.
        :rtype: str
        """
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion


    def _deserialize(self, params):
        self._DbHost = params.get("DbHost")
        self._DbPort = params.get("DbPort")
        self._ServiceType = params.get("ServiceType")
        self._DbType = params.get("DbType")
        self._Charset = params.get("Charset")
        self._DbUser = params.get("DbUser")
        self._DbPwd = params.get("DbPwd")
        self._DbName = params.get("DbName")
        self._SourceName = params.get("SourceName")
        self._Id = params.get("Id")
        self._ProjectId = params.get("ProjectId")
        self._Catalog = params.get("Catalog")
        self._DataOrigin = params.get("DataOrigin")
        self._DataOriginProjectId = params.get("DataOriginProjectId")
        self._DataOriginDatasourceId = params.get("DataOriginDatasourceId")
        self._ExtraParam = params.get("ExtraParam")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        self._UseVPC = params.get("UseVPC")
        self._RegionId = params.get("RegionId")
        self._Schema = params.get("Schema")
        self._DbVersion = params.get("DbVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatasourceResponse(AbstractModel):
    r"""ModifyDatasource response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Data: None.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: str
        :param _Extra: Additional information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: Prompt.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Data = None
        self._Extra = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Data(self):
        r"""None.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Extra(self):
        r"""Additional information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Prompt.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Data = params.get("Data")
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    r"""ModifyProject request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Project ID.

        :type Id: int
        :param _Name: Name.
        :type Name: str
        :param _ColorCode: Color value.
        :type ColorCode: str
        :param _Logo: Icon.
        :type Logo: str
        :param _Mark: Remarks.
        :type Mark: str
        :param _IsApply: Available upon request.
        :type IsApply: bool
        :param _Seed: Seed.
        :type Seed: str
        :param _DefaultPanelType: Default dashboard.
Value range:.
1: project dashboard. 
2: my dashboard.
        :type DefaultPanelType: int
        :param _PanelScope: 2
        :type PanelScope: str
        :param _ManagePlatform: Project management platform.
        :type ManagePlatform: str
        """
        self._Id = None
        self._Name = None
        self._ColorCode = None
        self._Logo = None
        self._Mark = None
        self._IsApply = None
        self._Seed = None
        self._DefaultPanelType = None
        self._PanelScope = None
        self._ManagePlatform = None

    @property
    def Id(self):
        r"""Project ID.

        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""Name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ColorCode(self):
        r"""Color value.
        :rtype: str
        """
        return self._ColorCode

    @ColorCode.setter
    def ColorCode(self, ColorCode):
        self._ColorCode = ColorCode

    @property
    def Logo(self):
        r"""Icon.
        :rtype: str
        """
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def Mark(self):
        r"""Remarks.
        :rtype: str
        """
        return self._Mark

    @Mark.setter
    def Mark(self, Mark):
        self._Mark = Mark

    @property
    def IsApply(self):
        r"""Available upon request.
        :rtype: bool
        """
        return self._IsApply

    @IsApply.setter
    def IsApply(self, IsApply):
        self._IsApply = IsApply

    @property
    def Seed(self):
        r"""Seed.
        :rtype: str
        """
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def DefaultPanelType(self):
        r"""Default dashboard.
Value range:.
1: project dashboard. 
2: my dashboard.
        :rtype: int
        """
        return self._DefaultPanelType

    @DefaultPanelType.setter
    def DefaultPanelType(self, DefaultPanelType):
        self._DefaultPanelType = DefaultPanelType

    @property
    def PanelScope(self):
        r"""2
        :rtype: str
        """
        return self._PanelScope

    @PanelScope.setter
    def PanelScope(self, PanelScope):
        self._PanelScope = PanelScope

    @property
    def ManagePlatform(self):
        r"""Project management platform.
        :rtype: str
        """
        return self._ManagePlatform

    @ManagePlatform.setter
    def ManagePlatform(self, ManagePlatform):
        self._ManagePlatform = ManagePlatform


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._ColorCode = params.get("ColorCode")
        self._Logo = params.get("Logo")
        self._Mark = params.get("Mark")
        self._IsApply = params.get("IsApply")
        self._Seed = params.get("Seed")
        self._DefaultPanelType = params.get("DefaultPanelType")
        self._PanelScope = params.get("PanelScope")
        self._ManagePlatform = params.get("ManagePlatform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectResponse(AbstractModel):
    r"""ModifyProject response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Additional information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Data: Returned data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: str
        :param _Msg: Result.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Additional information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        r"""Returned data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Msg(self):
        r"""Result.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Data = params.get("Data")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ModifyResourceUserGroupResourceRequest(AbstractModel):
    r"""ModifyResourceUserGroupResource request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _UserGroupId: User ID
        :type UserGroupId: int
        :param _Resource: resource
        :type Resource: :class:`tencentcloud.bi.v20220105.models.UserResourceDTO`
        :param _EntityIds: Entity class
        :type EntityIds: list of int
        :param _ResourceType: Resource type.
        :type ResourceType: str
        """
        self._ProjectId = None
        self._UserGroupId = None
        self._Resource = None
        self._EntityIds = None
        self._ResourceType = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def UserGroupId(self):
        r"""User ID
        :rtype: int
        """
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def Resource(self):
        r"""resource
        :rtype: :class:`tencentcloud.bi.v20220105.models.UserResourceDTO`
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def EntityIds(self):
        r"""Entity class
        :rtype: list of int
        """
        return self._EntityIds

    @EntityIds.setter
    def EntityIds(self, EntityIds):
        self._EntityIds = EntityIds

    @property
    def ResourceType(self):
        r"""Resource type.
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._UserGroupId = params.get("UserGroupId")
        if params.get("Resource") is not None:
            self._Resource = UserResourceDTO()
            self._Resource._deserialize(params.get("Resource"))
        self._EntityIds = params.get("EntityIds")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceUserGroupResourceResponse(AbstractModel):
    r"""ModifyResourceUserGroupResource response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: Message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _Data: Data.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Msg = None
        self._Data = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Data(self):
        r"""Data.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class ModifyResourceUserRequest(AbstractModel):
    r"""ModifyResourceUser request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _UserId: User ID
        :type UserId: str
        :param _Resource: resource
        :type Resource: :class:`tencentcloud.bi.v20220105.models.UserResourceDTO`
        :param _EntityIds: Entity class
        :type EntityIds: list of int
        :param _ResourceType: Resource type.
        :type ResourceType: str
        """
        self._ProjectId = None
        self._UserId = None
        self._Resource = None
        self._EntityIds = None
        self._ResourceType = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def UserId(self):
        r"""User ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Resource(self):
        r"""resource
        :rtype: :class:`tencentcloud.bi.v20220105.models.UserResourceDTO`
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def EntityIds(self):
        r"""Entity class
        :rtype: list of int
        """
        return self._EntityIds

    @EntityIds.setter
    def EntityIds(self, EntityIds):
        self._EntityIds = EntityIds

    @property
    def ResourceType(self):
        r"""Resource type.
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._UserId = params.get("UserId")
        if params.get("Resource") is not None:
            self._Resource = UserResourceDTO()
            self._Resource._deserialize(params.get("Resource"))
        self._EntityIds = params.get("EntityIds")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceUserResponse(AbstractModel):
    r"""ModifyResourceUser response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: Message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _Data: Data.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Msg = None
        self._Data = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Data(self):
        r"""Data.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class ModifyTagTableRequest(AbstractModel):
    r"""ModifyTagTable request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Tag table name
        :type Name: str
        :param _AutoImportProjectId: Project id associated with the tag table
        :type AutoImportProjectId: int
        :param _AutoImportTableId: id of the data table associated with the tag table
        :type AutoImportTableId: int
        :param _AutoImportUinField: Corresponding field of uin
        :type AutoImportUinField: str
        :param _Id: Tag table id
        :type Id: int
        """
        self._Name = None
        self._AutoImportProjectId = None
        self._AutoImportTableId = None
        self._AutoImportUinField = None
        self._Id = None

    @property
    def Name(self):
        r"""Tag table name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AutoImportProjectId(self):
        r"""Project id associated with the tag table
        :rtype: int
        """
        return self._AutoImportProjectId

    @AutoImportProjectId.setter
    def AutoImportProjectId(self, AutoImportProjectId):
        self._AutoImportProjectId = AutoImportProjectId

    @property
    def AutoImportTableId(self):
        r"""id of the data table associated with the tag table
        :rtype: int
        """
        return self._AutoImportTableId

    @AutoImportTableId.setter
    def AutoImportTableId(self, AutoImportTableId):
        self._AutoImportTableId = AutoImportTableId

    @property
    def AutoImportUinField(self):
        r"""Corresponding field of uin
        :rtype: str
        """
        return self._AutoImportUinField

    @AutoImportUinField.setter
    def AutoImportUinField(self, AutoImportUinField):
        self._AutoImportUinField = AutoImportUinField

    @property
    def Id(self):
        r"""Tag table id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AutoImportProjectId = params.get("AutoImportProjectId")
        self._AutoImportTableId = params.get("AutoImportTableId")
        self._AutoImportUinField = params.get("AutoImportUinField")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTagTableResponse(AbstractModel):
    r"""ModifyTagTable response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Data: Data.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.bi.v20220105.models.ModifyTagTableVO`
        :param _Extra: Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: Information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Data = None
        self._Extra = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Data(self):
        r"""Data.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyTagTableVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Extra(self):
        r"""Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        if params.get("Data") is not None:
            self._Data = ModifyTagTableVO()
            self._Data._deserialize(params.get("Data"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ModifyTagTableVO(AbstractModel):
    r"""Create tag output parameters

    """

    def __init__(self):
        r"""
        :param _Id: Tag table id
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        r"""Tag table id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserRoleProjectRequest(AbstractModel):
    r"""ModifyUserRoleProject request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _UserId: User ID.
        :type UserId: str
        :param _RoleIdList: Role ID list.
        :type RoleIdList: list of int
        :param _Email: Mailbox.
        :type Email: str
        :param _UserName: Username.
        :type UserName: str
        :param _AppUserId: WeCom app user ID.
        :type AppUserId: str
        """
        self._ProjectId = None
        self._UserId = None
        self._RoleIdList = None
        self._Email = None
        self._UserName = None
        self._AppUserId = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def UserId(self):
        r"""User ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoleIdList(self):
        r"""Role ID list.
        :rtype: list of int
        """
        return self._RoleIdList

    @RoleIdList.setter
    def RoleIdList(self, RoleIdList):
        self._RoleIdList = RoleIdList

    @property
    def Email(self):
        r"""Mailbox.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def UserName(self):
        r"""Username.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def AppUserId(self):
        r"""WeCom app user ID.
        :rtype: str
        """
        return self._AppUserId

    @AppUserId.setter
    def AppUserId(self, AppUserId):
        self._AppUserId = AppUserId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._UserId = params.get("UserId")
        self._RoleIdList = params.get("RoleIdList")
        self._Email = params.get("Email")
        self._UserName = params.get("UserName")
        self._AppUserId = params.get("AppUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserRoleProjectResponse(AbstractModel):
    r"""ModifyUserRoleProject response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _Data: Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Msg = None
        self._Data = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Data(self):
        r"""Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class ModifyUserRoleRequest(AbstractModel):
    r"""ModifyUserRole request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID.
        :type UserId: str
        :param _RoleIdList: Role ID list.
        :type RoleIdList: list of int
        :param _Email: Mailbox.
        :type Email: str
        :param _UserName: Username.
        :type UserName: str
        :param _PhoneNumber: Mobile number.
        :type PhoneNumber: str
        :param _AreaCode: Telephone country code.
        :type AreaCode: str
        :param _AppUserId: WeCom user ID.
        :type AppUserId: str
        :param _LoginSecurityStatus: Whether to enable mobile phone verification code login (0: disabled, 1: enabled).
        :type LoginSecurityStatus: int
        :param _ResetPassWordTip: Whether to enable password expiration reminder (0: disabled, 1: enabled).
        :type ResetPassWordTip: int
        :param _ForceResetPassWord: Force password reset (0: disabled, 1: enabled).
        :type ForceResetPassWord: int
        :param _PasswordExpired: Password expiration reminder period: 30, 60, 90 (default), or 180 days.
        :type PasswordExpired: int
        """
        self._UserId = None
        self._RoleIdList = None
        self._Email = None
        self._UserName = None
        self._PhoneNumber = None
        self._AreaCode = None
        self._AppUserId = None
        self._LoginSecurityStatus = None
        self._ResetPassWordTip = None
        self._ForceResetPassWord = None
        self._PasswordExpired = None

    @property
    def UserId(self):
        r"""User ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoleIdList(self):
        r"""Role ID list.
        :rtype: list of int
        """
        return self._RoleIdList

    @RoleIdList.setter
    def RoleIdList(self, RoleIdList):
        self._RoleIdList = RoleIdList

    @property
    def Email(self):
        r"""Mailbox.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def UserName(self):
        r"""Username.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PhoneNumber(self):
        r"""Mobile number.
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def AreaCode(self):
        r"""Telephone country code.
        :rtype: str
        """
        return self._AreaCode

    @AreaCode.setter
    def AreaCode(self, AreaCode):
        self._AreaCode = AreaCode

    @property
    def AppUserId(self):
        r"""WeCom user ID.
        :rtype: str
        """
        return self._AppUserId

    @AppUserId.setter
    def AppUserId(self, AppUserId):
        self._AppUserId = AppUserId

    @property
    def LoginSecurityStatus(self):
        r"""Whether to enable mobile phone verification code login (0: disabled, 1: enabled).
        :rtype: int
        """
        return self._LoginSecurityStatus

    @LoginSecurityStatus.setter
    def LoginSecurityStatus(self, LoginSecurityStatus):
        self._LoginSecurityStatus = LoginSecurityStatus

    @property
    def ResetPassWordTip(self):
        r"""Whether to enable password expiration reminder (0: disabled, 1: enabled).
        :rtype: int
        """
        return self._ResetPassWordTip

    @ResetPassWordTip.setter
    def ResetPassWordTip(self, ResetPassWordTip):
        self._ResetPassWordTip = ResetPassWordTip

    @property
    def ForceResetPassWord(self):
        r"""Force password reset (0: disabled, 1: enabled).
        :rtype: int
        """
        return self._ForceResetPassWord

    @ForceResetPassWord.setter
    def ForceResetPassWord(self, ForceResetPassWord):
        self._ForceResetPassWord = ForceResetPassWord

    @property
    def PasswordExpired(self):
        r"""Password expiration reminder period: 30, 60, 90 (default), or 180 days.
        :rtype: int
        """
        return self._PasswordExpired

    @PasswordExpired.setter
    def PasswordExpired(self, PasswordExpired):
        self._PasswordExpired = PasswordExpired


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._RoleIdList = params.get("RoleIdList")
        self._Email = params.get("Email")
        self._UserName = params.get("UserName")
        self._PhoneNumber = params.get("PhoneNumber")
        self._AreaCode = params.get("AreaCode")
        self._AppUserId = params.get("AppUserId")
        self._LoginSecurityStatus = params.get("LoginSecurityStatus")
        self._ResetPassWordTip = params.get("ResetPassWordTip")
        self._ForceResetPassWord = params.get("ForceResetPassWord")
        self._PasswordExpired = params.get("PasswordExpired")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserRoleResponse(AbstractModel):
    r"""ModifyUserRole response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Msg: Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _Data: Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Msg = None
        self._Data = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        r"""Expansion.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        r"""Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Data(self):
        r"""Data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class ModifyUserTagRequest(AbstractModel):
    r"""ModifyUserTag request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID.
        :type UserId: str
        :param _TagList: Tag information.
        :type TagList: list of UserTagInfo
        """
        self._UserId = None
        self._TagList = None

    @property
    def UserId(self):
        r"""User ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def TagList(self):
        r"""Tag information.
        :rtype: list of UserTagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = UserTagInfo()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserTagResponse(AbstractModel):
    r"""ModifyUserTag response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Msg: Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _Extra: Additional Information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _Data: Data.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Msg = None
        self._Extra = None
        self._Data = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        r"""Custom error information object
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Msg(self):
        r"""Message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Extra(self):
        r"""Additional Information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        r"""Data.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Msg = params.get("Msg")
        self._Extra = params.get("Extra")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class PageScreenListVO(AbstractModel):
    r"""Screenshot list

    """

    def __init__(self):
        r"""
        :param _PicType: Image export type. Valid values: Base64, and URL.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PicType: str
        :param _List: Image list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of PageScreenVO
        :param _TranId: Async transaction ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TranId: str
        :param _TranStatus: Transaction status.
1: processing; 2: processing successful; 3: processing failed (error content in outer Msg).
Note: This field may return null, indicating that no valid values can be obtained.
        :type TranStatus: int
        """
        self._PicType = None
        self._List = None
        self._TranId = None
        self._TranStatus = None

    @property
    def PicType(self):
        r"""Image export type. Valid values: Base64, and URL.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PicType

    @PicType.setter
    def PicType(self, PicType):
        self._PicType = PicType

    @property
    def List(self):
        r"""Image list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of PageScreenVO
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TranId(self):
        r"""Async transaction ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def TranStatus(self):
        r"""Transaction status.
1: processing; 2: processing successful; 3: processing failed (error content in outer Msg).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TranStatus

    @TranStatus.setter
    def TranStatus(self, TranStatus):
        self._TranStatus = TranStatus


    def _deserialize(self, params):
        self._PicType = params.get("PicType")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = PageScreenVO()
                obj._deserialize(item)
                self._List.append(obj)
        self._TranId = params.get("TranId")
        self._TranStatus = params.get("TranStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PageScreenVO(AbstractModel):
    r"""Page screenshot information

    """

    def __init__(self):
        r"""
        :param _Content: Screenshot Base64 or URL.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Content: str
        :param _WidgetId: Component ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WidgetId: str
        """
        self._Content = None
        self._WidgetId = None

    @property
    def Content(self):
        r"""Screenshot Base64 or URL.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def WidgetId(self):
        r"""Component ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._WidgetId

    @WidgetId.setter
    def WidgetId(self, WidgetId):
        self._WidgetId = WidgetId


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._WidgetId = params.get("WidgetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamCreateDTO(AbstractModel):
    r"""1

    """

    def __init__(self):
        r"""
        :param _ParamName: Parameter name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ParamName: str
        :param _DefaultValue: Default value
Note: This field may return null, indicating that no valid values can be obtained.
        :type DefaultValue: str
        :param _ParamType: Parameter type, string/datetime/number
Note: This field may return null, indicating that no valid values can be obtained.
        :type ParamType: str
        :param _FormatRule: Format type, yyyy-MM-dd HH:mm:ss.SSS (only time required)
Note: This field may return null, indicating that no valid values can be obtained.
        :type FormatRule: str
        :param _ComplexType: Complex type, another format expression, such as YYYY-MM
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComplexType: str
        :param _Scope: Application scope
Note: This field may return null, indicating that no valid values can be obtained.
        :type Scope: str
        """
        self._ParamName = None
        self._DefaultValue = None
        self._ParamType = None
        self._FormatRule = None
        self._ComplexType = None
        self._Scope = None

    @property
    def ParamName(self):
        r"""Parameter name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def DefaultValue(self):
        r"""Default value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def ParamType(self):
        r"""Parameter type, string/datetime/number
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def FormatRule(self):
        r"""Format type, yyyy-MM-dd HH:mm:ss.SSS (only time required)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FormatRule

    @FormatRule.setter
    def FormatRule(self, FormatRule):
        self._FormatRule = FormatRule

    @property
    def ComplexType(self):
        r"""Complex type, another format expression, such as YYYY-MM
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ComplexType

    @ComplexType.setter
    def ComplexType(self, ComplexType):
        self._ComplexType = ComplexType

    @property
    def Scope(self):
        r"""Application scope
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._DefaultValue = params.get("DefaultValue")
        self._ParamType = params.get("ParamType")
        self._FormatRule = params.get("FormatRule")
        self._ComplexType = params.get("ComplexType")
        self._Scope = params.get("Scope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PermissionComponent(AbstractModel):
    r"""Business edition permission unit

    """

    def __init__(self):
        r"""
        :param _ModuleId: Permission value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ModuleId: str
        :param _IncludeType: Availability.
Valid values:.

- usable.
- visible.
- disabled: unavailable.
- hidden: hide.

Default value: disabled.
Example value: disabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IncludeType: str
        :param _UpgradeVersionType: Target upgrade version.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpgradeVersionType: str
        :param _Tips: Supplemental information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tips: str
        :param _TipsKey: Key for supplementary information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TipsKey: str
        """
        self._ModuleId = None
        self._IncludeType = None
        self._UpgradeVersionType = None
        self._Tips = None
        self._TipsKey = None

    @property
    def ModuleId(self):
        r"""Permission value.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def IncludeType(self):
        r"""Availability.
Valid values:.

- usable.
- visible.
- disabled: unavailable.
- hidden: hide.

Default value: disabled.
Example value: disabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IncludeType

    @IncludeType.setter
    def IncludeType(self, IncludeType):
        self._IncludeType = IncludeType

    @property
    def UpgradeVersionType(self):
        r"""Target upgrade version.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpgradeVersionType

    @UpgradeVersionType.setter
    def UpgradeVersionType(self, UpgradeVersionType):
        self._UpgradeVersionType = UpgradeVersionType

    @property
    def Tips(self):
        r"""Supplemental information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def TipsKey(self):
        r"""Key for supplementary information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TipsKey

    @TipsKey.setter
    def TipsKey(self, TipsKey):
        self._TipsKey = TipsKey


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._IncludeType = params.get("IncludeType")
        self._UpgradeVersionType = params.get("UpgradeVersionType")
        self._Tips = params.get("Tips")
        self._TipsKey = params.get("TipsKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PermissionGroup(AbstractModel):
    r"""Commercial version permission grouping

    """

    def __init__(self):
        r"""
        :param _ModuleGroup: Group name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ModuleGroup: str
        :param _Components: Permission list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Components: list of PermissionComponent
        """
        self._ModuleGroup = None
        self._Components = None

    @property
    def ModuleGroup(self):
        r"""Group name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ModuleGroup

    @ModuleGroup.setter
    def ModuleGroup(self, ModuleGroup):
        self._ModuleGroup = ModuleGroup

    @property
    def Components(self):
        r"""Permission list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of PermissionComponent
        """
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components


    def _deserialize(self, params):
        self._ModuleGroup = params.get("ModuleGroup")
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = PermissionComponent()
                obj._deserialize(item)
                self._Components.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Project(AbstractModel):
    r"""Project description

    """

    def __init__(self):
        r"""
        :param _Id: Project ID.
        :type Id: int
        :param _Logo: Project logo.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Logo: str
        :param _Name: Project name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _ColorCode: Background color of the logo.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ColorCode: str
        :param _CreatedUser: Creator.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedUser: str
        :param _CreatedAt: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedAt: str
        :param _MemberCount: Number of members.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemberCount: int
        :param _PageCount: Number of pages.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageCount: int
        :param _LastModifyName: Last modified report and dashboard names.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastModifyName: str
        :param _Source: ""
Note: This field may return null, indicating that no valid values can be obtained.
        :type Source: str
        :param _Apply: ""
Note: This field may return null, indicating that no valid values can be obtained.
        :type Apply: bool
        :param _UpdatedUser: ""
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdatedUser: str
        :param _UpdatedAt: ""
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdatedAt: str
        :param _CorpId: ""
Note: This field may return null, indicating that no valid values can be obtained.
        :type CorpId: str
        :param _Mark: ""
Note: This field may return null, indicating that no valid values can be obtained.
        :type Mark: str
        :param _Seed: ""
Note: This field may return null, indicating that no valid values can be obtained.
        :type Seed: str
        :param _AuthList: Permission list in the project.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuthList: list of str
        :param _PanelScope: Default dashboard.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PanelScope: str
        :param _IsExternalManage: Whether it is managed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsExternalManage: bool
        :param _ManagePlatform: Management platform name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ManagePlatform: str
        :param _ConfigList: Customization parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConfigList: list of ProjectConfigList
        :param _CreatedUserName: Creator.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedUserName: str
        :param _Owner: Associated person ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Owner: str
        :param _OwnerName: Associated person.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OwnerName: str
        :param _NormalCount: Number of dashboard pages.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NormalCount: int
        :param _FreeCount: Number of free canvas pages.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FreeCount: int
        :param _AdhocCount: Number of ad-hoc analysis pages.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AdhocCount: int
        :param _BriefingCount: Number of pages in the briefing
Note: This field may return null, indicating that no valid values can be obtained.
        :type BriefingCount: int
        """
        self._Id = None
        self._Logo = None
        self._Name = None
        self._ColorCode = None
        self._CreatedUser = None
        self._CreatedAt = None
        self._MemberCount = None
        self._PageCount = None
        self._LastModifyName = None
        self._Source = None
        self._Apply = None
        self._UpdatedUser = None
        self._UpdatedAt = None
        self._CorpId = None
        self._Mark = None
        self._Seed = None
        self._AuthList = None
        self._PanelScope = None
        self._IsExternalManage = None
        self._ManagePlatform = None
        self._ConfigList = None
        self._CreatedUserName = None
        self._Owner = None
        self._OwnerName = None
        self._NormalCount = None
        self._FreeCount = None
        self._AdhocCount = None
        self._BriefingCount = None

    @property
    def Id(self):
        r"""Project ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Logo(self):
        r"""Project logo.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def Name(self):
        r"""Project name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ColorCode(self):
        r"""Background color of the logo.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ColorCode

    @ColorCode.setter
    def ColorCode(self, ColorCode):
        self._ColorCode = ColorCode

    @property
    def CreatedUser(self):
        r"""Creator.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatedUser

    @CreatedUser.setter
    def CreatedUser(self, CreatedUser):
        self._CreatedUser = CreatedUser

    @property
    def CreatedAt(self):
        r"""Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def MemberCount(self):
        r"""Number of members.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MemberCount

    @MemberCount.setter
    def MemberCount(self, MemberCount):
        self._MemberCount = MemberCount

    @property
    def PageCount(self):
        r"""Number of pages.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageCount

    @PageCount.setter
    def PageCount(self, PageCount):
        self._PageCount = PageCount

    @property
    def LastModifyName(self):
        r"""Last modified report and dashboard names.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LastModifyName

    @LastModifyName.setter
    def LastModifyName(self, LastModifyName):
        self._LastModifyName = LastModifyName

    @property
    def Source(self):
        r"""""
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Apply(self):
        r"""""
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Apply

    @Apply.setter
    def Apply(self, Apply):
        self._Apply = Apply

    @property
    def UpdatedUser(self):
        r"""""
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdatedUser

    @UpdatedUser.setter
    def UpdatedUser(self, UpdatedUser):
        self._UpdatedUser = UpdatedUser

    @property
    def UpdatedAt(self):
        r"""""
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def CorpId(self):
        r"""""
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Mark(self):
        r"""""
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Mark

    @Mark.setter
    def Mark(self, Mark):
        self._Mark = Mark

    @property
    def Seed(self):
        r"""""
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def AuthList(self):
        r"""Permission list in the project.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AuthList

    @AuthList.setter
    def AuthList(self, AuthList):
        self._AuthList = AuthList

    @property
    def PanelScope(self):
        r"""Default dashboard.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PanelScope

    @PanelScope.setter
    def PanelScope(self, PanelScope):
        self._PanelScope = PanelScope

    @property
    def IsExternalManage(self):
        r"""Whether it is managed.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsExternalManage

    @IsExternalManage.setter
    def IsExternalManage(self, IsExternalManage):
        self._IsExternalManage = IsExternalManage

    @property
    def ManagePlatform(self):
        r"""Management platform name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ManagePlatform

    @ManagePlatform.setter
    def ManagePlatform(self, ManagePlatform):
        self._ManagePlatform = ManagePlatform

    @property
    def ConfigList(self):
        r"""Customization parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ProjectConfigList
        """
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def CreatedUserName(self):
        r"""Creator.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatedUserName

    @CreatedUserName.setter
    def CreatedUserName(self, CreatedUserName):
        self._CreatedUserName = CreatedUserName

    @property
    def Owner(self):
        r"""Associated person ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def OwnerName(self):
        r"""Associated person.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OwnerName

    @OwnerName.setter
    def OwnerName(self, OwnerName):
        self._OwnerName = OwnerName

    @property
    def NormalCount(self):
        r"""Number of dashboard pages.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._NormalCount

    @NormalCount.setter
    def NormalCount(self, NormalCount):
        self._NormalCount = NormalCount

    @property
    def FreeCount(self):
        r"""Number of free canvas pages.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FreeCount

    @FreeCount.setter
    def FreeCount(self, FreeCount):
        self._FreeCount = FreeCount

    @property
    def AdhocCount(self):
        r"""Number of ad-hoc analysis pages.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AdhocCount

    @AdhocCount.setter
    def AdhocCount(self, AdhocCount):
        self._AdhocCount = AdhocCount

    @property
    def BriefingCount(self):
        r"""Number of pages in the briefing
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BriefingCount

    @BriefingCount.setter
    def BriefingCount(self, BriefingCount):
        self._BriefingCount = BriefingCount


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Logo = params.get("Logo")
        self._Name = params.get("Name")
        self._ColorCode = params.get("ColorCode")
        self._CreatedUser = params.get("CreatedUser")
        self._CreatedAt = params.get("CreatedAt")
        self._MemberCount = params.get("MemberCount")
        self._PageCount = params.get("PageCount")
        self._LastModifyName = params.get("LastModifyName")
        self._Source = params.get("Source")
        self._Apply = params.get("Apply")
        self._UpdatedUser = params.get("UpdatedUser")
        self._UpdatedAt = params.get("UpdatedAt")
        self._CorpId = params.get("CorpId")
        self._Mark = params.get("Mark")
        self._Seed = params.get("Seed")
        self._AuthList = params.get("AuthList")
        self._PanelScope = params.get("PanelScope")
        self._IsExternalManage = params.get("IsExternalManage")
        self._ManagePlatform = params.get("ManagePlatform")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = ProjectConfigList()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._CreatedUserName = params.get("CreatedUserName")
        self._Owner = params.get("Owner")
        self._OwnerName = params.get("OwnerName")
        self._NormalCount = params.get("NormalCount")
        self._FreeCount = params.get("FreeCount")
        self._AdhocCount = params.get("AdhocCount")
        self._BriefingCount = params.get("BriefingCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectConfigList(AbstractModel):
    r"""Customized query

    """

    def __init__(self):
        r"""
        :param _ModuleGroup: Module group.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ModuleGroup: str
        :param _Components: Content.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Components: list of ProjectConfigResult
        """
        self._ModuleGroup = None
        self._Components = None

    @property
    def ModuleGroup(self):
        r"""Module group.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ModuleGroup

    @ModuleGroup.setter
    def ModuleGroup(self, ModuleGroup):
        self._ModuleGroup = ModuleGroup

    @property
    def Components(self):
        r"""Content.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ProjectConfigResult
        """
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components


    def _deserialize(self, params):
        self._ModuleGroup = params.get("ModuleGroup")
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = ProjectConfigResult()
                obj._deserialize(item)
                self._Components.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectConfigResult(AbstractModel):
    r"""Customized query

    """

    def __init__(self):
        r"""
        :param _ModuleId: Configuration name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ModuleId: str
        :param _IncludeType: Configuration mode.
Valid values:.

- usable.
- visible.
- disabled: unavailable.
- hidden: hide.

Default value: disabled.
Example value: disabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IncludeType: str
        :param _Params: Additional parameters.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Params: str
        """
        self._ModuleId = None
        self._IncludeType = None
        self._Params = None

    @property
    def ModuleId(self):
        r"""Configuration name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def IncludeType(self):
        r"""Configuration mode.
Valid values:.

- usable.
- visible.
- disabled: unavailable.
- hidden: hide.

Default value: disabled.
Example value: disabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IncludeType

    @IncludeType.setter
    def IncludeType(self, IncludeType):
        self._IncludeType = IncludeType

    @property
    def Params(self):
        r"""Additional parameters.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._IncludeType = params.get("IncludeType")
        self._Params = params.get("Params")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectListData(AbstractModel):
    r"""Project list data

    """

    def __init__(self):
        r"""
        :param _List: Array.
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of Project
        :param _Total: Total number.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _TotalPages: 1
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalPages: int
        """
        self._List = None
        self._Total = None
        self._TotalPages = None

    @property
    def List(self):
        r"""Array.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Project
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        r"""Total number.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalPages(self):
        r"""1
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalPages

    @TotalPages.setter
    def TotalPages(self, TotalPages):
        self._TotalPages = TotalPages


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Project()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._TotalPages = params.get("TotalPages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceItem(AbstractModel):
    r"""resource

    """

    def __init__(self):
        r"""
        :param _ResourceName: Resource name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceName: str
        :param _ResourceValue: resource value
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceValue: bool
        :param _CanChange: Changeable
Note: This field may return null, indicating that no valid values can be obtained.
        :type CanChange: bool
        :param _Tips: Prompt message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tips: str
        """
        self._ResourceName = None
        self._ResourceValue = None
        self._CanChange = None
        self._Tips = None

    @property
    def ResourceName(self):
        r"""Resource name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceValue(self):
        r"""resource value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._ResourceValue

    @ResourceValue.setter
    def ResourceValue(self, ResourceValue):
        self._ResourceValue = ResourceValue

    @property
    def CanChange(self):
        r"""Changeable
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._CanChange

    @CanChange.setter
    def CanChange(self, CanChange):
        self._CanChange = CanChange

    @property
    def Tips(self):
        r"""Prompt message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips


    def _deserialize(self, params):
        self._ResourceName = params.get("ResourceName")
        self._ResourceValue = params.get("ResourceValue")
        self._CanChange = params.get("CanChange")
        self._Tips = params.get("Tips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RowColumnConfig(AbstractModel):
    r"""Row/column permission configuration

    """

    def __init__(self):
        r"""
        :param _RulerInfo: Row column permission rule
Note: This field may return null, indicating that no valid values can be obtained.
        :type RulerInfo: str
        :param _TagValueList: Tag value list
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagValueList: list of RowColumnTagValue
        """
        self._RulerInfo = None
        self._TagValueList = None

    @property
    def RulerInfo(self):
        r"""Row column permission rule
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RulerInfo

    @RulerInfo.setter
    def RulerInfo(self, RulerInfo):
        self._RulerInfo = RulerInfo

    @property
    def TagValueList(self):
        r"""Tag value list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of RowColumnTagValue
        """
        return self._TagValueList

    @TagValueList.setter
    def TagValueList(self, TagValueList):
        self._TagValueList = TagValueList


    def _deserialize(self, params):
        self._RulerInfo = params.get("RulerInfo")
        if params.get("TagValueList") is not None:
            self._TagValueList = []
            for item in params.get("TagValueList"):
                obj = RowColumnTagValue()
                obj._deserialize(item)
                self._TagValueList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RowColumnTagValue(AbstractModel):
    r"""Row/column permission tag input/output parameter

    """

    def __init__(self):
        r"""
        :param _Id: Tag ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: int
        :param _Name: Tag name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Values: Tag value list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Values: list of str
        """
        self._Id = None
        self._Name = None
        self._Values = None

    @property
    def Id(self):
        r"""Tag ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""Tag name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""Tag value list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableColumn(AbstractModel):
    r"""Column data abstraction of a table

    """

    def __init__(self):
        r"""
        :param _DbName: Column name
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbName: str
        :param _AliasName: alias name
Note: This field may return null, indicating that no valid values can be obtained.
        :type AliasName: str
        :param _DbType: Column type
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbType: str
        :param _FieldType: Segment type
Note: This field may return null, indicating that no valid values can be obtained.
        :type FieldType: str
        :param _Mark: Remarks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Mark: str
        :param _ExcelName: excel name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExcelName: str
        :param _DictId: Associated dictionary table Id
Note: This field may return null, indicating that no valid values can be obtained.
        :type DictId: int
        :param _DictName: Associated dictionary table name
Note: This field may return null, indicating that no valid values can be obtained.
        :type DictName: str
        :param _TableNodeId: Join tables and add fields
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableNodeId: str
        :param _TableName: Table name to which the field belongs
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param _FieldComplexType: Complex format of the target set by the user
Note: This field may return null, indicating that no valid values can be obtained.
        :type FieldComplexType: str
        :param _FormatRule: format rule
Note: This field may return null, indicating that no valid values can be obtained.
        :type FormatRule: str
        :param _IsFilter: Whether to filter empty data fields
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsFilter: bool
        :param _CalcType: Compute field type
Note: This field may return null, indicating that no valid values can be obtained.
        :type CalcType: str
        :param _CalcFormula: Formula content of the calculated field
Note: This field may return null, indicating that no valid values can be obtained.
        :type CalcFormula: str
        :param _CalcDesc: Chinese formula content of the calculated field
Note: This field may return null, indicating that no valid values can be obtained.
        :type CalcDesc: str
        :param _JsonPathName: Api data source json path name
Note: This field may return null, indicating that no valid values can be obtained.
        :type JsonPathName: str
        :param _Granularity: Geographic type identifier
Note: This field may return null, indicating that no valid values can be obtained.
        :type Granularity: str
        :param _GeoJsonId: Custom map Id
Note: This field may return null, indicating that no valid values can be obtained.
        :type GeoJsonId: int
        :param _EmptyValueConfig: Style configuration for null value display
Note: This field may return null, indicating that no valid values can be obtained.
        :type EmptyValueConfig: :class:`tencentcloud.bi.v20220105.models.EmptyValueConfig`
        :param _DbFieldName: Original column name
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbFieldName: str
        :param _IsCopyOperation: Whether to copy field operation
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsCopyOperation: bool
        :param _IsCopyFromNormal: Whether to copy from common fields
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsCopyFromNormal: bool
        """
        self._DbName = None
        self._AliasName = None
        self._DbType = None
        self._FieldType = None
        self._Mark = None
        self._ExcelName = None
        self._DictId = None
        self._DictName = None
        self._TableNodeId = None
        self._TableName = None
        self._FieldComplexType = None
        self._FormatRule = None
        self._IsFilter = None
        self._CalcType = None
        self._CalcFormula = None
        self._CalcDesc = None
        self._JsonPathName = None
        self._Granularity = None
        self._GeoJsonId = None
        self._EmptyValueConfig = None
        self._DbFieldName = None
        self._IsCopyOperation = None
        self._IsCopyFromNormal = None

    @property
    def DbName(self):
        r"""Column name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def AliasName(self):
        r"""alias name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def DbType(self):
        r"""Column type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def FieldType(self):
        r"""Segment type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FieldType

    @FieldType.setter
    def FieldType(self, FieldType):
        self._FieldType = FieldType

    @property
    def Mark(self):
        r"""Remarks.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Mark

    @Mark.setter
    def Mark(self, Mark):
        self._Mark = Mark

    @property
    def ExcelName(self):
        r"""excel name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExcelName

    @ExcelName.setter
    def ExcelName(self, ExcelName):
        self._ExcelName = ExcelName

    @property
    def DictId(self):
        r"""Associated dictionary table Id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DictId

    @DictId.setter
    def DictId(self, DictId):
        self._DictId = DictId

    @property
    def DictName(self):
        r"""Associated dictionary table name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DictName

    @DictName.setter
    def DictName(self, DictName):
        self._DictName = DictName

    @property
    def TableNodeId(self):
        r"""Join tables and add fields
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableNodeId

    @TableNodeId.setter
    def TableNodeId(self, TableNodeId):
        self._TableNodeId = TableNodeId

    @property
    def TableName(self):
        r"""Table name to which the field belongs
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def FieldComplexType(self):
        r"""Complex format of the target set by the user
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FieldComplexType

    @FieldComplexType.setter
    def FieldComplexType(self, FieldComplexType):
        self._FieldComplexType = FieldComplexType

    @property
    def FormatRule(self):
        r"""format rule
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FormatRule

    @FormatRule.setter
    def FormatRule(self, FormatRule):
        self._FormatRule = FormatRule

    @property
    def IsFilter(self):
        r"""Whether to filter empty data fields
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsFilter

    @IsFilter.setter
    def IsFilter(self, IsFilter):
        self._IsFilter = IsFilter

    @property
    def CalcType(self):
        r"""Compute field type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CalcType

    @CalcType.setter
    def CalcType(self, CalcType):
        self._CalcType = CalcType

    @property
    def CalcFormula(self):
        r"""Formula content of the calculated field
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CalcFormula

    @CalcFormula.setter
    def CalcFormula(self, CalcFormula):
        self._CalcFormula = CalcFormula

    @property
    def CalcDesc(self):
        r"""Chinese formula content of the calculated field
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CalcDesc

    @CalcDesc.setter
    def CalcDesc(self, CalcDesc):
        self._CalcDesc = CalcDesc

    @property
    def JsonPathName(self):
        r"""Api data source json path name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JsonPathName

    @JsonPathName.setter
    def JsonPathName(self, JsonPathName):
        self._JsonPathName = JsonPathName

    @property
    def Granularity(self):
        r"""Geographic type identifier
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity

    @property
    def GeoJsonId(self):
        r"""Custom map Id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._GeoJsonId

    @GeoJsonId.setter
    def GeoJsonId(self, GeoJsonId):
        self._GeoJsonId = GeoJsonId

    @property
    def EmptyValueConfig(self):
        r"""Style configuration for null value display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.EmptyValueConfig`
        """
        return self._EmptyValueConfig

    @EmptyValueConfig.setter
    def EmptyValueConfig(self, EmptyValueConfig):
        self._EmptyValueConfig = EmptyValueConfig

    @property
    def DbFieldName(self):
        r"""Original column name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbFieldName

    @DbFieldName.setter
    def DbFieldName(self, DbFieldName):
        self._DbFieldName = DbFieldName

    @property
    def IsCopyOperation(self):
        r"""Whether to copy field operation
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsCopyOperation

    @IsCopyOperation.setter
    def IsCopyOperation(self, IsCopyOperation):
        self._IsCopyOperation = IsCopyOperation

    @property
    def IsCopyFromNormal(self):
        r"""Whether to copy from common fields
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsCopyFromNormal

    @IsCopyFromNormal.setter
    def IsCopyFromNormal(self, IsCopyFromNormal):
        self._IsCopyFromNormal = IsCopyFromNormal


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._AliasName = params.get("AliasName")
        self._DbType = params.get("DbType")
        self._FieldType = params.get("FieldType")
        self._Mark = params.get("Mark")
        self._ExcelName = params.get("ExcelName")
        self._DictId = params.get("DictId")
        self._DictName = params.get("DictName")
        self._TableNodeId = params.get("TableNodeId")
        self._TableName = params.get("TableName")
        self._FieldComplexType = params.get("FieldComplexType")
        self._FormatRule = params.get("FormatRule")
        self._IsFilter = params.get("IsFilter")
        self._CalcType = params.get("CalcType")
        self._CalcFormula = params.get("CalcFormula")
        self._CalcDesc = params.get("CalcDesc")
        self._JsonPathName = params.get("JsonPathName")
        self._Granularity = params.get("Granularity")
        self._GeoJsonId = params.get("GeoJsonId")
        if params.get("EmptyValueConfig") is not None:
            self._EmptyValueConfig = EmptyValueConfig()
            self._EmptyValueConfig._deserialize(params.get("EmptyValueConfig"))
        self._DbFieldName = params.get("DbFieldName")
        self._IsCopyOperation = params.get("IsCopyOperation")
        self._IsCopyFromNormal = params.get("IsCopyFromNormal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableColumnListData(AbstractModel):
    r"""Data list of all column names in the table

    """

    def __init__(self):
        r"""
        :param _List: Column list in the table
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of TableColumn
        :param _TranId: async transaction id
Note: This field may return null, indicating that no valid values can be obtained.
        :type TranId: str
        :param _TranStatus: Async transaction status
Note: This field may return null, indicating that no valid values can be obtained.
        :type TranStatus: int
        """
        self._List = None
        self._TranId = None
        self._TranStatus = None

    @property
    def List(self):
        r"""Column list in the table
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TableColumn
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TranId(self):
        r"""async transaction id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def TranStatus(self):
        r"""Async transaction status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TranStatus

    @TranStatus.setter
    def TranStatus(self, TranStatus):
        self._TranStatus = TranStatus


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = TableColumn()
                obj._deserialize(item)
                self._List.append(obj)
        self._TranId = params.get("TranId")
        self._TranStatus = params.get("TranStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableField(AbstractModel):
    r"""Table field description

    """

    def __init__(self):
        r"""
        :param _DbName: Field name in the db
        :type DbName: str
        :param _AliasName: bi display name
        :type AliasName: str
        :param _DbType: Field type in the db
        :type DbType: str
        :param _FieldType: Abstract field types after BI categorization, such as string, number, time
        :type FieldType: str
        :param _FieldComplexType: Complex detail type generated after calculation formula of combination of fields
Note: This field may return null, indicating that no valid values can be obtained.
        :type FieldComplexType: str
        :param _Mark: Field description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Mark: str
        :param _FormatRule: Field calculation formula
Note: This field may return null, indicating that no valid values can be obtained.
        :type FormatRule: str
        :param _IsFilter: Whether to filter empty data fields
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsFilter: bool
        :param _CalcType: Compute field type
Note: This field may return null, indicating that no valid values can be obtained.
        :type CalcType: str
        :param _CalcFormula: Formula content of the calculated field
Note: This field may return null, indicating that no valid values can be obtained.
        :type CalcFormula: str
        :param _CalcDesc: Chinese formula content of the calculated field, displayed on the front-end
Note: This field may return null, indicating that no valid values can be obtained.
        :type CalcDesc: str
        :param _DictId: Associate dictionary table id
Note: This field may return null, indicating that no valid values can be obtained.
        :type DictId: int
        :param _DictName: Associate dictionary table name
Note: This field may return null, indicating that no valid values can be obtained.
        :type DictName: str
        :param _TableNodeId: Optional, join tables to add field
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableNodeId: str
        :param _ExcelName: excel
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExcelName: str
        :param _TableName: Optional, join tables to add field, name of the table the field belongs to
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param _JsonPathName: api data source path name
Note: This field may return null, indicating that no valid values can be obtained.
        :type JsonPathName: str
        :param _Granularity: Geographic field identifier
Note: This field may return null, indicating that no valid values can be obtained.
        :type Granularity: str
        :param _GeoJsonId: Map id
Note: This field may return null, indicating that no valid values can be obtained.
        :type GeoJsonId: int
        :param _EmptyValueConfig: Style configuration for null value display
Note: This field may return null, indicating that no valid values can be obtained.
        :type EmptyValueConfig: :class:`tencentcloud.bi.v20220105.models.EmptyValueConfig`
        :param _DbFieldName: Original column name
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbFieldName: str
        :param _IsCopyOperation: Whether to copy field operation
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsCopyOperation: bool
        :param _IsCopyFromNormal: Whether to copy from common fields
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsCopyFromNormal: bool
        """
        self._DbName = None
        self._AliasName = None
        self._DbType = None
        self._FieldType = None
        self._FieldComplexType = None
        self._Mark = None
        self._FormatRule = None
        self._IsFilter = None
        self._CalcType = None
        self._CalcFormula = None
        self._CalcDesc = None
        self._DictId = None
        self._DictName = None
        self._TableNodeId = None
        self._ExcelName = None
        self._TableName = None
        self._JsonPathName = None
        self._Granularity = None
        self._GeoJsonId = None
        self._EmptyValueConfig = None
        self._DbFieldName = None
        self._IsCopyOperation = None
        self._IsCopyFromNormal = None

    @property
    def DbName(self):
        r"""Field name in the db
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def AliasName(self):
        r"""bi display name
        :rtype: str
        """
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def DbType(self):
        r"""Field type in the db
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def FieldType(self):
        r"""Abstract field types after BI categorization, such as string, number, time
        :rtype: str
        """
        return self._FieldType

    @FieldType.setter
    def FieldType(self, FieldType):
        self._FieldType = FieldType

    @property
    def FieldComplexType(self):
        r"""Complex detail type generated after calculation formula of combination of fields
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FieldComplexType

    @FieldComplexType.setter
    def FieldComplexType(self, FieldComplexType):
        self._FieldComplexType = FieldComplexType

    @property
    def Mark(self):
        r"""Field description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Mark

    @Mark.setter
    def Mark(self, Mark):
        self._Mark = Mark

    @property
    def FormatRule(self):
        r"""Field calculation formula
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FormatRule

    @FormatRule.setter
    def FormatRule(self, FormatRule):
        self._FormatRule = FormatRule

    @property
    def IsFilter(self):
        r"""Whether to filter empty data fields
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsFilter

    @IsFilter.setter
    def IsFilter(self, IsFilter):
        self._IsFilter = IsFilter

    @property
    def CalcType(self):
        r"""Compute field type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CalcType

    @CalcType.setter
    def CalcType(self, CalcType):
        self._CalcType = CalcType

    @property
    def CalcFormula(self):
        r"""Formula content of the calculated field
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CalcFormula

    @CalcFormula.setter
    def CalcFormula(self, CalcFormula):
        self._CalcFormula = CalcFormula

    @property
    def CalcDesc(self):
        r"""Chinese formula content of the calculated field, displayed on the front-end
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CalcDesc

    @CalcDesc.setter
    def CalcDesc(self, CalcDesc):
        self._CalcDesc = CalcDesc

    @property
    def DictId(self):
        r"""Associate dictionary table id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DictId

    @DictId.setter
    def DictId(self, DictId):
        self._DictId = DictId

    @property
    def DictName(self):
        r"""Associate dictionary table name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DictName

    @DictName.setter
    def DictName(self, DictName):
        self._DictName = DictName

    @property
    def TableNodeId(self):
        r"""Optional, join tables to add field
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableNodeId

    @TableNodeId.setter
    def TableNodeId(self, TableNodeId):
        self._TableNodeId = TableNodeId

    @property
    def ExcelName(self):
        r"""excel
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExcelName

    @ExcelName.setter
    def ExcelName(self, ExcelName):
        self._ExcelName = ExcelName

    @property
    def TableName(self):
        r"""Optional, join tables to add field, name of the table the field belongs to
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def JsonPathName(self):
        r"""api data source path name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JsonPathName

    @JsonPathName.setter
    def JsonPathName(self, JsonPathName):
        self._JsonPathName = JsonPathName

    @property
    def Granularity(self):
        r"""Geographic field identifier
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity

    @property
    def GeoJsonId(self):
        r"""Map id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._GeoJsonId

    @GeoJsonId.setter
    def GeoJsonId(self, GeoJsonId):
        self._GeoJsonId = GeoJsonId

    @property
    def EmptyValueConfig(self):
        r"""Style configuration for null value display
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.bi.v20220105.models.EmptyValueConfig`
        """
        return self._EmptyValueConfig

    @EmptyValueConfig.setter
    def EmptyValueConfig(self, EmptyValueConfig):
        self._EmptyValueConfig = EmptyValueConfig

    @property
    def DbFieldName(self):
        r"""Original column name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbFieldName

    @DbFieldName.setter
    def DbFieldName(self, DbFieldName):
        self._DbFieldName = DbFieldName

    @property
    def IsCopyOperation(self):
        r"""Whether to copy field operation
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsCopyOperation

    @IsCopyOperation.setter
    def IsCopyOperation(self, IsCopyOperation):
        self._IsCopyOperation = IsCopyOperation

    @property
    def IsCopyFromNormal(self):
        r"""Whether to copy from common fields
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsCopyFromNormal

    @IsCopyFromNormal.setter
    def IsCopyFromNormal(self, IsCopyFromNormal):
        self._IsCopyFromNormal = IsCopyFromNormal


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._AliasName = params.get("AliasName")
        self._DbType = params.get("DbType")
        self._FieldType = params.get("FieldType")
        self._FieldComplexType = params.get("FieldComplexType")
        self._Mark = params.get("Mark")
        self._FormatRule = params.get("FormatRule")
        self._IsFilter = params.get("IsFilter")
        self._CalcType = params.get("CalcType")
        self._CalcFormula = params.get("CalcFormula")
        self._CalcDesc = params.get("CalcDesc")
        self._DictId = params.get("DictId")
        self._DictName = params.get("DictName")
        self._TableNodeId = params.get("TableNodeId")
        self._ExcelName = params.get("ExcelName")
        self._TableName = params.get("TableName")
        self._JsonPathName = params.get("JsonPathName")
        self._Granularity = params.get("Granularity")
        self._GeoJsonId = params.get("GeoJsonId")
        if params.get("EmptyValueConfig") is not None:
            self._EmptyValueConfig = EmptyValueConfig()
            self._EmptyValueConfig._deserialize(params.get("EmptyValueConfig"))
        self._DbFieldName = params.get("DbFieldName")
        self._IsCopyOperation = params.get("IsCopyOperation")
        self._IsCopyFromNormal = params.get("IsCopyFromNormal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserGroupDTO(AbstractModel):
    r"""User group

    """

    def __init__(self):
        r"""
        :param _Id: id
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: int
        :param _GroupName: User group name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupName: str
        :param _ParentId: Parent node ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ParentId: int
        :param _IsDefault: Whether it is default.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDefault: int
        :param _AdminUserId: Administrator user ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AdminUserId: str
        :param _Description: Description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _Location: Location.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Location: int
        """
        self._Id = None
        self._GroupName = None
        self._ParentId = None
        self._IsDefault = None
        self._AdminUserId = None
        self._Description = None
        self._Location = None

    @property
    def Id(self):
        r"""id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def GroupName(self):
        r"""User group name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ParentId(self):
        r"""Parent node ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def IsDefault(self):
        r"""Whether it is default.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def AdminUserId(self):
        r"""Administrator user ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AdminUserId

    @AdminUserId.setter
    def AdminUserId(self, AdminUserId):
        self._AdminUserId = AdminUserId

    @property
    def Description(self):
        r"""Description.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Location(self):
        r"""Location.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._GroupName = params.get("GroupName")
        self._ParentId = params.get("ParentId")
        self._IsDefault = params.get("IsDefault")
        self._AdminUserId = params.get("AdminUserId")
        self._Description = params.get("Description")
        self._Location = params.get("Location")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserIdAndUserName(AbstractModel):
    r"""User ID and username

    """

    def __init__(self):
        r"""
        :param _UserId: User ID.
        :type UserId: str
        :param _UserName: Username.
        :type UserName: str
        :param _CorpId: Enterprise ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CorpId: str
        :param _Email: Email.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Email: str
        :param _LastLogin: Last login time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastLogin: str
        :param _Status: User status.
Valid values:.

- 1: Enable.
- 0: disabled.

The default value is 1.
Example value: 1.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _FirstModify: Whether to change password on first login.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FirstModify: int
        :param _PhoneNumber: Mobile number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhoneNumber: str
        :param _AreaCode: Telephone country code.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AreaCode: str
        :param _CreatedUser: Creator.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedUser: str
        :param _CreatedAt: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedAt: str
        :param _UpdatedUser: Modifier.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdatedUser: str
        :param _UpdatedAt: Change time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdatedAt: str
        :param _GlobalUserName: System global role.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GlobalUserName: str
        :param _GlobalUserCode: System global role code.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GlobalUserCode: str
        :param _Mobile: Mobile number.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Mobile: str
        :param _AppId: 1
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppId: str
        :param _AppUserId: 1
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppUserId: str
        :param _AppUserAliasName: 1
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppUserAliasName: str
        :param _AppUserName: 1
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppUserName: str
        :param _InValidateAppRange: 1
Note: This field may return null, indicating that no valid values can be obtained.
        :type InValidateAppRange: bool
        :param _EmailActivationStatus:  -1: No activation required. 0: Inactivated. 1: Activated. Null value represents pending binding.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EmailActivationStatus: int
        :param _Id: 1
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: int
        """
        self._UserId = None
        self._UserName = None
        self._CorpId = None
        self._Email = None
        self._LastLogin = None
        self._Status = None
        self._FirstModify = None
        self._PhoneNumber = None
        self._AreaCode = None
        self._CreatedUser = None
        self._CreatedAt = None
        self._UpdatedUser = None
        self._UpdatedAt = None
        self._GlobalUserName = None
        self._GlobalUserCode = None
        self._Mobile = None
        self._AppId = None
        self._AppUserId = None
        self._AppUserAliasName = None
        self._AppUserName = None
        self._InValidateAppRange = None
        self._EmailActivationStatus = None
        self._Id = None

    @property
    def UserId(self):
        r"""User ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        r"""Username.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def CorpId(self):
        r"""Enterprise ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Email(self):
        r"""Email.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def LastLogin(self):
        r"""Last login time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LastLogin

    @LastLogin.setter
    def LastLogin(self, LastLogin):
        self._LastLogin = LastLogin

    @property
    def Status(self):
        r"""User status.
Valid values:.

- 1: Enable.
- 0: disabled.

The default value is 1.
Example value: 1.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FirstModify(self):
        r"""Whether to change password on first login.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FirstModify

    @FirstModify.setter
    def FirstModify(self, FirstModify):
        self._FirstModify = FirstModify

    @property
    def PhoneNumber(self):
        r"""Mobile number.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def AreaCode(self):
        r"""Telephone country code.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AreaCode

    @AreaCode.setter
    def AreaCode(self, AreaCode):
        self._AreaCode = AreaCode

    @property
    def CreatedUser(self):
        r"""Creator.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatedUser

    @CreatedUser.setter
    def CreatedUser(self, CreatedUser):
        self._CreatedUser = CreatedUser

    @property
    def CreatedAt(self):
        r"""Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedUser(self):
        r"""Modifier.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdatedUser

    @UpdatedUser.setter
    def UpdatedUser(self, UpdatedUser):
        self._UpdatedUser = UpdatedUser

    @property
    def UpdatedAt(self):
        r"""Change time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def GlobalUserName(self):
        r"""System global role.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._GlobalUserName

    @GlobalUserName.setter
    def GlobalUserName(self, GlobalUserName):
        self._GlobalUserName = GlobalUserName

    @property
    def GlobalUserCode(self):
        r"""System global role code.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._GlobalUserCode

    @GlobalUserCode.setter
    def GlobalUserCode(self, GlobalUserCode):
        self._GlobalUserCode = GlobalUserCode

    @property
    def Mobile(self):
        r"""Mobile number.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def AppId(self):
        r"""1
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppUserId(self):
        r"""1
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppUserId

    @AppUserId.setter
    def AppUserId(self, AppUserId):
        self._AppUserId = AppUserId

    @property
    def AppUserAliasName(self):
        r"""1
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppUserAliasName

    @AppUserAliasName.setter
    def AppUserAliasName(self, AppUserAliasName):
        self._AppUserAliasName = AppUserAliasName

    @property
    def AppUserName(self):
        r"""1
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppUserName

    @AppUserName.setter
    def AppUserName(self, AppUserName):
        self._AppUserName = AppUserName

    @property
    def InValidateAppRange(self):
        r"""1
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._InValidateAppRange

    @InValidateAppRange.setter
    def InValidateAppRange(self, InValidateAppRange):
        self._InValidateAppRange = InValidateAppRange

    @property
    def EmailActivationStatus(self):
        r""" -1: No activation required. 0: Inactivated. 1: Activated. Null value represents pending binding.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EmailActivationStatus

    @EmailActivationStatus.setter
    def EmailActivationStatus(self, EmailActivationStatus):
        self._EmailActivationStatus = EmailActivationStatus

    @property
    def Id(self):
        r"""1
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._CorpId = params.get("CorpId")
        self._Email = params.get("Email")
        self._LastLogin = params.get("LastLogin")
        self._Status = params.get("Status")
        self._FirstModify = params.get("FirstModify")
        self._PhoneNumber = params.get("PhoneNumber")
        self._AreaCode = params.get("AreaCode")
        self._CreatedUser = params.get("CreatedUser")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedUser = params.get("UpdatedUser")
        self._UpdatedAt = params.get("UpdatedAt")
        self._GlobalUserName = params.get("GlobalUserName")
        self._GlobalUserCode = params.get("GlobalUserCode")
        self._Mobile = params.get("Mobile")
        self._AppId = params.get("AppId")
        self._AppUserId = params.get("AppUserId")
        self._AppUserAliasName = params.get("AppUserAliasName")
        self._AppUserName = params.get("AppUserName")
        self._InValidateAppRange = params.get("InValidateAppRange")
        self._EmailActivationStatus = params.get("EmailActivationStatus")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    r"""User ID and username

    """

    def __init__(self):
        r"""
        :param _UserId: User ID.
        :type UserId: str
        :param _UserName: Username.
        :type UserName: str
        :param _Email: Email.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Email: str
        :param _PhoneNumber: Mobile number.

Note: This field may return null, indicating that no valid values can be obtained.
        :type PhoneNumber: str
        :param _AreaCode: Telephone country code.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AreaCode: str
        :param _AppUserId: WeCom account ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppUserId: str
        :param _AppUserName: WeCom account name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppUserName: str
        """
        self._UserId = None
        self._UserName = None
        self._Email = None
        self._PhoneNumber = None
        self._AreaCode = None
        self._AppUserId = None
        self._AppUserName = None

    @property
    def UserId(self):
        r"""User ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        r"""Username.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Email(self):
        r"""Email.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def PhoneNumber(self):
        r"""Mobile number.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def AreaCode(self):
        r"""Telephone country code.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AreaCode

    @AreaCode.setter
    def AreaCode(self, AreaCode):
        self._AreaCode = AreaCode

    @property
    def AppUserId(self):
        r"""WeCom account ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppUserId

    @AppUserId.setter
    def AppUserId(self, AppUserId):
        self._AppUserId = AppUserId

    @property
    def AppUserName(self):
        r"""WeCom account name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppUserName

    @AppUserName.setter
    def AppUserName(self, AppUserName):
        self._AppUserName = AppUserName


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._Email = params.get("Email")
        self._PhoneNumber = params.get("PhoneNumber")
        self._AreaCode = params.get("AreaCode")
        self._AppUserId = params.get("AppUserId")
        self._AppUserName = params.get("AppUserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserResourceDTO(AbstractModel):
    r"""User resource input parameter

    """

    def __init__(self):
        r"""
        :param _CorpId: Enterprise ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CorpId: str
        :param _UserId: User ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param _UserName: Username.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _ResourceList: Resource list
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceList: list of ResourceItem
        """
        self._CorpId = None
        self._UserId = None
        self._UserName = None
        self._ResourceList = None

    @property
    def CorpId(self):
        r"""Enterprise ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def UserId(self):
        r"""User ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        r"""Username.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def ResourceList(self):
        r"""Resource list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ResourceItem
        """
        return self._ResourceList

    @ResourceList.setter
    def ResourceList(self, ResourceList):
        self._ResourceList = ResourceList


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        if params.get("ResourceList") is not None:
            self._ResourceList = []
            for item in params.get("ResourceList"):
                obj = ResourceItem()
                obj._deserialize(item)
                self._ResourceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserRoleListData(AbstractModel):
    r"""User role information

    """

    def __init__(self):
        r"""
        :param _Total: Total number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _TotalPages: Total number of pages.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalPages: int
        :param _List: List.
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of UserRoleListDataUserRoleInfo
        """
        self._Total = None
        self._TotalPages = None
        self._List = None

    @property
    def Total(self):
        r"""Total number.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalPages(self):
        r"""Total number of pages.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalPages

    @TotalPages.setter
    def TotalPages(self, TotalPages):
        self._TotalPages = TotalPages

    @property
    def List(self):
        r"""List.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of UserRoleListDataUserRoleInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._TotalPages = params.get("TotalPages")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = UserRoleListDataUserRoleInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserRoleListDataRoleInfo(AbstractModel):
    r"""Role information of the user role list

    """

    def __init__(self):
        r"""
        :param _RoleName: Role Name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoleName: str
        :param _RoleId: Role ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoleId: int
        :param _ProjectId: Project ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param _ProjectName: Project name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectName: str
        :param _ScopeType: Whether it is a global role (0: no; 1: yes).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ScopeType: int
        :param _ModuleCollection: Role key.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ModuleCollection: str
        """
        self._RoleName = None
        self._RoleId = None
        self._ProjectId = None
        self._ProjectName = None
        self._ScopeType = None
        self._ModuleCollection = None

    @property
    def RoleName(self):
        r"""Role Name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def RoleId(self):
        r"""Role ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def ProjectId(self):
        r"""Project ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""Project name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ScopeType(self):
        r"""Whether it is a global role (0: no; 1: yes).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ScopeType

    @ScopeType.setter
    def ScopeType(self, ScopeType):
        self._ScopeType = ScopeType

    @property
    def ModuleCollection(self):
        r"""Role key.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ModuleCollection

    @ModuleCollection.setter
    def ModuleCollection(self, ModuleCollection):
        self._ModuleCollection = ModuleCollection


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._RoleId = params.get("RoleId")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._ScopeType = params.get("ScopeType")
        self._ModuleCollection = params.get("ModuleCollection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserRoleListDataUserRoleInfo(AbstractModel):
    r"""User role information

    """

    def __init__(self):
        r"""
        :param _Id: Business ID.
        :type Id: int
        :param _RoleList: This API is used to obtain the role list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoleList: list of UserRoleListDataRoleInfo
        :param _RoleIdList: Role ID list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoleIdList: list of int non-negative
        :param _UserId: User ID.
        :type UserId: str
        :param _UserName: Username.
        :type UserName: str
        :param _CorpId: Enterprise ID.
        :type CorpId: str
        :param _Email: Email.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Email: str
        :param _CreatedUser: Creator.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedUser: str
        :param _CreatedAt: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedAt: str
        :param _UpdatedUser: Updater.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdatedUser: str
        :param _UpdatedAt: Update time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdatedAt: str
        :param _LastLogin: Last login time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastLogin: str
        :param _Status: Account status.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _PhoneNumber: Mobile number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhoneNumber: str
        :param _AreaCode: Telephone country code.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AreaCode: str
        :param _RootAccount: Whether it is the root account.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RootAccount: bool
        :param _CorpAdmin: Whether it is an enterprise administrator.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CorpAdmin: bool
        :param _AppUserId: WeCom user ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppUserId: str
        :param _AppUserAliasName: Nickname.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppUserAliasName: str
        :param _AppUserName: Application username.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppUserName: str
        :param _InValidateAppRange: Whether it is within the visible range.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InValidateAppRange: bool
        :param _AppOpenUserId: User openID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppOpenUserId: str
        :param _EmailActivationStatus: Activation status of email.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EmailActivationStatus: int
        :param _UserGroupList: User group information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserGroupList: list of UserGroupDTO
        """
        self._Id = None
        self._RoleList = None
        self._RoleIdList = None
        self._UserId = None
        self._UserName = None
        self._CorpId = None
        self._Email = None
        self._CreatedUser = None
        self._CreatedAt = None
        self._UpdatedUser = None
        self._UpdatedAt = None
        self._LastLogin = None
        self._Status = None
        self._PhoneNumber = None
        self._AreaCode = None
        self._RootAccount = None
        self._CorpAdmin = None
        self._AppUserId = None
        self._AppUserAliasName = None
        self._AppUserName = None
        self._InValidateAppRange = None
        self._AppOpenUserId = None
        self._EmailActivationStatus = None
        self._UserGroupList = None

    @property
    def Id(self):
        r"""Business ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RoleList(self):
        r"""This API is used to obtain the role list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of UserRoleListDataRoleInfo
        """
        return self._RoleList

    @RoleList.setter
    def RoleList(self, RoleList):
        self._RoleList = RoleList

    @property
    def RoleIdList(self):
        r"""Role ID list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of int non-negative
        """
        return self._RoleIdList

    @RoleIdList.setter
    def RoleIdList(self, RoleIdList):
        self._RoleIdList = RoleIdList

    @property
    def UserId(self):
        r"""User ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        r"""Username.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def CorpId(self):
        r"""Enterprise ID.
        :rtype: str
        """
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Email(self):
        r"""Email.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def CreatedUser(self):
        r"""Creator.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatedUser

    @CreatedUser.setter
    def CreatedUser(self, CreatedUser):
        self._CreatedUser = CreatedUser

    @property
    def CreatedAt(self):
        r"""Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedUser(self):
        r"""Updater.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdatedUser

    @UpdatedUser.setter
    def UpdatedUser(self, UpdatedUser):
        self._UpdatedUser = UpdatedUser

    @property
    def UpdatedAt(self):
        r"""Update time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def LastLogin(self):
        r"""Last login time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LastLogin

    @LastLogin.setter
    def LastLogin(self, LastLogin):
        self._LastLogin = LastLogin

    @property
    def Status(self):
        r"""Account status.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PhoneNumber(self):
        r"""Mobile number.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def AreaCode(self):
        r"""Telephone country code.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AreaCode

    @AreaCode.setter
    def AreaCode(self, AreaCode):
        self._AreaCode = AreaCode

    @property
    def RootAccount(self):
        r"""Whether it is the root account.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._RootAccount

    @RootAccount.setter
    def RootAccount(self, RootAccount):
        self._RootAccount = RootAccount

    @property
    def CorpAdmin(self):
        r"""Whether it is an enterprise administrator.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._CorpAdmin

    @CorpAdmin.setter
    def CorpAdmin(self, CorpAdmin):
        self._CorpAdmin = CorpAdmin

    @property
    def AppUserId(self):
        r"""WeCom user ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppUserId

    @AppUserId.setter
    def AppUserId(self, AppUserId):
        self._AppUserId = AppUserId

    @property
    def AppUserAliasName(self):
        r"""Nickname.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppUserAliasName

    @AppUserAliasName.setter
    def AppUserAliasName(self, AppUserAliasName):
        self._AppUserAliasName = AppUserAliasName

    @property
    def AppUserName(self):
        r"""Application username.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppUserName

    @AppUserName.setter
    def AppUserName(self, AppUserName):
        self._AppUserName = AppUserName

    @property
    def InValidateAppRange(self):
        r"""Whether it is within the visible range.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._InValidateAppRange

    @InValidateAppRange.setter
    def InValidateAppRange(self, InValidateAppRange):
        self._InValidateAppRange = InValidateAppRange

    @property
    def AppOpenUserId(self):
        r"""User openID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppOpenUserId

    @AppOpenUserId.setter
    def AppOpenUserId(self, AppOpenUserId):
        self._AppOpenUserId = AppOpenUserId

    @property
    def EmailActivationStatus(self):
        r"""Activation status of email.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EmailActivationStatus

    @EmailActivationStatus.setter
    def EmailActivationStatus(self, EmailActivationStatus):
        self._EmailActivationStatus = EmailActivationStatus

    @property
    def UserGroupList(self):
        r"""User group information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of UserGroupDTO
        """
        return self._UserGroupList

    @UserGroupList.setter
    def UserGroupList(self, UserGroupList):
        self._UserGroupList = UserGroupList


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("RoleList") is not None:
            self._RoleList = []
            for item in params.get("RoleList"):
                obj = UserRoleListDataRoleInfo()
                obj._deserialize(item)
                self._RoleList.append(obj)
        self._RoleIdList = params.get("RoleIdList")
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._CorpId = params.get("CorpId")
        self._Email = params.get("Email")
        self._CreatedUser = params.get("CreatedUser")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedUser = params.get("UpdatedUser")
        self._UpdatedAt = params.get("UpdatedAt")
        self._LastLogin = params.get("LastLogin")
        self._Status = params.get("Status")
        self._PhoneNumber = params.get("PhoneNumber")
        self._AreaCode = params.get("AreaCode")
        self._RootAccount = params.get("RootAccount")
        self._CorpAdmin = params.get("CorpAdmin")
        self._AppUserId = params.get("AppUserId")
        self._AppUserAliasName = params.get("AppUserAliasName")
        self._AppUserName = params.get("AppUserName")
        self._InValidateAppRange = params.get("InValidateAppRange")
        self._AppOpenUserId = params.get("AppOpenUserId")
        self._EmailActivationStatus = params.get("EmailActivationStatus")
        if params.get("UserGroupList") is not None:
            self._UserGroupList = []
            for item in params.get("UserGroupList"):
                obj = UserGroupDTO()
                obj._deserialize(item)
                self._UserGroupList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserTagInfo(AbstractModel):
    r"""User tag info

    """

    def __init__(self):
        r"""
        :param _Id: tag ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: int
        :param _Name: Tag name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Value: Tag value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        :param _IsExternalManage: Managed or not
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsExternalManage: bool
        :param _ManagePlatform: Tag hosting platform
Note: This field may return null, indicating that no valid values can be obtained.
        :type ManagePlatform: str
        :param _ImportType: Import type
Note: This field may return null, indicating that no valid values can be obtained.
        :type ImportType: str
        """
        self._Id = None
        self._Name = None
        self._Value = None
        self._IsExternalManage = None
        self._ManagePlatform = None
        self._ImportType = None

    @property
    def Id(self):
        r"""tag ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""Tag name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""Tag value.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def IsExternalManage(self):
        r"""Managed or not
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsExternalManage

    @IsExternalManage.setter
    def IsExternalManage(self, IsExternalManage):
        self._IsExternalManage = IsExternalManage

    @property
    def ManagePlatform(self):
        r"""Tag hosting platform
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ManagePlatform

    @ManagePlatform.setter
    def ManagePlatform(self, ManagePlatform):
        self._ManagePlatform = ManagePlatform

    @property
    def ImportType(self):
        r"""Import type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ImportType

    @ImportType.setter
    def ImportType(self, ImportType):
        self._ImportType = ImportType


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._IsExternalManage = params.get("IsExternalManage")
        self._ManagePlatform = params.get("ManagePlatform")
        self._ImportType = params.get("ImportType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WidgetListVO(AbstractModel):
    r"""Page component information

    """

    def __init__(self):
        r"""
        :param _CorpId: uin
Note: This field may return null, indicating that no valid values can be obtained.
        :type CorpId: str
        :param _ProjectId: Project ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectId: str
        :param _PageId: Page ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageId: str
        :param _WidgetList: Component array.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WidgetList: list of WidgetVO
        """
        self._CorpId = None
        self._ProjectId = None
        self._PageId = None
        self._WidgetList = None

    @property
    def CorpId(self):
        r"""uin
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def ProjectId(self):
        r"""Project ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageId(self):
        r"""Page ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def WidgetList(self):
        r"""Component array.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of WidgetVO
        """
        return self._WidgetList

    @WidgetList.setter
    def WidgetList(self, WidgetList):
        self._WidgetList = WidgetList


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        self._ProjectId = params.get("ProjectId")
        self._PageId = params.get("PageId")
        if params.get("WidgetList") is not None:
            self._WidgetList = []
            for item in params.get("WidgetList"):
                obj = WidgetVO()
                obj._deserialize(item)
                self._WidgetList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WidgetVO(AbstractModel):
    r"""Component information

    """

    def __init__(self):
        r"""
        :param _WidgetId: Component ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WidgetId: str
        :param _WidgetName: Component name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WidgetName: str
        """
        self._WidgetId = None
        self._WidgetName = None

    @property
    def WidgetId(self):
        r"""Component ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._WidgetId

    @WidgetId.setter
    def WidgetId(self, WidgetId):
        self._WidgetId = WidgetId

    @property
    def WidgetName(self):
        r"""Component name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._WidgetName

    @WidgetName.setter
    def WidgetName(self, WidgetName):
        self._WidgetName = WidgetName


    def _deserialize(self, params):
        self._WidgetId = params.get("WidgetId")
        self._WidgetName = params.get("WidgetName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        