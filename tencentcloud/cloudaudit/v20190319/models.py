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


class ConfigurationItems(AbstractModel):
    """Resource configuration items

    """

    def __init__(self):
        r"""
        :param ConfigurationItemCaptureTime: Time of getting a configuration item
        :type ConfigurationItemCaptureTime: str
        :param Relationships: Resource relationship list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Relationships: str
        :param LastItemInfo: This parameter takes effect only when `DiffMode` is set to `true`. When the input parameter `ChronologicalOrder` of the `GetConfigurationItems` API is set to `Forward`, details of the configuration item before the first one (if not a creation configuration item) will be returned. When this parameter is set to `Reverse`, details of the configuration item after the last one (if not a resource deletion configuration item) will be returned.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LastItemInfo: str
        :param RelatedEvents: List of events associated with the configuration changes
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RelatedEvents: list of RelatedEvent
        :param ResourceType: Resource type
        :type ResourceType: str
        :param ResourceId: Resource ID
        :type ResourceId: str
        :param ConfigurationStateId: Configuration item ID
        :type ConfigurationStateId: str
        :param ResourceCreateTime: Resource creation time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ResourceCreateTime: str
        :param Version: CFA version
        :type Version: str
        :param ResourceRegion: Resource region
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ResourceRegion: str
        :param Configuration: 
        :type Configuration: str
        :param ResourceAlias: Resource name
        :type ResourceAlias: str
        :param ConfigurationItemStatus: Configuration item status. Valid values: OK, ResourceDiscovered, ResourceNotRecorded, ResourceDeleted, ResourceDeletedNotRecorded.
        :type ConfigurationItemStatus: str
        """
        self.ConfigurationItemCaptureTime = None
        self.Relationships = None
        self.LastItemInfo = None
        self.RelatedEvents = None
        self.ResourceType = None
        self.ResourceId = None
        self.ConfigurationStateId = None
        self.ResourceCreateTime = None
        self.Version = None
        self.ResourceRegion = None
        self.Configuration = None
        self.ResourceAlias = None
        self.ConfigurationItemStatus = None


    def _deserialize(self, params):
        self.ConfigurationItemCaptureTime = params.get("ConfigurationItemCaptureTime")
        self.Relationships = params.get("Relationships")
        self.LastItemInfo = params.get("LastItemInfo")
        if params.get("RelatedEvents") is not None:
            self.RelatedEvents = []
            for item in params.get("RelatedEvents"):
                obj = RelatedEvent()
                obj._deserialize(item)
                self.RelatedEvents.append(obj)
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.ConfigurationStateId = params.get("ConfigurationStateId")
        self.ResourceCreateTime = params.get("ResourceCreateTime")
        self.Version = params.get("Version")
        self.ResourceRegion = params.get("ResourceRegion")
        self.Configuration = params.get("Configuration")
        self.ResourceAlias = params.get("ResourceAlias")
        self.ConfigurationItemStatus = params.get("ConfigurationItemStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecorderRequest(AbstractModel):
    """CreateRecorder request structure.

    """

    def __init__(self):
        r"""
        :param Role: Role name authorized to CFA
        :type Role: str
        :param AllSupported: Whether to select all supported resource types. Valid values: true (default), false.
        :type AllSupported: bool
        :param Enable: Whether to enable the resource recorder. Valid values: true (default), false.
        :type Enable: bool
        :param Name: Resource recorder name. Default name: default.
        :type Name: str
        """
        self.Role = None
        self.AllSupported = None
        self.Enable = None
        self.Name = None


    def _deserialize(self, params):
        self.Role = params.get("Role")
        self.AllSupported = params.get("AllSupported")
        self.Enable = params.get("Enable")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecorderResponse(AbstractModel):
    """CreateRecorder response structure.

    """

    def __init__(self):
        r"""
        :param IsSuccess: Whether the recorder was created successfully
        :type IsSuccess: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class DeleteRecorderRequest(AbstractModel):
    """DeleteRecorder request structure.

    """


class DeleteRecorderResponse(AbstractModel):
    """DeleteRecorder response structure.

    """

    def __init__(self):
        r"""
        :param IsSuccess: Whether the recorder was deleted successfully
        :type IsSuccess: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class DescribeDiscoveredResourceRequest(AbstractModel):
    """DescribeDiscoveredResource request structure.

    """

    def __init__(self):
        r"""
        :param ResourceId: Request ID
        :type ResourceId: str
        """
        self.ResourceId = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiscoveredResourceResponse(AbstractModel):
    """DescribeDiscoveredResource response structure.

    """

    def __init__(self):
        r"""
        :param LastUpdateTime: Last update time
        :type LastUpdateTime: str
        :param ResourceType: Resource type
        :type ResourceType: str
        :param ResourceId: Resource ID
        :type ResourceId: str
        :param CreateTime: Resource creation time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param Tag: Tag details
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tag: str
        :param ResourceInfo: Current resource configuration details
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ResourceInfo: str
        :param ResourceRegion: Resource region
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ResourceRegion: str
        :param ResourceAlias: Resource alias
        :type ResourceAlias: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LastUpdateTime = None
        self.ResourceType = None
        self.ResourceId = None
        self.CreateTime = None
        self.Tag = None
        self.ResourceInfo = None
        self.ResourceRegion = None
        self.ResourceAlias = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LastUpdateTime = params.get("LastUpdateTime")
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.CreateTime = params.get("CreateTime")
        self.Tag = params.get("Tag")
        self.ResourceInfo = params.get("ResourceInfo")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ResourceAlias = params.get("ResourceAlias")
        self.RequestId = params.get("RequestId")


class DescribeRecorderRequest(AbstractModel):
    """DescribeRecorder request structure.

    """


class DescribeRecorderResponse(AbstractModel):
    """DescribeRecorder response structure.

    """

    def __init__(self):
        r"""
        :param Enable: Whether to enable the recorder. Valid values: true (enable), false (disable).
        :type Enable: bool
        :param Name: Recorder name
        :type Name: str
        :param LastErrorMessage: Last error message of the recorder, which corresponds to `LastErrorCode`.
        :type LastErrorMessage: str
        :param LastStatus: The status of the recorder when it recorded information last time. Valid values: PENDING, OK, FAILED.
        :type LastStatus: str
        :param ResourceTypes: List of the resource types monitored by the recorder
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ResourceTypes: list of RecordResourceType
        :param LastStartTime: Time when the recorder was enabled last time
        :type LastStartTime: str
        :param LastErrorCode: Last error code of the recorder
        :type LastErrorCode: str
        :param LastStopTime: Time when the recorder was disabled last time
        :type LastStopTime: str
        :param AllSupported: Whether to monitor all currently supported resource types. Valid values: true (yes), false (no).
        :type AllSupported: bool
        :param CreateTime: Recorder creation time
        :type CreateTime: str
        :param Role: Role name authorized to CFA
        :type Role: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Enable = None
        self.Name = None
        self.LastErrorMessage = None
        self.LastStatus = None
        self.ResourceTypes = None
        self.LastStartTime = None
        self.LastErrorCode = None
        self.LastStopTime = None
        self.AllSupported = None
        self.CreateTime = None
        self.Role = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        self.Name = params.get("Name")
        self.LastErrorMessage = params.get("LastErrorMessage")
        self.LastStatus = params.get("LastStatus")
        if params.get("ResourceTypes") is not None:
            self.ResourceTypes = []
            for item in params.get("ResourceTypes"):
                obj = RecordResourceType()
                obj._deserialize(item)
                self.ResourceTypes.append(obj)
        self.LastStartTime = params.get("LastStartTime")
        self.LastErrorCode = params.get("LastErrorCode")
        self.LastStopTime = params.get("LastStopTime")
        self.AllSupported = params.get("AllSupported")
        self.CreateTime = params.get("CreateTime")
        self.Role = params.get("Role")
        self.RequestId = params.get("RequestId")


class GetConfigurationItemsRequest(AbstractModel):
    """GetConfigurationItems request structure.

    """

    def __init__(self):
        r"""
        :param ResourceId: Resource ID
        :type ResourceId: str
        :param ChronologicalOrder: Chronological order. Valid values: Reverse, Forward (default).
        :type ChronologicalOrder: str
        :param StartTime: Start time
        :type StartTime: str
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param DiffMode: Whether to enable `DiffMode`. Valid values: true, false (default).
        :type DiffMode: bool
        :param Limit: Returned number. default: 10, maximum: 100.
        :type Limit: int
        :param EndTime: End time
        :type EndTime: str
        """
        self.ResourceId = None
        self.ChronologicalOrder = None
        self.StartTime = None
        self.Offset = None
        self.DiffMode = None
        self.Limit = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.ChronologicalOrder = params.get("ChronologicalOrder")
        self.StartTime = params.get("StartTime")
        self.Offset = params.get("Offset")
        self.DiffMode = params.get("DiffMode")
        self.Limit = params.get("Limit")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetConfigurationItemsResponse(AbstractModel):
    """GetConfigurationItems response structure.

    """

    def __init__(self):
        r"""
        :param ConfigurationItems: Resource configuration item list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ConfigurationItems: list of ConfigurationItems
        :param TotalCount: Total number
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ConfigurationItems = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ConfigurationItems") is not None:
            self.ConfigurationItems = []
            for item in params.get("ConfigurationItems"):
                obj = ConfigurationItems()
                obj._deserialize(item)
                self.ConfigurationItems.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListDiscoveredResourcesRequest(AbstractModel):
    """ListDiscoveredResources request structure.

    """

    def __init__(self):
        r"""
        :param ResourceType: Resource type
        :type ResourceType: str
        :param ResourceId: Resource ID
        :type ResourceId: str
        :param Limit: Returned number. default: 20, maximum: 200.
        :type Limit: int
        :param ResourceRegion: Resource region
        :type ResourceRegion: str
        :param Offset: Offset. Default: 0.
        :type Offset: int
        :param IsDeleted: Whether the resource is deleted
        :type IsDeleted: bool
        """
        self.ResourceType = None
        self.ResourceId = None
        self.Limit = None
        self.ResourceRegion = None
        self.Offset = None
        self.IsDeleted = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.Limit = params.get("Limit")
        self.ResourceRegion = params.get("ResourceRegion")
        self.Offset = params.get("Offset")
        self.IsDeleted = params.get("IsDeleted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDiscoveredResourcesResponse(AbstractModel):
    """ListDiscoveredResources response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number
        :type TotalCount: int
        :param Resources: Resource list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Resources: list of Resources
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Resources = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Resources") is not None:
            self.Resources = []
            for item in params.get("Resources"):
                obj = Resources()
                obj._deserialize(item)
                self.Resources.append(obj)
        self.RequestId = params.get("RequestId")


class ListSupportResourceTypesRequest(AbstractModel):
    """ListSupportResourceTypes request structure.

    """


class ListSupportResourceTypesResponse(AbstractModel):
    """ListSupportResourceTypes response structure.

    """

    def __init__(self):
        r"""
        :param ResourceTypes: List of supported resource types
        :type ResourceTypes: list of SupportResourceType
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ResourceTypes = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResourceTypes") is not None:
            self.ResourceTypes = []
            for item in params.get("ResourceTypes"):
                obj = SupportResourceType()
                obj._deserialize(item)
                self.ResourceTypes.append(obj)
        self.RequestId = params.get("RequestId")


class RecordResourceType(AbstractModel):
    """Resource types monitored by CFA

    """

    def __init__(self):
        r"""
        :param PolicyName: CAM policy name
        :type PolicyName: str
        :param UpdateTime: Modification time of resource types for monitoring
        :type UpdateTime: str
        :param Service: Service
        :type Service: str
        :param ResourceType: Resource type
        :type ResourceType: str
        :param ServiceName: Service name
        :type ServiceName: str
        :param ResourceTypeName: Resource type name
        :type ResourceTypeName: str
        """
        self.PolicyName = None
        self.UpdateTime = None
        self.Service = None
        self.ResourceType = None
        self.ServiceName = None
        self.ResourceTypeName = None


    def _deserialize(self, params):
        self.PolicyName = params.get("PolicyName")
        self.UpdateTime = params.get("UpdateTime")
        self.Service = params.get("Service")
        self.ResourceType = params.get("ResourceType")
        self.ServiceName = params.get("ServiceName")
        self.ResourceTypeName = params.get("ResourceTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelatedEvent(AbstractModel):
    """List of associated events

    """

    def __init__(self):
        r"""
        :param EventName: Event name
        :type EventName: str
        :param EventTime: Operation time
        :type EventTime: str
        :param OperateUin: ID of the operator account
        :type OperateUin: int
        :param EventReqId: CloudAudit event ID
        :type EventReqId: str
        """
        self.EventName = None
        self.EventTime = None
        self.OperateUin = None
        self.EventReqId = None


    def _deserialize(self, params):
        self.EventName = params.get("EventName")
        self.EventTime = params.get("EventTime")
        self.OperateUin = params.get("OperateUin")
        self.EventReqId = params.get("EventReqId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Resources(AbstractModel):
    """Resource list

    """

    def __init__(self):
        r"""
        :param ResourceType: Resource type
        :type ResourceType: str
        :param ResourceId: Resource ID
        :type ResourceId: str
        :param CreateTime: Resource creation time
        :type CreateTime: str
        :param ResourceRegion: Resource region
        :type ResourceRegion: str
        :param ResourceAlias: Resource alias
        :type ResourceAlias: str
        :param IsDeleted: Whether the resource is deleted
        :type IsDeleted: bool
        """
        self.ResourceType = None
        self.ResourceId = None
        self.CreateTime = None
        self.ResourceRegion = None
        self.ResourceAlias = None
        self.IsDeleted = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.CreateTime = params.get("CreateTime")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ResourceAlias = params.get("ResourceAlias")
        self.IsDeleted = params.get("IsDeleted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SupportResourceType(AbstractModel):
    """Supported resource types

    """

    def __init__(self):
        r"""
        :param ResourceType: Resource type
        :type ResourceType: str
        :param PolicyName: CAM policy name
        :type PolicyName: str
        :param ServiceName: Service name
        :type ServiceName: str
        :param ResourceTypeName: Resource type name in Chinese
        :type ResourceTypeName: str
        :param Service: Service
        :type Service: str
        """
        self.ResourceType = None
        self.PolicyName = None
        self.ServiceName = None
        self.ResourceTypeName = None
        self.Service = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.PolicyName = params.get("PolicyName")
        self.ServiceName = params.get("ServiceName")
        self.ResourceTypeName = params.get("ResourceTypeName")
        self.Service = params.get("Service")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecorderRequest(AbstractModel):
    """UpdateRecorder request structure.

    """

    def __init__(self):
        r"""
        :param AllSupported: Whether to select all currently supported resource types
        :type AllSupported: bool
        :param Enable: Whether to enable the recorder. Valid values: true (enable), false (disable).
        :type Enable: bool
        :param Name: Recorder name after modification
        :type Name: str
        """
        self.AllSupported = None
        self.Enable = None
        self.Name = None


    def _deserialize(self, params):
        self.AllSupported = params.get("AllSupported")
        self.Enable = params.get("Enable")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecorderResponse(AbstractModel):
    """UpdateRecorder response structure.

    """

    def __init__(self):
        r"""
        :param IsSuccess: Whether the modification is successful
        :type IsSuccess: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")