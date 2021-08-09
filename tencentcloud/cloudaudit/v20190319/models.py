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
        """
        :param ConfigurationItemCaptureTime: Time of getting a configuration item\n        :type ConfigurationItemCaptureTime: str\n        :param Relationships: Resource relationship list
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Relationships: str\n        :param LastItemInfo: This parameter takes effect only when `DiffMode` is set to `true`. When the input parameter `ChronologicalOrder` of the `GetConfigurationItems` API is set to `Forward`, details of the configuration item before the first one (if not a creation configuration item) will be returned. When this parameter is set to `Reverse`, details of the configuration item after the last one (if not a resource deletion configuration item) will be returned.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type LastItemInfo: str\n        :param RelatedEvents: List of events associated with the configuration changes
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type RelatedEvents: list of RelatedEvent\n        :param ResourceType: Resource type\n        :type ResourceType: str\n        :param ResourceId: Resource ID\n        :type ResourceId: str\n        :param ConfigurationStateId: Configuration item ID\n        :type ConfigurationStateId: str\n        :param ResourceCreateTime: Resource creation time
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ResourceCreateTime: str\n        :param Version: CFA version\n        :type Version: str\n        :param ResourceRegion: Resource region
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ResourceRegion: str\n        :param Configuration: \n        :type Configuration: str\n        :param ResourceAlias: Resource name\n        :type ResourceAlias: str\n        :param ConfigurationItemStatus: Configuration item status. Valid values: OK, ResourceDiscovered, ResourceNotRecorded, ResourceDeleted, ResourceDeletedNotRecorded.\n        :type ConfigurationItemStatus: str\n        """
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
        """
        :param Role: Role name authorized to CFA\n        :type Role: str\n        :param AllSupported: Whether to select all supported resource types. Valid values: true (default), false.\n        :type AllSupported: bool\n        :param Enable: Whether to enable the resource recorder. Valid values: true (default), false.\n        :type Enable: bool\n        :param Name: Resource recorder name. Default name: default.\n        :type Name: str\n        """
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
        """
        :param IsSuccess: Whether the recorder was created successfully\n        :type IsSuccess: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param IsSuccess: Whether the recorder was deleted successfully\n        :type IsSuccess: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class DescribeDiscoveredResourceRequest(AbstractModel):
    """DescribeDiscoveredResource request structure.

    """

    def __init__(self):
        """
        :param ResourceId: Request ID\n        :type ResourceId: str\n        """
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
        """
        :param LastUpdateTime: Last update time\n        :type LastUpdateTime: str\n        :param ResourceType: Resource type\n        :type ResourceType: str\n        :param ResourceId: Resource ID\n        :type ResourceId: str\n        :param CreateTime: Resource creation time
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type CreateTime: str\n        :param Tag: Tag details
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Tag: str\n        :param ResourceInfo: Current resource configuration details
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ResourceInfo: str\n        :param ResourceRegion: Resource region
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ResourceRegion: str\n        :param ResourceAlias: Resource alias\n        :type ResourceAlias: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Enable: Whether to enable the recorder. Valid values: true (enable), false (disable).\n        :type Enable: bool\n        :param Name: Recorder name\n        :type Name: str\n        :param LastErrorMessage: Last error message of the recorder, which corresponds to `LastErrorCode`.\n        :type LastErrorMessage: str\n        :param LastStatus: The status of the recorder when it recorded information last time. Valid values: PENDING, OK, FAILED.\n        :type LastStatus: str\n        :param ResourceTypes: List of the resource types monitored by the recorder
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ResourceTypes: list of RecordResourceType\n        :param LastStartTime: Time when the recorder was enabled last time\n        :type LastStartTime: str\n        :param LastErrorCode: Last error code of the recorder\n        :type LastErrorCode: str\n        :param LastStopTime: Time when the recorder was disabled last time\n        :type LastStopTime: str\n        :param AllSupported: Whether to monitor all currently supported resource types. Valid values: true (yes), false (no).\n        :type AllSupported: bool\n        :param CreateTime: Recorder creation time\n        :type CreateTime: str\n        :param Role: Role name authorized to CFA\n        :type Role: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ResourceId: Resource ID\n        :type ResourceId: str\n        :param ChronologicalOrder: Chronological order. Valid values: Reverse, Forward (default).\n        :type ChronologicalOrder: str\n        :param StartTime: Start time\n        :type StartTime: str\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param DiffMode: Whether to enable `DiffMode`. Valid values: true, false (default).\n        :type DiffMode: bool\n        :param Limit: Returned number. default: 10, maximum: 100.\n        :type Limit: int\n        :param EndTime: End time\n        :type EndTime: str\n        """
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
        """
        :param ConfigurationItems: Resource configuration item list
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ConfigurationItems: list of ConfigurationItems\n        :param TotalCount: Total number\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ResourceType: Resource type\n        :type ResourceType: str\n        :param ResourceId: Resource ID\n        :type ResourceId: str\n        :param Limit: Returned number. default: 20, maximum: 200.\n        :type Limit: int\n        :param ResourceRegion: Resource region\n        :type ResourceRegion: str\n        :param Offset: Offset. Default: 0.\n        :type Offset: int\n        :param IsDeleted: Whether the resource is deleted\n        :type IsDeleted: bool\n        """
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
        """
        :param TotalCount: Total number\n        :type TotalCount: int\n        :param Resources: Resource list
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Resources: list of Resources\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ResourceTypes: List of supported resource types\n        :type ResourceTypes: list of SupportResourceType\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param PolicyName: CAM policy name\n        :type PolicyName: str\n        :param UpdateTime: Modification time of resource types for monitoring\n        :type UpdateTime: str\n        :param Service: Service\n        :type Service: str\n        :param ResourceType: Resource type\n        :type ResourceType: str\n        :param ServiceName: Service name\n        :type ServiceName: str\n        :param ResourceTypeName: Resource type name\n        :type ResourceTypeName: str\n        """
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
        """
        :param EventName: Event name\n        :type EventName: str\n        :param EventTime: Operation time\n        :type EventTime: str\n        :param OperateUin: ID of the operator account\n        :type OperateUin: int\n        :param EventReqId: CloudAudit event ID\n        :type EventReqId: str\n        """
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
        """
        :param ResourceType: Resource type\n        :type ResourceType: str\n        :param ResourceId: Resource ID\n        :type ResourceId: str\n        :param CreateTime: Resource creation time\n        :type CreateTime: str\n        :param ResourceRegion: Resource region\n        :type ResourceRegion: str\n        :param ResourceAlias: Resource alias\n        :type ResourceAlias: str\n        :param IsDeleted: Whether the resource is deleted\n        :type IsDeleted: bool\n        """
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
        """
        :param ResourceType: Resource type\n        :type ResourceType: str\n        :param PolicyName: CAM policy name\n        :type PolicyName: str\n        :param ServiceName: Service name\n        :type ServiceName: str\n        :param ResourceTypeName: Resource type name in Chinese\n        :type ResourceTypeName: str\n        :param Service: Service\n        :type Service: str\n        """
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
        """
        :param AllSupported: Whether to select all currently supported resource types\n        :type AllSupported: bool\n        :param Enable: Whether to enable the recorder. Valid values: true (enable), false (disable).\n        :type Enable: bool\n        :param Name: Recorder name after modification\n        :type Name: str\n        """
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
        """
        :param IsSuccess: Whether the modification is successful\n        :type IsSuccess: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")