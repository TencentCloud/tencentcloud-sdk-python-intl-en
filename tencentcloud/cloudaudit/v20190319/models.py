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


class AttributeKeyDetail(AbstractModel):
    """`AttributeKey` value details

    """

    def __init__(self):
        """
        :param Label: Tag
        :type Label: str
        :param LabelType: Input box type
        :type LabelType: str
        :param Order: Display sort order
        :type Order: int
        :param Starter: Initial display
        :type Starter: str
        :param Value: `AttributeKey` value
        :type Value: str
        """
        self.Label = None
        self.LabelType = None
        self.Order = None
        self.Starter = None
        self.Value = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.LabelType = params.get("LabelType")
        self.Order = params.get("Order")
        self.Starter = params.get("Starter")
        self.Value = params.get("Value")


class AuditSummary(AbstractModel):
    """Tracking set overview

    """

    def __init__(self):
        """
        :param AuditName: Tracking set name
        :type AuditName: str
        :param AuditStatus: Tracking set status. Valid values: 1: enabled, 0: disabled
        :type AuditStatus: int
        :param CosBucketName: COS bucket name
        :type CosBucketName: str
        :param LogFilePrefix: Log prefix
        :type LogFilePrefix: str
        """
        self.AuditName = None
        self.AuditStatus = None
        self.CosBucketName = None
        self.LogFilePrefix = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        self.AuditStatus = params.get("AuditStatus")
        self.CosBucketName = params.get("CosBucketName")
        self.LogFilePrefix = params.get("LogFilePrefix")


class CmqRegionInfo(AbstractModel):
    """CMQ region information

    """

    def __init__(self):
        """
        :param CmqRegion: CMQ region
        :type CmqRegion: str
        :param CmqRegionName: Region description
        :type CmqRegionName: str
        """
        self.CmqRegion = None
        self.CmqRegionName = None


    def _deserialize(self, params):
        self.CmqRegion = params.get("CmqRegion")
        self.CmqRegionName = params.get("CmqRegionName")


class CosRegionInfo(AbstractModel):
    """COS region information

    """

    def __init__(self):
        """
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


class CreateAuditRequest(AbstractModel):
    """`CreateAudit` request parameters structure

    """

    def __init__(self):
        """
        :param AuditName: Tracking set name, which can contain 3–128 ASCII letters (a–z; A–Z), digits (0–9), and underscores (_).
        :type AuditName: str
        :param CosBucketName: User-defined COS bucket name, which can only contain 1–40 lowercase letters (a–z), digits (0–9), and dashes (-) and cannot begin or end with "-". If a bucket is not newly created, CloudAudit will not verify whether it actually exists. Please enter the name with caution so as to avoid log delivery failure and consequent data loss.
        :type CosBucketName: str
        :param CosRegion: COS region. Supported regions can be queried through the `ListCosEnableRegion` API.
        :type CosRegion: str
        :param IsCreateNewBucket: Whether to create a COS bucket. Valid values: 1: yes; 0: no.
        :type IsCreateNewBucket: int
        :param IsEnableCmqNotify: Whether to enable CMQ message notification. Valid values: 1: yes; 0: no. Currently, only CMQ is supported for message queue services. If CMQ message notification is enabled, CloudAudit will deliver your log contents to the designated queue in the specified region in real time.
        :type IsEnableCmqNotify: int
        :param ReadWriteAttribute: Manages the read/write attribute of event. Valid values: 1 (read-only), 2 (write-only), 3 (read/write).
        :type ReadWriteAttribute: int
        :param CmqQueueName: Queue name, which must begin with a letter and can contain up to 64 letters, digits, and dashes (-). This field is required if the value of `IsEnableCmqNotify` is 1. If a queue is not newly created, CloudAudit will not verify whether it actually exists. Please enter the name with caution so as to avoid log delivery failure and consequent data loss.
        :type CmqQueueName: str
        :param CmqRegion: Region where the queue is located. Supported CMQ regions can be queried through the `ListCmqEnableRegion` API. This field is required if the value of `IsEnableCmqNotify` is 1.
        :type CmqRegion: str
        :param IsCreateNewQueue: Whether to create a queue. Valid values: 1: yes; 0: no. This field is required if the value of `IsEnableCmqNotify` is 1.
        :type IsCreateNewQueue: int
        :param IsEnableKmsEncry: Whether to enable KMS encryption. Valid values: 1: yes, 0: no. If KMS encryption is enabled, the data will be encrypted when delivered to COS.
        :type IsEnableKmsEncry: int
        :param KeyId: Globally unique ID of the CMK. This value is required if it is not a newly created KMS element. It can be obtained via the `ListKeyAliasByRegion` API. CloudAudit will not verify the validity of the `KeyId`. Please enter it with caution to avoid consequent data loss.
        :type KeyId: str
        :param KmsRegion: KMS region. Currently supported regions can be obtained via the `ListKmsEnableRegion` API. This must be the same as the COS region.
        :type KmsRegion: str
        :param LogFilePrefix: Log file prefix, which can only contain 3–40 ASCII letters (a–z; A–Z) and digits (0–9). It can be left empty and is set to the account ID by default.
        :type LogFilePrefix: str
        """
        self.AuditName = None
        self.CosBucketName = None
        self.CosRegion = None
        self.IsCreateNewBucket = None
        self.IsEnableCmqNotify = None
        self.ReadWriteAttribute = None
        self.CmqQueueName = None
        self.CmqRegion = None
        self.IsCreateNewQueue = None
        self.IsEnableKmsEncry = None
        self.KeyId = None
        self.KmsRegion = None
        self.LogFilePrefix = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        self.CosBucketName = params.get("CosBucketName")
        self.CosRegion = params.get("CosRegion")
        self.IsCreateNewBucket = params.get("IsCreateNewBucket")
        self.IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self.ReadWriteAttribute = params.get("ReadWriteAttribute")
        self.CmqQueueName = params.get("CmqQueueName")
        self.CmqRegion = params.get("CmqRegion")
        self.IsCreateNewQueue = params.get("IsCreateNewQueue")
        self.IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self.KeyId = params.get("KeyId")
        self.KmsRegion = params.get("KmsRegion")
        self.LogFilePrefix = params.get("LogFilePrefix")


class CreateAuditResponse(AbstractModel):
    """`CreateAudit` response parameters structure

    """

    def __init__(self):
        """
        :param IsSuccess: Indicates if the creation was successful
        :type IsSuccess: int
        :param RequestId: Unique ID of request. Each request returns a unique ID. The `RequestId` is required for troubleshooting.
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class DeleteAuditRequest(AbstractModel):
    """`DeleteAudit` request parameters structure

    """

    def __init__(self):
        """
        :param AuditName: Tracking set name
        :type AuditName: str
        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")


class DeleteAuditResponse(AbstractModel):
    """`DeleteAudit` response parameters structure

    """

    def __init__(self):
        """
        :param IsSuccess: Indicates if the deletion was successful
        :type IsSuccess: int
        :param RequestId: Unique ID of request. Each request returns a unique ID. The `RequestId` is required for troubleshooting.
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class DescribeAuditRequest(AbstractModel):
    """`DescribeAudit` request parameters structure

    """

    def __init__(self):
        """
        :param AuditName: Tracking set name
        :type AuditName: str
        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")


class DescribeAuditResponse(AbstractModel):
    """`DescribeAudit` response parameters structure

    """

    def __init__(self):
        """
        :param AuditName: Tracking set name.
        :type AuditName: str
        :param AuditStatus: Tracking set status. Valid values: 1: enabled, 0: disabled.
        :type AuditStatus: int
        :param CmqQueueName: Queue name.
        :type CmqQueueName: str
        :param CmqRegion: Queue region.
        :type CmqRegion: str
        :param CosBucketName: COS bucket name.
        :type CosBucketName: str
        :param CosRegion: COS bucket region.
        :type CosRegion: str
        :param IsEnableCmqNotify: Whether to enable CMQ message notification. Valid values: 1: yes; 0: no.
        :type IsEnableCmqNotify: int
        :param IsEnableKmsEncry: Whether to enable KMS encryption. Valid values: 1: yes, 0: no. If KMS encryption is enabled, the data will be encrypted when delivered to COS.
        :type IsEnableKmsEncry: int
        :param KeyId: Globally unique CMK ID.
        :type KeyId: str
        :param KmsAlias: CMK alias.
        :type KmsAlias: str
        :param KmsRegion: KMS region.
        :type KmsRegion: str
        :param LogFilePrefix: Log prefix.
        :type LogFilePrefix: str
        :param ReadWriteAttribute: Manages the read/write attribute of event. Valid values: 1 (read-only), 2 (write-only), 3 (read/write)
        :type ReadWriteAttribute: int
        :param RequestId: Unique ID of request. Each request returns a unique ID. The `RequestId` is required for troubleshooting.
        :type RequestId: str
        """
        self.AuditName = None
        self.AuditStatus = None
        self.CmqQueueName = None
        self.CmqRegion = None
        self.CosBucketName = None
        self.CosRegion = None
        self.IsEnableCmqNotify = None
        self.IsEnableKmsEncry = None
        self.KeyId = None
        self.KmsAlias = None
        self.KmsRegion = None
        self.LogFilePrefix = None
        self.ReadWriteAttribute = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        self.AuditStatus = params.get("AuditStatus")
        self.CmqQueueName = params.get("CmqQueueName")
        self.CmqRegion = params.get("CmqRegion")
        self.CosBucketName = params.get("CosBucketName")
        self.CosRegion = params.get("CosRegion")
        self.IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self.IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self.KeyId = params.get("KeyId")
        self.KmsAlias = params.get("KmsAlias")
        self.KmsRegion = params.get("KmsRegion")
        self.LogFilePrefix = params.get("LogFilePrefix")
        self.ReadWriteAttribute = params.get("ReadWriteAttribute")
        self.RequestId = params.get("RequestId")


class Event(AbstractModel):
    """Log details

    """

    def __init__(self):
        """
        :param Resources: Resource pair
        :type Resources: :class:`tencentcloud.cloudaudit.v20190319.models.Resource`
        :param AccountID: Root account ID
        :type AccountID: int
        :param CloudAuditEvent: Log details
        :type CloudAuditEvent: str
        :param ErrorCode: Authentication error code
        :type ErrorCode: int
        :param EventId: Log ID
        :type EventId: str
        :param EventName: Event name
        :type EventName: str
        :param EventNameCn: Chinese description of event name (please use this field as required; if you are using other languages, ignore this field)
        :type EventNameCn: str
        :param EventRegion: Event region
        :type EventRegion: str
        :param EventSource: Request source
        :type EventSource: str
        :param EventTime: Event time
        :type EventTime: str
        :param RequestID: Request ID
        :type RequestID: str
        :param ResourceRegion: Resource region
        :type ResourceRegion: str
        :param ResourceTypeCn: Chinese description of resource type (please use this field as required; if you are using other languages, ignore this field)
        :type ResourceTypeCn: str
        :param SecretId: Certificate ID
        :type SecretId: str
        :param SourceIPAddress: Source IP
        :type SourceIPAddress: str
        :param Username: Username
        :type Username: str
        """
        self.Resources = None
        self.AccountID = None
        self.CloudAuditEvent = None
        self.ErrorCode = None
        self.EventId = None
        self.EventName = None
        self.EventNameCn = None
        self.EventRegion = None
        self.EventSource = None
        self.EventTime = None
        self.RequestID = None
        self.ResourceRegion = None
        self.ResourceTypeCn = None
        self.SecretId = None
        self.SourceIPAddress = None
        self.Username = None


    def _deserialize(self, params):
        if params.get("Resources") is not None:
            self.Resources = Resource()
            self.Resources._deserialize(params.get("Resources"))
        self.AccountID = params.get("AccountID")
        self.CloudAuditEvent = params.get("CloudAuditEvent")
        self.ErrorCode = params.get("ErrorCode")
        self.EventId = params.get("EventId")
        self.EventName = params.get("EventName")
        self.EventNameCn = params.get("EventNameCn")
        self.EventRegion = params.get("EventRegion")
        self.EventSource = params.get("EventSource")
        self.EventTime = params.get("EventTime")
        self.RequestID = params.get("RequestID")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ResourceTypeCn = params.get("ResourceTypeCn")
        self.SecretId = params.get("SecretId")
        self.SourceIPAddress = params.get("SourceIPAddress")
        self.Username = params.get("Username")


class GetAttributeKeyRequest(AbstractModel):
    """`GetAttributeKey` request parameters structure

    """

    def __init__(self):
        """
        :param WebsiteType: Website type. Valid values: zh, en. If this parameter is left empty, `zh` will be used by default
        :type WebsiteType: str
        """
        self.WebsiteType = None


    def _deserialize(self, params):
        self.WebsiteType = params.get("WebsiteType")


class GetAttributeKeyResponse(AbstractModel):
    """`GetAttributeKey` response parameters structure

    """

    def __init__(self):
        """
        :param AttributeKeyDetails: Valid values range of `AttributeKey`
        :type AttributeKeyDetails: list of AttributeKeyDetail
        :param RequestId: Unique ID of request. Each request returns a unique ID. The `RequestId` is required for troubleshooting.
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
    """`InquireAuditCredit` request parameters structure

    """


class InquireAuditCreditResponse(AbstractModel):
    """`InquireAuditCredit` response parameters structure

    """

    def __init__(self):
        """
        :param AuditAmount: Number of tracking sets that can be created
        :type AuditAmount: int
        :param RequestId: Unique ID of request. Each request returns a unique ID. The `RequestId` is required for troubleshooting.
        :type RequestId: str
        """
        self.AuditAmount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AuditAmount = params.get("AuditAmount")
        self.RequestId = params.get("RequestId")


class ListAuditsRequest(AbstractModel):
    """`ListAudits` request parameters structure

    """


class ListAuditsResponse(AbstractModel):
    """`ListAudits` response parameters structure

    """

    def __init__(self):
        """
        :param AuditSummarys: Set of queried tracking set summaries
        :type AuditSummarys: list of AuditSummary
        :param RequestId: Unique ID of request. Each request returns a unique ID. The `RequestId` is required for troubleshooting.
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
    """`ListCmqEnableRegion` request parameters structure

    """

    def __init__(self):
        """
        :param WebsiteType: Website type. Valid values: zh (Chinese mainland); en (outside Chinese mainland). Default value: zh
        :type WebsiteType: str
        """
        self.WebsiteType = None


    def _deserialize(self, params):
        self.WebsiteType = params.get("WebsiteType")


class ListCmqEnableRegionResponse(AbstractModel):
    """`ListCmqEnableRegion` response parameters structure

    """

    def __init__(self):
        """
        :param EnableRegions: CloudAudit-enabled CMQ AZs
        :type EnableRegions: list of CmqRegionInfo
        :param RequestId: Unique ID of request. Each request returns a unique ID. The `RequestId` is required for troubleshooting.
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
    """`ListCosEnableRegion` request parameters structure

    """

    def __init__(self):
        """
        :param WebsiteType: Website type. Valid values: zh (Chinese mainland); en (outside Chinese mainland). Default value: zh
        :type WebsiteType: str
        """
        self.WebsiteType = None


    def _deserialize(self, params):
        self.WebsiteType = params.get("WebsiteType")


class ListCosEnableRegionResponse(AbstractModel):
    """`ListCosEnableRegion` response parameters structure

    """

    def __init__(self):
        """
        :param EnableRegions: CloudAudit-enabled COS AZs
        :type EnableRegions: list of CosRegionInfo
        :param RequestId: Unique ID of request. Each request returns a unique ID. The `RequestId` is required for troubleshooting.
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
    """`LookUpEvents` request parameters structure

    """

    def __init__(self):
        """
        :param EndTime: End time
        :type EndTime: int
        :param StartTime: Start time
        :type StartTime: int
        :param LookupAttributes: Search criteria
        :type LookupAttributes: list of LookupAttribute
        :param MaxResults: Maximum number of logs to be returned
        :type MaxResults: int
        :param Mode: CloudAudit mode. Valid values: standard, quick. Default value: standard
        :type Mode: str
        :param NextToken: Credential for viewing more logs
        :type NextToken: str
        """
        self.EndTime = None
        self.StartTime = None
        self.LookupAttributes = None
        self.MaxResults = None
        self.Mode = None
        self.NextToken = None


    def _deserialize(self, params):
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        if params.get("LookupAttributes") is not None:
            self.LookupAttributes = []
            for item in params.get("LookupAttributes"):
                obj = LookupAttribute()
                obj._deserialize(item)
                self.LookupAttributes.append(obj)
        self.MaxResults = params.get("MaxResults")
        self.Mode = params.get("Mode")
        self.NextToken = params.get("NextToken")


class LookUpEventsResponse(AbstractModel):
    """`LookUpEvents` response parameters structure

    """

    def __init__(self):
        """
        :param Events: Logset
        :type Events: list of Event
        :param ListOver: Whether the logset ends
        :type ListOver: bool
        :param NextToken: Credential for viewing more logs
        :type NextToken: str
        :param RequestId: Unique ID of request. Each request returns a unique ID. The `RequestId` is required for troubleshooting.
        :type RequestId: str
        """
        self.Events = None
        self.ListOver = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = Event()
                obj._deserialize(item)
                self.Events.append(obj)
        self.ListOver = params.get("ListOver")
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class LookupAttribute(AbstractModel):
    """Search criteria

    """

    def __init__(self):
        """
        :param AttributeKey: Valid values of `AttributeKey`: RequestId, EventName, ReadOnly, Username, ResourceType, ResourceName, AccessKeyId, EventId
        :type AttributeKey: str
        :param AttributeValue: AttributeValue
        :type AttributeValue: str
        """
        self.AttributeKey = None
        self.AttributeValue = None


    def _deserialize(self, params):
        self.AttributeKey = params.get("AttributeKey")
        self.AttributeValue = params.get("AttributeValue")


class Resource(AbstractModel):
    """Resource type

    """

    def __init__(self):
        """
        :param ResourceName: Resource name
        :type ResourceName: str
        :param ResourceType: Resource type
        :type ResourceType: str
        """
        self.ResourceName = None
        self.ResourceType = None


    def _deserialize(self, params):
        self.ResourceName = params.get("ResourceName")
        self.ResourceType = params.get("ResourceType")


class StartLoggingRequest(AbstractModel):
    """`StartLogging` request parameters structure

    """

    def __init__(self):
        """
        :param AuditName: Tracking set name
        :type AuditName: str
        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")


class StartLoggingResponse(AbstractModel):
    """`StartLogging` response parameters structure

    """

    def __init__(self):
        """
        :param IsSuccess: Indicates if the tracking set was enabled successfully
        :type IsSuccess: int
        :param RequestId: Unique ID of request. Each request returns a unique ID. The `RequestId` is required for troubleshooting.
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class StopLoggingRequest(AbstractModel):
    """`StopLogging` request parameters structure

    """

    def __init__(self):
        """
        :param AuditName: Tracking set name
        :type AuditName: str
        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")


class StopLoggingResponse(AbstractModel):
    """`StopLogging` response parameters structure

    """

    def __init__(self):
        """
        :param IsSuccess: Indicates if the tracking set was disabled successfully
        :type IsSuccess: int
        :param RequestId: Unique ID of request. Each request returns a unique ID. The `RequestId` is required for troubleshooting.
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class UpdateAuditRequest(AbstractModel):
    """`UpdateAudit` request parameters structure

    """

    def __init__(self):
        """
        :param AuditName: Tracking set name
        :type AuditName: str
        :param CmqQueueName: Queue name, which must begin with a letter and can contain up to 64 letters, digits, and dashes (-). This field is required if the value of `IsEnableCmqNotify` is 1. If a queue is not newly created, CloudAudit will not verify whether it actually exists. Please enter the name with caution so as to avoid log delivery failure and consequent data loss.
        :type CmqQueueName: str
        :param CmqRegion: Region where the queue is located. Supported CMQ regions can be queried through the `ListCmqEnableRegion` API. This field is required if the value of `IsEnableCmqNotify` is 1.
        :type CmqRegion: str
        :param CosBucketName: User-defined COS bucket name, which can only contain 1–40 lowercase letters (a–z), digits (0–9), and dashes (-) and cannot begin or end with "-". If a bucket is not newly created, CloudAudit will not verify whether it actually exists. Please enter the name with caution so as to avoid log delivery failure and consequent data loss.
        :type CosBucketName: str
        :param CosRegion: COS region. Supported regions can be queried through the `ListCosEnableRegion` API.
        :type CosRegion: str
        :param IsCreateNewBucket: Whether to create a COS bucket. Valid values: 1: yes; 0: no.
        :type IsCreateNewBucket: int
        :param IsCreateNewQueue: Whether to create a queue. Valid values: 1: yes; 0: no. This field is required if the value of `IsEnableCmqNotify` is 1.
        :type IsCreateNewQueue: int
        :param IsEnableCmqNotify: Whether to enable CMQ message notification. Valid values: 1: yes; 0: no. Currently, only CMQ is supported for message queue services. If CMQ message notification is enabled, CloudAudit will deliver your log contents to the designated queue in the specified region in real time.
        :type IsEnableCmqNotify: int
        :param IsEnableKmsEncry: Whether to enable KMS encryption. Valid values: 1: yes, 0: no. If KMS encryption is enabled, the data will be encrypted when delivered to COS.
        :type IsEnableKmsEncry: int
        :param KeyId: Globally unique ID of the CMK. This value is required if it is not a newly created KMS element. It can be obtained via the `ListKeyAliasByRegion` API. CloudAudit will not verify the validity of the `KeyId`. Please enter it with caution to avoid consequent data loss.
        :type KeyId: str
        :param KmsRegion: KMS region. Currently supported regions can be obtained via the `ListKmsEnableRegion` API. This must be the same as the COS region.
        :type KmsRegion: str
        :param LogFilePrefix: Log file prefix, which can only contain 3–40 ASCII letters (a–z; A–Z) and digits (0–9).
        :type LogFilePrefix: str
        :param ReadWriteAttribute: Manages the read/write attribute of event. Valid values: 1 (read-only), 2 (write-only), 3 (read/write).
        :type ReadWriteAttribute: int
        """
        self.AuditName = None
        self.CmqQueueName = None
        self.CmqRegion = None
        self.CosBucketName = None
        self.CosRegion = None
        self.IsCreateNewBucket = None
        self.IsCreateNewQueue = None
        self.IsEnableCmqNotify = None
        self.IsEnableKmsEncry = None
        self.KeyId = None
        self.KmsRegion = None
        self.LogFilePrefix = None
        self.ReadWriteAttribute = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        self.CmqQueueName = params.get("CmqQueueName")
        self.CmqRegion = params.get("CmqRegion")
        self.CosBucketName = params.get("CosBucketName")
        self.CosRegion = params.get("CosRegion")
        self.IsCreateNewBucket = params.get("IsCreateNewBucket")
        self.IsCreateNewQueue = params.get("IsCreateNewQueue")
        self.IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self.IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self.KeyId = params.get("KeyId")
        self.KmsRegion = params.get("KmsRegion")
        self.LogFilePrefix = params.get("LogFilePrefix")
        self.ReadWriteAttribute = params.get("ReadWriteAttribute")


class UpdateAuditResponse(AbstractModel):
    """`UpdateAudit` response parameters structure

    """

    def __init__(self):
        """
        :param IsSuccess: Indicates if the update was completed successfully
        :type IsSuccess: int
        :param RequestId: Unique ID of request. Each request returns a unique ID. The `RequestId` is required for troubleshooting.
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")