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
        :param _ActivityType: Scaling activity type. Valid values:
<li>SCALE_OUT: Scale out an instance.</li>
<li>SCALE_IN: Scale in an instance.</li>
<li>ATTACH_INSTANCES: Add an instance.</li>
<li>REMOVE_INSTANCES: Terminate an instance.</li>
<li>DETACH_INSTANCES: Remove an instance.</li>
<li>TERMINATE_INSTANCES_UNEXPECTEDLY: Terminate an instance in the CVM console.</li>
<li>REPLACE_UNHEALTHY_INSTANCE: Replace an unhealthy instance.</li>
<li>START_INSTANCES: Start an instance.</li>
<li>STOP_INSTANCES: Stop an instance.</li>
<li>INVOKE_COMMAND: Execute a command.</li>
        :type ActivityType: str
        :param _StatusCode: Scaling activity status. Valid values:
<li>INIT: initializing.</li>
<li>RUNNING: running.</li>
<li>SUCCESSFUL: successful.</li>
<li>PARTIALLY_SUCCESSFUL: partially successful.</li>
<li>FAILED: failed.</li>
<li>CANCELLED: canceled.</li>
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
        """Auto scaling group ID.
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ActivityId(self):
        """Scaling activity ID.
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def ActivityType(self):
        """Scaling activity type. Valid values:
<li>SCALE_OUT: Scale out an instance.</li>
<li>SCALE_IN: Scale in an instance.</li>
<li>ATTACH_INSTANCES: Add an instance.</li>
<li>REMOVE_INSTANCES: Terminate an instance.</li>
<li>DETACH_INSTANCES: Remove an instance.</li>
<li>TERMINATE_INSTANCES_UNEXPECTEDLY: Terminate an instance in the CVM console.</li>
<li>REPLACE_UNHEALTHY_INSTANCE: Replace an unhealthy instance.</li>
<li>START_INSTANCES: Start an instance.</li>
<li>STOP_INSTANCES: Stop an instance.</li>
<li>INVOKE_COMMAND: Execute a command.</li>
        :rtype: str
        """
        return self._ActivityType

    @ActivityType.setter
    def ActivityType(self, ActivityType):
        self._ActivityType = ActivityType

    @property
    def StatusCode(self):
        """Scaling activity status. Valid values:
<li>INIT: initializing.</li>
<li>RUNNING: running.</li>
<li>SUCCESSFUL: successful.</li>
<li>PARTIALLY_SUCCESSFUL: partially successful.</li>
<li>FAILED: failed.</li>
<li>CANCELLED: canceled.</li>
        :rtype: str
        """
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def StatusMessage(self):
        """Description of the scaling activity status.
        :rtype: str
        """
        return self._StatusMessage

    @StatusMessage.setter
    def StatusMessage(self, StatusMessage):
        self._StatusMessage = StatusMessage

    @property
    def Cause(self):
        """Cause of the scaling activity.
        :rtype: str
        """
        return self._Cause

    @Cause.setter
    def Cause(self, Cause):
        self._Cause = Cause

    @property
    def Description(self):
        """Description of the scaling activity.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def StartTime(self):
        """Start time of the scaling activity.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time of the scaling activity.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreatedTime(self):
        """Creation time of the scaling activity.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ActivityRelatedInstanceSet(self):
        warnings.warn("parameter `ActivityRelatedInstanceSet` is deprecated", DeprecationWarning) 

        """This parameter has been deprecated.
        :rtype: list of ActivtyRelatedInstance
        """
        return self._ActivityRelatedInstanceSet

    @ActivityRelatedInstanceSet.setter
    def ActivityRelatedInstanceSet(self, ActivityRelatedInstanceSet):
        warnings.warn("parameter `ActivityRelatedInstanceSet` is deprecated", DeprecationWarning) 

        self._ActivityRelatedInstanceSet = ActivityRelatedInstanceSet

    @property
    def StatusMessageSimplified(self):
        """Brief description of the scaling activity status.
        :rtype: str
        """
        return self._StatusMessageSimplified

    @StatusMessageSimplified.setter
    def StatusMessageSimplified(self, StatusMessageSimplified):
        self._StatusMessageSimplified = StatusMessageSimplified

    @property
    def LifecycleActionResultSet(self):
        """Result of the lifecycle hook action in the scaling activity
        :rtype: list of LifecycleActionResultInfo
        """
        return self._LifecycleActionResultSet

    @LifecycleActionResultSet.setter
    def LifecycleActionResultSet(self, LifecycleActionResultSet):
        self._LifecycleActionResultSet = LifecycleActionResultSet

    @property
    def DetailedStatusMessageSet(self):
        """Detailed description of scaling activity status
        :rtype: list of DetailedStatusMessage
        """
        return self._DetailedStatusMessageSet

    @DetailedStatusMessageSet.setter
    def DetailedStatusMessageSet(self, DetailedStatusMessageSet):
        self._DetailedStatusMessageSet = DetailedStatusMessageSet

    @property
    def InvocationResultSet(self):
        """Result of the command execution
        :rtype: list of InvocationResult
        """
        return self._InvocationResultSet

    @InvocationResultSet.setter
    def InvocationResultSet(self, InvocationResultSet):
        self._InvocationResultSet = InvocationResultSet

    @property
    def RelatedInstanceSet(self):
        """Information set of the instances related to the scaling activity.
        :rtype: list of RelatedInstance
        """
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
        :param _InstanceStatus: Status of the instance in the scaling activity. Valid values: <br><li>INIT: initializing;</li> <li>RUNNING: instance in operation;</li> <li>SUCCESSFUL: activity successful;</li> <li>FAILED: activity failed.
        :type InstanceStatus: str
        """
        self._InstanceId = None
        self._InstanceStatus = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceStatus(self):
        """Status of the instance in the scaling activity. Valid values: <br><li>INIT: initializing;</li> <li>RUNNING: instance in operation;</li> <li>SUCCESSFUL: activity successful;</li> <li>FAILED: activity failed.
        :rtype: str
        """
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
        :param _Level: Scaling suggestion warning level. Valid values:
<li>WARNING: warning.</li>
<li>CRITICAL: critical.</li>
        :type Level: str
        """
        self._Problem = None
        self._Detail = None
        self._Solution = None
        self._Level = None

    @property
    def Problem(self):
        """Problem Description
        :rtype: str
        """
        return self._Problem

    @Problem.setter
    def Problem(self, Problem):
        self._Problem = Problem

    @property
    def Detail(self):
        """Problem Details
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Solution(self):
        """Recommended resolutions
        :rtype: str
        """
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution

    @property
    def Level(self):
        """Scaling suggestion warning level. Valid values:
<li>WARNING: warning.</li>
<li>CRITICAL: critical.</li>
        :rtype: str
        """
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
        """Auto scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        """List of CVM instance IDs
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        """Scaling activity ID
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def LoadBalancerIds(self):
        """List of classic CLB IDs. Up to 20 classic CLBs can be bound to a security group. `LoadBalancerIds` and `ForwardLoadBalancers` cannot be specified at the same time.
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ForwardLoadBalancers(self):
        """List of application CLBs. Up to 100 application CLBs can be bound to a scaling group. `LoadBalancerIds` and `ForwardLoadBalancers` cannot be specified at the same time.
        :rtype: list of ForwardLoadBalancer
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        """Scaling activity ID
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _Level: Scaling group warning level. Valid values:
<li>NORMAL: normal.</li>
<li>WARNING: warning.</li>
<li>CRITICAL: critical.</li>
        :type Level: str
        :param _Advices: A collection of suggestions for scaling group configurations.
        :type Advices: list of Advice
        """
        self._AutoScalingGroupId = None
        self._Level = None
        self._Advices = None

    @property
    def AutoScalingGroupId(self):
        """Scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def Level(self):
        """Scaling group warning level. Valid values:
<li>NORMAL: normal.</li>
<li>WARNING: warning.</li>
<li>CRITICAL: critical.</li>
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Advices(self):
        """A collection of suggestions for scaling group configurations.
        :rtype: list of Advice
        """
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
        :param _AutoScalingGroupStatus: Current status of the scaling group. Valid values:
<li>NORMAL: The scaling group is normal.</li>
<li>CVM_ABNORMAL: The launch configuration is abnormal.</li>
<li>LB_ABNORMAL: The CLB is abnormal.</li>
<li>LB_LISTENER_ABNORMAL: The CLB listener is abnormal.</li>
<li>LB_LOCATION_ABNORMAL: The forwarding configuration of the CLB listener is abnormal.</li>
<li>VPC_ABNORMAL: The VPC is abnormal.</li>
<li>SUBNET_ABNORMAL: The VPC subnet is abnormal.</li>
<li>INSUFFICIENT_BALANCE: The balance is insufficient.</li>
<li>LB_BACKEND_REGION_NOT_MATCH: The region of the CLB instance backend does not match that of the AS service.</li>
<li>LB_BACKEND_VPC_NOT_MATCH: The VPC of the CLB instance does not match that of the scaling group.</li>
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
        :param _MultiZoneSubnetPolicy: Multi-AZ/subnet policy.
<li>PRIORITY: The instances are attempted to be created taking the order of the AZ/subnet list as the priority. If the highest-priority AZ/subnet can create instances successfully, instances can always be created in that AZ/subnet.</li>
<li>EQUALITY: Select the AZ/subnet with the least number of instances for scale-out. In this way, each AZ/subnet has an opportunity for scale-out. Instances produced from multiple scale-out operations will be distributed to multiple AZs/subnets.</li>
        :type MultiZoneSubnetPolicy: str
        :param _HealthCheckType: Scaling group instance health check type, whose valid values include:
<li>CVM: Determine whether an instance is unhealthy based on its network status. An unhealthy network status is indicated by an event where instances become unreachable via PING. Detailed criteria of judgment can be found in [Instance Health Check](https://intl.cloud.tencent.com/document/product/377/8553?from_cn_redirect=1).</li>
<li>CLB: Determine whether an instance is unhealthy based on the health check status of CLB. For principles behind CLB health checks, see [Health Check](https://intl.cloud.tencent.com/document/product/214/6097?from_cn_redirect=1).</li>
        :type HealthCheckType: str
        :param _LoadBalancerHealthCheckGracePeriod: Grace period of the CLB health check
        :type LoadBalancerHealthCheckGracePeriod: int
        :param _InstanceAllocationPolicy: Instance assignment policy, whose valid values include LAUNCH_CONFIGURATION and SPOT_MIXED.
<li>LAUNCH_CONFIGURATION: Represent the traditional mode of assigning instances according to the launch configuration.</li>
<li>SPOT_MIXED: Represent the spot mixed mode. Currently, this mode is supported only when the launch configuration is set to the pay-as-you-go billing mode. In the mixed mode, the scaling group will scale out pay-as-you-go models or spot models based on the predefined settings. When the mixed mode is used, the billing type of the associated launch configuration cannot be modified.</li>
        :type InstanceAllocationPolicy: str
        :param _SpotMixedAllocationPolicy: Specifies how to assign pay-as-you-go instances and spot instances.
A valid value will be returned only when `InstanceAllocationPolicy` is set to `SPOT_MIXED`.
        :type SpotMixedAllocationPolicy: :class:`tencentcloud.autoscaling.v20180419.models.SpotMixedAllocationPolicy`
        :param _CapacityRebalance: Capacity rebalancing feature, which is applicable only to spot instances within the scaling group. Valid values:
<li>TRUE: Enable this feature. When spot instances in the scaling group are about to be automatically recycled by the spot instance service, AS proactively initiates the termination process of the spot instances. If there is a configured scale-in hook, it will be triggered before termination. After the termination process starts, AS asynchronously initiates the scale-out to reach the expected number of instances.</li>
<li>FALSE: Disable this feature. AS waits for the spot instance to be terminated before scaling out to reach the number of instances expected by the scaling group.</li>
        :type CapacityRebalance: bool
        :param _InstanceNameIndexSettings: Instance name sequencing settings.
Note: This field may return null, indicating that no valid value can be obtained.
        :type InstanceNameIndexSettings: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameIndexSettings`
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
        self._InstanceNameIndexSettings = None

    @property
    def AutoScalingGroupId(self):
        """Auto scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def AutoScalingGroupName(self):
        """Auto scaling group name
        :rtype: str
        """
        return self._AutoScalingGroupName

    @AutoScalingGroupName.setter
    def AutoScalingGroupName(self, AutoScalingGroupName):
        self._AutoScalingGroupName = AutoScalingGroupName

    @property
    def AutoScalingGroupStatus(self):
        """Current status of the scaling group. Valid values:
<li>NORMAL: The scaling group is normal.</li>
<li>CVM_ABNORMAL: The launch configuration is abnormal.</li>
<li>LB_ABNORMAL: The CLB is abnormal.</li>
<li>LB_LISTENER_ABNORMAL: The CLB listener is abnormal.</li>
<li>LB_LOCATION_ABNORMAL: The forwarding configuration of the CLB listener is abnormal.</li>
<li>VPC_ABNORMAL: The VPC is abnormal.</li>
<li>SUBNET_ABNORMAL: The VPC subnet is abnormal.</li>
<li>INSUFFICIENT_BALANCE: The balance is insufficient.</li>
<li>LB_BACKEND_REGION_NOT_MATCH: The region of the CLB instance backend does not match that of the AS service.</li>
<li>LB_BACKEND_VPC_NOT_MATCH: The VPC of the CLB instance does not match that of the scaling group.</li>
        :rtype: str
        """
        return self._AutoScalingGroupStatus

    @AutoScalingGroupStatus.setter
    def AutoScalingGroupStatus(self, AutoScalingGroupStatus):
        self._AutoScalingGroupStatus = AutoScalingGroupStatus

    @property
    def CreatedTime(self):
        """Creation time in UTC format
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def DefaultCooldown(self):
        """Default cooldown period in seconds
        :rtype: int
        """
        return self._DefaultCooldown

    @DefaultCooldown.setter
    def DefaultCooldown(self, DefaultCooldown):
        self._DefaultCooldown = DefaultCooldown

    @property
    def DesiredCapacity(self):
        """Desired number of instances
        :rtype: int
        """
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def EnabledStatus(self):
        """Enabled status. Value range: `ENABLED`, `DISABLED`
        :rtype: str
        """
        return self._EnabledStatus

    @EnabledStatus.setter
    def EnabledStatus(self, EnabledStatus):
        self._EnabledStatus = EnabledStatus

    @property
    def ForwardLoadBalancerSet(self):
        """List of application load balancers
        :rtype: list of ForwardLoadBalancer
        """
        return self._ForwardLoadBalancerSet

    @ForwardLoadBalancerSet.setter
    def ForwardLoadBalancerSet(self, ForwardLoadBalancerSet):
        self._ForwardLoadBalancerSet = ForwardLoadBalancerSet

    @property
    def InstanceCount(self):
        """Number of instances
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def InServiceInstanceCount(self):
        """Number of instances in `IN_SERVICE` status
        :rtype: int
        """
        return self._InServiceInstanceCount

    @InServiceInstanceCount.setter
    def InServiceInstanceCount(self, InServiceInstanceCount):
        self._InServiceInstanceCount = InServiceInstanceCount

    @property
    def LaunchConfigurationId(self):
        """Launch configuration ID
        :rtype: str
        """
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def LaunchConfigurationName(self):
        """Launch configuration name
        :rtype: str
        """
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def LoadBalancerIdSet(self):
        """List of Classic load balancer IDs
        :rtype: list of str
        """
        return self._LoadBalancerIdSet

    @LoadBalancerIdSet.setter
    def LoadBalancerIdSet(self, LoadBalancerIdSet):
        self._LoadBalancerIdSet = LoadBalancerIdSet

    @property
    def MaxSize(self):
        """Maximum number of instances
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        """Minimum number of instances
        :rtype: int
        """
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def ProjectId(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SubnetIdSet(self):
        """List of subnet IDs
        :rtype: list of str
        """
        return self._SubnetIdSet

    @SubnetIdSet.setter
    def SubnetIdSet(self, SubnetIdSet):
        self._SubnetIdSet = SubnetIdSet

    @property
    def TerminationPolicySet(self):
        """Termination policy
        :rtype: list of str
        """
        return self._TerminationPolicySet

    @TerminationPolicySet.setter
    def TerminationPolicySet(self, TerminationPolicySet):
        self._TerminationPolicySet = TerminationPolicySet

    @property
    def VpcId(self):
        """VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ZoneSet(self):
        """List of availability zones
        :rtype: list of str
        """
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

    @property
    def RetryPolicy(self):
        """Retry policy
        :rtype: str
        """
        return self._RetryPolicy

    @RetryPolicy.setter
    def RetryPolicy(self, RetryPolicy):
        self._RetryPolicy = RetryPolicy

    @property
    def InActivityStatus(self):
        """Whether the auto scaling group is performing a scaling activity. `IN_ACTIVITY` indicates yes, and `NOT_IN_ACTIVITY` indicates no.
        :rtype: str
        """
        return self._InActivityStatus

    @InActivityStatus.setter
    def InActivityStatus(self, InActivityStatus):
        self._InActivityStatus = InActivityStatus

    @property
    def Tags(self):
        """List of auto scaling group tags
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ServiceSettings(self):
        """Service settings
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ServiceSettings`
        """
        return self._ServiceSettings

    @ServiceSettings.setter
    def ServiceSettings(self, ServiceSettings):
        self._ServiceSettings = ServiceSettings

    @property
    def Ipv6AddressCount(self):
        """The number of IPv6 addresses that an instance has.
        :rtype: int
        """
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount

    @property
    def MultiZoneSubnetPolicy(self):
        """Multi-AZ/subnet policy.
<li>PRIORITY: The instances are attempted to be created taking the order of the AZ/subnet list as the priority. If the highest-priority AZ/subnet can create instances successfully, instances can always be created in that AZ/subnet.</li>
<li>EQUALITY: Select the AZ/subnet with the least number of instances for scale-out. In this way, each AZ/subnet has an opportunity for scale-out. Instances produced from multiple scale-out operations will be distributed to multiple AZs/subnets.</li>
        :rtype: str
        """
        return self._MultiZoneSubnetPolicy

    @MultiZoneSubnetPolicy.setter
    def MultiZoneSubnetPolicy(self, MultiZoneSubnetPolicy):
        self._MultiZoneSubnetPolicy = MultiZoneSubnetPolicy

    @property
    def HealthCheckType(self):
        """Scaling group instance health check type, whose valid values include:
<li>CVM: Determine whether an instance is unhealthy based on its network status. An unhealthy network status is indicated by an event where instances become unreachable via PING. Detailed criteria of judgment can be found in [Instance Health Check](https://intl.cloud.tencent.com/document/product/377/8553?from_cn_redirect=1).</li>
<li>CLB: Determine whether an instance is unhealthy based on the health check status of CLB. For principles behind CLB health checks, see [Health Check](https://intl.cloud.tencent.com/document/product/214/6097?from_cn_redirect=1).</li>
        :rtype: str
        """
        return self._HealthCheckType

    @HealthCheckType.setter
    def HealthCheckType(self, HealthCheckType):
        self._HealthCheckType = HealthCheckType

    @property
    def LoadBalancerHealthCheckGracePeriod(self):
        """Grace period of the CLB health check
        :rtype: int
        """
        return self._LoadBalancerHealthCheckGracePeriod

    @LoadBalancerHealthCheckGracePeriod.setter
    def LoadBalancerHealthCheckGracePeriod(self, LoadBalancerHealthCheckGracePeriod):
        self._LoadBalancerHealthCheckGracePeriod = LoadBalancerHealthCheckGracePeriod

    @property
    def InstanceAllocationPolicy(self):
        """Instance assignment policy, whose valid values include LAUNCH_CONFIGURATION and SPOT_MIXED.
<li>LAUNCH_CONFIGURATION: Represent the traditional mode of assigning instances according to the launch configuration.</li>
<li>SPOT_MIXED: Represent the spot mixed mode. Currently, this mode is supported only when the launch configuration is set to the pay-as-you-go billing mode. In the mixed mode, the scaling group will scale out pay-as-you-go models or spot models based on the predefined settings. When the mixed mode is used, the billing type of the associated launch configuration cannot be modified.</li>
        :rtype: str
        """
        return self._InstanceAllocationPolicy

    @InstanceAllocationPolicy.setter
    def InstanceAllocationPolicy(self, InstanceAllocationPolicy):
        self._InstanceAllocationPolicy = InstanceAllocationPolicy

    @property
    def SpotMixedAllocationPolicy(self):
        """Specifies how to assign pay-as-you-go instances and spot instances.
A valid value will be returned only when `InstanceAllocationPolicy` is set to `SPOT_MIXED`.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.SpotMixedAllocationPolicy`
        """
        return self._SpotMixedAllocationPolicy

    @SpotMixedAllocationPolicy.setter
    def SpotMixedAllocationPolicy(self, SpotMixedAllocationPolicy):
        self._SpotMixedAllocationPolicy = SpotMixedAllocationPolicy

    @property
    def CapacityRebalance(self):
        """Capacity rebalancing feature, which is applicable only to spot instances within the scaling group. Valid values:
<li>TRUE: Enable this feature. When spot instances in the scaling group are about to be automatically recycled by the spot instance service, AS proactively initiates the termination process of the spot instances. If there is a configured scale-in hook, it will be triggered before termination. After the termination process starts, AS asynchronously initiates the scale-out to reach the expected number of instances.</li>
<li>FALSE: Disable this feature. AS waits for the spot instance to be terminated before scaling out to reach the number of instances expected by the scaling group.</li>
        :rtype: bool
        """
        return self._CapacityRebalance

    @CapacityRebalance.setter
    def CapacityRebalance(self, CapacityRebalance):
        self._CapacityRebalance = CapacityRebalance

    @property
    def InstanceNameIndexSettings(self):
        """Instance name sequencing settings.
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameIndexSettings`
        """
        return self._InstanceNameIndexSettings

    @InstanceNameIndexSettings.setter
    def InstanceNameIndexSettings(self, InstanceNameIndexSettings):
        self._InstanceNameIndexSettings = InstanceNameIndexSettings


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
        if params.get("InstanceNameIndexSettings") is not None:
            self._InstanceNameIndexSettings = InstanceNameIndexSettings()
            self._InstanceNameIndexSettings._deserialize(params.get("InstanceNameIndexSettings"))
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
        """Scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def AutoScalingGroupName(self):
        """Auto scaling group name.
        :rtype: str
        """
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
        """Auto scaling group ID.
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def NotificationUserGroupIds(self):
        """List of user group IDs.
        :rtype: list of str
        """
        return self._NotificationUserGroupIds

    @NotificationUserGroupIds.setter
    def NotificationUserGroupIds(self, NotificationUserGroupIds):
        self._NotificationUserGroupIds = NotificationUserGroupIds

    @property
    def NotificationTypes(self):
        """List of notification events.
        :rtype: list of str
        """
        return self._NotificationTypes

    @NotificationTypes.setter
    def NotificationTypes(self, NotificationTypes):
        self._NotificationTypes = NotificationTypes

    @property
    def AutoScalingNotificationId(self):
        """Event notification ID.
        :rtype: str
        """
        return self._AutoScalingNotificationId

    @AutoScalingNotificationId.setter
    def AutoScalingNotificationId(self, AutoScalingNotificationId):
        self._AutoScalingNotificationId = AutoScalingNotificationId

    @property
    def TargetType(self):
        """Notification receiver type.
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def QueueName(self):
        """CMQ queue name.
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def TopicName(self):
        """CMQ topic name.
        :rtype: str
        """
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
        


class CancelInstanceRefreshRequest(AbstractModel):
    """CancelInstanceRefresh request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Scaling group ID.
        :type AutoScalingGroupId: str
        :param _RefreshActivityId: Refresh activity ID.
        :type RefreshActivityId: str
        """
        self._AutoScalingGroupId = None
        self._RefreshActivityId = None

    @property
    def AutoScalingGroupId(self):
        """Scaling group ID.
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RefreshActivityId(self):
        """Refresh activity ID.
        :rtype: str
        """
        return self._RefreshActivityId

    @RefreshActivityId.setter
    def RefreshActivityId(self, RefreshActivityId):
        self._RefreshActivityId = RefreshActivityId


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._RefreshActivityId = params.get("RefreshActivityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelInstanceRefreshResponse(AbstractModel):
    """CancelInstanceRefresh response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


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
Setting it to `true` will clear the instance name settings, which means that CVM newly created on this launch configuration will be named in the as-{{AutoScalingGroupName}} format.
        :type ClearInstanceNameSettings: bool
        :param _ClearDisasterRecoverGroupIds: Whether to clear placement group information. This parameter is optional. Default value: `false`.
`True` means clearing placement group information. After that, no placement groups are specified for CVMs created based on the information.
        :type ClearDisasterRecoverGroupIds: bool
        :param _ClearInstanceTags: Whether to clear the instance tag list. This parameter is optional, and its default value is false.
If true is filled in, it indicates that the instance tag list should be cleared. After the list is cleared, the CVMs created based on this will not be bound to the tags in the list.
        :type ClearInstanceTags: bool
        :param _ClearMetadata: Whether to clear metadata, optional, defaults to false. Setting it to true will clear metadata, the CVMs created based on this will not be associated with custom metadata.
        :type ClearMetadata: bool
        """
        self._LaunchConfigurationId = None
        self._ClearDataDisks = None
        self._ClearHostNameSettings = None
        self._ClearInstanceNameSettings = None
        self._ClearDisasterRecoverGroupIds = None
        self._ClearInstanceTags = None
        self._ClearMetadata = None

    @property
    def LaunchConfigurationId(self):
        """Launch configuration ID
        :rtype: str
        """
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def ClearDataDisks(self):
        """Whether to clear data disk information. This parameter is optional and the default value is `false`.
Setting it to `true` will clear data disks, which means that CVM newly created on this launch configuration will have no data disk.
        :rtype: bool
        """
        return self._ClearDataDisks

    @ClearDataDisks.setter
    def ClearDataDisks(self, ClearDataDisks):
        self._ClearDataDisks = ClearDataDisks

    @property
    def ClearHostNameSettings(self):
        """Whether to clear the CVM hostname settings. This parameter is optional and the default value is `false`.
Setting it to `true` will clear the hostname settings, which means that CVM newly created on this launch configuration will have no hostname.
        :rtype: bool
        """
        return self._ClearHostNameSettings

    @ClearHostNameSettings.setter
    def ClearHostNameSettings(self, ClearHostNameSettings):
        self._ClearHostNameSettings = ClearHostNameSettings

    @property
    def ClearInstanceNameSettings(self):
        """Whether to clear the CVM instance name settings. This parameter is optional and the default value is `false`.
Setting it to `true` will clear the instance name settings, which means that CVM newly created on this launch configuration will be named in the as-{{AutoScalingGroupName}} format.
        :rtype: bool
        """
        return self._ClearInstanceNameSettings

    @ClearInstanceNameSettings.setter
    def ClearInstanceNameSettings(self, ClearInstanceNameSettings):
        self._ClearInstanceNameSettings = ClearInstanceNameSettings

    @property
    def ClearDisasterRecoverGroupIds(self):
        """Whether to clear placement group information. This parameter is optional. Default value: `false`.
`True` means clearing placement group information. After that, no placement groups are specified for CVMs created based on the information.
        :rtype: bool
        """
        return self._ClearDisasterRecoverGroupIds

    @ClearDisasterRecoverGroupIds.setter
    def ClearDisasterRecoverGroupIds(self, ClearDisasterRecoverGroupIds):
        self._ClearDisasterRecoverGroupIds = ClearDisasterRecoverGroupIds

    @property
    def ClearInstanceTags(self):
        """Whether to clear the instance tag list. This parameter is optional, and its default value is false.
If true is filled in, it indicates that the instance tag list should be cleared. After the list is cleared, the CVMs created based on this will not be bound to the tags in the list.
        :rtype: bool
        """
        return self._ClearInstanceTags

    @ClearInstanceTags.setter
    def ClearInstanceTags(self, ClearInstanceTags):
        self._ClearInstanceTags = ClearInstanceTags

    @property
    def ClearMetadata(self):
        """Whether to clear metadata, optional, defaults to false. Setting it to true will clear metadata, the CVMs created based on this will not be associated with custom metadata.
        :rtype: bool
        """
        return self._ClearMetadata

    @ClearMetadata.setter
    def ClearMetadata(self, ClearMetadata):
        self._ClearMetadata = ClearMetadata


    def _deserialize(self, params):
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._ClearDataDisks = params.get("ClearDataDisks")
        self._ClearHostNameSettings = params.get("ClearHostNameSettings")
        self._ClearInstanceNameSettings = params.get("ClearInstanceNameSettings")
        self._ClearDisasterRecoverGroupIds = params.get("ClearDisasterRecoverGroupIds")
        self._ClearInstanceTags = params.get("ClearInstanceTags")
        self._ClearMetadata = params.get("ClearMetadata")
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Lifecycle hook ID
        :rtype: str
        """
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def LifecycleActionResult(self):
        """Result of the lifecycle action. Value range: "CONTINUE", "ABANDON"
        :rtype: str
        """
        return self._LifecycleActionResult

    @LifecycleActionResult.setter
    def LifecycleActionResult(self, LifecycleActionResult):
        self._LifecycleActionResult = LifecycleActionResult

    @property
    def InstanceId(self):
        """Instance ID. Either "InstanceId" or "LifecycleActionToken" must be specified
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LifecycleActionToken(self):
        """Either "InstanceId" or "LifecycleActionToken" must be specified
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """The scaling group name. It must be unique under your account. The name can only contain letters, numbers, underscore, hyphen “-” and periods. It cannot exceed 55 bytes.
        :rtype: str
        """
        return self._AutoScalingGroupName

    @AutoScalingGroupName.setter
    def AutoScalingGroupName(self, AutoScalingGroupName):
        self._AutoScalingGroupName = AutoScalingGroupName

    @property
    def InstanceId(self):
        """The instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MinSize(self):
        """The minimum number of instances. Value range: 0-2000.
        :rtype: int
        """
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        """The maximum number of instances. Value range: 0-2000.
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def DesiredCapacity(self):
        """The desired capacity. Its value must be greater than the minimum and smaller than the maximum.
        :rtype: int
        """
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def InheritInstanceTag(self):
        """Whether to inherit the instance tag. Default value: False
        :rtype: bool
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoScalingGroupId = None
        self._RequestId = None

    @property
    def AutoScalingGroupId(self):
        """The scaling group ID.
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _TerminationPolicies: Termination policy, whose maximum length is currently 1. Valid values: OLDEST_INSTANCE and NEWEST_INSTANCE. Default value: OLDEST_INSTANCE.
<li>OLDEST_INSTANCE: Terminate the oldest instance in the scaling group first.</li>
<li>NEWEST_INSTANCE: Terminate the newest instance in the scaling group first.</li>
        :type TerminationPolicies: list of str
        :param _Zones: List of availability zones. An availability zone must be specified in the basic network scenario. If multiple availability zones are entered, their priority will be determined by the order in which they are entered, and they will be tried one by one until instances can be successfully created.
        :type Zones: list of str
        :param _RetryPolicy: Retry policy. Valid values: IMMEDIATE_RETRY, INCREMENTAL_INTERVALS, and NO_RETRY. Default value: IMMEDIATE_RETRY. A partially successful scaling activity is considered a failed activity.
<li>IMMEDIATE_RETRY: Immediately retry or quickly retry in a short period. There will be no retry anymore after a certain number of consecutive failures (5).</li>
<li>INCREMENTAL_INTERVALS: Retry at an incremental interval. As the number of continuous failures increase, the retry interval gradually increases. The interval for the first 10 retries is the same as the immediate retry mode, and that for the subsequent retries gradually increases to 10 minutes, 30 minutes, 60 minutes, or 1 day.</li>
<li>NO_RETRY: There will be no retry until another user call or alarm information is received.</li>  
        :type RetryPolicy: str
        :param _ZonesCheckPolicy: AZ verification policy. Valid values: ALL and ANY. Default value: ANY.
<li>ALL: Verification passes if all AZs or subnets are available; otherwise, a verification error will be reported.<li>
<li>ANY: Verification passes if any AZ or subnet is available; otherwise, a verification error will be reported.</li>

Common reasons for unavailable AZs or subnets include the CVM InstanceType in the AZ being sold out, the CBS cloud disk in the AZ being sold out, insufficient quota in the AZ, and insufficient IP addresses in the subnet.
If there is no AZ or subnet in Zones/SubnetIds, a verification error will be reported regardless of the values of ZonesCheckPolicy.
        :type ZonesCheckPolicy: str
        :param _Tags: List of tag descriptions. In this parameter, you can specify the tags to be bound with a scaling group as well as corresponding resource instances. Each scaling group can have up to 30 tags.
        :type Tags: list of Tag
        :param _ServiceSettings: Service settings such as unhealthy instance replacement.
        :type ServiceSettings: :class:`tencentcloud.autoscaling.v20180419.models.ServiceSettings`
        :param _Ipv6AddressCount: The number of IPv6 addresses that an instance has. Valid values: 0 and 1. Default value: 0.
        :type Ipv6AddressCount: int
        :param _MultiZoneSubnetPolicy: Multi-AZ/multi-subnet policy, whose valid values include PRIORITY and EQUALITY, with the default value being PRIORITY.
<li>PRIORITY: The instances are attempted to be created taking the order of the AZ/subnet list as the priority. If instances can be successfully created in the highest-priority AZ/subnet, they will always be created in that AZ/subnet.</li>
<li>EQUALITY: The instances added through scale-out will be distributed across multiple AZs/subnets to ensure a relatively balanced number of instances in each AZ/subnet after scaling out.</li>

Points to consider regarding this policy:
<li>When the scaling group is based on a classic network, this policy applies to the multi-AZ; when the scaling group is based on a VPC network, this policy applies to the multi-subnet, in this case, the AZs are no longer considered. For example, if there are four subnets labeled A, B, C, and D, where A, B, and C are in AZ 1 and D is in AZ 2, the subnets A, B, C, and D are considered for sorting without regard to AZs 1 and 2.</li>
<li>This policy applies to the multi-AZ/multi-subnet and not to the InstanceTypes parameter of the launch configuration, which is selected according to the priority policy.</li>
<li>When instances are created according to the PRIORITY policy, ensure the policy for multiple models first, followed by the policy for the multi-AZ/subnet. For example, with models A and B and subnets 1, 2, and 3, attempts will be made in the order of A1, A2, A3, B1, B2, and B3. If A1 is sold out, A2 will be attempted (instead of B1).</li>
        :type MultiZoneSubnetPolicy: str
        :param _HealthCheckType: Health check type for scaling group instances. Valid values:
<li>CVM: Determine whether an instance is unhealthy based on its network status. An unhealthy network status is indicated by an event where instances become unreachable via PING. For detailed criteria of judgment, see [Instance Health Check](https://www.tencentcloud.com/document/product/377/8553?lang=en&pg=).</li>
<li>CLB: Determine whether an instance is unhealthy based on the health check status of CLB. For principles behind CLB health checks, see [Health Check Overview](https://www.tencentcloud.com/document/product/214/6097?from_search=1&lang=en&pg=).</li>
If CLB is selected, the scaling group will check both the instance's network status and the CLB's health check status. If the instance's network status is unhealthy, the instance will be marked as UNHEALTHY. If the CLB's health check status is abnormal, the instance will be marked as CLB_UNHEALTHY. If both of them are abnormal, the instance will be marked as UNHEALTHY|CLB_UNHEALTHY. Default value: CLB.
        :type HealthCheckType: str
        :param _LoadBalancerHealthCheckGracePeriod: Grace period of the CLB health check during which the `IN_SERVICE` instances added will not be marked as `CLB_UNHEALTHY`.<br>Valid range: 0-7200, in seconds. Default value: `0`.
        :type LoadBalancerHealthCheckGracePeriod: int
        :param _InstanceAllocationPolicy: Instance assignment policy. Valid values: LAUNCH_CONFIGURATION and SPOT_MIXED. Default value: LAUNCH_CONFIGURATION.
<li>LAUNCH_CONFIGURATION: Represent the traditional mode of assigning instances according to the launch configuration.</li>
<li>SPOT_MIXED: Represent the spot mixed mode. Currently, this mode is supported only when the launch configuration is set to the pay-as-you-go billing mode. In the mixed mode, the scaling group will scale out pay-as-you-go models or spot models based on the predefined settings. When the mixed mode is used, the billing type of the associated launch configuration cannot be modified.</li>
        :type InstanceAllocationPolicy: str
        :param _SpotMixedAllocationPolicy: Specifies how to assign pay-as-you-go instances and spot instances.
This parameter is valid only when `InstanceAllocationPolicy ` is set to `SPOT_MIXED`.
        :type SpotMixedAllocationPolicy: :class:`tencentcloud.autoscaling.v20180419.models.SpotMixedAllocationPolicy`
        :param _CapacityRebalance: Capacity rebalancing feature, which is applicable only to spot instances within the scaling group. Valid values:
<li>TRUE: Enable this feature. When spot instances in the scaling group are about to be automatically recycled by the spot instance service, AS proactively initiates the termination process of the spot instances. If there is a configured scale-in hook, it will be triggered before termination. After the termination process starts, AS asynchronously initiates the scale-out to reach the expected number of instances.</li>
<li>FALSE: Disable this feature. AS waits for the spot instance to be terminated before scaling out to reach the number of instances expected by the scaling group.</li>

Default value: FALSE.
        :type CapacityRebalance: bool
        :param _InstanceNameIndexSettings: Instance name sequencing settings. If this parameter is not specified, the default is not enabled. When enabled, an incremental numeric sequence will be appended to the names of instances automatically created within the scaling group.
        :type InstanceNameIndexSettings: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameIndexSettings`
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
        self._InstanceNameIndexSettings = None

    @property
    def AutoScalingGroupName(self):
        """Auto scaling group name, which can only contain letters, numbers, underscores, hyphens ("-"), and decimal points with a maximum length of 55 bytes and must be unique under your account.
        :rtype: str
        """
        return self._AutoScalingGroupName

    @AutoScalingGroupName.setter
    def AutoScalingGroupName(self, AutoScalingGroupName):
        self._AutoScalingGroupName = AutoScalingGroupName

    @property
    def LaunchConfigurationId(self):
        """Launch configuration ID
        :rtype: str
        """
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def MaxSize(self):
        """Maximum number of instances. Value range: 0-2,000.
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        """Minimum number of instances. Value range: 0-2,000.
        :rtype: int
        """
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def VpcId(self):
        """VPC ID; if on a basic network, enter an empty string
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def DefaultCooldown(self):
        """Default cooldown period in seconds. Default value: 300
        :rtype: int
        """
        return self._DefaultCooldown

    @DefaultCooldown.setter
    def DefaultCooldown(self, DefaultCooldown):
        self._DefaultCooldown = DefaultCooldown

    @property
    def DesiredCapacity(self):
        """Desired number of instances. The number should be no larger than the maximum and no smaller than minimum number of instances
        :rtype: int
        """
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def LoadBalancerIds(self):
        """List of classic CLB IDs. Currently, the maximum length is 20. You cannot specify LoadBalancerIds and ForwardLoadBalancers at the same time.
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ProjectId(self):
        """Project ID of an instance in a scaling group. The default project is used if it’s left blank.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ForwardLoadBalancers(self):
        """List of application CLBs. Up to 100 CLBs are allowed. `LoadBalancerIds` and `ForwardLoadBalancers` cannot be specified at the same time.
        :rtype: list of ForwardLoadBalancer
        """
        return self._ForwardLoadBalancers

    @ForwardLoadBalancers.setter
    def ForwardLoadBalancers(self, ForwardLoadBalancers):
        self._ForwardLoadBalancers = ForwardLoadBalancers

    @property
    def SubnetIds(self):
        """List of subnet IDs. A subnet must be specified in the VPC scenario. If multiple subnets are entered, their priority will be determined by the order in which they are entered, and they will be tried one by one until instances can be successfully created.
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def TerminationPolicies(self):
        """Termination policy, whose maximum length is currently 1. Valid values: OLDEST_INSTANCE and NEWEST_INSTANCE. Default value: OLDEST_INSTANCE.
<li>OLDEST_INSTANCE: Terminate the oldest instance in the scaling group first.</li>
<li>NEWEST_INSTANCE: Terminate the newest instance in the scaling group first.</li>
        :rtype: list of str
        """
        return self._TerminationPolicies

    @TerminationPolicies.setter
    def TerminationPolicies(self, TerminationPolicies):
        self._TerminationPolicies = TerminationPolicies

    @property
    def Zones(self):
        """List of availability zones. An availability zone must be specified in the basic network scenario. If multiple availability zones are entered, their priority will be determined by the order in which they are entered, and they will be tried one by one until instances can be successfully created.
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RetryPolicy(self):
        """Retry policy. Valid values: IMMEDIATE_RETRY, INCREMENTAL_INTERVALS, and NO_RETRY. Default value: IMMEDIATE_RETRY. A partially successful scaling activity is considered a failed activity.
<li>IMMEDIATE_RETRY: Immediately retry or quickly retry in a short period. There will be no retry anymore after a certain number of consecutive failures (5).</li>
<li>INCREMENTAL_INTERVALS: Retry at an incremental interval. As the number of continuous failures increase, the retry interval gradually increases. The interval for the first 10 retries is the same as the immediate retry mode, and that for the subsequent retries gradually increases to 10 minutes, 30 minutes, 60 minutes, or 1 day.</li>
<li>NO_RETRY: There will be no retry until another user call or alarm information is received.</li>  
        :rtype: str
        """
        return self._RetryPolicy

    @RetryPolicy.setter
    def RetryPolicy(self, RetryPolicy):
        self._RetryPolicy = RetryPolicy

    @property
    def ZonesCheckPolicy(self):
        """AZ verification policy. Valid values: ALL and ANY. Default value: ANY.
<li>ALL: Verification passes if all AZs or subnets are available; otherwise, a verification error will be reported.<li>
<li>ANY: Verification passes if any AZ or subnet is available; otherwise, a verification error will be reported.</li>

Common reasons for unavailable AZs or subnets include the CVM InstanceType in the AZ being sold out, the CBS cloud disk in the AZ being sold out, insufficient quota in the AZ, and insufficient IP addresses in the subnet.
If there is no AZ or subnet in Zones/SubnetIds, a verification error will be reported regardless of the values of ZonesCheckPolicy.
        :rtype: str
        """
        return self._ZonesCheckPolicy

    @ZonesCheckPolicy.setter
    def ZonesCheckPolicy(self, ZonesCheckPolicy):
        self._ZonesCheckPolicy = ZonesCheckPolicy

    @property
    def Tags(self):
        """List of tag descriptions. In this parameter, you can specify the tags to be bound with a scaling group as well as corresponding resource instances. Each scaling group can have up to 30 tags.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ServiceSettings(self):
        """Service settings such as unhealthy instance replacement.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ServiceSettings`
        """
        return self._ServiceSettings

    @ServiceSettings.setter
    def ServiceSettings(self, ServiceSettings):
        self._ServiceSettings = ServiceSettings

    @property
    def Ipv6AddressCount(self):
        """The number of IPv6 addresses that an instance has. Valid values: 0 and 1. Default value: 0.
        :rtype: int
        """
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount

    @property
    def MultiZoneSubnetPolicy(self):
        """Multi-AZ/multi-subnet policy, whose valid values include PRIORITY and EQUALITY, with the default value being PRIORITY.
<li>PRIORITY: The instances are attempted to be created taking the order of the AZ/subnet list as the priority. If instances can be successfully created in the highest-priority AZ/subnet, they will always be created in that AZ/subnet.</li>
<li>EQUALITY: The instances added through scale-out will be distributed across multiple AZs/subnets to ensure a relatively balanced number of instances in each AZ/subnet after scaling out.</li>

Points to consider regarding this policy:
<li>When the scaling group is based on a classic network, this policy applies to the multi-AZ; when the scaling group is based on a VPC network, this policy applies to the multi-subnet, in this case, the AZs are no longer considered. For example, if there are four subnets labeled A, B, C, and D, where A, B, and C are in AZ 1 and D is in AZ 2, the subnets A, B, C, and D are considered for sorting without regard to AZs 1 and 2.</li>
<li>This policy applies to the multi-AZ/multi-subnet and not to the InstanceTypes parameter of the launch configuration, which is selected according to the priority policy.</li>
<li>When instances are created according to the PRIORITY policy, ensure the policy for multiple models first, followed by the policy for the multi-AZ/subnet. For example, with models A and B and subnets 1, 2, and 3, attempts will be made in the order of A1, A2, A3, B1, B2, and B3. If A1 is sold out, A2 will be attempted (instead of B1).</li>
        :rtype: str
        """
        return self._MultiZoneSubnetPolicy

    @MultiZoneSubnetPolicy.setter
    def MultiZoneSubnetPolicy(self, MultiZoneSubnetPolicy):
        self._MultiZoneSubnetPolicy = MultiZoneSubnetPolicy

    @property
    def HealthCheckType(self):
        """Health check type for scaling group instances. Valid values:
<li>CVM: Determine whether an instance is unhealthy based on its network status. An unhealthy network status is indicated by an event where instances become unreachable via PING. For detailed criteria of judgment, see [Instance Health Check](https://www.tencentcloud.com/document/product/377/8553?lang=en&pg=).</li>
<li>CLB: Determine whether an instance is unhealthy based on the health check status of CLB. For principles behind CLB health checks, see [Health Check Overview](https://www.tencentcloud.com/document/product/214/6097?from_search=1&lang=en&pg=).</li>
If CLB is selected, the scaling group will check both the instance's network status and the CLB's health check status. If the instance's network status is unhealthy, the instance will be marked as UNHEALTHY. If the CLB's health check status is abnormal, the instance will be marked as CLB_UNHEALTHY. If both of them are abnormal, the instance will be marked as UNHEALTHY|CLB_UNHEALTHY. Default value: CLB.
        :rtype: str
        """
        return self._HealthCheckType

    @HealthCheckType.setter
    def HealthCheckType(self, HealthCheckType):
        self._HealthCheckType = HealthCheckType

    @property
    def LoadBalancerHealthCheckGracePeriod(self):
        """Grace period of the CLB health check during which the `IN_SERVICE` instances added will not be marked as `CLB_UNHEALTHY`.<br>Valid range: 0-7200, in seconds. Default value: `0`.
        :rtype: int
        """
        return self._LoadBalancerHealthCheckGracePeriod

    @LoadBalancerHealthCheckGracePeriod.setter
    def LoadBalancerHealthCheckGracePeriod(self, LoadBalancerHealthCheckGracePeriod):
        self._LoadBalancerHealthCheckGracePeriod = LoadBalancerHealthCheckGracePeriod

    @property
    def InstanceAllocationPolicy(self):
        """Instance assignment policy. Valid values: LAUNCH_CONFIGURATION and SPOT_MIXED. Default value: LAUNCH_CONFIGURATION.
<li>LAUNCH_CONFIGURATION: Represent the traditional mode of assigning instances according to the launch configuration.</li>
<li>SPOT_MIXED: Represent the spot mixed mode. Currently, this mode is supported only when the launch configuration is set to the pay-as-you-go billing mode. In the mixed mode, the scaling group will scale out pay-as-you-go models or spot models based on the predefined settings. When the mixed mode is used, the billing type of the associated launch configuration cannot be modified.</li>
        :rtype: str
        """
        return self._InstanceAllocationPolicy

    @InstanceAllocationPolicy.setter
    def InstanceAllocationPolicy(self, InstanceAllocationPolicy):
        self._InstanceAllocationPolicy = InstanceAllocationPolicy

    @property
    def SpotMixedAllocationPolicy(self):
        """Specifies how to assign pay-as-you-go instances and spot instances.
This parameter is valid only when `InstanceAllocationPolicy ` is set to `SPOT_MIXED`.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.SpotMixedAllocationPolicy`
        """
        return self._SpotMixedAllocationPolicy

    @SpotMixedAllocationPolicy.setter
    def SpotMixedAllocationPolicy(self, SpotMixedAllocationPolicy):
        self._SpotMixedAllocationPolicy = SpotMixedAllocationPolicy

    @property
    def CapacityRebalance(self):
        """Capacity rebalancing feature, which is applicable only to spot instances within the scaling group. Valid values:
<li>TRUE: Enable this feature. When spot instances in the scaling group are about to be automatically recycled by the spot instance service, AS proactively initiates the termination process of the spot instances. If there is a configured scale-in hook, it will be triggered before termination. After the termination process starts, AS asynchronously initiates the scale-out to reach the expected number of instances.</li>
<li>FALSE: Disable this feature. AS waits for the spot instance to be terminated before scaling out to reach the number of instances expected by the scaling group.</li>

Default value: FALSE.
        :rtype: bool
        """
        return self._CapacityRebalance

    @CapacityRebalance.setter
    def CapacityRebalance(self, CapacityRebalance):
        self._CapacityRebalance = CapacityRebalance

    @property
    def InstanceNameIndexSettings(self):
        """Instance name sequencing settings. If this parameter is not specified, the default is not enabled. When enabled, an incremental numeric sequence will be appended to the names of instances automatically created within the scaling group.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameIndexSettings`
        """
        return self._InstanceNameIndexSettings

    @InstanceNameIndexSettings.setter
    def InstanceNameIndexSettings(self, InstanceNameIndexSettings):
        self._InstanceNameIndexSettings = InstanceNameIndexSettings


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
        if params.get("InstanceNameIndexSettings") is not None:
            self._InstanceNameIndexSettings = InstanceNameIndexSettings()
            self._InstanceNameIndexSettings._deserialize(params.get("InstanceNameIndexSettings"))
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoScalingGroupId = None
        self._RequestId = None

    @property
    def AutoScalingGroupId(self):
        """Auto scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _ProjectId: Project ID of the launch configuration. The default project is used if it is left blank.
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
<li>POSTPAID_BY_HOUR: pay-as-you-go hourly</li>
<li>SPOTPAID: spot instance</li>
<li> CDCPAID: dedicated cluster</li>
        :type InstanceChargeType: str
        :param _InstanceMarketOptions: Market options of the instance, such as parameters related to spot instances. This parameter is required for spot instances.
        :type InstanceMarketOptions: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        :param _InstanceTypes: List of instance models. Different instance models specify different resource specifications. Up to 10 instance models can be supported.
`InstanceType` and `InstanceTypes` are mutually exclusive, and one and only one of them must be entered.
        :type InstanceTypes: list of str
        :param _CamRoleName: CAM role name. This parameter can be obtained from the `roleName` field returned by DescribeRoleList API.
        :type CamRoleName: str
        :param _InstanceTypesCheckPolicy: InstanceType verification policy, whose valid values include ALL and ANY, with the default value being ANY.
<li>ALL: Verification passes if all InstanceTypes are available; otherwise, a verification error will be reported.</li>
<li>ANY: Verification passes if any InstanceType is available; otherwise, a verification error will be reported.</li>

Common reasons for unavailable InstanceTypes include the InstanceType being sold out, and the corresponding cloud disk being sold out.
If a model in InstanceTypes does not exist or has been abolished, a verification error will be reported regardless of the valid values set for InstanceTypesCheckPolicy.
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
        :param _DiskTypePolicy: Cloud disk type selection policy, whose default value is ORIGINAL. Valid values:
<li>ORIGINAL: Use the set cloud disk type.</li>
<li>AUTOMATIC: Automatically select the currently available cloud disk type.</li>
        :type DiskTypePolicy: str
        :param _HpcClusterId: HPC ID<br>
Note: This field is default to empty
        :type HpcClusterId: str
        :param _IPv6InternetAccessible: IPv6 public network bandwidth configuration. If the IPv6 address is available in the new instance, public network bandwidth can be allocated to the IPv6 address. This parameter is invalid if `Ipv6AddressCount` of the scaling group associated with the launch configuration is 0.
        :type IPv6InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.IPv6InternetAccessible`
        :param _DisasterRecoverGroupIds: Placement group ID. Only one is allowed.
        :type DisasterRecoverGroupIds: list of str
        :param _ImageFamily: Image family name. Either image ID or image family name should be filled in, and only one of which can be filled.
        :type ImageFamily: str
        :param _DedicatedClusterId: CDC ID.
        :type DedicatedClusterId: str
        :param _Metadata: Custom metadata.
        :type Metadata: :class:`tencentcloud.autoscaling.v20180419.models.Metadata`
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
        self._ImageFamily = None
        self._DedicatedClusterId = None
        self._Metadata = None

    @property
    def LaunchConfigurationName(self):
        """Display name of the launch configuration, which can contain letters, digits, underscores and hyphens (-), and dots. Up to of 60 bytes allowed..
        :rtype: str
        """
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def ImageId(self):
        """[Image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are three types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><br/>You can obtain the image IDs in the [CVM console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE).</li><li>You can also use the [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response.</li>
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ProjectId(self):
        """Project ID of the launch configuration. The default project is used if it is left blank.
Note that this project ID is not the same as the project ID of the scaling group. 
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceType(self):
        """Instance model. Different instance models specify different resource specifications. The specific value can be obtained by calling the [DescribeInstanceTypeConfigs](https://intl.cloud.tencent.com/document/api/213/15749?from_cn_redirect=1) API to get the latest specification table or referring to the descriptions in [Instance Types](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1).
`InstanceType` and `InstanceTypes` are mutually exclusive, and one and only one of them must be entered.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        """System disk configuration of the instance. If this parameter is not specified, the default value will be used.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """Information of the instance's data disk configuration. If this parameter is not specified, no data disk is purchased by default. Up to 11 data disks can be supported.
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def InternetAccessible(self):
        """Configuration of public network bandwidth. If this parameter is not specified, 0 Mbps will be used by default.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def LoginSettings(self):
        """Login settings of the instance. You can use this parameter to set the login method, password, and key of the instance or keep the login settings of the original image. By default, a random password will be generated and sent to you via the Message Center.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.LoginSettings`
        """
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SecurityGroupIds(self):
        """The security group to which the instance belongs. This parameter can be obtained by calling the `SecurityGroupId` field in the returned value of [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808?from_cn_redirect=1). If this parameter is not specified, no security group will be bound by default.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def EnhancedService(self):
        """Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Security and Cloud Monitor. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled by default.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.EnhancedService`
        """
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def UserData(self):
        """Base64-encoded custom data of up to 16 KB.
        :rtype: str
        """
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def InstanceChargeType(self):
        """Instance billing mode. CVM instances take `POSTPAID_BY_HOUR` by default. Valid values:
<li>POSTPAID_BY_HOUR: pay-as-you-go hourly</li>
<li>SPOTPAID: spot instance</li>
<li> CDCPAID: dedicated cluster</li>
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceMarketOptions(self):
        """Market options of the instance, such as parameters related to spot instances. This parameter is required for spot instances.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        """
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def InstanceTypes(self):
        """List of instance models. Different instance models specify different resource specifications. Up to 10 instance models can be supported.
`InstanceType` and `InstanceTypes` are mutually exclusive, and one and only one of them must be entered.
        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def CamRoleName(self):
        """CAM role name. This parameter can be obtained from the `roleName` field returned by DescribeRoleList API.
        :rtype: str
        """
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def InstanceTypesCheckPolicy(self):
        """InstanceType verification policy, whose valid values include ALL and ANY, with the default value being ANY.
<li>ALL: Verification passes if all InstanceTypes are available; otherwise, a verification error will be reported.</li>
<li>ANY: Verification passes if any InstanceType is available; otherwise, a verification error will be reported.</li>

Common reasons for unavailable InstanceTypes include the InstanceType being sold out, and the corresponding cloud disk being sold out.
If a model in InstanceTypes does not exist or has been abolished, a verification error will be reported regardless of the valid values set for InstanceTypesCheckPolicy.
        :rtype: str
        """
        return self._InstanceTypesCheckPolicy

    @InstanceTypesCheckPolicy.setter
    def InstanceTypesCheckPolicy(self, InstanceTypesCheckPolicy):
        self._InstanceTypesCheckPolicy = InstanceTypesCheckPolicy

    @property
    def InstanceTags(self):
        """List of tags. This parameter is used to bind up to 10 tags to newly added instances.
        :rtype: list of InstanceTag
        """
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def Tags(self):
        """List of tags. You can specify tags that you want to bind to the launch configuration. Each launch configuration can have up to 30 tags.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HostNameSettings(self):
        """CVM hostname settings.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.HostNameSettings`
        """
        return self._HostNameSettings

    @HostNameSettings.setter
    def HostNameSettings(self, HostNameSettings):
        self._HostNameSettings = HostNameSettings

    @property
    def InstanceNameSettings(self):
        """Settings of CVM instance names
If this field is configured in a launch configuration, the `InstanceName` of a CVM created by the scaling group will be generated according to the configuration; otherwise, it will be in the `as-{{AutoScalingGroupName }}` format.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameSettings`
        """
        return self._InstanceNameSettings

    @InstanceNameSettings.setter
    def InstanceNameSettings(self, InstanceNameSettings):
        self._InstanceNameSettings = InstanceNameSettings

    @property
    def InstanceChargePrepaid(self):
        """Details of the monthly subscription, including the purchase period, auto-renewal. It is required if the `InstanceChargeType` is `PREPAID`.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def DiskTypePolicy(self):
        """Cloud disk type selection policy, whose default value is ORIGINAL. Valid values:
<li>ORIGINAL: Use the set cloud disk type.</li>
<li>AUTOMATIC: Automatically select the currently available cloud disk type.</li>
        :rtype: str
        """
        return self._DiskTypePolicy

    @DiskTypePolicy.setter
    def DiskTypePolicy(self, DiskTypePolicy):
        self._DiskTypePolicy = DiskTypePolicy

    @property
    def HpcClusterId(self):
        """HPC ID<br>
Note: This field is default to empty
        :rtype: str
        """
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def IPv6InternetAccessible(self):
        """IPv6 public network bandwidth configuration. If the IPv6 address is available in the new instance, public network bandwidth can be allocated to the IPv6 address. This parameter is invalid if `Ipv6AddressCount` of the scaling group associated with the launch configuration is 0.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.IPv6InternetAccessible`
        """
        return self._IPv6InternetAccessible

    @IPv6InternetAccessible.setter
    def IPv6InternetAccessible(self, IPv6InternetAccessible):
        self._IPv6InternetAccessible = IPv6InternetAccessible

    @property
    def DisasterRecoverGroupIds(self):
        """Placement group ID. Only one is allowed.
        :rtype: list of str
        """
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def ImageFamily(self):
        """Image family name. Either image ID or image family name should be filled in, and only one of which can be filled.
        :rtype: str
        """
        return self._ImageFamily

    @ImageFamily.setter
    def ImageFamily(self, ImageFamily):
        self._ImageFamily = ImageFamily

    @property
    def DedicatedClusterId(self):
        """CDC ID.
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def Metadata(self):
        """Custom metadata.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.Metadata`
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata


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
        self._ImageFamily = params.get("ImageFamily")
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        if params.get("Metadata") is not None:
            self._Metadata = Metadata()
            self._Metadata._deserialize(params.get("Metadata"))
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LaunchConfigurationId = None
        self._RequestId = None

    @property
    def LaunchConfigurationId(self):
        """This parameter is returned when a launch configuration is created through this API, indicating the launch configuration ID.
        :rtype: str
        """
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Auto scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def LifecycleHookName(self):
        """Lifecycle hook name, which can contain Chinese characters, letters, numbers, underscores (_), hyphens (-), and periods (.) with a maximum length of 128 bytes.
        :rtype: str
        """
        return self._LifecycleHookName

    @LifecycleHookName.setter
    def LifecycleHookName(self, LifecycleHookName):
        self._LifecycleHookName = LifecycleHookName

    @property
    def LifecycleTransition(self):
        """Scenario for the lifecycle hook. Valid values: "INSTANCE_LAUNCHING" and "INSTANCE_TERMINATING"
        :rtype: str
        """
        return self._LifecycleTransition

    @LifecycleTransition.setter
    def LifecycleTransition(self, LifecycleTransition):
        self._LifecycleTransition = LifecycleTransition

    @property
    def DefaultResult(self):
        """Defined actions when lifecycle hook times out. Valid values: "CONTINUE" and "ABANDON". Default value: "CONTINUE"
        :rtype: str
        """
        return self._DefaultResult

    @DefaultResult.setter
    def DefaultResult(self, DefaultResult):
        self._DefaultResult = DefaultResult

    @property
    def HeartbeatTimeout(self):
        """The maximum length of time (in seconds) that can elapse before the lifecycle hook times out. Value range: 30-7200. Default value: 300
        :rtype: int
        """
        return self._HeartbeatTimeout

    @HeartbeatTimeout.setter
    def HeartbeatTimeout(self, HeartbeatTimeout):
        self._HeartbeatTimeout = HeartbeatTimeout

    @property
    def NotificationMetadata(self):
        """Additional information of a notification that Auto Scaling sends to targets. This parameter is set when you configure a notification (default value: ""). Up to 1024 characters are allowed.
        :rtype: str
        """
        return self._NotificationMetadata

    @NotificationMetadata.setter
    def NotificationMetadata(self, NotificationMetadata):
        self._NotificationMetadata = NotificationMetadata

    @property
    def NotificationTarget(self):
        """Notification target. `NotificationTarget` and `LifecycleCommand` cannot be specified at the same time.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.NotificationTarget`
        """
        return self._NotificationTarget

    @NotificationTarget.setter
    def NotificationTarget(self, NotificationTarget):
        self._NotificationTarget = NotificationTarget

    @property
    def LifecycleTransitionType(self):
        """The scenario where the lifecycle hook is applied. `EXTENSION`: the lifecycle hook will be triggered when AttachInstances, DetachInstances or RemoveInstaces is called. `NORMAL`: the lifecycle hook is not triggered by the above APIs. 
        :rtype: str
        """
        return self._LifecycleTransitionType

    @LifecycleTransitionType.setter
    def LifecycleTransitionType(self, LifecycleTransitionType):
        self._LifecycleTransitionType = LifecycleTransitionType

    @property
    def LifecycleCommand(self):
        """Remote command execution object. `NotificationTarget` and `LifecycleCommand` cannot be specified at the same time.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.LifecycleCommand`
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LifecycleHookId = None
        self._RequestId = None

    @property
    def LifecycleHookId(self):
        """Lifecycle hook ID
        :rtype: str
        """
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Auto scaling group ID.
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def NotificationTypes(self):
        """Notification type, i.e., the set of types of notifications to be subscribed to. Value range:
<li>SCALE_OUT_SUCCESSFUL: scale-out succeeded</li>
<li>SCALE_OUT_FAILED: scale-out failed</li>
<li>SCALE_IN_SUCCESSFUL: scale-in succeeded</li>
<li>SCALE_IN_FAILED: scale-in failed</li>
<li>REPLACE_UNHEALTHY_INSTANCE_SUCCESSFUL: unhealthy instance replacement succeeded</li>
<li>REPLACE_UNHEALTHY_INSTANCE_FAILED: unhealthy instance replacement failed</li>
        :rtype: list of str
        """
        return self._NotificationTypes

    @NotificationTypes.setter
    def NotificationTypes(self, NotificationTypes):
        self._NotificationTypes = NotificationTypes

    @property
    def NotificationUserGroupIds(self):
        """Notification group ID, which is the set of user group IDs. You can query the user group IDs through the [ListGroups](https://intl.cloud.tencent.com/document/product/598/34589?from_cn_redirect=1) API.
        :rtype: list of str
        """
        return self._NotificationUserGroupIds

    @NotificationUserGroupIds.setter
    def NotificationUserGroupIds(self, NotificationUserGroupIds):
        self._NotificationUserGroupIds = NotificationUserGroupIds

    @property
    def TargetType(self):
        """Notification receiver type. Valid values:
<br><li>USER_GROUP:User group
<br><li>CMQ_QUEUE:CMQ queue
<br><li>CMQ_TOPIC:CMQ topic
<br><li>TDMQ_CMQ_TOPIC:TDMQ CMQ topic
<br><li>TDMQ_CMQ_QUEUE:TDMQ CMQ queue

Default value: `USER_GROUP`.
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def QueueName(self):
        """CMQ queue name. This parameter is required when `TargetType` is `CMQ_QUEUE` or `TDMQ_CMQ_QUEUE`.
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def TopicName(self):
        """CMQ topic name. This parameter is required when `TargetType` is `CMQ_TOPIC` or `TDMQ_CMQ_TOPIC`.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoScalingNotificationId = None
        self._RequestId = None

    @property
    def AutoScalingNotificationId(self):
        """Notification ID.
        :rtype: str
        """
        return self._AutoScalingNotificationId

    @AutoScalingNotificationId.setter
    def AutoScalingNotificationId(self, AutoScalingNotificationId):
        self._AutoScalingNotificationId = AutoScalingNotificationId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _AdjustmentType: The method to adjust the desired capacity after the alarm is triggered. It is only available when `ScalingPolicyType` is `Simple`. Valid values: <br><li>`CHANGE_IN_CAPACITY`: Increase or decrease the desired capacity </li><li>`EXACT_CAPACITY`: Adjust to the specified desired capacity </li> <li>`PERCENT_CHANGE_IN_CAPACITY`: Adjust the desired capacity by percentage </li>
        :type AdjustmentType: str
        :param _AdjustmentValue: Adjustment value for the expected number of instances after an alarm is triggered, which is applicable only to simple policies.
<li>When AdjustmentType is set to CHANGE_IN_CAPACITY, a positive value of AdjustmentValue indicates an increase in the number of instances after the alarm is triggered, while a negative value indicates a decrease in the number of instances after the alarm is triggered.</li>
<li>When AdjustmentType is set to EXACT_CAPACITY, the value of AdjustmentValue indicates the new desired number of instances after the alarm is triggered. It should be greater than or equal to 0.</li>
<li>When AdjustmentType is set to PERCENT_CHANGE_IN_CAPACITY, a positive value of AdjustmentValue indicates an increase in the number of instances by a percentage after the alarm is triggered, while a negative value indicates a decrease in the number of instances by a percentage after the alarm is triggered. Unit: %.</li>
        :type AdjustmentValue: int
        :param _Cooldown: Cooldown period (in seconds). This parameter is only applicable to a simple policy. Default value: 300.
        :type Cooldown: int
        :param _MetricAlarm: Alarm monitoring metric. It is only available when `ScalingPolicyType` is `Simple`.
        :type MetricAlarm: :class:`tencentcloud.autoscaling.v20180419.models.MetricAlarm`
        :param _PredefinedMetricType: Predefined monitoring item, applicable only to target tracking policies. Valid values:
<li>ASG_AVG_CPU_UTILIZATION: average CPU utilization</li>
<li>ASG_AVG_LAN_TRAFFIC_OUT: average outbound private network bandwidth</li>
<li>ASG_AVG_LAN_TRAFFIC_IN: average inbound private network bandwidth</li>
<li>ASG_AVG_WAN_TRAFFIC_OUT: average outbound public network bandwidth</li>
<li>ASG_AVG_WAN_TRAFFIC_IN: average inbound public network bandwidth</li>
        :type PredefinedMetricType: str
        :param _TargetValue: Target value, which is applicable only to target tracking policies.
<li>ASG_AVG_CPU_UTILIZATION: value range: [1, 100); unit: %.</li>
<li>ASG_AVG_LAN_TRAFFIC_OUT: value range: > 0; unit: Mbps.</li>
<li>ASG_AVG_LAN_TRAFFIC_IN: value range: > 0; unit: Mbps.</li>
<li>ASG_AVG_WAN_TRAFFIC_OUT: value range: > 0; unit: Mbps.</li>
<li>ASG_AVG_WAN_TRAFFIC_IN: value range: > 0; unit: Mbps.</li>
        :type TargetValue: int
        :param _EstimatedInstanceWarmup: Instance warm-up period (in seconds). It is only available when `ScalingPolicyType` is `TARGET_TRACKING`. Value range: 0-3600. Default value: 300.
        :type EstimatedInstanceWarmup: int
        :param _DisableScaleIn: Whether to disable scale-in, which is applicable only to target tracking policies. Default value: false. Valid values:
<li>true: Target tracking policies trigger only scale-out.</li>
<li>false: Target tracking policies trigger both scale-out and scale-in.</li>
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
        """Auto scaling group ID.
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ScalingPolicyName(self):
        """Alarm trigger policy name.
        :rtype: str
        """
        return self._ScalingPolicyName

    @ScalingPolicyName.setter
    def ScalingPolicyName(self, ScalingPolicyName):
        self._ScalingPolicyName = ScalingPolicyName

    @property
    def ScalingPolicyType(self):
        """Scaling policy type. Valid values: <br><li>`SIMPLE` (default): A simple policy</li><li>`TARGET_TRACKING`: A target tracking policy</li>.
        :rtype: str
        """
        return self._ScalingPolicyType

    @ScalingPolicyType.setter
    def ScalingPolicyType(self, ScalingPolicyType):
        self._ScalingPolicyType = ScalingPolicyType

    @property
    def AdjustmentType(self):
        """The method to adjust the desired capacity after the alarm is triggered. It is only available when `ScalingPolicyType` is `Simple`. Valid values: <br><li>`CHANGE_IN_CAPACITY`: Increase or decrease the desired capacity </li><li>`EXACT_CAPACITY`: Adjust to the specified desired capacity </li> <li>`PERCENT_CHANGE_IN_CAPACITY`: Adjust the desired capacity by percentage </li>
        :rtype: str
        """
        return self._AdjustmentType

    @AdjustmentType.setter
    def AdjustmentType(self, AdjustmentType):
        self._AdjustmentType = AdjustmentType

    @property
    def AdjustmentValue(self):
        """Adjustment value for the expected number of instances after an alarm is triggered, which is applicable only to simple policies.
<li>When AdjustmentType is set to CHANGE_IN_CAPACITY, a positive value of AdjustmentValue indicates an increase in the number of instances after the alarm is triggered, while a negative value indicates a decrease in the number of instances after the alarm is triggered.</li>
<li>When AdjustmentType is set to EXACT_CAPACITY, the value of AdjustmentValue indicates the new desired number of instances after the alarm is triggered. It should be greater than or equal to 0.</li>
<li>When AdjustmentType is set to PERCENT_CHANGE_IN_CAPACITY, a positive value of AdjustmentValue indicates an increase in the number of instances by a percentage after the alarm is triggered, while a negative value indicates a decrease in the number of instances by a percentage after the alarm is triggered. Unit: %.</li>
        :rtype: int
        """
        return self._AdjustmentValue

    @AdjustmentValue.setter
    def AdjustmentValue(self, AdjustmentValue):
        self._AdjustmentValue = AdjustmentValue

    @property
    def Cooldown(self):
        """Cooldown period (in seconds). This parameter is only applicable to a simple policy. Default value: 300.
        :rtype: int
        """
        return self._Cooldown

    @Cooldown.setter
    def Cooldown(self, Cooldown):
        self._Cooldown = Cooldown

    @property
    def MetricAlarm(self):
        """Alarm monitoring metric. It is only available when `ScalingPolicyType` is `Simple`.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.MetricAlarm`
        """
        return self._MetricAlarm

    @MetricAlarm.setter
    def MetricAlarm(self, MetricAlarm):
        self._MetricAlarm = MetricAlarm

    @property
    def PredefinedMetricType(self):
        """Predefined monitoring item, applicable only to target tracking policies. Valid values:
<li>ASG_AVG_CPU_UTILIZATION: average CPU utilization</li>
<li>ASG_AVG_LAN_TRAFFIC_OUT: average outbound private network bandwidth</li>
<li>ASG_AVG_LAN_TRAFFIC_IN: average inbound private network bandwidth</li>
<li>ASG_AVG_WAN_TRAFFIC_OUT: average outbound public network bandwidth</li>
<li>ASG_AVG_WAN_TRAFFIC_IN: average inbound public network bandwidth</li>
        :rtype: str
        """
        return self._PredefinedMetricType

    @PredefinedMetricType.setter
    def PredefinedMetricType(self, PredefinedMetricType):
        self._PredefinedMetricType = PredefinedMetricType

    @property
    def TargetValue(self):
        """Target value, which is applicable only to target tracking policies.
<li>ASG_AVG_CPU_UTILIZATION: value range: [1, 100); unit: %.</li>
<li>ASG_AVG_LAN_TRAFFIC_OUT: value range: > 0; unit: Mbps.</li>
<li>ASG_AVG_LAN_TRAFFIC_IN: value range: > 0; unit: Mbps.</li>
<li>ASG_AVG_WAN_TRAFFIC_OUT: value range: > 0; unit: Mbps.</li>
<li>ASG_AVG_WAN_TRAFFIC_IN: value range: > 0; unit: Mbps.</li>
        :rtype: int
        """
        return self._TargetValue

    @TargetValue.setter
    def TargetValue(self, TargetValue):
        self._TargetValue = TargetValue

    @property
    def EstimatedInstanceWarmup(self):
        """Instance warm-up period (in seconds). It is only available when `ScalingPolicyType` is `TARGET_TRACKING`. Value range: 0-3600. Default value: 300.
        :rtype: int
        """
        return self._EstimatedInstanceWarmup

    @EstimatedInstanceWarmup.setter
    def EstimatedInstanceWarmup(self, EstimatedInstanceWarmup):
        self._EstimatedInstanceWarmup = EstimatedInstanceWarmup

    @property
    def DisableScaleIn(self):
        """Whether to disable scale-in, which is applicable only to target tracking policies. Default value: false. Valid values:
<li>true: Target tracking policies trigger only scale-out.</li>
<li>false: Target tracking policies trigger both scale-out and scale-in.</li>
        :rtype: bool
        """
        return self._DisableScaleIn

    @DisableScaleIn.setter
    def DisableScaleIn(self, DisableScaleIn):
        self._DisableScaleIn = DisableScaleIn

    @property
    def NotificationUserGroupIds(self):
        """This parameter is diused. Please use [CreateNotificationConfiguration](https://intl.cloud.tencent.com/document/api/377/33185?from_cn_redirect=1) instead.
Notification group ID, which is the set of user group IDs.
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoScalingPolicyId = None
        self._RequestId = None

    @property
    def AutoScalingPolicyId(self):
        """Alarm trigger policy ID.
        :rtype: str
        """
        return self._AutoScalingPolicyId

    @AutoScalingPolicyId.setter
    def AutoScalingPolicyId(self, AutoScalingPolicyId):
        self._AutoScalingPolicyId = AutoScalingPolicyId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Auto scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ScheduledActionName(self):
        """Scheduled task name, which can only contain letters, numbers, underscores, hyphens ("-"), and decimal points with a maximum length of 60 bytes and must be unique in an auto scaling group.
        :rtype: str
        """
        return self._ScheduledActionName

    @ScheduledActionName.setter
    def ScheduledActionName(self, ScheduledActionName):
        self._ScheduledActionName = ScheduledActionName

    @property
    def MaxSize(self):
        """The maximum number of instances set for the auto scaling group when the scheduled task is triggered.
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        """The minimum number of instances set for the auto scaling group when the scheduled task is triggered.
        :rtype: int
        """
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def DesiredCapacity(self):
        """The desired number of instances set for the auto scaling group when the scheduled task is triggered.
        :rtype: int
        """
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def StartTime(self):
        """Initial triggered time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard. <br><br>This parameter and `Recurrence` need to be specified at the same time. After the end time, the scheduled task will no longer take effect.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Recurrence(self):
        """Repeating mode of the scheduled task, which is in standard cron format. <br><br>This parameter and `EndTime` need to be specified at the same time.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ScheduledActionId = None
        self._RequestId = None

    @property
    def ScheduledActionId(self):
        """Scheduled task ID
        :rtype: str
        """
        return self._ScheduledActionId

    @ScheduledActionId.setter
    def ScheduledActionId(self, ScheduledActionId):
        self._ScheduledActionId = ScheduledActionId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _DiskType: Data disk type. For restrictions on the data disk type, see [cloud block storage types](https://intl.cloud.tencent.com/document/product/362/2353?from_cn_redirect=1). Valid values:
<li>LOCAL_BASIC: Local Disk.</li>
<li>LOCAL_SSD: Local SSD.</li>
<li>CLOUD_BASIC: Basic Cloud Disk.</li>
<li>CLOUD_PREMIUM: Premium Disk.</li>
<li>CLOUD_SSD: Cloud SSD.</li>
<li>CLOUD_HSSD: Enhanced SSD.</li>
<li>CLOUD_TSSD: Tremendous SSD.</li>
The default value is consistent with the system disk type (SystemDisk.DiskType).
        :type DiskType: str
        :param _DiskSize: Data disk size, in GB. The minimum adjustment step size is 10 GB. The value range varies according to the data disk type. For specific restrictions, see [CVM instance configuration](https://intl.cloud.tencent.com/document/product/213/2177?from_cn_redirect=1). Default value: 0, which means that no data disk is purchased. For more restrictions, see the product documentation.
        :type DiskSize: int
        :param _SnapshotId: Data disk snapshot ID, such as `snap-l8psqwnt`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SnapshotId: str
        :param _DeleteWithInstance: Whether the data disk is terminated along with the instance. Valid values:
<li>TRUE: When the instance is terminated, the data disk is also terminated. This option is only supported for hourly postpaid cloud disks.</li>
<li>FALSE: When the instance is terminated, the data disk is retained.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeleteWithInstance: bool
        :param _Encrypt: Whether the data disk is encrypted. Valid values:
<li>TRUE: Encrypted.</li>
<li>FALSE: Not encrypted.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Encrypt: bool
        :param _ThroughputPerformance: Cloud disk performance (MB/s). This parameter is used to purchase extra performance for the cloud disk. For details on the feature and limits, see [Enhanced SSD Performance](https://intl.cloud.tencent.com/document/product/362/51896?from_cn_redirect=1#. E5.A2.9E.E5.BC.BA.E5.9E.8B-ssd-.E4.BA.91.E7.A1.AC.E7.9B.98.E9.A2.9D.E5.A4.96 .E6.80.A7.E8.83.BD).
This feature is only available to enhanced SSD (`CLOUD_HSSD`) and tremendous SSD (`CLOUD_TSSD`) disks with a capacity greater than 460 GB.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ThroughputPerformance: int
        :param _BurstPerformance: Burst performance: Whether to enable burst performance. The default value is false.

Note: This feature is in beta test and requires a ticket to be submitted for usage.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BurstPerformance: bool
        """
        self._DiskType = None
        self._DiskSize = None
        self._SnapshotId = None
        self._DeleteWithInstance = None
        self._Encrypt = None
        self._ThroughputPerformance = None
        self._BurstPerformance = None

    @property
    def DiskType(self):
        """Data disk type. For restrictions on the data disk type, see [cloud block storage types](https://intl.cloud.tencent.com/document/product/362/2353?from_cn_redirect=1). Valid values:
<li>LOCAL_BASIC: Local Disk.</li>
<li>LOCAL_SSD: Local SSD.</li>
<li>CLOUD_BASIC: Basic Cloud Disk.</li>
<li>CLOUD_PREMIUM: Premium Disk.</li>
<li>CLOUD_SSD: Cloud SSD.</li>
<li>CLOUD_HSSD: Enhanced SSD.</li>
<li>CLOUD_TSSD: Tremendous SSD.</li>
The default value is consistent with the system disk type (SystemDisk.DiskType).
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """Data disk size, in GB. The minimum adjustment step size is 10 GB. The value range varies according to the data disk type. For specific restrictions, see [CVM instance configuration](https://intl.cloud.tencent.com/document/product/213/2177?from_cn_redirect=1). Default value: 0, which means that no data disk is purchased. For more restrictions, see the product documentation.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def SnapshotId(self):
        """Data disk snapshot ID, such as `snap-l8psqwnt`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DeleteWithInstance(self):
        """Whether the data disk is terminated along with the instance. Valid values:
<li>TRUE: When the instance is terminated, the data disk is also terminated. This option is only supported for hourly postpaid cloud disks.</li>
<li>FALSE: When the instance is terminated, the data disk is retained.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def Encrypt(self):
        """Whether the data disk is encrypted. Valid values:
<li>TRUE: Encrypted.</li>
<li>FALSE: Not encrypted.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def ThroughputPerformance(self):
        """Cloud disk performance (MB/s). This parameter is used to purchase extra performance for the cloud disk. For details on the feature and limits, see [Enhanced SSD Performance](https://intl.cloud.tencent.com/document/product/362/51896?from_cn_redirect=1#. E5.A2.9E.E5.BC.BA.E5.9E.8B-ssd-.E4.BA.91.E7.A1.AC.E7.9B.98.E9.A2.9D.E5.A4.96 .E6.80.A7.E8.83.BD).
This feature is only available to enhanced SSD (`CLOUD_HSSD`) and tremendous SSD (`CLOUD_TSSD`) disks with a capacity greater than 460 GB.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def BurstPerformance(self):
        """Burst performance: Whether to enable burst performance. The default value is false.

Note: This feature is in beta test and requires a ticket to be submitted for usage.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._BurstPerformance

    @BurstPerformance.setter
    def BurstPerformance(self, BurstPerformance):
        self._BurstPerformance = BurstPerformance


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._SnapshotId = params.get("SnapshotId")
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._Encrypt = params.get("Encrypt")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        self._BurstPerformance = params.get("BurstPerformance")
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
        """Auto scaling group ID
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """ID of the launch configuration to be deleted.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Lifecycle hook ID
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """ID of the notification to be deleted.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """ID of the alarm policy to be deleted.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """ID of the scheduled task to be deleted.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MaxNumberOfLaunchConfigurations = None
        self._NumberOfLaunchConfigurations = None
        self._MaxNumberOfAutoScalingGroups = None
        self._NumberOfAutoScalingGroups = None
        self._RequestId = None

    @property
    def MaxNumberOfLaunchConfigurations(self):
        """Maximum number of launch configurations allowed for creation by the user account
        :rtype: int
        """
        return self._MaxNumberOfLaunchConfigurations

    @MaxNumberOfLaunchConfigurations.setter
    def MaxNumberOfLaunchConfigurations(self, MaxNumberOfLaunchConfigurations):
        self._MaxNumberOfLaunchConfigurations = MaxNumberOfLaunchConfigurations

    @property
    def NumberOfLaunchConfigurations(self):
        """Current number of launch configurations under the user account
        :rtype: int
        """
        return self._NumberOfLaunchConfigurations

    @NumberOfLaunchConfigurations.setter
    def NumberOfLaunchConfigurations(self, NumberOfLaunchConfigurations):
        self._NumberOfLaunchConfigurations = NumberOfLaunchConfigurations

    @property
    def MaxNumberOfAutoScalingGroups(self):
        """Maximum number of auto scaling groups allowed for creation by the user account
        :rtype: int
        """
        return self._MaxNumberOfAutoScalingGroups

    @MaxNumberOfAutoScalingGroups.setter
    def MaxNumberOfAutoScalingGroups(self, MaxNumberOfAutoScalingGroups):
        self._MaxNumberOfAutoScalingGroups = MaxNumberOfAutoScalingGroups

    @property
    def NumberOfAutoScalingGroups(self):
        """Current number of auto scaling groups under the user account
        :rtype: int
        """
        return self._NumberOfAutoScalingGroups

    @NumberOfAutoScalingGroups.setter
    def NumberOfAutoScalingGroups(self, NumberOfAutoScalingGroups):
        self._NumberOfAutoScalingGroups = NumberOfAutoScalingGroups

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Queries by one or more scaling activity IDs in the format of `asa-5l2ejpfo`. The maximum quantity per request is 100. This parameter does not support specifying both `ActivityIds` and `Filters` at the same time.
        :rtype: list of str
        """
        return self._ActivityIds

    @ActivityIds.setter
    def ActivityIds(self, ActivityIds):
        self._ActivityIds = ActivityIds

    @property
    def Filters(self):
        """Filter.
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
<li> activity-status-code - String - Required: No - (Filter) Filter by scaling activity status . (INIT: initializing | RUNNING: running | SUCCESSFUL: succeeded | PARTIALLY_SUCCESSFUL: partially succeeded | FAILED: failed | CANCELLED: canceled)</li>
<li> activity-type - String - Required: No - (Filter) Filter by scaling activity type. (SCALE_OUT: scale-out | SCALE_IN: scale-in | ATTACH_INSTANCES: adding an instance | REMOVE_INSTANCES: terminating an instance | DETACH_INSTANCES: removing an instance | TERMINATE_INSTANCES_UNEXPECTEDLY: terminating an instance in the CVM console | REPLACE_UNHEALTHY_INSTANCE: replacing an unhealthy instance | UPDATE_LOAD_BALANCERS: updating a load balancer)</li>
<li> activity-id - String - Required: No - (Filter) Filter by scaling activity ID.</li>
The maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `ActivityIds` and `Filters` at the same time.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def StartTime(self):
        """The earliest start time of the scaling activity, which will be ignored if ActivityIds is specified. The value is in `UTC time` in the format of `YYYY-MM-DDThh:mm:ssZ` according to the `ISO8601` standard.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """The latest end time of the scaling activity, which will be ignored if ActivityIds is specified. The value is in `UTC time` in the format of `YYYY-MM-DDThh:mm:ssZ` according to the `ISO8601` standard.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ActivitySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible scaling activities.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ActivitySet(self):
        """Information set of eligible scaling activities.
        :rtype: list of Activity
        """
        return self._ActivitySet

    @ActivitySet.setter
    def ActivitySet(self, ActivitySet):
        self._ActivitySet = ActivitySet

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """List of scaling groups to be queried. Upper limit: 100.
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoScalingAdviceSet = None
        self._RequestId = None

    @property
    def AutoScalingAdviceSet(self):
        """A collection of suggestions for scaling group configurations.
        :rtype: list of AutoScalingAdvice
        """
        return self._AutoScalingAdviceSet

    @AutoScalingAdviceSet.setter
    def AutoScalingAdviceSet(self, AutoScalingAdviceSet):
        self._AutoScalingAdviceSet = AutoScalingAdviceSet

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _AutoScalingGroupIds: ID list of auto scaling groups.
        :type AutoScalingGroupIds: list of str
        :param _ExcludeCancelledActivity: Excludes cancelled type activities when querying. Default value is false, which means cancelled type activities are not excluded.
        :type ExcludeCancelledActivity: bool
        """
        self._AutoScalingGroupIds = None
        self._ExcludeCancelledActivity = None

    @property
    def AutoScalingGroupIds(self):
        """ID list of auto scaling groups.
        :rtype: list of str
        """
        return self._AutoScalingGroupIds

    @AutoScalingGroupIds.setter
    def AutoScalingGroupIds(self, AutoScalingGroupIds):
        self._AutoScalingGroupIds = AutoScalingGroupIds

    @property
    def ExcludeCancelledActivity(self):
        """Excludes cancelled type activities when querying. Default value is false, which means cancelled type activities are not excluded.
        :rtype: bool
        """
        return self._ExcludeCancelledActivity

    @ExcludeCancelledActivity.setter
    def ExcludeCancelledActivity(self, ExcludeCancelledActivity):
        self._ExcludeCancelledActivity = ExcludeCancelledActivity


    def _deserialize(self, params):
        self._AutoScalingGroupIds = params.get("AutoScalingGroupIds")
        self._ExcludeCancelledActivity = params.get("ExcludeCancelledActivity")
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivitySet = None
        self._RequestId = None

    @property
    def ActivitySet(self):
        """Information set of eligible scaling activities. Scaling groups without scaling activities are not returned. For example, if there are 50 auto scaling group IDs but only 45 records are returned, it indicates that 5 of the auto scaling groups do not have scaling activities.
        :rtype: list of Activity
        """
        return self._ActivitySet

    @ActivitySet.setter
    def ActivitySet(self, ActivitySet):
        self._ActivitySet = ActivitySet

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Queries by one or more auto scaling group IDs in the format of `asg-nkdwoui0`. The maximum quantity per request is 100. This parameter does not support specifying both `AutoScalingGroupIds` and `Filters` at the same time.
        :rtype: list of str
        """
        return self._AutoScalingGroupIds

    @AutoScalingGroupIds.setter
    def AutoScalingGroupIds(self, AutoScalingGroupIds):
        self._AutoScalingGroupIds = AutoScalingGroupIds

    @property
    def Filters(self):
        """Filters.
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
<li> auto-scaling-group-name - String - Required: No - (Filter) Filter by auto scaling group name.</li>
<li> vague-auto-scaling-group-name - String - Required: No - (Filter) Fuzzy search by auto scaling group name.</li>
<li> launch-configuration-id - String - Required: No - (Filter) Filter by launch configuration ID.</li>
<li> tag-key - String - Required: No - (Filter) Filter by tag key.</li>
<li> tag-value - String - Required: No - (Filter) Filter by tag value.</li>
<li> tag:tag-key - String - Required: No - (Filter) Filter by tag key-value pair. The tag-key should be replaced with a specified tag key. For more information, see example 2.</li>
The maximum number of `Filters` in each request is 10. The upper limit for `Filter.Values` is 5. This parameter cannot specify `AutoScalingGroupIds` and `Filters` at the same time.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoScalingGroupSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AutoScalingGroupSet(self):
        """List of auto scaling group details.
        :rtype: list of AutoScalingGroup
        """
        return self._AutoScalingGroupSet

    @AutoScalingGroupSet.setter
    def AutoScalingGroupSet(self, AutoScalingGroupSet):
        self._AutoScalingGroupSet = AutoScalingGroupSet

    @property
    def TotalCount(self):
        """Number of eligible auto scaling groups.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """IDs of the CVM instances to query. Up to 100 IDs can be queried at one time. `InstanceIds` and `Filters` can not be both specified.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Filters(self):
        """Filter.
<li> instance-id - String - Required: No - (Filter) Filter by instance ID.</li>
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
The maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `InstanceIds` and `Filters` at the same time.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """The number of returned results. Default value: `20`. Maximum value: `100`. For more information on `Limit`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoScalingInstanceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AutoScalingInstanceSet(self):
        """List of instance details.
        :rtype: list of Instance
        """
        return self._AutoScalingInstanceSet

    @AutoScalingInstanceSet.setter
    def AutoScalingInstanceSet(self, AutoScalingInstanceSet):
        self._AutoScalingInstanceSet = AutoScalingInstanceSet

    @property
    def TotalCount(self):
        """Number of eligible instances.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _Filters: Filter criteria

<li>launch-configuration-id - String - required: no - (filter condition) filter by launch configuration ID.</li>
<li>launch-configuration-name - String - required: no - (filter condition) filter by launch configuration name.</li>
<li>vague-launch-configuration-name - String - required: no - (filter condition) fuzzy search by launch configuration name.</li>
<li>tag-key - String - required: no - (filter condition) filter by tag key.</li>
<li>tag-value - String - required: no - (filter condition) filter by tag value.</li>
<li>tag:tag-key - String - required: no - (filter condition) filter by Tag key-value pair. Replace tag-key with a specific tag key. See Example 3 for usage.</li>
The maximum number of `Filters` per request is 10, and the maximum number of `Filter.Values` is 5. The parameter does not support specifying both `LaunchConfigurationIds` and `Filters`.
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
        """Queries by one or more launch configuration IDs in the format of `asc-ouy1ax38`. The maximum quantity per request is 100. This parameter does not support specifying both `LaunchConfigurationIds` and `Filters` at the same time.
        :rtype: list of str
        """
        return self._LaunchConfigurationIds

    @LaunchConfigurationIds.setter
    def LaunchConfigurationIds(self, LaunchConfigurationIds):
        self._LaunchConfigurationIds = LaunchConfigurationIds

    @property
    def Filters(self):
        """Filter criteria

<li>launch-configuration-id - String - required: no - (filter condition) filter by launch configuration ID.</li>
<li>launch-configuration-name - String - required: no - (filter condition) filter by launch configuration name.</li>
<li>vague-launch-configuration-name - String - required: no - (filter condition) fuzzy search by launch configuration name.</li>
<li>tag-key - String - required: no - (filter condition) filter by tag key.</li>
<li>tag-value - String - required: no - (filter condition) filter by tag value.</li>
<li>tag:tag-key - String - required: no - (filter condition) filter by Tag key-value pair. Replace tag-key with a specific tag key. See Example 3 for usage.</li>
The maximum number of `Filters` per request is 10, and the maximum number of `Filter.Values` is 5. The parameter does not support specifying both `LaunchConfigurationIds` and `Filters`.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """The number of returned results. Default value: `20`. Maximum value: `100`. For more information on `Limit`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """The offset. Default value: `0`. For more information on `Offset`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._LaunchConfigurationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible launch configurations.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LaunchConfigurationSet(self):
        """List of launch configuration details.
        :rtype: list of LaunchConfiguration
        """
        return self._LaunchConfigurationSet

    @LaunchConfigurationSet.setter
    def LaunchConfigurationSet(self, LaunchConfigurationSet):
        self._LaunchConfigurationSet = LaunchConfigurationSet

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Queries by one or more lifecycle hook IDs in the format of `ash-8azjzxcl`. The maximum quantity per request is 100. This parameter does not support specifying both `LifecycleHookIds` and `Filters` at the same time.
        :rtype: list of str
        """
        return self._LifecycleHookIds

    @LifecycleHookIds.setter
    def LifecycleHookIds(self, LifecycleHookIds):
        self._LifecycleHookIds = LifecycleHookIds

    @property
    def Filters(self):
        """Filters.
<li> `lifecycle-hook-id` - String - Required: No - (Filter) Filter by lifecycle hook ID.</li>
<li> `lifecycle-hook-name` - String - Required: No - (Filter) Filter by lifecycle hook name.</li>
<li> `auto-scaling-group-id` - String - Required: No - (Filter) Filter by scaling group ID.</li>
Up to 10 filters can be included in a request and up to 5 values for each filter. It cannot be specified with `LifecycleHookIds` at the same time.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LifecycleHookSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def LifecycleHookSet(self):
        """Array of lifecycle hooks
        :rtype: list of LifecycleHook
        """
        return self._LifecycleHookSet

    @LifecycleHookSet.setter
    def LifecycleHookSet(self, LifecycleHookSet):
        self._LifecycleHookSet = LifecycleHookSet

    @property
    def TotalCount(self):
        """Total quantity
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Queries by one or more notification IDs in the format of asn-2sestqbr. The maximum number of instances per request is 100. This parameter does not support specifying both `AutoScalingNotificationIds` and `Filters` at the same time.
        :rtype: list of str
        """
        return self._AutoScalingNotificationIds

    @AutoScalingNotificationIds.setter
    def AutoScalingNotificationIds(self, AutoScalingNotificationIds):
        self._AutoScalingNotificationIds = AutoScalingNotificationIds

    @property
    def Filters(self):
        """Filter.
<li> auto-scaling-notification-id - String - Required: No - (Filter) Filter by notification ID.</li>
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
The maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `AutoScalingNotificationIds` and `Filters` at the same time.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AutoScalingNotificationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible notifications.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AutoScalingNotificationSet(self):
        """List of AS event notification details.
        :rtype: list of AutoScalingNotification
        """
        return self._AutoScalingNotificationSet

    @AutoScalingNotificationSet.setter
    def AutoScalingNotificationSet(self, AutoScalingNotificationSet):
        self._AutoScalingNotificationSet = AutoScalingNotificationSet

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class DescribeRefreshActivitiesRequest(AbstractModel):
    """DescribeRefreshActivities request structure.

    """

    def __init__(self):
        r"""
        :param _RefreshActivityIds: List of refresh activity IDs. IDs are formatted like: 'asr-5l2ejpfo'. The upper limit per request is 100. Parameters do not support specifying both RefreshActivityIds and Filters simultaneously.
        :type RefreshActivityIds: list of str
        :param _Filters: Filter criteria

<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
<li> refresh-activity-status-code - String - Required: No - (Filter)Filter based on refresh activity status. (INIT: Initialization | RUNNING:Running | SUCCESSFUL: Successful Activity | FAILED_PAUSE: Failed & Paused | AUTO_PAUSE: Auto Paused | MANUAL_PAUSE: Manually Paused | CANCELLED: Activity Cancelled | FAILED: Activity Failed)</li>
<li> refresh-activity-type - String - Required: No - (Filter) Filter by refresh activity types. (NORMAL: Regular Refresh Activity | ROLLBACK: Rollback Refresh Activity)</li>
<li> refresh-activity-id - String - Required: No - (Filter) Filter by refresh activity ID.</li>
<li>The upper limit of Filters per request is 10, and that of Filter.Values is 5. The RefreshActivityIds and Filters parameters cannot be specified at the same time.</li>
        :type Filters: list of Filter
        :param _Limit: Number of returned pieces. Default value: 20. Maximum value: 100. For further information on Limit, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _Offset: Offset, 0 by default. For further information on Offset, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        """
        self._RefreshActivityIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def RefreshActivityIds(self):
        """List of refresh activity IDs. IDs are formatted like: 'asr-5l2ejpfo'. The upper limit per request is 100. Parameters do not support specifying both RefreshActivityIds and Filters simultaneously.
        :rtype: list of str
        """
        return self._RefreshActivityIds

    @RefreshActivityIds.setter
    def RefreshActivityIds(self, RefreshActivityIds):
        self._RefreshActivityIds = RefreshActivityIds

    @property
    def Filters(self):
        """Filter criteria

<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
<li> refresh-activity-status-code - String - Required: No - (Filter)Filter based on refresh activity status. (INIT: Initialization | RUNNING:Running | SUCCESSFUL: Successful Activity | FAILED_PAUSE: Failed & Paused | AUTO_PAUSE: Auto Paused | MANUAL_PAUSE: Manually Paused | CANCELLED: Activity Cancelled | FAILED: Activity Failed)</li>
<li> refresh-activity-type - String - Required: No - (Filter) Filter by refresh activity types. (NORMAL: Regular Refresh Activity | ROLLBACK: Rollback Refresh Activity)</li>
<li> refresh-activity-id - String - Required: No - (Filter) Filter by refresh activity ID.</li>
<li>The upper limit of Filters per request is 10, and that of Filter.Values is 5. The RefreshActivityIds and Filters parameters cannot be specified at the same time.</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """Number of returned pieces. Default value: 20. Maximum value: 100. For further information on Limit, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset, 0 by default. For further information on Offset, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._RefreshActivityIds = params.get("RefreshActivityIds")
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
        


class DescribeRefreshActivitiesResponse(AbstractModel):
    """DescribeRefreshActivities response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of refresh activities that meet the conditions.
        :type TotalCount: int
        :param _RefreshActivitySet: A collection of information about refresh activities that meet the conditions.
        :type RefreshActivitySet: list of RefreshActivity
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RefreshActivitySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of refresh activities that meet the conditions.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RefreshActivitySet(self):
        """A collection of information about refresh activities that meet the conditions.
        :rtype: list of RefreshActivity
        """
        return self._RefreshActivitySet

    @RefreshActivitySet.setter
    def RefreshActivitySet(self, RefreshActivitySet):
        self._RefreshActivitySet = RefreshActivitySet

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RefreshActivitySet") is not None:
            self._RefreshActivitySet = []
            for item in params.get("RefreshActivitySet"):
                obj = RefreshActivity()
                obj._deserialize(item)
                self._RefreshActivitySet.append(obj)
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
        """Queries by one or more alarm policy IDs in the format of asp-i9vkg894. The maximum number of instances per request is 100. This parameter does not support specifying both `AutoScalingPolicyIds` and `Filters` at the same time.
        :rtype: list of str
        """
        return self._AutoScalingPolicyIds

    @AutoScalingPolicyIds.setter
    def AutoScalingPolicyIds(self, AutoScalingPolicyIds):
        self._AutoScalingPolicyIds = AutoScalingPolicyIds

    @property
    def Filters(self):
        """Filters.
<li> `auto-scaling-policy-id` - String - Optional - Filter by the alarm policy ID.</li>
<li> `auto-scaling-group-id` - String - Optional - Filter by the scaling group ID.</li>
<li> `scaling-policy-name` - String - Optional - Filter by the alarm policy name.</li>
<li> `scaling-policy-type` - String - Optional - Filter by the alarm policy type. Valid values: `SIMPLE`, `TARGET_TRACKING`.</li>
The maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. You cannot specify `AutoScalingPolicyIds` and `Filters` at the same time.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ScalingPolicySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ScalingPolicySet(self):
        """List of AS alarm trigger policy details.
        :rtype: list of ScalingPolicy
        """
        return self._ScalingPolicySet

    @ScalingPolicySet.setter
    def ScalingPolicySet(self, ScalingPolicySet):
        self._ScalingPolicySet = ScalingPolicySet

    @property
    def TotalCount(self):
        """Number of eligible notifications.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Queries by one or more scheduled task IDs in the format of asst-am691zxo. The maximum number of instances per request is 100. This parameter does not support specifying both ScheduledActionIds` and `Filters` at the same time.
        :rtype: list of str
        """
        return self._ScheduledActionIds

    @ScheduledActionIds.setter
    def ScheduledActionIds(self, ScheduledActionIds):
        self._ScheduledActionIds = ScheduledActionIds

    @property
    def Filters(self):
        """Filter.
<li> scheduled-action-id - String - Required: No - (Filter) Filter by scheduled task ID.</li>
<li> scheduled-action-name - String - Required: No - (Filter) Filter by scheduled task name.</li>
<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ScheduledActionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible scheduled tasks.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ScheduledActionSet(self):
        """List of scheduled task details.
        :rtype: list of ScheduledAction
        """
        return self._ScheduledActionSet

    @ScheduledActionSet.setter
    def ScheduledActionSet(self, ScheduledActionSet):
        self._ScheduledActionSet = ScheduledActionSet

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Auto scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        """List of CVM instance IDs
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        """Scaling activity ID
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def LoadBalancerIds(self):
        """List of classic CLB IDs. Up to 20 IDs are allowed. `LoadBalancerIds` and `ForwardLoadBalancerIdentifications` cannot be specified at the same time.
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ForwardLoadBalancerIdentifications(self):
        """List of application CLB IDs. Up to 100 IDs are allowed. `LoadBalancerIds` and `ForwardLoadBalancerIdentifications` cannot be specified at the same time.
        :rtype: list of ForwardLoadBalancerIdentification
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        """Scaling activity ID
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Error type
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Zone(self):
        """AZ information
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceChargeType(self):
        """Instance billing mode
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SubnetId(self):
        """Subnet ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Message(self):
        """Error message
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def InstanceType(self):
        """Instance type
        :rtype: str
        """
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
        """Scaling group ID
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Auto scaling group ID
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Enables the Cloud Security service. If this parameter is not specified, the Cloud Security service will be enabled by default.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.RunSecurityServiceEnabled`
        """
        return self._SecurityService

    @SecurityService.setter
    def SecurityService(self, SecurityService):
        self._SecurityService = SecurityService

    @property
    def MonitorService(self):
        """Enables the Cloud Monitor service. If this parameter is not specified, the Cloud Monitor service will be enabled by default.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.RunMonitorServiceEnabled`
        """
        return self._MonitorService

    @MonitorService.setter
    def MonitorService(self, MonitorService):
        self._MonitorService = MonitorService

    @property
    def AutomationService(self):
        warnings.warn("parameter `AutomationService` is deprecated", DeprecationWarning) 

        """Deprecated parameter.
        :rtype: list of RunAutomationServiceEnabled
        """
        return self._AutomationService

    @AutomationService.setter
    def AutomationService(self, AutomationService):
        warnings.warn("parameter `AutomationService` is deprecated", DeprecationWarning) 

        self._AutomationService = AutomationService

    @property
    def AutomationToolsService(self):
        """Enable TAT service. If this parameter is not specified, the default logic is the same as that of the CVM instance. Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.RunAutomationServiceEnabled`
        """
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
        """Auto-scaling policy ID. This parameter is not available to a target tracking policy.
        :rtype: str
        """
        return self._AutoScalingPolicyId

    @AutoScalingPolicyId.setter
    def AutoScalingPolicyId(self, AutoScalingPolicyId):
        self._AutoScalingPolicyId = AutoScalingPolicyId

    @property
    def HonorCooldown(self):
        """Whether to check if the auto scaling group is in the cooldown period. Default value: false
        :rtype: bool
        """
        return self._HonorCooldown

    @HonorCooldown.setter
    def HonorCooldown(self, HonorCooldown):
        self._HonorCooldown = HonorCooldown

    @property
    def TriggerSource(self):
        """Source that triggers the scaling policy. Valid values: API and CLOUD_MONITOR. Default value: API. The value `CLOUD_MONITOR` is specific to the Cloud Monitor service.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        """Scaling activity ID
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class ExitStandbyRequest(AbstractModel):
    """ExitStandby request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Scaling group ID.
        :type AutoScalingGroupId: str
        :param _InstanceIds: List of CVM instances in standby status.
        :type InstanceIds: list of str
        """
        self._AutoScalingGroupId = None
        self._InstanceIds = None

    @property
    def AutoScalingGroupId(self):
        """Scaling group ID.
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        """List of CVM instances in standby status.
        :rtype: list of str
        """
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
        


class ExitStandbyResponse(AbstractModel):
    """ExitStandby response structure.

    """

    def __init__(self):
        r"""
        :param _ActivityId: Scaling activity ID.
Note: This field may return null, indicating that no valid value can be obtained.
        :type ActivityId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        """Scaling activity ID.
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Field to be filtered.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """Filter value of the field.
        :rtype: list of str
        """
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
        """Load balancer ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        """Application load balancer listener ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def TargetAttributes(self):
        """List of target rule attributes
        :rtype: list of TargetAttribute
        """
        return self._TargetAttributes

    @TargetAttributes.setter
    def TargetAttributes(self, TargetAttributes):
        self._TargetAttributes = TargetAttributes

    @property
    def LocationId(self):
        """ID of a forwarding rule. This parameter is required for layer-7 listeners.
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Region(self):
        """The region of CLB instance. It defaults to the region of AS service and is in the format of the common parameter `Region`, such as `ap-guangzhou`.
        :rtype: str
        """
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
        """ID of the CLB
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        """Application CLB listener ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LocationId(self):
        """ID of a forwarding rule. This parameter is required for layer-7 listeners.
        :rtype: str
        """
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
        :param _HostName: CVM HostName.
<li>Dots (.) and hyphens (-) cannot be used as the first or last character of HostName, and cannot be used consecutively.</li>
<li>Windows instances are not supported.</li>
<li>Instances of other types (e.g., Linux): The length of the character should be within the range of [2, 40]. Multiple dots (.) are allowed. Each segment between dot marks can consist of letters (case-insensitive), digits, and hyphens (-). Using only digits is not allowed.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type HostName: str
        :param _HostNameStyle: The style of the CVM HostName. Valid values include ORIGINAL and UNIQUE, and the default value is ORIGINAL.
<li>ORIGINAL: AS passes HostName filled in the input parameters to CVM. CVM may append serial numbers to HostName, which can result in conflicts with HostName of instances in the scaling group.</li>
<li> UNIQUE: HostName filled in the input parameters acts as a prefix for the HostName. AS and CVM will expand this prefix to ensure that HostName of the instance in the scaling group is unique.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type HostNameStyle: str
        :param _HostNameSuffix: HostName suffix for CVM.
<li>Dots (.) and hyphens (-) cannot be used as the first or last character of HostNameSuffix, and cannot be used consecutively.</li>
<li>Windows instances are not supported.</li>
<li>Instances of other types (e.g., Linux): The length of the character should be within the range of [1, 37], and the combined length with HostName should not exceed 39. Multiple dots (.) are allowed. Each segment between dots can consist of letters (case-insensitive), digits, and hyphens (-).</li>
Assume the suffix name is suffix and the original HostName is test.0, then the final HostName is test.0.suffix.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HostNameSuffix: str
        """
        self._HostName = None
        self._HostNameStyle = None
        self._HostNameSuffix = None

    @property
    def HostName(self):
        """CVM HostName.
<li>Dots (.) and hyphens (-) cannot be used as the first or last character of HostName, and cannot be used consecutively.</li>
<li>Windows instances are not supported.</li>
<li>Instances of other types (e.g., Linux): The length of the character should be within the range of [2, 40]. Multiple dots (.) are allowed. Each segment between dot marks can consist of letters (case-insensitive), digits, and hyphens (-). Using only digits is not allowed.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def HostNameStyle(self):
        """The style of the CVM HostName. Valid values include ORIGINAL and UNIQUE, and the default value is ORIGINAL.
<li>ORIGINAL: AS passes HostName filled in the input parameters to CVM. CVM may append serial numbers to HostName, which can result in conflicts with HostName of instances in the scaling group.</li>
<li> UNIQUE: HostName filled in the input parameters acts as a prefix for the HostName. AS and CVM will expand this prefix to ensure that HostName of the instance in the scaling group is unique.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HostNameStyle

    @HostNameStyle.setter
    def HostNameStyle(self, HostNameStyle):
        self._HostNameStyle = HostNameStyle

    @property
    def HostNameSuffix(self):
        """HostName suffix for CVM.
<li>Dots (.) and hyphens (-) cannot be used as the first or last character of HostNameSuffix, and cannot be used consecutively.</li>
<li>Windows instances are not supported.</li>
<li>Instances of other types (e.g., Linux): The length of the character should be within the range of [1, 37], and the combined length with HostName should not exceed 39. Multiple dots (.) are allowed. Each segment between dots can consist of letters (case-insensitive), digits, and hyphens (-).</li>
Assume the suffix name is suffix and the original HostName is test.0, then the final HostName is test.0.suffix.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HostNameSuffix

    @HostNameSuffix.setter
    def HostNameSuffix(self, HostNameSuffix):
        self._HostNameSuffix = HostNameSuffix


    def _deserialize(self, params):
        self._HostName = params.get("HostName")
        self._HostNameStyle = params.get("HostNameStyle")
        self._HostNameSuffix = params.get("HostNameSuffix")
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
        :param _InternetChargeType: Network billing mode. Valid values: TRAFFIC_POSTPAID_BY_HOUR, BANDWIDTH_PACKAGE. Default value: TRAFFIC_POSTPAID_BY_HOUR. For the current account type, see [Account Type Description](https://intl.cloud.tencent.com/document/product/684/15246?from_cn_redirect=1#judge).
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
        """Network billing mode. Valid values: TRAFFIC_POSTPAID_BY_HOUR, BANDWIDTH_PACKAGE. Default value: TRAFFIC_POSTPAID_BY_HOUR. For the current account type, see [Account Type Description](https://intl.cloud.tencent.com/document/product/684/15246?from_cn_redirect=1#judge).
<br><li> IPv6 supports `TRAFFIC_POSTPAID_BY_HOUR` under a bill-by-IP account.
<br><li> IPv6 supports `BANDWIDTH_PACKAGE` under a bill-by-CVM account.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        """Outbound bandwidth cap of the public network (in Mbps). <br>It defaults to `0`, which indicates no public network bandwidth is allocated to IPv6. The value range of bandwidth caps varies with the model, availability zone and billing mode. For more information, see [Public Network Bandwidth Cap](https://intl.cloud.tencent.com/document/product/213/12523?from_cn_redirect=1).
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def BandwidthPackageId(self):
        """Bandwidth package ID. You can obtain the ID from the `BandwidthPackageId` field in the response of the [DescribeBandwidthPackages](https://intl.cloud.tencent.com/document/api/215/19209?from_cn_redirect=1) API.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AutoScalingGroupId(self):
        """Auto scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def LaunchConfigurationId(self):
        """Launch configuration ID
        :rtype: str
        """
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def LaunchConfigurationName(self):
        """Launch configuration name
        :rtype: str
        """
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def LifeCycleState(self):
        """Lifecycle status. Valid values:<br>
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
        :rtype: str
        """
        return self._LifeCycleState

    @LifeCycleState.setter
    def LifeCycleState(self, LifeCycleState):
        self._LifeCycleState = LifeCycleState

    @property
    def HealthStatus(self):
        """Health status. Value range: HEALTHY, UNHEALTHY
        :rtype: str
        """
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def ProtectedFromScaleIn(self):
        """Whether to add scale-in protection
        :rtype: bool
        """
        return self._ProtectedFromScaleIn

    @ProtectedFromScaleIn.setter
    def ProtectedFromScaleIn(self, ProtectedFromScaleIn):
        self._ProtectedFromScaleIn = ProtectedFromScaleIn

    @property
    def Zone(self):
        """Availability zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CreationType(self):
        """Creation type. Value range: AUTO_CREATION, MANUAL_ATTACHING.
        :rtype: str
        """
        return self._CreationType

    @CreationType.setter
    def CreationType(self, CreationType):
        self._CreationType = CreationType

    @property
    def AddTime(self):
        """Instance addition time
        :rtype: str
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def InstanceType(self):
        """Instance type
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def VersionNumber(self):
        """Version number
        :rtype: int
        """
        return self._VersionNumber

    @VersionNumber.setter
    def VersionNumber(self, VersionNumber):
        self._VersionNumber = VersionNumber

    @property
    def AutoScalingGroupName(self):
        """Auto scaling group name
        :rtype: str
        """
        return self._AutoScalingGroupName

    @AutoScalingGroupName.setter
    def AutoScalingGroupName(self, AutoScalingGroupName):
        self._AutoScalingGroupName = AutoScalingGroupName

    @property
    def WarmupStatus(self):
        """Warming up status. Valid values:
<li>`WAITING_ENTER_WARMUP`: The instance is waiting to be warmed up.
<li>`NO_NEED_WARMUP`: Warming up is not required.
<li>`IN_WARMUP`: The instance is being warmed up.
<li>`AFTER_WARMUP`: Warming up is completed.
        :rtype: str
        """
        return self._WarmupStatus

    @WarmupStatus.setter
    def WarmupStatus(self, WarmupStatus):
        self._WarmupStatus = WarmupStatus

    @property
    def DisasterRecoverGroupIds(self):
        """Placement group ID. Only one is allowed.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of str
        """
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
        :param _RenewFlag: Auto-renewal flag. Valid values: <li>NOTIFY_AND_AUTO_RENEW: Notify upon expiration and automatically renew.</li> <li>NOTIFY_AND_MANUAL_RENEW: Notify upon expiration but do not auto-renew.</li> <li>DISABLE_NOTIFY_AND_MANUAL_RENEW: Do not notify and do not auto-renew</li> Default value: NOTIFY_AND_MANUAL_RENEW. If this parameter is set to NOTIFY_AND_AUTO_RENEW, and the account balance is sufficient, the instance will automatically renew monthly upon its expiration date.
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        """Purchased usage period of an instance in months. Value range: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        """Auto-renewal flag. Valid values: <li>NOTIFY_AND_AUTO_RENEW: Notify upon expiration and automatically renew.</li> <li>NOTIFY_AND_MANUAL_RENEW: Notify upon expiration but do not auto-renew.</li> <li>DISABLE_NOTIFY_AND_MANUAL_RENEW: Do not notify and do not auto-renew</li> Default value: NOTIFY_AND_MANUAL_RENEW. If this parameter is set to NOTIFY_AND_AUTO_RENEW, and the account balance is sufficient, the instance will automatically renew monthly upon its expiration date.
        :rtype: str
        """
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
        :param _MarketType: Market option type. The value can only be spot currently.
        :type MarketType: str
        """
        self._SpotOptions = None
        self._MarketType = None

    @property
    def SpotOptions(self):
        """Bidding-related options
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.SpotMarketOptions`
        """
        return self._SpotOptions

    @SpotOptions.setter
    def SpotOptions(self, SpotOptions):
        self._SpotOptions = SpotOptions

    @property
    def MarketType(self):
        """Market option type. The value can only be spot currently.
        :rtype: str
        """
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
        


class InstanceNameIndexSettings(AbstractModel):
    """Instance name sequencing settings.

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether to enable instance creation sequencing, which is disabled by default. Valid values: <li>TRUE: Indicates that instance creation sequencing is enabled. <li>FALSE: Indicates that instance creation sequencing is disabled.
Note: This field may return null, indicating that no valid value can be obtained.
        :type Enabled: bool
        :param _BeginIndex: Initial sequence number, with a value range of [0, 99,999,999]. When the sequence number exceeds this range after incrementing, scale-out activities will fail. <li>Upon the first enabling of instance name sequencing: The default value is 0. <li>Upon the enabling of instance name sequencing (not for the first time): If this parameter is not specified, the historical sequence number will be carried forward. Lowering the initial sequence number may result in duplicate instance name sequences within the scaling group.
Note: This field may return null, indicating that no valid value can be obtained.
        :type BeginIndex: int
        """
        self._Enabled = None
        self._BeginIndex = None

    @property
    def Enabled(self):
        """Whether to enable instance creation sequencing, which is disabled by default. Valid values: <li>TRUE: Indicates that instance creation sequencing is enabled. <li>FALSE: Indicates that instance creation sequencing is disabled.
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def BeginIndex(self):
        """Initial sequence number, with a value range of [0, 99,999,999]. When the sequence number exceeds this range after incrementing, scale-out activities will fail. <li>Upon the first enabling of instance name sequencing: The default value is 0. <li>Upon the enabling of instance name sequencing (not for the first time): If this parameter is not specified, the historical sequence number will be carried forward. Lowering the initial sequence number may result in duplicate instance name sequences within the scaling group.
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._BeginIndex

    @BeginIndex.setter
    def BeginIndex(self, BeginIndex):
        self._BeginIndex = BeginIndex


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._BeginIndex = params.get("BeginIndex")
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
        :param _InstanceName: CVM instance name. Value range: 2-108.
        :type InstanceName: str
        :param _InstanceNameStyle: Type of CVM instance name. Valid values: `ORIGINAL` and `UNIQUE`. Default value: `ORIGINAL`.

`ORIGINAL`: Auto Scaling sends the input parameter `InstanceName` to the CVM directly. The CVM may append a serial number to the `InstanceName`. The `InstanceName` of the instances within the scaling group may conflict.

`UNIQUE`: the input parameter `InstanceName` is the prefix of an instance name. Auto Scaling and CVM expand it. The `InstanceName` of an instance in the scaling group is unique.
        :type InstanceNameStyle: str
        :param _InstanceNameSuffix: CVM instance name suffix. The length of the character is within the range of [1, 105], and the combined length with InstanceName should not exceed 107.

Assume the suffix name is suffix and the original instance name is test.0, then the final instance name is test.0.suffix.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceNameSuffix: str
        """
        self._InstanceName = None
        self._InstanceNameStyle = None
        self._InstanceNameSuffix = None

    @property
    def InstanceName(self):
        """CVM instance name. Value range: 2-108.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceNameStyle(self):
        """Type of CVM instance name. Valid values: `ORIGINAL` and `UNIQUE`. Default value: `ORIGINAL`.

`ORIGINAL`: Auto Scaling sends the input parameter `InstanceName` to the CVM directly. The CVM may append a serial number to the `InstanceName`. The `InstanceName` of the instances within the scaling group may conflict.

`UNIQUE`: the input parameter `InstanceName` is the prefix of an instance name. Auto Scaling and CVM expand it. The `InstanceName` of an instance in the scaling group is unique.
        :rtype: str
        """
        return self._InstanceNameStyle

    @InstanceNameStyle.setter
    def InstanceNameStyle(self, InstanceNameStyle):
        self._InstanceNameStyle = InstanceNameStyle

    @property
    def InstanceNameSuffix(self):
        """CVM instance name suffix. The length of the character is within the range of [1, 105], and the combined length with InstanceName should not exceed 107.

Assume the suffix name is suffix and the original instance name is test.0, then the final instance name is test.0.suffix.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceNameSuffix

    @InstanceNameSuffix.setter
    def InstanceNameSuffix(self, InstanceNameSuffix):
        self._InstanceNameSuffix = InstanceNameSuffix


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._InstanceNameStyle = params.get("InstanceNameStyle")
        self._InstanceNameSuffix = params.get("InstanceNameSuffix")
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
        """Tag key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Tag value
        :rtype: str
        """
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
        :param _InternetChargeType: Network billing type. Valid values: <li>BANDWIDTH_PREPAID: prepaid by bandwidth;</li> <li>TRAFFIC_POSTPAID_BY_HOUR: postpaid by traffic per hour;</li> <li>BANDWIDTH_POSTPAID_BY_HOUR: postpaid by bandwidth per hour;</li> <li>BANDWIDTH_PACKAGE: bandwidth package users.</li> Default value: TRAFFIC_POSTPAID_BY_HOUR.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: The maximum outbound bandwidth in Mbps of the public network. The default value is 0 Mbps. The upper limit of bandwidth varies by model. For more information, see [Purchase Network Bandwidth](https://intl.cloud.tencent.com/document/product/213/509?from_cn_redirect=1).
Note: This field may return null, indicating that no valid values can be obtained.
        :type InternetMaxBandwidthOut: int
        :param _PublicIpAssigned: Whether to assign a public IP address. Valid values: <li>TRUE: Allocate a public IP address.</li> <li>FALSE: Do not allocate a public IP address.</li> When the public network bandwidth is greater than 0 Mbps, you can choose whether to enable this feature based on your needs. By default, this feature is enabled. When the public network bandwidth is 0, public IP address assignment is not allowed.
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
        """Network billing type. Valid values: <li>BANDWIDTH_PREPAID: prepaid by bandwidth;</li> <li>TRAFFIC_POSTPAID_BY_HOUR: postpaid by traffic per hour;</li> <li>BANDWIDTH_POSTPAID_BY_HOUR: postpaid by bandwidth per hour;</li> <li>BANDWIDTH_PACKAGE: bandwidth package users.</li> Default value: TRAFFIC_POSTPAID_BY_HOUR.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        """The maximum outbound bandwidth in Mbps of the public network. The default value is 0 Mbps. The upper limit of bandwidth varies by model. For more information, see [Purchase Network Bandwidth](https://intl.cloud.tencent.com/document/product/213/509?from_cn_redirect=1).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def PublicIpAssigned(self):
        """Whether to assign a public IP address. Valid values: <li>TRUE: Allocate a public IP address.</li> <li>FALSE: Do not allocate a public IP address.</li> When the public network bandwidth is greater than 0 Mbps, you can choose whether to enable this feature based on your needs. By default, this feature is enabled. When the public network bandwidth is 0, public IP address assignment is not allowed.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._PublicIpAssigned

    @PublicIpAssigned.setter
    def PublicIpAssigned(self, PublicIpAssigned):
        self._PublicIpAssigned = PublicIpAssigned

    @property
    def BandwidthPackageId(self):
        """Bandwidth package ID. You can obtain the ID from the `BandwidthPackageId` field in the response of the [DescribeBandwidthPackages](https://intl.cloud.tencent.com/document/api/215/19209?from_cn_redirect=1) API.
Note: this field may return null, indicating that no valid value was found.
        :rtype: str
        """
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
        :type InstanceId: str
        :param _InvocationId: Execution activity ID.
        :type InvocationId: str
        :param _InvocationTaskId: Task ID.
        :type InvocationTaskId: str
        :param _CommandId: Command ID.
        :type CommandId: str
        :param _TaskStatus: Specifies the execution task status.
        :type TaskStatus: str
        :param _ErrorMessage: Specifies the exception information during execution.
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
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InvocationId(self):
        """Execution activity ID.
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def InvocationTaskId(self):
        """Task ID.
        :rtype: str
        """
        return self._InvocationTaskId

    @InvocationTaskId.setter
    def InvocationTaskId(self, InvocationTaskId):
        self._InvocationTaskId = InvocationTaskId

    @property
    def CommandId(self):
        """Command ID.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def TaskStatus(self):
        """Specifies the execution task status.
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def ErrorMessage(self):
        """Specifies the exception information during execution.
        :rtype: str
        """
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
        :param _LaunchConfigurationStatus: Current status of the launch configuration. Valid values: <li>NORMAL: Normal.</li> <li>IMAGE_ABNORMAL: Image exception in the launch configuration.</li> <li>CBS_SNAP_ABNORMAL: Exception with data disk snapshot in the launch configuration.</li> <li>SECURITY_GROUP_ABNORMAL: Security group exception in the launch configuration.</li>
        :type LaunchConfigurationStatus: str
        :param _InstanceChargeType: Instance billing type, with the CVM default value processed as POSTPAID_BY_HOUR. <li>POSTPAID_BY_HOUR: Hourly postpaid billing.</li> <li>SPOTPAID: Spot billing.</li>
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
        :param _DiskTypePolicy: Cloud disk type selection policy. Valid values: <li>ORIGINAL: Use the set cloud disk type.</li> <li>AUTOMATIC: Automatically select available cloud disk types in the current availability zone.</li>
        :type DiskTypePolicy: str
        :param _HpcClusterId: HPC ID<br>
Note: This field is default to empty
        :type HpcClusterId: str
        :param _IPv6InternetAccessible: IPv6 public network bandwidth configuration.
        :type IPv6InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.IPv6InternetAccessible`
        :param _DisasterRecoverGroupIds: Placement group ID, supporting specification of only one.
        :type DisasterRecoverGroupIds: list of str
        :param _ImageFamily: Image family name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ImageFamily: str
        :param _DedicatedClusterId: CDC ID.
        :type DedicatedClusterId: str
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
        self._DisasterRecoverGroupIds = None
        self._ImageFamily = None
        self._DedicatedClusterId = None

    @property
    def ProjectId(self):
        """Project ID of the instance.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def LaunchConfigurationId(self):
        """Launch configuration ID
        :rtype: str
        """
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def LaunchConfigurationName(self):
        """Launch configuration name.
        :rtype: str
        """
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def InstanceType(self):
        """Instance model.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        """Information of the instance's system disk configuration.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """Information of the instance's data disk configuration.
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def LoginSettings(self):
        """Instance login settings.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.LimitedLoginSettings`
        """
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def InternetAccessible(self):
        """Information of the public network bandwidth configuration.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def SecurityGroupIds(self):
        """Security group of the instance.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def AutoScalingGroupAbstractSet(self):
        """Auto scaling group associated with the launch configuration.
        :rtype: list of AutoScalingGroupAbstract
        """
        return self._AutoScalingGroupAbstractSet

    @AutoScalingGroupAbstractSet.setter
    def AutoScalingGroupAbstractSet(self, AutoScalingGroupAbstractSet):
        self._AutoScalingGroupAbstractSet = AutoScalingGroupAbstractSet

    @property
    def UserData(self):
        """Custom data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def CreatedTime(self):
        """Creation time of the launch configuration.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def EnhancedService(self):
        """Conditions of enhancement services for the instance and their settings.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.EnhancedService`
        """
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def ImageId(self):
        """Image ID.
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def LaunchConfigurationStatus(self):
        """Current status of the launch configuration. Valid values: <li>NORMAL: Normal.</li> <li>IMAGE_ABNORMAL: Image exception in the launch configuration.</li> <li>CBS_SNAP_ABNORMAL: Exception with data disk snapshot in the launch configuration.</li> <li>SECURITY_GROUP_ABNORMAL: Security group exception in the launch configuration.</li>
        :rtype: str
        """
        return self._LaunchConfigurationStatus

    @LaunchConfigurationStatus.setter
    def LaunchConfigurationStatus(self, LaunchConfigurationStatus):
        self._LaunchConfigurationStatus = LaunchConfigurationStatus

    @property
    def InstanceChargeType(self):
        """Instance billing type, with the CVM default value processed as POSTPAID_BY_HOUR. <li>POSTPAID_BY_HOUR: Hourly postpaid billing.</li> <li>SPOTPAID: Spot billing.</li>
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceMarketOptions(self):
        """Market options of the instance, such as parameters related to spot instances. This parameter is required for spot instances.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        """
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def InstanceTypes(self):
        """List of instance models.
        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def InstanceTags(self):
        """List of instance tags, which will be added to instances created by the scale-out activity. Up to 10 tags allowed.
        :rtype: list of InstanceTag
        """
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def Tags(self):
        """Tag list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def VersionNumber(self):
        """Version
        :rtype: int
        """
        return self._VersionNumber

    @VersionNumber.setter
    def VersionNumber(self, VersionNumber):
        self._VersionNumber = VersionNumber

    @property
    def UpdatedTime(self):
        """Update time
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def CamRoleName(self):
        """CAM role name. This parameter can be obtained from the `roleName` field returned by DescribeRoleList API.
        :rtype: str
        """
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def LastOperationInstanceTypesCheckPolicy(self):
        """Value of InstanceTypesCheckPolicy upon the last operation.
        :rtype: str
        """
        return self._LastOperationInstanceTypesCheckPolicy

    @LastOperationInstanceTypesCheckPolicy.setter
    def LastOperationInstanceTypesCheckPolicy(self, LastOperationInstanceTypesCheckPolicy):
        self._LastOperationInstanceTypesCheckPolicy = LastOperationInstanceTypesCheckPolicy

    @property
    def HostNameSettings(self):
        """CVM hostname settings.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.HostNameSettings`
        """
        return self._HostNameSettings

    @HostNameSettings.setter
    def HostNameSettings(self, HostNameSettings):
        self._HostNameSettings = HostNameSettings

    @property
    def InstanceNameSettings(self):
        """Settings of CVM instance names
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameSettings`
        """
        return self._InstanceNameSettings

    @InstanceNameSettings.setter
    def InstanceNameSettings(self, InstanceNameSettings):
        self._InstanceNameSettings = InstanceNameSettings

    @property
    def InstanceChargePrepaid(self):
        """Details of the monthly subscription, including the purchase period, auto-renewal. It is required if the `InstanceChargeType` is `PREPAID`.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def DiskTypePolicy(self):
        """Cloud disk type selection policy. Valid values: <li>ORIGINAL: Use the set cloud disk type.</li> <li>AUTOMATIC: Automatically select available cloud disk types in the current availability zone.</li>
        :rtype: str
        """
        return self._DiskTypePolicy

    @DiskTypePolicy.setter
    def DiskTypePolicy(self, DiskTypePolicy):
        self._DiskTypePolicy = DiskTypePolicy

    @property
    def HpcClusterId(self):
        """HPC ID<br>
Note: This field is default to empty
        :rtype: str
        """
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def IPv6InternetAccessible(self):
        """IPv6 public network bandwidth configuration.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.IPv6InternetAccessible`
        """
        return self._IPv6InternetAccessible

    @IPv6InternetAccessible.setter
    def IPv6InternetAccessible(self, IPv6InternetAccessible):
        self._IPv6InternetAccessible = IPv6InternetAccessible

    @property
    def DisasterRecoverGroupIds(self):
        """Placement group ID, supporting specification of only one.
        :rtype: list of str
        """
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def ImageFamily(self):
        """Image family name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ImageFamily

    @ImageFamily.setter
    def ImageFamily(self, ImageFamily):
        self._ImageFamily = ImageFamily

    @property
    def DedicatedClusterId(self):
        """CDC ID.
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId


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
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self._ImageFamily = params.get("ImageFamily")
        self._DedicatedClusterId = params.get("DedicatedClusterId")
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
        """ID of the lifecycle hook
        :rtype: str
        """
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def InstanceId(self):
        """ID of the instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InvocationId(self):
        """Execution task ID. You can query the result by using the [DescribeInvocations](https://intl.cloud.tencent.com/document/api/1340/52679?from_cn_redirect=1) API of TAT. 
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def InvokeCommandResult(self):
        """Result of command invocation,
<li>`SUCCESSFUL`: Successful command invocation. It does mean that the task is successfully. You can query the task result with the `InvocationId.</li>
<li>`FAILED`: Failed to invoke the command</li>
<li>`NONE`</li>
        :rtype: str
        """
        return self._InvokeCommandResult

    @InvokeCommandResult.setter
    def InvokeCommandResult(self, InvokeCommandResult):
        self._InvokeCommandResult = InvokeCommandResult

    @property
    def NotificationResult(self):
        """Notification result, which indicates whether it is successful to notify CMQ/TDMQ.<br>
<li>SUCCESSFUL: It is successful to notify CMQ/TDMQ.</li>
<li>FAILED: It is failed to notify CMQ/TDMQ.</li>
<li>NONE</li>
        :rtype: str
        """
        return self._NotificationResult

    @NotificationResult.setter
    def NotificationResult(self, NotificationResult):
        self._NotificationResult = NotificationResult

    @property
    def LifecycleActionResult(self):
        """Result of the lifecyle hook action. Values: CONTINUE, ABANDON
        :rtype: str
        """
        return self._LifecycleActionResult

    @LifecycleActionResult.setter
    def LifecycleActionResult(self, LifecycleActionResult):
        self._LifecycleActionResult = LifecycleActionResult

    @property
    def ResultReason(self):
        """Reason of the result <br>
<li>`HEARTBEAT_TIMEOUT`: Heartbeat timed out. The setting of `DefaultResult` is used.</li>
<li>`NOTIFICATION_FAILURE`: Failed to send the notification. The setting of `DefaultResult` is used.</li>
<li>`CALL_INTERFACE`: Calls the `CompleteLifecycleAction` to set the result</li>
<li>ANOTHER_ACTION_ABANDON: It has been set to `ABANDON` by another operation.</li>
<li>COMMAND_CALL_FAILURE: Failed to call the command. The DefaultResult is applied.</li>
<li>COMMAND_EXEC_FINISH: Command completed</li>
<li>COMMAND_CALL_FAILURE: Failed to execute the command. The DefaultResult is applied.</li>
<li>COMMAND_EXEC_RESULT_CHECK_FAILURE: Failed to check the command result. The DefaultResult is applied.</li>
        :rtype: str
        """
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
        """Remote command ID. It’s required to execute a command.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def Parameters(self):
        """Custom parameter. The field type is JSON encoded string. For example, {"varA": "222"}.
`key` is the name of the custom parameter and `value` is the default value. Both `key` and `value` are strings.
If this parameter is not specified, the `DefaultParameters` of `Command` is used.
Up to 20 customer parameters allowed. The parameter name can contain up to 64 characters, including [a-z], [A-Z], [0-9] and [-_].
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        """Lifecycle hook ID
        :rtype: str
        """
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def LifecycleHookName(self):
        """Lifecycle hook name
        :rtype: str
        """
        return self._LifecycleHookName

    @LifecycleHookName.setter
    def LifecycleHookName(self, LifecycleHookName):
        self._LifecycleHookName = LifecycleHookName

    @property
    def AutoScalingGroupId(self):
        """Auto scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def DefaultResult(self):
        """Default result of the lifecycle hook
        :rtype: str
        """
        return self._DefaultResult

    @DefaultResult.setter
    def DefaultResult(self, DefaultResult):
        self._DefaultResult = DefaultResult

    @property
    def HeartbeatTimeout(self):
        """Wait timeout period of the lifecycle hook
        :rtype: int
        """
        return self._HeartbeatTimeout

    @HeartbeatTimeout.setter
    def HeartbeatTimeout(self, HeartbeatTimeout):
        self._HeartbeatTimeout = HeartbeatTimeout

    @property
    def LifecycleTransition(self):
        """Applicable scenario of the lifecycle hook
        :rtype: str
        """
        return self._LifecycleTransition

    @LifecycleTransition.setter
    def LifecycleTransition(self, LifecycleTransition):
        self._LifecycleTransition = LifecycleTransition

    @property
    def NotificationMetadata(self):
        """Additional information for the notification target
        :rtype: str
        """
        return self._NotificationMetadata

    @NotificationMetadata.setter
    def NotificationMetadata(self, NotificationMetadata):
        self._NotificationMetadata = NotificationMetadata

    @property
    def CreatedTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def NotificationTarget(self):
        """Notification target
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.NotificationTarget`
        """
        return self._NotificationTarget

    @NotificationTarget.setter
    def NotificationTarget(self, NotificationTarget):
        self._NotificationTarget = NotificationTarget

    @property
    def LifecycleTransitionType(self):
        """Applicable scenario of the lifecycle hook
        :rtype: str
        """
        return self._LifecycleTransitionType

    @LifecycleTransitionType.setter
    def LifecycleTransitionType(self, LifecycleTransitionType):
        self._LifecycleTransitionType = LifecycleTransitionType

    @property
    def LifecycleCommand(self):
        """Remote command execution object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.LifecycleCommand`
        """
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
        """List of key IDs.
        :rtype: list of str
        """
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
        :param _Password: Instance login password. The password complexity requirements vary according to the operating system type. The details are as follows:
- For a Linux system, the password should contain 8 to 30 characters consisting of at least two of the four character types: lowercase letters, uppercase letters, digits, and special characters.
- For a Windows system, the password should contain 12 to 30 characters consisting of at least three of the four character types: lowercase letters, uppercase letters, digits, and special characters.
- If this parameter is not specified, the system will generate a random password and notify the user via the message centerSupported special characters: ( ) ` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? /
        :type Password: str
        :param _KeyIds: List of key IDs. After an instance is associated with a key, you can access the instance with the private key in the key pair. You can call `DescribeKeyPairs` to obtain `KeyId`. Key and password cannot be specified at the same time. Windows instances do not support keys. Currently, you can only specify one key when purchasing an instance.
        :type KeyIds: list of str
        :param _KeepImageLogin: Retain the original settings of the image. This parameter cannot be specified simultaneously with Password or KeyIds.N. It can only be set to TRUE when you create an instance by using a custom image, shared image, or externally imported image. Valid values:
<li>TRUE: Retain the login settings of the image.</li>
<li>FALSE: Do not retain the login settings of the image.</li> Default value: FALSE.
        :type KeepImageLogin: bool
        """
        self._Password = None
        self._KeyIds = None
        self._KeepImageLogin = None

    @property
    def Password(self):
        """Instance login password. The password complexity requirements vary according to the operating system type. The details are as follows:
- For a Linux system, the password should contain 8 to 30 characters consisting of at least two of the four character types: lowercase letters, uppercase letters, digits, and special characters.
- For a Windows system, the password should contain 12 to 30 characters consisting of at least three of the four character types: lowercase letters, uppercase letters, digits, and special characters.
- If this parameter is not specified, the system will generate a random password and notify the user via the message centerSupported special characters: ( ) ` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? /
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def KeyIds(self):
        """List of key IDs. After an instance is associated with a key, you can access the instance with the private key in the key pair. You can call `DescribeKeyPairs` to obtain `KeyId`. Key and password cannot be specified at the same time. Windows instances do not support keys. Currently, you can only specify one key when purchasing an instance.
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def KeepImageLogin(self):
        """Retain the original settings of the image. This parameter cannot be specified simultaneously with Password or KeyIds.N. It can only be set to TRUE when you create an instance by using a custom image, shared image, or externally imported image. Valid values:
<li>TRUE: Retain the login settings of the image.</li>
<li>FALSE: Do not retain the login settings of the image.</li> Default value: FALSE.
        :rtype: bool
        """
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
        


class Metadata(AbstractModel):
    """Custom Metadata

    """

    def __init__(self):
        r"""
        :param _Items: Custom metadata key-value pair list.
        :type Items: list of MetadataItem
        """
        self._Items = None

    @property
    def Items(self):
        """Custom metadata key-value pair list.
        :rtype: list of MetadataItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = MetadataItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetadataItem(AbstractModel):
    """A set of key-value pair information for custom Metadata

    """

    def __init__(self):
        r"""
        :param _Key: Custom metadata key.
        :type Key: str
        :param _Value: Custom metadata value.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Custom metadata key.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Custom metadata value.
        :rtype: str
        """
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
        


class MetricAlarm(AbstractModel):
    """Alarming metric of AS

    """

    def __init__(self):
        r"""
        :param _ComparisonOperator: Comparison operator. Value range: <br><li>GREATER_THAN: greater than </li><li>GREATER_THAN_OR_EQUAL_TO: greater than or equal to </li><li>LESS_THAN: less than </li><li> LESS_THAN_OR_EQUAL_TO: less than or equal to </li><li> EQUAL_TO: equal to </li> <li>NOT_EQUAL_TO: not equal to </li>
        :type ComparisonOperator: str
        :param _MetricName: Metric names, with the following optional fields: <br><li>CPU_UTILIZATION: CPU utilization.</li> <li>MEM_UTILIZATION: Memory utilization.</li> <li>LAN_TRAFFIC_OUT: Private network outbound bandwidth.</li> <li>LAN_TRAFFIC_IN: Private network inbound bandwidth.</li> <li>WAN_TRAFFIC_OUT: Public network outbound bandwidth.</li> <li>WAN_TRAFFIC_IN: Public network inbound bandwidth.</li> <li>TCP_CURR_ESTAB: TCP connections.</li>
        :type MetricName: str
        :param _Threshold: Alarm threshold values: <br><li>CPU_UTILIZATION: [1, 100], Unit: %.</li> <li>MEM_UTILIZATION: [1, 100], Unit: %.</li> <li>LAN_TRAFFIC_OUT: >0, Unit: Mbps.</li> <li>LAN_TRAFFIC_IN: >0, Unit: Mbps.</li> <li>WAN_TRAFFIC_OUT: >0, Unit: Mbps.</li> <li>WAN_TRAFFIC_IN: >0, Unit: Mbps.</li> <li>TCP_CURR_ESTAB: >0, Unit: Count.</li>
        :type Threshold: int
        :param _Period: Time period in seconds. Enumerated values: 60, 300.
        :type Period: int
        :param _ContinuousTime: Number of repetitions. Value range: [1, 10]
        :type ContinuousTime: int
        :param _Statistic: Statistics type. Value range: <br><li>AVERAGE: average </li><li>MAXIMUM: maximum <li>MINIMUM: minimum </li><br> Default value: AVERAGE
        :type Statistic: str
        :param _PreciseThreshold: Precise alarm threshold values. This parameter is not used as an input argument but is used solely as an output parameter for the query API: <br><li>CPU_UTILIZATION: (0, 100], Unit: %.</li> <li>MEM_UTILIZATION: (0, 100], Unit: %.</li> <li>LAN_TRAFFIC_OUT: >0, Unit: Mbps.</li> <li>LAN_TRAFFIC_IN: >0, Unit: Mbps.</li> <li>WAN_TRAFFIC_OUT: >0, Unit: Mbps.</li> <li>WAN_TRAFFIC_IN: >0, Unit: Mbps.</li> <li>TCP_CURR_ESTAB: >0, Unit: Count.</li>
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
        """Comparison operator. Value range: <br><li>GREATER_THAN: greater than </li><li>GREATER_THAN_OR_EQUAL_TO: greater than or equal to </li><li>LESS_THAN: less than </li><li> LESS_THAN_OR_EQUAL_TO: less than or equal to </li><li> EQUAL_TO: equal to </li> <li>NOT_EQUAL_TO: not equal to </li>
        :rtype: str
        """
        return self._ComparisonOperator

    @ComparisonOperator.setter
    def ComparisonOperator(self, ComparisonOperator):
        self._ComparisonOperator = ComparisonOperator

    @property
    def MetricName(self):
        """Metric names, with the following optional fields: <br><li>CPU_UTILIZATION: CPU utilization.</li> <li>MEM_UTILIZATION: Memory utilization.</li> <li>LAN_TRAFFIC_OUT: Private network outbound bandwidth.</li> <li>LAN_TRAFFIC_IN: Private network inbound bandwidth.</li> <li>WAN_TRAFFIC_OUT: Public network outbound bandwidth.</li> <li>WAN_TRAFFIC_IN: Public network inbound bandwidth.</li> <li>TCP_CURR_ESTAB: TCP connections.</li>
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Threshold(self):
        """Alarm threshold values: <br><li>CPU_UTILIZATION: [1, 100], Unit: %.</li> <li>MEM_UTILIZATION: [1, 100], Unit: %.</li> <li>LAN_TRAFFIC_OUT: >0, Unit: Mbps.</li> <li>LAN_TRAFFIC_IN: >0, Unit: Mbps.</li> <li>WAN_TRAFFIC_OUT: >0, Unit: Mbps.</li> <li>WAN_TRAFFIC_IN: >0, Unit: Mbps.</li> <li>TCP_CURR_ESTAB: >0, Unit: Count.</li>
        :rtype: int
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Period(self):
        """Time period in seconds. Enumerated values: 60, 300.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ContinuousTime(self):
        """Number of repetitions. Value range: [1, 10]
        :rtype: int
        """
        return self._ContinuousTime

    @ContinuousTime.setter
    def ContinuousTime(self, ContinuousTime):
        self._ContinuousTime = ContinuousTime

    @property
    def Statistic(self):
        """Statistics type. Value range: <br><li>AVERAGE: average </li><li>MAXIMUM: maximum <li>MINIMUM: minimum </li><br> Default value: AVERAGE
        :rtype: str
        """
        return self._Statistic

    @Statistic.setter
    def Statistic(self, Statistic):
        self._Statistic = Statistic

    @property
    def PreciseThreshold(self):
        """Precise alarm threshold values. This parameter is not used as an input argument but is used solely as an output parameter for the query API: <br><li>CPU_UTILIZATION: (0, 100], Unit: %.</li> <li>MEM_UTILIZATION: (0, 100], Unit: %.</li> <li>LAN_TRAFFIC_OUT: >0, Unit: Mbps.</li> <li>LAN_TRAFFIC_IN: >0, Unit: Mbps.</li> <li>WAN_TRAFFIC_OUT: >0, Unit: Mbps.</li> <li>WAN_TRAFFIC_IN: >0, Unit: Mbps.</li> <li>TCP_CURR_ESTAB: >0, Unit: Count.</li>
        :rtype: float
        """
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
        :param _TerminationPolicies: Termination policy, whose maximum length is currently 1. Valid values include OLDEST_INSTANCE and NEWEST_INSTANCE.
<li>OLDEST_INSTANCE: Terminate the oldest instance in the scaling group first.</li>
<li>NEWEST_INSTANCE: Terminate the newest instance in the scaling group first.</li>
        :type TerminationPolicies: list of str
        :param _VpcId: VPC ID. This field is left empty for basic networks. You need to specify SubnetIds when modifying the network of the auto scaling group to a VPC with a specified VPC ID. Specify Zones when modifying the network to a basic network.
        :type VpcId: str
        :param _Zones: List of availability zones
        :type Zones: list of str
        :param _RetryPolicy: Retry policy, whose valid values include IMMEDIATE_RETRY, INCREMENTAL_INTERVALS, and NO_RETRY, with the default value being IMMEDIATE_RETRY. A partially successful scaling activity is considered a failed activity.
<li>IMMEDIATE_RETRY: Immediately retry, and quickly retry in a short period. There will be no retry anymore after a certain number of consecutive failures (5).</li>
<li>INCREMENTAL_INTERVALS: Retry with incremental intervals. As the number of consecutive failures increases, the retry intervals gradually become longer, ranging from seconds to one day.</li>
<li>NO_RETRY: There will be no retry until another user call or alarm information is received.</li>
        :type RetryPolicy: str
        :param _ZonesCheckPolicy: AZ verification policy, whose valid values include ALL and ANY, with the default value being ANY. This policy comes into effect when actual changes are made to resource-related fields in the scaling group (such as launch configuration, AZ, or subnet).
<li>ALL: Verification passes if all AZs or subnets are available; otherwise, a verification error will be reported.<li>
<li>ANY: Verification passes if any AZ or subnet is available; otherwise, a verification error will be reported.</li>

Common reasons for unavailable AZs or subnets include the CVM InstanceType in the AZ being sold out, the CBS cloud disk in the AZ being sold out, insufficient quota in the AZ, and insufficient IP addresses in the subnet.
If there is no AZ or subnet in Zones/SubnetIds, a verification error will be reported regardless of the values of ZonesCheckPolicy.
        :type ZonesCheckPolicy: str
        :param _ServiceSettings: Service settings such as unhealthy instance replacement.
        :type ServiceSettings: :class:`tencentcloud.autoscaling.v20180419.models.ServiceSettings`
        :param _Ipv6AddressCount: The number of IPv6 addresses that an instance has. Valid values: 0 and 1.
        :type Ipv6AddressCount: int
        :param _MultiZoneSubnetPolicy: Multi-AZ/multi-subnet policy, whose valid values include PRIORITY and EQUALITY, with the default value being PRIORITY.
<li>PRIORITY: Instances are attempted to be created taking the order of the AZ/subnet list as the priority. If the highest-priority AZ/subnet can create instances successfully, instances can always be created in that AZ/subnet.</li>
<li>EQUALITY: The instances added through scale-out will be distributed across multiple AZs/subnets to ensure a relatively balanced number of instances in each AZ/subnet after scaling out.</li>

Points to consider regarding this policy:
<li>When the scaling group is based on a classic network, this policy applies to the multi-AZ; when the scaling group is based on a VPC network, this policy applies to the multi-subnet, in this case, the AZs are no longer considered. For example, if there are four subnets labeled A, B, C, and D, where A, B, and C are in AZ 1 and D is in AZ 2, the subnets A, B, C, and D are considered for sorting without regard to AZs 1 and 2.</li>
<li>This policy applies to the multi-AZ/multi-subnet and not to the InstanceTypes parameter of the launch configuration, which is selected according to the priority policy.</li>
<li>When instances are created according to the PRIORITY policy, ensure the policy for multiple models first, followed by the policy for the multi-AZ/subnet. For example, with models A and B and subnets 1, 2, and 3, attempts will be made in the order of A1, A2, A3, B1, B2, and B3. If A1 is sold out, A2 will be attempted (instead of B1).</li>
        :type MultiZoneSubnetPolicy: str
        :param _HealthCheckType: Scaling group instance health check type, whose valid values include:
<li>CVM: Determines whether an instance is unhealthy based on its network status. An unhealthy network status is indicated by an event where instances become unreachable via PING. Detailed criteria of judgment can be found in [Instance Health Check](https://intl.cloud.tencent.com/document/product/377/8553?from_cn_redirect=1).</li>
<li>CLB: Determines whether an instance is unhealthy based on the health check status of CLB. For principles behind CLB health checks, see [Health Check](https://intl.cloud.tencent.com/document/product/214/6097?from_cn_redirect=1).</li>
        :type HealthCheckType: str
        :param _LoadBalancerHealthCheckGracePeriod: Grace period of the CLB health check
        :type LoadBalancerHealthCheckGracePeriod: int
        :param _InstanceAllocationPolicy: Instance assignment policy, whose valid values include LAUNCH_CONFIGURATION and SPOT_MIXED.
<li>LAUNCH_CONFIGURATION: Represent the traditional mode of assigning instances according to the launch configuration.</li>
<li>SPOT_MIXED: Represent the spot mixed mode. Currently, this mode is supported only when the launch configuration is set to the pay-as-you-go billing mode. In the mixed mode, the scaling group will scale out pay-as-you-go models or spot models based on the predefined settings. When the mixed mode is used, the billing type of the associated launch configuration cannot be modified.</li>
        :type InstanceAllocationPolicy: str
        :param _SpotMixedAllocationPolicy: Specifies how to assign pay-as-you-go instances and spot instances.
This parameter is valid only when `InstanceAllocationPolicy` is set to `SPOT_MIXED`.
        :type SpotMixedAllocationPolicy: :class:`tencentcloud.autoscaling.v20180419.models.SpotMixedAllocationPolicy`
        :param _CapacityRebalance: Capacity rebalancing feature, which is applicable only to spot instances within the scaling group. Valid values:
<li>TRUE: Enable this feature. When spot instances in the scaling group are about to be automatically recycled by the spot instance service, AS proactively initiates the termination process of the spot instances. If there is a configured scale-in hook, it will be triggered before termination. After the termination process starts, AS asynchronously initiates the scale-out to reach the expected number of instances.</li>
<li>FALSE: Disable this feature. AS waits for the spot instance to be terminated before scaling out to reach the number of instances expected by the scaling group.</li>
        :type CapacityRebalance: bool
        :param _InstanceNameIndexSettings: Instance name sequencing settings. When enabled, an incremental numeric sequence will be appended to the names of instances automatically created within the scaling group.
        :type InstanceNameIndexSettings: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameIndexSettings`
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
        self._InstanceNameIndexSettings = None

    @property
    def AutoScalingGroupId(self):
        """Auto scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def AutoScalingGroupName(self):
        """Auto scaling group name, which can only contain letters, numbers, underscores, hyphens ("-"), and decimal points with a maximum length of 55 bytes and must be unique under your account.
        :rtype: str
        """
        return self._AutoScalingGroupName

    @AutoScalingGroupName.setter
    def AutoScalingGroupName(self, AutoScalingGroupName):
        self._AutoScalingGroupName = AutoScalingGroupName

    @property
    def DefaultCooldown(self):
        """Default cooldown period in seconds. Default value: 300
        :rtype: int
        """
        return self._DefaultCooldown

    @DefaultCooldown.setter
    def DefaultCooldown(self, DefaultCooldown):
        self._DefaultCooldown = DefaultCooldown

    @property
    def DesiredCapacity(self):
        """Desired number of instances. The number should be no larger than the maximum and no smaller than minimum number of instances
        :rtype: int
        """
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def LaunchConfigurationId(self):
        """Launch configuration ID
        :rtype: str
        """
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def MaxSize(self):
        """Maximum number of instances. Value range: 0-2,000.
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        """Minimum number of instances. Value range: 0-2,000.
        :rtype: int
        """
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def ProjectId(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SubnetIds(self):
        """List of subnet IDs
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def TerminationPolicies(self):
        """Termination policy, whose maximum length is currently 1. Valid values include OLDEST_INSTANCE and NEWEST_INSTANCE.
<li>OLDEST_INSTANCE: Terminate the oldest instance in the scaling group first.</li>
<li>NEWEST_INSTANCE: Terminate the newest instance in the scaling group first.</li>
        :rtype: list of str
        """
        return self._TerminationPolicies

    @TerminationPolicies.setter
    def TerminationPolicies(self, TerminationPolicies):
        self._TerminationPolicies = TerminationPolicies

    @property
    def VpcId(self):
        """VPC ID. This field is left empty for basic networks. You need to specify SubnetIds when modifying the network of the auto scaling group to a VPC with a specified VPC ID. Specify Zones when modifying the network to a basic network.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Zones(self):
        """List of availability zones
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RetryPolicy(self):
        """Retry policy, whose valid values include IMMEDIATE_RETRY, INCREMENTAL_INTERVALS, and NO_RETRY, with the default value being IMMEDIATE_RETRY. A partially successful scaling activity is considered a failed activity.
<li>IMMEDIATE_RETRY: Immediately retry, and quickly retry in a short period. There will be no retry anymore after a certain number of consecutive failures (5).</li>
<li>INCREMENTAL_INTERVALS: Retry with incremental intervals. As the number of consecutive failures increases, the retry intervals gradually become longer, ranging from seconds to one day.</li>
<li>NO_RETRY: There will be no retry until another user call or alarm information is received.</li>
        :rtype: str
        """
        return self._RetryPolicy

    @RetryPolicy.setter
    def RetryPolicy(self, RetryPolicy):
        self._RetryPolicy = RetryPolicy

    @property
    def ZonesCheckPolicy(self):
        """AZ verification policy, whose valid values include ALL and ANY, with the default value being ANY. This policy comes into effect when actual changes are made to resource-related fields in the scaling group (such as launch configuration, AZ, or subnet).
<li>ALL: Verification passes if all AZs or subnets are available; otherwise, a verification error will be reported.<li>
<li>ANY: Verification passes if any AZ or subnet is available; otherwise, a verification error will be reported.</li>

Common reasons for unavailable AZs or subnets include the CVM InstanceType in the AZ being sold out, the CBS cloud disk in the AZ being sold out, insufficient quota in the AZ, and insufficient IP addresses in the subnet.
If there is no AZ or subnet in Zones/SubnetIds, a verification error will be reported regardless of the values of ZonesCheckPolicy.
        :rtype: str
        """
        return self._ZonesCheckPolicy

    @ZonesCheckPolicy.setter
    def ZonesCheckPolicy(self, ZonesCheckPolicy):
        self._ZonesCheckPolicy = ZonesCheckPolicy

    @property
    def ServiceSettings(self):
        """Service settings such as unhealthy instance replacement.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ServiceSettings`
        """
        return self._ServiceSettings

    @ServiceSettings.setter
    def ServiceSettings(self, ServiceSettings):
        self._ServiceSettings = ServiceSettings

    @property
    def Ipv6AddressCount(self):
        """The number of IPv6 addresses that an instance has. Valid values: 0 and 1.
        :rtype: int
        """
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount

    @property
    def MultiZoneSubnetPolicy(self):
        """Multi-AZ/multi-subnet policy, whose valid values include PRIORITY and EQUALITY, with the default value being PRIORITY.
<li>PRIORITY: Instances are attempted to be created taking the order of the AZ/subnet list as the priority. If the highest-priority AZ/subnet can create instances successfully, instances can always be created in that AZ/subnet.</li>
<li>EQUALITY: The instances added through scale-out will be distributed across multiple AZs/subnets to ensure a relatively balanced number of instances in each AZ/subnet after scaling out.</li>

Points to consider regarding this policy:
<li>When the scaling group is based on a classic network, this policy applies to the multi-AZ; when the scaling group is based on a VPC network, this policy applies to the multi-subnet, in this case, the AZs are no longer considered. For example, if there are four subnets labeled A, B, C, and D, where A, B, and C are in AZ 1 and D is in AZ 2, the subnets A, B, C, and D are considered for sorting without regard to AZs 1 and 2.</li>
<li>This policy applies to the multi-AZ/multi-subnet and not to the InstanceTypes parameter of the launch configuration, which is selected according to the priority policy.</li>
<li>When instances are created according to the PRIORITY policy, ensure the policy for multiple models first, followed by the policy for the multi-AZ/subnet. For example, with models A and B and subnets 1, 2, and 3, attempts will be made in the order of A1, A2, A3, B1, B2, and B3. If A1 is sold out, A2 will be attempted (instead of B1).</li>
        :rtype: str
        """
        return self._MultiZoneSubnetPolicy

    @MultiZoneSubnetPolicy.setter
    def MultiZoneSubnetPolicy(self, MultiZoneSubnetPolicy):
        self._MultiZoneSubnetPolicy = MultiZoneSubnetPolicy

    @property
    def HealthCheckType(self):
        """Scaling group instance health check type, whose valid values include:
<li>CVM: Determines whether an instance is unhealthy based on its network status. An unhealthy network status is indicated by an event where instances become unreachable via PING. Detailed criteria of judgment can be found in [Instance Health Check](https://intl.cloud.tencent.com/document/product/377/8553?from_cn_redirect=1).</li>
<li>CLB: Determines whether an instance is unhealthy based on the health check status of CLB. For principles behind CLB health checks, see [Health Check](https://intl.cloud.tencent.com/document/product/214/6097?from_cn_redirect=1).</li>
        :rtype: str
        """
        return self._HealthCheckType

    @HealthCheckType.setter
    def HealthCheckType(self, HealthCheckType):
        self._HealthCheckType = HealthCheckType

    @property
    def LoadBalancerHealthCheckGracePeriod(self):
        """Grace period of the CLB health check
        :rtype: int
        """
        return self._LoadBalancerHealthCheckGracePeriod

    @LoadBalancerHealthCheckGracePeriod.setter
    def LoadBalancerHealthCheckGracePeriod(self, LoadBalancerHealthCheckGracePeriod):
        self._LoadBalancerHealthCheckGracePeriod = LoadBalancerHealthCheckGracePeriod

    @property
    def InstanceAllocationPolicy(self):
        """Instance assignment policy, whose valid values include LAUNCH_CONFIGURATION and SPOT_MIXED.
<li>LAUNCH_CONFIGURATION: Represent the traditional mode of assigning instances according to the launch configuration.</li>
<li>SPOT_MIXED: Represent the spot mixed mode. Currently, this mode is supported only when the launch configuration is set to the pay-as-you-go billing mode. In the mixed mode, the scaling group will scale out pay-as-you-go models or spot models based on the predefined settings. When the mixed mode is used, the billing type of the associated launch configuration cannot be modified.</li>
        :rtype: str
        """
        return self._InstanceAllocationPolicy

    @InstanceAllocationPolicy.setter
    def InstanceAllocationPolicy(self, InstanceAllocationPolicy):
        self._InstanceAllocationPolicy = InstanceAllocationPolicy

    @property
    def SpotMixedAllocationPolicy(self):
        """Specifies how to assign pay-as-you-go instances and spot instances.
This parameter is valid only when `InstanceAllocationPolicy` is set to `SPOT_MIXED`.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.SpotMixedAllocationPolicy`
        """
        return self._SpotMixedAllocationPolicy

    @SpotMixedAllocationPolicy.setter
    def SpotMixedAllocationPolicy(self, SpotMixedAllocationPolicy):
        self._SpotMixedAllocationPolicy = SpotMixedAllocationPolicy

    @property
    def CapacityRebalance(self):
        """Capacity rebalancing feature, which is applicable only to spot instances within the scaling group. Valid values:
<li>TRUE: Enable this feature. When spot instances in the scaling group are about to be automatically recycled by the spot instance service, AS proactively initiates the termination process of the spot instances. If there is a configured scale-in hook, it will be triggered before termination. After the termination process starts, AS asynchronously initiates the scale-out to reach the expected number of instances.</li>
<li>FALSE: Disable this feature. AS waits for the spot instance to be terminated before scaling out to reach the number of instances expected by the scaling group.</li>
        :rtype: bool
        """
        return self._CapacityRebalance

    @CapacityRebalance.setter
    def CapacityRebalance(self, CapacityRebalance):
        self._CapacityRebalance = CapacityRebalance

    @property
    def InstanceNameIndexSettings(self):
        """Instance name sequencing settings. When enabled, an incremental numeric sequence will be appended to the names of instances automatically created within the scaling group.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameIndexSettings`
        """
        return self._InstanceNameIndexSettings

    @InstanceNameIndexSettings.setter
    def InstanceNameIndexSettings(self, InstanceNameIndexSettings):
        self._InstanceNameIndexSettings = InstanceNameIndexSettings


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
        if params.get("InstanceNameIndexSettings") is not None:
            self._InstanceNameIndexSettings = InstanceNameIndexSettings()
            self._InstanceNameIndexSettings._deserialize(params.get("InstanceNameIndexSettings"))
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Auto scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def DesiredCapacity(self):
        """Desired capacity
        :rtype: int
        """
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def MinSize(self):
        """Minimum number of instances. Value range: 0-2000.
        :rtype: int
        """
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        """Maximum number of instances. Value range: 0-2000.
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _InstanceTypesCheckPolicy: InstanceType verification policy, which is effective when actual modification is made to InstanceTypes. Valid values include ALL and ANY and the default value is ANY.
<li>ALL: Verification passes if all InstanceTypes are available; otherwise, a verification error will be reported.</li>
<li>ANY: Verification passes if any InstanceType is available; otherwise, a verification error will be reported.</li>
Common reasons for unavailable InstanceTypes include the InstanceType being sold out, and the corresponding cloud disk being sold out.
If a model in InstanceTypes does not exist or has been abolished, a verification error will be reported regardless of the valid values set for InstanceTypesCheckPolicy.
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
<li>POSTPAID_BY_HOUR: pay-as-you-go hourly</li>
<li>SPOTPAID: spot instance</li>
<li> CDCPAID: dedicated cluster</li>
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
        :param _DiskTypePolicy: Cloud disk type selection policy. Valid values:
<li>ORIGINAL: Use the set cloud disk type.</li>
<li>AUTOMATIC: Automatically select the currently available cloud disk type.</li>
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
        :param _LoginSettings: Instance login settings, which include passwords, keys, or the original login settings inherited from the image. <br>Please note that specifying new login settings will overwrite the existing ones. For instance, if you previously used a password for login and then use this parameter to switch the login settings to a key, the original password will be removed.
        :type LoginSettings: :class:`tencentcloud.autoscaling.v20180419.models.LoginSettings`
        :param _InstanceTags: Instance tag list. By specifying this parameter, the instances added through scale-out can be bound to the tag. Up to 10 Tags can be specified.
This parameter will overwrite the original instance tag list. To add new tags, you need to pass the new tags along with the original tags.
        :type InstanceTags: list of InstanceTag
        :param _ImageFamily: Image family name.
        :type ImageFamily: str
        :param _DedicatedClusterId: Cloud Dedicated Cluster (CDC) ID.
        :type DedicatedClusterId: str
        :param _Metadata: Custom metadata.
        :type Metadata: :class:`tencentcloud.autoscaling.v20180419.models.Metadata`
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
        self._LoginSettings = None
        self._InstanceTags = None
        self._ImageFamily = None
        self._DedicatedClusterId = None
        self._Metadata = None

    @property
    def LaunchConfigurationId(self):
        """Launch configuration ID
        :rtype: str
        """
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def ImageId(self):
        """[Image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are three types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><br/>You can obtain the image IDs in the [CVM console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE).</li><li>You can also use the [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response.</li>
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def InstanceTypes(self):
        """List of instance types. Each type specifies different resource specifications. This list contains up to 10 instance types.
The launch configuration uses `InstanceType` to indicate one single instance type and `InstanceTypes` to indicate multiple instance types. Specifying the `InstanceTypes` field will invalidate the original `InstanceType`.
        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def InstanceTypesCheckPolicy(self):
        """InstanceType verification policy, which is effective when actual modification is made to InstanceTypes. Valid values include ALL and ANY and the default value is ANY.
<li>ALL: Verification passes if all InstanceTypes are available; otherwise, a verification error will be reported.</li>
<li>ANY: Verification passes if any InstanceType is available; otherwise, a verification error will be reported.</li>
Common reasons for unavailable InstanceTypes include the InstanceType being sold out, and the corresponding cloud disk being sold out.
If a model in InstanceTypes does not exist or has been abolished, a verification error will be reported regardless of the valid values set for InstanceTypesCheckPolicy.
        :rtype: str
        """
        return self._InstanceTypesCheckPolicy

    @InstanceTypesCheckPolicy.setter
    def InstanceTypesCheckPolicy(self, InstanceTypesCheckPolicy):
        self._InstanceTypesCheckPolicy = InstanceTypesCheckPolicy

    @property
    def LaunchConfigurationName(self):
        """Display name of the launch configuration, which can contain Chinese characters, letters, numbers, underscores, separators ("-"), and decimal points with a maximum length of 60 bytes.
        :rtype: str
        """
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def UserData(self):
        """Base64-encoded custom data of up to 16 KB. If you want to clear `UserData`, set it to an empty string.
        :rtype: str
        """
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def SecurityGroupIds(self):
        """Security group to which the instance belongs. This parameter can be obtained from the `SecurityGroupId` field in the response of the [`DescribeSecurityGroups`](https://intl.cloud.tencent.com/document/api/215/15808?from_cn_redirect=1) API.
At least one security group is required for this parameter. The security group specified is sequential.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InternetAccessible(self):
        """Information of the public network bandwidth configuration.
When the public outbound network bandwidth is 0 Mbps, assigning a public IP is not allowed. Accordingly, if a public IP is assigned, the new public network outbound bandwidth must be greater than 0 Mbps.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceChargeType(self):
        """Instance billing mode. Valid values:
<li>POSTPAID_BY_HOUR: pay-as-you-go hourly</li>
<li>SPOTPAID: spot instance</li>
<li> CDCPAID: dedicated cluster</li>
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        """Parameter setting for the prepaid mode (monthly subscription mode). This parameter can specify the renewal period, whether to set the auto-renewal, and other attributes of the monthly-subscribed instances.
This parameter is required when changing the instance billing mode to monthly subscription. It will be automatically discarded after you choose another billing mode.
This field requires passing in the `Period` field. Other fields that are not passed in will use their default values.
This field can be modified only when the current billing mode is monthly subscription.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def InstanceMarketOptions(self):
        """Market-related options for instances, such as parameters related to spot instances.
This parameter is required when changing the instance billing mode to spot instance. It will be automatically discarded after you choose another instance billing mode.
This field requires passing in the `MaxPrice` field under the `SpotOptions`. Other fields that are not passed in will use their default values.
This field can be modified only when the current billing mode is spot instance.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        """
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def DiskTypePolicy(self):
        """Cloud disk type selection policy. Valid values:
<li>ORIGINAL: Use the set cloud disk type.</li>
<li>AUTOMATIC: Automatically select the currently available cloud disk type.</li>
        :rtype: str
        """
        return self._DiskTypePolicy

    @DiskTypePolicy.setter
    def DiskTypePolicy(self, DiskTypePolicy):
        self._DiskTypePolicy = DiskTypePolicy

    @property
    def SystemDisk(self):
        """Instance system disk configurations
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """Configuration information of instance data disks.
Up to 11 data disks can be specified and will be collectively modified. Please provide all the new values for the modification.
The default data disk should be the same as the system disk.
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def HostNameSettings(self):
        """CVM hostname settings.
This field is not supported for Windows instances.
This field requires passing the `HostName` field. Other fields that are not passed in will use their default values.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.HostNameSettings`
        """
        return self._HostNameSettings

    @HostNameSettings.setter
    def HostNameSettings(self, HostNameSettings):
        self._HostNameSettings = HostNameSettings

    @property
    def InstanceNameSettings(self):
        """Settings of CVM instance names. 
If this field is configured in a launch configuration, the `InstanceName` of a CVM created by the scaling group will be generated according to the configuration; otherwise, it will be in the `as-{{AutoScalingGroupName }}` format.
This field requires passing in the `InstanceName` field. Other fields that are not passed in will use their default values.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameSettings`
        """
        return self._InstanceNameSettings

    @InstanceNameSettings.setter
    def InstanceNameSettings(self, InstanceNameSettings):
        self._InstanceNameSettings = InstanceNameSettings

    @property
    def EnhancedService(self):
        """Specifies whether to enable additional services, such as security services and monitoring service.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.EnhancedService`
        """
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def CamRoleName(self):
        """CAM role name. This parameter can be obtained from the `roleName` field returned by DescribeRoleList API.
        :rtype: str
        """
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HpcClusterId(self):
        """HPC ID<br>
Note: This field is default to empty
        :rtype: str
        """
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def IPv6InternetAccessible(self):
        """IPv6 public network bandwidth configuration. If the IPv6 address is available in the new instance, public network bandwidth can be allocated to the IPv6 address. This parameter is invalid if `Ipv6AddressCount` of the scaling group associated with the launch configuration is 0.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.IPv6InternetAccessible`
        """
        return self._IPv6InternetAccessible

    @IPv6InternetAccessible.setter
    def IPv6InternetAccessible(self, IPv6InternetAccessible):
        self._IPv6InternetAccessible = IPv6InternetAccessible

    @property
    def DisasterRecoverGroupIds(self):
        """Placement group ID. Only one is allowed.
        :rtype: list of str
        """
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def LoginSettings(self):
        """Instance login settings, which include passwords, keys, or the original login settings inherited from the image. <br>Please note that specifying new login settings will overwrite the existing ones. For instance, if you previously used a password for login and then use this parameter to switch the login settings to a key, the original password will be removed.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.LoginSettings`
        """
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def InstanceTags(self):
        """Instance tag list. By specifying this parameter, the instances added through scale-out can be bound to the tag. Up to 10 Tags can be specified.
This parameter will overwrite the original instance tag list. To add new tags, you need to pass the new tags along with the original tags.
        :rtype: list of InstanceTag
        """
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def ImageFamily(self):
        """Image family name.
        :rtype: str
        """
        return self._ImageFamily

    @ImageFamily.setter
    def ImageFamily(self, ImageFamily):
        self._ImageFamily = ImageFamily

    @property
    def DedicatedClusterId(self):
        """Cloud Dedicated Cluster (CDC) ID.
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def Metadata(self):
        """Custom metadata.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.Metadata`
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata


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
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("InstanceTags") is not None:
            self._InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTag()
                obj._deserialize(item)
                self._InstanceTags.append(obj)
        self._ImageFamily = params.get("ImageFamily")
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        if params.get("Metadata") is not None:
            self._Metadata = Metadata()
            self._Metadata._deserialize(params.get("Metadata"))
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _LifecycleTransition: Scenario for entering the lifecycle hook. Valid values:
<li>INSTANCE_LAUNCHING: after the instance is launched.</li>
<li>INSTANCE_TERMINATING: before the instance is terminated.</li>
        :type LifecycleTransition: str
        :param _DefaultResult: Action to be taken by the scaling group in case of lifecycle hook timeout. Valid values:
<li>CONTINUE: Continue the scaling activity after timeout.</li>
<li>ABANDON: Terminate the scaling activity after timeout.</li>
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
        """Lifecycle hook ID.
        :rtype: str
        """
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def LifecycleHookName(self):
        """Lifecycle hook name.
        :rtype: str
        """
        return self._LifecycleHookName

    @LifecycleHookName.setter
    def LifecycleHookName(self, LifecycleHookName):
        self._LifecycleHookName = LifecycleHookName

    @property
    def LifecycleTransition(self):
        """Scenario for entering the lifecycle hook. Valid values:
<li>INSTANCE_LAUNCHING: after the instance is launched.</li>
<li>INSTANCE_TERMINATING: before the instance is terminated.</li>
        :rtype: str
        """
        return self._LifecycleTransition

    @LifecycleTransition.setter
    def LifecycleTransition(self, LifecycleTransition):
        self._LifecycleTransition = LifecycleTransition

    @property
    def DefaultResult(self):
        """Action to be taken by the scaling group in case of lifecycle hook timeout. Valid values:
<li>CONTINUE: Continue the scaling activity after timeout.</li>
<li>ABANDON: Terminate the scaling activity after timeout.</li>
        :rtype: str
        """
        return self._DefaultResult

    @DefaultResult.setter
    def DefaultResult(self, DefaultResult):
        self._DefaultResult = DefaultResult

    @property
    def HeartbeatTimeout(self):
        """The maximum length of time (in seconds) that can elapse before the lifecycle hook times out. Value range: 30 - 7,200 seconds.
        :rtype: int
        """
        return self._HeartbeatTimeout

    @HeartbeatTimeout.setter
    def HeartbeatTimeout(self, HeartbeatTimeout):
        self._HeartbeatTimeout = HeartbeatTimeout

    @property
    def NotificationMetadata(self):
        """Additional information sent by AS to the notification target.
        :rtype: str
        """
        return self._NotificationMetadata

    @NotificationMetadata.setter
    def NotificationMetadata(self, NotificationMetadata):
        self._NotificationMetadata = NotificationMetadata

    @property
    def LifecycleTransitionType(self):
        """The scenario where the lifecycle hook is applied. `EXTENSION`: The lifecycle hook will be triggered when `AttachInstances`, `DetachInstances` or `RemoveInstances` is called. `NORMAL`: The lifecycle hook is not triggered by the above APIs.
        :rtype: str
        """
        return self._LifecycleTransitionType

    @LifecycleTransitionType.setter
    def LifecycleTransitionType(self, LifecycleTransitionType):
        self._LifecycleTransitionType = LifecycleTransitionType

    @property
    def NotificationTarget(self):
        """Information of the notification target.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.NotificationTarget`
        """
        return self._NotificationTarget

    @NotificationTarget.setter
    def NotificationTarget(self, NotificationTarget):
        self._NotificationTarget = NotificationTarget

    @property
    def LifecycleCommand(self):
        """Remote command execution object.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.LifecycleCommand`
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ForwardLoadBalancers(self):
        """List of application CLBs to modify. Up to 100 CLBs allowed.
        :rtype: list of ForwardLoadBalancer
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        """Scaling activity ID
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _LoadBalancersCheckPolicy: CLB verification policy. Valid values: ALL and DIFF. Default value: ALL.
<li>ALL: The CLB passes the verification only when all CLB parameters are valid. Otherwise, a verification error occurs.</li>
<li>DIFF: The CLB passes the verification only when the CLB parameters with changes are valid. Otherwise, a verification error occurs.</li>
        :type LoadBalancersCheckPolicy: str
        """
        self._AutoScalingGroupId = None
        self._LoadBalancerIds = None
        self._ForwardLoadBalancers = None
        self._LoadBalancersCheckPolicy = None

    @property
    def AutoScalingGroupId(self):
        """Auto scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def LoadBalancerIds(self):
        """List of classic CLB IDs. Currently, the maximum length is 20. You cannot specify LoadBalancerIds and ForwardLoadBalancers at the same time.
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ForwardLoadBalancers(self):
        """List of application CLBs. Up to 100 CLBs are allowed. `LoadBalancerIds` and `ForwardLoadBalancers` cannot be specified at the same time.
        :rtype: list of ForwardLoadBalancer
        """
        return self._ForwardLoadBalancers

    @ForwardLoadBalancers.setter
    def ForwardLoadBalancers(self, ForwardLoadBalancers):
        self._ForwardLoadBalancers = ForwardLoadBalancers

    @property
    def LoadBalancersCheckPolicy(self):
        """CLB verification policy. Valid values: ALL and DIFF. Default value: ALL.
<li>ALL: The CLB passes the verification only when all CLB parameters are valid. Otherwise, a verification error occurs.</li>
<li>DIFF: The CLB passes the verification only when the CLB parameters with changes are valid. Otherwise, a verification error occurs.</li>
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        """Scaling activity ID
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """ID of the notification to be modified.
        :rtype: str
        """
        return self._AutoScalingNotificationId

    @AutoScalingNotificationId.setter
    def AutoScalingNotificationId(self, AutoScalingNotificationId):
        self._AutoScalingNotificationId = AutoScalingNotificationId

    @property
    def NotificationTypes(self):
        """Notification type, i.e., the set of types of notifications to be subscribed to. Value range:
<li>SCALE_OUT_SUCCESSFUL: scale-out succeeded</li>
<li>SCALE_OUT_FAILED: scale-out failed</li>
<li>SCALE_IN_SUCCESSFUL: scale-in succeeded</li>
<li>SCALE_IN_FAILED: scale-in failed</li>
<li>REPLACE_UNHEALTHY_INSTANCE_SUCCESSFUL: unhealthy instance replacement succeeded</li>
<li>REPLACE_UNHEALTHY_INSTANCE_FAILED: unhealthy instance replacement failed</li>
        :rtype: list of str
        """
        return self._NotificationTypes

    @NotificationTypes.setter
    def NotificationTypes(self, NotificationTypes):
        self._NotificationTypes = NotificationTypes

    @property
    def NotificationUserGroupIds(self):
        """Notification group ID, which is the set of user group IDs. You can query the user group IDs through the [ListGroups](https://intl.cloud.tencent.com/document/product/598/34589?from_cn_redirect=1) API.
        :rtype: list of str
        """
        return self._NotificationUserGroupIds

    @NotificationUserGroupIds.setter
    def NotificationUserGroupIds(self, NotificationUserGroupIds):
        self._NotificationUserGroupIds = NotificationUserGroupIds

    @property
    def QueueName(self):
        """CMQ or TDMQ CMQ queue name.
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def TopicName(self):
        """CMQ or TDMQ CMQ toipc name.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _AdjustmentValue: The adjustment value for the expected number of instances after an alarm is triggered. It applies only to simple policies. <li>When AdjustmentType is CHANGE_IN_CAPACITY, a positive AdjustmentValue indicates an increase in the number of instances after the alarm is triggered, and a negative AdjustmentValue indicates a decrease in the number of instances after the alarm is triggered.</li> <li>When AdjustmentType is EXACT_CAPACITY, the value of AdjustmentValue represents the expected number of instances after the alarm is triggered, which should be greater than or equal to 0.</li> <li>When AdjustmentType is PERCENT_CHANGE_IN_CAPACITY, a positive AdjustmentValue indicates an increase in the number of instances by percentage after the alarm is triggered, and a negative AdjustmentValue indicates a decrease in the number of instances by percentage after the alarm is triggered. The unit is: %.</li>
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
        """Alarm policy ID.
        :rtype: str
        """
        return self._AutoScalingPolicyId

    @AutoScalingPolicyId.setter
    def AutoScalingPolicyId(self, AutoScalingPolicyId):
        self._AutoScalingPolicyId = AutoScalingPolicyId

    @property
    def ScalingPolicyName(self):
        """Alarm policy name.
        :rtype: str
        """
        return self._ScalingPolicyName

    @ScalingPolicyName.setter
    def ScalingPolicyName(self, ScalingPolicyName):
        self._ScalingPolicyName = ScalingPolicyName

    @property
    def AdjustmentType(self):
        """The method to adjust the desired capacity after the alarm is triggered. It’s only available when `ScalingPolicyType` is `Simple`. Valid values: <br><li>`CHANGE_IN_CAPACITY`: Increase or decrease the desired capacity </li><li>`EXACT_CAPACITY`: Adjust to the specified desired capacity </li> <li>`PERCENT_CHANGE_IN_CAPACITY`: Adjust the desired capacity by percentage </li>
        :rtype: str
        """
        return self._AdjustmentType

    @AdjustmentType.setter
    def AdjustmentType(self, AdjustmentType):
        self._AdjustmentType = AdjustmentType

    @property
    def AdjustmentValue(self):
        """The adjustment value for the expected number of instances after an alarm is triggered. It applies only to simple policies. <li>When AdjustmentType is CHANGE_IN_CAPACITY, a positive AdjustmentValue indicates an increase in the number of instances after the alarm is triggered, and a negative AdjustmentValue indicates a decrease in the number of instances after the alarm is triggered.</li> <li>When AdjustmentType is EXACT_CAPACITY, the value of AdjustmentValue represents the expected number of instances after the alarm is triggered, which should be greater than or equal to 0.</li> <li>When AdjustmentType is PERCENT_CHANGE_IN_CAPACITY, a positive AdjustmentValue indicates an increase in the number of instances by percentage after the alarm is triggered, and a negative AdjustmentValue indicates a decrease in the number of instances by percentage after the alarm is triggered. The unit is: %.</li>
        :rtype: int
        """
        return self._AdjustmentValue

    @AdjustmentValue.setter
    def AdjustmentValue(self, AdjustmentValue):
        self._AdjustmentValue = AdjustmentValue

    @property
    def Cooldown(self):
        """Cooldown period (in seconds). It’s only available when `ScalingPolicyType` is `Simple`.
        :rtype: int
        """
        return self._Cooldown

    @Cooldown.setter
    def Cooldown(self, Cooldown):
        self._Cooldown = Cooldown

    @property
    def MetricAlarm(self):
        """Alarm monitoring metric. It’s only available when `ScalingPolicyType` is `Simple`.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.MetricAlarm`
        """
        return self._MetricAlarm

    @MetricAlarm.setter
    def MetricAlarm(self, MetricAlarm):
        self._MetricAlarm = MetricAlarm

    @property
    def PredefinedMetricType(self):
        """Preset monitoring item. It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Valid values: <br><li>ASG_AVG_CPU_UTILIZATION: Average CPU utilization</li><li>ASG_AVG_LAN_TRAFFIC_OUT: Average private bandwidth out</li><li>ASG_AVG_LAN_TRAFFIC_IN: Average private bandwidth in</li><li>ASG_AVG_WAN_TRAFFIC_OUT: Average public bandwidth out</li><li>ASG_AVG_WAN_TRAFFIC_IN: Average public bandwidth in</li>
        :rtype: str
        """
        return self._PredefinedMetricType

    @PredefinedMetricType.setter
    def PredefinedMetricType(self, PredefinedMetricType):
        self._PredefinedMetricType = PredefinedMetricType

    @property
    def TargetValue(self):
        """Target value. It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Value ranges: <br><li>`ASG_AVG_CPU_UTILIZATION` (in %): [1, 100)</li><li>`ASG_AVG_LAN_TRAFFIC_OUT` (in Mbps): >0</li><li>`ASG_AVG_LAN_TRAFFIC_IN` (in Mbps): >0</li><li>`ASG_AVG_WAN_TRAFFIC_OUT` (in Mbps): >0</li><li>`ASG_AVG_WAN_TRAFFIC_IN` (in Mbps): >0</li>
        :rtype: int
        """
        return self._TargetValue

    @TargetValue.setter
    def TargetValue(self, TargetValue):
        self._TargetValue = TargetValue

    @property
    def EstimatedInstanceWarmup(self):
        """Instance warm-up period (in seconds). It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Value range: 0-3600.
        :rtype: int
        """
        return self._EstimatedInstanceWarmup

    @EstimatedInstanceWarmup.setter
    def EstimatedInstanceWarmup(self, EstimatedInstanceWarmup):
        self._EstimatedInstanceWarmup = EstimatedInstanceWarmup

    @property
    def DisableScaleIn(self):
        """Whether to disable scale-in. It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Valid values: <br><li>`true`: Scaling in is not allowed.</li><li>`false`: Allows both scale-out and scale-in</li>
        :rtype: bool
        """
        return self._DisableScaleIn

    @DisableScaleIn.setter
    def DisableScaleIn(self, DisableScaleIn):
        self._DisableScaleIn = DisableScaleIn

    @property
    def NotificationUserGroupIds(self):
        """This parameter is diused. Please use [CreateNotificationConfiguration](https://intl.cloud.tencent.com/document/api/377/33185?from_cn_redirect=1) instead.
Notification group ID, which is the set of user group IDs.
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """ID of the scheduled task to be edited
        :rtype: str
        """
        return self._ScheduledActionId

    @ScheduledActionId.setter
    def ScheduledActionId(self, ScheduledActionId):
        self._ScheduledActionId = ScheduledActionId

    @property
    def ScheduledActionName(self):
        """Scheduled task name, which can only contain letters, numbers, underscores, hyphens ("-"), and decimal points with a maximum length of 60 bytes and must be unique in an auto scaling group.
        :rtype: str
        """
        return self._ScheduledActionName

    @ScheduledActionName.setter
    def ScheduledActionName(self, ScheduledActionName):
        self._ScheduledActionName = ScheduledActionName

    @property
    def MaxSize(self):
        """The maximum number of instances set for the auto scaling group when the scheduled task is triggered.
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        """The minimum number of instances set for the auto scaling group when the scheduled task is triggered.
        :rtype: int
        """
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def DesiredCapacity(self):
        """The desired number of instances set for the auto scaling group when the scheduled task is triggered.
        :rtype: int
        """
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def StartTime(self):
        """Initial triggered time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard. <br>This parameter and `Recurrence` need to be specified at the same time. After the end time, the scheduled task will no longer take effect.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Recurrence(self):
        """Repeating mode of the scheduled task, which is in standard cron format. <br>This parameter and `EndTime` need to be specified at the same time.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Target type. Valid values: `CMQ_QUEUE`, `CMQ_TOPIC`, `TDMQ_CMQ_QUEUE` and `TDMQ_CMQ_TOPIC`.
<li> CMQ_QUEUE: Tencent Cloud message queue - queue model.</li>
<li> CMQ_TOPIC: Tencent Cloud message queue - topic model.</li>
<li> TDMQ_CMQ_QUEUE: Tencent Cloud TDMQ message queue - queue model.</li>
<li> TDMQ_CMQ_TOPIC: Tencent Cloud TDMQ message queue - topic model.</li>
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def QueueName(self):
        """Queue name. This parameter is required when `TargetType` is `CMQ_QUEUE` or `TDMQ_CMQ_QUEUE`.
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def TopicName(self):
        """Topic name. This parameter is required when `TargetType` is `CMQ_TOPIC` or `TDMQ_CMQ_TOPIC`.
        :rtype: str
        """
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
        


class RefreshActivity(AbstractModel):
    """Instance refresh activity.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Scaling group ID.
        :type AutoScalingGroupId: str
        :param _RefreshActivityId: Refresh activity ID.
        :type RefreshActivityId: str
        :param _OriginRefreshActivityId: Original refresh activity ID, which exists only in the rollback refresh activity.
Note: This field may return null, indicating that no valid value can be obtained.
        :type OriginRefreshActivityId: str
        :param _RefreshBatchSet: Refresh batch information list.
        :type RefreshBatchSet: list of RefreshBatch
        :param _RefreshMode: Refresh mode.
        :type RefreshMode: str
        :param _RefreshSettings: Instance update setting parameters.
        :type RefreshSettings: :class:`tencentcloud.autoscaling.v20180419.models.RefreshSettings`
        :param _ActivityType: Refresh activity type. Valid values:
<li>NORMAL: normal refresh activity.</li>
<li>ROLLBACK: rollback refresh activity.</li>
        :type ActivityType: str
        :param _Status: Refresh activity status. Valid values:
<li>INIT: initializing.</li>
<li>RUNNING: running.</li>
<li>SUCCESSFUL: successful.</li>
<li>FAILED_PAUSE: paused due to the failure of a refresh batch.</li>
<li>AUTO_PAUSE: automatically paused due to the pause policy.</li>
<li>MANUAL_PAUSE: manually paused.</li>
<li>CANCELLED: canceled.</li>
<li>FAILED: failed.</li>
        :type Status: str
        :param _CurrentRefreshBatchNum: Current refresh batch number. For example, a value of 2 indicates that the current activity is refreshing the second batch of instances.
Note: This field may return null, indicating that no valid value can be obtained.
        :type CurrentRefreshBatchNum: int
        :param _StartTime: Refresh activity start time.
Note: This field may return null, indicating that no valid value can be obtained.
        :type StartTime: str
        :param _EndTime: Refresh activity end time.
Note: This field may return null, indicating that no valid value can be obtained.
        :type EndTime: str
        :param _CreatedTime: Refresh activity creation time.
Note: This field may return null, indicating that no valid value can be obtained.
        :type CreatedTime: str
        """
        self._AutoScalingGroupId = None
        self._RefreshActivityId = None
        self._OriginRefreshActivityId = None
        self._RefreshBatchSet = None
        self._RefreshMode = None
        self._RefreshSettings = None
        self._ActivityType = None
        self._Status = None
        self._CurrentRefreshBatchNum = None
        self._StartTime = None
        self._EndTime = None
        self._CreatedTime = None

    @property
    def AutoScalingGroupId(self):
        """Scaling group ID.
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RefreshActivityId(self):
        """Refresh activity ID.
        :rtype: str
        """
        return self._RefreshActivityId

    @RefreshActivityId.setter
    def RefreshActivityId(self, RefreshActivityId):
        self._RefreshActivityId = RefreshActivityId

    @property
    def OriginRefreshActivityId(self):
        """Original refresh activity ID, which exists only in the rollback refresh activity.
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._OriginRefreshActivityId

    @OriginRefreshActivityId.setter
    def OriginRefreshActivityId(self, OriginRefreshActivityId):
        self._OriginRefreshActivityId = OriginRefreshActivityId

    @property
    def RefreshBatchSet(self):
        """Refresh batch information list.
        :rtype: list of RefreshBatch
        """
        return self._RefreshBatchSet

    @RefreshBatchSet.setter
    def RefreshBatchSet(self, RefreshBatchSet):
        self._RefreshBatchSet = RefreshBatchSet

    @property
    def RefreshMode(self):
        """Refresh mode.
        :rtype: str
        """
        return self._RefreshMode

    @RefreshMode.setter
    def RefreshMode(self, RefreshMode):
        self._RefreshMode = RefreshMode

    @property
    def RefreshSettings(self):
        """Instance update setting parameters.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.RefreshSettings`
        """
        return self._RefreshSettings

    @RefreshSettings.setter
    def RefreshSettings(self, RefreshSettings):
        self._RefreshSettings = RefreshSettings

    @property
    def ActivityType(self):
        """Refresh activity type. Valid values:
<li>NORMAL: normal refresh activity.</li>
<li>ROLLBACK: rollback refresh activity.</li>
        :rtype: str
        """
        return self._ActivityType

    @ActivityType.setter
    def ActivityType(self, ActivityType):
        self._ActivityType = ActivityType

    @property
    def Status(self):
        """Refresh activity status. Valid values:
<li>INIT: initializing.</li>
<li>RUNNING: running.</li>
<li>SUCCESSFUL: successful.</li>
<li>FAILED_PAUSE: paused due to the failure of a refresh batch.</li>
<li>AUTO_PAUSE: automatically paused due to the pause policy.</li>
<li>MANUAL_PAUSE: manually paused.</li>
<li>CANCELLED: canceled.</li>
<li>FAILED: failed.</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CurrentRefreshBatchNum(self):
        """Current refresh batch number. For example, a value of 2 indicates that the current activity is refreshing the second batch of instances.
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._CurrentRefreshBatchNum

    @CurrentRefreshBatchNum.setter
    def CurrentRefreshBatchNum(self, CurrentRefreshBatchNum):
        self._CurrentRefreshBatchNum = CurrentRefreshBatchNum

    @property
    def StartTime(self):
        """Refresh activity start time.
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Refresh activity end time.
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreatedTime(self):
        """Refresh activity creation time.
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._RefreshActivityId = params.get("RefreshActivityId")
        self._OriginRefreshActivityId = params.get("OriginRefreshActivityId")
        if params.get("RefreshBatchSet") is not None:
            self._RefreshBatchSet = []
            for item in params.get("RefreshBatchSet"):
                obj = RefreshBatch()
                obj._deserialize(item)
                self._RefreshBatchSet.append(obj)
        self._RefreshMode = params.get("RefreshMode")
        if params.get("RefreshSettings") is not None:
            self._RefreshSettings = RefreshSettings()
            self._RefreshSettings._deserialize(params.get("RefreshSettings"))
        self._ActivityType = params.get("ActivityType")
        self._Status = params.get("Status")
        self._CurrentRefreshBatchNum = params.get("CurrentRefreshBatchNum")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefreshBatch(AbstractModel):
    """Instance refresh batch information, containing the refresh status, instances, start and end time, etc., of the batch.

    """

    def __init__(self):
        r"""
        :param _RefreshBatchNum: Refresh batch number. For example, a value of 2 indicates that the current batch of instances will be refreshed in the second batch.
        :type RefreshBatchNum: int
        :param _RefreshBatchStatus: Refresh batch status. Valid values: <li>WAITING: pending refresh;</li> <li>INIT: initializing;</li> <li>RUNNING: refreshing;</li> <li>FAILED: refresh failed;</li> <li>PARTIALLY_SUCCESSFUL: partially successful in the batch;</li> <li>CANCELLED: cancelled;</li> <li>SUCCESSFUL: refresh successful.</li>
        :type RefreshBatchStatus: str
        :param _RefreshBatchRelatedInstanceSet: List of instances linked to a refresh batch.
        :type RefreshBatchRelatedInstanceSet: list of RefreshBatchRelatedInstance
        :param _StartTime: Refresh batch start time.
Note: This field may return null, indicating that no valid value can be obtained.
        :type StartTime: str
        :param _EndTime: Refresh batch end time.
Note: This field may return null, indicating that no valid value can be obtained.
        :type EndTime: str
        """
        self._RefreshBatchNum = None
        self._RefreshBatchStatus = None
        self._RefreshBatchRelatedInstanceSet = None
        self._StartTime = None
        self._EndTime = None

    @property
    def RefreshBatchNum(self):
        """Refresh batch number. For example, a value of 2 indicates that the current batch of instances will be refreshed in the second batch.
        :rtype: int
        """
        return self._RefreshBatchNum

    @RefreshBatchNum.setter
    def RefreshBatchNum(self, RefreshBatchNum):
        self._RefreshBatchNum = RefreshBatchNum

    @property
    def RefreshBatchStatus(self):
        """Refresh batch status. Valid values: <li>WAITING: pending refresh;</li> <li>INIT: initializing;</li> <li>RUNNING: refreshing;</li> <li>FAILED: refresh failed;</li> <li>PARTIALLY_SUCCESSFUL: partially successful in the batch;</li> <li>CANCELLED: cancelled;</li> <li>SUCCESSFUL: refresh successful.</li>
        :rtype: str
        """
        return self._RefreshBatchStatus

    @RefreshBatchStatus.setter
    def RefreshBatchStatus(self, RefreshBatchStatus):
        self._RefreshBatchStatus = RefreshBatchStatus

    @property
    def RefreshBatchRelatedInstanceSet(self):
        """List of instances linked to a refresh batch.
        :rtype: list of RefreshBatchRelatedInstance
        """
        return self._RefreshBatchRelatedInstanceSet

    @RefreshBatchRelatedInstanceSet.setter
    def RefreshBatchRelatedInstanceSet(self, RefreshBatchRelatedInstanceSet):
        self._RefreshBatchRelatedInstanceSet = RefreshBatchRelatedInstanceSet

    @property
    def StartTime(self):
        """Refresh batch start time.
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Refresh batch end time.
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._RefreshBatchNum = params.get("RefreshBatchNum")
        self._RefreshBatchStatus = params.get("RefreshBatchStatus")
        if params.get("RefreshBatchRelatedInstanceSet") is not None:
            self._RefreshBatchRelatedInstanceSet = []
            for item in params.get("RefreshBatchRelatedInstanceSet"):
                obj = RefreshBatchRelatedInstance()
                obj._deserialize(item)
                self._RefreshBatchRelatedInstanceSet.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefreshBatchRelatedInstance(AbstractModel):
    """Refresh batch associated instances, including the refresh activity status of individual instances and related scaling activity information.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _InstanceStatus: Refresh instance status. If an instance is removed or destroyed during the refresh process, its status will be updated to NOT_FOUND. Valid values: <br><li>WAITING: pending refresh.</li> <li>INIT: Initializing.</li> <li>RUNNING: Refreshing in progress.</li> <li>FAILED: Refresh failed.</li> <li>CANCELLED: Canceled.</li> <li>SUCCESSFUL: Refreshed.</li> <li>NOT_FOUND: Instance not found.
        :type InstanceStatus: str
        :param _LastActivityId: The most recent scaling activity ID during instance refresh can be queried via the DescribeAutoScalingActivities API.
Please note that scaling activities differ from instance refresh activities; a single instance refresh activity may involve multiple scaling activities.
Note: This field may return null, indicating that no valid value can be obtained.
        :type LastActivityId: str
        :param _InstanceStatusMessage: Instance refresh status information.
Note: This field may return null, indicating that no valid value can be obtained.
        :type InstanceStatusMessage: str
        """
        self._InstanceId = None
        self._InstanceStatus = None
        self._LastActivityId = None
        self._InstanceStatusMessage = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceStatus(self):
        """Refresh instance status. If an instance is removed or destroyed during the refresh process, its status will be updated to NOT_FOUND. Valid values: <br><li>WAITING: pending refresh.</li> <li>INIT: Initializing.</li> <li>RUNNING: Refreshing in progress.</li> <li>FAILED: Refresh failed.</li> <li>CANCELLED: Canceled.</li> <li>SUCCESSFUL: Refreshed.</li> <li>NOT_FOUND: Instance not found.
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def LastActivityId(self):
        """The most recent scaling activity ID during instance refresh can be queried via the DescribeAutoScalingActivities API.
Please note that scaling activities differ from instance refresh activities; a single instance refresh activity may involve multiple scaling activities.
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._LastActivityId

    @LastActivityId.setter
    def LastActivityId(self, LastActivityId):
        self._LastActivityId = LastActivityId

    @property
    def InstanceStatusMessage(self):
        """Instance refresh status information.
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._InstanceStatusMessage

    @InstanceStatusMessage.setter
    def InstanceStatusMessage(self, InstanceStatusMessage):
        self._InstanceStatusMessage = InstanceStatusMessage


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceStatus = params.get("InstanceStatus")
        self._LastActivityId = params.get("LastActivityId")
        self._InstanceStatusMessage = params.get("InstanceStatusMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefreshSettings(AbstractModel):
    """Instance refresh settings.

    """

    def __init__(self):
        r"""
        :param _RollingUpdateSettings: Rolling update settings parameters. RefreshMode is the rolling update. This parameter must be filled in.Note: This field may return null, indicating that no valid value can be obtained.
        :type RollingUpdateSettings: :class:`tencentcloud.autoscaling.v20180419.models.RollingUpdateSettings`
        :param _CheckInstanceTargetHealth: Whether to enable the backend service health check for the instance. Default value: FALSE. This parameter is valid only for the scaling group bound to an application-based CLB. After this feature is enabled, if the instance fails the check after refresh, the port weight of the CLB will be always 0, and it will be marked as a refresh failure. Valid values: <li>TRUE: enable;</li> <li>FALSE: disable.</li>
        :type CheckInstanceTargetHealth: bool
        """
        self._RollingUpdateSettings = None
        self._CheckInstanceTargetHealth = None

    @property
    def RollingUpdateSettings(self):
        """Rolling update settings parameters. RefreshMode is the rolling update. This parameter must be filled in.Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.RollingUpdateSettings`
        """
        return self._RollingUpdateSettings

    @RollingUpdateSettings.setter
    def RollingUpdateSettings(self, RollingUpdateSettings):
        self._RollingUpdateSettings = RollingUpdateSettings

    @property
    def CheckInstanceTargetHealth(self):
        """Whether to enable the backend service health check for the instance. Default value: FALSE. This parameter is valid only for the scaling group bound to an application-based CLB. After this feature is enabled, if the instance fails the check after refresh, the port weight of the CLB will be always 0, and it will be marked as a refresh failure. Valid values: <li>TRUE: enable;</li> <li>FALSE: disable.</li>
        :rtype: bool
        """
        return self._CheckInstanceTargetHealth

    @CheckInstanceTargetHealth.setter
    def CheckInstanceTargetHealth(self, CheckInstanceTargetHealth):
        self._CheckInstanceTargetHealth = CheckInstanceTargetHealth


    def _deserialize(self, params):
        if params.get("RollingUpdateSettings") is not None:
            self._RollingUpdateSettings = RollingUpdateSettings()
            self._RollingUpdateSettings._deserialize(params.get("RollingUpdateSettings"))
        self._CheckInstanceTargetHealth = params.get("CheckInstanceTargetHealth")
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
`RUNNING`: Processing the instance
`SUCCESSFUL`: Task succeeded on the instance
`FAILED`: Task failed on the instance
        :type InstanceStatus: str
        """
        self._InstanceId = None
        self._InstanceStatus = None

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceStatus(self):
        """Status of the instance in the scaling activity. Valid values:
`INIT`: Initializing
`RUNNING`: Processing the instance
`SUCCESSFUL`: Task succeeded on the instance
`FAILED`: Task failed on the instance
        :rtype: str
        """
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
        """Auto scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        """List of CVM instance IDs
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        """Scaling activity ID
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class ResumeInstanceRefreshRequest(AbstractModel):
    """ResumeInstanceRefresh request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Scaling group ID.
        :type AutoScalingGroupId: str
        :param _RefreshActivityId: Refresh activity ID.
        :type RefreshActivityId: str
        :param _ResumeMode: Recovery mode of instances that have failed to be refreshed in the current batch. If there are no failed instances, this parameter is invalid. Default value: RETRY. Valid values: <li>RETRY: Retry instances that have failed to be refreshed in the current batch.</li> <li>CONTINUE: Skip instances that have failed to be refreshed in the current batch.</li>
        :type ResumeMode: str
        """
        self._AutoScalingGroupId = None
        self._RefreshActivityId = None
        self._ResumeMode = None

    @property
    def AutoScalingGroupId(self):
        """Scaling group ID.
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RefreshActivityId(self):
        """Refresh activity ID.
        :rtype: str
        """
        return self._RefreshActivityId

    @RefreshActivityId.setter
    def RefreshActivityId(self, RefreshActivityId):
        self._RefreshActivityId = RefreshActivityId

    @property
    def ResumeMode(self):
        """Recovery mode of instances that have failed to be refreshed in the current batch. If there are no failed instances, this parameter is invalid. Default value: RETRY. Valid values: <li>RETRY: Retry instances that have failed to be refreshed in the current batch.</li> <li>CONTINUE: Skip instances that have failed to be refreshed in the current batch.</li>
        :rtype: str
        """
        return self._ResumeMode

    @ResumeMode.setter
    def ResumeMode(self, ResumeMode):
        self._ResumeMode = ResumeMode


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._RefreshActivityId = params.get("RefreshActivityId")
        self._ResumeMode = params.get("ResumeMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeInstanceRefreshResponse(AbstractModel):
    """ResumeInstanceRefresh response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RollbackInstanceRefreshRequest(AbstractModel):
    """RollbackInstanceRefresh request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Scaling group ID.
        :type AutoScalingGroupId: str
        :param _RefreshSettings: Refresh settings.
        :type RefreshSettings: :class:`tencentcloud.autoscaling.v20180419.models.RefreshSettings`
        :param _OriginRefreshActivityId: Original refresh activity ID.
        :type OriginRefreshActivityId: str
        :param _RefreshMode: Refresh mode, currently, only rolling updates are supported, with the default value being ROLLING_UPDATE_RESET.
        :type RefreshMode: str
        """
        self._AutoScalingGroupId = None
        self._RefreshSettings = None
        self._OriginRefreshActivityId = None
        self._RefreshMode = None

    @property
    def AutoScalingGroupId(self):
        """Scaling group ID.
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RefreshSettings(self):
        """Refresh settings.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.RefreshSettings`
        """
        return self._RefreshSettings

    @RefreshSettings.setter
    def RefreshSettings(self, RefreshSettings):
        self._RefreshSettings = RefreshSettings

    @property
    def OriginRefreshActivityId(self):
        """Original refresh activity ID.
        :rtype: str
        """
        return self._OriginRefreshActivityId

    @OriginRefreshActivityId.setter
    def OriginRefreshActivityId(self, OriginRefreshActivityId):
        self._OriginRefreshActivityId = OriginRefreshActivityId

    @property
    def RefreshMode(self):
        """Refresh mode, currently, only rolling updates are supported, with the default value being ROLLING_UPDATE_RESET.
        :rtype: str
        """
        return self._RefreshMode

    @RefreshMode.setter
    def RefreshMode(self, RefreshMode):
        self._RefreshMode = RefreshMode


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        if params.get("RefreshSettings") is not None:
            self._RefreshSettings = RefreshSettings()
            self._RefreshSettings._deserialize(params.get("RefreshSettings"))
        self._OriginRefreshActivityId = params.get("OriginRefreshActivityId")
        self._RefreshMode = params.get("RefreshMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackInstanceRefreshResponse(AbstractModel):
    """RollbackInstanceRefresh response structure.

    """

    def __init__(self):
        r"""
        :param _RefreshActivityId: Refresh activity ID.
        :type RefreshActivityId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RefreshActivityId = None
        self._RequestId = None

    @property
    def RefreshActivityId(self):
        """Refresh activity ID.
        :rtype: str
        """
        return self._RefreshActivityId

    @RefreshActivityId.setter
    def RefreshActivityId(self, RefreshActivityId):
        self._RefreshActivityId = RefreshActivityId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RefreshActivityId = params.get("RefreshActivityId")
        self._RequestId = params.get("RequestId")


class RollingUpdateSettings(AbstractModel):
    """Rolling update settings.

    """

    def __init__(self):
        r"""
        :param _BatchNumber: Batch quantity. The batch quantity should be a positive integer greater than 0, but cannot exceed the total number of instances pending refresh.
        :type BatchNumber: int
        :param _BatchPause: Pause policy between batches. Default value: Automatic. Valid values:
<li>FIRST_BATCH_PAUSE: Pause after the first batch of updates is completed.</li>
<li>BATCH_INTERVAL_PAUSE: Pause between batches.</li>
<li>AUTOMATIC: Do not pause.</li>
        :type BatchPause: str
        :param _MaxSurge: The maximum additional quantity of instances. After this parameter is set, create a batch of additional pay-as-you-go instances according to the launch configuration before the rolling update starts. After the rolling update is completed, the additional instances will be terminated.This parameter is used to ensure a certain number of instances available during the rolling update. The maximum additional quantity of instances cannot exceed the number of refreshing instances in a single batch of the rolling update. The rollback process does not support this parameter currently.
        :type MaxSurge: int
        """
        self._BatchNumber = None
        self._BatchPause = None
        self._MaxSurge = None

    @property
    def BatchNumber(self):
        """Batch quantity. The batch quantity should be a positive integer greater than 0, but cannot exceed the total number of instances pending refresh.
        :rtype: int
        """
        return self._BatchNumber

    @BatchNumber.setter
    def BatchNumber(self, BatchNumber):
        self._BatchNumber = BatchNumber

    @property
    def BatchPause(self):
        """Pause policy between batches. Default value: Automatic. Valid values:
<li>FIRST_BATCH_PAUSE: Pause after the first batch of updates is completed.</li>
<li>BATCH_INTERVAL_PAUSE: Pause between batches.</li>
<li>AUTOMATIC: Do not pause.</li>
        :rtype: str
        """
        return self._BatchPause

    @BatchPause.setter
    def BatchPause(self, BatchPause):
        self._BatchPause = BatchPause

    @property
    def MaxSurge(self):
        """The maximum additional quantity of instances. After this parameter is set, create a batch of additional pay-as-you-go instances according to the launch configuration before the rolling update starts. After the rolling update is completed, the additional instances will be terminated.This parameter is used to ensure a certain number of instances available during the rolling update. The maximum additional quantity of instances cannot exceed the number of refreshing instances in a single batch of the rolling update. The rollback process does not support this parameter currently.
        :rtype: int
        """
        return self._MaxSurge

    @MaxSurge.setter
    def MaxSurge(self, MaxSurge):
        self._MaxSurge = MaxSurge


    def _deserialize(self, params):
        self._BatchNumber = params.get("BatchNumber")
        self._BatchPause = params.get("BatchPause")
        self._MaxSurge = params.get("MaxSurge")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        """Whether to enable [TencentCloud Automation Tools](https://intl.cloud.tencent.com/document/product/1340?from_cn_redirect=1). Valid values:<br><li>`TRUE`: Enable<br><li>`FALSE`: Not enable.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: bool
        """
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
    """Information related to Tencent Cloud Observability Platform (TCOP, formerly Cloud Monitor).

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether to enable [Tencent Cloud Observability Platform (formerly Cloud Monitor)](https://intl.cloud.tencent.com/document/product/248?from_cn_redirect=1) (TCOP). Valid values:
<li>TRUE: enable TCOP.</li>
<li>FALSE: disable TCOP.</li>
Default value: TRUE.
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        """Whether to enable [Tencent Cloud Observability Platform (formerly Cloud Monitor)](https://intl.cloud.tencent.com/document/product/248?from_cn_redirect=1) (TCOP). Valid values:
<li>TRUE: enable TCOP.</li>
<li>FALSE: disable TCOP.</li>
Default value: TRUE.
        :rtype: bool
        """
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
        :param _Enabled: Whether to enable [Cloud Workload Protection Platform (CWPP)](https://intl.cloud.tencent.com/document/product/296?from_cn_redirect=1). Valid values:
<li>TRUE: enable CWPP.</li>
<li>FALSE: disable CWPP.</li>
Default value: TRUE.
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        """Whether to enable [Cloud Workload Protection Platform (CWPP)](https://intl.cloud.tencent.com/document/product/296?from_cn_redirect=1). Valid values:
<li>TRUE: enable CWPP.</li>
<li>FALSE: disable CWPP.</li>
Default value: TRUE.
        :rtype: bool
        """
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
        """Scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ScaleInNumber(self):
        """Number of instances to be reduced
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        """Scaling activity ID
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Scaling group ID
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ScaleOutNumber(self):
        """Number of instances to be added
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        """Scaling activity ID
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Auto scaling group ID.
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def AutoScalingPolicyId(self):
        """Alarm trigger policy ID.
        :rtype: str
        """
        return self._AutoScalingPolicyId

    @AutoScalingPolicyId.setter
    def AutoScalingPolicyId(self, AutoScalingPolicyId):
        self._AutoScalingPolicyId = AutoScalingPolicyId

    @property
    def ScalingPolicyType(self):
        """Scaling policy type. Valid values:
- `SIMPLE`: A simple policy.
- `TARGET_TRACKING`: A target tracking policy.
        :rtype: str
        """
        return self._ScalingPolicyType

    @ScalingPolicyType.setter
    def ScalingPolicyType(self, ScalingPolicyType):
        self._ScalingPolicyType = ScalingPolicyType

    @property
    def ScalingPolicyName(self):
        """Alarm trigger policy name.
        :rtype: str
        """
        return self._ScalingPolicyName

    @ScalingPolicyName.setter
    def ScalingPolicyName(self, ScalingPolicyName):
        self._ScalingPolicyName = ScalingPolicyName

    @property
    def AdjustmentType(self):
        """The method to adjust the desired capacity after the alarm is triggered. It’s only available when `ScalingPolicyType` is `Simple`. Valid values: <br><li>`CHANGE_IN_CAPACITY`: Increase or decrease the desired capacity </li><li>`EXACT_CAPACITY`: Adjust to the specified desired capacity </li> <li>`PERCENT_CHANGE_IN_CAPACITY`: Adjust the desired capacity by percentage </li>
        :rtype: str
        """
        return self._AdjustmentType

    @AdjustmentType.setter
    def AdjustmentType(self, AdjustmentType):
        self._AdjustmentType = AdjustmentType

    @property
    def AdjustmentValue(self):
        """The adjusted value of desired capacity after the alarm is triggered. This parameter is only applicable to a simple policy.
        :rtype: int
        """
        return self._AdjustmentValue

    @AdjustmentValue.setter
    def AdjustmentValue(self, AdjustmentValue):
        self._AdjustmentValue = AdjustmentValue

    @property
    def Cooldown(self):
        """Cooldown period. This parameter is only applicable to a simple policy.
        :rtype: int
        """
        return self._Cooldown

    @Cooldown.setter
    def Cooldown(self, Cooldown):
        self._Cooldown = Cooldown

    @property
    def MetricAlarm(self):
        """Alarm monitoring metrics of a simple policy.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.MetricAlarm`
        """
        return self._MetricAlarm

    @MetricAlarm.setter
    def MetricAlarm(self, MetricAlarm):
        self._MetricAlarm = MetricAlarm

    @property
    def PredefinedMetricType(self):
        """Preset monitoring item. It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Valid values: <br><li>ASG_AVG_CPU_UTILIZATION: Average CPU utilization</li><li>ASG_AVG_LAN_TRAFFIC_OUT: Average private bandwidth out</li><li>ASG_AVG_LAN_TRAFFIC_IN: Average private bandwidth in</li><li>ASG_AVG_WAN_TRAFFIC_OUT: Average public bandwidth out</li><li>ASG_AVG_WAN_TRAFFIC_IN: Average public bandwidth in</li>
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PredefinedMetricType

    @PredefinedMetricType.setter
    def PredefinedMetricType(self, PredefinedMetricType):
        self._PredefinedMetricType = PredefinedMetricType

    @property
    def TargetValue(self):
        """Target value. It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Value ranges: <br><li>`ASG_AVG_CPU_UTILIZATION` (in %): [1, 100)</li><li>`ASG_AVG_LAN_TRAFFIC_OUT` (in Mbps): >0</li><li>`ASG_AVG_LAN_TRAFFIC_IN` (in Mbps): >0</li><li>`ASG_AVG_WAN_TRAFFIC_OUT` (in Mbps): >0</li><li>`ASG_AVG_WAN_TRAFFIC_IN` (in Mbps): >0</li>
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TargetValue

    @TargetValue.setter
    def TargetValue(self, TargetValue):
        self._TargetValue = TargetValue

    @property
    def EstimatedInstanceWarmup(self):
        """Instance warm-up period (in seconds). It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Value range: 0-3600.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EstimatedInstanceWarmup

    @EstimatedInstanceWarmup.setter
    def EstimatedInstanceWarmup(self, EstimatedInstanceWarmup):
        self._EstimatedInstanceWarmup = EstimatedInstanceWarmup

    @property
    def DisableScaleIn(self):
        """Whether to disable scale-in. It’s only available when `ScalingPolicyType` is `TARGET_TRACKING`. Valid values: <br><li>`true`: Scaling in is not allowed.</li><li>`false`: Allows both scale-out and scale-in</li>
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._DisableScaleIn

    @DisableScaleIn.setter
    def DisableScaleIn(self, DisableScaleIn):
        self._DisableScaleIn = DisableScaleIn

    @property
    def MetricAlarms(self):
        """List of alarm monitoring metrics. This parameter is only applicable to a target tracking policy.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of MetricAlarm
        """
        return self._MetricAlarms

    @MetricAlarms.setter
    def MetricAlarms(self, MetricAlarms):
        self._MetricAlarms = MetricAlarms

    @property
    def NotificationUserGroupIds(self):
        """Notification group ID, which is the set of user group IDs.
        :rtype: list of str
        """
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
        :param _ScheduledType: Scheduled task execution type. Valid values:
<li>CRONTAB: repeated execution.</li>
<li>ONCE: single execution.</li>
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
        """Scheduled task ID.
        :rtype: str
        """
        return self._ScheduledActionId

    @ScheduledActionId.setter
    def ScheduledActionId(self, ScheduledActionId):
        self._ScheduledActionId = ScheduledActionId

    @property
    def ScheduledActionName(self):
        """Scheduled task name.
        :rtype: str
        """
        return self._ScheduledActionName

    @ScheduledActionName.setter
    def ScheduledActionName(self, ScheduledActionName):
        self._ScheduledActionName = ScheduledActionName

    @property
    def AutoScalingGroupId(self):
        """ID of the auto scaling group where the scheduled task is located.
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def StartTime(self):
        """Start time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Recurrence(self):
        """Repeating mode of the scheduled task.
        :rtype: str
        """
        return self._Recurrence

    @Recurrence.setter
    def Recurrence(self, Recurrence):
        self._Recurrence = Recurrence

    @property
    def EndTime(self):
        """End time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MaxSize(self):
        """Maximum number of instances set by the scheduled task.
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def DesiredCapacity(self):
        """Desired number of instances set by the scheduled task.
        :rtype: int
        """
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def MinSize(self):
        """Minimum number of instances set by the scheduled task.
        :rtype: int
        """
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def CreatedTime(self):
        """Creation time of the scheduled task. The value is in `UTC time` in the format of `YYYY-MM-DDThh:mm:ssZ` according to the `ISO8601` standard.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ScheduledType(self):
        """Scheduled task execution type. Valid values:
<li>CRONTAB: repeated execution.</li>
<li>ONCE: single execution.</li>
        :rtype: str
        """
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
        :param _ReplaceMode: Replace mode of unhealthy replacement service. Valid values:
RECREATE: Rebuild an instance to replace the original unhealthy instance.
RESET: Performing a system reinstallation on unhealthy instances to keep information such as data disks, private IP addresses, and instance IDs unchanged. The instance login settings, HostName, enhanced services, and UserData will remain consistent with the current launch configuration.
Default value: RECREATE.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReplaceMode: str
        :param _AutoUpdateInstanceTags: Automatic instance tag update. The default value is false. If this feature is enabled, tags of running instances in a scaling group will be updated as well if the scaling group tags are updated. (This feature takes effect for tag creation and editing but not tag deletion.) The update does not take effect immediately due to certain latency.
        :type AutoUpdateInstanceTags: bool
        """
        self._ReplaceMonitorUnhealthy = None
        self._ScalingMode = None
        self._ReplaceLoadBalancerUnhealthy = None
        self._ReplaceMode = None
        self._AutoUpdateInstanceTags = None

    @property
    def ReplaceMonitorUnhealthy(self):
        """Enables unhealthy instance replacement. If this feature is enabled, AS will replace instances that are flagged as unhealthy by Cloud Monitor. If this parameter is not specified, the value will be False by default.
        :rtype: bool
        """
        return self._ReplaceMonitorUnhealthy

    @ReplaceMonitorUnhealthy.setter
    def ReplaceMonitorUnhealthy(self, ReplaceMonitorUnhealthy):
        self._ReplaceMonitorUnhealthy = ReplaceMonitorUnhealthy

    @property
    def ScalingMode(self):
        """Valid values: 
CLASSIC_SCALING: this is the typical scaling method, which creates and terminates instances to perform scaling operations. 
WAKE_UP_STOPPED_SCALING: this scaling method first tries to start stopped instances. If the number of instances woken up is insufficient, the system creates new instances for scale-out. For scale-in, instances are terminated as in the typical method. You can use the StopAutoScalingInstances API to stop instances in the scaling group. Scale-out operations triggered by alarms will still create new instances.
Default value: CLASSIC_SCALING
        :rtype: str
        """
        return self._ScalingMode

    @ScalingMode.setter
    def ScalingMode(self, ScalingMode):
        self._ScalingMode = ScalingMode

    @property
    def ReplaceLoadBalancerUnhealthy(self):
        """Enable unhealthy instance replacement. If this feature is enabled, AS will replace instances that are found unhealthy in the CLB health check. If this parameter is not specified, the default value `False` will be used.
        :rtype: bool
        """
        return self._ReplaceLoadBalancerUnhealthy

    @ReplaceLoadBalancerUnhealthy.setter
    def ReplaceLoadBalancerUnhealthy(self, ReplaceLoadBalancerUnhealthy):
        self._ReplaceLoadBalancerUnhealthy = ReplaceLoadBalancerUnhealthy

    @property
    def ReplaceMode(self):
        """Replace mode of unhealthy replacement service. Valid values:
RECREATE: Rebuild an instance to replace the original unhealthy instance.
RESET: Performing a system reinstallation on unhealthy instances to keep information such as data disks, private IP addresses, and instance IDs unchanged. The instance login settings, HostName, enhanced services, and UserData will remain consistent with the current launch configuration.
Default value: RECREATE.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ReplaceMode

    @ReplaceMode.setter
    def ReplaceMode(self, ReplaceMode):
        self._ReplaceMode = ReplaceMode

    @property
    def AutoUpdateInstanceTags(self):
        """Automatic instance tag update. The default value is false. If this feature is enabled, tags of running instances in a scaling group will be updated as well if the scaling group tags are updated. (This feature takes effect for tag creation and editing but not tag deletion.) The update does not take effect immediately due to certain latency.
        :rtype: bool
        """
        return self._AutoUpdateInstanceTags

    @AutoUpdateInstanceTags.setter
    def AutoUpdateInstanceTags(self, AutoUpdateInstanceTags):
        self._AutoUpdateInstanceTags = AutoUpdateInstanceTags


    def _deserialize(self, params):
        self._ReplaceMonitorUnhealthy = params.get("ReplaceMonitorUnhealthy")
        self._ScalingMode = params.get("ScalingMode")
        self._ReplaceLoadBalancerUnhealthy = params.get("ReplaceLoadBalancerUnhealthy")
        self._ReplaceMode = params.get("ReplaceMode")
        self._AutoUpdateInstanceTags = params.get("AutoUpdateInstanceTags")
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
        """Auto scaling group ID.
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        """Instance ID.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ProtectedFromScaleIn(self):
        """Whether to enable scale-in protection for this instance
        :rtype: bool
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _SpotInstanceType: Spot instance type. The value can only be one-time currently. Default value: one-time.
        :type SpotInstanceType: str
        """
        self._MaxPrice = None
        self._SpotInstanceType = None

    @property
    def MaxPrice(self):
        """Bidding price such as "1.05"
        :rtype: str
        """
        return self._MaxPrice

    @MaxPrice.setter
    def MaxPrice(self, MaxPrice):
        self._MaxPrice = MaxPrice

    @property
    def SpotInstanceType(self):
        """Spot instance type. The value can only be one-time currently. Default value: one-time.
        :rtype: str
        """
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
        """The minimum number of the scaling group’s capacity that must be fulfilled by pay-as-you-go instances. It defaults to 0 if not specified. Its value cannot exceed the max capacity of the scaling group.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._BaseCapacity

    @BaseCapacity.setter
    def BaseCapacity(self, BaseCapacity):
        self._BaseCapacity = BaseCapacity

    @property
    def OnDemandPercentageAboveBaseCapacity(self):
        """Controls the percentage of pay-as-you-go instances for the additional capacity beyond `BaseCapacity`. Valid range: 0-100. The value 0 indicates that only spot instances are provisioned, while the value 100 indicates that only pay-as-you-go instances are provisioned. It defaults to 70 if not specified. The number of pay-as-you-go instances calculated on the percentage should be rounded up.
For example, if the desired capacity is 3, the `BaseCapacity` is set to 1, and the `OnDemandPercentageAboveBaseCapacity` is set to 1, the scaling group will have 2 pay-as-you-go instance (one comes from the base capacity, and the other comes from the rounded up value of the proportion), and 1 spot instance.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._OnDemandPercentageAboveBaseCapacity

    @OnDemandPercentageAboveBaseCapacity.setter
    def OnDemandPercentageAboveBaseCapacity(self, OnDemandPercentageAboveBaseCapacity):
        self._OnDemandPercentageAboveBaseCapacity = OnDemandPercentageAboveBaseCapacity

    @property
    def SpotAllocationStrategy(self):
        """Specifies how to assign spot instances in a mixed instance mode. Valid values: `COST_OPTIMIZED` and `CAPACITY_OPTIMIZED`; default value: `COST_OPTIMIZED`.
<br><li>`COST_OPTIMIZED`: the lowest cost policy. For each model in the launch configuration, AS tries to purchase it based on the lowest unit price per core in each availability zone. If the purchase failed, try the second-lowest unit price.
<br><li>`CAPACITY_OPTIMIZED`: the optimal capacity policy. For each model in the launch configuration, AS tries to purchase it based on the largest stock in each availability zone, minimizing the automatic repossession probability of spot instances.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._SpotAllocationStrategy

    @SpotAllocationStrategy.setter
    def SpotAllocationStrategy(self, SpotAllocationStrategy):
        self._SpotAllocationStrategy = SpotAllocationStrategy

    @property
    def CompensateWithBaseInstance(self):
        """Whether to replace with pay-as-you go instances. Valid values:
<br><li>`TRUE`: yes. After the purchase of spot instances failed due to insufficient stock and other reasons, purchase pay-as-you-go instances.
<br><li>`FALSE`: no. The scaling group only tries the configured model of spot instances when it needs to add spot instances.

Default value: `TRUE`.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: bool
        """
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
        """The scaling group ID.
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        """The list of the CVM instances you want to start up.
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        """The scaling activity ID.
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class StartInstanceRefreshRequest(AbstractModel):
    """StartInstanceRefresh request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Scaling group ID.
        :type AutoScalingGroupId: str
        :param _RefreshSettings: Refresh settings.
        :type RefreshSettings: :class:`tencentcloud.autoscaling.v20180419.models.RefreshSettings`
        :param _RefreshMode: Refresh mode. Valid values:
<li>ROLLING_UPDATE_RESET: Reinstall the system for rolling updates.</li>
<li>ROLLING_UPDATE_REPLACE: Create an instance and replace the old instance with it for rolling updates. This mode does not support the rollback API currently.</li>
        :type RefreshMode: str
        """
        self._AutoScalingGroupId = None
        self._RefreshSettings = None
        self._RefreshMode = None

    @property
    def AutoScalingGroupId(self):
        """Scaling group ID.
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RefreshSettings(self):
        """Refresh settings.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.RefreshSettings`
        """
        return self._RefreshSettings

    @RefreshSettings.setter
    def RefreshSettings(self, RefreshSettings):
        self._RefreshSettings = RefreshSettings

    @property
    def RefreshMode(self):
        """Refresh mode. Valid values:
<li>ROLLING_UPDATE_RESET: Reinstall the system for rolling updates.</li>
<li>ROLLING_UPDATE_REPLACE: Create an instance and replace the old instance with it for rolling updates. This mode does not support the rollback API currently.</li>
        :rtype: str
        """
        return self._RefreshMode

    @RefreshMode.setter
    def RefreshMode(self, RefreshMode):
        self._RefreshMode = RefreshMode


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        if params.get("RefreshSettings") is not None:
            self._RefreshSettings = RefreshSettings()
            self._RefreshSettings._deserialize(params.get("RefreshSettings"))
        self._RefreshMode = params.get("RefreshMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstanceRefreshResponse(AbstractModel):
    """StartInstanceRefresh response structure.

    """

    def __init__(self):
        r"""
        :param _RefreshActivityId: Refresh activity ID.
        :type RefreshActivityId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RefreshActivityId = None
        self._RequestId = None

    @property
    def RefreshActivityId(self):
        """Refresh activity ID.
        :rtype: str
        """
        return self._RefreshActivityId

    @RefreshActivityId.setter
    def RefreshActivityId(self, RefreshActivityId):
        self._RefreshActivityId = RefreshActivityId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RefreshActivityId = params.get("RefreshActivityId")
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
        """The scaling group ID.
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        """The list of the CVM instances you want to shut down.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def StoppedMode(self):
        """Whether the shutdown instances will be charged. Valid values:  
KEEP_CHARGING: keep charging after shutdown.  
STOP_CHARGING: stop charging after shutdown.
Default value: KEEP_CHARGING.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        """The scaling activity ID.
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class StopInstanceRefreshRequest(AbstractModel):
    """StopInstanceRefresh request structure.

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Scaling group ID.
        :type AutoScalingGroupId: str
        :param _RefreshActivityId: Refresh activity ID.
        :type RefreshActivityId: str
        """
        self._AutoScalingGroupId = None
        self._RefreshActivityId = None

    @property
    def AutoScalingGroupId(self):
        """Scaling group ID.
        :rtype: str
        """
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RefreshActivityId(self):
        """Refresh activity ID.
        :rtype: str
        """
        return self._RefreshActivityId

    @RefreshActivityId.setter
    def RefreshActivityId(self, RefreshActivityId):
        self._RefreshActivityId = RefreshActivityId


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._RefreshActivityId = params.get("RefreshActivityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstanceRefreshResponse(AbstractModel):
    """StopInstanceRefresh response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SystemDisk(AbstractModel):
    """System disk configuration of the launch configuration. If this parameter is not specified, the default value is assigned to it.

    """

    def __init__(self):
        r"""
        :param _DiskType: System disk type. For restrictions on the system disk type, see [cloud block storage types](https://intl.cloud.tencent.com/document/product/362/2353?from_cn_redirect=1). Valid values:
<li>LOCAL_BASIC: Local Disk.</li>
<li>LOCAL_SSD: Local SSD.</li>
<li>CLOUD_BASIC: Basic Cloud Disk.</li>
<li>CLOUD_PREMIUM: Premium Disk.</li>
<li>CLOUD_SSD: Cloud SSD.</li>
<li>Default value: CLOUD_PREMIUM.</li>
        :type DiskType: str
        :param _DiskSize: System disk size, in GB. Default value: 50.
        :type DiskSize: int
        """
        self._DiskType = None
        self._DiskSize = None

    @property
    def DiskType(self):
        """System disk type. For restrictions on the system disk type, see [cloud block storage types](https://intl.cloud.tencent.com/document/product/362/2353?from_cn_redirect=1). Valid values:
<li>LOCAL_BASIC: Local Disk.</li>
<li>LOCAL_SSD: Local SSD.</li>
<li>CLOUD_BASIC: Basic Cloud Disk.</li>
<li>CLOUD_PREMIUM: Premium Disk.</li>
<li>CLOUD_SSD: Cloud SSD.</li>
<li>Default value: CLOUD_PREMIUM.</li>
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """System disk size, in GB. Default value: 50.
        :rtype: int
        """
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
        :param _ResourceType: Resource type bound with tags. Valid values: auto-scaling-group and launch-configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceType: str
        """
        self._Key = None
        self._Value = None
        self._ResourceType = None

    @property
    def Key(self):
        """Tag key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Tag value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ResourceType(self):
        """Resource type bound with tags. Valid values: auto-scaling-group and launch-configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        """Port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        """Weight
        :rtype: int
        """
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
        :param _LoginSettings: This parameter is now invalid and should not be used. Upgrading the launch configuration API does not allow modification or overwriting of the LoginSettings parameter. LoginSettings will not change after upgrade.
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
        """Launch configuration ID.
        :rtype: str
        """
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def ImageId(self):
        """[Image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are three types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><br/>You can obtain the image IDs in the [CVM console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE).</li><li>You can also use the [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response.</li>
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def InstanceTypes(self):
        """List of instance models. Different instance models specify different resource specifications. Up to 5 instance models can be supported.
        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def LaunchConfigurationName(self):
        """Display name of the launch configuration, which can contain letters, digits, underscores and hyphens (-), and dots. Up to of 60 bytes allowed..
        :rtype: str
        """
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def DataDisks(self):
        """Information of the instance's data disk configuration. If this parameter is not specified, no data disk is purchased by default. Up to 11 data disks can be supported.
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def EnhancedService(self):
        """Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Security and Cloud Monitor. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled by default.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.EnhancedService`
        """
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def InstanceChargeType(self):
        """Instance billing type. CVM instances are POSTPAID_BY_HOUR by default.
<br><li>POSTPAID_BY_HOUR: Pay-as-you-go on an hourly basis
<br><li>SPOTPAID: Bidding
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceMarketOptions(self):
        """Market options of the instance, such as parameters related to spot instances. This parameter is required for spot instances.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        """
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def InstanceTypesCheckPolicy(self):
        """Instance type verification policy. Value range: ALL, ANY. Default value: ANY.
<br><li> ALL: The verification will success only if all instance types (InstanceType) are available; otherwise, an error will be reported.
<br><li> ANY: The verification will success if any instance type (InstanceType) is available; otherwise, an error will be reported.

Common reasons why an instance type is unavailable include stock-out of the instance type or the corresponding cloud disk.
If a model in InstanceTypes does not exist or has been discontinued, a verification error will be reported regardless of the value of InstanceTypesCheckPolicy.
        :rtype: str
        """
        return self._InstanceTypesCheckPolicy

    @InstanceTypesCheckPolicy.setter
    def InstanceTypesCheckPolicy(self, InstanceTypesCheckPolicy):
        self._InstanceTypesCheckPolicy = InstanceTypesCheckPolicy

    @property
    def InternetAccessible(self):
        """Configuration of public network bandwidth. If this parameter is not specified, 0 Mbps will be used by default.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def LoginSettings(self):
        """This parameter is now invalid and should not be used. Upgrading the launch configuration API does not allow modification or overwriting of the LoginSettings parameter. LoginSettings will not change after upgrade.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.LoginSettings`
        """
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def ProjectId(self):
        """Project ID of the instance. Leave it blank as the default.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SecurityGroupIds(self):
        """The security group to which the instance belongs. This parameter can be obtained by calling the `SecurityGroupId` field in the returned value of [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808?from_cn_redirect=1). If this parameter is not specified, no security group will be bound by default.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def SystemDisk(self):
        """System disk configuration of the instance. If this parameter is not specified, the default value will be used.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def UserData(self):
        """Base64-encoded custom data of up to 16 KB.
        :rtype: str
        """
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def InstanceTags(self):
        """List of tags. This parameter is used to bind up to 10 tags to newly added instances.
        :rtype: list of InstanceTag
        """
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def CamRoleName(self):
        """CAM role name, which can be obtained from the roleName field in the return value of the DescribeRoleList API.
        :rtype: str
        """
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HostNameSettings(self):
        """CVM hostname settings.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.HostNameSettings`
        """
        return self._HostNameSettings

    @HostNameSettings.setter
    def HostNameSettings(self, HostNameSettings):
        self._HostNameSettings = HostNameSettings

    @property
    def InstanceNameSettings(self):
        """Settings of CVM instance names
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameSettings`
        """
        return self._InstanceNameSettings

    @InstanceNameSettings.setter
    def InstanceNameSettings(self, InstanceNameSettings):
        self._InstanceNameSettings = InstanceNameSettings

    @property
    def InstanceChargePrepaid(self):
        """Details of the monthly subscription, including the purchase period, auto-renewal. It is required if the `InstanceChargeType` is `PREPAID`.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def DiskTypePolicy(self):
        """Selection policy of cloud disks. Default value: ORIGINAL. Valid values:
<br><li>ORIGINAL: uses the configured cloud disk type
<br><li>AUTOMATIC: automatically chooses an available cloud disk type
        :rtype: str
        """
        return self._DiskTypePolicy

    @DiskTypePolicy.setter
    def DiskTypePolicy(self, DiskTypePolicy):
        self._DiskTypePolicy = DiskTypePolicy

    @property
    def IPv6InternetAccessible(self):
        """IPv6 public network bandwidth configuration. If the IPv6 address is available in the new instance, public network bandwidth can be allocated to the IPv6 address. This parameter is invalid if `Ipv6AddressCount` of the scaling group associated with the launch configuration is 0.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.IPv6InternetAccessible`
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Lifecycle hook ID
        :rtype: str
        """
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def LifecycleHookName(self):
        """Lifecycle hook name
        :rtype: str
        """
        return self._LifecycleHookName

    @LifecycleHookName.setter
    def LifecycleHookName(self, LifecycleHookName):
        self._LifecycleHookName = LifecycleHookName

    @property
    def LifecycleTransition(self):
        """Scenario for the lifecycle hook. Value range: "INSTANCE_LAUNCHING", "INSTANCE_TERMINATING"
        :rtype: str
        """
        return self._LifecycleTransition

    @LifecycleTransition.setter
    def LifecycleTransition(self, LifecycleTransition):
        self._LifecycleTransition = LifecycleTransition

    @property
    def DefaultResult(self):
        """Defines the action to be taken by the auto scaling group upon lifecycle hook timeout. Value range: "CONTINUE", "ABANDON". Default value: "CONTINUE"
        :rtype: str
        """
        return self._DefaultResult

    @DefaultResult.setter
    def DefaultResult(self, DefaultResult):
        self._DefaultResult = DefaultResult

    @property
    def HeartbeatTimeout(self):
        """The maximum length of time (in seconds) that can elapse before the lifecycle hook times out. Value range: 30-7200. Default value: 300
        :rtype: int
        """
        return self._HeartbeatTimeout

    @HeartbeatTimeout.setter
    def HeartbeatTimeout(self, HeartbeatTimeout):
        self._HeartbeatTimeout = HeartbeatTimeout

    @property
    def NotificationMetadata(self):
        """Additional information of a notification that Auto Scaling sends to targets. This parameter is set when you configure a notification (default value: "").
        :rtype: str
        """
        return self._NotificationMetadata

    @NotificationMetadata.setter
    def NotificationMetadata(self, NotificationMetadata):
        self._NotificationMetadata = NotificationMetadata

    @property
    def NotificationTarget(self):
        """Notification result. `NotificationTarget` and `LifecycleCommand` cannot be specified at the same time.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.NotificationTarget`
        """
        return self._NotificationTarget

    @NotificationTarget.setter
    def NotificationTarget(self, NotificationTarget):
        self._NotificationTarget = NotificationTarget

    @property
    def LifecycleTransitionType(self):
        """The scenario where the lifecycle hook is applied. `EXTENSION`: the lifecycle hook will be triggered when AttachInstances, DetachInstances or RemoveInstaces is called. `NORMAL`: the lifecycle hook is not triggered by the above APIs. 
        :rtype: str
        """
        return self._LifecycleTransitionType

    @LifecycleTransitionType.setter
    def LifecycleTransitionType(self, LifecycleTransitionType):
        self._LifecycleTransitionType = LifecycleTransitionType

    @property
    def LifecycleCommand(self):
        """Remote command execution object. `NotificationTarget` and `LifecycleCommand` cannot be specified at the same time.
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.LifecycleCommand`
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")