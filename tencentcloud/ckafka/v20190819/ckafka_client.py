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


    def CreateAcl(self, request):
        """This API is used to add an ACL policy.

        :param request: Request instance for CreateAcl.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateAclRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateAclResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAcl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAclResponse()
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


    def CreatePartition(self, request):
        """This API is used to add a partition in a topic.

        :param request: Request instance for CreatePartition.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreatePartitionRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreatePartitionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePartition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePartitionResponse()
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


    def CreateTopic(self, request):
        """This API is used to create a CKafka topic.

        :param request: Request instance for CreateTopic.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTopicResponse()
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


    def CreateTopicIpWhiteList(self, request):
        """This API is used to create a topic IP allowlist.

        :param request: Request instance for CreateTopicIpWhiteList.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicIpWhiteListRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicIpWhiteListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTopicIpWhiteList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTopicIpWhiteListResponse()
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


    def CreateUser(self, request):
        """This API is used to add a user.

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUserResponse()
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


    def DeleteAcl(self, request):
        """This API is used to delete an ACL.

        :param request: Request instance for DeleteAcl.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteAclRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteAclResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAcl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAclResponse()
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


    def DeleteTopic(self, request):
        """This API is used to delete a CKafka topic.

        :param request: Request instance for DeleteTopic.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteTopicRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTopicResponse()
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


    def DeleteTopicIpWhiteList(self, request):
        """This API is used to delete a topic IP allowlist.

        :param request: Request instance for DeleteTopicIpWhiteList.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteTopicIpWhiteListRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteTopicIpWhiteListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTopicIpWhiteList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTopicIpWhiteListResponse()
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


    def DeleteUser(self, request):
        """This API is used to delete a user.

        :param request: Request instance for DeleteUser.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteUserRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUserResponse()
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


    def DescribeACL(self, request):
        """This API is used to enumerate ACLs.

        :param request: Request instance for DescribeACL.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeACLRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeACLResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeACL", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeACLResponse()
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


    def DescribeAppInfo(self, request):
        """This API is used to query the user list.

        :param request: Request instance for DescribeAppInfo.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeAppInfoRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeAppInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAppInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAppInfoResponse()
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


    def DescribeCkafkaZone(self, request):
        """This API is used to view the AZ list of Ckafka.

        :param request: Request instance for DescribeCkafkaZone.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeCkafkaZoneRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeCkafkaZoneResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCkafkaZone", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCkafkaZoneResponse()
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


    def DescribeConsumerGroup(self, request):
        """This API is used to query consumer group information.

        :param request: Request instance for DescribeConsumerGroup.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeConsumerGroupRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConsumerGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConsumerGroupResponse()
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


    def DescribeGroup(self, request):
        """This API is used to enumerate consumer groups (simplified).

        :param request: Request instance for DescribeGroup.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupResponse()
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


    def DescribeGroupInfo(self, request):
        """This API is used to get consumer group information.

        :param request: Request instance for DescribeGroupInfo.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupInfoRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroupInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupInfoResponse()
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


    def DescribeGroupOffsets(self, request):
        """This API is used to get the consumer group offset.

        :param request: Request instance for DescribeGroupOffsets.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupOffsetsRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupOffsetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroupOffsets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupOffsetsResponse()
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


    def DescribeInstanceAttributes(self, request):
        """This API is used to get instance attributes.

        :param request: Request instance for DescribeInstanceAttributes.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstanceAttributesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstanceAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceAttributesResponse()
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


    def DescribeInstances(self, request):
        """This API is used to get the list of CKafka instances under a user account.

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesResponse()
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


    def DescribeInstancesDetail(self, request):
        """This API is used to get instance list details under a user account.

        :param request: Request instance for DescribeInstancesDetail.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstancesDetailRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstancesDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstancesDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesDetailResponse()
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


    def DescribeRegion(self, request):
        """This API is used to enumerate regions, and can be called only in Guangzhou.

        :param request: Request instance for DescribeRegion.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeRegionRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeRegionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionResponse()
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


    def DescribeRoute(self, request):
        """This API is used to view route information.

        :param request: Request instance for DescribeRoute.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeRouteRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeRouteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRoute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRouteResponse()
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


    def DescribeTopic(self, request):
        """API domain name: https://ckafka.tencentcloudapi.com
        This API is used to get the list of topics in a CKafka instance of a user.

        :param request: Request instance for DescribeTopic.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTopicResponse()
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


    def DescribeTopicAttributes(self, request):
        """This API is used to get topic attributes.

        :param request: Request instance for DescribeTopicAttributes.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicAttributesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTopicAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTopicAttributesResponse()
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


    def DescribeTopicDetail(self, request):
        """This API is used to get topic list details (only for call in the console).

        :param request: Request instance for DescribeTopicDetail.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicDetailRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTopicDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTopicDetailResponse()
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


    def DescribeUser(self, request):
        """This API is used to query user information.

        :param request: Request instance for DescribeUser.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeUserRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserResponse()
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


    def ModifyGroupOffsets(self, request):
        """This API is used to set the consumer group (Groups) offset.

        :param request: Request instance for ModifyGroupOffsets.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyGroupOffsetsRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyGroupOffsetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyGroupOffsets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyGroupOffsetsResponse()
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


    def ModifyInstanceAttributes(self, request):
        """This API is used to set instance attributes.

        :param request: Request instance for ModifyInstanceAttributes.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstanceAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceAttributesResponse()
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


    def ModifyPassword(self, request):
        """This API is used to change the password.

        :param request: Request instance for ModifyPassword.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyPasswordRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPasswordResponse()
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


    def ModifyTopicAttributes(self, request):
        """This API is used to modify topic attributes.

        :param request: Request instance for ModifyTopicAttributes.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyTopicAttributesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyTopicAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTopicAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTopicAttributesResponse()
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