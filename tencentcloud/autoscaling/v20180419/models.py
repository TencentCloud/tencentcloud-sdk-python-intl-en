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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class Activity(AbstractModel):
    """Information on eligible scaling activities.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID.
        :type AutoScalingGroupId: str
        :param _ActivityId: Scaling activity ID.
        :type ActivityId: str
        :param _ActivityType: Type of the scaling activity. Valid values:<br>
<li>`SCALE_OUT`: Scale out. <li>`SCALE_IN`: Scale in. <li>`ATTACH_INSTANCES`: Add instances. <li>`REMOVE_INSTANCES`: Terminate instances. <li>`DETACH_INSTANCES`: Remove instances. <li>`TERMINATE_INSTANCES_UNEXPECTEDLY`: Terminate instances in the CVM console. <li>`REPLACE_UNHEALTHY_INSTANCE`: Replace an unhealthy instance.
<li>`START_INSTANCES`: Starts up instances.
<li>`STOP_INSTANCES`: Shut down instances.
<li>`INVOKE_COMMAND`: Execute commands
        :type ActivityType: str
        :param _StatusCode: Scaling activity status. Value range:<br>
<li>INIT: initializing
<li>RUNNING: running
<li>SUCCESSFUL: succeeded
<li>PARTIALLY_SUCCESSFUL: partially succeeded
<li>FAILED: failed
<li>CANCELLED: canceled
        :type StatusCode: str
        :param _StatusMessage: Description of the scaling activity status.
        :type StatusMessage: str
        :param _Cause: Cause of the scaling activity.
        :type Cause: str
        :param _Description: Description of the scaling activity.
        :type Description: str
        :param _StartTime: Start time of the scaling activity.
        :type StartTime: str
        :param _EndTime: End time of the scaling activity.
        :type EndTime: str
        :param _CreatedTime: Creation time of the scaling activity.
        :type CreatedTime: str
        :param _ActivityRelatedInstanceSet: This parameter has been deprecated.
        :type ActivityRelatedInstanceSet: list of ActivtyRelatedInstance
        :param _StatusMessageSimplified: Brief description of the scaling activity status.
        :type StatusMessageSimplified: str
        :param _LifecycleActionResultSet: Result of the lifecycle hook action in the scaling activity
        :type LifecycleActionResultSet: list of LifecycleActionResultInfo
        :param _DetailedStatusMessageSet: Detailed description of scaling activity status
        :type DetailedStatusMessageSet: list of DetailedStatusMessage
        :param _InvocationResultSet: Result of the command execution
        :type InvocationResultSet: list of InvocationResult
        :param _RelatedInstanceSet: Information set of the instances related to the scaling activity.
        :type RelatedInstanceSet: list of RelatedInstance
        """
        self._AutoScalingGroupId = None
        self._ActivityId = None
        self._ActivityType = None
        self._StatusCode = None
        self._StatusMessage = None
        self._Cause = None
        self._Description = None
        self._StartTime = None
        self._EndTime = None
        self._CreatedTime = None
        self._ActivityRelatedInstanceSet = None
        self._StatusMessageSimplified = None
        self._LifecycleActionResultSet = None
        self._DetailedStatusMessageSet = None
        self._InvocationResultSet = None
        self._RelatedInstanceSet = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def ActivityType(self):
        return self._ActivityType

    @ActivityType.setter
    def ActivityType(self, ActivityType):
        self._ActivityType = ActivityType

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def StatusMessage(self):
        return self._StatusMessage

    @StatusMessage.setter
    def StatusMessage(self, StatusMessage):
        self._StatusMessage = StatusMessage

    @property
    def Cause(self):
        return self._Cause

    @Cause.setter
    def Cause(self, Cause):
        self._Cause = Cause

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ActivityRelatedInstanceSet(self):
        warnings.warn("parameter `ActivityRelatedInstanceSet` is deprecated", DeprecationWarning) 

        return self._ActivityRelatedInstanceSet

    @ActivityRelatedInstanceSet.setter
    def ActivityRelatedInstanceSet(self, ActivityRelatedInstanceSet):
        warnings.warn("parameter `ActivityRelatedInstanceSet` is deprecated", DeprecationWarning) 

        self._ActivityRelatedInstanceSet = ActivityRelatedInstanceSet

    @property
    def StatusMessageSimplified(self):
        return self._StatusMessageSimplified

    @StatusMessageSimplified.setter
    def StatusMessageSimplified(self, StatusMessageSimplified):
        self._StatusMessageSimplified = StatusMessageSimplified

    @property
    def LifecycleActionResultSet(self):
        return self._LifecycleActionResultSet

    @LifecycleActionResultSet.setter
    def LifecycleActionResultSet(self, LifecycleActionResultSet):
        self._LifecycleActionResultSet = LifecycleActionResultSet

    @property
    def DetailedStatusMessageSet(self):
        return self._DetailedStatusMessageSet

    @DetailedStatusMessageSet.setter
    def DetailedStatusMessageSet(self, DetailedStatusMessageSet):
        self._DetailedStatusMessageSet = DetailedStatusMessageSet

    @property
    def InvocationResultSet(self):
        return self._InvocationResultSet

    @InvocationResultSet.setter
    def InvocationResultSet(self, InvocationResultSet):
        self._InvocationResultSet = InvocationResultSet

    @property
    def RelatedInstanceSet(self):
        return self._RelatedInstanceSet

    @RelatedInstanceSet.setter
    def RelatedInstanceSet(self, RelatedInstanceSet):
        self._RelatedInstanceSet = RelatedInstanceSet


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._ActivityId = params.get("ActivityId")
        self._ActivityType = params.get("ActivityType")
        self._StatusCode = params.get("StatusCode")
        self._StatusMessage = params.get("StatusMessage")
        self._Cause = params.get("Cause")
        self._Description = params.get("Description")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CreatedTime = params.get("CreatedTime")
        if params.get("ActivityRelatedInstanceSet") is not None:
            self._ActivityRelatedInstanceSet = []
            for item in params.get("ActivityRelatedInstanceSet"):
                obj = ActivtyRelatedInstance()
                obj._deserialize(item)
                self._ActivityRelatedInstanceSet.append(obj)
        self._StatusMessageSimplified = params.get("StatusMessageSimplified")
        if params.get("LifecycleActionResultSet") is not None:
            self._LifecycleActionResultSet = []
            for item in params.get("LifecycleActionResultSet"):
                obj = LifecycleActionResultInfo()
                obj._deserialize(item)
                self._LifecycleActionResultSet.append(obj)
        if params.get("DetailedStatusMessageSet") is not None:
            self._DetailedStatusMessageSet = []
            for item in params.get("DetailedStatusMessageSet"):
                obj = DetailedStatusMessage()
                obj._deserialize(item)
                self._DetailedStatusMessageSet.append(obj)
        if params.get("InvocationResultSet") is not None:
            self._InvocationResultSet = []
            for item in params.get("InvocationResultSet"):
                obj = InvocationResult()
                obj._deserialize(item)
                self._InvocationResultSet.append(obj)
        if params.get("RelatedInstanceSet") is not None:
            self._RelatedInstanceSet = []
            for item in params.get("RelatedInstanceSet"):
                obj = RelatedInstance()
                obj._deserialize(item)
                self._RelatedInstanceSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivtyRelatedInstance(AbstractModel):
    """Information of the instances related to the current scaling activity.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _InstanceStatus: Status of the instance in the scaling activity. Value range:
<li>INIT: initializing
<li>RUNNING: running
<li>SUCCESSFUL: succeeded
<li>FAILED: failed
        :type InstanceStatus: str
        """
        self._InstanceId = None
        self._InstanceStatus = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceStatus = params.get("InstanceStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Advice(AbstractModel):
    """Suggestions for scaling group configurations.

    """

    def __init__(self):
        r"""
        :param _Problem: Problem Description
        :type Problem: str
        :param _Detail: Problem Details
        :type Detail: str
        :param _Solution: Recommended resolutions
        :type Solution: str
        :param _Level: u200dRisk level of the scaling group configuration. Valid values: <br>
<li>WARNING<br>
<li>CRITICAL<br>
        :type Level: str
        """
        self._Problem = None
        self._Detail = None
        self._Solution = None
        self._Level = None

    @property
    def Problem(self):
        return self._Problem

    @Problem.setter
    def Problem(self, Problem):
        self._Problem = Problem

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Solution(self):
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level


    def _deserialize(self, params):
        self._Problem = params.get("Problem")
        self._Detail = params.get("Detail")
        self._Solution = params.get("Solution")
        self._Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachInstancesRequest(AbstractModel):
    """AttachInstances request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param _InstanceIds: List of CVM instance IDs
        :type InstanceIds: list of str
        """
        self._AutoScalingGroupId = None
        self._InstanceIds = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachInstancesResponse(AbstractModel):
    """AttachInstances response structure.

    """

    def __init__(self):
        r"""
        :param _ActivityId: Scaling activity ID
        :type ActivityId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class AttachLoadBalancersRequest(AbstractModel):
    """AttachLoadBalancers request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Scaling group ID
        :type AutoScalingGroupId: str
        :param _LoadBalancerIds: List of classic CLB IDs. Up to 20 classic CLBs can be bound to a security group. `LoadBalancerIds` and `ForwardLoadBalancers` cannot be specified at the same time.
        :type LoadBalancerIds: list of str
        :param _ForwardLoadBalancers: List of application CLBs. Up to 100 application CLBs can be bound to a scaling group. `LoadBalancerIds` and `ForwardLoadBalancers` cannot be specified at the same time.
        :type ForwardLoadBalancers: list of ForwardLoadBalancer
        """
        self._AutoScalingGroupId = None
        self._LoadBalancerIds = None
        self._ForwardLoadBalancers = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ForwardLoadBalancers(self):
        return self._ForwardLoadBalancers

    @ForwardLoadBalancers.setter
    def ForwardLoadBalancers(self, ForwardLoadBalancers):
        self._ForwardLoadBalancers = ForwardLoadBalancers


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        if params.get("ForwardLoadBalancers") is not None:
            self._ForwardLoadBalancers = []
            for item in params.get("ForwardLoadBalancers"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self._ForwardLoadBalancers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachLoadBalancersResponse(AbstractModel):
    """AttachLoadBalancers response structure.

    """

    def __init__(self):
        r"""
        :param _ActivityId: Scaling activity ID
        :type ActivityId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class AutoScalingAdvice(AbstractModel):
    """Suggestions for scaling group configurations.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Scaling group ID
        :type AutoScalingGroupId: str
        :param _Level: Scaling group warning level. Valid values:<br>
<li>NORMAL: Normal<br>
<li>WARNING: Warning<br>
<li>CRITICAL: Serious warning<br>
        :type Level: str
        :param _Advices: A collection of suggestions for scaling group configurations.
        :type Advices: list of Advice
        """
        self._AutoScalingGroupId = None
        self._Level = None
        self._Advices = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Advices(self):
        return self._Advices

    @Advices.setter
    def Advices(self, Advices):
        self._Advices = Advices


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._Level = params.get("Level")
        if params.get("Advices") is not None:
            self._Advices = []
            for item in params.get("Advices"):
                obj = Advice()
                obj._deserialize(item)
                self._Advices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScalingGroup(AbstractModel):
    """Auto scaling group

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param _AutoScalingGroupName: Auto scaling group name
        :type AutoScalingGroupName: str
        :param _AutoScalingGroupStatus: Current scaling group status. Valid values:<br>
<li>NORMAL: Normal<br>
<li>CVM_ABNORMAL: Abnormal launch configuration<br>
<li>LB_ABNORMAL: Abnormal load balancer<br>
<li>LB_LISTENER_ABNORMAL: Abnormal load balancer listener<br>
<li>LB_LOCATION_ABNORMAL: Abnormal forwarding configuration of the load balancer listener<br>
<li>VPC_ABNORMAL: VPC network error<br>
<li>SUBNET_ABNORMAL: VPC subnet exception<br>
<li>INSUFFICIENT_BALANCE: Insufficient account balance<br>
<li>LB_BACKEND_REGION_NOT_MATCH: The CLB backend and the AS service are not in the same region.<br>
<li>LB_BACKEND_VPC_NOT_MATCH: The CLB instance and the scaling group are not in the same VPC.
        :type AutoScalingGroupStatus: str
        :param _CreatedTime: Creation time in UTC format
        :type CreatedTime: str
        :param _DefaultCooldown: Default cooldown period in seconds
        :type DefaultCooldown: int
        :param _DesiredCapacity: Desired number of instances
        :type DesiredCapacity: int
        :param _EnabledStatus: Enabled status. Value range: `ENABLED`, `DISABLED`
        :type EnabledStatus: str
        :param _ForwardLoadBalancerSet: List of application load balancers
        :type ForwardLoadBalancerSet: list of ForwardLoadBalancer
        :param _InstanceCount: Number of instances
        :type InstanceCount: int
        :param _InServiceInstanceCount: Number of instances in `IN_SERVICE` status
        :type InServiceInstanceCount: int
        :param _LaunchConfigurationId: Launch configuration ID
        :type LaunchConfigurationId: str
        :param _LaunchConfigurationName: Launch configuration name
        :type LaunchConfigurationName: str
        :param _LoadBalancerIdSet: List of Classic load balancer IDs
        :type LoadBalancerIdSet: list of str
        :param _MaxSize: Maximum number of instances
        :type MaxSize: int
        :param _MinSize: Minimum number of instances
        :type MinSize: int
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _SubnetIdSet: List of subnet IDs
        :type SubnetIdSet: list of str
        :param _TerminationPolicySet: Termination policy
        :type TerminationPolicySet: list of str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _ZoneSet: List of availability zones
        :type ZoneSet: list of str
        :param _RetryPolicy: Retry policy
        :type RetryPolicy: str
        :param _InActivityStatus: Whether the auto scaling group is performing a scaling activity. `IN_ACTIVITY` indicates yes, and `NOT_IN_ACTIVITY` indicates no.
        :type InActivityStatus: str
        :param _Tags: List of auto scaling group tags
        :type Tags: list of Tag
        :param _ServiceSettings: Service settings
        :type ServiceSettings: :class:`tencentcloud.autoscaling.v20180419.models.ServiceSettings`
        :param _Ipv6AddressCount: The number of IPv6 addresses that an instance has.
        :type Ipv6AddressCount: int
        :param _MultiZoneSubnetPolicy: The policy applied when there are multiple availability zones/subnets
<br><li> PRIORITY: when creating instances, choose the availability zone/subnet based on the order in the list from top to bottom. If the first instance is successfully created in the availability zone/subnet of the highest priority, all instances will be created in this availability zone/subnet.
<br><li> EQUALITY: chooses the availability zone/subnet with the least instances for scale-out. This gives each availability zone/subnet an opportunity for scale-out and disperses the instances created during multiple scale-out operations across different availability zones/subnets.
        :type MultiZoneSubnetPolicy: str
        :param _HealthCheckType: Health check type of instances in a scaling group.<br><li>CVM: confirm whether an instance is healthy based on the network status. If the pinged instance is unreachable, the instance will be considered unhealthy. For more information, see [Instance Health Check](https://intl.cloud.tencent.com/document/product/377/8553?from_cn_redirect=1)<br><li>CLB: confirm whether an instance is healthy based on the CLB health check status. For more information, see [Health Check Overview](https://intl.cloud.tencent.com/document/product/214/6097?from_cn_redirect=1).
        :type HealthCheckType: str
        :param _LoadBalancerHealthCheckGracePeriod: Grace period of the CLB health check
        :type LoadBalancerHealthCheckGracePeriod: int
        :param _InstanceAllocationPolicy: Specifies how to assign instances. Valid values: `LAUNCH_CONFIGURATION` and `SPOT_MIXED`.
<br><li>`LAUNCH_CONFIGURATION`: the launch configuration mode.
<br><li>`SPOT_MIXED`: a mixed instance mode. Currently, this mode is supported only when the launch configuration takes the pay-as-you-go billing mode. With this mode, the scaling group can provision a combination of pay-as-you-go instances and spot instances to meet the configured capacity. Note that the billing mode of the associated launch configuration cannot be modified when this mode is used.
        :type InstanceAllocationPolicy: str
        :param _SpotMixedAllocationPolicy: Specifies how to assign pay-as-you-go instances and spot instances.
A valid value will be returned only when `InstanceAllocationPolicy` is set to `SPOT_MIXED`.
        :type SpotMixedAllocationPolicy: :class:`tencentcloud.autoscaling.v20180419.models.SpotMixedAllocationPolicy`
        :param _CapacityRebalance: Indicates whether the capacity rebalancing feature is enabled. This parameter is only valid for spot instances in the scaling group. Valid values:
<br><li>`TRUE`: yes. Before the spot instances in the scaling group are about to be automatically repossessed, AS will terminate them. The scale-in hook (if configured) will take effect before the termination. After the termination process starts, AS will asynchronously initiate a scaling activity to meet the desired capacity.
<br><li>`FALSE`: no. AS will add instances to meet the desired capacity only after the spot instances are terminated.
        :type CapacityRebalance: bool
        """
        self._AutoScalingGroupId = None
        self._AutoScalingGroupName = None
        self._AutoScalingGroupStatus = None
        self._CreatedTime = None
        self._DefaultCooldown = None
        self._DesiredCapacity = None
        self._EnabledStatus = None
        self._ForwardLoadBalancerSet = None
        self._InstanceCount = None
        self._InServiceInstanceCount = None
        self._LaunchConfigurationId = None
        self._LaunchConfigurationName = None
        self._LoadBalancerIdSet = None
        self._MaxSize = None
        self._MinSize = None
        self._ProjectId = None
        self._SubnetIdSet = None
        self._TerminationPolicySet = None
        self._VpcId = None
        self._ZoneSet = None
        self._RetryPolicy = None
        self._InActivityStatus = None
        self._Tags = None
        self._ServiceSettings = None
        self._Ipv6AddressCount = None
        self._MultiZoneSubnetPolicy = None
        self._HealthCheckType = None
        self._LoadBalancerHealthCheckGracePeriod = None
        self._InstanceAllocationPolicy = None
        self._SpotMixedAllocationPolicy = None
        self._CapacityRebalance = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def AutoScalingGroupName(self):
        return self._AutoScalingGroupName

    @AutoScalingGroupName.setter
    def AutoScalingGroupName(self, AutoScalingGroupName):
        self._AutoScalingGroupName = AutoScalingGroupName

    @property
    def AutoScalingGroupStatus(self):
        return self._AutoScalingGroupStatus

    @AutoScalingGroupStatus.setter
    def AutoScalingGroupStatus(self, AutoScalingGroupStatus):
        self._AutoScalingGroupStatus = AutoScalingGroupStatus

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def DefaultCooldown(self):
        return self._DefaultCooldown

    @DefaultCooldown.setter
    def DefaultCooldown(self, DefaultCooldown):
        self._DefaultCooldown = DefaultCooldown

    @property
    def DesiredCapacity(self):
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def EnabledStatus(self):
        return self._EnabledStatus

    @EnabledStatus.setter
    def EnabledStatus(self, EnabledStatus):
        self._EnabledStatus = EnabledStatus

    @property
    def ForwardLoadBalancerSet(self):
        return self._ForwardLoadBalancerSet

    @ForwardLoadBalancerSet.setter
    def ForwardLoadBalancerSet(self, ForwardLoadBalancerSet):
        self._ForwardLoadBalancerSet = ForwardLoadBalancerSet

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def InServiceInstanceCount(self):
        return self._InServiceInstanceCount

    @InServiceInstanceCount.setter
    def InServiceInstanceCount(self, InServiceInstanceCount):
        self._InServiceInstanceCount = InServiceInstanceCount

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def LaunchConfigurationName(self):
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def LoadBalancerIdSet(self):
        return self._LoadBalancerIdSet

    @LoadBalancerIdSet.setter
    def LoadBalancerIdSet(self, LoadBalancerIdSet):
        self._LoadBalancerIdSet = LoadBalancerIdSet

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SubnetIdSet(self):
        return self._SubnetIdSet

    @SubnetIdSet.setter
    def SubnetIdSet(self, SubnetIdSet):
        self._SubnetIdSet = SubnetIdSet

    @property
    def TerminationPolicySet(self):
        return self._TerminationPolicySet

    @TerminationPolicySet.setter
    def TerminationPolicySet(self, TerminationPolicySet):
        self._TerminationPolicySet = TerminationPolicySet

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ZoneSet(self):
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

    @property
    def RetryPolicy(self):
        return self._RetryPolicy

    @RetryPolicy.setter
    def RetryPolicy(self, RetryPolicy):
        self._RetryPolicy = RetryPolicy

    @property
    def InActivityStatus(self):
        return self._InActivityStatus

    @InActivityStatus.setter
    def InActivityStatus(self, InActivityStatus):
        self._InActivityStatus = InActivityStatus

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ServiceSettings(self):
        return self._ServiceSettings

    @ServiceSettings.setter
    def ServiceSettings(self, ServiceSettings):
        self._ServiceSettings = ServiceSettings

    @property
    def Ipv6AddressCount(self):
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount

    @property
    def MultiZoneSubnetPolicy(self):
        return self._MultiZoneSubnetPolicy

    @MultiZoneSubnetPolicy.setter
    def MultiZoneSubnetPolicy(self, MultiZoneSubnetPolicy):
        self._MultiZoneSubnetPolicy = MultiZoneSubnetPolicy

    @property
    def HealthCheckType(self):
        return self._HealthCheckType

    @HealthCheckType.setter
    def HealthCheckType(self, HealthCheckType):
        self._HealthCheckType = HealthCheckType

    @property
    def LoadBalancerHealthCheckGracePeriod(self):
        return self._LoadBalancerHealthCheckGracePeriod

    @LoadBalancerHealthCheckGracePeriod.setter
    def LoadBalancerHealthCheckGracePeriod(self, LoadBalancerHealthCheckGracePeriod):
        self._LoadBalancerHealthCheckGracePeriod = LoadBalancerHealthCheckGracePeriod

    @property
    def InstanceAllocationPolicy(self):
        return self._InstanceAllocationPolicy

    @InstanceAllocationPolicy.setter
    def InstanceAllocationPolicy(self, InstanceAllocationPolicy):
        self._InstanceAllocationPolicy = InstanceAllocationPolicy

    @property
    def SpotMixedAllocationPolicy(self):
        return self._SpotMixedAllocationPolicy

    @SpotMixedAllocationPolicy.setter
    def SpotMixedAllocationPolicy(self, SpotMixedAllocationPolicy):
        self._SpotMixedAllocationPolicy = SpotMixedAllocationPolicy

    @property
    def CapacityRebalance(self):
        return self._CapacityRebalance

    @CapacityRebalance.setter
    def CapacityRebalance(self, CapacityRebalance):
        self._CapacityRebalance = CapacityRebalance


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._AutoScalingGroupName = params.get("AutoScalingGroupName")
        self._AutoScalingGroupStatus = params.get("AutoScalingGroupStatus")
        self._CreatedTime = params.get("CreatedTime")
        self._DefaultCooldown = params.get("DefaultCooldown")
        self._DesiredCapacity = params.get("DesiredCapacity")
        self._EnabledStatus = params.get("EnabledStatus")
        if params.get("ForwardLoadBalancerSet") is not None:
            self._ForwardLoadBalancerSet = []
            for item in params.get("ForwardLoadBalancerSet"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self._ForwardLoadBalancerSet.append(obj)
        self._InstanceCount = params.get("InstanceCount")
        self._InServiceInstanceCount = params.get("InServiceInstanceCount")
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._LaunchConfigurationName = params.get("LaunchConfigurationName")
        self._LoadBalancerIdSet = params.get("LoadBalancerIdSet")
        self._MaxSize = params.get("MaxSize")
        self._MinSize = params.get("MinSize")
        self._ProjectId = params.get("ProjectId")
        self._SubnetIdSet = params.get("SubnetIdSet")
        self._TerminationPolicySet = params.get("TerminationPolicySet")
        self._VpcId = params.get("VpcId")
        self._ZoneSet = params.get("ZoneSet")
        self._RetryPolicy = params.get("RetryPolicy")
        self._InActivityStatus = params.get("InActivityStatus")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("ServiceSettings") is not None:
            self._ServiceSettings = ServiceSettings()
            self._ServiceSettings._deserialize(params.get("ServiceSettings"))
        self._Ipv6AddressCount = params.get("Ipv6AddressCount")
        self._MultiZoneSubnetPolicy = params.get("MultiZoneSubnetPolicy")
        self._HealthCheckType = params.get("HealthCheckType")
        self._LoadBalancerHealthCheckGracePeriod = params.get("LoadBalancerHealthCheckGracePeriod")
        self._InstanceAllocationPolicy = params.get("InstanceAllocationPolicy")
        if params.get("SpotMixedAllocationPolicy") is not None:
            self._SpotMixedAllocationPolicy = SpotMixedAllocationPolicy()
            self._SpotMixedAllocationPolicy._deserialize(params.get("SpotMixedAllocationPolicy"))
        self._CapacityRebalance = params.get("CapacityRebalance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScalingGroupAbstract(AbstractModel):
    """Brief information of a scaling group.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Scaling group ID
        :type AutoScalingGroupId: str
        :param _AutoScalingGroupName: Auto scaling group name.
        :type AutoScalingGroupName: str
        """
        self._AutoScalingGroupId = None
        self._AutoScalingGroupName = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def AutoScalingGroupName(self):
        return self._AutoScalingGroupName

    @AutoScalingGroupName.setter
    def AutoScalingGroupName(self, AutoScalingGroupName):
        self._AutoScalingGroupName = AutoScalingGroupName


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._AutoScalingGroupName = params.get("AutoScalingGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScalingNotification(AbstractModel):
    """AS event notification

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID.
        :type AutoScalingGroupId: str
        :param _NotificationUserGroupIds: List of user group IDs.
        :type NotificationUserGroupIds: list of str
        :param _NotificationTypes: List of notification events.
        :type NotificationTypes: list of str
        :param _AutoScalingNotificationId: Event notification ID.
        :type AutoScalingNotificationId: str
        :param _TargetType: Notification receiver type.
        :type TargetType: str
        :param _QueueName: CMQ queue name.
        :type QueueName: str
        :param _TopicName: CMQ topic name.
        :type TopicName: str
        """
        self._AutoScalingGroupId = None
        self._NotificationUserGroupIds = None
        self._NotificationTypes = None
        self._AutoScalingNotificationId = None
        self._TargetType = None
        self._QueueName = None
        self._TopicName = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def NotificationUserGroupIds(self):
        return self._NotificationUserGroupIds

    @NotificationUserGroupIds.setter
    def NotificationUserGroupIds(self, NotificationUserGroupIds):
        self._NotificationUserGroupIds = NotificationUserGroupIds

    @property
    def NotificationTypes(self):
        return self._NotificationTypes

    @NotificationTypes.setter
    def NotificationTypes(self, NotificationTypes):
        self._NotificationTypes = NotificationTypes

    @property
    def AutoScalingNotificationId(self):
        return self._AutoScalingNotificationId

    @AutoScalingNotificationId.setter
    def AutoScalingNotificationId(self, AutoScalingNotificationId):
        self._AutoScalingNotificationId = AutoScalingNotificationId

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._NotificationUserGroupIds = params.get("NotificationUserGroupIds")
        self._NotificationTypes = params.get("NotificationTypes")
        self._AutoScalingNotificationId = params.get("AutoScalingNotificationId")
        self._TargetType = params.get("TargetType")
        self._QueueName = params.get("QueueName")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearLaunchConfigurationAttributesRequest(AbstractModel):
    """ClearLaunchConfigurationAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _LaunchConfigurationId: Launch configuration ID
        :type LaunchConfigurationId: str
        :param _ClearDataDisks: Whether to clear data disk information. This parameter is optional and the default value is `false`.
Setting it to `true` will clear data disks, which means that CVM newly created on this launch configuration will have no data disk.
        :type ClearDataDisks: bool
        :param _ClearHostNameSettings: Whether to clear the CVM hostname settings. This parameter is optional and the default value is `false`.
Setting it to `true` will clear the hostname settings, which means that CVM newly created on this launch configuration will have no hostname.
        :type ClearHostNameSettings: bool
        :param _ClearInstanceNameSettings: Whether to clear the CVM instance name settings. This parameter is optional and the default value is `false`.
Setting it to `true` will clear the instance name settings, which means that CVM newly created on this launch configuration will be named in the “as-{{AutoScalingGroupName}} format.
        :type ClearInstanceNameSettings: bool
        :param _ClearDisasterRecoverGroupIds: Whether to clear placement group information. This parameter is optional. Default value: `false`.
`True` means clearing placement group information. After that, no placement groups are specified for CVMs created based on the information.
        :type ClearDisasterRecoverGroupIds: bool
        """
        self._LaunchConfigurationId = None
        self._ClearDataDisks = None
        self._ClearHostNameSettings = None
        self._ClearInstanceNameSettings = None
        self._ClearDisasterRecoverGroupIds = None

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def ClearDataDisks(self):
        return self._ClearDataDisks

    @ClearDataDisks.setter
    def ClearDataDisks(self, ClearDataDisks):
        self._ClearDataDisks = ClearDataDisks

    @property
    def ClearHostNameSettings(self):
        return self._ClearHostNameSettings

    @ClearHostNameSettings.setter
    def ClearHostNameSettings(self, ClearHostNameSettings):
        self._ClearHostNameSettings = ClearHostNameSettings

    @property
    def ClearInstanceNameSettings(self):
        return self._ClearInstanceNameSettings

    @ClearInstanceNameSettings.setter
    def ClearInstanceNameSettings(self, ClearInstanceNameSettings):
        self._ClearInstanceNameSettings = ClearInstanceNameSettings

    @property
    def ClearDisasterRecoverGroupIds(self):
        return self._ClearDisasterRecoverGroupIds

    @ClearDisasterRecoverGroupIds.setter
    def ClearDisasterRecoverGroupIds(self, ClearDisasterRecoverGroupIds):
        self._ClearDisasterRecoverGroupIds = ClearDisasterRecoverGroupIds


    def _deserialize(self, params):
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._ClearDataDisks = params.get("ClearDataDisks")
        self._ClearHostNameSettings = params.get("ClearHostNameSettings")
        self._ClearInstanceNameSettings = params.get("ClearInstanceNameSettings")
        self._ClearDisasterRecoverGroupIds = params.get("ClearDisasterRecoverGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearLaunchConfigurationAttributesResponse(AbstractModel):
    """ClearLaunchConfigurationAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CompleteLifecycleActionRequest(AbstractModel):
    """CompleteLifecycleAction request structure.

    """

    def __init__(self):
        r"""
        :param _LifecycleHookId: Lifecycle hook ID
        :type LifecycleHookId: str
        :param _LifecycleActionResult: Result of the lifecycle action. Value range: "CONTINUE", "ABANDON"
        :type LifecycleActionResult: str
        :param _InstanceId: Instance ID. Either "InstanceId" or "LifecycleActionToken" must be specified
        :type InstanceId: str
        :param _LifecycleActionToken: Either "InstanceId" or "LifecycleActionToken" must be specified
        :type LifecycleActionToken: str
        """
        self._LifecycleHookId = None
        self._LifecycleActionResult = None
        self._InstanceId = None
        self._LifecycleActionToken = None

    @property
    def LifecycleHookId(self):
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def LifecycleActionResult(self):
        return self._LifecycleActionResult

    @LifecycleActionResult.setter
    def LifecycleActionResult(self, LifecycleActionResult):
        self._LifecycleActionResult = LifecycleActionResult

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LifecycleActionToken(self):
        return self._LifecycleActionToken

    @LifecycleActionToken.setter
    def LifecycleActionToken(self, LifecycleActionToken):
        self._LifecycleActionToken = LifecycleActionToken


    def _deserialize(self, params):
        self._LifecycleHookId = params.get("LifecycleHookId")
        self._LifecycleActionResult = params.get("LifecycleActionResult")
        self._InstanceId = params.get("InstanceId")
        self._LifecycleActionToken = params.get("LifecycleActionToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteLifecycleActionResponse(AbstractModel):
    """CompleteLifecycleAction response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateAutoScalingGroupFromInstanceRequest(AbstractModel):
    """CreateAutoScalingGroupFromInstance request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupName: The scaling group name. It must be unique under your account. The name can only contain letters, numbers, underscore, hyphen “-” and periods. It cannot exceed 55 bytes.
        :type AutoScalingGroupName: str
        :param _InstanceId: The instance ID.
        :type InstanceId: str
        :param _MinSize: The minimum number of instances. Value range: 0-2000.
        :type MinSize: int
        :param _MaxSize: The maximum number of instances. Value range: 0-2000.
        :type MaxSize: int
        :param _DesiredCapacity: The desired capacity. Its value must be greater than the minimum and smaller than the maximum.
        :type DesiredCapacity: int
        :param _InheritInstanceTag: Whether to inherit the instance tag. Default value: False
        :type InheritInstanceTag: bool
        """
        self._AutoScalingGroupName = None
        self._InstanceId = None
        self._MinSize = None
        self._MaxSize = None
        self._DesiredCapacity = None
        self._InheritInstanceTag = None

    @property
    def AutoScalingGroupName(self):
        return self._AutoScalingGroupName

    @AutoScalingGroupName.setter
    def AutoScalingGroupName(self, AutoScalingGroupName):
        self._AutoScalingGroupName = AutoScalingGroupName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def DesiredCapacity(self):
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def InheritInstanceTag(self):
        return self._InheritInstanceTag

    @InheritInstanceTag.setter
    def InheritInstanceTag(self, InheritInstanceTag):
        self._InheritInstanceTag = InheritInstanceTag


    def _deserialize(self, params):
        self._AutoScalingGroupName = params.get("AutoScalingGroupName")
        self._InstanceId = params.get("InstanceId")
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        self._DesiredCapacity = params.get("DesiredCapacity")
        self._InheritInstanceTag = params.get("InheritInstanceTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoScalingGroupFromInstanceResponse(AbstractModel):
    """CreateAutoScalingGroupFromInstance response structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: The scaling group ID.
        :type AutoScalingGroupId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoScalingGroupId = None
        self._RequestId = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._RequestId = params.get("RequestId")


class CreateAutoScalingGroupRequest(AbstractModel):
    """CreateAutoScalingGroup request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupName: Auto scaling group name, which can only contain letters, numbers, underscores, hyphens ("-"), and decimal points with a maximum length of 55 bytes and must be unique under your account.
        :type AutoScalingGroupName: str
        :param _LaunchConfigurationId: Launch configuration ID
        :type LaunchConfigurationId: str
        :param _MaxSize: Maximum number of instances. Value range: 0-2,000.
        :type MaxSize: int
        :param _MinSize: Minimum number of instances. Value range: 0-2,000.
        :type MinSize: int
        :param _VpcId: VPC ID; if on a basic network, enter an empty string
        :type VpcId: str
        :param _DefaultCooldown: Default cooldown period in seconds. Default value: 300
        :type DefaultCooldown: int
        :param _DesiredCapacity: Desired number of instances. The number should be no larger than the maximum and no smaller than minimum number of instances
        :type DesiredCapacity: int
        :param _LoadBalancerIds: List of classic CLB IDs. Currently, the maximum length is 20. You cannot specify LoadBalancerIds and ForwardLoadBalancers at the same time.
        :type LoadBalancerIds: list of str
        :param _ProjectId: Project ID of an instance in a scaling group. The default project is used if it’s left blank.
        :type ProjectId: int
        :param _ForwardLoadBalancers: List of application CLBs. Up to 100 CLBs are allowed. `LoadBalancerIds` and `ForwardLoadBalancers` cannot be specified at the same time.
        :type ForwardLoadBalancers: list of ForwardLoadBalancer
        :param _SubnetIds: List of subnet IDs. A subnet must be specified in the VPC scenario. If multiple subnets are entered, their priority will be determined by the order in which they are entered, and they will be tried one by one until instances can be successfully created.
        :type SubnetIds: list of str
        :param _TerminationPolicies: Termination policy. Currently, the maximum length is 1. Value range: OLDEST_INSTANCE, NEWEST_INSTANCE. Default value: OLDEST_INSTANCE.
<br><li> OLDEST_INSTANCE: The oldest instance in the auto scaling group will be terminated first.
<br><li> NEWEST_INSTANCE: The newest instance in the auto scaling group will be terminated first.
        :type TerminationPolicies: list of str
        :param _Zones: List of availability zones. An availability zone must be specified in the basic network scenario. If multiple availability zones are entered, their priority will be determined by the order in which they are entered, and they will be tried one by one until instances can be successfully created.
        :type Zones: list of str
        :param _RetryPolicy: Retry policy. Valid values: `IMMEDIATE_RETRY` (default), `INCREMENTAL_INTERVALS`, `NO_RETRY`. A partially successful scaling is judged as a failed one.
<br><li>`IMMEDIATE_RETRY`: Retry immediately. Stop retrying after five consecutive failures.
<br><li>`INCREMENTAL_INTERVALS`: Retry at incremental intervals. As the number of consecutive failures increases, the retry interval gradually increases, ranging from seconds to one day.
<br><li>`NO_RETRY`: Do not retry. Actions are taken when the next call or alarm message comes.
        :type RetryPolicy: str
        :param _ZonesCheckPolicy: Availability zone verification policy. Value range: ALL, ANY. Default value: ANY.
<br><li> ALL: The verification will succeed only if all availability zones (Zone) or subnets (SubnetId) are available; otherwise, an error will be reported.
<br><li> ANY: The verification will success if any availability zone (Zone) or subnet (SubnetId) is available; otherwise, an error will be reported.

Common reasons why an availability zone or subnet is unavailable include stock-out of CVM instances or CBS cloud disks in the availability zone, insufficient quota in the availability zone, or insufficient IPs in the subnet.
If an availability zone or subnet in Zones/SubnetIds does not exist, a verification error will be reported regardless of the value of ZonesCheckPolicy.
        :type ZonesCheckPolicy: str
        :param _Tags: List of tag descriptions. In this parameter, you can specify the tags to be bound with a scaling group as well as corresponding resource instances. Each scaling group can have up to 30 tags.
        :type Tags: list of Tag
        :param _ServiceSettings: Service settings such as unhealthy instance replacement.
        :type ServiceSettings: :class:`tencentcloud.autoscaling.v20180419.models.ServiceSettings`
        :param _Ipv6AddressCount: The number of IPv6 addresses that an instance has. Valid values: 0 and 1. Default value: 0.
        :type Ipv6AddressCount: int
        :param _MultiZoneSubnetPolicy: Multi-availability zone/subnet policy. Valid values: PRIORITY and EQUALITY. Default value: PRIORITY.
<br><li> PRIORITY: when creating instances, choose the availability zone/subnet based on the order in the list from top to bottom. If the first instance is successfully created in the availability zone/subnet of the highest priority, all instances will be created in this availability zone/subnet.
<br><li>EQUALITY: instances created for scale-out are distributed to multiple availability zones/subnets, so as to keep the number of instances in different availability zone/subnet in balance.

Notes: 
<br><li> When the scaling group is based on the classic network, this policy applies to multiple availability zones. When the scaling group is based on a VPC, this policy applies to multiple subnets, and you do not need to consider availability zones. For example, if you have four subnets (A, B, C, and D) and A, B, and C are in availability zone 1 and D is in availability zone 2, you only need to decide the order of the four subnets, without worrying about the issue of availability zones.
<br><li> This policy is applicable to multiple availability zones/subnets, but is not applicable to multiple models with launch configurations. Specify the models according to the model priority.
<br><li> When creating instances based on the PRIORITY policy, apply the multi-model policy and then apply the multi-availability zones/subnet policy. For example, if you have models A and B and subnets 1, 2, and 3, creation will be attempted in the following order: A1, A2, A3, B1, B2, and B3. If A1 is sold out, A2 (not B1) is tried next.
        :type MultiZoneSubnetPolicy: str
        :param _HealthCheckType: Health check type of instances in a scaling group.<br><li>CVM: confirm whether an instance is healthy based on the network status. If the pinged instance is unreachable, the instance will be considered unhealthy. For more information, see [Instance Health Check](https://intl.cloud.tencent.com/document/product/377/8553?from_cn_redirect=1)<br><li>CLB: confirm whether an instance is healthy based on the CLB health check status. For more information, see [Health Check Overview](https://intl.cloud.tencent.com/document/product/214/6097?from_cn_redirect=1).<br>If the parameter is set to `CLB`, the scaling group will check both the network status and the CLB health check status. If the network check indicates unhealthy, the `HealthStatus` field will return `UNHEALTHY`. If the CLB health check indicates unhealthy, the `HealthStatus` field will return `CLB_UNHEALTHY`. If both checks indicate unhealthy, the `HealthStatus` field will return `UNHEALTHY|CLB_UNHEALTHY`. Default value: `CLB`.
        :type HealthCheckType: str
        :param _LoadBalancerHealthCheckGracePeriod: Grace period of the CLB health check during which the `IN_SERVICE` instances added will not be marked as `CLB_UNHEALTHY`.<br>Valid range: 0-7200, in seconds. Default value: `0`.
        :type LoadBalancerHealthCheckGracePeriod: int
        :param _InstanceAllocationPolicy: Specifies how to assign instances. Valid values: `LAUNCH_CONFIGURATION` and `SPOT_MIXED`; default value: `LAUNCH_CONFIGURATION`.
<br><li>`LAUNCH_CONFIGURATION`: the launch configuration mode.
<br><li>`SPOT_MIXED`: a mixed instance mode. Currently, this mode is supported only when the launch configuration takes the pay-as-you-go billing mode. With this mode, the scaling group can provision a combination of pay-as-you-go instances and spot instances to meet the configured capacity. Note that the billing mode of the associated launch configuration cannot be modified when this mode is used.
        :type InstanceAllocationPolicy: str
        :param _SpotMixedAllocationPolicy: Specifies how to assign pay-as-you-go instances and spot instances.
This parameter is valid only when `InstanceAllocationPolicy ` is set to `SPOT_MIXED`.
        :type SpotMixedAllocationPolicy: :class:`tencentcloud.autoscaling.v20180419.models.SpotMixedAllocationPolicy`
        :param _CapacityRebalance: Indicates whether the capacity re-balancing feature is enabled. This parameter is only valid for spot instances in the scaling group. Valid values:
<br><li>`TRUE`: yes. Before the spot instances in the scaling group are about to be automatically repossessed, AS will terminate them. The scale-in hook (if configured) will take effect before the termination. After the termination process starts, AS will asynchronously initiate a scaling activity to meet the desired capacity.
<br><li>`FALSE`: no. In this case, AS will add instances to meet the desired capacity only after the spot instances are terminated.

Default value: `False`.
        :type CapacityRebalance: bool
        """
        self._AutoScalingGroupName = None
        self._LaunchConfigurationId = None
        self._MaxSize = None
        self._MinSize = None
        self._VpcId = None
        self._DefaultCooldown = None
        self._DesiredCapacity = None
        self._LoadBalancerIds = None
        self._ProjectId = None
        self._ForwardLoadBalancers = None
        self._SubnetIds = None
        self._TerminationPolicies = None
        self._Zones = None
        self._RetryPolicy = None
        self._ZonesCheckPolicy = None
        self._Tags = None
        self._ServiceSettings = None
        self._Ipv6AddressCount = None
        self._MultiZoneSubnetPolicy = None
        self._HealthCheckType = None
        self._LoadBalancerHealthCheckGracePeriod = None
        self._InstanceAllocationPolicy = None
        self._SpotMixedAllocationPolicy = None
        self._CapacityRebalance = None

    @property
    def AutoScalingGroupName(self):
        return self._AutoScalingGroupName

    @AutoScalingGroupName.setter
    def AutoScalingGroupName(self, AutoScalingGroupName):
        self._AutoScalingGroupName = AutoScalingGroupName

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def DefaultCooldown(self):
        return self._DefaultCooldown

    @DefaultCooldown.setter
    def DefaultCooldown(self, DefaultCooldown):
        self._DefaultCooldown = DefaultCooldown

    @property
    def DesiredCapacity(self):
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ForwardLoadBalancers(self):
        return self._ForwardLoadBalancers

    @ForwardLoadBalancers.setter
    def ForwardLoadBalancers(self, ForwardLoadBalancers):
        self._ForwardLoadBalancers = ForwardLoadBalancers

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def TerminationPolicies(self):
        return self._TerminationPolicies

    @TerminationPolicies.setter
    def TerminationPolicies(self, TerminationPolicies):
        self._TerminationPolicies = TerminationPolicies

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RetryPolicy(self):
        return self._RetryPolicy

    @RetryPolicy.setter
    def RetryPolicy(self, RetryPolicy):
        self._RetryPolicy = RetryPolicy

    @property
    def ZonesCheckPolicy(self):
        return self._ZonesCheckPolicy

    @ZonesCheckPolicy.setter
    def ZonesCheckPolicy(self, ZonesCheckPolicy):
        self._ZonesCheckPolicy = ZonesCheckPolicy

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ServiceSettings(self):
        return self._ServiceSettings

    @ServiceSettings.setter
    def ServiceSettings(self, ServiceSettings):
        self._ServiceSettings = ServiceSettings

    @property
    def Ipv6AddressCount(self):
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount

    @property
    def MultiZoneSubnetPolicy(self):
        return self._MultiZoneSubnetPolicy

    @MultiZoneSubnetPolicy.setter
    def MultiZoneSubnetPolicy(self, MultiZoneSubnetPolicy):
        self._MultiZoneSubnetPolicy = MultiZoneSubnetPolicy

    @property
    def HealthCheckType(self):
        return self._HealthCheckType

    @HealthCheckType.setter
    def HealthCheckType(self, HealthCheckType):
        self._HealthCheckType = HealthCheckType

    @property
    def LoadBalancerHealthCheckGracePeriod(self):
        return self._LoadBalancerHealthCheckGracePeriod

    @LoadBalancerHealthCheckGracePeriod.setter
    def LoadBalancerHealthCheckGracePeriod(self, LoadBalancerHealthCheckGracePeriod):
        self._LoadBalancerHealthCheckGracePeriod = LoadBalancerHealthCheckGracePeriod

    @property
    def InstanceAllocationPolicy(self):
        return self._InstanceAllocationPolicy

    @InstanceAllocationPolicy.setter
    def InstanceAllocationPolicy(self, InstanceAllocationPolicy):
        self._InstanceAllocationPolicy = InstanceAllocationPolicy

    @property
    def SpotMixedAllocationPolicy(self):
        return self._SpotMixedAllocationPolicy

    @SpotMixedAllocationPolicy.setter
    def SpotMixedAllocationPolicy(self, SpotMixedAllocationPolicy):
        self._SpotMixedAllocationPolicy = SpotMixedAllocationPolicy

    @property
    def CapacityRebalance(self):
        return self._CapacityRebalance

    @CapacityRebalance.setter
    def CapacityRebalance(self, CapacityRebalance):
        self._CapacityRebalance = CapacityRebalance


    def _deserialize(self, params):
        self._AutoScalingGroupName = params.get("AutoScalingGroupName")
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._MaxSize = params.get("MaxSize")
        self._MinSize = params.get("MinSize")
        self._VpcId = params.get("VpcId")
        self._DefaultCooldown = params.get("DefaultCooldown")
        self._DesiredCapacity = params.get("DesiredCapacity")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._ProjectId = params.get("ProjectId")
        if params.get("ForwardLoadBalancers") is not None:
            self._ForwardLoadBalancers = []
            for item in params.get("ForwardLoadBalancers"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self._ForwardLoadBalancers.append(obj)
        self._SubnetIds = params.get("SubnetIds")
        self._TerminationPolicies = params.get("TerminationPolicies")
        self._Zones = params.get("Zones")
        self._RetryPolicy = params.get("RetryPolicy")
        self._ZonesCheckPolicy = params.get("ZonesCheckPolicy")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("ServiceSettings") is not None:
            self._ServiceSettings = ServiceSettings()
            self._ServiceSettings._deserialize(params.get("ServiceSettings"))
        self._Ipv6AddressCount = params.get("Ipv6AddressCount")
        self._MultiZoneSubnetPolicy = params.get("MultiZoneSubnetPolicy")
        self._HealthCheckType = params.get("HealthCheckType")
        self._LoadBalancerHealthCheckGracePeriod = params.get("LoadBalancerHealthCheckGracePeriod")
        self._InstanceAllocationPolicy = params.get("InstanceAllocationPolicy")
        if params.get("SpotMixedAllocationPolicy") is not None:
            self._SpotMixedAllocationPolicy = SpotMixedAllocationPolicy()
            self._SpotMixedAllocationPolicy._deserialize(params.get("SpotMixedAllocationPolicy"))
        self._CapacityRebalance = params.get("CapacityRebalance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoScalingGroupResponse(AbstractModel):
    """CreateAutoScalingGroup response structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoScalingGroupId = None
        self._RequestId = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._RequestId = params.get("RequestId")


class CreateLaunchConfigurationRequest(AbstractModel):
    """CreateLaunchConfiguration request structure.

    """

    def __init__(self):
        r"""
        :param _LaunchConfigurationName: Display name of the launch configuration, which can contain letters, digits, underscores and hyphens (-), and dots. Up to of 60 bytes allowed..
        :type LaunchConfigurationName: str
        :param _ImageId: [Image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are three types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><br/>You can obtain the image IDs in the [CVM console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE).</li><li>You can also use the [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response.</li>
        :type ImageId: str
        :param _ProjectId: Project ID of the launch configuration. The default project is used if it’s left blank.
Note that this project ID is not the same as the project ID of the scaling group. 
        :type ProjectId: int
        :param _InstanceType: Instance model. Different instance models specify different resource specifications. The specific value can be obtained by calling the [DescribeInstanceTypeConfigs](https://intl.cloud.tencent.com/document/api/213/15749?from_cn_redirect=1) API to get the latest specification table or referring to the descriptions in [Instance Types](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1).
`InstanceType` and `InstanceTypes` are mutually exclusive, and one and only one of them must be entered.
        :type InstanceType: str
        :param _SystemDisk: System disk configuration of the instance. If this parameter is not specified, the default value will be used.
        :type SystemDisk: :class:`tencentcloud.autoscaling.v20180419.models.SystemDisk`
        :param _DataDisks: Information of the instance's data disk configuration. If this parameter is not specified, no data disk is purchased by default. Up to 11 data disks can be supported.
        :type DataDisks: list of DataDisk
        :param _InternetAccessible: Configuration of public network bandwidth. If this parameter is not specified, 0 Mbps will be used by default.
        :type InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        :param _LoginSettings: Login settings of the instance. You can use this parameter to set the login method, password, and key of the instance or keep the login settings of the original image. By default, a random password will be generated and sent to you via the Message Center.
        :type LoginSettings: :class:`tencentcloud.autoscaling.v20180419.models.LoginSettings`
        :param _SecurityGroupIds: The security group to which the instance belongs. This parameter can be obtained by calling the `SecurityGroupId` field in the returned value of [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808?from_cn_redirect=1). If this parameter is not specified, no security group will be bound by default.
        :type SecurityGroupIds: list of str
        :param _EnhancedService: Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Security and Cloud Monitor. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled by default.
        :type EnhancedService: :class:`tencentcloud.autoscaling.v20180419.models.EnhancedService`
        :param _UserData: Base64-encoded custom data of up to 16 KB.
        :type UserData: str
        :param _InstanceChargeType: Instance billing mode. CVM instances take `POSTPAID_BY_HOUR` by default. Valid values:
<br><li>POSTPAID_BY_HOUR: pay-as-you-go hourly
<br><li>SPOTPAID: spot instance
        :type InstanceChargeType: str
        :param _InstanceMarketOptions: Market options of the instance, such as parameters related to spot instances. This parameter is required for spot instances.
        :type InstanceMarketOptions: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        :param _InstanceTypes: List of instance models. Different instance models specify different resource specifications. Up to 10 instance models can be supported.
`InstanceType` and `InstanceTypes` are mutually exclusive, and one and only one of them must be entered.
        :type InstanceTypes: list of str
        :param _CamRoleName: CAM role name. This parameter can be obtained from the `roleName` field returned by DescribeRoleList API.
        :type CamRoleName: str
        :param _InstanceTypesCheckPolicy: Instance type verification policy. Value range: ALL, ANY. Default value: ANY.
<br><li> ALL: The verification will success only if all instance types (InstanceType) are available; otherwise, an error will be reported.
<br><li> ANY: The verification will success if any instance type (InstanceType) is available; otherwise, an error will be reported.

Common reasons why an instance type is unavailable include stock-out of the instance type or the corresponding cloud disk.
If a model in InstanceTypes does not exist or has been discontinued, a verification error will be reported regardless of the value of InstanceTypesCheckPolicy.
        :type InstanceTypesCheckPolicy: str
        :param _InstanceTags: List of tags. This parameter is used to bind up to 10 tags to newly added instances.
        :type InstanceTags: list of InstanceTag
        :param _Tags: List of tags. You can specify tags that you want to bind to the launch configuration. Each launch configuration can have up to 30 tags.
        :type Tags: list of Tag
        :param _HostNameSettings: CVM hostname settings.
        :type HostNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.HostNameSettings`
        :param _InstanceNameSettings: Settings of CVM instance names
If this field is configured in a launch configuration, the `InstanceName` of a CVM created by the scaling group will be generated according to the configuration; otherwise, it will be in the `as-{{AutoScalingGroupName }}` format.
        :type InstanceNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameSettings`
        :param _InstanceChargePrepaid: Details of the monthly subscription, including the purchase period, auto-renewal. It is required if the `InstanceChargeType` is `PREPAID`.
        :type InstanceChargePrepaid: :class:`tencentcloud.autoscaling.v20180419.models.InstanceChargePrepaid`
        :param _DiskTypePolicy: Selection policy of cloud disks. Default value: ORIGINAL. Valid values:
<br><li>ORIGINAL: uses the configured cloud disk type
<br><li>AUTOMATIC: automatically chooses an available cloud disk type
        :type DiskTypePolicy: str
        :param _HpcClusterId: HPC ID<br>
Note: This field is default to empty
        :type HpcClusterId: str
        :param _IPv6InternetAccessible: IPv6 public network bandwidth configuration. If the IPv6 address is available in the new instance, public network bandwidth can be allocated to the IPv6 address. This parameter is invalid if `Ipv6AddressCount` of the scaling group associated with the launch configuration is 0.
        :type IPv6InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.IPv6InternetAccessible`
        :param _DisasterRecoverGroupIds: Placement group ID. Only one is allowed.
        :type DisasterRecoverGroupIds: list of str
        """
        self._LaunchConfigurationName = None
        self._ImageId = None
        self._ProjectId = None
        self._InstanceType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._InternetAccessible = None
        self._LoginSettings = None
        self._SecurityGroupIds = None
        self._EnhancedService = None
        self._UserData = None
        self._InstanceChargeType = None
        self._InstanceMarketOptions = None
        self._InstanceTypes = None
        self._CamRoleName = None
        self._InstanceTypesCheckPolicy = None
        self._InstanceTags = None
        self._Tags = None
        self._HostNameSettings = None
        self._InstanceNameSettings = None
        self._InstanceChargePrepaid = None
        self._DiskTypePolicy = None
        self._HpcClusterId = None
        self._IPv6InternetAccessible = None
        self._DisasterRecoverGroupIds = None

    @property
    def LaunchConfigurationName(self):
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def InstanceTypesCheckPolicy(self):
        return self._InstanceTypesCheckPolicy

    @InstanceTypesCheckPolicy.setter
    def InstanceTypesCheckPolicy(self, InstanceTypesCheckPolicy):
        self._InstanceTypesCheckPolicy = InstanceTypesCheckPolicy

    @property
    def InstanceTags(self):
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HostNameSettings(self):
        return self._HostNameSettings

    @HostNameSettings.setter
    def HostNameSettings(self, HostNameSettings):
        self._HostNameSettings = HostNameSettings

    @property
    def InstanceNameSettings(self):
        return self._InstanceNameSettings

    @InstanceNameSettings.setter
    def InstanceNameSettings(self, InstanceNameSettings):
        self._InstanceNameSettings = InstanceNameSettings

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def DiskTypePolicy(self):
        return self._DiskTypePolicy

    @DiskTypePolicy.setter
    def DiskTypePolicy(self, DiskTypePolicy):
        self._DiskTypePolicy = DiskTypePolicy

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def IPv6InternetAccessible(self):
        return self._IPv6InternetAccessible

    @IPv6InternetAccessible.setter
    def IPv6InternetAccessible(self, IPv6InternetAccessible):
        self._IPv6InternetAccessible = IPv6InternetAccessible

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds


    def _deserialize(self, params):
        self._LaunchConfigurationName = params.get("LaunchConfigurationName")
        self._ImageId = params.get("ImageId")
        self._ProjectId = params.get("ProjectId")
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._UserData = params.get("UserData")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._InstanceTypes = params.get("InstanceTypes")
        self._CamRoleName = params.get("CamRoleName")
        self._InstanceTypesCheckPolicy = params.get("InstanceTypesCheckPolicy")
        if params.get("InstanceTags") is not None:
            self._InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTag()
                obj._deserialize(item)
                self._InstanceTags.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("HostNameSettings") is not None:
            self._HostNameSettings = HostNameSettings()
            self._HostNameSettings._deserialize(params.get("HostNameSettings"))
        if params.get("InstanceNameSettings") is not None:
            self._InstanceNameSettings = InstanceNameSettings()
            self._InstanceNameSettings._deserialize(params.get("InstanceNameSettings"))
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._DiskTypePolicy = params.get("DiskTypePolicy")
        self._HpcClusterId = params.get("HpcClusterId")
        if params.get("IPv6InternetAccessible") is not None:
            self._IPv6InternetAccessible = IPv6InternetAccessible()
            self._IPv6InternetAccessible._deserialize(params.get("IPv6InternetAccessible"))
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLaunchConfigurationResponse(AbstractModel):
    """CreateLaunchConfiguration response structure.

    """

    def __init__(self):
        r"""
        :param _LaunchConfigurationId: This parameter is returned when a launch configuration is created through this API, indicating the launch configuration ID.
        :type LaunchConfigurationId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LaunchConfigurationId = None
        self._RequestId = None

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._RequestId = params.get("RequestId")


class CreateLifecycleHookRequest(AbstractModel):
    """CreateLifecycleHook request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param _LifecycleHookName: Lifecycle hook name, which can contain Chinese characters, letters, numbers, underscores (_), hyphens (-), and periods (.) with a maximum length of 128 bytes.
        :type LifecycleHookName: str
        :param _LifecycleTransition: Scenario for the lifecycle hook. Valid values: "INSTANCE_LAUNCHING" and "INSTANCE_TERMINATING"
        :type LifecycleTransition: str
        :param _DefaultResult: Defined actions when lifecycle hook times out. Valid values: "CONTINUE" and "ABANDON". Default value: "CONTINUE"
        :type DefaultResult: str
        :param _HeartbeatTimeout: The maximum length of time (in seconds) that can elapse before the lifecycle hook times out. Value range: 30-7200. Default value: 300
        :type HeartbeatTimeout: int
        :param _NotificationMetadata: Additional information of a notification that Auto Scaling sends to targets. This parameter is set when you configure a notification (default value: ""). Up to 1024 characters are allowed.
        :type NotificationMetadata: str
        :param _NotificationTarget: Notification target. `NotificationTarget` and `LifecycleCommand` cannot be specified at the same time.
        :type NotificationTarget: :class:`tencentcloud.autoscaling.v20180419.models.NotificationTarget`
        :param _LifecycleTransitionType: The scenario where the lifecycle hook is applied. `EXTENSION`: the lifecycle hook will be triggered when AttachInstances, DetachInstances or RemoveInstaces is called. `NORMAL`: the lifecycle hook is not triggered by the above APIs. 
        :type LifecycleTransitionType: str
        :param _LifecycleCommand: Remote command execution object. `NotificationTarget` and `LifecycleCommand` cannot be specified at the same time.
        :type LifecycleCommand: :class:`tencentcloud.autoscaling.v20180419.models.LifecycleCommand`
        """
        self._AutoScalingGroupId = None
        self._LifecycleHookName = None
        self._LifecycleTransition = None
        self._DefaultResult = None
        self._HeartbeatTimeout = None
        self._NotificationMetadata = None
        self._NotificationTarget = None
        self._LifecycleTransitionType = None
        self._LifecycleCommand = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def LifecycleHookName(self):
        return self._LifecycleHookName

    @LifecycleHookName.setter
    def LifecycleHookName(self, LifecycleHookName):
        self._LifecycleHookName = LifecycleHookName

    @property
    def LifecycleTransition(self):
        return self._LifecycleTransition

    @LifecycleTransition.setter
    def LifecycleTransition(self, LifecycleTransition):
        self._LifecycleTransition = LifecycleTransition

    @property
    def DefaultResult(self):
        return self._DefaultResult

    @DefaultResult.setter
    def DefaultResult(self, DefaultResult):
        self._DefaultResult = DefaultResult

    @property
    def HeartbeatTimeout(self):
        return self._HeartbeatTimeout

    @HeartbeatTimeout.setter
    def HeartbeatTimeout(self, HeartbeatTimeout):
        self._HeartbeatTimeout = HeartbeatTimeout

    @property
    def NotificationMetadata(self):
        return self._NotificationMetadata

    @NotificationMetadata.setter
    def NotificationMetadata(self, NotificationMetadata):
        self._NotificationMetadata = NotificationMetadata

    @property
    def NotificationTarget(self):
        return self._NotificationTarget

    @NotificationTarget.setter
    def NotificationTarget(self, NotificationTarget):
        self._NotificationTarget = NotificationTarget

    @property
    def LifecycleTransitionType(self):
        return self._LifecycleTransitionType

    @LifecycleTransitionType.setter
    def LifecycleTransitionType(self, LifecycleTransitionType):
        self._LifecycleTransitionType = LifecycleTransitionType

    @property
    def LifecycleCommand(self):
        return self._LifecycleCommand

    @LifecycleCommand.setter
    def LifecycleCommand(self, LifecycleCommand):
        self._LifecycleCommand = LifecycleCommand


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._LifecycleHookName = params.get("LifecycleHookName")
        self._LifecycleTransition = params.get("LifecycleTransition")
        self._DefaultResult = params.get("DefaultResult")
        self._HeartbeatTimeout = params.get("HeartbeatTimeout")
        self._NotificationMetadata = params.get("NotificationMetadata")
        if params.get("NotificationTarget") is not None:
            self._NotificationTarget = NotificationTarget()
            self._NotificationTarget._deserialize(params.get("NotificationTarget"))
        self._LifecycleTransitionType = params.get("LifecycleTransitionType")
        if params.get("LifecycleCommand") is not None:
            self._LifecycleCommand = LifecycleCommand()
            self._LifecycleCommand._deserialize(params.get("LifecycleCommand"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLifecycleHookResponse(AbstractModel):
    """CreateLifecycleHook response structure.

    """

    def __init__(self):
        r"""
        :param _LifecycleHookId: Lifecycle hook ID
        :type LifecycleHookId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LifecycleHookId = None
        self._RequestId = None

    @property
    def LifecycleHookId(self):
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LifecycleHookId = params.get("LifecycleHookId")
        self._RequestId = params.get("RequestId")


class CreateNotificationConfigurationRequest(AbstractModel):
    """CreateNotificationConfiguration request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID.
        :type AutoScalingGroupId: str
        :param _NotificationTypes: Notification type, i.e., the set of types of notifications to be subscribed to. Value range:
<li>SCALE_OUT_SUCCESSFUL: scale-out succeeded</li>
<li>SCALE_OUT_FAILED: scale-out failed</li>
<li>SCALE_IN_SUCCESSFUL: scale-in succeeded</li>
<li>SCALE_IN_FAILED: scale-in failed</li>
<li>REPLACE_UNHEALTHY_INSTANCE_SUCCESSFUL: unhealthy instance replacement succeeded</li>
<li>REPLACE_UNHEALTHY_INSTANCE_FAILED: unhealthy instance replacement failed</li>
        :type NotificationTypes: list of str
        :param _NotificationUserGroupIds: Notification group ID, which is the set of user group IDs. You can query the user group IDs through the [ListGroups](https://intl.cloud.tencent.com/document/product/598/34589?from_cn_redirect=1) API.
        :type NotificationUserGroupIds: list of str
        :param _TargetType: Notification receiver type. Valid values:
<br><li>USER_GROUP:User group
<br><li>CMQ_QUEUE:CMQ queue
<br><li>CMQ_TOPIC:CMQ topic
<br><li>TDMQ_CMQ_TOPIC:TDMQ CMQ topic
<br><li>TDMQ_CMQ_QUEUE:TDMQ CMQ queue

Default value: `USER_GROUP`.
        :type TargetType: str
        :param _QueueName: CMQ queue name. This parameter is required when `TargetType` is `CMQ_QUEUE` or `TDMQ_CMQ_QUEUE`.
        :type QueueName: str
        :param _TopicName: CMQ topic name. This parameter is required when `TargetType` is `CMQ_TOPIC` or `TDMQ_CMQ_TOPIC`.
        :type TopicName: str
        """
        self._AutoScalingGroupId = None
        self._NotificationTypes = None
        self._NotificationUserGroupIds = None
        self._TargetType = None
        self._QueueName = None
        self._TopicName = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def NotificationTypes(self):
        return self._NotificationTypes

    @NotificationTypes.setter
    def NotificationTypes(self, NotificationTypes):
        self._NotificationTypes = NotificationTypes

    @property
    def NotificationUserGroupIds(self):
        return self._NotificationUserGroupIds

    @NotificationUserGroupIds.setter
    def NotificationUserGroupIds(self, NotificationUserGroupIds):
        self._NotificationUserGroupIds = NotificationUserGroupIds

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._NotificationTypes = params.get("NotificationTypes")
        self._NotificationUserGroupIds = params.get("NotificationUserGroupIds")
        self._TargetType = params.get("TargetType")
        self._QueueName = params.get("QueueName")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNotificationConfigurationResponse(AbstractModel):
    """CreateNotificationConfiguration response structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingNotificationId: Notification ID.
        :type AutoScalingNotificationId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoScalingNotificationId = None
        self._RequestId = None

    @property
    def AutoScalingNotificationId(self):
        return self._AutoScalingNotificationId

    @AutoScalingNotificationId.setter
    def AutoScalingNotificationId(self, AutoScalingNotificationId):
        self._AutoScalingNotificationId = AutoScalingNotificationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoScalingNotificationId = params.get("AutoScalingNotificationId")
        self._RequestId = params.get("RequestId")


class CreateScalingPolicyRequest(AbstractModel):
    """CreateScalingPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID.
        :type AutoScalingGroupId: str
        :param _ScalingPolicyName: Alarm trigger policy name.
        :type ScalingPolicyName: str
        :param _ScalingPolicyType: Scaling policy type. Valid values: <br><li>`SIMPLE` (default): A simple policy</li><li>`TARGET_TRACKING`: A target tracking policy</li>.
        :type ScalingPolicyType: str
        :param _AdjustmentType: The method to adjust the desired capacity after the alarm is triggered. It’s only available when `ScalingPolicyType` is `Simple`. Valid values: <br><li>`CHANGE_IN_CAPACITY`: Increase or decrease the desired capacity </li><li>`EXACT_CAPACITY`: Adjust to the specified desired capacity </li> <li>`PERCENT_CHANGE_IN_CAPACITY`: Adjust the desired capacity by percentage </li>
        :type AdjustmentType: str
        :param _AdjustmentValue: Specifies how to adjust the number of desired capacity when the alarm is triggered. It’s only available when `ScalingPolicyType` is `Simple`. Values: <br><li>`AdjustmentType`=`CHANGE_IN_CAPACITY`: Number of instances to add (positive number) or remove (negative number). </li> <li>`AdjustmentType`=`EXACT_CAPACITY`: Set the desired capacity to the specified number. It must be ≥ 0. </li> <li>`AdjustmentType`=`PERCENT_CHANGE_IN_CAPACITY`: Percentage of instance number. Add instances (positive value) or remove instances (negative value) accordingly.
        :type AdjustmentValue: int
        :param _Cooldown: Cooldown period (in seconds). This parameter is only applicable to a simple policy. Default value: 300.
        :type Cooldown: int
        :param _MetricAlarm: Alarm monitoring metric. It’s only available when `ScalingPolicyType` is `Simple`.
        :type MetricAlarm: :class:`tencentcloud.autoscaling.v20180419.models.MetricAlarm`
        :param _PredefinedMetricType: Preset monitoring item. It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Valid values: <br><li>ASG_AVG_CPU_UTILIZATION: Average CPU utilization</li><li>ASG_AVG_LAN_TRAFFIC_OUT: Average private bandwidth out</li><li>ASG_AVG_LAN_TRAFFIC_IN: Average private bandwidth in</li><li>ASG_AVG_WAN_TRAFFIC_OUT: Average public bandwidth out</li><li>ASG_AVG_WAN_TRAFFIC_IN: Average public bandwidth in</li>
        :type PredefinedMetricType: str
        :param _TargetValue: Target value. It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Value ranges: <br><li>`ASG_AVG_CPU_UTILIZATION` (in %): [1, 100)</li><li>`ASG_AVG_LAN_TRAFFIC_OUT` (in Mbps): >0</li><li>`ASG_AVG_LAN_TRAFFIC_IN` (in Mbps): >0</li><li>`ASG_AVG_WAN_TRAFFIC_OUT` (in Mbps): >0</li><li>`ASG_AVG_WAN_TRAFFIC_IN` (in Mbps): >0</li>
        :type TargetValue: int
        :param _EstimatedInstanceWarmup: Instance warm-up period (in seconds). It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Value range: 0-3600. Default value: 300.
        :type EstimatedInstanceWarmup: int
        :param _DisableScaleIn: Whether to disable scale-in. It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Valid values: <br><li>`true`: Do not scale in </li><li>`false` (default): Both scale-out and scale-in can be triggered.</li>
        :type DisableScaleIn: bool
        :param _NotificationUserGroupIds: This parameter is diused. Please use [CreateNotificationConfiguration](https://intl.cloud.tencent.com/document/api/377/33185?from_cn_redirect=1) instead.
Notification group ID, which is the set of user group IDs.
        :type NotificationUserGroupIds: list of str
        """
        self._AutoScalingGroupId = None
        self._ScalingPolicyName = None
        self._ScalingPolicyType = None
        self._AdjustmentType = None
        self._AdjustmentValue = None
        self._Cooldown = None
        self._MetricAlarm = None
        self._PredefinedMetricType = None
        self._TargetValue = None
        self._EstimatedInstanceWarmup = None
        self._DisableScaleIn = None
        self._NotificationUserGroupIds = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ScalingPolicyName(self):
        return self._ScalingPolicyName

    @ScalingPolicyName.setter
    def ScalingPolicyName(self, ScalingPolicyName):
        self._ScalingPolicyName = ScalingPolicyName

    @property
    def ScalingPolicyType(self):
        return self._ScalingPolicyType

    @ScalingPolicyType.setter
    def ScalingPolicyType(self, ScalingPolicyType):
        self._ScalingPolicyType = ScalingPolicyType

    @property
    def AdjustmentType(self):
        return self._AdjustmentType

    @AdjustmentType.setter
    def AdjustmentType(self, AdjustmentType):
        self._AdjustmentType = AdjustmentType

    @property
    def AdjustmentValue(self):
        return self._AdjustmentValue

    @AdjustmentValue.setter
    def AdjustmentValue(self, AdjustmentValue):
        self._AdjustmentValue = AdjustmentValue

    @property
    def Cooldown(self):
        return self._Cooldown

    @Cooldown.setter
    def Cooldown(self, Cooldown):
        self._Cooldown = Cooldown

    @property
    def MetricAlarm(self):
        return self._MetricAlarm

    @MetricAlarm.setter
    def MetricAlarm(self, MetricAlarm):
        self._MetricAlarm = MetricAlarm

    @property
    def PredefinedMetricType(self):
        return self._PredefinedMetricType

    @PredefinedMetricType.setter
    def PredefinedMetricType(self, PredefinedMetricType):
        self._PredefinedMetricType = PredefinedMetricType

    @property
    def TargetValue(self):
        return self._TargetValue

    @TargetValue.setter
    def TargetValue(self, TargetValue):
        self._TargetValue = TargetValue

    @property
    def EstimatedInstanceWarmup(self):
        return self._EstimatedInstanceWarmup

    @EstimatedInstanceWarmup.setter
    def EstimatedInstanceWarmup(self, EstimatedInstanceWarmup):
        self._EstimatedInstanceWarmup = EstimatedInstanceWarmup

    @property
    def DisableScaleIn(self):
        return self._DisableScaleIn

    @DisableScaleIn.setter
    def DisableScaleIn(self, DisableScaleIn):
        self._DisableScaleIn = DisableScaleIn

    @property
    def NotificationUserGroupIds(self):
        return self._NotificationUserGroupIds

    @NotificationUserGroupIds.setter
    def NotificationUserGroupIds(self, NotificationUserGroupIds):
        self._NotificationUserGroupIds = NotificationUserGroupIds


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._ScalingPolicyName = params.get("ScalingPolicyName")
        self._ScalingPolicyType = params.get("ScalingPolicyType")
        self._AdjustmentType = params.get("AdjustmentType")
        self._AdjustmentValue = params.get("AdjustmentValue")
        self._Cooldown = params.get("Cooldown")
        if params.get("MetricAlarm") is not None:
            self._MetricAlarm = MetricAlarm()
            self._MetricAlarm._deserialize(params.get("MetricAlarm"))
        self._PredefinedMetricType = params.get("PredefinedMetricType")
        self._TargetValue = params.get("TargetValue")
        self._EstimatedInstanceWarmup = params.get("EstimatedInstanceWarmup")
        self._DisableScaleIn = params.get("DisableScaleIn")
        self._NotificationUserGroupIds = params.get("NotificationUserGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScalingPolicyResponse(AbstractModel):
    """CreateScalingPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingPolicyId: Alarm trigger policy ID.
        :type AutoScalingPolicyId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoScalingPolicyId = None
        self._RequestId = None

    @property
    def AutoScalingPolicyId(self):
        return self._AutoScalingPolicyId

    @AutoScalingPolicyId.setter
    def AutoScalingPolicyId(self, AutoScalingPolicyId):
        self._AutoScalingPolicyId = AutoScalingPolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        self._RequestId = params.get("RequestId")


class CreateScheduledActionRequest(AbstractModel):
    """CreateScheduledAction request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param _ScheduledActionName: Scheduled task name, which can only contain letters, numbers, underscores, hyphens ("-"), and decimal points with a maximum length of 60 bytes and must be unique in an auto scaling group.
        :type ScheduledActionName: str
        :param _MaxSize: The maximum number of instances set for the auto scaling group when the scheduled task is triggered.
        :type MaxSize: int
        :param _MinSize: The minimum number of instances set for the auto scaling group when the scheduled task is triggered.
        :type MinSize: int
        :param _DesiredCapacity: The desired number of instances set for the auto scaling group when the scheduled task is triggered.
        :type DesiredCapacity: int
        :param _StartTime: Initial triggered time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard.
        :type StartTime: str
        :param _EndTime: End time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard. <br><br>This parameter and `Recurrence` need to be specified at the same time. After the end time, the scheduled task will no longer take effect.
        :type EndTime: str
        :param _Recurrence: Repeating mode of the scheduled task, which is in standard cron format. <br><br>This parameter and `EndTime` need to be specified at the same time.
        :type Recurrence: str
        """
        self._AutoScalingGroupId = None
        self._ScheduledActionName = None
        self._MaxSize = None
        self._MinSize = None
        self._DesiredCapacity = None
        self._StartTime = None
        self._EndTime = None
        self._Recurrence = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ScheduledActionName(self):
        return self._ScheduledActionName

    @ScheduledActionName.setter
    def ScheduledActionName(self, ScheduledActionName):
        self._ScheduledActionName = ScheduledActionName

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def DesiredCapacity(self):
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Recurrence(self):
        return self._Recurrence

    @Recurrence.setter
    def Recurrence(self, Recurrence):
        self._Recurrence = Recurrence


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._ScheduledActionName = params.get("ScheduledActionName")
        self._MaxSize = params.get("MaxSize")
        self._MinSize = params.get("MinSize")
        self._DesiredCapacity = params.get("DesiredCapacity")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Recurrence = params.get("Recurrence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScheduledActionResponse(AbstractModel):
    """CreateScheduledAction response structure.

    """

    def __init__(self):
        r"""
        :param _ScheduledActionId: Scheduled task ID
        :type ScheduledActionId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ScheduledActionId = None
        self._RequestId = None

    @property
    def ScheduledActionId(self):
        return self._ScheduledActionId

    @ScheduledActionId.setter
    def ScheduledActionId(self, ScheduledActionId):
        self._ScheduledActionId = ScheduledActionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ScheduledActionId = params.get("ScheduledActionId")
        self._RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """Configuration information of data disk in launch configuration. If this parameter is not specified, no data disk will be purchased by default. You can specify only one data disk when purchasing it.

    """

    def __init__(self):
        r"""
        :param _DiskType: Data disk type. See [Cloud Disk Types](https://intl.cloud.tencent.com/document/product/362/31636). Valid values:<br><li>`LOCAL_BASIC`: Local disk<br><li>`LOCAL_SSD`: Local SSD disk<br><li>`CLOUD_BASIC`: HDD cloud disk<br><li>`CLOUD_PREMIUM`: Premium cloud storage<br><li>`CLOUD_SSD`: SSD cloud disk<br><li>`CLOUD_HSSD`: Enhanced SSD<br><li>`CLOUD_TSSD`: Tremendous SSD<br><br>The default value should be the same as the `DiskType` field under `SystemDisk`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DiskType: str
        :param _DiskSize: Data disk size (in GB). The minimum adjustment increment is 10 GB. The value range varies by data disk type. For more information on limits, see [CVM Instance Configuration](https://intl.cloud.tencent.com/document/product/213/2177?from_cn_redirect=1). The default value is 0, indicating that no data disk is purchased. For more information, see the product documentation.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskSize: int
        :param _SnapshotId: Data disk snapshot ID, such as `snap-l8psqwnt`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SnapshotId: str
        :param _DeleteWithInstance: Specifies whether the data disk is terminated along with the termination of the associated CVM instance.  Values: <br><li>`TRUE` (only available for pay-as-you-go cloud disks that are billed by hour) and `FALSE`.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type DeleteWithInstance: bool
        :param _Encrypt: Data disk encryption. Valid values: <br><li>`TRUE`: Encrypted<br><li>`FALSE`: Not encrypted
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Encrypt: bool
        :param _ThroughputPerformance: Cloud disk performance (MB/s). This parameter is used to purchase extra performance for the cloud disk. For details on the feature and limits, see [Enhanced SSD Performance](https://intl.cloud.tencent.com/document/product/362/51896?from_cn_redirect=1#. E5.A2.9E.E5.BC.BA.E5.9E.8B-ssd-.E4.BA.91.E7.A1.AC.E7.9B.98.E9.A2.9D.E5.A4.96 .E6.80.A7.E8.83.BD).
This feature is only available to enhanced SSD (`CLOUD_HSSD`) and tremendous SSD (`CLOUD_TSSD`) disks with a capacity greater than 460 GB.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ThroughputPerformance: int
        """
        self._DiskType = None
        self._DiskSize = None
        self._SnapshotId = None
        self._DeleteWithInstance = None
        self._Encrypt = None
        self._ThroughputPerformance = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DeleteWithInstance(self):
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def Encrypt(self):
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def ThroughputPerformance(self):
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._SnapshotId = params.get("SnapshotId")
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._Encrypt = params.get("Encrypt")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoScalingGroupRequest(AbstractModel):
    """DeleteAutoScalingGroup request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        """
        self._AutoScalingGroupId = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoScalingGroupResponse(AbstractModel):
    """DeleteAutoScalingGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteLaunchConfigurationRequest(AbstractModel):
    """DeleteLaunchConfiguration request structure.

    """

    def __init__(self):
        r"""
        :param _LaunchConfigurationId: ID of the launch configuration to be deleted.
        :type LaunchConfigurationId: str
        """
        self._LaunchConfigurationId = None

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId


    def _deserialize(self, params):
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLaunchConfigurationResponse(AbstractModel):
    """DeleteLaunchConfiguration response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteLifecycleHookRequest(AbstractModel):
    """DeleteLifecycleHook request structure.

    """

    def __init__(self):
        r"""
        :param _LifecycleHookId: Lifecycle hook ID
        :type LifecycleHookId: str
        """
        self._LifecycleHookId = None

    @property
    def LifecycleHookId(self):
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId


    def _deserialize(self, params):
        self._LifecycleHookId = params.get("LifecycleHookId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLifecycleHookResponse(AbstractModel):
    """DeleteLifecycleHook response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteNotificationConfigurationRequest(AbstractModel):
    """DeleteNotificationConfiguration request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingNotificationId: ID of the notification to be deleted.
        :type AutoScalingNotificationId: str
        """
        self._AutoScalingNotificationId = None

    @property
    def AutoScalingNotificationId(self):
        return self._AutoScalingNotificationId

    @AutoScalingNotificationId.setter
    def AutoScalingNotificationId(self, AutoScalingNotificationId):
        self._AutoScalingNotificationId = AutoScalingNotificationId


    def _deserialize(self, params):
        self._AutoScalingNotificationId = params.get("AutoScalingNotificationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNotificationConfigurationResponse(AbstractModel):
    """DeleteNotificationConfiguration response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteScalingPolicyRequest(AbstractModel):
    """DeleteScalingPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingPolicyId: ID of the alarm policy to be deleted.
        :type AutoScalingPolicyId: str
        """
        self._AutoScalingPolicyId = None

    @property
    def AutoScalingPolicyId(self):
        return self._AutoScalingPolicyId

    @AutoScalingPolicyId.setter
    def AutoScalingPolicyId(self, AutoScalingPolicyId):
        self._AutoScalingPolicyId = AutoScalingPolicyId


    def _deserialize(self, params):
        self._AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteScalingPolicyResponse(AbstractModel):
    """DeleteScalingPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteScheduledActionRequest(AbstractModel):
    """DeleteScheduledAction request structure.

    """

    def __init__(self):
        r"""
        :param _ScheduledActionId: ID of the scheduled task to be deleted.
        :type ScheduledActionId: str
        """
        self._ScheduledActionId = None

    @property
    def ScheduledActionId(self):
        return self._ScheduledActionId

    @ScheduledActionId.setter
    def ScheduledActionId(self, ScheduledActionId):
        self._ScheduledActionId = ScheduledActionId


    def _deserialize(self, params):
        self._ScheduledActionId = params.get("ScheduledActionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteScheduledActionResponse(AbstractModel):
    """DeleteScheduledAction response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAccountLimitsRequest(AbstractModel):
    """DescribeAccountLimits request structure.

    """


class DescribeAccountLimitsResponse(AbstractModel):
    """DescribeAccountLimits response structure.

    """

    def __init__(self):
        r"""
        :param _MaxNumberOfLaunchConfigurations: Maximum number of launch configurations allowed for creation by the user account
        :type MaxNumberOfLaunchConfigurations: int
        :param _NumberOfLaunchConfigurations: Current number of launch configurations under the user account
        :type NumberOfLaunchConfigurations: int
        :param _MaxNumberOfAutoScalingGroups: Maximum number of auto scaling groups allowed for creation by the user account
        :type MaxNumberOfAutoScalingGroups: int
        :param _NumberOfAutoScalingGroups: Current number of auto scaling groups under the user account
        :type NumberOfAutoScalingGroups: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MaxNumberOfLaunchConfigurations = None
        self._NumberOfLaunchConfigurations = None
        self._MaxNumberOfAutoScalingGroups = None
        self._NumberOfAutoScalingGroups = None
        self._RequestId = None

    @property
    def MaxNumberOfLaunchConfigurations(self):
        return self._MaxNumberOfLaunchConfigurations

    @MaxNumberOfLaunchConfigurations.setter
    def MaxNumberOfLaunchConfigurations(self, MaxNumberOfLaunchConfigurations):
        self._MaxNumberOfLaunchConfigurations = MaxNumberOfLaunchConfigurations

    @property
    def NumberOfLaunchConfigurations(self):
        return self._NumberOfLaunchConfigurations

    @NumberOfLaunchConfigurations.setter
    def NumberOfLaunchConfigurations(self, NumberOfLaunchConfigurations):
        self._NumberOfLaunchConfigurations = NumberOfLaunchConfigurations

    @property
    def MaxNumberOfAutoScalingGroups(self):
        return self._MaxNumberOfAutoScalingGroups

    @MaxNumberOfAutoScalingGroups.setter
    def MaxNumberOfAutoScalingGroups(self, MaxNumberOfAutoScalingGroups):
        self._MaxNumberOfAutoScalingGroups = MaxNumberOfAutoScalingGroups

    @property
    def NumberOfAutoScalingGroups(self):
        return self._NumberOfAutoScalingGroups

    @NumberOfAutoScalingGroups.setter
    def NumberOfAutoScalingGroups(self, NumberOfAutoScalingGroups):
        self._NumberOfAutoScalingGroups = NumberOfAutoScalingGroups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MaxNumberOfLaunchConfigurations = params.get("MaxNumberOfLaunchConfigurations")
        self._NumberOfLaunchConfigurations = params.get("NumberOfLaunchConfigurations")
        self._MaxNumberOfAutoScalingGroups = params.get("MaxNumberOfAutoScalingGroups")
        self._NumberOfAutoScalingGroups = params.get("NumberOfAutoScalingGroups")
        self._RequestId = params.get("RequestId")


class DescribeAutoScalingActivitiesRequest(AbstractModel):
    """DescribeAutoScalingActivities request structure.

    """

    def __init__(self):
        r"""
        :param _ActivityIds: Queries by one or more scaling activity IDs in the format of `asa-5l2ejpfo`. The maximum quantity per request is 100. This parameter does not support specifying both `ActivityIds` and `Filters` at the same time.
        :type ActivityIds: list of str
        :param _Filters: Filter.
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
<li> activity-status-code - String - Required: No - (Filter) Filter by scaling activity status . (INIT: initializing | RUNNING: running | SUCCESSFUL: succeeded | PARTIALLY_SUCCESSFUL: partially succeeded | FAILED: failed | CANCELLED: canceled)</li>
<li> activity-type - String - Required: No - (Filter) Filter by scaling activity type. (SCALE_OUT: scale-out | SCALE_IN: scale-in | ATTACH_INSTANCES: adding an instance | REMOVE_INSTANCES: terminating an instance | DETACH_INSTANCES: removing an instance | TERMINATE_INSTANCES_UNEXPECTEDLY: terminating an instance in the CVM console | REPLACE_UNHEALTHY_INSTANCE: replacing an unhealthy instance | UPDATE_LOAD_BALANCERS: updating a load balancer)</li>
<li> activity-id - String - Required: No - (Filter) Filter by scaling activity ID.</li>
The maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `ActivityIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param _StartTime: The earliest start time of the scaling activity, which will be ignored if ActivityIds is specified. The value is in `UTC time` in the format of `YYYY-MM-DDThh:mm:ssZ` according to the `ISO8601` standard.
        :type StartTime: str
        :param _EndTime: The latest end time of the scaling activity, which will be ignored if ActivityIds is specified. The value is in `UTC time` in the format of `YYYY-MM-DDThh:mm:ssZ` according to the `ISO8601` standard.
        :type EndTime: str
        """
        self._ActivityIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ActivityIds(self):
        return self._ActivityIds

    @ActivityIds.setter
    def ActivityIds(self, ActivityIds):
        self._ActivityIds = ActivityIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ActivityIds = params.get("ActivityIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoScalingActivitiesResponse(AbstractModel):
    """DescribeAutoScalingActivities response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible scaling activities.
        :type TotalCount: int
        :param _ActivitySet: Information set of eligible scaling activities.
        :type ActivitySet: list of Activity
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ActivitySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ActivitySet(self):
        return self._ActivitySet

    @ActivitySet.setter
    def ActivitySet(self, ActivitySet):
        self._ActivitySet = ActivitySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ActivitySet") is not None:
            self._ActivitySet = []
            for item in params.get("ActivitySet"):
                obj = Activity()
                obj._deserialize(item)
                self._ActivitySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAutoScalingAdvicesRequest(AbstractModel):
    """DescribeAutoScalingAdvices request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupIds: List of scaling groups to be queried. Upper limit: 100.
        :type AutoScalingGroupIds: list of str
        """
        self._AutoScalingGroupIds = None

    @property
    def AutoScalingGroupIds(self):
        return self._AutoScalingGroupIds

    @AutoScalingGroupIds.setter
    def AutoScalingGroupIds(self, AutoScalingGroupIds):
        self._AutoScalingGroupIds = AutoScalingGroupIds


    def _deserialize(self, params):
        self._AutoScalingGroupIds = params.get("AutoScalingGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoScalingAdvicesResponse(AbstractModel):
    """DescribeAutoScalingAdvices response structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingAdviceSet: A collection of suggestions for scaling group configurations.
        :type AutoScalingAdviceSet: list of AutoScalingAdvice
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoScalingAdviceSet = None
        self._RequestId = None

    @property
    def AutoScalingAdviceSet(self):
        return self._AutoScalingAdviceSet

    @AutoScalingAdviceSet.setter
    def AutoScalingAdviceSet(self, AutoScalingAdviceSet):
        self._AutoScalingAdviceSet = AutoScalingAdviceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AutoScalingAdviceSet") is not None:
            self._AutoScalingAdviceSet = []
            for item in params.get("AutoScalingAdviceSet"):
                obj = AutoScalingAdvice()
                obj._deserialize(item)
                self._AutoScalingAdviceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAutoScalingGroupLastActivitiesRequest(AbstractModel):
    """DescribeAutoScalingGroupLastActivities request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupIds: ID list of an auto scaling group.
        :type AutoScalingGroupIds: list of str
        """
        self._AutoScalingGroupIds = None

    @property
    def AutoScalingGroupIds(self):
        return self._AutoScalingGroupIds

    @AutoScalingGroupIds.setter
    def AutoScalingGroupIds(self, AutoScalingGroupIds):
        self._AutoScalingGroupIds = AutoScalingGroupIds


    def _deserialize(self, params):
        self._AutoScalingGroupIds = params.get("AutoScalingGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoScalingGroupLastActivitiesResponse(AbstractModel):
    """DescribeAutoScalingGroupLastActivities response structure.

    """

    def __init__(self):
        r"""
        :param _ActivitySet: Information set of eligible scaling activities. Scaling groups without scaling activities are not returned. For example, if there are 50 auto scaling group IDs but only 45 records are returned, it indicates that 5 of the auto scaling groups do not have scaling activities.
        :type ActivitySet: list of Activity
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivitySet = None
        self._RequestId = None

    @property
    def ActivitySet(self):
        return self._ActivitySet

    @ActivitySet.setter
    def ActivitySet(self, ActivitySet):
        self._ActivitySet = ActivitySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ActivitySet") is not None:
            self._ActivitySet = []
            for item in params.get("ActivitySet"):
                obj = Activity()
                obj._deserialize(item)
                self._ActivitySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAutoScalingGroupsRequest(AbstractModel):
    """DescribeAutoScalingGroups request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupIds: Queries by one or more auto scaling group IDs in the format of `asg-nkdwoui0`. The maximum quantity per request is 100. This parameter does not support specifying both `AutoScalingGroupIds` and `Filters` at the same time.
        :type AutoScalingGroupIds: list of str
        :param _Filters: Filters.
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
<li> auto-scaling-group-name - String - Required: No - (Filter) Filter by auto scaling group name.</li>
<li> vague-auto-scaling-group-name - String - Required: No - (Filter) Fuzzy search by auto scaling group name.</li>
<li> launch-configuration-id - String - Required: No - (Filter) Filter by launch configuration ID.</li>
<li> tag-key - String - Required: No - (Filter) Filter by tag key.</li>
<li> tag-value - String - Required: No - (Filter) Filter by tag value.</li>
<li> tag:tag-key - String - Required: No - (Filter) Filter by tag key-value pair. The tag-key should be replaced with a specified tag key. For more information, see example 2.</li>
The maximum number of `Filters` in each request is 10. The upper limit for `Filter.Values` is 5. This parameter cannot specify `AutoScalingGroupIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        """
        self._AutoScalingGroupIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def AutoScalingGroupIds(self):
        return self._AutoScalingGroupIds

    @AutoScalingGroupIds.setter
    def AutoScalingGroupIds(self, AutoScalingGroupIds):
        self._AutoScalingGroupIds = AutoScalingGroupIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._AutoScalingGroupIds = params.get("AutoScalingGroupIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoScalingGroupsResponse(AbstractModel):
    """DescribeAutoScalingGroups response structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupSet: List of auto scaling group details.
        :type AutoScalingGroupSet: list of AutoScalingGroup
        :param _TotalCount: Number of eligible auto scaling groups.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoScalingGroupSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AutoScalingGroupSet(self):
        return self._AutoScalingGroupSet

    @AutoScalingGroupSet.setter
    def AutoScalingGroupSet(self, AutoScalingGroupSet):
        self._AutoScalingGroupSet = AutoScalingGroupSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AutoScalingGroupSet") is not None:
            self._AutoScalingGroupSet = []
            for item in params.get("AutoScalingGroupSet"):
                obj = AutoScalingGroup()
                obj._deserialize(item)
                self._AutoScalingGroupSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAutoScalingInstancesRequest(AbstractModel):
    """DescribeAutoScalingInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: IDs of the CVM instances to query. Up to 100 IDs can be queried at one time. `InstanceIds` and `Filters` can not be both specified.
        :type InstanceIds: list of str
        :param _Filters: Filter.
<li> instance-id - String - Required: No - (Filter) Filter by instance ID.</li>
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
The maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `InstanceIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param _Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: The number of returned results. Default value: `20`. Maximum value: `100`. For more information on `Limit`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        """
        self._InstanceIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoScalingInstancesResponse(AbstractModel):
    """DescribeAutoScalingInstances response structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingInstanceSet: List of instance details.
        :type AutoScalingInstanceSet: list of Instance
        :param _TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoScalingInstanceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AutoScalingInstanceSet(self):
        return self._AutoScalingInstanceSet

    @AutoScalingInstanceSet.setter
    def AutoScalingInstanceSet(self, AutoScalingInstanceSet):
        self._AutoScalingInstanceSet = AutoScalingInstanceSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AutoScalingInstanceSet") is not None:
            self._AutoScalingInstanceSet = []
            for item in params.get("AutoScalingInstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self._AutoScalingInstanceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeLaunchConfigurationsRequest(AbstractModel):
    """DescribeLaunchConfigurations request structure.

    """

    def __init__(self):
        r"""
        :param _LaunchConfigurationIds: Queries by one or more launch configuration IDs in the format of `asc-ouy1ax38`. The maximum quantity per request is 100. This parameter does not support specifying both `LaunchConfigurationIds` and `Filters` at the same time.
        :type LaunchConfigurationIds: list of str
        :param _Filters: Filters
<li> `launch-configuration-id` - String - Required: No - Filter by launch configuration ID.</li>
<li> `launch-configuration-name` - String - Required: No - Filter by launch configuration name.</li>
<li> `launch-configuration-name` - String - Required: No - Fuzzy search by launch configuration name.</li>
<li> `tag-key` - String - Required: No - Filter by the tag key.</li>
<li> `tag-value` - String - Required: No - Filter by the tag value.</li>
<li>tag:tag-key - String - Optional - Filter by tag key pair. Use a specific tag key to replace `tag-key`. See Example 3 for the detailed usage.</li>
</li>
The maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `LaunchConfigurationIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param _Limit: The number of returned results. Default value: `20`. Maximum value: `100`. For more information on `Limit`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _Offset: The offset. Default value: `0`. For more information on `Offset`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        """
        self._LaunchConfigurationIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def LaunchConfigurationIds(self):
        return self._LaunchConfigurationIds

    @LaunchConfigurationIds.setter
    def LaunchConfigurationIds(self, LaunchConfigurationIds):
        self._LaunchConfigurationIds = LaunchConfigurationIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._LaunchConfigurationIds = params.get("LaunchConfigurationIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLaunchConfigurationsResponse(AbstractModel):
    """DescribeLaunchConfigurations response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible launch configurations.
        :type TotalCount: int
        :param _LaunchConfigurationSet: List of launch configuration details.
        :type LaunchConfigurationSet: list of LaunchConfiguration
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._LaunchConfigurationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LaunchConfigurationSet(self):
        return self._LaunchConfigurationSet

    @LaunchConfigurationSet.setter
    def LaunchConfigurationSet(self, LaunchConfigurationSet):
        self._LaunchConfigurationSet = LaunchConfigurationSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("LaunchConfigurationSet") is not None:
            self._LaunchConfigurationSet = []
            for item in params.get("LaunchConfigurationSet"):
                obj = LaunchConfiguration()
                obj._deserialize(item)
                self._LaunchConfigurationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLifecycleHooksRequest(AbstractModel):
    """DescribeLifecycleHooks request structure.

    """

    def __init__(self):
        r"""
        :param _LifecycleHookIds: Queries by one or more lifecycle hook IDs in the format of `ash-8azjzxcl`. The maximum quantity per request is 100. This parameter does not support specifying both `LifecycleHookIds` and `Filters` at the same time.
        :type LifecycleHookIds: list of str
        :param _Filters: Filters.
<li> `lifecycle-hook-id` - String - Required: No - (Filter) Filter by lifecycle hook ID.</li>
<li> `lifecycle-hook-name` - String - Required: No - (Filter) Filter by lifecycle hook name.</li>
<li> `auto-scaling-group-id` - String - Required: No - (Filter) Filter by scaling group ID.</li>
Up to 10 filters can be included in a request and up to 5 values for each filter. It cannot be specified with `LifecycleHookIds` at the same time.
        :type Filters: list of Filter
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        """
        self._LifecycleHookIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def LifecycleHookIds(self):
        return self._LifecycleHookIds

    @LifecycleHookIds.setter
    def LifecycleHookIds(self, LifecycleHookIds):
        self._LifecycleHookIds = LifecycleHookIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._LifecycleHookIds = params.get("LifecycleHookIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLifecycleHooksResponse(AbstractModel):
    """DescribeLifecycleHooks response structure.

    """

    def __init__(self):
        r"""
        :param _LifecycleHookSet: Array of lifecycle hooks
        :type LifecycleHookSet: list of LifecycleHook
        :param _TotalCount: Total quantity
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LifecycleHookSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def LifecycleHookSet(self):
        return self._LifecycleHookSet

    @LifecycleHookSet.setter
    def LifecycleHookSet(self, LifecycleHookSet):
        self._LifecycleHookSet = LifecycleHookSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LifecycleHookSet") is not None:
            self._LifecycleHookSet = []
            for item in params.get("LifecycleHookSet"):
                obj = LifecycleHook()
                obj._deserialize(item)
                self._LifecycleHookSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeNotificationConfigurationsRequest(AbstractModel):
    """DescribeNotificationConfigurations request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingNotificationIds: Queries by one or more notification IDs in the format of asn-2sestqbr. The maximum number of instances per request is 100. This parameter does not support specifying both `AutoScalingNotificationIds` and `Filters` at the same time.
        :type AutoScalingNotificationIds: list of str
        :param _Filters: Filter.
<li> auto-scaling-notification-id - String - Required: No - (Filter) Filter by notification ID.</li>
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
The maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `AutoScalingNotificationIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        """
        self._AutoScalingNotificationIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def AutoScalingNotificationIds(self):
        return self._AutoScalingNotificationIds

    @AutoScalingNotificationIds.setter
    def AutoScalingNotificationIds(self, AutoScalingNotificationIds):
        self._AutoScalingNotificationIds = AutoScalingNotificationIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._AutoScalingNotificationIds = params.get("AutoScalingNotificationIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotificationConfigurationsResponse(AbstractModel):
    """DescribeNotificationConfigurations response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible notifications.
        :type TotalCount: int
        :param _AutoScalingNotificationSet: List of AS event notification details.
        :type AutoScalingNotificationSet: list of AutoScalingNotification
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AutoScalingNotificationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AutoScalingNotificationSet(self):
        return self._AutoScalingNotificationSet

    @AutoScalingNotificationSet.setter
    def AutoScalingNotificationSet(self, AutoScalingNotificationSet):
        self._AutoScalingNotificationSet = AutoScalingNotificationSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AutoScalingNotificationSet") is not None:
            self._AutoScalingNotificationSet = []
            for item in params.get("AutoScalingNotificationSet"):
                obj = AutoScalingNotification()
                obj._deserialize(item)
                self._AutoScalingNotificationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScalingPoliciesRequest(AbstractModel):
    """DescribeScalingPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingPolicyIds: Queries by one or more alarm policy IDs in the format of asp-i9vkg894. The maximum number of instances per request is 100. This parameter does not support specifying both `AutoScalingPolicyIds` and `Filters` at the same time.
        :type AutoScalingPolicyIds: list of str
        :param _Filters: Filters.
<li> `auto-scaling-policy-id` - String - Optional - Filter by the alarm policy ID.</li>
<li> `auto-scaling-group-id` - String - Optional - Filter by the scaling group ID.</li>
<li> `scaling-policy-name` - String - Optional - Filter by the alarm policy name.</li>
<li> `scaling-policy-type` - String - Optional - Filter by the alarm policy type. Valid values: `SIMPLE`, `TARGET_TRACKING`.</li>
The maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. You cannot specify `AutoScalingPolicyIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        """
        self._AutoScalingPolicyIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def AutoScalingPolicyIds(self):
        return self._AutoScalingPolicyIds

    @AutoScalingPolicyIds.setter
    def AutoScalingPolicyIds(self, AutoScalingPolicyIds):
        self._AutoScalingPolicyIds = AutoScalingPolicyIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._AutoScalingPolicyIds = params.get("AutoScalingPolicyIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScalingPoliciesResponse(AbstractModel):
    """DescribeScalingPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _ScalingPolicySet: List of AS alarm trigger policy details.
        :type ScalingPolicySet: list of ScalingPolicy
        :param _TotalCount: Number of eligible notifications.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ScalingPolicySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ScalingPolicySet(self):
        return self._ScalingPolicySet

    @ScalingPolicySet.setter
    def ScalingPolicySet(self, ScalingPolicySet):
        self._ScalingPolicySet = ScalingPolicySet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ScalingPolicySet") is not None:
            self._ScalingPolicySet = []
            for item in params.get("ScalingPolicySet"):
                obj = ScalingPolicy()
                obj._deserialize(item)
                self._ScalingPolicySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeScheduledActionsRequest(AbstractModel):
    """DescribeScheduledActions request structure.

    """

    def __init__(self):
        r"""
        :param _ScheduledActionIds: Queries by one or more scheduled task IDs in the format of asst-am691zxo. The maximum number of instances per request is 100. This parameter does not support specifying both ScheduledActionIds` and `Filters` at the same time.
        :type ScheduledActionIds: list of str
        :param _Filters: Filter.
<li> scheduled-action-id - String - Required: No - (Filter) Filter by scheduled task ID.</li>
<li> scheduled-action-name - String - Required: No - (Filter) Filter by scheduled task name.</li>
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
        :type Filters: list of Filter
        :param _Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        """
        self._ScheduledActionIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ScheduledActionIds(self):
        return self._ScheduledActionIds

    @ScheduledActionIds.setter
    def ScheduledActionIds(self, ScheduledActionIds):
        self._ScheduledActionIds = ScheduledActionIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ScheduledActionIds = params.get("ScheduledActionIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScheduledActionsResponse(AbstractModel):
    """DescribeScheduledActions response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible scheduled tasks.
        :type TotalCount: int
        :param _ScheduledActionSet: List of scheduled task details.
        :type ScheduledActionSet: list of ScheduledAction
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ScheduledActionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ScheduledActionSet(self):
        return self._ScheduledActionSet

    @ScheduledActionSet.setter
    def ScheduledActionSet(self, ScheduledActionSet):
        self._ScheduledActionSet = ScheduledActionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ScheduledActionSet") is not None:
            self._ScheduledActionSet = []
            for item in params.get("ScheduledActionSet"):
                obj = ScheduledAction()
                obj._deserialize(item)
                self._ScheduledActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DetachInstancesRequest(AbstractModel):
    """DetachInstances request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param _InstanceIds: List of CVM instance IDs
        :type InstanceIds: list of str
        """
        self._AutoScalingGroupId = None
        self._InstanceIds = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachInstancesResponse(AbstractModel):
    """DetachInstances response structure.

    """

    def __init__(self):
        r"""
        :param _ActivityId: Scaling activity ID
        :type ActivityId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class DetachLoadBalancersRequest(AbstractModel):
    """DetachLoadBalancers request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Scaling group ID
        :type AutoScalingGroupId: str
        :param _LoadBalancerIds: List of classic CLB IDs. Up to 20 IDs are allowed. `LoadBalancerIds` and `ForwardLoadBalancerIdentifications` cannot be specified at the same time.
        :type LoadBalancerIds: list of str
        :param _ForwardLoadBalancerIdentifications: List of application CLB IDs. Up to 100 IDs are allowed. `LoadBalancerIds` and `ForwardLoadBalancerIdentifications` cannot be specified at the same time.
        :type ForwardLoadBalancerIdentifications: list of ForwardLoadBalancerIdentification
        """
        self._AutoScalingGroupId = None
        self._LoadBalancerIds = None
        self._ForwardLoadBalancerIdentifications = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ForwardLoadBalancerIdentifications(self):
        return self._ForwardLoadBalancerIdentifications

    @ForwardLoadBalancerIdentifications.setter
    def ForwardLoadBalancerIdentifications(self, ForwardLoadBalancerIdentifications):
        self._ForwardLoadBalancerIdentifications = ForwardLoadBalancerIdentifications


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        if params.get("ForwardLoadBalancerIdentifications") is not None:
            self._ForwardLoadBalancerIdentifications = []
            for item in params.get("ForwardLoadBalancerIdentifications"):
                obj = ForwardLoadBalancerIdentification()
                obj._deserialize(item)
                self._ForwardLoadBalancerIdentifications.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachLoadBalancersResponse(AbstractModel):
    """DetachLoadBalancers response structure.

    """

    def __init__(self):
        r"""
        :param _ActivityId: Scaling activity ID
        :type ActivityId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class DetailedStatusMessage(AbstractModel):
    """Detailed description of scaling activity status

    """

    def __init__(self):
        r"""
        :param _Code: Error type
        :type Code: str
        :param _Zone: AZ information
        :type Zone: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceChargeType: Instance billing mode
        :type InstanceChargeType: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _Message: Error message
        :type Message: str
        :param _InstanceType: Instance type
        :type InstanceType: str
        """
        self._Code = None
        self._Zone = None
        self._InstanceId = None
        self._InstanceChargeType = None
        self._SubnetId = None
        self._Message = None
        self._InstanceType = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Zone = params.get("Zone")
        self._InstanceId = params.get("InstanceId")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._SubnetId = params.get("SubnetId")
        self._Message = params.get("Message")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableAutoScalingGroupRequest(AbstractModel):
    """DisableAutoScalingGroup request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Scaling group ID
        :type AutoScalingGroupId: str
        """
        self._AutoScalingGroupId = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableAutoScalingGroupResponse(AbstractModel):
    """DisableAutoScalingGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnableAutoScalingGroupRequest(AbstractModel):
    """EnableAutoScalingGroup request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        """
        self._AutoScalingGroupId = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableAutoScalingGroupResponse(AbstractModel):
    """EnableAutoScalingGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnhancedService(AbstractModel):
    """This describes the conditions and configurations of the enhanced services of the instance, such as cloud security, cloud monitor, TencentCloud Automation Tools, and other instance agents.

    """

    def __init__(self):
        r"""
        :param _SecurityService: Enables the Cloud Security service. If this parameter is not specified, the Cloud Security service will be enabled by default.
        :type SecurityService: :class:`tencentcloud.autoscaling.v20180419.models.RunSecurityServiceEnabled`
        :param _MonitorService: Enables the Cloud Monitor service. If this parameter is not specified, the Cloud Monitor service will be enabled by default.
        :type MonitorService: :class:`tencentcloud.autoscaling.v20180419.models.RunMonitorServiceEnabled`
        :param _AutomationService: Deprecated parameter.
        :type AutomationService: list of RunAutomationServiceEnabled
        :param _AutomationToolsService: Enable TAT service. If this parameter is not specified, the default logic is the same as that of the CVM instance. Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AutomationToolsService: :class:`tencentcloud.autoscaling.v20180419.models.RunAutomationServiceEnabled`
        """
        self._SecurityService = None
        self._MonitorService = None
        self._AutomationService = None
        self._AutomationToolsService = None

    @property
    def SecurityService(self):
        return self._SecurityService

    @SecurityService.setter
    def SecurityService(self, SecurityService):
        self._SecurityService = SecurityService

    @property
    def MonitorService(self):
        return self._MonitorService

    @MonitorService.setter
    def MonitorService(self, MonitorService):
        self._MonitorService = MonitorService

    @property
    def AutomationService(self):
        return self._AutomationService

    @AutomationService.setter
    def AutomationService(self, AutomationService):
        self._AutomationService = AutomationService

    @property
    def AutomationToolsService(self):
        return self._AutomationToolsService

    @AutomationToolsService.setter
    def AutomationToolsService(self, AutomationToolsService):
        self._AutomationToolsService = AutomationToolsService


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self._SecurityService = RunSecurityServiceEnabled()
            self._SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self._MonitorService = RunMonitorServiceEnabled()
            self._MonitorService._deserialize(params.get("MonitorService"))
        if params.get("AutomationService") is not None:
            self._AutomationService = []
            for item in params.get("AutomationService"):
                obj = RunAutomationServiceEnabled()
                obj._deserialize(item)
                self._AutomationService.append(obj)
        if params.get("AutomationToolsService") is not None:
            self._AutomationToolsService = RunAutomationServiceEnabled()
            self._AutomationToolsService._deserialize(params.get("AutomationToolsService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteScalingPolicyRequest(AbstractModel):
    """ExecuteScalingPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingPolicyId: Auto-scaling policy ID. This parameter is not available to a target tracking policy.
        :type AutoScalingPolicyId: str
        :param _HonorCooldown: Whether to check if the auto scaling group is in the cooldown period. Default value: false
        :type HonorCooldown: bool
        :param _TriggerSource: Source that triggers the scaling policy. Valid values: API and CLOUD_MONITOR. Default value: API. The value `CLOUD_MONITOR` is specific to the Cloud Monitor service.
        :type TriggerSource: str
        """
        self._AutoScalingPolicyId = None
        self._HonorCooldown = None
        self._TriggerSource = None

    @property
    def AutoScalingPolicyId(self):
        return self._AutoScalingPolicyId

    @AutoScalingPolicyId.setter
    def AutoScalingPolicyId(self, AutoScalingPolicyId):
        self._AutoScalingPolicyId = AutoScalingPolicyId

    @property
    def HonorCooldown(self):
        return self._HonorCooldown

    @HonorCooldown.setter
    def HonorCooldown(self, HonorCooldown):
        self._HonorCooldown = HonorCooldown

    @property
    def TriggerSource(self):
        return self._TriggerSource

    @TriggerSource.setter
    def TriggerSource(self, TriggerSource):
        self._TriggerSource = TriggerSource


    def _deserialize(self, params):
        self._AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        self._HonorCooldown = params.get("HonorCooldown")
        self._TriggerSource = params.get("TriggerSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteScalingPolicyResponse(AbstractModel):
    """ExecuteScalingPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _ActivityId: Scaling activity ID
        :type ActivityId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """> Describes key-value pair filters used for conditional queries, such as filtering results by ID, name and state.
    > * If there are multiple `Filter` parameters, the relationship among them will be logical `AND`.
    > * If there are multiple `Values` for the same `Filter`, the relationship among the `Values` for the same `Filter` will be logical `OR`.

    """

    def __init__(self):
        r"""
        :param _Name: Field to be filtered.
        :type Name: str
        :param _Values: Filter value of the field.
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForwardLoadBalancer(AbstractModel):
    """Application load balancer

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: Load balancer ID
        :type LoadBalancerId: str
        :param _ListenerId: Application load balancer listener ID
        :type ListenerId: str
        :param _TargetAttributes: List of target rule attributes
        :type TargetAttributes: list of TargetAttribute
        :param _LocationId: ID of a forwarding rule. This parameter is required for layer-7 listeners.
        :type LocationId: str
        :param _Region: The region of CLB instance. It defaults to the region of AS service and is in the format of the common parameter `Region`, such as `ap-guangzhou`.
        :type Region: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._TargetAttributes = None
        self._LocationId = None
        self._Region = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def TargetAttributes(self):
        return self._TargetAttributes

    @TargetAttributes.setter
    def TargetAttributes(self, TargetAttributes):
        self._TargetAttributes = TargetAttributes

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("TargetAttributes") is not None:
            self._TargetAttributes = []
            for item in params.get("TargetAttributes"):
                obj = TargetAttribute()
                obj._deserialize(item)
                self._TargetAttributes.append(obj)
        self._LocationId = params.get("LocationId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForwardLoadBalancerIdentification(AbstractModel):
    """Application CLB IDs

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: ID of the CLB
        :type LoadBalancerId: str
        :param _ListenerId: Application CLB listener ID
        :type ListenerId: str
        :param _LocationId: ID of a forwarding rule. This parameter is required for layer-7 listeners.
        :type LocationId: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._LocationId = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._LocationId = params.get("LocationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostNameSettings(AbstractModel):
    """CVM HostName settings

    """

    def __init__(self):
        r"""
        :param _HostName: Hostname of a CVM
<br><li>The `HostName` cannot start or end with a period (.) or hyphen (-), and cannot contain consecutive periods and hyphens.
<br><li>This field is unavailable to CVM instances.
<br><li>Other types of instances (such as Linux): the name contains 2 to 40 characters, and supports multiple periods (.). The string between two periods can consist of letters (case insensitive), numbers, and hyphens (-), and cannot be all numbers.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type HostName: str
        :param _HostNameStyle: Type of CVM host name. Valid values: "ORIGINAL" and "UNIQUE". Default value: "ORIGINAL"
<br><li> ORIGINAL. Auto Scaling transfers the HostName set in input parameters to the CVM directly. CVM may adds serial numbers for the HostName. The HostName of instances within the auto scaling group may conflict.
<br><li> UNIQUE. The HostName set in input parameters is the prefix of a host name. Auto Scaling and CVM expand it. The HostName of an instance in the auto scaling group is unique.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HostNameStyle: str
        """
        self._HostName = None
        self._HostNameStyle = None

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def HostNameStyle(self):
        return self._HostNameStyle

    @HostNameStyle.setter
    def HostNameStyle(self, HostNameStyle):
        self._HostNameStyle = HostNameStyle


    def _deserialize(self, params):
        self._HostName = params.get("HostName")
        self._HostNameStyle = params.get("HostNameStyle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPv6InternetAccessible(AbstractModel):
    """This describes the IPv6 address public network accessibility of the instance created by a launch configuration and declares the public network usage billing method of the IPv6 address and the maximum bandwidth.

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: Network billing mode. Valid values: TRAFFIC_POSTPAID_BY_HOUR, BANDWIDTH_PACKAGE. Default value: TRAFFIC_POSTPAID_BY_HOUR. For the current account type, see [Account Type Description](https://intl.cloud.tencent.com/document/product/1199/49090?from_cn_redirect=1#judge).
<br><li> IPv6 supports `TRAFFIC_POSTPAID_BY_HOUR` under a bill-by-IP account.
<br><li> IPv6 supports `BANDWIDTH_PACKAGE` under a bill-by-CVM account.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: Outbound bandwidth cap of the public network (in Mbps). <br>It defaults to `0`, which indicates no public network bandwidth is allocated to IPv6. The value range of bandwidth caps varies with the model, availability zone and billing mode. For more information, see [Public Network Bandwidth Cap](https://intl.cloud.tencent.com/document/product/213/12523?from_cn_redirect=1).
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InternetMaxBandwidthOut: int
        :param _BandwidthPackageId: Bandwidth package ID. You can obtain the ID from the `BandwidthPackageId` field in the response of the [DescribeBandwidthPackages](https://intl.cloud.tencent.com/document/api/215/19209?from_cn_redirect=1) API.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BandwidthPackageId: str
        """
        self._InternetChargeType = None
        self._InternetMaxBandwidthOut = None
        self._BandwidthPackageId = None

    @property
    def InternetChargeType(self):
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def BandwidthPackageId(self):
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId


    def _deserialize(self, params):
        self._InternetChargeType = params.get("InternetChargeType")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """Instance information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param _LaunchConfigurationId: Launch configuration ID
        :type LaunchConfigurationId: str
        :param _LaunchConfigurationName: Launch configuration name
        :type LaunchConfigurationName: str
        :param _LifeCycleState: Lifecycle status. Valid values:<br>
<li>`IN_SERVICE`: The instance is running.
<li>`CREATING`: The instance is being created.
<li>`CREATION_FAILED`: The instance fails to be created.
<li>`TERMINATING`: The instance is being terminated.
<li>`TERMINATION_FAILED`: The instance fails to be terminated.
<li>`ATTACHING`: The instance is being bound.
<li>`ATTACH_FAILED`: The instance fails to be bound.
<li>`DETACHING`: The instance is being unbound.
<li>`DETACH_FAILED`: The instance fails to be unbound.
<li>`ATTACHING_LB`: The LB is being bound.
<li>DETACHING_LB: The LB is being unbound.
<li>`MODIFYING_LB`: The LB is being modified.
<li>`STARTING`: The instance is being started up.
<li>`START_FAILED`: The instance fails to be started up.
<li>`STOPPING`: The instance is being shut down.
<li>`STOP_FAILED`: The instance fails to be shut down.
<li>`STOPPED`: The instance is shut down.
<li>`IN_LAUNCHING_HOOK`: The lifecycle hook is being scaled out.
<li>`IN_TERMINATING_HOOK`: The lifecycle hook is being scaled in.
        :type LifeCycleState: str
        :param _HealthStatus: Health status. Value range: HEALTHY, UNHEALTHY
        :type HealthStatus: str
        :param _ProtectedFromScaleIn: Whether to add scale-in protection
        :type ProtectedFromScaleIn: bool
        :param _Zone: Availability zone
        :type Zone: str
        :param _CreationType: Creation type. Value range: AUTO_CREATION, MANUAL_ATTACHING.
        :type CreationType: str
        :param _AddTime: Instance addition time
        :type AddTime: str
        :param _InstanceType: Instance type
        :type InstanceType: str
        :param _VersionNumber: Version number
        :type VersionNumber: int
        :param _AutoScalingGroupName: Auto scaling group name
        :type AutoScalingGroupName: str
        :param _WarmupStatus: Warming up status. Valid values:
<li>`WAITING_ENTER_WARMUP`: The instance is waiting to be warmed up.
<li>`NO_NEED_WARMUP`: Warming up is not required.
<li>`IN_WARMUP`: The instance is being warmed up.
<li>`AFTER_WARMUP`: Warming up is completed.
        :type WarmupStatus: str
        :param _DisasterRecoverGroupIds: Placement group ID. Only one is allowed.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DisasterRecoverGroupIds: list of str
        """
        self._InstanceId = None
        self._AutoScalingGroupId = None
        self._LaunchConfigurationId = None
        self._LaunchConfigurationName = None
        self._LifeCycleState = None
        self._HealthStatus = None
        self._ProtectedFromScaleIn = None
        self._Zone = None
        self._CreationType = None
        self._AddTime = None
        self._InstanceType = None
        self._VersionNumber = None
        self._AutoScalingGroupName = None
        self._WarmupStatus = None
        self._DisasterRecoverGroupIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def LaunchConfigurationName(self):
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def LifeCycleState(self):
        return self._LifeCycleState

    @LifeCycleState.setter
    def LifeCycleState(self, LifeCycleState):
        self._LifeCycleState = LifeCycleState

    @property
    def HealthStatus(self):
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def ProtectedFromScaleIn(self):
        return self._ProtectedFromScaleIn

    @ProtectedFromScaleIn.setter
    def ProtectedFromScaleIn(self, ProtectedFromScaleIn):
        self._ProtectedFromScaleIn = ProtectedFromScaleIn

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CreationType(self):
        return self._CreationType

    @CreationType.setter
    def CreationType(self, CreationType):
        self._CreationType = CreationType

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def VersionNumber(self):
        return self._VersionNumber

    @VersionNumber.setter
    def VersionNumber(self, VersionNumber):
        self._VersionNumber = VersionNumber

    @property
    def AutoScalingGroupName(self):
        return self._AutoScalingGroupName

    @AutoScalingGroupName.setter
    def AutoScalingGroupName(self, AutoScalingGroupName):
        self._AutoScalingGroupName = AutoScalingGroupName

    @property
    def WarmupStatus(self):
        return self._WarmupStatus

    @WarmupStatus.setter
    def WarmupStatus(self, WarmupStatus):
        self._WarmupStatus = WarmupStatus

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._LaunchConfigurationName = params.get("LaunchConfigurationName")
        self._LifeCycleState = params.get("LifeCycleState")
        self._HealthStatus = params.get("HealthStatus")
        self._ProtectedFromScaleIn = params.get("ProtectedFromScaleIn")
        self._Zone = params.get("Zone")
        self._CreationType = params.get("CreationType")
        self._AddTime = params.get("AddTime")
        self._InstanceType = params.get("InstanceType")
        self._VersionNumber = params.get("VersionNumber")
        self._AutoScalingGroupName = params.get("AutoScalingGroupName")
        self._WarmupStatus = params.get("WarmupStatus")
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargePrepaid(AbstractModel):
    """This API is used to describe the billing mode of an instance.

    """

    def __init__(self):
        r"""
        :param _Period: Purchased usage period of an instance in months. Value range: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.
        :type Period: int
        :param _RenewFlag: Auto-renewal flag. Value range: <br><li>NOTIFY_AND_AUTO_RENEW: Notify expiry and renew automatically <br><li>NOTIFY_AND_MANUAL_RENEW: Notify expiry but not renew automatically <br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: Neither notify expiry nor renew automatically <br><br>Default value: NOTIFY_AND_MANUAL_RENEW. If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis if the account balance is sufficient.
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceMarketOptionsRequest(AbstractModel):
    """Options related to a CVM bidding request

    """

    def __init__(self):
        r"""
        :param _SpotOptions: Bidding-related options
        :type SpotOptions: :class:`tencentcloud.autoscaling.v20180419.models.SpotMarketOptions`
        :param _MarketType: Market option type. Currently, this only supports the value "spot"
Note: This field may return null, indicating that no valid values can be obtained.
        :type MarketType: str
        """
        self._SpotOptions = None
        self._MarketType = None

    @property
    def SpotOptions(self):
        return self._SpotOptions

    @SpotOptions.setter
    def SpotOptions(self, SpotOptions):
        self._SpotOptions = SpotOptions

    @property
    def MarketType(self):
        return self._MarketType

    @MarketType.setter
    def MarketType(self, MarketType):
        self._MarketType = MarketType


    def _deserialize(self, params):
        if params.get("SpotOptions") is not None:
            self._SpotOptions = SpotMarketOptions()
            self._SpotOptions._deserialize(params.get("SpotOptions"))
        self._MarketType = params.get("MarketType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNameSettings(AbstractModel):
    """Settings of CVM instance names.

    """

    def __init__(self):
        r"""
        :param _InstanceName: CVM instance name

The `InstanceName` cannot start or end with a dot (.) or hyphen (-), and cannot contain consecutive dots and hyphens.
The name contains 2 to 40 characters, and supports multiple dots (.). The string between two dots can consist of letters (case-insensitive), numbers, and hyphens (-), and cannot be all numbers.
        :type InstanceName: str
        :param _InstanceNameStyle: Type of CVM instance name. Valid values: `ORIGINAL` and `UNIQUE`. Default value: `ORIGINAL`.

`ORIGINAL`: Auto Scaling sends the input parameter `InstanceName` to the CVM directly. The CVM may append a serial number to the `InstanceName`. The `InstanceName` of the instances within the scaling group may conflict.

`UNIQUE`: the input parameter `InstanceName` is the prefix of an instance name. Auto Scaling and CVM expand it. The `InstanceName` of an instance in the scaling group is unique.
        :type InstanceNameStyle: str
        """
        self._InstanceName = None
        self._InstanceNameStyle = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceNameStyle(self):
        return self._InstanceNameStyle

    @InstanceNameStyle.setter
    def InstanceNameStyle(self, InstanceNameStyle):
        self._InstanceNameStyle = InstanceNameStyle


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._InstanceNameStyle = params.get("InstanceNameStyle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTag(AbstractModel):
    """Instance tag. This parameter is used to bind tags to newly added instances.

    """

    def __init__(self):
        r"""
        :param _Key: Tag key
        :type Key: str
        :param _Value: Tag value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAccessible(AbstractModel):
    """This describes the internet accessibility of the instance created by a launch configuration and declares the internet usage billing method of the instance and the maximum bandwidth

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: Network billing method. Value range: <br><li>BANDWIDTH_PREPAID: Prepaid by bandwidth <br><li>TRAFFIC_POSTPAID_BY_HOUR: Postpaid by traffic on a per hour basis <br><li>BANDWIDTH_POSTPAID_BY_HOUR: Postpaid by bandwidth on a per hour basis <br><li>BANDWIDTH_PACKAGE: BWP user <br>Default value: TRAFFIC_POSTPAID_BY_HOUR.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: The maximum outbound bandwidth in Mbps of the public network. The default value is 0 Mbps. The upper limit of bandwidth varies by model. For more information, see [Purchase Network Bandwidth](https://intl.cloud.tencent.com/document/product/213/509?from_cn_redirect=1).
Note: This field may return null, indicating that no valid values can be obtained.
        :type InternetMaxBandwidthOut: int
        :param _PublicIpAssigned: Whether to assign a public IP. Value range: <br><li>TRUE: Assign a public IP <br><li>FALSE: Do not assign a public IP <br><br>If the public network bandwidth is greater than 0 Mbps, you are free to choose whether to enable the public IP (which is enabled by default). If the public network bandwidth is 0 Mbps, no public IP will be allowed to be assigned.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicIpAssigned: bool
        :param _BandwidthPackageId: Bandwidth package ID. You can obtain the ID from the `BandwidthPackageId` field in the response of the [DescribeBandwidthPackages](https://intl.cloud.tencent.com/document/api/215/19209?from_cn_redirect=1) API.
Note: this field may return null, indicating that no valid value was found.
        :type BandwidthPackageId: str
        """
        self._InternetChargeType = None
        self._InternetMaxBandwidthOut = None
        self._PublicIpAssigned = None
        self._BandwidthPackageId = None

    @property
    def InternetChargeType(self):
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def PublicIpAssigned(self):
        return self._PublicIpAssigned

    @PublicIpAssigned.setter
    def PublicIpAssigned(self, PublicIpAssigned):
        self._PublicIpAssigned = PublicIpAssigned

    @property
    def BandwidthPackageId(self):
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId


    def _deserialize(self, params):
        self._InternetChargeType = params.get("InternetChargeType")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._PublicIpAssigned = params.get("PublicIpAssigned")
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvocationResult(AbstractModel):
    """Result of the command execution

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _InvocationId: Execution activity ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InvocationId: str
        :param _InvocationTaskId: Execution task ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InvocationTaskId: str
        :param _CommandId: Command ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CommandId: str
        :param _TaskStatus: Execution Status
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskStatus: str
        :param _ErrorMessage: Execution exception information
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMessage: str
        """
        self._InstanceId = None
        self._InvocationId = None
        self._InvocationTaskId = None
        self._CommandId = None
        self._TaskStatus = None
        self._ErrorMessage = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InvocationId(self):
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def InvocationTaskId(self):
        return self._InvocationTaskId

    @InvocationTaskId.setter
    def InvocationTaskId(self, InvocationTaskId):
        self._InvocationTaskId = InvocationTaskId

    @property
    def CommandId(self):
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InvocationId = params.get("InvocationId")
        self._InvocationTaskId = params.get("InvocationTaskId")
        self._CommandId = params.get("CommandId")
        self._TaskStatus = params.get("TaskStatus")
        self._ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaunchConfiguration(AbstractModel):
    """Information set of eligible launch configurations.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID of the instance.
        :type ProjectId: int
        :param _LaunchConfigurationId: Launch configuration ID
        :type LaunchConfigurationId: str
        :param _LaunchConfigurationName: Launch configuration name.
        :type LaunchConfigurationName: str
        :param _InstanceType: Instance model.
        :type InstanceType: str
        :param _SystemDisk: Information of the instance's system disk configuration.
        :type SystemDisk: :class:`tencentcloud.autoscaling.v20180419.models.SystemDisk`
        :param _DataDisks: Information of the instance's data disk configuration.
        :type DataDisks: list of DataDisk
        :param _LoginSettings: Instance login settings.
        :type LoginSettings: :class:`tencentcloud.autoscaling.v20180419.models.LimitedLoginSettings`
        :param _InternetAccessible: Information of the public network bandwidth configuration.
        :type InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        :param _SecurityGroupIds: Security group of the instance.
        :type SecurityGroupIds: list of str
        :param _AutoScalingGroupAbstractSet: Auto scaling group associated with the launch configuration.
        :type AutoScalingGroupAbstractSet: list of AutoScalingGroupAbstract
        :param _UserData: Custom data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserData: str
        :param _CreatedTime: Creation time of the launch configuration.
        :type CreatedTime: str
        :param _EnhancedService: Conditions of enhancement services for the instance and their settings.
        :type EnhancedService: :class:`tencentcloud.autoscaling.v20180419.models.EnhancedService`
        :param _ImageId: Image ID.
        :type ImageId: str
        :param _LaunchConfigurationStatus: Current status of the launch configuration. Value range: <br><li>NORMAL: normal <br><li>IMAGE_ABNORMAL: Exception with the image of the launch configuration <br><li>CBS_SNAP_ABNORMAL: Exception with the data disk snapshot of the launch configuration <br><li>SECURITY_GROUP_ABNORMAL: Exception with the security group of the launch configuration<br>
        :type LaunchConfigurationStatus: str
        :param _InstanceChargeType: Instance billing mode. CVM instances take `POSTPAID_BY_HOUR` by default. Valid values:
<br><li>POSTPAID_BY_HOUR: pay-as-you-go hourly
<br><li>SPOTPAID: spot instance
        :type InstanceChargeType: str
        :param _InstanceMarketOptions: Market options of the instance, such as parameters related to spot instances. This parameter is required for spot instances.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceMarketOptions: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        :param _InstanceTypes: List of instance models.
        :type InstanceTypes: list of str
        :param _InstanceTags: List of instance tags, which will be added to instances created by the scale-out activity. Up to 10 tags allowed.
        :type InstanceTags: list of InstanceTag
        :param _Tags: Tag list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _VersionNumber: Version
        :type VersionNumber: int
        :param _UpdatedTime: Update time
        :type UpdatedTime: str
        :param _CamRoleName: CAM role name. This parameter can be obtained from the `roleName` field returned by DescribeRoleList API.
        :type CamRoleName: str
        :param _LastOperationInstanceTypesCheckPolicy: Value of InstanceTypesCheckPolicy upon the last operation.
        :type LastOperationInstanceTypesCheckPolicy: str
        :param _HostNameSettings: CVM hostname settings.
        :type HostNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.HostNameSettings`
        :param _InstanceNameSettings: Settings of CVM instance names
        :type InstanceNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameSettings`
        :param _InstanceChargePrepaid: Details of the monthly subscription, including the purchase period, auto-renewal. It is required if the `InstanceChargeType` is `PREPAID`.
        :type InstanceChargePrepaid: :class:`tencentcloud.autoscaling.v20180419.models.InstanceChargePrepaid`
        :param _DiskTypePolicy: Selection policy of cloud disks. Default value: ORIGINAL. Valid values:
<br><li>ORIGINAL: uses the configured cloud disk type
<br><li>AUTOMATIC: automatically chooses an available cloud disk type in the current availability zone
        :type DiskTypePolicy: str
        :param _HpcClusterId: HPC ID<br>
Note: This field is default to empty
        :type HpcClusterId: str
        :param _IPv6InternetAccessible: IPv6 public network bandwidth configuration.
        :type IPv6InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.IPv6InternetAccessible`
        """
        self._ProjectId = None
        self._LaunchConfigurationId = None
        self._LaunchConfigurationName = None
        self._InstanceType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._LoginSettings = None
        self._InternetAccessible = None
        self._SecurityGroupIds = None
        self._AutoScalingGroupAbstractSet = None
        self._UserData = None
        self._CreatedTime = None
        self._EnhancedService = None
        self._ImageId = None
        self._LaunchConfigurationStatus = None
        self._InstanceChargeType = None
        self._InstanceMarketOptions = None
        self._InstanceTypes = None
        self._InstanceTags = None
        self._Tags = None
        self._VersionNumber = None
        self._UpdatedTime = None
        self._CamRoleName = None
        self._LastOperationInstanceTypesCheckPolicy = None
        self._HostNameSettings = None
        self._InstanceNameSettings = None
        self._InstanceChargePrepaid = None
        self._DiskTypePolicy = None
        self._HpcClusterId = None
        self._IPv6InternetAccessible = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def LaunchConfigurationName(self):
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def AutoScalingGroupAbstractSet(self):
        return self._AutoScalingGroupAbstractSet

    @AutoScalingGroupAbstractSet.setter
    def AutoScalingGroupAbstractSet(self, AutoScalingGroupAbstractSet):
        self._AutoScalingGroupAbstractSet = AutoScalingGroupAbstractSet

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def LaunchConfigurationStatus(self):
        return self._LaunchConfigurationStatus

    @LaunchConfigurationStatus.setter
    def LaunchConfigurationStatus(self, LaunchConfigurationStatus):
        self._LaunchConfigurationStatus = LaunchConfigurationStatus

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def InstanceTags(self):
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def VersionNumber(self):
        return self._VersionNumber

    @VersionNumber.setter
    def VersionNumber(self, VersionNumber):
        self._VersionNumber = VersionNumber

    @property
    def UpdatedTime(self):
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def LastOperationInstanceTypesCheckPolicy(self):
        return self._LastOperationInstanceTypesCheckPolicy

    @LastOperationInstanceTypesCheckPolicy.setter
    def LastOperationInstanceTypesCheckPolicy(self, LastOperationInstanceTypesCheckPolicy):
        self._LastOperationInstanceTypesCheckPolicy = LastOperationInstanceTypesCheckPolicy

    @property
    def HostNameSettings(self):
        return self._HostNameSettings

    @HostNameSettings.setter
    def HostNameSettings(self, HostNameSettings):
        self._HostNameSettings = HostNameSettings

    @property
    def InstanceNameSettings(self):
        return self._InstanceNameSettings

    @InstanceNameSettings.setter
    def InstanceNameSettings(self, InstanceNameSettings):
        self._InstanceNameSettings = InstanceNameSettings

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def DiskTypePolicy(self):
        return self._DiskTypePolicy

    @DiskTypePolicy.setter
    def DiskTypePolicy(self, DiskTypePolicy):
        self._DiskTypePolicy = DiskTypePolicy

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def IPv6InternetAccessible(self):
        return self._IPv6InternetAccessible

    @IPv6InternetAccessible.setter
    def IPv6InternetAccessible(self, IPv6InternetAccessible):
        self._IPv6InternetAccessible = IPv6InternetAccessible


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._LaunchConfigurationName = params.get("LaunchConfigurationName")
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LimitedLoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("AutoScalingGroupAbstractSet") is not None:
            self._AutoScalingGroupAbstractSet = []
            for item in params.get("AutoScalingGroupAbstractSet"):
                obj = AutoScalingGroupAbstract()
                obj._deserialize(item)
                self._AutoScalingGroupAbstractSet.append(obj)
        self._UserData = params.get("UserData")
        self._CreatedTime = params.get("CreatedTime")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._ImageId = params.get("ImageId")
        self._LaunchConfigurationStatus = params.get("LaunchConfigurationStatus")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._InstanceTypes = params.get("InstanceTypes")
        if params.get("InstanceTags") is not None:
            self._InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTag()
                obj._deserialize(item)
                self._InstanceTags.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._VersionNumber = params.get("VersionNumber")
        self._UpdatedTime = params.get("UpdatedTime")
        self._CamRoleName = params.get("CamRoleName")
        self._LastOperationInstanceTypesCheckPolicy = params.get("LastOperationInstanceTypesCheckPolicy")
        if params.get("HostNameSettings") is not None:
            self._HostNameSettings = HostNameSettings()
            self._HostNameSettings._deserialize(params.get("HostNameSettings"))
        if params.get("InstanceNameSettings") is not None:
            self._InstanceNameSettings = InstanceNameSettings()
            self._InstanceNameSettings._deserialize(params.get("InstanceNameSettings"))
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._DiskTypePolicy = params.get("DiskTypePolicy")
        self._HpcClusterId = params.get("HpcClusterId")
        if params.get("IPv6InternetAccessible") is not None:
            self._IPv6InternetAccessible = IPv6InternetAccessible()
            self._IPv6InternetAccessible._deserialize(params.get("IPv6InternetAccessible"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifecycleActionResultInfo(AbstractModel):
    """Result information of the lifecycle hook action

    """

    def __init__(self):
        r"""
        :param _LifecycleHookId: ID of the lifecycle hook
        :type LifecycleHookId: str
        :param _InstanceId: ID of the instance
        :type InstanceId: str
        :param _InvocationId: Execution task ID. You can query the result by using the [DescribeInvocations](https://intl.cloud.tencent.com/document/api/1340/52679?from_cn_redirect=1) API of TAT. 
        :type InvocationId: str
        :param _InvokeCommandResult: Result of command invocation,
<li>`SUCCESSFUL`: Successful command invocation. It does mean that the task is successfully. You can query the task result with the `InvocationId.</li>
<li>`FAILED`: Failed to invoke the command</li>
<li>`NONE`</li>
        :type InvokeCommandResult: str
        :param _NotificationResult: Notification result, which indicates whether it is successful to notify CMQ/TDMQ.<br>
<li>SUCCESSFUL: It is successful to notify CMQ/TDMQ.</li>
<li>FAILED: It is failed to notify CMQ/TDMQ.</li>
<li>NONE</li>
        :type NotificationResult: str
        :param _LifecycleActionResult: Result of the lifecyle hook action. Values: CONTINUE, ABANDON
        :type LifecycleActionResult: str
        :param _ResultReason: Reason of the result <br>
<li>`HEARTBEAT_TIMEOUT`: Heartbeat timed out. The setting of `DefaultResult` is used.</li>
<li>`NOTIFICATION_FAILURE`: Failed to send the notification. The setting of `DefaultResult` is used.</li>
<li>`CALL_INTERFACE`: Calls the `CompleteLifecycleAction` to set the result</li>
<li>ANOTHER_ACTION_ABANDON: It has been set to `ABANDON` by another operation.</li>
<li>COMMAND_CALL_FAILURE: Failed to call the command. The DefaultResult is applied.</li>
<li>COMMAND_EXEC_FINISH: Command completed</li>
<li>COMMAND_CALL_FAILURE: Failed to execute the command. The DefaultResult is applied.</li>
<li>COMMAND_EXEC_RESULT_CHECK_FAILURE: Failed to check the command result. The DefaultResult is applied.</li>
        :type ResultReason: str
        """
        self._LifecycleHookId = None
        self._InstanceId = None
        self._InvocationId = None
        self._InvokeCommandResult = None
        self._NotificationResult = None
        self._LifecycleActionResult = None
        self._ResultReason = None

    @property
    def LifecycleHookId(self):
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InvocationId(self):
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def InvokeCommandResult(self):
        return self._InvokeCommandResult

    @InvokeCommandResult.setter
    def InvokeCommandResult(self, InvokeCommandResult):
        self._InvokeCommandResult = InvokeCommandResult

    @property
    def NotificationResult(self):
        return self._NotificationResult

    @NotificationResult.setter
    def NotificationResult(self, NotificationResult):
        self._NotificationResult = NotificationResult

    @property
    def LifecycleActionResult(self):
        return self._LifecycleActionResult

    @LifecycleActionResult.setter
    def LifecycleActionResult(self, LifecycleActionResult):
        self._LifecycleActionResult = LifecycleActionResult

    @property
    def ResultReason(self):
        return self._ResultReason

    @ResultReason.setter
    def ResultReason(self, ResultReason):
        self._ResultReason = ResultReason


    def _deserialize(self, params):
        self._LifecycleHookId = params.get("LifecycleHookId")
        self._InstanceId = params.get("InstanceId")
        self._InvocationId = params.get("InvocationId")
        self._InvokeCommandResult = params.get("InvokeCommandResult")
        self._NotificationResult = params.get("NotificationResult")
        self._LifecycleActionResult = params.get("LifecycleActionResult")
        self._ResultReason = params.get("ResultReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifecycleCommand(AbstractModel):
    """Remote command execution object.

    """

    def __init__(self):
        r"""
        :param _CommandId: Remote command ID. It’s required to execute a command.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CommandId: str
        :param _Parameters: Custom parameter. The field type is JSON encoded string. For example, {"varA": "222"}.
`key` is the name of the custom parameter and `value` is the default value. Both `key` and `value` are strings.
If this parameter is not specified, the `DefaultParameters` of `Command` is used.
Up to 20 customer parameters allowed. The parameter name can contain up to 64 characters, including [a-z], [A-Z], [0-9] and [-_].
Note: This field may return null, indicating that no valid values can be obtained.
        :type Parameters: str
        """
        self._CommandId = None
        self._Parameters = None

    @property
    def CommandId(self):
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters


    def _deserialize(self, params):
        self._CommandId = params.get("CommandId")
        self._Parameters = params.get("Parameters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifecycleHook(AbstractModel):
    """Lifecycle hook

    """

    def __init__(self):
        r"""
        :param _LifecycleHookId: Lifecycle hook ID
        :type LifecycleHookId: str
        :param _LifecycleHookName: Lifecycle hook name
        :type LifecycleHookName: str
        :param _AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param _DefaultResult: Default result of the lifecycle hook
        :type DefaultResult: str
        :param _HeartbeatTimeout: Wait timeout period of the lifecycle hook
        :type HeartbeatTimeout: int
        :param _LifecycleTransition: Applicable scenario of the lifecycle hook
        :type LifecycleTransition: str
        :param _NotificationMetadata: Additional information for the notification target
        :type NotificationMetadata: str
        :param _CreatedTime: Creation time
        :type CreatedTime: str
        :param _NotificationTarget: Notification target
        :type NotificationTarget: :class:`tencentcloud.autoscaling.v20180419.models.NotificationTarget`
        :param _LifecycleTransitionType: Applicable scenario of the lifecycle hook
        :type LifecycleTransitionType: str
        :param _LifecycleCommand: Remote command execution object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LifecycleCommand: :class:`tencentcloud.autoscaling.v20180419.models.LifecycleCommand`
        """
        self._LifecycleHookId = None
        self._LifecycleHookName = None
        self._AutoScalingGroupId = None
        self._DefaultResult = None
        self._HeartbeatTimeout = None
        self._LifecycleTransition = None
        self._NotificationMetadata = None
        self._CreatedTime = None
        self._NotificationTarget = None
        self._LifecycleTransitionType = None
        self._LifecycleCommand = None

    @property
    def LifecycleHookId(self):
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def LifecycleHookName(self):
        return self._LifecycleHookName

    @LifecycleHookName.setter
    def LifecycleHookName(self, LifecycleHookName):
        self._LifecycleHookName = LifecycleHookName

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def DefaultResult(self):
        return self._DefaultResult

    @DefaultResult.setter
    def DefaultResult(self, DefaultResult):
        self._DefaultResult = DefaultResult

    @property
    def HeartbeatTimeout(self):
        return self._HeartbeatTimeout

    @HeartbeatTimeout.setter
    def HeartbeatTimeout(self, HeartbeatTimeout):
        self._HeartbeatTimeout = HeartbeatTimeout

    @property
    def LifecycleTransition(self):
        return self._LifecycleTransition

    @LifecycleTransition.setter
    def LifecycleTransition(self, LifecycleTransition):
        self._LifecycleTransition = LifecycleTransition

    @property
    def NotificationMetadata(self):
        return self._NotificationMetadata

    @NotificationMetadata.setter
    def NotificationMetadata(self, NotificationMetadata):
        self._NotificationMetadata = NotificationMetadata

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def NotificationTarget(self):
        return self._NotificationTarget

    @NotificationTarget.setter
    def NotificationTarget(self, NotificationTarget):
        self._NotificationTarget = NotificationTarget

    @property
    def LifecycleTransitionType(self):
        return self._LifecycleTransitionType

    @LifecycleTransitionType.setter
    def LifecycleTransitionType(self, LifecycleTransitionType):
        self._LifecycleTransitionType = LifecycleTransitionType

    @property
    def LifecycleCommand(self):
        return self._LifecycleCommand

    @LifecycleCommand.setter
    def LifecycleCommand(self, LifecycleCommand):
        self._LifecycleCommand = LifecycleCommand


    def _deserialize(self, params):
        self._LifecycleHookId = params.get("LifecycleHookId")
        self._LifecycleHookName = params.get("LifecycleHookName")
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._DefaultResult = params.get("DefaultResult")
        self._HeartbeatTimeout = params.get("HeartbeatTimeout")
        self._LifecycleTransition = params.get("LifecycleTransition")
        self._NotificationMetadata = params.get("NotificationMetadata")
        self._CreatedTime = params.get("CreatedTime")
        if params.get("NotificationTarget") is not None:
            self._NotificationTarget = NotificationTarget()
            self._NotificationTarget._deserialize(params.get("NotificationTarget"))
        self._LifecycleTransitionType = params.get("LifecycleTransitionType")
        if params.get("LifecycleCommand") is not None:
            self._LifecycleCommand = LifecycleCommand()
            self._LifecycleCommand._deserialize(params.get("LifecycleCommand"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LimitedLoginSettings(AbstractModel):
    """This describes the configuration and information related to instance login. For security reasons, sensitive information is not described.

    """

    def __init__(self):
        r"""
        :param _KeyIds: List of key IDs.
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginSettings(AbstractModel):
    """Describes login settings of an instance.

    """

    def __init__(self):
        r"""
        :param _Password: Instance login password. <br><li>Linux: 8-16 characters. It should contain at least two sets of the following categories: [a-z], [A-Z], [0-9] and [()`~!@#$%^&*-+=|{}[]:;',.?/]. <br><li>Windows: 12-16 characters. It should contain at least three sets of the following categories: [a-z], [A-Z], [0-9] and [()`~!@#$%^&*-+={}[]:;',.?/]. <br><br>If this parameter is not specified, a random password is generated and sent to you via the Message Center.
        :type Password: str
        :param _KeyIds: List of key IDs. After an instance is associated with a key, you can access the instance with the private key in the key pair. You can call `DescribeKeyPairs` to obtain `KeyId`. Key and password cannot be specified at the same time. Windows instances do not support keys. Currently, you can only specify one key when purchasing an instance.
        :type KeyIds: list of str
        :param _KeepImageLogin: Whether to keep the original settings of an image. It cannot be specified together with `Password` or `KeyIds.N`. You can specify this parameter as `TRUE` only when you create an instance using a custom image, a shared image, or an imported image. Valid values: <br><li>`TRUE`: Keep the login settings of the image <br><li>`FALSE` (Default): Do not keep the login settings of the image <br>
        :type KeepImageLogin: bool
        """
        self._Password = None
        self._KeyIds = None
        self._KeepImageLogin = None

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def KeepImageLogin(self):
        return self._KeepImageLogin

    @KeepImageLogin.setter
    def KeepImageLogin(self, KeepImageLogin):
        self._KeepImageLogin = KeepImageLogin


    def _deserialize(self, params):
        self._Password = params.get("Password")
        self._KeyIds = params.get("KeyIds")
        self._KeepImageLogin = params.get("KeepImageLogin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricAlarm(AbstractModel):
    """Alarming metric of AS

    """

    def __init__(self):
        r"""
        :param _ComparisonOperator: Comparison operator. Value range: <br><li>GREATER_THAN: greater than </li><li>GREATER_THAN_OR_EQUAL_TO: greater than or equal to </li><li>LESS_THAN: less than </li><li> LESS_THAN_OR_EQUAL_TO: less than or equal to </li><li> EQUAL_TO: equal to </li> <li>NOT_EQUAL_TO: not equal to </li>
        :type ComparisonOperator: str
        :param _MetricName: Metric name. Value range: <br><li>CPU_UTILIZATION: CPU utilization </li><li>MEM_UTILIZATION: memory utilization </li><li>LAN_TRAFFIC_OUT: private network outbound bandwidth </li><li>LAN_TRAFFIC_IN: private network inbound bandwidth </li><li>WAN_TRAFFIC_OUT: public network outbound bandwidth </li><li>WAN_TRAFFIC_IN: public network inbound bandwidth </li>
        :type MetricName: str
        :param _Threshold: Alarming threshold: <br><li>CPU_UTILIZATION: [1, 100] in % </li><li>MEM_UTILIZATION: [1, 100] in % </li><li>LAN_TRAFFIC_OUT: >0 in Mbps </li><li>LAN_TRAFFIC_IN: >0 in Mbps </li><li>WAN_TRAFFIC_OUT: >0 in Mbps </li><li>WAN_TRAFFIC_IN: >0 in Mbps </li>
        :type Threshold: int
        :param _Period: Time period in seconds. Enumerated values: 60, 300.
        :type Period: int
        :param _ContinuousTime: Number of repetitions. Value range: [1, 10]
        :type ContinuousTime: int
        :param _Statistic: Statistics type. Value range: <br><li>AVERAGE: average </li><li>MAXIMUM: maximum <li>MINIMUM: minimum </li><br> Default value: AVERAGE
        :type Statistic: str
        :param _PreciseThreshold: Exact alarming threshold. This parameter is only used in API outputs. Values: <br><li>`CPU_UTILIZATION` (in %): (0, 100]</li><li>`MEM_UTILIZATION` (in %): (0, 100]</li><li>`LAN_TRAFFIC_OUT` (in Mbps): > 0</li><li>`LAN_TRAFFIC_IN` (in Mbps): > 0</li><li>`WAN_TRAFFIC_OUT` (in Mbps): > 0</li><li>`WAN_TRAFFIC_IN` (in Mbps): > 0</li>
        :type PreciseThreshold: float
        """
        self._ComparisonOperator = None
        self._MetricName = None
        self._Threshold = None
        self._Period = None
        self._ContinuousTime = None
        self._Statistic = None
        self._PreciseThreshold = None

    @property
    def ComparisonOperator(self):
        return self._ComparisonOperator

    @ComparisonOperator.setter
    def ComparisonOperator(self, ComparisonOperator):
        self._ComparisonOperator = ComparisonOperator

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ContinuousTime(self):
        return self._ContinuousTime

    @ContinuousTime.setter
    def ContinuousTime(self, ContinuousTime):
        self._ContinuousTime = ContinuousTime

    @property
    def Statistic(self):
        return self._Statistic

    @Statistic.setter
    def Statistic(self, Statistic):
        self._Statistic = Statistic

    @property
    def PreciseThreshold(self):
        return self._PreciseThreshold

    @PreciseThreshold.setter
    def PreciseThreshold(self, PreciseThreshold):
        self._PreciseThreshold = PreciseThreshold


    def _deserialize(self, params):
        self._ComparisonOperator = params.get("ComparisonOperator")
        self._MetricName = params.get("MetricName")
        self._Threshold = params.get("Threshold")
        self._Period = params.get("Period")
        self._ContinuousTime = params.get("ContinuousTime")
        self._Statistic = params.get("Statistic")
        self._PreciseThreshold = params.get("PreciseThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoScalingGroupRequest(AbstractModel):
    """ModifyAutoScalingGroup request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param _AutoScalingGroupName: Auto scaling group name, which can only contain letters, numbers, underscores, hyphens ("-"), and decimal points with a maximum length of 55 bytes and must be unique under your account.
        :type AutoScalingGroupName: str
        :param _DefaultCooldown: Default cooldown period in seconds. Default value: 300
        :type DefaultCooldown: int
        :param _DesiredCapacity: Desired number of instances. The number should be no larger than the maximum and no smaller than minimum number of instances
        :type DesiredCapacity: int
        :param _LaunchConfigurationId: Launch configuration ID
        :type LaunchConfigurationId: str
        :param _MaxSize: Maximum number of instances. Value range: 0-2,000.
        :type MaxSize: int
        :param _MinSize: Minimum number of instances. Value range: 0-2,000.
        :type MinSize: int
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _SubnetIds: List of subnet IDs
        :type SubnetIds: list of str
        :param _TerminationPolicies: Termination policy. Currently, the maximum length is 1. Value range: OLDEST_INSTANCE, NEWEST_INSTANCE.
<br><li> OLDEST_INSTANCE: The oldest instance in the auto scaling group will be terminated first.
<br><li> NEWEST_INSTANCE: The newest instance in the auto scaling group will be terminated first.
        :type TerminationPolicies: list of str
        :param _VpcId: VPC ID. This field is left empty for basic networks. You need to specify SubnetIds when modifying the network of the auto scaling group to a VPC with a specified VPC ID. Specify Zones when modifying the network to a basic network.
        :type VpcId: str
        :param _Zones: List of availability zones
        :type Zones: list of str
        :param _RetryPolicy: Retry policy. Valid values: `IMMEDIATE_RETRY` (default), `INCREMENTAL_INTERVALS`, `NO_RETRY`. A partially successful scaling is judged as a failed one.
<br><li>
`IMMEDIATE_RETRY`: Retrying immediately in a short period of time and stopping after five consecutive failures.
<br><li>
`INCREMENTAL_INTERVALS`: Retrying at incremental intervals. As the number of consecutive failures increases, the retry interval gradually increases, ranging from seconds to one day.
<br><li>`NO_RETRY`: Do not retry. Actions are taken when the next call or alarm message comes.
        :type RetryPolicy: str
        :param _ZonesCheckPolicy: Availability zone verification policy. Value range: ALL, ANY. Default value: ANY. This will work when the resource-related fields (launch configuration, availability zone, or subnet) of the auto scaling group are actually modified.
<br><li> ALL: The verification will succeed only if all availability zones (Zone) or subnets (SubnetId) are available; otherwise, an error will be reported.
<br><li> ANY: The verification will success if any availability zone (Zone) or subnet (SubnetId) is available; otherwise, an error will be reported.

Common reasons why an availability zone or subnet is unavailable include stock-out of CVM instances or CBS cloud disks in the availability zone, insufficient quota in the availability zone, or insufficient IPs in the subnet.
If an availability zone or subnet in Zones/SubnetIds does not exist, a verification error will be reported regardless of the value of ZonesCheckPolicy.
        :type ZonesCheckPolicy: str
        :param _ServiceSettings: Service settings such as unhealthy instance replacement.
        :type ServiceSettings: :class:`tencentcloud.autoscaling.v20180419.models.ServiceSettings`
        :param _Ipv6AddressCount: The number of IPv6 addresses that an instance has. Valid values: 0 and 1.
        :type Ipv6AddressCount: int
        :param _MultiZoneSubnetPolicy: Multi-availability zone/subnet policy. Valid values: `PRIORITY` and `EQUALITY`. Default value: `PRIORITY`.
<br><li>`PRIORITY`: When an instance is being created, the availability zone/subnet is chosen from top to bottom in the list. The first availability zone/subnet is always used as long as instances can be created.
<br><li>`EQUALITY`: Instances created for scaling out are distributed to multiple availability zones/subnets, so as to keep the number of instances in different availability zone/subnet in balance.

Notes:
<br><li> When the scaling group is based on the classic network, this policy applies to multiple availability zones. When the scaling group is based on a VPC, this policy applies to multiple subnets, and you do not need to consider availability zones. For example, if you have four subnets (A, B, C, and D) and A, B, and C are in availability zone 1 and D is in availability zone 2, you only need to decide the order of the four subnets, without worrying about the issue of availability zones.
<br><li> This policy is applicable to multiple availability zones/subnets, but is not applicable to multiple models with launch configurations. Specify the models according to the model priority.
<br><li> When `PRIORITY` policy is used, the multi-model policy prevails the multi-availability zones/subnet policy. For example, if you have Model A/B, and Subnet 1/2/3, the model-subnet combinations are tried in the following order: A1 -> A2 -> A3 -> B1 -> B2 -> B3. If A1 is sold out, A2 (not B1) is tried next.
        :type MultiZoneSubnetPolicy: str
        :param _HealthCheckType: Health check type of instances in a scaling group.<br><li>CVM: confirm whether an instance is healthy based on the network status. If the pinged instance is unreachable, the instance will be considered unhealthy. For more information, see [Instance Health Check](https://intl.cloud.tencent.com/document/product/377/8553?from_cn_redirect=1)<br><li>CLB: confirm whether an instance is healthy based on the CLB health check status. For more information, see [Health Check Overview](https://intl.cloud.tencent.com/document/product/214/6097?from_cn_redirect=1).
        :type HealthCheckType: str
        :param _LoadBalancerHealthCheckGracePeriod: Grace period of the CLB health check
        :type LoadBalancerHealthCheckGracePeriod: int
        :param _InstanceAllocationPolicy: Specifies how to assign instances. Valid values: `LAUNCH_CONFIGURATION` and `SPOT_MIXED`.
<br><li>`LAUNCH_CONFIGURATION`: the launch configuration mode.
<br><li>`SPOT_MIXED`: a mixed instance mode. Currently, this mode is supported only when the launch configuration takes the pay-as-you-go billing mode. With this mode, the scaling group can provision a combination of pay-as-you-go instances and spot instances to meet the configured capacity. Note that the billing mode of the associated launch configuration cannot be modified when this mode is used.
        :type InstanceAllocationPolicy: str
        :param _SpotMixedAllocationPolicy: Specifies how to assign pay-as-you-go instances and spot instances.
This parameter is valid only when `InstanceAllocationPolicy` is set to `SPOT_MIXED`.
        :type SpotMixedAllocationPolicy: :class:`tencentcloud.autoscaling.v20180419.models.SpotMixedAllocationPolicy`
        :param _CapacityRebalance: Indicates whether the capacity rebalancing feature is enabled. This parameter is only valid for spot instances in the scaling group. Valid values:
<br><li>`TRUE`: yes. Before the spot instances in the scaling group are about to be automatically repossessed, AS will terminate them. The scale-in hook (if configured) will take effect before the termination. After the termination process starts, AS will asynchronously initiate a scaling activity to meet the desired capacity.
<br><li>`FALSE`: no. In this case, AS will add instances to meet the desired capacity only after the spot instances are terminated.
        :type CapacityRebalance: bool
        """
        self._AutoScalingGroupId = None
        self._AutoScalingGroupName = None
        self._DefaultCooldown = None
        self._DesiredCapacity = None
        self._LaunchConfigurationId = None
        self._MaxSize = None
        self._MinSize = None
        self._ProjectId = None
        self._SubnetIds = None
        self._TerminationPolicies = None
        self._VpcId = None
        self._Zones = None
        self._RetryPolicy = None
        self._ZonesCheckPolicy = None
        self._ServiceSettings = None
        self._Ipv6AddressCount = None
        self._MultiZoneSubnetPolicy = None
        self._HealthCheckType = None
        self._LoadBalancerHealthCheckGracePeriod = None
        self._InstanceAllocationPolicy = None
        self._SpotMixedAllocationPolicy = None
        self._CapacityRebalance = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def AutoScalingGroupName(self):
        return self._AutoScalingGroupName

    @AutoScalingGroupName.setter
    def AutoScalingGroupName(self, AutoScalingGroupName):
        self._AutoScalingGroupName = AutoScalingGroupName

    @property
    def DefaultCooldown(self):
        return self._DefaultCooldown

    @DefaultCooldown.setter
    def DefaultCooldown(self, DefaultCooldown):
        self._DefaultCooldown = DefaultCooldown

    @property
    def DesiredCapacity(self):
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def TerminationPolicies(self):
        return self._TerminationPolicies

    @TerminationPolicies.setter
    def TerminationPolicies(self, TerminationPolicies):
        self._TerminationPolicies = TerminationPolicies

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RetryPolicy(self):
        return self._RetryPolicy

    @RetryPolicy.setter
    def RetryPolicy(self, RetryPolicy):
        self._RetryPolicy = RetryPolicy

    @property
    def ZonesCheckPolicy(self):
        return self._ZonesCheckPolicy

    @ZonesCheckPolicy.setter
    def ZonesCheckPolicy(self, ZonesCheckPolicy):
        self._ZonesCheckPolicy = ZonesCheckPolicy

    @property
    def ServiceSettings(self):
        return self._ServiceSettings

    @ServiceSettings.setter
    def ServiceSettings(self, ServiceSettings):
        self._ServiceSettings = ServiceSettings

    @property
    def Ipv6AddressCount(self):
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount

    @property
    def MultiZoneSubnetPolicy(self):
        return self._MultiZoneSubnetPolicy

    @MultiZoneSubnetPolicy.setter
    def MultiZoneSubnetPolicy(self, MultiZoneSubnetPolicy):
        self._MultiZoneSubnetPolicy = MultiZoneSubnetPolicy

    @property
    def HealthCheckType(self):
        return self._HealthCheckType

    @HealthCheckType.setter
    def HealthCheckType(self, HealthCheckType):
        self._HealthCheckType = HealthCheckType

    @property
    def LoadBalancerHealthCheckGracePeriod(self):
        return self._LoadBalancerHealthCheckGracePeriod

    @LoadBalancerHealthCheckGracePeriod.setter
    def LoadBalancerHealthCheckGracePeriod(self, LoadBalancerHealthCheckGracePeriod):
        self._LoadBalancerHealthCheckGracePeriod = LoadBalancerHealthCheckGracePeriod

    @property
    def InstanceAllocationPolicy(self):
        return self._InstanceAllocationPolicy

    @InstanceAllocationPolicy.setter
    def InstanceAllocationPolicy(self, InstanceAllocationPolicy):
        self._InstanceAllocationPolicy = InstanceAllocationPolicy

    @property
    def SpotMixedAllocationPolicy(self):
        return self._SpotMixedAllocationPolicy

    @SpotMixedAllocationPolicy.setter
    def SpotMixedAllocationPolicy(self, SpotMixedAllocationPolicy):
        self._SpotMixedAllocationPolicy = SpotMixedAllocationPolicy

    @property
    def CapacityRebalance(self):
        return self._CapacityRebalance

    @CapacityRebalance.setter
    def CapacityRebalance(self, CapacityRebalance):
        self._CapacityRebalance = CapacityRebalance


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._AutoScalingGroupName = params.get("AutoScalingGroupName")
        self._DefaultCooldown = params.get("DefaultCooldown")
        self._DesiredCapacity = params.get("DesiredCapacity")
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._MaxSize = params.get("MaxSize")
        self._MinSize = params.get("MinSize")
        self._ProjectId = params.get("ProjectId")
        self._SubnetIds = params.get("SubnetIds")
        self._TerminationPolicies = params.get("TerminationPolicies")
        self._VpcId = params.get("VpcId")
        self._Zones = params.get("Zones")
        self._RetryPolicy = params.get("RetryPolicy")
        self._ZonesCheckPolicy = params.get("ZonesCheckPolicy")
        if params.get("ServiceSettings") is not None:
            self._ServiceSettings = ServiceSettings()
            self._ServiceSettings._deserialize(params.get("ServiceSettings"))
        self._Ipv6AddressCount = params.get("Ipv6AddressCount")
        self._MultiZoneSubnetPolicy = params.get("MultiZoneSubnetPolicy")
        self._HealthCheckType = params.get("HealthCheckType")
        self._LoadBalancerHealthCheckGracePeriod = params.get("LoadBalancerHealthCheckGracePeriod")
        self._InstanceAllocationPolicy = params.get("InstanceAllocationPolicy")
        if params.get("SpotMixedAllocationPolicy") is not None:
            self._SpotMixedAllocationPolicy = SpotMixedAllocationPolicy()
            self._SpotMixedAllocationPolicy._deserialize(params.get("SpotMixedAllocationPolicy"))
        self._CapacityRebalance = params.get("CapacityRebalance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoScalingGroupResponse(AbstractModel):
    """ModifyAutoScalingGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDesiredCapacityRequest(AbstractModel):
    """ModifyDesiredCapacity request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param _DesiredCapacity: Desired capacity
        :type DesiredCapacity: int
        :param _MinSize: Minimum number of instances. Value range: 0-2000.
        :type MinSize: int
        :param _MaxSize: Maximum number of instances. Value range: 0-2000.
        :type MaxSize: int
        """
        self._AutoScalingGroupId = None
        self._DesiredCapacity = None
        self._MinSize = None
        self._MaxSize = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def DesiredCapacity(self):
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._DesiredCapacity = params.get("DesiredCapacity")
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDesiredCapacityResponse(AbstractModel):
    """ModifyDesiredCapacity response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyLaunchConfigurationAttributesRequest(AbstractModel):
    """ModifyLaunchConfigurationAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _LaunchConfigurationId: Launch configuration ID
        :type LaunchConfigurationId: str
        :param _ImageId: [Image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are three types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><br/>You can obtain the image IDs in the [CVM console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE).</li><li>You can also use the [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response.</li>
        :type ImageId: str
        :param _InstanceTypes: List of instance types. Each type specifies different resource specifications. This list contains up to 10 instance types.
The launch configuration uses `InstanceType` to indicate one single instance type and `InstanceTypes` to indicate multiple instance types. Specifying the `InstanceTypes` field will invalidate the original `InstanceType`.
        :type InstanceTypes: list of str
        :param _InstanceTypesCheckPolicy: Instance type verification policy which works when InstanceTypes is actually modified. Value range: ALL, ANY. Default value: ANY.
<br><li> ALL: The verification will success only if all instance types (InstanceType) are available; otherwise, an error will be reported.
<br><li> ANY: The verification will success if any instance type (InstanceType) is available; otherwise, an error will be reported.

Common reasons why an instance type is unavailable include stock-out of the instance type or the corresponding cloud disk.
If a model in InstanceTypes does not exist or has been discontinued, a verification error will be reported regardless of the value of InstanceTypesCheckPolicy.
        :type InstanceTypesCheckPolicy: str
        :param _LaunchConfigurationName: Display name of the launch configuration, which can contain Chinese characters, letters, numbers, underscores, separators ("-"), and decimal points with a maximum length of 60 bytes.
        :type LaunchConfigurationName: str
        :param _UserData: Base64-encoded custom data of up to 16 KB. If you want to clear `UserData`, set it to an empty string.
        :type UserData: str
        :param _SecurityGroupIds: Security group to which the instance belongs. This parameter can be obtained from the `SecurityGroupId` field in the response of the [`DescribeSecurityGroups`](https://intl.cloud.tencent.com/document/api/215/15808?from_cn_redirect=1) API.
At least one security group is required for this parameter. The security group specified is sequential.
        :type SecurityGroupIds: list of str
        :param _InternetAccessible: Information of the public network bandwidth configuration.
When the public outbound network bandwidth is 0 Mbps, assigning a public IP is not allowed. Accordingly, if a public IP is assigned, the new public network outbound bandwidth must be greater than 0 Mbps.
        :type InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        :param _InstanceChargeType: Instance billing mode. Valid values:
<br><li>POSTPAID_BY_HOUR: pay-as-you-go hourly
<br><li>SPOTPAID: spot instance
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: Parameter setting for the prepaid mode (monthly subscription mode). This parameter can specify the renewal period, whether to set the auto-renewal, and other attributes of the monthly-subscribed instances.
This parameter is required when changing the instance billing mode to monthly subscription. It will be automatically discarded after you choose another billing mode.
This field requires passing in the `Period` field. Other fields that are not passed in will use their default values.
This field can be modified only when the current billing mode is monthly subscription.
        :type InstanceChargePrepaid: :class:`tencentcloud.autoscaling.v20180419.models.InstanceChargePrepaid`
        :param _InstanceMarketOptions: Market-related options for instances, such as parameters related to spot instances.
This parameter is required when changing the instance billing mode to spot instance. It will be automatically discarded after you choose another instance billing mode.
This field requires passing in the `MaxPrice` field under the `SpotOptions`. Other fields that are not passed in will use their default values.
This field can be modified only when the current billing mode is spot instance.
        :type InstanceMarketOptions: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        :param _DiskTypePolicy: Selection policy of cloud disks. Default value: ORIGINAL. Valid values:
<br><li>ORIGINAL: uses the configured cloud disk type
<br><li>AUTOMATIC: automatically chooses an available cloud disk type
        :type DiskTypePolicy: str
        :param _SystemDisk: Instance system disk configurations
        :type SystemDisk: :class:`tencentcloud.autoscaling.v20180419.models.SystemDisk`
        :param _DataDisks: Configuration information of instance data disks.
Up to 11 data disks can be specified and will be collectively modified. Please provide all the new values for the modification.
The default data disk should be the same as the system disk.
        :type DataDisks: list of DataDisk
        :param _HostNameSettings: CVM hostname settings.
This field is not supported for Windows instances.
This field requires passing the `HostName` field. Other fields that are not passed in will use their default values.
        :type HostNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.HostNameSettings`
        :param _InstanceNameSettings: Settings of CVM instance names. 
If this field is configured in a launch configuration, the `InstanceName` of a CVM created by the scaling group will be generated according to the configuration; otherwise, it will be in the `as-{{AutoScalingGroupName }}` format.
This field requires passing in the `InstanceName` field. Other fields that are not passed in will use their default values.
        :type InstanceNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameSettings`
        :param _EnhancedService: Specifies whether to enable additional services, such as security services and monitoring service.
        :type EnhancedService: :class:`tencentcloud.autoscaling.v20180419.models.EnhancedService`
        :param _CamRoleName: CAM role name. This parameter can be obtained from the `roleName` field returned by DescribeRoleList API.
        :type CamRoleName: str
        :param _HpcClusterId: HPC ID<br>
Note: This field is default to empty
        :type HpcClusterId: str
        :param _IPv6InternetAccessible: IPv6 public network bandwidth configuration. If the IPv6 address is available in the new instance, public network bandwidth can be allocated to the IPv6 address. This parameter is invalid if `Ipv6AddressCount` of the scaling group associated with the launch configuration is 0.
        :type IPv6InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.IPv6InternetAccessible`
        :param _DisasterRecoverGroupIds: Placement group ID. Only one is allowed.
        :type DisasterRecoverGroupIds: list of str
        """
        self._LaunchConfigurationId = None
        self._ImageId = None
        self._InstanceTypes = None
        self._InstanceTypesCheckPolicy = None
        self._LaunchConfigurationName = None
        self._UserData = None
        self._SecurityGroupIds = None
        self._InternetAccessible = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._InstanceMarketOptions = None
        self._DiskTypePolicy = None
        self._SystemDisk = None
        self._DataDisks = None
        self._HostNameSettings = None
        self._InstanceNameSettings = None
        self._EnhancedService = None
        self._CamRoleName = None
        self._HpcClusterId = None
        self._IPv6InternetAccessible = None
        self._DisasterRecoverGroupIds = None

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def InstanceTypesCheckPolicy(self):
        return self._InstanceTypesCheckPolicy

    @InstanceTypesCheckPolicy.setter
    def InstanceTypesCheckPolicy(self, InstanceTypesCheckPolicy):
        self._InstanceTypesCheckPolicy = InstanceTypesCheckPolicy

    @property
    def LaunchConfigurationName(self):
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def DiskTypePolicy(self):
        return self._DiskTypePolicy

    @DiskTypePolicy.setter
    def DiskTypePolicy(self, DiskTypePolicy):
        self._DiskTypePolicy = DiskTypePolicy

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def HostNameSettings(self):
        return self._HostNameSettings

    @HostNameSettings.setter
    def HostNameSettings(self, HostNameSettings):
        self._HostNameSettings = HostNameSettings

    @property
    def InstanceNameSettings(self):
        return self._InstanceNameSettings

    @InstanceNameSettings.setter
    def InstanceNameSettings(self, InstanceNameSettings):
        self._InstanceNameSettings = InstanceNameSettings

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def IPv6InternetAccessible(self):
        return self._IPv6InternetAccessible

    @IPv6InternetAccessible.setter
    def IPv6InternetAccessible(self, IPv6InternetAccessible):
        self._IPv6InternetAccessible = IPv6InternetAccessible

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds


    def _deserialize(self, params):
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._ImageId = params.get("ImageId")
        self._InstanceTypes = params.get("InstanceTypes")
        self._InstanceTypesCheckPolicy = params.get("InstanceTypesCheckPolicy")
        self._LaunchConfigurationName = params.get("LaunchConfigurationName")
        self._UserData = params.get("UserData")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._DiskTypePolicy = params.get("DiskTypePolicy")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("HostNameSettings") is not None:
            self._HostNameSettings = HostNameSettings()
            self._HostNameSettings._deserialize(params.get("HostNameSettings"))
        if params.get("InstanceNameSettings") is not None:
            self._InstanceNameSettings = InstanceNameSettings()
            self._InstanceNameSettings._deserialize(params.get("InstanceNameSettings"))
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._CamRoleName = params.get("CamRoleName")
        self._HpcClusterId = params.get("HpcClusterId")
        if params.get("IPv6InternetAccessible") is not None:
            self._IPv6InternetAccessible = IPv6InternetAccessible()
            self._IPv6InternetAccessible._deserialize(params.get("IPv6InternetAccessible"))
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLaunchConfigurationAttributesResponse(AbstractModel):
    """ModifyLaunchConfigurationAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyLifecycleHookRequest(AbstractModel):
    """ModifyLifecycleHook request structure.

    """

    def __init__(self):
        r"""
        :param _LifecycleHookId: Lifecycle hook ID.
        :type LifecycleHookId: str
        :param _LifecycleHookName: Lifecycle hook name.
        :type LifecycleHookName: str
        :param _LifecycleTransition: The time when the lifecycle hook is applied. Valid values:
<li> `INSTANCE_LAUNCHING`: After the instance launch
<li> `INSTANCE_TERMINATING`: Before the instance termination
        :type LifecycleTransition: str
        :param _DefaultResult: Actions after the lifecycle hook times out. Valid values:
<li> `CONTINUE`: Continue the scaling activity after the timeout
<li> `ABANDON`: Terminate the scaling activity after the timeout
        :type DefaultResult: str
        :param _HeartbeatTimeout: The maximum length of time (in seconds) that can elapse before the lifecycle hook times out. Value range: 30 - 7,200 seconds.
        :type HeartbeatTimeout: int
        :param _NotificationMetadata: Additional information sent by AS to the notification target.
        :type NotificationMetadata: str
        :param _LifecycleTransitionType: The scenario where the lifecycle hook is applied. `EXTENSION`: The lifecycle hook will be triggered when `AttachInstances`, `DetachInstances` or `RemoveInstances` is called. `NORMAL`: The lifecycle hook is not triggered by the above APIs.
        :type LifecycleTransitionType: str
        :param _NotificationTarget: Information of the notification target.
        :type NotificationTarget: :class:`tencentcloud.autoscaling.v20180419.models.NotificationTarget`
        :param _LifecycleCommand: Remote command execution object.
        :type LifecycleCommand: :class:`tencentcloud.autoscaling.v20180419.models.LifecycleCommand`
        """
        self._LifecycleHookId = None
        self._LifecycleHookName = None
        self._LifecycleTransition = None
        self._DefaultResult = None
        self._HeartbeatTimeout = None
        self._NotificationMetadata = None
        self._LifecycleTransitionType = None
        self._NotificationTarget = None
        self._LifecycleCommand = None

    @property
    def LifecycleHookId(self):
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def LifecycleHookName(self):
        return self._LifecycleHookName

    @LifecycleHookName.setter
    def LifecycleHookName(self, LifecycleHookName):
        self._LifecycleHookName = LifecycleHookName

    @property
    def LifecycleTransition(self):
        return self._LifecycleTransition

    @LifecycleTransition.setter
    def LifecycleTransition(self, LifecycleTransition):
        self._LifecycleTransition = LifecycleTransition

    @property
    def DefaultResult(self):
        return self._DefaultResult

    @DefaultResult.setter
    def DefaultResult(self, DefaultResult):
        self._DefaultResult = DefaultResult

    @property
    def HeartbeatTimeout(self):
        return self._HeartbeatTimeout

    @HeartbeatTimeout.setter
    def HeartbeatTimeout(self, HeartbeatTimeout):
        self._HeartbeatTimeout = HeartbeatTimeout

    @property
    def NotificationMetadata(self):
        return self._NotificationMetadata

    @NotificationMetadata.setter
    def NotificationMetadata(self, NotificationMetadata):
        self._NotificationMetadata = NotificationMetadata

    @property
    def LifecycleTransitionType(self):
        return self._LifecycleTransitionType

    @LifecycleTransitionType.setter
    def LifecycleTransitionType(self, LifecycleTransitionType):
        self._LifecycleTransitionType = LifecycleTransitionType

    @property
    def NotificationTarget(self):
        return self._NotificationTarget

    @NotificationTarget.setter
    def NotificationTarget(self, NotificationTarget):
        self._NotificationTarget = NotificationTarget

    @property
    def LifecycleCommand(self):
        return self._LifecycleCommand

    @LifecycleCommand.setter
    def LifecycleCommand(self, LifecycleCommand):
        self._LifecycleCommand = LifecycleCommand


    def _deserialize(self, params):
        self._LifecycleHookId = params.get("LifecycleHookId")
        self._LifecycleHookName = params.get("LifecycleHookName")
        self._LifecycleTransition = params.get("LifecycleTransition")
        self._DefaultResult = params.get("DefaultResult")
        self._HeartbeatTimeout = params.get("HeartbeatTimeout")
        self._NotificationMetadata = params.get("NotificationMetadata")
        self._LifecycleTransitionType = params.get("LifecycleTransitionType")
        if params.get("NotificationTarget") is not None:
            self._NotificationTarget = NotificationTarget()
            self._NotificationTarget._deserialize(params.get("NotificationTarget"))
        if params.get("LifecycleCommand") is not None:
            self._LifecycleCommand = LifecycleCommand()
            self._LifecycleCommand._deserialize(params.get("LifecycleCommand"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLifecycleHookResponse(AbstractModel):
    """ModifyLifecycleHook response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyLoadBalancerTargetAttributesRequest(AbstractModel):
    """ModifyLoadBalancerTargetAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Scaling group ID
        :type AutoScalingGroupId: str
        :param _ForwardLoadBalancers: List of application CLBs to modify. Up to 100 CLBs allowed.
        :type ForwardLoadBalancers: list of ForwardLoadBalancer
        """
        self._AutoScalingGroupId = None
        self._ForwardLoadBalancers = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ForwardLoadBalancers(self):
        return self._ForwardLoadBalancers

    @ForwardLoadBalancers.setter
    def ForwardLoadBalancers(self, ForwardLoadBalancers):
        self._ForwardLoadBalancers = ForwardLoadBalancers


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        if params.get("ForwardLoadBalancers") is not None:
            self._ForwardLoadBalancers = []
            for item in params.get("ForwardLoadBalancers"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self._ForwardLoadBalancers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerTargetAttributesResponse(AbstractModel):
    """ModifyLoadBalancerTargetAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _ActivityId: Scaling activity ID
        :type ActivityId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class ModifyLoadBalancersRequest(AbstractModel):
    """ModifyLoadBalancers request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param _LoadBalancerIds: List of classic CLB IDs. Currently, the maximum length is 20. You cannot specify LoadBalancerIds and ForwardLoadBalancers at the same time.
        :type LoadBalancerIds: list of str
        :param _ForwardLoadBalancers: List of application CLBs. Up to 100 CLBs are allowed. `LoadBalancerIds` and `ForwardLoadBalancers` cannot be specified at the same time.
        :type ForwardLoadBalancers: list of ForwardLoadBalancer
        :param _LoadBalancersCheckPolicy: CLB verification policy. Valid values: "ALL" and "DIFF". Default value: "ALL"
<br><li> ALL. Verification is successful only when all CLBs are valid. Otherwise, verification fails.
<br><li> DIFF. Only the changes in the CLB parameters are verified. If valid, the verification is successful. Otherwise, verification fails.
        :type LoadBalancersCheckPolicy: str
        """
        self._AutoScalingGroupId = None
        self._LoadBalancerIds = None
        self._ForwardLoadBalancers = None
        self._LoadBalancersCheckPolicy = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ForwardLoadBalancers(self):
        return self._ForwardLoadBalancers

    @ForwardLoadBalancers.setter
    def ForwardLoadBalancers(self, ForwardLoadBalancers):
        self._ForwardLoadBalancers = ForwardLoadBalancers

    @property
    def LoadBalancersCheckPolicy(self):
        return self._LoadBalancersCheckPolicy

    @LoadBalancersCheckPolicy.setter
    def LoadBalancersCheckPolicy(self, LoadBalancersCheckPolicy):
        self._LoadBalancersCheckPolicy = LoadBalancersCheckPolicy


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        if params.get("ForwardLoadBalancers") is not None:
            self._ForwardLoadBalancers = []
            for item in params.get("ForwardLoadBalancers"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self._ForwardLoadBalancers.append(obj)
        self._LoadBalancersCheckPolicy = params.get("LoadBalancersCheckPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancersResponse(AbstractModel):
    """ModifyLoadBalancers response structure.

    """

    def __init__(self):
        r"""
        :param _ActivityId: Scaling activity ID
        :type ActivityId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class ModifyNotificationConfigurationRequest(AbstractModel):
    """ModifyNotificationConfiguration request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingNotificationId: ID of the notification to be modified.
        :type AutoScalingNotificationId: str
        :param _NotificationTypes: Notification type, i.e., the set of types of notifications to be subscribed to. Value range:
<li>SCALE_OUT_SUCCESSFUL: scale-out succeeded</li>
<li>SCALE_OUT_FAILED: scale-out failed</li>
<li>SCALE_IN_SUCCESSFUL: scale-in succeeded</li>
<li>SCALE_IN_FAILED: scale-in failed</li>
<li>REPLACE_UNHEALTHY_INSTANCE_SUCCESSFUL: unhealthy instance replacement succeeded</li>
<li>REPLACE_UNHEALTHY_INSTANCE_FAILED: unhealthy instance replacement failed</li>
        :type NotificationTypes: list of str
        :param _NotificationUserGroupIds: Notification group ID, which is the set of user group IDs. You can query the user group IDs through the [ListGroups](https://intl.cloud.tencent.com/document/product/598/34589?from_cn_redirect=1) API.
        :type NotificationUserGroupIds: list of str
        :param _QueueName: CMQ or TDMQ CMQ queue name.
        :type QueueName: str
        :param _TopicName: CMQ or TDMQ CMQ toipc name.
        :type TopicName: str
        """
        self._AutoScalingNotificationId = None
        self._NotificationTypes = None
        self._NotificationUserGroupIds = None
        self._QueueName = None
        self._TopicName = None

    @property
    def AutoScalingNotificationId(self):
        return self._AutoScalingNotificationId

    @AutoScalingNotificationId.setter
    def AutoScalingNotificationId(self, AutoScalingNotificationId):
        self._AutoScalingNotificationId = AutoScalingNotificationId

    @property
    def NotificationTypes(self):
        return self._NotificationTypes

    @NotificationTypes.setter
    def NotificationTypes(self, NotificationTypes):
        self._NotificationTypes = NotificationTypes

    @property
    def NotificationUserGroupIds(self):
        return self._NotificationUserGroupIds

    @NotificationUserGroupIds.setter
    def NotificationUserGroupIds(self, NotificationUserGroupIds):
        self._NotificationUserGroupIds = NotificationUserGroupIds

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._AutoScalingNotificationId = params.get("AutoScalingNotificationId")
        self._NotificationTypes = params.get("NotificationTypes")
        self._NotificationUserGroupIds = params.get("NotificationUserGroupIds")
        self._QueueName = params.get("QueueName")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNotificationConfigurationResponse(AbstractModel):
    """ModifyNotificationConfiguration response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyScalingPolicyRequest(AbstractModel):
    """ModifyScalingPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingPolicyId: Alarm policy ID.
        :type AutoScalingPolicyId: str
        :param _ScalingPolicyName: Alarm policy name.
        :type ScalingPolicyName: str
        :param _AdjustmentType: The method to adjust the desired capacity after the alarm is triggered. It’s only available when `ScalingPolicyType` is `Simple`. Valid values: <br><li>`CHANGE_IN_CAPACITY`: Increase or decrease the desired capacity </li><li>`EXACT_CAPACITY`: Adjust to the specified desired capacity </li> <li>`PERCENT_CHANGE_IN_CAPACITY`: Adjust the desired capacity by percentage </li>
        :type AdjustmentType: str
        :param _AdjustmentValue: Specifies how to adjust the number of desired capacity when the alarm is triggered. It’s only available when `ScalingPolicyType` is `Simple`. Values: <br><li>`AdjustmentType`=`CHANGE_IN_CAPACITY`: Number of instances to add (positive number) or remove (negative number). </li> <li>`AdjustmentType`=`EXACT_CAPACITY`: Set the desired capacity to the specified number. It must be ≥ 0. </li> <li>`AdjustmentType`=`PERCENT_CHANGE_IN_CAPACITY`: Percentage of instance number. Add instances (positive value) or remove instances (negative value) accordingly.
        :type AdjustmentValue: int
        :param _Cooldown: Cooldown period (in seconds). It’s only available when `ScalingPolicyType` is `Simple`.
        :type Cooldown: int
        :param _MetricAlarm: Alarm monitoring metric. It’s only available when `ScalingPolicyType` is `Simple`.
        :type MetricAlarm: :class:`tencentcloud.autoscaling.v20180419.models.MetricAlarm`
        :param _PredefinedMetricType: Preset monitoring item. It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Valid values: <br><li>ASG_AVG_CPU_UTILIZATION: Average CPU utilization</li><li>ASG_AVG_LAN_TRAFFIC_OUT: Average private bandwidth out</li><li>ASG_AVG_LAN_TRAFFIC_IN: Average private bandwidth in</li><li>ASG_AVG_WAN_TRAFFIC_OUT: Average public bandwidth out</li><li>ASG_AVG_WAN_TRAFFIC_IN: Average public bandwidth in</li>
        :type PredefinedMetricType: str
        :param _TargetValue: Target value. It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Value ranges: <br><li>`ASG_AVG_CPU_UTILIZATION` (in %): [1, 100)</li><li>`ASG_AVG_LAN_TRAFFIC_OUT` (in Mbps): >0</li><li>`ASG_AVG_LAN_TRAFFIC_IN` (in Mbps): >0</li><li>`ASG_AVG_WAN_TRAFFIC_OUT` (in Mbps): >0</li><li>`ASG_AVG_WAN_TRAFFIC_IN` (in Mbps): >0</li>
        :type TargetValue: int
        :param _EstimatedInstanceWarmup: Instance warm-up period (in seconds). It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Value range: 0-3600.
        :type EstimatedInstanceWarmup: int
        :param _DisableScaleIn: Whether to disable scale-in. It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Valid values: <br><li>`true`: Scaling in is not allowed.</li><li>`false`: Allows both scale-out and scale-in</li>
        :type DisableScaleIn: bool
        :param _NotificationUserGroupIds: This parameter is diused. Please use [CreateNotificationConfiguration](https://intl.cloud.tencent.com/document/api/377/33185?from_cn_redirect=1) instead.
Notification group ID, which is the set of user group IDs.
        :type NotificationUserGroupIds: list of str
        """
        self._AutoScalingPolicyId = None
        self._ScalingPolicyName = None
        self._AdjustmentType = None
        self._AdjustmentValue = None
        self._Cooldown = None
        self._MetricAlarm = None
        self._PredefinedMetricType = None
        self._TargetValue = None
        self._EstimatedInstanceWarmup = None
        self._DisableScaleIn = None
        self._NotificationUserGroupIds = None

    @property
    def AutoScalingPolicyId(self):
        return self._AutoScalingPolicyId

    @AutoScalingPolicyId.setter
    def AutoScalingPolicyId(self, AutoScalingPolicyId):
        self._AutoScalingPolicyId = AutoScalingPolicyId

    @property
    def ScalingPolicyName(self):
        return self._ScalingPolicyName

    @ScalingPolicyName.setter
    def ScalingPolicyName(self, ScalingPolicyName):
        self._ScalingPolicyName = ScalingPolicyName

    @property
    def AdjustmentType(self):
        return self._AdjustmentType

    @AdjustmentType.setter
    def AdjustmentType(self, AdjustmentType):
        self._AdjustmentType = AdjustmentType

    @property
    def AdjustmentValue(self):
        return self._AdjustmentValue

    @AdjustmentValue.setter
    def AdjustmentValue(self, AdjustmentValue):
        self._AdjustmentValue = AdjustmentValue

    @property
    def Cooldown(self):
        return self._Cooldown

    @Cooldown.setter
    def Cooldown(self, Cooldown):
        self._Cooldown = Cooldown

    @property
    def MetricAlarm(self):
        return self._MetricAlarm

    @MetricAlarm.setter
    def MetricAlarm(self, MetricAlarm):
        self._MetricAlarm = MetricAlarm

    @property
    def PredefinedMetricType(self):
        return self._PredefinedMetricType

    @PredefinedMetricType.setter
    def PredefinedMetricType(self, PredefinedMetricType):
        self._PredefinedMetricType = PredefinedMetricType

    @property
    def TargetValue(self):
        return self._TargetValue

    @TargetValue.setter
    def TargetValue(self, TargetValue):
        self._TargetValue = TargetValue

    @property
    def EstimatedInstanceWarmup(self):
        return self._EstimatedInstanceWarmup

    @EstimatedInstanceWarmup.setter
    def EstimatedInstanceWarmup(self, EstimatedInstanceWarmup):
        self._EstimatedInstanceWarmup = EstimatedInstanceWarmup

    @property
    def DisableScaleIn(self):
        return self._DisableScaleIn

    @DisableScaleIn.setter
    def DisableScaleIn(self, DisableScaleIn):
        self._DisableScaleIn = DisableScaleIn

    @property
    def NotificationUserGroupIds(self):
        return self._NotificationUserGroupIds

    @NotificationUserGroupIds.setter
    def NotificationUserGroupIds(self, NotificationUserGroupIds):
        self._NotificationUserGroupIds = NotificationUserGroupIds


    def _deserialize(self, params):
        self._AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        self._ScalingPolicyName = params.get("ScalingPolicyName")
        self._AdjustmentType = params.get("AdjustmentType")
        self._AdjustmentValue = params.get("AdjustmentValue")
        self._Cooldown = params.get("Cooldown")
        if params.get("MetricAlarm") is not None:
            self._MetricAlarm = MetricAlarm()
            self._MetricAlarm._deserialize(params.get("MetricAlarm"))
        self._PredefinedMetricType = params.get("PredefinedMetricType")
        self._TargetValue = params.get("TargetValue")
        self._EstimatedInstanceWarmup = params.get("EstimatedInstanceWarmup")
        self._DisableScaleIn = params.get("DisableScaleIn")
        self._NotificationUserGroupIds = params.get("NotificationUserGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyScalingPolicyResponse(AbstractModel):
    """ModifyScalingPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyScheduledActionRequest(AbstractModel):
    """ModifyScheduledAction request structure.

    """

    def __init__(self):
        r"""
        :param _ScheduledActionId: ID of the scheduled task to be edited
        :type ScheduledActionId: str
        :param _ScheduledActionName: Scheduled task name, which can only contain letters, numbers, underscores, hyphens ("-"), and decimal points with a maximum length of 60 bytes and must be unique in an auto scaling group.
        :type ScheduledActionName: str
        :param _MaxSize: The maximum number of instances set for the auto scaling group when the scheduled task is triggered.
        :type MaxSize: int
        :param _MinSize: The minimum number of instances set for the auto scaling group when the scheduled task is triggered.
        :type MinSize: int
        :param _DesiredCapacity: The desired number of instances set for the auto scaling group when the scheduled task is triggered.
        :type DesiredCapacity: int
        :param _StartTime: Initial triggered time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard.
        :type StartTime: str
        :param _EndTime: End time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard. <br>This parameter and `Recurrence` need to be specified at the same time. After the end time, the scheduled task will no longer take effect.
        :type EndTime: str
        :param _Recurrence: Repeating mode of the scheduled task, which is in standard cron format. <br>This parameter and `EndTime` need to be specified at the same time.
        :type Recurrence: str
        """
        self._ScheduledActionId = None
        self._ScheduledActionName = None
        self._MaxSize = None
        self._MinSize = None
        self._DesiredCapacity = None
        self._StartTime = None
        self._EndTime = None
        self._Recurrence = None

    @property
    def ScheduledActionId(self):
        return self._ScheduledActionId

    @ScheduledActionId.setter
    def ScheduledActionId(self, ScheduledActionId):
        self._ScheduledActionId = ScheduledActionId

    @property
    def ScheduledActionName(self):
        return self._ScheduledActionName

    @ScheduledActionName.setter
    def ScheduledActionName(self, ScheduledActionName):
        self._ScheduledActionName = ScheduledActionName

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def DesiredCapacity(self):
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Recurrence(self):
        return self._Recurrence

    @Recurrence.setter
    def Recurrence(self, Recurrence):
        self._Recurrence = Recurrence


    def _deserialize(self, params):
        self._ScheduledActionId = params.get("ScheduledActionId")
        self._ScheduledActionName = params.get("ScheduledActionName")
        self._MaxSize = params.get("MaxSize")
        self._MinSize = params.get("MinSize")
        self._DesiredCapacity = params.get("DesiredCapacity")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Recurrence = params.get("Recurrence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyScheduledActionResponse(AbstractModel):
    """ModifyScheduledAction response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class NotificationTarget(AbstractModel):
    """Notification target

    """

    def __init__(self):
        r"""
        :param _TargetType: Target type. Valid values: `CMQ_QUEUE`, `CMQ_TOPIC`, `TDMQ_CMQ_QUEUE` and `TDMQ_CMQ_TOPIC`.
<li> CMQ_QUEUE: Tencent Cloud message queue - queue model.</li>
<li> CMQ_TOPIC: Tencent Cloud message queue - topic model.</li>
<li> TDMQ_CMQ_QUEUE: Tencent Cloud TDMQ message queue - queue model.</li>
<li> TDMQ_CMQ_TOPIC: Tencent Cloud TDMQ message queue - topic model.</li>
        :type TargetType: str
        :param _QueueName: Queue name. This parameter is required when `TargetType` is `CMQ_QUEUE` or `TDMQ_CMQ_QUEUE`.
        :type QueueName: str
        :param _TopicName: Topic name. This parameter is required when `TargetType` is `CMQ_TOPIC` or `TDMQ_CMQ_TOPIC`.
        :type TopicName: str
        """
        self._TargetType = None
        self._QueueName = None
        self._TopicName = None

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._TargetType = params.get("TargetType")
        self._QueueName = params.get("QueueName")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelatedInstance(AbstractModel):
    """Information of the instances related to the current scaling activity.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceStatus: Status of the instance in the scaling activity. Valid values:
`INIT`: Initializing
`RUNNING`: u200dProcessing u200dthe instance
`SUCCESSFUL`: Task succeeded on the instance
`FAILED`: Task failed on the instance
        :type InstanceStatus: str
        """
        self._InstanceId = None
        self._InstanceStatus = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceStatus = params.get("InstanceStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveInstancesRequest(AbstractModel):
    """RemoveInstances request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID
        :type AutoScalingGroupId: str
        :param _InstanceIds: List of CVM instance IDs
        :type InstanceIds: list of str
        """
        self._AutoScalingGroupId = None
        self._InstanceIds = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveInstancesResponse(AbstractModel):
    """RemoveInstances response structure.

    """

    def __init__(self):
        r"""
        :param _ActivityId: Scaling activity ID
        :type ActivityId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class RunAutomationServiceEnabled(AbstractModel):
    """Status of TAT service.

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether to enable [TencentCloud Automation Tools](https://intl.cloud.tencent.com/document/product/1340?from_cn_redirect=1). Valid values:<br><li>`TRUE`: Enable<br><li>`FALSE`: Not enable.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunMonitorServiceEnabled(AbstractModel):
    """This describes the information related to the Cloud Monitor service.

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether to enable the [Cloud Monitor](https://intl.cloud.tencent.com/document/product/248?from_cn_redirect=1) service. Value range: <br><li>TRUE: Cloud Monitor is enabled <br><li>FALSE: Cloud Monitor is disabled <br><br>Default value: TRUE. |
Note: This field may return null, indicating that no valid values can be obtained.
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSecurityServiceEnabled(AbstractModel):
    """This describes the information on the Cloud Security service

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether to enable the [Cloud Security](https://intl.cloud.tencent.com/document/product/296?from_cn_redirect=1) service. Value range: <br><li>TRUE: Cloud Security is enabled <br><li>FALSE: Cloud Security is disabled <br><br>Default value: TRUE.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleInInstancesRequest(AbstractModel):
    """ScaleInInstances request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Scaling group ID
        :type AutoScalingGroupId: str
        :param _ScaleInNumber: Number of instances to be reduced
        :type ScaleInNumber: int
        """
        self._AutoScalingGroupId = None
        self._ScaleInNumber = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ScaleInNumber(self):
        return self._ScaleInNumber

    @ScaleInNumber.setter
    def ScaleInNumber(self, ScaleInNumber):
        self._ScaleInNumber = ScaleInNumber


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._ScaleInNumber = params.get("ScaleInNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleInInstancesResponse(AbstractModel):
    """ScaleInInstances response structure.

    """

    def __init__(self):
        r"""
        :param _ActivityId: Scaling activity ID
        :type ActivityId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class ScaleOutInstancesRequest(AbstractModel):
    """ScaleOutInstances request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Scaling group ID
        :type AutoScalingGroupId: str
        :param _ScaleOutNumber: Number of instances to be added
        :type ScaleOutNumber: int
        """
        self._AutoScalingGroupId = None
        self._ScaleOutNumber = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ScaleOutNumber(self):
        return self._ScaleOutNumber

    @ScaleOutNumber.setter
    def ScaleOutNumber(self, ScaleOutNumber):
        self._ScaleOutNumber = ScaleOutNumber


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._ScaleOutNumber = params.get("ScaleOutNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutInstancesResponse(AbstractModel):
    """ScaleOutInstances response structure.

    """

    def __init__(self):
        r"""
        :param _ActivityId: Scaling activity ID
        :type ActivityId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class ScalingPolicy(AbstractModel):
    """Alarm trigger policy.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID.
        :type AutoScalingGroupId: str
        :param _AutoScalingPolicyId: Alarm trigger policy ID.
        :type AutoScalingPolicyId: str
        :param _ScalingPolicyType: Scaling policy type. Valid values:
- `SIMPLE`: A simple policy.
- `TARGET_TRACKING`: A target tracking policy.
        :type ScalingPolicyType: str
        :param _ScalingPolicyName: Alarm trigger policy name.
        :type ScalingPolicyName: str
        :param _AdjustmentType: The method to adjust the desired capacity after the alarm is triggered. It’s only available when `ScalingPolicyType` is `Simple`. Valid values: <br><li>`CHANGE_IN_CAPACITY`: Increase or decrease the desired capacity </li><li>`EXACT_CAPACITY`: Adjust to the specified desired capacity </li> <li>`PERCENT_CHANGE_IN_CAPACITY`: Adjust the desired capacity by percentage </li>
        :type AdjustmentType: str
        :param _AdjustmentValue: The adjusted value of desired capacity after the alarm is triggered. This parameter is only applicable to a simple policy.
        :type AdjustmentValue: int
        :param _Cooldown: Cooldown period. This parameter is only applicable to a simple policy.
        :type Cooldown: int
        :param _MetricAlarm: Alarm monitoring metrics of a simple policy.
        :type MetricAlarm: :class:`tencentcloud.autoscaling.v20180419.models.MetricAlarm`
        :param _PredefinedMetricType: Preset monitoring item. It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Valid values: <br><li>ASG_AVG_CPU_UTILIZATION: Average CPU utilization</li><li>ASG_AVG_LAN_TRAFFIC_OUT: Average private bandwidth out</li><li>ASG_AVG_LAN_TRAFFIC_IN: Average private bandwidth in</li><li>ASG_AVG_WAN_TRAFFIC_OUT: Average public bandwidth out</li><li>ASG_AVG_WAN_TRAFFIC_IN: Average public bandwidth in</li>
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PredefinedMetricType: str
        :param _TargetValue: Target value. It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Value ranges: <br><li>`ASG_AVG_CPU_UTILIZATION` (in %): [1, 100)</li><li>`ASG_AVG_LAN_TRAFFIC_OUT` (in Mbps): >0</li><li>`ASG_AVG_LAN_TRAFFIC_IN` (in Mbps): >0</li><li>`ASG_AVG_WAN_TRAFFIC_OUT` (in Mbps): >0</li><li>`ASG_AVG_WAN_TRAFFIC_IN` (in Mbps): >0</li>
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TargetValue: int
        :param _EstimatedInstanceWarmup: Instance warm-up period (in seconds). It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Value range: 0-3600.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EstimatedInstanceWarmup: int
        :param _DisableScaleIn: Whether to disable scale-in. It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Valid values: <br><li>`true`: Scaling in is not allowed.</li><li>`false`: Allows both scale-out and scale-in</li>
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DisableScaleIn: bool
        :param _MetricAlarms: List of alarm monitoring metrics. This parameter is only applicable to a target tracking policy.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type MetricAlarms: list of MetricAlarm
        :param _NotificationUserGroupIds: Notification group ID, which is the set of user group IDs.
        :type NotificationUserGroupIds: list of str
        """
        self._AutoScalingGroupId = None
        self._AutoScalingPolicyId = None
        self._ScalingPolicyType = None
        self._ScalingPolicyName = None
        self._AdjustmentType = None
        self._AdjustmentValue = None
        self._Cooldown = None
        self._MetricAlarm = None
        self._PredefinedMetricType = None
        self._TargetValue = None
        self._EstimatedInstanceWarmup = None
        self._DisableScaleIn = None
        self._MetricAlarms = None
        self._NotificationUserGroupIds = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def AutoScalingPolicyId(self):
        return self._AutoScalingPolicyId

    @AutoScalingPolicyId.setter
    def AutoScalingPolicyId(self, AutoScalingPolicyId):
        self._AutoScalingPolicyId = AutoScalingPolicyId

    @property
    def ScalingPolicyType(self):
        return self._ScalingPolicyType

    @ScalingPolicyType.setter
    def ScalingPolicyType(self, ScalingPolicyType):
        self._ScalingPolicyType = ScalingPolicyType

    @property
    def ScalingPolicyName(self):
        return self._ScalingPolicyName

    @ScalingPolicyName.setter
    def ScalingPolicyName(self, ScalingPolicyName):
        self._ScalingPolicyName = ScalingPolicyName

    @property
    def AdjustmentType(self):
        return self._AdjustmentType

    @AdjustmentType.setter
    def AdjustmentType(self, AdjustmentType):
        self._AdjustmentType = AdjustmentType

    @property
    def AdjustmentValue(self):
        return self._AdjustmentValue

    @AdjustmentValue.setter
    def AdjustmentValue(self, AdjustmentValue):
        self._AdjustmentValue = AdjustmentValue

    @property
    def Cooldown(self):
        return self._Cooldown

    @Cooldown.setter
    def Cooldown(self, Cooldown):
        self._Cooldown = Cooldown

    @property
    def MetricAlarm(self):
        return self._MetricAlarm

    @MetricAlarm.setter
    def MetricAlarm(self, MetricAlarm):
        self._MetricAlarm = MetricAlarm

    @property
    def PredefinedMetricType(self):
        return self._PredefinedMetricType

    @PredefinedMetricType.setter
    def PredefinedMetricType(self, PredefinedMetricType):
        self._PredefinedMetricType = PredefinedMetricType

    @property
    def TargetValue(self):
        return self._TargetValue

    @TargetValue.setter
    def TargetValue(self, TargetValue):
        self._TargetValue = TargetValue

    @property
    def EstimatedInstanceWarmup(self):
        return self._EstimatedInstanceWarmup

    @EstimatedInstanceWarmup.setter
    def EstimatedInstanceWarmup(self, EstimatedInstanceWarmup):
        self._EstimatedInstanceWarmup = EstimatedInstanceWarmup

    @property
    def DisableScaleIn(self):
        return self._DisableScaleIn

    @DisableScaleIn.setter
    def DisableScaleIn(self, DisableScaleIn):
        self._DisableScaleIn = DisableScaleIn

    @property
    def MetricAlarms(self):
        return self._MetricAlarms

    @MetricAlarms.setter
    def MetricAlarms(self, MetricAlarms):
        self._MetricAlarms = MetricAlarms

    @property
    def NotificationUserGroupIds(self):
        return self._NotificationUserGroupIds

    @NotificationUserGroupIds.setter
    def NotificationUserGroupIds(self, NotificationUserGroupIds):
        self._NotificationUserGroupIds = NotificationUserGroupIds


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        self._ScalingPolicyType = params.get("ScalingPolicyType")
        self._ScalingPolicyName = params.get("ScalingPolicyName")
        self._AdjustmentType = params.get("AdjustmentType")
        self._AdjustmentValue = params.get("AdjustmentValue")
        self._Cooldown = params.get("Cooldown")
        if params.get("MetricAlarm") is not None:
            self._MetricAlarm = MetricAlarm()
            self._MetricAlarm._deserialize(params.get("MetricAlarm"))
        self._PredefinedMetricType = params.get("PredefinedMetricType")
        self._TargetValue = params.get("TargetValue")
        self._EstimatedInstanceWarmup = params.get("EstimatedInstanceWarmup")
        self._DisableScaleIn = params.get("DisableScaleIn")
        if params.get("MetricAlarms") is not None:
            self._MetricAlarms = []
            for item in params.get("MetricAlarms"):
                obj = MetricAlarm()
                obj._deserialize(item)
                self._MetricAlarms.append(obj)
        self._NotificationUserGroupIds = params.get("NotificationUserGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduledAction(AbstractModel):
    """This describes the information of a scheduled task.

    """

    def __init__(self):
        r"""
        :param _ScheduledActionId: Scheduled task ID.
        :type ScheduledActionId: str
        :param _ScheduledActionName: Scheduled task name.
        :type ScheduledActionName: str
        :param _AutoScalingGroupId: ID of the auto scaling group where the scheduled task is located.
        :type AutoScalingGroupId: str
        :param _StartTime: Start time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard.
        :type StartTime: str
        :param _Recurrence: Repeating mode of the scheduled task.
        :type Recurrence: str
        :param _EndTime: End time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard.
        :type EndTime: str
        :param _MaxSize: Maximum number of instances set by the scheduled task.
        :type MaxSize: int
        :param _DesiredCapacity: Desired number of instances set by the scheduled task.
        :type DesiredCapacity: int
        :param _MinSize: Minimum number of instances set by the scheduled task.
        :type MinSize: int
        :param _CreatedTime: Creation time of the scheduled task. The value is in `UTC time` in the format of `YYYY-MM-DDThh:mm:ssZ` according to the `ISO8601` standard.
        :type CreatedTime: str
        :param _ScheduledType: Specifies how the scheduled action is executed. <br><li>`CRONTAB`: execute repeatedly <br><li>`ONCE`: execute only once
        :type ScheduledType: str
        """
        self._ScheduledActionId = None
        self._ScheduledActionName = None
        self._AutoScalingGroupId = None
        self._StartTime = None
        self._Recurrence = None
        self._EndTime = None
        self._MaxSize = None
        self._DesiredCapacity = None
        self._MinSize = None
        self._CreatedTime = None
        self._ScheduledType = None

    @property
    def ScheduledActionId(self):
        return self._ScheduledActionId

    @ScheduledActionId.setter
    def ScheduledActionId(self, ScheduledActionId):
        self._ScheduledActionId = ScheduledActionId

    @property
    def ScheduledActionName(self):
        return self._ScheduledActionName

    @ScheduledActionName.setter
    def ScheduledActionName(self, ScheduledActionName):
        self._ScheduledActionName = ScheduledActionName

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Recurrence(self):
        return self._Recurrence

    @Recurrence.setter
    def Recurrence(self, Recurrence):
        self._Recurrence = Recurrence

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def DesiredCapacity(self):
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ScheduledType(self):
        return self._ScheduledType

    @ScheduledType.setter
    def ScheduledType(self, ScheduledType):
        self._ScheduledType = ScheduledType


    def _deserialize(self, params):
        self._ScheduledActionId = params.get("ScheduledActionId")
        self._ScheduledActionName = params.get("ScheduledActionName")
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._StartTime = params.get("StartTime")
        self._Recurrence = params.get("Recurrence")
        self._EndTime = params.get("EndTime")
        self._MaxSize = params.get("MaxSize")
        self._DesiredCapacity = params.get("DesiredCapacity")
        self._MinSize = params.get("MinSize")
        self._CreatedTime = params.get("CreatedTime")
        self._ScheduledType = params.get("ScheduledType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceSettings(AbstractModel):
    """Service settings

    """

    def __init__(self):
        r"""
        :param _ReplaceMonitorUnhealthy: Enables unhealthy instance replacement. If this feature is enabled, AS will replace instances that are flagged as unhealthy by Cloud Monitor. If this parameter is not specified, the value will be False by default.
        :type ReplaceMonitorUnhealthy: bool
        :param _ScalingMode: Valid values: 
CLASSIC_SCALING: this is the typical scaling method, which creates and terminates instances to perform scaling operations. 
WAKE_UP_STOPPED_SCALING: this scaling method first tries to start stopped instances. If the number of instances woken up is insufficient, the system creates new instances for scale-out. For scale-in, instances are terminated as in the typical method. You can use the StopAutoScalingInstances API to stop instances in the scaling group. Scale-out operations triggered by alarms will still create new instances.
Default value: CLASSIC_SCALING
        :type ScalingMode: str
        :param _ReplaceLoadBalancerUnhealthy: Enable unhealthy instance replacement. If this feature is enabled, AS will replace instances that are found unhealthy in the CLB health check. If this parameter is not specified, the default value `False` will be used.
        :type ReplaceLoadBalancerUnhealthy: bool
        """
        self._ReplaceMonitorUnhealthy = None
        self._ScalingMode = None
        self._ReplaceLoadBalancerUnhealthy = None

    @property
    def ReplaceMonitorUnhealthy(self):
        return self._ReplaceMonitorUnhealthy

    @ReplaceMonitorUnhealthy.setter
    def ReplaceMonitorUnhealthy(self, ReplaceMonitorUnhealthy):
        self._ReplaceMonitorUnhealthy = ReplaceMonitorUnhealthy

    @property
    def ScalingMode(self):
        return self._ScalingMode

    @ScalingMode.setter
    def ScalingMode(self, ScalingMode):
        self._ScalingMode = ScalingMode

    @property
    def ReplaceLoadBalancerUnhealthy(self):
        return self._ReplaceLoadBalancerUnhealthy

    @ReplaceLoadBalancerUnhealthy.setter
    def ReplaceLoadBalancerUnhealthy(self, ReplaceLoadBalancerUnhealthy):
        self._ReplaceLoadBalancerUnhealthy = ReplaceLoadBalancerUnhealthy


    def _deserialize(self, params):
        self._ReplaceMonitorUnhealthy = params.get("ReplaceMonitorUnhealthy")
        self._ScalingMode = params.get("ScalingMode")
        self._ReplaceLoadBalancerUnhealthy = params.get("ReplaceLoadBalancerUnhealthy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetInstancesProtectionRequest(AbstractModel):
    """SetInstancesProtection request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Auto scaling group ID.
        :type AutoScalingGroupId: str
        :param _InstanceIds: Instance ID.
        :type InstanceIds: list of str
        :param _ProtectedFromScaleIn: Whether to enable scale-in protection for this instance
        :type ProtectedFromScaleIn: bool
        """
        self._AutoScalingGroupId = None
        self._InstanceIds = None
        self._ProtectedFromScaleIn = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ProtectedFromScaleIn(self):
        return self._ProtectedFromScaleIn

    @ProtectedFromScaleIn.setter
    def ProtectedFromScaleIn(self, ProtectedFromScaleIn):
        self._ProtectedFromScaleIn = ProtectedFromScaleIn


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._InstanceIds = params.get("InstanceIds")
        self._ProtectedFromScaleIn = params.get("ProtectedFromScaleIn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetInstancesProtectionResponse(AbstractModel):
    """SetInstancesProtection response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SpotMarketOptions(AbstractModel):
    """Bidding-related options

    """

    def __init__(self):
        r"""
        :param _MaxPrice: Bidding price such as "1.05"
        :type MaxPrice: str
        :param _SpotInstanceType: Bid request type. Currently, only "one-time" type is supported. Default value: one-time
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpotInstanceType: str
        """
        self._MaxPrice = None
        self._SpotInstanceType = None

    @property
    def MaxPrice(self):
        return self._MaxPrice

    @MaxPrice.setter
    def MaxPrice(self, MaxPrice):
        self._MaxPrice = MaxPrice

    @property
    def SpotInstanceType(self):
        return self._SpotInstanceType

    @SpotInstanceType.setter
    def SpotInstanceType(self, SpotInstanceType):
        self._SpotInstanceType = SpotInstanceType


    def _deserialize(self, params):
        self._MaxPrice = params.get("MaxPrice")
        self._SpotInstanceType = params.get("SpotInstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpotMixedAllocationPolicy(AbstractModel):
    """Specifies how to assign pay-as-you-go instances and spot instances in a mixed instance mode.

    """

    def __init__(self):
        r"""
        :param _BaseCapacity: The minimum number of the scaling group’s capacity that must be fulfilled by pay-as-you-go instances. It defaults to 0 if not specified. Its value cannot exceed the max capacity of the scaling group.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type BaseCapacity: int
        :param _OnDemandPercentageAboveBaseCapacity: Controls the percentage of pay-as-you-go instances for the additional capacity beyond `BaseCapacity`. Valid range: 0-100. The value 0 indicates that only spot instances are provisioned, while the value 100 indicates that only pay-as-you-go instances are provisioned. It defaults to 70 if not specified. The number of pay-as-you-go instances calculated on the percentage should be rounded up.
For example, if the desired capacity is 3, the `BaseCapacity` is set to 1, and the `OnDemandPercentageAboveBaseCapacity` is set to 1, the scaling group will have 2 pay-as-you-go instance (one comes from the base capacity, and the other comes from the rounded up value of the proportion), and 1 spot instance.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type OnDemandPercentageAboveBaseCapacity: int
        :param _SpotAllocationStrategy: Specifies how to assign spot instances in a mixed instance mode. Valid values: `COST_OPTIMIZED` and `CAPACITY_OPTIMIZED`; default value: `COST_OPTIMIZED`.
<br><li>`COST_OPTIMIZED`: the lowest cost policy. For each model in the launch configuration, AS tries to purchase it based on the lowest unit price per core in each availability zone. If the purchase failed, try the second-lowest unit price.
<br><li>`CAPACITY_OPTIMIZED`: the optimal capacity policy. For each model in the launch configuration, AS tries to purchase it based on the largest stock in each availability zone, minimizing the automatic repossession probability of spot instances.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type SpotAllocationStrategy: str
        :param _CompensateWithBaseInstance: Whether to replace with pay-as-you go instances. Valid values:
<br><li>`TRUE`: yes. After the purchase of spot instances failed due to insufficient stock and other reasons, purchase pay-as-you-go instances.
<br><li>`FALSE`: no. The scaling group only tries the configured model of spot instances when it needs to add spot instances.

Default value: `TRUE`.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type CompensateWithBaseInstance: bool
        """
        self._BaseCapacity = None
        self._OnDemandPercentageAboveBaseCapacity = None
        self._SpotAllocationStrategy = None
        self._CompensateWithBaseInstance = None

    @property
    def BaseCapacity(self):
        return self._BaseCapacity

    @BaseCapacity.setter
    def BaseCapacity(self, BaseCapacity):
        self._BaseCapacity = BaseCapacity

    @property
    def OnDemandPercentageAboveBaseCapacity(self):
        return self._OnDemandPercentageAboveBaseCapacity

    @OnDemandPercentageAboveBaseCapacity.setter
    def OnDemandPercentageAboveBaseCapacity(self, OnDemandPercentageAboveBaseCapacity):
        self._OnDemandPercentageAboveBaseCapacity = OnDemandPercentageAboveBaseCapacity

    @property
    def SpotAllocationStrategy(self):
        return self._SpotAllocationStrategy

    @SpotAllocationStrategy.setter
    def SpotAllocationStrategy(self, SpotAllocationStrategy):
        self._SpotAllocationStrategy = SpotAllocationStrategy

    @property
    def CompensateWithBaseInstance(self):
        return self._CompensateWithBaseInstance

    @CompensateWithBaseInstance.setter
    def CompensateWithBaseInstance(self, CompensateWithBaseInstance):
        self._CompensateWithBaseInstance = CompensateWithBaseInstance


    def _deserialize(self, params):
        self._BaseCapacity = params.get("BaseCapacity")
        self._OnDemandPercentageAboveBaseCapacity = params.get("OnDemandPercentageAboveBaseCapacity")
        self._SpotAllocationStrategy = params.get("SpotAllocationStrategy")
        self._CompensateWithBaseInstance = params.get("CompensateWithBaseInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAutoScalingInstancesRequest(AbstractModel):
    """StartAutoScalingInstances request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: The scaling group ID.
        :type AutoScalingGroupId: str
        :param _InstanceIds: The list of the CVM instances you want to start up.
        :type InstanceIds: list of str
        """
        self._AutoScalingGroupId = None
        self._InstanceIds = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAutoScalingInstancesResponse(AbstractModel):
    """StartAutoScalingInstances response structure.

    """

    def __init__(self):
        r"""
        :param _ActivityId: The scaling activity ID.
        :type ActivityId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class StopAutoScalingInstancesRequest(AbstractModel):
    """StopAutoScalingInstances request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: The scaling group ID.
        :type AutoScalingGroupId: str
        :param _InstanceIds: The list of the CVM instances you want to shut down.
        :type InstanceIds: list of str
        :param _StoppedMode: Whether the shutdown instances will be charged. Valid values:  
KEEP_CHARGING: keep charging after shutdown.  
STOP_CHARGING: stop charging after shutdown.
Default value: KEEP_CHARGING.
        :type StoppedMode: str
        """
        self._AutoScalingGroupId = None
        self._InstanceIds = None
        self._StoppedMode = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def StoppedMode(self):
        return self._StoppedMode

    @StoppedMode.setter
    def StoppedMode(self, StoppedMode):
        self._StoppedMode = StoppedMode


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._InstanceIds = params.get("InstanceIds")
        self._StoppedMode = params.get("StoppedMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopAutoScalingInstancesResponse(AbstractModel):
    """StopAutoScalingInstances response structure.

    """

    def __init__(self):
        r"""
        :param _ActivityId: The scaling activity ID.
        :type ActivityId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class SystemDisk(AbstractModel):
    """System disk configuration of the launch configuration. If this parameter is not specified, the default value is assigned to it.

    """

    def __init__(self):
        r"""
        :param _DiskType: System disk type. For more information on limits of system disk types, see [Cloud Disk Types](https://intl.cloud.tencent.com/document/product/362/31636). Valid values:<br><li>`LOCAL_BASIC`: local disk <br><li>`LOCAL_SSD`: local SSD disk <br><li>`CLOUD_BASIC`: HDD cloud disk <br><li>`CLOUD_PREMIUM`: premium cloud storage<br><li>`CLOUD_SSD`: SSD cloud disk <br><br>Default value: `CLOUD_PREMIUM`.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type DiskType: str
        :param _DiskSize: System disk size in GB. Default value: 50
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskSize: int
        """
        self._DiskType = None
        self._DiskSize = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Resource type and tag key-value pair

    """

    def __init__(self):
        r"""
        :param _Key: Tag key
        :type Key: str
        :param _Value: Tag value
        :type Value: str
        :param _ResourceType: Type of the resource binded to the tag. Currently supported types include "auto-scaling-group"
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceType: str
        """
        self._Key = None
        self._Value = None
        self._ResourceType = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetAttribute(AbstractModel):
    """Load balancer target attribute

    """

    def __init__(self):
        r"""
        :param _Port: Port
        :type Port: int
        :param _Weight: Weight
        :type Weight: int
        """
        self._Port = None
        self._Weight = None

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeLaunchConfigurationRequest(AbstractModel):
    """UpgradeLaunchConfiguration request structure.

    """

    def __init__(self):
        r"""
        :param _LaunchConfigurationId: Launch configuration ID.
        :type LaunchConfigurationId: str
        :param _ImageId: [Image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are three types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><br/>You can obtain the image IDs in the [CVM console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE).</li><li>You can also use the [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response.</li>
        :type ImageId: str
        :param _InstanceTypes: List of instance models. Different instance models specify different resource specifications. Up to 5 instance models can be supported.
        :type InstanceTypes: list of str
        :param _LaunchConfigurationName: Display name of the launch configuration, which can contain letters, digits, underscores and hyphens (-), and dots. Up to of 60 bytes allowed..
        :type LaunchConfigurationName: str
        :param _DataDisks: Information of the instance's data disk configuration. If this parameter is not specified, no data disk is purchased by default. Up to 11 data disks can be supported.
        :type DataDisks: list of DataDisk
        :param _EnhancedService: Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Security and Cloud Monitor. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled by default.
        :type EnhancedService: :class:`tencentcloud.autoscaling.v20180419.models.EnhancedService`
        :param _InstanceChargeType: Instance billing type. CVM instances are POSTPAID_BY_HOUR by default.
<br><li>POSTPAID_BY_HOUR: Pay-as-you-go on an hourly basis
<br><li>SPOTPAID: Bidding
        :type InstanceChargeType: str
        :param _InstanceMarketOptions: Market options of the instance, such as parameters related to spot instances. This parameter is required for spot instances.
        :type InstanceMarketOptions: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        :param _InstanceTypesCheckPolicy: Instance type verification policy. Value range: ALL, ANY. Default value: ANY.
<br><li> ALL: The verification will success only if all instance types (InstanceType) are available; otherwise, an error will be reported.
<br><li> ANY: The verification will success if any instance type (InstanceType) is available; otherwise, an error will be reported.

Common reasons why an instance type is unavailable include stock-out of the instance type or the corresponding cloud disk.
If a model in InstanceTypes does not exist or has been discontinued, a verification error will be reported regardless of the value of InstanceTypesCheckPolicy.
        :type InstanceTypesCheckPolicy: str
        :param _InternetAccessible: Configuration of public network bandwidth. If this parameter is not specified, 0 Mbps will be used by default.
        :type InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        :param _LoginSettings: Login settings of the instance. You can use this parameter to set the login method, password, and key of the instance or keep the login settings of the original image. By default, a random password will be generated and sent to you via the Message Center.
        :type LoginSettings: :class:`tencentcloud.autoscaling.v20180419.models.LoginSettings`
        :param _ProjectId: Project ID of the instance. Leave it blank as the default.
        :type ProjectId: int
        :param _SecurityGroupIds: The security group to which the instance belongs. This parameter can be obtained by calling the `SecurityGroupId` field in the returned value of [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808?from_cn_redirect=1). If this parameter is not specified, no security group will be bound by default.
        :type SecurityGroupIds: list of str
        :param _SystemDisk: System disk configuration of the instance. If this parameter is not specified, the default value will be used.
        :type SystemDisk: :class:`tencentcloud.autoscaling.v20180419.models.SystemDisk`
        :param _UserData: Base64-encoded custom data of up to 16 KB.
        :type UserData: str
        :param _InstanceTags: List of tags. This parameter is used to bind up to 10 tags to newly added instances.
        :type InstanceTags: list of InstanceTag
        :param _CamRoleName: CAM role name, which can be obtained from the roleName field in the return value of the DescribeRoleList API.
        :type CamRoleName: str
        :param _HostNameSettings: CVM hostname settings.
        :type HostNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.HostNameSettings`
        :param _InstanceNameSettings: Settings of CVM instance names
        :type InstanceNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameSettings`
        :param _InstanceChargePrepaid: Details of the monthly subscription, including the purchase period, auto-renewal. It is required if the `InstanceChargeType` is `PREPAID`.
        :type InstanceChargePrepaid: :class:`tencentcloud.autoscaling.v20180419.models.InstanceChargePrepaid`
        :param _DiskTypePolicy: Selection policy of cloud disks. Default value: ORIGINAL. Valid values:
<br><li>ORIGINAL: uses the configured cloud disk type
<br><li>AUTOMATIC: automatically chooses an available cloud disk type
        :type DiskTypePolicy: str
        :param _IPv6InternetAccessible: IPv6 public network bandwidth configuration. If the IPv6 address is available in the new instance, public network bandwidth can be allocated to the IPv6 address. This parameter is invalid if `Ipv6AddressCount` of the scaling group associated with the launch configuration is 0.
        :type IPv6InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.IPv6InternetAccessible`
        """
        self._LaunchConfigurationId = None
        self._ImageId = None
        self._InstanceTypes = None
        self._LaunchConfigurationName = None
        self._DataDisks = None
        self._EnhancedService = None
        self._InstanceChargeType = None
        self._InstanceMarketOptions = None
        self._InstanceTypesCheckPolicy = None
        self._InternetAccessible = None
        self._LoginSettings = None
        self._ProjectId = None
        self._SecurityGroupIds = None
        self._SystemDisk = None
        self._UserData = None
        self._InstanceTags = None
        self._CamRoleName = None
        self._HostNameSettings = None
        self._InstanceNameSettings = None
        self._InstanceChargePrepaid = None
        self._DiskTypePolicy = None
        self._IPv6InternetAccessible = None

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def LaunchConfigurationName(self):
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def InstanceTypesCheckPolicy(self):
        return self._InstanceTypesCheckPolicy

    @InstanceTypesCheckPolicy.setter
    def InstanceTypesCheckPolicy(self, InstanceTypesCheckPolicy):
        self._InstanceTypesCheckPolicy = InstanceTypesCheckPolicy

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def InstanceTags(self):
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HostNameSettings(self):
        return self._HostNameSettings

    @HostNameSettings.setter
    def HostNameSettings(self, HostNameSettings):
        self._HostNameSettings = HostNameSettings

    @property
    def InstanceNameSettings(self):
        return self._InstanceNameSettings

    @InstanceNameSettings.setter
    def InstanceNameSettings(self, InstanceNameSettings):
        self._InstanceNameSettings = InstanceNameSettings

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def DiskTypePolicy(self):
        return self._DiskTypePolicy

    @DiskTypePolicy.setter
    def DiskTypePolicy(self, DiskTypePolicy):
        self._DiskTypePolicy = DiskTypePolicy

    @property
    def IPv6InternetAccessible(self):
        return self._IPv6InternetAccessible

    @IPv6InternetAccessible.setter
    def IPv6InternetAccessible(self, IPv6InternetAccessible):
        self._IPv6InternetAccessible = IPv6InternetAccessible


    def _deserialize(self, params):
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._ImageId = params.get("ImageId")
        self._InstanceTypes = params.get("InstanceTypes")
        self._LaunchConfigurationName = params.get("LaunchConfigurationName")
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._InstanceTypesCheckPolicy = params.get("InstanceTypesCheckPolicy")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._ProjectId = params.get("ProjectId")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._UserData = params.get("UserData")
        if params.get("InstanceTags") is not None:
            self._InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTag()
                obj._deserialize(item)
                self._InstanceTags.append(obj)
        self._CamRoleName = params.get("CamRoleName")
        if params.get("HostNameSettings") is not None:
            self._HostNameSettings = HostNameSettings()
            self._HostNameSettings._deserialize(params.get("HostNameSettings"))
        if params.get("InstanceNameSettings") is not None:
            self._InstanceNameSettings = InstanceNameSettings()
            self._InstanceNameSettings._deserialize(params.get("InstanceNameSettings"))
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._DiskTypePolicy = params.get("DiskTypePolicy")
        if params.get("IPv6InternetAccessible") is not None:
            self._IPv6InternetAccessible = IPv6InternetAccessible()
            self._IPv6InternetAccessible._deserialize(params.get("IPv6InternetAccessible"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeLaunchConfigurationResponse(AbstractModel):
    """UpgradeLaunchConfiguration response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpgradeLifecycleHookRequest(AbstractModel):
    """UpgradeLifecycleHook request structure.

    """

    def __init__(self):
        r"""
        :param _LifecycleHookId: Lifecycle hook ID
        :type LifecycleHookId: str
        :param _LifecycleHookName: Lifecycle hook name
        :type LifecycleHookName: str
        :param _LifecycleTransition: Scenario for the lifecycle hook. Value range: "INSTANCE_LAUNCHING", "INSTANCE_TERMINATING"
        :type LifecycleTransition: str
        :param _DefaultResult: Defines the action to be taken by the auto scaling group upon lifecycle hook timeout. Value range: "CONTINUE", "ABANDON". Default value: "CONTINUE"
        :type DefaultResult: str
        :param _HeartbeatTimeout: The maximum length of time (in seconds) that can elapse before the lifecycle hook times out. Value range: 30-7200. Default value: 300
        :type HeartbeatTimeout: int
        :param _NotificationMetadata: Additional information of a notification that Auto Scaling sends to targets. This parameter is set when you configure a notification (default value: "").
        :type NotificationMetadata: str
        :param _NotificationTarget: Notification result. `NotificationTarget` and `LifecycleCommand` cannot be specified at the same time.
        :type NotificationTarget: :class:`tencentcloud.autoscaling.v20180419.models.NotificationTarget`
        :param _LifecycleTransitionType: The scenario where the lifecycle hook is applied. `EXTENSION`: the lifecycle hook will be triggered when AttachInstances, DetachInstances or RemoveInstaces is called. `NORMAL`: the lifecycle hook is not triggered by the above APIs. 
        :type LifecycleTransitionType: str
        :param _LifecycleCommand: Remote command execution object. `NotificationTarget` and `LifecycleCommand` cannot be specified at the same time.
        :type LifecycleCommand: :class:`tencentcloud.autoscaling.v20180419.models.LifecycleCommand`
        """
        self._LifecycleHookId = None
        self._LifecycleHookName = None
        self._LifecycleTransition = None
        self._DefaultResult = None
        self._HeartbeatTimeout = None
        self._NotificationMetadata = None
        self._NotificationTarget = None
        self._LifecycleTransitionType = None
        self._LifecycleCommand = None

    @property
    def LifecycleHookId(self):
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def LifecycleHookName(self):
        return self._LifecycleHookName

    @LifecycleHookName.setter
    def LifecycleHookName(self, LifecycleHookName):
        self._LifecycleHookName = LifecycleHookName

    @property
    def LifecycleTransition(self):
        return self._LifecycleTransition

    @LifecycleTransition.setter
    def LifecycleTransition(self, LifecycleTransition):
        self._LifecycleTransition = LifecycleTransition

    @property
    def DefaultResult(self):
        return self._DefaultResult

    @DefaultResult.setter
    def DefaultResult(self, DefaultResult):
        self._DefaultResult = DefaultResult

    @property
    def HeartbeatTimeout(self):
        return self._HeartbeatTimeout

    @HeartbeatTimeout.setter
    def HeartbeatTimeout(self, HeartbeatTimeout):
        self._HeartbeatTimeout = HeartbeatTimeout

    @property
    def NotificationMetadata(self):
        return self._NotificationMetadata

    @NotificationMetadata.setter
    def NotificationMetadata(self, NotificationMetadata):
        self._NotificationMetadata = NotificationMetadata

    @property
    def NotificationTarget(self):
        return self._NotificationTarget

    @NotificationTarget.setter
    def NotificationTarget(self, NotificationTarget):
        self._NotificationTarget = NotificationTarget

    @property
    def LifecycleTransitionType(self):
        return self._LifecycleTransitionType

    @LifecycleTransitionType.setter
    def LifecycleTransitionType(self, LifecycleTransitionType):
        self._LifecycleTransitionType = LifecycleTransitionType

    @property
    def LifecycleCommand(self):
        return self._LifecycleCommand

    @LifecycleCommand.setter
    def LifecycleCommand(self, LifecycleCommand):
        self._LifecycleCommand = LifecycleCommand


    def _deserialize(self, params):
        self._LifecycleHookId = params.get("LifecycleHookId")
        self._LifecycleHookName = params.get("LifecycleHookName")
        self._LifecycleTransition = params.get("LifecycleTransition")
        self._DefaultResult = params.get("DefaultResult")
        self._HeartbeatTimeout = params.get("HeartbeatTimeout")
        self._NotificationMetadata = params.get("NotificationMetadata")
        if params.get("NotificationTarget") is not None:
            self._NotificationTarget = NotificationTarget()
            self._NotificationTarget._deserialize(params.get("NotificationTarget"))
        self._LifecycleTransitionType = params.get("LifecycleTransitionType")
        if params.get("LifecycleCommand") is not None:
            self._LifecycleCommand = LifecycleCommand()
            self._LifecycleCommand._deserialize(params.get("LifecycleCommand"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeLifecycleHookResponse(AbstractModel):
    """UpgradeLifecycleHook response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")