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
from tencentcloud.autoscaling.v20180419 import models
from typing import Dict


class AutoscalingClient(AbstractClient):
    _apiVersion = '2018-04-19'
    _endpoint = 'as.intl.tencentcloudapi.com'
    _service = 'as'

    async def AttachInstances(
            self,
            request: models.AttachInstancesRequest,
            opts: Dict = None,
    ) -> models.AttachInstancesResponse:
        """
        This interface (AttachInstances) is used to add CVM instances to a scaling group.
        * Only CVM instances in `RUNNING` or `STOPPED` status can be added.
        This API is used to ensure added CVM instances match the VPC network of the scaling group.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachLoadBalancers(
            self,
            request: models.AttachLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.AttachLoadBalancersResponse:
        """
        This API is used to add CLBs to a security group.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelInstanceRefresh(
            self,
            request: models.CancelInstanceRefreshRequest,
            opts: Dict = None,
    ) -> models.CancelInstanceRefreshResponse:
        """
        This API is used to cancel the instance refresh activity of the scaling group.
        * The batches that have already been refreshed remain unaffected, but the batches pending refresh will be canceled.
        * If a batch is currently refreshing, cancellation is not allowed. You can suspend the event and wait until the current batch finishes before canceling.
        This API is used to refresh the failed instances. If a refresh fails, the affected instances will remain in standby status, and require manual intervention to exit the standby status or terminate the instances.
        * Rollback operations are not allowed after cancellation, and recovery is unsupported.
        Temporarily expanded instances due to the maxSurge parameter are automatically destroyed after cancellation.
        * During scale-in, all instances have already been updated and cannot be canceled.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelInstanceRefresh"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelInstanceRefreshResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClearLaunchConfigurationAttributes(
            self,
            request: models.ClearLaunchConfigurationAttributesRequest,
            opts: Dict = None,
    ) -> models.ClearLaunchConfigurationAttributesResponse:
        """
        This API is used to clear specific attributes of the launch configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ClearLaunchConfigurationAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearLaunchConfigurationAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CompleteLifecycleAction(
            self,
            request: models.CompleteLifecycleActionRequest,
            opts: Dict = None,
    ) -> models.CompleteLifecycleActionResponse:
        """
        This API is used to complete a lifecycle action by setting the status of lifecycle hook to `CONTINUE` or `ABANDON`.

        * If this API is not called, the lifecycle hook goes to the status specified in `DefaultResult` after the timeout period.
        """
        
        kwargs = {}
        kwargs["action"] = "CompleteLifecycleAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompleteLifecycleActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAutoScalingGroup(
            self,
            request: models.CreateAutoScalingGroupRequest,
            opts: Dict = None,
    ) -> models.CreateAutoScalingGroupResponse:
        """
        This API (CreateAutoScalingGroup) is used to create an auto scaling group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAutoScalingGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAutoScalingGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAutoScalingGroupFromInstance(
            self,
            request: models.CreateAutoScalingGroupFromInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateAutoScalingGroupFromInstanceResponse:
        """
        This API is used to create launch configurations and scaling groups based on an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAutoScalingGroupFromInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAutoScalingGroupFromInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLaunchConfiguration(
            self,
            request: models.CreateLaunchConfigurationRequest,
            opts: Dict = None,
    ) -> models.CreateLaunchConfigurationResponse:
        """
        This interface (CreateLaunchConfiguration) is used to create new launch configuration.

        * To modify a launch configuration, use [ModifyLaunchConfigurationAttributes](https://intl.cloud.tencent.com/document/api/377/31298?from_cn_redirect=1) to partially modify fields. If needed, create a new launch configuration.

        By default, 50 launch configurations can be created per region. For details, see [Usage Limits](https://intl.cloud.tencent.com/document/product/377/3120?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLaunchConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLaunchConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLifecycleHook(
            self,
            request: models.CreateLifecycleHookRequest,
            opts: Dict = None,
    ) -> models.CreateLifecycleHookResponse:
        """
        This interface (CreateLifecycleHook) is used for creating a lifecycle hook.

        * You can configure notifications or automation commands for the lifecycle hook.

        If you configured a notification, Auto Scaling will notify the TDMQ Message Queue of the following information:.

        ```
        {
        	"Service": "Tencent Cloud Auto Scaling",
        	"Time": "2019-03-14T10:15:11Z",
        	"AppId": "1251783334",
        	"ActivityId": "asa-fznnvrja",
        	"AutoScalingGroupId": "asg-ft6y7u8n",
        	"LifecycleHookId": "ash-p9i7y6t5",
        	"LifecycleHookName": "my-hook",
        	"LifecycleActionToken": "3080e1c9-0efe-4dd7-ad3b-90cd6618298f",
        	"InstanceId": "ins-y6dr5e43",
        	"LifecycleTransition": "INSTANCE_LAUNCHING",
        	"NotificationMetadata": ""
        }
        ```
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLifecycleHook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLifecycleHookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNotificationConfiguration(
            self,
            request: models.CreateNotificationConfigurationRequest,
            opts: Dict = None,
    ) -> models.CreateNotificationConfigurationResponse:
        """
        This API is used to create a notification.
        This API is used to send notifications to a CMQ topic or queue with the following message content:.
        ```
        {
            "Service": "Tencent Cloud Auto Scaling",
        "CreatedTime": "2021-10-11T10:15:11Z", // Activity creation time.
            "AppId": "100000000",
        "ActivityId": "asa-fznnvrja", // scaling activity ID.
        This API is used to specify the scaling group ID.
        "ActivityType": "SCALE_OUT",  // scaling activity type.
        "StatusCode": "SUCCESSFUL".
            "Description": "Activity was launched in response to a difference between desired capacity and actual capacity,
        This API is used to scale out 1 instance.
        This API is used to set the activity start time.
        "EndTime": "2021-10-11T10:15:32Z",    // activity end time.
        "DetailedStatusMessageSet": [ // Collection of activity internal errors (non-empty does not mean activity failure).
                {
                    "Code": "InvalidInstanceType",
                    "Zone": "ap-guangzhou-6",
                    "InstanceId": "",
                    "InstanceChargeType": "POSTPAID_BY_HOUR",
                    "SubnetId": "subnet-4t5mgeuu",
                    "Message": "The specified instance type `S5.LARGE8` is invalid in `subnet-4t5mgeuu`, `ap-guangzhou-6`.",
                    "InstanceType": "S5.LARGE8"
                }
            ]
        }
        ```
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNotificationConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNotificationConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScalingPolicy(
            self,
            request: models.CreateScalingPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateScalingPolicyResponse:
        """
        This API (CreateScalingPolicy) is used to create an alarm trigger policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScalingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScalingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScheduledAction(
            self,
            request: models.CreateScheduledActionRequest,
            opts: Dict = None,
    ) -> models.CreateScheduledActionResponse:
        """
        This API (CreateScheduledAction) is used to create a scheduled task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScheduledAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScheduledActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAutoScalingGroup(
            self,
            request: models.DeleteAutoScalingGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteAutoScalingGroupResponse:
        """
        This API is used to delete an auto-scaling group. Make sure that there are no `IN_SERVICE` instances in the group, and there are no ongoing scaling activities. When you delete a scaling group, instances in the status of `CREATION_FAILED`, `TERMINATION_FAILED` and `DETACH_FAILED` are not terminated.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAutoScalingGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAutoScalingGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLaunchConfiguration(
            self,
            request: models.DeleteLaunchConfigurationRequest,
            opts: Dict = None,
    ) -> models.DeleteLaunchConfigurationResponse:
        """
        This API (DeleteLaunchConfiguration) is used to delete a launch configuration.

        * If the launch configuration is active in a scaling group, it cannot be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLaunchConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLaunchConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLifecycleHook(
            self,
            request: models.DeleteLifecycleHookRequest,
            opts: Dict = None,
    ) -> models.DeleteLifecycleHookResponse:
        """
        This API (DeleteLifeCycleHook) is used to delete a lifecycle hook.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLifecycleHook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLifecycleHookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNotificationConfiguration(
            self,
            request: models.DeleteNotificationConfigurationRequest,
            opts: Dict = None,
    ) -> models.DeleteNotificationConfigurationResponse:
        """
        This API (DeleteNotificationConfiguration) is used to delete the specified notification.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNotificationConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNotificationConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteScalingPolicy(
            self,
            request: models.DeleteScalingPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteScalingPolicyResponse:
        """
        This API (DeleteScalingPolicy) is used to delete an alarm trigger policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteScalingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteScalingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteScheduledAction(
            self,
            request: models.DeleteScheduledActionRequest,
            opts: Dict = None,
    ) -> models.DeleteScheduledActionResponse:
        """
        This API (DeleteScheduledAction) is used to delete the specified scheduled task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteScheduledAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteScheduledActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountLimits(
            self,
            request: models.DescribeAccountLimitsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountLimitsResponse:
        """
        This API (DescribeAccountLimits) is used to query the limits of user's AS resources.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScalingActivities(
            self,
            request: models.DescribeAutoScalingActivitiesRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScalingActivitiesResponse:
        """
        This API (DescribeAutoScalingActivities) is used to query the activity history of an auto scaling group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScalingActivities"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScalingActivitiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScalingAdvices(
            self,
            request: models.DescribeAutoScalingAdvicesRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScalingAdvicesResponse:
        """
        This API is used to query suggestions for scaling group configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScalingAdvices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScalingAdvicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScalingGroupLastActivities(
            self,
            request: models.DescribeAutoScalingGroupLastActivitiesRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScalingGroupLastActivitiesResponse:
        """
        This API is used to query the latest activity history of an auto scaling group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScalingGroupLastActivities"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScalingGroupLastActivitiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScalingGroups(
            self,
            request: models.DescribeAutoScalingGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScalingGroupsResponse:
        """
        This API (DescribeAutoScalingGroups) is used to query the information of auto scaling groups.

        * You can query the details of auto scaling groups based on information such as auto scaling group ID, auto scaling group name, or launch configuration ID. For more information on filters, see `Filter`.
        * If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of auto scaling groups of the current user will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScalingGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScalingGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScalingInstances(
            self,
            request: models.DescribeAutoScalingInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScalingInstancesResponse:
        """
        This API (DescribeAutoScalingInstances) is used to query the information of instances associated with AS.

        * You can query the details of instances based on information such as instance ID and auto scaling group ID. For more information on filters, see `Filter`.
        * If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of instances of the current user will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScalingInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScalingInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLaunchConfigurations(
            self,
            request: models.DescribeLaunchConfigurationsRequest,
            opts: Dict = None,
    ) -> models.DescribeLaunchConfigurationsResponse:
        """
        This API is used to query the information of launch configurations.

        * You can query the launch configuration details based on information such as launch configuration ID and name. For more information on filters, see `Filter`.
        * If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of launch configurations of the current user will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLaunchConfigurations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLaunchConfigurationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLifecycleHooks(
            self,
            request: models.DescribeLifecycleHooksRequest,
            opts: Dict = None,
    ) -> models.DescribeLifecycleHooksResponse:
        """
        This API (DescribeLifecycleHooks) is used to query the information of lifecycle hooks.

        * You can query the details of lifecycle hooks based on information such as auto scaling group ID, lifecycle hook ID, or lifecycle hook name. For more information on filters, see `Filter`.
        * If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of lifecycle hooks of the current user will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLifecycleHooks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLifecycleHooksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotificationConfigurations(
            self,
            request: models.DescribeNotificationConfigurationsRequest,
            opts: Dict = None,
    ) -> models.DescribeNotificationConfigurationsResponse:
        """
        This API (DescribeNotificationConfigurations) is used to query the information of one or more notifications.

        You can query the details of notifications based on information such as notification ID and auto scaling group ID. For more information on filters, see `Filter`.
        If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of notifications of the current user will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotificationConfigurations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotificationConfigurationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRefreshActivities(
            self,
            request: models.DescribeRefreshActivitiesRequest,
            opts: Dict = None,
    ) -> models.DescribeRefreshActivitiesResponse:
        """
        This API (DescribeRefreshActivities) is used to query the instance refresh activity records of a scaling group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRefreshActivities"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRefreshActivitiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScalingPolicies(
            self,
            request: models.DescribeScalingPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeScalingPoliciesResponse:
        """
        This API (DescribeScalingPolicies) is used to query alarm trigger policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScalingPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScalingPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScheduledActions(
            self,
            request: models.DescribeScheduledActionsRequest,
            opts: Dict = None,
    ) -> models.DescribeScheduledActionsResponse:
        """
        This API (DescribeScheduledActions) is used to query the details of one or more scheduled tasks.

        * You can query the details of scheduled tasks based on information such as scheduled task ID, scheduled task name, or auto scaling group ID. For more information on filters, see `Filter`.
        * If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of scheduled tasks of the current user will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScheduledActions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScheduledActionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachInstances(
            self,
            request: models.DetachInstancesRequest,
            opts: Dict = None,
    ) -> models.DetachInstancesResponse:
        """
        This API is used to remove CVM instances from a scaling group. Instances removed via this API will not be terminated.
        * If the number of remaining `IN_SERVICE` instances in the scaling group is less than the minimum capacity, this API will return an error.
        * However, if the scaling group is in `DISABLED` status, the removal will not verify the relationship between the number of `IN_SERVICE` instances and the minimum capacity.
        * This removal will unassociate the CVM from the CLB instance that has been configured for the scaling group.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachLoadBalancers(
            self,
            request: models.DetachLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.DetachLoadBalancersResponse:
        """
        This API is used to unbind one or more CLBs from a scaling group. This API will not terminate CLBs.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableAutoScalingGroup(
            self,
            request: models.DisableAutoScalingGroupRequest,
            opts: Dict = None,
    ) -> models.DisableAutoScalingGroupResponse:
        """
        This API is used to disable the specified auto-scaling group.
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
        """
        
        kwargs = {}
        kwargs["action"] = "DisableAutoScalingGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableAutoScalingGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableAutoScalingGroup(
            self,
            request: models.EnableAutoScalingGroupRequest,
            opts: Dict = None,
    ) -> models.EnableAutoScalingGroupResponse:
        """
        This API (EnableAutoScalingGroup) is used to enable the specified auto scaling group.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableAutoScalingGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableAutoScalingGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnterStandby(
            self,
            request: models.EnterStandbyRequest,
            opts: Dict = None,
    ) -> models.EnterStandbyResponse:
        """
        This API is used to set instances within the scaling group to standby status.
        Instances in standby status have a CLB weight value of 0 and will not be selected for scaling in, unhealthy replacement, or refresh operation.
        This API is used to call the Auto Scaling power-on/power-off API which may change the standby status, while the Cloud Virtual Machine server power on/off API will not affect it.
        The instance enters standby status, and the scaling group attempts to lower the expected number of instances, which will not be less than the minimum value.
        """
        
        kwargs = {}
        kwargs["action"] = "EnterStandby"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnterStandbyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExecuteScalingPolicy(
            self,
            request: models.ExecuteScalingPolicyRequest,
            opts: Dict = None,
    ) -> models.ExecuteScalingPolicyResponse:
        """
        This API is used to execute a scaling policy.

        * The scaling policy can be executed based on the scaling policy ID.
        * The policy cannot be executed if there are ongoing scaling actions on the scaling group.
        * Executing a target tracking policy is not supported.
        """
        
        kwargs = {}
        kwargs["action"] = "ExecuteScalingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExecuteScalingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExitStandby(
            self,
            request: models.ExitStandbyRequest,
            opts: Dict = None,
    ) -> models.ExitStandbyResponse:
        """
        This API is used to exit instances from standby status in the scaling group.
        * After exiting standby status, the instance enters running state and the CLB weight value is restored to the default value.
        This API is used to call the Auto Scaling power-on/power-off API which may change the standby status, while the Cloud Virtual Machine server power on/off API will not affect it.
        After instances exit standby status, the scaling group will raise the expected number of instances. The new expected number cannot exceed the maximum value.
        """
        
        kwargs = {}
        kwargs["action"] = "ExitStandby"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExitStandbyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoScalingGroup(
            self,
            request: models.ModifyAutoScalingGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoScalingGroupResponse:
        """
        This API (ModifyAutoScalingGroup) is used to modify an auto scaling group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoScalingGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoScalingGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDesiredCapacity(
            self,
            request: models.ModifyDesiredCapacityRequest,
            opts: Dict = None,
    ) -> models.ModifyDesiredCapacityResponse:
        """
        This API (ModifyDesiredCapacity) is used to modify the desired number of instances in the specified auto scaling group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDesiredCapacity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDesiredCapacityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLaunchConfigurationAttributes(
            self,
            request: models.ModifyLaunchConfigurationAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyLaunchConfigurationAttributesResponse:
        """
        This API (ModifyLaunchConfigurationAttributes) is used to modify part of a launch configuration's attributes.

        This API is used to modify the startup configuration. Existing instances scaled out using this configuration will not change, while newly added instances using this launch configuration will scale out according to the new configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLaunchConfigurationAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLaunchConfigurationAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLifecycleHook(
            self,
            request: models.ModifyLifecycleHookRequest,
            opts: Dict = None,
    ) -> models.ModifyLifecycleHookResponse:
        """
        This API is used to modify the lifecycle hook.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLifecycleHook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLifecycleHookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancerTargetAttributes(
            self,
            request: models.ModifyLoadBalancerTargetAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancerTargetAttributesResponse:
        """
        This API is used to modify the target rule attributes of the CLB in the scaling group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancerTargetAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancerTargetAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancers(
            self,
            request: models.ModifyLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancersResponse:
        """
        This API is used to modify the cloud load balancers of a scaling group.

        * This API can specify a new cloud load balancer configuration for the scaling group. The new configuration overwrites the original load balancer configuration.
        * To clear the cloud load balancer of the scaling group, specify only the scaling group ID but not the specific cloud load balancer.
        * This API modifies the cloud load balancer of the scaling group and generate a scaling activity to asynchronously modify the cloud load balancers of existing instances.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNotificationConfiguration(
            self,
            request: models.ModifyNotificationConfigurationRequest,
            opts: Dict = None,
    ) -> models.ModifyNotificationConfigurationResponse:
        """
        This API is used to modify a notification policy.
        * The receiver type of the notification policy cannot be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNotificationConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNotificationConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyScalingPolicy(
            self,
            request: models.ModifyScalingPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyScalingPolicyResponse:
        """
        This API (ModifyScalingPolicy) is used to modify an alarm trigger policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyScalingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyScalingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyScheduledAction(
            self,
            request: models.ModifyScheduledActionRequest,
            opts: Dict = None,
    ) -> models.ModifyScheduledActionResponse:
        """
        This API (ModifyScheduledAction) is used to modify a scheduled task.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyScheduledAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyScheduledActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveInstances(
            self,
            request: models.RemoveInstancesRequest,
            opts: Dict = None,
    ) -> models.RemoveInstancesResponse:
        """
        This API is used to delete CVM instances from a scaling group. Instances that are automatically created through AS will be terminated, while those manually added to the scaling group will be removed and retained.
        * If the number of remaining `IN_SERVICE` instances in the scaling group is less than the minimum capacity, this API will return an error.
        * However, if the scaling group is in `DISABLED` status, the removal will not verify the relationship between the number of `IN_SERVICE` instances and the minimum capacity.
        * This removal will unassociate the CVM from the CLB instance that has been configured for the scaling group.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeInstanceRefresh(
            self,
            request: models.ResumeInstanceRefreshRequest,
            opts: Dict = None,
    ) -> models.ResumeInstanceRefreshResponse:
        """
        This API is used to resume the paused instance refresh activity, allowing it to retry failed instances in the current batch or proceed with refreshing subsequent batches. Note that calling this API is ineffective when the activity is not in a paused status.

        - When the MaxSurge parameter is used, the activity may be paused due to scale-out or scale-in failures. This API can also be used to retry scaling operations.
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeInstanceRefresh"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeInstanceRefreshResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackInstanceRefresh(
            self,
            request: models.RollbackInstanceRefreshRequest,
            opts: Dict = None,
    ) -> models.RollbackInstanceRefreshResponse:
        """
        This API is used to generate a new instance refresh activity, which also supports batch refreshing and operations such as pausing, resuming, and canceling. This API returns RefreshActivityId for the rollback activity.
        * The instances pending refresh in the original activity are updated to canceled status. Nonexistent instances are disregarded, while instances in all other statuses proceed to enter the rollback process.
        * The instances that are being refreshed in the original activity will not be immediately terminated. Instead, the rollback activity will be executed after their refresh complete.
        * Rollback is supported for activities that are in the paused status or those succeeded in refreshing last time. It is not supported for activities in other statuses.
        * When the original refresh activity involves reinstalling instances, for the ImageId parameter, it will automatically recover to the image ID before the rollback; for parameters such as UserData, EnhancedService, LoginSettings, and HostName, they will still be read from the launch configuration, requiring users to manually modify the launch configuration before initiating the rollback.
        * The rollback activity does not support the MaxSurge parameter currently.
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackInstanceRefresh"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackInstanceRefreshResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleInInstances(
            self,
            request: models.ScaleInInstancesRequest,
            opts: Dict = None,
    ) -> models.ScaleInInstancesResponse:
        """
        This API is used to reduce the specified number of instances from the scaling group.
        * There is no on going scaling task.
        * This API is valid even when the scaling group is disabled. For more details, see [DisableAutoScalingGroup](https://intl.cloud.tencent.com/document/api/377/20435?from_cn_redirect=1).
        * You can specify the instances to remove in the scale-in activity by using `TerminationPolicies`. For more information, see [Scaling In Policies](https://intl.cloud.tencent.com/document/product/377/8563?from_cn_redirect=1).
        * Only the `IN_SERVICE` instances will be reduced. To reduce instances in other statues, use the [`DetachInstances`](https://intl.cloud.tencent.com/document/api/377/31011?from_cn_redirect=1) or [`RemoveInstances`](https://intl.cloud.tencent.com/document/api/377/31005?from_cn_redirect=1) API.
        * The desired capacity will be reduced accordingly. The new desired capacity should be no less than the minimum capacity.
        * If the scale-in activity failed or partially succeeded, the final desired capacity only deducts the instances that have been reduced successfully.
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleInInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleInInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleOutInstances(
            self,
            request: models.ScaleOutInstancesRequest,
            opts: Dict = None,
    ) -> models.ScaleOutInstancesResponse:
        """
        This API is used to add the specified number of instances to a scaling group. It returns the scaling activity ID `ActivityId`.
        * Make sure that there are no ongoing scaling tasks.
        * This API is valid even when the scaling group is disabled. For more details, see [DisableAutoScalingGroup](https://intl.cloud.tencent.com/document/api/377/20435?from_cn_redirect=1).
        * The total number of instances after this action cannot exceed the maximum capacity.
        * If a scale-out action failed or partially succeeded, only the number of successfully created instances is added to the number of desired capacity.
        * If the allocation policy is `SPOT_MIXED`, there may be multiple scaling activities triggered for one scaling task. In this case, the first activity ID (`ActivityId`) is returned.
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleOutInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleOutInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetInstancesProtection(
            self,
            request: models.SetInstancesProtectionRequest,
            opts: Dict = None,
    ) -> models.SetInstancesProtectionResponse:
        """
        This API is used to enable scale-in protection for an instance.
        When scale-in protection is enabled, the instance will not be removed in scale-in activities triggered by replacement of unhealthy instances, alarm threshold reached, change of desired quantity, etc.
        """
        
        kwargs = {}
        kwargs["action"] = "SetInstancesProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetInstancesProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartAutoScalingInstances(
            self,
            request: models.StartAutoScalingInstancesRequest,
            opts: Dict = None,
    ) -> models.StartAutoScalingInstancesResponse:
        """
        This API is used to start up CVM instances in a scaling group.
        * After startup, the instance will be in the `IN_SERVICE` status, which will increase the desired capacity. Please note that the desired capacity cannot exceed the maximum value.
        * This API supports batch operation. Up to 100 instances can be started up in each request.
        """
        
        kwargs = {}
        kwargs["action"] = "StartAutoScalingInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartAutoScalingInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartInstanceRefresh(
            self,
            request: models.StartInstanceRefreshRequest,
            opts: Dict = None,
    ) -> models.StartInstanceRefreshResponse:
        """
        This API is used to refresh running CVM instances in the scaling group and return the RefreshActivityId for the instance refresh activity based on parameters in the launch configuration.
        * For refresh methods involving reinstallation (currently only reinstallation is supported), during reinstallation, only the ImageId, UserData, EnhancedService, HostName, and LoginSettings parameters will be fetched from the launch configuration for refreshing; other parameters of the instance will not be refreshed.
        * During the instance refresh process (including paused status), the scaling group will be disabled. It is not recommended to modify the associated launch configuration during a refresh, as this may impact the refresh parameters, leading to inconsistent instance configurations.
        * In rolling update mode, instance refreshes are performed in multiple batches. If there are failed refreshes within a batch, the activity will enter a failed paused status.
        * Instances pending refresh that are removed or destroyed will be marked as NOT_FOUND status, but they will not block the instance refresh activity.
        * Even if a running instance has parameters consistent with the latest launch configuration, it can still undergo another refresh.
        """
        
        kwargs = {}
        kwargs["action"] = "StartInstanceRefresh"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartInstanceRefreshResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopAutoScalingInstances(
            self,
            request: models.StopAutoScalingInstancesRequest,
            opts: Dict = None,
    ) -> models.StopAutoScalingInstancesResponse:
        """
        This API is used to shut down CVM instances in a scaling group.
        * Use the `SOFT_FIRST` shutdown, which means the CVM will be forcibly shut down if the soft shutdown fails.
        * Shutting down instances in the `IN_SERVICE` status will reduce the desired capacity, but the desired capacity cannot be less than the minimum value.
        * To use the `STOP_CHARGING` shutdown, the instances you want to shut down must satisfy the conditions of [no charges when shut down](https://intl.cloud.tencent.com/document/product/213/19918?from_cn_redirect=1).
        * This API supports batch operation. Up to 100 instances can be shut down in each request.
        """
        
        kwargs = {}
        kwargs["action"] = "StopAutoScalingInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopAutoScalingInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopInstanceRefresh(
            self,
            request: models.StopInstanceRefreshRequest,
            opts: Dict = None,
    ) -> models.StopInstanceRefreshResponse:
        """
        This API is used to pause the ongoing instance refresh activity.
        * In the paused status, the scaling group will also be disabled.
        * The instances that are currently being updated or scaled out will not be paused, but instances pending updates will have their updates paused.
        * During scale-in, all instances have already been updated and cannot be paused.
        """
        
        kwargs = {}
        kwargs["action"] = "StopInstanceRefresh"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopInstanceRefreshResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeLaunchConfiguration(
            self,
            request: models.UpgradeLaunchConfigurationRequest,
            opts: Dict = None,
    ) -> models.UpgradeLaunchConfigurationResponse:
        """
        There is a replacement API: ModifyLaunchConfiguration. This API carries the risk of parameter overwriting, and it has currently been hidden on the official website.
        This API (UpgradeLaunchConfiguration) is used to upgrade the launch configuration.
        * This API is used to upgrade the launch configuration, adopting an "entirely overwrite" approach. Regardless of previous parameter settings, they will be uniformly replaced with new configurations as specified in the interface parameters. For non-mandatory fields, if not filled in, default values will be assigned.
        * After upgrading and modifying the launch configuration, existing instances that have been scaled out using this configuration will not undergo any changes. Subsequently, newly added instances using this upgraded launch configuration will be scaled out according to the new configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeLaunchConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeLaunchConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeLifecycleHook(
            self,
            request: models.UpgradeLifecycleHookRequest,
            opts: Dict = None,
    ) -> models.UpgradeLifecycleHookResponse:
        """
        This API is used to upgrade the lifecycle hook.

        * This API is used to upgrade the lifecycle hook, adopting a "comprehensive overwrite" style. Regardless of how the previous parameters were set, it uniformly uses the new configurations for API parameters. For optional fields, if they are not filled in, default values will be used.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeLifecycleHook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeLifecycleHookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)