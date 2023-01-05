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
        :param LabelType: Input box type
        :type LabelType: str
        :param Starter: Initial display
        :type Starter: str
        :param Order: Display sort order
        :type Order: int
        :param Value: `AttributeKey` value
        :type Value: str
        :param Label: Tag
        :type Label: str
        """
        self.LabelType = None
        self.Starter = None
        self.Order = None
        self.Value = None
        self.Label = None


    def _deserialize(self, params):
        self.LabelType = params.get("LabelType")
        self.Starter = params.get("Starter")
        self.Order = params.get("Order")
        self.Value = params.get("Value")
        self.Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditSummary(AbstractModel):
    """Tracking set overview

    """

    def __init__(self):
        r"""
        :param AuditStatus: Tracking set status. 1: enabled, 0: disabled
        :type AuditStatus: int
        :param CosBucketName: COS bucket name
        :type CosBucketName: str
        :param AuditName: Tracking set name
        :type AuditName: str
        :param LogFilePrefix: Log prefix
        :type LogFilePrefix: str
        """
        self.AuditStatus = None
        self.CosBucketName = None
        self.AuditName = None
        self.LogFilePrefix = None


    def _deserialize(self, params):
        self.AuditStatus = params.get("AuditStatus")
        self.CosBucketName = params.get("CosBucketName")
        self.AuditName = params.get("AuditName")
        self.LogFilePrefix = params.get("LogFilePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqRegionInfo(AbstractModel):
    """CMQ region information

    """

    def __init__(self):
        r"""
        :param CmqRegionName: Region description
        :type CmqRegionName: str
        :param CmqRegion: CMQ region
        :type CmqRegion: str
        """
        self.CmqRegionName = None
        self.CmqRegion = None


    def _deserialize(self, params):
        self.CmqRegionName = params.get("CmqRegionName")
        self.CmqRegion = params.get("CmqRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosRegionInfo(AbstractModel):
    """COS region information

    """

    def __init__(self):
        r"""
        :param CosRegion: COS region
        :type CosRegion: str
        :param CosRegionName: Region description
        :type CosRegionName: str
        """
        self.CosRegion = None
        self.CosRegionName = None


    def _deserialize(self, params):
        self.CosRegion = params.get("CosRegion")
        self.CosRegionName = params.get("CosRegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditRequest(AbstractModel):
    """CreateAudit request structure.

    """

    def __init__(self):
        r"""
        :param IsEnableCmqNotify: Whether to enable CMQ message notification. 1: Yes; 0: No. Only CMQ queue service is currently supported. If CMQ message notification is enabled, CloudAudit will deliver your log contents to the designated queue in the specified region in real time.
        :type IsEnableCmqNotify: int
        :param ReadWriteAttribute: Manages the read/write attribute of event. Valid values: 1 (read-only), 2 (write-only), 3 (read/write).
        :type ReadWriteAttribute: int
        :param AuditName: Tracking set name, which can contain 3–128 ASCII letters (a–z; A–Z), digits (0–9), and underscores (_).
        :type AuditName: str
        :param CosRegion: COS region. Supported regions can be queried through the `ListCosEnableRegion` API.
        :type CosRegion: str
        :param IsCreateNewBucket: Whether to create a COS bucket. 1: Yes; 0: No.
        :type IsCreateNewBucket: int
        :param CosBucketName: User-defined COS bucket name, which can only contain 1–40 lowercase letters (a–z), digits (0–9), and dashes (-) and cannot begin or end with "-". If a bucket is not newly created, CloudAudit will not verify whether it actually exists. Enter the name with caution to avoid log delivery failure and consequent data loss.
        :type CosBucketName: str
        :param KeyId: Globally unique ID of the CMK. This value is required if it is not a newly created KMS element. It can be obtained through `ListKeyAliasByRegion`. CloudAudit will not verify the validity of the `KeyId`. Enter it carefully to avoid data loss.
        :type KeyId: str
        :param CmqQueueName: Queue name, which must begin with a letter and can contain up to 64 letters, digits, and dashes (-). This field is required if the value of `IsEnableCmqNotify` is 1. If a queue is not newly created, CloudAudit will not verify whether it actually exists. Enter the name with caution to avoid log delivery failure and consequent data loss.
        :type CmqQueueName: str
        :param KmsRegion: KMS region. Currently supported regions can be obtained through `ListKmsEnableRegion`. This must be the same as the COS region.
        :type KmsRegion: str
        :param IsEnableKmsEncry: Whether to enable KMS encryption. 1: Yes, 0: No. If KMS encryption is enabled, the data will be encrypted when delivered to COS.
        :type IsEnableKmsEncry: int
        :param CmqRegion: Region where the queue is located. Supported CMQ regions can be queried through the `ListCmqEnableRegion` API. This field is required if the value of `IsEnableCmqNotify` is 1.
        :type CmqRegion: str
        :param LogFilePrefix: Log file prefix, which can only contain 3–40 ASCII letters (a–z; A–Z) and digits (0–9). It can be left empty and is the account ID by default.
        :type LogFilePrefix: str
        :param IsCreateNewQueue: Whether to create a queue. 1: Yes; 0: No. This field is required if the value of `IsEnableCmqNotify` is 1.
        :type IsCreateNewQueue: int
        """
        self.IsEnableCmqNotify = None
        self.ReadWriteAttribute = None
        self.AuditName = None
        self.CosRegion = None
        self.IsCreateNewBucket = None
        self.CosBucketName = None
        self.KeyId = None
        self.CmqQueueName = None
        self.KmsRegion = None
        self.IsEnableKmsEncry = None
        self.CmqRegion = None
        self.LogFilePrefix = None
        self.IsCreateNewQueue = None


    def _deserialize(self, params):
        self.IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self.ReadWriteAttribute = params.get("ReadWriteAttribute")
        self.AuditName = params.get("AuditName")
        self.CosRegion = params.get("CosRegion")
        self.IsCreateNewBucket = params.get("IsCreateNewBucket")
        self.CosBucketName = params.get("CosBucketName")
        self.KeyId = params.get("KeyId")
        self.CmqQueueName = params.get("CmqQueueName")
        self.KmsRegion = params.get("KmsRegion")
        self.IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self.CmqRegion = params.get("CmqRegion")
        self.LogFilePrefix = params.get("LogFilePrefix")
        self.IsCreateNewQueue = params.get("IsCreateNewQueue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditResponse(AbstractModel):
    """CreateAudit response structure.

    """

    def __init__(self):
        r"""
        :param IsSuccess: Whether creation succeeded.
        :type IsSuccess: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class CreateAuditTrackRequest(AbstractModel):
    """CreateAuditTrack request structure.

    """

    def __init__(self):
        r"""
        :param Name: Tracking set name, which can only contain 3-48 letters, digits, hyphens, and underscores.
        :type Name: str
        :param ActionType: Tracking set event type (`Read`: Read; `Write`: Write; `*`: All)
        :type ActionType: str
        :param ResourceType: The product to which the tracking set event belongs. The value can be a single product such as `cos`, or `*` that indicates all products.
        :type ResourceType: str
        :param Status: Tracking set status (0: Not enabled; 1: Enabled)
        :type Status: int
        :param EventNames: The list of API names of tracking set events. When `ResourceType` is `*`, the value of `EventNames` must be `*`. When `ResourceType` is a specified product, the value of `EventNames` can be `*`. When `ResourceType` is `cos` or `cls`, up to 10 APIs are supported.
        :type EventNames: list of str
        :param Storage: Storage type of shipped data. Valid values: `cos`, `cls`.
        :type Storage: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        :param TrackForAllMembers: Whether to enable the feature of shipping organization members’ operation logs to the organization admin account or the trusted service admin account (0: Not enabled; 1: Enabled. This feature can only be enabled by the organization admin account or the trusted service admin account)
        :type TrackForAllMembers: int
        """
        self.Name = None
        self.ActionType = None
        self.ResourceType = None
        self.Status = None
        self.EventNames = None
        self.Storage = None
        self.TrackForAllMembers = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ActionType = params.get("ActionType")
        self.ResourceType = params.get("ResourceType")
        self.Status = params.get("Status")
        self.EventNames = params.get("EventNames")
        if params.get("Storage") is not None:
            self.Storage = Storage()
            self.Storage._deserialize(params.get("Storage"))
        self.TrackForAllMembers = params.get("TrackForAllMembers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditTrackResponse(AbstractModel):
    """CreateAuditTrack response structure.

    """

    def __init__(self):
        r"""
        :param TrackId: Tracking set ID
        :type TrackId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TrackId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TrackId = params.get("TrackId")
        self.RequestId = params.get("RequestId")


class DeleteAuditRequest(AbstractModel):
    """DeleteAudit request structure.

    """

    def __init__(self):
        r"""
        :param AuditName: Tracking set name
        :type AuditName: str
        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditResponse(AbstractModel):
    """DeleteAudit response structure.

    """

    def __init__(self):
        r"""
        :param IsSuccess: Whether deletion succeeded
        :type IsSuccess: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class DeleteAuditTrackRequest(AbstractModel):
    """DeleteAuditTrack request structure.

    """

    def __init__(self):
        r"""
        :param TrackId: Tracking set ID
        :type TrackId: int
        """
        self.TrackId = None


    def _deserialize(self, params):
        self.TrackId = params.get("TrackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditTrackResponse(AbstractModel):
    """DeleteAuditTrack response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAuditRequest(AbstractModel):
    """DescribeAudit request structure.

    """

    def __init__(self):
        r"""
        :param AuditName: Tracking set name
        :type AuditName: str
        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditResponse(AbstractModel):
    """DescribeAudit response structure.

    """

    def __init__(self):
        r"""
        :param IsEnableCmqNotify: Whether to enable CMQ message notification. 1: Yes; 0: No.
        :type IsEnableCmqNotify: int
        :param ReadWriteAttribute: Manages the read/write attribute of event. Valid values: 1 (read-only), 2 (write-only), 3 (read/write)
        :type ReadWriteAttribute: int
        :param KeyId: Globally unique CMK ID.
        :type KeyId: str
        :param AuditStatus: Tracking set status. 1: enabled, 0: disabled.
        :type AuditStatus: int
        :param AuditName: Tracking set name.
        :type AuditName: str
        :param CosRegion: COS bucket region.
        :type CosRegion: str
        :param CmqQueueName: Queue name.
        :type CmqQueueName: str
        :param KmsAlias: CMK alias.
        :type KmsAlias: str
        :param KmsRegion: KMS region.
        :type KmsRegion: str
        :param IsEnableKmsEncry: Whether to enable KMS encryption. 1: Yes, 0: No. If KMS encryption is enabled, the data will be encrypted when it is delivered to COS.
        :type IsEnableKmsEncry: int
        :param CosBucketName: COS bucket name.
        :type CosBucketName: str
        :param CmqRegion: Queue region.
        :type CmqRegion: str
        :param LogFilePrefix: Log prefix.
        :type LogFilePrefix: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IsEnableCmqNotify = None
        self.ReadWriteAttribute = None
        self.KeyId = None
        self.AuditStatus = None
        self.AuditName = None
        self.CosRegion = None
        self.CmqQueueName = None
        self.KmsAlias = None
        self.KmsRegion = None
        self.IsEnableKmsEncry = None
        self.CosBucketName = None
        self.CmqRegion = None
        self.LogFilePrefix = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self.ReadWriteAttribute = params.get("ReadWriteAttribute")
        self.KeyId = params.get("KeyId")
        self.AuditStatus = params.get("AuditStatus")
        self.AuditName = params.get("AuditName")
        self.CosRegion = params.get("CosRegion")
        self.CmqQueueName = params.get("CmqQueueName")
        self.KmsAlias = params.get("KmsAlias")
        self.KmsRegion = params.get("KmsRegion")
        self.IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self.CosBucketName = params.get("CosBucketName")
        self.CmqRegion = params.get("CmqRegion")
        self.LogFilePrefix = params.get("LogFilePrefix")
        self.RequestId = params.get("RequestId")


class DescribeAuditTrackRequest(AbstractModel):
    """DescribeAuditTrack request structure.

    """

    def __init__(self):
        r"""
        :param TrackId: Tracking set ID
        :type TrackId: int
        """
        self.TrackId = None


    def _deserialize(self, params):
        self.TrackId = params.get("TrackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditTrackResponse(AbstractModel):
    """DescribeAuditTrack response structure.

    """

    def __init__(self):
        r"""
        :param Name: Tracking set name
        :type Name: str
        :param ActionType: Tracking set event type (`Read`: Read; `Write`: Write; `*`: All)
        :type ActionType: str
        :param ResourceType: The product to which the tracking set event belongs, such as `cos`, or `*` that indicates all products
        :type ResourceType: str
        :param Status: Tracking set status (0: Not enabled; 1: Enabled)
        :type Status: int
        :param EventNames: The list of API names of tracking set events (`*`: All)
        :type EventNames: list of str
        :param Storage: Storage type of shipped data. Valid values: `cos`, `cls`.
        :type Storage: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        :param CreateTime: Creation time of the tracking set
        :type CreateTime: str
        :param TrackForAllMembers: Whether to enable the feature of shipping organization members’ operation logs to the organization admin account or the trusted service admin account
Note: This field may return null, indicating that no valid values can be obtained.
        :type TrackForAllMembers: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Name = None
        self.ActionType = None
        self.ResourceType = None
        self.Status = None
        self.EventNames = None
        self.Storage = None
        self.CreateTime = None
        self.TrackForAllMembers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ActionType = params.get("ActionType")
        self.ResourceType = params.get("ResourceType")
        self.Status = params.get("Status")
        self.EventNames = params.get("EventNames")
        if params.get("Storage") is not None:
            self.Storage = Storage()
            self.Storage._deserialize(params.get("Storage"))
        self.CreateTime = params.get("CreateTime")
        self.TrackForAllMembers = params.get("TrackForAllMembers")
        self.RequestId = params.get("RequestId")


class DescribeAuditTracksRequest(AbstractModel):
    """DescribeAuditTracks request structure.

    """

    def __init__(self):
        r"""
        :param PageNumber: Page number
        :type PageNumber: int
        :param PageSize: The number of tracking sets per page
        :type PageSize: int
        """
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditTracksResponse(AbstractModel):
    """DescribeAuditTracks response structure.

    """

    def __init__(self):
        r"""
        :param Tracks: Tracking set list
        :type Tracks: list of Tracks
        :param TotalCount: Total number of tracking sets
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Tracks = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tracks") is not None:
            self.Tracks = []
            for item in params.get("Tracks"):
                obj = Tracks()
                obj._deserialize(item)
                self.Tracks.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeEventsRequest(AbstractModel):
    """DescribeEvents request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start timestamp in seconds (cannot be 90 days after the current time).
        :type StartTime: int
        :param EndTime: End timestamp in seconds (the time range for query is less than 30 days).
        :type EndTime: int
        :param NextToken: Credential for viewing more logs.
        :type NextToken: int
        :param MaxResults: Max number of returned logs (up to 50).
        :type MaxResults: int
        :param LookupAttributes: Search condition. Valid values: `RequestId`, `EventName`, `ActionType` (write/read), `PrincipalId` (sub-account), `ResourceType`, `ResourceName`, `AccessKeyId`, `SensitiveAction`, `ApiErrorCode`, `CamErrorCode`, and `Tags` (Format of AttributeValue: [{"key":"*","value":"*"}])
        :type LookupAttributes: list of LookupAttribute
        :param IsReturnLocation: Whether to return the IP location. `1`: yes, `0`: no.
        :type IsReturnLocation: int
        """
        self.StartTime = None
        self.EndTime = None
        self.NextToken = None
        self.MaxResults = None
        self.LookupAttributes = None
        self.IsReturnLocation = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.NextToken = params.get("NextToken")
        self.MaxResults = params.get("MaxResults")
        if params.get("LookupAttributes") is not None:
            self.LookupAttributes = []
            for item in params.get("LookupAttributes"):
                obj = LookupAttribute()
                obj._deserialize(item)
                self.LookupAttributes.append(obj)
        self.IsReturnLocation = params.get("IsReturnLocation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEventsResponse(AbstractModel):
    """DescribeEvents response structure.

    """

    def __init__(self):
        r"""
        :param ListOver: Whether the log list has come to an end. `true`: Yes. Pagination is not required.
        :type ListOver: bool
        :param NextToken: Credential for viewing more logs.
        :type NextToken: int
        :param Events: Logset.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Events: list of Event
        :param TotalCount: This parameter has been deprecated. Please use `ListOver` and `NextToken` for pagination, and read data of the next page when the value of `ListOver` is `false`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ListOver = None
        self.NextToken = None
        self.Events = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListOver = params.get("ListOver")
        self.NextToken = params.get("NextToken")
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = Event()
                obj._deserialize(item)
                self.Events.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class Event(AbstractModel):
    """Log details

    """

    def __init__(self):
        r"""
        :param EventId: Log ID
        :type EventId: str
        :param Username: Username
        :type Username: str
        :param EventTime: Event Time
        :type EventTime: str
        :param CloudAuditEvent: Log details
        :type CloudAuditEvent: str
        :param ResourceTypeCn: Description of resource type in Chinese (please use this field as required; if you are using other languages, ignore this field)
        :type ResourceTypeCn: str
        :param ErrorCode: Authentication error code
        :type ErrorCode: int
        :param EventName: Event name
        :type EventName: str
        :param SecretId: Certificate ID
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SecretId: str
        :param EventSource: Request source
        :type EventSource: str
        :param RequestID: Request ID
        :type RequestID: str
        :param ResourceRegion: Resource region
        :type ResourceRegion: str
        :param AccountID: Root account ID
        :type AccountID: int
        :param SourceIPAddress: Source IP
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SourceIPAddress: str
        :param EventNameCn: Description of event name in Chinese (please use this field as required; if you are using other languages, ignore this field)
        :type EventNameCn: str
        :param Resources: Resource pair
        :type Resources: :class:`tencentcloud.cloudaudit.v20190319.models.Resource`
        :param EventRegion: Event region
        :type EventRegion: str
        :param Location: IP location
        :type Location: str
        """
        self.EventId = None
        self.Username = None
        self.EventTime = None
        self.CloudAuditEvent = None
        self.ResourceTypeCn = None
        self.ErrorCode = None
        self.EventName = None
        self.SecretId = None
        self.EventSource = None
        self.RequestID = None
        self.ResourceRegion = None
        self.AccountID = None
        self.SourceIPAddress = None
        self.EventNameCn = None
        self.Resources = None
        self.EventRegion = None
        self.Location = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.Username = params.get("Username")
        self.EventTime = params.get("EventTime")
        self.CloudAuditEvent = params.get("CloudAuditEvent")
        self.ResourceTypeCn = params.get("ResourceTypeCn")
        self.ErrorCode = params.get("ErrorCode")
        self.EventName = params.get("EventName")
        self.SecretId = params.get("SecretId")
        self.EventSource = params.get("EventSource")
        self.RequestID = params.get("RequestID")
        self.ResourceRegion = params.get("ResourceRegion")
        self.AccountID = params.get("AccountID")
        self.SourceIPAddress = params.get("SourceIPAddress")
        self.EventNameCn = params.get("EventNameCn")
        if params.get("Resources") is not None:
            self.Resources = Resource()
            self.Resources._deserialize(params.get("Resources"))
        self.EventRegion = params.get("EventRegion")
        self.Location = params.get("Location")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAttributeKeyRequest(AbstractModel):
    """GetAttributeKey request structure.

    """

    def __init__(self):
        r"""
        :param WebsiteType: Website type. Valid values: zh, en. If this parameter is left empty, `zh` will be used by default
        :type WebsiteType: str
        """
        self.WebsiteType = None


    def _deserialize(self, params):
        self.WebsiteType = params.get("WebsiteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAttributeKeyResponse(AbstractModel):
    """GetAttributeKey response structure.

    """

    def __init__(self):
        r"""
        :param AttributeKeyDetails: Valid values of `AttributeKey`
        :type AttributeKeyDetails: list of AttributeKeyDetail
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AttributeKeyDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AttributeKeyDetails") is not None:
            self.AttributeKeyDetails = []
            for item in params.get("AttributeKeyDetails"):
                obj = AttributeKeyDetail()
                obj._deserialize(item)
                self.AttributeKeyDetails.append(obj)
        self.RequestId = params.get("RequestId")


class InquireAuditCreditRequest(AbstractModel):
    """InquireAuditCredit request structure.

    """


class InquireAuditCreditResponse(AbstractModel):
    """InquireAuditCredit response structure.

    """

    def __init__(self):
        r"""
        :param AuditAmount: Number of tracking sets that can be created
        :type AuditAmount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AuditAmount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AuditAmount = params.get("AuditAmount")
        self.RequestId = params.get("RequestId")


class ListAuditsRequest(AbstractModel):
    """ListAudits request structure.

    """


class ListAuditsResponse(AbstractModel):
    """ListAudits response structure.

    """

    def __init__(self):
        r"""
        :param AuditSummarys: Set of queried tracking set summaries
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuditSummarys: list of AuditSummary
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AuditSummarys = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AuditSummarys") is not None:
            self.AuditSummarys = []
            for item in params.get("AuditSummarys"):
                obj = AuditSummary()
                obj._deserialize(item)
                self.AuditSummarys.append(obj)
        self.RequestId = params.get("RequestId")


class ListCmqEnableRegionRequest(AbstractModel):
    """ListCmqEnableRegion request structure.

    """

    def __init__(self):
        r"""
        :param WebsiteType: Website type. zh: Chinese mainland (default); en: outside Chinese mainland.
        :type WebsiteType: str
        """
        self.WebsiteType = None


    def _deserialize(self, params):
        self.WebsiteType = params.get("WebsiteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCmqEnableRegionResponse(AbstractModel):
    """ListCmqEnableRegion response structure.

    """

    def __init__(self):
        r"""
        :param EnableRegions: CloudAudit-enabled CMQ AZs
        :type EnableRegions: list of CmqRegionInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EnableRegions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EnableRegions") is not None:
            self.EnableRegions = []
            for item in params.get("EnableRegions"):
                obj = CmqRegionInfo()
                obj._deserialize(item)
                self.EnableRegions.append(obj)
        self.RequestId = params.get("RequestId")


class ListCosEnableRegionRequest(AbstractModel):
    """ListCosEnableRegion request structure.

    """

    def __init__(self):
        r"""
        :param WebsiteType: Website type. zh: Chinese mainland (default); en: outside Chinese mainland.
        :type WebsiteType: str
        """
        self.WebsiteType = None


    def _deserialize(self, params):
        self.WebsiteType = params.get("WebsiteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCosEnableRegionResponse(AbstractModel):
    """ListCosEnableRegion response structure.

    """

    def __init__(self):
        r"""
        :param EnableRegions: CloudAudit-enabled COS AZs
        :type EnableRegions: list of CosRegionInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EnableRegions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EnableRegions") is not None:
            self.EnableRegions = []
            for item in params.get("EnableRegions"):
                obj = CosRegionInfo()
                obj._deserialize(item)
                self.EnableRegions.append(obj)
        self.RequestId = params.get("RequestId")


class LookUpEventsRequest(AbstractModel):
    """LookUpEvents request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: int
        :param EndTime: End time
        :type EndTime: int
        :param LookupAttributes: Search criteria
        :type LookupAttributes: list of LookupAttribute
        :param NextToken: Credential for viewing more logs
        :type NextToken: str
        :param MaxResults: Maximum number of logs to be returned
        :type MaxResults: int
        :param Mode: CloudAudit mode. Valid values: standard, quick. Default value: standard
        :type Mode: str
        """
        self.StartTime = None
        self.EndTime = None
        self.LookupAttributes = None
        self.NextToken = None
        self.MaxResults = None
        self.Mode = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("LookupAttributes") is not None:
            self.LookupAttributes = []
            for item in params.get("LookupAttributes"):
                obj = LookupAttribute()
                obj._deserialize(item)
                self.LookupAttributes.append(obj)
        self.NextToken = params.get("NextToken")
        self.MaxResults = params.get("MaxResults")
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LookUpEventsResponse(AbstractModel):
    """LookUpEvents response structure.

    """

    def __init__(self):
        r"""
        :param NextToken: Credential for viewing more logs
Note: This field may return null, indicating that no valid values can be obtained.
        :type NextToken: str
        :param Events: Logset
Note: This field may return null, indicating that no valid values can be obtained.
        :type Events: list of Event
        :param ListOver: Whether the logset ends
Note: This field may return null, indicating that no valid values can be obtained.
        :type ListOver: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NextToken = None
        self.Events = None
        self.ListOver = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NextToken = params.get("NextToken")
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = Event()
                obj._deserialize(item)
                self.Events.append(obj)
        self.ListOver = params.get("ListOver")
        self.RequestId = params.get("RequestId")


class LookupAttribute(AbstractModel):
    """Search criterion

    """

    def __init__(self):
        r"""
        :param AttributeKey: Valid values: RequestId, EventName, ReadOnly, Username, ResourceType, ResourceName, AccessKeyId, and EventId
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type AttributeKey: str
        :param AttributeValue: Value of `AttributeValue`
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type AttributeValue: str
        """
        self.AttributeKey = None
        self.AttributeValue = None


    def _deserialize(self, params):
        self.AttributeKey = params.get("AttributeKey")
        self.AttributeValue = params.get("AttributeValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditTrackRequest(AbstractModel):
    """ModifyAuditTrack request structure.

    """

    def __init__(self):
        r"""
        :param TrackId: Tracking set ID
        :type TrackId: int
        :param Name: Tracking set name, which can only contain 3-48 letters, digits, hyphens, and underscores.
        :type Name: str
        :param ActionType: Tracking set event type (`Read`: Read; `Write`: Write; `*`: All)
        :type ActionType: str
        :param ResourceType: The product to which the tracking set event belongs. The value can be a single product such as `cos`, or `*` that indicates all products.
        :type ResourceType: str
        :param Status: Tracking set status (0: Not enabled; 1: Enabled)
        :type Status: int
        :param EventNames: The list of API names of tracking set events. When `ResourceType` is `*`, the value of `EventNames` must be `*`. When `ResourceType` is a specified product, the value of `EventNames` can be `*`. When `ResourceType` is `cos` or `cls`, up to 10 APIs are supported.
        :type EventNames: list of str
        :param Storage: Storage type of shipped data. Valid values: `cos`, `cls`.
        :type Storage: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        :param TrackForAllMembers: Whether to enable the feature of shipping organization members’ operation logs to the organization admin account or the trusted service admin account (0: Not enabled; 1: Enabled. This feature can only be enabled by the organization admin account or the trusted service admin account)
        :type TrackForAllMembers: int
        """
        self.TrackId = None
        self.Name = None
        self.ActionType = None
        self.ResourceType = None
        self.Status = None
        self.EventNames = None
        self.Storage = None
        self.TrackForAllMembers = None


    def _deserialize(self, params):
        self.TrackId = params.get("TrackId")
        self.Name = params.get("Name")
        self.ActionType = params.get("ActionType")
        self.ResourceType = params.get("ResourceType")
        self.Status = params.get("Status")
        self.EventNames = params.get("EventNames")
        if params.get("Storage") is not None:
            self.Storage = Storage()
            self.Storage._deserialize(params.get("Storage"))
        self.TrackForAllMembers = params.get("TrackForAllMembers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditTrackResponse(AbstractModel):
    """ModifyAuditTrack response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Resource(AbstractModel):
    """Resource type

    """

    def __init__(self):
        r"""
        :param ResourceType: Resource type
        :type ResourceType: str
        :param ResourceName: Resource name
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ResourceName: str
        """
        self.ResourceType = None
        self.ResourceName = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartLoggingRequest(AbstractModel):
    """StartLogging request structure.

    """

    def __init__(self):
        r"""
        :param AuditName: Tracking set name
        :type AuditName: str
        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartLoggingResponse(AbstractModel):
    """StartLogging response structure.

    """

    def __init__(self):
        r"""
        :param IsSuccess: Whether enablement succeeded
        :type IsSuccess: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class StopLoggingRequest(AbstractModel):
    """StopLogging request structure.

    """

    def __init__(self):
        r"""
        :param AuditName: Tracking set name
        :type AuditName: str
        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopLoggingResponse(AbstractModel):
    """StopLogging response structure.

    """

    def __init__(self):
        r"""
        :param IsSuccess: Whether disablement succeeded
        :type IsSuccess: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class Storage(AbstractModel):
    """Tracking set storage information

    """

    def __init__(self):
        r"""
        :param StorageType: Storage type (Valid values: cos, cls)
        :type StorageType: str
        :param StorageRegion: Storage region
        :type StorageRegion: str
        :param StorageName: Storage name. For COS, the storage name is the custom bucket name, which can contain up to 50 lowercase letters, digits, and hyphens. It cannot contain "-APPID" and cannot start or end with a hyphen. For CLS, the storage name is the log topic ID, which can contain 1-50 characters.
        :type StorageName: str
        :param StoragePrefix: Storage directory prefix. The COS log file prefix can only contain 3-40 letters and digits.
        :type StoragePrefix: str
        """
        self.StorageType = None
        self.StorageRegion = None
        self.StorageName = None
        self.StoragePrefix = None


    def _deserialize(self, params):
        self.StorageType = params.get("StorageType")
        self.StorageRegion = params.get("StorageRegion")
        self.StorageName = params.get("StorageName")
        self.StoragePrefix = params.get("StoragePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tracks(AbstractModel):
    """Tracking set list

    """

    def __init__(self):
        r"""
        :param Name: Tracking set name
        :type Name: str
        :param ActionType: Tracking set event type (`Read`: Read; `Write`: Write; `*`: All)
        :type ActionType: str
        :param ResourceType: The product to which the tracking set event belongs, such as `cos`, or `*` that indicates all products
        :type ResourceType: str
        :param Status: Tracking set status (0: Not enabled; 1: Enabled)
        :type Status: int
        :param EventNames: The list of API names of tracking set events (`*`: All)
        :type EventNames: list of str
        :param Storage: Storage type of shipped data. Valid values: `cos`, `cls`.
        :type Storage: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        :param CreateTime: Creation time of the tracking set
        :type CreateTime: str
        :param TrackId: Tracking set ID
        :type TrackId: int
        """
        self.Name = None
        self.ActionType = None
        self.ResourceType = None
        self.Status = None
        self.EventNames = None
        self.Storage = None
        self.CreateTime = None
        self.TrackId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ActionType = params.get("ActionType")
        self.ResourceType = params.get("ResourceType")
        self.Status = params.get("Status")
        self.EventNames = params.get("EventNames")
        if params.get("Storage") is not None:
            self.Storage = Storage()
            self.Storage._deserialize(params.get("Storage"))
        self.CreateTime = params.get("CreateTime")
        self.TrackId = params.get("TrackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAuditRequest(AbstractModel):
    """UpdateAudit request structure.

    """

    def __init__(self):
        r"""
        :param AuditName: Tracking set name
        :type AuditName: str
        :param IsEnableCmqNotify: Whether to enable CMQ message notification. 1: Yes; 0: No. Only CMQ queue service is currently supported. If CMQ message notification is enabled, CloudAudit will deliver your log contents to the designated queue in the specified region in real time.
        :type IsEnableCmqNotify: int
        :param ReadWriteAttribute: Manages the read/write attribute of event. Valid values: 1 (read-only), 2 (write-only), 3 (read/write).
        :type ReadWriteAttribute: int
        :param KeyId: Globally unique ID of the CMK. This value is required if it is not a newly created KMS element. It can be obtained through `ListKeyAliasByRegion`. CloudAudit will not verify the validity of the `KeyId`. Enter it carefully to avoid data loss.
        :type KeyId: str
        :param CosRegion: COS region. Supported regions can be queried through the `ListCosEnableRegion` API.
        :type CosRegion: str
        :param CmqQueueName: Queue name, which must begin with a letter and can contain up to 64 letters, digits, and dashes (-). This field is required if the value of `IsEnableCmqNotify` is 1. If a queue is not newly created, CloudAudit will not verify whether it actually exists. Enter the name with caution to avoid log delivery failure and consequent data loss.
        :type CmqQueueName: str
        :param IsCreateNewBucket: Whether to create a COS bucket. 1: Yes; 0: No.
        :type IsCreateNewBucket: int
        :param KmsRegion: KMS region. Currently supported regions can be obtained through `ListKmsEnableRegion`. This must be the same as the COS region.
        :type KmsRegion: str
        :param IsEnableKmsEncry: Whether to enable KMS encryption. 1: Yes, 0: No. If KMS encryption is enabled, the data will be encrypted when delivered to COS.
        :type IsEnableKmsEncry: int
        :param CosBucketName: User-defined COS bucket name, which can only contain 1–40 lowercase letters (a–z), digits (0–9), and dashes (-) and cannot begin or end with "-". If a bucket is not newly created, CloudAudit will not verify whether it actually exists. Enter the name with caution to avoid log delivery failure and consequent data loss.
        :type CosBucketName: str
        :param CmqRegion: Region where the queue is located. Supported CMQ regions can be queried through the `ListCmqEnableRegion` API. This field is required if the value of `IsEnableCmqNotify` is 1.
        :type CmqRegion: str
        :param LogFilePrefix: Log file prefix, which can only contain 3–40 ASCII letters (a–z; A–Z) and digits (0–9).
        :type LogFilePrefix: str
        :param IsCreateNewQueue: Whether to create a queue. 1: Yes; 0: No. This field is required if the value of `IsEnableCmqNotify` is 1.
        :type IsCreateNewQueue: int
        """
        self.AuditName = None
        self.IsEnableCmqNotify = None
        self.ReadWriteAttribute = None
        self.KeyId = None
        self.CosRegion = None
        self.CmqQueueName = None
        self.IsCreateNewBucket = None
        self.KmsRegion = None
        self.IsEnableKmsEncry = None
        self.CosBucketName = None
        self.CmqRegion = None
        self.LogFilePrefix = None
        self.IsCreateNewQueue = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        self.IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self.ReadWriteAttribute = params.get("ReadWriteAttribute")
        self.KeyId = params.get("KeyId")
        self.CosRegion = params.get("CosRegion")
        self.CmqQueueName = params.get("CmqQueueName")
        self.IsCreateNewBucket = params.get("IsCreateNewBucket")
        self.KmsRegion = params.get("KmsRegion")
        self.IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self.CosBucketName = params.get("CosBucketName")
        self.CmqRegion = params.get("CmqRegion")
        self.LogFilePrefix = params.get("LogFilePrefix")
        self.IsCreateNewQueue = params.get("IsCreateNewQueue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAuditResponse(AbstractModel):
    """UpdateAudit response structure.

    """

    def __init__(self):
        r"""
        :param IsSuccess: Whether update succeeded
        :type IsSuccess: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")