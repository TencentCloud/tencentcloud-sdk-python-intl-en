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
        


class BatchCreateFailedItem(AbstractModel):
    r"""Batch create failed items

    """

    def __init__(self):
        r"""
        :param _Index: Serial number of the failed item (starting from 1, corresponding to the suffix number).
        :type Index: int
        :param _Name: Name of the failed item.
        :type Name: str
        :param _Reason: Failure reason.
        :type Reason: str
        """
        self._Index = None
        self._Name = None
        self._Reason = None

    @property
    def Index(self):
        r"""Serial number of the failed item (starting from 1, corresponding to the suffix number).
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Name(self):
        r"""Name of the failed item.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Reason(self):
        r"""Failure reason.
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Name = params.get("Name")
        self._Reason = params.get("Reason")
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


class CreateApiKeysResultItem(AbstractModel):
    r"""Batch create succeeded items

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: APIKey ID.
        :type ApiKeyId: str
        """
        self._ApiKeyId = None

    @property
    def ApiKeyId(self):
        r"""APIKey ID.
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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


class CreateTokenPlanApiKeysRequest(AbstractModel):
    r"""CreateTokenPlanApiKeys request structure.

    """

    def __init__(self):
        r"""
        :param _TeamId: Package ID. You can obtain it through the DescribeTokenPlanList API.
        :type TeamId: str
        :param _ApiKeyName: API key name, up to 128 characters. If the number of API keys created exceeds 1, the actual name format is {ApiKeyName}-{serial number} (for example, mykey-1, mykey-2).
        :type ApiKeyName: str
        :param _Count: Number of creations. Value range: 1–10.
        :type Count: int
        :param _AllowedModels: List of available models. If the package type is the enterprise edition professional package, you can specify a model or pass in "all". "all" means all models supported by the package are available for use. To specify specific models, pass in Model IDs. "all" and specific Model IDs cannot be specified at the same time. If not provided, it indicates the API Key does not support any models, thereby impacting normal use of the API Key. If the package type is the enterprise edition lite package, this field will be force overwritten to ["auto"] regardless of whether it is provided and what value is passed in.
        :type AllowedModels: list of str
        :param _ExclusiveQuota: Exclusive reserved quota. If not passed in, the value is `0`, which means no exclusive reserved quota is assigned to the API Key. Measurement units are as follows:
-Package type is professional, unit value is points;
-Package type is lite package, and the measurement unit is token.
        :type ExclusiveQuota: int
        :param _TotalQuota: Total credit limit. -1 means unlimited. It must be -1 or greater than or equal to the current ExclusiveQuota of the API Key. If not passed, no upper limit is set. The units are as follows:
-Package type is professional, unit value is points;
-Package type is lite package, and the measurement unit is token.
        :type TotalQuota: int
        :param _TPM: TPM (Tokens Per Minute) limit. If not passed, the plan-level TPM is used. Must be >= 0 and <= the package TPM.
        :type TPM: int
        """
        self._TeamId = None
        self._ApiKeyName = None
        self._Count = None
        self._AllowedModels = None
        self._ExclusiveQuota = None
        self._TotalQuota = None
        self._TPM = None

    @property
    def TeamId(self):
        r"""Package ID. You can obtain it through the DescribeTokenPlanList API.
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def ApiKeyName(self):
        r"""API key name, up to 128 characters. If the number of API keys created exceeds 1, the actual name format is {ApiKeyName}-{serial number} (for example, mykey-1, mykey-2).
        :rtype: str
        """
        return self._ApiKeyName

    @ApiKeyName.setter
    def ApiKeyName(self, ApiKeyName):
        self._ApiKeyName = ApiKeyName

    @property
    def Count(self):
        r"""Number of creations. Value range: 1–10.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def AllowedModels(self):
        r"""List of available models. If the package type is the enterprise edition professional package, you can specify a model or pass in "all". "all" means all models supported by the package are available for use. To specify specific models, pass in Model IDs. "all" and specific Model IDs cannot be specified at the same time. If not provided, it indicates the API Key does not support any models, thereby impacting normal use of the API Key. If the package type is the enterprise edition lite package, this field will be force overwritten to ["auto"] regardless of whether it is provided and what value is passed in.
        :rtype: list of str
        """
        return self._AllowedModels

    @AllowedModels.setter
    def AllowedModels(self, AllowedModels):
        self._AllowedModels = AllowedModels

    @property
    def ExclusiveQuota(self):
        r"""Exclusive reserved quota. If not passed in, the value is `0`, which means no exclusive reserved quota is assigned to the API Key. Measurement units are as follows:
-Package type is professional, unit value is points;
-Package type is lite package, and the measurement unit is token.
        :rtype: int
        """
        return self._ExclusiveQuota

    @ExclusiveQuota.setter
    def ExclusiveQuota(self, ExclusiveQuota):
        self._ExclusiveQuota = ExclusiveQuota

    @property
    def TotalQuota(self):
        r"""Total credit limit. -1 means unlimited. It must be -1 or greater than or equal to the current ExclusiveQuota of the API Key. If not passed, no upper limit is set. The units are as follows:
-Package type is professional, unit value is points;
-Package type is lite package, and the measurement unit is token.
        :rtype: int
        """
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def TPM(self):
        r"""TPM (Tokens Per Minute) limit. If not passed, the plan-level TPM is used. Must be >= 0 and <= the package TPM.
        :rtype: int
        """
        return self._TPM

    @TPM.setter
    def TPM(self, TPM):
        self._TPM = TPM


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._ApiKeyName = params.get("ApiKeyName")
        self._Count = params.get("Count")
        self._AllowedModels = params.get("AllowedModels")
        self._ExclusiveQuota = params.get("ExclusiveQuota")
        self._TotalQuota = params.get("TotalQuota")
        self._TPM = params.get("TPM")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTokenPlanApiKeysResponse(AbstractModel):
    r"""CreateTokenPlanApiKeys response structure.

    """

    def __init__(self):
        r"""
        :param _Items: Item list of successful creation.
        :type Items: list of CreateApiKeysResultItem
        :param _FailedItems: Item list that failed to be created.
        :type FailedItems: list of BatchCreateFailedItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._FailedItems = None
        self._RequestId = None

    @property
    def Items(self):
        r"""Item list of successful creation.
        :rtype: list of CreateApiKeysResultItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def FailedItems(self):
        r"""Item list that failed to be created.
        :rtype: list of BatchCreateFailedItem
        """
        return self._FailedItems

    @FailedItems.setter
    def FailedItems(self, FailedItems):
        self._FailedItems = FailedItems

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
                obj = CreateApiKeysResultItem()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("FailedItems") is not None:
            self._FailedItems = []
            for item in params.get("FailedItems"):
                obj = BatchCreateFailedItem()
                obj._deserialize(item)
                self._FailedItems.append(obj)
        self._RequestId = params.get("RequestId")


class CreateTokenPlanTeamOrderAndBuyRequest(AbstractModel):
    r"""CreateTokenPlanTeamOrderAndBuy request structure.

    """

    def __init__(self):
        r"""
        :param _ProductType: <p>Package type. Value: enterprise (enterprise edition professional package), enterprise-auto (enterprise edition lite package).</p>
        :type ProductType: str
        :param _TeamName: <p>Package name. It can only contain Chinese, letters, digits, underscores, and hyphens. It must start with a Chinese character or a letter and end with a Chinese character, letter, or digit. The length should be 2-50 characters.</p>
        :type TeamName: str
        :param _TimeSpan: <p>Purchase duration. Unit: Month. It must be greater than 0, supporting 1 to 12 months.</p>
        :type TimeSpan: int
        :param _CreditOrToken: <p>Specification of the purchased package. If the package type is enterprise, the measurement unit is point; if the package type is enterprise-auto, the measurement unit is tokens.</p>
        :type CreditOrToken: int
        :param _EnableAutoRenew: <p>Whether to enable auto-renewal. Not enabled by default.</p>
        :type EnableAutoRenew: bool
        :param _TeamId: <p>Existing package ID (if not empty, the renewal process is performed; if empty, a new purchase is performed)</p>
        :type TeamId: str
        """
        self._ProductType = None
        self._TeamName = None
        self._TimeSpan = None
        self._CreditOrToken = None
        self._EnableAutoRenew = None
        self._TeamId = None

    @property
    def ProductType(self):
        r"""<p>Package type. Value: enterprise (enterprise edition professional package), enterprise-auto (enterprise edition lite package).</p>
        :rtype: str
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def TeamName(self):
        r"""<p>Package name. It can only contain Chinese, letters, digits, underscores, and hyphens. It must start with a Chinese character or a letter and end with a Chinese character, letter, or digit. The length should be 2-50 characters.</p>
        :rtype: str
        """
        return self._TeamName

    @TeamName.setter
    def TeamName(self, TeamName):
        self._TeamName = TeamName

    @property
    def TimeSpan(self):
        r"""<p>Purchase duration. Unit: Month. It must be greater than 0, supporting 1 to 12 months.</p>
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def CreditOrToken(self):
        r"""<p>Specification of the purchased package. If the package type is enterprise, the measurement unit is point; if the package type is enterprise-auto, the measurement unit is tokens.</p>
        :rtype: int
        """
        return self._CreditOrToken

    @CreditOrToken.setter
    def CreditOrToken(self, CreditOrToken):
        self._CreditOrToken = CreditOrToken

    @property
    def EnableAutoRenew(self):
        r"""<p>Whether to enable auto-renewal. Not enabled by default.</p>
        :rtype: bool
        """
        return self._EnableAutoRenew

    @EnableAutoRenew.setter
    def EnableAutoRenew(self, EnableAutoRenew):
        self._EnableAutoRenew = EnableAutoRenew

    @property
    def TeamId(self):
        r"""<p>Existing package ID (if not empty, the renewal process is performed; if empty, a new purchase is performed)</p>
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId


    def _deserialize(self, params):
        self._ProductType = params.get("ProductType")
        self._TeamName = params.get("TeamName")
        self._TimeSpan = params.get("TimeSpan")
        self._CreditOrToken = params.get("CreditOrToken")
        self._EnableAutoRenew = params.get("EnableAutoRenew")
        self._TeamId = params.get("TeamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTokenPlanTeamOrderAndBuyResponse(AbstractModel):
    r"""CreateTokenPlanTeamOrderAndBuy response structure.

    """

    def __init__(self):
        r"""
        :param _BigOrderId: <p>Tencent Cloud order ID. Used to associate all sub-orders under a purchase operation.</p>
        :type BigOrderId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BigOrderId = None
        self._RequestId = None

    @property
    def BigOrderId(self):
        r"""<p>Tencent Cloud order ID. Used to associate all sub-orders under a purchase operation.</p>
        :rtype: str
        """
        return self._BigOrderId

    @BigOrderId.setter
    def BigOrderId(self, BigOrderId):
        self._BigOrderId = BigOrderId

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
        self._BigOrderId = params.get("BigOrderId")
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


class DeleteTokenPlanApiKeyRequest(AbstractModel):
    r"""DeleteTokenPlanApiKey request structure.

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID. You can obtain it through the DescribeTokenPlanApiKeyList API.
        :type ApiKeyId: str
        """
        self._ApiKeyId = None

    @property
    def ApiKeyId(self):
        r"""API Key ID. You can obtain it through the DescribeTokenPlanApiKeyList API.
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTokenPlanApiKeyResponse(AbstractModel):
    r"""DeleteTokenPlanApiKey response structure.

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


class DescribeTokenPlanApiKeyListRequest(AbstractModel):
    r"""DescribeTokenPlanApiKeyList request structure.

    """

    def __init__(self):
        r"""
        :param _TeamId: Package ID. You can obtain it through the DescribeTokenPlanList API.
        :type TeamId: str
        :param _Offset: Offset of paginated query. Default value: 0.
        :type Offset: int
        :param _Limit: Number of results returned by paging query. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Filters: Paginate the list of query filter criteria. Supported filter fields: ApiKeyId (API Key ID), Name (API Key name), Status (whether the API Key is available), StopReason (reason for disabling the API Key), UseStatus (API Key user-side switch).
        :type Filters: list of RequestFilter
        :param _Sorts: Paginate the list of sorting criteria. Supported sorting fields: CreatedAt (creation time) and UpdatedAt (update time). By default, results are sorted by CreatedAt in descending order.
        :type Sorts: list of RequestSort
        """
        self._TeamId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Sorts = None

    @property
    def TeamId(self):
        r"""Package ID. You can obtain it through the DescribeTokenPlanList API.
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def Offset(self):
        r"""Offset of paginated query. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of results returned by paging query. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""Paginate the list of query filter criteria. Supported filter fields: ApiKeyId (API Key ID), Name (API Key name), Status (whether the API Key is available), StopReason (reason for disabling the API Key), UseStatus (API Key user-side switch).
        :rtype: list of RequestFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Sorts(self):
        r"""Paginate the list of sorting criteria. Supported sorting fields: CreatedAt (creation time) and UpdatedAt (update time). By default, results are sorted by CreatedAt in descending order.
        :rtype: list of RequestSort
        """
        return self._Sorts

    @Sorts.setter
    def Sorts(self, Sorts):
        self._Sorts = Sorts


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeTokenPlanApiKeyListResponse(AbstractModel):
    r"""DescribeTokenPlanApiKeyList response structure.

    """

    def __init__(self):
        r"""
        :param _ApiKeySet: API Key list.
        :type ApiKeySet: list of TokenPlanApiKeyListItem
        :param _TotalCount: Total number of API Keys.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApiKeySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ApiKeySet(self):
        r"""API Key list.
        :rtype: list of TokenPlanApiKeyListItem
        """
        return self._ApiKeySet

    @ApiKeySet.setter
    def ApiKeySet(self, ApiKeySet):
        self._ApiKeySet = ApiKeySet

    @property
    def TotalCount(self):
        r"""Total number of API Keys.
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
                obj = TokenPlanApiKeyListItem()
                obj._deserialize(item)
                self._ApiKeySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTokenPlanApiKeyRequest(AbstractModel):
    r"""DescribeTokenPlanApiKey request structure.

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID. You can obtain it through the DescribeTokenPlanApiKeyList API.
        :type ApiKeyId: str
        """
        self._ApiKeyId = None

    @property
    def ApiKeyId(self):
        r"""API Key ID. You can obtain it through the DescribeTokenPlanApiKeyList API.
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenPlanApiKeyResponse(AbstractModel):
    r"""DescribeTokenPlanApiKey response structure.

    """

    def __init__(self):
        r"""
        :param _ApiKey: API Key details.
        :type ApiKey: :class:`tencentcloud.tokenhub.v20260322.models.TokenPlanApiKeyInfo`
        :param _Balance: API Key limit and usage information.
        :type Balance: :class:`tencentcloud.tokenhub.v20260322.models.SubPackageBalance`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApiKey = None
        self._Balance = None
        self._RequestId = None

    @property
    def ApiKey(self):
        r"""API Key details.
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.TokenPlanApiKeyInfo`
        """
        return self._ApiKey

    @ApiKey.setter
    def ApiKey(self, ApiKey):
        self._ApiKey = ApiKey

    @property
    def Balance(self):
        r"""API Key limit and usage information.
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.SubPackageBalance`
        """
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

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
        if params.get("ApiKey") is not None:
            self._ApiKey = TokenPlanApiKeyInfo()
            self._ApiKey._deserialize(params.get("ApiKey"))
        if params.get("Balance") is not None:
            self._Balance = SubPackageBalance()
            self._Balance._deserialize(params.get("Balance"))
        self._RequestId = params.get("RequestId")


class DescribeTokenPlanApiKeySecretRequest(AbstractModel):
    r"""DescribeTokenPlanApiKeySecret request structure.

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID. You can obtain it through the DescribeTokenPlanApiKeyList API.
        :type ApiKeyId: str
        """
        self._ApiKeyId = None

    @property
    def ApiKeyId(self):
        r"""API Key ID. You can obtain it through the DescribeTokenPlanApiKeyList API.
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenPlanApiKeySecretResponse(AbstractModel):
    r"""DescribeTokenPlanApiKeySecret response structure.

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: APIKey ID.
        :type ApiKeyId: str
        :param _ApiKey: APIKey key value (plaintext). Keep it safe.
        :type ApiKey: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApiKeyId = None
        self._ApiKey = None
        self._RequestId = None

    @property
    def ApiKeyId(self):
        r"""APIKey ID.
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId

    @property
    def ApiKey(self):
        r"""APIKey key value (plaintext). Keep it safe.
        :rtype: str
        """
        return self._ApiKey

    @ApiKey.setter
    def ApiKey(self, ApiKey):
        self._ApiKey = ApiKey

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
        self._ApiKey = params.get("ApiKey")
        self._RequestId = params.get("RequestId")


class DescribeTokenPlanApiKeyUsageDetailRequest(AbstractModel):
    r"""DescribeTokenPlanApiKeyUsageDetail request structure.

    """


class DescribeTokenPlanApiKeyUsageDetailResponse(AbstractModel):
    r"""DescribeTokenPlanApiKeyUsageDetail response structure.

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


class DescribeTokenPlanListRequest(AbstractModel):
    r"""DescribeTokenPlanList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset of paginated query. Default value: 0.
        :type Offset: int
        :param _Limit: Number of results returned by paging query. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Filters: Paginate the query filter criteria list. Supported filter fields: TeamId (Package ID), Name (package name), StopReason (disable reason), ProductType (package type).
        :type Filters: list of RequestFilter
        :param _Sorts: List of sorting criteria. Supported sorting fields: CreatedAt (creation time) and UpdatedAt (update time). By default, results are sorted by CreatedAt in descending order.
        :type Sorts: list of RequestSort
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Sorts = None

    @property
    def Offset(self):
        r"""Offset of paginated query. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of results returned by paging query. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""Paginate the query filter criteria list. Supported filter fields: TeamId (Package ID), Name (package name), StopReason (disable reason), ProductType (package type).
        :rtype: list of RequestFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Sorts(self):
        r"""List of sorting criteria. Supported sorting fields: CreatedAt (creation time) and UpdatedAt (update time). By default, results are sorted by CreatedAt in descending order.
        :rtype: list of RequestSort
        """
        return self._Sorts

    @Sorts.setter
    def Sorts(self, Sorts):
        self._Sorts = Sorts


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeTokenPlanListResponse(AbstractModel):
    r"""DescribeTokenPlanList response structure.

    """

    def __init__(self):
        r"""
        :param _TokenPlanSet: List of package options.
        :type TokenPlanSet: list of TokenPlanListItem
        :param _TotalCount: Total number of packages.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TokenPlanSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TokenPlanSet(self):
        r"""List of package options.
        :rtype: list of TokenPlanListItem
        """
        return self._TokenPlanSet

    @TokenPlanSet.setter
    def TokenPlanSet(self, TokenPlanSet):
        self._TokenPlanSet = TokenPlanSet

    @property
    def TotalCount(self):
        r"""Total number of packages.
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
        if params.get("TokenPlanSet") is not None:
            self._TokenPlanSet = []
            for item in params.get("TokenPlanSet"):
                obj = TokenPlanListItem()
                obj._deserialize(item)
                self._TokenPlanSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTokenPlanRequest(AbstractModel):
    r"""DescribeTokenPlan request structure.

    """

    def __init__(self):
        r"""
        :param _TeamId: Package ID. You can obtain it through the DescribeTokenPlanList API.
        :type TeamId: str
        """
        self._TeamId = None

    @property
    def TeamId(self):
        r"""Package ID. You can obtain it through the DescribeTokenPlanList API.
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenPlanResponse(AbstractModel):
    r"""DescribeTokenPlan response structure.

    """

    def __init__(self):
        r"""
        :param _TeamId: Package ID
        :type TeamId: str
        :param _Name: Package name.
        :type Name: str
        :param _AppId: Root account APP ID.
        :type AppId: str
        :param _Uin: Main account UIN.
        :type Uin: str
        :param _Status: Status. Valid values: enable, disable.
        :type Status: str
        :param _StopReason: Disablement reason. Value: NORMAL, ISOLATED, FROZEN, EXHAUSTED, DESTROYED.
        :type StopReason: str
        :param _ApiKeyMax: Maximum number of API Keys that can be created.
        :type ApiKeyMax: int
        :param _PrepayResourceID: Cloud billing prepaid resource package ID.
        :type PrepayResourceID: str
        :param _Creator: Creator. Packages created by a sub-account show the sub-account UIN.
        :type Creator: str
        :param _CreatedAt: Creation time.
        :type CreatedAt: str
        :param _UpdatedAt: Update time.
        :type UpdatedAt: str
        :param _PackageInfo: Basic information of the package.
        :type PackageInfo: :class:`tencentcloud.tokenhub.v20260322.models.TokenPlanPackageInfo`
        :param _AutoRenewFlag: Auto-renewal flag. Value: 0 (manual renewal), 1 (auto renewal), 2 (no automatic renewal). It is not returned if not bound to a prepaid resource.
        :type AutoRenewFlag: int
        :param _ApiKeyCount: Current number of created API Keys.
        :type ApiKeyCount: int
        :param _TokenSummary: Token usage details in the current cycle
        :type TokenSummary: :class:`tencentcloud.tokenhub.v20260322.models.TokenSummary`
        :param _ProductType: Package type. Values: enterprise (Enterprise Professional package), enterprise-auto (Enterprise Light package)
        :type ProductType: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TeamId = None
        self._Name = None
        self._AppId = None
        self._Uin = None
        self._Status = None
        self._StopReason = None
        self._ApiKeyMax = None
        self._PrepayResourceID = None
        self._Creator = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._PackageInfo = None
        self._AutoRenewFlag = None
        self._ApiKeyCount = None
        self._TokenSummary = None
        self._ProductType = None
        self._RequestId = None

    @property
    def TeamId(self):
        r"""Package ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def Name(self):
        r"""Package name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AppId(self):
        r"""Root account APP ID.
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""Main account UIN.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

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
    def StopReason(self):
        r"""Disablement reason. Value: NORMAL, ISOLATED, FROZEN, EXHAUSTED, DESTROYED.
        :rtype: str
        """
        return self._StopReason

    @StopReason.setter
    def StopReason(self, StopReason):
        self._StopReason = StopReason

    @property
    def ApiKeyMax(self):
        r"""Maximum number of API Keys that can be created.
        :rtype: int
        """
        return self._ApiKeyMax

    @ApiKeyMax.setter
    def ApiKeyMax(self, ApiKeyMax):
        self._ApiKeyMax = ApiKeyMax

    @property
    def PrepayResourceID(self):
        r"""Cloud billing prepaid resource package ID.
        :rtype: str
        """
        return self._PrepayResourceID

    @PrepayResourceID.setter
    def PrepayResourceID(self, PrepayResourceID):
        self._PrepayResourceID = PrepayResourceID

    @property
    def Creator(self):
        r"""Creator. Packages created by a sub-account show the sub-account UIN.
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

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
        r"""Update time.
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def PackageInfo(self):
        r"""Basic information of the package.
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.TokenPlanPackageInfo`
        """
        return self._PackageInfo

    @PackageInfo.setter
    def PackageInfo(self, PackageInfo):
        self._PackageInfo = PackageInfo

    @property
    def AutoRenewFlag(self):
        r"""Auto-renewal flag. Value: 0 (manual renewal), 1 (auto renewal), 2 (no automatic renewal). It is not returned if not bound to a prepaid resource.
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def ApiKeyCount(self):
        r"""Current number of created API Keys.
        :rtype: int
        """
        return self._ApiKeyCount

    @ApiKeyCount.setter
    def ApiKeyCount(self, ApiKeyCount):
        self._ApiKeyCount = ApiKeyCount

    @property
    def TokenSummary(self):
        r"""Token usage details in the current cycle
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.TokenSummary`
        """
        return self._TokenSummary

    @TokenSummary.setter
    def TokenSummary(self, TokenSummary):
        self._TokenSummary = TokenSummary

    @property
    def ProductType(self):
        r"""Package type. Values: enterprise (Enterprise Professional package), enterprise-auto (Enterprise Light package)
        :rtype: str
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

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
        self._TeamId = params.get("TeamId")
        self._Name = params.get("Name")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Status = params.get("Status")
        self._StopReason = params.get("StopReason")
        self._ApiKeyMax = params.get("ApiKeyMax")
        self._PrepayResourceID = params.get("PrepayResourceID")
        self._Creator = params.get("Creator")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        if params.get("PackageInfo") is not None:
            self._PackageInfo = TokenPlanPackageInfo()
            self._PackageInfo._deserialize(params.get("PackageInfo"))
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._ApiKeyCount = params.get("ApiKeyCount")
        if params.get("TokenSummary") is not None:
            self._TokenSummary = TokenSummary()
            self._TokenSummary._deserialize(params.get("TokenSummary"))
        self._ProductType = params.get("ProductType")
        self._RequestId = params.get("RequestId")


class DescribeUsageRankListRequest(AbstractModel):
    r"""DescribeUsageRankList request structure.

    """

    def __init__(self):
        r"""
        :param _Dimension: <p>Statistical dimension. Values: apikey (statistics by APIKey), endpoint (statistics by access point), model (statistics by model).</p>
        :type Dimension: str
        :param _StartTime: <p>Start time (inclusive interval), in RFC3339 format.</p>
        :type StartTime: str
        :param _EndTime: <p>End time (open interval) in RFC3339 format. The maximum span from StartTime is 90 days.</p>
        :type EndTime: str
        :param _MetricType: <p>Metric family switch field.</p><ul><li>tokens (default): Token consumption chart (statistics=sum), supports Dimension = apikey/endpoint/model</li><li>search [to be launched]: Online search call count (statistics=sum), only supports Dimension = model</li><li>Other values return InvalidParameter.</li></ul><p>Enum values:</p><ul><li>tokens: tokens</li></ul>
        :type MetricType: str
        :param _Target: <p>Dimension filtering value. An empty string indicates querying all objects; a non-empty string indicates querying only the specified single object (for example, a designated APIKey ID). Maximum 256 characters.</p>
        :type Target: str
        :param _Period: <p>Statistical granularity (seconds). Value: 60, 300, 3600, 86400. Must not be less than the lower limit corresponding to the span: span ≤ 1 day → 60; 1–5 days → 300; 5–10 days → 3600; &gt; 10 days → 86400. Used only when ShowAll=false.</p>
        :type Period: int
        :param _Offset: <p>Pagination starting point, starting from 0, default 0. Ignore timing when ShowAll=true. Page size fixed as 10.</p>
        :type Offset: int
        :param _ShowAll: <p>Whether to return full result.</p><ul><li>false (default): Return TopList in pages by Offset (10 items per page). Each object contains <br>Series time series points for drawing curves.</li><li>true: Ignore Offset and return the full object list without Series (CSV export scenario).</li></ul>
        :type ShowAll: bool
        """
        self._Dimension = None
        self._StartTime = None
        self._EndTime = None
        self._MetricType = None
        self._Target = None
        self._Period = None
        self._Offset = None
        self._ShowAll = None

    @property
    def Dimension(self):
        r"""<p>Statistical dimension. Values: apikey (statistics by APIKey), endpoint (statistics by access point), model (statistics by model).</p>
        :rtype: str
        """
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension

    @property
    def StartTime(self):
        r"""<p>Start time (inclusive interval), in RFC3339 format.</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>End time (open interval) in RFC3339 format. The maximum span from StartTime is 90 days.</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricType(self):
        r"""<p>Metric family switch field.</p><ul><li>tokens (default): Token consumption chart (statistics=sum), supports Dimension = apikey/endpoint/model</li><li>search [to be launched]: Online search call count (statistics=sum), only supports Dimension = model</li><li>Other values return InvalidParameter.</li></ul><p>Enum values:</p><ul><li>tokens: tokens</li></ul>
        :rtype: str
        """
        return self._MetricType

    @MetricType.setter
    def MetricType(self, MetricType):
        self._MetricType = MetricType

    @property
    def Target(self):
        r"""<p>Dimension filtering value. An empty string indicates querying all objects; a non-empty string indicates querying only the specified single object (for example, a designated APIKey ID). Maximum 256 characters.</p>
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def Period(self):
        r"""<p>Statistical granularity (seconds). Value: 60, 300, 3600, 86400. Must not be less than the lower limit corresponding to the span: span ≤ 1 day → 60; 1–5 days → 300; 5–10 days → 3600; &gt; 10 days → 86400. Used only when ShowAll=false.</p>
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Offset(self):
        r"""<p>Pagination starting point, starting from 0, default 0. Ignore timing when ShowAll=true. Page size fixed as 10.</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ShowAll(self):
        r"""<p>Whether to return full result.</p><ul><li>false (default): Return TopList in pages by Offset (10 items per page). Each object contains <br>Series time series points for drawing curves.</li><li>true: Ignore Offset and return the full object list without Series (CSV export scenario).</li></ul>
        :rtype: bool
        """
        return self._ShowAll

    @ShowAll.setter
    def ShowAll(self, ShowAll):
        self._ShowAll = ShowAll


    def _deserialize(self, params):
        self._Dimension = params.get("Dimension")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricType = params.get("MetricType")
        self._Target = params.get("Target")
        self._Period = params.get("Period")
        self._Offset = params.get("Offset")
        self._ShowAll = params.get("ShowAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsageRankListResponse(AbstractModel):
    r"""DescribeUsageRankList response structure.

    """

    def __init__(self):
        r"""
        :param _Dimension: <p>Statistical dimension of the backfill request.</p>
        :type Dimension: str
        :param _MetricType: <p>Metrics family of the backfill request: tokens / search.</p>
        :type MetricType: str
        :param _MetricKeys: <p>List of metric keys actually included in Stats / Series / PageStats / TotalStats in this response, case-sensitive by MetricType: tokens=[Total,Input,Output,Cache], search=[SearchRequestCount,SearchCount]</p>
        :type MetricKeys: list of str
        :param _ViewName: <p>View (data source)</p>
        :type ViewName: str
        :param _Period: <p>Statistical granularity (in seconds) of the backfill request. It is 0 when ShowAll=true.</p>
        :type Period: int
        :param _StartTime: <p>Backfill the start time of the request.</p>
        :type StartTime: str
        :param _EndTime: <p>End time of the backfill request.</p>
        :type EndTime: str
        :param _Total: <p>Total number of objects.</p>
        :type Total: int
        :param _Offset: <p>Backfill the pagination starting point of the request. It is 0 when ShowAll=true.</p>
        :type Offset: int
        :param _Limit: <p>Page size. It is always 10. When ShowAll=true, it is Total.</p>
        :type Limit: int
        :param _Timestamps: <p>Timestamp sequence corresponding to the Series array (Unix seconds). Empty array when ShowAll=true.</p>
        :type Timestamps: list of int
        :param _TopList: <p>Object ranking list, sorted by <code>MetricKeys[0]</code> in descending order. When ShowAll=false, it is the 10 objects on the current page (including Series); when ShowAll=true, it is all objects (excluding Series, used for CSV export).</p>
        :type TopList: list of UsageRankItem
        :param _PageStats: <p>Pagination statistics result</p>
        :type PageStats: :class:`tencentcloud.tokenhub.v20260322.models.UsageStats`
        :param _TotalStats: <p>Total statistics result</p>
        :type TotalStats: :class:`tencentcloud.tokenhub.v20260322.models.UsageStats`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Dimension = None
        self._MetricType = None
        self._MetricKeys = None
        self._ViewName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Total = None
        self._Offset = None
        self._Limit = None
        self._Timestamps = None
        self._TopList = None
        self._PageStats = None
        self._TotalStats = None
        self._RequestId = None

    @property
    def Dimension(self):
        r"""<p>Statistical dimension of the backfill request.</p>
        :rtype: str
        """
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension

    @property
    def MetricType(self):
        r"""<p>Metrics family of the backfill request: tokens / search.</p>
        :rtype: str
        """
        return self._MetricType

    @MetricType.setter
    def MetricType(self, MetricType):
        self._MetricType = MetricType

    @property
    def MetricKeys(self):
        r"""<p>List of metric keys actually included in Stats / Series / PageStats / TotalStats in this response, case-sensitive by MetricType: tokens=[Total,Input,Output,Cache], search=[SearchRequestCount,SearchCount]</p>
        :rtype: list of str
        """
        return self._MetricKeys

    @MetricKeys.setter
    def MetricKeys(self, MetricKeys):
        self._MetricKeys = MetricKeys

    @property
    def ViewName(self):
        r"""<p>View (data source)</p>
        :rtype: str
        """
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def Period(self):
        r"""<p>Statistical granularity (in seconds) of the backfill request. It is 0 when ShowAll=true.</p>
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        r"""<p>Backfill the start time of the request.</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>End time of the backfill request.</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Total(self):
        r"""<p>Total number of objects.</p>
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Offset(self):
        r"""<p>Backfill the pagination starting point of the request. It is 0 when ShowAll=true.</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>Page size. It is always 10. When ShowAll=true, it is Total.</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Timestamps(self):
        r"""<p>Timestamp sequence corresponding to the Series array (Unix seconds). Empty array when ShowAll=true.</p>
        :rtype: list of int
        """
        return self._Timestamps

    @Timestamps.setter
    def Timestamps(self, Timestamps):
        self._Timestamps = Timestamps

    @property
    def TopList(self):
        r"""<p>Object ranking list, sorted by <code>MetricKeys[0]</code> in descending order. When ShowAll=false, it is the 10 objects on the current page (including Series); when ShowAll=true, it is all objects (excluding Series, used for CSV export).</p>
        :rtype: list of UsageRankItem
        """
        return self._TopList

    @TopList.setter
    def TopList(self, TopList):
        self._TopList = TopList

    @property
    def PageStats(self):
        r"""<p>Pagination statistics result</p>
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.UsageStats`
        """
        return self._PageStats

    @PageStats.setter
    def PageStats(self, PageStats):
        self._PageStats = PageStats

    @property
    def TotalStats(self):
        r"""<p>Total statistics result</p>
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.UsageStats`
        """
        return self._TotalStats

    @TotalStats.setter
    def TotalStats(self, TotalStats):
        self._TotalStats = TotalStats

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
        self._Dimension = params.get("Dimension")
        self._MetricType = params.get("MetricType")
        self._MetricKeys = params.get("MetricKeys")
        self._ViewName = params.get("ViewName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Total = params.get("Total")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Timestamps = params.get("Timestamps")
        if params.get("TopList") is not None:
            self._TopList = []
            for item in params.get("TopList"):
                obj = UsageRankItem()
                obj._deserialize(item)
                self._TopList.append(obj)
        if params.get("PageStats") is not None:
            self._PageStats = UsageStats()
            self._PageStats._deserialize(params.get("PageStats"))
        if params.get("TotalStats") is not None:
            self._TotalStats = UsageStats()
            self._TotalStats._deserialize(params.get("TotalStats"))
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
        


class ModifyTokenPlanApiKeyRequest(AbstractModel):
    r"""ModifyTokenPlanApiKey request structure.

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID.
        :type ApiKeyId: str
        :param _AllowedModels: Available model list. If this parameter is not specified, no modification is made.

- If the package type is enterprise professional:
1) Input "all": use all models supported by the package
2) Import Model ID: specify a specific model. "all" and a specific Model ID cannot be specified at the same time.

-If the package type is enterprise lightweight edition, do not pass in this parameter.
        :type AllowedModels: list of str
        :param _ExclusiveQuota: Dedicated limit. If this parameter is not specified, no modification will be made. Unit:

-Package type: professional. Measurement unit: point.
- Package type is lite package, and the measurement unit is token.
        :type ExclusiveQuota: int
        :param _TotalQuota: Total credit limit. -1 means unlimited. It must be -1 or greater than or equal to the current ExclusiveQuota of the API Key. If not passed, no modification is made. Measurement units are as follows:
-Package type: professional. Measurement unit: point.
- Package type is lite package, and the measurement unit is token.
        :type TotalQuota: int
        :param _UseStatus: Whether to enable the API Key. Values: enable (enable), disable (disable). If not passed, no modification is made.
        :type UseStatus: str
        :param _TPM: TPM (Tokens Per Minute) limit. If not passed, no modification will be made. Must be >= 0 and <= the package TPM.
        :type TPM: int
        """
        self._ApiKeyId = None
        self._AllowedModels = None
        self._ExclusiveQuota = None
        self._TotalQuota = None
        self._UseStatus = None
        self._TPM = None

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
    def AllowedModels(self):
        r"""Available model list. If this parameter is not specified, no modification is made.

- If the package type is enterprise professional:
1) Input "all": use all models supported by the package
2) Import Model ID: specify a specific model. "all" and a specific Model ID cannot be specified at the same time.

-If the package type is enterprise lightweight edition, do not pass in this parameter.
        :rtype: list of str
        """
        return self._AllowedModels

    @AllowedModels.setter
    def AllowedModels(self, AllowedModels):
        self._AllowedModels = AllowedModels

    @property
    def ExclusiveQuota(self):
        r"""Dedicated limit. If this parameter is not specified, no modification will be made. Unit:

-Package type: professional. Measurement unit: point.
- Package type is lite package, and the measurement unit is token.
        :rtype: int
        """
        return self._ExclusiveQuota

    @ExclusiveQuota.setter
    def ExclusiveQuota(self, ExclusiveQuota):
        self._ExclusiveQuota = ExclusiveQuota

    @property
    def TotalQuota(self):
        r"""Total credit limit. -1 means unlimited. It must be -1 or greater than or equal to the current ExclusiveQuota of the API Key. If not passed, no modification is made. Measurement units are as follows:
-Package type: professional. Measurement unit: point.
- Package type is lite package, and the measurement unit is token.
        :rtype: int
        """
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def UseStatus(self):
        r"""Whether to enable the API Key. Values: enable (enable), disable (disable). If not passed, no modification is made.
        :rtype: str
        """
        return self._UseStatus

    @UseStatus.setter
    def UseStatus(self, UseStatus):
        self._UseStatus = UseStatus

    @property
    def TPM(self):
        r"""TPM (Tokens Per Minute) limit. If not passed, no modification will be made. Must be >= 0 and <= the package TPM.
        :rtype: int
        """
        return self._TPM

    @TPM.setter
    def TPM(self, TPM):
        self._TPM = TPM


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        self._AllowedModels = params.get("AllowedModels")
        self._ExclusiveQuota = params.get("ExclusiveQuota")
        self._TotalQuota = params.get("TotalQuota")
        self._UseStatus = params.get("UseStatus")
        self._TPM = params.get("TPM")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTokenPlanApiKeyResponse(AbstractModel):
    r"""ModifyTokenPlanApiKey response structure.

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


class ModifyTokenPlanApiKeySecretRequest(AbstractModel):
    r"""ModifyTokenPlanApiKeySecret request structure.

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID. You can obtain it through the DescribeTokenPlanApiKeyList API.
        :type ApiKeyId: str
        """
        self._ApiKeyId = None

    @property
    def ApiKeyId(self):
        r"""API Key ID. You can obtain it through the DescribeTokenPlanApiKeyList API.
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTokenPlanApiKeySecretResponse(AbstractModel):
    r"""ModifyTokenPlanApiKeySecret response structure.

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID.
        :type ApiKeyId: str
        :param _KeyVersion: Key version after resetting.
        :type KeyVersion: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApiKeyId = None
        self._KeyVersion = None
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
    def KeyVersion(self):
        r"""Key version after resetting.
        :rtype: int
        """
        return self._KeyVersion

    @KeyVersion.setter
    def KeyVersion(self, KeyVersion):
        self._KeyVersion = KeyVersion

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
        self._KeyVersion = params.get("KeyVersion")
        self._RequestId = params.get("RequestId")


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
        


class RenewTokenPlanTeamOrderRequest(AbstractModel):
    r"""RenewTokenPlanTeamOrder request structure.

    """

    def __init__(self):
        r"""
        :param _TeamId: Package ID, which can be obtained through the DescribeTokenPlanList API.
        :type TeamId: str
        :param _TimeSpan: Renewal duration. Unit: month. Must be greater than 0.
        :type TimeSpan: int
        """
        self._TeamId = None
        self._TimeSpan = None

    @property
    def TeamId(self):
        r"""Package ID, which can be obtained through the DescribeTokenPlanList API.
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def TimeSpan(self):
        r"""Renewal duration. Unit: month. Must be greater than 0.
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._TimeSpan = params.get("TimeSpan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewTokenPlanTeamOrderResponse(AbstractModel):
    r"""RenewTokenPlanTeamOrder response structure.

    """

    def __init__(self):
        r"""
        :param _BigOrderId: Tencent Cloud order ID. Used to associate all sub-orders under a renewal operation.
        :type BigOrderId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BigOrderId = None
        self._RequestId = None

    @property
    def BigOrderId(self):
        r"""Tencent Cloud order ID. Used to associate all sub-orders under a renewal operation.
        :rtype: str
        """
        return self._BigOrderId

    @BigOrderId.setter
    def BigOrderId(self, BigOrderId):
        self._BigOrderId = BigOrderId

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
        self._BigOrderId = params.get("BigOrderId")
        self._RequestId = params.get("RequestId")


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
        


class SubPackageBalance(AbstractModel):
    r"""API Key limit and usage information

    """

    def __init__(self):
        r"""
        :param _ExclusiveQuota: Dedicated limit. Units are as follows:
-Package type: professional. Measurement unit: point.
- Package type is lite package, and the measurement unit is token.
        :type ExclusiveQuota: str
        :param _ExclusiveUsed: Used amount of the dedicated limit. The measurement units are as follows:
-Package type: professional. Measurement unit: point.
- Package type is lite package, and the measurement unit is token.
        :type ExclusiveUsed: str
        :param _ExclusiveRemain: Remaining exclusive quota. Units are as follows:
-Package type: professional. Measurement unit: point.
-Package type: lite package. Measurement unit: token.
        :type ExclusiveRemain: str
        :param _SharedQuota: Shared credit limit. -1 means unlimited. Measurement units are as follows:
-Package type is professional package, measurement unit value is point;
-Package type: lite package. Measurement unit: token.
        :type SharedQuota: str
        :param _SharedUsed: Used amount of the shared quota. Measurement units are as follows:
-Package type is professional package, measurement unit value is point;
-Package type: lite package. Measurement unit: token.
        :type SharedUsed: str
        :param _SharedRemain: Remaining shared quota. Units are described as follows:
-Package type is professional package, measurement unit value is point;
-Package type: lite package. Measurement unit: token.
        :type SharedRemain: str
        :param _Status: API Key package status. Valid values: 0 (normal), 1 (exhausted).
        :type Status: int
        """
        self._ExclusiveQuota = None
        self._ExclusiveUsed = None
        self._ExclusiveRemain = None
        self._SharedQuota = None
        self._SharedUsed = None
        self._SharedRemain = None
        self._Status = None

    @property
    def ExclusiveQuota(self):
        r"""Dedicated limit. Units are as follows:
-Package type: professional. Measurement unit: point.
- Package type is lite package, and the measurement unit is token.
        :rtype: str
        """
        return self._ExclusiveQuota

    @ExclusiveQuota.setter
    def ExclusiveQuota(self, ExclusiveQuota):
        self._ExclusiveQuota = ExclusiveQuota

    @property
    def ExclusiveUsed(self):
        r"""Used amount of the dedicated limit. The measurement units are as follows:
-Package type: professional. Measurement unit: point.
- Package type is lite package, and the measurement unit is token.
        :rtype: str
        """
        return self._ExclusiveUsed

    @ExclusiveUsed.setter
    def ExclusiveUsed(self, ExclusiveUsed):
        self._ExclusiveUsed = ExclusiveUsed

    @property
    def ExclusiveRemain(self):
        r"""Remaining exclusive quota. Units are as follows:
-Package type: professional. Measurement unit: point.
-Package type: lite package. Measurement unit: token.
        :rtype: str
        """
        return self._ExclusiveRemain

    @ExclusiveRemain.setter
    def ExclusiveRemain(self, ExclusiveRemain):
        self._ExclusiveRemain = ExclusiveRemain

    @property
    def SharedQuota(self):
        r"""Shared credit limit. -1 means unlimited. Measurement units are as follows:
-Package type is professional package, measurement unit value is point;
-Package type: lite package. Measurement unit: token.
        :rtype: str
        """
        return self._SharedQuota

    @SharedQuota.setter
    def SharedQuota(self, SharedQuota):
        self._SharedQuota = SharedQuota

    @property
    def SharedUsed(self):
        r"""Used amount of the shared quota. Measurement units are as follows:
-Package type is professional package, measurement unit value is point;
-Package type: lite package. Measurement unit: token.
        :rtype: str
        """
        return self._SharedUsed

    @SharedUsed.setter
    def SharedUsed(self, SharedUsed):
        self._SharedUsed = SharedUsed

    @property
    def SharedRemain(self):
        r"""Remaining shared quota. Units are described as follows:
-Package type is professional package, measurement unit value is point;
-Package type: lite package. Measurement unit: token.
        :rtype: str
        """
        return self._SharedRemain

    @SharedRemain.setter
    def SharedRemain(self, SharedRemain):
        self._SharedRemain = SharedRemain

    @property
    def Status(self):
        r"""API Key package status. Valid values: 0 (normal), 1 (exhausted).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ExclusiveQuota = params.get("ExclusiveQuota")
        self._ExclusiveUsed = params.get("ExclusiveUsed")
        self._ExclusiveRemain = params.get("ExclusiveRemain")
        self._SharedQuota = params.get("SharedQuota")
        self._SharedUsed = params.get("SharedUsed")
        self._SharedRemain = params.get("SharedRemain")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenPlanApiKeyInfo(AbstractModel):
    r"""Token Plan API Key details

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID.
        :type ApiKeyId: str
        :param _ApiKey: API Key secret key value (masked).
        :type ApiKey: str
        :param _Name: API Key name.
        :type Name: str
        :param _TeamId: Bundle ID.
        :type TeamId: str
        :param _AppId: Account APP ID.
        :type AppId: str
        :param _Uin: Main account UIN.
        :type Uin: str
        :param _AllowedModels: API Key available model list (JSON array string).
        :type AllowedModels: str
        :param _Status: Whether the API Key is available. Values: enable (enable), disable (disable).
        :type Status: str
        :param _StopReason: Reason for disabling the API Key. Valid values: NORMAL (normal, default value), QUOTA_EXHAUSTED (API Key quota package exhausted), ABNORMAL (exception, human intervention required)
        :type StopReason: str
        :param _UseStatus: User-side switch. Valid values: enable, disable.
        :type UseStatus: str
        :param _KeyVersion: Key version.
        :type KeyVersion: int
        :param _LastRotatedAt: Last reset time (ISO 8601).
        :type LastRotatedAt: str
        :param _Creator: Creator. If it is created by a sub-account, this value is the sub-account UIN.
        :type Creator: str
        :param _CreatedAt: Creation time.
        :type CreatedAt: str
        :param _UpdatedAt: Update time.
        :type UpdatedAt: str
        :param _TPM: TPM limit (Tokens Per Minute).
        :type TPM: int
        :param _ProductType: Package type. Values: enterprise (Enterprise Professional package), enterprise-auto (Enterprise Light package)
        :type ProductType: str
        """
        self._ApiKeyId = None
        self._ApiKey = None
        self._Name = None
        self._TeamId = None
        self._AppId = None
        self._Uin = None
        self._AllowedModels = None
        self._Status = None
        self._StopReason = None
        self._UseStatus = None
        self._KeyVersion = None
        self._LastRotatedAt = None
        self._Creator = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._TPM = None
        self._ProductType = None

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
    def ApiKey(self):
        r"""API Key secret key value (masked).
        :rtype: str
        """
        return self._ApiKey

    @ApiKey.setter
    def ApiKey(self, ApiKey):
        self._ApiKey = ApiKey

    @property
    def Name(self):
        r"""API Key name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TeamId(self):
        r"""Bundle ID.
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def AppId(self):
        r"""Account APP ID.
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""Main account UIN.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AllowedModels(self):
        r"""API Key available model list (JSON array string).
        :rtype: str
        """
        return self._AllowedModels

    @AllowedModels.setter
    def AllowedModels(self, AllowedModels):
        self._AllowedModels = AllowedModels

    @property
    def Status(self):
        r"""Whether the API Key is available. Values: enable (enable), disable (disable).
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StopReason(self):
        r"""Reason for disabling the API Key. Valid values: NORMAL (normal, default value), QUOTA_EXHAUSTED (API Key quota package exhausted), ABNORMAL (exception, human intervention required)
        :rtype: str
        """
        return self._StopReason

    @StopReason.setter
    def StopReason(self, StopReason):
        self._StopReason = StopReason

    @property
    def UseStatus(self):
        r"""User-side switch. Valid values: enable, disable.
        :rtype: str
        """
        return self._UseStatus

    @UseStatus.setter
    def UseStatus(self, UseStatus):
        self._UseStatus = UseStatus

    @property
    def KeyVersion(self):
        r"""Key version.
        :rtype: int
        """
        return self._KeyVersion

    @KeyVersion.setter
    def KeyVersion(self, KeyVersion):
        self._KeyVersion = KeyVersion

    @property
    def LastRotatedAt(self):
        r"""Last reset time (ISO 8601).
        :rtype: str
        """
        return self._LastRotatedAt

    @LastRotatedAt.setter
    def LastRotatedAt(self, LastRotatedAt):
        self._LastRotatedAt = LastRotatedAt

    @property
    def Creator(self):
        r"""Creator. If it is created by a sub-account, this value is the sub-account UIN.
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

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
        r"""Update time.
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def TPM(self):
        r"""TPM limit (Tokens Per Minute).
        :rtype: int
        """
        return self._TPM

    @TPM.setter
    def TPM(self, TPM):
        self._TPM = TPM

    @property
    def ProductType(self):
        r"""Package type. Values: enterprise (Enterprise Professional package), enterprise-auto (Enterprise Light package)
        :rtype: str
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        self._ApiKey = params.get("ApiKey")
        self._Name = params.get("Name")
        self._TeamId = params.get("TeamId")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._AllowedModels = params.get("AllowedModels")
        self._Status = params.get("Status")
        self._StopReason = params.get("StopReason")
        self._UseStatus = params.get("UseStatus")
        self._KeyVersion = params.get("KeyVersion")
        self._LastRotatedAt = params.get("LastRotatedAt")
        self._Creator = params.get("Creator")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._TPM = params.get("TPM")
        self._ProductType = params.get("ProductType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenPlanApiKeyListItem(AbstractModel):
    r"""Token Plan API Key list item

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID.
        :type ApiKeyId: str
        :param _ApiKey: API Key secret key value (masking).
        :type ApiKey: str
        :param _Name: API Key name.
        :type Name: str
        :param _TeamId: Bundle ID
        :type TeamId: str
        :param _AppId: Account APP ID.
        :type AppId: str
        :param _Uin: Main account UIN. Maximum 128 characters.
        :type Uin: str
        :param _AllowedModels: API Key available model list (JSON array string).
        :type AllowedModels: str
        :param _Status: Whether the API Key is available. Values: enable (enable), disable (disable).
        :type Status: str
        :param _StopReason: Reason for disabling the API Key. Value: NORMAL (normal, default value), QUOTA_EXHAUSTED (API Key quota package exhausted), ABNORMAL (abnormal, requires human intervention)
        :type StopReason: str
        :param _UseStatus: User-side switch. Valid values: enable, disable.
        :type UseStatus: str
        :param _KeyVersion: Key version.
        :type KeyVersion: int
        :param _LastRotatedAt: Last reset time (ISO 8601).
        :type LastRotatedAt: str
        :param _Creator: Creator. If it is created by a sub-account, this value is the sub-account UIN.
        :type Creator: str
        :param _CreatedAt: Creation time.
        :type CreatedAt: str
        :param _UpdatedAt: Update time.
        :type UpdatedAt: str
        :param _Balance: API Key limit usage information
        :type Balance: :class:`tencentcloud.tokenhub.v20260322.models.SubPackageBalance`
        :param _ProductType: Package type. Values: enterprise (Enterprise Professional package), enterprise-auto (Enterprise Light package).
        :type ProductType: str
        """
        self._ApiKeyId = None
        self._ApiKey = None
        self._Name = None
        self._TeamId = None
        self._AppId = None
        self._Uin = None
        self._AllowedModels = None
        self._Status = None
        self._StopReason = None
        self._UseStatus = None
        self._KeyVersion = None
        self._LastRotatedAt = None
        self._Creator = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._Balance = None
        self._ProductType = None

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
    def ApiKey(self):
        r"""API Key secret key value (masking).
        :rtype: str
        """
        return self._ApiKey

    @ApiKey.setter
    def ApiKey(self, ApiKey):
        self._ApiKey = ApiKey

    @property
    def Name(self):
        r"""API Key name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TeamId(self):
        r"""Bundle ID
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def AppId(self):
        r"""Account APP ID.
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""Main account UIN. Maximum 128 characters.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AllowedModels(self):
        r"""API Key available model list (JSON array string).
        :rtype: str
        """
        return self._AllowedModels

    @AllowedModels.setter
    def AllowedModels(self, AllowedModels):
        self._AllowedModels = AllowedModels

    @property
    def Status(self):
        r"""Whether the API Key is available. Values: enable (enable), disable (disable).
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StopReason(self):
        r"""Reason for disabling the API Key. Value: NORMAL (normal, default value), QUOTA_EXHAUSTED (API Key quota package exhausted), ABNORMAL (abnormal, requires human intervention)
        :rtype: str
        """
        return self._StopReason

    @StopReason.setter
    def StopReason(self, StopReason):
        self._StopReason = StopReason

    @property
    def UseStatus(self):
        r"""User-side switch. Valid values: enable, disable.
        :rtype: str
        """
        return self._UseStatus

    @UseStatus.setter
    def UseStatus(self, UseStatus):
        self._UseStatus = UseStatus

    @property
    def KeyVersion(self):
        r"""Key version.
        :rtype: int
        """
        return self._KeyVersion

    @KeyVersion.setter
    def KeyVersion(self, KeyVersion):
        self._KeyVersion = KeyVersion

    @property
    def LastRotatedAt(self):
        r"""Last reset time (ISO 8601).
        :rtype: str
        """
        return self._LastRotatedAt

    @LastRotatedAt.setter
    def LastRotatedAt(self, LastRotatedAt):
        self._LastRotatedAt = LastRotatedAt

    @property
    def Creator(self):
        r"""Creator. If it is created by a sub-account, this value is the sub-account UIN.
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

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
        r"""Update time.
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Balance(self):
        r"""API Key limit usage information
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.SubPackageBalance`
        """
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def ProductType(self):
        r"""Package type. Values: enterprise (Enterprise Professional package), enterprise-auto (Enterprise Light package).
        :rtype: str
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        self._ApiKey = params.get("ApiKey")
        self._Name = params.get("Name")
        self._TeamId = params.get("TeamId")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._AllowedModels = params.get("AllowedModels")
        self._Status = params.get("Status")
        self._StopReason = params.get("StopReason")
        self._UseStatus = params.get("UseStatus")
        self._KeyVersion = params.get("KeyVersion")
        self._LastRotatedAt = params.get("LastRotatedAt")
        self._Creator = params.get("Creator")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        if params.get("Balance") is not None:
            self._Balance = SubPackageBalance()
            self._Balance._deserialize(params.get("Balance"))
        self._ProductType = params.get("ProductType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenPlanListItem(AbstractModel):
    r"""Token Plan package option

    """

    def __init__(self):
        r"""
        :param _TeamId: <p>Package ID.</p>
        :type TeamId: str
        :param _ProductType: <p>Package type. Values: enterprise (Enterprise Professional package), enterprise-auto (Enterprise Light package)</p>
        :type ProductType: str
        :param _Name: <p>Package name. Maximum 128 characters.</p>
        :type Name: str
        :param _AppId: <p>Account APP ID.</p>
        :type AppId: str
        :param _Uin: <p>Main account UIN.</p>
        :type Uin: str
        :param _Status: <p>Package status. Valid values: enable, disable.</p>
        :type Status: str
        :param _StopReason: <p>Reason for package disablement. Value: NORMAL, ISOLATED, FROZEN, EXHAUSTED, DESTROYED</p>
        :type StopReason: str
        :param _ApiKeyMax: <p>Maximum number of API Keys that can be created.</p>
        :type ApiKeyMax: int
        :param _ApiKeyCount: <p>Number of API Keys currently created</p>
        :type ApiKeyCount: int
        :param _PrepayResourceID: <p>Cloud billing prepaid resource package ID.</p>
        :type PrepayResourceID: str
        :param _Creator: <p>Creator. If the package is created by a sub-account, this value is the sub-account UIN.</p>
        :type Creator: str
        :param _CreatedAt: <p>Creation time.</p>
        :type CreatedAt: str
        :param _UpdatedAt: <p>Update time.</p>
        :type UpdatedAt: str
        :param _PackageInfo: <p>Basic information of the package.</p>
        :type PackageInfo: :class:`tencentcloud.tokenhub.v20260322.models.TokenPlanPackageInfo`
        :param _AutoRenewFlag: <p>Whether to enable auto-renewal. Value: 0 (not enabled), 1 (enabled)</p>
        :type AutoRenewFlag: int
        """
        self._TeamId = None
        self._ProductType = None
        self._Name = None
        self._AppId = None
        self._Uin = None
        self._Status = None
        self._StopReason = None
        self._ApiKeyMax = None
        self._ApiKeyCount = None
        self._PrepayResourceID = None
        self._Creator = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._PackageInfo = None
        self._AutoRenewFlag = None

    @property
    def TeamId(self):
        r"""<p>Package ID.</p>
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def ProductType(self):
        r"""<p>Package type. Values: enterprise (Enterprise Professional package), enterprise-auto (Enterprise Light package)</p>
        :rtype: str
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def Name(self):
        r"""<p>Package name. Maximum 128 characters.</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AppId(self):
        r"""<p>Account APP ID.</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""<p>Main account UIN.</p>
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Status(self):
        r"""<p>Package status. Valid values: enable, disable.</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StopReason(self):
        r"""<p>Reason for package disablement. Value: NORMAL, ISOLATED, FROZEN, EXHAUSTED, DESTROYED</p>
        :rtype: str
        """
        return self._StopReason

    @StopReason.setter
    def StopReason(self, StopReason):
        self._StopReason = StopReason

    @property
    def ApiKeyMax(self):
        r"""<p>Maximum number of API Keys that can be created.</p>
        :rtype: int
        """
        return self._ApiKeyMax

    @ApiKeyMax.setter
    def ApiKeyMax(self, ApiKeyMax):
        self._ApiKeyMax = ApiKeyMax

    @property
    def ApiKeyCount(self):
        r"""<p>Number of API Keys currently created</p>
        :rtype: int
        """
        return self._ApiKeyCount

    @ApiKeyCount.setter
    def ApiKeyCount(self, ApiKeyCount):
        self._ApiKeyCount = ApiKeyCount

    @property
    def PrepayResourceID(self):
        r"""<p>Cloud billing prepaid resource package ID.</p>
        :rtype: str
        """
        return self._PrepayResourceID

    @PrepayResourceID.setter
    def PrepayResourceID(self, PrepayResourceID):
        self._PrepayResourceID = PrepayResourceID

    @property
    def Creator(self):
        r"""<p>Creator. If the package is created by a sub-account, this value is the sub-account UIN.</p>
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreatedAt(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""<p>Update time.</p>
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def PackageInfo(self):
        r"""<p>Basic information of the package.</p>
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.TokenPlanPackageInfo`
        """
        return self._PackageInfo

    @PackageInfo.setter
    def PackageInfo(self, PackageInfo):
        self._PackageInfo = PackageInfo

    @property
    def AutoRenewFlag(self):
        r"""<p>Whether to enable auto-renewal. Value: 0 (not enabled), 1 (enabled)</p>
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._ProductType = params.get("ProductType")
        self._Name = params.get("Name")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Status = params.get("Status")
        self._StopReason = params.get("StopReason")
        self._ApiKeyMax = params.get("ApiKeyMax")
        self._ApiKeyCount = params.get("ApiKeyCount")
        self._PrepayResourceID = params.get("PrepayResourceID")
        self._Creator = params.get("Creator")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        if params.get("PackageInfo") is not None:
            self._PackageInfo = TokenPlanPackageInfo()
            self._PackageInfo._deserialize(params.get("PackageInfo"))
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenPlanPackageInfo(AbstractModel):
    r"""Main limit package info

    """

    def __init__(self):
        r"""
        :param _TotalQuota: Total quota. The unit is determined by the package type: credits for the Enterprise Professional package and tokens for the Enterprise auto package.
        :type TotalQuota: str
        :param _TotalUsed: Total used quota. The unit varies by package type: credits (enterprise edition professional package), tokens (enterprise edition auto package)
        :type TotalUsed: str
        :param _TotalCycles: Total number of periods.
        :type TotalCycles: int
        :param _CycleUnit: Period unit. Value: month
        :type CycleUnit: str
        :param _StartTime: Package effective time.
        :type StartTime: str
        :param _ExpireTime: Package expiration time.
        :type ExpireTime: str
        :param _ExclusiveAllocated: Allocated quota for dedicated pool. The unit varies by package type: credits (enterprise edition professional package), tokens (enterprise edition auto package)
        :type ExclusiveAllocated: str
        :param _ExclusiveUsed: Used credit of the dedicated pool. The unit varies based on the package type: credits for the enterprise professional package, and tokens for the enterprise auto package.
        :type ExclusiveUsed: str
        :param _SharedPool: Total shared pool quota. The measurement unit varies based on the package type: credits (enterprise edition professional package), tokens (enterprise edition auto package).
        :type SharedPool: str
        :param _SharedUsed: Shared used credit. The unit varies by package type: credits (enterprise edition professional package), tokens (enterprise edition auto package)
        :type SharedUsed: str
        :param _CycleQuota: Current period limit. The unit varies by package type: credits (Enterprise Edition Professional), tokens (Enterprise Edition auto).
        :type CycleQuota: str
        :param _CurrentCycle: Current cycle.
        :type CurrentCycle: int
        :param _RemainCycles: Remaining cycle.
        :type RemainCycles: int
        """
        self._TotalQuota = None
        self._TotalUsed = None
        self._TotalCycles = None
        self._CycleUnit = None
        self._StartTime = None
        self._ExpireTime = None
        self._ExclusiveAllocated = None
        self._ExclusiveUsed = None
        self._SharedPool = None
        self._SharedUsed = None
        self._CycleQuota = None
        self._CurrentCycle = None
        self._RemainCycles = None

    @property
    def TotalQuota(self):
        r"""Total quota. The unit is determined by the package type: credits for the Enterprise Professional package and tokens for the Enterprise auto package.
        :rtype: str
        """
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def TotalUsed(self):
        r"""Total used quota. The unit varies by package type: credits (enterprise edition professional package), tokens (enterprise edition auto package)
        :rtype: str
        """
        return self._TotalUsed

    @TotalUsed.setter
    def TotalUsed(self, TotalUsed):
        self._TotalUsed = TotalUsed

    @property
    def TotalCycles(self):
        r"""Total number of periods.
        :rtype: int
        """
        return self._TotalCycles

    @TotalCycles.setter
    def TotalCycles(self, TotalCycles):
        self._TotalCycles = TotalCycles

    @property
    def CycleUnit(self):
        r"""Period unit. Value: month
        :rtype: str
        """
        return self._CycleUnit

    @CycleUnit.setter
    def CycleUnit(self, CycleUnit):
        self._CycleUnit = CycleUnit

    @property
    def StartTime(self):
        r"""Package effective time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpireTime(self):
        r"""Package expiration time.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ExclusiveAllocated(self):
        r"""Allocated quota for dedicated pool. The unit varies by package type: credits (enterprise edition professional package), tokens (enterprise edition auto package)
        :rtype: str
        """
        return self._ExclusiveAllocated

    @ExclusiveAllocated.setter
    def ExclusiveAllocated(self, ExclusiveAllocated):
        self._ExclusiveAllocated = ExclusiveAllocated

    @property
    def ExclusiveUsed(self):
        r"""Used credit of the dedicated pool. The unit varies based on the package type: credits for the enterprise professional package, and tokens for the enterprise auto package.
        :rtype: str
        """
        return self._ExclusiveUsed

    @ExclusiveUsed.setter
    def ExclusiveUsed(self, ExclusiveUsed):
        self._ExclusiveUsed = ExclusiveUsed

    @property
    def SharedPool(self):
        r"""Total shared pool quota. The measurement unit varies based on the package type: credits (enterprise edition professional package), tokens (enterprise edition auto package).
        :rtype: str
        """
        return self._SharedPool

    @SharedPool.setter
    def SharedPool(self, SharedPool):
        self._SharedPool = SharedPool

    @property
    def SharedUsed(self):
        r"""Shared used credit. The unit varies by package type: credits (enterprise edition professional package), tokens (enterprise edition auto package)
        :rtype: str
        """
        return self._SharedUsed

    @SharedUsed.setter
    def SharedUsed(self, SharedUsed):
        self._SharedUsed = SharedUsed

    @property
    def CycleQuota(self):
        r"""Current period limit. The unit varies by package type: credits (Enterprise Edition Professional), tokens (Enterprise Edition auto).
        :rtype: str
        """
        return self._CycleQuota

    @CycleQuota.setter
    def CycleQuota(self, CycleQuota):
        self._CycleQuota = CycleQuota

    @property
    def CurrentCycle(self):
        r"""Current cycle.
        :rtype: int
        """
        return self._CurrentCycle

    @CurrentCycle.setter
    def CurrentCycle(self, CurrentCycle):
        self._CurrentCycle = CurrentCycle

    @property
    def RemainCycles(self):
        r"""Remaining cycle.
        :rtype: int
        """
        return self._RemainCycles

    @RemainCycles.setter
    def RemainCycles(self, RemainCycles):
        self._RemainCycles = RemainCycles


    def _deserialize(self, params):
        self._TotalQuota = params.get("TotalQuota")
        self._TotalUsed = params.get("TotalUsed")
        self._TotalCycles = params.get("TotalCycles")
        self._CycleUnit = params.get("CycleUnit")
        self._StartTime = params.get("StartTime")
        self._ExpireTime = params.get("ExpireTime")
        self._ExclusiveAllocated = params.get("ExclusiveAllocated")
        self._ExclusiveUsed = params.get("ExclusiveUsed")
        self._SharedPool = params.get("SharedPool")
        self._SharedUsed = params.get("SharedUsed")
        self._CycleQuota = params.get("CycleQuota")
        self._CurrentCycle = params.get("CurrentCycle")
        self._RemainCycles = params.get("RemainCycles")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenSummary(AbstractModel):
    r"""Main package Token summary

    """

    def __init__(self):
        r"""
        :param _CycleSeq: Package serial number of the current billing cycle
        :type CycleSeq: int
        :param _CycleStartTime: Package billing cycle start time (RFC3339)
        :type CycleStartTime: str
        :param _CycleEndTime: Package billing cycle end time (RFC3339)
        :type CycleEndTime: str
        :param _BillingItems: Summary list of tokens grouped by billing item
        :type BillingItems: list of TokenSummaryBillingItem
        """
        self._CycleSeq = None
        self._CycleStartTime = None
        self._CycleEndTime = None
        self._BillingItems = None

    @property
    def CycleSeq(self):
        r"""Package serial number of the current billing cycle
        :rtype: int
        """
        return self._CycleSeq

    @CycleSeq.setter
    def CycleSeq(self, CycleSeq):
        self._CycleSeq = CycleSeq

    @property
    def CycleStartTime(self):
        r"""Package billing cycle start time (RFC3339)
        :rtype: str
        """
        return self._CycleStartTime

    @CycleStartTime.setter
    def CycleStartTime(self, CycleStartTime):
        self._CycleStartTime = CycleStartTime

    @property
    def CycleEndTime(self):
        r"""Package billing cycle end time (RFC3339)
        :rtype: str
        """
        return self._CycleEndTime

    @CycleEndTime.setter
    def CycleEndTime(self, CycleEndTime):
        self._CycleEndTime = CycleEndTime

    @property
    def BillingItems(self):
        r"""Summary list of tokens grouped by billing item
        :rtype: list of TokenSummaryBillingItem
        """
        return self._BillingItems

    @BillingItems.setter
    def BillingItems(self, BillingItems):
        self._BillingItems = BillingItems


    def _deserialize(self, params):
        self._CycleSeq = params.get("CycleSeq")
        self._CycleStartTime = params.get("CycleStartTime")
        self._CycleEndTime = params.get("CycleEndTime")
        if params.get("BillingItems") is not None:
            self._BillingItems = []
            for item in params.get("BillingItems"):
                obj = TokenSummaryBillingItem()
                obj._deserialize(item)
                self._BillingItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenSummaryBillingItem(AbstractModel):
    r"""Billing item for Token aggregation

    """

    def __init__(self):
        r"""
        :param _BillingItem: Billing item. Values: input (input Token), output (output Token), cache (cache Token), call_count (call count).
        :type BillingItem: str
        :param _TotalQty: Aggregated raw usage of this billing item during a period. Unit: tokens.
        :type TotalQty: int
        """
        self._BillingItem = None
        self._TotalQty = None

    @property
    def BillingItem(self):
        r"""Billing item. Values: input (input Token), output (output Token), cache (cache Token), call_count (call count).
        :rtype: str
        """
        return self._BillingItem

    @BillingItem.setter
    def BillingItem(self, BillingItem):
        self._BillingItem = BillingItem

    @property
    def TotalQty(self):
        r"""Aggregated raw usage of this billing item during a period. Unit: tokens.
        :rtype: int
        """
        return self._TotalQty

    @TotalQty.setter
    def TotalQty(self, TotalQty):
        self._TotalQty = TotalQty


    def _deserialize(self, params):
        self._BillingItem = params.get("BillingItem")
        self._TotalQty = params.get("TotalQty")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeTokenPlanTeamOrderRequest(AbstractModel):
    r"""UpgradeTokenPlanTeamOrder request structure.

    """

    def __init__(self):
        r"""
        :param _TeamId: Package ID. You can obtain it through the DescribeTokenPlanList API.
        :type TeamId: str
        :param _NewCreditOrToken: Limit of the new specification after upgrade. For the enterprise package type, it refers to the point limit. For the enterprise-auto package type, it refers to the Token count. Must be greater than the current limit.
        :type NewCreditOrToken: int
        """
        self._TeamId = None
        self._NewCreditOrToken = None

    @property
    def TeamId(self):
        r"""Package ID. You can obtain it through the DescribeTokenPlanList API.
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def NewCreditOrToken(self):
        r"""Limit of the new specification after upgrade. For the enterprise package type, it refers to the point limit. For the enterprise-auto package type, it refers to the Token count. Must be greater than the current limit.
        :rtype: int
        """
        return self._NewCreditOrToken

    @NewCreditOrToken.setter
    def NewCreditOrToken(self, NewCreditOrToken):
        self._NewCreditOrToken = NewCreditOrToken


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._NewCreditOrToken = params.get("NewCreditOrToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeTokenPlanTeamOrderResponse(AbstractModel):
    r"""UpgradeTokenPlanTeamOrder response structure.

    """

    def __init__(self):
        r"""
        :param _BigOrderId: Tencent Cloud order ID. Used to associate all sub-orders under an upgrade operation.
        :type BigOrderId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BigOrderId = None
        self._RequestId = None

    @property
    def BigOrderId(self):
        r"""Tencent Cloud order ID. Used to associate all sub-orders under an upgrade operation.
        :rtype: str
        """
        return self._BigOrderId

    @BigOrderId.setter
    def BigOrderId(self, BigOrderId):
        self._BigOrderId = BigOrderId

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
        self._BigOrderId = params.get("BigOrderId")
        self._RequestId = params.get("RequestId")


class UsageRankItem(AbstractModel):
    r"""Usage item of an individual object in the ranking list, including the object identifier, statistical values within a time period (Stats), and a list of time series points within a time period (Series, returned only when ShowAll=false).

    """

    def __init__(self):
        r"""
        :param _Rank: Global ranking (starting from 1). In pagination scenarios, this is still the position in the full sorting order, not the serial number within the page.
        :type Rank: int
        :param _Key: Object identifier. The apikey dimension is the APIKey ID; the endpoint dimension is the access point; the model dimension is the model name.
        :type Key: str
        :param _Name: Display name of the object. In the apikey dimension, return the APIKey name (deleted APIKeys retain their original names);
Key whose endpoint and model dimensions are equal.
        :type Name: str
        :param _Stats: Statistical value within a time period
        :type Stats: :class:`tencentcloud.tokenhub.v20260322.models.UsageStats`
        :param _Series: List of time series points within a time period
        :type Series: :class:`tencentcloud.tokenhub.v20260322.models.UsageSeries`
        """
        self._Rank = None
        self._Key = None
        self._Name = None
        self._Stats = None
        self._Series = None

    @property
    def Rank(self):
        r"""Global ranking (starting from 1). In pagination scenarios, this is still the position in the full sorting order, not the serial number within the page.
        :rtype: int
        """
        return self._Rank

    @Rank.setter
    def Rank(self, Rank):
        self._Rank = Rank

    @property
    def Key(self):
        r"""Object identifier. The apikey dimension is the APIKey ID; the endpoint dimension is the access point; the model dimension is the model name.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Name(self):
        r"""Display name of the object. In the apikey dimension, return the APIKey name (deleted APIKeys retain their original names);
Key whose endpoint and model dimensions are equal.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Stats(self):
        r"""Statistical value within a time period
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.UsageStats`
        """
        return self._Stats

    @Stats.setter
    def Stats(self, Stats):
        self._Stats = Stats

    @property
    def Series(self):
        r"""List of time series points within a time period
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.UsageSeries`
        """
        return self._Series

    @Series.setter
    def Series(self, Series):
        self._Series = Series


    def _deserialize(self, params):
        self._Rank = params.get("Rank")
        self._Key = params.get("Key")
        self._Name = params.get("Name")
        if params.get("Stats") is not None:
            self._Stats = UsageStats()
            self._Stats._deserialize(params.get("Stats"))
        if params.get("Series") is not None:
            self._Series = UsageSeries()
            self._Series._deserialize(params.get("Series"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageSeries(AbstractModel):
    r"""List of time series points within the usage time period (indexed by metric key). It is a JSON array in string form. The array length matches the response Timestamps, and null is used where there is no data point. The specific keys included are determined by the response MetricKeys.

    """

    def __init__(self):
        r"""
        :param _TotalToken: <p>Amount of total tokens used within a time period in JSON string form, for example, <code>&quot;[12,null,15]&quot;</code>.</p>
        :type TotalToken: str
        :param _InputTotalToken: <p>Amount of input tokens used within a time period in JSON string form, for example, <code>&quot;[7,null,9]&quot;</code>.</p>
        :type InputTotalToken: str
        :param _OutputTotalToken: <p>Amount of output tokens used within a time period in JSON string form, for example, <code>&quot;[5,null,6]&quot;</code>.</p>
        :type OutputTotalToken: str
        :param _CacheTotalToken: <p>Read cache token count usage of the tokens family in JSON string form within a time period, for example, <code>&quot;[5,null,6]&quot;</code>.</p>
        :type CacheTotalToken: str
        :param _SearchRequestCount: <p>Usage of search requests in JSON string form within a time period, for example, <code>&quot;[5,null,6]&quot;</code>.</p>
        :type SearchRequestCount: str
        :param _SearchCount: <p>Usage of search engine call count in JSON string form within a time period, for example, <code>&quot;[5,null,6]&quot;</code>.</p>
        :type SearchCount: str
        """
        self._TotalToken = None
        self._InputTotalToken = None
        self._OutputTotalToken = None
        self._CacheTotalToken = None
        self._SearchRequestCount = None
        self._SearchCount = None

    @property
    def TotalToken(self):
        r"""<p>Amount of total tokens used within a time period in JSON string form, for example, <code>&quot;[12,null,15]&quot;</code>.</p>
        :rtype: str
        """
        return self._TotalToken

    @TotalToken.setter
    def TotalToken(self, TotalToken):
        self._TotalToken = TotalToken

    @property
    def InputTotalToken(self):
        r"""<p>Amount of input tokens used within a time period in JSON string form, for example, <code>&quot;[7,null,9]&quot;</code>.</p>
        :rtype: str
        """
        return self._InputTotalToken

    @InputTotalToken.setter
    def InputTotalToken(self, InputTotalToken):
        self._InputTotalToken = InputTotalToken

    @property
    def OutputTotalToken(self):
        r"""<p>Amount of output tokens used within a time period in JSON string form, for example, <code>&quot;[5,null,6]&quot;</code>.</p>
        :rtype: str
        """
        return self._OutputTotalToken

    @OutputTotalToken.setter
    def OutputTotalToken(self, OutputTotalToken):
        self._OutputTotalToken = OutputTotalToken

    @property
    def CacheTotalToken(self):
        r"""<p>Read cache token count usage of the tokens family in JSON string form within a time period, for example, <code>&quot;[5,null,6]&quot;</code>.</p>
        :rtype: str
        """
        return self._CacheTotalToken

    @CacheTotalToken.setter
    def CacheTotalToken(self, CacheTotalToken):
        self._CacheTotalToken = CacheTotalToken

    @property
    def SearchRequestCount(self):
        r"""<p>Usage of search requests in JSON string form within a time period, for example, <code>&quot;[5,null,6]&quot;</code>.</p>
        :rtype: str
        """
        return self._SearchRequestCount

    @SearchRequestCount.setter
    def SearchRequestCount(self, SearchRequestCount):
        self._SearchRequestCount = SearchRequestCount

    @property
    def SearchCount(self):
        r"""<p>Usage of search engine call count in JSON string form within a time period, for example, <code>&quot;[5,null,6]&quot;</code>.</p>
        :rtype: str
        """
        return self._SearchCount

    @SearchCount.setter
    def SearchCount(self, SearchCount):
        self._SearchCount = SearchCount


    def _deserialize(self, params):
        self._TotalToken = params.get("TotalToken")
        self._InputTotalToken = params.get("InputTotalToken")
        self._OutputTotalToken = params.get("OutputTotalToken")
        self._CacheTotalToken = params.get("CacheTotalToken")
        self._SearchRequestCount = params.get("SearchRequestCount")
        self._SearchCount = params.get("SearchCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageStats(AbstractModel):
    r"""Statistical aggregate values within a time period (indexed by metric key). Declares that both the tokens and search field families are in this schema, with values obtained based on the actual MetricKeys returned. See the top-level `MetricKeys` field in the response.

    """

    def __init__(self):
        r"""
        :param _TotalToken: <p>Total tokens accumulated within a time period.</p>
        :type TotalToken: int
        :param _InputTotalToken: <p>[tokens family] Total input tokens within a time period.</p>
        :type InputTotalToken: int
        :param _OutputTotalToken: <p>[tokens family] Total output tokens within a time period.</p>
        :type OutputTotalToken: int
        :param _CacheTotalToken: <p>[token family] Cumulative number of tokens read from the cache within a time period (cache hit part)</p>
        :type CacheTotalToken: int
        :param _SearchRequestCount: <p>Total online search requests in the [search group]</p>
        :type SearchRequestCount: int
        :param _SearchCount: <p>[search family] Total search engine calls</p>
        :type SearchCount: int
        """
        self._TotalToken = None
        self._InputTotalToken = None
        self._OutputTotalToken = None
        self._CacheTotalToken = None
        self._SearchRequestCount = None
        self._SearchCount = None

    @property
    def TotalToken(self):
        r"""<p>Total tokens accumulated within a time period.</p>
        :rtype: int
        """
        return self._TotalToken

    @TotalToken.setter
    def TotalToken(self, TotalToken):
        self._TotalToken = TotalToken

    @property
    def InputTotalToken(self):
        r"""<p>[tokens family] Total input tokens within a time period.</p>
        :rtype: int
        """
        return self._InputTotalToken

    @InputTotalToken.setter
    def InputTotalToken(self, InputTotalToken):
        self._InputTotalToken = InputTotalToken

    @property
    def OutputTotalToken(self):
        r"""<p>[tokens family] Total output tokens within a time period.</p>
        :rtype: int
        """
        return self._OutputTotalToken

    @OutputTotalToken.setter
    def OutputTotalToken(self, OutputTotalToken):
        self._OutputTotalToken = OutputTotalToken

    @property
    def CacheTotalToken(self):
        r"""<p>[token family] Cumulative number of tokens read from the cache within a time period (cache hit part)</p>
        :rtype: int
        """
        return self._CacheTotalToken

    @CacheTotalToken.setter
    def CacheTotalToken(self, CacheTotalToken):
        self._CacheTotalToken = CacheTotalToken

    @property
    def SearchRequestCount(self):
        r"""<p>Total online search requests in the [search group]</p>
        :rtype: int
        """
        return self._SearchRequestCount

    @SearchRequestCount.setter
    def SearchRequestCount(self, SearchRequestCount):
        self._SearchRequestCount = SearchRequestCount

    @property
    def SearchCount(self):
        r"""<p>[search family] Total search engine calls</p>
        :rtype: int
        """
        return self._SearchCount

    @SearchCount.setter
    def SearchCount(self, SearchCount):
        self._SearchCount = SearchCount


    def _deserialize(self, params):
        self._TotalToken = params.get("TotalToken")
        self._InputTotalToken = params.get("InputTotalToken")
        self._OutputTotalToken = params.get("OutputTotalToken")
        self._CacheTotalToken = params.get("CacheTotalToken")
        self._SearchRequestCount = params.get("SearchRequestCount")
        self._SearchCount = params.get("SearchCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        