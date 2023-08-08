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
from tencentcloud.autoscaling.v20180419 import models


class AutoscalingClient(AbstractClient):
    _apiVersion = '2018-04-19'
    _endpoint = 'as.tencentcloudapi.com'
    _service = 'as'


    def AttachInstances(self, request):
        """This API is used to add CVM instances to an auto scaling group.
        * Only CVM instances in `RUNNING` or `STOPPED` status can be added.
        * The added CVM instances must in the same VPC as the scaling group.

        :param request: Request instance for AttachInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.AttachInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.AttachInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachInstances", params, headers=headers)
            response = json.loads(body)
            model = models.AttachInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachLoadBalancers(self, request):
        """This API is used to add CLBs to a security group.

        :param request: Request instance for AttachLoadBalancers.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.AttachLoadBalancersRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.AttachLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.AttachLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ClearLaunchConfigurationAttributes(self, request):
        """This API is used to clear specific attributes of the launch configuration.

        :param request: Request instance for ClearLaunchConfigurationAttributes.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ClearLaunchConfigurationAttributesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ClearLaunchConfigurationAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearLaunchConfigurationAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ClearLaunchConfigurationAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CompleteLifecycleAction(self, request):
        """This API is used to complete a lifecycle action by setting the status of lifecycle hook to `CONTINUE` or `ABANDON`.

        * If this API is not called, the lifecycle hook goes to the status specified in `DefaultResult` after the timeout period.

        :param request: Request instance for CompleteLifecycleAction.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CompleteLifecycleActionRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CompleteLifecycleActionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CompleteLifecycleAction", params, headers=headers)
            response = json.loads(body)
            model = models.CompleteLifecycleActionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAutoScalingGroup(self, request):
        """This API (CreateAutoScalingGroup) is used to create an auto scaling group.

        :param request: Request instance for CreateAutoScalingGroup.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateAutoScalingGroupRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAutoScalingGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAutoScalingGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAutoScalingGroupFromInstance(self, request):
        """This API is used to create launch configurations and scaling groups based on an instance.

        Note: for a scaling group that is created based on a monthly-subscribed instance, the instances added for scale-out are pay-as-you-go instance.

        :param request: Request instance for CreateAutoScalingGroupFromInstance.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateAutoScalingGroupFromInstanceRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateAutoScalingGroupFromInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAutoScalingGroupFromInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAutoScalingGroupFromInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLaunchConfiguration(self, request):
        """This API is used to create a launch configuration.

        * To modify a launch configuration, please use `ModifyLaunchConfigurationAttributes`.

        * Up to 20 launch configurations can be created for each project. For more information, see [Usage Limits](https://intl.cloud.tencent.com/document/product/377/3120?from_cn_redirect=1).

        :param request: Request instance for CreateLaunchConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateLaunchConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateLaunchConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLaunchConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLaunchConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLifecycleHook(self, request):
        """This API is used to create a lifecycle hook.

        * You can configure notifications or automation commands (TAT) for the lifecycle hook.

        If you configured a notification, Auto Scaling will notify the TDMQ queue of the following information:

        ```
        {
        	"Service": "Tencent Cloud Auto Scaling",
        	"Time": "2019-03-14T10:15:11Z",
        	"AppId": "1251783334",
        	"ActivityId": "asa-fznnvrja",
        	"AutoScalingGroupId": "asg-rrrrtttt",
        	"LifecycleHookId": "ash-xxxxyyyy",
        	"LifecycleHookName": "my-hook",
        	"LifecycleActionToken": "3080e1c9-0efe-4dd7-ad3b-90cd6618298f",
        	"InstanceId": "ins-aaaabbbb",
        	"LifecycleTransition": "INSTANCE_LAUNCHING",
        	"NotificationMetadata": ""
        }
        ```

        :param request: Request instance for CreateLifecycleHook.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateLifecycleHookRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateLifecycleHookResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLifecycleHook", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLifecycleHookResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNotificationConfiguration(self, request):
        """This API is used to create a notification policy.
        When the notification is sent to a CMQ topic or queue, the following contents are included:
        ```
        {
            "Service": "Tencent Cloud Auto Scaling",
            "CreatedTime": "2021-10-11T10:15:11Z", // Activity creation time
            "AppId": "100000000",
            "ActivityId": "asa-fznnvrja", // Scaling activity ID
            "AutoScalingGroupId": "asg-pc2oqu2z", // Scaling group ID
            "ActivityType": "SCALE_OUT",  // Scaling activity type
            "StatusCode": "SUCCESSFUL",   // Scaling activity result
            "Description": "Activity was launched in response to a difference between desired capacity and actual capacity,
            scale out 1 instance(s).", // Scaling activity description
            "StartTime": "2021-10-11T10:15:11Z",  // Activity starting time
            "EndTime": "2021-10-11T10:15:32Z",    // Activity ending time
            "DetailedStatusMessageSet": [ // A collection of failed attempts during the scaling process (Failed attempts are allowed in a successful scaling activity)
                {
                    "Code": "InvalidInstanceType",
                    "Zone": "ap-guangzhou-2",
                    "InstanceId": "",
                    "InstanceChargeType": "POSTPAID_BY_HOUR",
                    "SubnetId": "subnet-4t5mgeuu",
                    "Message": "The specified instance type `S5.LARGE8` is invalid in `subnet-4t5mgeuu`, `ap-guangzhou-2`.",
                    "InstanceType": "S5.LARGE8",
                }
            ]
        }
        ```

        :param request: Request instance for CreateNotificationConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateNotificationConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateNotificationConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNotificationConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNotificationConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateScalingPolicy(self, request):
        """This API (CreateScalingPolicy) is used to create an alarm trigger policy.

        :param request: Request instance for CreateScalingPolicy.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateScalingPolicyRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScalingPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScalingPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateScheduledAction(self, request):
        """This API (CreateScheduledAction) is used to create a scheduled task.

        :param request: Request instance for CreateScheduledAction.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateScheduledActionRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateScheduledActionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScheduledAction", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScheduledActionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAutoScalingGroup(self, request):
        """This API is used to delete an auto-scaling group. Make sure that there are no `IN_SERVICE` instances in the group, and there are no ongoing scaling activities. When you delete a scaling group, instances in the status of `CREATION_FAILED`, `TERMINATION_FAILED` and `DETACH_FAILED` are not terminated.

        :param request: Request instance for DeleteAutoScalingGroup.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteAutoScalingGroupRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAutoScalingGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAutoScalingGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLaunchConfiguration(self, request):
        """This API (DeleteLaunchConfiguration) is used to delete a launch configuration.

        * If the launch configuration is active in an auto scaling group, it cannot be deleted.

        :param request: Request instance for DeleteLaunchConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteLaunchConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteLaunchConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLaunchConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLaunchConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLifecycleHook(self, request):
        """This API (DeleteLifeCycleHook) is used to delete a lifecycle hook.

        :param request: Request instance for DeleteLifecycleHook.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteLifecycleHookRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteLifecycleHookResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLifecycleHook", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLifecycleHookResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNotificationConfiguration(self, request):
        """This API (DeleteNotificationConfiguration) is used to delete the specified notification.

        :param request: Request instance for DeleteNotificationConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteNotificationConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteNotificationConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNotificationConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNotificationConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteScalingPolicy(self, request):
        """This API (DeleteScalingPolicy) is used to delete an alarm trigger policy.

        :param request: Request instance for DeleteScalingPolicy.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteScalingPolicyRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteScalingPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteScalingPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteScheduledAction(self, request):
        """This API (DeleteScheduledAction) is used to delete the specified scheduled task.

        :param request: Request instance for DeleteScheduledAction.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteScheduledActionRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteScheduledActionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteScheduledAction", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteScheduledActionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountLimits(self, request):
        """This API (DescribeAccountLimits) is used to query the limits of user's AS resources.

        :param request: Request instance for DescribeAccountLimits.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAccountLimitsRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAccountLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountLimits", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScalingActivities(self, request):
        """This API (DescribeAutoScalingActivities) is used to query the activity history of an auto scaling group.

        :param request: Request instance for DescribeAutoScalingActivities.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingActivitiesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingActivitiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScalingActivities", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScalingActivitiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScalingAdvices(self, request):
        """This API is used to query suggestions for scaling group configurations.

        :param request: Request instance for DescribeAutoScalingAdvices.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingAdvicesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingAdvicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScalingAdvices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScalingAdvicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScalingGroupLastActivities(self, request):
        """This API is used to query the latest activity history of an auto scaling group.

        :param request: Request instance for DescribeAutoScalingGroupLastActivities.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingGroupLastActivitiesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingGroupLastActivitiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScalingGroupLastActivities", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScalingGroupLastActivitiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScalingGroups(self, request):
        """This API (DescribeAutoScalingGroups) is used to query the information of auto scaling groups.

        * You can query the details of auto scaling groups based on information such as auto scaling group ID, auto scaling group name, or launch configuration ID. For more information on filters, see `Filter`.
        * If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of auto scaling groups of the current user will be returned.

        :param request: Request instance for DescribeAutoScalingGroups.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingGroupsRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScalingGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScalingGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScalingInstances(self, request):
        """This API (DescribeAutoScalingInstances) is used to query the information of instances associated with AS.

        * You can query the details of instances based on information such as instance ID and auto scaling group ID. For more information on filters, see `Filter`.
        * If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of instances of the current user will be returned.

        :param request: Request instance for DescribeAutoScalingInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScalingInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScalingInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLaunchConfigurations(self, request):
        """This API is used to query the information of launch configurations.

        * You can query the launch configuration details based on information such as launch configuration ID and name. For more information on filters, see `Filter`.
        * If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of launch configurations of the current user will be returned.

        :param request: Request instance for DescribeLaunchConfigurations.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeLaunchConfigurationsRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeLaunchConfigurationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLaunchConfigurations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLaunchConfigurationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLifecycleHooks(self, request):
        """This API (DescribeLifecycleHooks) is used to query the information of lifecycle hooks.

        * You can query the details of lifecycle hooks based on information such as auto scaling group ID, lifecycle hook ID, or lifecycle hook name. For more information on filters, see `Filter`.
        * If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of lifecycle hooks of the current user will be returned.

        :param request: Request instance for DescribeLifecycleHooks.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeLifecycleHooksRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeLifecycleHooksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLifecycleHooks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLifecycleHooksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotificationConfigurations(self, request):
        """This API (DescribeNotificationConfigurations) is used to query the information of one or more notifications.

        You can query the details of notifications based on information such as notification ID and auto scaling group ID. For more information on filters, see `Filter`.
        If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of notifications of the current user will be returned.

        :param request: Request instance for DescribeNotificationConfigurations.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeNotificationConfigurationsRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeNotificationConfigurationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotificationConfigurations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotificationConfigurationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScalingPolicies(self, request):
        """This API (DescribeScalingPolicies) is used to query alarm trigger policies.

        :param request: Request instance for DescribeScalingPolicies.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeScalingPoliciesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeScalingPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScalingPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScalingPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScheduledActions(self, request):
        """This API (DescribeScheduledActions) is used to query the details of one or more scheduled tasks.

        * You can query the details of scheduled tasks based on information such as scheduled task ID, scheduled task name, or auto scaling group ID. For more information on filters, see `Filter`.
        * If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of scheduled tasks of the current user will be returned.

        :param request: Request instance for DescribeScheduledActions.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeScheduledActionsRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeScheduledActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScheduledActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScheduledActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachInstances(self, request):
        """This API is used to remove CVM instances from a scaling group. Instances removed via this API will not be terminated.
        * If the number of remaining `IN_SERVICE` instances in the scaling group is less than the minimum capacity, this API will return an error.
        * However, if the scaling group is in `DISABLED` status, the removal will not verify the relationship between the number of `IN_SERVICE` instances and the minimum capacity.
        * This removal will unassociate the CVM from the CLB instance that has been configured for the scaling group.

        :param request: Request instance for DetachInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DetachInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DetachInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DetachInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachLoadBalancers(self, request):
        """This API is used to unbind one or more CLBs from a scaling group. This API will not terminate CLBs.

        :param request: Request instance for DetachLoadBalancers.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DetachLoadBalancersRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DetachLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.DetachLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableAutoScalingGroup(self, request):
        """This API is used to disable the specified auto-scaling group.
        * When a scaling group is disabled, the following activities are not triggered automatically:
            - Scaling activities triggered alert policies
            - Scaling activities triggered by desired group capacity
            - Replacement of unhealthy instances
            - Scheduled actions
        * When the scaling group is disabled, you can trigger scaling activities manually, including:
            - Scale out to the specify number of instances (ScaleOutInstances)
            - Scale in to the specify number of instances (ScaleInInstances)
            - Remove instances from the scaling group (DetachInstances)
            - Delete instances from the scaling group (RemoveInstances)
            - Add instances to a scaling group (AttachInstances)
            - Shut down CVM instances in a scaling group (StopAutoScalingInstances)
            - Start up CVM instances in a scaling group (StartAutoScalingInstances)

        :param request: Request instance for DisableAutoScalingGroup.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DisableAutoScalingGroupRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DisableAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableAutoScalingGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DisableAutoScalingGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableAutoScalingGroup(self, request):
        """This API (EnableAutoScalingGroup) is used to enable the specified auto scaling group.

        :param request: Request instance for EnableAutoScalingGroup.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.EnableAutoScalingGroupRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.EnableAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableAutoScalingGroup", params, headers=headers)
            response = json.loads(body)
            model = models.EnableAutoScalingGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExecuteScalingPolicy(self, request):
        """This API is used to execute a scaling policy.

        * The scaling policy can be executed based on the scaling policy ID.
        * The policy cannot be executed if there are ongoing scaling actions on the scaling group.
        * Executing a target tracking policy is not supported.

        :param request: Request instance for ExecuteScalingPolicy.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ExecuteScalingPolicyRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ExecuteScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExecuteScalingPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ExecuteScalingPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoScalingGroup(self, request):
        """This API (ModifyAutoScalingGroup) is used to modify an auto scaling group.

        :param request: Request instance for ModifyAutoScalingGroup.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyAutoScalingGroupRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoScalingGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoScalingGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDesiredCapacity(self, request):
        """This API (ModifyDesiredCapacity) is used to modify the desired number of instances in the specified auto scaling group.

        :param request: Request instance for ModifyDesiredCapacity.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyDesiredCapacityRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyDesiredCapacityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDesiredCapacity", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDesiredCapacityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLaunchConfigurationAttributes(self, request):
        """This API (ModifyLaunchConfigurationAttributes) is used to modify some attributes of a launch configuration.

        * The changes of launch configuration do not affect the existing instances. New instances will be created based on the modified configuration.
        * This API supports modifying certain simple types of attributes.

        :param request: Request instance for ModifyLaunchConfigurationAttributes.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyLaunchConfigurationAttributesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyLaunchConfigurationAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLaunchConfigurationAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLaunchConfigurationAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLifecycleHook(self, request):
        """This API is used to modify the lifecycle hook.

        :param request: Request instance for ModifyLifecycleHook.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyLifecycleHookRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyLifecycleHookResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLifecycleHook", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLifecycleHookResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoadBalancerTargetAttributes(self, request):
        """This API is used to modify the target rule attributes of the CLB in the scaling group.

        :param request: Request instance for ModifyLoadBalancerTargetAttributes.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyLoadBalancerTargetAttributesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyLoadBalancerTargetAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancerTargetAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancerTargetAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoadBalancers(self, request):
        """This API is used to modify the cloud load balancers of a scaling group.

        * This API can specify a new cloud load balancer configuration for the scaling group. The new configuration overwrites the original load balancer configuration.
        * To clear the cloud load balancer of the scaling group, specify only the scaling group ID but not the specific cloud load balancer.
        * This API modifies the cloud load balancer of the scaling group and generate a scaling activity to asynchronously modify the cloud load balancers of existing instances.

        :param request: Request instance for ModifyLoadBalancers.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyLoadBalancersRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNotificationConfiguration(self, request):
        """This API is used to modify a notification policy.
        * The receiver type of the notification policy cannot be modified.

        :param request: Request instance for ModifyNotificationConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyNotificationConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyNotificationConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNotificationConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNotificationConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyScalingPolicy(self, request):
        """This API (ModifyScalingPolicy) is used to modify an alarm trigger policy.

        :param request: Request instance for ModifyScalingPolicy.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyScalingPolicyRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyScalingPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyScalingPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyScheduledAction(self, request):
        """This API (ModifyScheduledAction) is used to modify a scheduled task.

        :param request: Request instance for ModifyScheduledAction.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyScheduledActionRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyScheduledActionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyScheduledAction", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyScheduledActionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveInstances(self, request):
        """This API is used to delete CVM instances from a scaling group. Instances that are automatically created through AS will be terminated, while those manually added to the scaling group will be removed and retained.
        * If the number of remaining `IN_SERVICE` instances in the scaling group is less than the minimum capacity, this API will return an error.
        * However, if the scaling group is in `DISABLED` status, the removal will not verify the relationship between the number of `IN_SERVICE` instances and the minimum capacity.
        * This removal will unassociate the CVM from the CLB instance that has been configured for the scaling group.

        :param request: Request instance for RemoveInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.RemoveInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.RemoveInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleInInstances(self, request):
        """This API is used to reduce the specified number of instances from the scaling group.
        * There is no on going scaling task.
        * This API is valid even when the scaling group is disabled. For more details, see [DisableAutoScalingGroup](https://intl.cloud.tencent.com/document/api/377/20435?from_cn_redirect=1).
        * You can specify the instances to remove in the scale-in activity by using `TerminationPolicies`. For more information, see [Scaling In Policies](https://intl.cloud.tencent.com/document/product/377/8563?from_cn_redirect=1).
        * Only the `IN_SERVICE` instances will be reduced. To reduce instances in other statues, use the [`DetachInstances`](https://intl.cloud.tencent.com/document/api/377/20436?from_cn_redirect=1) or [`RemoveInstances`](https://intl.cloud.tencent.com/document/api/377/20431?from_cn_redirect=1) API.
        * The desired capacity will be reduced accordingly. The new desired capacity should be no less than the minimum capacity.
        * If the scale-in activity failed or partially succeeded, the final desired capacity only deducts the instances that have been reduced successfully.

        :param request: Request instance for ScaleInInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ScaleInInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ScaleInInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleInInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleInInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleOutInstances(self, request):
        """This API is used to add the specified number of instances to a scaling group. It returns the scaling activity ID `ActivityId`.
        * u200dMake sure that there are no ongoing scaling tasks.
        * This API is valid even when the scaling group is disabled. For more details, see [DisableAutoScalingGroup](https://intl.cloud.tencent.com/document/api/377/20435?from_cn_redirect=1).
        * The total number of instances after this action cannot exceed the maximum capacity.
        * If a scale-out action failed or partially succeeded, only the number of successfully created instances is added to the number of desired capacity.
        * If the allocation policy is `SPOT_MIXED`, there may be multiple scaling activities triggered for one scaling task. u200dIn this case, the first activity ID (`ActivityId`) is returned.

        :param request: Request instance for ScaleOutInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ScaleOutInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ScaleOutInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleOutInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleOutInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetInstancesProtection(self, request):
        """This API is used to enable scale-in protection for an instance.
        When scale-in protection is enabled, the instance will not be removed in scale-in activities triggered by replacement of unhealthy instances, alarm threshold reached, change of desired quantity, etc.

        :param request: Request instance for SetInstancesProtection.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.SetInstancesProtectionRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.SetInstancesProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetInstancesProtection", params, headers=headers)
            response = json.loads(body)
            model = models.SetInstancesProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartAutoScalingInstances(self, request):
        """This API is used to start up CVM instances in a scaling group.
        * After startup, the instance will be in the `IN_SERVICE` status, which will increase the desired capacity. Please note that the desired capacity cannot exceed the maximum value.
        * This API supports batch operation. Up to 100 instances can be started up in each request.

        :param request: Request instance for StartAutoScalingInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.StartAutoScalingInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.StartAutoScalingInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartAutoScalingInstances", params, headers=headers)
            response = json.loads(body)
            model = models.StartAutoScalingInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopAutoScalingInstances(self, request):
        """This API is used to shut down CVM instances in a scaling group.
        * Use the `SOFT_FIRST` shutdown, which means the CVM will be forcibly shut down if the soft shutdown fails.
        * Shutting down instances in the `IN_SERVICE` status will reduce the desired capacity, but the desired capacity cannot be less than the minimum value.
        * To use the `STOP_CHARGING` shutdown, the instances you want to shut down must satisfy the conditions of [no charges when shut down](https://intl.cloud.tencent.com/document/product/213/19918?from_cn_redirect=1).
        * This API supports batch operation. Up to 100 instances can be shut down in each request.

        :param request: Request instance for StopAutoScalingInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.StopAutoScalingInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.StopAutoScalingInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopAutoScalingInstances", params, headers=headers)
            response = json.loads(body)
            model = models.StopAutoScalingInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeLaunchConfiguration(self, request):
        """This API is used to upgrade a launch configuration.

        * This API is used to upgrade a launch configuration in a "completely overriding" manner, i.e., it uniformly sets a new configuration according to the API parameters regardless of the original parameters. If optional fields are left empty, their default values will be used.
        * After the launch configuration is upgraded, the existing instances that have been created by it will not be changed, but new instances will be created according to the new configuration.

        :param request: Request instance for UpgradeLaunchConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.UpgradeLaunchConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.UpgradeLaunchConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeLaunchConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeLaunchConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeLifecycleHook(self, request):
        """This API (UpgradeLifecycleHook) is used to upgrade a lifecycle hook.

        * This API is used to upgrade a lifecycle hook in a "completely overriding" manner, i.e., it uniformly sets a new configuration according to the API parameters regardless of the original parameters. If optional fields are left empty, their default values will be used.

        :param request: Request instance for UpgradeLifecycleHook.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.UpgradeLifecycleHookRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.UpgradeLifecycleHookResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeLifecycleHook", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeLifecycleHookResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))