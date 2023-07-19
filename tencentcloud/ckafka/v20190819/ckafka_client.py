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
from tencentcloud.ckafka.v20190819 import models


class CkafkaClient(AbstractClient):
    _apiVersion = '2019-08-19'
    _endpoint = 'ckafka.tencentcloudapi.com'
    _service = 'ckafka'


    def BatchCreateAcl(self, request):
        """This API is used to create ACL policies in batches.

        :param request: Request instance for BatchCreateAcl.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.BatchCreateAclRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.BatchCreateAclResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchCreateAcl", params, headers=headers)
            response = json.loads(body)
            model = models.BatchCreateAclResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyGroupOffsets(self, request):
        """This API is used to batch modify consumer group offsets.

        :param request: Request instance for BatchModifyGroupOffsets.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.BatchModifyGroupOffsetsRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.BatchModifyGroupOffsetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyGroupOffsets", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyGroupOffsetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyTopicAttributes(self, request):
        """This API is used to batch set topic attributes.

        :param request: Request instance for BatchModifyTopicAttributes.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.BatchModifyTopicAttributesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.BatchModifyTopicAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyTopicAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyTopicAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAcl(self, request):
        """This API is used to add an ACL policy.

        :param request: Request instance for CreateAcl.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateAclRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateAclResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAcl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAclResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAclRule(self, request):
        """This API shows you how to create an ACL rule.

        :param request: Request instance for CreateAclRule.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateAclRuleRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConsumer(self, request):
        """This API is used to create a consumer group.

        :param request: Request instance for CreateConsumer.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateConsumerRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDatahubTopic(self, request):
        """This API is used to create a DataHub topic.

        :param request: Request instance for CreateDatahubTopic.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateDatahubTopicRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateDatahubTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDatahubTopic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDatahubTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstancePost(self, request):
        """This API is used to create a pay-as-you-go instance.  It will be deprecated in future versions. We recommend that you use the `CreatePostPaidInstance` API instead.  You can call this API via SDK or the TencentCloud API console to create a pay-as-you-go CKafka instance,  which is an alternate option for making a purchase in the console.

        :param request: Request instance for CreateInstancePost.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePostRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstancePost", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstancePostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePartition(self, request):
        """This API is used to add a partition in a topic.

        :param request: Request instance for CreatePartition.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreatePartitionRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreatePartitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePartition", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePartitionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePostPaidInstance(self, request):
        """This API is used to replace `CreateInstancePost`  to create a pay-as-you-go instance.  You can call this API via SDK or the TencentCloud API console to create a pay-as-you-go CKafka instance,  which is an alternate option for making a purchase in the console.

        :param request: Request instance for CreatePostPaidInstance.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreatePostPaidInstanceRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreatePostPaidInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePostPaidInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePostPaidInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTopic(self, request):
        """This API is used to create a CKafka topic.

        :param request: Request instance for CreateTopic.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicResponse`

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


    def CreateTopicIpWhiteList(self, request):
        """This API is used to create a topic IP allowlist.

        :param request: Request instance for CreateTopicIpWhiteList.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicIpWhiteListRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicIpWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTopicIpWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTopicIpWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUser(self, request):
        """This API is used to add a user.

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAcl(self, request):
        """This API is used to delete an ACL.

        :param request: Request instance for DeleteAcl.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteAclRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteAclResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAcl", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAclResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstancePre(self, request):
        """This API is used to delete a monthly subscribed (prepaid) instance.

        :param request: Request instance for DeleteInstancePre.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteInstancePreRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteInstancePreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInstancePre", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInstancePreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRoute(self, request):
        """This API is used to delete a route.

        :param request: Request instance for DeleteRoute.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteRouteRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoute", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRouteTriggerTime(self, request):
        """This API is used to modify the delayed trigger time of route deletion.

        :param request: Request instance for DeleteRouteTriggerTime.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteRouteTriggerTimeRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteRouteTriggerTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRouteTriggerTime", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRouteTriggerTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTopic(self, request):
        """This API is used to delete a CKafka topic.

        :param request: Request instance for DeleteTopic.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteTopicRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteTopicResponse`

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


    def DeleteTopicIpWhiteList(self, request):
        """This API is used to delete a topic IP allowlist.

        :param request: Request instance for DeleteTopicIpWhiteList.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteTopicIpWhiteListRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteTopicIpWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTopicIpWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTopicIpWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUser(self, request):
        """This API is used to delete a user.

        :param request: Request instance for DeleteUser.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteUserRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeACL(self, request):
        """This API is used to enumerate ACLs.

        :param request: Request instance for DescribeACL.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeACLRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeACL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAclRule(self, request):
        """This API is used to query the ACL rule list.

        :param request: Request instance for DescribeAclRule.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeAclRuleRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppInfo(self, request):
        """This API is used to query the user list.

        :param request: Request instance for DescribeAppInfo.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeAppInfoRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeAppInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCkafkaZone(self, request):
        """This API is used to view the AZ list of Ckafka.

        :param request: Request instance for DescribeCkafkaZone.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeCkafkaZoneRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeCkafkaZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCkafkaZone", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCkafkaZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConsumerGroup(self, request):
        """This API is used to query consumer group information.

        :param request: Request instance for DescribeConsumerGroup.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeConsumerGroupRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatahubTopic(self, request):
        """This API is used to get the DataHub topic attributes.

        :param request: Request instance for DescribeDatahubTopic.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatahubTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatahubTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatahubTopics(self, request):
        """This API is used to query the DataHub topic list.

        :param request: Request instance for DescribeDatahubTopics.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicsRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatahubTopics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatahubTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroup(self, request):
        """This API is used to enumerate consumer groups (simplified).

        :param request: Request instance for DescribeGroup.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupInfo(self, request):
        """This API is used to get consumer group information.

        :param request: Request instance for DescribeGroupInfo.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupInfoRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupOffsets(self, request):
        """This API is used to get the consumer group offset.

        :param request: Request instance for DescribeGroupOffsets.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupOffsetsRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupOffsetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupOffsets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupOffsetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceAttributes(self, request):
        """This API is used to get instance attributes.

        :param request: Request instance for DescribeInstanceAttributes.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstanceAttributesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstanceAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """This API is used to get the list of CKafka instances under a user account.

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesDetail(self, request):
        """This API is used to get instance list details under a user account.

        :param request: Request instance for DescribeInstancesDetail.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstancesDetailRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstancesDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegion(self, request):
        """This API is used to enumerate regions, and can be called only in Guangzhou.

        :param request: Request instance for DescribeRegion.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeRegionRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoute(self, request):
        """This API is used to view route information.

        :param request: Request instance for DescribeRoute.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeRouteRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskStatus(self, request):
        """This API is used to query the task status.

        :param request: Request instance for DescribeTaskStatus.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTaskStatusRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopic(self, request):
        """API domain name: https://ckafka.tencentcloudapi.com
        This API is used to get the list of topics in a CKafka instance of a user.

        :param request: Request instance for DescribeTopic.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicAttributes(self, request):
        """This API is used to get topic attributes.

        :param request: Request instance for DescribeTopicAttributes.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicAttributesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicDetail(self, request):
        """This API is used to get topic list details (only for call in the console).

        :param request: Request instance for DescribeTopicDetail.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicDetailRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicDetailResponse`

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


    def DescribeTopicProduceConnection(self, request):
        """This API is used to query the connection information of the topic producer.

        :param request: Request instance for DescribeTopicProduceConnection.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicProduceConnectionRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicProduceConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicProduceConnection", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicProduceConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicSubscribeGroup(self, request):
        """This API is used to search and subscribe the message group information of a topic.

        :param request: Request instance for DescribeTopicSubscribeGroup.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicSubscribeGroupRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicSubscribeGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicSubscribeGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicSubscribeGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicSyncReplica(self, request):
        """This API is used to get the details of a synced topic replica.

        :param request: Request instance for DescribeTopicSyncReplica.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicSyncReplicaRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicSyncReplicaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicSyncReplica", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicSyncReplicaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUser(self, request):
        """This API is used to query user information.

        :param request: Request instance for DescribeUser.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeUserRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUser", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FetchMessageByOffset(self, request):
        """This API is used to query messages based on a specified offset position.

        :param request: Request instance for FetchMessageByOffset.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.FetchMessageByOffsetRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.FetchMessageByOffsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FetchMessageByOffset", params, headers=headers)
            response = json.loads(body)
            model = models.FetchMessageByOffsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FetchMessageListByOffset(self, request):
        """This API is used to query the message list based on an offset.

        :param request: Request instance for FetchMessageListByOffset.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.FetchMessageListByOffsetRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.FetchMessageListByOffsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FetchMessageListByOffset", params, headers=headers)
            response = json.loads(body)
            model = models.FetchMessageListByOffsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquireCkafkaPrice(self, request):
        """This API is used to purchase a CKafka instance or query the instance renewal price.

        :param request: Request instance for InquireCkafkaPrice.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.InquireCkafkaPriceRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquireCkafkaPriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquireCkafkaPrice", params, headers=headers)
            response = json.loads(body)
            model = models.InquireCkafkaPriceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAclRule(self, request):
        """This API is used to modify an ACL policy, and currently only supports specifying whether to apply the preset rule to new topics.

        :param request: Request instance for ModifyAclRule.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyAclRuleRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatahubTopic(self, request):
        """This API is used to modify the DataHub topic attributes.

        :param request: Request instance for ModifyDatahubTopic.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyDatahubTopicRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyDatahubTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatahubTopic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatahubTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGroupOffsets(self, request):
        """This API is used to set the consumer group (Groups) offset.

        :param request: Request instance for ModifyGroupOffsets.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyGroupOffsetsRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyGroupOffsetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGroupOffsets", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGroupOffsetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceAttributes(self, request):
        """This API is used to set instance attributes.

        :param request: Request instance for ModifyInstanceAttributes.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancePre(self, request):
        """This API is used to change the configurations of a prepaid instance, such as disk capacity and bandwidth.

        :param request: Request instance for ModifyInstancePre.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstancePreRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstancePreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancePre", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancePreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPassword(self, request):
        """This API is used to change the password.

        :param request: Request instance for ModifyPassword.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyPasswordRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTopicAttributes(self, request):
        """This API is used to modify topic attributes.

        :param request: Request instance for ModifyTopicAttributes.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyTopicAttributesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyTopicAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTopicAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTopicAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendMessage(self, request):
        """This API is used to send messages through the HTTP access layer.

        :param request: Request instance for SendMessage.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.SendMessageRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.SendMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendMessage", params, headers=headers)
            response = json.loads(body)
            model = models.SendMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))