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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.tag.v20180813 import models


class TagClient(AbstractClient):
    _apiVersion = '2018-08-13'
    _endpoint = 'tag.tencentcloudapi.com'
    _service = 'tag'


    def AddResourceTag(self, request):
        """This API is used to associate resources with tags.

        :param request: Request instance for AddResourceTag.
        :type request: :class:`tencentcloud.tag.v20180813.models.AddResourceTagRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.AddResourceTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddResourceTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddResourceTagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachResourcesTag(self, request):
        """This API is used to associate a tag with multiple resources.

        :param request: Request instance for AttachResourcesTag.
        :type request: :class:`tencentcloud.tag.v20180813.models.AttachResourcesTagRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.AttachResourcesTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachResourcesTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachResourcesTagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTag(self, request):
        """This API is used to create a tag key and tag value pair.

        :param request: Request instance for CreateTag.
        :type request: :class:`tencentcloud.tag.v20180813.models.CreateTagRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.CreateTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteResourceTag(self, request):
        """This API is used to unassociate tags and resources.

        :param request: Request instance for DeleteResourceTag.
        :type request: :class:`tencentcloud.tag.v20180813.models.DeleteResourceTagRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DeleteResourceTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteResourceTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteResourceTagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTag(self, request):
        """This API is used to delete a tag key and tag value pair.

        :param request: Request instance for DeleteTag.
        :type request: :class:`tencentcloud.tag.v20180813.models.DeleteTagRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DeleteTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourceTags(self, request):
        """This API is used to query the tags associated with a resource.

        :param request: Request instance for DescribeResourceTags.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourceTagsByResourceIds(self, request):
        """This API is used to query tag key and value pairs for existing resources.

        :param request: Request instance for DescribeResourceTagsByResourceIds.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsByResourceIdsRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsByResourceIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceTagsByResourceIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceTagsByResourceIdsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourceTagsByResourceIdsSeq(self, request):
        """This API is used to view the tags associated with a resource in sequence.

        :param request: Request instance for DescribeResourceTagsByResourceIdsSeq.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsByResourceIdsSeqRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsByResourceIdsSeqResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceTagsByResourceIdsSeq", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceTagsByResourceIdsSeqResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourceTagsByTagKeys(self, request):
        """This API is used to get resource tags based on tag keys.

        :param request: Request instance for DescribeResourceTagsByTagKeys.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsByTagKeysRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsByTagKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceTagsByTagKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceTagsByTagKeysResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourcesByTags(self, request):
        """This API is used to query resources by tags.

        :param request: Request instance for DescribeResourcesByTags.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeResourcesByTagsRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeResourcesByTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourcesByTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourcesByTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourcesByTagsUnion(self, request):
        """This API is used to query resource list by tags.

        :param request: Request instance for DescribeResourcesByTagsUnion.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeResourcesByTagsUnionRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeResourcesByTagsUnionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourcesByTagsUnion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourcesByTagsUnionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTagKeys(self, request):
        """This API is used to query tag keys in an existing tag list.

        :param request: Request instance for DescribeTagKeys.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeTagKeysRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeTagKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTagKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTagKeysResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTagValues(self, request):
        """This API is used to query tag values in an existing tag list.

        :param request: Request instance for DescribeTagValues.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeTagValuesRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeTagValuesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTagValues", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTagValuesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTagValuesSeq(self, request):
        """This API is used to query tag values in a created tag list.

        :param request: Request instance for DescribeTagValuesSeq.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeTagValuesSeqRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeTagValuesSeqResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTagValuesSeq", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTagValuesSeqResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTags(self, request):
        """This API is used to query existing tag lists.

        :param request: Request instance for DescribeTags.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeTagsRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTagsSeq(self, request):
        """This API is used to query the created tag lists.

        :param request: Request instance for DescribeTagsSeq.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeTagsSeqRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeTagsSeqResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTagsSeq", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTagsSeqResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachResourcesTag(self, request):
        """This API is used to unbind a tag from multiple resources.

        :param request: Request instance for DetachResourcesTag.
        :type request: :class:`tencentcloud.tag.v20180813.models.DetachResourcesTagRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DetachResourcesTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachResourcesTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachResourcesTagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyResourceTags(self, request):
        """This API is used to modify all tags associated with a resource.

        :param request: Request instance for ModifyResourceTags.
        :type request: :class:`tencentcloud.tag.v20180813.models.ModifyResourceTagsRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.ModifyResourceTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyResourceTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyResourceTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyResourcesTagValue(self, request):
        """This API is used to modify the tag value corresponding to a tag key associated with multiple resources.

        :param request: Request instance for ModifyResourcesTagValue.
        :type request: :class:`tencentcloud.tag.v20180813.models.ModifyResourcesTagValueRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.ModifyResourcesTagValueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyResourcesTagValue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyResourcesTagValueResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateResourceTagValue(self, request):
        """This API is used to modify the values of tags associated with a resource (the tag key does not change).

        :param request: Request instance for UpdateResourceTagValue.
        :type request: :class:`tencentcloud.tag.v20180813.models.UpdateResourceTagValueRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.UpdateResourceTagValueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateResourceTagValue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateResourceTagValueResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)