# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class Activity(AbstractModel):
    """Information on eligible scaling activities.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID.
        :type AutoScalingGroupId: str
        :param ActivityId: Scaling activity ID.
        :type ActivityId: str
        :param ActivityType: Scaling activity type. Value range:<br>
<li>SCALE_OUT: scale-out <li>SCALE_IN: scale-in <li>ATTACH_INSTANCES: adding an instance <li>REMOVE_INSTANCES: terminating an instance <li>DETACH_INSTANCES: removing an instance <li>TERMINATE_INSTANCES_UNEXPECTEDLY: terminating an instance in the CVM console <li>REPLACE_UNHEALTHY_INSTANCE: replacing an unhealthy instance
        :type ActivityType: str
        :param StatusCode: Scaling activity status. Value range:<br>
<li>INIT: initializing
<li>RUNNING: running
<li>SUCCESSFUL: succeeded
<li>PARTIALLY_SUCCESSFUL: partially succeeded
<li>FAILED: failed
<li>CANCELLED: canceled
        :type StatusCode: str
        :param StatusMessage: Description of the scaling activity status.
        :type StatusMessage: str
        :param Cause: Cause of the scaling activity.
        :type Cause: str
        :param Description: Description of the scaling activity.
        :type Description: str
        :param StartTime: Start time of the scaling activity.
        :type StartTime: str
        :param EndTime: End time of the scaling activity.
        :type EndTime: str
        :param CreatedTime: Creation time of the scaling activity.
        :type CreatedTime: str
        :param ActivityRelatedInstanceSet: Information set of the instances related to the scaling activity.
        :type ActivityRelatedInstanceSet: list of ActivtyRelatedInstance
        :param StatusMessageSimplified: Brief description of the scaling activity status.
        :type StatusMessageSimplified: str
        :param LifecycleActionResultSet: Result of the lifecycle hook action in the scaling activity
        :type LifecycleActionResultSet: list of LifecycleActionResultInfo
        """
        self.AutoScalingGroupId = None
        self.ActivityId = None
        self.ActivityType = None
        self.StatusCode = None
        self.StatusMessage = None
        self.Cause = None
        self.Description = None
        self.StartTime = None
        self.EndTime = None
        self.CreatedTime = None
        self.ActivityRelatedInstanceSet = None
        self.StatusMessageSimplified = None
        self.LifecycleActionResultSet = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.ActivityId = params.get("ActivityId")
        self.ActivityType = params.get("ActivityType")
        self.StatusCode = params.get("StatusCode")
        self.StatusMessage = params.get("StatusMessage")
        self.Cause = params.get("Cause")
        self.Description = params.get("Description")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("ActivityRelatedInstanceSet") is not None:
            self.ActivityRelatedInstanceSet = []
            for item in params.get("ActivityRelatedInstanceSet"):
                obj = ActivtyRelatedInstance()
                obj._deserialize(item)
                self.ActivityRelatedInstanceSet.append(obj)
        self.StatusMessageSimplified = params.get("StatusMessageSimplified")
        if params.get("LifecycleActionResultSet") is not None:
            self.LifecycleActionResultSet = []
            for item in params.get("LifecycleActionResultSet"):
                obj = LifecycleActionResultInfo()
                obj._deserialize(item)
                self.LifecycleActionResultSet.append(obj)


class ActivtyRelatedInstance(AbstractModel):
    """Information of the instances related to the current scaling activity.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param InstanceStatus: Status of the instance in the scaling activity. Value range:
<li>INIT: initializing
<li>RUNNING: running
<li>SUCCESSFUL: succeeded
<li>FAILED: failed
        :type InstanceStatus: str
        """
        self.InstanceId = None
        self.InstanceStatus = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceStatus = params.get("InstanceStatus")


class AttachInstancesRequest(AbstractModel):
    """AttachInstances request structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param InstanceIds: List of CVM instance IDs
        :type InstanceIds: list of str
        """
        self.AutoScalingGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.InstanceIds = params.get("InstanceIds")


class AttachInstancesResponse(AbstractModel):
    """AttachInstances response structure.

    """

    def __init__(self):
        """
        :param ActivityId: Scaling activity ID
        :type ActivityId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ActivityId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.RequestId = params.get("RequestId")


class AutoScalingGroup(AbstractModel):
    """Auto scaling group

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param AutoScalingGroupName: Auto scaling group name
        :type AutoScalingGroupName: str
        :param AutoScalingGroupStatus: Current status of the auto scaling group. Value range: <br><li>NORMAL: normal <br><li>CVM_ABNORMAL: Exception with the launch configuration <br><li>LB_ABNORMAL: exception with the load balancer <br><li>VPC_ABNORMAL: exception with the VPC <br><li>INSUFFICIENT_BALANCE: insufficient balance <br><li>LB_BACKEND_REGION_NOT_MATCH: the backend region of the CLB instance is not the same as the one of AS service.<br>
        :type AutoScalingGroupStatus: str
        :param CreatedTime: Creation time in UTC format
        :type CreatedTime: str
        :param DefaultCooldown: Default cooldown period in seconds
        :type DefaultCooldown: int
        :param DesiredCapacity: Desired number of instances
        :type DesiredCapacity: int
        :param EnabledStatus: Enabled status. Value range: `ENABLED`, `DISABLED`
        :type EnabledStatus: str
        :param ForwardLoadBalancerSet: List of application load balancers
        :type ForwardLoadBalancerSet: list of ForwardLoadBalancer
        :param InstanceCount: Number of instances
        :type InstanceCount: int
        :param InServiceInstanceCount: Number of instances in `IN_SERVICE` status
        :type InServiceInstanceCount: int
        :param LaunchConfigurationId: Launch configuration ID
        :type LaunchConfigurationId: str
        :param LaunchConfigurationName: Launch configuration name
        :type LaunchConfigurationName: str
        :param LoadBalancerIdSet: List of Classic load balancer IDs
        :type LoadBalancerIdSet: list of str
        :param MaxSize: Maximum number of instances
        :type MaxSize: int
        :param MinSize: Minimum number of instances
        :type MinSize: int
        :param ProjectId: Project ID
        :type ProjectId: int
        :param SubnetIdSet: List of subnet IDs
        :type SubnetIdSet: list of str
        :param TerminationPolicySet: Termination policy
        :type TerminationPolicySet: list of str
        :param VpcId: VPC ID
        :type VpcId: str
        :param ZoneSet: List of availability zones
        :type ZoneSet: list of str
        :param RetryPolicy: Retry policy
        :type RetryPolicy: str
        :param InActivityStatus: Whether the auto scaling group is performing a scaling activity. `IN_ACTIVITY` indicates yes, and `NOT_IN_ACTIVITY` indicates no.
        :type InActivityStatus: str
        :param Tags: List of auto scaling group tags
        :type Tags: list of Tag
        :param ServiceSettings: Service settings
        :type ServiceSettings: :class:`tencentcloud.autoscaling.v20180419.models.ServiceSettings`
        :param Ipv6AddressCount: 
        :type Ipv6AddressCount: int
        :param MultiZoneSubnetPolicy: 
        :type MultiZoneSubnetPolicy: str
        """
        self.AutoScalingGroupId = None
        self.AutoScalingGroupName = None
        self.AutoScalingGroupStatus = None
        self.CreatedTime = None
        self.DefaultCooldown = None
        self.DesiredCapacity = None
        self.EnabledStatus = None
        self.ForwardLoadBalancerSet = None
        self.InstanceCount = None
        self.InServiceInstanceCount = None
        self.LaunchConfigurationId = None
        self.LaunchConfigurationName = None
        self.LoadBalancerIdSet = None
        self.MaxSize = None
        self.MinSize = None
        self.ProjectId = None
        self.SubnetIdSet = None
        self.TerminationPolicySet = None
        self.VpcId = None
        self.ZoneSet = None
        self.RetryPolicy = None
        self.InActivityStatus = None
        self.Tags = None
        self.ServiceSettings = None
        self.Ipv6AddressCount = None
        self.MultiZoneSubnetPolicy = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.AutoScalingGroupName = params.get("AutoScalingGroupName")
        self.AutoScalingGroupStatus = params.get("AutoScalingGroupStatus")
        self.CreatedTime = params.get("CreatedTime")
        self.DefaultCooldown = params.get("DefaultCooldown")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.EnabledStatus = params.get("EnabledStatus")
        if params.get("ForwardLoadBalancerSet") is not None:
            self.ForwardLoadBalancerSet = []
            for item in params.get("ForwardLoadBalancerSet"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self.ForwardLoadBalancerSet.append(obj)
        self.InstanceCount = params.get("InstanceCount")
        self.InServiceInstanceCount = params.get("InServiceInstanceCount")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.LaunchConfigurationName = params.get("LaunchConfigurationName")
        self.LoadBalancerIdSet = params.get("LoadBalancerIdSet")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.ProjectId = params.get("ProjectId")
        self.SubnetIdSet = params.get("SubnetIdSet")
        self.TerminationPolicySet = params.get("TerminationPolicySet")
        self.VpcId = params.get("VpcId")
        self.ZoneSet = params.get("ZoneSet")
        self.RetryPolicy = params.get("RetryPolicy")
        self.InActivityStatus = params.get("InActivityStatus")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("ServiceSettings") is not None:
            self.ServiceSettings = ServiceSettings()
            self.ServiceSettings._deserialize(params.get("ServiceSettings"))
        self.Ipv6AddressCount = params.get("Ipv6AddressCount")
        self.MultiZoneSubnetPolicy = params.get("MultiZoneSubnetPolicy")


class AutoScalingGroupAbstract(AbstractModel):
    """Brief information of an auto scaling group.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID.
        :type AutoScalingGroupId: str
        :param AutoScalingGroupName: Auto scaling group name.
        :type AutoScalingGroupName: str
        """
        self.AutoScalingGroupId = None
        self.AutoScalingGroupName = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.AutoScalingGroupName = params.get("AutoScalingGroupName")


class AutoScalingNotification(AbstractModel):
    """AS event notification

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID.
        :type AutoScalingGroupId: str
        :param NotificationUserGroupIds: List of user group IDs.
        :type NotificationUserGroupIds: list of str
        :param NotificationTypes: List of notification events.
        :type NotificationTypes: list of str
        :param AutoScalingNotificationId: Event notification ID.
        :type AutoScalingNotificationId: str
        """
        self.AutoScalingGroupId = None
        self.NotificationUserGroupIds = None
        self.NotificationTypes = None
        self.AutoScalingNotificationId = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.NotificationUserGroupIds = params.get("NotificationUserGroupIds")
        self.NotificationTypes = params.get("NotificationTypes")
        self.AutoScalingNotificationId = params.get("AutoScalingNotificationId")


class CompleteLifecycleActionRequest(AbstractModel):
    """CompleteLifecycleAction request structure.

    """

    def __init__(self):
        """
        :param LifecycleHookId: Lifecycle hook ID
        :type LifecycleHookId: str
        :param LifecycleActionResult: Result of the lifecycle action. Value range: "CONTINUE", "ABANDON"
        :type LifecycleActionResult: str
        :param InstanceId: Instance ID. Either "InstanceId" or "LifecycleActionToken" must be specified
        :type InstanceId: str
        :param LifecycleActionToken: Either "InstanceId" or "LifecycleActionToken" must be specified
        :type LifecycleActionToken: str
        """
        self.LifecycleHookId = None
        self.LifecycleActionResult = None
        self.InstanceId = None
        self.LifecycleActionToken = None


    def _deserialize(self, params):
        self.LifecycleHookId = params.get("LifecycleHookId")
        self.LifecycleActionResult = params.get("LifecycleActionResult")
        self.InstanceId = params.get("InstanceId")
        self.LifecycleActionToken = params.get("LifecycleActionToken")


class CompleteLifecycleActionResponse(AbstractModel):
    """CompleteLifecycleAction response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAutoScalingGroupRequest(AbstractModel):
    """CreateAutoScalingGroup request structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupName: Auto scaling group name, which can only contain letters, numbers, underscores, hyphens ("-"), and decimal points with a maximum length of 55 bytes and must be unique under your account.
        :type AutoScalingGroupName: str
        :param LaunchConfigurationId: Launch configuration ID
        :type LaunchConfigurationId: str
        :param MaxSize: Maximum number of instances. Value range: 0-2,000.
        :type MaxSize: int
        :param MinSize: Minimum number of instances. Value range: 0-2,000.
        :type MinSize: int
        :param VpcId: VPC ID; if on a basic network, enter an empty string
        :type VpcId: str
        :param DefaultCooldown: Default cooldown period in seconds. Default value: 300
        :type DefaultCooldown: int
        :param DesiredCapacity: Desired number of instances. The number should be no larger than the maximum and no smaller than minimum number of instances
        :type DesiredCapacity: int
        :param LoadBalancerIds: List of classic CLB IDs. Currently, the maximum length is 20. You cannot specify LoadBalancerIds and ForwardLoadBalancers at the same time.
        :type LoadBalancerIds: list of str
        :param ProjectId: Project ID
        :type ProjectId: int
        :param ForwardLoadBalancers: List of CLBs. Currently, the maximum length is 20. You cannot specify LoadBalancerIds and ForwardLoadBalancers at the same time.
        :type ForwardLoadBalancers: list of ForwardLoadBalancer
        :param SubnetIds: List of subnet IDs. A subnet must be specified in the VPC scenario. If multiple subnets are entered, their priority will be determined by the order in which they are entered, and they will be tried one by one until instances can be successfully created.
        :type SubnetIds: list of str
        :param TerminationPolicies: Termination policy. Currently, the maximum length is 1. Value range: OLDEST_INSTANCE, NEWEST_INSTANCE. Default value: OLDEST_INSTANCE.
<br><li> OLDEST_INSTANCE: The oldest instance in the auto scaling group will be terminated first.
<br><li> NEWEST_INSTANCE: The newest instance in the auto scaling group will be terminated first.
        :type TerminationPolicies: list of str
        :param Zones: List of availability zones. An availability zone must be specified in the basic network scenario. If multiple availability zones are entered, their priority will be determined by the order in which they are entered, and they will be tried one by one until instances can be successfully created.
        :type Zones: list of str
        :param RetryPolicy: Retry policy. Value range: IMMEDIATE_RETRY, INCREMENTAL_INTERVALS, and NO_RETRY. Default value: IMMEDIATE_RETRY.
<br><li> IMMEDIATE_RETRY: Retrying immediately in a short period of time and stopping after a number of consecutive failures (5).
<br><li> INCREMENTAL_INTERVALS: Retrying at incremental intervals, i.e., as the number of consecutive failures increases, the retry interval gradually increases, ranging from one second to one day.
<br><li> NO_RETRY: No retry until a user call or alarm message is received again.
        :type RetryPolicy: str
        :param ZonesCheckPolicy: Availability zone verification policy. Value range: ALL, ANY. Default value: ANY.
<br><li> ALL: The verification will succeed only if all availability zones (Zone) or subnets (SubnetId) are available; otherwise, an error will be reported.
<br><li> ANY: The verification will success if any availability zone (Zone) or subnet (SubnetId) is available; otherwise, an error will be reported.

Common reasons why an availability zone or subnet is unavailable include stock-out of CVM instances or CBS cloud disks in the availability zone, insufficient quota in the availability zone, or insufficient IPs in the subnet.
If an availability zone or subnet in Zones/SubnetIds does not exist, a verification error will be reported regardless of the value of ZonesCheckPolicy.
        :type ZonesCheckPolicy: str
        :param Tags: List of tag descriptions. This parameter is used to bind a tag to an auto scaling group as well as the corresponding resource instances.
        :type Tags: list of Tag
        :param ServiceSettings: Service settings such as unhealthy instance replacement.
        :type ServiceSettings: :class:`tencentcloud.autoscaling.v20180419.models.ServiceSettings`
        :param Ipv6AddressCount: 
        :type Ipv6AddressCount: int
        """
        self.AutoScalingGroupName = None
        self.LaunchConfigurationId = None
        self.MaxSize = None
        self.MinSize = None
        self.VpcId = None
        self.DefaultCooldown = None
        self.DesiredCapacity = None
        self.LoadBalancerIds = None
        self.ProjectId = None
        self.ForwardLoadBalancers = None
        self.SubnetIds = None
        self.TerminationPolicies = None
        self.Zones = None
        self.RetryPolicy = None
        self.ZonesCheckPolicy = None
        self.Tags = None
        self.ServiceSettings = None
        self.Ipv6AddressCount = None


    def _deserialize(self, params):
        self.AutoScalingGroupName = params.get("AutoScalingGroupName")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.VpcId = params.get("VpcId")
        self.DefaultCooldown = params.get("DefaultCooldown")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.ProjectId = params.get("ProjectId")
        if params.get("ForwardLoadBalancers") is not None:
            self.ForwardLoadBalancers = []
            for item in params.get("ForwardLoadBalancers"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self.ForwardLoadBalancers.append(obj)
        self.SubnetIds = params.get("SubnetIds")
        self.TerminationPolicies = params.get("TerminationPolicies")
        self.Zones = params.get("Zones")
        self.RetryPolicy = params.get("RetryPolicy")
        self.ZonesCheckPolicy = params.get("ZonesCheckPolicy")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("ServiceSettings") is not None:
            self.ServiceSettings = ServiceSettings()
            self.ServiceSettings._deserialize(params.get("ServiceSettings"))
        self.Ipv6AddressCount = params.get("Ipv6AddressCount")


class CreateAutoScalingGroupResponse(AbstractModel):
    """CreateAutoScalingGroup response structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AutoScalingGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.RequestId = params.get("RequestId")


class CreateLaunchConfigurationRequest(AbstractModel):
    """CreateLaunchConfiguration request structure.

    """

    def __init__(self):
        """
        :param LaunchConfigurationName: Display name of the launch configuration, which can contain Chinese characters, letters, numbers, underscores, separators ("-"), and decimal points with a maximum length of 60 bytes.
        :type LaunchConfigurationName: str
        :param ImageId: Valid [image](https://cloud.tencent.com/document/product/213/4940) ID in the format of `img-8toqc6s3`. There are four types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><li>Marketplace images </li><br/>You can obtain the available image IDs in the following ways: <br/><li>For `public images`, `custom images`, and `shared images`, log in to the [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the image IDs; for `marketplace images`, query the image IDs through [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li>This value can be obtained from the `ImageId` field in the return value of the [DescribeImages API](https://cloud.tencent.com/document/api/213/15715).</li>
        :type ImageId: str
        :param ProjectId: ID of the project to which the instance belongs. This parameter can be obtained from the `projectId` field in the returned values of [DescribeProject](https://cloud.tencent.com/document/api/378/4400). If this is left empty, default project is used.
        :type ProjectId: int
        :param InstanceType: Instance model. Different instance models specify different resource specifications. The specific value can be obtained by calling the [DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749) API to get the latest specification table or referring to the descriptions in [Instance Types](https://cloud.tencent.com/document/product/213/11518).
`InstanceType` and `InstanceTypes` are mutually exclusive, and one and only one of them must be entered.
        :type InstanceType: str
        :param SystemDisk: System disk configuration of the instance. If this parameter is not specified, the default value will be assigned to it.
        :type SystemDisk: :class:`tencentcloud.autoscaling.v20180419.models.SystemDisk`
        :param DataDisks: Information of the instance's data disk configuration. If this parameter is not specified, no data disk is purchased by default. Up to 11 data disks can be supported.
        :type DataDisks: list of DataDisk
        :param InternetAccessible: Configuration information of public network bandwidth. If this parameter is not specified, the default public network bandwidth is 0 Mbps.
        :type InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        :param LoginSettings: Login settings of the instance. This parameter is used to set the login password and key for the instance, or to keep the original login settings for the image. By default, a random password is generated and sent to the user via the internal message.
        :type LoginSettings: :class:`tencentcloud.autoscaling.v20180419.models.LoginSettings`
        :param SecurityGroupIds: The security group to which the instance belongs. This parameter can be obtained by calling the `SecurityGroupId` field in the returned value of [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808). If this parameter is not specified, no security group will be bound by default.
        :type SecurityGroupIds: list of str
        :param EnhancedService: Enhanced service. This parameter is used to specify whether to enable Cloud Security, Cloud Monitoring and other services. If this parameter is not specified, Cloud Monitoring and Cloud Security will be enabled by default.
        :type EnhancedService: :class:`tencentcloud.autoscaling.v20180419.models.EnhancedService`
        :param UserData: Base64-encoded custom data of up to 16 KB.
        :type UserData: str
        :param InstanceChargeType: Instance billing type. CVM instances are POSTPAID_BY_HOUR by default.
<br><li>POSTPAID_BY_HOUR: Pay-as-you-go on an hourly basis
<br><li>SPOTPAID: Bidding
        :type InstanceChargeType: str
        :param InstanceMarketOptions: Market-related options of the instance, such as the parameters related to stop instances. If the billing method of instance is specified as bidding, this parameter must be passed in.
        :type InstanceMarketOptions: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        :param InstanceTypes: List of instance models. Different instance models specify different resource specifications. Up to 10 instance models can be supported.
`InstanceType` and `InstanceTypes` are mutually exclusive, and one and only one of them must be entered.
        :type InstanceTypes: list of str
        :param InstanceTypesCheckPolicy: Instance type verification policy. Value range: ALL, ANY. Default value: ANY.
<br><li> ALL: The verification will success only if all instance types (InstanceType) are available; otherwise, an error will be reported.
<br><li> ANY: The verification will success if any instance type (InstanceType) is available; otherwise, an error will be reported.

Common reasons why an instance type is unavailable include stock-out of the instance type or the corresponding cloud disk.
If a model in InstanceTypes does not exist or has been discontinued, a verification error will be reported regardless of the value of InstanceTypesCheckPolicy.
        :type InstanceTypesCheckPolicy: str
        :param InstanceTags: List of tags. This parameter is used to bind up to 10 tags to newly added instances.
        :type InstanceTags: list of InstanceTag
        :param CamRoleName: CAM role name, which can be obtained from the roleName field in the return value of the DescribeRoleList API.
        :type CamRoleName: str
        :param HostNameSettings: CVM HostName settings.
        :type HostNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.HostNameSettings`
        """
        self.LaunchConfigurationName = None
        self.ImageId = None
        self.ProjectId = None
        self.InstanceType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.InternetAccessible = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.EnhancedService = None
        self.UserData = None
        self.InstanceChargeType = None
        self.InstanceMarketOptions = None
        self.InstanceTypes = None
        self.InstanceTypesCheckPolicy = None
        self.InstanceTags = None
        self.CamRoleName = None
        self.HostNameSettings = None


    def _deserialize(self, params):
        self.LaunchConfigurationName = params.get("LaunchConfigurationName")
        self.ImageId = params.get("ImageId")
        self.ProjectId = params.get("ProjectId")
        self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.UserData = params.get("UserData")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.InstanceTypes = params.get("InstanceTypes")
        self.InstanceTypesCheckPolicy = params.get("InstanceTypesCheckPolicy")
        if params.get("InstanceTags") is not None:
            self.InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTag()
                obj._deserialize(item)
                self.InstanceTags.append(obj)
        self.CamRoleName = params.get("CamRoleName")
        if params.get("HostNameSettings") is not None:
            self.HostNameSettings = HostNameSettings()
            self.HostNameSettings._deserialize(params.get("HostNameSettings"))


class CreateLaunchConfigurationResponse(AbstractModel):
    """CreateLaunchConfiguration response structure.

    """

    def __init__(self):
        """
        :param LaunchConfigurationId: This parameter is returned when a launch configuration is created through this API, indicating the launch configuration ID.
        :type LaunchConfigurationId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LaunchConfigurationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.RequestId = params.get("RequestId")


class CreateLifecycleHookRequest(AbstractModel):
    """CreateLifecycleHook request structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param LifecycleHookName: Lifecycle hook name, which can contain Chinese characters, letters, numbers, underscores (_), hyphens (-), and periods (.) with a maximum length of 128 bytes.
        :type LifecycleHookName: str
        :param LifecycleTransition: Scenario for the lifecycle hook. Valid values: "INSTANCE_LAUNCHING" and "INSTANCE_TERMINATING"
        :type LifecycleTransition: str
        :param DefaultResult: Defined actions when lifecycle hook times out. Valid values: "CONTINUE" and "ABANDON". Default value: "CONTINUE"
        :type DefaultResult: str
        :param HeartbeatTimeout: The maximum length of time (in seconds) that can elapse before the lifecycle hook times out. Value range: 30-3,600. Default value: 300
        :type HeartbeatTimeout: int
        :param NotificationMetadata: Additional information sent by Auto Scaling to the notification target. Default value is “”. Maximum length is 1024 characters.
        :type NotificationMetadata: str
        :param NotificationTarget: Notification target
        :type NotificationTarget: :class:`tencentcloud.autoscaling.v20180419.models.NotificationTarget`
        :param LifecycleTransitionType: The scenario where the lifecycle hook is applied. `EXTENSION`: the lifecycle hook will be triggered when AttachInstances, DetachInstances or RemoveInstaces is called. `NORMAL`: the lifecycle hook is not triggered by the above APIs. 
        :type LifecycleTransitionType: str
        """
        self.AutoScalingGroupId = None
        self.LifecycleHookName = None
        self.LifecycleTransition = None
        self.DefaultResult = None
        self.HeartbeatTimeout = None
        self.NotificationMetadata = None
        self.NotificationTarget = None
        self.LifecycleTransitionType = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.LifecycleHookName = params.get("LifecycleHookName")
        self.LifecycleTransition = params.get("LifecycleTransition")
        self.DefaultResult = params.get("DefaultResult")
        self.HeartbeatTimeout = params.get("HeartbeatTimeout")
        self.NotificationMetadata = params.get("NotificationMetadata")
        if params.get("NotificationTarget") is not None:
            self.NotificationTarget = NotificationTarget()
            self.NotificationTarget._deserialize(params.get("NotificationTarget"))
        self.LifecycleTransitionType = params.get("LifecycleTransitionType")


class CreateLifecycleHookResponse(AbstractModel):
    """CreateLifecycleHook response structure.

    """

    def __init__(self):
        """
        :param LifecycleHookId: Lifecycle hook ID
        :type LifecycleHookId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LifecycleHookId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LifecycleHookId = params.get("LifecycleHookId")
        self.RequestId = params.get("RequestId")


class CreateNotificationConfigurationRequest(AbstractModel):
    """CreateNotificationConfiguration request structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID.
        :type AutoScalingGroupId: str
        :param NotificationTypes: Notification type, i.e., the set of types of notifications to be subscribed to. Value range:
<li>SCALE_OUT_SUCCESSFUL: scale-out succeeded</li>
<li>SCALE_OUT_FAILED: scale-out failed</li>
<li>SCALE_IN_SUCCESSFUL: scale-in succeeded</li>
<li>SCALE_IN_FAILED: scale-in failed</li>
<li>REPLACE_UNHEALTHY_INSTANCE_SUCCESSFUL: unhealthy instance replacement succeeded</li>
<li>REPLACE_UNHEALTHY_INSTANCE_FAILED: unhealthy instance replacement failed</li>
        :type NotificationTypes: list of str
        :param NotificationUserGroupIds: Notification group ID, which is the set of user group IDs. You can query the user group IDs through the [ListGroups](https://cloud.tencent.com/document/product/598/34589) API.
        :type NotificationUserGroupIds: list of str
        """
        self.AutoScalingGroupId = None
        self.NotificationTypes = None
        self.NotificationUserGroupIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.NotificationTypes = params.get("NotificationTypes")
        self.NotificationUserGroupIds = params.get("NotificationUserGroupIds")


class CreateNotificationConfigurationResponse(AbstractModel):
    """CreateNotificationConfiguration response structure.

    """

    def __init__(self):
        """
        :param AutoScalingNotificationId: Notification ID.
        :type AutoScalingNotificationId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AutoScalingNotificationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoScalingNotificationId = params.get("AutoScalingNotificationId")
        self.RequestId = params.get("RequestId")


class CreatePaiInstanceRequest(AbstractModel):
    """CreatePaiInstance request structure.

    """

    def __init__(self):
        """
        :param DomainName: PAI instance domain name.
        :type DomainName: str
        :param InternetAccessible: Information of the public network bandwidth configuration.
        :type InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        :param InitScript: Base64-encoded string of the launch script.
        :type InitScript: str
        :param Zones: List of availability zones.
        :type Zones: list of str
        :param VpcId: VpcId.
        :type VpcId: str
        :param SubnetIds: List of subnets.
        :type SubnetIds: list of str
        :param InstanceName: Instance display name.
        :type InstanceName: str
        :param InstanceTypes: List of instance models.
        :type InstanceTypes: list of str
        :param LoginSettings: Instance login settings.
        :type LoginSettings: :class:`tencentcloud.autoscaling.v20180419.models.LoginSettings`
        :param InstanceChargeType: Instance billing type.
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: Relevant parameter settings for the prepaid mode (i.e., monthly subscription). This parameter can specify the purchased usage period, whether to set automatic renewal, and other attributes of the instance purchased on a prepaid basis. If the billing method of the specified instance is prepaid, this parameter is required.
        :type InstanceChargePrepaid: :class:`tencentcloud.autoscaling.v20180419.models.InstanceChargePrepaid`
        """
        self.DomainName = None
        self.InternetAccessible = None
        self.InitScript = None
        self.Zones = None
        self.VpcId = None
        self.SubnetIds = None
        self.InstanceName = None
        self.InstanceTypes = None
        self.LoginSettings = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.InitScript = params.get("InitScript")
        self.Zones = params.get("Zones")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")
        self.InstanceName = params.get("InstanceName")
        self.InstanceTypes = params.get("InstanceTypes")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class CreatePaiInstanceResponse(AbstractModel):
    """CreatePaiInstance response structure.

    """

    def __init__(self):
        """
        :param InstanceIdSet: This parameter is returned when an instance is created via this API, representing one or more instance `IDs`. The return of the instance `ID` list does not mean that the instance is created successfully. You can find out whether the instance is created by checking the status of the instance `ID` in the InstancesSet returned by the [DescribeInstances API](https://cloud.tencent.com/document/api/213/15728). If the status of the instance changes from "pending" to "running", the instance is created successfully.
        :type InstanceIdSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.RequestId = params.get("RequestId")


class CreateScalingPolicyRequest(AbstractModel):
    """CreateScalingPolicy request structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID.
        :type AutoScalingGroupId: str
        :param ScalingPolicyName: Alarm trigger policy name.
        :type ScalingPolicyName: str
        :param AdjustmentType: The method to adjust the desired number of instances after the alarm is triggered. Value range: <br><li>CHANGE_IN_CAPACITY: Increase or decrease the desired number of instances </li><li>EXACT_CAPACITY: Adjust to the specified desired number of instances </li> <li>PERCENT_CHANGE_IN_CAPACITY: Adjust the desired number of instances by percentage </li>
        :type AdjustmentType: str
        :param AdjustmentValue: The adjusted value of desired number of instances after the alarm is triggered. Value range: <br><li>When AdjustmentType is CHANGE_IN_CAPACITY, if AdjustmentValue is a positive value, some new instances will be added after the alarm is triggered, and if it is a negative value, some existing instances will be removed after the alarm is triggered </li> <li> When AdjustmentType is EXACT_CAPACITY, the value of AdjustmentValue is the desired number of instances after the alarm is triggered, which should be equal to or greater than 0 </li> <li> When AdjustmentType is PERCENT_CHANGE_IN_CAPACITY, if AdjusmentValue (in %) is a positive value, new instances will be added by percentage after the alarm is triggered; if it is a negative value, existing instances will be removed by percentage after the alarm is triggered.
        :type AdjustmentValue: int
        :param MetricAlarm: Alarm monitoring metric.
        :type MetricAlarm: :class:`tencentcloud.autoscaling.v20180419.models.MetricAlarm`
        :param Cooldown: Cooldown period in seconds. Default value: 300 seconds.
        :type Cooldown: int
        :param NotificationUserGroupIds: Notification group ID, which is the set of user group IDs. You can query the user group IDs through the [ListGroups](https://cloud.tencent.com/document/product/598/34589) API.
        :type NotificationUserGroupIds: list of str
        """
        self.AutoScalingGroupId = None
        self.ScalingPolicyName = None
        self.AdjustmentType = None
        self.AdjustmentValue = None
        self.MetricAlarm = None
        self.Cooldown = None
        self.NotificationUserGroupIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.ScalingPolicyName = params.get("ScalingPolicyName")
        self.AdjustmentType = params.get("AdjustmentType")
        self.AdjustmentValue = params.get("AdjustmentValue")
        if params.get("MetricAlarm") is not None:
            self.MetricAlarm = MetricAlarm()
            self.MetricAlarm._deserialize(params.get("MetricAlarm"))
        self.Cooldown = params.get("Cooldown")
        self.NotificationUserGroupIds = params.get("NotificationUserGroupIds")


class CreateScalingPolicyResponse(AbstractModel):
    """CreateScalingPolicy response structure.

    """

    def __init__(self):
        """
        :param AutoScalingPolicyId: Alarm trigger policy ID.
        :type AutoScalingPolicyId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AutoScalingPolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        self.RequestId = params.get("RequestId")


class CreateScheduledActionRequest(AbstractModel):
    """CreateScheduledAction request structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param ScheduledActionName: Scheduled task name, which can only contain letters, numbers, underscores, hyphens ("-"), and decimal points with a maximum length of 60 bytes and must be unique in an auto scaling group.
        :type ScheduledActionName: str
        :param MaxSize: The maximum number of instances set for the auto scaling group when the scheduled task is triggered.
        :type MaxSize: int
        :param MinSize: The minimum number of instances set for the auto scaling group when the scheduled task is triggered.
        :type MinSize: int
        :param DesiredCapacity: The desired number of instances set for the auto scaling group when the scheduled task is triggered.
        :type DesiredCapacity: int
        :param StartTime: Initial triggered time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard.
        :type StartTime: str
        :param EndTime: End time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard. <br><br>This parameter and `Recurrence` need to be specified at the same time. After the end time, the scheduled task will no longer take effect.
        :type EndTime: str
        :param Recurrence: Repeating mode of the scheduled task, which is in standard cron format. <br><br>This parameter and `EndTime` need to be specified at the same time.
        :type Recurrence: str
        """
        self.AutoScalingGroupId = None
        self.ScheduledActionName = None
        self.MaxSize = None
        self.MinSize = None
        self.DesiredCapacity = None
        self.StartTime = None
        self.EndTime = None
        self.Recurrence = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.ScheduledActionName = params.get("ScheduledActionName")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Recurrence = params.get("Recurrence")


class CreateScheduledActionResponse(AbstractModel):
    """CreateScheduledAction response structure.

    """

    def __init__(self):
        """
        :param ScheduledActionId: Scheduled task ID
        :type ScheduledActionId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ScheduledActionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ScheduledActionId = params.get("ScheduledActionId")
        self.RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """Configuration information of data disk in launch configuration. If this parameter is not specified, no data disk will be purchased by default. You can specify only one data disk when purchasing it.

    """

    def __init__(self):
        """
        :param DiskType: Data disk type. For more information on limits of data disk types, see [CVM Instance Configuration](https://cloud.tencent.com/document/product/213/2177). Value range: <br><li>LOCAL_BASIC: Local disk <br><li>LOCAL_SSD: Local SSD disk <br><li>CLOUD_BASIC: HDD cloud disk <br><li>CLOUD_PREMIUM: Premium cloud disk <br><li>CLOUD_SSD: SSD cloud disk <br><br>Default value: LOCAL_BASIC.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param DiskSize: Data disk size (in GB). The minimum adjustment increment is 10 GB. The value range varies by data disk type. For more information on limits, see [CVM Instance Configuration](https://cloud.tencent.com/document/product/213/2177). The default value is 0, indicating that no data disk is purchased. For more information, see the product documentation.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskSize: int
        :param SnapshotId: Data disk snapshot ID, such as `snap-l8psqwnt`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SnapshotId: str
        """
        self.DiskType = None
        self.DiskSize = None
        self.SnapshotId = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.SnapshotId = params.get("SnapshotId")


class DeleteAutoScalingGroupRequest(AbstractModel):
    """DeleteAutoScalingGroup request structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        """
        self.AutoScalingGroupId = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")


class DeleteAutoScalingGroupResponse(AbstractModel):
    """DeleteAutoScalingGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLaunchConfigurationRequest(AbstractModel):
    """DeleteLaunchConfiguration request structure.

    """

    def __init__(self):
        """
        :param LaunchConfigurationId: ID of the launch configuration to be deleted.
        :type LaunchConfigurationId: str
        """
        self.LaunchConfigurationId = None


    def _deserialize(self, params):
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")


class DeleteLaunchConfigurationResponse(AbstractModel):
    """DeleteLaunchConfiguration response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLifecycleHookRequest(AbstractModel):
    """DeleteLifecycleHook request structure.

    """

    def __init__(self):
        """
        :param LifecycleHookId: Lifecycle hook ID
        :type LifecycleHookId: str
        """
        self.LifecycleHookId = None


    def _deserialize(self, params):
        self.LifecycleHookId = params.get("LifecycleHookId")


class DeleteLifecycleHookResponse(AbstractModel):
    """DeleteLifecycleHook response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNotificationConfigurationRequest(AbstractModel):
    """DeleteNotificationConfiguration request structure.

    """

    def __init__(self):
        """
        :param AutoScalingNotificationId: ID of the notification to be deleted.
        :type AutoScalingNotificationId: str
        """
        self.AutoScalingNotificationId = None


    def _deserialize(self, params):
        self.AutoScalingNotificationId = params.get("AutoScalingNotificationId")


class DeleteNotificationConfigurationResponse(AbstractModel):
    """DeleteNotificationConfiguration response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteScalingPolicyRequest(AbstractModel):
    """DeleteScalingPolicy request structure.

    """

    def __init__(self):
        """
        :param AutoScalingPolicyId: ID of the alarm policy to be deleted.
        :type AutoScalingPolicyId: str
        """
        self.AutoScalingPolicyId = None


    def _deserialize(self, params):
        self.AutoScalingPolicyId = params.get("AutoScalingPolicyId")


class DeleteScalingPolicyResponse(AbstractModel):
    """DeleteScalingPolicy response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteScheduledActionRequest(AbstractModel):
    """DeleteScheduledAction request structure.

    """

    def __init__(self):
        """
        :param ScheduledActionId: ID of the scheduled task to be deleted.
        :type ScheduledActionId: str
        """
        self.ScheduledActionId = None


    def _deserialize(self, params):
        self.ScheduledActionId = params.get("ScheduledActionId")


class DeleteScheduledActionResponse(AbstractModel):
    """DeleteScheduledAction response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountLimitsRequest(AbstractModel):
    """DescribeAccountLimits request structure.

    """


class DescribeAccountLimitsResponse(AbstractModel):
    """DescribeAccountLimits response structure.

    """

    def __init__(self):
        """
        :param MaxNumberOfLaunchConfigurations: Maximum number of launch configurations allowed for creation by the user account
        :type MaxNumberOfLaunchConfigurations: int
        :param NumberOfLaunchConfigurations: Current number of launch configurations under the user account
        :type NumberOfLaunchConfigurations: int
        :param MaxNumberOfAutoScalingGroups: Maximum number of auto scaling groups allowed for creation by the user account
        :type MaxNumberOfAutoScalingGroups: int
        :param NumberOfAutoScalingGroups: Current number of auto scaling groups under the user account
        :type NumberOfAutoScalingGroups: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MaxNumberOfLaunchConfigurations = None
        self.NumberOfLaunchConfigurations = None
        self.MaxNumberOfAutoScalingGroups = None
        self.NumberOfAutoScalingGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaxNumberOfLaunchConfigurations = params.get("MaxNumberOfLaunchConfigurations")
        self.NumberOfLaunchConfigurations = params.get("NumberOfLaunchConfigurations")
        self.MaxNumberOfAutoScalingGroups = params.get("MaxNumberOfAutoScalingGroups")
        self.NumberOfAutoScalingGroups = params.get("NumberOfAutoScalingGroups")
        self.RequestId = params.get("RequestId")


class DescribeAutoScalingActivitiesRequest(AbstractModel):
    """DescribeAutoScalingActivities request structure.

    """

    def __init__(self):
        """
        :param ActivityIds: Queries by one or more scaling activity IDs in the format of `asa-5l2ejpfo`. The maximum quantity per request is 100. This parameter does not support specifying both `ActivityIds` and `Filters` at the same time.
        :type ActivityIds: list of str
        :param Filters: Filter.
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
<li> activity-status-code - String - Required: No - (Filter) Filter by scaling activity status . (INIT: initializing | RUNNING: running | SUCCESSFUL: succeeded | PARTIALLY_SUCCESSFUL: partially succeeded | FAILED: failed | CANCELLED: canceled)</li>
<li> activity-type - String - Required: No - (Filter) Filter by scaling activity type. (SCALE_OUT: scale-out | SCALE_IN: scale-in | ATTACH_INSTANCES: adding an instance | REMOVE_INSTANCES: terminating an instance | DETACH_INSTANCES: removing an instance | TERMINATE_INSTANCES_UNEXPECTEDLY: terminating an instance in the CVM console | REPLACE_UNHEALTHY_INSTANCE: replacing an unhealthy instance | UPDATE_LOAD_BALANCERS: updating a load balancer)</li>
<li> activity-id - String - Required: No - (Filter) Filter by scaling activity ID.</li>
The maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `ActivityIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://cloud.tencent.com/document/api/213/15688).
        :type Limit: int
        :param Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://cloud.tencent.com/document/api/213/15688).
        :type Offset: int
        :param StartTime: The earliest start time of the scaling activity, which will be ignored if ActivityIds is specified. The value is in `UTC time` in the format of `YYYY-MM-DDThh:mm:ssZ` according to the `ISO8601` standard.
        :type StartTime: str
        :param EndTime: The latest end time of the scaling activity, which will be ignored if ActivityIds is specified. The value is in `UTC time` in the format of `YYYY-MM-DDThh:mm:ssZ` according to the `ISO8601` standard.
        :type EndTime: str
        """
        self.ActivityIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ActivityIds = params.get("ActivityIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeAutoScalingActivitiesResponse(AbstractModel):
    """DescribeAutoScalingActivities response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible scaling activities.
        :type TotalCount: int
        :param ActivitySet: Information set of eligible scaling activities.
        :type ActivitySet: list of Activity
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ActivitySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ActivitySet") is not None:
            self.ActivitySet = []
            for item in params.get("ActivitySet"):
                obj = Activity()
                obj._deserialize(item)
                self.ActivitySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAutoScalingGroupLastActivitiesRequest(AbstractModel):
    """DescribeAutoScalingGroupLastActivities request structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupIds: ID list of an auto scaling group.
        :type AutoScalingGroupIds: list of str
        """
        self.AutoScalingGroupIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupIds = params.get("AutoScalingGroupIds")


class DescribeAutoScalingGroupLastActivitiesResponse(AbstractModel):
    """DescribeAutoScalingGroupLastActivities response structure.

    """

    def __init__(self):
        """
        :param ActivitySet: Information set of eligible scaling activities. Scaling groups without scaling activities are not returned. For example, if there are 50 auto scaling group IDs but only 45 records are returned, it indicates that 5 of the auto scaling groups do not have scaling activities.
        :type ActivitySet: list of Activity
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ActivitySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ActivitySet") is not None:
            self.ActivitySet = []
            for item in params.get("ActivitySet"):
                obj = Activity()
                obj._deserialize(item)
                self.ActivitySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAutoScalingGroupsRequest(AbstractModel):
    """DescribeAutoScalingGroups request structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupIds: Queries by one or more auto scaling group IDs in the format of `asg-nkdwoui0`. The maximum quantity per request is 100. This parameter does not support specifying both `AutoScalingGroupIds` and `Filters` at the same time.
        :type AutoScalingGroupIds: list of str
        :param Filters: Filter.
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
<li> auto-scaling-group-name - String - Required: No - (Filter) Filter by auto scaling group name.</li>
<li> launch-configuration-id - String - Required: No - (Filter) Filter by launch configuration ID.</li>
<li> tag-key - String - Required: No - (Filter) Filter by tag key.</li>
<li> tag-value - String - Required: No - (Filter) Filter by tag value.</li>
<li> tag:tag-key - String - Required: No - (Filter) Filter by tag key-value pair. The tag-key should be replaced with a specified tag key. For detailed usage, see sample 2</li>
The maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `AutoScalingGroupIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://cloud.tencent.com/document/api/213/15688).
        :type Limit: int
        :param Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://cloud.tencent.com/document/api/213/15688).
        :type Offset: int
        """
        self.AutoScalingGroupIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.AutoScalingGroupIds = params.get("AutoScalingGroupIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeAutoScalingGroupsResponse(AbstractModel):
    """DescribeAutoScalingGroups response structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupSet: List of auto scaling group details.
        :type AutoScalingGroupSet: list of AutoScalingGroup
        :param TotalCount: Number of eligible auto scaling groups.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AutoScalingGroupSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AutoScalingGroupSet") is not None:
            self.AutoScalingGroupSet = []
            for item in params.get("AutoScalingGroupSet"):
                obj = AutoScalingGroup()
                obj._deserialize(item)
                self.AutoScalingGroupSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAutoScalingInstancesRequest(AbstractModel):
    """DescribeAutoScalingInstances request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: ID of the CVM instance to be queried. This parameter does not support specifying both InstanceIds and Filters at the same time.
        :type InstanceIds: list of str
        :param Filters: Filter.
<li> instance-id - String - Required: No - (Filter) Filter by instance ID.</li>
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
The maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `InstanceIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://cloud.tencent.com/document/api/213/15688).
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://cloud.tencent.com/document/api/213/15688).
        :type Limit: int
        """
        self.InstanceIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAutoScalingInstancesResponse(AbstractModel):
    """DescribeAutoScalingInstances response structure.

    """

    def __init__(self):
        """
        :param AutoScalingInstanceSet: List of instance details.
        :type AutoScalingInstanceSet: list of Instance
        :param TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AutoScalingInstanceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AutoScalingInstanceSet") is not None:
            self.AutoScalingInstanceSet = []
            for item in params.get("AutoScalingInstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self.AutoScalingInstanceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeLaunchConfigurationsRequest(AbstractModel):
    """DescribeLaunchConfigurations request structure.

    """

    def __init__(self):
        """
        :param LaunchConfigurationIds: Queries by one or more launch configuration IDs in the format of `asc-ouy1ax38`. The maximum quantity per request is 100. This parameter does not support specifying both `LaunchConfigurationIds` and `Filters` at the same time.
        :type LaunchConfigurationIds: list of str
        :param Filters: Filter.
<li> launch-configuration-id - String - Required: No - (Filter) Filter by launch configuration ID.</li>
<li> launch-configuration-name - String - Required: No - (Filter) Filter by launch configuration name.</li>
The maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `LaunchConfigurationIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://cloud.tencent.com/document/api/213/15688).
        :type Limit: int
        :param Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://cloud.tencent.com/document/api/213/15688).
        :type Offset: int
        """
        self.LaunchConfigurationIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.LaunchConfigurationIds = params.get("LaunchConfigurationIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeLaunchConfigurationsResponse(AbstractModel):
    """DescribeLaunchConfigurations response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible launch configurations.
        :type TotalCount: int
        :param LaunchConfigurationSet: List of launch configuration details.
        :type LaunchConfigurationSet: list of LaunchConfiguration
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.LaunchConfigurationSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LaunchConfigurationSet") is not None:
            self.LaunchConfigurationSet = []
            for item in params.get("LaunchConfigurationSet"):
                obj = LaunchConfiguration()
                obj._deserialize(item)
                self.LaunchConfigurationSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLifecycleHooksRequest(AbstractModel):
    """DescribeLifecycleHooks request structure.

    """

    def __init__(self):
        """
        :param LifecycleHookIds: Queries by one or more lifecycle hook IDs in the format of `ash-8azjzxcl`. The maximum quantity per request is 100. This parameter does not support specifying both `LifecycleHookIds` and `Filters` at the same time.
        :type LifecycleHookIds: list of str
        :param Filters: Filter.
<li> lifecycle-hook-id - String - Required: No - (Filter) Filter by lifecycle hook ID.</li>
<li> lifecycle-hook-name - String - Required: No - (Filter) Filter by lifecycle hook name.</li>
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
Filter.
<li> lifecycle-hook-id - String - Required: No - (Filter) Filter by lifecycle hook ID.</li>
<li> lifecycle-hook-name - String - Required: No - (Filter) Filter by lifecycle hook name.</li>
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
The maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `LifecycleHookIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://cloud.tencent.com/document/api/213/15688).
        :type Limit: int
        :param Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://cloud.tencent.com/document/api/213/15688).
        :type Offset: int
        """
        self.LifecycleHookIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.LifecycleHookIds = params.get("LifecycleHookIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeLifecycleHooksResponse(AbstractModel):
    """DescribeLifecycleHooks response structure.

    """

    def __init__(self):
        """
        :param LifecycleHookSet: Array of lifecycle hooks
        :type LifecycleHookSet: list of LifecycleHook
        :param TotalCount: Total quantity
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LifecycleHookSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LifecycleHookSet") is not None:
            self.LifecycleHookSet = []
            for item in params.get("LifecycleHookSet"):
                obj = LifecycleHook()
                obj._deserialize(item)
                self.LifecycleHookSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNotificationConfigurationsRequest(AbstractModel):
    """DescribeNotificationConfigurations request structure.

    """

    def __init__(self):
        """
        :param AutoScalingNotificationIds: Queries by one or more notification IDs in the format of asn-2sestqbr. The maximum number of instances per request is 100. This parameter does not support specifying both `AutoScalingNotificationIds` and `Filters` at the same time.
        :type AutoScalingNotificationIds: list of str
        :param Filters: Filter.
<li> auto-scaling-notification-id - String - Required: No - (Filter) Filter by notification ID.</li>
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
The maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `AutoScalingNotificationIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://cloud.tencent.com/document/api/213/15688).
        :type Limit: int
        :param Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://cloud.tencent.com/document/api/213/15688).
        :type Offset: int
        """
        self.AutoScalingNotificationIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.AutoScalingNotificationIds = params.get("AutoScalingNotificationIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeNotificationConfigurationsResponse(AbstractModel):
    """DescribeNotificationConfigurations response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible notifications.
        :type TotalCount: int
        :param AutoScalingNotificationSet: List of AS event notification details.
        :type AutoScalingNotificationSet: list of AutoScalingNotification
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.AutoScalingNotificationSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AutoScalingNotificationSet") is not None:
            self.AutoScalingNotificationSet = []
            for item in params.get("AutoScalingNotificationSet"):
                obj = AutoScalingNotification()
                obj._deserialize(item)
                self.AutoScalingNotificationSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePaiInstancesRequest(AbstractModel):
    """DescribePaiInstances request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Queries by PAI instance ID.
        :type InstanceIds: list of str
        :param Filters: Filter.
        :type Filters: list of Filter
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.InstanceIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribePaiInstancesResponse(AbstractModel):
    """DescribePaiInstances response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible PAI instances
        :type TotalCount: int
        :param PaiInstanceSet: PAI instance details
        :type PaiInstanceSet: list of PaiInstance
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.PaiInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PaiInstanceSet") is not None:
            self.PaiInstanceSet = []
            for item in params.get("PaiInstanceSet"):
                obj = PaiInstance()
                obj._deserialize(item)
                self.PaiInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeScalingPoliciesRequest(AbstractModel):
    """DescribeScalingPolicies request structure.

    """

    def __init__(self):
        """
        :param AutoScalingPolicyIds: Queries by one or more alarm policy IDs in the format of asp-i9vkg894. The maximum number of instances per request is 100. This parameter does not support specifying both `AutoScalingPolicyIds` and `Filters` at the same time.
        :type AutoScalingPolicyIds: list of str
        :param Filters: Filter.
<li> auto-scaling-policy-id - String - Required: No - (Filter) Filter by alarm policy ID.</li>
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
<li> scaling-policy-name - String - Required: No - (Filter) Filter by alarm policy name.</li>
The maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `AutoScalingPolicyIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://cloud.tencent.com/document/api/213/15688).
        :type Limit: int
        :param Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://cloud.tencent.com/document/api/213/15688).
        :type Offset: int
        """
        self.AutoScalingPolicyIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.AutoScalingPolicyIds = params.get("AutoScalingPolicyIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeScalingPoliciesResponse(AbstractModel):
    """DescribeScalingPolicies response structure.

    """

    def __init__(self):
        """
        :param ScalingPolicySet: List of AS alarm trigger policy details.
        :type ScalingPolicySet: list of ScalingPolicy
        :param TotalCount: Number of eligible notifications.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ScalingPolicySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ScalingPolicySet") is not None:
            self.ScalingPolicySet = []
            for item in params.get("ScalingPolicySet"):
                obj = ScalingPolicy()
                obj._deserialize(item)
                self.ScalingPolicySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeScheduledActionsRequest(AbstractModel):
    """DescribeScheduledActions request structure.

    """

    def __init__(self):
        """
        :param ScheduledActionIds: Queries by one or more scheduled task IDs in the format of asst-am691zxo. The maximum number of instances per request is 100. This parameter does not support specifying both ScheduledActionIds` and `Filters` at the same time.
        :type ScheduledActionIds: list of str
        :param Filters: Filter.
<li> scheduled-action-id - String - Required: No - (Filter) Filter by scheduled task ID.</li>
<li> scheduled-action-name - String - Required: No - (Filter) Filter by scheduled task name.</li>
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
        :type Filters: list of Filter
        :param Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://cloud.tencent.com/document/api/213/15688).
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://cloud.tencent.com/document/api/213/15688).
        :type Limit: int
        """
        self.ScheduledActionIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ScheduledActionIds = params.get("ScheduledActionIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeScheduledActionsResponse(AbstractModel):
    """DescribeScheduledActions response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible scheduled tasks.
        :type TotalCount: int
        :param ScheduledActionSet: List of scheduled task details.
        :type ScheduledActionSet: list of ScheduledAction
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ScheduledActionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ScheduledActionSet") is not None:
            self.ScheduledActionSet = []
            for item in params.get("ScheduledActionSet"):
                obj = ScheduledAction()
                obj._deserialize(item)
                self.ScheduledActionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DetachInstancesRequest(AbstractModel):
    """DetachInstances request structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param InstanceIds: List of CVM instance IDs
        :type InstanceIds: list of str
        """
        self.AutoScalingGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.InstanceIds = params.get("InstanceIds")


class DetachInstancesResponse(AbstractModel):
    """DetachInstances response structure.

    """

    def __init__(self):
        """
        :param ActivityId: Scaling activity ID
        :type ActivityId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ActivityId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.RequestId = params.get("RequestId")


class DisableAutoScalingGroupRequest(AbstractModel):
    """DisableAutoScalingGroup request structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        """
        self.AutoScalingGroupId = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")


class DisableAutoScalingGroupResponse(AbstractModel):
    """DisableAutoScalingGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableAutoScalingGroupRequest(AbstractModel):
    """EnableAutoScalingGroup request structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        """
        self.AutoScalingGroupId = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")


class EnableAutoScalingGroupResponse(AbstractModel):
    """EnableAutoScalingGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnhancedService(AbstractModel):
    """This describes the conditions of enhancement services for the instance and their settings, such as the Agent of Cloud Security or Cloud Monitor.

    """

    def __init__(self):
        """
        :param SecurityService: Enables the Cloud Security service. If this parameter is not specified, the Cloud Security service will be enabled by default.
        :type SecurityService: :class:`tencentcloud.autoscaling.v20180419.models.RunSecurityServiceEnabled`
        :param MonitorService: Enables the Cloud Monitor service. If this parameter is not specified, the Cloud Monitor service will be enabled by default.
        :type MonitorService: :class:`tencentcloud.autoscaling.v20180419.models.RunMonitorServiceEnabled`
        """
        self.SecurityService = None
        self.MonitorService = None


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self.SecurityService = RunSecurityServiceEnabled()
            self.SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self.MonitorService = RunMonitorServiceEnabled()
            self.MonitorService._deserialize(params.get("MonitorService"))


class ExecuteScalingPolicyRequest(AbstractModel):
    """ExecuteScalingPolicy request structure.

    """

    def __init__(self):
        """
        :param AutoScalingPolicyId: Alarm-based scaling policy ID
        :type AutoScalingPolicyId: str
        :param HonorCooldown: Whether to check if the auto scaling group is in the cooldown period. Default value: false
        :type HonorCooldown: bool
        """
        self.AutoScalingPolicyId = None
        self.HonorCooldown = None


    def _deserialize(self, params):
        self.AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        self.HonorCooldown = params.get("HonorCooldown")


class ExecuteScalingPolicyResponse(AbstractModel):
    """ExecuteScalingPolicy response structure.

    """

    def __init__(self):
        """
        :param ActivityId: Scaling activity ID
        :type ActivityId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ActivityId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """> Describes key-value pair filters used for conditional queries, such as filtering results by ID, name and state.
    > * If there are multiple `Filter` parameters, the relationship among them will be logical `AND`.
    > * If there are multiple `Values` for the same `Filter`, the relationship among the `Values` for the same `Filter` will be logical `OR`.

    """

    def __init__(self):
        """
        :param Name: Field to be filtered.
        :type Name: str
        :param Values: Filter value of the field.
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class ForwardLoadBalancer(AbstractModel):
    """Application load balancer

    """

    def __init__(self):
        """
        :param LoadBalancerId: Load balancer ID
        :type LoadBalancerId: str
        :param ListenerId: Application load balancer listener ID
        :type ListenerId: str
        :param TargetAttributes: List of target rule attributes
        :type TargetAttributes: list of TargetAttribute
        :param LocationId: ID of a forwarding rule. This parameter is required for layer-7 listeners.
        :type LocationId: str
        :param Region: The region of CLB instance. It defaults to the region of AS service and is in the format of the common parameter `Region`, such as `ap-guangzhou`.
        :type Region: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.TargetAttributes = None
        self.LocationId = None
        self.Region = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("TargetAttributes") is not None:
            self.TargetAttributes = []
            for item in params.get("TargetAttributes"):
                obj = TargetAttribute()
                obj._deserialize(item)
                self.TargetAttributes.append(obj)
        self.LocationId = params.get("LocationId")
        self.Region = params.get("Region")


class HostNameSettings(AbstractModel):
    """CVM HostName settings

    """

    def __init__(self):
        """
        :param HostName: Host name of a CVM.
<br><li> A period (.) and hyphen (-) cannot be used as the first and the last characters of HostName, and multiple consecutive hyphens (-) or periods (.) are not allowed.
<br><li> No support for Windows instances.
<br><li> Other types of instances (such as Linux): the name should be a combination of 2 to 40 characters, supports multiple periods (.). The string between two periods can be composed of letters (case insensitive), numbers, and hyphens (-).
Note: This field may return null, indicating that no valid values can be obtained.
        :type HostName: str
        :param HostNameStyle: Type of CVM host name. Valid values: "ORIGINAL" and "UNIQUE". Default value: "ORIGINAL"
<br><li> ORIGINAL. Auto Scaling transfers the HostName set in input parameters to the CVM directly. CVM may adds serial numbers for the HostName. The HostName of instances within the auto scaling group may conflict.
<br><li> UNIQUE. The HostName set in input parameters is the prefix of a host name. Auto Scaling and CVM expand it. The HostName of an instance in the auto scaling group is unique.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HostNameStyle: str
        """
        self.HostName = None
        self.HostNameStyle = None


    def _deserialize(self, params):
        self.HostName = params.get("HostName")
        self.HostNameStyle = params.get("HostNameStyle")


class Instance(AbstractModel):
    """Instance information

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param LaunchConfigurationId: Launch configuration ID
        :type LaunchConfigurationId: str
        :param LaunchConfigurationName: Launch configuration name
        :type LaunchConfigurationName: str
        :param LifeCycleState: Lifecycle status. Value range: IN_SERVICE, CREATING, TERMINATING, ATTACHING, DETACHING, ATTACHING_LB, DETACHING_LB
        :type LifeCycleState: str
        :param HealthStatus: Health status. Value range: HEALTHY, UNHEALTHY
        :type HealthStatus: str
        :param ProtectedFromScaleIn: Whether to add scale-in protection
        :type ProtectedFromScaleIn: bool
        :param Zone: Availability zone
        :type Zone: str
        :param CreationType: Creation type. Value range: AUTO_CREATION, MANUAL_ATTACHING.
        :type CreationType: str
        :param AddTime: Instance addition time
        :type AddTime: str
        :param InstanceType: Instance type
        :type InstanceType: str
        :param VersionNumber: Version number
        :type VersionNumber: int
        :param AutoScalingGroupName: Auto scaling group name
        :type AutoScalingGroupName: str
        """
        self.InstanceId = None
        self.AutoScalingGroupId = None
        self.LaunchConfigurationId = None
        self.LaunchConfigurationName = None
        self.LifeCycleState = None
        self.HealthStatus = None
        self.ProtectedFromScaleIn = None
        self.Zone = None
        self.CreationType = None
        self.AddTime = None
        self.InstanceType = None
        self.VersionNumber = None
        self.AutoScalingGroupName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.LaunchConfigurationName = params.get("LaunchConfigurationName")
        self.LifeCycleState = params.get("LifeCycleState")
        self.HealthStatus = params.get("HealthStatus")
        self.ProtectedFromScaleIn = params.get("ProtectedFromScaleIn")
        self.Zone = params.get("Zone")
        self.CreationType = params.get("CreationType")
        self.AddTime = params.get("AddTime")
        self.InstanceType = params.get("InstanceType")
        self.VersionNumber = params.get("VersionNumber")
        self.AutoScalingGroupName = params.get("AutoScalingGroupName")


class InstanceChargePrepaid(AbstractModel):
    """This describes the billing method of an instance

    """

    def __init__(self):
        """
        :param Period: Purchased usage period of an instance in months. Value range: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.
        :type Period: int
        :param RenewFlag: Auto-renewal flag. Value range: <br><li>NOTIFY_AND_AUTO_RENEW: Notify expiry and renew automatically <br><li>NOTIFY_AND_MANUAL_RENEW: Notify expiry but not renew automatically <br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: Neither notify expiry nor renew automatically <br><br>Default value: NOTIFY_AND_MANUAL_RENEW. If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis if the account balance is sufficient.
        :type RenewFlag: str
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")


class InstanceMarketOptionsRequest(AbstractModel):
    """Options related to a CVM bidding request

    """

    def __init__(self):
        """
        :param SpotOptions: Bidding-related options
        :type SpotOptions: :class:`tencentcloud.autoscaling.v20180419.models.SpotMarketOptions`
        :param MarketType: Market option type. Currently, this only supports the value "spot"
Note: This field may return null, indicating that no valid values can be obtained.
        :type MarketType: str
        """
        self.SpotOptions = None
        self.MarketType = None


    def _deserialize(self, params):
        if params.get("SpotOptions") is not None:
            self.SpotOptions = SpotMarketOptions()
            self.SpotOptions._deserialize(params.get("SpotOptions"))
        self.MarketType = params.get("MarketType")


class InstanceTag(AbstractModel):
    """Instance tag. This parameter is used to bind tags to newly added instances.

    """

    def __init__(self):
        """
        :param Key: Tag key
        :type Key: str
        :param Value: Tag value
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class InternetAccessible(AbstractModel):
    """This describes the internet accessibility of the instance created by a launch configuration and declares the internet usage billing method of the instance and the maximum bandwidth

    """

    def __init__(self):
        """
        :param InternetChargeType: Network billing method. Value range: <br><li>BANDWIDTH_PREPAID: Prepaid by bandwidth <br><li>TRAFFIC_POSTPAID_BY_HOUR: Postpaid by traffic on a per hour basis <br><li>BANDWIDTH_POSTPAID_BY_HOUR: Postpaid by bandwidth on a per hour basis <br><li>BANDWIDTH_PACKAGE: BWP user <br>Default value: TRAFFIC_POSTPAID_BY_HOUR.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: The maximum outbound bandwidth in Mbps of the public network. The default value is 0 Mbps. The upper limit of bandwidth varies by model. For more information, see [Purchase Network Bandwidth](https://cloud.tencent.com/document/product/213/509).
Note: This field may return null, indicating that no valid values can be obtained.
        :type InternetMaxBandwidthOut: int
        :param PublicIpAssigned: Whether to assign a public IP. Value range: <br><li>TRUE: Assign a public IP <br><li>FALSE: Do not assign a public IP <br><br>If the public network bandwidth is greater than 0 Mbps, you are free to choose whether to enable the public IP (which is enabled by default). If the public network bandwidth is 0 Mbps, no public IP will be allowed to be assigned.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicIpAssigned: bool
        """
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.PublicIpAssigned = None


    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.PublicIpAssigned = params.get("PublicIpAssigned")


class LaunchConfiguration(AbstractModel):
    """Information set of eligible launch configurations.

    """

    def __init__(self):
        """
        :param ProjectId: Project ID of the instance.
        :type ProjectId: int
        :param LaunchConfigurationId: Launch configuration ID.
        :type LaunchConfigurationId: str
        :param LaunchConfigurationName: Launch configuration name.
        :type LaunchConfigurationName: str
        :param InstanceType: Instance model.
        :type InstanceType: str
        :param SystemDisk: Information of the instance's system disk configuration.
        :type SystemDisk: :class:`tencentcloud.autoscaling.v20180419.models.SystemDisk`
        :param DataDisks: Information of the instance's data disk configuration.
        :type DataDisks: list of DataDisk
        :param LoginSettings: Instance login settings.
        :type LoginSettings: :class:`tencentcloud.autoscaling.v20180419.models.LimitedLoginSettings`
        :param InternetAccessible: Information of the public network bandwidth configuration.
        :type InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        :param SecurityGroupIds: Security group of the instance.
        :type SecurityGroupIds: list of str
        :param AutoScalingGroupAbstractSet: Auto scaling group associated with the launch configuration.
        :type AutoScalingGroupAbstractSet: list of AutoScalingGroupAbstract
        :param UserData: Custom data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserData: str
        :param CreatedTime: Creation time of the launch configuration.
        :type CreatedTime: str
        :param EnhancedService: Conditions of enhancement services for the instance and their settings.
        :type EnhancedService: :class:`tencentcloud.autoscaling.v20180419.models.EnhancedService`
        :param ImageId: Image ID.
        :type ImageId: str
        :param LaunchConfigurationStatus: Current status of the launch configuration. Value range: <br><li>NORMAL: normal <br><li>IMAGE_ABNORMAL: Exception with the image of the launch configuration <br><li>CBS_SNAP_ABNORMAL: Exception with the data disk snapshot of the launch configuration <br><li>SECURITY_GROUP_ABNORMAL: Exception with the security group of the launch configuration<br>
        :type LaunchConfigurationStatus: str
        :param InstanceChargeType: Instance billing type. CVM instances are POSTPAID_BY_HOUR by default.
<br><li>POSTPAID_BY_HOUR: Pay-as-you-go on an hourly basis
<br><li>SPOTPAID: Bidding
        :type InstanceChargeType: str
        :param InstanceMarketOptions: Market-related options of the instance, such as the parameters related to stop instances. If the billing method of instance is specified as bidding, this parameter must be passed in.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceMarketOptions: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        :param InstanceTypes: List of instance models.
        :type InstanceTypes: list of str
        :param InstanceTags: List of tags.
        :type InstanceTags: list of InstanceTag
        :param VersionNumber: Version number.
        :type VersionNumber: int
        :param UpdatedTime: Update time.
        :type UpdatedTime: str
        :param CamRoleName: CAM role name, which can be obtained from the roleName field in the return value of the DescribeRoleList API.
        :type CamRoleName: str
        :param LastOperationInstanceTypesCheckPolicy: Value of InstanceTypesCheckPolicy upon the last operation.
        :type LastOperationInstanceTypesCheckPolicy: str
        :param HostNameSettings: CVM HostName settings.
        :type HostNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.HostNameSettings`
        """
        self.ProjectId = None
        self.LaunchConfigurationId = None
        self.LaunchConfigurationName = None
        self.InstanceType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.LoginSettings = None
        self.InternetAccessible = None
        self.SecurityGroupIds = None
        self.AutoScalingGroupAbstractSet = None
        self.UserData = None
        self.CreatedTime = None
        self.EnhancedService = None
        self.ImageId = None
        self.LaunchConfigurationStatus = None
        self.InstanceChargeType = None
        self.InstanceMarketOptions = None
        self.InstanceTypes = None
        self.InstanceTags = None
        self.VersionNumber = None
        self.UpdatedTime = None
        self.CamRoleName = None
        self.LastOperationInstanceTypesCheckPolicy = None
        self.HostNameSettings = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.LaunchConfigurationName = params.get("LaunchConfigurationName")
        self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LimitedLoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("AutoScalingGroupAbstractSet") is not None:
            self.AutoScalingGroupAbstractSet = []
            for item in params.get("AutoScalingGroupAbstractSet"):
                obj = AutoScalingGroupAbstract()
                obj._deserialize(item)
                self.AutoScalingGroupAbstractSet.append(obj)
        self.UserData = params.get("UserData")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.ImageId = params.get("ImageId")
        self.LaunchConfigurationStatus = params.get("LaunchConfigurationStatus")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.InstanceTypes = params.get("InstanceTypes")
        if params.get("InstanceTags") is not None:
            self.InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTag()
                obj._deserialize(item)
                self.InstanceTags.append(obj)
        self.VersionNumber = params.get("VersionNumber")
        self.UpdatedTime = params.get("UpdatedTime")
        self.CamRoleName = params.get("CamRoleName")
        self.LastOperationInstanceTypesCheckPolicy = params.get("LastOperationInstanceTypesCheckPolicy")
        if params.get("HostNameSettings") is not None:
            self.HostNameSettings = HostNameSettings()
            self.HostNameSettings._deserialize(params.get("HostNameSettings"))


class LifecycleActionResultInfo(AbstractModel):
    """Result information of the lifecycle hook action

    """

    def __init__(self):
        """
        :param LifecycleHookId: ID of the lifecycle hook
        :type LifecycleHookId: str
        :param InstanceId: ID of the instance
        :type InstanceId: str
        :param NotificationResult: Whether the notification is sent to CMQ successfully
        :type NotificationResult: str
        :param LifecycleActionResult: Result of the lifecyle hook action. Values: CONTINUE, ABANDON
        :type LifecycleActionResult: str
        :param ResultReason: Cause of the result
        :type ResultReason: str
        """
        self.LifecycleHookId = None
        self.InstanceId = None
        self.NotificationResult = None
        self.LifecycleActionResult = None
        self.ResultReason = None


    def _deserialize(self, params):
        self.LifecycleHookId = params.get("LifecycleHookId")
        self.InstanceId = params.get("InstanceId")
        self.NotificationResult = params.get("NotificationResult")
        self.LifecycleActionResult = params.get("LifecycleActionResult")
        self.ResultReason = params.get("ResultReason")


class LifecycleHook(AbstractModel):
    """Lifecycle hook

    """

    def __init__(self):
        """
        :param LifecycleHookId: Lifecycle hook ID
        :type LifecycleHookId: str
        :param LifecycleHookName: Lifecycle hook name
        :type LifecycleHookName: str
        :param AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param DefaultResult: Default result of the lifecycle hook
        :type DefaultResult: str
        :param HeartbeatTimeout: Wait timeout period of the lifecycle hook
        :type HeartbeatTimeout: int
        :param LifecycleTransition: Applicable scenario of the lifecycle hook
        :type LifecycleTransition: str
        :param NotificationMetadata: Additional information for the notification target
        :type NotificationMetadata: str
        :param CreatedTime: Creation time
        :type CreatedTime: str
        :param NotificationTarget: Notification target
        :type NotificationTarget: :class:`tencentcloud.autoscaling.v20180419.models.NotificationTarget`
        :param LifecycleTransitionType: Applicable scenario of the lifecycle hook
        :type LifecycleTransitionType: str
        """
        self.LifecycleHookId = None
        self.LifecycleHookName = None
        self.AutoScalingGroupId = None
        self.DefaultResult = None
        self.HeartbeatTimeout = None
        self.LifecycleTransition = None
        self.NotificationMetadata = None
        self.CreatedTime = None
        self.NotificationTarget = None
        self.LifecycleTransitionType = None


    def _deserialize(self, params):
        self.LifecycleHookId = params.get("LifecycleHookId")
        self.LifecycleHookName = params.get("LifecycleHookName")
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.DefaultResult = params.get("DefaultResult")
        self.HeartbeatTimeout = params.get("HeartbeatTimeout")
        self.LifecycleTransition = params.get("LifecycleTransition")
        self.NotificationMetadata = params.get("NotificationMetadata")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("NotificationTarget") is not None:
            self.NotificationTarget = NotificationTarget()
            self.NotificationTarget._deserialize(params.get("NotificationTarget"))
        self.LifecycleTransitionType = params.get("LifecycleTransitionType")


class LimitedLoginSettings(AbstractModel):
    """This describes the configuration and information related to instance login. For security reasons, sensitive information is not described.

    """

    def __init__(self):
        """
        :param KeyIds: List of key IDs.
        :type KeyIds: list of str
        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")


class LoginSettings(AbstractModel):
    """This describes the configuration and information related to instance login.

    """

    def __init__(self):
        """
        :param Password: Login password of the instance. The rule of password complexity varies by operating system: <br><li>For Linux instances, the password must be a combination of 8-16 characters comprised of at least two of the following types: [a-z, A-Z], [0-9] and [( ) ` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? / ]. <br><li>For Windows instances, the password must be a combination of 12-16 characters comprised of at least three of the following types: [a-z], [A-Z], [0-9] and [( ) ` ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /]. <br><br>If this parameter is not specified, a password will be randomly generated and sent to you via internal message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Password: str
        :param KeyIds: List of key IDs. An instance associated with the key can be accessed using the corresponding private key. KeyId can be obtained via the API DescribeKeyPairs. A key and a password cannot be specified at the same time, and specifying the key is not supported in Windows. You can specify only one key when purchasing an instance.
        :type KeyIds: list of str
        :param KeepImageLogin: Keep the original settings for an image. You cannot specify this parameter if Password or KeyIds.N is specified. You can specify this parameter to TRUE only when you create an instance using a custom image, shared image, or image imported from external resources. Value range: <br><li>TRUE: Keep the login settings for the image <br><li>FALSE: Do not keep the login settings for the image <br><br>Default value: FALSE.
Note: This field may return null, indicating that no valid values can be obtained.
        :type KeepImageLogin: bool
        """
        self.Password = None
        self.KeyIds = None
        self.KeepImageLogin = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.KeyIds = params.get("KeyIds")
        self.KeepImageLogin = params.get("KeepImageLogin")


class MetricAlarm(AbstractModel):
    """Alarming metric of AS

    """

    def __init__(self):
        """
        :param ComparisonOperator: Comparison operator. Value range: <br><li>GREATER_THAN: greater than </li><li>GREATER_THAN_OR_EQUAL_TO: greater than or equal to </li><li>LESS_THAN: less than </li><li> LESS_THAN_OR_EQUAL_TO: less than or equal to </li><li> EQUAL_TO: equal to </li> <li>NOT_EQUAL_TO: not equal to </li>
        :type ComparisonOperator: str
        :param MetricName: Metric name. Value range: <br><li>CPU_UTILIZATION: CPU utilization </li><li>MEM_UTILIZATION: memory utilization </li><li>LAN_TRAFFIC_OUT: private network outbound bandwidth </li><li>LAN_TRAFFIC_IN: private network inbound bandwidth </li><li>WAN_TRAFFIC_OUT: public network outbound bandwidth </li><li>WAN_TRAFFIC_IN: public network inbound bandwidth </li>
        :type MetricName: str
        :param Threshold: Alarming threshold: <br><li>CPU_UTILIZATION: [1, 100] in % </li><li>MEM_UTILIZATION: [1, 100] in % </li><li>LAN_TRAFFIC_OUT: >0 in Mbps </li><li>LAN_TRAFFIC_IN: >0 in Mbps </li><li>WAN_TRAFFIC_OUT: >0 in Mbps </li><li>WAN_TRAFFIC_IN: >0 in Mbps </li>
        :type Threshold: int
        :param Period: Time period in seconds. Enumerated values: 60, 300.
        :type Period: int
        :param ContinuousTime: Number of repetitions. Value range: [1, 10]
        :type ContinuousTime: int
        :param Statistic: Statistics type. Value range: <br><li>AVERAGE: average </li><li>MAXIMUM: maximum <li>MINIMUM: minimum </li><br> Default value: AVERAGE
        :type Statistic: str
        """
        self.ComparisonOperator = None
        self.MetricName = None
        self.Threshold = None
        self.Period = None
        self.ContinuousTime = None
        self.Statistic = None


    def _deserialize(self, params):
        self.ComparisonOperator = params.get("ComparisonOperator")
        self.MetricName = params.get("MetricName")
        self.Threshold = params.get("Threshold")
        self.Period = params.get("Period")
        self.ContinuousTime = params.get("ContinuousTime")
        self.Statistic = params.get("Statistic")


class ModifyAutoScalingGroupRequest(AbstractModel):
    """ModifyAutoScalingGroup request structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param AutoScalingGroupName: Auto scaling group name, which can only contain letters, numbers, underscores, hyphens ("-"), and decimal points with a maximum length of 55 bytes and must be unique under your account.
        :type AutoScalingGroupName: str
        :param DefaultCooldown: Default cooldown period in seconds. Default value: 300
        :type DefaultCooldown: int
        :param DesiredCapacity: Desired number of instances. The number should be no larger than the maximum and no smaller than minimum number of instances
        :type DesiredCapacity: int
        :param LaunchConfigurationId: Launch configuration ID
        :type LaunchConfigurationId: str
        :param MaxSize: Maximum number of instances. Value range: 0-2,000.
        :type MaxSize: int
        :param MinSize: Minimum number of instances. Value range: 0-2,000.
        :type MinSize: int
        :param ProjectId: Project ID
        :type ProjectId: int
        :param SubnetIds: List of subnet IDs
        :type SubnetIds: list of str
        :param TerminationPolicies: Termination policy. Currently, the maximum length is 1. Value range: OLDEST_INSTANCE, NEWEST_INSTANCE.
<br><li> OLDEST_INSTANCE: The oldest instance in the auto scaling group will be terminated first.
<br><li> NEWEST_INSTANCE: The newest instance in the auto scaling group will be terminated first.
        :type TerminationPolicies: list of str
        :param VpcId: VPC ID. This field is left empty for basic networks. You need to specify SubnetIds when modifying the network of the auto scaling group to a VPC with a specified VPC ID. Specify Zones when modifying the network to a basic network.
        :type VpcId: str
        :param Zones: List of availability zones
        :type Zones: list of str
        :param RetryPolicy: Retry policy. Value range: IMMEDIATE_RETRY, INCREMENTAL_INTERVALS, and NO_RETRY. Default value: IMMEDIATE_RETRY.
<br><li> IMMEDIATE_RETRY: Retrying immediately in a short period of time and stopping after a number of consecutive failures (5).
<br><li> INCREMENTAL_INTERVALS: Retrying at incremental intervals, i.e., as the number of consecutive failures increases, the retry interval gradually increases, ranging from one second to one day.
<br><li> NO_RETRY: No retry until a user call or alarm message is received again.
        :type RetryPolicy: str
        :param ZonesCheckPolicy: Availability zone verification policy. Value range: ALL, ANY. Default value: ANY. This will work when the resource-related fields (launch configuration, availability zone, or subnet) of the auto scaling group are actually modified.
<br><li> ALL: The verification will succeed only if all availability zones (Zone) or subnets (SubnetId) are available; otherwise, an error will be reported.
<br><li> ANY: The verification will success if any availability zone (Zone) or subnet (SubnetId) is available; otherwise, an error will be reported.

Common reasons why an availability zone or subnet is unavailable include stock-out of CVM instances or CBS cloud disks in the availability zone, insufficient quota in the availability zone, or insufficient IPs in the subnet.
If an availability zone or subnet in Zones/SubnetIds does not exist, a verification error will be reported regardless of the value of ZonesCheckPolicy.
        :type ZonesCheckPolicy: str
        :param ServiceSettings: Service settings such as unhealthy instance replacement.
        :type ServiceSettings: :class:`tencentcloud.autoscaling.v20180419.models.ServiceSettings`
        :param Ipv6AddressCount: 
        :type Ipv6AddressCount: int
        """
        self.AutoScalingGroupId = None
        self.AutoScalingGroupName = None
        self.DefaultCooldown = None
        self.DesiredCapacity = None
        self.LaunchConfigurationId = None
        self.MaxSize = None
        self.MinSize = None
        self.ProjectId = None
        self.SubnetIds = None
        self.TerminationPolicies = None
        self.VpcId = None
        self.Zones = None
        self.RetryPolicy = None
        self.ZonesCheckPolicy = None
        self.ServiceSettings = None
        self.Ipv6AddressCount = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.AutoScalingGroupName = params.get("AutoScalingGroupName")
        self.DefaultCooldown = params.get("DefaultCooldown")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.ProjectId = params.get("ProjectId")
        self.SubnetIds = params.get("SubnetIds")
        self.TerminationPolicies = params.get("TerminationPolicies")
        self.VpcId = params.get("VpcId")
        self.Zones = params.get("Zones")
        self.RetryPolicy = params.get("RetryPolicy")
        self.ZonesCheckPolicy = params.get("ZonesCheckPolicy")
        if params.get("ServiceSettings") is not None:
            self.ServiceSettings = ServiceSettings()
            self.ServiceSettings._deserialize(params.get("ServiceSettings"))
        self.Ipv6AddressCount = params.get("Ipv6AddressCount")


class ModifyAutoScalingGroupResponse(AbstractModel):
    """ModifyAutoScalingGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDesiredCapacityRequest(AbstractModel):
    """ModifyDesiredCapacity request structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param DesiredCapacity: Desired capacity
        :type DesiredCapacity: int
        """
        self.AutoScalingGroupId = None
        self.DesiredCapacity = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.DesiredCapacity = params.get("DesiredCapacity")


class ModifyDesiredCapacityResponse(AbstractModel):
    """ModifyDesiredCapacity response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLaunchConfigurationAttributesRequest(AbstractModel):
    """ModifyLaunchConfigurationAttributes request structure.

    """

    def __init__(self):
        """
        :param LaunchConfigurationId: Launch configuration ID
        :type LaunchConfigurationId: str
        :param ImageId: Valid [image](https://cloud.tencent.com/document/product/213/4940) ID in the format of `img-8toqc6s3`. There are four types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><li>Marketplace images </li><br/>You can obtain the available image IDs in the following ways: <br/><li>For `public images`, `custom images`, and `shared images`, log in to the [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the image IDs; for `marketplace images`, query the image IDs through [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li>This value can be obtained from the `ImageId` field in the return value of the [DescribeImages API](https://cloud.tencent.com/document/api/213/15715).</li>
        :type ImageId: str
        :param InstanceTypes: List of instance types. Different instance models specify different resource specifications. Up to 5 instance models can be supported.
The launch configuration uses InstanceType to indicate one single instance type and InstanceTypes to indicate multiple instance types. After InstanceTypes is successfully specified for the launch configuration, the original InstanceType will be automatically invalidated.
        :type InstanceTypes: list of str
        :param InstanceTypesCheckPolicy: Instance type verification policy which works when InstanceTypes is actually modified. Value range: ALL, ANY. Default value: ANY.
<br><li> ALL: The verification will success only if all instance types (InstanceType) are available; otherwise, an error will be reported.
<br><li> ANY: The verification will success if any instance type (InstanceType) is available; otherwise, an error will be reported.

Common reasons why an instance type is unavailable include stock-out of the instance type or the corresponding cloud disk.
If a model in InstanceTypes does not exist or has been discontinued, a verification error will be reported regardless of the value of InstanceTypesCheckPolicy.
        :type InstanceTypesCheckPolicy: str
        :param LaunchConfigurationName: Display name of the launch configuration, which can contain Chinese characters, letters, numbers, underscores, separators ("-"), and decimal points with a maximum length of 60 bytes.
        :type LaunchConfigurationName: str
        :param UserData: Base64-encoded custom data of up to 16 KB. If you want to clear UserData, specify it as an empty string
        :type UserData: str
        """
        self.LaunchConfigurationId = None
        self.ImageId = None
        self.InstanceTypes = None
        self.InstanceTypesCheckPolicy = None
        self.LaunchConfigurationName = None
        self.UserData = None


    def _deserialize(self, params):
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.ImageId = params.get("ImageId")
        self.InstanceTypes = params.get("InstanceTypes")
        self.InstanceTypesCheckPolicy = params.get("InstanceTypesCheckPolicy")
        self.LaunchConfigurationName = params.get("LaunchConfigurationName")
        self.UserData = params.get("UserData")


class ModifyLaunchConfigurationAttributesResponse(AbstractModel):
    """ModifyLaunchConfigurationAttributes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancersRequest(AbstractModel):
    """ModifyLoadBalancers request structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param LoadBalancerIds: List of classic CLB IDs. Currently, the maximum length is 20. You cannot specify LoadBalancerIds and ForwardLoadBalancers at the same time.
        :type LoadBalancerIds: list of str
        :param ForwardLoadBalancers: List of CLBs. Currently, the maximum length is 20. You cannot specify LoadBalancerIds and ForwardLoadBalancers at the same time.
        :type ForwardLoadBalancers: list of ForwardLoadBalancer
        :param LoadBalancersCheckPolicy: CLB verification policy. Valid values: "ALL" and "DIFF". Default value: "ALL"
<br><li> ALL. Verification is successful only when all CLBs are valid. Otherwise, verification fails.
<br><li> DIFF. Only the changes in the CLB parameters are verified. If valid, the verification is successful. Otherwise, verification fails.
        :type LoadBalancersCheckPolicy: str
        """
        self.AutoScalingGroupId = None
        self.LoadBalancerIds = None
        self.ForwardLoadBalancers = None
        self.LoadBalancersCheckPolicy = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        if params.get("ForwardLoadBalancers") is not None:
            self.ForwardLoadBalancers = []
            for item in params.get("ForwardLoadBalancers"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self.ForwardLoadBalancers.append(obj)
        self.LoadBalancersCheckPolicy = params.get("LoadBalancersCheckPolicy")


class ModifyLoadBalancersResponse(AbstractModel):
    """ModifyLoadBalancers response structure.

    """

    def __init__(self):
        """
        :param ActivityId: Scaling activity ID
        :type ActivityId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ActivityId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.RequestId = params.get("RequestId")


class ModifyNotificationConfigurationRequest(AbstractModel):
    """ModifyNotificationConfiguration request structure.

    """

    def __init__(self):
        """
        :param AutoScalingNotificationId: ID of the notification to be modified.
        :type AutoScalingNotificationId: str
        :param NotificationTypes: Notification type, i.e., the set of types of notifications to be subscribed to. Value range:
<li>SCALE_OUT_SUCCESSFUL: scale-out succeeded</li>
<li>SCALE_OUT_FAILED: scale-out failed</li>
<li>SCALE_IN_SUCCESSFUL: scale-in succeeded</li>
<li>SCALE_IN_FAILED: scale-in failed</li>
<li>REPLACE_UNHEALTHY_INSTANCE_SUCCESSFUL: unhealthy instance replacement succeeded</li>
<li>REPLACE_UNHEALTHY_INSTANCE_FAILED: unhealthy instance replacement failed</li>
        :type NotificationTypes: list of str
        :param NotificationUserGroupIds: Notification group ID, which is the set of user group IDs. You can query the user group IDs through the [ListGroups](https://cloud.tencent.com/document/product/598/34589) API.
        :type NotificationUserGroupIds: list of str
        """
        self.AutoScalingNotificationId = None
        self.NotificationTypes = None
        self.NotificationUserGroupIds = None


    def _deserialize(self, params):
        self.AutoScalingNotificationId = params.get("AutoScalingNotificationId")
        self.NotificationTypes = params.get("NotificationTypes")
        self.NotificationUserGroupIds = params.get("NotificationUserGroupIds")


class ModifyNotificationConfigurationResponse(AbstractModel):
    """ModifyNotificationConfiguration response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyScalingPolicyRequest(AbstractModel):
    """ModifyScalingPolicy request structure.

    """

    def __init__(self):
        """
        :param AutoScalingPolicyId: Alarm policy ID.
        :type AutoScalingPolicyId: str
        :param ScalingPolicyName: Alarm policy name.
        :type ScalingPolicyName: str
        :param AdjustmentType: The method to adjust the desired number of instances after the alarm is triggered. Value range: <br><li>CHANGE_IN_CAPACITY: Increase or decrease the desired number of instances </li><li>EXACT_CAPACITY: Adjust to the specified desired number of instances </li> <li>PERCENT_CHANGE_IN_CAPACITY: Adjust the desired number of instances by percentage </li>
        :type AdjustmentType: str
        :param AdjustmentValue: The adjusted value of desired number of instances after the alarm is triggered. Value range: <br><li>When AdjustmentType is CHANGE_IN_CAPACITY, if AdjustmentValue is a positive value, some new instances will be added after the alarm is triggered, and if it is a negative value, some existing instances will be removed after the alarm is triggered </li> <li> When AdjustmentType is EXACT_CAPACITY, the value of AdjustmentValue is the desired number of instances after the alarm is triggered, which should be equal to or greater than 0 </li> <li> When AdjustmentType is PERCENT_CHANGE_IN_CAPACITY, if AdjusmentValue (in %) is a positive value, new instances will be added by percentage after the alarm is triggered; if it is a negative value, existing instances will be removed by percentage after the alarm is triggered.
        :type AdjustmentValue: int
        :param Cooldown: Cooldown period in seconds.
        :type Cooldown: int
        :param MetricAlarm: Alarm monitoring metric.
        :type MetricAlarm: :class:`tencentcloud.autoscaling.v20180419.models.MetricAlarm`
        :param NotificationUserGroupIds: Notification group ID, which is the set of user group IDs. You can query the user group IDs through the [ListGroups](https://cloud.tencent.com/document/product/598/34589) API.
If you want to clear the user group, you need to pass in the specific string "NULL" to the list.
        :type NotificationUserGroupIds: list of str
        """
        self.AutoScalingPolicyId = None
        self.ScalingPolicyName = None
        self.AdjustmentType = None
        self.AdjustmentValue = None
        self.Cooldown = None
        self.MetricAlarm = None
        self.NotificationUserGroupIds = None


    def _deserialize(self, params):
        self.AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        self.ScalingPolicyName = params.get("ScalingPolicyName")
        self.AdjustmentType = params.get("AdjustmentType")
        self.AdjustmentValue = params.get("AdjustmentValue")
        self.Cooldown = params.get("Cooldown")
        if params.get("MetricAlarm") is not None:
            self.MetricAlarm = MetricAlarm()
            self.MetricAlarm._deserialize(params.get("MetricAlarm"))
        self.NotificationUserGroupIds = params.get("NotificationUserGroupIds")


class ModifyScalingPolicyResponse(AbstractModel):
    """ModifyScalingPolicy response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyScheduledActionRequest(AbstractModel):
    """ModifyScheduledAction request structure.

    """

    def __init__(self):
        """
        :param ScheduledActionId: ID of the scheduled task to be edited
        :type ScheduledActionId: str
        :param ScheduledActionName: Scheduled task name, which can only contain letters, numbers, underscores, hyphens ("-"), and decimal points with a maximum length of 60 bytes and must be unique in an auto scaling group.
        :type ScheduledActionName: str
        :param MaxSize: The maximum number of instances set for the auto scaling group when the scheduled task is triggered.
        :type MaxSize: int
        :param MinSize: The minimum number of instances set for the auto scaling group when the scheduled task is triggered.
        :type MinSize: int
        :param DesiredCapacity: The desired number of instances set for the auto scaling group when the scheduled task is triggered.
        :type DesiredCapacity: int
        :param StartTime: Initial triggered time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard.
        :type StartTime: str
        :param EndTime: End time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard. <br>This parameter and `Recurrence` need to be specified at the same time. After the end time, the scheduled task will no longer take effect.
        :type EndTime: str
        :param Recurrence: Repeating mode of the scheduled task, which is in standard cron format. <br>This parameter and `EndTime` need to be specified at the same time.
        :type Recurrence: str
        """
        self.ScheduledActionId = None
        self.ScheduledActionName = None
        self.MaxSize = None
        self.MinSize = None
        self.DesiredCapacity = None
        self.StartTime = None
        self.EndTime = None
        self.Recurrence = None


    def _deserialize(self, params):
        self.ScheduledActionId = params.get("ScheduledActionId")
        self.ScheduledActionName = params.get("ScheduledActionName")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Recurrence = params.get("Recurrence")


class ModifyScheduledActionResponse(AbstractModel):
    """ModifyScheduledAction response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NotificationTarget(AbstractModel):
    """Notification target

    """

    def __init__(self):
        """
        :param TargetType: Target type. Value range: `CMQ_QUEUE`, `CMQ_TOPIC`.
<li> CMQ_QUEUE: CMQ_QUEUE: CMQ queue model.</li>
<li> CMQ_TOPIC: CMQ topic model.</li>
        :type TargetType: str
        :param QueueName: Queue name. If `TargetType` is `CMQ_QUEUE`, this parameter is required.
        :type QueueName: str
        :param TopicName: Topic name. If `TargetType` is `CMQ_TOPIC`, this parameter is required.
        :type TopicName: str
        """
        self.TargetType = None
        self.QueueName = None
        self.TopicName = None


    def _deserialize(self, params):
        self.TargetType = params.get("TargetType")
        self.QueueName = params.get("QueueName")
        self.TopicName = params.get("TopicName")


class PaiInstance(AbstractModel):
    """PAI instance

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param DomainName: Instance domain name
        :type DomainName: str
        :param PaiMateUrl: 
        :type PaiMateUrl: str
        """
        self.InstanceId = None
        self.DomainName = None
        self.PaiMateUrl = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DomainName = params.get("DomainName")
        self.PaiMateUrl = params.get("PaiMateUrl")


class PreviewPaiDomainNameRequest(AbstractModel):
    """PreviewPaiDomainName request structure.

    """

    def __init__(self):
        """
        :param DomainNameType: Domain name type
        :type DomainNameType: str
        """
        self.DomainNameType = None


    def _deserialize(self, params):
        self.DomainNameType = params.get("DomainNameType")


class PreviewPaiDomainNameResponse(AbstractModel):
    """PreviewPaiDomainName response structure.

    """

    def __init__(self):
        """
        :param DomainName: Available PAI domain name
        :type DomainName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DomainName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.RequestId = params.get("RequestId")


class RemoveInstancesRequest(AbstractModel):
    """RemoveInstances request structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param InstanceIds: List of CVM instance IDs
        :type InstanceIds: list of str
        """
        self.AutoScalingGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.InstanceIds = params.get("InstanceIds")


class RemoveInstancesResponse(AbstractModel):
    """RemoveInstances response structure.

    """

    def __init__(self):
        """
        :param ActivityId: Scaling activity ID
        :type ActivityId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ActivityId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.RequestId = params.get("RequestId")


class RunMonitorServiceEnabled(AbstractModel):
    """This describes the information related to the Cloud Monitor service.

    """

    def __init__(self):
        """
        :param Enabled: Whether to enable the [Cloud Monitor](https://cloud.tencent.com/document/product/248) service. Value range: <br><li>TRUE: Cloud Monitor is enabled <br><li>FALSE: Cloud Monitor is disabled <br><br>Default value: TRUE. |
Note: This field may return null, indicating that no valid values can be obtained.
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")


class RunSecurityServiceEnabled(AbstractModel):
    """This describes the information on the Cloud Security service

    """

    def __init__(self):
        """
        :param Enabled: Whether to enable the [Cloud Security](https://cloud.tencent.com/document/product/296) service. Value range: <br><li>TRUE: Cloud Security is enabled <br><li>FALSE: Cloud Security is disabled <br><br>Default value: TRUE.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")


class ScalingPolicy(AbstractModel):
    """Alarm trigger policy.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID.
        :type AutoScalingGroupId: str
        :param AutoScalingPolicyId: Alarm trigger policy ID.
        :type AutoScalingPolicyId: str
        :param ScalingPolicyName: Alarm trigger policy name.
        :type ScalingPolicyName: str
        :param AdjustmentType: The method to adjust the desired number of instances after the alarm is triggered. Value range: <br><li>CHANGE_IN_CAPACITY: Increase or decrease the desired number of instances </li><li>EXACT_CAPACITY: Adjust to the specified desired number of instances </li> <li>PERCENT_CHANGE_IN_CAPACITY: Adjust the desired number of instances by percentage </li>
        :type AdjustmentType: str
        :param AdjustmentValue: The adjusted value of desired number of instances after the alarm is triggered.
        :type AdjustmentValue: int
        :param Cooldown: Cooldown period.
        :type Cooldown: int
        :param MetricAlarm: Alarm monitoring metric.
        :type MetricAlarm: :class:`tencentcloud.autoscaling.v20180419.models.MetricAlarm`
        :param NotificationUserGroupIds: Notification group ID, which is the set of user group IDs.
        :type NotificationUserGroupIds: list of str
        """
        self.AutoScalingGroupId = None
        self.AutoScalingPolicyId = None
        self.ScalingPolicyName = None
        self.AdjustmentType = None
        self.AdjustmentValue = None
        self.Cooldown = None
        self.MetricAlarm = None
        self.NotificationUserGroupIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        self.ScalingPolicyName = params.get("ScalingPolicyName")
        self.AdjustmentType = params.get("AdjustmentType")
        self.AdjustmentValue = params.get("AdjustmentValue")
        self.Cooldown = params.get("Cooldown")
        if params.get("MetricAlarm") is not None:
            self.MetricAlarm = MetricAlarm()
            self.MetricAlarm._deserialize(params.get("MetricAlarm"))
        self.NotificationUserGroupIds = params.get("NotificationUserGroupIds")


class ScheduledAction(AbstractModel):
    """This describes the information of a scheduled task.

    """

    def __init__(self):
        """
        :param ScheduledActionId: Scheduled task ID.
        :type ScheduledActionId: str
        :param ScheduledActionName: Scheduled task name.
        :type ScheduledActionName: str
        :param AutoScalingGroupId: ID of the auto scaling group where the scheduled task is located.
        :type AutoScalingGroupId: str
        :param StartTime: Start time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard.
        :type StartTime: str
        :param Recurrence: Repeating mode of the scheduled task.
        :type Recurrence: str
        :param EndTime: End time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard.
        :type EndTime: str
        :param MaxSize: Maximum number of instances set by the scheduled task.
        :type MaxSize: int
        :param DesiredCapacity: Desired number of instances set by the scheduled task.
        :type DesiredCapacity: int
        :param MinSize: Minimum number of instances set by the scheduled task.
        :type MinSize: int
        :param CreatedTime: Creation time of the scheduled task. The value is in `UTC time` in the format of `YYYY-MM-DDThh:mm:ssZ` according to the `ISO8601` standard.
        :type CreatedTime: str
        """
        self.ScheduledActionId = None
        self.ScheduledActionName = None
        self.AutoScalingGroupId = None
        self.StartTime = None
        self.Recurrence = None
        self.EndTime = None
        self.MaxSize = None
        self.DesiredCapacity = None
        self.MinSize = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.ScheduledActionId = params.get("ScheduledActionId")
        self.ScheduledActionName = params.get("ScheduledActionName")
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.StartTime = params.get("StartTime")
        self.Recurrence = params.get("Recurrence")
        self.EndTime = params.get("EndTime")
        self.MaxSize = params.get("MaxSize")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.MinSize = params.get("MinSize")
        self.CreatedTime = params.get("CreatedTime")


class ServiceSettings(AbstractModel):
    """Service settings

    """

    def __init__(self):
        """
        :param ReplaceMonitorUnhealthy: Enables unhealthy instance replacement. If this feature is enabled, AS will replace instances that are flagged as unhealthy by Cloud Monitor. If this parameter is not specified, the value will be False by default.
        :type ReplaceMonitorUnhealthy: bool
        """
        self.ReplaceMonitorUnhealthy = None


    def _deserialize(self, params):
        self.ReplaceMonitorUnhealthy = params.get("ReplaceMonitorUnhealthy")


class SetInstancesProtectionRequest(AbstractModel):
    """SetInstancesProtection request structure.

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Auto scaling group ID.
        :type AutoScalingGroupId: str
        :param InstanceIds: Instance ID.
        :type InstanceIds: list of str
        :param ProtectedFromScaleIn: Whether the instance needs to be protected from scale-in.
        :type ProtectedFromScaleIn: bool
        """
        self.AutoScalingGroupId = None
        self.InstanceIds = None
        self.ProtectedFromScaleIn = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.InstanceIds = params.get("InstanceIds")
        self.ProtectedFromScaleIn = params.get("ProtectedFromScaleIn")


class SetInstancesProtectionResponse(AbstractModel):
    """SetInstancesProtection response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SpotMarketOptions(AbstractModel):
    """Bidding-related options

    """

    def __init__(self):
        """
        :param MaxPrice: Bidding price such as "1.05"
        :type MaxPrice: str
        :param SpotInstanceType: Bid request type. Currently, only "one-time" type is supported. Default value: one-time
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpotInstanceType: str
        """
        self.MaxPrice = None
        self.SpotInstanceType = None


    def _deserialize(self, params):
        self.MaxPrice = params.get("MaxPrice")
        self.SpotInstanceType = params.get("SpotInstanceType")


class SystemDisk(AbstractModel):
    """System disk configuration of the launch configuration. If this parameter is not specified, the default value is assigned to it.

    """

    def __init__(self):
        """
        :param DiskType: System disk type. For more information on limits of system disk types, see [CVM Instance Configuration](https://cloud.tencent.com/document/product/213/2177). Value range: <br><li>LOCAL_BASIC: Local disk <br><li>LOCAL_SSD: Local SSD disk <br><li>CLOUD_BASIC: HDD cloud disk <br><li>CLOUD_PREMIUM: Premium cloud disk <br><li>CLOUD_SSD: SSD cloud disk <br><br>Default value: LOCAL_BASIC.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param DiskSize: System disk size in GB. Default value: 50
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskSize: int
        """
        self.DiskType = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")


class Tag(AbstractModel):
    """Resource type and tag key-value pair

    """

    def __init__(self):
        """
        :param Key: Tag key
        :type Key: str
        :param Value: Tag value
        :type Value: str
        :param ResourceType: Type of the resource binded to the tag. Currently supported types include "auto-scaling-group"
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceType: str
        """
        self.Key = None
        self.Value = None
        self.ResourceType = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.ResourceType = params.get("ResourceType")


class TargetAttribute(AbstractModel):
    """Load balancer target attribute

    """

    def __init__(self):
        """
        :param Port: Port
        :type Port: int
        :param Weight: Weight
        :type Weight: int
        """
        self.Port = None
        self.Weight = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")


class UpgradeLaunchConfigurationRequest(AbstractModel):
    """UpgradeLaunchConfiguration request structure.

    """

    def __init__(self):
        """
        :param LaunchConfigurationId: Launch configuration ID.
        :type LaunchConfigurationId: str
        :param ImageId: Valid [image](https://cloud.tencent.com/document/product/213/4940) ID in the format of `img-8toqc6s3`. There are four types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><li>Marketplace images </li><br/>You can obtain the available image IDs in the following ways: <br/><li>For `public images`, `custom images`, and `shared images`, log in to the [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the image IDs; for `marketplace images`, query the image IDs through [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li>This value can be obtained from the `ImageId` field in the return value of the [DescribeImages API](https://cloud.tencent.com/document/api/213/15715).</li>
        :type ImageId: str
        :param InstanceTypes: List of instance models. Different instance models specify different resource specifications. Up to 5 instance models can be supported.
        :type InstanceTypes: list of str
        :param LaunchConfigurationName: Display name of the launch configuration, which can contain Chinese characters, letters, numbers, underscores, separators ("-"), and decimal points with a maximum length of 60 bytes.
        :type LaunchConfigurationName: str
        :param DataDisks: Information of the instance's data disk configuration. If this parameter is not specified, no data disk is purchased by default. Up to 11 data disks can be supported.
        :type DataDisks: list of DataDisk
        :param EnhancedService: Enhanced service. This parameter is used to specify whether to enable Cloud Security, Cloud Monitoring and other services. If this parameter is not specified, Cloud Monitoring and Cloud Security will be enabled by default.
        :type EnhancedService: :class:`tencentcloud.autoscaling.v20180419.models.EnhancedService`
        :param InstanceChargeType: Instance billing type. CVM instances are POSTPAID_BY_HOUR by default.
<br><li>POSTPAID_BY_HOUR: Pay-as-you-go on an hourly basis
<br><li>SPOTPAID: Bidding
        :type InstanceChargeType: str
        :param InstanceMarketOptions: Market-related options of the instance, such as the parameters related to stop instances. If the billing method of instance is specified as bidding, this parameter must be passed in.
        :type InstanceMarketOptions: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        :param InstanceTypesCheckPolicy: Instance type verification policy. Value range: ALL, ANY. Default value: ANY.
<br><li> ALL: The verification will success only if all instance types (InstanceType) are available; otherwise, an error will be reported.
<br><li> ANY: The verification will success if any instance type (InstanceType) is available; otherwise, an error will be reported.

Common reasons why an instance type is unavailable include stock-out of the instance type and the corresponding cloud disk.
If a model in InstanceTypes does not exist or has been deactivated, a verification error will be reported regardless of the value of InstanceTypesCheckPolicy.
        :type InstanceTypesCheckPolicy: str
        :param InternetAccessible: Configuration information of public network bandwidth. If this parameter is not specified, the default public network bandwidth is 0 Mbps.
        :type InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        :param LoginSettings: Login settings of the instance. This parameter is used to set the login password and key for the instance, or to keep the original login settings for the image. By default, a random password is generated and sent to the user via the internal message.
        :type LoginSettings: :class:`tencentcloud.autoscaling.v20180419.models.LoginSettings`
        :param ProjectId: Project ID of the instance. This parameter can be obtained from the `projectId` field in the returned values of [DescribeProject](https://cloud.tencent.com/document/api/378/4400). If this is left empty, default project is used.
        :type ProjectId: int
        :param SecurityGroupIds: The security group of instance. This parameter can be obtained by calling the `SecurityGroupId` field in the returned value of [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808). If this parameter is not specified, no security group will be bound by default.
        :type SecurityGroupIds: list of str
        :param SystemDisk: System disk configuration of the instance. If this parameter is not specified, the default value will be assigned to it.
        :type SystemDisk: :class:`tencentcloud.autoscaling.v20180419.models.SystemDisk`
        :param UserData: Base64-encoded custom data of up to 16 KB.
        :type UserData: str
        :param InstanceTags: List of tags. This parameter is used to bind up to 10 tags to newly added instances.
        :type InstanceTags: list of InstanceTag
        :param CamRoleName: CAM role name, which can be obtained from the roleName field in the return value of the DescribeRoleList API.
        :type CamRoleName: str
        :param HostNameSettings: CVM HostName settings.
        :type HostNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.HostNameSettings`
        """
        self.LaunchConfigurationId = None
        self.ImageId = None
        self.InstanceTypes = None
        self.LaunchConfigurationName = None
        self.DataDisks = None
        self.EnhancedService = None
        self.InstanceChargeType = None
        self.InstanceMarketOptions = None
        self.InstanceTypesCheckPolicy = None
        self.InternetAccessible = None
        self.LoginSettings = None
        self.ProjectId = None
        self.SecurityGroupIds = None
        self.SystemDisk = None
        self.UserData = None
        self.InstanceTags = None
        self.CamRoleName = None
        self.HostNameSettings = None


    def _deserialize(self, params):
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.ImageId = params.get("ImageId")
        self.InstanceTypes = params.get("InstanceTypes")
        self.LaunchConfigurationName = params.get("LaunchConfigurationName")
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.InstanceTypesCheckPolicy = params.get("InstanceTypesCheckPolicy")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.ProjectId = params.get("ProjectId")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        self.UserData = params.get("UserData")
        if params.get("InstanceTags") is not None:
            self.InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTag()
                obj._deserialize(item)
                self.InstanceTags.append(obj)
        self.CamRoleName = params.get("CamRoleName")
        if params.get("HostNameSettings") is not None:
            self.HostNameSettings = HostNameSettings()
            self.HostNameSettings._deserialize(params.get("HostNameSettings"))


class UpgradeLaunchConfigurationResponse(AbstractModel):
    """UpgradeLaunchConfiguration response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeLifecycleHookRequest(AbstractModel):
    """UpgradeLifecycleHook request structure.

    """

    def __init__(self):
        """
        :param LifecycleHookId: Lifecycle hook ID
        :type LifecycleHookId: str
        :param LifecycleHookName: Lifecycle hook name
        :type LifecycleHookName: str
        :param LifecycleTransition: Scenario for the lifecycle hook. Value range: "INSTANCE_LAUNCHING", "INSTANCE_TERMINATING"
        :type LifecycleTransition: str
        :param DefaultResult: Defines the action to be taken by the auto scaling group upon lifecycle hook timeout. Value range: "CONTINUE", "ABANDON". Default value: "CONTINUE"
        :type DefaultResult: str
        :param HeartbeatTimeout: The maximum length of time (in seconds) that can elapse before the lifecycle hook times out. Value range: 30-3,600. Default value: 300
        :type HeartbeatTimeout: int
        :param NotificationMetadata: Additional information sent by AS to the notification target. The default value is ''
        :type NotificationMetadata: str
        :param NotificationTarget: Notification target
        :type NotificationTarget: :class:`tencentcloud.autoscaling.v20180419.models.NotificationTarget`
        :param LifecycleTransitionType: The scenario where the lifecycle hook is applied. `EXTENSION`: the lifecycle hook will be triggered when AttachInstances, DetachInstances or RemoveInstaces is called. `NORMAL`: the lifecycle hook is not triggered by the above APIs. 
        :type LifecycleTransitionType: str
        """
        self.LifecycleHookId = None
        self.LifecycleHookName = None
        self.LifecycleTransition = None
        self.DefaultResult = None
        self.HeartbeatTimeout = None
        self.NotificationMetadata = None
        self.NotificationTarget = None
        self.LifecycleTransitionType = None


    def _deserialize(self, params):
        self.LifecycleHookId = params.get("LifecycleHookId")
        self.LifecycleHookName = params.get("LifecycleHookName")
        self.LifecycleTransition = params.get("LifecycleTransition")
        self.DefaultResult = params.get("DefaultResult")
        self.HeartbeatTimeout = params.get("HeartbeatTimeout")
        self.NotificationMetadata = params.get("NotificationMetadata")
        if params.get("NotificationTarget") is not None:
            self.NotificationTarget = NotificationTarget()
            self.NotificationTarget._deserialize(params.get("NotificationTarget"))
        self.LifecycleTransitionType = params.get("LifecycleTransitionType")


class UpgradeLifecycleHookResponse(AbstractModel):
    """UpgradeLifecycleHook response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")