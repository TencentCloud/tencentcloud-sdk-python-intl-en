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


class AttributeKeyDetail(AbstractModel):
    """`AttributeKey` value details

    """

    def __init__(self):
        r"""
        :param _LabelType: Input box type
        :type LabelType: str
        :param _Starter: Initial display
        :type Starter: str
        :param _Order: Display sort order
        :type Order: int
        :param _Value: `AttributeKey` value
        :type Value: str
        :param _Label: Tag
        :type Label: str
        """
        self._LabelType = None
        self._Starter = None
        self._Order = None
        self._Value = None
        self._Label = None

    @property
    def LabelType(self):
        """Input box type
        :rtype: str
        """
        return self._LabelType

    @LabelType.setter
    def LabelType(self, LabelType):
        self._LabelType = LabelType

    @property
    def Starter(self):
        """Initial display
        :rtype: str
        """
        return self._Starter

    @Starter.setter
    def Starter(self, Starter):
        self._Starter = Starter

    @property
    def Order(self):
        """Display sort order
        :rtype: int
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Value(self):
        """`AttributeKey` value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Label(self):
        """Tag
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label


    def _deserialize(self, params):
        self._LabelType = params.get("LabelType")
        self._Starter = params.get("Starter")
        self._Order = params.get("Order")
        self._Value = params.get("Value")
        self._Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditSummary(AbstractModel):
    """Tracking set overview

    """

    def __init__(self):
        r"""
        :param _AuditStatus: Tracking set status. 1: enabled, 0: disabled
        :type AuditStatus: int
        :param _CosBucketName: COS bucket name
        :type CosBucketName: str
        :param _AuditName: Tracking set name
        :type AuditName: str
        :param _LogFilePrefix: Log prefix
        :type LogFilePrefix: str
        """
        self._AuditStatus = None
        self._CosBucketName = None
        self._AuditName = None
        self._LogFilePrefix = None

    @property
    def AuditStatus(self):
        """Tracking set status. 1: enabled, 0: disabled
        :rtype: int
        """
        return self._AuditStatus

    @AuditStatus.setter
    def AuditStatus(self, AuditStatus):
        self._AuditStatus = AuditStatus

    @property
    def CosBucketName(self):
        """COS bucket name
        :rtype: str
        """
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def AuditName(self):
        """Tracking set name
        :rtype: str
        """
        return self._AuditName

    @AuditName.setter
    def AuditName(self, AuditName):
        self._AuditName = AuditName

    @property
    def LogFilePrefix(self):
        """Log prefix
        :rtype: str
        """
        return self._LogFilePrefix

    @LogFilePrefix.setter
    def LogFilePrefix(self, LogFilePrefix):
        self._LogFilePrefix = LogFilePrefix


    def _deserialize(self, params):
        self._AuditStatus = params.get("AuditStatus")
        self._CosBucketName = params.get("CosBucketName")
        self._AuditName = params.get("AuditName")
        self._LogFilePrefix = params.get("LogFilePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqRegionInfo(AbstractModel):
    """CMQ region information

    """

    def __init__(self):
        r"""
        :param _CmqRegionName: Region description
        :type CmqRegionName: str
        :param _CmqRegion: CMQ region
        :type CmqRegion: str
        """
        self._CmqRegionName = None
        self._CmqRegion = None

    @property
    def CmqRegionName(self):
        """Region description
        :rtype: str
        """
        return self._CmqRegionName

    @CmqRegionName.setter
    def CmqRegionName(self, CmqRegionName):
        self._CmqRegionName = CmqRegionName

    @property
    def CmqRegion(self):
        """CMQ region
        :rtype: str
        """
        return self._CmqRegion

    @CmqRegion.setter
    def CmqRegion(self, CmqRegion):
        self._CmqRegion = CmqRegion


    def _deserialize(self, params):
        self._CmqRegionName = params.get("CmqRegionName")
        self._CmqRegion = params.get("CmqRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosRegionInfo(AbstractModel):
    """COS region information

    """

    def __init__(self):
        r"""
        :param _CosRegion: COS region
        :type CosRegion: str
        :param _CosRegionName: Region description
        :type CosRegionName: str
        """
        self._CosRegion = None
        self._CosRegionName = None

    @property
    def CosRegion(self):
        """COS region
        :rtype: str
        """
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def CosRegionName(self):
        """Region description
        :rtype: str
        """
        return self._CosRegionName

    @CosRegionName.setter
    def CosRegionName(self, CosRegionName):
        self._CosRegionName = CosRegionName


    def _deserialize(self, params):
        self._CosRegion = params.get("CosRegion")
        self._CosRegionName = params.get("CosRegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditRequest(AbstractModel):
    """CreateAudit request structure.

    """

    def __init__(self):
        r"""
        :param _IsEnableCmqNotify: Whether to enable CMQ message notification. 1: Yes; 0: No. Only CMQ queue service is currently supported. If CMQ message notification is enabled, CloudAudit will deliver your log contents to the designated queue in the specified region in real time.
        :type IsEnableCmqNotify: int
        :param _ReadWriteAttribute: Manages the read/write attribute of event. Valid values: 1 (read-only), 2 (write-only), 3 (read/write).
        :type ReadWriteAttribute: int
        :param _AuditName: Tracking set name, which can contain 3–128 ASCII letters (a–z; A–Z), digits (0–9), and underscores (_).
        :type AuditName: str
        :param _CosRegion: COS region. Supported regions can be queried through the `ListCosEnableRegion` API.
        :type CosRegion: str
        :param _IsCreateNewBucket: Whether to create a COS bucket. 1: Yes; 0: No.
        :type IsCreateNewBucket: int
        :param _CosBucketName: User-defined COS bucket name, which can only contain 1–40 lowercase letters (a–z), digits (0–9), and dashes (-) and cannot begin or end with "-". If a bucket is not newly created, CloudAudit will not verify whether it actually exists. Enter the name with caution to avoid log delivery failure and consequent data loss.
        :type CosBucketName: str
        :param _KeyId: Globally unique ID of the CMK. This value is required if it is not a newly created KMS element. It can be obtained through `ListKeyAliasByRegion`. CloudAudit will not verify the validity of the `KeyId`. Enter it carefully to avoid data loss.
        :type KeyId: str
        :param _CmqQueueName: Queue name, which must begin with a letter and can contain up to 64 letters, digits, and dashes (-). This field is required if the value of `IsEnableCmqNotify` is 1. If a queue is not newly created, CloudAudit will not verify whether it actually exists. Enter the name with caution to avoid log delivery failure and consequent data loss.
        :type CmqQueueName: str
        :param _KmsRegion: KMS region. Currently supported regions can be obtained through `ListKmsEnableRegion`. This must be the same as the COS region.
        :type KmsRegion: str
        :param _IsEnableKmsEncry: Whether to enable KMS encryption. 1: Yes, 0: No. If KMS encryption is enabled, the data will be encrypted when delivered to COS.
        :type IsEnableKmsEncry: int
        :param _CmqRegion: Region where the queue is located. Supported CMQ regions can be queried through the `ListCmqEnableRegion` API. This field is required if the value of `IsEnableCmqNotify` is 1.
        :type CmqRegion: str
        :param _LogFilePrefix: Log file prefix, which can only contain 3–40 ASCII letters (a–z; A–Z) and digits (0–9). It can be left empty and is the account ID by default.
        :type LogFilePrefix: str
        :param _IsCreateNewQueue: Whether to create a queue. 1: Yes; 0: No. This field is required if the value of `IsEnableCmqNotify` is 1.
        :type IsCreateNewQueue: int
        """
        self._IsEnableCmqNotify = None
        self._ReadWriteAttribute = None
        self._AuditName = None
        self._CosRegion = None
        self._IsCreateNewBucket = None
        self._CosBucketName = None
        self._KeyId = None
        self._CmqQueueName = None
        self._KmsRegion = None
        self._IsEnableKmsEncry = None
        self._CmqRegion = None
        self._LogFilePrefix = None
        self._IsCreateNewQueue = None

    @property
    def IsEnableCmqNotify(self):
        """Whether to enable CMQ message notification. 1: Yes; 0: No. Only CMQ queue service is currently supported. If CMQ message notification is enabled, CloudAudit will deliver your log contents to the designated queue in the specified region in real time.
        :rtype: int
        """
        return self._IsEnableCmqNotify

    @IsEnableCmqNotify.setter
    def IsEnableCmqNotify(self, IsEnableCmqNotify):
        self._IsEnableCmqNotify = IsEnableCmqNotify

    @property
    def ReadWriteAttribute(self):
        """Manages the read/write attribute of event. Valid values: 1 (read-only), 2 (write-only), 3 (read/write).
        :rtype: int
        """
        return self._ReadWriteAttribute

    @ReadWriteAttribute.setter
    def ReadWriteAttribute(self, ReadWriteAttribute):
        self._ReadWriteAttribute = ReadWriteAttribute

    @property
    def AuditName(self):
        """Tracking set name, which can contain 3–128 ASCII letters (a–z; A–Z), digits (0–9), and underscores (_).
        :rtype: str
        """
        return self._AuditName

    @AuditName.setter
    def AuditName(self, AuditName):
        self._AuditName = AuditName

    @property
    def CosRegion(self):
        """COS region. Supported regions can be queried through the `ListCosEnableRegion` API.
        :rtype: str
        """
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def IsCreateNewBucket(self):
        """Whether to create a COS bucket. 1: Yes; 0: No.
        :rtype: int
        """
        return self._IsCreateNewBucket

    @IsCreateNewBucket.setter
    def IsCreateNewBucket(self, IsCreateNewBucket):
        self._IsCreateNewBucket = IsCreateNewBucket

    @property
    def CosBucketName(self):
        """User-defined COS bucket name, which can only contain 1–40 lowercase letters (a–z), digits (0–9), and dashes (-) and cannot begin or end with "-". If a bucket is not newly created, CloudAudit will not verify whether it actually exists. Enter the name with caution to avoid log delivery failure and consequent data loss.
        :rtype: str
        """
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def KeyId(self):
        """Globally unique ID of the CMK. This value is required if it is not a newly created KMS element. It can be obtained through `ListKeyAliasByRegion`. CloudAudit will not verify the validity of the `KeyId`. Enter it carefully to avoid data loss.
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def CmqQueueName(self):
        """Queue name, which must begin with a letter and can contain up to 64 letters, digits, and dashes (-). This field is required if the value of `IsEnableCmqNotify` is 1. If a queue is not newly created, CloudAudit will not verify whether it actually exists. Enter the name with caution to avoid log delivery failure and consequent data loss.
        :rtype: str
        """
        return self._CmqQueueName

    @CmqQueueName.setter
    def CmqQueueName(self, CmqQueueName):
        self._CmqQueueName = CmqQueueName

    @property
    def KmsRegion(self):
        """KMS region. Currently supported regions can be obtained through `ListKmsEnableRegion`. This must be the same as the COS region.
        :rtype: str
        """
        return self._KmsRegion

    @KmsRegion.setter
    def KmsRegion(self, KmsRegion):
        self._KmsRegion = KmsRegion

    @property
    def IsEnableKmsEncry(self):
        """Whether to enable KMS encryption. 1: Yes, 0: No. If KMS encryption is enabled, the data will be encrypted when delivered to COS.
        :rtype: int
        """
        return self._IsEnableKmsEncry

    @IsEnableKmsEncry.setter
    def IsEnableKmsEncry(self, IsEnableKmsEncry):
        self._IsEnableKmsEncry = IsEnableKmsEncry

    @property
    def CmqRegion(self):
        """Region where the queue is located. Supported CMQ regions can be queried through the `ListCmqEnableRegion` API. This field is required if the value of `IsEnableCmqNotify` is 1.
        :rtype: str
        """
        return self._CmqRegion

    @CmqRegion.setter
    def CmqRegion(self, CmqRegion):
        self._CmqRegion = CmqRegion

    @property
    def LogFilePrefix(self):
        """Log file prefix, which can only contain 3–40 ASCII letters (a–z; A–Z) and digits (0–9). It can be left empty and is the account ID by default.
        :rtype: str
        """
        return self._LogFilePrefix

    @LogFilePrefix.setter
    def LogFilePrefix(self, LogFilePrefix):
        self._LogFilePrefix = LogFilePrefix

    @property
    def IsCreateNewQueue(self):
        """Whether to create a queue. 1: Yes; 0: No. This field is required if the value of `IsEnableCmqNotify` is 1.
        :rtype: int
        """
        return self._IsCreateNewQueue

    @IsCreateNewQueue.setter
    def IsCreateNewQueue(self, IsCreateNewQueue):
        self._IsCreateNewQueue = IsCreateNewQueue


    def _deserialize(self, params):
        self._IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self._ReadWriteAttribute = params.get("ReadWriteAttribute")
        self._AuditName = params.get("AuditName")
        self._CosRegion = params.get("CosRegion")
        self._IsCreateNewBucket = params.get("IsCreateNewBucket")
        self._CosBucketName = params.get("CosBucketName")
        self._KeyId = params.get("KeyId")
        self._CmqQueueName = params.get("CmqQueueName")
        self._KmsRegion = params.get("KmsRegion")
        self._IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self._CmqRegion = params.get("CmqRegion")
        self._LogFilePrefix = params.get("LogFilePrefix")
        self._IsCreateNewQueue = params.get("IsCreateNewQueue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditResponse(AbstractModel):
    """CreateAudit response structure.

    """

    def __init__(self):
        r"""
        :param _IsSuccess: Whether creation succeeded.
        :type IsSuccess: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsSuccess = None
        self._RequestId = None

    @property
    def IsSuccess(self):
        """Whether creation succeeded.
        :rtype: int
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsSuccess = params.get("IsSuccess")
        self._RequestId = params.get("RequestId")


class CreateAuditTrackRequest(AbstractModel):
    """CreateAuditTrack request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Tracking set name, which can only contain 3-48 letters, digits, hyphens, and underscores.
        :type Name: str
        :param _ActionType: Tracking set event type (`Read`: Read; `Write`: Write; `*`: All)
        :type ActionType: str
        :param _ResourceType: The product to which the tracking set event belongs. The value can be a single product such as `cos`, or `*` that indicates all products.
        :type ResourceType: str
        :param _Status: Tracking set status (0: Not enabled; 1: Enabled)
        :type Status: int
        :param _EventNames: The list of API names of tracking set events. When `ResourceType` is `*`, the value of `EventNames` must be `*`. When `ResourceType` is a specified product, the value of `EventNames` can be `*`. When `ResourceType` is `cos` or `cls`, up to 10 APIs are supported.
        :type EventNames: list of str
        :param _Storage: Storage type of shipped data. Valid values: `cos`, `cls`.
        :type Storage: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        :param _TrackForAllMembers: Whether to enable the feature of shipping organization members’ operation logs to the organization admin account or the trusted service admin account (0: Not enabled; 1: Enabled. This feature can only be enabled by the organization admin account or the trusted service admin account)
        :type TrackForAllMembers: int
        """
        self._Name = None
        self._ActionType = None
        self._ResourceType = None
        self._Status = None
        self._EventNames = None
        self._Storage = None
        self._TrackForAllMembers = None

    @property
    def Name(self):
        """Tracking set name, which can only contain 3-48 letters, digits, hyphens, and underscores.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ActionType(self):
        """Tracking set event type (`Read`: Read; `Write`: Write; `*`: All)
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ResourceType(self):
        """The product to which the tracking set event belongs. The value can be a single product such as `cos`, or `*` that indicates all products.
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Status(self):
        """Tracking set status (0: Not enabled; 1: Enabled)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EventNames(self):
        """The list of API names of tracking set events. When `ResourceType` is `*`, the value of `EventNames` must be `*`. When `ResourceType` is a specified product, the value of `EventNames` can be `*`. When `ResourceType` is `cos` or `cls`, up to 10 APIs are supported.
        :rtype: list of str
        """
        return self._EventNames

    @EventNames.setter
    def EventNames(self, EventNames):
        self._EventNames = EventNames

    @property
    def Storage(self):
        """Storage type of shipped data. Valid values: `cos`, `cls`.
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def TrackForAllMembers(self):
        """Whether to enable the feature of shipping organization members’ operation logs to the organization admin account or the trusted service admin account (0: Not enabled; 1: Enabled. This feature can only be enabled by the organization admin account or the trusted service admin account)
        :rtype: int
        """
        return self._TrackForAllMembers

    @TrackForAllMembers.setter
    def TrackForAllMembers(self, TrackForAllMembers):
        self._TrackForAllMembers = TrackForAllMembers


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ActionType = params.get("ActionType")
        self._ResourceType = params.get("ResourceType")
        self._Status = params.get("Status")
        self._EventNames = params.get("EventNames")
        if params.get("Storage") is not None:
            self._Storage = Storage()
            self._Storage._deserialize(params.get("Storage"))
        self._TrackForAllMembers = params.get("TrackForAllMembers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditTrackResponse(AbstractModel):
    """CreateAuditTrack response structure.

    """

    def __init__(self):
        r"""
        :param _TrackId: Tracking set ID
        :type TrackId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TrackId = None
        self._RequestId = None

    @property
    def TrackId(self):
        """Tracking set ID
        :rtype: int
        """
        return self._TrackId

    @TrackId.setter
    def TrackId(self, TrackId):
        self._TrackId = TrackId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TrackId = params.get("TrackId")
        self._RequestId = params.get("RequestId")


class DeleteAuditRequest(AbstractModel):
    """DeleteAudit request structure.

    """

    def __init__(self):
        r"""
        :param _AuditName: Tracking set name
        :type AuditName: str
        """
        self._AuditName = None

    @property
    def AuditName(self):
        """Tracking set name
        :rtype: str
        """
        return self._AuditName

    @AuditName.setter
    def AuditName(self, AuditName):
        self._AuditName = AuditName


    def _deserialize(self, params):
        self._AuditName = params.get("AuditName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditResponse(AbstractModel):
    """DeleteAudit response structure.

    """

    def __init__(self):
        r"""
        :param _IsSuccess: Whether deletion succeeded
        :type IsSuccess: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsSuccess = None
        self._RequestId = None

    @property
    def IsSuccess(self):
        """Whether deletion succeeded
        :rtype: int
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsSuccess = params.get("IsSuccess")
        self._RequestId = params.get("RequestId")


class DeleteAuditTrackRequest(AbstractModel):
    """DeleteAuditTrack request structure.

    """

    def __init__(self):
        r"""
        :param _TrackId: Tracking set ID
        :type TrackId: int
        """
        self._TrackId = None

    @property
    def TrackId(self):
        """Tracking set ID
        :rtype: int
        """
        return self._TrackId

    @TrackId.setter
    def TrackId(self, TrackId):
        self._TrackId = TrackId


    def _deserialize(self, params):
        self._TrackId = params.get("TrackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditTrackResponse(AbstractModel):
    """DeleteAuditTrack response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAuditRequest(AbstractModel):
    """DescribeAudit request structure.

    """

    def __init__(self):
        r"""
        :param _AuditName: Tracking set name
        :type AuditName: str
        """
        self._AuditName = None

    @property
    def AuditName(self):
        """Tracking set name
        :rtype: str
        """
        return self._AuditName

    @AuditName.setter
    def AuditName(self, AuditName):
        self._AuditName = AuditName


    def _deserialize(self, params):
        self._AuditName = params.get("AuditName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditResponse(AbstractModel):
    """DescribeAudit response structure.

    """

    def __init__(self):
        r"""
        :param _IsEnableCmqNotify: Whether to enable CMQ message notification. 1: Yes; 0: No.
        :type IsEnableCmqNotify: int
        :param _ReadWriteAttribute: Manages the read/write attribute of event. Valid values: 1 (read-only), 2 (write-only), 3 (read/write)
        :type ReadWriteAttribute: int
        :param _KeyId: Globally unique CMK ID.
        :type KeyId: str
        :param _AuditStatus: Tracking set status. 1: enabled, 0: disabled.
        :type AuditStatus: int
        :param _AuditName: Tracking set name.
        :type AuditName: str
        :param _CosRegion: COS bucket region.
        :type CosRegion: str
        :param _CmqQueueName: Queue name.
        :type CmqQueueName: str
        :param _KmsAlias: CMK alias.
        :type KmsAlias: str
        :param _KmsRegion: KMS region.
        :type KmsRegion: str
        :param _IsEnableKmsEncry: Whether to enable KMS encryption. 1: Yes, 0: No. If KMS encryption is enabled, the data will be encrypted when it is delivered to COS.
        :type IsEnableKmsEncry: int
        :param _CosBucketName: COS bucket name.
        :type CosBucketName: str
        :param _CmqRegion: Queue region.
        :type CmqRegion: str
        :param _LogFilePrefix: Log prefix.
        :type LogFilePrefix: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsEnableCmqNotify = None
        self._ReadWriteAttribute = None
        self._KeyId = None
        self._AuditStatus = None
        self._AuditName = None
        self._CosRegion = None
        self._CmqQueueName = None
        self._KmsAlias = None
        self._KmsRegion = None
        self._IsEnableKmsEncry = None
        self._CosBucketName = None
        self._CmqRegion = None
        self._LogFilePrefix = None
        self._RequestId = None

    @property
    def IsEnableCmqNotify(self):
        """Whether to enable CMQ message notification. 1: Yes; 0: No.
        :rtype: int
        """
        return self._IsEnableCmqNotify

    @IsEnableCmqNotify.setter
    def IsEnableCmqNotify(self, IsEnableCmqNotify):
        self._IsEnableCmqNotify = IsEnableCmqNotify

    @property
    def ReadWriteAttribute(self):
        """Manages the read/write attribute of event. Valid values: 1 (read-only), 2 (write-only), 3 (read/write)
        :rtype: int
        """
        return self._ReadWriteAttribute

    @ReadWriteAttribute.setter
    def ReadWriteAttribute(self, ReadWriteAttribute):
        self._ReadWriteAttribute = ReadWriteAttribute

    @property
    def KeyId(self):
        """Globally unique CMK ID.
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def AuditStatus(self):
        """Tracking set status. 1: enabled, 0: disabled.
        :rtype: int
        """
        return self._AuditStatus

    @AuditStatus.setter
    def AuditStatus(self, AuditStatus):
        self._AuditStatus = AuditStatus

    @property
    def AuditName(self):
        """Tracking set name.
        :rtype: str
        """
        return self._AuditName

    @AuditName.setter
    def AuditName(self, AuditName):
        self._AuditName = AuditName

    @property
    def CosRegion(self):
        """COS bucket region.
        :rtype: str
        """
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def CmqQueueName(self):
        """Queue name.
        :rtype: str
        """
        return self._CmqQueueName

    @CmqQueueName.setter
    def CmqQueueName(self, CmqQueueName):
        self._CmqQueueName = CmqQueueName

    @property
    def KmsAlias(self):
        """CMK alias.
        :rtype: str
        """
        return self._KmsAlias

    @KmsAlias.setter
    def KmsAlias(self, KmsAlias):
        self._KmsAlias = KmsAlias

    @property
    def KmsRegion(self):
        """KMS region.
        :rtype: str
        """
        return self._KmsRegion

    @KmsRegion.setter
    def KmsRegion(self, KmsRegion):
        self._KmsRegion = KmsRegion

    @property
    def IsEnableKmsEncry(self):
        """Whether to enable KMS encryption. 1: Yes, 0: No. If KMS encryption is enabled, the data will be encrypted when it is delivered to COS.
        :rtype: int
        """
        return self._IsEnableKmsEncry

    @IsEnableKmsEncry.setter
    def IsEnableKmsEncry(self, IsEnableKmsEncry):
        self._IsEnableKmsEncry = IsEnableKmsEncry

    @property
    def CosBucketName(self):
        """COS bucket name.
        :rtype: str
        """
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def CmqRegion(self):
        """Queue region.
        :rtype: str
        """
        return self._CmqRegion

    @CmqRegion.setter
    def CmqRegion(self, CmqRegion):
        self._CmqRegion = CmqRegion

    @property
    def LogFilePrefix(self):
        """Log prefix.
        :rtype: str
        """
        return self._LogFilePrefix

    @LogFilePrefix.setter
    def LogFilePrefix(self, LogFilePrefix):
        self._LogFilePrefix = LogFilePrefix

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self._ReadWriteAttribute = params.get("ReadWriteAttribute")
        self._KeyId = params.get("KeyId")
        self._AuditStatus = params.get("AuditStatus")
        self._AuditName = params.get("AuditName")
        self._CosRegion = params.get("CosRegion")
        self._CmqQueueName = params.get("CmqQueueName")
        self._KmsAlias = params.get("KmsAlias")
        self._KmsRegion = params.get("KmsRegion")
        self._IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self._CosBucketName = params.get("CosBucketName")
        self._CmqRegion = params.get("CmqRegion")
        self._LogFilePrefix = params.get("LogFilePrefix")
        self._RequestId = params.get("RequestId")


class DescribeAuditTrackRequest(AbstractModel):
    """DescribeAuditTrack request structure.

    """

    def __init__(self):
        r"""
        :param _TrackId: Tracking set ID
        :type TrackId: int
        """
        self._TrackId = None

    @property
    def TrackId(self):
        """Tracking set ID
        :rtype: int
        """
        return self._TrackId

    @TrackId.setter
    def TrackId(self, TrackId):
        self._TrackId = TrackId


    def _deserialize(self, params):
        self._TrackId = params.get("TrackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditTrackResponse(AbstractModel):
    """DescribeAuditTrack response structure.

    """

    def __init__(self):
        r"""
        :param _Name: Tracking set name
        :type Name: str
        :param _ActionType: Tracking set event type (`Read`: Read; `Write`: Write; `*`: All)
        :type ActionType: str
        :param _ResourceType: The product to which the tracking set event belongs, such as `cos`, or `*` that indicates all products
        :type ResourceType: str
        :param _Status: Tracking set status (0: Not enabled; 1: Enabled)
        :type Status: int
        :param _EventNames: The list of API names of tracking set events (`*`: All)
        :type EventNames: list of str
        :param _Storage: Storage type of shipped data. Valid values: `cos`, `cls`.
        :type Storage: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        :param _CreateTime: Creation time of the tracking set
        :type CreateTime: str
        :param _TrackForAllMembers: Whether to enable the feature of shipping organization members’ operation logs to the organization admin account or the trusted service admin account
Note: This field may return null, indicating that no valid values can be obtained.
        :type TrackForAllMembers: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Name = None
        self._ActionType = None
        self._ResourceType = None
        self._Status = None
        self._EventNames = None
        self._Storage = None
        self._CreateTime = None
        self._TrackForAllMembers = None
        self._RequestId = None

    @property
    def Name(self):
        """Tracking set name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ActionType(self):
        """Tracking set event type (`Read`: Read; `Write`: Write; `*`: All)
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ResourceType(self):
        """The product to which the tracking set event belongs, such as `cos`, or `*` that indicates all products
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Status(self):
        """Tracking set status (0: Not enabled; 1: Enabled)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EventNames(self):
        """The list of API names of tracking set events (`*`: All)
        :rtype: list of str
        """
        return self._EventNames

    @EventNames.setter
    def EventNames(self, EventNames):
        self._EventNames = EventNames

    @property
    def Storage(self):
        """Storage type of shipped data. Valid values: `cos`, `cls`.
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def CreateTime(self):
        """Creation time of the tracking set
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TrackForAllMembers(self):
        """Whether to enable the feature of shipping organization members’ operation logs to the organization admin account or the trusted service admin account
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TrackForAllMembers

    @TrackForAllMembers.setter
    def TrackForAllMembers(self, TrackForAllMembers):
        self._TrackForAllMembers = TrackForAllMembers

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ActionType = params.get("ActionType")
        self._ResourceType = params.get("ResourceType")
        self._Status = params.get("Status")
        self._EventNames = params.get("EventNames")
        if params.get("Storage") is not None:
            self._Storage = Storage()
            self._Storage._deserialize(params.get("Storage"))
        self._CreateTime = params.get("CreateTime")
        self._TrackForAllMembers = params.get("TrackForAllMembers")
        self._RequestId = params.get("RequestId")


class DescribeAuditTracksRequest(AbstractModel):
    """DescribeAuditTracks request structure.

    """

    def __init__(self):
        r"""
        :param _PageNumber: Page number
        :type PageNumber: int
        :param _PageSize: The number of tracking sets per page
        :type PageSize: int
        """
        self._PageNumber = None
        self._PageSize = None

    @property
    def PageNumber(self):
        """Page number
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """The number of tracking sets per page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditTracksResponse(AbstractModel):
    """DescribeAuditTracks response structure.

    """

    def __init__(self):
        r"""
        :param _Tracks: Tracking set list
        :type Tracks: list of Tracks
        :param _TotalCount: Total number of tracking sets
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Tracks = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Tracks(self):
        """Tracking set list
        :rtype: list of Tracks
        """
        return self._Tracks

    @Tracks.setter
    def Tracks(self, Tracks):
        self._Tracks = Tracks

    @property
    def TotalCount(self):
        """Total number of tracking sets
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tracks") is not None:
            self._Tracks = []
            for item in params.get("Tracks"):
                obj = Tracks()
                obj._deserialize(item)
                self._Tracks.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeEventsRequest(AbstractModel):
    """DescribeEvents request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start timestamp in seconds (cannot be 90 days after the current time).
        :type StartTime: int
        :param _EndTime: End timestamp in seconds (the time range for query is less than 30 days).
        :type EndTime: int
        :param _NextToken: Credential for viewing more logs.
        :type NextToken: int
        :param _MaxResults: Max number of returned logs (up to 50).
        :type MaxResults: int
        :param _LookupAttributes: Search condition. Valid values: `RequestId`, `EventName`, `ActionType` (write/read), `PrincipalId` (sub-account), `ResourceType`, `ResourceName`, `AccessKeyId`, `SensitiveAction`, `ApiErrorCode`, `CamErrorCode`, and `Tags` (Format of AttributeValue: [{"key":"*","value":"*"}])
        :type LookupAttributes: list of LookupAttribute
        :param _IsReturnLocation: Whether to return the IP location. `1`: yes, `0`: no.
        :type IsReturnLocation: int
        """
        self._StartTime = None
        self._EndTime = None
        self._NextToken = None
        self._MaxResults = None
        self._LookupAttributes = None
        self._IsReturnLocation = None

    @property
    def StartTime(self):
        """Start timestamp in seconds (cannot be 90 days after the current time).
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End timestamp in seconds (the time range for query is less than 30 days).
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NextToken(self):
        """Credential for viewing more logs.
        :rtype: int
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def MaxResults(self):
        """Max number of returned logs (up to 50).
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def LookupAttributes(self):
        """Search condition. Valid values: `RequestId`, `EventName`, `ActionType` (write/read), `PrincipalId` (sub-account), `ResourceType`, `ResourceName`, `AccessKeyId`, `SensitiveAction`, `ApiErrorCode`, `CamErrorCode`, and `Tags` (Format of AttributeValue: [{"key":"*","value":"*"}])
        :rtype: list of LookupAttribute
        """
        return self._LookupAttributes

    @LookupAttributes.setter
    def LookupAttributes(self, LookupAttributes):
        self._LookupAttributes = LookupAttributes

    @property
    def IsReturnLocation(self):
        """Whether to return the IP location. `1`: yes, `0`: no.
        :rtype: int
        """
        return self._IsReturnLocation

    @IsReturnLocation.setter
    def IsReturnLocation(self, IsReturnLocation):
        self._IsReturnLocation = IsReturnLocation


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._NextToken = params.get("NextToken")
        self._MaxResults = params.get("MaxResults")
        if params.get("LookupAttributes") is not None:
            self._LookupAttributes = []
            for item in params.get("LookupAttributes"):
                obj = LookupAttribute()
                obj._deserialize(item)
                self._LookupAttributes.append(obj)
        self._IsReturnLocation = params.get("IsReturnLocation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEventsResponse(AbstractModel):
    """DescribeEvents response structure.

    """

    def __init__(self):
        r"""
        :param _ListOver: Whether the log list has come to an end. `true`: Yes. Pagination is not required.
        :type ListOver: bool
        :param _NextToken: Credential for viewing more logs.
        :type NextToken: int
        :param _Events: Logset.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Events: list of Event
        :param _TotalCount: This parameter has been deprecated. Please use `ListOver` and `NextToken` for pagination, and read data of the next page when the value of `ListOver` is `false`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ListOver = None
        self._NextToken = None
        self._Events = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ListOver(self):
        """Whether the log list has come to an end. `true`: Yes. Pagination is not required.
        :rtype: bool
        """
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def NextToken(self):
        """Credential for viewing more logs.
        :rtype: int
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def Events(self):
        """Logset.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: list of Event
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def TotalCount(self):
        """This parameter has been deprecated. Please use `ListOver` and `NextToken` for pagination, and read data of the next page when the value of `ListOver` is `false`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ListOver = params.get("ListOver")
        self._NextToken = params.get("NextToken")
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = Event()
                obj._deserialize(item)
                self._Events.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class Event(AbstractModel):
    """Log details

    """

    def __init__(self):
        r"""
        :param _EventId: Log ID
        :type EventId: str
        :param _Username: Username
        :type Username: str
        :param _EventTime: Event Time
        :type EventTime: str
        :param _CloudAuditEvent: Log details
        :type CloudAuditEvent: str
        :param _ResourceTypeCn: Description of resource type in Chinese (please use this field as required; if you are using other languages, ignore this field)
        :type ResourceTypeCn: str
        :param _ErrorCode: Authentication error code
        :type ErrorCode: int
        :param _EventName: Event name
        :type EventName: str
        :param _SecretId: Certificate ID
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SecretId: str
        :param _EventSource: Request source
        :type EventSource: str
        :param _RequestID: Request ID
        :type RequestID: str
        :param _ResourceRegion: Resource region
        :type ResourceRegion: str
        :param _AccountID: Root account ID
        :type AccountID: int
        :param _SourceIPAddress: Source IP
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SourceIPAddress: str
        :param _EventNameCn: Description of event name in Chinese (please use this field as required; if you are using other languages, ignore this field)
        :type EventNameCn: str
        :param _Resources: Resource pair
        :type Resources: :class:`tencentcloud.cloudaudit.v20190319.models.Resource`
        :param _EventRegion: Event region
        :type EventRegion: str
        :param _Location: IP location
        :type Location: str
        """
        self._EventId = None
        self._Username = None
        self._EventTime = None
        self._CloudAuditEvent = None
        self._ResourceTypeCn = None
        self._ErrorCode = None
        self._EventName = None
        self._SecretId = None
        self._EventSource = None
        self._RequestID = None
        self._ResourceRegion = None
        self._AccountID = None
        self._SourceIPAddress = None
        self._EventNameCn = None
        self._Resources = None
        self._EventRegion = None
        self._Location = None

    @property
    def EventId(self):
        """Log ID
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Username(self):
        """Username
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def EventTime(self):
        """Event Time
        :rtype: str
        """
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime

    @property
    def CloudAuditEvent(self):
        """Log details
        :rtype: str
        """
        return self._CloudAuditEvent

    @CloudAuditEvent.setter
    def CloudAuditEvent(self, CloudAuditEvent):
        self._CloudAuditEvent = CloudAuditEvent

    @property
    def ResourceTypeCn(self):
        """Description of resource type in Chinese (please use this field as required; if you are using other languages, ignore this field)
        :rtype: str
        """
        return self._ResourceTypeCn

    @ResourceTypeCn.setter
    def ResourceTypeCn(self, ResourceTypeCn):
        self._ResourceTypeCn = ResourceTypeCn

    @property
    def ErrorCode(self):
        """Authentication error code
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def EventName(self):
        """Event name
        :rtype: str
        """
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def SecretId(self):
        """Certificate ID
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def EventSource(self):
        """Request source
        :rtype: str
        """
        return self._EventSource

    @EventSource.setter
    def EventSource(self, EventSource):
        self._EventSource = EventSource

    @property
    def RequestID(self):
        """Request ID
        :rtype: str
        """
        return self._RequestID

    @RequestID.setter
    def RequestID(self, RequestID):
        self._RequestID = RequestID

    @property
    def ResourceRegion(self):
        """Resource region
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def AccountID(self):
        """Root account ID
        :rtype: int
        """
        return self._AccountID

    @AccountID.setter
    def AccountID(self, AccountID):
        self._AccountID = AccountID

    @property
    def SourceIPAddress(self):
        """Source IP
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SourceIPAddress

    @SourceIPAddress.setter
    def SourceIPAddress(self, SourceIPAddress):
        self._SourceIPAddress = SourceIPAddress

    @property
    def EventNameCn(self):
        """Description of event name in Chinese (please use this field as required; if you are using other languages, ignore this field)
        :rtype: str
        """
        return self._EventNameCn

    @EventNameCn.setter
    def EventNameCn(self, EventNameCn):
        self._EventNameCn = EventNameCn

    @property
    def Resources(self):
        """Resource pair
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.Resource`
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def EventRegion(self):
        """Event region
        :rtype: str
        """
        return self._EventRegion

    @EventRegion.setter
    def EventRegion(self, EventRegion):
        self._EventRegion = EventRegion

    @property
    def Location(self):
        """IP location
        :rtype: str
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._Username = params.get("Username")
        self._EventTime = params.get("EventTime")
        self._CloudAuditEvent = params.get("CloudAuditEvent")
        self._ResourceTypeCn = params.get("ResourceTypeCn")
        self._ErrorCode = params.get("ErrorCode")
        self._EventName = params.get("EventName")
        self._SecretId = params.get("SecretId")
        self._EventSource = params.get("EventSource")
        self._RequestID = params.get("RequestID")
        self._ResourceRegion = params.get("ResourceRegion")
        self._AccountID = params.get("AccountID")
        self._SourceIPAddress = params.get("SourceIPAddress")
        self._EventNameCn = params.get("EventNameCn")
        if params.get("Resources") is not None:
            self._Resources = Resource()
            self._Resources._deserialize(params.get("Resources"))
        self._EventRegion = params.get("EventRegion")
        self._Location = params.get("Location")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAttributeKeyRequest(AbstractModel):
    """GetAttributeKey request structure.

    """

    def __init__(self):
        r"""
        :param _WebsiteType: Website type. Valid values: zh, en. If this parameter is left empty, `zh` will be used by default
        :type WebsiteType: str
        """
        self._WebsiteType = None

    @property
    def WebsiteType(self):
        """Website type. Valid values: zh, en. If this parameter is left empty, `zh` will be used by default
        :rtype: str
        """
        return self._WebsiteType

    @WebsiteType.setter
    def WebsiteType(self, WebsiteType):
        self._WebsiteType = WebsiteType


    def _deserialize(self, params):
        self._WebsiteType = params.get("WebsiteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAttributeKeyResponse(AbstractModel):
    """GetAttributeKey response structure.

    """

    def __init__(self):
        r"""
        :param _AttributeKeyDetails: Valid values of `AttributeKey`
        :type AttributeKeyDetails: list of AttributeKeyDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AttributeKeyDetails = None
        self._RequestId = None

    @property
    def AttributeKeyDetails(self):
        """Valid values of `AttributeKey`
        :rtype: list of AttributeKeyDetail
        """
        return self._AttributeKeyDetails

    @AttributeKeyDetails.setter
    def AttributeKeyDetails(self, AttributeKeyDetails):
        self._AttributeKeyDetails = AttributeKeyDetails

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AttributeKeyDetails") is not None:
            self._AttributeKeyDetails = []
            for item in params.get("AttributeKeyDetails"):
                obj = AttributeKeyDetail()
                obj._deserialize(item)
                self._AttributeKeyDetails.append(obj)
        self._RequestId = params.get("RequestId")


class InquireAuditCreditRequest(AbstractModel):
    """InquireAuditCredit request structure.

    """


class InquireAuditCreditResponse(AbstractModel):
    """InquireAuditCredit response structure.

    """

    def __init__(self):
        r"""
        :param _AuditAmount: Number of tracking sets that can be created
        :type AuditAmount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AuditAmount = None
        self._RequestId = None

    @property
    def AuditAmount(self):
        """Number of tracking sets that can be created
        :rtype: int
        """
        return self._AuditAmount

    @AuditAmount.setter
    def AuditAmount(self, AuditAmount):
        self._AuditAmount = AuditAmount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AuditAmount = params.get("AuditAmount")
        self._RequestId = params.get("RequestId")


class ListAuditsRequest(AbstractModel):
    """ListAudits request structure.

    """


class ListAuditsResponse(AbstractModel):
    """ListAudits response structure.

    """

    def __init__(self):
        r"""
        :param _AuditSummarys: Set of queried tracking set summaries
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuditSummarys: list of AuditSummary
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AuditSummarys = None
        self._RequestId = None

    @property
    def AuditSummarys(self):
        """Set of queried tracking set summaries
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of AuditSummary
        """
        return self._AuditSummarys

    @AuditSummarys.setter
    def AuditSummarys(self, AuditSummarys):
        self._AuditSummarys = AuditSummarys

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AuditSummarys") is not None:
            self._AuditSummarys = []
            for item in params.get("AuditSummarys"):
                obj = AuditSummary()
                obj._deserialize(item)
                self._AuditSummarys.append(obj)
        self._RequestId = params.get("RequestId")


class ListCmqEnableRegionRequest(AbstractModel):
    """ListCmqEnableRegion request structure.

    """

    def __init__(self):
        r"""
        :param _WebsiteType: Website type. zh: Chinese mainland (default); en: outside Chinese mainland.
        :type WebsiteType: str
        """
        self._WebsiteType = None

    @property
    def WebsiteType(self):
        """Website type. zh: Chinese mainland (default); en: outside Chinese mainland.
        :rtype: str
        """
        return self._WebsiteType

    @WebsiteType.setter
    def WebsiteType(self, WebsiteType):
        self._WebsiteType = WebsiteType


    def _deserialize(self, params):
        self._WebsiteType = params.get("WebsiteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCmqEnableRegionResponse(AbstractModel):
    """ListCmqEnableRegion response structure.

    """

    def __init__(self):
        r"""
        :param _EnableRegions: CloudAudit-enabled CMQ AZs
        :type EnableRegions: list of CmqRegionInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EnableRegions = None
        self._RequestId = None

    @property
    def EnableRegions(self):
        """CloudAudit-enabled CMQ AZs
        :rtype: list of CmqRegionInfo
        """
        return self._EnableRegions

    @EnableRegions.setter
    def EnableRegions(self, EnableRegions):
        self._EnableRegions = EnableRegions

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EnableRegions") is not None:
            self._EnableRegions = []
            for item in params.get("EnableRegions"):
                obj = CmqRegionInfo()
                obj._deserialize(item)
                self._EnableRegions.append(obj)
        self._RequestId = params.get("RequestId")


class ListCosEnableRegionRequest(AbstractModel):
    """ListCosEnableRegion request structure.

    """

    def __init__(self):
        r"""
        :param _WebsiteType: Website type. zh: Chinese mainland (default); en: outside Chinese mainland.
        :type WebsiteType: str
        """
        self._WebsiteType = None

    @property
    def WebsiteType(self):
        """Website type. zh: Chinese mainland (default); en: outside Chinese mainland.
        :rtype: str
        """
        return self._WebsiteType

    @WebsiteType.setter
    def WebsiteType(self, WebsiteType):
        self._WebsiteType = WebsiteType


    def _deserialize(self, params):
        self._WebsiteType = params.get("WebsiteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCosEnableRegionResponse(AbstractModel):
    """ListCosEnableRegion response structure.

    """

    def __init__(self):
        r"""
        :param _EnableRegions: CloudAudit-enabled COS AZs
        :type EnableRegions: list of CosRegionInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EnableRegions = None
        self._RequestId = None

    @property
    def EnableRegions(self):
        """CloudAudit-enabled COS AZs
        :rtype: list of CosRegionInfo
        """
        return self._EnableRegions

    @EnableRegions.setter
    def EnableRegions(self, EnableRegions):
        self._EnableRegions = EnableRegions

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EnableRegions") is not None:
            self._EnableRegions = []
            for item in params.get("EnableRegions"):
                obj = CosRegionInfo()
                obj._deserialize(item)
                self._EnableRegions.append(obj)
        self._RequestId = params.get("RequestId")


class LookUpEventsRequest(AbstractModel):
    """LookUpEvents request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: int
        :param _EndTime: End time
        :type EndTime: int
        :param _LookupAttributes: Search criteria
        :type LookupAttributes: list of LookupAttribute
        :param _NextToken: Credential for viewing more logs
        :type NextToken: str
        :param _MaxResults: Maximum number of logs to be returned
        :type MaxResults: int
        :param _Mode: CloudAudit mode. Valid values: standard, quick. Default value: standard
        :type Mode: str
        """
        self._StartTime = None
        self._EndTime = None
        self._LookupAttributes = None
        self._NextToken = None
        self._MaxResults = None
        self._Mode = None

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def LookupAttributes(self):
        """Search criteria
        :rtype: list of LookupAttribute
        """
        return self._LookupAttributes

    @LookupAttributes.setter
    def LookupAttributes(self, LookupAttributes):
        self._LookupAttributes = LookupAttributes

    @property
    def NextToken(self):
        """Credential for viewing more logs
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def MaxResults(self):
        """Maximum number of logs to be returned
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def Mode(self):
        """CloudAudit mode. Valid values: standard, quick. Default value: standard
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("LookupAttributes") is not None:
            self._LookupAttributes = []
            for item in params.get("LookupAttributes"):
                obj = LookupAttribute()
                obj._deserialize(item)
                self._LookupAttributes.append(obj)
        self._NextToken = params.get("NextToken")
        self._MaxResults = params.get("MaxResults")
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LookUpEventsResponse(AbstractModel):
    """LookUpEvents response structure.

    """

    def __init__(self):
        r"""
        :param _NextToken: Credential for viewing more logs
Note: This field may return null, indicating that no valid values can be obtained.
        :type NextToken: str
        :param _Events: Logset
Note: This field may return null, indicating that no valid values can be obtained.
        :type Events: list of Event
        :param _ListOver: Whether the logset ends
Note: This field may return null, indicating that no valid values can be obtained.
        :type ListOver: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NextToken = None
        self._Events = None
        self._ListOver = None
        self._RequestId = None

    @property
    def NextToken(self):
        """Credential for viewing more logs
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def Events(self):
        """Logset
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Event
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def ListOver(self):
        """Whether the logset ends
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextToken = params.get("NextToken")
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = Event()
                obj._deserialize(item)
                self._Events.append(obj)
        self._ListOver = params.get("ListOver")
        self._RequestId = params.get("RequestId")


class LookupAttribute(AbstractModel):
    """Search criterion

    """

    def __init__(self):
        r"""
        :param _AttributeKey: Valid values: RequestId, EventName, ReadOnly, Username, ResourceType, ResourceName, AccessKeyId, and EventId
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type AttributeKey: str
        :param _AttributeValue: Value of `AttributeValue`
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type AttributeValue: str
        """
        self._AttributeKey = None
        self._AttributeValue = None

    @property
    def AttributeKey(self):
        """Valid values: RequestId, EventName, ReadOnly, Username, ResourceType, ResourceName, AccessKeyId, and EventId
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AttributeKey

    @AttributeKey.setter
    def AttributeKey(self, AttributeKey):
        self._AttributeKey = AttributeKey

    @property
    def AttributeValue(self):
        """Value of `AttributeValue`
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AttributeValue

    @AttributeValue.setter
    def AttributeValue(self, AttributeValue):
        self._AttributeValue = AttributeValue


    def _deserialize(self, params):
        self._AttributeKey = params.get("AttributeKey")
        self._AttributeValue = params.get("AttributeValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditTrackRequest(AbstractModel):
    """ModifyAuditTrack request structure.

    """

    def __init__(self):
        r"""
        :param _TrackId: Tracking set ID
        :type TrackId: int
        :param _Name: Tracking set name, which can only contain 3-48 letters, digits, hyphens, and underscores.
        :type Name: str
        :param _ActionType: Tracking set event type (`Read`: Read; `Write`: Write; `*`: All)
        :type ActionType: str
        :param _ResourceType: The product to which the tracking set event belongs. The value can be a single product such as `cos`, or `*` that indicates all products.
        :type ResourceType: str
        :param _Status: Tracking set status (0: Not enabled; 1: Enabled)
        :type Status: int
        :param _EventNames: The list of API names of tracking set events. When `ResourceType` is `*`, the value of `EventNames` must be `*`. When `ResourceType` is a specified product, the value of `EventNames` can be `*`. When `ResourceType` is `cos` or `cls`, up to 10 APIs are supported.
        :type EventNames: list of str
        :param _Storage: Storage type of shipped data. Valid values: `cos`, `cls`.
        :type Storage: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        :param _TrackForAllMembers: Whether to enable the feature of shipping organization members’ operation logs to the organization admin account or the trusted service admin account (0: Not enabled; 1: Enabled. This feature can only be enabled by the organization admin account or the trusted service admin account)
        :type TrackForAllMembers: int
        """
        self._TrackId = None
        self._Name = None
        self._ActionType = None
        self._ResourceType = None
        self._Status = None
        self._EventNames = None
        self._Storage = None
        self._TrackForAllMembers = None

    @property
    def TrackId(self):
        """Tracking set ID
        :rtype: int
        """
        return self._TrackId

    @TrackId.setter
    def TrackId(self, TrackId):
        self._TrackId = TrackId

    @property
    def Name(self):
        """Tracking set name, which can only contain 3-48 letters, digits, hyphens, and underscores.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ActionType(self):
        """Tracking set event type (`Read`: Read; `Write`: Write; `*`: All)
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ResourceType(self):
        """The product to which the tracking set event belongs. The value can be a single product such as `cos`, or `*` that indicates all products.
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Status(self):
        """Tracking set status (0: Not enabled; 1: Enabled)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EventNames(self):
        """The list of API names of tracking set events. When `ResourceType` is `*`, the value of `EventNames` must be `*`. When `ResourceType` is a specified product, the value of `EventNames` can be `*`. When `ResourceType` is `cos` or `cls`, up to 10 APIs are supported.
        :rtype: list of str
        """
        return self._EventNames

    @EventNames.setter
    def EventNames(self, EventNames):
        self._EventNames = EventNames

    @property
    def Storage(self):
        """Storage type of shipped data. Valid values: `cos`, `cls`.
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def TrackForAllMembers(self):
        """Whether to enable the feature of shipping organization members’ operation logs to the organization admin account or the trusted service admin account (0: Not enabled; 1: Enabled. This feature can only be enabled by the organization admin account or the trusted service admin account)
        :rtype: int
        """
        return self._TrackForAllMembers

    @TrackForAllMembers.setter
    def TrackForAllMembers(self, TrackForAllMembers):
        self._TrackForAllMembers = TrackForAllMembers


    def _deserialize(self, params):
        self._TrackId = params.get("TrackId")
        self._Name = params.get("Name")
        self._ActionType = params.get("ActionType")
        self._ResourceType = params.get("ResourceType")
        self._Status = params.get("Status")
        self._EventNames = params.get("EventNames")
        if params.get("Storage") is not None:
            self._Storage = Storage()
            self._Storage._deserialize(params.get("Storage"))
        self._TrackForAllMembers = params.get("TrackForAllMembers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditTrackResponse(AbstractModel):
    """ModifyAuditTrack response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Resource(AbstractModel):
    """Resource type

    """

    def __init__(self):
        r"""
        :param _ResourceType: Resource type
        :type ResourceType: str
        :param _ResourceName: Resource name
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ResourceName: str
        """
        self._ResourceType = None
        self._ResourceName = None

    @property
    def ResourceType(self):
        """Resource type
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        """Resource name
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartLoggingRequest(AbstractModel):
    """StartLogging request structure.

    """

    def __init__(self):
        r"""
        :param _AuditName: Tracking set name
        :type AuditName: str
        """
        self._AuditName = None

    @property
    def AuditName(self):
        """Tracking set name
        :rtype: str
        """
        return self._AuditName

    @AuditName.setter
    def AuditName(self, AuditName):
        self._AuditName = AuditName


    def _deserialize(self, params):
        self._AuditName = params.get("AuditName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartLoggingResponse(AbstractModel):
    """StartLogging response structure.

    """

    def __init__(self):
        r"""
        :param _IsSuccess: Whether enablement succeeded
        :type IsSuccess: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsSuccess = None
        self._RequestId = None

    @property
    def IsSuccess(self):
        """Whether enablement succeeded
        :rtype: int
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsSuccess = params.get("IsSuccess")
        self._RequestId = params.get("RequestId")


class StopLoggingRequest(AbstractModel):
    """StopLogging request structure.

    """

    def __init__(self):
        r"""
        :param _AuditName: Tracking set name
        :type AuditName: str
        """
        self._AuditName = None

    @property
    def AuditName(self):
        """Tracking set name
        :rtype: str
        """
        return self._AuditName

    @AuditName.setter
    def AuditName(self, AuditName):
        self._AuditName = AuditName


    def _deserialize(self, params):
        self._AuditName = params.get("AuditName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopLoggingResponse(AbstractModel):
    """StopLogging response structure.

    """

    def __init__(self):
        r"""
        :param _IsSuccess: Whether disablement succeeded
        :type IsSuccess: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsSuccess = None
        self._RequestId = None

    @property
    def IsSuccess(self):
        """Whether disablement succeeded
        :rtype: int
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsSuccess = params.get("IsSuccess")
        self._RequestId = params.get("RequestId")


class Storage(AbstractModel):
    """Tracking set storage information

    """

    def __init__(self):
        r"""
        :param _StorageType: Storage type (Valid values: cos, cls)
        :type StorageType: str
        :param _StorageRegion: Storage region
        :type StorageRegion: str
        :param _StorageName: Storage name. For COS, the storage name is the custom bucket name, which can contain up to 50 lowercase letters, digits, and hyphens. It cannot contain "-APPID" and cannot start or end with a hyphen. For CLS, the storage name is the log topic ID, which can contain 1-50 characters.
        :type StorageName: str
        :param _StoragePrefix: Storage directory prefix. The COS log file prefix can only contain 3-40 letters and digits.
        :type StoragePrefix: str
        """
        self._StorageType = None
        self._StorageRegion = None
        self._StorageName = None
        self._StoragePrefix = None

    @property
    def StorageType(self):
        """Storage type (Valid values: cos, cls)
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def StorageRegion(self):
        """Storage region
        :rtype: str
        """
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def StorageName(self):
        """Storage name. For COS, the storage name is the custom bucket name, which can contain up to 50 lowercase letters, digits, and hyphens. It cannot contain "-APPID" and cannot start or end with a hyphen. For CLS, the storage name is the log topic ID, which can contain 1-50 characters.
        :rtype: str
        """
        return self._StorageName

    @StorageName.setter
    def StorageName(self, StorageName):
        self._StorageName = StorageName

    @property
    def StoragePrefix(self):
        """Storage directory prefix. The COS log file prefix can only contain 3-40 letters and digits.
        :rtype: str
        """
        return self._StoragePrefix

    @StoragePrefix.setter
    def StoragePrefix(self, StoragePrefix):
        self._StoragePrefix = StoragePrefix


    def _deserialize(self, params):
        self._StorageType = params.get("StorageType")
        self._StorageRegion = params.get("StorageRegion")
        self._StorageName = params.get("StorageName")
        self._StoragePrefix = params.get("StoragePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tracks(AbstractModel):
    """Tracking set list

    """

    def __init__(self):
        r"""
        :param _Name: Tracking set name
        :type Name: str
        :param _ActionType: Tracking set event type (`Read`: Read; `Write`: Write; `*`: All)
        :type ActionType: str
        :param _ResourceType: The product to which the tracking set event belongs, such as `cos`, or `*` that indicates all products
        :type ResourceType: str
        :param _Status: Tracking set status (0: Not enabled; 1: Enabled)
        :type Status: int
        :param _EventNames: The list of API names of tracking set events (`*`: All)
        :type EventNames: list of str
        :param _Storage: Storage type of shipped data. Valid values: `cos`, `cls`.
        :type Storage: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        :param _CreateTime: Creation time of the tracking set
        :type CreateTime: str
        :param _TrackId: Tracking set ID
        :type TrackId: int
        """
        self._Name = None
        self._ActionType = None
        self._ResourceType = None
        self._Status = None
        self._EventNames = None
        self._Storage = None
        self._CreateTime = None
        self._TrackId = None

    @property
    def Name(self):
        """Tracking set name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ActionType(self):
        """Tracking set event type (`Read`: Read; `Write`: Write; `*`: All)
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ResourceType(self):
        """The product to which the tracking set event belongs, such as `cos`, or `*` that indicates all products
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Status(self):
        """Tracking set status (0: Not enabled; 1: Enabled)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EventNames(self):
        """The list of API names of tracking set events (`*`: All)
        :rtype: list of str
        """
        return self._EventNames

    @EventNames.setter
    def EventNames(self, EventNames):
        self._EventNames = EventNames

    @property
    def Storage(self):
        """Storage type of shipped data. Valid values: `cos`, `cls`.
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def CreateTime(self):
        """Creation time of the tracking set
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TrackId(self):
        """Tracking set ID
        :rtype: int
        """
        return self._TrackId

    @TrackId.setter
    def TrackId(self, TrackId):
        self._TrackId = TrackId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ActionType = params.get("ActionType")
        self._ResourceType = params.get("ResourceType")
        self._Status = params.get("Status")
        self._EventNames = params.get("EventNames")
        if params.get("Storage") is not None:
            self._Storage = Storage()
            self._Storage._deserialize(params.get("Storage"))
        self._CreateTime = params.get("CreateTime")
        self._TrackId = params.get("TrackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAuditRequest(AbstractModel):
    """UpdateAudit request structure.

    """

    def __init__(self):
        r"""
        :param _AuditName: Tracking set name
        :type AuditName: str
        :param _IsEnableCmqNotify: Whether to enable CMQ message notification. 1: Yes; 0: No. Only CMQ queue service is currently supported. If CMQ message notification is enabled, CloudAudit will deliver your log contents to the designated queue in the specified region in real time.
        :type IsEnableCmqNotify: int
        :param _ReadWriteAttribute: Manages the read/write attribute of event. Valid values: 1 (read-only), 2 (write-only), 3 (read/write).
        :type ReadWriteAttribute: int
        :param _KeyId: Globally unique ID of the CMK. This value is required if it is not a newly created KMS element. It can be obtained through `ListKeyAliasByRegion`. CloudAudit will not verify the validity of the `KeyId`. Enter it carefully to avoid data loss.
        :type KeyId: str
        :param _CosRegion: COS region. Supported regions can be queried through the `ListCosEnableRegion` API.
        :type CosRegion: str
        :param _CmqQueueName: Queue name, which must begin with a letter and can contain up to 64 letters, digits, and dashes (-). This field is required if the value of `IsEnableCmqNotify` is 1. If a queue is not newly created, CloudAudit will not verify whether it actually exists. Enter the name with caution to avoid log delivery failure and consequent data loss.
        :type CmqQueueName: str
        :param _IsCreateNewBucket: Whether to create a COS bucket. 1: Yes; 0: No.
        :type IsCreateNewBucket: int
        :param _KmsRegion: KMS region. Currently supported regions can be obtained through `ListKmsEnableRegion`. This must be the same as the COS region.
        :type KmsRegion: str
        :param _IsEnableKmsEncry: Whether to enable KMS encryption. 1: Yes, 0: No. If KMS encryption is enabled, the data will be encrypted when delivered to COS.
        :type IsEnableKmsEncry: int
        :param _CosBucketName: User-defined COS bucket name, which can only contain 1–40 lowercase letters (a–z), digits (0–9), and dashes (-) and cannot begin or end with "-". If a bucket is not newly created, CloudAudit will not verify whether it actually exists. Enter the name with caution to avoid log delivery failure and consequent data loss.
        :type CosBucketName: str
        :param _CmqRegion: Region where the queue is located. Supported CMQ regions can be queried through the `ListCmqEnableRegion` API. This field is required if the value of `IsEnableCmqNotify` is 1.
        :type CmqRegion: str
        :param _LogFilePrefix: Log file prefix, which can only contain 3–40 ASCII letters (a–z; A–Z) and digits (0–9).
        :type LogFilePrefix: str
        :param _IsCreateNewQueue: Whether to create a queue. 1: Yes; 0: No. This field is required if the value of `IsEnableCmqNotify` is 1.
        :type IsCreateNewQueue: int
        """
        self._AuditName = None
        self._IsEnableCmqNotify = None
        self._ReadWriteAttribute = None
        self._KeyId = None
        self._CosRegion = None
        self._CmqQueueName = None
        self._IsCreateNewBucket = None
        self._KmsRegion = None
        self._IsEnableKmsEncry = None
        self._CosBucketName = None
        self._CmqRegion = None
        self._LogFilePrefix = None
        self._IsCreateNewQueue = None

    @property
    def AuditName(self):
        """Tracking set name
        :rtype: str
        """
        return self._AuditName

    @AuditName.setter
    def AuditName(self, AuditName):
        self._AuditName = AuditName

    @property
    def IsEnableCmqNotify(self):
        """Whether to enable CMQ message notification. 1: Yes; 0: No. Only CMQ queue service is currently supported. If CMQ message notification is enabled, CloudAudit will deliver your log contents to the designated queue in the specified region in real time.
        :rtype: int
        """
        return self._IsEnableCmqNotify

    @IsEnableCmqNotify.setter
    def IsEnableCmqNotify(self, IsEnableCmqNotify):
        self._IsEnableCmqNotify = IsEnableCmqNotify

    @property
    def ReadWriteAttribute(self):
        """Manages the read/write attribute of event. Valid values: 1 (read-only), 2 (write-only), 3 (read/write).
        :rtype: int
        """
        return self._ReadWriteAttribute

    @ReadWriteAttribute.setter
    def ReadWriteAttribute(self, ReadWriteAttribute):
        self._ReadWriteAttribute = ReadWriteAttribute

    @property
    def KeyId(self):
        """Globally unique ID of the CMK. This value is required if it is not a newly created KMS element. It can be obtained through `ListKeyAliasByRegion`. CloudAudit will not verify the validity of the `KeyId`. Enter it carefully to avoid data loss.
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def CosRegion(self):
        """COS region. Supported regions can be queried through the `ListCosEnableRegion` API.
        :rtype: str
        """
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def CmqQueueName(self):
        """Queue name, which must begin with a letter and can contain up to 64 letters, digits, and dashes (-). This field is required if the value of `IsEnableCmqNotify` is 1. If a queue is not newly created, CloudAudit will not verify whether it actually exists. Enter the name with caution to avoid log delivery failure and consequent data loss.
        :rtype: str
        """
        return self._CmqQueueName

    @CmqQueueName.setter
    def CmqQueueName(self, CmqQueueName):
        self._CmqQueueName = CmqQueueName

    @property
    def IsCreateNewBucket(self):
        """Whether to create a COS bucket. 1: Yes; 0: No.
        :rtype: int
        """
        return self._IsCreateNewBucket

    @IsCreateNewBucket.setter
    def IsCreateNewBucket(self, IsCreateNewBucket):
        self._IsCreateNewBucket = IsCreateNewBucket

    @property
    def KmsRegion(self):
        """KMS region. Currently supported regions can be obtained through `ListKmsEnableRegion`. This must be the same as the COS region.
        :rtype: str
        """
        return self._KmsRegion

    @KmsRegion.setter
    def KmsRegion(self, KmsRegion):
        self._KmsRegion = KmsRegion

    @property
    def IsEnableKmsEncry(self):
        """Whether to enable KMS encryption. 1: Yes, 0: No. If KMS encryption is enabled, the data will be encrypted when delivered to COS.
        :rtype: int
        """
        return self._IsEnableKmsEncry

    @IsEnableKmsEncry.setter
    def IsEnableKmsEncry(self, IsEnableKmsEncry):
        self._IsEnableKmsEncry = IsEnableKmsEncry

    @property
    def CosBucketName(self):
        """User-defined COS bucket name, which can only contain 1–40 lowercase letters (a–z), digits (0–9), and dashes (-) and cannot begin or end with "-". If a bucket is not newly created, CloudAudit will not verify whether it actually exists. Enter the name with caution to avoid log delivery failure and consequent data loss.
        :rtype: str
        """
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def CmqRegion(self):
        """Region where the queue is located. Supported CMQ regions can be queried through the `ListCmqEnableRegion` API. This field is required if the value of `IsEnableCmqNotify` is 1.
        :rtype: str
        """
        return self._CmqRegion

    @CmqRegion.setter
    def CmqRegion(self, CmqRegion):
        self._CmqRegion = CmqRegion

    @property
    def LogFilePrefix(self):
        """Log file prefix, which can only contain 3–40 ASCII letters (a–z; A–Z) and digits (0–9).
        :rtype: str
        """
        return self._LogFilePrefix

    @LogFilePrefix.setter
    def LogFilePrefix(self, LogFilePrefix):
        self._LogFilePrefix = LogFilePrefix

    @property
    def IsCreateNewQueue(self):
        """Whether to create a queue. 1: Yes; 0: No. This field is required if the value of `IsEnableCmqNotify` is 1.
        :rtype: int
        """
        return self._IsCreateNewQueue

    @IsCreateNewQueue.setter
    def IsCreateNewQueue(self, IsCreateNewQueue):
        self._IsCreateNewQueue = IsCreateNewQueue


    def _deserialize(self, params):
        self._AuditName = params.get("AuditName")
        self._IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self._ReadWriteAttribute = params.get("ReadWriteAttribute")
        self._KeyId = params.get("KeyId")
        self._CosRegion = params.get("CosRegion")
        self._CmqQueueName = params.get("CmqQueueName")
        self._IsCreateNewBucket = params.get("IsCreateNewBucket")
        self._KmsRegion = params.get("KmsRegion")
        self._IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self._CosBucketName = params.get("CosBucketName")
        self._CmqRegion = params.get("CmqRegion")
        self._LogFilePrefix = params.get("LogFilePrefix")
        self._IsCreateNewQueue = params.get("IsCreateNewQueue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAuditResponse(AbstractModel):
    """UpdateAudit response structure.

    """

    def __init__(self):
        r"""
        :param _IsSuccess: Whether update succeeded
        :type IsSuccess: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsSuccess = None
        self._RequestId = None

    @property
    def IsSuccess(self):
        """Whether update succeeded
        :rtype: int
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsSuccess = params.get("IsSuccess")
        self._RequestId = params.get("RequestId")