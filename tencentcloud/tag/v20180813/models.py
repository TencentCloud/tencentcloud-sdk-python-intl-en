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


class AddResourceTagRequest(AbstractModel):
    """AddResourceTag request structure.

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key.
        :type TagKey: str
        :param TagValue: Tag value.
        :type TagValue: str
        :param Resource: [Six-segment resource description](https://intl.cloud.tencent.com/document/product/598/10606?from_cn_redirect=1)
        :type Resource: str
        """
        self.TagKey = None
        self.TagValue = None
        self.Resource = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.Resource = params.get("Resource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddResourceTagResponse(AbstractModel):
    """AddResourceTag response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachResourcesTagRequest(AbstractModel):
    """AttachResourcesTag request structure.

    """

    def __init__(self):
        r"""
        :param ServiceType: Resource service name (the third segment in the six-segment resource description)
        :type ServiceType: str
        :param ResourceIds: Resource ID array, which can contain up to 50 resources
        :type ResourceIds: list of str
        :param TagKey: Tag key
        :type TagKey: str
        :param TagValue: Tag value
        :type TagValue: str
        :param ResourceRegion: Resource region. If resources have the region attribute, this field is required; otherwise, it is optional.
        :type ResourceRegion: str
        :param ResourcePrefix: Resource prefix (the part before "/" in the last segment in the six-segment resource description), which is optional for COS buckets but required for other Tencent Cloud resources.
        :type ResourcePrefix: str
        """
        self.ServiceType = None
        self.ResourceIds = None
        self.TagKey = None
        self.TagValue = None
        self.ResourceRegion = None
        self.ResourcePrefix = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.ResourceIds = params.get("ResourceIds")
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ResourcePrefix = params.get("ResourcePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachResourcesTagResponse(AbstractModel):
    """AttachResourcesTag response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTagRequest(AbstractModel):
    """CreateTag request structure.

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key.
        :type TagKey: str
        :param TagValue: Tag value.
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTagResponse(AbstractModel):
    """CreateTag response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTagsRequest(AbstractModel):
    """CreateTags request structure.

    """

    def __init__(self):
        r"""
        :param Tags: Tag list.
Value range of N: 0–9
        :type Tags: list of Tag
        """
        self.Tags = None


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTagsResponse(AbstractModel):
    """CreateTags response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteResourceTagRequest(AbstractModel):
    """DeleteResourceTag request structure.

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key.
        :type TagKey: str
        :param Resource: [Six-segment resource description](https://intl.cloud.tencent.com/document/product/598/10606?from_cn_redirect=1)
        :type Resource: str
        """
        self.TagKey = None
        self.Resource = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.Resource = params.get("Resource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteResourceTagResponse(AbstractModel):
    """DeleteResourceTag response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTagRequest(AbstractModel):
    """DeleteTag request structure.

    """

    def __init__(self):
        r"""
        :param TagKey: The tag key to be deleted.
        :type TagKey: str
        :param TagValue: The tag value to be deleted.
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTagResponse(AbstractModel):
    """DeleteTag response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTagsRequest(AbstractModel):
    """DeleteTags request structure.

    """

    def __init__(self):
        r"""
        :param Tags: Tag list.
Value range of N: 0–9
        :type Tags: list of Tag
        """
        self.Tags = None


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTagsResponse(AbstractModel):
    """DeleteTags response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeResourceTagsByResourceIdsRequest(AbstractModel):
    """DescribeResourceTagsByResourceIds request structure.

    """

    def __init__(self):
        r"""
        :param ServiceType: Service type.
        :type ServiceType: str
        :param ResourcePrefix: Resource prefix.
        :type ResourcePrefix: str
        :param ResourceIds: Array of resource IDs (up to 50)
        :type ResourceIds: list of str
        :param ResourceRegion: The resource's region.
        :type ResourceRegion: str
        :param Offset: Data offset. The default value is 0. Must be an integral multiple of the `Limit` parameter.
        :type Offset: int
        :param Limit: Page size. The default value is 0.
        :type Limit: int
        """
        self.ServiceType = None
        self.ResourcePrefix = None
        self.ResourceIds = None
        self.ResourceRegion = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceIds = params.get("ResourceIds")
        self.ResourceRegion = params.get("ResourceRegion")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsByResourceIdsResponse(AbstractModel):
    """DescribeResourceTagsByResourceIds response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of results.
        :type TotalCount: int
        :param Offset: Data offset.
        :type Offset: int
        :param Limit: Page size.
        :type Limit: int
        :param Tags: Tag list.
        :type Tags: list of TagResource
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagResource()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceTagsByResourceIdsSeqRequest(AbstractModel):
    """DescribeResourceTagsByResourceIdsSeq request structure.

    """

    def __init__(self):
        r"""
        :param ServiceType: Service type
        :type ServiceType: str
        :param ResourcePrefix: Resource prefix
        :type ResourcePrefix: str
        :param ResourceIds: Unique resource ID
        :type ResourceIds: list of str
        :param ResourceRegion: Resource region
        :type ResourceRegion: str
        :param Offset: Data offset. Default value: 0. It must be an integer multiple of the `Limit` parameter
        :type Offset: int
        :param Limit: Number of entries per page. Default value: 15
        :type Limit: int
        """
        self.ServiceType = None
        self.ResourcePrefix = None
        self.ResourceIds = None
        self.ResourceRegion = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceIds = params.get("ResourceIds")
        self.ResourceRegion = params.get("ResourceRegion")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsByResourceIdsSeqResponse(AbstractModel):
    """DescribeResourceTagsByResourceIdsSeq response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of results
        :type TotalCount: int
        :param Offset: Data offset
        :type Offset: int
        :param Limit: Number of entries per page
        :type Limit: int
        :param Tags: Tag list
        :type Tags: list of TagResource
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagResource()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceTagsByTagKeysRequest(AbstractModel):
    """DescribeResourceTagsByTagKeys request structure.

    """

    def __init__(self):
        r"""
        :param ServiceType: Service type
        :type ServiceType: str
        :param ResourcePrefix: Resource prefix
        :type ResourcePrefix: str
        :param ResourceRegion: Resource region
        :type ResourceRegion: str
        :param ResourceIds: Unique resource ID
        :type ResourceIds: list of str
        :param TagKeys: Resource tag key
        :type TagKeys: list of str
        :param Limit: Number of entries per page. Default value: 400
        :type Limit: int
        :param Offset: Data offset. Default value: 0. It must be an integer multiple of the `Limit` parameter
        :type Offset: int
        """
        self.ServiceType = None
        self.ResourcePrefix = None
        self.ResourceRegion = None
        self.ResourceIds = None
        self.TagKeys = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ResourceIds = params.get("ResourceIds")
        self.TagKeys = params.get("TagKeys")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsByTagKeysResponse(AbstractModel):
    """DescribeResourceTagsByTagKeys response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of results
        :type TotalCount: int
        :param Offset: Data offset
        :type Offset: int
        :param Limit: Number of entries per page
        :type Limit: int
        :param Rows: Resource tag
        :type Rows: list of ResourceIdTag
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = ResourceIdTag()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceTagsRequest(AbstractModel):
    """DescribeResourceTags request structure.

    """

    def __init__(self):
        r"""
        :param CreateUin: Creator `uin`
        :type CreateUin: int
        :param ResourceRegion: Resource region.
        :type ResourceRegion: str
        :param ServiceType: Service type.
        :type ServiceType: str
        :param ResourcePrefix: Resource prefix
        :type ResourcePrefix: str
        :param ResourceId: Unique resource ID. Queries with `ResourceId` only may be slow or fail to return results. We recommend you also enter `ServiceType`, `ResourcePrefix`, and `ResourceRegion` (which can be ignored for resources that don't have the region attribute) when entering `ResourceId`.
        :type ResourceId: str
        :param Offset: Data offset. Default value: 0. It must be an integer multiple of the `Limit` parameter
        :type Offset: int
        :param Limit: Number of entries per page. Default value: 15
        :type Limit: int
        :param CosResourceId: Whether it is a COS resource (0 or 1). This parameter is required when the entered `ResourceId` is a COS resource.
        :type CosResourceId: int
        """
        self.CreateUin = None
        self.ResourceRegion = None
        self.ServiceType = None
        self.ResourcePrefix = None
        self.ResourceId = None
        self.Offset = None
        self.Limit = None
        self.CosResourceId = None


    def _deserialize(self, params):
        self.CreateUin = params.get("CreateUin")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ServiceType = params.get("ServiceType")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceId = params.get("ResourceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CosResourceId = params.get("CosResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsResponse(AbstractModel):
    """DescribeResourceTags response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of results
        :type TotalCount: int
        :param Offset: Data offset.
        :type Offset: int
        :param Limit: Number of entries per page.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Limit: int
        :param Rows: Resource tag
        :type Rows: list of TagResource
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = TagResource()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourcesByTagsRequest(AbstractModel):
    """DescribeResourcesByTags request structure.

    """

    def __init__(self):
        r"""
        :param TagFilters: Tag filtering arrays.
        :type TagFilters: list of TagFilter
        :param CreateUin: Tag creator uin.
        :type CreateUin: int
        :param Offset: Data offset. The default value is 0. Must be an integral multiple of the `Limit` parameter.
        :type Offset: int
        :param Limit: Page size. The default value is 15.
        :type Limit: int
        :param ResourcePrefix: Resource prefix.
        :type ResourcePrefix: str
        :param ResourceId: Unique resource ID.
        :type ResourceId: str
        :param ResourceRegion: The resource's region.
        :type ResourceRegion: str
        :param ServiceType: Service type.
        :type ServiceType: str
        """
        self.TagFilters = None
        self.CreateUin = None
        self.Offset = None
        self.Limit = None
        self.ResourcePrefix = None
        self.ResourceId = None
        self.ResourceRegion = None
        self.ServiceType = None


    def _deserialize(self, params):
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        self.CreateUin = params.get("CreateUin")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceId = params.get("ResourceId")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ServiceType = params.get("ServiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByTagsResponse(AbstractModel):
    """DescribeResourcesByTags response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of results.
        :type TotalCount: int
        :param Offset: Data offset.
        :type Offset: int
        :param Limit: Number of entries per page.
Note: This field may return null, indicating that no valid value is found.
        :type Limit: int
        :param Rows: Resource tag.
        :type Rows: list of ResourceTag
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourcesByTagsUnionRequest(AbstractModel):
    """DescribeResourcesByTagsUnion request structure.

    """

    def __init__(self):
        r"""
        :param TagFilters: Tag filtering arrays.
        :type TagFilters: list of TagFilter
        :param CreateUin: Tag creator uin.
        :type CreateUin: int
        :param Offset: Data offset. The default value is 0. Must be an integral multiple of the `Limit` parameter.
        :type Offset: int
        :param Limit: Page size. The default value is 15.
        :type Limit: int
        :param ResourcePrefix: Resource prefix.
        :type ResourcePrefix: str
        :param ResourceId: Unique resource ID.
        :type ResourceId: str
        :param ResourceRegion: The resource’s region.
        :type ResourceRegion: str
        :param ServiceType: Service type
        :type ServiceType: str
        """
        self.TagFilters = None
        self.CreateUin = None
        self.Offset = None
        self.Limit = None
        self.ResourcePrefix = None
        self.ResourceId = None
        self.ResourceRegion = None
        self.ServiceType = None


    def _deserialize(self, params):
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        self.CreateUin = params.get("CreateUin")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceId = params.get("ResourceId")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ServiceType = params.get("ServiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByTagsUnionResponse(AbstractModel):
    """DescribeResourcesByTagsUnion response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of results.
        :type TotalCount: int
        :param Offset: Data offset.
        :type Offset: int
        :param Limit: The size of each page.
        :type Limit: int
        :param Rows: Resource tag.
        :type Rows: list of ResourceTag
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagKeysRequest(AbstractModel):
    """DescribeTagKeys request structure.

    """

    def __init__(self):
        r"""
        :param CreateUin: Creator `Uin`. If not specified, `Uin` is only used as the query condition.
        :type CreateUin: int
        :param Offset: Data offset. The default value is 0. Must be an integral multiple of the `Limit` parameter.
        :type Offset: int
        :param Limit: Page size. The default value is 0.
        :type Limit: int
        :param ShowProject: Whether to show project
        :type ShowProject: int
        """
        self.CreateUin = None
        self.Offset = None
        self.Limit = None
        self.ShowProject = None


    def _deserialize(self, params):
        self.CreateUin = params.get("CreateUin")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ShowProject = params.get("ShowProject")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagKeysResponse(AbstractModel):
    """DescribeTagKeys response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of results.
        :type TotalCount: int
        :param Offset: Data offset.
        :type Offset: int
        :param Limit: Page size.
        :type Limit: int
        :param Tags: Tag list.
        :type Tags: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Tags = params.get("Tags")
        self.RequestId = params.get("RequestId")


class DescribeTagValuesRequest(AbstractModel):
    """DescribeTagValues request structure.

    """

    def __init__(self):
        r"""
        :param TagKeys: Tag key list.
        :type TagKeys: list of str
        :param CreateUin: Creator `Uin`. If not specified, `Uin` is only used as the query condition.
        :type CreateUin: int
        :param Offset: Data offset. The default value is 0. Must be an integral multiple of the `Limit` parameter.
        :type Offset: int
        :param Limit: Page size. The default value is 0.
        :type Limit: int
        """
        self.TagKeys = None
        self.CreateUin = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TagKeys = params.get("TagKeys")
        self.CreateUin = params.get("CreateUin")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagValuesResponse(AbstractModel):
    """DescribeTagValues response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of results.
        :type TotalCount: int
        :param Offset: Data offset.
        :type Offset: int
        :param Limit: Page size.
        :type Limit: int
        :param Tags: Tag list.
        :type Tags: list of Tag
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagValuesSeqRequest(AbstractModel):
    """DescribeTagValuesSeq request structure.

    """

    def __init__(self):
        r"""
        :param TagKeys: Tag key list
        :type TagKeys: list of str
        :param CreateUin: Creator `Uin`. If this parameter is blank or left empty, only `Uin` will be used as a condition for query
        :type CreateUin: int
        :param Offset: Data offset. Default value: 0. It must be an integer multiple of the `Limit` parameter
        :type Offset: int
        :param Limit: Number of entries per page. Default value: 15
        :type Limit: int
        """
        self.TagKeys = None
        self.CreateUin = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TagKeys = params.get("TagKeys")
        self.CreateUin = params.get("CreateUin")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagValuesSeqResponse(AbstractModel):
    """DescribeTagValuesSeq response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of results
        :type TotalCount: int
        :param Offset: Data offset
        :type Offset: int
        :param Limit: Number of entries per page
        :type Limit: int
        :param Tags: Tag list
        :type Tags: list of Tag
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagsRequest(AbstractModel):
    """DescribeTags request structure.

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key. Either exists or does not exist alongside the tag value. If it does not exist, all of the user's tags will be queried.
        :type TagKey: str
        :param TagValue: Tag value. Either exists or does not exist alongside the tag key. If it does not exist, all of the user's tags will be queried.
        :type TagValue: str
        :param Offset: Data offset. The default value is 0. Must be an integral multiple of the `Limit` parameter.
        :type Offset: int
        :param Limit: Page size. The default value is 0.
        :type Limit: int
        :param CreateUin: Creator `Uin`. If not specified, `Uin` is only used as the query condition.
        :type CreateUin: int
        :param TagKeys: Tag key array, which either exists or does not exist with the tag value. If it does not exist, all tags of the user will be queried. If it is passed in together with `TagKey`, it will be used and the `TagKey` will be ignored.
        :type TagKeys: list of str
        :param ShowProject: Whether to show project tag
        :type ShowProject: int
        """
        self.TagKey = None
        self.TagValue = None
        self.Offset = None
        self.Limit = None
        self.CreateUin = None
        self.TagKeys = None
        self.ShowProject = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CreateUin = params.get("CreateUin")
        self.TagKeys = params.get("TagKeys")
        self.ShowProject = params.get("ShowProject")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsResponse(AbstractModel):
    """DescribeTags response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of results.
        :type TotalCount: int
        :param Offset: Data offset.
        :type Offset: int
        :param Limit: Page size.
        :type Limit: int
        :param Tags: Tag list.
        :type Tags: list of TagWithDelete
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagWithDelete()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagsSeqRequest(AbstractModel):
    """DescribeTagsSeq request structure.

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key, which either exists or does not exist with the tag value. If it does not exist, all tags of the user will be queried
        :type TagKey: str
        :param TagValue: Tag value, which either exists or does not exist with the tag key. If it does not exist, all tags of the user will be queried
        :type TagValue: str
        :param Offset: Data offset. Default value: 0. It must be an integer multiple of the `Limit` parameter
        :type Offset: int
        :param Limit: Number of entries per page. Default value: 15
        :type Limit: int
        :param CreateUin: Creator `Uin`. If this parameter is blank or left empty, only `Uin` will be used as a condition for query
        :type CreateUin: int
        :param TagKeys: Tag key array, which either exists or does not exist with the tag value. If it does not exist, all tags of the user will be queried. If it is passed in together with `TagKey`, it will be used and the `TagKey` will be ignored.
        :type TagKeys: list of str
        :param ShowProject: Whether to show project tag
        :type ShowProject: int
        """
        self.TagKey = None
        self.TagValue = None
        self.Offset = None
        self.Limit = None
        self.CreateUin = None
        self.TagKeys = None
        self.ShowProject = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CreateUin = params.get("CreateUin")
        self.TagKeys = params.get("TagKeys")
        self.ShowProject = params.get("ShowProject")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsSeqResponse(AbstractModel):
    """DescribeTagsSeq response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of results
        :type TotalCount: int
        :param Offset: Data offset
        :type Offset: int
        :param Limit: Number of entries per page
        :type Limit: int
        :param Tags: Tag list
        :type Tags: list of TagWithDelete
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagWithDelete()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DetachResourcesTagRequest(AbstractModel):
    """DetachResourcesTag request structure.

    """

    def __init__(self):
        r"""
        :param ServiceType: Resource service name (the third segment in the six-segment resource description)
        :type ServiceType: str
        :param ResourceIds: Resource ID array, which can contain up to 50 resources
        :type ResourceIds: list of str
        :param TagKey: Tag key to be unbound
        :type TagKey: str
        :param ResourceRegion: Resource region. If resources have the region attribute, this field is required; otherwise, it is optional.
        :type ResourceRegion: str
        :param ResourcePrefix: Resource prefix (the part before "/" in the last segment in the six-segment resource description), which is optional for COS buckets but required for other Tencent Cloud resources.
        :type ResourcePrefix: str
        """
        self.ServiceType = None
        self.ResourceIds = None
        self.TagKey = None
        self.ResourceRegion = None
        self.ResourcePrefix = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.ResourceIds = params.get("ResourceIds")
        self.TagKey = params.get("TagKey")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ResourcePrefix = params.get("ResourcePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachResourcesTagResponse(AbstractModel):
    """DetachResourcesTag response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class FailedResource(AbstractModel):
    """Information of failed resources.
    This is returned when resource tag binding or unbinding fails.

    """

    def __init__(self):
        r"""
        :param Resource: Six-segment descriptions of failed resources
        :type Resource: str
        :param Code: Error code
        :type Code: str
        :param Message: Error message
        :type Message: str
        """
        self.Resource = None
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetResourcesRequest(AbstractModel):
    """GetResources request structure.

    """

    def __init__(self):
        r"""
        :param ResourceList: Six-segment resource description list. Tencent Cloud uses a six-segment value to describe a resource.
For example, ResourceList.1 = qcs::${ServiceType}:${Region}:${Account}:${ResourcePreifx}/${ResourceId}.
If this parameter is passed in, the list of all matching resources will be returned, and the specified `MaxResults` will become invalid.
Value range of N: 0–9
        :type ResourceList: list of str
        :param TagFilters: Tag key and value.
If multiple tags are specified, resources bound to all such tags will be queried.
Value range of N: 0–5
There can be up to 10 `TagValues` in each `TagFilters`.
        :type TagFilters: list of TagFilter
        :param PaginationToken: The token value of the next page obtained from the response of the previous page.
Leave it empty for the first request.
        :type PaginationToken: str
        :param MaxResults: Number of data entries to return per page (up to 200).
Default value: 50.
        :type MaxResults: int
        """
        self.ResourceList = None
        self.TagFilters = None
        self.PaginationToken = None
        self.MaxResults = None


    def _deserialize(self, params):
        self.ResourceList = params.get("ResourceList")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        self.PaginationToken = params.get("PaginationToken")
        self.MaxResults = params.get("MaxResults")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetResourcesResponse(AbstractModel):
    """GetResources response structure.

    """

    def __init__(self):
        r"""
        :param PaginationToken: Token value obtained for the next page
        :type PaginationToken: str
        :param ResourceTagMappingList: List of resources and their associated tags (key-value pairs)
        :type ResourceTagMappingList: list of ResourceTagMapping
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PaginationToken = None
        self.ResourceTagMappingList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PaginationToken = params.get("PaginationToken")
        if params.get("ResourceTagMappingList") is not None:
            self.ResourceTagMappingList = []
            for item in params.get("ResourceTagMappingList"):
                obj = ResourceTagMapping()
                obj._deserialize(item)
                self.ResourceTagMappingList.append(obj)
        self.RequestId = params.get("RequestId")


class GetTagKeysRequest(AbstractModel):
    """GetTagKeys request structure.

    """

    def __init__(self):
        r"""
        :param PaginationToken: The token value of the next page obtained from the response of the previous page.
Leave it empty for the first request.
        :type PaginationToken: str
        :param MaxResults: Number of data entries to return per page (up to 1,000).
Default value: 50.
        :type MaxResults: int
        """
        self.PaginationToken = None
        self.MaxResults = None


    def _deserialize(self, params):
        self.PaginationToken = params.get("PaginationToken")
        self.MaxResults = params.get("MaxResults")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTagKeysResponse(AbstractModel):
    """GetTagKeys response structure.

    """

    def __init__(self):
        r"""
        :param PaginationToken: Token value obtained for the next page
        :type PaginationToken: str
        :param TagKeys: Tag key information.
        :type TagKeys: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PaginationToken = None
        self.TagKeys = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PaginationToken = params.get("PaginationToken")
        self.TagKeys = params.get("TagKeys")
        self.RequestId = params.get("RequestId")


class GetTagValuesRequest(AbstractModel):
    """GetTagValues request structure.

    """

    def __init__(self):
        r"""
        :param TagKeys: Tag key.
All tag values corresponding to the list of tag keys.
Maximum length: 20
        :type TagKeys: list of str
        :param PaginationToken: The token value of the next page obtained from the response of the previous page.
Leave it empty for the first request.
        :type PaginationToken: str
        :param MaxResults: Number of data entries to return per page (up to 1,000).
Default value: 50.
        :type MaxResults: int
        """
        self.TagKeys = None
        self.PaginationToken = None
        self.MaxResults = None


    def _deserialize(self, params):
        self.TagKeys = params.get("TagKeys")
        self.PaginationToken = params.get("PaginationToken")
        self.MaxResults = params.get("MaxResults")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTagValuesResponse(AbstractModel):
    """GetTagValues response structure.

    """

    def __init__(self):
        r"""
        :param PaginationToken: Token value obtained for the next page
        :type PaginationToken: str
        :param Tags: Tag list.
        :type Tags: list of Tag
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PaginationToken = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PaginationToken = params.get("PaginationToken")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class GetTagsRequest(AbstractModel):
    """GetTags request structure.

    """

    def __init__(self):
        r"""
        :param PaginationToken: The token value of the next page obtained from the response of the previous page.
Leave it empty for the first request.
        :type PaginationToken: str
        :param MaxResults: Number of data entries to return per page (up to 1,000).
Default value: 50.
        :type MaxResults: int
        :param TagKeys: Tag key.
All tags corresponding to the list of tag keys.
Maximum length: 20
        :type TagKeys: list of str
        """
        self.PaginationToken = None
        self.MaxResults = None
        self.TagKeys = None


    def _deserialize(self, params):
        self.PaginationToken = params.get("PaginationToken")
        self.MaxResults = params.get("MaxResults")
        self.TagKeys = params.get("TagKeys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTagsResponse(AbstractModel):
    """GetTags response structure.

    """

    def __init__(self):
        r"""
        :param PaginationToken: Token value obtained for the next page
        :type PaginationToken: str
        :param Tags: Tag list.
        :type Tags: list of Tag
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PaginationToken = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PaginationToken = params.get("PaginationToken")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyResourceTagsRequest(AbstractModel):
    """ModifyResourceTags request structure.

    """

    def __init__(self):
        r"""
        :param Resource: [Six-segment resource description](https://intl.cloud.tencent.com/document/product/598/10606?from_cn_redirect=1)
        :type Resource: str
        :param ReplaceTags: The tags to be added or modified. If the resource described by `Resource` is not associated with the input tag keys, an association will be added. If the tag keys are already associated, the values corresponding to the associated tag keys will be modified to the input values. This API must contain either `ReplaceTags` or `DeleteTag`, and these two parameters cannot include the same tag keys. This parameter can be omitted, but it cannot be an empty array.
        :type ReplaceTags: list of Tag
        :param DeleteTags: The tags to be disassociated. This API must contain either `ReplaceTags` or `DeleteTag`, and these two parameters cannot include the same tag keys. This parameter can be omitted, but it cannot be an empty array.
        :type DeleteTags: list of TagKeyObject
        """
        self.Resource = None
        self.ReplaceTags = None
        self.DeleteTags = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("ReplaceTags") is not None:
            self.ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = Tag()
                obj._deserialize(item)
                self.ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self.DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagKeyObject()
                obj._deserialize(item)
                self.DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceTagsResponse(AbstractModel):
    """ModifyResourceTags response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyResourcesTagValueRequest(AbstractModel):
    """ModifyResourcesTagValue request structure.

    """

    def __init__(self):
        r"""
        :param ServiceType: Resource service name (the third segment in the six-segment resource description)
        :type ServiceType: str
        :param ResourceIds: Resource ID array, which can contain up to 50 resources
        :type ResourceIds: list of str
        :param TagKey: Tag key
        :type TagKey: str
        :param TagValue: Tag value
        :type TagValue: str
        :param ResourceRegion: Resource region. If resources have the region attribute, this field is required; otherwise, it is optional.
        :type ResourceRegion: str
        :param ResourcePrefix: Resource prefix (the part before "/" in the last segment in the six-segment resource description), which is optional for COS buckets but required for other Tencent Cloud resources.
        :type ResourcePrefix: str
        """
        self.ServiceType = None
        self.ResourceIds = None
        self.TagKey = None
        self.TagValue = None
        self.ResourceRegion = None
        self.ResourcePrefix = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.ResourceIds = params.get("ResourceIds")
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ResourcePrefix = params.get("ResourcePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourcesTagValueResponse(AbstractModel):
    """ModifyResourcesTagValue response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceIdTag(AbstractModel):
    """Resource tag key value

    """

    def __init__(self):
        r"""
        :param ResourceId: Unique resource ID
Note: this field may return null, indicating that no valid values can be obtained
        :type ResourceId: str
        :param TagKeyValues: Tag key-value pair
Note: this field may return null, indicating that no valid values can be obtained
        :type TagKeyValues: list of Tag
        """
        self.ResourceId = None
        self.TagKeyValues = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        if params.get("TagKeyValues") is not None:
            self.TagKeyValues = []
            for item in params.get("TagKeyValues"):
                obj = Tag()
                obj._deserialize(item)
                self.TagKeyValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceTag(AbstractModel):
    """Resource tag.

    """

    def __init__(self):
        r"""
        :param ResourceRegion: The resource's region.
Note: This field may return null, indicating that no valid value is found.
        :type ResourceRegion: str
        :param ServiceType: Service type.
Note: This field may return null, indicating that no valid value is found.
        :type ServiceType: str
        :param ResourcePrefix: Resource prefix.
Note: This field may return null, indicating that no valid value is found.
        :type ResourcePrefix: str
        :param ResourceId: Unique resource ID.
Note: This field may return null, indicating that no valid value is found.
        :type ResourceId: str
        :param Tags: Resource tag.
Note: This field may return null, indicating that no valid value is found.
        :type Tags: list of Tag
        """
        self.ResourceRegion = None
        self.ServiceType = None
        self.ResourcePrefix = None
        self.ResourceId = None
        self.Tags = None


    def _deserialize(self, params):
        self.ResourceRegion = params.get("ResourceRegion")
        self.ServiceType = params.get("ServiceType")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceId = params.get("ResourceId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceTagMapping(AbstractModel):
    """Resources and their associated tags (key-value pairs).

    """

    def __init__(self):
        r"""
        :param Resource: Six-segment resource description. Tencent Cloud uses a six-segment value to describe a resource.
For example, ResourceList.1 = qcs::${ServiceType}:${Region}:${Account}:${ResourcePreifx}/${ResourceId}.
        :type Resource: str
        :param Tags: List of tags associated with the resource
        :type Tags: list of Tag
        """
        self.Resource = None
        self.Tags = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """A tag key-value pair.

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key.
        :type TagKey: str
        :param TagValue: Tag value.
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """Tag filtering array. '**AND**' relation if multiple arrays.

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key.
        :type TagKey: str
        :param TagValue: Tag value array. '**OR**' relation if multiple values.
        :type TagValue: list of str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagKeyObject(AbstractModel):
    """Tag key object.

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key.
        :type TagKey: str
        """
        self.TagKey = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagResource(AbstractModel):
    """Tag key-value pair and resource ID.

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key.
        :type TagKey: str
        :param TagValue: Tag value.
        :type TagValue: str
        :param ResourceId: Resource ID.
        :type ResourceId: str
        :param TagKeyMd5: Tag key MD5 value.
        :type TagKeyMd5: str
        :param TagValueMd5: Tag value MD5 value.
        :type TagValueMd5: str
        :param ServiceType: Resource type
Note: this field may return null, indicating that no valid values found.
        :type ServiceType: str
        """
        self.TagKey = None
        self.TagValue = None
        self.ResourceId = None
        self.TagKeyMd5 = None
        self.TagValueMd5 = None
        self.ServiceType = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.ResourceId = params.get("ResourceId")
        self.TagKeyMd5 = params.get("TagKeyMd5")
        self.TagValueMd5 = params.get("TagValueMd5")
        self.ServiceType = params.get("ServiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagResourcesRequest(AbstractModel):
    """TagResources request structure.

    """

    def __init__(self):
        r"""
        :param ResourceList: Six-segment resource description list. Tencent Cloud uses a six-segment value to describe a resource. For more information, see [CAM](https://intl.cloud.tencent.com/document/product/598/67350?from_cn_redirect=1) > Overview > API List > Six-Segment Resource Information.
For example, ResourceList.1 = qcs::${ServiceType}:${Region}:${Account}:${ResourcePreifx}/${ResourceId}.
Value range of N: 0–9
        :type ResourceList: list of str
        :param Tags: Tag key and value.
If multiple tags are specified, all such tags will be created and bound to the specified resources.
For each resource, each tag key can have only one value. If you try to add an existing tag key, the corresponding tag value will be updated to the new value.
Non-existent tags will be automatically created.
Value range of N: 0–9
        :type Tags: list of Tag
        """
        self.ResourceList = None
        self.Tags = None


    def _deserialize(self, params):
        self.ResourceList = params.get("ResourceList")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagResourcesResponse(AbstractModel):
    """TagResources response structure.

    """

    def __init__(self):
        r"""
        :param FailedResources: Information of failed resources.
When tag creating and binding succeeds, the returned `FailedResources` will be empty.
When tag creating and binding partially or completely fails, the returned `FailedResources` will display the details of failed resources.
        :type FailedResources: list of FailedResource
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FailedResources = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FailedResources") is not None:
            self.FailedResources = []
            for item in params.get("FailedResources"):
                obj = FailedResource()
                obj._deserialize(item)
                self.FailedResources.append(obj)
        self.RequestId = params.get("RequestId")


class TagWithDelete(AbstractModel):
    """A tag key-value pair and if deletion is allowed.

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key.
        :type TagKey: str
        :param TagValue: Tag value.
        :type TagValue: str
        :param CanDelete: If deletion is allowed.
        :type CanDelete: int
        """
        self.TagKey = None
        self.TagValue = None
        self.CanDelete = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.CanDelete = params.get("CanDelete")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnTagResourcesRequest(AbstractModel):
    """UnTagResources request structure.

    """

    def __init__(self):
        r"""
        :param ResourceList: Six-segment resource description list. Tencent Cloud uses a six-segment value to describe a resource. For more information, see [CAM](https://intl.cloud.tencent.com/document/product/598/67350?from_cn_redirect=1) > Overview > API List > Six-Segment Resource Information.
For example, ResourceList.1 = qcs::${ServiceType}:${Region}:${Account}:${ResourcePreifx}/${ResourceId}.
Value range of N: 0–9
        :type ResourceList: list of str
        :param TagKeys: Tag key.
Value range: 0–9
        :type TagKeys: list of str
        """
        self.ResourceList = None
        self.TagKeys = None


    def _deserialize(self, params):
        self.ResourceList = params.get("ResourceList")
        self.TagKeys = params.get("TagKeys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnTagResourcesResponse(AbstractModel):
    """UnTagResources response structure.

    """

    def __init__(self):
        r"""
        :param FailedResources: Information of failed resources.
When tag unbinding succeeds, the returned `FailedResources` will be empty.
When tag unbinding partially or completely fails, the returned `FailedResources` will display the details of failed resources.
        :type FailedResources: list of FailedResource
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FailedResources = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FailedResources") is not None:
            self.FailedResources = []
            for item in params.get("FailedResources"):
                obj = FailedResource()
                obj._deserialize(item)
                self.FailedResources.append(obj)
        self.RequestId = params.get("RequestId")


class UpdateResourceTagValueRequest(AbstractModel):
    """UpdateResourceTagValue request structure.

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key associated with the resource.
        :type TagKey: str
        :param TagValue: Modified tag value.
        :type TagValue: str
        :param Resource: [Six-segment resource description](https://intl.cloud.tencent.com/document/product/598/10606?from_cn_redirect=1)
        :type Resource: str
        """
        self.TagKey = None
        self.TagValue = None
        self.Resource = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.Resource = params.get("Resource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateResourceTagValueResponse(AbstractModel):
    """UpdateResourceTagValue response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")