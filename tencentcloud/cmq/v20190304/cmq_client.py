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
from tencentcloud.cmq.v20190304 import models


class CmqClient(AbstractClient):
    _apiVersion = '2019-03-04'
    _endpoint = 'cmq.intl.tencentcloudapi.com'
    _service = 'cmq'


    def ClearQueue(self, request):
        """This API is used to clear all messages in a queue.

        :param request: Request instance for ClearQueue.
        :type request: :class:`tencentcloud.cmq.v20190304.models.ClearQueueRequest`
        :rtype: :class:`tencentcloud.cmq.v20190304.models.ClearQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearQueue", params, headers=headers)
            response = json.loads(body)
            model = models.ClearQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ClearSubscriptionFilterTags(self, request):
        """This API is used to clear the message tags of a subscriber.

        :param request: Request instance for ClearSubscriptionFilterTags.
        :type request: :class:`tencentcloud.cmq.v20190304.models.ClearSubscriptionFilterTagsRequest`
        :rtype: :class:`tencentcloud.cmq.v20190304.models.ClearSubscriptionFilterTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearSubscriptionFilterTags", params, headers=headers)
            response = json.loads(body)
            model = models.ClearSubscriptionFilterTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateQueue(self, request):
        """This API is used to create a queue.

        :param request: Request instance for CreateQueue.
        :type request: :class:`tencentcloud.cmq.v20190304.models.CreateQueueRequest`
        :rtype: :class:`tencentcloud.cmq.v20190304.models.CreateQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateQueue", params, headers=headers)
            response = json.loads(body)
            model = models.CreateQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSubscribe(self, request):
        """This API is used to create a subscription.

        :param request: Request instance for CreateSubscribe.
        :type request: :class:`tencentcloud.cmq.v20190304.models.CreateSubscribeRequest`
        :rtype: :class:`tencentcloud.cmq.v20190304.models.CreateSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTopic(self, request):
        """This API is used to create a topic.

        :param request: Request instance for CreateTopic.
        :type request: :class:`tencentcloud.cmq.v20190304.models.CreateTopicRequest`
        :rtype: :class:`tencentcloud.cmq.v20190304.models.CreateTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTopic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteQueue(self, request):
        """This API is used to delete a queue.

        :param request: Request instance for DeleteQueue.
        :type request: :class:`tencentcloud.cmq.v20190304.models.DeleteQueueRequest`
        :rtype: :class:`tencentcloud.cmq.v20190304.models.DeleteQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteQueue", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSubscribe(self, request):
        """This API is used to delete a subscription.

        :param request: Request instance for DeleteSubscribe.
        :type request: :class:`tencentcloud.cmq.v20190304.models.DeleteSubscribeRequest`
        :rtype: :class:`tencentcloud.cmq.v20190304.models.DeleteSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTopic(self, request):
        """This API is used to delete a topic.

        :param request: Request instance for DeleteTopic.
        :type request: :class:`tencentcloud.cmq.v20190304.models.DeleteTopicRequest`
        :rtype: :class:`tencentcloud.cmq.v20190304.models.DeleteTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeadLetterSourceQueues(self, request):
        """This API is used to enumerate the source queues of a dead letter queue.

        :param request: Request instance for DescribeDeadLetterSourceQueues.
        :type request: :class:`tencentcloud.cmq.v20190304.models.DescribeDeadLetterSourceQueuesRequest`
        :rtype: :class:`tencentcloud.cmq.v20190304.models.DescribeDeadLetterSourceQueuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeadLetterSourceQueues", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeadLetterSourceQueuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQueueDetail(self, request):
        """This API is used to enumerate queues.

        :param request: Request instance for DescribeQueueDetail.
        :type request: :class:`tencentcloud.cmq.v20190304.models.DescribeQueueDetailRequest`
        :rtype: :class:`tencentcloud.cmq.v20190304.models.DescribeQueueDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQueueDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQueueDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubscriptionDetail(self, request):
        """This API is used to query subscription details.

        :param request: Request instance for DescribeSubscriptionDetail.
        :type request: :class:`tencentcloud.cmq.v20190304.models.DescribeSubscriptionDetailRequest`
        :rtype: :class:`tencentcloud.cmq.v20190304.models.DescribeSubscriptionDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubscriptionDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubscriptionDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicDetail(self, request):
        """This API is used to query topic details.

        :param request: Request instance for DescribeTopicDetail.
        :type request: :class:`tencentcloud.cmq.v20190304.models.DescribeTopicDetailRequest`
        :rtype: :class:`tencentcloud.cmq.v20190304.models.DescribeTopicDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyQueueAttribute(self, request):
        """This API is used to modify queue attributes.

        :param request: Request instance for ModifyQueueAttribute.
        :type request: :class:`tencentcloud.cmq.v20190304.models.ModifyQueueAttributeRequest`
        :rtype: :class:`tencentcloud.cmq.v20190304.models.ModifyQueueAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyQueueAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyQueueAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySubscriptionAttribute(self, request):
        """This API is used to modify subscription attributes.

        :param request: Request instance for ModifySubscriptionAttribute.
        :type request: :class:`tencentcloud.cmq.v20190304.models.ModifySubscriptionAttributeRequest`
        :rtype: :class:`tencentcloud.cmq.v20190304.models.ModifySubscriptionAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubscriptionAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubscriptionAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTopicAttribute(self, request):
        """This API is used to modify topic attributes.

        :param request: Request instance for ModifyTopicAttribute.
        :type request: :class:`tencentcloud.cmq.v20190304.models.ModifyTopicAttributeRequest`
        :rtype: :class:`tencentcloud.cmq.v20190304.models.ModifyTopicAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTopicAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTopicAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RewindQueue(self, request):
        """This API is used to rewind a queue.

        :param request: Request instance for RewindQueue.
        :type request: :class:`tencentcloud.cmq.v20190304.models.RewindQueueRequest`
        :rtype: :class:`tencentcloud.cmq.v20190304.models.RewindQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RewindQueue", params, headers=headers)
            response = json.loads(body)
            model = models.RewindQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindDeadLetter(self, request):
        """This API is used to unbind a dead letter queue.

        :param request: Request instance for UnbindDeadLetter.
        :type request: :class:`tencentcloud.cmq.v20190304.models.UnbindDeadLetterRequest`
        :rtype: :class:`tencentcloud.cmq.v20190304.models.UnbindDeadLetterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindDeadLetter", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindDeadLetterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))