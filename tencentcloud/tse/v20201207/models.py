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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AccurateQpsThreshold(AbstractModel):
    r"""Cloud-native gateway traffic throttling plugin parameter throttling precise Qps threshold

    """

    def __init__(self):
        r"""
        :param _Unit: qps threshold control dimension, including: second, minute, hour, day, month, year.
        :type Unit: str
        :param _GlobalConfigId: Global configuration ID
        :type GlobalConfigId: str
        """
        self._Unit = None
        self._GlobalConfigId = None

    @property
    def Unit(self):
        r"""qps threshold control dimension, including: second, minute, hour, day, month, year.
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def GlobalConfigId(self):
        r"""Global configuration ID
        :rtype: str
        """
        return self._GlobalConfigId

    @GlobalConfigId.setter
    def GlobalConfigId(self, GlobalConfigId):
        self._GlobalConfigId = GlobalConfigId


    def _deserialize(self, params):
        self._Unit = params.get("Unit")
        self._GlobalConfigId = params.get("GlobalConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Argument(AbstractModel):
    r"""Routing rule request from source service configuration detail

    """

    def __init__(self):
        r"""
        :param _Type: Type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _Key: Key value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param _Value: Matching condition parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: :class:`tencentcloud.tse.v20201207.models.ArgumentValue`
        """
        self._Type = None
        self._Key = None
        self._Value = None

    @property
    def Type(self):
        r"""Type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Key(self):
        r"""Key value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Matching condition parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tse.v20201207.models.ArgumentValue`
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Key = params.get("Key")
        if params.get("Value") is not None:
            self._Value = ArgumentValue()
            self._Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArgumentValue(AbstractModel):
    r"""Called service configuration expression

    """

    def __init__(self):
        r"""
        :param _Type: expression type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _Value: Match Value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        :param _ValueType: value type
Note: This field may return null, indicating that no valid values can be obtained.
        :type ValueType: str
        """
        self._Type = None
        self._Value = None
        self._ValueType = None

    @property
    def Type(self):
        r"""expression type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        r"""Match Value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ValueType(self):
        r"""value type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        self._ValueType = params.get("ValueType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScalerBehavior(AbstractModel):
    r"""Metric scaling behavior

    """

    def __init__(self):
        r"""
        :param _ScaleUp: Scale-out behavior configuration
        :type ScaleUp: :class:`tencentcloud.tse.v20201207.models.AutoScalerRules`
        :param _ScaleDown: Behavior configuration for scale-in
        :type ScaleDown: :class:`tencentcloud.tse.v20201207.models.AutoScalerRules`
        """
        self._ScaleUp = None
        self._ScaleDown = None

    @property
    def ScaleUp(self):
        r"""Scale-out behavior configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.AutoScalerRules`
        """
        return self._ScaleUp

    @ScaleUp.setter
    def ScaleUp(self, ScaleUp):
        self._ScaleUp = ScaleUp

    @property
    def ScaleDown(self):
        r"""Behavior configuration for scale-in
        :rtype: :class:`tencentcloud.tse.v20201207.models.AutoScalerRules`
        """
        return self._ScaleDown

    @ScaleDown.setter
    def ScaleDown(self, ScaleDown):
        self._ScaleDown = ScaleDown


    def _deserialize(self, params):
        if params.get("ScaleUp") is not None:
            self._ScaleUp = AutoScalerRules()
            self._ScaleUp._deserialize(params.get("ScaleUp"))
        if params.get("ScaleDown") is not None:
            self._ScaleDown = AutoScalerRules()
            self._ScaleDown._deserialize(params.get("ScaleDown"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScalerPolicy(AbstractModel):
    r"""Scaling policy

    """

    def __init__(self):
        r"""
        :param _Type: Type, Pods
        :type Type: str
        :param _Value: Quantity.
        :type Value: int
        :param _PeriodSeconds: Expansion cycle
        :type PeriodSeconds: int
        """
        self._Type = None
        self._Value = None
        self._PeriodSeconds = None

    @property
    def Type(self):
        r"""Type, Pods
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        r"""Quantity.
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def PeriodSeconds(self):
        r"""Expansion cycle
        :rtype: int
        """
        return self._PeriodSeconds

    @PeriodSeconds.setter
    def PeriodSeconds(self, PeriodSeconds):
        self._PeriodSeconds = PeriodSeconds


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        self._PeriodSeconds = params.get("PeriodSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScalerRules(AbstractModel):
    r"""Metric scaling rule

    """

    def __init__(self):
        r"""
        :param _StabilizationWindowSeconds: Stability window time. Default is 0 during scaling and 300 during descaling.
        :type StabilizationWindowSeconds: int
        :param _SelectPolicy: Selection policy basis
        :type SelectPolicy: str
        :param _Policies: Scaling policy
        :type Policies: list of AutoScalerPolicy
        """
        self._StabilizationWindowSeconds = None
        self._SelectPolicy = None
        self._Policies = None

    @property
    def StabilizationWindowSeconds(self):
        r"""Stability window time. Default is 0 during scaling and 300 during descaling.
        :rtype: int
        """
        return self._StabilizationWindowSeconds

    @StabilizationWindowSeconds.setter
    def StabilizationWindowSeconds(self, StabilizationWindowSeconds):
        self._StabilizationWindowSeconds = StabilizationWindowSeconds

    @property
    def SelectPolicy(self):
        r"""Selection policy basis
        :rtype: str
        """
        return self._SelectPolicy

    @SelectPolicy.setter
    def SelectPolicy(self, SelectPolicy):
        self._SelectPolicy = SelectPolicy

    @property
    def Policies(self):
        r"""Scaling policy
        :rtype: list of AutoScalerPolicy
        """
        return self._Policies

    @Policies.setter
    def Policies(self, Policies):
        self._Policies = Policies


    def _deserialize(self, params):
        self._StabilizationWindowSeconds = params.get("StabilizationWindowSeconds")
        self._SelectPolicy = params.get("SelectPolicy")
        if params.get("Policies") is not None:
            self._Policies = []
            for item in params.get("Policies"):
                obj = AutoScalerPolicy()
                obj._deserialize(item)
                self._Policies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAutoScalerResourceStrategyToGroupsRequest(AbstractModel):
    r"""BindAutoScalerResourceStrategyToGroups request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway instance ID
        :type GatewayId: str
        :param _StrategyId: Policy ID
        :type StrategyId: str
        :param _GroupIds: gateway group ID list
        :type GroupIds: list of str
        """
        self._GatewayId = None
        self._StrategyId = None
        self._GroupIds = None

    @property
    def GatewayId(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def StrategyId(self):
        r"""Policy ID
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def GroupIds(self):
        r"""gateway group ID list
        :rtype: list of str
        """
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._StrategyId = params.get("StrategyId")
        self._GroupIds = params.get("GroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAutoScalerResourceStrategyToGroupsResponse(AbstractModel):
    r"""BindAutoScalerResourceStrategyToGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Success status
        :type Result: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Success status
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CanaryPriorityRule(AbstractModel):
    r"""Grayscale Rule Priority - Rule

    """

    def __init__(self):
        r"""
        :param _Priority: Priority
        :type Priority: int
        :param _CanaryRule: Grayscale rule configuration
        :type CanaryRule: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayCanaryRule`
        """
        self._Priority = None
        self._CanaryRule = None

    @property
    def Priority(self):
        r"""Priority
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def CanaryRule(self):
        r"""Grayscale rule configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayCanaryRule`
        """
        return self._CanaryRule

    @CanaryRule.setter
    def CanaryRule(self, CanaryRule):
        self._CanaryRule = CanaryRule


    def _deserialize(self, params):
        self._Priority = params.get("Priority")
        if params.get("CanaryRule") is not None:
            self._CanaryRule = CloudNativeAPIGatewayCanaryRule()
            self._CanaryRule._deserialize(params.get("CanaryRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateInfo(AbstractModel):
    r"""Certificate information

    """

    def __init__(self):
        r"""
        :param _Id: Unique ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        r"""Unique ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseWafProtectionRequest(AbstractModel):
    r"""CloseWafProtection request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: gateway ID
        :type GatewayId: str
        :param _Type: Type of protection resource.
-Global instance
-Service
-Route
-Object
        :type Type: str
        :param _List: When resource type Type is Service or Route, input the list of services or routes
        :type List: list of str
        """
        self._GatewayId = None
        self._Type = None
        self._List = None

    @property
    def GatewayId(self):
        r"""gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Type(self):
        r"""Type of protection resource.
-Global instance
-Service
-Route
-Object
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def List(self):
        r"""When resource type Type is Service or Route, input the list of services or routes
        :rtype: list of str
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Type = params.get("Type")
        self._List = params.get("List")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseWafProtectionResponse(AbstractModel):
    r"""CloseWafProtection response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CloudAPIGatewayCanaryRuleList(AbstractModel):
    r"""Grayscale rule list.

    """

    def __init__(self):
        r"""
        :param _CanaryRuleList: Grayscale rule
        :type CanaryRuleList: list of CloudNativeAPIGatewayCanaryRule
        :param _TotalCount: Total number.
        :type TotalCount: int
        """
        self._CanaryRuleList = None
        self._TotalCount = None

    @property
    def CanaryRuleList(self):
        r"""Grayscale rule
        :rtype: list of CloudNativeAPIGatewayCanaryRule
        """
        return self._CanaryRuleList

    @CanaryRuleList.setter
    def CanaryRuleList(self, CanaryRuleList):
        self._CanaryRuleList = CanaryRuleList

    @property
    def TotalCount(self):
        r"""Total number.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("CanaryRuleList") is not None:
            self._CanaryRuleList = []
            for item in params.get("CanaryRuleList"):
                obj = CloudNativeAPIGatewayCanaryRule()
                obj._deserialize(item)
                self._CanaryRuleList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayBalancedService(AbstractModel):
    r"""Service with percentage traffic configuration

    """

    def __init__(self):
        r"""
        :param _ServiceID: Service ID, required as an input parameter
        :type ServiceID: str
        :param _ServiceName: Service name, as an input parameter, meaningless
        :type ServiceName: str
        :param _UpstreamName: Upstream name, meaningless as an input parameter
        :type UpstreamName: str
        :param _Percent: Percentage, 10 means 10%, range 0-100
        :type Percent: float
        """
        self._ServiceID = None
        self._ServiceName = None
        self._UpstreamName = None
        self._Percent = None

    @property
    def ServiceID(self):
        r"""Service ID, required as an input parameter
        :rtype: str
        """
        return self._ServiceID

    @ServiceID.setter
    def ServiceID(self, ServiceID):
        self._ServiceID = ServiceID

    @property
    def ServiceName(self):
        r"""Service name, as an input parameter, meaningless
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def UpstreamName(self):
        r"""Upstream name, meaningless as an input parameter
        :rtype: str
        """
        return self._UpstreamName

    @UpstreamName.setter
    def UpstreamName(self, UpstreamName):
        self._UpstreamName = UpstreamName

    @property
    def Percent(self):
        r"""Percentage, 10 means 10%, range 0-100
        :rtype: float
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent


    def _deserialize(self, params):
        self._ServiceID = params.get("ServiceID")
        self._ServiceName = params.get("ServiceName")
        self._UpstreamName = params.get("UpstreamName")
        self._Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayCanaryRule(AbstractModel):
    r"""Grayscale rule

    """

    def __init__(self):
        r"""
        :param _Priority: Priority, with a range of 0 to 100. A larger value indicates a higher priority. Priorities must be unique across different rules.
        :type Priority: int
        :param _Enabled: Whether the rule is enabled.
        :type Enabled: bool
        :param _ConditionList: Match condition parameter
        :type ConditionList: list of CloudNativeAPIGatewayCanaryRuleCondition
        :param _BalancedServiceList: Traffic percentage configuration of the service
Note: This field may return null, indicating that no valid values can be obtained.
        :type BalancedServiceList: list of CloudNativeAPIGatewayBalancedService
        :param _ServiceId: service ID
        :type ServiceId: str
        :param _ServiceName: Service name
        :type ServiceName: str
        :param _RuleType: Grayscale rule type
Standard｜Lane
        :type RuleType: str
        :param _MatchType: Full-link grayscale policy match mode between multiple conditions: AND, OR
        :type MatchType: str
        :param _GroupId: Lane group ID
        :type GroupId: str
        :param _GroupName: Lane group name
        :type GroupName: str
        :param _LaneId: Lane ID
        :type LaneId: str
        :param _LaneName: swimlane name
        :type LaneName: str
        :param _MatchMode: Lane match rule: STRICT | PERMISSIVE
        :type MatchMode: str
        :param _LaneTag: Lane tag
        :type LaneTag: str
        """
        self._Priority = None
        self._Enabled = None
        self._ConditionList = None
        self._BalancedServiceList = None
        self._ServiceId = None
        self._ServiceName = None
        self._RuleType = None
        self._MatchType = None
        self._GroupId = None
        self._GroupName = None
        self._LaneId = None
        self._LaneName = None
        self._MatchMode = None
        self._LaneTag = None

    @property
    def Priority(self):
        r"""Priority, with a range of 0 to 100. A larger value indicates a higher priority. Priorities must be unique across different rules.
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Enabled(self):
        r"""Whether the rule is enabled.
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def ConditionList(self):
        r"""Match condition parameter
        :rtype: list of CloudNativeAPIGatewayCanaryRuleCondition
        """
        return self._ConditionList

    @ConditionList.setter
    def ConditionList(self, ConditionList):
        self._ConditionList = ConditionList

    @property
    def BalancedServiceList(self):
        r"""Traffic percentage configuration of the service
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CloudNativeAPIGatewayBalancedService
        """
        return self._BalancedServiceList

    @BalancedServiceList.setter
    def BalancedServiceList(self, BalancedServiceList):
        self._BalancedServiceList = BalancedServiceList

    @property
    def ServiceId(self):
        r"""service ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceName(self):
        r"""Service name
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def RuleType(self):
        r"""Grayscale rule type
Standard｜Lane
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def MatchType(self):
        r"""Full-link grayscale policy match mode between multiple conditions: AND, OR
        :rtype: str
        """
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType

    @property
    def GroupId(self):
        r"""Lane group ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""Lane group name
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def LaneId(self):
        r"""Lane ID
        :rtype: str
        """
        return self._LaneId

    @LaneId.setter
    def LaneId(self, LaneId):
        self._LaneId = LaneId

    @property
    def LaneName(self):
        r"""swimlane name
        :rtype: str
        """
        return self._LaneName

    @LaneName.setter
    def LaneName(self, LaneName):
        self._LaneName = LaneName

    @property
    def MatchMode(self):
        r"""Lane match rule: STRICT | PERMISSIVE
        :rtype: str
        """
        return self._MatchMode

    @MatchMode.setter
    def MatchMode(self, MatchMode):
        self._MatchMode = MatchMode

    @property
    def LaneTag(self):
        r"""Lane tag
        :rtype: str
        """
        return self._LaneTag

    @LaneTag.setter
    def LaneTag(self, LaneTag):
        self._LaneTag = LaneTag


    def _deserialize(self, params):
        self._Priority = params.get("Priority")
        self._Enabled = params.get("Enabled")
        if params.get("ConditionList") is not None:
            self._ConditionList = []
            for item in params.get("ConditionList"):
                obj = CloudNativeAPIGatewayCanaryRuleCondition()
                obj._deserialize(item)
                self._ConditionList.append(obj)
        if params.get("BalancedServiceList") is not None:
            self._BalancedServiceList = []
            for item in params.get("BalancedServiceList"):
                obj = CloudNativeAPIGatewayBalancedService()
                obj._deserialize(item)
                self._BalancedServiceList.append(obj)
        self._ServiceId = params.get("ServiceId")
        self._ServiceName = params.get("ServiceName")
        self._RuleType = params.get("RuleType")
        self._MatchType = params.get("MatchType")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._LaneId = params.get("LaneId")
        self._LaneName = params.get("LaneName")
        self._MatchMode = params.get("MatchMode")
        self._LaneTag = params.get("LaneTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayCanaryRuleCondition(AbstractModel):
    r"""Condition configuration in grayscale rule

    """

    def __init__(self):
        r"""
        :param _Type: Condition type, support path, method, query, header, cookie, body, and system.
        :type Type: str
        :param _Key: Parameter name.
        :type Key: str
        :param _Operator: Operator, supports "le", "eq", "lt", "ne", "ge", "gt", "regex", "exists", "in", "not in", "prefix", "exact", "regex"
        :type Operator: str
        :param _Value: Target parameter value
        :type Value: str
        :param _Delimiter: Separator. This parameter is valid only when Operator is in or not in. Supported values: comma, semicolon, space, line break.
        :type Delimiter: str
        :param _GlobalConfigId: Global configuration Id
        :type GlobalConfigId: str
        :param _GlobalConfigName: Global configuration name
        :type GlobalConfigName: str
        """
        self._Type = None
        self._Key = None
        self._Operator = None
        self._Value = None
        self._Delimiter = None
        self._GlobalConfigId = None
        self._GlobalConfigName = None

    @property
    def Type(self):
        r"""Condition type, support path, method, query, header, cookie, body, and system.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Key(self):
        r"""Parameter name.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        r"""Operator, supports "le", "eq", "lt", "ne", "ge", "gt", "regex", "exists", "in", "not in", "prefix", "exact", "regex"
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        r"""Target parameter value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Delimiter(self):
        r"""Separator. This parameter is valid only when Operator is in or not in. Supported values: comma, semicolon, space, line break.
        :rtype: str
        """
        return self._Delimiter

    @Delimiter.setter
    def Delimiter(self, Delimiter):
        self._Delimiter = Delimiter

    @property
    def GlobalConfigId(self):
        r"""Global configuration Id
        :rtype: str
        """
        return self._GlobalConfigId

    @GlobalConfigId.setter
    def GlobalConfigId(self, GlobalConfigId):
        self._GlobalConfigId = GlobalConfigId

    @property
    def GlobalConfigName(self):
        r"""Global configuration name
        :rtype: str
        """
        return self._GlobalConfigName

    @GlobalConfigName.setter
    def GlobalConfigName(self, GlobalConfigName):
        self._GlobalConfigName = GlobalConfigName


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Key = params.get("Key")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        self._Delimiter = params.get("Delimiter")
        self._GlobalConfigId = params.get("GlobalConfigId")
        self._GlobalConfigName = params.get("GlobalConfigName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayConfig(AbstractModel):
    r"""Cloud native API gateway configuration message.

    """

    def __init__(self):
        r"""
        :param _ConsoleType: Console type.
        :type ConsoleType: str
        :param _HttpUrl: HTTP URL.
        :type HttpUrl: str
        :param _HttpsUrl: HTTPS URL.
        :type HttpsUrl: str
        :param _NetType: Network type, Open|Internal.
        :type NetType: str
        :param _AdminUser: Admin username.
        :type AdminUser: str
        :param _AdminPassword: Administrator password.
        :type AdminPassword: str
        :param _Status: Network Status, Open|Closed|Updating
        :type Status: str
        :param _AccessControl: Network access policy
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessControl: :class:`tencentcloud.tse.v20201207.models.NetworkAccessControl`
        :param _SubnetId: Intranet subnet ID
        :type SubnetId: str
        :param _VpcId: Private network VPC ID
        :type VpcId: str
        :param _Description: Description of load balancing
        :type Description: str
        :param _SlaType: Load balancing specification type
        :type SlaType: str
        :param _SlaName: clb specification name
        :type SlaName: str
        :param _Vip: clb vip
        :type Vip: str
        :param _InternetMaxBandwidthOut: Bandwidth
        :type InternetMaxBandwidthOut: int
        :param _MultiZoneFlag: Whether the multiple-AZ deployment mode is used.
        :type MultiZoneFlag: bool
        :param _MasterZoneId: Primary AZ.
        :type MasterZoneId: str
        :param _SlaveZoneId: standby availability zone
        :type SlaveZoneId: str
        :param _MasterZoneName: Primary availability zone name
        :type MasterZoneName: str
        :param _SlaveZoneName: Backup availability zone name
        :type SlaveZoneName: str
        :param _NetworkId: Network id
        :type NetworkId: str
        :param _IPV6FullChain: Whether the CLB is a new ipv6 CLB
        :type IPV6FullChain: bool
        :param _CustomizedConfigContent: Load balancing personalized configuration content
        :type CustomizedConfigContent: str
        """
        self._ConsoleType = None
        self._HttpUrl = None
        self._HttpsUrl = None
        self._NetType = None
        self._AdminUser = None
        self._AdminPassword = None
        self._Status = None
        self._AccessControl = None
        self._SubnetId = None
        self._VpcId = None
        self._Description = None
        self._SlaType = None
        self._SlaName = None
        self._Vip = None
        self._InternetMaxBandwidthOut = None
        self._MultiZoneFlag = None
        self._MasterZoneId = None
        self._SlaveZoneId = None
        self._MasterZoneName = None
        self._SlaveZoneName = None
        self._NetworkId = None
        self._IPV6FullChain = None
        self._CustomizedConfigContent = None

    @property
    def ConsoleType(self):
        r"""Console type.
        :rtype: str
        """
        return self._ConsoleType

    @ConsoleType.setter
    def ConsoleType(self, ConsoleType):
        self._ConsoleType = ConsoleType

    @property
    def HttpUrl(self):
        r"""HTTP URL.
        :rtype: str
        """
        return self._HttpUrl

    @HttpUrl.setter
    def HttpUrl(self, HttpUrl):
        self._HttpUrl = HttpUrl

    @property
    def HttpsUrl(self):
        r"""HTTPS URL.
        :rtype: str
        """
        return self._HttpsUrl

    @HttpsUrl.setter
    def HttpsUrl(self, HttpsUrl):
        self._HttpsUrl = HttpsUrl

    @property
    def NetType(self):
        r"""Network type, Open|Internal.
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def AdminUser(self):
        r"""Admin username.
        :rtype: str
        """
        return self._AdminUser

    @AdminUser.setter
    def AdminUser(self, AdminUser):
        self._AdminUser = AdminUser

    @property
    def AdminPassword(self):
        r"""Administrator password.
        :rtype: str
        """
        return self._AdminPassword

    @AdminPassword.setter
    def AdminPassword(self, AdminPassword):
        self._AdminPassword = AdminPassword

    @property
    def Status(self):
        r"""Network Status, Open|Closed|Updating
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AccessControl(self):
        r"""Network access policy
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tse.v20201207.models.NetworkAccessControl`
        """
        return self._AccessControl

    @AccessControl.setter
    def AccessControl(self, AccessControl):
        self._AccessControl = AccessControl

    @property
    def SubnetId(self):
        r"""Intranet subnet ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        r"""Private network VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Description(self):
        r"""Description of load balancing
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SlaType(self):
        r"""Load balancing specification type
        :rtype: str
        """
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType

    @property
    def SlaName(self):
        r"""clb specification name
        :rtype: str
        """
        return self._SlaName

    @SlaName.setter
    def SlaName(self, SlaName):
        self._SlaName = SlaName

    @property
    def Vip(self):
        r"""clb vip
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def InternetMaxBandwidthOut(self):
        r"""Bandwidth
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def MultiZoneFlag(self):
        r"""Whether the multiple-AZ deployment mode is used.
        :rtype: bool
        """
        return self._MultiZoneFlag

    @MultiZoneFlag.setter
    def MultiZoneFlag(self, MultiZoneFlag):
        self._MultiZoneFlag = MultiZoneFlag

    @property
    def MasterZoneId(self):
        r"""Primary AZ.
        :rtype: str
        """
        return self._MasterZoneId

    @MasterZoneId.setter
    def MasterZoneId(self, MasterZoneId):
        self._MasterZoneId = MasterZoneId

    @property
    def SlaveZoneId(self):
        r"""standby availability zone
        :rtype: str
        """
        return self._SlaveZoneId

    @SlaveZoneId.setter
    def SlaveZoneId(self, SlaveZoneId):
        self._SlaveZoneId = SlaveZoneId

    @property
    def MasterZoneName(self):
        r"""Primary availability zone name
        :rtype: str
        """
        return self._MasterZoneName

    @MasterZoneName.setter
    def MasterZoneName(self, MasterZoneName):
        self._MasterZoneName = MasterZoneName

    @property
    def SlaveZoneName(self):
        r"""Backup availability zone name
        :rtype: str
        """
        return self._SlaveZoneName

    @SlaveZoneName.setter
    def SlaveZoneName(self, SlaveZoneName):
        self._SlaveZoneName = SlaveZoneName

    @property
    def NetworkId(self):
        r"""Network id
        :rtype: str
        """
        return self._NetworkId

    @NetworkId.setter
    def NetworkId(self, NetworkId):
        self._NetworkId = NetworkId

    @property
    def IPV6FullChain(self):
        r"""Whether the CLB is a new ipv6 CLB
        :rtype: bool
        """
        return self._IPV6FullChain

    @IPV6FullChain.setter
    def IPV6FullChain(self, IPV6FullChain):
        self._IPV6FullChain = IPV6FullChain

    @property
    def CustomizedConfigContent(self):
        r"""Load balancing personalized configuration content
        :rtype: str
        """
        return self._CustomizedConfigContent

    @CustomizedConfigContent.setter
    def CustomizedConfigContent(self, CustomizedConfigContent):
        self._CustomizedConfigContent = CustomizedConfigContent


    def _deserialize(self, params):
        self._ConsoleType = params.get("ConsoleType")
        self._HttpUrl = params.get("HttpUrl")
        self._HttpsUrl = params.get("HttpsUrl")
        self._NetType = params.get("NetType")
        self._AdminUser = params.get("AdminUser")
        self._AdminPassword = params.get("AdminPassword")
        self._Status = params.get("Status")
        if params.get("AccessControl") is not None:
            self._AccessControl = NetworkAccessControl()
            self._AccessControl._deserialize(params.get("AccessControl"))
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Description = params.get("Description")
        self._SlaType = params.get("SlaType")
        self._SlaName = params.get("SlaName")
        self._Vip = params.get("Vip")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._MultiZoneFlag = params.get("MultiZoneFlag")
        self._MasterZoneId = params.get("MasterZoneId")
        self._SlaveZoneId = params.get("SlaveZoneId")
        self._MasterZoneName = params.get("MasterZoneName")
        self._SlaveZoneName = params.get("SlaveZoneName")
        self._NetworkId = params.get("NetworkId")
        self._IPV6FullChain = params.get("IPV6FullChain")
        self._CustomizedConfigContent = params.get("CustomizedConfigContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayNode(AbstractModel):
    r"""Cloud Native API Gateway Node Information.

    """

    def __init__(self):
        r"""
        :param _NodeId: Cloud-native gateway node id
        :type NodeId: str
        :param _NodeIp: Node ip
        :type NodeIp: str
        :param _ZoneId: Zone id
        :type ZoneId: str
        :param _Zone: Zone
        :type Zone: str
        :param _GroupId: group ID
        :type GroupId: str
        :param _GroupName: Group name
        :type GroupName: str
        :param _Status: Status.
        :type Status: str
        :param _Weight: Node weight
        :type Weight: int
        :param _IsDefaultWeight: Default weight required or not
        :type IsDefaultWeight: bool
        """
        self._NodeId = None
        self._NodeIp = None
        self._ZoneId = None
        self._Zone = None
        self._GroupId = None
        self._GroupName = None
        self._Status = None
        self._Weight = None
        self._IsDefaultWeight = None

    @property
    def NodeId(self):
        r"""Cloud-native gateway node id
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeIp(self):
        r"""Node ip
        :rtype: str
        """
        return self._NodeIp

    @NodeIp.setter
    def NodeIp(self, NodeIp):
        self._NodeIp = NodeIp

    @property
    def ZoneId(self):
        r"""Zone id
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Zone(self):
        r"""Zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def GroupId(self):
        r"""group ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""Group name
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Status(self):
        r"""Status.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Weight(self):
        r"""Node weight
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def IsDefaultWeight(self):
        r"""Default weight required or not
        :rtype: bool
        """
        return self._IsDefaultWeight

    @IsDefaultWeight.setter
    def IsDefaultWeight(self, IsDefaultWeight):
        self._IsDefaultWeight = IsDefaultWeight


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeIp = params.get("NodeIp")
        self._ZoneId = params.get("ZoneId")
        self._Zone = params.get("Zone")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Status = params.get("Status")
        self._Weight = params.get("Weight")
        self._IsDefaultWeight = params.get("IsDefaultWeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayNodeConfig(AbstractModel):
    r"""Cloud Native API gateway node configuration.

    """

    def __init__(self):
        r"""
        :param _Specification: Node configuration, 1c2g|2c4g|4c8g|8c16g.
        :type Specification: str
        :param _Number: Node count, 2-9.
        :type Number: int
        """
        self._Specification = None
        self._Number = None

    @property
    def Specification(self):
        r"""Node configuration, 1c2g|2c4g|4c8g|8c16g.
        :rtype: str
        """
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def Number(self):
        r"""Node count, 2-9.
        :rtype: int
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number


    def _deserialize(self, params):
        self._Specification = params.get("Specification")
        self._Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayRateLimitDetail(AbstractModel):
    r"""Cloud-native gateway Tse traffic throttling plugin configuration

    """

    def __init__(self):
        r"""
        :param _Enabled: Plug-in enable status
        :type Enabled: bool
        :param _QpsThresholds: qps threshold
        :type QpsThresholds: list of QpsThreshold
        :param _Path: Request path that requires traffic control
        :type Path: str
        :param _Header: Request header Key for traffic control
        :type Header: str
        :param _LimitBy: Traffic throttling basis
ip service consumer credential path header
        :type LimitBy: str
        :param _ExternalRedis: external redis configuration
        :type ExternalRedis: :class:`tencentcloud.tse.v20201207.models.ExternalRedis`
        :param _GlobalConfigId: redis configuration in global configuration
        :type GlobalConfigId: str
        :param _Policy: Counter policy 
local standalone
default redis
external redis

        :type Policy: str
        :param _RateLimitResponse: Response configuration, response policy is text

        :type RateLimitResponse: :class:`tencentcloud.tse.v20201207.models.RateLimitResponse`
        :param _RateLimitResponseUrl: Request forwarding address
        :type RateLimitResponseUrl: str
        :param _ResponseType: response policy
url request forwarding
Response configuration
default mode: return directly.

        :type ResponseType: str
        :param _HideClientHeaders: Whether to hide the traffic throttling client response header
        :type HideClientHeaders: bool
        :param _LineUpTime: queuing time
        :type LineUpTime: int
        :param _IsDelay: Whether request queuing is enabled
        :type IsDelay: bool
        :param _BasicLimitQpsThresholds: Basic throttling
Note: This field may return null, indicating that no valid values can be obtained.
        :type BasicLimitQpsThresholds: list of QpsThreshold
        :param _LimitRules: Parameter throttling policy
Note: This field may return null, indicating that no valid values can be obtained.
        :type LimitRules: list of LimitRule
        """
        self._Enabled = None
        self._QpsThresholds = None
        self._Path = None
        self._Header = None
        self._LimitBy = None
        self._ExternalRedis = None
        self._GlobalConfigId = None
        self._Policy = None
        self._RateLimitResponse = None
        self._RateLimitResponseUrl = None
        self._ResponseType = None
        self._HideClientHeaders = None
        self._LineUpTime = None
        self._IsDelay = None
        self._BasicLimitQpsThresholds = None
        self._LimitRules = None

    @property
    def Enabled(self):
        r"""Plug-in enable status
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def QpsThresholds(self):
        r"""qps threshold
        :rtype: list of QpsThreshold
        """
        return self._QpsThresholds

    @QpsThresholds.setter
    def QpsThresholds(self, QpsThresholds):
        self._QpsThresholds = QpsThresholds

    @property
    def Path(self):
        r"""Request path that requires traffic control
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Header(self):
        r"""Request header Key for traffic control
        :rtype: str
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def LimitBy(self):
        r"""Traffic throttling basis
ip service consumer credential path header
        :rtype: str
        """
        return self._LimitBy

    @LimitBy.setter
    def LimitBy(self, LimitBy):
        self._LimitBy = LimitBy

    @property
    def ExternalRedis(self):
        r"""external redis configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.ExternalRedis`
        """
        return self._ExternalRedis

    @ExternalRedis.setter
    def ExternalRedis(self, ExternalRedis):
        self._ExternalRedis = ExternalRedis

    @property
    def GlobalConfigId(self):
        r"""redis configuration in global configuration
        :rtype: str
        """
        return self._GlobalConfigId

    @GlobalConfigId.setter
    def GlobalConfigId(self, GlobalConfigId):
        self._GlobalConfigId = GlobalConfigId

    @property
    def Policy(self):
        r"""Counter policy 
local standalone
default redis
external redis

        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def RateLimitResponse(self):
        r"""Response configuration, response policy is text

        :rtype: :class:`tencentcloud.tse.v20201207.models.RateLimitResponse`
        """
        return self._RateLimitResponse

    @RateLimitResponse.setter
    def RateLimitResponse(self, RateLimitResponse):
        self._RateLimitResponse = RateLimitResponse

    @property
    def RateLimitResponseUrl(self):
        r"""Request forwarding address
        :rtype: str
        """
        return self._RateLimitResponseUrl

    @RateLimitResponseUrl.setter
    def RateLimitResponseUrl(self, RateLimitResponseUrl):
        self._RateLimitResponseUrl = RateLimitResponseUrl

    @property
    def ResponseType(self):
        r"""response policy
url request forwarding
Response configuration
default mode: return directly.

        :rtype: str
        """
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def HideClientHeaders(self):
        r"""Whether to hide the traffic throttling client response header
        :rtype: bool
        """
        return self._HideClientHeaders

    @HideClientHeaders.setter
    def HideClientHeaders(self, HideClientHeaders):
        self._HideClientHeaders = HideClientHeaders

    @property
    def LineUpTime(self):
        r"""queuing time
        :rtype: int
        """
        return self._LineUpTime

    @LineUpTime.setter
    def LineUpTime(self, LineUpTime):
        self._LineUpTime = LineUpTime

    @property
    def IsDelay(self):
        r"""Whether request queuing is enabled
        :rtype: bool
        """
        return self._IsDelay

    @IsDelay.setter
    def IsDelay(self, IsDelay):
        self._IsDelay = IsDelay

    @property
    def BasicLimitQpsThresholds(self):
        r"""Basic throttling
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of QpsThreshold
        """
        return self._BasicLimitQpsThresholds

    @BasicLimitQpsThresholds.setter
    def BasicLimitQpsThresholds(self, BasicLimitQpsThresholds):
        self._BasicLimitQpsThresholds = BasicLimitQpsThresholds

    @property
    def LimitRules(self):
        r"""Parameter throttling policy
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of LimitRule
        """
        return self._LimitRules

    @LimitRules.setter
    def LimitRules(self, LimitRules):
        self._LimitRules = LimitRules


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        if params.get("QpsThresholds") is not None:
            self._QpsThresholds = []
            for item in params.get("QpsThresholds"):
                obj = QpsThreshold()
                obj._deserialize(item)
                self._QpsThresholds.append(obj)
        self._Path = params.get("Path")
        self._Header = params.get("Header")
        self._LimitBy = params.get("LimitBy")
        if params.get("ExternalRedis") is not None:
            self._ExternalRedis = ExternalRedis()
            self._ExternalRedis._deserialize(params.get("ExternalRedis"))
        self._GlobalConfigId = params.get("GlobalConfigId")
        self._Policy = params.get("Policy")
        if params.get("RateLimitResponse") is not None:
            self._RateLimitResponse = RateLimitResponse()
            self._RateLimitResponse._deserialize(params.get("RateLimitResponse"))
        self._RateLimitResponseUrl = params.get("RateLimitResponseUrl")
        self._ResponseType = params.get("ResponseType")
        self._HideClientHeaders = params.get("HideClientHeaders")
        self._LineUpTime = params.get("LineUpTime")
        self._IsDelay = params.get("IsDelay")
        if params.get("BasicLimitQpsThresholds") is not None:
            self._BasicLimitQpsThresholds = []
            for item in params.get("BasicLimitQpsThresholds"):
                obj = QpsThreshold()
                obj._deserialize(item)
                self._BasicLimitQpsThresholds.append(obj)
        if params.get("LimitRules") is not None:
            self._LimitRules = []
            for item in params.get("LimitRules"):
                obj = LimitRule()
                obj._deserialize(item)
                self._LimitRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayStrategy(AbstractModel):
    r"""Gateway instance policy

    """

    def __init__(self):
        r"""
        :param _StrategyId: Policy ID
        :type StrategyId: str
        :param _StrategyName: Policy name.
        :type StrategyName: str
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _ModifyTime: Update time
        :type ModifyTime: str
        :param _Description: Policy description
        :type Description: str
        :param _Config: Auto scaling configuration
        :type Config: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyAutoScalerConfig`
        :param _GatewayId: Gateway instance ID
        :type GatewayId: str
        :param _CronConfig: Scheduled scaling configuration
        :type CronConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyCronScalerConfig`
        :param _MaxReplicas: Maximum number of nodes
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxReplicas: int
        """
        self._StrategyId = None
        self._StrategyName = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Description = None
        self._Config = None
        self._GatewayId = None
        self._CronConfig = None
        self._MaxReplicas = None

    @property
    def StrategyId(self):
        r"""Policy ID
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def StrategyName(self):
        r"""Policy name.
        :rtype: str
        """
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def CreateTime(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        r"""Update time
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Description(self):
        r"""Policy description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Config(self):
        r"""Auto scaling configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyAutoScalerConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def GatewayId(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def CronConfig(self):
        r"""Scheduled scaling configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyCronScalerConfig`
        """
        return self._CronConfig

    @CronConfig.setter
    def CronConfig(self, CronConfig):
        self._CronConfig = CronConfig

    @property
    def MaxReplicas(self):
        warnings.warn("parameter `MaxReplicas` is deprecated", DeprecationWarning) 

        r"""Maximum number of nodes
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        warnings.warn("parameter `MaxReplicas` is deprecated", DeprecationWarning) 

        self._MaxReplicas = MaxReplicas


    def _deserialize(self, params):
        self._StrategyId = params.get("StrategyId")
        self._StrategyName = params.get("StrategyName")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Description = params.get("Description")
        if params.get("Config") is not None:
            self._Config = CloudNativeAPIGatewayStrategyAutoScalerConfig()
            self._Config._deserialize(params.get("Config"))
        self._GatewayId = params.get("GatewayId")
        if params.get("CronConfig") is not None:
            self._CronConfig = CloudNativeAPIGatewayStrategyCronScalerConfig()
            self._CronConfig._deserialize(params.get("CronConfig"))
        self._MaxReplicas = params.get("MaxReplicas")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayStrategyAutoScalerConfig(AbstractModel):
    r"""Auto scaling policy

    """

    def __init__(self):
        r"""
        :param _MaxReplicas: Maximum number of replicas
        :type MaxReplicas: int
        :param _Metrics: Metric list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Metrics: list of CloudNativeAPIGatewayStrategyAutoScalerConfigMetric
        :param _Enabled: Whether metric scaling is enabled
Note: This field may return null, indicating that no valid values can be obtained.
        :type Enabled: bool
        :param _CreateTime: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _ModifyTime: Modification time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ModifyTime: str
        :param _StrategyId: Policy ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type StrategyId: str
        :param _AutoScalerId: Metric configuration ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoScalerId: str
        :param _Behavior: Metric scaling behavior configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Behavior: :class:`tencentcloud.tse.v20201207.models.AutoScalerBehavior`
        """
        self._MaxReplicas = None
        self._Metrics = None
        self._Enabled = None
        self._CreateTime = None
        self._ModifyTime = None
        self._StrategyId = None
        self._AutoScalerId = None
        self._Behavior = None

    @property
    def MaxReplicas(self):
        r"""Maximum number of replicas
        :rtype: int
        """
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        self._MaxReplicas = MaxReplicas

    @property
    def Metrics(self):
        r"""Metric list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CloudNativeAPIGatewayStrategyAutoScalerConfigMetric
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def Enabled(self):
        warnings.warn("parameter `Enabled` is deprecated", DeprecationWarning) 

        r"""Whether metric scaling is enabled
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        warnings.warn("parameter `Enabled` is deprecated", DeprecationWarning) 

        self._Enabled = Enabled

    @property
    def CreateTime(self):
        warnings.warn("parameter `CreateTime` is deprecated", DeprecationWarning) 

        r"""Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        warnings.warn("parameter `CreateTime` is deprecated", DeprecationWarning) 

        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        warnings.warn("parameter `ModifyTime` is deprecated", DeprecationWarning) 

        r"""Modification time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        warnings.warn("parameter `ModifyTime` is deprecated", DeprecationWarning) 

        self._ModifyTime = ModifyTime

    @property
    def StrategyId(self):
        warnings.warn("parameter `StrategyId` is deprecated", DeprecationWarning) 

        r"""Policy ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        warnings.warn("parameter `StrategyId` is deprecated", DeprecationWarning) 

        self._StrategyId = StrategyId

    @property
    def AutoScalerId(self):
        warnings.warn("parameter `AutoScalerId` is deprecated", DeprecationWarning) 

        r"""Metric configuration ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AutoScalerId

    @AutoScalerId.setter
    def AutoScalerId(self, AutoScalerId):
        warnings.warn("parameter `AutoScalerId` is deprecated", DeprecationWarning) 

        self._AutoScalerId = AutoScalerId

    @property
    def Behavior(self):
        r"""Metric scaling behavior configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tse.v20201207.models.AutoScalerBehavior`
        """
        return self._Behavior

    @Behavior.setter
    def Behavior(self, Behavior):
        self._Behavior = Behavior


    def _deserialize(self, params):
        self._MaxReplicas = params.get("MaxReplicas")
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = CloudNativeAPIGatewayStrategyAutoScalerConfigMetric()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._Enabled = params.get("Enabled")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._StrategyId = params.get("StrategyId")
        self._AutoScalerId = params.get("AutoScalerId")
        if params.get("Behavior") is not None:
            self._Behavior = AutoScalerBehavior()
            self._Behavior._deserialize(params.get("Behavior"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayStrategyAutoScalerConfigMetric(AbstractModel):
    r"""Auto scaling configuration metrics

    """

    def __init__(self):
        r"""
        :param _Type: Metric Type
- Resource
        :type Type: str
        :param _ResourceName: Metric resource name
- cpu
- memory
        :type ResourceName: str
        :param _TargetType: Metric target type, currently only support percentage Utilization
        :type TargetType: str
        :param _TargetValue: Target value of the metric
        :type TargetValue: int
        """
        self._Type = None
        self._ResourceName = None
        self._TargetType = None
        self._TargetValue = None

    @property
    def Type(self):
        r"""Metric Type
- Resource
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ResourceName(self):
        r"""Metric resource name
- cpu
- memory
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def TargetType(self):
        r"""Metric target type, currently only support percentage Utilization
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TargetValue(self):
        r"""Target value of the metric
        :rtype: int
        """
        return self._TargetValue

    @TargetValue.setter
    def TargetValue(self, TargetValue):
        self._TargetValue = TargetValue


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._ResourceName = params.get("ResourceName")
        self._TargetType = params.get("TargetType")
        self._TargetValue = params.get("TargetValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayStrategyBindingGroupInfo(AbstractModel):
    r"""Gateway group information of policy binding

    """

    def __init__(self):
        r"""
        :param _GroupId: gateway group ID
        :type GroupId: str
        :param _NodeConfig: Node configuration
        :type NodeConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        :param _BindTime: Binding time
        :type BindTime: str
        :param _GroupName: gateway group name
        :type GroupName: str
        :param _Status: Binding status
        :type Status: str
        """
        self._GroupId = None
        self._NodeConfig = None
        self._BindTime = None
        self._GroupName = None
        self._Status = None

    @property
    def GroupId(self):
        r"""gateway group ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def NodeConfig(self):
        r"""Node configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        """
        return self._NodeConfig

    @NodeConfig.setter
    def NodeConfig(self, NodeConfig):
        self._NodeConfig = NodeConfig

    @property
    def BindTime(self):
        r"""Binding time
        :rtype: str
        """
        return self._BindTime

    @BindTime.setter
    def BindTime(self, BindTime):
        self._BindTime = BindTime

    @property
    def GroupName(self):
        r"""gateway group name
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Status(self):
        r"""Binding status
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("NodeConfig") is not None:
            self._NodeConfig = CloudNativeAPIGatewayNodeConfig()
            self._NodeConfig._deserialize(params.get("NodeConfig"))
        self._BindTime = params.get("BindTime")
        self._GroupName = params.get("GroupName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayStrategyCronScalerConfig(AbstractModel):
    r"""Scheduled scaling policy configuration

    """

    def __init__(self):
        r"""
        :param _Enabled: Enable scheduled scaling
Note: This field may return null, indicating that no valid values can be obtained.
        :type Enabled: bool
        :param _Params: Scheduled scaling configuration parameter list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Params: list of CloudNativeAPIGatewayStrategyCronScalerConfigParam
        :param _CreateTime: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _ModifyTime: Modification time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ModifyTime: str
        :param _StrategyId: Auto scaling policy ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type StrategyId: str
        """
        self._Enabled = None
        self._Params = None
        self._CreateTime = None
        self._ModifyTime = None
        self._StrategyId = None

    @property
    def Enabled(self):
        warnings.warn("parameter `Enabled` is deprecated", DeprecationWarning) 

        r"""Enable scheduled scaling
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        warnings.warn("parameter `Enabled` is deprecated", DeprecationWarning) 

        self._Enabled = Enabled

    @property
    def Params(self):
        r"""Scheduled scaling configuration parameter list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CloudNativeAPIGatewayStrategyCronScalerConfigParam
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def CreateTime(self):
        warnings.warn("parameter `CreateTime` is deprecated", DeprecationWarning) 

        r"""Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        warnings.warn("parameter `CreateTime` is deprecated", DeprecationWarning) 

        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        warnings.warn("parameter `ModifyTime` is deprecated", DeprecationWarning) 

        r"""Modification time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        warnings.warn("parameter `ModifyTime` is deprecated", DeprecationWarning) 

        self._ModifyTime = ModifyTime

    @property
    def StrategyId(self):
        warnings.warn("parameter `StrategyId` is deprecated", DeprecationWarning) 

        r"""Auto scaling policy ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        warnings.warn("parameter `StrategyId` is deprecated", DeprecationWarning) 

        self._StrategyId = StrategyId


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = CloudNativeAPIGatewayStrategyCronScalerConfigParam()
                obj._deserialize(item)
                self._Params.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayStrategyCronScalerConfigParam(AbstractModel):
    r"""Scheduled scaling configuration parameter

    """

    def __init__(self):
        r"""
        :param _Period: Scheduled scaling period
        :type Period: str
        :param _StartAt: Start time of scheduled scaling
        :type StartAt: str
        :param _TargetReplicas: Scheduled scaling target node count, no more than the maximum node count defined in metric scaling
        :type TargetReplicas: int
        :param _Crontab: Scheduled scaling cron expression, no need to input
        :type Crontab: str
        """
        self._Period = None
        self._StartAt = None
        self._TargetReplicas = None
        self._Crontab = None

    @property
    def Period(self):
        r"""Scheduled scaling period
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartAt(self):
        r"""Start time of scheduled scaling
        :rtype: str
        """
        return self._StartAt

    @StartAt.setter
    def StartAt(self, StartAt):
        self._StartAt = StartAt

    @property
    def TargetReplicas(self):
        r"""Scheduled scaling target node count, no more than the maximum node count defined in metric scaling
        :rtype: int
        """
        return self._TargetReplicas

    @TargetReplicas.setter
    def TargetReplicas(self, TargetReplicas):
        self._TargetReplicas = TargetReplicas

    @property
    def Crontab(self):
        r"""Scheduled scaling cron expression, no need to input
        :rtype: str
        """
        return self._Crontab

    @Crontab.setter
    def Crontab(self, Crontab):
        self._Crontab = Crontab


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._StartAt = params.get("StartAt")
        self._TargetReplicas = params.get("TargetReplicas")
        self._Crontab = params.get("Crontab")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayVpcConfig(AbstractModel):
    r"""Cloud native API gateway vpc configuration.

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID.
        :type VpcId: str
        :param _SubnetId: Subnet ID.
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

    @property
    def VpcId(self):
        r"""VPC ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet ID.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoScalerResourceStrategyRequest(AbstractModel):
    r"""CreateAutoScalerResourceStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway instance ID
        :type GatewayId: str
        :param _StrategyName: Policy name.
        :type StrategyName: str
        :param _Description: Policy description
        :type Description: str
        :param _Config: Metric scaling configuration
        :type Config: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyAutoScalerConfig`
        :param _CronScalerConfig: Scheduled scaling configuration list
        :type CronScalerConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyCronScalerConfig`
        :param _MaxReplicas: Maximum number of nodes
        :type MaxReplicas: int
        :param _CronConfig: Scheduled scaling configuration
        :type CronConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyCronScalerConfig`
        """
        self._GatewayId = None
        self._StrategyName = None
        self._Description = None
        self._Config = None
        self._CronScalerConfig = None
        self._MaxReplicas = None
        self._CronConfig = None

    @property
    def GatewayId(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def StrategyName(self):
        r"""Policy name.
        :rtype: str
        """
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def Description(self):
        r"""Policy description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Config(self):
        r"""Metric scaling configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyAutoScalerConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def CronScalerConfig(self):
        warnings.warn("parameter `CronScalerConfig` is deprecated", DeprecationWarning) 

        r"""Scheduled scaling configuration list
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyCronScalerConfig`
        """
        return self._CronScalerConfig

    @CronScalerConfig.setter
    def CronScalerConfig(self, CronScalerConfig):
        warnings.warn("parameter `CronScalerConfig` is deprecated", DeprecationWarning) 

        self._CronScalerConfig = CronScalerConfig

    @property
    def MaxReplicas(self):
        warnings.warn("parameter `MaxReplicas` is deprecated", DeprecationWarning) 

        r"""Maximum number of nodes
        :rtype: int
        """
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        warnings.warn("parameter `MaxReplicas` is deprecated", DeprecationWarning) 

        self._MaxReplicas = MaxReplicas

    @property
    def CronConfig(self):
        r"""Scheduled scaling configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyCronScalerConfig`
        """
        return self._CronConfig

    @CronConfig.setter
    def CronConfig(self, CronConfig):
        self._CronConfig = CronConfig


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._StrategyName = params.get("StrategyName")
        self._Description = params.get("Description")
        if params.get("Config") is not None:
            self._Config = CloudNativeAPIGatewayStrategyAutoScalerConfig()
            self._Config._deserialize(params.get("Config"))
        if params.get("CronScalerConfig") is not None:
            self._CronScalerConfig = CloudNativeAPIGatewayStrategyCronScalerConfig()
            self._CronScalerConfig._deserialize(params.get("CronScalerConfig"))
        self._MaxReplicas = params.get("MaxReplicas")
        if params.get("CronConfig") is not None:
            self._CronConfig = CloudNativeAPIGatewayStrategyCronScalerConfig()
            self._CronConfig._deserialize(params.get("CronConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoScalerResourceStrategyResponse(AbstractModel):
    r"""CreateAutoScalerResourceStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Success status
        :type Result: bool
        :param _StrategyId: Policy ID
        :type StrategyId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._StrategyId = None
        self._RequestId = None

    @property
    def Result(self):
        warnings.warn("parameter `Result` is deprecated", DeprecationWarning) 

        r"""Success status
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        warnings.warn("parameter `Result` is deprecated", DeprecationWarning) 

        self._Result = Result

    @property
    def StrategyId(self):
        r"""Policy ID
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._StrategyId = params.get("StrategyId")
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewayCanaryRuleRequest(AbstractModel):
    r"""CreateCloudNativeAPIGatewayCanaryRule request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _ServiceId: Service ID
        :type ServiceId: str
        :param _CanaryRule: Grayscale rule configuration
        :type CanaryRule: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayCanaryRule`
        :param _CanaryRuleList: Grayscale rule configuration list. If configured, this parameter takes precedence and the CanaryRule parameter is ignored.
        :type CanaryRuleList: list of CloudNativeAPIGatewayCanaryRule
        """
        self._GatewayId = None
        self._ServiceId = None
        self._CanaryRule = None
        self._CanaryRuleList = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServiceId(self):
        r"""Service ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def CanaryRule(self):
        r"""Grayscale rule configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayCanaryRule`
        """
        return self._CanaryRule

    @CanaryRule.setter
    def CanaryRule(self, CanaryRule):
        self._CanaryRule = CanaryRule

    @property
    def CanaryRuleList(self):
        r"""Grayscale rule configuration list. If configured, this parameter takes precedence and the CanaryRule parameter is ignored.
        :rtype: list of CloudNativeAPIGatewayCanaryRule
        """
        return self._CanaryRuleList

    @CanaryRuleList.setter
    def CanaryRuleList(self, CanaryRuleList):
        self._CanaryRuleList = CanaryRuleList


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServiceId = params.get("ServiceId")
        if params.get("CanaryRule") is not None:
            self._CanaryRule = CloudNativeAPIGatewayCanaryRule()
            self._CanaryRule._deserialize(params.get("CanaryRule"))
        if params.get("CanaryRuleList") is not None:
            self._CanaryRuleList = []
            for item in params.get("CanaryRuleList"):
                obj = CloudNativeAPIGatewayCanaryRule()
                obj._deserialize(item)
                self._CanaryRuleList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayCanaryRuleResponse(AbstractModel):
    r"""CreateCloudNativeAPIGatewayCanaryRule response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewayCertificateRequest(AbstractModel):
    r"""CreateCloudNativeAPIGatewayCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _BindDomains: Bound domain name
        :type BindDomains: list of str
        :param _CertId: ssl platform cert Id
        :type CertId: str
        :param _Name: Certificate Name
        :type Name: str
        :param _Key: Certificate Private Key
        :type Key: str
        :param _Crt: Certificate in pem format
        :type Crt: str
        """
        self._GatewayId = None
        self._BindDomains = None
        self._CertId = None
        self._Name = None
        self._Key = None
        self._Crt = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def BindDomains(self):
        r"""Bound domain name
        :rtype: list of str
        """
        return self._BindDomains

    @BindDomains.setter
    def BindDomains(self, BindDomains):
        self._BindDomains = BindDomains

    @property
    def CertId(self):
        r"""ssl platform cert Id
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Name(self):
        r"""Certificate Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Key(self):
        warnings.warn("parameter `Key` is deprecated", DeprecationWarning) 

        r"""Certificate Private Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        warnings.warn("parameter `Key` is deprecated", DeprecationWarning) 

        self._Key = Key

    @property
    def Crt(self):
        warnings.warn("parameter `Crt` is deprecated", DeprecationWarning) 

        r"""Certificate in pem format
        :rtype: str
        """
        return self._Crt

    @Crt.setter
    def Crt(self, Crt):
        warnings.warn("parameter `Crt` is deprecated", DeprecationWarning) 

        self._Crt = Crt


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._BindDomains = params.get("BindDomains")
        self._CertId = params.get("CertId")
        self._Name = params.get("Name")
        self._Key = params.get("Key")
        self._Crt = params.get("Crt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayCertificateResponse(AbstractModel):
    r"""CreateCloudNativeAPIGatewayCertificate response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Create certificate result
        :type Result: :class:`tencentcloud.tse.v20201207.models.CertificateInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Create certificate result
        :rtype: :class:`tencentcloud.tse.v20201207.models.CertificateInfo`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CertificateInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewayPublicNetworkRequest(AbstractModel):
    r"""CreateCloudNativeAPIGatewayPublicNetwork request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud native API gateway instance ID.
        :type GatewayId: str
        :param _GroupId: group id.
        :type GroupId: str
        :param _InternetConfig: Public network CLB configuration.
        :type InternetConfig: :class:`tencentcloud.tse.v20201207.models.InternetConfig`
        """
        self._GatewayId = None
        self._GroupId = None
        self._InternetConfig = None

    @property
    def GatewayId(self):
        r"""Cloud native API gateway instance ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        r"""group id.
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def InternetConfig(self):
        r"""Public network CLB configuration.
        :rtype: :class:`tencentcloud.tse.v20201207.models.InternetConfig`
        """
        return self._InternetConfig

    @InternetConfig.setter
    def InternetConfig(self, InternetConfig):
        self._InternetConfig = InternetConfig


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        if params.get("InternetConfig") is not None:
            self._InternetConfig = InternetConfig()
            self._InternetConfig._deserialize(params.get("InternetConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayPublicNetworkResponse(AbstractModel):
    r"""CreateCloudNativeAPIGatewayPublicNetwork response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned results
        :type Result: :class:`tencentcloud.tse.v20201207.models.CreatePublicNetworkResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned results
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreatePublicNetworkResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CreatePublicNetworkResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewayRequest(AbstractModel):
    r"""CreateCloudNativeAPIGateway request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Cloud native API gateway name supports up to 60 characters.
        :type Name: str
        :param _Type: Cloud native API gateway type, currently only support kong.
        :type Type: str
        :param _GatewayVersion: Cloud Native API gateway version. Reference value:
- 2.4.1
- 2.5.1
        :type GatewayVersion: str
        :param _NodeConfig: Cloud Native API gateway node configuration.
        :type NodeConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        :param _VpcConfig: Cloud native API gateway vpc configuration.
        :type VpcConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayVpcConfig`
        :param _Description: Cloud native API gateway description supports up to 120 characters.
        :type Description: str
        :param _Tags: Tag list
        :type Tags: list of InstanceTagInfo
        :param _EnableCls: Whether CLS log is enabled. Default value: false.
        :type EnableCls: bool
        :param _FeatureVersion: Product version. Reference value:
-TRIAL: Development edition
-STANDARD: Standard version (default value)
-PROFESSIONAL: Pro Edition
        :type FeatureVersion: str
        :param _InternetMaxBandwidthOut: Public network outbound traffic bandwidth, [1,2048]Mbps
        :type InternetMaxBandwidthOut: int
        :param _EngineRegion: Actual region information of the instance. Default value: ap-guangzhou.
        :type EngineRegion: str
        :param _IngressClassName: ingress Class name
        :type IngressClassName: str
        :param _TradeType: Payment type. Reference value:
0: Postpaid (default value)
1: Prepayment (The API does not currently support creating prepaid instances)
        :type TradeType: int
        :param _InternetConfig: Public network configuration
        :type InternetConfig: :class:`tencentcloud.tse.v20201207.models.InternetConfig`
        :param _PromId: Associated prometheus ID
        :type PromId: str
        """
        self._Name = None
        self._Type = None
        self._GatewayVersion = None
        self._NodeConfig = None
        self._VpcConfig = None
        self._Description = None
        self._Tags = None
        self._EnableCls = None
        self._FeatureVersion = None
        self._InternetMaxBandwidthOut = None
        self._EngineRegion = None
        self._IngressClassName = None
        self._TradeType = None
        self._InternetConfig = None
        self._PromId = None

    @property
    def Name(self):
        r"""Cloud native API gateway name supports up to 60 characters.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""Cloud native API gateway type, currently only support kong.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def GatewayVersion(self):
        r"""Cloud Native API gateway version. Reference value:
- 2.4.1
- 2.5.1
        :rtype: str
        """
        return self._GatewayVersion

    @GatewayVersion.setter
    def GatewayVersion(self, GatewayVersion):
        self._GatewayVersion = GatewayVersion

    @property
    def NodeConfig(self):
        r"""Cloud Native API gateway node configuration.
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        """
        return self._NodeConfig

    @NodeConfig.setter
    def NodeConfig(self, NodeConfig):
        self._NodeConfig = NodeConfig

    @property
    def VpcConfig(self):
        r"""Cloud native API gateway vpc configuration.
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayVpcConfig`
        """
        return self._VpcConfig

    @VpcConfig.setter
    def VpcConfig(self, VpcConfig):
        self._VpcConfig = VpcConfig

    @property
    def Description(self):
        r"""Cloud native API gateway description supports up to 120 characters.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        r"""Tag list
        :rtype: list of InstanceTagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def EnableCls(self):
        r"""Whether CLS log is enabled. Default value: false.
        :rtype: bool
        """
        return self._EnableCls

    @EnableCls.setter
    def EnableCls(self, EnableCls):
        self._EnableCls = EnableCls

    @property
    def FeatureVersion(self):
        r"""Product version. Reference value:
-TRIAL: Development edition
-STANDARD: Standard version (default value)
-PROFESSIONAL: Pro Edition
        :rtype: str
        """
        return self._FeatureVersion

    @FeatureVersion.setter
    def FeatureVersion(self, FeatureVersion):
        self._FeatureVersion = FeatureVersion

    @property
    def InternetMaxBandwidthOut(self):
        r"""Public network outbound traffic bandwidth, [1,2048]Mbps
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def EngineRegion(self):
        r"""Actual region information of the instance. Default value: ap-guangzhou.
        :rtype: str
        """
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion

    @property
    def IngressClassName(self):
        r"""ingress Class name
        :rtype: str
        """
        return self._IngressClassName

    @IngressClassName.setter
    def IngressClassName(self, IngressClassName):
        self._IngressClassName = IngressClassName

    @property
    def TradeType(self):
        r"""Payment type. Reference value:
0: Postpaid (default value)
1: Prepayment (The API does not currently support creating prepaid instances)
        :rtype: int
        """
        return self._TradeType

    @TradeType.setter
    def TradeType(self, TradeType):
        self._TradeType = TradeType

    @property
    def InternetConfig(self):
        r"""Public network configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.InternetConfig`
        """
        return self._InternetConfig

    @InternetConfig.setter
    def InternetConfig(self, InternetConfig):
        self._InternetConfig = InternetConfig

    @property
    def PromId(self):
        r"""Associated prometheus ID
        :rtype: str
        """
        return self._PromId

    @PromId.setter
    def PromId(self, PromId):
        self._PromId = PromId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._GatewayVersion = params.get("GatewayVersion")
        if params.get("NodeConfig") is not None:
            self._NodeConfig = CloudNativeAPIGatewayNodeConfig()
            self._NodeConfig._deserialize(params.get("NodeConfig"))
        if params.get("VpcConfig") is not None:
            self._VpcConfig = CloudNativeAPIGatewayVpcConfig()
            self._VpcConfig._deserialize(params.get("VpcConfig"))
        self._Description = params.get("Description")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = InstanceTagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._EnableCls = params.get("EnableCls")
        self._FeatureVersion = params.get("FeatureVersion")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._EngineRegion = params.get("EngineRegion")
        self._IngressClassName = params.get("IngressClassName")
        self._TradeType = params.get("TradeType")
        if params.get("InternetConfig") is not None:
            self._InternetConfig = InternetConfig()
            self._InternetConfig._deserialize(params.get("InternetConfig"))
        self._PromId = params.get("PromId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayResponse(AbstractModel):
    r"""CreateCloudNativeAPIGateway response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Create the response result of the Cloud Native API gateway instance.
        :type Result: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Create the response result of the Cloud Native API gateway instance.
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CreateCloudNativeAPIGatewayResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewayResult(AbstractModel):
    r"""Create the cloud native API gateway response result.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud Native API Gateway ID.
        :type GatewayId: str
        :param _Status: Cloud-native gateway status.
        :type Status: str
        :param _TaskId: Task ID.
        :type TaskId: str
        """
        self._GatewayId = None
        self._Status = None
        self._TaskId = None

    @property
    def GatewayId(self):
        r"""Cloud Native API Gateway ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Status(self):
        r"""Cloud-native gateway status.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayRouteRateLimitRequest(AbstractModel):
    r"""CreateCloudNativeAPIGatewayRouteRateLimit request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: gateway ID
        :type GatewayId: str
        :param _Id: Route id or routing name.
"Unnamed" is not supported.
        :type Id: str
        :param _LimitDetail: Configure stream
        :type LimitDetail: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        """
        self._GatewayId = None
        self._Id = None
        self._LimitDetail = None

    @property
    def GatewayId(self):
        r"""gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Id(self):
        r"""Route id or routing name.
"Unnamed" is not supported.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def LimitDetail(self):
        r"""Configure stream
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        """
        return self._LimitDetail

    @LimitDetail.setter
    def LimitDetail(self, LimitDetail):
        self._LimitDetail = LimitDetail


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Id = params.get("Id")
        if params.get("LimitDetail") is not None:
            self._LimitDetail = CloudNativeAPIGatewayRateLimitDetail()
            self._LimitDetail._deserialize(params.get("LimitDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayRouteRateLimitResponse(AbstractModel):
    r"""CreateCloudNativeAPIGatewayRouteRateLimit response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewayRouteRequest(AbstractModel):
    r"""CreateCloudNativeAPIGatewayRoute request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _ServiceID: Service ID
        :type ServiceID: str
        :param _RouteName: The name of the route, unique at the instance level, does not need to be provided.
        :type RouteName: str
        :param _Methods: Method of route. Available values:
- GET
- POST
- DELETE
- PUT
- OPTIONS
- PATCH
- HEAD
- ANY
- TRACE
- COPY
- MOVE
- PROPFIND
- PROPPATCH
- MKCOL
- LOCK
- UNLOCK
        :type Methods: list of str
        :param _Hosts: Domain of the route
        :type Hosts: list of str
        :param _Paths: Path of the route
        :type Paths: list of str
        :param _Protocols: Route protocol, optional
- https
- http
        :type Protocols: list of str
        :param _PreserveHost: Preserve Host when forwarding to backend
        :type PreserveHost: bool
        :param _HttpsRedirectStatusCode: HTTP redirection status code
        :type HttpsRedirectStatusCode: int
        :param _StripPath: StripPath when forwarding to backend
        :type StripPath: bool
        :param _ForceHttps: Whether to enable mandatory HTTPS
        :type ForceHttps: bool
        :param _DestinationPorts: Destination port for Layer 4 match
        :type DestinationPorts: list of int non-negative
        :param _Headers: Headers of the route
        :type Headers: list of KVMapping
        :param _RequestBuffering: Whether to cache the request body, default true
        :type RequestBuffering: bool
        :param _ResponseBuffering: Whether to cache the response body. Default true
        :type ResponseBuffering: bool
        :param _RegexPriority: Regular priority
        :type RegexPriority: int
        :param _QueryStringParameters: queryString parameter
        :type QueryStringParameters: list of KVMapping
        """
        self._GatewayId = None
        self._ServiceID = None
        self._RouteName = None
        self._Methods = None
        self._Hosts = None
        self._Paths = None
        self._Protocols = None
        self._PreserveHost = None
        self._HttpsRedirectStatusCode = None
        self._StripPath = None
        self._ForceHttps = None
        self._DestinationPorts = None
        self._Headers = None
        self._RequestBuffering = None
        self._ResponseBuffering = None
        self._RegexPriority = None
        self._QueryStringParameters = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServiceID(self):
        r"""Service ID
        :rtype: str
        """
        return self._ServiceID

    @ServiceID.setter
    def ServiceID(self, ServiceID):
        self._ServiceID = ServiceID

    @property
    def RouteName(self):
        r"""The name of the route, unique at the instance level, does not need to be provided.
        :rtype: str
        """
        return self._RouteName

    @RouteName.setter
    def RouteName(self, RouteName):
        self._RouteName = RouteName

    @property
    def Methods(self):
        r"""Method of route. Available values:
- GET
- POST
- DELETE
- PUT
- OPTIONS
- PATCH
- HEAD
- ANY
- TRACE
- COPY
- MOVE
- PROPFIND
- PROPPATCH
- MKCOL
- LOCK
- UNLOCK
        :rtype: list of str
        """
        return self._Methods

    @Methods.setter
    def Methods(self, Methods):
        self._Methods = Methods

    @property
    def Hosts(self):
        r"""Domain of the route
        :rtype: list of str
        """
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def Paths(self):
        r"""Path of the route
        :rtype: list of str
        """
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths

    @property
    def Protocols(self):
        r"""Route protocol, optional
- https
- http
        :rtype: list of str
        """
        return self._Protocols

    @Protocols.setter
    def Protocols(self, Protocols):
        self._Protocols = Protocols

    @property
    def PreserveHost(self):
        r"""Preserve Host when forwarding to backend
        :rtype: bool
        """
        return self._PreserveHost

    @PreserveHost.setter
    def PreserveHost(self, PreserveHost):
        self._PreserveHost = PreserveHost

    @property
    def HttpsRedirectStatusCode(self):
        r"""HTTP redirection status code
        :rtype: int
        """
        return self._HttpsRedirectStatusCode

    @HttpsRedirectStatusCode.setter
    def HttpsRedirectStatusCode(self, HttpsRedirectStatusCode):
        self._HttpsRedirectStatusCode = HttpsRedirectStatusCode

    @property
    def StripPath(self):
        r"""StripPath when forwarding to backend
        :rtype: bool
        """
        return self._StripPath

    @StripPath.setter
    def StripPath(self, StripPath):
        self._StripPath = StripPath

    @property
    def ForceHttps(self):
        warnings.warn("parameter `ForceHttps` is deprecated", DeprecationWarning) 

        r"""Whether to enable mandatory HTTPS
        :rtype: bool
        """
        return self._ForceHttps

    @ForceHttps.setter
    def ForceHttps(self, ForceHttps):
        warnings.warn("parameter `ForceHttps` is deprecated", DeprecationWarning) 

        self._ForceHttps = ForceHttps

    @property
    def DestinationPorts(self):
        r"""Destination port for Layer 4 match
        :rtype: list of int non-negative
        """
        return self._DestinationPorts

    @DestinationPorts.setter
    def DestinationPorts(self, DestinationPorts):
        self._DestinationPorts = DestinationPorts

    @property
    def Headers(self):
        r"""Headers of the route
        :rtype: list of KVMapping
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def RequestBuffering(self):
        r"""Whether to cache the request body, default true
        :rtype: bool
        """
        return self._RequestBuffering

    @RequestBuffering.setter
    def RequestBuffering(self, RequestBuffering):
        self._RequestBuffering = RequestBuffering

    @property
    def ResponseBuffering(self):
        r"""Whether to cache the response body. Default true
        :rtype: bool
        """
        return self._ResponseBuffering

    @ResponseBuffering.setter
    def ResponseBuffering(self, ResponseBuffering):
        self._ResponseBuffering = ResponseBuffering

    @property
    def RegexPriority(self):
        r"""Regular priority
        :rtype: int
        """
        return self._RegexPriority

    @RegexPriority.setter
    def RegexPriority(self, RegexPriority):
        self._RegexPriority = RegexPriority

    @property
    def QueryStringParameters(self):
        r"""queryString parameter
        :rtype: list of KVMapping
        """
        return self._QueryStringParameters

    @QueryStringParameters.setter
    def QueryStringParameters(self, QueryStringParameters):
        self._QueryStringParameters = QueryStringParameters


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServiceID = params.get("ServiceID")
        self._RouteName = params.get("RouteName")
        self._Methods = params.get("Methods")
        self._Hosts = params.get("Hosts")
        self._Paths = params.get("Paths")
        self._Protocols = params.get("Protocols")
        self._PreserveHost = params.get("PreserveHost")
        self._HttpsRedirectStatusCode = params.get("HttpsRedirectStatusCode")
        self._StripPath = params.get("StripPath")
        self._ForceHttps = params.get("ForceHttps")
        self._DestinationPorts = params.get("DestinationPorts")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = KVMapping()
                obj._deserialize(item)
                self._Headers.append(obj)
        self._RequestBuffering = params.get("RequestBuffering")
        self._ResponseBuffering = params.get("ResponseBuffering")
        self._RegexPriority = params.get("RegexPriority")
        if params.get("QueryStringParameters") is not None:
            self._QueryStringParameters = []
            for item in params.get("QueryStringParameters"):
                obj = KVMapping()
                obj._deserialize(item)
                self._QueryStringParameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayRouteResponse(AbstractModel):
    r"""CreateCloudNativeAPIGatewayRoute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewayServerGroupResult(AbstractModel):
    r"""Create Gateway Group Information

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway instance ID
        :type GatewayId: str
        :param _GroupId: Group ID
        :type GroupId: str
        :param _Status: Status.
        :type Status: str
        :param _TaskId: Task ID.
        :type TaskId: str
        """
        self._GatewayId = None
        self._GroupId = None
        self._Status = None
        self._TaskId = None

    @property
    def GatewayId(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        r"""Group ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Status(self):
        r"""Status.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayServiceRateLimitRequest(AbstractModel):
    r"""CreateCloudNativeAPIGatewayServiceRateLimit request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _Name: Service name or service ID
        :type Name: str
        :param _LimitDetail: Configure throttling
        :type LimitDetail: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        """
        self._GatewayId = None
        self._Name = None
        self._LimitDetail = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""Service name or service ID
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LimitDetail(self):
        r"""Configure throttling
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        """
        return self._LimitDetail

    @LimitDetail.setter
    def LimitDetail(self, LimitDetail):
        self._LimitDetail = LimitDetail


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        if params.get("LimitDetail") is not None:
            self._LimitDetail = CloudNativeAPIGatewayRateLimitDetail()
            self._LimitDetail._deserialize(params.get("LimitDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayServiceRateLimitResponse(AbstractModel):
    r"""CreateCloudNativeAPIGatewayServiceRateLimit response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewayServiceRequest(AbstractModel):
    r"""CreateCloudNativeAPIGatewayService request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: gateway ID
        :type GatewayId: str
        :param _Name: Service name
        :type Name: str
        :param _Protocol: Request protocol:
- https
- http
- tcp
- udp
        :type Protocol: str
        :param _Timeout: Timeout interval. Unit: ms
        :type Timeout: int
        :param _Retries: Number of retries.
        :type Retries: int
        :param _UpstreamType: Service type 
- Kubernetes 
- Registry
- IPList
- HostIP
- Scf	
        :type UpstreamType: str
        :param _UpstreamInfo: Service configuration information
        :type UpstreamInfo: :class:`tencentcloud.tse.v20201207.models.KongUpstreamInfo`
        :param _Path: Request path
        :type Path: str
        """
        self._GatewayId = None
        self._Name = None
        self._Protocol = None
        self._Timeout = None
        self._Retries = None
        self._UpstreamType = None
        self._UpstreamInfo = None
        self._Path = None

    @property
    def GatewayId(self):
        r"""gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""Service name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Protocol(self):
        r"""Request protocol:
- https
- http
- tcp
- udp
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Timeout(self):
        r"""Timeout interval. Unit: ms
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Retries(self):
        r"""Number of retries.
        :rtype: int
        """
        return self._Retries

    @Retries.setter
    def Retries(self, Retries):
        self._Retries = Retries

    @property
    def UpstreamType(self):
        r"""Service type 
- Kubernetes 
- Registry
- IPList
- HostIP
- Scf	
        :rtype: str
        """
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def UpstreamInfo(self):
        r"""Service configuration information
        :rtype: :class:`tencentcloud.tse.v20201207.models.KongUpstreamInfo`
        """
        return self._UpstreamInfo

    @UpstreamInfo.setter
    def UpstreamInfo(self, UpstreamInfo):
        self._UpstreamInfo = UpstreamInfo

    @property
    def Path(self):
        r"""Request path
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        self._Protocol = params.get("Protocol")
        self._Timeout = params.get("Timeout")
        self._Retries = params.get("Retries")
        self._UpstreamType = params.get("UpstreamType")
        if params.get("UpstreamInfo") is not None:
            self._UpstreamInfo = KongUpstreamInfo()
            self._UpstreamInfo._deserialize(params.get("UpstreamInfo"))
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayServiceResponse(AbstractModel):
    r"""CreateCloudNativeAPIGatewayService response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Gateway service creation result
        :type Result: :class:`tencentcloud.tse.v20201207.models.CreateGatewayServiceResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Gateway service creation result
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateGatewayServiceResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CreateGatewayServiceResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateGatewayServiceResult(AbstractModel):
    r"""Cloud-native gateway service creation result

    """

    def __init__(self):
        r"""
        :param _ServiceId: Gateway Service ID
        :type ServiceId: str
        """
        self._ServiceId = None

    @property
    def ServiceId(self):
        r"""Gateway Service ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGovernanceLaneGroupsRequest(AbstractModel):
    r"""CreateGovernanceLaneGroups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Engine Instance ID
        :type InstanceId: str
        :param _LaneGroups: Lane group rule list
        :type LaneGroups: list of GovernanceLaneGroup
        """
        self._InstanceId = None
        self._LaneGroups = None

    @property
    def InstanceId(self):
        r"""Engine Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LaneGroups(self):
        r"""Lane group rule list
        :rtype: list of GovernanceLaneGroup
        """
        return self._LaneGroups

    @LaneGroups.setter
    def LaneGroups(self, LaneGroups):
        self._LaneGroups = LaneGroups


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("LaneGroups") is not None:
            self._LaneGroups = []
            for item in params.get("LaneGroups"):
                obj = GovernanceLaneGroup()
                obj._deserialize(item)
                self._LaneGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGovernanceLaneGroupsResponse(AbstractModel):
    r"""CreateGovernanceLaneGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the creation succeeded
        :type Result: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Whether the creation succeeded
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateNativeGatewayServerGroupRequest(AbstractModel):
    r"""CreateNativeGatewayServerGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway instance id.
Only supports postpaid instances
        :type GatewayId: str
        :param _Name: gateway group name
        :type Name: str
        :param _NodeConfig: Node configuration
        :type NodeConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _Description: Description information
        :type Description: str
        :param _InternetMaxBandwidthOut: Public network bandwidth information
        :type InternetMaxBandwidthOut: int
        :param _InternetConfig: Public Network Configuration.
        :type InternetConfig: :class:`tencentcloud.tse.v20201207.models.InternetConfig`
        """
        self._GatewayId = None
        self._Name = None
        self._NodeConfig = None
        self._SubnetId = None
        self._Description = None
        self._InternetMaxBandwidthOut = None
        self._InternetConfig = None

    @property
    def GatewayId(self):
        r"""Gateway instance id.
Only supports postpaid instances
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""gateway group name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NodeConfig(self):
        r"""Node configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        """
        return self._NodeConfig

    @NodeConfig.setter
    def NodeConfig(self, NodeConfig):
        self._NodeConfig = NodeConfig

    @property
    def SubnetId(self):
        r"""Subnet ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Description(self):
        r"""Description information
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InternetMaxBandwidthOut(self):
        r"""Public network bandwidth information
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def InternetConfig(self):
        r"""Public Network Configuration.
        :rtype: :class:`tencentcloud.tse.v20201207.models.InternetConfig`
        """
        return self._InternetConfig

    @InternetConfig.setter
    def InternetConfig(self, InternetConfig):
        self._InternetConfig = InternetConfig


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        if params.get("NodeConfig") is not None:
            self._NodeConfig = CloudNativeAPIGatewayNodeConfig()
            self._NodeConfig._deserialize(params.get("NodeConfig"))
        self._SubnetId = params.get("SubnetId")
        self._Description = params.get("Description")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        if params.get("InternetConfig") is not None:
            self._InternetConfig = InternetConfig()
            self._InternetConfig._deserialize(params.get("InternetConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNativeGatewayServerGroupResponse(AbstractModel):
    r"""CreateNativeGatewayServerGroup response structure.

    """

    def __init__(self):
        r"""
        :param _Result: gateway group creation info
        :type Result: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayServerGroupResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""gateway group creation info
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayServerGroupResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CreateCloudNativeAPIGatewayServerGroupResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateNativeGatewayServiceSourceRequest(AbstractModel):
    r"""CreateNativeGatewayServiceSource request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayID: Gateway instance ID
        :type GatewayID: str
        :param _SourceType: Service source type. Reference value:
- TSE-Nacos 
- TSE-Consul 
- TSE-PolarisMesh
- Customer-Nacos
- Customer-Consul
- Customer-PolarisMesh
- TSF
- TKE
- EKS
- PrivateDNS
- Customer-DNS
        :type SourceType: str
        :param _SourceID: Instance ID of the service source. Required when SourceType is not PrivateDNS or Customer-DNS.
        :type SourceID: str
        :param _SourceName: Source instance name of the service. Required when SourceType is not PrivateDNS.
        :type SourceName: str
        :param _SourceInfo: Service source instance additional information
        :type SourceInfo: :class:`tencentcloud.tse.v20201207.models.SourceInfo`
        """
        self._GatewayID = None
        self._SourceType = None
        self._SourceID = None
        self._SourceName = None
        self._SourceInfo = None

    @property
    def GatewayID(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayID

    @GatewayID.setter
    def GatewayID(self, GatewayID):
        self._GatewayID = GatewayID

    @property
    def SourceType(self):
        r"""Service source type. Reference value:
- TSE-Nacos 
- TSE-Consul 
- TSE-PolarisMesh
- Customer-Nacos
- Customer-Consul
- Customer-PolarisMesh
- TSF
- TKE
- EKS
- PrivateDNS
- Customer-DNS
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceID(self):
        r"""Instance ID of the service source. Required when SourceType is not PrivateDNS or Customer-DNS.
        :rtype: str
        """
        return self._SourceID

    @SourceID.setter
    def SourceID(self, SourceID):
        self._SourceID = SourceID

    @property
    def SourceName(self):
        r"""Source instance name of the service. Required when SourceType is not PrivateDNS.
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def SourceInfo(self):
        r"""Service source instance additional information
        :rtype: :class:`tencentcloud.tse.v20201207.models.SourceInfo`
        """
        return self._SourceInfo

    @SourceInfo.setter
    def SourceInfo(self, SourceInfo):
        self._SourceInfo = SourceInfo


    def _deserialize(self, params):
        self._GatewayID = params.get("GatewayID")
        self._SourceType = params.get("SourceType")
        self._SourceID = params.get("SourceID")
        self._SourceName = params.get("SourceName")
        if params.get("SourceInfo") is not None:
            self._SourceInfo = SourceInfo()
            self._SourceInfo._deserialize(params.get("SourceInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNativeGatewayServiceSourceResponse(AbstractModel):
    r"""CreateNativeGatewayServiceSource response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the creation succeeded
        :type Result: bool
        :param _SourceID: Service Source ID
        :type SourceID: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._SourceID = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Whether the creation succeeded
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def SourceID(self):
        r"""Service Source ID
        :rtype: str
        """
        return self._SourceID

    @SourceID.setter
    def SourceID(self, SourceID):
        self._SourceID = SourceID

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._SourceID = params.get("SourceID")
        self._RequestId = params.get("RequestId")


class CreateOrModifyCloudNativeAPIGatewayCORSRequest(AbstractModel):
    r"""CreateOrModifyCloudNativeAPIGatewayCORS request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _SourceType: Resource type bound to the cross-origin plug-in: route|service
        :type SourceType: str
        :param _SourceId: id of the route or service
        :type SourceId: str
        :param _Enabled: Whether to enable the plug-in
        :type Enabled: bool
        :param _Origins: Cross-Origin Access-Control-Allow-Origin
        :type Origins: list of str
        :param _Headers: Cross-Origin Access-Control-Allow-Headers header
        :type Headers: list of str
        :param _Methods: Access-Control-Allow-Methods for CORS
        :type Methods: list of str
        :param _ExposedHeaders: Access-Control-Expose-Headers
        :type ExposedHeaders: list of str
        :param _MaxAge: preflight request cache time
        :type MaxAge: int
        :param _Credentials: Access-Control-Allow-Credentials for CORS
        :type Credentials: bool
        :param _PreFlightContinue: Whether to pass through the OPTIONS request to the backend
        :type PreFlightContinue: bool
        """
        self._GatewayId = None
        self._SourceType = None
        self._SourceId = None
        self._Enabled = None
        self._Origins = None
        self._Headers = None
        self._Methods = None
        self._ExposedHeaders = None
        self._MaxAge = None
        self._Credentials = None
        self._PreFlightContinue = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def SourceType(self):
        r"""Resource type bound to the cross-origin plug-in: route|service
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceId(self):
        r"""id of the route or service
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def Enabled(self):
        r"""Whether to enable the plug-in
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Origins(self):
        r"""Cross-Origin Access-Control-Allow-Origin
        :rtype: list of str
        """
        return self._Origins

    @Origins.setter
    def Origins(self, Origins):
        self._Origins = Origins

    @property
    def Headers(self):
        r"""Cross-Origin Access-Control-Allow-Headers header
        :rtype: list of str
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def Methods(self):
        r"""Access-Control-Allow-Methods for CORS
        :rtype: list of str
        """
        return self._Methods

    @Methods.setter
    def Methods(self, Methods):
        self._Methods = Methods

    @property
    def ExposedHeaders(self):
        r"""Access-Control-Expose-Headers
        :rtype: list of str
        """
        return self._ExposedHeaders

    @ExposedHeaders.setter
    def ExposedHeaders(self, ExposedHeaders):
        self._ExposedHeaders = ExposedHeaders

    @property
    def MaxAge(self):
        r"""preflight request cache time
        :rtype: int
        """
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def Credentials(self):
        r"""Access-Control-Allow-Credentials for CORS
        :rtype: bool
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def PreFlightContinue(self):
        r"""Whether to pass through the OPTIONS request to the backend
        :rtype: bool
        """
        return self._PreFlightContinue

    @PreFlightContinue.setter
    def PreFlightContinue(self, PreFlightContinue):
        self._PreFlightContinue = PreFlightContinue


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._SourceType = params.get("SourceType")
        self._SourceId = params.get("SourceId")
        self._Enabled = params.get("Enabled")
        self._Origins = params.get("Origins")
        self._Headers = params.get("Headers")
        self._Methods = params.get("Methods")
        self._ExposedHeaders = params.get("ExposedHeaders")
        self._MaxAge = params.get("MaxAge")
        self._Credentials = params.get("Credentials")
        self._PreFlightContinue = params.get("PreFlightContinue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrModifyCloudNativeAPIGatewayCORSResponse(AbstractModel):
    r"""CreateOrModifyCloudNativeAPIGatewayCORS response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreatePublicNetworkResult(AbstractModel):
    r"""Create a public network result for the kong client

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway instance ID
        :type GatewayId: str
        :param _GroupId: group ID
        :type GroupId: str
        :param _NetworkId: Client public network ID
        :type NetworkId: str
        """
        self._GatewayId = None
        self._GroupId = None
        self._NetworkId = None

    @property
    def GatewayId(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        r"""group ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def NetworkId(self):
        r"""Client public network ID
        :rtype: str
        """
        return self._NetworkId

    @NetworkId.setter
    def NetworkId(self, NetworkId):
        self._NetworkId = NetworkId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._NetworkId = params.get("NetworkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWafDomainsRequest(AbstractModel):
    r"""CreateWafDomains request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _Domains: List of WAF-protected domain names
        :type Domains: list of str
        """
        self._GatewayId = None
        self._Domains = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Domains(self):
        r"""List of WAF-protected domain names
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWafDomainsResponse(AbstractModel):
    r"""CreateWafDomains response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteAutoScalerResourceStrategyRequest(AbstractModel):
    r"""DeleteAutoScalerResourceStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway instance ID
        :type GatewayId: str
        :param _StrategyId: Policy ID
        :type StrategyId: str
        """
        self._GatewayId = None
        self._StrategyId = None

    @property
    def GatewayId(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def StrategyId(self):
        r"""Policy ID
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoScalerResourceStrategyResponse(AbstractModel):
    r"""DeleteAutoScalerResourceStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Success status
        :type Result: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Success status
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteCloudNativeAPIGatewayCORSRequest(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayCORS request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _SourceType: Resource type bound to the cross-origin plug-in: route|service
        :type SourceType: str
        :param _SourceId: id of the route or service
        :type SourceId: str
        """
        self._GatewayId = None
        self._SourceType = None
        self._SourceId = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def SourceType(self):
        r"""Resource type bound to the cross-origin plug-in: route|service
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceId(self):
        r"""id of the route or service
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._SourceType = params.get("SourceType")
        self._SourceId = params.get("SourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayCORSResponse(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayCORS response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteCloudNativeAPIGatewayCanaryRuleRequest(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayCanaryRule request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _ServiceId: Service ID
        :type ServiceId: str
        :param _Priority: Priority
        :type Priority: int
        :param _PriorityList: Priority list. If configured, this parameter takes precedence and the Priority parameter is ignored.
        :type PriorityList: list of int
        """
        self._GatewayId = None
        self._ServiceId = None
        self._Priority = None
        self._PriorityList = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServiceId(self):
        r"""Service ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Priority(self):
        r"""Priority
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def PriorityList(self):
        r"""Priority list. If configured, this parameter takes precedence and the Priority parameter is ignored.
        :rtype: list of int
        """
        return self._PriorityList

    @PriorityList.setter
    def PriorityList(self, PriorityList):
        self._PriorityList = PriorityList


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServiceId = params.get("ServiceId")
        self._Priority = params.get("Priority")
        self._PriorityList = params.get("PriorityList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayCanaryRuleResponse(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayCanaryRule response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteCloudNativeAPIGatewayCertificateRequest(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: gateway ID
        :type GatewayId: str
        :param _Id: Certificate ID
        :type Id: str
        """
        self._GatewayId = None
        self._Id = None

    @property
    def GatewayId(self):
        r"""gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Id(self):
        r"""Certificate ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayCertificateResponse(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayCertificate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteCloudNativeAPIGatewayPublicNetworkRequest(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayPublicNetwork request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud native API gateway instance ID.
        :type GatewayId: str
        :param _GroupId: group id, required for kong event type
        :type GroupId: str
        :param _InternetAddressVersion: public network type
-IPV4 (default value)
- IPV6
        :type InternetAddressVersion: str
        :param _Vip: Public IP address. Required when public IP addresses exist across multiple public networks.
        :type Vip: str
        """
        self._GatewayId = None
        self._GroupId = None
        self._InternetAddressVersion = None
        self._Vip = None

    @property
    def GatewayId(self):
        r"""Cloud native API gateway instance ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        r"""group id, required for kong event type
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def InternetAddressVersion(self):
        r"""public network type
-IPV4 (default value)
- IPV6
        :rtype: str
        """
        return self._InternetAddressVersion

    @InternetAddressVersion.setter
    def InternetAddressVersion(self, InternetAddressVersion):
        self._InternetAddressVersion = InternetAddressVersion

    @property
    def Vip(self):
        r"""Public IP address. Required when public IP addresses exist across multiple public networks.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._InternetAddressVersion = params.get("InternetAddressVersion")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayPublicNetworkResponse(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayPublicNetwork response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteCloudNativeAPIGatewayRequest(AbstractModel):
    r"""DeleteCloudNativeAPIGateway request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud native API gateway instance ID.
        :type GatewayId: str
        :param _DeleteClsTopic: Whether to delete the CLS log topic associated with the instance.
        :type DeleteClsTopic: bool
        """
        self._GatewayId = None
        self._DeleteClsTopic = None

    @property
    def GatewayId(self):
        r"""Cloud native API gateway instance ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def DeleteClsTopic(self):
        r"""Whether to delete the CLS log topic associated with the instance.
        :rtype: bool
        """
        return self._DeleteClsTopic

    @DeleteClsTopic.setter
    def DeleteClsTopic(self, DeleteClsTopic):
        self._DeleteClsTopic = DeleteClsTopic


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._DeleteClsTopic = params.get("DeleteClsTopic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayResponse(AbstractModel):
    r"""DeleteCloudNativeAPIGateway response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Delete the cloud native API gateway instance response result.
        :type Result: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Delete the cloud native API gateway instance response result.
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DeleteCloudNativeAPIGatewayResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteCloudNativeAPIGatewayResult(AbstractModel):
    r"""Delete the response result of the cloud native API gateway.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud-native gateway ID.
        :type GatewayId: str
        :param _Status: Cloud-native gateway status.
        :type Status: str
        """
        self._GatewayId = None
        self._Status = None

    @property
    def GatewayId(self):
        r"""Cloud-native gateway ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Status(self):
        r"""Cloud-native gateway status.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayRouteRateLimitRequest(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayRouteRateLimit request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _Id: Route Id or routing name.
"Unnamed" is not supported.
        :type Id: str
        """
        self._GatewayId = None
        self._Id = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Id(self):
        r"""Route Id or routing name.
"Unnamed" is not supported.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayRouteRateLimitResponse(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayRouteRateLimit response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteCloudNativeAPIGatewayRouteRequest(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayRoute request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _Name: The ID or name of the route. The name "unnamed" is not supported.
        :type Name: str
        """
        self._GatewayId = None
        self._Name = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""The ID or name of the route. The name "unnamed" is not supported.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayRouteResponse(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayRoute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteCloudNativeAPIGatewayServiceRateLimitRequest(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayServiceRateLimit request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _Name: Service name or service ID
        :type Name: str
        """
        self._GatewayId = None
        self._Name = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""Service name or service ID
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayServiceRateLimitResponse(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayServiceRateLimit response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteCloudNativeAPIGatewayServiceRequest(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayService request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: gateway ID
        :type GatewayId: str
        :param _Name: Service name, service ID
        :type Name: str
        :param _DeleteRoutes: Whether to synchronize the deletion of routes bound to the service
        :type DeleteRoutes: bool
        """
        self._GatewayId = None
        self._Name = None
        self._DeleteRoutes = None

    @property
    def GatewayId(self):
        r"""gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""Service name, service ID
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DeleteRoutes(self):
        r"""Whether to synchronize the deletion of routes bound to the service
        :rtype: bool
        """
        return self._DeleteRoutes

    @DeleteRoutes.setter
    def DeleteRoutes(self, DeleteRoutes):
        self._DeleteRoutes = DeleteRoutes


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        self._DeleteRoutes = params.get("DeleteRoutes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayServiceResponse(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayService response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteGovernanceLaneGroup(AbstractModel):
    r"""Lane group

    """

    def __init__(self):
        r"""
        :param _Name: lane name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _ID: Lane group ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ID: str
        :param _TrafficEntries: Lane entry service list
Note: This field may return null, indicating that no valid values can be obtained.
        :type TrafficEntries: list of LaneTrafficEntry
        :param _Destinations: Lane service list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Destinations: list of GovernanceServiceDestination
        :param _Description: Lane group description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _Revision: Rule content summary
Note: This field may return null, indicating that no valid values can be obtained.
        :type Revision: str
        :param _CreateTime: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _ModifyTime: Modification time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ModifyTime: str
        :param _Consistency: Rule consistency status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Consistency: str
        :param _Rules: Lane rule list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Rules: list of GovernanceLaneRule
        """
        self._Name = None
        self._ID = None
        self._TrafficEntries = None
        self._Destinations = None
        self._Description = None
        self._Revision = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Consistency = None
        self._Rules = None

    @property
    def Name(self):
        r"""lane name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ID(self):
        r"""Lane group ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def TrafficEntries(self):
        r"""Lane entry service list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of LaneTrafficEntry
        """
        return self._TrafficEntries

    @TrafficEntries.setter
    def TrafficEntries(self, TrafficEntries):
        self._TrafficEntries = TrafficEntries

    @property
    def Destinations(self):
        r"""Lane service list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of GovernanceServiceDestination
        """
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def Description(self):
        r"""Lane group description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Revision(self):
        r"""Rule content summary
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Revision

    @Revision.setter
    def Revision(self, Revision):
        self._Revision = Revision

    @property
    def CreateTime(self):
        r"""Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        r"""Modification time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Consistency(self):
        r"""Rule consistency status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Consistency

    @Consistency.setter
    def Consistency(self, Consistency):
        self._Consistency = Consistency

    @property
    def Rules(self):
        r"""Lane rule list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of GovernanceLaneRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ID = params.get("ID")
        if params.get("TrafficEntries") is not None:
            self._TrafficEntries = []
            for item in params.get("TrafficEntries"):
                obj = LaneTrafficEntry()
                obj._deserialize(item)
                self._TrafficEntries.append(obj)
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = GovernanceServiceDestination()
                obj._deserialize(item)
                self._Destinations.append(obj)
        self._Description = params.get("Description")
        self._Revision = params.get("Revision")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Consistency = params.get("Consistency")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = GovernanceLaneRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGovernanceLaneGroupsRequest(AbstractModel):
    r"""DeleteGovernanceLaneGroups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Engine Instance ID
        :type InstanceId: str
        :param _LaneGroups: Lane group rule list
        :type LaneGroups: list of DeleteGovernanceLaneGroup
        """
        self._InstanceId = None
        self._LaneGroups = None

    @property
    def InstanceId(self):
        r"""Engine Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LaneGroups(self):
        r"""Lane group rule list
        :rtype: list of DeleteGovernanceLaneGroup
        """
        return self._LaneGroups

    @LaneGroups.setter
    def LaneGroups(self, LaneGroups):
        self._LaneGroups = LaneGroups


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("LaneGroups") is not None:
            self._LaneGroups = []
            for item in params.get("LaneGroups"):
                obj = DeleteGovernanceLaneGroup()
                obj._deserialize(item)
                self._LaneGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGovernanceLaneGroupsResponse(AbstractModel):
    r"""DeleteGovernanceLaneGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the creation succeeded
        :type Result: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Whether the creation succeeded
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteNativeGatewayServerGroupRequest(AbstractModel):
    r"""DeleteNativeGatewayServerGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway instance id.
Only supports postpaid instances
        :type GatewayId: str
        :param _GroupId: gateway group id
        :type GroupId: str
        """
        self._GatewayId = None
        self._GroupId = None

    @property
    def GatewayId(self):
        r"""Gateway instance id.
Only supports postpaid instances
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        r"""gateway group id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNativeGatewayServerGroupResponse(AbstractModel):
    r"""DeleteNativeGatewayServerGroup response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Deletes messages.
        :type Result: :class:`tencentcloud.tse.v20201207.models.DeleteNativeGatewayServerGroupResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Deletes messages.
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteNativeGatewayServerGroupResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DeleteNativeGatewayServerGroupResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteNativeGatewayServerGroupResult(AbstractModel):
    r"""Delete gateway instance result

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway instance ID
        :type GatewayId: str
        :param _GroupId: Gateway group id
        :type GroupId: str
        :param _Status: deleted
        :type Status: str
        :param _TaskId: Task ID.
        :type TaskId: str
        """
        self._GatewayId = None
        self._GroupId = None
        self._Status = None
        self._TaskId = None

    @property
    def GatewayId(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        r"""Gateway group id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Status(self):
        r"""deleted
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNativeGatewayServiceSourceRequest(AbstractModel):
    r"""DeleteNativeGatewayServiceSource request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayID: Gateway instance ID
        :type GatewayID: str
        :param _SourceID: Service source instance ID
        :type SourceID: str
        """
        self._GatewayID = None
        self._SourceID = None

    @property
    def GatewayID(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayID

    @GatewayID.setter
    def GatewayID(self, GatewayID):
        self._GatewayID = GatewayID

    @property
    def SourceID(self):
        r"""Service source instance ID
        :rtype: str
        """
        return self._SourceID

    @SourceID.setter
    def SourceID(self, SourceID):
        self._SourceID = SourceID


    def _deserialize(self, params):
        self._GatewayID = params.get("GatewayID")
        self._SourceID = params.get("SourceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNativeGatewayServiceSourceResponse(AbstractModel):
    r"""DeleteNativeGatewayServiceSource response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Result
        :type Result: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Result
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteWafDomainsRequest(AbstractModel):
    r"""DeleteWafDomains request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: gateway ID
        :type GatewayId: str
        :param _Domains: WAF-protected domain name list
        :type Domains: list of str
        """
        self._GatewayId = None
        self._Domains = None

    @property
    def GatewayId(self):
        r"""gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Domains(self):
        r"""WAF-protected domain name list
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWafDomainsResponse(AbstractModel):
    r"""DeleteWafDomains response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAutoScalerResourceStrategiesRequest(AbstractModel):
    r"""DescribeAutoScalerResourceStrategies request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway instance ID
        :type GatewayId: str
        :param _StrategyId: Policy ID
        :type StrategyId: str
        """
        self._GatewayId = None
        self._StrategyId = None

    @property
    def GatewayId(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def StrategyId(self):
        r"""Policy ID
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoScalerResourceStrategiesResponse(AbstractModel):
    r"""DescribeAutoScalerResourceStrategies response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Get the response result of the auto scaling policy list for the Cloud Native API gateway instance.
        :type Result: :class:`tencentcloud.tse.v20201207.models.ListCloudNativeAPIGatewayStrategyResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Get the response result of the auto scaling policy list for the Cloud Native API gateway instance.
        :rtype: :class:`tencentcloud.tse.v20201207.models.ListCloudNativeAPIGatewayStrategyResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ListCloudNativeAPIGatewayStrategyResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeAutoScalerResourceStrategyBindingGroupsRequest(AbstractModel):
    r"""DescribeAutoScalerResourceStrategyBindingGroups request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway instance ID
        :type GatewayId: str
        :param _StrategyId: Policy ID
        :type StrategyId: str
        :param _Offset: Query offset
        :type Offset: int
        :param _Limit: Query Quantity Limit
        :type Limit: int
        """
        self._GatewayId = None
        self._StrategyId = None
        self._Offset = None
        self._Limit = None

    @property
    def GatewayId(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def StrategyId(self):
        r"""Policy ID
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def Offset(self):
        r"""Query offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Query Quantity Limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._StrategyId = params.get("StrategyId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoScalerResourceStrategyBindingGroupsResponse(AbstractModel):
    r"""DescribeAutoScalerResourceStrategyBindingGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Cloud Native API gateway instance policy binding gateway grouping list response result
        :type Result: :class:`tencentcloud.tse.v20201207.models.ListCloudNativeAPIGatewayStrategyBindingGroupInfoResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Cloud Native API gateway instance policy binding gateway grouping list response result
        :rtype: :class:`tencentcloud.tse.v20201207.models.ListCloudNativeAPIGatewayStrategyBindingGroupInfoResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ListCloudNativeAPIGatewayStrategyBindingGroupInfoResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayCORSRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayCORS request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: gateway ID
        :type GatewayId: str
        :param _SourceType: Resource type bound by the cross-origin plug-in: route|service
        :type SourceType: str
        :param _SourceId: id of the route or services
        :type SourceId: str
        """
        self._GatewayId = None
        self._SourceType = None
        self._SourceId = None

    @property
    def GatewayId(self):
        r"""gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def SourceType(self):
        r"""Resource type bound by the cross-origin plug-in: route|service
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceId(self):
        r"""id of the route or services
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._SourceType = params.get("SourceType")
        self._SourceId = params.get("SourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayCORSResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayCORS response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Output parameters
Note: This field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribeKongCORSResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Output parameters
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeKongCORSResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeKongCORSResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayCanaryRulesRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayCanaryRules request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _ServiceId: service ID
        :type ServiceId: str
        :param _RuleType: Grayscale rule type Standard | Lane
        :type RuleType: str
        :param _Limit: Number of tables in the list
        :type Limit: int
        :param _Offset: List offset
        :type Offset: int
        """
        self._GatewayId = None
        self._ServiceId = None
        self._RuleType = None
        self._Limit = None
        self._Offset = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServiceId(self):
        r"""service ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def RuleType(self):
        r"""Grayscale rule type Standard | Lane
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def Limit(self):
        r"""Number of tables in the list
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""List offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServiceId = params.get("ServiceId")
        self._RuleType = params.get("RuleType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayCanaryRulesResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayCanaryRules response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Grayscale rule list.
        :type Result: :class:`tencentcloud.tse.v20201207.models.CloudAPIGatewayCanaryRuleList`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Grayscale rule list.
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudAPIGatewayCanaryRuleList`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CloudAPIGatewayCanaryRuleList()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayCertificateDetailsRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayCertificateDetails request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _Id: Certificate ID
        :type Id: str
        """
        self._GatewayId = None
        self._Id = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Id(self):
        r"""Certificate ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayCertificateDetailsResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayCertificateDetails response structure.

    """

    def __init__(self):
        r"""
        :param _Result: None.
        :type Result: :class:`tencentcloud.tse.v20201207.models.KongCertificate`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""None.
        :rtype: :class:`tencentcloud.tse.v20201207.models.KongCertificate`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = KongCertificate()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayCertificatesRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayCertificates request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: gateway ID
        :type GatewayId: str
        :param _Limit: Number of tables in the list
        :type Limit: int
        :param _Offset: List offset
        :type Offset: int
        :param _Filters: Filter criteria. Multiple filter conditions are in an AND relationship with each other. Support BindDomain and Name.
        :type Filters: list of ListFilter
        """
        self._GatewayId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def GatewayId(self):
        r"""gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Limit(self):
        r"""Number of tables in the list
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""List offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""Filter criteria. Multiple filter conditions are in an AND relationship with each other. Support BindDomain and Name.
        :rtype: list of ListFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ListFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayCertificatesResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayCertificates response structure.

    """

    def __init__(self):
        r"""
        :param _Result: None.
        :type Result: :class:`tencentcloud.tse.v20201207.models.KongCertificatesList`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""None.
        :rtype: :class:`tencentcloud.tse.v20201207.models.KongCertificatesList`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = KongCertificatesList()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayConfigRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayConfig request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud Native API gateway instance ID.
        :type GatewayId: str
        :param _GroupId: group id. Default group if left blank.
        :type GroupId: str
        """
        self._GatewayId = None
        self._GroupId = None

    @property
    def GatewayId(self):
        r"""Cloud Native API gateway instance ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        r"""group id. Default group if left blank.
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayConfigResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Retrieve the response result of the cloud native API gateway.
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayConfigResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Retrieve the response result of the cloud native API gateway.
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayConfigResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeCloudNativeAPIGatewayConfigResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayConfigResult(AbstractModel):
    r"""Retrieve the configuration result of the cloud native API gateway instance network.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway Instance ID
        :type GatewayId: str
        :param _ConfigList: Grouped network configuration list.
        :type ConfigList: list of CloudNativeAPIGatewayConfig
        :param _GroupSubnetId: Grouped subnet info
        :type GroupSubnetId: str
        :param _GroupVpcId: Grouped VPC info
        :type GroupVpcId: str
        :param _GroupId: group ID
        :type GroupId: str
        """
        self._GatewayId = None
        self._ConfigList = None
        self._GroupSubnetId = None
        self._GroupVpcId = None
        self._GroupId = None

    @property
    def GatewayId(self):
        r"""Gateway Instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ConfigList(self):
        r"""Grouped network configuration list.
        :rtype: list of CloudNativeAPIGatewayConfig
        """
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def GroupSubnetId(self):
        r"""Grouped subnet info
        :rtype: str
        """
        return self._GroupSubnetId

    @GroupSubnetId.setter
    def GroupSubnetId(self, GroupSubnetId):
        self._GroupSubnetId = GroupSubnetId

    @property
    def GroupVpcId(self):
        r"""Grouped VPC info
        :rtype: str
        """
        return self._GroupVpcId

    @GroupVpcId.setter
    def GroupVpcId(self, GroupVpcId):
        self._GroupVpcId = GroupVpcId

    @property
    def GroupId(self):
        r"""group ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = CloudNativeAPIGatewayConfig()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._GroupSubnetId = params.get("GroupSubnetId")
        self._GroupVpcId = params.get("GroupVpcId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayInfoByIpRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayInfoByIp request structure.

    """

    def __init__(self):
        r"""
        :param _PublicNetworkIP: Public ip address of the cloud-native gateway
        :type PublicNetworkIP: str
        """
        self._PublicNetworkIP = None

    @property
    def PublicNetworkIP(self):
        r"""Public ip address of the cloud-native gateway
        :rtype: str
        """
        return self._PublicNetworkIP

    @PublicNetworkIP.setter
    def PublicNetworkIP(self, PublicNetworkIP):
        self._PublicNetworkIP = PublicNetworkIP


    def _deserialize(self, params):
        self._PublicNetworkIP = params.get("PublicNetworkIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayInfoByIpResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayInfoByIp response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Output parameters
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribeInstanceInfoByIpResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Output parameters
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeInstanceInfoByIpResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeInstanceInfoByIpResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayNodesRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayNodes request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud Native API gateway instance ID.
        :type GatewayId: str
        :param _GroupId: Instance Group ID
        :type GroupId: str
        :param _Limit: Number of paginated items
        :type Limit: int
        :param _Offset: Start acquisition from page number
        :type Offset: int
        """
        self._GatewayId = None
        self._GroupId = None
        self._Limit = None
        self._Offset = None

    @property
    def GatewayId(self):
        r"""Cloud Native API gateway instance ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        r"""Instance Group ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Limit(self):
        r"""Number of paginated items
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Start acquisition from page number
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayNodesResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayNodes response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Retrieve cloud-native gateway node list results.
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayNodesResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Retrieve cloud-native gateway node list results.
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayNodesResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeCloudNativeAPIGatewayNodesResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayNodesResult(AbstractModel):
    r"""Obtain gateway node info

    """

    def __init__(self):
        r"""
        :param _TotalCount: Retrieve the cloud native API gateway node list response result.
        :type TotalCount: int
        :param _NodeList: Cloud native API gateway node list.
        :type NodeList: list of CloudNativeAPIGatewayNode
        """
        self._TotalCount = None
        self._NodeList = None

    @property
    def TotalCount(self):
        r"""Retrieve the cloud native API gateway node list response result.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NodeList(self):
        r"""Cloud native API gateway node list.
        :rtype: list of CloudNativeAPIGatewayNode
        """
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("NodeList") is not None:
            self._NodeList = []
            for item in params.get("NodeList"):
                obj = CloudNativeAPIGatewayNode()
                obj._deserialize(item)
                self._NodeList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayPortsRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayPorts request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud native API gateway instance ID
        :type GatewayId: str
        """
        self._GatewayId = None

    @property
    def GatewayId(self):
        r"""Cloud native API gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayPortsResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayPorts response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Cloud Native API gateway instance protocol port list response result
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribeGatewayInstancePortResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Cloud Native API gateway instance protocol port list response result
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeGatewayInstancePortResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeGatewayInstancePortResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGateway request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud Native API gateway instance ID
        :type GatewayId: str
        """
        self._GatewayId = None

    @property
    def GatewayId(self):
        r"""Cloud Native API gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGateway response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Retrieve the response result of the Cloud Native API gateway basic information.
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Retrieve the response result of the Cloud Native API gateway basic information.
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeCloudNativeAPIGatewayResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayResult(AbstractModel):
    r"""Retrieve the response result of the Cloud Native API gateway basic information.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud Native API Gateway ID.
        :type GatewayId: str
        :param _Status: Cloud native API gateway status.
        :type Status: str
        :param _Name: Cloud native API gateway name.
        :type Name: str
        :param _Type: Cloud native API gateway type.
        :type Type: str
        :param _GatewayVersion: Instance version:
- 2.4.1
- 2.5.1
        :type GatewayVersion: str
        :param _NodeConfig: Cloud native API gateway node information.
        :type NodeConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        :param _VpcConfig: Cloud native API gateway vpc configuration.
        :type VpcConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayVpcConfig`
        :param _Description: Cloud native API gateway description.
        :type Description: str
        :param _CreateTime: Creation time of the cloud native API gateway.
        :type CreateTime: str
        :param _Tags: Tag information of the instance
        :type Tags: list of InstanceTagInfo
        :param _EnableCls: Is cls log enabled?
        :type EnableCls: bool
        :param _TradeType: Payment mode. 0 indicates postpaid, and 1 indicates prepaid.
        :type TradeType: int
        :param _FeatureVersion: Instance version. Currently supported: development edition, standard version, and professional version [TRIAL, STANDARD, PROFESSIONAL].
        :type FeatureVersion: str
        :param _InternetMaxBandwidthOut: Public network outbound traffic bandwidth, [1,2048]Mbps
        :type InternetMaxBandwidthOut: int
        :param _AutoRenewFlag: Auto-renewal flag. 0 means the default state (not set by the user, that is, the initial state).
1 means auto-renew, 2 means no automatic renewal (set by the user). If the business has no renewal concept or no need for auto-renewal, set it to 0.
        :type AutoRenewFlag: int
        :param _CurDeadline: Expiry time, used when prepaid
        :type CurDeadline: str
        :param _IsolateTime: Isolation time. Used when an instance is isolated.
        :type IsolateTime: str
        :param _EnableInternet: Is client public network enabled?
        :type EnableInternet: bool
        :param _EngineRegion: Actual regional information of the instance
        :type EngineRegion: str
        :param _IngressClassName: Ingress class name
        :type IngressClassName: str
        :param _InternetPayMode: Public network billing method. Selectable values: BANDWIDTH | TRAFFIC, representing billing by bandwidth and by traffic.
        :type InternetPayMode: str
        :param _GatewayMinorVersion: Cloud Native API Gateway minor version number
        :type GatewayMinorVersion: str
        :param _InstancePort: Ports monitored by the instance
        :type InstancePort: :class:`tencentcloud.tse.v20201207.models.InstancePort`
        :param _LoadBalancerType: Public network CLB default type
        :type LoadBalancerType: str
        :param _PublicIpAddresses: Public IP address list
        :type PublicIpAddresses: list of str
        :param _DeleteProtect: Whether to enable deletion protection
        :type DeleteProtect: bool
        :param _AvailableVersions: Version number that can be upgraded
Note: This field may return null, indicating that no valid values can be obtained.
        :type AvailableVersions: list of str
        :param _AvailableUpgradeVersions: Version list for gateway upgrade
        :type AvailableUpgradeVersions: list of str
        :param _AvailableUpgrade: Whether to prompt for upgrade
        :type AvailableUpgrade: bool
        :param _AvailableRollbackVersion: Rollback version
        :type AvailableRollbackVersion: str
        """
        self._GatewayId = None
        self._Status = None
        self._Name = None
        self._Type = None
        self._GatewayVersion = None
        self._NodeConfig = None
        self._VpcConfig = None
        self._Description = None
        self._CreateTime = None
        self._Tags = None
        self._EnableCls = None
        self._TradeType = None
        self._FeatureVersion = None
        self._InternetMaxBandwidthOut = None
        self._AutoRenewFlag = None
        self._CurDeadline = None
        self._IsolateTime = None
        self._EnableInternet = None
        self._EngineRegion = None
        self._IngressClassName = None
        self._InternetPayMode = None
        self._GatewayMinorVersion = None
        self._InstancePort = None
        self._LoadBalancerType = None
        self._PublicIpAddresses = None
        self._DeleteProtect = None
        self._AvailableVersions = None
        self._AvailableUpgradeVersions = None
        self._AvailableUpgrade = None
        self._AvailableRollbackVersion = None

    @property
    def GatewayId(self):
        r"""Cloud Native API Gateway ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Status(self):
        r"""Cloud native API gateway status.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Name(self):
        r"""Cloud native API gateway name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""Cloud native API gateway type.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def GatewayVersion(self):
        r"""Instance version:
- 2.4.1
- 2.5.1
        :rtype: str
        """
        return self._GatewayVersion

    @GatewayVersion.setter
    def GatewayVersion(self, GatewayVersion):
        self._GatewayVersion = GatewayVersion

    @property
    def NodeConfig(self):
        r"""Cloud native API gateway node information.
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        """
        return self._NodeConfig

    @NodeConfig.setter
    def NodeConfig(self, NodeConfig):
        self._NodeConfig = NodeConfig

    @property
    def VpcConfig(self):
        r"""Cloud native API gateway vpc configuration.
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayVpcConfig`
        """
        return self._VpcConfig

    @VpcConfig.setter
    def VpcConfig(self, VpcConfig):
        self._VpcConfig = VpcConfig

    @property
    def Description(self):
        r"""Cloud native API gateway description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        r"""Creation time of the cloud native API gateway.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Tags(self):
        r"""Tag information of the instance
        :rtype: list of InstanceTagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def EnableCls(self):
        r"""Is cls log enabled?
        :rtype: bool
        """
        return self._EnableCls

    @EnableCls.setter
    def EnableCls(self, EnableCls):
        self._EnableCls = EnableCls

    @property
    def TradeType(self):
        r"""Payment mode. 0 indicates postpaid, and 1 indicates prepaid.
        :rtype: int
        """
        return self._TradeType

    @TradeType.setter
    def TradeType(self, TradeType):
        self._TradeType = TradeType

    @property
    def FeatureVersion(self):
        r"""Instance version. Currently supported: development edition, standard version, and professional version [TRIAL, STANDARD, PROFESSIONAL].
        :rtype: str
        """
        return self._FeatureVersion

    @FeatureVersion.setter
    def FeatureVersion(self, FeatureVersion):
        self._FeatureVersion = FeatureVersion

    @property
    def InternetMaxBandwidthOut(self):
        r"""Public network outbound traffic bandwidth, [1,2048]Mbps
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def AutoRenewFlag(self):
        r"""Auto-renewal flag. 0 means the default state (not set by the user, that is, the initial state).
1 means auto-renew, 2 means no automatic renewal (set by the user). If the business has no renewal concept or no need for auto-renewal, set it to 0.
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def CurDeadline(self):
        r"""Expiry time, used when prepaid
        :rtype: str
        """
        return self._CurDeadline

    @CurDeadline.setter
    def CurDeadline(self, CurDeadline):
        self._CurDeadline = CurDeadline

    @property
    def IsolateTime(self):
        r"""Isolation time. Used when an instance is isolated.
        :rtype: str
        """
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def EnableInternet(self):
        r"""Is client public network enabled?
        :rtype: bool
        """
        return self._EnableInternet

    @EnableInternet.setter
    def EnableInternet(self, EnableInternet):
        self._EnableInternet = EnableInternet

    @property
    def EngineRegion(self):
        r"""Actual regional information of the instance
        :rtype: str
        """
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion

    @property
    def IngressClassName(self):
        r"""Ingress class name
        :rtype: str
        """
        return self._IngressClassName

    @IngressClassName.setter
    def IngressClassName(self, IngressClassName):
        self._IngressClassName = IngressClassName

    @property
    def InternetPayMode(self):
        r"""Public network billing method. Selectable values: BANDWIDTH | TRAFFIC, representing billing by bandwidth and by traffic.
        :rtype: str
        """
        return self._InternetPayMode

    @InternetPayMode.setter
    def InternetPayMode(self, InternetPayMode):
        self._InternetPayMode = InternetPayMode

    @property
    def GatewayMinorVersion(self):
        r"""Cloud Native API Gateway minor version number
        :rtype: str
        """
        return self._GatewayMinorVersion

    @GatewayMinorVersion.setter
    def GatewayMinorVersion(self, GatewayMinorVersion):
        self._GatewayMinorVersion = GatewayMinorVersion

    @property
    def InstancePort(self):
        r"""Ports monitored by the instance
        :rtype: :class:`tencentcloud.tse.v20201207.models.InstancePort`
        """
        return self._InstancePort

    @InstancePort.setter
    def InstancePort(self, InstancePort):
        self._InstancePort = InstancePort

    @property
    def LoadBalancerType(self):
        r"""Public network CLB default type
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def PublicIpAddresses(self):
        r"""Public IP address list
        :rtype: list of str
        """
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def DeleteProtect(self):
        r"""Whether to enable deletion protection
        :rtype: bool
        """
        return self._DeleteProtect

    @DeleteProtect.setter
    def DeleteProtect(self, DeleteProtect):
        self._DeleteProtect = DeleteProtect

    @property
    def AvailableVersions(self):
        r"""Version number that can be upgraded
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AvailableVersions

    @AvailableVersions.setter
    def AvailableVersions(self, AvailableVersions):
        self._AvailableVersions = AvailableVersions

    @property
    def AvailableUpgradeVersions(self):
        r"""Version list for gateway upgrade
        :rtype: list of str
        """
        return self._AvailableUpgradeVersions

    @AvailableUpgradeVersions.setter
    def AvailableUpgradeVersions(self, AvailableUpgradeVersions):
        self._AvailableUpgradeVersions = AvailableUpgradeVersions

    @property
    def AvailableUpgrade(self):
        r"""Whether to prompt for upgrade
        :rtype: bool
        """
        return self._AvailableUpgrade

    @AvailableUpgrade.setter
    def AvailableUpgrade(self, AvailableUpgrade):
        self._AvailableUpgrade = AvailableUpgrade

    @property
    def AvailableRollbackVersion(self):
        r"""Rollback version
        :rtype: str
        """
        return self._AvailableRollbackVersion

    @AvailableRollbackVersion.setter
    def AvailableRollbackVersion(self, AvailableRollbackVersion):
        self._AvailableRollbackVersion = AvailableRollbackVersion


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Status = params.get("Status")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._GatewayVersion = params.get("GatewayVersion")
        if params.get("NodeConfig") is not None:
            self._NodeConfig = CloudNativeAPIGatewayNodeConfig()
            self._NodeConfig._deserialize(params.get("NodeConfig"))
        if params.get("VpcConfig") is not None:
            self._VpcConfig = CloudNativeAPIGatewayVpcConfig()
            self._VpcConfig._deserialize(params.get("VpcConfig"))
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = InstanceTagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._EnableCls = params.get("EnableCls")
        self._TradeType = params.get("TradeType")
        self._FeatureVersion = params.get("FeatureVersion")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._CurDeadline = params.get("CurDeadline")
        self._IsolateTime = params.get("IsolateTime")
        self._EnableInternet = params.get("EnableInternet")
        self._EngineRegion = params.get("EngineRegion")
        self._IngressClassName = params.get("IngressClassName")
        self._InternetPayMode = params.get("InternetPayMode")
        self._GatewayMinorVersion = params.get("GatewayMinorVersion")
        if params.get("InstancePort") is not None:
            self._InstancePort = InstancePort()
            self._InstancePort._deserialize(params.get("InstancePort"))
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._DeleteProtect = params.get("DeleteProtect")
        self._AvailableVersions = params.get("AvailableVersions")
        self._AvailableUpgradeVersions = params.get("AvailableUpgradeVersions")
        self._AvailableUpgrade = params.get("AvailableUpgrade")
        self._AvailableRollbackVersion = params.get("AvailableRollbackVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayRouteRateLimitRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayRouteRateLimit request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _Id: Route Id or routing name.
"Unnamed" is not supported.
        :type Id: str
        """
        self._GatewayId = None
        self._Id = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Id(self):
        r"""Route Id or routing name.
"Unnamed" is not supported.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayRouteRateLimitResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayRouteRateLimit response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Retrieve the cloud-native gateway traffic throttling plugin (route)
        :type Result: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Retrieve the cloud-native gateway traffic throttling plugin (route)
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CloudNativeAPIGatewayRateLimitDetail()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayRoutesRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayRoutes request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _Limit: Pagination query limit count [0,1000], default value 0
        :type Limit: int
        :param _Offset: Page offset amount for pagination. Default value: 0
        :type Offset: int
        :param _ServiceName: Service name, exact match
        :type ServiceName: str
        :param _RouteName: Route name, exact match
        :type RouteName: str
        :param _Filters: Filter conditions. Multiple filter conditions have an AND relationship with each other, supporting name, path, host, method, service, and protocol.
        :type Filters: list of ListFilter
        """
        self._GatewayId = None
        self._Limit = None
        self._Offset = None
        self._ServiceName = None
        self._RouteName = None
        self._Filters = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Limit(self):
        r"""Pagination query limit count [0,1000], default value 0
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Page offset amount for pagination. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ServiceName(self):
        r"""Service name, exact match
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def RouteName(self):
        r"""Route name, exact match
        :rtype: str
        """
        return self._RouteName

    @RouteName.setter
    def RouteName(self, RouteName):
        self._RouteName = RouteName

    @property
    def Filters(self):
        r"""Filter conditions. Multiple filter conditions have an AND relationship with each other, supporting name, path, host, method, service, and protocol.
        :rtype: list of ListFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ServiceName = params.get("ServiceName")
        self._RouteName = params.get("RouteName")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ListFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayRoutesResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayRoutes response structure.

    """

    def __init__(self):
        r"""
        :param _Result: None.
        :type Result: :class:`tencentcloud.tse.v20201207.models.KongServiceRouteList`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""None.
        :rtype: :class:`tencentcloud.tse.v20201207.models.KongServiceRouteList`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = KongServiceRouteList()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayServiceRateLimitRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayServiceRateLimit request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _Name: Service name or service ID.
        :type Name: str
        """
        self._GatewayId = None
        self._Name = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""Service name or service ID.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayServiceRateLimitResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayServiceRateLimit response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Query the cloud-native gateway traffic throttling plugin (service)
        :type Result: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Query the cloud-native gateway traffic throttling plugin (service)
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CloudNativeAPIGatewayRateLimitDetail()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayServicesLightRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayServicesLight request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _Limit: Number of tables in the list
        :type Limit: int
        :param _Offset: List offset
        :type Offset: int
        :param _Filters: Filter conditions. Multiple filter conditions have an AND relationship with each other, supporting id, name, and upstreamType.
        :type Filters: list of ListFilter
        """
        self._GatewayId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Limit(self):
        r"""Number of tables in the list
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""List offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""Filter conditions. Multiple filter conditions have an AND relationship with each other, supporting id, name, and upstreamType.
        :rtype: list of ListFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ListFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayServicesLightResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayServicesLight response structure.

    """

    def __init__(self):
        r"""
        :param _Result: None.
        :type Result: :class:`tencentcloud.tse.v20201207.models.GatewayServices`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""None.
        :rtype: :class:`tencentcloud.tse.v20201207.models.GatewayServices`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = GatewayServices()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayServicesRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayServices request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: gateway ID
        :type GatewayId: str
        :param _Limit: Number of tables in the list
        :type Limit: int
        :param _Offset: List offset
        :type Offset: int
        :param _Filters: Filter criteria. Multiple filter conditions are in an AND relationship with each other. Support name and upstreamType.
        :type Filters: list of ListFilter
        """
        self._GatewayId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def GatewayId(self):
        r"""gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Limit(self):
        r"""Number of tables in the list
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""List offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""Filter criteria. Multiple filter conditions are in an AND relationship with each other. Support name and upstreamType.
        :rtype: list of ListFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ListFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayServicesResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayServices response structure.

    """

    def __init__(self):
        r"""
        :param _Result: None.
        :type Result: :class:`tencentcloud.tse.v20201207.models.KongServices`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""None.
        :rtype: :class:`tencentcloud.tse.v20201207.models.KongServices`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = KongServices()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayUpstreamRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayUpstream request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: gateway ID
        :type GatewayId: str
        :param _ServiceName: Service name.
        :type ServiceName: str
        """
        self._GatewayId = None
        self._ServiceName = None

    @property
    def GatewayId(self):
        r"""gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServiceName(self):
        r"""Service name.
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayUpstreamResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayUpstream response structure.

    """

    def __init__(self):
        r"""
        :param _Result: None.
        :type Result: :class:`tencentcloud.tse.v20201207.models.KongUpstreamList`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""None.
        :rtype: :class:`tencentcloud.tse.v20201207.models.KongUpstreamList`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = KongUpstreamList()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewaysRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGateways request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of returned results, defaults to 20, maximum value is 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Request filter parameters support filtering by instance name, ID, and tag key value (Name, GatewayId, Tag).
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        r"""Number of returned results, defaults to 20, maximum value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""Request filter parameters support filtering by instance name, ID, and tag key value (Name, GatewayId, Tag).
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewaysResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGateways response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Retrieve the response result of the cloud native API gateway instance list.
        :type Result: :class:`tencentcloud.tse.v20201207.models.ListCloudNativeAPIGatewayResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Retrieve the response result of the cloud native API gateway instance list.
        :rtype: :class:`tencentcloud.tse.v20201207.models.ListCloudNativeAPIGatewayResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ListCloudNativeAPIGatewayResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeGatewayInstancePortResult(AbstractModel):
    r"""Retrieve the response result of the protocol port list for a cloud-native API gateway instance

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud Native API Gateway ID
        :type GatewayId: str
        :param _GatewayInstancePortList: Gateway instance protocol port list
        :type GatewayInstancePortList: list of GatewayInstanceSchemeAndPorts
        """
        self._GatewayId = None
        self._GatewayInstancePortList = None

    @property
    def GatewayId(self):
        r"""Cloud Native API Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GatewayInstancePortList(self):
        r"""Gateway instance protocol port list
        :rtype: list of GatewayInstanceSchemeAndPorts
        """
        return self._GatewayInstancePortList

    @GatewayInstancePortList.setter
    def GatewayInstancePortList(self, GatewayInstancePortList):
        self._GatewayInstancePortList = GatewayInstancePortList


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        if params.get("GatewayInstancePortList") is not None:
            self._GatewayInstancePortList = []
            for item in params.get("GatewayInstancePortList"):
                obj = GatewayInstanceSchemeAndPorts()
                obj._deserialize(item)
                self._GatewayInstancePortList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGovernanceLaneGroupsRequest(AbstractModel):
    r"""DescribeGovernanceLaneGroups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Engine Instance ID
        :type InstanceId: str
        :param _Offset: Pagination query offset.
        :type Offset: int
        :param _Limit: Number of items per page.
        :type Limit: int
        :param _Name: swimlane name
        :type Name: str
        :param _GroupID: Lane ID
        :type GroupID: str
        :param _Brief: Whether to display the lane rule list
        :type Brief: bool
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._Name = None
        self._GroupID = None
        self._Brief = None

    @property
    def InstanceId(self):
        r"""Engine Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        r"""Pagination query offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of items per page.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Name(self):
        r"""swimlane name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def GroupID(self):
        r"""Lane ID
        :rtype: str
        """
        return self._GroupID

    @GroupID.setter
    def GroupID(self, GroupID):
        self._GroupID = GroupID

    @property
    def Brief(self):
        r"""Whether to display the lane rule list
        :rtype: bool
        """
        return self._Brief

    @Brief.setter
    def Brief(self, Brief):
        self._Brief = Brief


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Name = params.get("Name")
        self._GroupID = params.get("GroupID")
        self._Brief = params.get("Brief")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGovernanceLaneGroupsResponse(AbstractModel):
    r"""DescribeGovernanceLaneGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number.
        :type Total: int
        :param _LaneGroups: Lane rule list
        :type LaneGroups: list of GovernanceLaneGroup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._LaneGroups = None
        self._RequestId = None

    @property
    def Total(self):
        r"""Total number.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def LaneGroups(self):
        r"""Lane rule list
        :rtype: list of GovernanceLaneGroup
        """
        return self._LaneGroups

    @LaneGroups.setter
    def LaneGroups(self, LaneGroups):
        self._LaneGroups = LaneGroups

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("LaneGroups") is not None:
            self._LaneGroups = []
            for item in params.get("LaneGroups"):
                obj = GovernanceLaneGroup()
                obj._deserialize(item)
                self._LaneGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceInfoByIpResult(AbstractModel):
    r"""Query cloud native gateway instance info based on public network IP

    """

    def __init__(self):
        r"""
        :param _GatewayId: Instance ID.
        :type GatewayId: str
        :param _GroupId: Group ID
        :type GroupId: str
        """
        self._GatewayId = None
        self._GroupId = None

    @property
    def GatewayId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        r"""Group ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKongCORSResult(AbstractModel):
    r"""Query cross-origin configuration output parameters

    """

    def __init__(self):
        r"""
        :param _SourceType: Resource type.
        :type SourceType: str
        :param _SourceId: Resource ID
        :type SourceId: str
        :param _Enabled: enabled or not
        :type Enabled: bool
        :param _Origins: Cross-origin Origins
        :type Origins: list of str
        :param _Headers: Cross-Origin Headers
        :type Headers: list of str
        :param _Methods: Cross-origin Methods
        :type Methods: list of str
        :param _ExposedHeaders: Cross-Origin ExposedHeaders
        :type ExposedHeaders: list of str
        :param _MaxAge: Cache time of cross-origin OPTIONS request
        :type MaxAge: int
        :param _Credentials: Whether cross-origin access requests are allowed to carry identity information
        :type Credentials: bool
        :param _PreFlightContinue: Whether to forward cross-origin access requests to the backend
        :type PreFlightContinue: bool
        """
        self._SourceType = None
        self._SourceId = None
        self._Enabled = None
        self._Origins = None
        self._Headers = None
        self._Methods = None
        self._ExposedHeaders = None
        self._MaxAge = None
        self._Credentials = None
        self._PreFlightContinue = None

    @property
    def SourceType(self):
        r"""Resource type.
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceId(self):
        r"""Resource ID
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def Enabled(self):
        r"""enabled or not
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Origins(self):
        r"""Cross-origin Origins
        :rtype: list of str
        """
        return self._Origins

    @Origins.setter
    def Origins(self, Origins):
        self._Origins = Origins

    @property
    def Headers(self):
        r"""Cross-Origin Headers
        :rtype: list of str
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def Methods(self):
        r"""Cross-origin Methods
        :rtype: list of str
        """
        return self._Methods

    @Methods.setter
    def Methods(self, Methods):
        self._Methods = Methods

    @property
    def ExposedHeaders(self):
        r"""Cross-Origin ExposedHeaders
        :rtype: list of str
        """
        return self._ExposedHeaders

    @ExposedHeaders.setter
    def ExposedHeaders(self, ExposedHeaders):
        self._ExposedHeaders = ExposedHeaders

    @property
    def MaxAge(self):
        r"""Cache time of cross-origin OPTIONS request
        :rtype: int
        """
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def Credentials(self):
        r"""Whether cross-origin access requests are allowed to carry identity information
        :rtype: bool
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def PreFlightContinue(self):
        r"""Whether to forward cross-origin access requests to the backend
        :rtype: bool
        """
        return self._PreFlightContinue

    @PreFlightContinue.setter
    def PreFlightContinue(self, PreFlightContinue):
        self._PreFlightContinue = PreFlightContinue


    def _deserialize(self, params):
        self._SourceType = params.get("SourceType")
        self._SourceId = params.get("SourceId")
        self._Enabled = params.get("Enabled")
        self._Origins = params.get("Origins")
        self._Headers = params.get("Headers")
        self._Methods = params.get("Methods")
        self._ExposedHeaders = params.get("ExposedHeaders")
        self._MaxAge = params.get("MaxAge")
        self._Credentials = params.get("Credentials")
        self._PreFlightContinue = params.get("PreFlightContinue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNativeGatewayServerGroupsRequest(AbstractModel):
    r"""DescribeNativeGatewayServerGroups request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud native API gateway instance ID.
        :type GatewayId: str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results, defaults to 20.
        :type Limit: int
        :param _Filters: Filter parameters, based on group name and group ID (Name, GroupId) for filter criteria.
        :type Filters: list of Filter
        """
        self._GatewayId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def GatewayId(self):
        r"""Cloud native API gateway instance ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Offset(self):
        r"""Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of returned results, defaults to 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""Filter parameters, based on group name and group ID (Name, GroupId) for filter criteria.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNativeGatewayServerGroupsResponse(AbstractModel):
    r"""DescribeNativeGatewayServerGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Group list info
        :type Result: :class:`tencentcloud.tse.v20201207.models.NativeGatewayServerGroups`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Group list info
        :rtype: :class:`tencentcloud.tse.v20201207.models.NativeGatewayServerGroups`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = NativeGatewayServerGroups()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeNativeGatewayServiceSourcesRequest(AbstractModel):
    r"""DescribeNativeGatewayServiceSources request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayID: Gateway instance ID
        :type GatewayID: str
        :param _Limit: Items per page. Maximum value: 100.
        :type Limit: int
        :param _Offset: Pagination offset.
        :type Offset: int
        :param _SourceID: Service Source ID
        :type SourceID: str
        :param _SourceName: Service Source Instance Name, Fuzzy Search
        :type SourceName: str
        :param _SourceTypes: Microservice engine type: TSE-Nacos｜TSE-Consul｜TSE-PolarisMesh｜Customer-Nacos｜Customer-Consul｜Customer-PolarisMesh
        :type SourceTypes: list of str
        :param _OrderField: Sorting field data type, currently only support SourceName
        :type OrderField: str
        :param _OrderType: Sorting type, AES/DESC
        :type OrderType: str
        """
        self._GatewayID = None
        self._Limit = None
        self._Offset = None
        self._SourceID = None
        self._SourceName = None
        self._SourceTypes = None
        self._OrderField = None
        self._OrderType = None

    @property
    def GatewayID(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayID

    @GatewayID.setter
    def GatewayID(self, GatewayID):
        self._GatewayID = GatewayID

    @property
    def Limit(self):
        r"""Items per page. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Pagination offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SourceID(self):
        r"""Service Source ID
        :rtype: str
        """
        return self._SourceID

    @SourceID.setter
    def SourceID(self, SourceID):
        self._SourceID = SourceID

    @property
    def SourceName(self):
        r"""Service Source Instance Name, Fuzzy Search
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def SourceTypes(self):
        r"""Microservice engine type: TSE-Nacos｜TSE-Consul｜TSE-PolarisMesh｜Customer-Nacos｜Customer-Consul｜Customer-PolarisMesh
        :rtype: list of str
        """
        return self._SourceTypes

    @SourceTypes.setter
    def SourceTypes(self, SourceTypes):
        self._SourceTypes = SourceTypes

    @property
    def OrderField(self):
        r"""Sorting field data type, currently only support SourceName
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def OrderType(self):
        r"""Sorting type, AES/DESC
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._GatewayID = params.get("GatewayID")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SourceID = params.get("SourceID")
        self._SourceName = params.get("SourceName")
        self._SourceTypes = params.get("SourceTypes")
        self._OrderField = params.get("OrderField")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNativeGatewayServiceSourcesResponse(AbstractModel):
    r"""DescribeNativeGatewayServiceSources response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total instances
        :type Total: int
        :param _List: Service source instance list
        :type List: list of NativeGatewayServiceSourceItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        r"""Total instances
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        r"""Service source instance list
        :rtype: list of NativeGatewayServiceSourceItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = NativeGatewayServiceSourceItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOneCloudNativeAPIGatewayServiceRequest(AbstractModel):
    r"""DescribeOneCloudNativeAPIGatewayService request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: gateway ID
        :type GatewayId: str
        :param _Name: Service name or service ID
        :type Name: str
        """
        self._GatewayId = None
        self._Name = None

    @property
    def GatewayId(self):
        r"""gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""Service name or service ID
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOneCloudNativeAPIGatewayServiceResponse(AbstractModel):
    r"""DescribeOneCloudNativeAPIGatewayService response structure.

    """

    def __init__(self):
        r"""
        :param _Result: None.
        :type Result: :class:`tencentcloud.tse.v20201207.models.KongServiceDetail`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""None.
        :rtype: :class:`tencentcloud.tse.v20201207.models.KongServiceDetail`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = KongServiceDetail()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribePublicAddressConfigRequest(AbstractModel):
    r"""DescribePublicAddressConfig request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway instance ID
        :type GatewayId: str
        :param _GroupId: Query public network information of this group. If not specified, query all public network load balance information of the instance.
        :type GroupId: str
        """
        self._GatewayId = None
        self._GroupId = None

    @property
    def GatewayId(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        r"""Query public network information of this group. If not specified, query all public network load balance information of the instance.
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicAddressConfigResponse(AbstractModel):
    r"""DescribePublicAddressConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Public IP address info
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribePublicAddressConfigResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Public IP address info
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribePublicAddressConfigResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribePublicAddressConfigResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribePublicAddressConfigResult(AbstractModel):
    r"""Retrieve the cloud native api Gateway public IP address info response result

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway instance ID
        :type GatewayId: str
        :param _ConfigList: Public IP address info
        :type ConfigList: list of PublicAddressConfig
        :param _TotalCount: Total number	
        :type TotalCount: int
        """
        self._GatewayId = None
        self._ConfigList = None
        self._TotalCount = None

    @property
    def GatewayId(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ConfigList(self):
        r"""Public IP address info
        :rtype: list of PublicAddressConfig
        """
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def TotalCount(self):
        r"""Total number	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = PublicAddressConfig()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicNetworkRequest(AbstractModel):
    r"""DescribePublicNetwork request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud native API gateway instance ID.
        :type GatewayId: str
        :param _GroupId: gateway group ID
        :type GroupId: str
        :param _NetworkId: Network ID.
        :type NetworkId: str
        """
        self._GatewayId = None
        self._GroupId = None
        self._NetworkId = None

    @property
    def GatewayId(self):
        r"""Cloud native API gateway instance ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        r"""gateway group ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def NetworkId(self):
        r"""Network ID.
        :rtype: str
        """
        return self._NetworkId

    @NetworkId.setter
    def NetworkId(self, NetworkId):
        self._NetworkId = NetworkId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._NetworkId = params.get("NetworkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicNetworkResponse(AbstractModel):
    r"""DescribePublicNetwork response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Retrieve the cloud native API gateway public network detailed information response result.
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribePublicNetworkResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Retrieve the cloud native API gateway public network detailed information response result.
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribePublicNetworkResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribePublicNetworkResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribePublicNetworkResult(AbstractModel):
    r"""Query client public network information

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway instance ID
        :type GatewayId: str
        :param _GroupId: gateway group ID
        :type GroupId: str
        :param _PublicNetwork: Client public network information
        :type PublicNetwork: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayConfig`
        """
        self._GatewayId = None
        self._GroupId = None
        self._PublicNetwork = None

    @property
    def GatewayId(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        r"""gateway group ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PublicNetwork(self):
        r"""Client public network information
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayConfig`
        """
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        if params.get("PublicNetwork") is not None:
            self._PublicNetwork = CloudNativeAPIGatewayConfig()
            self._PublicNetwork._deserialize(params.get("PublicNetwork"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpstreamHealthCheckConfigRequest(AbstractModel):
    r"""DescribeUpstreamHealthCheckConfig request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _Name: Gateway service name.
        :type Name: str
        """
        self._GatewayId = None
        self._Name = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""Gateway service name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpstreamHealthCheckConfigResponse(AbstractModel):
    r"""DescribeUpstreamHealthCheckConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Health check configuration
        :type Result: :class:`tencentcloud.tse.v20201207.models.UpstreamHealthCheckConfig`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Health check configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.UpstreamHealthCheckConfig`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UpstreamHealthCheckConfig()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeWafDomainsRequest(AbstractModel):
    r"""DescribeWafDomains request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: gateway ID
        :type GatewayId: str
        """
        self._GatewayId = None

    @property
    def GatewayId(self):
        r"""gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWafDomainsResponse(AbstractModel):
    r"""DescribeWafDomains response structure.

    """

    def __init__(self):
        r"""
        :param _Result: WAF-protected domain name
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribeWafDomainsResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""WAF-protected domain name
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeWafDomainsResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeWafDomainsResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeWafDomainsResult(AbstractModel):
    r"""Retrieve WAF-protected domain name list

    """

    def __init__(self):
        r"""
        :param _Domains: WAF-protected domain name list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domains: list of str
        """
        self._Domains = None

    @property
    def Domains(self):
        r"""WAF-protected domain name list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWafProtectionRequest(AbstractModel):
    r"""DescribeWafProtection request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: gateway ID
        :type GatewayId: str
        :param _Type: Type of protection resource.
-Global instance
-Service
-Route
-Object
        :type Type: str
        :param _TypeList: Resource type list for protection supports querying multiple types (Global, Service, Route, Object). If left empty, it defaults to querying the Global type.
        :type TypeList: list of str
        """
        self._GatewayId = None
        self._Type = None
        self._TypeList = None

    @property
    def GatewayId(self):
        r"""gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Type(self):
        warnings.warn("parameter `Type` is deprecated", DeprecationWarning) 

        r"""Type of protection resource.
-Global instance
-Service
-Route
-Object
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        warnings.warn("parameter `Type` is deprecated", DeprecationWarning) 

        self._Type = Type

    @property
    def TypeList(self):
        r"""Resource type list for protection supports querying multiple types (Global, Service, Route, Object). If left empty, it defaults to querying the Global type.
        :rtype: list of str
        """
        return self._TypeList

    @TypeList.setter
    def TypeList(self, TypeList):
        self._TypeList = TypeList


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Type = params.get("Type")
        self._TypeList = params.get("TypeList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWafProtectionResponse(AbstractModel):
    r"""DescribeWafProtection response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Protection status
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribeWafProtectionResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Protection status
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeWafProtectionResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeWafProtectionResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeWafProtectionResult(AbstractModel):
    r"""Retrieve WAF protection resource status

    """

    def __init__(self):
        r"""
        :param _GlobalStatus: Global protection status
        :type GlobalStatus: str
        :param _ServicesStatus: Protection status
        :type ServicesStatus: list of ServiceWafStatus
        :param _RouteStatus: Route protection status
        :type RouteStatus: list of RouteWafStatus
        :param _ObjectStatus: Object protection status
        :type ObjectStatus: str
        """
        self._GlobalStatus = None
        self._ServicesStatus = None
        self._RouteStatus = None
        self._ObjectStatus = None

    @property
    def GlobalStatus(self):
        r"""Global protection status
        :rtype: str
        """
        return self._GlobalStatus

    @GlobalStatus.setter
    def GlobalStatus(self, GlobalStatus):
        self._GlobalStatus = GlobalStatus

    @property
    def ServicesStatus(self):
        r"""Protection status
        :rtype: list of ServiceWafStatus
        """
        return self._ServicesStatus

    @ServicesStatus.setter
    def ServicesStatus(self, ServicesStatus):
        self._ServicesStatus = ServicesStatus

    @property
    def RouteStatus(self):
        r"""Route protection status
        :rtype: list of RouteWafStatus
        """
        return self._RouteStatus

    @RouteStatus.setter
    def RouteStatus(self, RouteStatus):
        self._RouteStatus = RouteStatus

    @property
    def ObjectStatus(self):
        r"""Object protection status
        :rtype: str
        """
        return self._ObjectStatus

    @ObjectStatus.setter
    def ObjectStatus(self, ObjectStatus):
        self._ObjectStatus = ObjectStatus


    def _deserialize(self, params):
        self._GlobalStatus = params.get("GlobalStatus")
        if params.get("ServicesStatus") is not None:
            self._ServicesStatus = []
            for item in params.get("ServicesStatus"):
                obj = ServiceWafStatus()
                obj._deserialize(item)
                self._ServicesStatus.append(obj)
        if params.get("RouteStatus") is not None:
            self._RouteStatus = []
            for item in params.get("RouteStatus"):
                obj = RouteWafStatus()
                obj._deserialize(item)
                self._RouteStatus.append(obj)
        self._ObjectStatus = params.get("ObjectStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalRedis(AbstractModel):
    r"""Cloud-native gateway traffic throttling plugin external redis configuration

    """

    def __init__(self):
        r"""
        :param _RedisHost: redis ip
        :type RedisHost: str
        :param _RedisPassword: redis password
        :type RedisPassword: str
        :param _RedisPort: redis port
        :type RedisPort: int
        :param _RedisTimeout: Timeout interval. Unit: ms
        :type RedisTimeout: int
        """
        self._RedisHost = None
        self._RedisPassword = None
        self._RedisPort = None
        self._RedisTimeout = None

    @property
    def RedisHost(self):
        r"""redis ip
        :rtype: str
        """
        return self._RedisHost

    @RedisHost.setter
    def RedisHost(self, RedisHost):
        self._RedisHost = RedisHost

    @property
    def RedisPassword(self):
        r"""redis password
        :rtype: str
        """
        return self._RedisPassword

    @RedisPassword.setter
    def RedisPassword(self, RedisPassword):
        self._RedisPassword = RedisPassword

    @property
    def RedisPort(self):
        r"""redis port
        :rtype: int
        """
        return self._RedisPort

    @RedisPort.setter
    def RedisPort(self, RedisPort):
        self._RedisPort = RedisPort

    @property
    def RedisTimeout(self):
        r"""Timeout interval. Unit: ms
        :rtype: int
        """
        return self._RedisTimeout

    @RedisTimeout.setter
    def RedisTimeout(self, RedisTimeout):
        self._RedisTimeout = RedisTimeout


    def _deserialize(self, params):
        self._RedisHost = params.get("RedisHost")
        self._RedisPassword = params.get("RedisPassword")
        self._RedisPort = params.get("RedisPort")
        self._RedisTimeout = params.get("RedisTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""Query filter general object

    """

    def __init__(self):
        r"""
        :param _Name: Filter parameter name
        :type Name: str
        :param _Values: Filter parameter value
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""Filter parameter name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""Filter parameter value
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
        


class GatewayInstanceSchemeAndPorts(AbstractModel):
    r"""Protocol port list of the gateway instance

    """

    def __init__(self):
        r"""
        :param _Scheme: Port protocol, selectable HTTP, HTTPS, TCP, and UDP.
        :type Scheme: str
        :param _PortList: port list
        :type PortList: list of int non-negative
        """
        self._Scheme = None
        self._PortList = None

    @property
    def Scheme(self):
        r"""Port protocol, selectable HTTP, HTTPS, TCP, and UDP.
        :rtype: str
        """
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme

    @property
    def PortList(self):
        r"""port list
        :rtype: list of int non-negative
        """
        return self._PortList

    @PortList.setter
    def PortList(self, PortList):
        self._PortList = PortList


    def _deserialize(self, params):
        self._Scheme = params.get("Scheme")
        self._PortList = params.get("PortList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayServices(AbstractModel):
    r"""Lightweight querying the gateway service list output parameters

    """

    def __init__(self):
        r"""
        :param _ServiceList: Service list
        :type ServiceList: list of KongServiceLightPreview
        :param _TotalCount: Total number of results
        :type TotalCount: int
        """
        self._ServiceList = None
        self._TotalCount = None

    @property
    def ServiceList(self):
        r"""Service list
        :rtype: list of KongServiceLightPreview
        """
        return self._ServiceList

    @ServiceList.setter
    def ServiceList(self, ServiceList):
        self._ServiceList = ServiceList

    @property
    def TotalCount(self):
        r"""Total number of results
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("ServiceList") is not None:
            self._ServiceList = []
            for item in params.get("ServiceList"):
                obj = KongServiceLightPreview()
                obj._deserialize(item)
                self._ServiceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GovernanceLaneGroup(AbstractModel):
    r"""Lane group

    """

    def __init__(self):
        r"""
        :param _Name: lane name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _ID: Lane group ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ID: str
        :param _TrafficEntries: Lane entry service list
Note: This field may return null, indicating that no valid values can be obtained.
        :type TrafficEntries: list of LaneTrafficEntry
        :param _Destinations: Lane service list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Destinations: list of GovernanceServiceDestination
        :param _Description: Lane group description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _Rules: Lane rule list of ALL lane groups
Note: This field may return null, indicating that no valid values can be obtained.
        :type Rules: list of GovernanceLaneRule
        :param _Revision: Rule content summary
Note: This field may return null, indicating that no valid values can be obtained.
        :type Revision: str
        :param _CreateTime: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _ModifyTime: Modification time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ModifyTime: str
        :param _Consistency: Rule consistency status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Consistency: str
        """
        self._Name = None
        self._ID = None
        self._TrafficEntries = None
        self._Destinations = None
        self._Description = None
        self._Rules = None
        self._Revision = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Consistency = None

    @property
    def Name(self):
        r"""lane name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ID(self):
        r"""Lane group ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def TrafficEntries(self):
        r"""Lane entry service list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of LaneTrafficEntry
        """
        return self._TrafficEntries

    @TrafficEntries.setter
    def TrafficEntries(self, TrafficEntries):
        self._TrafficEntries = TrafficEntries

    @property
    def Destinations(self):
        r"""Lane service list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of GovernanceServiceDestination
        """
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def Description(self):
        r"""Lane group description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Rules(self):
        r"""Lane rule list of ALL lane groups
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of GovernanceLaneRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Revision(self):
        r"""Rule content summary
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Revision

    @Revision.setter
    def Revision(self, Revision):
        self._Revision = Revision

    @property
    def CreateTime(self):
        r"""Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        r"""Modification time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Consistency(self):
        r"""Rule consistency status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Consistency

    @Consistency.setter
    def Consistency(self, Consistency):
        self._Consistency = Consistency


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ID = params.get("ID")
        if params.get("TrafficEntries") is not None:
            self._TrafficEntries = []
            for item in params.get("TrafficEntries"):
                obj = LaneTrafficEntry()
                obj._deserialize(item)
                self._TrafficEntries.append(obj)
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = GovernanceServiceDestination()
                obj._deserialize(item)
                self._Destinations.append(obj)
        self._Description = params.get("Description")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = GovernanceLaneRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Revision = params.get("Revision")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Consistency = params.get("Consistency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GovernanceLaneRule(AbstractModel):
    r"""Lane rule

    """

    def __init__(self):
        r"""
        :param _ID: Lane rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ID: str
        :param _Name: lane name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _LaneGroup: Swimlane group of the lane
Note: This field may return null, indicating that no valid values can be obtained.
        :type LaneGroup: str
        :param _Enable: Rule Enable Status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Enable: bool
        :param _TrafficLabels: Traffic Tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type TrafficLabels: list of Argument
        :param _TrafficMatchMode: Multiple traffic tag matching methods
AND
OR
Note: This field may return null, indicating that no valid values can be obtained.
        :type TrafficMatchMode: str
        :param _LaneMatchMode: Lane match mode
STRICT: Strict match
PERMISSIVE: Loose match
Note: This field may return null, indicating that no valid values can be obtained.
        :type LaneMatchMode: str
        :param _TrafficGray: Lane grayscale rule
        :type TrafficGray: :class:`tencentcloud.tse.v20201207.models.TrafficGray`
        :param _Description: Lane rule description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _LaneLabelValue: Lane tag content
Note: This field may return null, indicating that no valid values can be obtained.
        :type LaneLabelValue: str
        :param _CreateTime: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _EnableTime: Enabling time
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableTime: str
        :param _ModifyTime: Modification time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ModifyTime: str
        :param _Priority: Lane rule priority
Note: This field may return null, indicating that no valid values can be obtained.
        :type Priority: int
        :param _Revision: Rule abstract
Note: This field may return null, indicating that no valid values can be obtained.
        :type Revision: str
        """
        self._ID = None
        self._Name = None
        self._LaneGroup = None
        self._Enable = None
        self._TrafficLabels = None
        self._TrafficMatchMode = None
        self._LaneMatchMode = None
        self._TrafficGray = None
        self._Description = None
        self._LaneLabelValue = None
        self._CreateTime = None
        self._EnableTime = None
        self._ModifyTime = None
        self._Priority = None
        self._Revision = None

    @property
    def ID(self):
        r"""Lane rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""lane name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LaneGroup(self):
        r"""Swimlane group of the lane
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LaneGroup

    @LaneGroup.setter
    def LaneGroup(self, LaneGroup):
        self._LaneGroup = LaneGroup

    @property
    def Enable(self):
        r"""Rule Enable Status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def TrafficLabels(self):
        r"""Traffic Tag
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Argument
        """
        return self._TrafficLabels

    @TrafficLabels.setter
    def TrafficLabels(self, TrafficLabels):
        self._TrafficLabels = TrafficLabels

    @property
    def TrafficMatchMode(self):
        r"""Multiple traffic tag matching methods
AND
OR
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TrafficMatchMode

    @TrafficMatchMode.setter
    def TrafficMatchMode(self, TrafficMatchMode):
        self._TrafficMatchMode = TrafficMatchMode

    @property
    def LaneMatchMode(self):
        r"""Lane match mode
STRICT: Strict match
PERMISSIVE: Loose match
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LaneMatchMode

    @LaneMatchMode.setter
    def LaneMatchMode(self, LaneMatchMode):
        self._LaneMatchMode = LaneMatchMode

    @property
    def TrafficGray(self):
        r"""Lane grayscale rule
        :rtype: :class:`tencentcloud.tse.v20201207.models.TrafficGray`
        """
        return self._TrafficGray

    @TrafficGray.setter
    def TrafficGray(self, TrafficGray):
        self._TrafficGray = TrafficGray

    @property
    def Description(self):
        r"""Lane rule description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def LaneLabelValue(self):
        r"""Lane tag content
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LaneLabelValue

    @LaneLabelValue.setter
    def LaneLabelValue(self, LaneLabelValue):
        self._LaneLabelValue = LaneLabelValue

    @property
    def CreateTime(self):
        r"""Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EnableTime(self):
        r"""Enabling time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EnableTime

    @EnableTime.setter
    def EnableTime(self, EnableTime):
        self._EnableTime = EnableTime

    @property
    def ModifyTime(self):
        r"""Modification time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Priority(self):
        r"""Lane rule priority
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Revision(self):
        r"""Rule abstract
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Revision

    @Revision.setter
    def Revision(self, Revision):
        self._Revision = Revision


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._LaneGroup = params.get("LaneGroup")
        self._Enable = params.get("Enable")
        if params.get("TrafficLabels") is not None:
            self._TrafficLabels = []
            for item in params.get("TrafficLabels"):
                obj = Argument()
                obj._deserialize(item)
                self._TrafficLabels.append(obj)
        self._TrafficMatchMode = params.get("TrafficMatchMode")
        self._LaneMatchMode = params.get("LaneMatchMode")
        if params.get("TrafficGray") is not None:
            self._TrafficGray = TrafficGray()
            self._TrafficGray._deserialize(params.get("TrafficGray"))
        self._Description = params.get("Description")
        self._LaneLabelValue = params.get("LaneLabelValue")
        self._CreateTime = params.get("CreateTime")
        self._EnableTime = params.get("EnableTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Priority = params.get("Priority")
        self._Revision = params.get("Revision")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GovernanceServiceDestination(AbstractModel):
    r"""Service instance group

    """

    def __init__(self):
        r"""
        :param _Namespace: Namespace
Note: This field may return null, indicating that no valid values can be obtained.
        :type Namespace: str
        :param _Service: Service.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Service: str
        :param _Labels: Instance tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type Labels: list of RoutingDestinationRuleLabel
        """
        self._Namespace = None
        self._Service = None
        self._Labels = None

    @property
    def Namespace(self):
        r"""Namespace
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Service(self):
        r"""Service.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Labels(self):
        r"""Instance tag
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of RoutingDestinationRuleLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._Service = params.get("Service")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = RoutingDestinationRuleLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstancePort(AbstractModel):
    r"""Instance listen port information

    """

    def __init__(self):
        r"""
        :param _HttpPort: Listen http port range.
        :type HttpPort: str
        :param _HttpsPort: Listen port range for https.
        :type HttpsPort: str
        :param _TcpPort: Listen port range for tcp.
        :type TcpPort: str
        :param _UdpPort: Listen udp port range.
        :type UdpPort: str
        """
        self._HttpPort = None
        self._HttpsPort = None
        self._TcpPort = None
        self._UdpPort = None

    @property
    def HttpPort(self):
        r"""Listen http port range.
        :rtype: str
        """
        return self._HttpPort

    @HttpPort.setter
    def HttpPort(self, HttpPort):
        self._HttpPort = HttpPort

    @property
    def HttpsPort(self):
        r"""Listen port range for https.
        :rtype: str
        """
        return self._HttpsPort

    @HttpsPort.setter
    def HttpsPort(self, HttpsPort):
        self._HttpsPort = HttpsPort

    @property
    def TcpPort(self):
        r"""Listen port range for tcp.
        :rtype: str
        """
        return self._TcpPort

    @TcpPort.setter
    def TcpPort(self, TcpPort):
        self._TcpPort = TcpPort

    @property
    def UdpPort(self):
        r"""Listen udp port range.
        :rtype: str
        """
        return self._UdpPort

    @UdpPort.setter
    def UdpPort(self, UdpPort):
        self._UdpPort = UdpPort


    def _deserialize(self, params):
        self._HttpPort = params.get("HttpPort")
        self._HttpsPort = params.get("HttpsPort")
        self._TcpPort = params.get("TcpPort")
        self._UdpPort = params.get("UdpPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTagInfo(AbstractModel):
    r"""Tag information of the engine instance

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key.
        :type TagKey: str
        :param _TagValue: Tag value.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""Tag key.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Tag value.
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetConfig(AbstractModel):
    r"""Public network load balancing configuration

    """

    def __init__(self):
        r"""
        :param _InternetAddressVersion: Public network address version. Optional: "IPV4" | "IPV6". By default IPV4 if left blank.
        :type InternetAddressVersion: str
        :param _InternetPayMode: Public network payment mode. Currently, only "BANDWIDTH" is selectable. Defaults to "BANDWIDTH" if left blank.
        :type InternetPayMode: str
        :param _InternetMaxBandwidthOut: Public network bandwidth.
        :type InternetMaxBandwidthOut: int
        :param _Description: Description of load balancing
        :type Description: str
        :param _SlaType: Load balancing specification type. Support clb.c2.medium, clb.c3.small, clb.c3.medium, clb.c4.small, clb.c4.medium, clb.c4.large, clb.c4.xlarge. Defaults to shared type.
        :type SlaType: str
        :param _MultiZoneFlag: Whether load balancing is multi-availability zone
        :type MultiZoneFlag: bool
        :param _MasterZoneId: Primary AZ.
        :type MasterZoneId: str
        :param _SlaveZoneId: standby availability zone
        :type SlaveZoneId: str
        """
        self._InternetAddressVersion = None
        self._InternetPayMode = None
        self._InternetMaxBandwidthOut = None
        self._Description = None
        self._SlaType = None
        self._MultiZoneFlag = None
        self._MasterZoneId = None
        self._SlaveZoneId = None

    @property
    def InternetAddressVersion(self):
        r"""Public network address version. Optional: "IPV4" | "IPV6". By default IPV4 if left blank.
        :rtype: str
        """
        return self._InternetAddressVersion

    @InternetAddressVersion.setter
    def InternetAddressVersion(self, InternetAddressVersion):
        self._InternetAddressVersion = InternetAddressVersion

    @property
    def InternetPayMode(self):
        r"""Public network payment mode. Currently, only "BANDWIDTH" is selectable. Defaults to "BANDWIDTH" if left blank.
        :rtype: str
        """
        return self._InternetPayMode

    @InternetPayMode.setter
    def InternetPayMode(self, InternetPayMode):
        self._InternetPayMode = InternetPayMode

    @property
    def InternetMaxBandwidthOut(self):
        r"""Public network bandwidth.
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def Description(self):
        r"""Description of load balancing
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SlaType(self):
        r"""Load balancing specification type. Support clb.c2.medium, clb.c3.small, clb.c3.medium, clb.c4.small, clb.c4.medium, clb.c4.large, clb.c4.xlarge. Defaults to shared type.
        :rtype: str
        """
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType

    @property
    def MultiZoneFlag(self):
        r"""Whether load balancing is multi-availability zone
        :rtype: bool
        """
        return self._MultiZoneFlag

    @MultiZoneFlag.setter
    def MultiZoneFlag(self, MultiZoneFlag):
        self._MultiZoneFlag = MultiZoneFlag

    @property
    def MasterZoneId(self):
        r"""Primary AZ.
        :rtype: str
        """
        return self._MasterZoneId

    @MasterZoneId.setter
    def MasterZoneId(self, MasterZoneId):
        self._MasterZoneId = MasterZoneId

    @property
    def SlaveZoneId(self):
        r"""standby availability zone
        :rtype: str
        """
        return self._SlaveZoneId

    @SlaveZoneId.setter
    def SlaveZoneId(self, SlaveZoneId):
        self._SlaveZoneId = SlaveZoneId


    def _deserialize(self, params):
        self._InternetAddressVersion = params.get("InternetAddressVersion")
        self._InternetPayMode = params.get("InternetPayMode")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._Description = params.get("Description")
        self._SlaType = params.get("SlaType")
        self._MultiZoneFlag = params.get("MultiZoneFlag")
        self._MasterZoneId = params.get("MasterZoneId")
        self._SlaveZoneId = params.get("SlaveZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KVMapping(AbstractModel):
    r"""Key-value pair

    """

    def __init__(self):
        r"""
        :param _Key: key
        :type Key: str
        :param _Value: value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""value
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
        


class KeyValue(AbstractModel):
    r"""Key/Value structure

    """

    def __init__(self):
        r"""
        :param _Key: Key of the condition
        :type Key: str
        :param _Value: Value of the condition
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Key of the condition
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Value of the condition
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
        


class KongActiveHealthCheck(AbstractModel):
    r"""Kong gateway proactive health check configuration

    """

    def __init__(self):
        r"""
        :param _HealthyInterval: Probe interval for active health check in seconds. 0 means disabled.
        :type HealthyInterval: int
        :param _UnHealthyInterval: Proactive health check exception probe interval, unit: second. 0 indicates disabled.
        :type UnHealthyInterval: int
        :param _HttpPath: Path used in GET HTTP request to run as a proactive health check probe. Default: "/".
        :type HttpPath: str
        :param _Timeout: Timeout for GET HTTP requests, unit: seconds. Default 60.
        :type Timeout: float
        """
        self._HealthyInterval = None
        self._UnHealthyInterval = None
        self._HttpPath = None
        self._Timeout = None

    @property
    def HealthyInterval(self):
        r"""Probe interval for active health check in seconds. 0 means disabled.
        :rtype: int
        """
        return self._HealthyInterval

    @HealthyInterval.setter
    def HealthyInterval(self, HealthyInterval):
        self._HealthyInterval = HealthyInterval

    @property
    def UnHealthyInterval(self):
        r"""Proactive health check exception probe interval, unit: second. 0 indicates disabled.
        :rtype: int
        """
        return self._UnHealthyInterval

    @UnHealthyInterval.setter
    def UnHealthyInterval(self, UnHealthyInterval):
        self._UnHealthyInterval = UnHealthyInterval

    @property
    def HttpPath(self):
        r"""Path used in GET HTTP request to run as a proactive health check probe. Default: "/".
        :rtype: str
        """
        return self._HttpPath

    @HttpPath.setter
    def HttpPath(self, HttpPath):
        self._HttpPath = HttpPath

    @property
    def Timeout(self):
        r"""Timeout for GET HTTP requests, unit: seconds. Default 60.
        :rtype: float
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout


    def _deserialize(self, params):
        self._HealthyInterval = params.get("HealthyInterval")
        self._UnHealthyInterval = params.get("UnHealthyInterval")
        self._HttpPath = params.get("HttpPath")
        self._Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongCertificate(AbstractModel):
    r"""Cloud-native gateway certificate

    """

    def __init__(self):
        r"""
        :param _Cert: None.
        :type Cert: :class:`tencentcloud.tse.v20201207.models.KongCertificatesPreview`
        """
        self._Cert = None

    @property
    def Cert(self):
        r"""None.
        :rtype: :class:`tencentcloud.tse.v20201207.models.KongCertificatesPreview`
        """
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert


    def _deserialize(self, params):
        if params.get("Cert") is not None:
            self._Cert = KongCertificatesPreview()
            self._Cert._deserialize(params.get("Cert"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongCertificatesList(AbstractModel):
    r"""Certificate list of the kong instance

    """

    def __init__(self):
        r"""
        :param _Total: Total Quantity of Certificate Lists
        :type Total: int
        :param _CertificatesList: None.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertificatesList: list of KongCertificatesPreview
        :param _Pages: Total number of pages in the certificate list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        """
        self._Total = None
        self._CertificatesList = None
        self._Pages = None

    @property
    def Total(self):
        r"""Total Quantity of Certificate Lists
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def CertificatesList(self):
        r"""None.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of KongCertificatesPreview
        """
        return self._CertificatesList

    @CertificatesList.setter
    def CertificatesList(self, CertificatesList):
        self._CertificatesList = CertificatesList

    @property
    def Pages(self):
        warnings.warn("parameter `Pages` is deprecated", DeprecationWarning) 

        r"""Total number of pages in the certificate list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        warnings.warn("parameter `Pages` is deprecated", DeprecationWarning) 

        self._Pages = Pages


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("CertificatesList") is not None:
            self._CertificatesList = []
            for item in params.get("CertificatesList"):
                obj = KongCertificatesPreview()
                obj._deserialize(item)
                self._CertificatesList.append(obj)
        self._Pages = params.get("Pages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongCertificatesPreview(AbstractModel):
    r"""Cloud-native gateway certificate preview information

    """

    def __init__(self):
        r"""
        :param _Name: certificate name
        :type Name: str
        :param _Id: Id
        :type Id: str
        :param _BindDomains: Bound domain name
        :type BindDomains: list of str
        :param _Status: Certificate status: expired.
active
        :type Status: str
        :param _Crt: Certificate in pem format
        :type Crt: str
        :param _Key: Certificate Private Key
        :type Key: str
        :param _ExpireTime: certificate expiration time
        :type ExpireTime: str
        :param _CreateTime: Certificate upload time
        :type CreateTime: str
        :param _IssueTime: Certificate issuance time
        :type IssueTime: str
        :param _CertSource: Certificate source: native (kong custom certificate)
ssl (platform cert)
        :type CertSource: str
        :param _CertId: ssl Platform Certificate Id
        :type CertId: str
        """
        self._Name = None
        self._Id = None
        self._BindDomains = None
        self._Status = None
        self._Crt = None
        self._Key = None
        self._ExpireTime = None
        self._CreateTime = None
        self._IssueTime = None
        self._CertSource = None
        self._CertId = None

    @property
    def Name(self):
        r"""certificate name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        r"""Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def BindDomains(self):
        r"""Bound domain name
        :rtype: list of str
        """
        return self._BindDomains

    @BindDomains.setter
    def BindDomains(self, BindDomains):
        self._BindDomains = BindDomains

    @property
    def Status(self):
        r"""Certificate status: expired.
active
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Crt(self):
        r"""Certificate in pem format
        :rtype: str
        """
        return self._Crt

    @Crt.setter
    def Crt(self, Crt):
        self._Crt = Crt

    @property
    def Key(self):
        r"""Certificate Private Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def ExpireTime(self):
        r"""certificate expiration time
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def CreateTime(self):
        r"""Certificate upload time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IssueTime(self):
        r"""Certificate issuance time
        :rtype: str
        """
        return self._IssueTime

    @IssueTime.setter
    def IssueTime(self, IssueTime):
        self._IssueTime = IssueTime

    @property
    def CertSource(self):
        r"""Certificate source: native (kong custom certificate)
ssl (platform cert)
        :rtype: str
        """
        return self._CertSource

    @CertSource.setter
    def CertSource(self, CertSource):
        self._CertSource = CertSource

    @property
    def CertId(self):
        r"""ssl Platform Certificate Id
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        self._BindDomains = params.get("BindDomains")
        self._Status = params.get("Status")
        self._Crt = params.get("Crt")
        self._Key = params.get("Key")
        self._ExpireTime = params.get("ExpireTime")
        self._CreateTime = params.get("CreateTime")
        self._IssueTime = params.get("IssueTime")
        self._CertSource = params.get("CertSource")
        self._CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongPassiveHealthCheck(AbstractModel):
    r"""Kong gateway passive health check configuration

    """

    def __init__(self):
        r"""
        :param _Type: Backend target protocol type. Passive health check supports http and tcp. Proactive health check supports http.
        :type Type: str
        """
        self._Type = None

    @property
    def Type(self):
        r"""Backend target protocol type. Passive health check supports http and tcp. Proactive health check supports http.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongRoutePreview(AbstractModel):
    r"""Cloud-native gateway routing information

    """

    def __init__(self):
        r"""
        :param _ID: Service ID
        :type ID: str
        :param _Name: Service name.
        :type Name: str
        :param _Methods: None.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Methods: list of str
        :param _Paths: None.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Paths: list of str
        :param _Hosts: None.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Hosts: list of str
        :param _Protocols: None.
        :type Protocols: list of str
        :param _PreserveHost: None.
        :type PreserveHost: bool
        :param _HttpsRedirectStatusCode: None.
        :type HttpsRedirectStatusCode: int
        :param _StripPath: None.
        :type StripPath: bool
        :param _CreatedTime: None.
        :type CreatedTime: str
        :param _ForceHttps: Is mandatory HTTPS enabled?
Note: This field may return null, indicating that no valid values can be obtained.
        :type ForceHttps: bool
        :param _ServiceName: Service name
        :type ServiceName: str
        :param _ServiceID: Service ID
        :type ServiceID: str
        :param _DestinationPorts: Destination Port
        :type DestinationPorts: list of int non-negative
        :param _Headers: Headers of the route
        :type Headers: list of KVMapping
        :param _RequestBuffering: Whether to cache the request body, default true
        :type RequestBuffering: bool
        :param _ResponseBuffering: Whether to cache response body, default true
        :type ResponseBuffering: bool
        :param _RegexPriority: Regular Priority
        :type RegexPriority: int
        :param _QueryStringParameters: querystring parameter
        :type QueryStringParameters: list of KVMapping
        """
        self._ID = None
        self._Name = None
        self._Methods = None
        self._Paths = None
        self._Hosts = None
        self._Protocols = None
        self._PreserveHost = None
        self._HttpsRedirectStatusCode = None
        self._StripPath = None
        self._CreatedTime = None
        self._ForceHttps = None
        self._ServiceName = None
        self._ServiceID = None
        self._DestinationPorts = None
        self._Headers = None
        self._RequestBuffering = None
        self._ResponseBuffering = None
        self._RegexPriority = None
        self._QueryStringParameters = None

    @property
    def ID(self):
        r"""Service ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""Service name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Methods(self):
        r"""None.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Methods

    @Methods.setter
    def Methods(self, Methods):
        self._Methods = Methods

    @property
    def Paths(self):
        r"""None.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths

    @property
    def Hosts(self):
        r"""None.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def Protocols(self):
        r"""None.
        :rtype: list of str
        """
        return self._Protocols

    @Protocols.setter
    def Protocols(self, Protocols):
        self._Protocols = Protocols

    @property
    def PreserveHost(self):
        r"""None.
        :rtype: bool
        """
        return self._PreserveHost

    @PreserveHost.setter
    def PreserveHost(self, PreserveHost):
        self._PreserveHost = PreserveHost

    @property
    def HttpsRedirectStatusCode(self):
        r"""None.
        :rtype: int
        """
        return self._HttpsRedirectStatusCode

    @HttpsRedirectStatusCode.setter
    def HttpsRedirectStatusCode(self, HttpsRedirectStatusCode):
        self._HttpsRedirectStatusCode = HttpsRedirectStatusCode

    @property
    def StripPath(self):
        r"""None.
        :rtype: bool
        """
        return self._StripPath

    @StripPath.setter
    def StripPath(self, StripPath):
        self._StripPath = StripPath

    @property
    def CreatedTime(self):
        r"""None.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ForceHttps(self):
        warnings.warn("parameter `ForceHttps` is deprecated", DeprecationWarning) 

        r"""Is mandatory HTTPS enabled?
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._ForceHttps

    @ForceHttps.setter
    def ForceHttps(self, ForceHttps):
        warnings.warn("parameter `ForceHttps` is deprecated", DeprecationWarning) 

        self._ForceHttps = ForceHttps

    @property
    def ServiceName(self):
        r"""Service name
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceID(self):
        r"""Service ID
        :rtype: str
        """
        return self._ServiceID

    @ServiceID.setter
    def ServiceID(self, ServiceID):
        self._ServiceID = ServiceID

    @property
    def DestinationPorts(self):
        r"""Destination Port
        :rtype: list of int non-negative
        """
        return self._DestinationPorts

    @DestinationPorts.setter
    def DestinationPorts(self, DestinationPorts):
        self._DestinationPorts = DestinationPorts

    @property
    def Headers(self):
        r"""Headers of the route
        :rtype: list of KVMapping
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def RequestBuffering(self):
        r"""Whether to cache the request body, default true
        :rtype: bool
        """
        return self._RequestBuffering

    @RequestBuffering.setter
    def RequestBuffering(self, RequestBuffering):
        self._RequestBuffering = RequestBuffering

    @property
    def ResponseBuffering(self):
        r"""Whether to cache response body, default true
        :rtype: bool
        """
        return self._ResponseBuffering

    @ResponseBuffering.setter
    def ResponseBuffering(self, ResponseBuffering):
        self._ResponseBuffering = ResponseBuffering

    @property
    def RegexPriority(self):
        r"""Regular Priority
        :rtype: int
        """
        return self._RegexPriority

    @RegexPriority.setter
    def RegexPriority(self, RegexPriority):
        self._RegexPriority = RegexPriority

    @property
    def QueryStringParameters(self):
        r"""querystring parameter
        :rtype: list of KVMapping
        """
        return self._QueryStringParameters

    @QueryStringParameters.setter
    def QueryStringParameters(self, QueryStringParameters):
        self._QueryStringParameters = QueryStringParameters


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Methods = params.get("Methods")
        self._Paths = params.get("Paths")
        self._Hosts = params.get("Hosts")
        self._Protocols = params.get("Protocols")
        self._PreserveHost = params.get("PreserveHost")
        self._HttpsRedirectStatusCode = params.get("HttpsRedirectStatusCode")
        self._StripPath = params.get("StripPath")
        self._CreatedTime = params.get("CreatedTime")
        self._ForceHttps = params.get("ForceHttps")
        self._ServiceName = params.get("ServiceName")
        self._ServiceID = params.get("ServiceID")
        self._DestinationPorts = params.get("DestinationPorts")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = KVMapping()
                obj._deserialize(item)
                self._Headers.append(obj)
        self._RequestBuffering = params.get("RequestBuffering")
        self._ResponseBuffering = params.get("ResponseBuffering")
        self._RegexPriority = params.get("RegexPriority")
        if params.get("QueryStringParameters") is not None:
            self._QueryStringParameters = []
            for item in params.get("QueryStringParameters"):
                obj = KVMapping()
                obj._deserialize(item)
                self._QueryStringParameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongServiceDetail(AbstractModel):
    r"""Service details of cloud-native gateway

    """

    def __init__(self):
        r"""
        :param _ID: service ID
        :type ID: str
        :param _Name: Service name.
        :type Name: str
        :param _Protocol: Backend protocol
        :type Protocol: str
        :param _Path: Backend path
Note: This field may return null, indicating that no valid values can be obtained.
        :type Path: str
        :param _Timeout: Backend delay in milliseconds
        :type Timeout: int
        :param _Retries: Number of retries.
        :type Retries: int
        :param _Tags: Tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of str
        :param _UpstreamInfo: backend configuration
        :type UpstreamInfo: :class:`tencentcloud.tse.v20201207.models.KongUpstreamInfo`
        :param _UpstreamType: Backend type
        :type UpstreamType: str
        :param _Editable: Whether it is editable.
        :type Editable: bool
        :param _CreatedTime: Creation time.
        :type CreatedTime: str
        """
        self._ID = None
        self._Name = None
        self._Protocol = None
        self._Path = None
        self._Timeout = None
        self._Retries = None
        self._Tags = None
        self._UpstreamInfo = None
        self._UpstreamType = None
        self._Editable = None
        self._CreatedTime = None

    @property
    def ID(self):
        r"""service ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""Service name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Protocol(self):
        r"""Backend protocol
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Path(self):
        r"""Backend path
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Timeout(self):
        r"""Backend delay in milliseconds
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Retries(self):
        r"""Number of retries.
        :rtype: int
        """
        return self._Retries

    @Retries.setter
    def Retries(self, Retries):
        self._Retries = Retries

    @property
    def Tags(self):
        r"""Tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def UpstreamInfo(self):
        r"""backend configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.KongUpstreamInfo`
        """
        return self._UpstreamInfo

    @UpstreamInfo.setter
    def UpstreamInfo(self, UpstreamInfo):
        self._UpstreamInfo = UpstreamInfo

    @property
    def UpstreamType(self):
        r"""Backend type
        :rtype: str
        """
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def Editable(self):
        r"""Whether it is editable.
        :rtype: bool
        """
        return self._Editable

    @Editable.setter
    def Editable(self, Editable):
        self._Editable = Editable

    @property
    def CreatedTime(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Protocol = params.get("Protocol")
        self._Path = params.get("Path")
        self._Timeout = params.get("Timeout")
        self._Retries = params.get("Retries")
        self._Tags = params.get("Tags")
        if params.get("UpstreamInfo") is not None:
            self._UpstreamInfo = KongUpstreamInfo()
            self._UpstreamInfo._deserialize(params.get("UpstreamInfo"))
        self._UpstreamType = params.get("UpstreamType")
        self._Editable = params.get("Editable")
        self._CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongServiceLightPreview(AbstractModel):
    r"""Simple Preview Information of Cloud-Native Gateway Service

    """

    def __init__(self):
        r"""
        :param _ID: service ID
        :type ID: str
        :param _Name: Service name.
        :type Name: str
        :param _UpstreamInfo: backend configuration
        :type UpstreamInfo: :class:`tencentcloud.tse.v20201207.models.KongUpstreamInfo`
        :param _UpstreamType: Backend type
        :type UpstreamType: str
        :param _CreatedTime: Creation time.
        :type CreatedTime: str
        :param _Path: request path
Note: This field may return null, indicating that no valid values can be obtained.
        :type Path: str
        :param _Protocol: Backend protocol
        :type Protocol: str
        :param _Retries: Number of retries.
        :type Retries: int
        :param _Timeout: Backend delay in milliseconds
        :type Timeout: int
        """
        self._ID = None
        self._Name = None
        self._UpstreamInfo = None
        self._UpstreamType = None
        self._CreatedTime = None
        self._Path = None
        self._Protocol = None
        self._Retries = None
        self._Timeout = None

    @property
    def ID(self):
        r"""service ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""Service name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def UpstreamInfo(self):
        r"""backend configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.KongUpstreamInfo`
        """
        return self._UpstreamInfo

    @UpstreamInfo.setter
    def UpstreamInfo(self, UpstreamInfo):
        self._UpstreamInfo = UpstreamInfo

    @property
    def UpstreamType(self):
        r"""Backend type
        :rtype: str
        """
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def CreatedTime(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Path(self):
        r"""request path
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Protocol(self):
        r"""Backend protocol
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Retries(self):
        r"""Number of retries.
        :rtype: int
        """
        return self._Retries

    @Retries.setter
    def Retries(self, Retries):
        self._Retries = Retries

    @property
    def Timeout(self):
        r"""Backend delay in milliseconds
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        if params.get("UpstreamInfo") is not None:
            self._UpstreamInfo = KongUpstreamInfo()
            self._UpstreamInfo._deserialize(params.get("UpstreamInfo"))
        self._UpstreamType = params.get("UpstreamType")
        self._CreatedTime = params.get("CreatedTime")
        self._Path = params.get("Path")
        self._Protocol = params.get("Protocol")
        self._Retries = params.get("Retries")
        self._Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongServicePreview(AbstractModel):
    r"""Preview Information of Cloud-Native Gateway Service

    """

    def __init__(self):
        r"""
        :param _ID: service ID
        :type ID: str
        :param _Name: Service name.
        :type Name: str
        :param _Tags: Tag.
        :type Tags: list of str
        :param _UpstreamInfo: backend configuration
        :type UpstreamInfo: :class:`tencentcloud.tse.v20201207.models.KongUpstreamInfo`
        :param _UpstreamType: Backend type
        :type UpstreamType: str
        :param _CreatedTime: Creation time.
        :type CreatedTime: str
        :param _Editable: Whether it is editable.
        :type Editable: bool
        :param _Path: request path
Note: This field may return null, indicating that no valid values can be obtained.
        :type Path: str
        """
        self._ID = None
        self._Name = None
        self._Tags = None
        self._UpstreamInfo = None
        self._UpstreamType = None
        self._CreatedTime = None
        self._Editable = None
        self._Path = None

    @property
    def ID(self):
        r"""service ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""Service name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Tags(self):
        r"""Tag.
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def UpstreamInfo(self):
        r"""backend configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.KongUpstreamInfo`
        """
        return self._UpstreamInfo

    @UpstreamInfo.setter
    def UpstreamInfo(self, UpstreamInfo):
        self._UpstreamInfo = UpstreamInfo

    @property
    def UpstreamType(self):
        r"""Backend type
        :rtype: str
        """
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def CreatedTime(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Editable(self):
        r"""Whether it is editable.
        :rtype: bool
        """
        return self._Editable

    @Editable.setter
    def Editable(self, Editable):
        self._Editable = Editable

    @property
    def Path(self):
        r"""request path
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Tags = params.get("Tags")
        if params.get("UpstreamInfo") is not None:
            self._UpstreamInfo = KongUpstreamInfo()
            self._UpstreamInfo._deserialize(params.get("UpstreamInfo"))
        self._UpstreamType = params.get("UpstreamType")
        self._CreatedTime = params.get("CreatedTime")
        self._Editable = params.get("Editable")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongServiceRouteList(AbstractModel):
    r"""Service route list of kong

    """

    def __init__(self):
        r"""
        :param _RouteList: None.
        :type RouteList: list of KongRoutePreview
        :param _TotalCount: Total number.
        :type TotalCount: int
        """
        self._RouteList = None
        self._TotalCount = None

    @property
    def RouteList(self):
        r"""None.
        :rtype: list of KongRoutePreview
        """
        return self._RouteList

    @RouteList.setter
    def RouteList(self, RouteList):
        self._RouteList = RouteList

    @property
    def TotalCount(self):
        r"""Total number.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("RouteList") is not None:
            self._RouteList = []
            for item in params.get("RouteList"):
                obj = KongRoutePreview()
                obj._deserialize(item)
                self._RouteList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongServices(AbstractModel):
    r"""Service list of the kong instance

    """

    def __init__(self):
        r"""
        :param _ServiceList: Service list of the kong instance
        :type ServiceList: list of KongServicePreview
        :param _TotalCount: Total Quantity of Lists
        :type TotalCount: int
        """
        self._ServiceList = None
        self._TotalCount = None

    @property
    def ServiceList(self):
        r"""Service list of the kong instance
        :rtype: list of KongServicePreview
        """
        return self._ServiceList

    @ServiceList.setter
    def ServiceList(self, ServiceList):
        self._ServiceList = ServiceList

    @property
    def TotalCount(self):
        r"""Total Quantity of Lists
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("ServiceList") is not None:
            self._ServiceList = []
            for item in params.get("ServiceList"):
                obj = KongServicePreview()
                obj._deserialize(item)
                self._ServiceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongTarget(AbstractModel):
    r"""Target in Kong Upstream

    """

    def __init__(self):
        r"""
        :param _Host: Host
        :type Host: str
        :param _Port: Port.
        :type Port: int
        :param _Weight: Weight
        :type Weight: int
        :param _Health: Health status.
        :type Health: str
        :param _CreatedTime: Creation time.
        :type CreatedTime: str
        :param _Source: Source of the Target
        :type Source: str
        :param _CvmInstanceId: CVM instance ID
        :type CvmInstanceId: str
        :param _CvmInstanceName: CVM instance name.
        :type CvmInstanceName: str
        :param _Tags: target tag
        :type Tags: list of str
        """
        self._Host = None
        self._Port = None
        self._Weight = None
        self._Health = None
        self._CreatedTime = None
        self._Source = None
        self._CvmInstanceId = None
        self._CvmInstanceName = None
        self._Tags = None

    @property
    def Host(self):
        r"""Host
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        r"""Port.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        r"""Weight
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Health(self):
        r"""Health status.
        :rtype: str
        """
        return self._Health

    @Health.setter
    def Health(self, Health):
        self._Health = Health

    @property
    def CreatedTime(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Source(self):
        r"""Source of the Target
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def CvmInstanceId(self):
        r"""CVM instance ID
        :rtype: str
        """
        return self._CvmInstanceId

    @CvmInstanceId.setter
    def CvmInstanceId(self, CvmInstanceId):
        self._CvmInstanceId = CvmInstanceId

    @property
    def CvmInstanceName(self):
        r"""CVM instance name.
        :rtype: str
        """
        return self._CvmInstanceName

    @CvmInstanceName.setter
    def CvmInstanceName(self, CvmInstanceName):
        self._CvmInstanceName = CvmInstanceName

    @property
    def Tags(self):
        r"""target tag
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._Health = params.get("Health")
        self._CreatedTime = params.get("CreatedTime")
        self._Source = params.get("Source")
        self._CvmInstanceId = params.get("CvmInstanceId")
        self._CvmInstanceName = params.get("CvmInstanceName")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongUpstreamInfo(AbstractModel):
    r"""backend configuration of the service

    """

    def __init__(self):
        r"""
        :param _Host: IP or domain
        :type Host: str
        :param _Port: Port.
        :type Port: int
        :param _SourceID: Service source ID
        :type SourceID: str
        :param _Namespace: Namespace
        :type Namespace: str
        :param _ServiceName: Service (registration center or service in Kubernetes) name
        :type ServiceName: str
        :param _Targets: The backend type is IPList when provided by the service
Note: This field may return null, indicating that no valid values can be obtained.
        :type Targets: list of KongTarget
        :param _SourceType: Service source type
        :type SourceType: str
        :param _ScfType: SCF Function Type
        :type ScfType: str
        :param _ScfNamespace: SCF function namespace
        :type ScfNamespace: str
        :param _ScfLambdaName: SCF Function Name
        :type ScfLambdaName: str
        :param _ScfLambdaQualifier: SCF Function Version
        :type ScfLambdaQualifier: str
        :param _SlowStart: Cold start time, in seconds
        :type SlowStart: int
        :param _Algorithm: Load balancing algorithm, defaults to round-robin, also supports least-connections, consisten_hashing
        :type Algorithm: str
        :param _AutoScalingGroupID: Auto scaling group ID of CVM
        :type AutoScalingGroupID: str
        :param _AutoScalingCvmPort: CVM auto scaling group port
        :type AutoScalingCvmPort: int
        :param _AutoScalingTatCmdStatus: TAT command status of the CVM used in the auto scaling group
        :type AutoScalingTatCmdStatus: str
        :param _AutoScalingHookStatus: CVM auto scaling group lifecycle hook status
        :type AutoScalingHookStatus: str
        :param _SourceName: Service source name.
        :type SourceName: str
        :param _RealSourceType: Precise service source type. Type passed in when creating a service source.
        :type RealSourceType: str
        :param _HealthStatus: upstream health status HEALTHY (healthy), UNHEALTHY (abnormal), HEALTHCHECKS_OFF (not enabled), and NONE (health checks not supported)
        :type HealthStatus: str
        :param _ScfCamAuthEnable: Whether CAM authentication is enabled for SCF. Enabled by default (true) when left blank.
        :type ScfCamAuthEnable: bool
        :param _ScfIsBase64Encoded: Whether Base64 encoding is enabled for SCF, default false
        :type ScfIsBase64Encoded: bool
        :param _ScfIsIntegratedResponse: Whether response integration is enabled for the cloud function, default false
        :type ScfIsIntegratedResponse: bool
        """
        self._Host = None
        self._Port = None
        self._SourceID = None
        self._Namespace = None
        self._ServiceName = None
        self._Targets = None
        self._SourceType = None
        self._ScfType = None
        self._ScfNamespace = None
        self._ScfLambdaName = None
        self._ScfLambdaQualifier = None
        self._SlowStart = None
        self._Algorithm = None
        self._AutoScalingGroupID = None
        self._AutoScalingCvmPort = None
        self._AutoScalingTatCmdStatus = None
        self._AutoScalingHookStatus = None
        self._SourceName = None
        self._RealSourceType = None
        self._HealthStatus = None
        self._ScfCamAuthEnable = None
        self._ScfIsBase64Encoded = None
        self._ScfIsIntegratedResponse = None

    @property
    def Host(self):
        r"""IP or domain
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        r"""Port.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def SourceID(self):
        r"""Service source ID
        :rtype: str
        """
        return self._SourceID

    @SourceID.setter
    def SourceID(self, SourceID):
        self._SourceID = SourceID

    @property
    def Namespace(self):
        r"""Namespace
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ServiceName(self):
        r"""Service (registration center or service in Kubernetes) name
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Targets(self):
        r"""The backend type is IPList when provided by the service
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of KongTarget
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def SourceType(self):
        r"""Service source type
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def ScfType(self):
        r"""SCF Function Type
        :rtype: str
        """
        return self._ScfType

    @ScfType.setter
    def ScfType(self, ScfType):
        self._ScfType = ScfType

    @property
    def ScfNamespace(self):
        r"""SCF function namespace
        :rtype: str
        """
        return self._ScfNamespace

    @ScfNamespace.setter
    def ScfNamespace(self, ScfNamespace):
        self._ScfNamespace = ScfNamespace

    @property
    def ScfLambdaName(self):
        r"""SCF Function Name
        :rtype: str
        """
        return self._ScfLambdaName

    @ScfLambdaName.setter
    def ScfLambdaName(self, ScfLambdaName):
        self._ScfLambdaName = ScfLambdaName

    @property
    def ScfLambdaQualifier(self):
        r"""SCF Function Version
        :rtype: str
        """
        return self._ScfLambdaQualifier

    @ScfLambdaQualifier.setter
    def ScfLambdaQualifier(self, ScfLambdaQualifier):
        self._ScfLambdaQualifier = ScfLambdaQualifier

    @property
    def SlowStart(self):
        r"""Cold start time, in seconds
        :rtype: int
        """
        return self._SlowStart

    @SlowStart.setter
    def SlowStart(self, SlowStart):
        self._SlowStart = SlowStart

    @property
    def Algorithm(self):
        r"""Load balancing algorithm, defaults to round-robin, also supports least-connections, consisten_hashing
        :rtype: str
        """
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def AutoScalingGroupID(self):
        r"""Auto scaling group ID of CVM
        :rtype: str
        """
        return self._AutoScalingGroupID

    @AutoScalingGroupID.setter
    def AutoScalingGroupID(self, AutoScalingGroupID):
        self._AutoScalingGroupID = AutoScalingGroupID

    @property
    def AutoScalingCvmPort(self):
        r"""CVM auto scaling group port
        :rtype: int
        """
        return self._AutoScalingCvmPort

    @AutoScalingCvmPort.setter
    def AutoScalingCvmPort(self, AutoScalingCvmPort):
        self._AutoScalingCvmPort = AutoScalingCvmPort

    @property
    def AutoScalingTatCmdStatus(self):
        r"""TAT command status of the CVM used in the auto scaling group
        :rtype: str
        """
        return self._AutoScalingTatCmdStatus

    @AutoScalingTatCmdStatus.setter
    def AutoScalingTatCmdStatus(self, AutoScalingTatCmdStatus):
        self._AutoScalingTatCmdStatus = AutoScalingTatCmdStatus

    @property
    def AutoScalingHookStatus(self):
        r"""CVM auto scaling group lifecycle hook status
        :rtype: str
        """
        return self._AutoScalingHookStatus

    @AutoScalingHookStatus.setter
    def AutoScalingHookStatus(self, AutoScalingHookStatus):
        self._AutoScalingHookStatus = AutoScalingHookStatus

    @property
    def SourceName(self):
        r"""Service source name.
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def RealSourceType(self):
        r"""Precise service source type. Type passed in when creating a service source.
        :rtype: str
        """
        return self._RealSourceType

    @RealSourceType.setter
    def RealSourceType(self, RealSourceType):
        self._RealSourceType = RealSourceType

    @property
    def HealthStatus(self):
        r"""upstream health status HEALTHY (healthy), UNHEALTHY (abnormal), HEALTHCHECKS_OFF (not enabled), and NONE (health checks not supported)
        :rtype: str
        """
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def ScfCamAuthEnable(self):
        r"""Whether CAM authentication is enabled for SCF. Enabled by default (true) when left blank.
        :rtype: bool
        """
        return self._ScfCamAuthEnable

    @ScfCamAuthEnable.setter
    def ScfCamAuthEnable(self, ScfCamAuthEnable):
        self._ScfCamAuthEnable = ScfCamAuthEnable

    @property
    def ScfIsBase64Encoded(self):
        r"""Whether Base64 encoding is enabled for SCF, default false
        :rtype: bool
        """
        return self._ScfIsBase64Encoded

    @ScfIsBase64Encoded.setter
    def ScfIsBase64Encoded(self, ScfIsBase64Encoded):
        self._ScfIsBase64Encoded = ScfIsBase64Encoded

    @property
    def ScfIsIntegratedResponse(self):
        r"""Whether response integration is enabled for the cloud function, default false
        :rtype: bool
        """
        return self._ScfIsIntegratedResponse

    @ScfIsIntegratedResponse.setter
    def ScfIsIntegratedResponse(self, ScfIsIntegratedResponse):
        self._ScfIsIntegratedResponse = ScfIsIntegratedResponse


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._SourceID = params.get("SourceID")
        self._Namespace = params.get("Namespace")
        self._ServiceName = params.get("ServiceName")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = KongTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._SourceType = params.get("SourceType")
        self._ScfType = params.get("ScfType")
        self._ScfNamespace = params.get("ScfNamespace")
        self._ScfLambdaName = params.get("ScfLambdaName")
        self._ScfLambdaQualifier = params.get("ScfLambdaQualifier")
        self._SlowStart = params.get("SlowStart")
        self._Algorithm = params.get("Algorithm")
        self._AutoScalingGroupID = params.get("AutoScalingGroupID")
        self._AutoScalingCvmPort = params.get("AutoScalingCvmPort")
        self._AutoScalingTatCmdStatus = params.get("AutoScalingTatCmdStatus")
        self._AutoScalingHookStatus = params.get("AutoScalingHookStatus")
        self._SourceName = params.get("SourceName")
        self._RealSourceType = params.get("RealSourceType")
        self._HealthStatus = params.get("HealthStatus")
        self._ScfCamAuthEnable = params.get("ScfCamAuthEnable")
        self._ScfIsBase64Encoded = params.get("ScfIsBase64Encoded")
        self._ScfIsIntegratedResponse = params.get("ScfIsIntegratedResponse")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongUpstreamList(AbstractModel):
    r"""kong backend upstream list

    """

    def __init__(self):
        r"""
        :param _UpstreamList: None.
        :type UpstreamList: list of KongUpstreamPreview
        """
        self._UpstreamList = None

    @property
    def UpstreamList(self):
        r"""None.
        :rtype: list of KongUpstreamPreview
        """
        return self._UpstreamList

    @UpstreamList.setter
    def UpstreamList(self, UpstreamList):
        self._UpstreamList = UpstreamList


    def _deserialize(self, params):
        if params.get("UpstreamList") is not None:
            self._UpstreamList = []
            for item in params.get("UpstreamList"):
                obj = KongUpstreamPreview()
                obj._deserialize(item)
                self._UpstreamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongUpstreamPreview(AbstractModel):
    r"""Cloud-native gateway Upstream info

    """

    def __init__(self):
        r"""
        :param _ID: Service ID
        :type ID: str
        :param _Name: Service name.
        :type Name: str
        :param _Target: Backend configuration
        :type Target: list of KongTarget
        """
        self._ID = None
        self._Name = None
        self._Target = None

    @property
    def ID(self):
        r"""Service ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""Service name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Target(self):
        r"""Backend configuration
        :rtype: list of KongTarget
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        if params.get("Target") is not None:
            self._Target = []
            for item in params.get("Target"):
                obj = KongTarget()
                obj._deserialize(item)
                self._Target.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    r"""Tag.

    """

    def __init__(self):
        r"""
        :param _Key: Tag key name
        :type Key: str
        :param _Value: Tag value.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Tag key name
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Tag value.
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
        


class LaneTrafficEntry(AbstractModel):
    r"""lane entrance info

    """

    def __init__(self):
        r"""
        :param _EntryType: // If type == "polarismesh.cn/gateway/tse-gateway", the selector is TSEGatewaySelector.
// type == "polarismesh.cn/gateway/spring-cloud-gateway", selector is ServiceGatewaySelector
// If type == "polarismesh.cn/service", selector is ServiceSelector
Note: This field may return null, indicating that no valid values can be obtained.
        :type EntryType: str
        :param _TSEGatewaySelector: TSE cloud-native gateway selector
Note: This field may return null, indicating that no valid values can be obtained.
        :type TSEGatewaySelector: :class:`tencentcloud.tse.v20201207.models.TSEGatewaySelector`
        :param _ServiceGatewaySelector: Microservice gateway selector
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceGatewaySelector: :class:`tencentcloud.tse.v20201207.models.ServiceGatewaySelector`
        :param _ServiceSelector: Standard microservice selector
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceSelector: :class:`tencentcloud.tse.v20201207.models.ServiceSelector`
        """
        self._EntryType = None
        self._TSEGatewaySelector = None
        self._ServiceGatewaySelector = None
        self._ServiceSelector = None

    @property
    def EntryType(self):
        r"""// If type == "polarismesh.cn/gateway/tse-gateway", the selector is TSEGatewaySelector.
// type == "polarismesh.cn/gateway/spring-cloud-gateway", selector is ServiceGatewaySelector
// If type == "polarismesh.cn/service", selector is ServiceSelector
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EntryType

    @EntryType.setter
    def EntryType(self, EntryType):
        self._EntryType = EntryType

    @property
    def TSEGatewaySelector(self):
        r"""TSE cloud-native gateway selector
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tse.v20201207.models.TSEGatewaySelector`
        """
        return self._TSEGatewaySelector

    @TSEGatewaySelector.setter
    def TSEGatewaySelector(self, TSEGatewaySelector):
        self._TSEGatewaySelector = TSEGatewaySelector

    @property
    def ServiceGatewaySelector(self):
        r"""Microservice gateway selector
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tse.v20201207.models.ServiceGatewaySelector`
        """
        return self._ServiceGatewaySelector

    @ServiceGatewaySelector.setter
    def ServiceGatewaySelector(self, ServiceGatewaySelector):
        self._ServiceGatewaySelector = ServiceGatewaySelector

    @property
    def ServiceSelector(self):
        r"""Standard microservice selector
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tse.v20201207.models.ServiceSelector`
        """
        return self._ServiceSelector

    @ServiceSelector.setter
    def ServiceSelector(self, ServiceSelector):
        self._ServiceSelector = ServiceSelector


    def _deserialize(self, params):
        self._EntryType = params.get("EntryType")
        if params.get("TSEGatewaySelector") is not None:
            self._TSEGatewaySelector = TSEGatewaySelector()
            self._TSEGatewaySelector._deserialize(params.get("TSEGatewaySelector"))
        if params.get("ServiceGatewaySelector") is not None:
            self._ServiceGatewaySelector = ServiceGatewaySelector()
            self._ServiceGatewaySelector._deserialize(params.get("ServiceGatewaySelector"))
        if params.get("ServiceSelector") is not None:
            self._ServiceSelector = ServiceSelector()
            self._ServiceSelector._deserialize(params.get("ServiceSelector"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LimitRule(AbstractModel):
    r"""Parameter throttling rule

    """

    def __init__(self):
        r"""
        :param _Filters: Request matching conditions
        :type Filters: list of RuleFilter
        :param _LimitBy: Parameter throttling based on composite
        :type LimitBy: list of KeyValue
        :param _QpsThresholds: Throttling threshold
        :type QpsThresholds: list of QpsThreshold
        :param _AccurateQpsThresholds: Precise throttling threshold
        :type AccurateQpsThresholds: list of AccurateQpsThreshold
        """
        self._Filters = None
        self._LimitBy = None
        self._QpsThresholds = None
        self._AccurateQpsThresholds = None

    @property
    def Filters(self):
        r"""Request matching conditions
        :rtype: list of RuleFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def LimitBy(self):
        r"""Parameter throttling based on composite
        :rtype: list of KeyValue
        """
        return self._LimitBy

    @LimitBy.setter
    def LimitBy(self, LimitBy):
        self._LimitBy = LimitBy

    @property
    def QpsThresholds(self):
        r"""Throttling threshold
        :rtype: list of QpsThreshold
        """
        return self._QpsThresholds

    @QpsThresholds.setter
    def QpsThresholds(self, QpsThresholds):
        self._QpsThresholds = QpsThresholds

    @property
    def AccurateQpsThresholds(self):
        r"""Precise throttling threshold
        :rtype: list of AccurateQpsThreshold
        """
        return self._AccurateQpsThresholds

    @AccurateQpsThresholds.setter
    def AccurateQpsThresholds(self, AccurateQpsThresholds):
        self._AccurateQpsThresholds = AccurateQpsThresholds


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = RuleFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("LimitBy") is not None:
            self._LimitBy = []
            for item in params.get("LimitBy"):
                obj = KeyValue()
                obj._deserialize(item)
                self._LimitBy.append(obj)
        if params.get("QpsThresholds") is not None:
            self._QpsThresholds = []
            for item in params.get("QpsThresholds"):
                obj = QpsThreshold()
                obj._deserialize(item)
                self._QpsThresholds.append(obj)
        if params.get("AccurateQpsThresholds") is not None:
            self._AccurateQpsThresholds = []
            for item in params.get("AccurateQpsThresholds"):
                obj = AccurateQpsThreshold()
                obj._deserialize(item)
                self._AccurateQpsThresholds.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCloudNativeAPIGatewayResult(AbstractModel):
    r"""Retrieve the response result of the Cloud Native API gateway instance list.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total quantity.
        :type TotalCount: int
        :param _GatewayList: Cloud Native API gateway instance list.
        :type GatewayList: list of DescribeCloudNativeAPIGatewayResult
        """
        self._TotalCount = None
        self._GatewayList = None

    @property
    def TotalCount(self):
        r"""Total quantity.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def GatewayList(self):
        r"""Cloud Native API gateway instance list.
        :rtype: list of DescribeCloudNativeAPIGatewayResult
        """
        return self._GatewayList

    @GatewayList.setter
    def GatewayList(self, GatewayList):
        self._GatewayList = GatewayList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("GatewayList") is not None:
            self._GatewayList = []
            for item in params.get("GatewayList"):
                obj = DescribeCloudNativeAPIGatewayResult()
                obj._deserialize(item)
                self._GatewayList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCloudNativeAPIGatewayStrategyBindingGroupInfoResult(AbstractModel):
    r"""Retrieve the response result of the gateway grouping list bound to the instance policy for a cloud-native API gateway.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Quantity.
        :type TotalCount: int
        :param _GroupInfos: Cloud native API gateway instance policy binding gateway grouping list
        :type GroupInfos: list of CloudNativeAPIGatewayStrategyBindingGroupInfo
        """
        self._TotalCount = None
        self._GroupInfos = None

    @property
    def TotalCount(self):
        r"""Quantity.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def GroupInfos(self):
        r"""Cloud native API gateway instance policy binding gateway grouping list
        :rtype: list of CloudNativeAPIGatewayStrategyBindingGroupInfo
        """
        return self._GroupInfos

    @GroupInfos.setter
    def GroupInfos(self, GroupInfos):
        self._GroupInfos = GroupInfos


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("GroupInfos") is not None:
            self._GroupInfos = []
            for item in params.get("GroupInfos"):
                obj = CloudNativeAPIGatewayStrategyBindingGroupInfo()
                obj._deserialize(item)
                self._GroupInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCloudNativeAPIGatewayStrategyResult(AbstractModel):
    r"""Retrieve the response result of the Cloud Native API gateway instance policy.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total quantity.
        :type TotalCount: int
        :param _StrategyList: Cloud Native API gateway instance policy list.
        :type StrategyList: list of CloudNativeAPIGatewayStrategy
        """
        self._TotalCount = None
        self._StrategyList = None

    @property
    def TotalCount(self):
        r"""Total quantity.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def StrategyList(self):
        r"""Cloud Native API gateway instance policy list.
        :rtype: list of CloudNativeAPIGatewayStrategy
        """
        return self._StrategyList

    @StrategyList.setter
    def StrategyList(self, StrategyList):
        self._StrategyList = StrategyList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("StrategyList") is not None:
            self._StrategyList = []
            for item in params.get("StrategyList"):
                obj = CloudNativeAPIGatewayStrategy()
                obj._deserialize(item)
                self._StrategyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListFilter(AbstractModel):
    r"""Filter conditions, fuzzy matching

    """

    def __init__(self):
        r"""
        :param _Key: Filter fields
        :type Key: str
        :param _Value: Values after filtering
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Filter fields
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Values after filtering
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
        


class ModifyAutoScalerResourceStrategyRequest(AbstractModel):
    r"""ModifyAutoScalerResourceStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway instance ID
        :type GatewayId: str
        :param _StrategyId: Policy ID
        :type StrategyId: str
        :param _StrategyName: Policy name.
        :type StrategyName: str
        :param _Description: Policy description
        :type Description: str
        :param _Config: Metric scaling configuration
        :type Config: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyAutoScalerConfig`
        :param _CronScalerConfig: Scheduled scaling configuration
        :type CronScalerConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyCronScalerConfig`
        :param _MaxReplicas: Maximum number of nodes
        :type MaxReplicas: int
        :param _CronConfig: Metric scaling configuration
        :type CronConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyCronScalerConfig`
        """
        self._GatewayId = None
        self._StrategyId = None
        self._StrategyName = None
        self._Description = None
        self._Config = None
        self._CronScalerConfig = None
        self._MaxReplicas = None
        self._CronConfig = None

    @property
    def GatewayId(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def StrategyId(self):
        r"""Policy ID
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def StrategyName(self):
        r"""Policy name.
        :rtype: str
        """
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def Description(self):
        r"""Policy description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Config(self):
        r"""Metric scaling configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyAutoScalerConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def CronScalerConfig(self):
        warnings.warn("parameter `CronScalerConfig` is deprecated", DeprecationWarning) 

        r"""Scheduled scaling configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyCronScalerConfig`
        """
        return self._CronScalerConfig

    @CronScalerConfig.setter
    def CronScalerConfig(self, CronScalerConfig):
        warnings.warn("parameter `CronScalerConfig` is deprecated", DeprecationWarning) 

        self._CronScalerConfig = CronScalerConfig

    @property
    def MaxReplicas(self):
        warnings.warn("parameter `MaxReplicas` is deprecated", DeprecationWarning) 

        r"""Maximum number of nodes
        :rtype: int
        """
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        warnings.warn("parameter `MaxReplicas` is deprecated", DeprecationWarning) 

        self._MaxReplicas = MaxReplicas

    @property
    def CronConfig(self):
        r"""Metric scaling configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyCronScalerConfig`
        """
        return self._CronConfig

    @CronConfig.setter
    def CronConfig(self, CronConfig):
        self._CronConfig = CronConfig


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._StrategyId = params.get("StrategyId")
        self._StrategyName = params.get("StrategyName")
        self._Description = params.get("Description")
        if params.get("Config") is not None:
            self._Config = CloudNativeAPIGatewayStrategyAutoScalerConfig()
            self._Config._deserialize(params.get("Config"))
        if params.get("CronScalerConfig") is not None:
            self._CronScalerConfig = CloudNativeAPIGatewayStrategyCronScalerConfig()
            self._CronScalerConfig._deserialize(params.get("CronScalerConfig"))
        self._MaxReplicas = params.get("MaxReplicas")
        if params.get("CronConfig") is not None:
            self._CronConfig = CloudNativeAPIGatewayStrategyCronScalerConfig()
            self._CronConfig._deserialize(params.get("CronConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoScalerResourceStrategyResponse(AbstractModel):
    r"""ModifyAutoScalerResourceStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Success status
        :type Result: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Success status
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyCloudNativeAPIGatewayCanaryRuleRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayCanaryRule request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _ServiceId: Service ID
        :type ServiceId: str
        :param _Priority: Priority. The grayscale rule priority of a service is unique.
        :type Priority: int
        :param _CanaryRule: Grayscale rule configuration
        :type CanaryRule: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayCanaryRule`
        :param _CanaryRuleList: Grayscale rule configuration list. If configured, this parameter takes precedence and the Priority and CanaryRule parameters are ignored.
        :type CanaryRuleList: list of CanaryPriorityRule
        """
        self._GatewayId = None
        self._ServiceId = None
        self._Priority = None
        self._CanaryRule = None
        self._CanaryRuleList = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServiceId(self):
        r"""Service ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Priority(self):
        r"""Priority. The grayscale rule priority of a service is unique.
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def CanaryRule(self):
        r"""Grayscale rule configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayCanaryRule`
        """
        return self._CanaryRule

    @CanaryRule.setter
    def CanaryRule(self, CanaryRule):
        self._CanaryRule = CanaryRule

    @property
    def CanaryRuleList(self):
        r"""Grayscale rule configuration list. If configured, this parameter takes precedence and the Priority and CanaryRule parameters are ignored.
        :rtype: list of CanaryPriorityRule
        """
        return self._CanaryRuleList

    @CanaryRuleList.setter
    def CanaryRuleList(self, CanaryRuleList):
        self._CanaryRuleList = CanaryRuleList


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServiceId = params.get("ServiceId")
        self._Priority = params.get("Priority")
        if params.get("CanaryRule") is not None:
            self._CanaryRule = CloudNativeAPIGatewayCanaryRule()
            self._CanaryRule._deserialize(params.get("CanaryRule"))
        if params.get("CanaryRuleList") is not None:
            self._CanaryRuleList = []
            for item in params.get("CanaryRuleList"):
                obj = CanaryPriorityRule()
                obj._deserialize(item)
                self._CanaryRuleList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayCanaryRuleResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayCanaryRule response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCloudNativeAPIGatewayCertificateRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: gateway ID
        :type GatewayId: str
        :param _Id: Certificate ID.
        :type Id: str
        :param _Name: Certificate name, will already be deprecated
        :type Name: str
        :param _Key: Certificate private key. Required when CertSource is native.
        :type Key: str
        :param _Crt: Certificate in pem format. Required when CertSource is native.
        :type Crt: str
        :param _BindDomains: Bound domain names will already be deprecated
        :type BindDomains: list of str
        :param _CertId: ssl platform cert Id. Required when CertSource is ssl.
        :type CertId: str
        :param _CertSource: Certificate source
-ssl (Platform Cert), default value
-native (kong custom certificate) 

        :type CertSource: str
        """
        self._GatewayId = None
        self._Id = None
        self._Name = None
        self._Key = None
        self._Crt = None
        self._BindDomains = None
        self._CertId = None
        self._CertSource = None

    @property
    def GatewayId(self):
        r"""gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Id(self):
        r"""Certificate ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        warnings.warn("parameter `Name` is deprecated", DeprecationWarning) 

        r"""Certificate name, will already be deprecated
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        warnings.warn("parameter `Name` is deprecated", DeprecationWarning) 

        self._Name = Name

    @property
    def Key(self):
        r"""Certificate private key. Required when CertSource is native.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Crt(self):
        r"""Certificate in pem format. Required when CertSource is native.
        :rtype: str
        """
        return self._Crt

    @Crt.setter
    def Crt(self, Crt):
        self._Crt = Crt

    @property
    def BindDomains(self):
        warnings.warn("parameter `BindDomains` is deprecated", DeprecationWarning) 

        r"""Bound domain names will already be deprecated
        :rtype: list of str
        """
        return self._BindDomains

    @BindDomains.setter
    def BindDomains(self, BindDomains):
        warnings.warn("parameter `BindDomains` is deprecated", DeprecationWarning) 

        self._BindDomains = BindDomains

    @property
    def CertId(self):
        r"""ssl platform cert Id. Required when CertSource is ssl.
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertSource(self):
        r"""Certificate source
-ssl (Platform Cert), default value
-native (kong custom certificate) 

        :rtype: str
        """
        return self._CertSource

    @CertSource.setter
    def CertSource(self, CertSource):
        self._CertSource = CertSource


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Key = params.get("Key")
        self._Crt = params.get("Crt")
        self._BindDomains = params.get("BindDomains")
        self._CertId = params.get("CertId")
        self._CertSource = params.get("CertSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayCertificateResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayCertificate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCloudNativeAPIGatewayRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGateway request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud native API gateway instance ID.
        :type GatewayId: str
        :param _Name: Cloud Native API Gateway name, supports up to 60 characters.
        :type Name: str
        :param _Description: Cloud native API gateway description, supports up to 120 characters.
        :type Description: str
        :param _EnableCls: Whether CLS log is enabled. The value can only be true temporarily, meaning it can only be changed from disabled to enabled.
        :type EnableCls: bool
        :param _InternetPayMode: Public network billing mode. Option values: BANDWIDTH | TRAFFIC, which means billing by bandwidth or by traffic.
        :type InternetPayMode: str
        :param _DeleteProtect: Enable instance deletion protection, default false
        :type DeleteProtect: bool
        """
        self._GatewayId = None
        self._Name = None
        self._Description = None
        self._EnableCls = None
        self._InternetPayMode = None
        self._DeleteProtect = None

    @property
    def GatewayId(self):
        r"""Cloud native API gateway instance ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""Cloud Native API Gateway name, supports up to 60 characters.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""Cloud native API gateway description, supports up to 120 characters.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EnableCls(self):
        r"""Whether CLS log is enabled. The value can only be true temporarily, meaning it can only be changed from disabled to enabled.
        :rtype: bool
        """
        return self._EnableCls

    @EnableCls.setter
    def EnableCls(self, EnableCls):
        self._EnableCls = EnableCls

    @property
    def InternetPayMode(self):
        r"""Public network billing mode. Option values: BANDWIDTH | TRAFFIC, which means billing by bandwidth or by traffic.
        :rtype: str
        """
        return self._InternetPayMode

    @InternetPayMode.setter
    def InternetPayMode(self, InternetPayMode):
        self._InternetPayMode = InternetPayMode

    @property
    def DeleteProtect(self):
        r"""Enable instance deletion protection, default false
        :rtype: bool
        """
        return self._DeleteProtect

    @DeleteProtect.setter
    def DeleteProtect(self, DeleteProtect):
        self._DeleteProtect = DeleteProtect


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._EnableCls = params.get("EnableCls")
        self._InternetPayMode = params.get("InternetPayMode")
        self._DeleteProtect = params.get("DeleteProtect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGateway response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCloudNativeAPIGatewayRouteRateLimitRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayRouteRateLimit request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: gateway ID
        :type GatewayId: str
        :param _Id: Route id or routing name.
"Unnamed" is not supported.
        :type Id: str
        :param _LimitDetail: Configure stream
        :type LimitDetail: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        """
        self._GatewayId = None
        self._Id = None
        self._LimitDetail = None

    @property
    def GatewayId(self):
        r"""gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Id(self):
        r"""Route id or routing name.
"Unnamed" is not supported.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def LimitDetail(self):
        r"""Configure stream
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        """
        return self._LimitDetail

    @LimitDetail.setter
    def LimitDetail(self, LimitDetail):
        self._LimitDetail = LimitDetail


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Id = params.get("Id")
        if params.get("LimitDetail") is not None:
            self._LimitDetail = CloudNativeAPIGatewayRateLimitDetail()
            self._LimitDetail._deserialize(params.get("LimitDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayRouteRateLimitResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayRouteRateLimit response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCloudNativeAPIGatewayRouteRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayRoute request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: gateway ID
        :type GatewayId: str
        :param _ServiceID: ID of the associated service
        :type ServiceID: str
        :param _RouteID: Route ID, unique at the instance level
        :type RouteID: str
        :param _RouteName: Route name, unique at the instance level, does not provide
        :type RouteName: str
        :param _Methods: Route method. Available values:
- GET
- POST
- DELETE
- PUT
- OPTIONS
- PATCH
- HEAD
- ANY
- TRACE
- COPY
- MOVE
- PROPFIND
- PROPPATCH
- MKCOL
- LOCK
- UNLOCK
        :type Methods: list of str
        :param _Hosts: Domain name of the route
        :type Hosts: list of str
        :param _Paths: Path of the route
        :type Paths: list of str
        :param _Protocols: Route protocol, selectable
- https
- http
        :type Protocols: list of str
        :param _PreserveHost: Preserve Host when forwarding to backend
        :type PreserveHost: bool
        :param _HttpsRedirectStatusCode: HTTP redirection status code
        :type HttpsRedirectStatusCode: int
        :param _StripPath: StripPath when forwarding to backend
        :type StripPath: bool
        :param _ForceHttps: Whether to enable mandatory HTTPS
        :type ForceHttps: bool
        :param _DestinationPorts: Destination port for Layer 4 match	
        :type DestinationPorts: list of int non-negative
        :param _Headers: Headers of the route
        :type Headers: list of KVMapping
        :param _RequestBuffering: Whether to cache the request body, default true
        :type RequestBuffering: bool
        :param _ResponseBuffering: Whether to cache response body, default true
        :type ResponseBuffering: bool
        :param _RegexPriority: Add priority
        :type RegexPriority: int
        :param _QueryStringParameters: QueryString parameter
        :type QueryStringParameters: list of KVMapping
        """
        self._GatewayId = None
        self._ServiceID = None
        self._RouteID = None
        self._RouteName = None
        self._Methods = None
        self._Hosts = None
        self._Paths = None
        self._Protocols = None
        self._PreserveHost = None
        self._HttpsRedirectStatusCode = None
        self._StripPath = None
        self._ForceHttps = None
        self._DestinationPorts = None
        self._Headers = None
        self._RequestBuffering = None
        self._ResponseBuffering = None
        self._RegexPriority = None
        self._QueryStringParameters = None

    @property
    def GatewayId(self):
        r"""gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServiceID(self):
        r"""ID of the associated service
        :rtype: str
        """
        return self._ServiceID

    @ServiceID.setter
    def ServiceID(self, ServiceID):
        self._ServiceID = ServiceID

    @property
    def RouteID(self):
        r"""Route ID, unique at the instance level
        :rtype: str
        """
        return self._RouteID

    @RouteID.setter
    def RouteID(self, RouteID):
        self._RouteID = RouteID

    @property
    def RouteName(self):
        r"""Route name, unique at the instance level, does not provide
        :rtype: str
        """
        return self._RouteName

    @RouteName.setter
    def RouteName(self, RouteName):
        self._RouteName = RouteName

    @property
    def Methods(self):
        r"""Route method. Available values:
- GET
- POST
- DELETE
- PUT
- OPTIONS
- PATCH
- HEAD
- ANY
- TRACE
- COPY
- MOVE
- PROPFIND
- PROPPATCH
- MKCOL
- LOCK
- UNLOCK
        :rtype: list of str
        """
        return self._Methods

    @Methods.setter
    def Methods(self, Methods):
        self._Methods = Methods

    @property
    def Hosts(self):
        r"""Domain name of the route
        :rtype: list of str
        """
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def Paths(self):
        r"""Path of the route
        :rtype: list of str
        """
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths

    @property
    def Protocols(self):
        r"""Route protocol, selectable
- https
- http
        :rtype: list of str
        """
        return self._Protocols

    @Protocols.setter
    def Protocols(self, Protocols):
        self._Protocols = Protocols

    @property
    def PreserveHost(self):
        r"""Preserve Host when forwarding to backend
        :rtype: bool
        """
        return self._PreserveHost

    @PreserveHost.setter
    def PreserveHost(self, PreserveHost):
        self._PreserveHost = PreserveHost

    @property
    def HttpsRedirectStatusCode(self):
        r"""HTTP redirection status code
        :rtype: int
        """
        return self._HttpsRedirectStatusCode

    @HttpsRedirectStatusCode.setter
    def HttpsRedirectStatusCode(self, HttpsRedirectStatusCode):
        self._HttpsRedirectStatusCode = HttpsRedirectStatusCode

    @property
    def StripPath(self):
        r"""StripPath when forwarding to backend
        :rtype: bool
        """
        return self._StripPath

    @StripPath.setter
    def StripPath(self, StripPath):
        self._StripPath = StripPath

    @property
    def ForceHttps(self):
        warnings.warn("parameter `ForceHttps` is deprecated", DeprecationWarning) 

        r"""Whether to enable mandatory HTTPS
        :rtype: bool
        """
        return self._ForceHttps

    @ForceHttps.setter
    def ForceHttps(self, ForceHttps):
        warnings.warn("parameter `ForceHttps` is deprecated", DeprecationWarning) 

        self._ForceHttps = ForceHttps

    @property
    def DestinationPorts(self):
        r"""Destination port for Layer 4 match	
        :rtype: list of int non-negative
        """
        return self._DestinationPorts

    @DestinationPorts.setter
    def DestinationPorts(self, DestinationPorts):
        self._DestinationPorts = DestinationPorts

    @property
    def Headers(self):
        r"""Headers of the route
        :rtype: list of KVMapping
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def RequestBuffering(self):
        r"""Whether to cache the request body, default true
        :rtype: bool
        """
        return self._RequestBuffering

    @RequestBuffering.setter
    def RequestBuffering(self, RequestBuffering):
        self._RequestBuffering = RequestBuffering

    @property
    def ResponseBuffering(self):
        r"""Whether to cache response body, default true
        :rtype: bool
        """
        return self._ResponseBuffering

    @ResponseBuffering.setter
    def ResponseBuffering(self, ResponseBuffering):
        self._ResponseBuffering = ResponseBuffering

    @property
    def RegexPriority(self):
        r"""Add priority
        :rtype: int
        """
        return self._RegexPriority

    @RegexPriority.setter
    def RegexPriority(self, RegexPriority):
        self._RegexPriority = RegexPriority

    @property
    def QueryStringParameters(self):
        r"""QueryString parameter
        :rtype: list of KVMapping
        """
        return self._QueryStringParameters

    @QueryStringParameters.setter
    def QueryStringParameters(self, QueryStringParameters):
        self._QueryStringParameters = QueryStringParameters


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServiceID = params.get("ServiceID")
        self._RouteID = params.get("RouteID")
        self._RouteName = params.get("RouteName")
        self._Methods = params.get("Methods")
        self._Hosts = params.get("Hosts")
        self._Paths = params.get("Paths")
        self._Protocols = params.get("Protocols")
        self._PreserveHost = params.get("PreserveHost")
        self._HttpsRedirectStatusCode = params.get("HttpsRedirectStatusCode")
        self._StripPath = params.get("StripPath")
        self._ForceHttps = params.get("ForceHttps")
        self._DestinationPorts = params.get("DestinationPorts")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = KVMapping()
                obj._deserialize(item)
                self._Headers.append(obj)
        self._RequestBuffering = params.get("RequestBuffering")
        self._ResponseBuffering = params.get("ResponseBuffering")
        self._RegexPriority = params.get("RegexPriority")
        if params.get("QueryStringParameters") is not None:
            self._QueryStringParameters = []
            for item in params.get("QueryStringParameters"):
                obj = KVMapping()
                obj._deserialize(item)
                self._QueryStringParameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayRouteResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayRoute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCloudNativeAPIGatewayServiceRateLimitRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayServiceRateLimit request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _Name: Service name or service ID
        :type Name: str
        :param _LimitDetail: Configure throttling
        :type LimitDetail: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        """
        self._GatewayId = None
        self._Name = None
        self._LimitDetail = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""Service name or service ID
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LimitDetail(self):
        r"""Configure throttling
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        """
        return self._LimitDetail

    @LimitDetail.setter
    def LimitDetail(self, LimitDetail):
        self._LimitDetail = LimitDetail


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        if params.get("LimitDetail") is not None:
            self._LimitDetail = CloudNativeAPIGatewayRateLimitDetail()
            self._LimitDetail._deserialize(params.get("LimitDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayServiceRateLimitResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayServiceRateLimit response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCloudNativeAPIGatewayServiceRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayService request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _Name: Service name
        :type Name: str
        :param _Protocol: Request protocol: 
- https 
- http 
- tcp 
- udp
        :type Protocol: str
        :param _Timeout: Timeout interval. Unit: ms
        :type Timeout: int
        :param _Retries: Number of retries.
        :type Retries: int
        :param _UpstreamType: Service type 
- Kubernetes 
- Registry
- IPList
- HostIP
- Scf	
        :type UpstreamType: str
        :param _UpstreamInfo: service configuration
        :type UpstreamInfo: :class:`tencentcloud.tse.v20201207.models.KongUpstreamInfo`
        :param _ID: service ID
        :type ID: str
        :param _Path: Request path
        :type Path: str
        """
        self._GatewayId = None
        self._Name = None
        self._Protocol = None
        self._Timeout = None
        self._Retries = None
        self._UpstreamType = None
        self._UpstreamInfo = None
        self._ID = None
        self._Path = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""Service name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Protocol(self):
        r"""Request protocol: 
- https 
- http 
- tcp 
- udp
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Timeout(self):
        r"""Timeout interval. Unit: ms
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Retries(self):
        r"""Number of retries.
        :rtype: int
        """
        return self._Retries

    @Retries.setter
    def Retries(self, Retries):
        self._Retries = Retries

    @property
    def UpstreamType(self):
        r"""Service type 
- Kubernetes 
- Registry
- IPList
- HostIP
- Scf	
        :rtype: str
        """
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def UpstreamInfo(self):
        r"""service configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.KongUpstreamInfo`
        """
        return self._UpstreamInfo

    @UpstreamInfo.setter
    def UpstreamInfo(self, UpstreamInfo):
        self._UpstreamInfo = UpstreamInfo

    @property
    def ID(self):
        r"""service ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Path(self):
        r"""Request path
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        self._Protocol = params.get("Protocol")
        self._Timeout = params.get("Timeout")
        self._Retries = params.get("Retries")
        self._UpstreamType = params.get("UpstreamType")
        if params.get("UpstreamInfo") is not None:
            self._UpstreamInfo = KongUpstreamInfo()
            self._UpstreamInfo._deserialize(params.get("UpstreamInfo"))
        self._ID = params.get("ID")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayServiceResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayService response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyConsoleNetworkRequest(AbstractModel):
    r"""ModifyConsoleNetwork request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud Native API gateway instance ID.
        :type GatewayId: str
        :param _NetworkType: Network type:
-Open public network
-Internal private network (not currently supported)
        :type NetworkType: str
        :param _Operate: Enable the Konga network. Default is Open.
-Open
- Close: disabled.
        :type Operate: str
        :param _AccessControl: Access control policy
        :type AccessControl: :class:`tencentcloud.tse.v20201207.models.NetworkAccessControl`
        """
        self._GatewayId = None
        self._NetworkType = None
        self._Operate = None
        self._AccessControl = None

    @property
    def GatewayId(self):
        r"""Cloud Native API gateway instance ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def NetworkType(self):
        r"""Network type:
-Open public network
-Internal private network (not currently supported)
        :rtype: str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def Operate(self):
        r"""Enable the Konga network. Default is Open.
-Open
- Close: disabled.
        :rtype: str
        """
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate

    @property
    def AccessControl(self):
        r"""Access control policy
        :rtype: :class:`tencentcloud.tse.v20201207.models.NetworkAccessControl`
        """
        return self._AccessControl

    @AccessControl.setter
    def AccessControl(self, AccessControl):
        self._AccessControl = AccessControl


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._NetworkType = params.get("NetworkType")
        self._Operate = params.get("Operate")
        if params.get("AccessControl") is not None:
            self._AccessControl = NetworkAccessControl()
            self._AccessControl._deserialize(params.get("AccessControl"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConsoleNetworkResponse(AbstractModel):
    r"""ModifyConsoleNetwork response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyGovernanceLaneGroupsRequest(AbstractModel):
    r"""ModifyGovernanceLaneGroups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Engine Instance ID
        :type InstanceId: str
        :param _LaneGroups: Lane group rule list
        :type LaneGroups: list of GovernanceLaneGroup
        """
        self._InstanceId = None
        self._LaneGroups = None

    @property
    def InstanceId(self):
        r"""Engine Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LaneGroups(self):
        r"""Lane group rule list
        :rtype: list of GovernanceLaneGroup
        """
        return self._LaneGroups

    @LaneGroups.setter
    def LaneGroups(self, LaneGroups):
        self._LaneGroups = LaneGroups


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("LaneGroups") is not None:
            self._LaneGroups = []
            for item in params.get("LaneGroups"):
                obj = GovernanceLaneGroup()
                obj._deserialize(item)
                self._LaneGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGovernanceLaneGroupsResponse(AbstractModel):
    r"""ModifyGovernanceLaneGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the creation succeeded
        :type Result: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Whether the creation succeeded
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyNativeGatewayServerGroupRequest(AbstractModel):
    r"""ModifyNativeGatewayServerGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud Native API gateway instance ID.
        :type GatewayId: str
        :param _GroupId: gateway group id
        :type GroupId: str
        :param _Name: Cloud native API gateway name supports up to 60 characters.
        :type Name: str
        :param _Description: Cloud native API gateway description supports up to 120 characters.
        :type Description: str
        """
        self._GatewayId = None
        self._GroupId = None
        self._Name = None
        self._Description = None

    @property
    def GatewayId(self):
        r"""Cloud Native API gateway instance ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        r"""gateway group id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Name(self):
        r"""Cloud native API gateway name supports up to 60 characters.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""Cloud native API gateway description supports up to 120 characters.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNativeGatewayServerGroupResponse(AbstractModel):
    r"""ModifyNativeGatewayServerGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyNativeGatewayServiceSourceRequest(AbstractModel):
    r"""ModifyNativeGatewayServiceSource request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayID: Gateway instance ID
        :type GatewayID: str
        :param _SourceID: Service Source Instance ID
        :type SourceID: str
        :param _SourceName: Service Source Name
        :type SourceName: str
        :param _SourceInfo: Service source instance additional information
        :type SourceInfo: :class:`tencentcloud.tse.v20201207.models.SourceInfo`
        """
        self._GatewayID = None
        self._SourceID = None
        self._SourceName = None
        self._SourceInfo = None

    @property
    def GatewayID(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayID

    @GatewayID.setter
    def GatewayID(self, GatewayID):
        self._GatewayID = GatewayID

    @property
    def SourceID(self):
        r"""Service Source Instance ID
        :rtype: str
        """
        return self._SourceID

    @SourceID.setter
    def SourceID(self, SourceID):
        self._SourceID = SourceID

    @property
    def SourceName(self):
        r"""Service Source Name
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def SourceInfo(self):
        r"""Service source instance additional information
        :rtype: :class:`tencentcloud.tse.v20201207.models.SourceInfo`
        """
        return self._SourceInfo

    @SourceInfo.setter
    def SourceInfo(self, SourceInfo):
        self._SourceInfo = SourceInfo


    def _deserialize(self, params):
        self._GatewayID = params.get("GatewayID")
        self._SourceID = params.get("SourceID")
        self._SourceName = params.get("SourceName")
        if params.get("SourceInfo") is not None:
            self._SourceInfo = SourceInfo()
            self._SourceInfo._deserialize(params.get("SourceInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNativeGatewayServiceSourceResponse(AbstractModel):
    r"""ModifyNativeGatewayServiceSource response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyNetworkAccessStrategyRequest(AbstractModel):
    r"""ModifyNetworkAccessStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud Native API gateway instance ID.
        :type GatewayId: str
        :param _GroupId: Group ID
        :type GroupId: str
        :param _NetworkType: Network type: 
-Open public network
-Internal private network (not currently supported)
        :type NetworkType: str
        :param _Vip: IP address
        :type Vip: str
        :param _AccessControl: Access control policy
        :type AccessControl: :class:`tencentcloud.tse.v20201207.models.NetworkAccessControl`
        """
        self._GatewayId = None
        self._GroupId = None
        self._NetworkType = None
        self._Vip = None
        self._AccessControl = None

    @property
    def GatewayId(self):
        r"""Cloud Native API gateway instance ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        r"""Group ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def NetworkType(self):
        r"""Network type: 
-Open public network
-Internal private network (not currently supported)
        :rtype: str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def Vip(self):
        r"""IP address
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def AccessControl(self):
        r"""Access control policy
        :rtype: :class:`tencentcloud.tse.v20201207.models.NetworkAccessControl`
        """
        return self._AccessControl

    @AccessControl.setter
    def AccessControl(self, AccessControl):
        self._AccessControl = AccessControl


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._NetworkType = params.get("NetworkType")
        self._Vip = params.get("Vip")
        if params.get("AccessControl") is not None:
            self._AccessControl = NetworkAccessControl()
            self._AccessControl._deserialize(params.get("AccessControl"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetworkAccessStrategyResponse(AbstractModel):
    r"""ModifyNetworkAccessStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyNetworkBasicInfoRequest(AbstractModel):
    r"""ModifyNetworkBasicInfo request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud Native API gateway instance ID.
        :type GatewayId: str
        :param _GroupId: Group ID
        :type GroupId: str
        :param _NetworkType: Network type:
-Enable public IP address
-Public IPv6 address
-Internal private network
        :type NetworkType: str
        :param _Vip: IP address
        :type Vip: str
        :param _InternetMaxBandwidthOut: Public network outbound traffic bandwidth, [1,2048]Mbps
        :type InternetMaxBandwidthOut: int
        :param _Description: Description of load balancing
        :type Description: str
        :param _SlaType: Load balancing specification types support:
-Leave empty for shared type.
-clb.c2.medium: standard specification
-clb.c3.small: High-performance type 1 specification
-clb.c3.medium: High-performance type 2 specification
-clb.c4.small: Super high-performance specification 1
-clb.c4.medium: Super high-performance specification 2
-clb.c4.large: Super high-performance specification 3
-clb.c4.xlarge: Super high-performance 4 specification.
        :type SlaType: str
        """
        self._GatewayId = None
        self._GroupId = None
        self._NetworkType = None
        self._Vip = None
        self._InternetMaxBandwidthOut = None
        self._Description = None
        self._SlaType = None

    @property
    def GatewayId(self):
        r"""Cloud Native API gateway instance ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        r"""Group ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def NetworkType(self):
        r"""Network type:
-Enable public IP address
-Public IPv6 address
-Internal private network
        :rtype: str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def Vip(self):
        r"""IP address
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def InternetMaxBandwidthOut(self):
        r"""Public network outbound traffic bandwidth, [1,2048]Mbps
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def Description(self):
        r"""Description of load balancing
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SlaType(self):
        r"""Load balancing specification types support:
-Leave empty for shared type.
-clb.c2.medium: standard specification
-clb.c3.small: High-performance type 1 specification
-clb.c3.medium: High-performance type 2 specification
-clb.c4.small: Super high-performance specification 1
-clb.c4.medium: Super high-performance specification 2
-clb.c4.large: Super high-performance specification 3
-clb.c4.xlarge: Super high-performance 4 specification.
        :rtype: str
        """
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._NetworkType = params.get("NetworkType")
        self._Vip = params.get("Vip")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._Description = params.get("Description")
        self._SlaType = params.get("SlaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetworkBasicInfoResponse(AbstractModel):
    r"""ModifyNetworkBasicInfo response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyUpstreamNodeStatusRequest(AbstractModel):
    r"""ModifyUpstreamNodeStatus request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway instance ID
        :type GatewayId: str
        :param _ServiceName: Service name
        :type ServiceName: str
        :param _Host: Access IP address or domain name
        :type Host: str
        :param _Port: Access Port
        :type Port: int
        :param _Status: HEALTHY or UNHEALTHY
        :type Status: str
        """
        self._GatewayId = None
        self._ServiceName = None
        self._Host = None
        self._Port = None
        self._Status = None

    @property
    def GatewayId(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServiceName(self):
        r"""Service name
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Host(self):
        r"""Access IP address or domain name
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        r"""Access Port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Status(self):
        r"""HEALTHY or UNHEALTHY
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServiceName = params.get("ServiceName")
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUpstreamNodeStatusResponse(AbstractModel):
    r"""ModifyUpstreamNodeStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Success status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Success status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class NativeGatewayServerGroup(AbstractModel):
    r"""Cloud-Native Gateway Group Information

    """

    def __init__(self):
        r"""
        :param _GroupId: Cloud-Native Gateway Group Unique id
        :type GroupId: str
        :param _Name: Group name
        :type Name: str
        :param _Description: Description information
        :type Description: str
        :param _NodeConfig: Node specification, number of nodes info
        :type NodeConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        :param _Status: Gateway group status.
        :type Status: str
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _IsFirstGroup: Whether it is the default group.
0: No.
1: Yes.
        :type IsFirstGroup: int
        :param _BindingStrategy: Associate policy information
        :type BindingStrategy: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategy`
        :param _GatewayId: Gateway instance ID.
        :type GatewayId: str
        :param _InternetMaxBandwidthOut: Bandwidth
        :type InternetMaxBandwidthOut: int
        :param _ModifyTime: Modification time.
        :type ModifyTime: str
        :param _SubnetIds: Subnet ID
        :type SubnetIds: str
        :param _DefaultWeight: Default weight of the group
        :type DefaultWeight: int
        :param _ElasticNumber: elastic node
        :type ElasticNumber: int
        :param _SupportTOA: Whether TOA is supported
        :type SupportTOA: bool
        :param _SupportIPV6: Whether IPV6 is supported
        :type SupportIPV6: bool
        """
        self._GroupId = None
        self._Name = None
        self._Description = None
        self._NodeConfig = None
        self._Status = None
        self._CreateTime = None
        self._IsFirstGroup = None
        self._BindingStrategy = None
        self._GatewayId = None
        self._InternetMaxBandwidthOut = None
        self._ModifyTime = None
        self._SubnetIds = None
        self._DefaultWeight = None
        self._ElasticNumber = None
        self._SupportTOA = None
        self._SupportIPV6 = None

    @property
    def GroupId(self):
        r"""Cloud-Native Gateway Group Unique id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Name(self):
        r"""Group name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""Description information
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def NodeConfig(self):
        r"""Node specification, number of nodes info
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        """
        return self._NodeConfig

    @NodeConfig.setter
    def NodeConfig(self, NodeConfig):
        self._NodeConfig = NodeConfig

    @property
    def Status(self):
        r"""Gateway group status.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsFirstGroup(self):
        r"""Whether it is the default group.
0: No.
1: Yes.
        :rtype: int
        """
        return self._IsFirstGroup

    @IsFirstGroup.setter
    def IsFirstGroup(self, IsFirstGroup):
        self._IsFirstGroup = IsFirstGroup

    @property
    def BindingStrategy(self):
        r"""Associate policy information
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategy`
        """
        return self._BindingStrategy

    @BindingStrategy.setter
    def BindingStrategy(self, BindingStrategy):
        self._BindingStrategy = BindingStrategy

    @property
    def GatewayId(self):
        r"""Gateway instance ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def InternetMaxBandwidthOut(self):
        r"""Bandwidth
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def ModifyTime(self):
        r"""Modification time.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def SubnetIds(self):
        r"""Subnet ID
        :rtype: str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def DefaultWeight(self):
        r"""Default weight of the group
        :rtype: int
        """
        return self._DefaultWeight

    @DefaultWeight.setter
    def DefaultWeight(self, DefaultWeight):
        self._DefaultWeight = DefaultWeight

    @property
    def ElasticNumber(self):
        r"""elastic node
        :rtype: int
        """
        return self._ElasticNumber

    @ElasticNumber.setter
    def ElasticNumber(self, ElasticNumber):
        self._ElasticNumber = ElasticNumber

    @property
    def SupportTOA(self):
        r"""Whether TOA is supported
        :rtype: bool
        """
        return self._SupportTOA

    @SupportTOA.setter
    def SupportTOA(self, SupportTOA):
        self._SupportTOA = SupportTOA

    @property
    def SupportIPV6(self):
        r"""Whether IPV6 is supported
        :rtype: bool
        """
        return self._SupportIPV6

    @SupportIPV6.setter
    def SupportIPV6(self, SupportIPV6):
        self._SupportIPV6 = SupportIPV6


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("NodeConfig") is not None:
            self._NodeConfig = CloudNativeAPIGatewayNodeConfig()
            self._NodeConfig._deserialize(params.get("NodeConfig"))
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._IsFirstGroup = params.get("IsFirstGroup")
        if params.get("BindingStrategy") is not None:
            self._BindingStrategy = CloudNativeAPIGatewayStrategy()
            self._BindingStrategy._deserialize(params.get("BindingStrategy"))
        self._GatewayId = params.get("GatewayId")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._ModifyTime = params.get("ModifyTime")
        self._SubnetIds = params.get("SubnetIds")
        self._DefaultWeight = params.get("DefaultWeight")
        self._ElasticNumber = params.get("ElasticNumber")
        self._SupportTOA = params.get("SupportTOA")
        self._SupportIPV6 = params.get("SupportIPV6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NativeGatewayServerGroups(AbstractModel):
    r"""gateway group list

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number.
        :type TotalCount: int
        :param _GatewayGroupList: Group information array.
        :type GatewayGroupList: list of NativeGatewayServerGroup
        """
        self._TotalCount = None
        self._GatewayGroupList = None

    @property
    def TotalCount(self):
        r"""Total number.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def GatewayGroupList(self):
        r"""Group information array.
        :rtype: list of NativeGatewayServerGroup
        """
        return self._GatewayGroupList

    @GatewayGroupList.setter
    def GatewayGroupList(self, GatewayGroupList):
        self._GatewayGroupList = GatewayGroupList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("GatewayGroupList") is not None:
            self._GatewayGroupList = []
            for item in params.get("GatewayGroupList"):
                obj = NativeGatewayServerGroup()
                obj._deserialize(item)
                self._GatewayGroupList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NativeGatewayServiceSourceItem(AbstractModel):
    r"""Gateway data source description

    """

    def __init__(self):
        r"""
        :param _GatewayID: Gateway instance ID
        :type GatewayID: str
        :param _SourceID: Service Source ID
        :type SourceID: str
        :param _SourceName: Service Source Name
        :type SourceName: str
        :param _SourceType: Service source type
        :type SourceType: str
        :param _SourceInfo: Service source additional information
        :type SourceInfo: :class:`tencentcloud.tse.v20201207.models.SourceInfo`
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _ModifyTime: Modification time.
        :type ModifyTime: str
        """
        self._GatewayID = None
        self._SourceID = None
        self._SourceName = None
        self._SourceType = None
        self._SourceInfo = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def GatewayID(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayID

    @GatewayID.setter
    def GatewayID(self, GatewayID):
        self._GatewayID = GatewayID

    @property
    def SourceID(self):
        r"""Service Source ID
        :rtype: str
        """
        return self._SourceID

    @SourceID.setter
    def SourceID(self, SourceID):
        self._SourceID = SourceID

    @property
    def SourceName(self):
        r"""Service Source Name
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def SourceType(self):
        r"""Service source type
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceInfo(self):
        r"""Service source additional information
        :rtype: :class:`tencentcloud.tse.v20201207.models.SourceInfo`
        """
        return self._SourceInfo

    @SourceInfo.setter
    def SourceInfo(self, SourceInfo):
        self._SourceInfo = SourceInfo

    @property
    def CreateTime(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        r"""Modification time.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._GatewayID = params.get("GatewayID")
        self._SourceID = params.get("SourceID")
        self._SourceName = params.get("SourceName")
        self._SourceType = params.get("SourceType")
        if params.get("SourceInfo") is not None:
            self._SourceInfo = SourceInfo()
            self._SourceInfo._deserialize(params.get("SourceInfo"))
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkAccessControl(AbstractModel):
    r"""Network access policy

    """

    def __init__(self):
        r"""
        :param _Mode: Access mode: Whitelist|Blacklist
        :type Mode: str
        :param _CidrWhiteList: List of allowlist
        :type CidrWhiteList: list of str
        :param _CidrBlackList: blocklist
        :type CidrBlackList: list of str
        """
        self._Mode = None
        self._CidrWhiteList = None
        self._CidrBlackList = None

    @property
    def Mode(self):
        r"""Access mode: Whitelist|Blacklist
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def CidrWhiteList(self):
        r"""List of allowlist
        :rtype: list of str
        """
        return self._CidrWhiteList

    @CidrWhiteList.setter
    def CidrWhiteList(self, CidrWhiteList):
        self._CidrWhiteList = CidrWhiteList

    @property
    def CidrBlackList(self):
        r"""blocklist
        :rtype: list of str
        """
        return self._CidrBlackList

    @CidrBlackList.setter
    def CidrBlackList(self, CidrBlackList):
        self._CidrBlackList = CidrBlackList


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._CidrWhiteList = params.get("CidrWhiteList")
        self._CidrBlackList = params.get("CidrBlackList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenWafProtectionRequest(AbstractModel):
    r"""OpenWafProtection request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _Type: Type of protection resource.
-Global instance
-Service
-Route
-Object (not currently supported)
        :type Type: str
        :param _List: When resource type Type is Service or Route, list of passed in services or routes
        :type List: list of str
        """
        self._GatewayId = None
        self._Type = None
        self._List = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Type(self):
        r"""Type of protection resource.
-Global instance
-Service
-Route
-Object (not currently supported)
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def List(self):
        r"""When resource type Type is Service or Route, list of passed in services or routes
        :rtype: list of str
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Type = params.get("Type")
        self._List = params.get("List")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenWafProtectionResponse(AbstractModel):
    r"""OpenWafProtection response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class PublicAddressConfig(AbstractModel):
    r"""Public IP address info

    """

    def __init__(self):
        r"""
        :param _Vip: Public ip address
        :type Vip: str
        :param _InternetMaxBandwidthOut: Maximum public network bandwidth
        :type InternetMaxBandwidthOut: int
        :param _GroupId: public network associated group id
        :type GroupId: str
        :param _GroupName: Public network associated group name
        :type GroupName: str
        :param _NetworkId: Public network CLB id
        :type NetworkId: str
        :param _Description: Description of public network CLB
        :type Description: str
        """
        self._Vip = None
        self._InternetMaxBandwidthOut = None
        self._GroupId = None
        self._GroupName = None
        self._NetworkId = None
        self._Description = None

    @property
    def Vip(self):
        r"""Public ip address
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def InternetMaxBandwidthOut(self):
        r"""Maximum public network bandwidth
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def GroupId(self):
        r"""public network associated group id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""Public network associated group name
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def NetworkId(self):
        r"""Public network CLB id
        :rtype: str
        """
        return self._NetworkId

    @NetworkId.setter
    def NetworkId(self, NetworkId):
        self._NetworkId = NetworkId

    @property
    def Description(self):
        r"""Description of public network CLB
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Vip = params.get("Vip")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._NetworkId = params.get("NetworkId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QpsThreshold(AbstractModel):
    r"""Cloud-native gateway traffic throttling plugin Qps threshold

    """

    def __init__(self):
        r"""
        :param _Unit: qps threshold control dimension, including: second, minute, hour, day, month, year.
        :type Unit: str
        :param _Max: Threshold.
        :type Max: int
        """
        self._Unit = None
        self._Max = None

    @property
    def Unit(self):
        r"""qps threshold control dimension, including: second, minute, hour, day, month, year.
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Max(self):
        r"""Threshold.
        :rtype: int
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max


    def _deserialize(self, params):
        self._Unit = params.get("Unit")
        self._Max = params.get("Max")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitResponse(AbstractModel):
    r"""Cloud-Native Gateway Traffic Throttling Plugin Custom Response

    """

    def __init__(self):
        r"""
        :param _Body: Custom response body
        :type Body: str
        :param _Headers: Headers
        :type Headers: list of KVMapping
        :param _HttpStatus: HTTP status code.
        :type HttpStatus: int
        """
        self._Body = None
        self._Headers = None
        self._HttpStatus = None

    @property
    def Body(self):
        r"""Custom response body
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Headers(self):
        r"""Headers
        :rtype: list of KVMapping
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def HttpStatus(self):
        r"""HTTP status code.
        :rtype: int
        """
        return self._HttpStatus

    @HttpStatus.setter
    def HttpStatus(self, HttpStatus):
        self._HttpStatus = HttpStatus


    def _deserialize(self, params):
        self._Body = params.get("Body")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = KVMapping()
                obj._deserialize(item)
                self._Headers.append(obj)
        self._HttpStatus = params.get("HttpStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteWafStatus(AbstractModel):
    r"""Route WAF status

    """

    def __init__(self):
        r"""
        :param _Name: Route name
        :type Name: str
        :param _Id: ID of the route
        :type Id: str
        :param _Status: Whether WAF protection is enabled for the route
        :type Status: str
        :param _Methods: Method.
        :type Methods: list of str
        :param _Paths: Path.
        :type Paths: list of str
        :param _Hosts: Domain
        :type Hosts: list of str
        :param _ServiceName: Name of the service corresponding to the route
        :type ServiceName: str
        :param _ServiceId: ID of the service corresponding to the route
        :type ServiceId: str
        """
        self._Name = None
        self._Id = None
        self._Status = None
        self._Methods = None
        self._Paths = None
        self._Hosts = None
        self._ServiceName = None
        self._ServiceId = None

    @property
    def Name(self):
        r"""Route name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        r"""ID of the route
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        r"""Whether WAF protection is enabled for the route
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Methods(self):
        r"""Method.
        :rtype: list of str
        """
        return self._Methods

    @Methods.setter
    def Methods(self, Methods):
        self._Methods = Methods

    @property
    def Paths(self):
        r"""Path.
        :rtype: list of str
        """
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths

    @property
    def Hosts(self):
        r"""Domain
        :rtype: list of str
        """
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def ServiceName(self):
        r"""Name of the service corresponding to the route
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceId(self):
        r"""ID of the service corresponding to the route
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        self._Methods = params.get("Methods")
        self._Paths = params.get("Paths")
        self._Hosts = params.get("Hosts")
        self._ServiceName = params.get("ServiceName")
        self._ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoutingDestinationRuleLabel(AbstractModel):
    r"""Target service instance instance tag info

    """

    def __init__(self):
        r"""
        :param _LabelKey: Tag key.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LabelKey: str
        :param _LabelValue: Tag value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LabelValue: str
        :param _LabelType: expression type
Note: This field may return null, indicating that no valid values can be obtained.
        :type LabelType: str
        :param _LabelValueType: value type
Note: This field may return null, indicating that no valid values can be obtained.
        :type LabelValueType: str
        """
        self._LabelKey = None
        self._LabelValue = None
        self._LabelType = None
        self._LabelValueType = None

    @property
    def LabelKey(self):
        r"""Tag key.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LabelKey

    @LabelKey.setter
    def LabelKey(self, LabelKey):
        self._LabelKey = LabelKey

    @property
    def LabelValue(self):
        r"""Tag value.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LabelValue

    @LabelValue.setter
    def LabelValue(self, LabelValue):
        self._LabelValue = LabelValue

    @property
    def LabelType(self):
        r"""expression type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LabelType

    @LabelType.setter
    def LabelType(self, LabelType):
        self._LabelType = LabelType

    @property
    def LabelValueType(self):
        r"""value type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LabelValueType

    @LabelValueType.setter
    def LabelValueType(self, LabelValueType):
        self._LabelValueType = LabelValueType


    def _deserialize(self, params):
        self._LabelKey = params.get("LabelKey")
        self._LabelValue = params.get("LabelValue")
        self._LabelType = params.get("LabelType")
        self._LabelValueType = params.get("LabelValueType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleFilter(AbstractModel):
    r"""Throttling rule Filter

    """

    def __init__(self):
        r"""
        :param _Key: Key of throttling conditions
        :type Key: str
        :param _Values: Values of throttling conditions
        :type Values: list of str
        :param _Operator: operator
        :type Operator: str
        :param _Name: name in header or query
        :type Name: str
        """
        self._Key = None
        self._Values = None
        self._Operator = None
        self._Name = None

    @property
    def Key(self):
        r"""Key of throttling conditions
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        r"""Values of throttling conditions
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Operator(self):
        r"""operator
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Name(self):
        r"""name in header or query
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        self._Operator = params.get("Operator")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceGatewaySelector(AbstractModel):
    r"""microservice gateway selector

    """

    def __init__(self):
        r"""
        :param _Namespace: Namespace
Note: This field may return null, indicating that no valid values can be obtained.
        :type Namespace: str
        :param _Service: Service.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Service: str
        :param _Labels: Instance tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type Labels: list of Label
        """
        self._Namespace = None
        self._Service = None
        self._Labels = None

    @property
    def Namespace(self):
        r"""Namespace
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Service(self):
        r"""Service.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Labels(self):
        r"""Instance tag
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Label
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._Service = params.get("Service")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceSelector(AbstractModel):
    r"""ordinary service selector

    """

    def __init__(self):
        r"""
        :param _Namespace: Namespace
Note: This field may return null, indicating that no valid values can be obtained.
        :type Namespace: str
        :param _Service: Service.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Service: str
        :param _Labels: Instance tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type Labels: list of Label
        """
        self._Namespace = None
        self._Service = None
        self._Labels = None

    @property
    def Namespace(self):
        r"""Namespace
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Service(self):
        r"""Service.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Labels(self):
        r"""Instance tag
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Label
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._Service = params.get("Service")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceWafStatus(AbstractModel):
    r"""WAF status of the service

    """

    def __init__(self):
        r"""
        :param _Name: Service name
        :type Name: str
        :param _Id: Service ID
        :type Id: str
        :param _Type: Service type
        :type Type: str
        :param _Status: Whether WAF protection is enabled for the service
        :type Status: str
        """
        self._Name = None
        self._Id = None
        self._Type = None
        self._Status = None

    @property
    def Name(self):
        r"""Service name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        r"""Service ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        r"""Service type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        r"""Whether WAF protection is enabled for the service
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceInfo(AbstractModel):
    r"""service source

    """

    def __init__(self):
        r"""
        :param _Addresses: Microservice engine integration IP address information
        :type Addresses: list of str
        :param _VpcInfo: VPC information of the microservice engine
        :type VpcInfo: :class:`tencentcloud.tse.v20201207.models.SourceInstanceVpcInfo`
        :param _Auth: Microservice engine authentication information
        :type Auth: :class:`tencentcloud.tse.v20201207.models.SourceInstanceAuth`
        """
        self._Addresses = None
        self._VpcInfo = None
        self._Auth = None

    @property
    def Addresses(self):
        r"""Microservice engine integration IP address information
        :rtype: list of str
        """
        return self._Addresses

    @Addresses.setter
    def Addresses(self, Addresses):
        self._Addresses = Addresses

    @property
    def VpcInfo(self):
        r"""VPC information of the microservice engine
        :rtype: :class:`tencentcloud.tse.v20201207.models.SourceInstanceVpcInfo`
        """
        return self._VpcInfo

    @VpcInfo.setter
    def VpcInfo(self, VpcInfo):
        self._VpcInfo = VpcInfo

    @property
    def Auth(self):
        r"""Microservice engine authentication information
        :rtype: :class:`tencentcloud.tse.v20201207.models.SourceInstanceAuth`
        """
        return self._Auth

    @Auth.setter
    def Auth(self, Auth):
        self._Auth = Auth


    def _deserialize(self, params):
        self._Addresses = params.get("Addresses")
        if params.get("VpcInfo") is not None:
            self._VpcInfo = SourceInstanceVpcInfo()
            self._VpcInfo._deserialize(params.get("VpcInfo"))
        if params.get("Auth") is not None:
            self._Auth = SourceInstanceAuth()
            self._Auth._deserialize(params.get("Auth"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceInstanceAuth(AbstractModel):
    r"""Instance authentication information

    """

    def __init__(self):
        r"""
        :param _Username: Username.
        :type Username: str
        :param _Password: account password
        :type Password: str
        :param _AccessToken: token credential
        :type AccessToken: str
        """
        self._Username = None
        self._Password = None
        self._AccessToken = None

    @property
    def Username(self):
        r"""Username.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        r"""account password
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def AccessToken(self):
        r"""token credential
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken


    def _deserialize(self, params):
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        self._AccessToken = params.get("AccessToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceInstanceVpcInfo(AbstractModel):
    r"""VPC information of the microservice engine instance

    """

    def __init__(self):
        r"""
        :param _VpcID: VPC information of the microservice engine
        :type VpcID: str
        :param _SubnetID: Microservice engine subnet info
        :type SubnetID: str
        """
        self._VpcID = None
        self._SubnetID = None

    @property
    def VpcID(self):
        r"""VPC information of the microservice engine
        :rtype: str
        """
        return self._VpcID

    @VpcID.setter
    def VpcID(self, VpcID):
        self._VpcID = VpcID

    @property
    def SubnetID(self):
        r"""Microservice engine subnet info
        :rtype: str
        """
        return self._SubnetID

    @SubnetID.setter
    def SubnetID(self, SubnetID):
        self._SubnetID = SubnetID


    def _deserialize(self, params):
        self._VpcID = params.get("VpcID")
        self._SubnetID = params.get("SubnetID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TSEGatewaySelector(AbstractModel):
    r"""Gateway service information match condition

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway engine instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type GatewayId: str
        :param _Services: Gateway service
Note: This field may return null, indicating that no valid values can be obtained.
        :type Services: list of str
        """
        self._GatewayId = None
        self._Services = None

    @property
    def GatewayId(self):
        r"""Gateway engine instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Services(self):
        r"""Gateway service
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Services

    @Services.setter
    def Services(self, Services):
        self._Services = Services


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Services = params.get("Services")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrafficGray(AbstractModel):
    r"""Traffic grayscale rule for lanes

    """

    def __init__(self):
        r"""
        :param _Mode: Grayscale release rules for traffic, grayscale by ratio or preheat method
        :type Mode: str
        :param _Percent: Grayscale percentage value 1-100 by proportion
        :type Percent: int
        :param _IntervalSecond: Preheated interval
        :type IntervalSecond: int
        :param _Curvature: Preheated curvature
        :type Curvature: int
        """
        self._Mode = None
        self._Percent = None
        self._IntervalSecond = None
        self._Curvature = None

    @property
    def Mode(self):
        r"""Grayscale release rules for traffic, grayscale by ratio or preheat method
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Percent(self):
        r"""Grayscale percentage value 1-100 by proportion
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def IntervalSecond(self):
        r"""Preheated interval
        :rtype: int
        """
        return self._IntervalSecond

    @IntervalSecond.setter
    def IntervalSecond(self, IntervalSecond):
        self._IntervalSecond = IntervalSecond

    @property
    def Curvature(self):
        r"""Preheated curvature
        :rtype: int
        """
        return self._Curvature

    @Curvature.setter
    def Curvature(self, Curvature):
        self._Curvature = Curvature


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._Percent = params.get("Percent")
        self._IntervalSecond = params.get("IntervalSecond")
        self._Curvature = params.get("Curvature")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindAutoScalerResourceStrategyFromGroupsRequest(AbstractModel):
    r"""UnbindAutoScalerResourceStrategyFromGroups request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway instance ID
        :type GatewayId: str
        :param _StrategyId: Policy ID
        :type StrategyId: str
        :param _GroupIds: gateway group ID list
        :type GroupIds: list of str
        """
        self._GatewayId = None
        self._StrategyId = None
        self._GroupIds = None

    @property
    def GatewayId(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def StrategyId(self):
        r"""Policy ID
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def GroupIds(self):
        r"""gateway group ID list
        :rtype: list of str
        """
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._StrategyId = params.get("StrategyId")
        self._GroupIds = params.get("GroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindAutoScalerResourceStrategyFromGroupsResponse(AbstractModel):
    r"""UnbindAutoScalerResourceStrategyFromGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Success status
        :type Result: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Success status
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UpdateCloudNativeAPIGatewayCertificateInfoRequest(AbstractModel):
    r"""UpdateCloudNativeAPIGatewayCertificateInfo request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
        :type GatewayId: str
        :param _Id: Certificate ID.
        :type Id: str
        :param _BindDomains: Domain name list bound to
        :type BindDomains: list of str
        :param _Name: Certificate Name
        :type Name: str
        """
        self._GatewayId = None
        self._Id = None
        self._BindDomains = None
        self._Name = None

    @property
    def GatewayId(self):
        r"""Gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Id(self):
        r"""Certificate ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def BindDomains(self):
        r"""Domain name list bound to
        :rtype: list of str
        """
        return self._BindDomains

    @BindDomains.setter
    def BindDomains(self, BindDomains):
        self._BindDomains = BindDomains

    @property
    def Name(self):
        r"""Certificate Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Id = params.get("Id")
        self._BindDomains = params.get("BindDomains")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCloudNativeAPIGatewayCertificateInfoResponse(AbstractModel):
    r"""UpdateCloudNativeAPIGatewayCertificateInfo response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateCloudNativeAPIGatewayResult(AbstractModel):
    r"""Refresh the cloud native API gateway response result.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud Native API Gateway ID.
        :type GatewayId: str
        :param _Status: Cloud-native gateway status.
        :type Status: str
        :param _TaskId: Task ID.
        :type TaskId: str
        """
        self._GatewayId = None
        self._Status = None
        self._TaskId = None

    @property
    def GatewayId(self):
        r"""Cloud Native API Gateway ID.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Status(self):
        r"""Cloud-native gateway status.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCloudNativeAPIGatewaySpecRequest(AbstractModel):
    r"""UpdateCloudNativeAPIGatewaySpec request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Cloud Native API gateway instance ID.
Only supports postpaid instances
        :type GatewayId: str
        :param _GroupId: Gateway group id
        :type GroupId: str
        :param _NodeConfig: Gateway grouping node specification configuration.
        :type NodeConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        """
        self._GatewayId = None
        self._GroupId = None
        self._NodeConfig = None

    @property
    def GatewayId(self):
        r"""Cloud Native API gateway instance ID.
Only supports postpaid instances
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        r"""Gateway group id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def NodeConfig(self):
        r"""Gateway grouping node specification configuration.
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        """
        return self._NodeConfig

    @NodeConfig.setter
    def NodeConfig(self, NodeConfig):
        self._NodeConfig = NodeConfig


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        if params.get("NodeConfig") is not None:
            self._NodeConfig = CloudNativeAPIGatewayNodeConfig()
            self._NodeConfig._deserialize(params.get("NodeConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCloudNativeAPIGatewaySpecResponse(AbstractModel):
    r"""UpdateCloudNativeAPIGatewaySpec response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Refresh the cloud native API gateway instance specification response result.
        :type Result: :class:`tencentcloud.tse.v20201207.models.UpdateCloudNativeAPIGatewayResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Refresh the cloud native API gateway instance specification response result.
        :rtype: :class:`tencentcloud.tse.v20201207.models.UpdateCloudNativeAPIGatewayResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UpdateCloudNativeAPIGatewayResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class UpdateUpstreamHealthCheckConfigRequest(AbstractModel):
    r"""UpdateUpstreamHealthCheckConfig request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: gateway ID
        :type GatewayId: str
        :param _Name: Gateway service name.
        :type Name: str
        :param _HealthCheckConfig: Health check configuration
        :type HealthCheckConfig: :class:`tencentcloud.tse.v20201207.models.UpstreamHealthCheckConfig`
        """
        self._GatewayId = None
        self._Name = None
        self._HealthCheckConfig = None

    @property
    def GatewayId(self):
        r"""gateway ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""Gateway service name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def HealthCheckConfig(self):
        r"""Health check configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.UpstreamHealthCheckConfig`
        """
        return self._HealthCheckConfig

    @HealthCheckConfig.setter
    def HealthCheckConfig(self, HealthCheckConfig):
        self._HealthCheckConfig = HealthCheckConfig


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        if params.get("HealthCheckConfig") is not None:
            self._HealthCheckConfig = UpstreamHealthCheckConfig()
            self._HealthCheckConfig._deserialize(params.get("HealthCheckConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUpstreamHealthCheckConfigResponse(AbstractModel):
    r"""UpdateUpstreamHealthCheckConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Success status
        :type Result: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Success status
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UpdateUpstreamTargetsRequest(AbstractModel):
    r"""UpdateUpstreamTargets request structure.

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway instance ID
        :type GatewayId: str
        :param _Name: Service name or ID
        :type Name: str
        :param _Targets: Instance list
        :type Targets: list of KongTarget
        """
        self._GatewayId = None
        self._Name = None
        self._Targets = None

    @property
    def GatewayId(self):
        r"""Gateway instance ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""Service name or ID
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Targets(self):
        r"""Instance list
        :rtype: list of KongTarget
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = KongTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUpstreamTargetsResponse(AbstractModel):
    r"""UpdateUpstreamTargets response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether update succeeded
        :type Result: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Whether update succeeded
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UpstreamHealthCheckConfig(AbstractModel):
    r"""Cloud-native gateway health check configuration

    """

    def __init__(self):
        r"""
        :param _EnableActiveHealthCheck: Enable active health check
        :type EnableActiveHealthCheck: bool
        :param _ActiveHealthCheck: Active health check configuration
        :type ActiveHealthCheck: :class:`tencentcloud.tse.v20201207.models.KongActiveHealthCheck`
        :param _EnablePassiveHealthCheck: Enable passive health check
        :type EnablePassiveHealthCheck: bool
        :param _PassiveHealthCheck: Passive health check configuration
        :type PassiveHealthCheck: :class:`tencentcloud.tse.v20201207.models.KongPassiveHealthCheck`
        :param _Successes: Consecutive health threshold, unit: times
        :type Successes: int
        :param _Failures: Continuous anomaly threshold, unit: times	
        :type Failures: int
        :param _Timeouts: Timeout threshold, unit: times
        :type Timeouts: int
        :param _HealthyHttpStatuses: Healthy HTTP status code
        :type HealthyHttpStatuses: list of int non-negative
        :param _UnhealthyHttpStatuses: abnormal HTTP status code
        :type UnhealthyHttpStatuses: list of int non-negative
        :param _IgnoreZeroWeightNodes: Health check monitoring blocks nodes with a weight of 0 in reported data
Note: This field may return null, indicating that no valid values can be obtained.
        :type IgnoreZeroWeightNodes: bool
        :param _ZeroWeightHeathCheck: Health check supports nodes with support weights of 0
        :type ZeroWeightHeathCheck: bool
        """
        self._EnableActiveHealthCheck = None
        self._ActiveHealthCheck = None
        self._EnablePassiveHealthCheck = None
        self._PassiveHealthCheck = None
        self._Successes = None
        self._Failures = None
        self._Timeouts = None
        self._HealthyHttpStatuses = None
        self._UnhealthyHttpStatuses = None
        self._IgnoreZeroWeightNodes = None
        self._ZeroWeightHeathCheck = None

    @property
    def EnableActiveHealthCheck(self):
        r"""Enable active health check
        :rtype: bool
        """
        return self._EnableActiveHealthCheck

    @EnableActiveHealthCheck.setter
    def EnableActiveHealthCheck(self, EnableActiveHealthCheck):
        self._EnableActiveHealthCheck = EnableActiveHealthCheck

    @property
    def ActiveHealthCheck(self):
        r"""Active health check configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.KongActiveHealthCheck`
        """
        return self._ActiveHealthCheck

    @ActiveHealthCheck.setter
    def ActiveHealthCheck(self, ActiveHealthCheck):
        self._ActiveHealthCheck = ActiveHealthCheck

    @property
    def EnablePassiveHealthCheck(self):
        r"""Enable passive health check
        :rtype: bool
        """
        return self._EnablePassiveHealthCheck

    @EnablePassiveHealthCheck.setter
    def EnablePassiveHealthCheck(self, EnablePassiveHealthCheck):
        self._EnablePassiveHealthCheck = EnablePassiveHealthCheck

    @property
    def PassiveHealthCheck(self):
        r"""Passive health check configuration
        :rtype: :class:`tencentcloud.tse.v20201207.models.KongPassiveHealthCheck`
        """
        return self._PassiveHealthCheck

    @PassiveHealthCheck.setter
    def PassiveHealthCheck(self, PassiveHealthCheck):
        self._PassiveHealthCheck = PassiveHealthCheck

    @property
    def Successes(self):
        r"""Consecutive health threshold, unit: times
        :rtype: int
        """
        return self._Successes

    @Successes.setter
    def Successes(self, Successes):
        self._Successes = Successes

    @property
    def Failures(self):
        r"""Continuous anomaly threshold, unit: times	
        :rtype: int
        """
        return self._Failures

    @Failures.setter
    def Failures(self, Failures):
        self._Failures = Failures

    @property
    def Timeouts(self):
        r"""Timeout threshold, unit: times
        :rtype: int
        """
        return self._Timeouts

    @Timeouts.setter
    def Timeouts(self, Timeouts):
        self._Timeouts = Timeouts

    @property
    def HealthyHttpStatuses(self):
        r"""Healthy HTTP status code
        :rtype: list of int non-negative
        """
        return self._HealthyHttpStatuses

    @HealthyHttpStatuses.setter
    def HealthyHttpStatuses(self, HealthyHttpStatuses):
        self._HealthyHttpStatuses = HealthyHttpStatuses

    @property
    def UnhealthyHttpStatuses(self):
        r"""abnormal HTTP status code
        :rtype: list of int non-negative
        """
        return self._UnhealthyHttpStatuses

    @UnhealthyHttpStatuses.setter
    def UnhealthyHttpStatuses(self, UnhealthyHttpStatuses):
        self._UnhealthyHttpStatuses = UnhealthyHttpStatuses

    @property
    def IgnoreZeroWeightNodes(self):
        warnings.warn("parameter `IgnoreZeroWeightNodes` is deprecated", DeprecationWarning) 

        r"""Health check monitoring blocks nodes with a weight of 0 in reported data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IgnoreZeroWeightNodes

    @IgnoreZeroWeightNodes.setter
    def IgnoreZeroWeightNodes(self, IgnoreZeroWeightNodes):
        warnings.warn("parameter `IgnoreZeroWeightNodes` is deprecated", DeprecationWarning) 

        self._IgnoreZeroWeightNodes = IgnoreZeroWeightNodes

    @property
    def ZeroWeightHeathCheck(self):
        r"""Health check supports nodes with support weights of 0
        :rtype: bool
        """
        return self._ZeroWeightHeathCheck

    @ZeroWeightHeathCheck.setter
    def ZeroWeightHeathCheck(self, ZeroWeightHeathCheck):
        self._ZeroWeightHeathCheck = ZeroWeightHeathCheck


    def _deserialize(self, params):
        self._EnableActiveHealthCheck = params.get("EnableActiveHealthCheck")
        if params.get("ActiveHealthCheck") is not None:
            self._ActiveHealthCheck = KongActiveHealthCheck()
            self._ActiveHealthCheck._deserialize(params.get("ActiveHealthCheck"))
        self._EnablePassiveHealthCheck = params.get("EnablePassiveHealthCheck")
        if params.get("PassiveHealthCheck") is not None:
            self._PassiveHealthCheck = KongPassiveHealthCheck()
            self._PassiveHealthCheck._deserialize(params.get("PassiveHealthCheck"))
        self._Successes = params.get("Successes")
        self._Failures = params.get("Failures")
        self._Timeouts = params.get("Timeouts")
        self._HealthyHttpStatuses = params.get("HealthyHttpStatuses")
        self._UnhealthyHttpStatuses = params.get("UnhealthyHttpStatuses")
        self._IgnoreZeroWeightNodes = params.get("IgnoreZeroWeightNodes")
        self._ZeroWeightHeathCheck = params.get("ZeroWeightHeathCheck")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        