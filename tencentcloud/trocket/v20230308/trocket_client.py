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
from tencentcloud.trocket.v20230308 import models


class TrocketClient(AbstractClient):
    _apiVersion = '2023-03-08'
    _endpoint = 'trocket.intl.tencentcloudapi.com'
    _service = 'trocket'


    def ChangeMigratingTopicToNextStage(self, request):
        r"""This API is used to modify the Topic status during migration and go to next step.

        :param request: Request instance for ChangeMigratingTopicToNextStage.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ChangeMigratingTopicToNextStageRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ChangeMigratingTopicToNextStageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeMigratingTopicToNextStage", params, headers=headers)
            response = json.loads(body)
            model = models.ChangeMigratingTopicToNextStageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConsumerGroup(self, request):
        r"""Create consumer groups.

        :param request: Request instance for CreateConsumerGroup.
        :type request: :class:`tencentcloud.trocket.v20230308.models.CreateConsumerGroupRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.CreateConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstance(self, request):
        r"""This API is used to create a RocketMQ 5.x cluster.

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.trocket.v20230308.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.CreateInstanceResponse`

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


    def CreateRole(self, request):
        r"""This API is used to add a role.

        :param request: Request instance for CreateRole.
        :type request: :class:`tencentcloud.trocket.v20230308.models.CreateRoleRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.CreateRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRole", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConsumerGroup(self, request):
        r"""This API is used to delete a consumer group. After a consumer group is deleted, all configurations and related data of the consumer group are cleared and cannot be restored. After deletion, online consumer clients report errors. It is recommended to take clients offline in advance.

        :param request: Request instance for DeleteConsumerGroup.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DeleteConsumerGroupRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DeleteConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstance(self, request):
        r"""This API is used to delete a TDMQ RocketMQ 5.x cluster. Topics, consumer groups, and roles in use should be deleted first.

        :param request: Request instance for DeleteInstance.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DeleteInstanceRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DeleteInstanceResponse`

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


    def DeleteRole(self, request):
        r"""This API is used to delete a role. Make sure that the related information on this role is not used in the current code. After the role is deleted, the keys (AccessKey and SecretKey) used to produce or consume messages with this role become invalid immediately.

        :param request: Request instance for DeleteRole.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DeleteRoleRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DeleteRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRole", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSmoothMigrationTask(self, request):
        r"""This API is used to delete a smooth migration task. Only canceled tasks can be deleted.

        :param request: Request instance for DeleteSmoothMigrationTask.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DeleteSmoothMigrationTaskRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DeleteSmoothMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSmoothMigrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSmoothMigrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTopic(self, request):
        r"""This API is used to delete a topic. After deletion, all configurations and related data of the topic will be cleared and cannot be restored.

        :param request: Request instance for DeleteTopic.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DeleteTopicRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DeleteTopicResponse`

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


    def DescribeConsumerClient(self, request):
        r"""Query consumer client details.

        :param request: Request instance for DescribeConsumerClient.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeConsumerClientRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeConsumerClientResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsumerClient", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsumerClientResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConsumerClientList(self, request):
        r"""This API is used to query the client connection list of a consumer group.

        :param request: Request instance for DescribeConsumerClientList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeConsumerClientListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeConsumerClientListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsumerClientList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsumerClientListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConsumerGroup(self, request):
        r"""Query consumer group details.

        :param request: Request instance for DescribeConsumerGroup.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeConsumerGroupRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeConsumerGroupResponse`

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


    def DescribeConsumerLag(self, request):
        r"""This API is used to query the number of heaped messages in a specified consumer group.

        :param request: Request instance for DescribeConsumerLag.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeConsumerLagRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeConsumerLagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsumerLag", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsumerLagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFusionInstanceList(self, request):
        r"""This API is used to describe clusters, supporting both 4.x and 5.x clusters. Among them, parameter usage of Filters is as follows:.

        -InstanceName, the cluster name, supports fuzzy query and can be obtained from the API return value or console.
        -InstanceId Cluster ID, exact query, obtain from the current API or console.
        - InstanceType cluster type, see [InstanceItem](https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#InstanceItem) data structure, supports multiple selections.
        - Version: cluster edition, enumeration values as follows:.
        -4 RocketMQ 4.x clusters.
        -Deploy a RocketMQ 5.x cluster.

        This API is used to demonstrate Filters.
         [{ "Name": "InstanceId", "Values": ["rmq-72mo3a9o"] }]

        :param request: Request instance for DescribeFusionInstanceList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeFusionInstanceListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeFusionInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFusionInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFusionInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstance(self, request):
        r"""This API is used to query RocketMQ 5.x cluster information.

        :param request: Request instance for DescribeInstance.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeInstanceRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeInstanceResponse`

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
        r"""This API is used to describe clusters. It only supports 5.x clusters. Description of the Filters parameter use is as follows:.

        -InstanceName Cluster name, supports fuzzy search.
        - InstanceId The Tencent Cloud RocketMQ instance ID, obtained from the [DescribeFusionInstanceList](https://www.tencentcloud.comom/document/api/1493/106745?from_cn_redirect=1) API or console.
        - InstanceType cluster type, see [InstanceItem](https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#InstanceItem) data structure, supports multiple selections.
        -InstanceStatus cluster status, see [InstanceItem](https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#InstanceItem) data structure, supports multiple selections.

        This API is used to demonstrate Filters.
        [{
            "Name": "InstanceId",
            "Values": ["rmq-72mo3a9o"]
        }]

        :param request: Request instance for DescribeInstanceList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeInstanceListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeInstanceListResponse`

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


    def DescribeMessage(self, request):
        r"""Query message details.

        :param request: Request instance for DescribeMessage.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMessageRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMessageList(self, request):
        r"""Query the message list. If querying dead letter messages, set the ConsumerGroup parameter.

        :param request: Request instance for DescribeMessageList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMessageListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMessageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMessageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMessageTrace(self, request):
        r"""This API is used to query message trace by message ID.

        :param request: Request instance for DescribeMessageTrace.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMessageTraceRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMessageTraceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessageTrace", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMessageTraceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigratingGroupStats(self, request):
        r"""This API is used to view real-time information of migration consumption groups.

        :param request: Request instance for DescribeMigratingGroupStats.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMigratingGroupStatsRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMigratingGroupStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigratingGroupStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigratingGroupStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigratingTopicList(self, request):
        r"""This API is used to query the Topic migration status list.

        The Filters field is a query filter that supports the following conditions:.
        This API is used to get topic names with fuzzy query support.
        This api is used to query the migration status. See the data structure in MigratingTopic (https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#MigratingTopic).
        This API is used to manage namespaces, valid only for 4.x clusters.

        This API is used to demonstrate Filters.
        [{
            "Name": "TopicName",
            "Values": ["topic-a"]
        }]

        :param request: Request instance for DescribeMigratingTopicList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMigratingTopicListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMigratingTopicListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigratingTopicList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigratingTopicListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigratingTopicStats(self, request):
        r"""This API is used to query real-time data of migration topics.

        :param request: Request instance for DescribeMigratingTopicStats.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMigratingTopicStatsRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMigratingTopicStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigratingTopicStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigratingTopicStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrationTaskList(self, request):
        r"""This API is used to search the data migration task list. Filter parameter usage instructions are as follows:.

        This API is used to search precisely according to task ID.
        InstanceId. This API is used to precisely search based on instance ID.
        This API is used to search by task Type.

        :param request: Request instance for DescribeMigrationTaskList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMigrationTaskListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMigrationTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrationTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrationTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProducerList(self, request):
        r"""This API is used to query producer list information associated with a topic. Filters support the following criteria:.
        -client IP.
        -client ID.

        :param request: Request instance for DescribeProducerList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeProducerListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeProducerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProducerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProducerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProductSKUs(self, request):
        r"""This API is used to query product sales specifications against RocketMQ 5.x clusters.

        :param request: Request instance for DescribeProductSKUs.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeProductSKUsRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeProductSKUsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductSKUs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductSKUsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoleList(self, request):
        r"""This API is used to query the list of roles. Filter parameter usage instructions are as follows:.

        -Role name supports fuzzy search and can be obtained from the API return value or console.
        -AccessKey, support fuzzy search, obtain from API return value or console.

        This API is used to demonstrate Filters.
        [{ "Name": "RoleName", "Values": ["test_role"] }]

        :param request: Request instance for DescribeRoleList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeRoleListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeRoleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSmoothMigrationTaskList(self, request):
        r"""This API is used to query the migration task list smoothly.

        This API is used to query the supported fields of the query parameter Filters as follows:.
        Task status, supports multiple selections.
        ConnectionType, network connection type, supports multiple selections. See the description of SmoothMigrationTaskItem (https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#SmoothMigrationTaskItem).
        This API is used to search for an instance by instance ID with precise matching.
        This API is used to query task names with fuzzy search support.

        This API is used to demonstrate Filters.
        [{
            "Name": "InstanceId",
            "Values": ["rmq-1gzecldfg"]
        }]

        :param request: Request instance for DescribeSmoothMigrationTaskList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeSmoothMigrationTaskListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeSmoothMigrationTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSmoothMigrationTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSmoothMigrationTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSourceClusterGroupList(self, request):
        r"""This API is used to obtain the group list of the source cluster during the smooth migration process.

        The Filters field is a query filter that supports the following fields:.
        This API is used to query consumer group names with fuzzy search support.
        This API is used to check whether the data is Imported.
        This api is used to check the import status. See SourceClusterGroupConfig (https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#SourceClusterGroupConfig) for details.
        This API is used to manage namespaces, valid only for 4.x clusters.

        This API is used to demonstrate Filters.
        [{
            "Name": "GroupName",
            "Values": ["group-a"]
        }]

        :param request: Request instance for DescribeSourceClusterGroupList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeSourceClusterGroupListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeSourceClusterGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSourceClusterGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSourceClusterGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopic(self, request):
        r"""This API is used to query topic details. The Offset and Limit parameters are pagination parameters for consumer groups subscribing to this topic. The Filter parameter usage instructions are as follows:.

        -The ConsumerGroup name can be obtained from the [ConsumeGroupItem](https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#ConsumeGroupItem) in the API response of [DescribeConsumerGroupList](https://www.tencentcloud.comom/document/api/1493/101535?from_cn_redirect=1) or from the console.

        This API is used to demonstrate Filters.
        [{ "Name": "ConsumerGroup", "Values": ["test_group"] }]

        :param request: Request instance for DescribeTopic.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeTopicRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeTopicResponse`

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


    def DescribeTopicList(self, request):
        r"""This API is used to search the topic list. Filter parameter usage instructions are as follows:.

        -TopicName supports fuzzy search. Obtain it from the [TopicItem](https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#TopicItem) in the [DescribeTopicList](https://www.tencentcloud.comom/document/api/1493/96030?from_cn_redirect=1) API response or the console.
        -Search by TopicType, support multiple selections. See the TopicType field in the [DescribeTopic](https://www.tencentcloud.comom/document/api/1493/97945?from_cn_redirect=1) API.

        This API is used to demonstrate Filters.
         [{ "Name": "TopicName", "Values": ["test_topic"] }]

        :param request: Request instance for DescribeTopicList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeTopicListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeTopicListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicListByGroup(self, request):
        r"""This API is used to get topic list by consumer group. Filter parameter usage instructions are as follows:.

        -TopicName. It can be obtained from [TopicItem](https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#TopicItem) returned by the API [DescribeTopicList](https://www.tencentcloud.comom/document/api/1493/96030?from_cn_redirect=1) or from the console.

        This API is used to demonstrate Filters.
        [{ "Name": "TopicName", "Values": ["test_topic"] }]

        :param request: Request instance for DescribeTopicListByGroup.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeTopicListByGroupRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeTopicListByGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicListByGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicListByGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DoHealthCheckOnMigratingTopic(self, request):
        r"""This API is used to check whether the topics being migrated are in normal status. Only topics in normal status can enter the next migration stage.

        :param request: Request instance for DoHealthCheckOnMigratingTopic.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DoHealthCheckOnMigratingTopicRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DoHealthCheckOnMigratingTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DoHealthCheckOnMigratingTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DoHealthCheckOnMigratingTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConsumerGroup(self, request):
        r"""Modify consumer group attributes.

        :param request: Request instance for ModifyConsumerGroup.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ModifyConsumerGroupRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ModifyConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstance(self, request):
        r"""This API is used to modify attributes of a TDMQ RocketMQ 5.x cluster. Only running clusters support this operation.

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ModifyInstanceResponse`

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


    def ModifyInstanceEndpoint(self, request):
        r"""This API is used to modify access points of a TDMQ RocketMQ 5.x cluster. Make sure that the access points exist before the operation.

        :param request: Request instance for ModifyInstanceEndpoint.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ModifyInstanceEndpointRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ModifyInstanceEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRole(self, request):
        r"""This API is used to modify a role.

        :param request: Request instance for ModifyRole.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ModifyRoleRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ModifyRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRole", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTopic(self, request):
        r"""Modify topic attributes.

        :param request: Request instance for ModifyTopic.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ModifyTopicRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ModifyTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTopic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveMigratingTopic(self, request):
        r"""This API is used to remove a topic from the migration list. It is valid only when the topic is in the initial state.

        :param request: Request instance for RemoveMigratingTopic.
        :type request: :class:`tencentcloud.trocket.v20230308.models.RemoveMigratingTopicRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.RemoveMigratingTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveMigratingTopic", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveMigratingTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResendDeadLetterMessage(self, request):
        r"""This API is used to resend dead letter messages.

        :param request: Request instance for ResendDeadLetterMessage.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ResendDeadLetterMessageRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ResendDeadLetterMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResendDeadLetterMessage", params, headers=headers)
            response = json.loads(body)
            model = models.ResendDeadLetterMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetConsumerGroupOffset(self, request):
        r"""Reset the consumption position.

        :param request: Request instance for ResetConsumerGroupOffset.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ResetConsumerGroupOffsetRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ResetConsumerGroupOffsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetConsumerGroupOffset", params, headers=headers)
            response = json.loads(body)
            model = models.ResetConsumerGroupOffsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackMigratingTopicStage(self, request):
        r"""This API is used to roll back the topic that is undergoing migration to the previous stage.

        :param request: Request instance for RollbackMigratingTopicStage.
        :type request: :class:`tencentcloud.trocket.v20230308.models.RollbackMigratingTopicStageRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.RollbackMigratingTopicStageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackMigratingTopicStage", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackMigratingTopicStageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))