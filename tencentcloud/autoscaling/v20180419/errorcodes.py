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


# The requesting account failed to pass the qualification review.
ACCOUNTQUALIFICATIONRESTRICTIONS = 'AccountQualificationRestrictions'

# CVM API call failed.
CALLCVMERROR = 'CallCvmError'

# No scaling activity is generated.
FAILEDOPERATION_NOACTIVITYTOGENERATE = 'FailedOperation.NoActivityToGenerate'

# An internal error occurred.
INTERNALERROR = 'InternalError'

# The CMQ API call failed.
INTERNALERROR_CALLCMQERROR = 'InternalError.CallCmqError'

# The internal API call failed.
INTERNALERROR_CALLERROR = 'InternalError.CallError'

# CLB API call failed.
INTERNALERROR_CALLLBERROR = 'InternalError.CallLbError'

# Monitor API call failed.
INTERNALERROR_CALLMONITORERROR = 'InternalError.CallMonitorError'

# The notification service API call failed.
INTERNALERROR_CALLNOTIFICATIONERROR = 'InternalError.CallNotificationError'

# The STS API call failed.
INTERNALERROR_CALLSTSERROR = 'InternalError.CallStsError'

# The tag API call failed.
INTERNALERROR_CALLTAGERROR = 'InternalError.CallTagError'

# The TVPC API call failed.
INTERNALERROR_CALLTVPCERROR = 'InternalError.CallTvpcError'

# VPC API call failed.
INTERNALERROR_CALLVPCERROR = 'InternalError.CallVpcError'

# Exceptions occurred while invoking other services.
INTERNALERROR_CALLEEERROR = 'InternalError.CalleeError'

# An internal request error occurred.
INTERNALERROR_REQUESTERROR = 'InternalError.RequestError'

# The image was not found.
INVALIDIMAGEID_NOTFOUND = 'InvalidImageId.NotFound'

# Invalid launch configuration.
INVALIDLAUNCHCONFIGURATION = 'InvalidLaunchConfiguration'

# The launch configuration ID is invalid.
INVALIDLAUNCHCONFIGURATIONID = 'InvalidLaunchConfigurationId'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Multiple parameters specified conflict and cannot co-exist.
INVALIDPARAMETER_CONFLICT = 'InvalidParameter.Conflict'

# The `hostname` parameter is unavailable to this image.
INVALIDPARAMETER_HOSTNAMEUNAVAILABLE = 'InvalidParameter.HostNameUnavailable'

# The parameter is invalid in a specific scenario.
INVALIDPARAMETER_INSCENARIO = 'InvalidParameter.InScenario'

# Invalid parameter combination.
INVALIDPARAMETER_INVALIDCOMBINATION = 'InvalidParameter.InvalidCombination'

# The specified CLB does not exist in the current scaling group.
INVALIDPARAMETER_LOADBALANCERNOTINAUTOSCALINGGROUP = 'InvalidParameter.LoadBalancerNotInAutoScalingGroup'

# A parameter is missing. One of the two parameters must be specified.
INVALIDPARAMETER_MUSTONEPARAMETER = 'InvalidParameter.MustOneParameter'

# Some parameters cannot coexist and should be deleted.
INVALIDPARAMETER_PARAMETERMUSTBEDELETED = 'InvalidParameter.ParameterMustBeDeleted'

# The two parameters specified conflict and cannot co-exist.
INVALIDPARAMETERCONFLICT = 'InvalidParameterConflict'

# Wrong parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The specified base capacity cannot exceed the max capacity.
INVALIDPARAMETERVALUE_BASECAPACITYTOOLARGE = 'InvalidParameterValue.BaseCapacityTooLarge'

# A classic CLB should be specified.
INVALIDPARAMETERVALUE_CLASSICLB = 'InvalidParameterValue.ClassicLb'

# Conflicting notification receiver type.
INVALIDPARAMETERVALUE_CONFLICTNOTIFICATIONTARGET = 'InvalidParameterValue.ConflictNotificationTarget'

# The cron expression specified for the scheduled task is invalid.
INVALIDPARAMETERVALUE_CRONEXPRESSIONILLEGAL = 'InvalidParameterValue.CronExpressionIllegal'

# Exception with CVM parameter validation.
INVALIDPARAMETERVALUE_CVMCONFIGURATIONERROR = 'InvalidParameterValue.CvmConfigurationError'

# Exception with CVM parameter validation.
INVALIDPARAMETERVALUE_CVMERROR = 'InvalidParameterValue.CvmError'

# Duplicate CLB instances
INVALIDPARAMETERVALUE_DUPLICATEDFORWARDLB = 'InvalidParameterValue.DuplicatedForwardLb'

# Duplicated subnet.
INVALIDPARAMETERVALUE_DUPLICATEDSUBNET = 'InvalidParameterValue.DuplicatedSubnet'

# The end time of the scheduled task is before the start time.
INVALIDPARAMETERVALUE_ENDTIMEBEFORESTARTTIME = 'InvalidParameterValue.EndTimeBeforeStartTime'

# Invalid filter.
INVALIDPARAMETERVALUE_FILTER = 'InvalidParameterValue.Filter'

# A CLB should be specified.
INVALIDPARAMETERVALUE_FORWARDLB = 'InvalidParameterValue.ForwardLb'

# The auto scaling group name already exists.
INVALIDPARAMETERVALUE_GROUPNAMEDUPLICATED = 'InvalidParameterValue.GroupNameDuplicated'

# Invalid hostname
INVALIDPARAMETERVALUE_HOSTNAMEILLEGAL = 'InvalidParameterValue.HostNameIllegal'

# The specified image does not exist.
INVALIDPARAMETERVALUE_IMAGENOTFOUND = 'InvalidParameterValue.ImageNotFound'

# Invalid instance name
INVALIDPARAMETERVALUE_INSTANCENAMEILLEGAL = 'InvalidParameterValue.InstanceNameIllegal'

# The instance type is not supported.
INVALIDPARAMETERVALUE_INSTANCETYPENOTSUPPORTED = 'InvalidParameterValue.InstanceTypeNotSupported'

# Invalid scaling activity ID.
INVALIDPARAMETERVALUE_INVALIDACTIVITYID = 'InvalidParameterValue.InvalidActivityId'

# Invalid scaling group ID.
INVALIDPARAMETERVALUE_INVALIDAUTOSCALINGGROUPID = 'InvalidParameterValue.InvalidAutoScalingGroupId'

# Invalid notification ID.
INVALIDPARAMETERVALUE_INVALIDAUTOSCALINGNOTIFICATIONID = 'InvalidParameterValue.InvalidAutoScalingNotificationId'

# Invalid alarm-triggered policy ID.
INVALIDPARAMETERVALUE_INVALIDAUTOSCALINGPOLICYID = 'InvalidParameterValue.InvalidAutoScalingPolicyId'

# The regions specified for CLB is invalid.
INVALIDPARAMETERVALUE_INVALIDCLBREGION = 'InvalidParameterValue.InvalidClbRegion'

# Invalid filter condition.
INVALIDPARAMETERVALUE_INVALIDFILTER = 'InvalidParameterValue.InvalidFilter'

# Invalid image ID.
INVALIDPARAMETERVALUE_INVALIDIMAGEID = 'InvalidParameterValue.InvalidImageId'

# Invalid instance ID.
INVALIDPARAMETERVALUE_INVALIDINSTANCEID = 'InvalidParameterValue.InvalidInstanceId'

# Invalid instance type.
INVALIDPARAMETERVALUE_INVALIDINSTANCETYPE = 'InvalidParameterValue.InvalidInstanceType'

# Invalid launch configuration
INVALIDPARAMETERVALUE_INVALIDLAUNCHCONFIGURATION = 'InvalidParameterValue.InvalidLaunchConfiguration'

# Invalid launch configuration ID.
INVALIDPARAMETERVALUE_INVALIDLAUNCHCONFIGURATIONID = 'InvalidParameterValue.InvalidLaunchConfigurationId'

# Invalid lifecycle hook ID.
INVALIDPARAMETERVALUE_INVALIDLIFECYCLEHOOKID = 'InvalidParameterValue.InvalidLifecycleHookId'

# The notification group ID should be a numeric string.
INVALIDPARAMETERVALUE_INVALIDNOTIFICATIONUSERGROUPID = 'InvalidParameterValue.InvalidNotificationUserGroupId'

# Invalid scheduled action ID.
INVALIDPARAMETERVALUE_INVALIDSCHEDULEDACTIONID = 'InvalidParameterValue.InvalidScheduledActionId'

# The scheduled task name contains invalid characters.
INVALIDPARAMETERVALUE_INVALIDSCHEDULEDACTIONNAMEINCLUDEILLEGALCHAR = 'InvalidParameterValue.InvalidScheduledActionNameIncludeIllegalChar'

# Invalid snapshot ID.
INVALIDPARAMETERVALUE_INVALIDSNAPSHOTID = 'InvalidParameterValue.InvalidSnapshotId'

# Invalid subnet ID.
INVALIDPARAMETERVALUE_INVALIDSUBNETID = 'InvalidParameterValue.InvalidSubnetId'

# The launch configuration name already exists.
INVALIDPARAMETERVALUE_LAUNCHCONFIGURATIONNAMEDUPLICATED = 'InvalidParameterValue.LaunchConfigurationNameDuplicated'

# The specified launch configuration was not found.
INVALIDPARAMETERVALUE_LAUNCHCONFIGURATIONNOTFOUND = 'InvalidParameterValue.LaunchConfigurationNotFound'

# The load balancer is in a different project.
INVALIDPARAMETERVALUE_LBPROJECTINCONSISTENT = 'InvalidParameterValue.LbProjectInconsistent'

# The lifecycle hook name already exists.
INVALIDPARAMETERVALUE_LIFECYCLEHOOKNAMEDUPLICATED = 'InvalidParameterValue.LifecycleHookNameDuplicated'

# The value exceeds the limit.
INVALIDPARAMETERVALUE_LIMITEXCEEDED = 'InvalidParameterValue.LimitExceeded'

# No resource permission.
INVALIDPARAMETERVALUE_NORESOURCEPERMISSION = 'InvalidParameterValue.NoResourcePermission'

# The value should be a floating point string.
INVALIDPARAMETERVALUE_NOTSTRINGTYPEFLOAT = 'InvalidParameterValue.NotStringTypeFloat'

# The account only supports VPCs.
INVALIDPARAMETERVALUE_ONLYVPC = 'InvalidParameterValue.OnlyVpc'

# The project ID does not exist.
INVALIDPARAMETERVALUE_PROJECTIDNOTFOUND = 'InvalidParameterValue.ProjectIdNotFound'

# The value is outside the specified range.
INVALIDPARAMETERVALUE_RANGE = 'InvalidParameterValue.Range'

# The alarm policy name already exists.
INVALIDPARAMETERVALUE_SCALINGPOLICYNAMEDUPLICATE = 'InvalidParameterValue.ScalingPolicyNameDuplicate'

# The scheduled task name already exists.
INVALIDPARAMETERVALUE_SCHEDULEDACTIONNAMEDUPLICATE = 'InvalidParameterValue.ScheduledActionNameDuplicate'

# The value of maximum, minimum, or desired number of instances in the auto scaling group is invalid.
INVALIDPARAMETERVALUE_SIZE = 'InvalidParameterValue.Size'

# The start time of the scheduled task is before the current time.
INVALIDPARAMETERVALUE_STARTTIMEBEFORECURRENTTIME = 'InvalidParameterValue.StartTimeBeforeCurrentTime'

# The subnet information is invalid.
INVALIDPARAMETERVALUE_SUBNETIDS = 'InvalidParameterValue.SubnetIds'

# The backend port of the CLB layer-4 listener already exists.
INVALIDPARAMETERVALUE_TARGETPORTDUPLICATED = 'InvalidParameterValue.TargetPortDuplicated'

# The specified threshold must be within the valid range.
INVALIDPARAMETERVALUE_THRESHOLDOUTOFRANGE = 'InvalidParameterValue.ThresholdOutOfRange'

# Wrong time format.
INVALIDPARAMETERVALUE_TIMEFORMAT = 'InvalidParameterValue.TimeFormat'

# Too many values.
INVALIDPARAMETERVALUE_TOOLONG = 'InvalidParameterValue.TooLong'

# The value of input parameter is too short.
INVALIDPARAMETERVALUE_TOOSHORT = 'InvalidParameterValue.TooShort'

# Incorrect UserData format.
INVALIDPARAMETERVALUE_USERDATAFORMATERROR = 'InvalidParameterValue.UserDataFormatError'

# The UserData is too long.
INVALIDPARAMETERVALUE_USERDATASIZEEXCEEDED = 'InvalidParameterValue.UserDataSizeExceeded'

# The user group does not exist.
INVALIDPARAMETERVALUE_USERGROUPIDNOTFOUND = 'InvalidParameterValue.UserGroupIdNotFound'

# The specified availability zone is not in the region.
INVALIDPARAMETERVALUE_ZONEMISMATCHREGION = 'InvalidParameterValue.ZoneMismatchRegion'

# The account does not support this operation.
INVALIDPERMISSION = 'InvalidPermission'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Binding with the specified CLBs will make the total number of bound CLBs exceeds the upper limit.
LIMITEXCEEDED_AFTERATTACHLBLIMITEXCEEDED = 'LimitExceeded.AfterAttachLbLimitExceeded'

# The number of auto scaling groups exceeds the limit.
LIMITEXCEEDED_AUTOSCALINGGROUPLIMITEXCEEDED = 'LimitExceeded.AutoScalingGroupLimitExceeded'

# The desired number of instances exceeds the limit.
LIMITEXCEEDED_DESIREDCAPACITYLIMITEXCEEDED = 'LimitExceeded.DesiredCapacityLimitExceeded'

# Too many values for the specified filter
LIMITEXCEEDED_FILTERVALUESTOOLONG = 'LimitExceeded.FilterValuesTooLong'

# You are short of the launch configuration quota.
LIMITEXCEEDED_LAUNCHCONFIGURATIONQUOTANOTENOUGH = 'LimitExceeded.LaunchConfigurationQuotaNotEnough'

# The maximum number of instances exceeds the limit.
LIMITEXCEEDED_MAXSIZELIMITEXCEEDED = 'LimitExceeded.MaxSizeLimitExceeded'

# The minimum number of instances is below the limit.
LIMITEXCEEDED_MINSIZELIMITEXCEEDED = 'LimitExceeded.MinSizeLimitExceeded'

# You are short of the quota.
LIMITEXCEEDED_QUOTANOTENOUGH = 'LimitExceeded.QuotaNotEnough'

# The number of scheduled tasks exceeds the limit.
LIMITEXCEEDED_SCHEDULEDACTIONLIMITEXCEEDED = 'LimitExceeded.ScheduledActionLimitExceeded'

# Parameter missing.
MISSINGPARAMETER = 'MissingParameter'

# A parameter is missing in a specific scenario.
MISSINGPARAMETER_INSCENARIO = 'MissingParameter.InScenario'

# The `InstanceMarketOptions` parameter of the spot instance is missing.
MISSINGPARAMETER_INSTANCEMARKETOPTIONS = 'MissingParameter.InstanceMarketOptions'

# The auto scaling group is performing a scaling activity.
RESOURCEINUSE_ACTIVITYINPROGRESS = 'ResourceInUse.ActivityInProgress'

# The scaling group is disabled.
RESOURCEINUSE_AUTOSCALINGGROUPNOTACTIVE = 'ResourceInUse.AutoScalingGroupNotActive'

# There are still normal instances in the auto scaling group.
RESOURCEINUSE_INSTANCEINGROUP = 'ResourceInUse.InstanceInGroup'

# The specified launch configuration is still used in the scaling group.
RESOURCEINUSE_LAUNCHCONFIGURATIONIDINUSE = 'ResourceInUse.LaunchConfigurationIdInUse'

# The maximum number of instances in the auto scaling group is exceeded.
RESOURCEINSUFFICIENT_AUTOSCALINGGROUPABOVEMAXSIZE = 'ResourceInsufficient.AutoScalingGroupAboveMaxSize'

# The number of instances in the auto scaling group is below the minimum value.
RESOURCEINSUFFICIENT_AUTOSCALINGGROUPBELOWMINSIZE = 'ResourceInsufficient.AutoScalingGroupBelowMinSize'

# The number of instances in a scaling group is more than the maximum capacity.
RESOURCEINSUFFICIENT_INSERVICEINSTANCEABOVEMAXSIZE = 'ResourceInsufficient.InServiceInstanceAboveMaxSize'

# The number of instances in a scaling group is less than the minimum capacity.
RESOURCEINSUFFICIENT_INSERVICEINSTANCEBELOWMINSIZE = 'ResourceInsufficient.InServiceInstanceBelowMinSize'

# The scaling group does not exist.
RESOURCENOTFOUND_AUTOSCALINGGROUPNOTFOUND = 'ResourceNotFound.AutoScalingGroupNotFound'

# The notification does not exist.
RESOURCENOTFOUND_AUTOSCALINGNOTIFICATIONNOTFOUND = 'ResourceNotFound.AutoScalingNotificationNotFound'

# The specified CMQ queue does not exist.
RESOURCENOTFOUND_CMQQUEUENOTFOUND = 'ResourceNotFound.CmqQueueNotFound'

# The specified instance does not exist.
RESOURCENOTFOUND_INSTANCESNOTFOUND = 'ResourceNotFound.InstancesNotFound'

# The target instance is not in the auto scaling group.
RESOURCENOTFOUND_INSTANCESNOTINAUTOSCALINGGROUP = 'ResourceNotFound.InstancesNotInAutoScalingGroup'

# The specified launch configuration does not exist.
RESOURCENOTFOUND_LAUNCHCONFIGURATIONIDNOTFOUND = 'ResourceNotFound.LaunchConfigurationIdNotFound'

# The instance corresponding to the lifecycle hook does not exist.
RESOURCENOTFOUND_LIFECYCLEHOOKINSTANCENOTFOUND = 'ResourceNotFound.LifecycleHookInstanceNotFound'

# The specified lifecycle hook was not found.
RESOURCENOTFOUND_LIFECYCLEHOOKNOTFOUND = 'ResourceNotFound.LifecycleHookNotFound'

# The specified listener does not exist.
RESOURCENOTFOUND_LISTENERNOTFOUND = 'ResourceNotFound.ListenerNotFound'

# The specified load balancer was not found.
RESOURCENOTFOUND_LOADBALANCERNOTFOUND = 'ResourceNotFound.LoadBalancerNotFound'

# The specified CLB does not exist in the current scaling group.
RESOURCENOTFOUND_LOADBALANCERNOTINAUTOSCALINGGROUP = 'ResourceNotFound.LoadBalancerNotInAutoScalingGroup'

# The specified location does not exist.
RESOURCENOTFOUND_LOCATIONNOTFOUND = 'ResourceNotFound.LocationNotFound'

# The alarm policy does not exist.
RESOURCENOTFOUND_SCALINGPOLICYNOTFOUND = 'ResourceNotFound.ScalingPolicyNotFound'

# The specified scheduled task does not exist.
RESOURCENOTFOUND_SCHEDULEDACTIONNOTFOUND = 'ResourceNotFound.ScheduledActionNotFound'

# The TDMQ-CMQ queue doesn't exist.
RESOURCENOTFOUND_TDMQCMQQUEUENOTFOUND = 'ResourceNotFound.TDMQCMQQueueNotFound'

# The TDMQ-CMQ topic doesn't exist.
RESOURCENOTFOUND_TDMQCMQTOPICNOTFOUND = 'ResourceNotFound.TDMQCMQTopicNotFound'

# The auto scaling group is exceptional.
RESOURCEUNAVAILABLE_AUTOSCALINGGROUPABNORMALSTATUS = 'ResourceUnavailable.AutoScalingGroupAbnormalStatus'

# The auto scaling group is disabled.
RESOURCEUNAVAILABLE_AUTOSCALINGGROUPDISABLED = 'ResourceUnavailable.AutoScalingGroupDisabled'

# The auto scaling group is active.
RESOURCEUNAVAILABLE_AUTOSCALINGGROUPINACTIVITY = 'ResourceUnavailable.AutoScalingGroupInActivity'

# There are no subscribers for the specified CMQ topic.
RESOURCEUNAVAILABLE_CMQTOPICHASNOSUBSCRIBER = 'ResourceUnavailable.CmqTopicHasNoSubscriber'

# The instance and the auto scaling group are in different VPCs.
RESOURCEUNAVAILABLE_CVMVPCINCONSISTENT = 'ResourceUnavailable.CvmVpcInconsistent'

# The specified instance is active.
RESOURCEUNAVAILABLE_INSTANCEINOPERATION = 'ResourceUnavailable.InstanceInOperation'

# The instance does not support **No Charges When Shut Down**.
RESOURCEUNAVAILABLE_INSTANCENOTSUPPORTSTOPCHARGING = 'ResourceUnavailable.InstanceNotSupportStopCharging'

# The instance already exists in the auto scaling group.
RESOURCEUNAVAILABLE_INSTANCESALREADYINAUTOSCALINGGROUP = 'ResourceUnavailable.InstancesAlreadyInAutoScalingGroup'

# The launch configuration is exceptional.
RESOURCEUNAVAILABLE_LAUNCHCONFIGURATIONSTATUSABNORMAL = 'ResourceUnavailable.LaunchConfigurationStatusAbnormal'

# The backend region of the CLB is not the same as the one for AS service.
RESOURCEUNAVAILABLE_LBBACKENDREGIONINCONSISTENT = 'ResourceUnavailable.LbBackendRegionInconsistent'

# The CLBs are not in the same project.
RESOURCEUNAVAILABLE_LBPROJECTINCONSISTENT = 'ResourceUnavailable.LbProjectInconsistent'

# The CLB and scaling group should reside in the same VPC.
RESOURCEUNAVAILABLE_LBVPCINCONSISTENT = 'ResourceUnavailable.LbVpcInconsistent'

# The lifecycle action has already been set.
RESOURCEUNAVAILABLE_LIFECYCLEACTIONRESULTHASSET = 'ResourceUnavailable.LifecycleActionResultHasSet'

# CLB is active in the scaling group.
RESOURCEUNAVAILABLE_LOADBALANCERINOPERATION = 'ResourceUnavailable.LoadBalancerInOperation'

# Project inconsistency.
RESOURCEUNAVAILABLE_PROJECTINCONSISTENT = 'ResourceUnavailable.ProjectInconsistent'

# Unable to add instances to the scaling group when they are shut down.
RESOURCEUNAVAILABLE_STOPPEDINSTANCENOTALLOWATTACH = 'ResourceUnavailable.StoppedInstanceNotAllowAttach'

# The TDMQ-CMQ topic is not subscribed.
RESOURCEUNAVAILABLE_TDMQCMQTOPICHASNOSUBSCRIBER = 'ResourceUnavailable.TDMQCMQTopicHasNoSubscriber'

# The specified availability zone is unavailable.
RESOURCEUNAVAILABLE_ZONEUNAVAILABLE = 'ResourceUnavailable.ZoneUnavailable'
