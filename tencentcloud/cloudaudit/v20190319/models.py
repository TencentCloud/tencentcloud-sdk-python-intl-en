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
        :param LookupAttributes: Search criterion. Valid values: RequestId, EventName, ActionType (write/read), PrincipalId (sub-account), ResourceType, ResourceName, AccessKeyId, SensitiveAction, ApiErrorCode, and CamErrorCode.
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
        :param ListOver: Whether the logset ends.
        :type ListOver: bool
        :param NextToken: Credential for viewing more logs.
        :type NextToken: int
        :param Events: Logset.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Events: list of Event
        :param TotalCount: Total number of events.
Note: this field may return `null`, indicating that no valid values can be obtained.
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
        