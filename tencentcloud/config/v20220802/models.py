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


class AggregateResourceInfo(AbstractModel):
    """Resource list information response parameters structure

    """

    def __init__(self):
        r"""
        :param _ResourceType: Resource type
        :type ResourceType: str
        :param _ResourceName: Resource name
        :type ResourceName: str
        :param _ResourceId: Resource ID
        :type ResourceId: str
        :param _ResourceRegion: Region

Note: This field may return null, indicating that no valid value is found.
        :type ResourceRegion: str
        :param _ResourceStatus: Resource Status

Note: This field may return null, indicating that no valid value is found.
        :type ResourceStatus: str
        :param _ResourceDelete: Whether to delete. 1: Deleted; 0: Not deleted.
Note: This field may return null, indicating that no valid value is found.
        :type ResourceDelete: int
        :param _ResourceCreateTime: Resource creation time

Note: This field may return null, indicating that no valid value is found.
        :type ResourceCreateTime: str
        :param _Tags: Tag information

Note: This field may return null, indicating that no valid value is found.
        :type Tags: list of Tag
        :param _ResourceZone: Availability zone

Note: This field may return null, indicating that no valid value is found.
        :type ResourceZone: str
        :param _ComplianceResult: Compliance status
Note: This field may return null, indicating that no valid value is found.
        :type ComplianceResult: str
        :param _ResourceOwnerId: Resource owner uid
        :type ResourceOwnerId: int
        :param _ResourceOwnerName: User nickname
Note: This field may return null, indicating that no valid value is found.
        :type ResourceOwnerName: str
        """
        self._ResourceType = None
        self._ResourceName = None
        self._ResourceId = None
        self._ResourceRegion = None
        self._ResourceStatus = None
        self._ResourceDelete = None
        self._ResourceCreateTime = None
        self._Tags = None
        self._ResourceZone = None
        self._ComplianceResult = None
        self._ResourceOwnerId = None
        self._ResourceOwnerName = None

    @property
    def ResourceType(self):
        """Resource type
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        """Resource name
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceId(self):
        """Resource ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceRegion(self):
        """Region

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceStatus(self):
        """Resource Status

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus

    @property
    def ResourceDelete(self):
        """Whether to delete. 1: Deleted; 0: Not deleted.
Note: This field may return null, indicating that no valid value is found.
        :rtype: int
        """
        return self._ResourceDelete

    @ResourceDelete.setter
    def ResourceDelete(self, ResourceDelete):
        self._ResourceDelete = ResourceDelete

    @property
    def ResourceCreateTime(self):
        """Resource creation time

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ResourceCreateTime

    @ResourceCreateTime.setter
    def ResourceCreateTime(self, ResourceCreateTime):
        self._ResourceCreateTime = ResourceCreateTime

    @property
    def Tags(self):
        """Tag information

Note: This field may return null, indicating that no valid value is found.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ResourceZone(self):
        """Availability zone

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ResourceZone

    @ResourceZone.setter
    def ResourceZone(self, ResourceZone):
        self._ResourceZone = ResourceZone

    @property
    def ComplianceResult(self):
        """Compliance status
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

    @property
    def ResourceOwnerId(self):
        """Resource owner uid
        :rtype: int
        """
        return self._ResourceOwnerId

    @ResourceOwnerId.setter
    def ResourceOwnerId(self, ResourceOwnerId):
        self._ResourceOwnerId = ResourceOwnerId

    @property
    def ResourceOwnerName(self):
        """User nickname
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ResourceOwnerName

    @ResourceOwnerName.setter
    def ResourceOwnerName(self, ResourceOwnerName):
        self._ResourceOwnerName = ResourceOwnerName


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._ResourceName = params.get("ResourceName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceStatus = params.get("ResourceStatus")
        self._ResourceDelete = params.get("ResourceDelete")
        self._ResourceCreateTime = params.get("ResourceCreateTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ResourceZone = params.get("ResourceZone")
        self._ComplianceResult = params.get("ComplianceResult")
        self._ResourceOwnerId = params.get("ResourceOwnerId")
        self._ResourceOwnerName = params.get("ResourceOwnerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Annotation(AbstractModel):
    """Compliance details

    """

    def __init__(self):
        r"""
        :param _Configuration: Current actual configuration of the resource. It can contain 0 to 256 characters, which is the non-compliant configuration of the resource.
Note: This field may return null, indicating that no valid value is found.
        :type Configuration: str
        :param _DesiredValue: Desired configuration of the resource. It can contain 0 to 256 characters, which is the compliant configuration of the resource.
Note: This field may return null, indicating that no valid value is found.
        :type DesiredValue: str
        :param _Operator: Comparison operator between current and desired configuration of the resource. Length is 0-16 characters. This field may be empty when custom rule reporting evaluation result.
        :type Operator: str
        :param _Property: JSON path of current configuration in resource attribute structure. Length is 0-256 characters. This field may be empty when custom rule reporting evaluation result.
        :type Property: str
        """
        self._Configuration = None
        self._DesiredValue = None
        self._Operator = None
        self._Property = None

    @property
    def Configuration(self):
        """Current actual configuration of the resource. It can contain 0 to 256 characters, which is the non-compliant configuration of the resource.
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration

    @property
    def DesiredValue(self):
        """Desired configuration of the resource. It can contain 0 to 256 characters, which is the compliant configuration of the resource.
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._DesiredValue

    @DesiredValue.setter
    def DesiredValue(self, DesiredValue):
        self._DesiredValue = DesiredValue

    @property
    def Operator(self):
        """Comparison operator between current and desired configuration of the resource. Length is 0-16 characters. This field may be empty when custom rule reporting evaluation result.
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Property(self):
        """JSON path of current configuration in resource attribute structure. Length is 0-256 characters. This field may be empty when custom rule reporting evaluation result.
        :rtype: str
        """
        return self._Property

    @Property.setter
    def Property(self, Property):
        self._Property = Property


    def _deserialize(self, params):
        self._Configuration = params.get("Configuration")
        self._DesiredValue = params.get("DesiredValue")
        self._Operator = params.get("Operator")
        self._Property = params.get("Property")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigRule(AbstractModel):
    """Rule details

    """

    def __init__(self):
        r"""
        :param _Identifier: Rule identifier
Note: This field may return null, indicating that no valid value is found.
        :type Identifier: str
        :param _RuleName: Name of the rule

Note: This field may return null, indicating that no valid value is found.
        :type RuleName: str
        :param _InputParameter: Rule parameters
Note: This field may return null, indicating that no valid value is found.
        :type InputParameter: list of InputParameter
        :param _SourceCondition: Rule trigger condition.

Note: This field may return null, indicating that no valid value is found.
        :type SourceCondition: list of SourceConditionForManage
        :param _ResourceType: Resource types supported by rule. The rule only applies to specified resource types.
Note: This field may return null, indicating that no valid value is found.
        :type ResourceType: list of str
        :param _Labels: Rule ownership tag
Note: This field may return null, indicating that no valid value is found.
        :type Labels: list of str
        :param _RiskLevel: Rule risk level
1: Low risk
2: Medium risk
3: High risk
Note: This field may return null, indicating that no valid value is found.
        :type RiskLevel: int
        :param _ServiceFunction: Function corresponding to rule
Note: This field may return null, indicating that no valid value is found.
        :type ServiceFunction: str
        :param _CreateTime: Creation time

Format: YYYY-MM-DD h:i:s
Note: This field may return null, indicating that no valid value is found.
        :type CreateTime: str
        :param _Description: Rule description

Note: This field may return null, indicating that no valid value is found.
        :type Description: str
        :param _Status: ACTIVE: Enabled
NO_ACTIVE: Disabled
Note: This field may return null, indicating that no valid value is found.
        :type Status: str
        :param _ComplianceResult: Compliance: 'COMPLIANT'
'NON_COMPLIANT'
'NOT_APPLICABLE'
Note: This field may return null, indicating that no valid value is found.
        :type ComplianceResult: str
        :param _Annotation: ["",""]
Note: This field may return null, indicating that no valid value is found.
        :type Annotation: :class:`tencentcloud.config.v20220802.models.Annotation`
        :param _ConfigRuleInvokedTime: Rule evaluation time
Format: YYYY-MM-DD h:i:s

Note: This field may return null, indicating that no valid value is found.
        :type ConfigRuleInvokedTime: str
        :param _ConfigRuleId: Rule ID

Note: This field may return null, indicating that no valid value is found.
        :type ConfigRuleId: str
        :param _IdentifierType: CUSTOMIZE
Managed rule
Note: This field may return null, indicating that no valid value is found.
        :type IdentifierType: str
        :param _CompliancePackId: Compliance package ID
Note: This field may return null, indicating that no valid value is found.
        :type CompliancePackId: str
        :param _TriggerType: Trigger Type

Scheduled trigger
Triggered by configuration change
Note: This field may return null, indicating that no valid value is found.
        :type TriggerType: list of TriggerType
        :param _ManageInputParameter: Parameter details

Note: This field may return null, indicating that no valid value is found.
        :type ManageInputParameter: list of InputParameterForManage
        :param _CompliancePackName: Rule name

Note: This field may return null, indicating that no valid value is found.
        :type CompliancePackName: str
        :param _RegionsScope: Associated region
Note: This field may return null, indicating that no valid value is found.
        :type RegionsScope: list of str
        :param _TagsScope: Associate Tag

Note: This field may return null, indicating that no valid value is found.
        :type TagsScope: list of Tag
        :param _ExcludeResourceIdsScope:  The rule is invalid for the specified resource ID, meaning it does not evaluate the resource.
Note: This field may return null, indicating that no valid value is found.
        :type ExcludeResourceIdsScope: list of str
        :param _AccountGroupId: Account group ID

Note: This field may return null, indicating that no valid value is found.
        :type AccountGroupId: str
        :param _AccountGroupName: Account group name
Note: This field may return null, indicating that no valid value is found.
        :type AccountGroupName: str
        :param _RuleOwnerId: Rule owner user ID
Note: This field may return null, indicating that no valid value is found.
        :type RuleOwnerId: int
        :param _ManageTriggerType: Trigger methods supported by preset rules
Scheduled trigger
Triggered by configuration change
        :type ManageTriggerType: list of str
        """
        self._Identifier = None
        self._RuleName = None
        self._InputParameter = None
        self._SourceCondition = None
        self._ResourceType = None
        self._Labels = None
        self._RiskLevel = None
        self._ServiceFunction = None
        self._CreateTime = None
        self._Description = None
        self._Status = None
        self._ComplianceResult = None
        self._Annotation = None
        self._ConfigRuleInvokedTime = None
        self._ConfigRuleId = None
        self._IdentifierType = None
        self._CompliancePackId = None
        self._TriggerType = None
        self._ManageInputParameter = None
        self._CompliancePackName = None
        self._RegionsScope = None
        self._TagsScope = None
        self._ExcludeResourceIdsScope = None
        self._AccountGroupId = None
        self._AccountGroupName = None
        self._RuleOwnerId = None
        self._ManageTriggerType = None

    @property
    def Identifier(self):
        """Rule identifier
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def RuleName(self):
        """Name of the rule

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def InputParameter(self):
        """Rule parameters
Note: This field may return null, indicating that no valid value is found.
        :rtype: list of InputParameter
        """
        return self._InputParameter

    @InputParameter.setter
    def InputParameter(self, InputParameter):
        self._InputParameter = InputParameter

    @property
    def SourceCondition(self):
        """Rule trigger condition.

Note: This field may return null, indicating that no valid value is found.
        :rtype: list of SourceConditionForManage
        """
        return self._SourceCondition

    @SourceCondition.setter
    def SourceCondition(self, SourceCondition):
        self._SourceCondition = SourceCondition

    @property
    def ResourceType(self):
        """Resource types supported by rule. The rule only applies to specified resource types.
Note: This field may return null, indicating that no valid value is found.
        :rtype: list of str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Labels(self):
        """Rule ownership tag
Note: This field may return null, indicating that no valid value is found.
        :rtype: list of str
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def RiskLevel(self):
        """Rule risk level
1: Low risk
2: Medium risk
3: High risk
Note: This field may return null, indicating that no valid value is found.
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def ServiceFunction(self):
        """Function corresponding to rule
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ServiceFunction

    @ServiceFunction.setter
    def ServiceFunction(self, ServiceFunction):
        self._ServiceFunction = ServiceFunction

    @property
    def CreateTime(self):
        """Creation time

Format: YYYY-MM-DD h:i:s
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Description(self):
        """Rule description

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        """ACTIVE: Enabled
NO_ACTIVE: Disabled
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ComplianceResult(self):
        """Compliance: 'COMPLIANT'
'NON_COMPLIANT'
'NOT_APPLICABLE'
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

    @property
    def Annotation(self):
        """["",""]
Note: This field may return null, indicating that no valid value is found.
        :rtype: :class:`tencentcloud.config.v20220802.models.Annotation`
        """
        return self._Annotation

    @Annotation.setter
    def Annotation(self, Annotation):
        self._Annotation = Annotation

    @property
    def ConfigRuleInvokedTime(self):
        """Rule evaluation time
Format: YYYY-MM-DD h:i:s

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ConfigRuleInvokedTime

    @ConfigRuleInvokedTime.setter
    def ConfigRuleInvokedTime(self, ConfigRuleInvokedTime):
        self._ConfigRuleInvokedTime = ConfigRuleInvokedTime

    @property
    def ConfigRuleId(self):
        """Rule ID

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ConfigRuleId

    @ConfigRuleId.setter
    def ConfigRuleId(self, ConfigRuleId):
        self._ConfigRuleId = ConfigRuleId

    @property
    def IdentifierType(self):
        """CUSTOMIZE
Managed rule
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._IdentifierType

    @IdentifierType.setter
    def IdentifierType(self, IdentifierType):
        self._IdentifierType = IdentifierType

    @property
    def CompliancePackId(self):
        """Compliance package ID
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def TriggerType(self):
        """Trigger Type

Scheduled trigger
Triggered by configuration change
Note: This field may return null, indicating that no valid value is found.
        :rtype: list of TriggerType
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def ManageInputParameter(self):
        """Parameter details

Note: This field may return null, indicating that no valid value is found.
        :rtype: list of InputParameterForManage
        """
        return self._ManageInputParameter

    @ManageInputParameter.setter
    def ManageInputParameter(self, ManageInputParameter):
        self._ManageInputParameter = ManageInputParameter

    @property
    def CompliancePackName(self):
        """Rule name

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._CompliancePackName

    @CompliancePackName.setter
    def CompliancePackName(self, CompliancePackName):
        self._CompliancePackName = CompliancePackName

    @property
    def RegionsScope(self):
        """Associated region
Note: This field may return null, indicating that no valid value is found.
        :rtype: list of str
        """
        return self._RegionsScope

    @RegionsScope.setter
    def RegionsScope(self, RegionsScope):
        self._RegionsScope = RegionsScope

    @property
    def TagsScope(self):
        """Associate Tag

Note: This field may return null, indicating that no valid value is found.
        :rtype: list of Tag
        """
        return self._TagsScope

    @TagsScope.setter
    def TagsScope(self, TagsScope):
        self._TagsScope = TagsScope

    @property
    def ExcludeResourceIdsScope(self):
        """ The rule is invalid for the specified resource ID, meaning it does not evaluate the resource.
Note: This field may return null, indicating that no valid value is found.
        :rtype: list of str
        """
        return self._ExcludeResourceIdsScope

    @ExcludeResourceIdsScope.setter
    def ExcludeResourceIdsScope(self, ExcludeResourceIdsScope):
        self._ExcludeResourceIdsScope = ExcludeResourceIdsScope

    @property
    def AccountGroupId(self):
        """Account group ID

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def AccountGroupName(self):
        """Account group name
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._AccountGroupName

    @AccountGroupName.setter
    def AccountGroupName(self, AccountGroupName):
        self._AccountGroupName = AccountGroupName

    @property
    def RuleOwnerId(self):
        """Rule owner user ID
Note: This field may return null, indicating that no valid value is found.
        :rtype: int
        """
        return self._RuleOwnerId

    @RuleOwnerId.setter
    def RuleOwnerId(self, RuleOwnerId):
        self._RuleOwnerId = RuleOwnerId

    @property
    def ManageTriggerType(self):
        """Trigger methods supported by preset rules
Scheduled trigger
Triggered by configuration change
        :rtype: list of str
        """
        return self._ManageTriggerType

    @ManageTriggerType.setter
    def ManageTriggerType(self, ManageTriggerType):
        self._ManageTriggerType = ManageTriggerType


    def _deserialize(self, params):
        self._Identifier = params.get("Identifier")
        self._RuleName = params.get("RuleName")
        if params.get("InputParameter") is not None:
            self._InputParameter = []
            for item in params.get("InputParameter"):
                obj = InputParameter()
                obj._deserialize(item)
                self._InputParameter.append(obj)
        if params.get("SourceCondition") is not None:
            self._SourceCondition = []
            for item in params.get("SourceCondition"):
                obj = SourceConditionForManage()
                obj._deserialize(item)
                self._SourceCondition.append(obj)
        self._ResourceType = params.get("ResourceType")
        self._Labels = params.get("Labels")
        self._RiskLevel = params.get("RiskLevel")
        self._ServiceFunction = params.get("ServiceFunction")
        self._CreateTime = params.get("CreateTime")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._ComplianceResult = params.get("ComplianceResult")
        if params.get("Annotation") is not None:
            self._Annotation = Annotation()
            self._Annotation._deserialize(params.get("Annotation"))
        self._ConfigRuleInvokedTime = params.get("ConfigRuleInvokedTime")
        self._ConfigRuleId = params.get("ConfigRuleId")
        self._IdentifierType = params.get("IdentifierType")
        self._CompliancePackId = params.get("CompliancePackId")
        if params.get("TriggerType") is not None:
            self._TriggerType = []
            for item in params.get("TriggerType"):
                obj = TriggerType()
                obj._deserialize(item)
                self._TriggerType.append(obj)
        if params.get("ManageInputParameter") is not None:
            self._ManageInputParameter = []
            for item in params.get("ManageInputParameter"):
                obj = InputParameterForManage()
                obj._deserialize(item)
                self._ManageInputParameter.append(obj)
        self._CompliancePackName = params.get("CompliancePackName")
        self._RegionsScope = params.get("RegionsScope")
        if params.get("TagsScope") is not None:
            self._TagsScope = []
            for item in params.get("TagsScope"):
                obj = Tag()
                obj._deserialize(item)
                self._TagsScope.append(obj)
        self._ExcludeResourceIdsScope = params.get("ExcludeResourceIdsScope")
        self._AccountGroupId = params.get("AccountGroupId")
        self._AccountGroupName = params.get("AccountGroupName")
        self._RuleOwnerId = params.get("RuleOwnerId")
        self._ManageTriggerType = params.get("ManageTriggerType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiscoveredResourceRequest(AbstractModel):
    """DescribeDiscoveredResource request structure.

    """

    def __init__(self):
        r"""
        :param _ResourceId: Resource ID
        :type ResourceId: str
        :param _ResourceType: Resource type
        :type ResourceType: str
        :param _ResourceRegion: Resource region
        :type ResourceRegion: str
        """
        self._ResourceId = None
        self._ResourceType = None
        self._ResourceRegion = None

    @property
    def ResourceId(self):
        """Resource ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        """Resource type
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceRegion(self):
        """Resource region
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceRegion = params.get("ResourceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiscoveredResourceResponse(AbstractModel):
    """DescribeDiscoveredResource response structure.

    """

    def __init__(self):
        r"""
        :param _ResourceId: Resource ID

Note: This field may return null, indicating that no valid value is found.
        :type ResourceId: str
        :param _ResourceType: Resource type

Note: This field may return null, indicating that no valid value is found.
        :type ResourceType: str
        :param _ResourceName: Resource Name

Note: This field may return null, indicating that no valid value is found.
        :type ResourceName: str
        :param _ResourceRegion: Resource region

Note: This field may return null, indicating that no valid value is found.
        :type ResourceRegion: str
        :param _ResourceZone: Resource availability zone
Note: This field may return null, indicating that no valid value is found.
        :type ResourceZone: str
        :param _Configuration: Resource configuration

Note: This field may return null, indicating that no valid value is found.
        :type Configuration: str
        :param _ResourceCreateTime: Resource creation time

Note: This field may return null, indicating that no valid value is found.
        :type ResourceCreateTime: str
        :param _Tags: Resource tag

Note: This field may return null, indicating that no valid value is found.
        :type Tags: list of Tag
        :param _UpdateTime: Resource update time
Note: This field may return null, indicating that no valid value is found.
        :type UpdateTime: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ResourceId = None
        self._ResourceType = None
        self._ResourceName = None
        self._ResourceRegion = None
        self._ResourceZone = None
        self._Configuration = None
        self._ResourceCreateTime = None
        self._Tags = None
        self._UpdateTime = None
        self._RequestId = None

    @property
    def ResourceId(self):
        """Resource ID

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        """Resource type

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        """Resource Name

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceRegion(self):
        """Resource region

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceZone(self):
        """Resource availability zone
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ResourceZone

    @ResourceZone.setter
    def ResourceZone(self, ResourceZone):
        self._ResourceZone = ResourceZone

    @property
    def Configuration(self):
        """Resource configuration

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration

    @property
    def ResourceCreateTime(self):
        """Resource creation time

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ResourceCreateTime

    @ResourceCreateTime.setter
    def ResourceCreateTime(self, ResourceCreateTime):
        self._ResourceCreateTime = ResourceCreateTime

    @property
    def Tags(self):
        """Resource tag

Note: This field may return null, indicating that no valid value is found.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def UpdateTime(self):
        """Resource update time
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

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
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceName = params.get("ResourceName")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceZone = params.get("ResourceZone")
        self._Configuration = params.get("Configuration")
        self._ResourceCreateTime = params.get("ResourceCreateTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._UpdateTime = params.get("UpdateTime")
        self._RequestId = params.get("RequestId")


class Evaluation(AbstractModel):
    """Custom rule evaluation result

    """

    def __init__(self):
        r"""
        :param _ComplianceResourceId: Evaluated resource id. It can contain 0 to 256 characters.
        :type ComplianceResourceId: str
        :param _ComplianceResourceType: Evaluated resource type.
Supported:
QCS::CVM::Instance、 QCS::CBS::Disk、QCS::VPC::Vpc、QCS::VPC::Subnet、QCS::VPC::SecurityGroup、 QCS::CAM::User、QCS::CAM::Group、QCS::CAM::Policy、QCS::CAM::Role、QCS::COS::Bucket
        :type ComplianceResourceType: str
        :param _ComplianceRegion: Evaluated resource region.
It can contain 0 to 32 characters.
        :type ComplianceRegion: str
        :param _ComplianceType: Compliance type. Valid values:
COMPLIANT: Compliant,
NON_COMPLIANT: Non-compliant
        :type ComplianceType: str
        :param _Annotation: Supplementary information for non-compliant resources.
        :type Annotation: :class:`tencentcloud.config.v20220802.models.Annotation`
        """
        self._ComplianceResourceId = None
        self._ComplianceResourceType = None
        self._ComplianceRegion = None
        self._ComplianceType = None
        self._Annotation = None

    @property
    def ComplianceResourceId(self):
        """Evaluated resource id. It can contain 0 to 256 characters.
        :rtype: str
        """
        return self._ComplianceResourceId

    @ComplianceResourceId.setter
    def ComplianceResourceId(self, ComplianceResourceId):
        self._ComplianceResourceId = ComplianceResourceId

    @property
    def ComplianceResourceType(self):
        """Evaluated resource type.
Supported:
QCS::CVM::Instance、 QCS::CBS::Disk、QCS::VPC::Vpc、QCS::VPC::Subnet、QCS::VPC::SecurityGroup、 QCS::CAM::User、QCS::CAM::Group、QCS::CAM::Policy、QCS::CAM::Role、QCS::COS::Bucket
        :rtype: str
        """
        return self._ComplianceResourceType

    @ComplianceResourceType.setter
    def ComplianceResourceType(self, ComplianceResourceType):
        self._ComplianceResourceType = ComplianceResourceType

    @property
    def ComplianceRegion(self):
        """Evaluated resource region.
It can contain 0 to 32 characters.
        :rtype: str
        """
        return self._ComplianceRegion

    @ComplianceRegion.setter
    def ComplianceRegion(self, ComplianceRegion):
        self._ComplianceRegion = ComplianceRegion

    @property
    def ComplianceType(self):
        """Compliance type. Valid values:
COMPLIANT: Compliant,
NON_COMPLIANT: Non-compliant
        :rtype: str
        """
        return self._ComplianceType

    @ComplianceType.setter
    def ComplianceType(self, ComplianceType):
        self._ComplianceType = ComplianceType

    @property
    def Annotation(self):
        """Supplementary information for non-compliant resources.
        :rtype: :class:`tencentcloud.config.v20220802.models.Annotation`
        """
        return self._Annotation

    @Annotation.setter
    def Annotation(self, Annotation):
        self._Annotation = Annotation


    def _deserialize(self, params):
        self._ComplianceResourceId = params.get("ComplianceResourceId")
        self._ComplianceResourceType = params.get("ComplianceResourceType")
        self._ComplianceRegion = params.get("ComplianceRegion")
        self._ComplianceType = params.get("ComplianceType")
        if params.get("Annotation") is not None:
            self._Annotation = Annotation()
            self._Annotation._deserialize(params.get("Annotation"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Resource list filter

    """

    def __init__(self):
        r"""
        :param _Name: Query field name Resource name: resourceName Resource ID: resourceId Resource type: resourceType Resource region: resourceRegion Deletion status: resourceDelete 0 not deleted, 1 deleted resourceregionandzone region/az
        :type Name: str
        :param _Values: Value of the field to query
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """Query field name Resource name: resourceName Resource ID: resourceId Resource type: resourceType Resource region: resourceRegion Deletion status: resourceDelete 0 not deleted, 1 deleted resourceregionandzone region/az
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """Value of the field to query
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
        


class InputParameter(AbstractModel):
    """Parameter value

    """

    def __init__(self):
        r"""
        :param _ParameterKey: Parameter name
        :type ParameterKey: str
        :param _Type: Parameter type. Required type: Require, optional type: Optional.
        :type Type: str
        :param _Value: Parameter value

Note: This field may return null, indicating that no valid value is found.
        :type Value: str
        """
        self._ParameterKey = None
        self._Type = None
        self._Value = None

    @property
    def ParameterKey(self):
        """Parameter name
        :rtype: str
        """
        return self._ParameterKey

    @ParameterKey.setter
    def ParameterKey(self, ParameterKey):
        self._ParameterKey = ParameterKey

    @property
    def Type(self):
        """Parameter type. Required type: Require, optional type: Optional.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        """Parameter value

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._ParameterKey = params.get("ParameterKey")
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputParameterForManage(AbstractModel):
    """Rule input parameters

    """

    def __init__(self):
        r"""
        :param _ValueType: Value type. Integer: Integer, String: String.
Note: This field may return null, indicating that no valid value is found.
        :type ValueType: str
        :param _ParameterKey: Parameter key
Note: This field may return null, indicating that no valid value is found.
        :type ParameterKey: str
        :param _Type: Parameter type. Required type: Required, Optional type: Optional.
Note: This field may return null, indicating that no valid value is found.
        :type Type: str
        :param _DefaultValue: Default value

Note: This field may return null, indicating that no valid value is found.
        :type DefaultValue: str
        :param _Description: Description

Note: This field may return null, indicating that no valid value is found.
        :type Description: str
        """
        self._ValueType = None
        self._ParameterKey = None
        self._Type = None
        self._DefaultValue = None
        self._Description = None

    @property
    def ValueType(self):
        """Value type. Integer: Integer, String: String.
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def ParameterKey(self):
        """Parameter key
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ParameterKey

    @ParameterKey.setter
    def ParameterKey(self, ParameterKey):
        self._ParameterKey = ParameterKey

    @property
    def Type(self):
        """Parameter type. Required type: Required, Optional type: Optional.
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DefaultValue(self):
        """Default value

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def Description(self):
        """Description

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ValueType = params.get("ValueType")
        self._ParameterKey = params.get("ParameterKey")
        self._Type = params.get("Type")
        self._DefaultValue = params.get("DefaultValue")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAggregateConfigRulesRequest(AbstractModel):
    """ListAggregateConfigRules request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Specifies the limit per page.
        :type Limit: int
        :param _Offset: Offset.
        :type Offset: int
        :param _AccountGroupId: Account group ID
        :type AccountGroupId: str
        :param _OrderType: Sort type, descending: desc, ascending: asc.
        :type OrderType: str
        :param _RiskLevel: Risk level

1: High risk.
2: Medium risk.
3: Low risk.
        :type RiskLevel: list of int non-negative
        :param _State: Rule status
        :type State: str
        :param _ComplianceResult: Evaluation result
        :type ComplianceResult: list of str
        :param _RuleName: Name of the rule
        :type RuleName: str
        :param _RuleOwnerId: Rule ownership account ID
        :type RuleOwnerId: int
        """
        self._Limit = None
        self._Offset = None
        self._AccountGroupId = None
        self._OrderType = None
        self._RiskLevel = None
        self._State = None
        self._ComplianceResult = None
        self._RuleName = None
        self._RuleOwnerId = None

    @property
    def Limit(self):
        """Specifies the limit per page.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def AccountGroupId(self):
        """Account group ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def OrderType(self):
        """Sort type, descending: desc, ascending: asc.
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def RiskLevel(self):
        """Risk level

1: High risk.
2: Medium risk.
3: Low risk.
        :rtype: list of int non-negative
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def State(self):
        """Rule status
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ComplianceResult(self):
        """Evaluation result
        :rtype: list of str
        """
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

    @property
    def RuleName(self):
        """Name of the rule
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleOwnerId(self):
        """Rule ownership account ID
        :rtype: int
        """
        return self._RuleOwnerId

    @RuleOwnerId.setter
    def RuleOwnerId(self, RuleOwnerId):
        self._RuleOwnerId = RuleOwnerId


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._AccountGroupId = params.get("AccountGroupId")
        self._OrderType = params.get("OrderType")
        self._RiskLevel = params.get("RiskLevel")
        self._State = params.get("State")
        self._ComplianceResult = params.get("ComplianceResult")
        self._RuleName = params.get("RuleName")
        self._RuleOwnerId = params.get("RuleOwnerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAggregateConfigRulesResponse(AbstractModel):
    """ListAggregateConfigRules response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number
        :type Total: int
        :param _Items: Details
        :type Items: list of ConfigRule
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        """Total number
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        """Details
        :rtype: list of ConfigRule
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ConfigRule()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class ListAggregateDiscoveredResourcesRequest(AbstractModel):
    """ListAggregateDiscoveredResources request structure.

    """

    def __init__(self):
        r"""
        :param _MaxResults: Items per Page
        :type MaxResults: int
        :param _AccountGroupId: Account group ID
        :type AccountGroupId: str
        :param _Filters: resourceName: Resource name; resourceId: Resource ID; resourceType: Resource type
        :type Filters: list of Filter
        :param _Tags: <Tag>
        :type Tags: list of Tag
        :param _NextToken: Next page token.
        :type NextToken: str
        :param _OrderType: Sorting method asc, desc
        :type OrderType: str
        """
        self._MaxResults = None
        self._AccountGroupId = None
        self._Filters = None
        self._Tags = None
        self._NextToken = None
        self._OrderType = None

    @property
    def MaxResults(self):
        """Items per Page
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def AccountGroupId(self):
        """Account group ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def Filters(self):
        """resourceName: Resource name; resourceId: Resource ID; resourceType: Resource type
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Tags(self):
        """<Tag>
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def NextToken(self):
        """Next page token.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def OrderType(self):
        """Sorting method asc, desc
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._MaxResults = params.get("MaxResults")
        self._AccountGroupId = params.get("AccountGroupId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._NextToken = params.get("NextToken")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAggregateDiscoveredResourcesResponse(AbstractModel):
    """ListAggregateDiscoveredResources response structure.

    """

    def __init__(self):
        r"""
        :param _Items: Details.
        :type Items: list of AggregateResourceInfo
        :param _NextToken: next page
Note: This field may return null, indicating that no valid value is found.
        :type NextToken: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._NextToken = None
        self._RequestId = None

    @property
    def Items(self):
        """Details.
        :rtype: list of AggregateResourceInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def NextToken(self):
        """next page
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AggregateResourceInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._NextToken = params.get("NextToken")
        self._RequestId = params.get("RequestId")


class ListConfigRulesRequest(AbstractModel):
    """ListConfigRules request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Page limit
        :type Limit: int
        :param _Offset: Offset.
        :type Offset: int
        :param _OrderType: Sort type. Descending: desc, Ascending: asc.
        :type OrderType: str
        :param _RiskLevel: Risk level

1: High risk.
2: Medium risk.
3: Low risk.
        :type RiskLevel: list of int non-negative
        :param _State: Rule status
        :type State: str
        :param _ComplianceResult: Evaluation result
        :type ComplianceResult: list of str
        :param _RuleName: Name of the rule
        :type RuleName: str
        """
        self._Limit = None
        self._Offset = None
        self._OrderType = None
        self._RiskLevel = None
        self._State = None
        self._ComplianceResult = None
        self._RuleName = None

    @property
    def Limit(self):
        """Page limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderType(self):
        """Sort type. Descending: desc, Ascending: asc.
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def RiskLevel(self):
        """Risk level

1: High risk.
2: Medium risk.
3: Low risk.
        :rtype: list of int non-negative
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def State(self):
        """Rule status
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ComplianceResult(self):
        """Evaluation result
        :rtype: list of str
        """
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

    @property
    def RuleName(self):
        """Name of the rule
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderType = params.get("OrderType")
        self._RiskLevel = params.get("RiskLevel")
        self._State = params.get("State")
        self._ComplianceResult = params.get("ComplianceResult")
        self._RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListConfigRulesResponse(AbstractModel):
    """ListConfigRules response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number
        :type Total: int
        :param _Items: Details
        :type Items: list of ConfigRule
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        """Total number
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        """Details
        :rtype: list of ConfigRule
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ConfigRule()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class ListDiscoveredResourcesRequest(AbstractModel):
    """ListDiscoveredResources request structure.

    """

    def __init__(self):
        r"""
        :param _MaxResults: Items per Page
        :type MaxResults: int
        :param _Filters: resourceName: Resource name resourceId: Resource ID
        :type Filters: list of Filter
        :param _Tags: Tag
        :type Tags: list of Tag
        :param _NextToken: Next page token.
        :type NextToken: str
        :param _OrderType: Sorting method asc, desc
        :type OrderType: str
        """
        self._MaxResults = None
        self._Filters = None
        self._Tags = None
        self._NextToken = None
        self._OrderType = None

    @property
    def MaxResults(self):
        """Items per Page
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def Filters(self):
        """resourceName: Resource name resourceId: Resource ID
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Tags(self):
        """Tag
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def NextToken(self):
        """Next page token.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def OrderType(self):
        """Sorting method asc, desc
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._MaxResults = params.get("MaxResults")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._NextToken = params.get("NextToken")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDiscoveredResourcesResponse(AbstractModel):
    """ListDiscoveredResources response structure.

    """

    def __init__(self):
        r"""
        :param _Items: Details
        :type Items: list of ResourceListInfo
        :param _NextToken: Next page
Note: This field may return null, indicating that no valid value is found.
        :type NextToken: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._NextToken = None
        self._RequestId = None

    @property
    def Items(self):
        """Details
        :rtype: list of ResourceListInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def NextToken(self):
        """Next page
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ResourceListInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._NextToken = params.get("NextToken")
        self._RequestId = params.get("RequestId")


class PutEvaluationsRequest(AbstractModel):
    """PutEvaluations request structure.

    """

    def __init__(self):
        r"""
        :param _ResultToken: Callback token. Obtained from the ResultToken value in the Context of the selected Serverless Cloud Function (SCF) for the custom rule.
        :type ResultToken: str
        :param _Evaluations: Custom rule evaluation result information.
        :type Evaluations: list of Evaluation
        """
        self._ResultToken = None
        self._Evaluations = None

    @property
    def ResultToken(self):
        """Callback token. Obtained from the ResultToken value in the Context of the selected Serverless Cloud Function (SCF) for the custom rule.
        :rtype: str
        """
        return self._ResultToken

    @ResultToken.setter
    def ResultToken(self, ResultToken):
        self._ResultToken = ResultToken

    @property
    def Evaluations(self):
        """Custom rule evaluation result information.
        :rtype: list of Evaluation
        """
        return self._Evaluations

    @Evaluations.setter
    def Evaluations(self, Evaluations):
        self._Evaluations = Evaluations


    def _deserialize(self, params):
        self._ResultToken = params.get("ResultToken")
        if params.get("Evaluations") is not None:
            self._Evaluations = []
            for item in params.get("Evaluations"):
                obj = Evaluation()
                obj._deserialize(item)
                self._Evaluations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutEvaluationsResponse(AbstractModel):
    """PutEvaluations response structure.

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


class ResourceListInfo(AbstractModel):
    """Resource list information response parameters structure

    """

    def __init__(self):
        r"""
        :param _ResourceType: Resource type
        :type ResourceType: str
        :param _ResourceName: Resource name
        :type ResourceName: str
        :param _ResourceId: Resource ID
        :type ResourceId: str
        :param _ResourceRegion: Region

Note: This field may return null, indicating that no valid value is found.
        :type ResourceRegion: str
        :param _ResourceStatus: Resource Status

Note: This field may return null, indicating that no valid value is found.
        :type ResourceStatus: str
        :param _ResourceDelete: 1: Deleted. 2: Not deleted.
Note: This field may return null, indicating that no valid value is found.
        :type ResourceDelete: int
        :param _ResourceCreateTime: Resource creation time

Note: This field may return null, indicating that no valid value is found.
        :type ResourceCreateTime: str
        :param _Tags: Tag information

Note: This field may return null, indicating that no valid value is found.
        :type Tags: list of Tag
        :param _ResourceZone: Availability zone

Note: This field may return null, indicating that no valid value is found.
        :type ResourceZone: str
        :param _ComplianceResult: Compliance status.
Note: This field may return null, indicating that no valid value is found.
        :type ComplianceResult: str
        """
        self._ResourceType = None
        self._ResourceName = None
        self._ResourceId = None
        self._ResourceRegion = None
        self._ResourceStatus = None
        self._ResourceDelete = None
        self._ResourceCreateTime = None
        self._Tags = None
        self._ResourceZone = None
        self._ComplianceResult = None

    @property
    def ResourceType(self):
        """Resource type
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        """Resource name
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceId(self):
        """Resource ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceRegion(self):
        """Region

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceStatus(self):
        """Resource Status

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus

    @property
    def ResourceDelete(self):
        """1: Deleted. 2: Not deleted.
Note: This field may return null, indicating that no valid value is found.
        :rtype: int
        """
        return self._ResourceDelete

    @ResourceDelete.setter
    def ResourceDelete(self, ResourceDelete):
        self._ResourceDelete = ResourceDelete

    @property
    def ResourceCreateTime(self):
        """Resource creation time

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ResourceCreateTime

    @ResourceCreateTime.setter
    def ResourceCreateTime(self, ResourceCreateTime):
        self._ResourceCreateTime = ResourceCreateTime

    @property
    def Tags(self):
        """Tag information

Note: This field may return null, indicating that no valid value is found.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ResourceZone(self):
        """Availability zone

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ResourceZone

    @ResourceZone.setter
    def ResourceZone(self, ResourceZone):
        self._ResourceZone = ResourceZone

    @property
    def ComplianceResult(self):
        """Compliance status.
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._ResourceName = params.get("ResourceName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceStatus = params.get("ResourceStatus")
        self._ResourceDelete = params.get("ResourceDelete")
        self._ResourceCreateTime = params.get("ResourceCreateTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ResourceZone = params.get("ResourceZone")
        self._ComplianceResult = params.get("ComplianceResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceConditionForManage(AbstractModel):
    """Managing end rule conditions

    """

    def __init__(self):
        r"""
        :param _EmptyAs: Condition is empty, Compliant: COMPLIANT, Non-compliant: NON_COMPLIANT, Not applicable: NOT_APPLICABLE.
Note: This field may return null, indicating that no valid value is found.
        :type EmptyAs: str
        :param _SelectPath: Configuration path

Note: This field may return null, indicating that no valid value is found.
        :type SelectPath: str
        :param _Operator: Operators
Note: This field may return null, indicating that no valid value is found.
        :type Operator: str
        :param _Required: Required or not.

Note: This field may return null, indicating that no valid value is found.
        :type Required: bool
        :param _DesiredValue: Expected value
Note: This field may return null, indicating that no valid value is found.
        :type DesiredValue: str
        """
        self._EmptyAs = None
        self._SelectPath = None
        self._Operator = None
        self._Required = None
        self._DesiredValue = None

    @property
    def EmptyAs(self):
        """Condition is empty, Compliant: COMPLIANT, Non-compliant: NON_COMPLIANT, Not applicable: NOT_APPLICABLE.
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._EmptyAs

    @EmptyAs.setter
    def EmptyAs(self, EmptyAs):
        self._EmptyAs = EmptyAs

    @property
    def SelectPath(self):
        """Configuration path

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._SelectPath

    @SelectPath.setter
    def SelectPath(self, SelectPath):
        self._SelectPath = SelectPath

    @property
    def Operator(self):
        """Operators
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Required(self):
        """Required or not.

Note: This field may return null, indicating that no valid value is found.
        :rtype: bool
        """
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required

    @property
    def DesiredValue(self):
        """Expected value
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._DesiredValue

    @DesiredValue.setter
    def DesiredValue(self, DesiredValue):
        self._DesiredValue = DesiredValue


    def _deserialize(self, params):
        self._EmptyAs = params.get("EmptyAs")
        self._SelectPath = params.get("SelectPath")
        self._Operator = params.get("Operator")
        self._Required = params.get("Required")
        self._DesiredValue = params.get("DesiredValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key

Note: This field may return null, indicating that no valid value is found.
        :type TagKey: str
        :param _TagValue: Tag value

Note: This field may return null, indicating that no valid value is found.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """Tag key

Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value

Note: This field may return null, indicating that no valid value is found.
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
        


class TriggerType(AbstractModel):
    """Rule supports trigger type

    """

    def __init__(self):
        r"""
        :param _MessageType: Trigger Type
        :type MessageType: str
        :param _MaximumExecutionFrequency: Trigger time period
Note: This field may return null, indicating that no valid value is found.
        :type MaximumExecutionFrequency: str
        """
        self._MessageType = None
        self._MaximumExecutionFrequency = None

    @property
    def MessageType(self):
        """Trigger Type
        :rtype: str
        """
        return self._MessageType

    @MessageType.setter
    def MessageType(self, MessageType):
        self._MessageType = MessageType

    @property
    def MaximumExecutionFrequency(self):
        """Trigger time period
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._MaximumExecutionFrequency

    @MaximumExecutionFrequency.setter
    def MaximumExecutionFrequency(self, MaximumExecutionFrequency):
        self._MaximumExecutionFrequency = MaximumExecutionFrequency


    def _deserialize(self, params):
        self._MessageType = params.get("MessageType")
        self._MaximumExecutionFrequency = params.get("MaximumExecutionFrequency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        