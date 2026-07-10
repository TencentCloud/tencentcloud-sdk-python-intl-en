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


class ApiKeyDetail(AbstractModel):
    r"""Details of the specified API key

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID.
        :type ApiKeyId: str
        :param _Name: Name
        :type Name: str
        :param _ApiKey: API key value. The API response contains the masking value.
        :type ApiKey: str
        :param _Remark: Remarks.
        :type Remark: str
        :param _Platform: Platform type. Currently supported values: maas.
        :type Platform: str
        :param _Uin: Root account.
        :type Uin: str
        :param _SubUin: Sub-account.
        :type SubUin: str
        :param _Status: Status. Valid values: enable, disable.
        :type Status: str
        :param _BindType: Binding type. Value: all (all models and services), model_all_endpoint_custom (all models + custom service), model_custom_endpoint_all (custom model + all services), model_custom_endpoint_custom (custom model + custom service).
        :type BindType: str
        :param _CreateTime: Creation time. Format: YYYY-MM-DD HH:mm:ss.
        :type CreateTime: str
        :param _UpdateTime: Last update time. Format: YYYY-MM-DD HH:mm:ss.
        :type UpdateTime: str
        :param _AppId: App ID.
        :type AppId: str
        :param _Editable: Whether it is editable. true means editable, false means non-editable.
        :type Editable: bool
        :param _BindingItems: List of bound resources, case-sensitive for endpoint and model kind.
        :type BindingItems: list of BindingItem
        :param _IpWhitelist: IP allowlist. Supports IPv4 and CIDR format. Empty array indicates no restriction.
        :type IpWhitelist: list of str
        :param _Creator: This field is empty when Platform is maas.
        :type Creator: str
        :param _QuotaSet: Multi-dimensional list of Token quota information. This field is not returned when unconfigured.
        :type QuotaSet: list of QuotaInfo
        :param _QuotaStatus: Token quota status. An empty string means no configuration. active means configured with current availability. inactive means configured but quota exhausted.
        :type QuotaStatus: str
        """
        self._ApiKeyId = None
        self._Name = None
        self._ApiKey = None
        self._Remark = None
        self._Platform = None
        self._Uin = None
        self._SubUin = None
        self._Status = None
        self._BindType = None
        self._CreateTime = None
        self._UpdateTime = None
        self._AppId = None
        self._Editable = None
        self._BindingItems = None
        self._IpWhitelist = None
        self._Creator = None
        self._QuotaSet = None
        self._QuotaStatus = None

    @property
    def ApiKeyId(self):
        r"""API Key ID.
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId

    @property
    def Name(self):
        r"""Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ApiKey(self):
        r"""API key value. The API response contains the masking value.
        :rtype: str
        """
        return self._ApiKey

    @ApiKey.setter
    def ApiKey(self, ApiKey):
        self._ApiKey = ApiKey

    @property
    def Remark(self):
        r"""Remarks.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Platform(self):
        r"""Platform type. Currently supported values: maas.
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Uin(self):
        r"""Root account.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubUin(self):
        r"""Sub-account.
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def Status(self):
        r"""Status. Valid values: enable, disable.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BindType(self):
        r"""Binding type. Value: all (all models and services), model_all_endpoint_custom (all models + custom service), model_custom_endpoint_all (custom model + all services), model_custom_endpoint_custom (custom model + custom service).
        :rtype: str
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType

    @property
    def CreateTime(self):
        r"""Creation time. Format: YYYY-MM-DD HH:mm:ss.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""Last update time. Format: YYYY-MM-DD HH:mm:ss.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AppId(self):
        r"""App ID.
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Editable(self):
        r"""Whether it is editable. true means editable, false means non-editable.
        :rtype: bool
        """
        return self._Editable

    @Editable.setter
    def Editable(self, Editable):
        self._Editable = Editable

    @property
    def BindingItems(self):
        r"""List of bound resources, case-sensitive for endpoint and model kind.
        :rtype: list of BindingItem
        """
        return self._BindingItems

    @BindingItems.setter
    def BindingItems(self, BindingItems):
        self._BindingItems = BindingItems

    @property
    def IpWhitelist(self):
        r"""IP allowlist. Supports IPv4 and CIDR format. Empty array indicates no restriction.
        :rtype: list of str
        """
        return self._IpWhitelist

    @IpWhitelist.setter
    def IpWhitelist(self, IpWhitelist):
        self._IpWhitelist = IpWhitelist

    @property
    def Creator(self):
        r"""This field is empty when Platform is maas.
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def QuotaSet(self):
        r"""Multi-dimensional list of Token quota information. This field is not returned when unconfigured.
        :rtype: list of QuotaInfo
        """
        return self._QuotaSet

    @QuotaSet.setter
    def QuotaSet(self, QuotaSet):
        self._QuotaSet = QuotaSet

    @property
    def QuotaStatus(self):
        r"""Token quota status. An empty string means no configuration. active means configured with current availability. inactive means configured but quota exhausted.
        :rtype: str
        """
        return self._QuotaStatus

    @QuotaStatus.setter
    def QuotaStatus(self, QuotaStatus):
        self._QuotaStatus = QuotaStatus


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        self._Name = params.get("Name")
        self._ApiKey = params.get("ApiKey")
        self._Remark = params.get("Remark")
        self._Platform = params.get("Platform")
        self._Uin = params.get("Uin")
        self._SubUin = params.get("SubUin")
        self._Status = params.get("Status")
        self._BindType = params.get("BindType")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._AppId = params.get("AppId")
        self._Editable = params.get("Editable")
        if params.get("BindingItems") is not None:
            self._BindingItems = []
            for item in params.get("BindingItems"):
                obj = BindingItem()
                obj._deserialize(item)
                self._BindingItems.append(obj)
        self._IpWhitelist = params.get("IpWhitelist")
        self._Creator = params.get("Creator")
        if params.get("QuotaSet") is not None:
            self._QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = QuotaInfo()
                obj._deserialize(item)
                self._QuotaSet.append(obj)
        self._QuotaStatus = params.get("QuotaStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindingItem(AbstractModel):
    r"""Bind Resource

    """

    def __init__(self):
        r"""
        :param _ResourceId: Resource ID (model ID or service ID).
        :type ResourceId: str
        :param _ResourceType: Resource type. Value: endpoint (service), model (model).
        :type ResourceType: str
        :param _Status: Resource status
        :type Status: str
        """
        self._ResourceId = None
        self._ResourceType = None
        self._Status = None

    @property
    def ResourceId(self):
        r"""Resource ID (model ID or service ID).
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        r"""Resource type. Value: endpoint (service), model (model).
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Status(self):
        r"""Resource status
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiKeyRequest(AbstractModel):
    r"""CreateApiKey request structure.

    """


class CreateApiKeyResponse(AbstractModel):
    r"""CreateApiKey response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateGlossaryEntriesRequest(AbstractModel):
    r"""CreateGlossaryEntries request structure.

    """

    def __init__(self):
        r"""
        :param _GlossaryId: Termbase ID. Obtain through the API DescribeGlossaries.
        :type GlossaryId: str
        :param _Entries: Terminology entry list. At a time 100.
        :type Entries: list of GlossaryEntryInput
        """
        self._GlossaryId = None
        self._Entries = None

    @property
    def GlossaryId(self):
        r"""Termbase ID. Obtain through the API DescribeGlossaries.
        :rtype: str
        """
        return self._GlossaryId

    @GlossaryId.setter
    def GlossaryId(self, GlossaryId):
        self._GlossaryId = GlossaryId

    @property
    def Entries(self):
        r"""Terminology entry list. At a time 100.
        :rtype: list of GlossaryEntryInput
        """
        return self._Entries

    @Entries.setter
    def Entries(self, Entries):
        self._Entries = Entries


    def _deserialize(self, params):
        self._GlossaryId = params.get("GlossaryId")
        if params.get("Entries") is not None:
            self._Entries = []
            for item in params.get("Entries"):
                obj = GlossaryEntryInput()
                obj._deserialize(item)
                self._Entries.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGlossaryEntriesResponse(AbstractModel):
    r"""CreateGlossaryEntries response structure.

    """

    def __init__(self):
        r"""
        :param _Entries: List of successfully created terminology entries.
        :type Entries: list of GlossaryEntryItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Entries = None
        self._RequestId = None

    @property
    def Entries(self):
        r"""List of successfully created terminology entries.
        :rtype: list of GlossaryEntryItem
        """
        return self._Entries

    @Entries.setter
    def Entries(self, Entries):
        self._Entries = Entries

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
        if params.get("Entries") is not None:
            self._Entries = []
            for item in params.get("Entries"):
                obj = GlossaryEntryItem()
                obj._deserialize(item)
                self._Entries.append(obj)
        self._RequestId = params.get("RequestId")


class CreateGlossaryRequest(AbstractModel):
    r"""CreateGlossary request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Terminology library name. Maximum 50 characters.
        :type Name: str
        :param _Source: Source language code. Maximum 16 characters, such as zh (Chinese), en (English).
        :type Source: str
        :param _Target: Target language code. Maximum 16 characters, such as zh (Chinese), en (English).
        :type Target: str
        :param _Description: Termbase description. Maximum 255 characters.
        :type Description: str
        """
        self._Name = None
        self._Source = None
        self._Target = None
        self._Description = None

    @property
    def Name(self):
        r"""Terminology library name. Maximum 50 characters.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Source(self):
        r"""Source language code. Maximum 16 characters, such as zh (Chinese), en (English).
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""Target language code. Maximum 16 characters, such as zh (Chinese), en (English).
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def Description(self):
        r"""Termbase description. Maximum 255 characters.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGlossaryResponse(AbstractModel):
    r"""CreateGlossary response structure.

    """

    def __init__(self):
        r"""
        :param _GlossaryId: Termbase ID.
        :type GlossaryId: str
        :param _Name: Terminology repository name.
        :type Name: str
        :param _CreatedAt: Creation time. Unix timestamp (ms).
        :type CreatedAt: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GlossaryId = None
        self._Name = None
        self._CreatedAt = None
        self._RequestId = None

    @property
    def GlossaryId(self):
        r"""Termbase ID.
        :rtype: str
        """
        return self._GlossaryId

    @GlossaryId.setter
    def GlossaryId(self, GlossaryId):
        self._GlossaryId = GlossaryId

    @property
    def Name(self):
        r"""Terminology repository name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreatedAt(self):
        r"""Creation time. Unix timestamp (ms).
        :rtype: int
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

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
        self._GlossaryId = params.get("GlossaryId")
        self._Name = params.get("Name")
        self._CreatedAt = params.get("CreatedAt")
        self._RequestId = params.get("RequestId")


class DeleteApiKeyRequest(AbstractModel):
    r"""DeleteApiKey request structure.

    """


class DeleteApiKeyResponse(AbstractModel):
    r"""DeleteApiKey response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteGlossaryEntriesRequest(AbstractModel):
    r"""DeleteGlossaryEntries request structure.

    """

    def __init__(self):
        r"""
        :param _GlossaryId: Termbase ID. Obtain through the API DescribeGlossaries.
        :type GlossaryId: str
        :param _Entries: Terminology entry list to be deleted. At a time 200.
        :type Entries: list of DeleteGlossaryEntryInput
        """
        self._GlossaryId = None
        self._Entries = None

    @property
    def GlossaryId(self):
        r"""Termbase ID. Obtain through the API DescribeGlossaries.
        :rtype: str
        """
        return self._GlossaryId

    @GlossaryId.setter
    def GlossaryId(self, GlossaryId):
        self._GlossaryId = GlossaryId

    @property
    def Entries(self):
        r"""Terminology entry list to be deleted. At a time 200.
        :rtype: list of DeleteGlossaryEntryInput
        """
        return self._Entries

    @Entries.setter
    def Entries(self, Entries):
        self._Entries = Entries


    def _deserialize(self, params):
        self._GlossaryId = params.get("GlossaryId")
        if params.get("Entries") is not None:
            self._Entries = []
            for item in params.get("Entries"):
                obj = DeleteGlossaryEntryInput()
                obj._deserialize(item)
                self._Entries.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGlossaryEntriesResponse(AbstractModel):
    r"""DeleteGlossaryEntries response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteGlossaryEntryInput(AbstractModel):
    r"""Delete terminology entry

    """

    def __init__(self):
        r"""
        :param _EntryId: Terminology entry ID. Obtain through the API DescribeGlossaryEntries.
        :type EntryId: str
        """
        self._EntryId = None

    @property
    def EntryId(self):
        r"""Terminology entry ID. Obtain through the API DescribeGlossaryEntries.
        :rtype: str
        """
        return self._EntryId

    @EntryId.setter
    def EntryId(self, EntryId):
        self._EntryId = EntryId


    def _deserialize(self, params):
        self._EntryId = params.get("EntryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGlossaryRequest(AbstractModel):
    r"""DeleteGlossary request structure.

    """

    def __init__(self):
        r"""
        :param _GlossaryId: Termbase ID. Obtain through the API DescribeGlossaries.
        :type GlossaryId: str
        """
        self._GlossaryId = None

    @property
    def GlossaryId(self):
        r"""Termbase ID. Obtain through the API DescribeGlossaries.
        :rtype: str
        """
        return self._GlossaryId

    @GlossaryId.setter
    def GlossaryId(self, GlossaryId):
        self._GlossaryId = GlossaryId


    def _deserialize(self, params):
        self._GlossaryId = params.get("GlossaryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGlossaryResponse(AbstractModel):
    r"""DeleteGlossary response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DescribeApiKeyListRequest(AbstractModel):
    r"""DescribeApiKeyList request structure.

    """

    def __init__(self):
        r"""
        :param _Platform: Platform type. Currently supported values: maas.
        :type Platform: str
        :param _Limit: Number of returned results, defaults to 20, maximum value 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter condition list. Supported filter fields: apikeyId (API Key ID), apiKeyName (name), platform (platform type), status (status), bindType (binding type).
        :type Filters: list of RequestFilter
        :param _Sorts: Sorting condition list. Supported sorting field: apiKeyName
        :type Sorts: list of RequestSort
        """
        self._Platform = None
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._Sorts = None

    @property
    def Platform(self):
        r"""Platform type. Currently supported values: maas.
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Limit(self):
        r"""Number of returned results, defaults to 20, maximum value 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""Filter condition list. Supported filter fields: apikeyId (API Key ID), apiKeyName (name), platform (platform type), status (status), bindType (binding type).
        :rtype: list of RequestFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Sorts(self):
        r"""Sorting condition list. Supported sorting field: apiKeyName
        :rtype: list of RequestSort
        """
        return self._Sorts

    @Sorts.setter
    def Sorts(self, Sorts):
        self._Sorts = Sorts


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = RequestFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Sorts") is not None:
            self._Sorts = []
            for item in params.get("Sorts"):
                obj = RequestSort()
                obj._deserialize(item)
                self._Sorts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiKeyListResponse(AbstractModel):
    r"""DescribeApiKeyList response structure.

    """

    def __init__(self):
        r"""
        :param _ApiKeySet: API Key List.
        :type ApiKeySet: list of ApiKeyDetail
        :param _TotalCount: Total number of eligible API keys.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApiKeySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ApiKeySet(self):
        r"""API Key List.
        :rtype: list of ApiKeyDetail
        """
        return self._ApiKeySet

    @ApiKeySet.setter
    def ApiKeySet(self, ApiKeySet):
        self._ApiKeySet = ApiKeySet

    @property
    def TotalCount(self):
        r"""Total number of eligible API keys.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("ApiKeySet") is not None:
            self._ApiKeySet = []
            for item in params.get("ApiKeySet"):
                obj = ApiKeyDetail()
                obj._deserialize(item)
                self._ApiKeySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeApiKeyRequest(AbstractModel):
    r"""DescribeApiKey request structure.

    """

    def __init__(self):
        r"""
        :param _Platform: Platform type. Currently supported values: maas.
        :type Platform: str
        :param _ApiKeyId: API Key ID. At least one of this or ApiKey is required. Prioritize ApiKeyId.
        :type ApiKeyId: str
        :param _ApiKey: API key plaintext. At least one of it and ApiKeyId must be imported.
        :type ApiKey: str
        """
        self._Platform = None
        self._ApiKeyId = None
        self._ApiKey = None

    @property
    def Platform(self):
        r"""Platform type. Currently supported values: maas.
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ApiKeyId(self):
        r"""API Key ID. At least one of this or ApiKey is required. Prioritize ApiKeyId.
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId

    @property
    def ApiKey(self):
        r"""API key plaintext. At least one of it and ApiKeyId must be imported.
        :rtype: str
        """
        return self._ApiKey

    @ApiKey.setter
    def ApiKey(self, ApiKey):
        self._ApiKey = ApiKey


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._ApiKeyId = params.get("ApiKeyId")
        self._ApiKey = params.get("ApiKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiKeyResponse(AbstractModel):
    r"""DescribeApiKey response structure.

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID.
        :type ApiKeyId: str
        :param _Name: Name
        :type Name: str
        :param _ApiKey: API Key value (plaintext).
        :type ApiKey: str
        :param _Remark: Remarks.
        :type Remark: str
        :param _Platform: Platform type. Enumerate: maas.
        :type Platform: str
        :param _Uin: Root account.
        :type Uin: str
        :param _SubUin: Sub-account.
        :type SubUin: str
        :param _Status: Status. Valid values: enable, disable.
        :type Status: str
        :param _BindType: Binding type. Value: all (all models and access points), model_all_endpoint_custom (all models + custom access point), model_custom_endpoint_all (custom model + all access points), model_custom_endpoint_custom (custom model + custom access point).
        :type BindType: str
        :param _CreateTime: Creation time. Format: YYYY-MM-DD HH:mm:ss.
        :type CreateTime: str
        :param _UpdateTime: Last update time. Format: YYYY-MM-DD HH:mm:ss.
        :type UpdateTime: str
        :param _AppId: App ID.
        :type AppId: str
        :param _Editable: Whether it is editable. true means editable, false means non-editable.
        :type Editable: bool
        :param _BindingItems: List of bound resources, case-sensitive for endpoint and model kind.
        :type BindingItems: list of BindingItem
        :param _IpWhitelist: IP allowlist. Supports IPv4 and CIDR format. Empty array indicates no restriction.
        :type IpWhitelist: list of str
        :param _Creator: This field is empty when Platform is maas.
        :type Creator: str
        :param _QuotaSet: Multi-dimensional information of Token quota. This field is not returned when unconfigured.
        :type QuotaSet: list of QuotaInfo
        :param _QuotaStatus: Token quota status. An empty string means no configuration. active means configured with current availability. inactive means configured but quota exhausted.
        :type QuotaStatus: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApiKeyId = None
        self._Name = None
        self._ApiKey = None
        self._Remark = None
        self._Platform = None
        self._Uin = None
        self._SubUin = None
        self._Status = None
        self._BindType = None
        self._CreateTime = None
        self._UpdateTime = None
        self._AppId = None
        self._Editable = None
        self._BindingItems = None
        self._IpWhitelist = None
        self._Creator = None
        self._QuotaSet = None
        self._QuotaStatus = None
        self._RequestId = None

    @property
    def ApiKeyId(self):
        r"""API Key ID.
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId

    @property
    def Name(self):
        r"""Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ApiKey(self):
        r"""API Key value (plaintext).
        :rtype: str
        """
        return self._ApiKey

    @ApiKey.setter
    def ApiKey(self, ApiKey):
        self._ApiKey = ApiKey

    @property
    def Remark(self):
        r"""Remarks.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Platform(self):
        r"""Platform type. Enumerate: maas.
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Uin(self):
        r"""Root account.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubUin(self):
        r"""Sub-account.
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def Status(self):
        r"""Status. Valid values: enable, disable.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BindType(self):
        r"""Binding type. Value: all (all models and access points), model_all_endpoint_custom (all models + custom access point), model_custom_endpoint_all (custom model + all access points), model_custom_endpoint_custom (custom model + custom access point).
        :rtype: str
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType

    @property
    def CreateTime(self):
        r"""Creation time. Format: YYYY-MM-DD HH:mm:ss.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""Last update time. Format: YYYY-MM-DD HH:mm:ss.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AppId(self):
        r"""App ID.
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Editable(self):
        r"""Whether it is editable. true means editable, false means non-editable.
        :rtype: bool
        """
        return self._Editable

    @Editable.setter
    def Editable(self, Editable):
        self._Editable = Editable

    @property
    def BindingItems(self):
        r"""List of bound resources, case-sensitive for endpoint and model kind.
        :rtype: list of BindingItem
        """
        return self._BindingItems

    @BindingItems.setter
    def BindingItems(self, BindingItems):
        self._BindingItems = BindingItems

    @property
    def IpWhitelist(self):
        r"""IP allowlist. Supports IPv4 and CIDR format. Empty array indicates no restriction.
        :rtype: list of str
        """
        return self._IpWhitelist

    @IpWhitelist.setter
    def IpWhitelist(self, IpWhitelist):
        self._IpWhitelist = IpWhitelist

    @property
    def Creator(self):
        r"""This field is empty when Platform is maas.
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def QuotaSet(self):
        r"""Multi-dimensional information of Token quota. This field is not returned when unconfigured.
        :rtype: list of QuotaInfo
        """
        return self._QuotaSet

    @QuotaSet.setter
    def QuotaSet(self, QuotaSet):
        self._QuotaSet = QuotaSet

    @property
    def QuotaStatus(self):
        r"""Token quota status. An empty string means no configuration. active means configured with current availability. inactive means configured but quota exhausted.
        :rtype: str
        """
        return self._QuotaStatus

    @QuotaStatus.setter
    def QuotaStatus(self, QuotaStatus):
        self._QuotaStatus = QuotaStatus

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
        self._ApiKeyId = params.get("ApiKeyId")
        self._Name = params.get("Name")
        self._ApiKey = params.get("ApiKey")
        self._Remark = params.get("Remark")
        self._Platform = params.get("Platform")
        self._Uin = params.get("Uin")
        self._SubUin = params.get("SubUin")
        self._Status = params.get("Status")
        self._BindType = params.get("BindType")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._AppId = params.get("AppId")
        self._Editable = params.get("Editable")
        if params.get("BindingItems") is not None:
            self._BindingItems = []
            for item in params.get("BindingItems"):
                obj = BindingItem()
                obj._deserialize(item)
                self._BindingItems.append(obj)
        self._IpWhitelist = params.get("IpWhitelist")
        self._Creator = params.get("Creator")
        if params.get("QuotaSet") is not None:
            self._QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = QuotaInfo()
                obj._deserialize(item)
                self._QuotaSet.append(obj)
        self._QuotaStatus = params.get("QuotaStatus")
        self._RequestId = params.get("RequestId")


class DescribeGlossariesRequest(AbstractModel):
    r"""DescribeGlossaries request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of returned results. Defaults to 20, maximum value is 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter condition list. Supported filter fields: GlossaryId (Termbase ID), Name, Source (source language code), Target (target language code).
        :type Filters: list of RequestFilter
        :param _Sorts: Sorting condition list. Supported sorting fields: CreatedTime (creation time), UpdatedTime (last update time).
        :type Sorts: list of RequestSort
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._Sorts = None

    @property
    def Limit(self):
        r"""Number of returned results. Defaults to 20, maximum value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""Filter condition list. Supported filter fields: GlossaryId (Termbase ID), Name, Source (source language code), Target (target language code).
        :rtype: list of RequestFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Sorts(self):
        r"""Sorting condition list. Supported sorting fields: CreatedTime (creation time), UpdatedTime (last update time).
        :rtype: list of RequestSort
        """
        return self._Sorts

    @Sorts.setter
    def Sorts(self, Sorts):
        self._Sorts = Sorts


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = RequestFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Sorts") is not None:
            self._Sorts = []
            for item in params.get("Sorts"):
                obj = RequestSort()
                obj._deserialize(item)
                self._Sorts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGlossariesResponse(AbstractModel):
    r"""DescribeGlossaries response structure.

    """

    def __init__(self):
        r"""
        :param _Items: Terminology repository list.
        :type Items: list of GlossaryItem
        :param _TotalCount: Total number of eligible terminology repositories.
        :type TotalCount: int
        :param _Current: Current page.
        :type Current: int
        :param _PageSize: Size per page
        :type PageSize: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._Current = None
        self._PageSize = None
        self._RequestId = None

    @property
    def Items(self):
        r"""Terminology repository list.
        :rtype: list of GlossaryItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        r"""Total number of eligible terminology repositories.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Current(self):
        r"""Current page.
        :rtype: int
        """
        return self._Current

    @Current.setter
    def Current(self, Current):
        self._Current = Current

    @property
    def PageSize(self):
        r"""Size per page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = GlossaryItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Current = params.get("Current")
        self._PageSize = params.get("PageSize")
        self._RequestId = params.get("RequestId")


class DescribeGlossaryEntriesRequest(AbstractModel):
    r"""DescribeGlossaryEntries request structure.

    """

    def __init__(self):
        r"""
        :param _GlossaryId: Termbase ID. Obtain through the API DescribeGlossaries.
        :type GlossaryId: str
        :param _Page: Page number. Default is 1.
        :type Page: int
        :param _PageSize: Size per page. The default value is 20, and the maximum value is 200.
        :type PageSize: int
        """
        self._GlossaryId = None
        self._Page = None
        self._PageSize = None

    @property
    def GlossaryId(self):
        r"""Termbase ID. Obtain through the API DescribeGlossaries.
        :rtype: str
        """
        return self._GlossaryId

    @GlossaryId.setter
    def GlossaryId(self, GlossaryId):
        self._GlossaryId = GlossaryId

    @property
    def Page(self):
        r"""Page number. Default is 1.
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        r"""Size per page. The default value is 20, and the maximum value is 200.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._GlossaryId = params.get("GlossaryId")
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGlossaryEntriesResponse(AbstractModel):
    r"""DescribeGlossaryEntries response structure.

    """

    def __init__(self):
        r"""
        :param _Entries: Terminology entry list.
        :type Entries: list of GlossaryEntryItem
        :param _Total: Total number of eligible terminology entries.
        :type Total: int
        :param _Page: Current page.
        :type Page: int
        :param _PageSize: Size per page
        :type PageSize: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Entries = None
        self._Total = None
        self._Page = None
        self._PageSize = None
        self._RequestId = None

    @property
    def Entries(self):
        r"""Terminology entry list.
        :rtype: list of GlossaryEntryItem
        """
        return self._Entries

    @Entries.setter
    def Entries(self, Entries):
        self._Entries = Entries

    @property
    def Total(self):
        r"""Total number of eligible terminology entries.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Page(self):
        r"""Current page.
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        r"""Size per page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

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
        if params.get("Entries") is not None:
            self._Entries = []
            for item in params.get("Entries"):
                obj = GlossaryEntryItem()
                obj._deserialize(item)
                self._Entries.append(obj)
        self._Total = params.get("Total")
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        self._RequestId = params.get("RequestId")


class GlossaryEntryInput(AbstractModel):
    r"""Create terminology entry

    """

    def __init__(self):
        r"""
        :param _SourceTerm: Source language terminology. Maximum 1000 characters.
        :type SourceTerm: str
        :param _TargetTerm: Target language terminology. Maximum 1000 characters.
        :type TargetTerm: str
        """
        self._SourceTerm = None
        self._TargetTerm = None

    @property
    def SourceTerm(self):
        r"""Source language terminology. Maximum 1000 characters.
        :rtype: str
        """
        return self._SourceTerm

    @SourceTerm.setter
    def SourceTerm(self, SourceTerm):
        self._SourceTerm = SourceTerm

    @property
    def TargetTerm(self):
        r"""Target language terminology. Maximum 1000 characters.
        :rtype: str
        """
        return self._TargetTerm

    @TargetTerm.setter
    def TargetTerm(self, TargetTerm):
        self._TargetTerm = TargetTerm


    def _deserialize(self, params):
        self._SourceTerm = params.get("SourceTerm")
        self._TargetTerm = params.get("TargetTerm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GlossaryEntryItem(AbstractModel):
    r"""Terminology entry detail

    """

    def __init__(self):
        r"""
        :param _EntryId: Terminology entry ID.
        :type EntryId: str
        :param _SourceTerm: Source language terminology.
        :type SourceTerm: str
        :param _TargetTerm: Target language terminology.
        :type TargetTerm: str
        :param _UpdatedAt: Last update time. Unix timestamp (ms).
        :type UpdatedAt: int
        """
        self._EntryId = None
        self._SourceTerm = None
        self._TargetTerm = None
        self._UpdatedAt = None

    @property
    def EntryId(self):
        r"""Terminology entry ID.
        :rtype: str
        """
        return self._EntryId

    @EntryId.setter
    def EntryId(self, EntryId):
        self._EntryId = EntryId

    @property
    def SourceTerm(self):
        r"""Source language terminology.
        :rtype: str
        """
        return self._SourceTerm

    @SourceTerm.setter
    def SourceTerm(self, SourceTerm):
        self._SourceTerm = SourceTerm

    @property
    def TargetTerm(self):
        r"""Target language terminology.
        :rtype: str
        """
        return self._TargetTerm

    @TargetTerm.setter
    def TargetTerm(self, TargetTerm):
        self._TargetTerm = TargetTerm

    @property
    def UpdatedAt(self):
        r"""Last update time. Unix timestamp (ms).
        :rtype: int
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._EntryId = params.get("EntryId")
        self._SourceTerm = params.get("SourceTerm")
        self._TargetTerm = params.get("TargetTerm")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GlossaryItem(AbstractModel):
    r"""Termbase detail

    """

    def __init__(self):
        r"""
        :param _GlossaryId: Termbase ID.
        :type GlossaryId: str
        :param _Name: Terminology repository name.
        :type Name: str
        :param _Description: Repository description.
        :type Description: str
        :param _Source: Source language code.
        :type Source: str
        :param _Target: Target language code.
        :type Target: str
        :param _CreatedTime: Creation time.
        :type CreatedTime: str
        :param _UpdatedTime: Update time.
        :type UpdatedTime: str
        """
        self._GlossaryId = None
        self._Name = None
        self._Description = None
        self._Source = None
        self._Target = None
        self._CreatedTime = None
        self._UpdatedTime = None

    @property
    def GlossaryId(self):
        r"""Termbase ID.
        :rtype: str
        """
        return self._GlossaryId

    @GlossaryId.setter
    def GlossaryId(self, GlossaryId):
        self._GlossaryId = GlossaryId

    @property
    def Name(self):
        r"""Terminology repository name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""Repository description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Source(self):
        r"""Source language code.
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""Target language code.
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def CreatedTime(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        r"""Update time.
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime


    def _deserialize(self, params):
        self._GlossaryId = params.get("GlossaryId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiKeyInfoRequest(AbstractModel):
    r"""ModifyApiKeyInfo request structure.

    """


class ModifyApiKeyInfoResponse(AbstractModel):
    r"""ModifyApiKeyInfo response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyApiKeyStatusRequest(AbstractModel):
    r"""ModifyApiKeyStatus request structure.

    """


class ModifyApiKeyStatusResponse(AbstractModel):
    r"""ModifyApiKeyStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyGlossaryEntriesRequest(AbstractModel):
    r"""ModifyGlossaryEntries request structure.

    """

    def __init__(self):
        r"""
        :param _GlossaryId: Termbase ID. Obtain through the API DescribeGlossaries.
        :type GlossaryId: str
        :param _Entries: Terminology entry list. At a time 200.
        :type Entries: list of ModifyGlossaryEntryInput
        """
        self._GlossaryId = None
        self._Entries = None

    @property
    def GlossaryId(self):
        r"""Termbase ID. Obtain through the API DescribeGlossaries.
        :rtype: str
        """
        return self._GlossaryId

    @GlossaryId.setter
    def GlossaryId(self, GlossaryId):
        self._GlossaryId = GlossaryId

    @property
    def Entries(self):
        r"""Terminology entry list. At a time 200.
        :rtype: list of ModifyGlossaryEntryInput
        """
        return self._Entries

    @Entries.setter
    def Entries(self, Entries):
        self._Entries = Entries


    def _deserialize(self, params):
        self._GlossaryId = params.get("GlossaryId")
        if params.get("Entries") is not None:
            self._Entries = []
            for item in params.get("Entries"):
                obj = ModifyGlossaryEntryInput()
                obj._deserialize(item)
                self._Entries.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGlossaryEntriesResponse(AbstractModel):
    r"""ModifyGlossaryEntries response structure.

    """

    def __init__(self):
        r"""
        :param _Entries: Terminology entry list after modification.
        :type Entries: list of GlossaryEntryItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Entries = None
        self._RequestId = None

    @property
    def Entries(self):
        r"""Terminology entry list after modification.
        :rtype: list of GlossaryEntryItem
        """
        return self._Entries

    @Entries.setter
    def Entries(self, Entries):
        self._Entries = Entries

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
        if params.get("Entries") is not None:
            self._Entries = []
            for item in params.get("Entries"):
                obj = GlossaryEntryItem()
                obj._deserialize(item)
                self._Entries.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyGlossaryEntryInput(AbstractModel):
    r"""Modify terminology entry

    """

    def __init__(self):
        r"""
        :param _EntryId: Terminology entry ID. Obtain through the API DescribeGlossaryEntries.
        :type EntryId: str
        :param _SourceTerm: Source language terminology. Maximum 1000 characters. If not passed, remain unchanged.
        :type SourceTerm: str
        :param _TargetTerm: Target language terminology. Maximum 1000 characters. Remain unchanged if not passed.
        :type TargetTerm: str
        """
        self._EntryId = None
        self._SourceTerm = None
        self._TargetTerm = None

    @property
    def EntryId(self):
        r"""Terminology entry ID. Obtain through the API DescribeGlossaryEntries.
        :rtype: str
        """
        return self._EntryId

    @EntryId.setter
    def EntryId(self, EntryId):
        self._EntryId = EntryId

    @property
    def SourceTerm(self):
        r"""Source language terminology. Maximum 1000 characters. If not passed, remain unchanged.
        :rtype: str
        """
        return self._SourceTerm

    @SourceTerm.setter
    def SourceTerm(self, SourceTerm):
        self._SourceTerm = SourceTerm

    @property
    def TargetTerm(self):
        r"""Target language terminology. Maximum 1000 characters. Remain unchanged if not passed.
        :rtype: str
        """
        return self._TargetTerm

    @TargetTerm.setter
    def TargetTerm(self, TargetTerm):
        self._TargetTerm = TargetTerm


    def _deserialize(self, params):
        self._EntryId = params.get("EntryId")
        self._SourceTerm = params.get("SourceTerm")
        self._TargetTerm = params.get("TargetTerm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuotaInfo(AbstractModel):
    r"""Token quota information

    """

    def __init__(self):
        r"""
        :param _PkgId: Quota package ID.
        :type PkgId: str
        :param _Status: Package status. Value: 1 (normal), 3 (exhausted), 4 (terminated).
        :type Status: int
        :param _CycleUnit: Quota period. Value: d (by day), m (monthly), lifetime (total quota, no reset).
        :type CycleUnit: str
        :param _CycleCredits: Dimensional quota total amount (number of tokens). Use string to avoid precision loss.
        :type CycleCredits: str
        :param _CycleUsed: Dimensional used amount (number of tokens). Use string literal to avoid precision loss.
        :type CycleUsed: str
        :param _StartTime: Quota effective start time.
        :type StartTime: str
        :param _ExpireTime: Quota expiration time.
        :type ExpireTime: str
        """
        self._PkgId = None
        self._Status = None
        self._CycleUnit = None
        self._CycleCredits = None
        self._CycleUsed = None
        self._StartTime = None
        self._ExpireTime = None

    @property
    def PkgId(self):
        r"""Quota package ID.
        :rtype: str
        """
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def Status(self):
        r"""Package status. Value: 1 (normal), 3 (exhausted), 4 (terminated).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CycleUnit(self):
        r"""Quota period. Value: d (by day), m (monthly), lifetime (total quota, no reset).
        :rtype: str
        """
        return self._CycleUnit

    @CycleUnit.setter
    def CycleUnit(self, CycleUnit):
        self._CycleUnit = CycleUnit

    @property
    def CycleCredits(self):
        r"""Dimensional quota total amount (number of tokens). Use string to avoid precision loss.
        :rtype: str
        """
        return self._CycleCredits

    @CycleCredits.setter
    def CycleCredits(self, CycleCredits):
        self._CycleCredits = CycleCredits

    @property
    def CycleUsed(self):
        r"""Dimensional used amount (number of tokens). Use string literal to avoid precision loss.
        :rtype: str
        """
        return self._CycleUsed

    @CycleUsed.setter
    def CycleUsed(self, CycleUsed):
        self._CycleUsed = CycleUsed

    @property
    def StartTime(self):
        r"""Quota effective start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpireTime(self):
        r"""Quota expiration time.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._PkgId = params.get("PkgId")
        self._Status = params.get("Status")
        self._CycleUnit = params.get("CycleUnit")
        self._CycleCredits = params.get("CycleCredits")
        self._CycleUsed = params.get("CycleUsed")
        self._StartTime = params.get("StartTime")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestFilter(AbstractModel):
    r"""Filter criteria

    """

    def __init__(self):
        r"""
        :param _Name: Filter field name.
        :type Name: str
        :param _Op: Filter operator. Values: EXACT (exact match), FUZZY (fuzzy matching), NOT (exclusion).
        :type Op: str
        :param _Values: Filter value list. Supports up to 10.
        :type Values: list of str
        """
        self._Name = None
        self._Op = None
        self._Values = None

    @property
    def Name(self):
        r"""Filter field name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Op(self):
        r"""Filter operator. Values: EXACT (exact match), FUZZY (fuzzy matching), NOT (exclusion).
        :rtype: str
        """
        return self._Op

    @Op.setter
    def Op(self, Op):
        self._Op = Op

    @property
    def Values(self):
        r"""Filter value list. Supports up to 10.
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Op = params.get("Op")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestSort(AbstractModel):
    r"""Sort criteria

    """

    def __init__(self):
        r"""
        :param _Name: Sorting field name.
        :type Name: str
        :param _Order: Sorting order. Value: ASC (ascending), DESC (descending).
        :type Order: str
        """
        self._Name = None
        self._Order = None

    @property
    def Name(self):
        r"""Sorting field name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Order(self):
        r"""Sorting order. Value: ASC (ascending), DESC (descending).
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        