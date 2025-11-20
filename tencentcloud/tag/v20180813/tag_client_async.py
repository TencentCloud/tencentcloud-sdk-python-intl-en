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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.tag.v20180813 import models
from typing import Dict


class TagClient(AbstractClient):
    _apiVersion = '2018-08-13'
    _endpoint = 'tag.intl.tencentcloudapi.com'
    _service = 'tag'

    async def AddProject(
            self,
            request: models.AddProjectRequest,
            opts: Dict = None,
    ) -> models.AddProjectResponse:
        """
        Creates a project
        """
        
        kwargs = {}
        kwargs["action"] = "AddProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddResourceTag(
            self,
            request: models.AddResourceTagRequest,
            opts: Dict = None,
    ) -> models.AddResourceTagResponse:
        """
        This API is used to associate resources with tags.
        """
        
        kwargs = {}
        kwargs["action"] = "AddResourceTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddResourceTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachResourcesTag(
            self,
            request: models.AttachResourcesTagRequest,
            opts: Dict = None,
    ) -> models.AttachResourcesTagResponse:
        """
        This API is used to associate a tag with multiple resources.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachResourcesTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachResourcesTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTag(
            self,
            request: models.CreateTagRequest,
            opts: Dict = None,
    ) -> models.CreateTagResponse:
        """
        This API is used to create a tag key and tag value pair.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTags(
            self,
            request: models.CreateTagsRequest,
            opts: Dict = None,
    ) -> models.CreateTagsResponse:
        """
        This API is used to create multiple tag key-value pairs.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteResourceTag(
            self,
            request: models.DeleteResourceTagRequest,
            opts: Dict = None,
    ) -> models.DeleteResourceTagResponse:
        """
        This API is used to unassociate tags and resources.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteResourceTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteResourceTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTag(
            self,
            request: models.DeleteTagRequest,
            opts: Dict = None,
    ) -> models.DeleteTagResponse:
        """
        This API is used to delete a tag key and tag value pair.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTags(
            self,
            request: models.DeleteTagsRequest,
            opts: Dict = None,
    ) -> models.DeleteTagsResponse:
        """
        This API is used to delete tag keys and tag values in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjects(
            self,
            request: models.DescribeProjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectsResponse:
        """
        This API is used to get project lists.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceTags(
            self,
            request: models.DescribeResourceTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceTagsResponse:
        """
        This API is used to query the tags associated with a resource.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceTagsByResourceIds(
            self,
            request: models.DescribeResourceTagsByResourceIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceTagsByResourceIdsResponse:
        """
        This API is used to query the tag key-value pairs associated with an existing resource.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceTagsByResourceIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceTagsByResourceIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceTagsByResourceIdsSeq(
            self,
            request: models.DescribeResourceTagsByResourceIdsSeqRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceTagsByResourceIdsSeqResponse:
        """
        This API is used to view the tags associated with a resource in sequence.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceTagsByResourceIdsSeq"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceTagsByResourceIdsSeqResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceTagsByTagKeys(
            self,
            request: models.DescribeResourceTagsByTagKeysRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceTagsByTagKeysResponse:
        """
        This API is used to get resource tags based on tag keys.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceTagsByTagKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceTagsByTagKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourcesByTags(
            self,
            request: models.DescribeResourcesByTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcesByTagsResponse:
        """
        This API is used to query resources by tags.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourcesByTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcesByTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourcesByTagsUnion(
            self,
            request: models.DescribeResourcesByTagsUnionRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcesByTagsUnionResponse:
        """
        This API is used to query resource list by tags.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourcesByTagsUnion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcesByTagsUnionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagKeys(
            self,
            request: models.DescribeTagKeysRequest,
            opts: Dict = None,
    ) -> models.DescribeTagKeysResponse:
        """
        This API is used to query tag keys in the list of created tags.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagValues(
            self,
            request: models.DescribeTagValuesRequest,
            opts: Dict = None,
    ) -> models.DescribeTagValuesResponse:
        """
        This API is used to query tag values in an existing tag list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagValues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagValuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagValuesSeq(
            self,
            request: models.DescribeTagValuesSeqRequest,
            opts: Dict = None,
    ) -> models.DescribeTagValuesSeqResponse:
        """
        This API is used to query tag values in a created tag list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagValuesSeq"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagValuesSeqResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTags(
            self,
            request: models.DescribeTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeTagsResponse:
        """
        This API is used to query the list of created tags.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagsSeq(
            self,
            request: models.DescribeTagsSeqRequest,
            opts: Dict = None,
    ) -> models.DescribeTagsSeqResponse:
        """
        This API is used to query the created tag lists.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagsSeq"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagsSeqResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachResourcesTag(
            self,
            request: models.DetachResourcesTagRequest,
            opts: Dict = None,
    ) -> models.DetachResourcesTagResponse:
        """
        This API is used to unbind a tag from multiple resources.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachResourcesTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachResourcesTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetResources(
            self,
            request: models.GetResourcesRequest,
            opts: Dict = None,
    ) -> models.GetResourcesResponse:
        """
        This API is used to query the list of resources associated with a tag.
        """
        
        kwargs = {}
        kwargs["action"] = "GetResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTagKeys(
            self,
            request: models.GetTagKeysRequest,
            opts: Dict = None,
    ) -> models.GetTagKeysResponse:
        """
        This API is used to query the list of tag keys.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTagKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTagKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTagValues(
            self,
            request: models.GetTagValuesRequest,
            opts: Dict = None,
    ) -> models.GetTagValuesResponse:
        """
        This API is used to query tag values in the list of created tags.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTagValues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTagValuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTags(
            self,
            request: models.GetTagsRequest,
            opts: Dict = None,
    ) -> models.GetTagsResponse:
        """
        This API is used to get the list of created tags.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourceTags(
            self,
            request: models.ModifyResourceTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyResourceTagsResponse:
        """
        This API is used to modify all tags associated with a resource.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourceTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourceTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourcesTagValue(
            self,
            request: models.ModifyResourcesTagValueRequest,
            opts: Dict = None,
    ) -> models.ModifyResourcesTagValueResponse:
        """
        This API is used to modify the tag value corresponding to a tag key associated with multiple resources.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourcesTagValue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourcesTagValueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TagResources(
            self,
            request: models.TagResourcesRequest,
            opts: Dict = None,
    ) -> models.TagResourcesResponse:
        """
        This API is used to create and bind a tag uniformly to multiple specified resources of multiple Tencent Cloud services.
        """
        
        kwargs = {}
        kwargs["action"] = "TagResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TagResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnTagResources(
            self,
            request: models.UnTagResourcesRequest,
            opts: Dict = None,
    ) -> models.UnTagResourcesResponse:
        """
        This API is used to unbind a tag uniformly from multiple specified resources of multiple Tencent Cloud services.
        """
        
        kwargs = {}
        kwargs["action"] = "UnTagResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnTagResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateResourceTagValue(
            self,
            request: models.UpdateResourceTagValueRequest,
            opts: Dict = None,
    ) -> models.UpdateResourceTagValueResponse:
        """
        This API is used to modify the values of tags associated with a resource (the tag key does not change).
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateResourceTagValue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateResourceTagValueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)