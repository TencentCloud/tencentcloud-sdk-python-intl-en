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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.mqtt.v20240516 import models


class MqttClient(AbstractClient):
    _apiVersion = '2024-05-16'
    _endpoint = 'mqtt.intl.tencentcloudapi.com'
    _service = 'mqtt'


    def AddClientSubscription(self, request):
        r"""This API is used to add a subscription for an MQTT client.

        :param request: Request instance for AddClientSubscription.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.AddClientSubscriptionRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.AddClientSubscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddClientSubscription", params, headers=headers)
            response = json.loads(body)
            model = models.AddClientSubscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAuthorizationPolicy(self, request):
        r"""This API is used to create a performance test task for an MQTT instance.

        :param request: Request instance for CreateAuthorizationPolicy.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.CreateAuthorizationPolicyRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.CreateAuthorizationPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAuthorizationPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAuthorizationPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDeviceIdentity(self, request):
        r"""Create a device signature for per-device secret

        :param request: Request instance for CreateDeviceIdentity.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.CreateDeviceIdentityRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.CreateDeviceIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDeviceIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDeviceIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstance(self, request):
        r"""This API is used to purchase a new MQTT instance.

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.CreateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMessageEnrichmentRule(self, request):
        r"""This API is used to create a message enrichment rule.

        :param request: Request instance for CreateMessageEnrichmentRule.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.CreateMessageEnrichmentRuleRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.CreateMessageEnrichmentRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMessageEnrichmentRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMessageEnrichmentRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUser(self, request):
        r"""This API is used to add an MQTT role.

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.CreateUserResponse`

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


    def DeleteAuthorizationPolicy(self, request):
        r"""This API is used to delete policy rules.

        :param request: Request instance for DeleteAuthorizationPolicy.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeleteAuthorizationPolicyRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeleteAuthorizationPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAuthorizationPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuthorizationPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClientSubscription(self, request):
        r"""This API is used to delete a subscription of an MQTT client.

        :param request: Request instance for DeleteClientSubscription.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeleteClientSubscriptionRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeleteClientSubscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClientSubscription", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClientSubscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDeviceIdentity(self, request):
        r"""Delete a device signature

        :param request: Request instance for DeleteDeviceIdentity.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeleteDeviceIdentityRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeleteDeviceIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDeviceIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDeviceIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstance(self, request):
        r"""This API is used to delete an MQTT instance.

        :param request: Request instance for DeleteInstance.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeleteInstanceRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeleteInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMessageEnrichmentRule(self, request):
        r"""This API is used to delete the message enrichment rule.

        :param request: Request instance for DeleteMessageEnrichmentRule.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeleteMessageEnrichmentRuleRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeleteMessageEnrichmentRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMessageEnrichmentRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMessageEnrichmentRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTopic(self, request):
        r"""This API is used to delete an MQTT topic.

        :param request: Request instance for DeleteTopic.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeleteTopicRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeleteTopicResponse`

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


    def DeleteUser(self, request):
        r"""This API is used to delete an MQTT user.

        :param request: Request instance for DeleteUser.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DeleteUserRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DeleteUserResponse`

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


    def DescribeAuthorizationPolicies(self, request):
        r"""This API is used to query authorization rules.

        :param request: Request instance for DescribeAuthorizationPolicies.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeAuthorizationPoliciesRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeAuthorizationPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuthorizationPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuthorizationPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClientList(self, request):
        r"""This API is used to query the MQTT client details.

        :param request: Request instance for DescribeClientList.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeClientListRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeClientListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClientList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClientListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceCertificates(self, request):
        r"""Query device certificates with paging

        :param request: Request instance for DescribeDeviceCertificates.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeDeviceCertificatesRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeDeviceCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceIdentities(self, request):
        r"""Query the list of device identifiers in a cluster

        :param request: Request instance for DescribeDeviceIdentities.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeDeviceIdentitiesRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeDeviceIdentitiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceIdentities", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceIdentitiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceIdentity(self, request):
        r"""Query device identification

        :param request: Request instance for DescribeDeviceIdentity.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeDeviceIdentityRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeDeviceIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstance(self, request):
        r"""This API is used to query instance information.

        :param request: Request instance for DescribeInstance.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeInstanceRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceList(self, request):
        r"""Get instance list. Description of the Filters parameter use is as follows:
        1. InstanceName, fuzzy search by name
        2. InstanceId, query by instance ID
        3. InstanceStatus, instance status query, supports multiple selections

        When using the TagFilters parameter for search, the filters parameter is invalid.

        :param request: Request instance for DescribeInstanceList.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeInstanceListRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMessageByTopic(self, request):
        r"""This API is used to query messages based on subscription.

        :param request: Request instance for DescribeMessageByTopic.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeMessageByTopicRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeMessageByTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessageByTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMessageByTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMessageDetails(self, request):
        r"""This API is used to query the MQTT message details.

        :param request: Request instance for DescribeMessageDetails.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeMessageDetailsRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeMessageDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessageDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMessageDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMessageEnrichmentRules(self, request):
        r"""This API is used to query message enrichment rules.

        :param request: Request instance for DescribeMessageEnrichmentRules.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeMessageEnrichmentRulesRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeMessageEnrichmentRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessageEnrichmentRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMessageEnrichmentRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProductSKUList(self, request):
        r"""This API is used to obtain product sales specifications.

        :param request: Request instance for DescribeProductSKUList.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeProductSKUListRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeProductSKUListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductSKUList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductSKUListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSharedSubscriptionClient(self, request):
        r"""Query shared subscription group detailed information

        :param request: Request instance for DescribeSharedSubscriptionClient.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeSharedSubscriptionClientRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeSharedSubscriptionClientResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSharedSubscriptionClient", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSharedSubscriptionClientResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSharedSubscriptionGroups(self, request):
        r"""This API is used to query the subscription group list shared within the cluster.

        :param request: Request instance for DescribeSharedSubscriptionGroups.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeSharedSubscriptionGroupsRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeSharedSubscriptionGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSharedSubscriptionGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSharedSubscriptionGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSharedSubscriptions(self, request):
        r"""Query the subscription list of a shared subscription group

        :param request: Request instance for DescribeSharedSubscriptions.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeSharedSubscriptionsRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeSharedSubscriptionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSharedSubscriptions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSharedSubscriptionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopic(self, request):
        r"""This API is used to query the MQTT topic details.

        :param request: Request instance for DescribeTopic.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeTopicRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeTopicResponse`

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


    def DescribeUserList(self, request):
        r"""This API is used to query the user list. Filter parameter usage instructions are as follows:.

        This API is used to perform Username fuzzy search.

        :param request: Request instance for DescribeUserList.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.DescribeUserListRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.DescribeUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KickOutClient(self, request):
        r"""This API is used to kick out a client.

        :param request: Request instance for KickOutClient.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.KickOutClientRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.KickOutClientResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KickOutClient", params, headers=headers)
            response = json.loads(body)
            model = models.KickOutClientResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAuthorizationPolicy(self, request):
        r"""This API is used to modify policy rules. See the data plane authorization policy description (https://www.tencentcloud.com/document/product/1778/109715?from_cn_redirect=1).

        :param request: Request instance for ModifyAuthorizationPolicy.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ModifyAuthorizationPolicyRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ModifyAuthorizationPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAuthorizationPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAuthorizationPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDeviceIdentity(self, request):
        r"""Modify the device signature

        :param request: Request instance for ModifyDeviceIdentity.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ModifyDeviceIdentityRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ModifyDeviceIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDeviceIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDeviceIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstance(self, request):
        r"""This API is used to modify instance attributes. Only running clusters can call this API to perform configuration change.

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ModifyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMessageEnrichmentRule(self, request):
        r"""This API is used to modify message enrichment rules.
        Note: All attributes of the current rule must be submitted, even if specific fields are not modified.

        :param request: Request instance for ModifyMessageEnrichmentRule.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ModifyMessageEnrichmentRuleRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ModifyMessageEnrichmentRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMessageEnrichmentRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMessageEnrichmentRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUser(self, request):
        r"""This API is used to modify an MQTT role.

        :param request: Request instance for ModifyUser.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.ModifyUserRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.ModifyUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUser", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAuthorizationPolicyPriority(self, request):
        r"""This API is used to modify policy rule priority.

        :param request: Request instance for UpdateAuthorizationPolicyPriority.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.UpdateAuthorizationPolicyPriorityRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.UpdateAuthorizationPolicyPriorityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAuthorizationPolicyPriority", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAuthorizationPolicyPriorityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateMessageEnrichmentRulePriority(self, request):
        r"""This API is used to modify the priority for message enrichment rule.

        :param request: Request instance for UpdateMessageEnrichmentRulePriority.
        :type request: :class:`tencentcloud.mqtt.v20240516.models.UpdateMessageEnrichmentRulePriorityRequest`
        :rtype: :class:`tencentcloud.mqtt.v20240516.models.UpdateMessageEnrichmentRulePriorityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateMessageEnrichmentRulePriority", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateMessageEnrichmentRulePriorityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))