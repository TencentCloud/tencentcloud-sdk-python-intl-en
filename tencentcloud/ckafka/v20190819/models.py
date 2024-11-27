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


class Acl(AbstractModel):
    """ACL object entity

    """

    def __init__(self):
        r"""
        :param _ResourceType: ACL resource type. 0: UNKNOWN, 1: ANY, 2: TOPIC, 3: GROUP, 4: CLUSTER, 5: TRANSACTIONAL_ID. Currently, only `TOPIC` is available,
        :type ResourceType: int
        :param _ResourceName: Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name
        :type ResourceName: str
        :param _Principal: User list. The default value is `User:*`, which means that any user can access. The current user can only be one included in the user list
Note: this field may return null, indicating that no valid values can be obtained.
        :type Principal: str
        :param _Host: The default value is `*`, which means that any host can access. Currently, CKafka does not support the host as `*`, but the future product based on the open-source Kafka will directly support this
Note: this field may return null, indicating that no valid values can be obtained.
        :type Host: str
        :param _Operation: ACL operation mode. 0: UNKNOWN, 1: ANY, 2: ALL, 3: READ, 4: WRITE, 5: CREATE, 6: DELETE, 7: ALTER, 8: DESCRIBE, 9: CLUSTER_ACTION, 10: DESCRIBE_CONFIGS, 11: ALTER_CONFIGS, 12: IDEMPOTEN_WRITE
        :type Operation: int
        :param _PermissionType: Permission type. 0: UNKNOWN, 1: ANY, 2: DENY, 3: ALLOW
        :type PermissionType: int
        """
        self._ResourceType = None
        self._ResourceName = None
        self._Principal = None
        self._Host = None
        self._Operation = None
        self._PermissionType = None

    @property
    def ResourceType(self):
        """ACL resource type. 0: UNKNOWN, 1: ANY, 2: TOPIC, 3: GROUP, 4: CLUSTER, 5: TRANSACTIONAL_ID. Currently, only `TOPIC` is available,
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        """Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Principal(self):
        """User list. The default value is `User:*`, which means that any user can access. The current user can only be one included in the user list
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Principal

    @Principal.setter
    def Principal(self, Principal):
        self._Principal = Principal

    @property
    def Host(self):
        """The default value is `*`, which means that any host can access. Currently, CKafka does not support the host as `*`, but the future product based on the open-source Kafka will directly support this
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Operation(self):
        """ACL operation mode. 0: UNKNOWN, 1: ANY, 2: ALL, 3: READ, 4: WRITE, 5: CREATE, 6: DELETE, 7: ALTER, 8: DESCRIBE, 9: CLUSTER_ACTION, 10: DESCRIBE_CONFIGS, 11: ALTER_CONFIGS, 12: IDEMPOTEN_WRITE
        :rtype: int
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PermissionType(self):
        """Permission type. 0: UNKNOWN, 1: ANY, 2: DENY, 3: ALLOW
        :rtype: int
        """
        return self._PermissionType

    @PermissionType.setter
    def PermissionType(self, PermissionType):
        self._PermissionType = PermissionType


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._ResourceName = params.get("ResourceName")
        self._Principal = params.get("Principal")
        self._Host = params.get("Host")
        self._Operation = params.get("Operation")
        self._PermissionType = params.get("PermissionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclResponse(AbstractModel):
    """Set of returned ACL results

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible data entries
        :type TotalCount: int
        :param _AclList: ACL list
Note: this field may return null, indicating that no valid values can be obtained.
        :type AclList: list of Acl
        """
        self._TotalCount = None
        self._AclList = None

    @property
    def TotalCount(self):
        """Number of eligible data entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AclList(self):
        """ACL list
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Acl
        """
        return self._AclList

    @AclList.setter
    def AclList(self, AclList):
        self._AclList = AclList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AclList") is not None:
            self._AclList = []
            for item in params.get("AclList"):
                obj = Acl()
                obj._deserialize(item)
                self._AclList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclRule(AbstractModel):
    """Output parameters of ACL rule list APIs

    """

    def __init__(self):
        r"""
        :param _RuleName: ACL rule name.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type RuleName: str
        :param _InstanceId: Instance ID.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _PatternType: Matching type. Currently, only prefix match is supported. Enumerated value list: PREFIXED
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type PatternType: str
        :param _Pattern: Prefix value for prefix match.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Pattern: str
        :param _ResourceType: ACL resource type. Only “Topic” is supported. Enumerated value list: Topic.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ResourceType: str
        :param _AclList: ACL information contained in the rule.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type AclList: str
        :param _CreateTimeStamp: Creation time of the rule.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type CreateTimeStamp: str
        :param _IsApplied: A parameter used to specify whether the preset ACL rule is applied to new topics.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type IsApplied: int
        :param _UpdateTimeStamp: Rule update time.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type UpdateTimeStamp: str
        :param _Comment: Remarks of the rule.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Comment: str
        :param _TopicName: One of the corresponding topic names that is displayed.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type TopicName: str
        :param _TopicCount: The number of topics that apply this ACL rule.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type TopicCount: int
        :param _PatternTypeTitle: Name of rule type.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PatternTypeTitle: str
        """
        self._RuleName = None
        self._InstanceId = None
        self._PatternType = None
        self._Pattern = None
        self._ResourceType = None
        self._AclList = None
        self._CreateTimeStamp = None
        self._IsApplied = None
        self._UpdateTimeStamp = None
        self._Comment = None
        self._TopicName = None
        self._TopicCount = None
        self._PatternTypeTitle = None

    @property
    def RuleName(self):
        """ACL rule name.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def InstanceId(self):
        """Instance ID.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PatternType(self):
        """Matching type. Currently, only prefix match is supported. Enumerated value list: PREFIXED
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PatternType

    @PatternType.setter
    def PatternType(self, PatternType):
        self._PatternType = PatternType

    @property
    def Pattern(self):
        """Prefix value for prefix match.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def ResourceType(self):
        """ACL resource type. Only “Topic” is supported. Enumerated value list: Topic.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def AclList(self):
        """ACL information contained in the rule.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AclList

    @AclList.setter
    def AclList(self, AclList):
        self._AclList = AclList

    @property
    def CreateTimeStamp(self):
        """Creation time of the rule.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTimeStamp

    @CreateTimeStamp.setter
    def CreateTimeStamp(self, CreateTimeStamp):
        self._CreateTimeStamp = CreateTimeStamp

    @property
    def IsApplied(self):
        """A parameter used to specify whether the preset ACL rule is applied to new topics.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsApplied

    @IsApplied.setter
    def IsApplied(self, IsApplied):
        self._IsApplied = IsApplied

    @property
    def UpdateTimeStamp(self):
        """Rule update time.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdateTimeStamp

    @UpdateTimeStamp.setter
    def UpdateTimeStamp(self, UpdateTimeStamp):
        self._UpdateTimeStamp = UpdateTimeStamp

    @property
    def Comment(self):
        """Remarks of the rule.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def TopicName(self):
        """One of the corresponding topic names that is displayed.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicCount(self):
        """The number of topics that apply this ACL rule.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TopicCount

    @TopicCount.setter
    def TopicCount(self, TopicCount):
        self._TopicCount = TopicCount

    @property
    def PatternTypeTitle(self):
        """Name of rule type.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PatternTypeTitle

    @PatternTypeTitle.setter
    def PatternTypeTitle(self, PatternTypeTitle):
        self._PatternTypeTitle = PatternTypeTitle


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._InstanceId = params.get("InstanceId")
        self._PatternType = params.get("PatternType")
        self._Pattern = params.get("Pattern")
        self._ResourceType = params.get("ResourceType")
        self._AclList = params.get("AclList")
        self._CreateTimeStamp = params.get("CreateTimeStamp")
        self._IsApplied = params.get("IsApplied")
        self._UpdateTimeStamp = params.get("UpdateTimeStamp")
        self._Comment = params.get("Comment")
        self._TopicName = params.get("TopicName")
        self._TopicCount = params.get("TopicCount")
        self._PatternTypeTitle = params.get("PatternTypeTitle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclRuleInfo(AbstractModel):
    """Four pieces of information of ACL rules: source IP address, destination IP address, source port, and destination port

    """

    def __init__(self):
        r"""
        :param _Operation: ACL operation types. Enumerated values: `All` (all operations), `Read` (read), `Write` (write).
        :type Operation: str
        :param _PermissionType: Permission types: `Deny`, `Allow`.
        :type PermissionType: str
        :param _Host: The default value is `*`, which means that any host can access the topic. CKafka currently does not support specifying a host value of * or an IP range.
        :type Host: str
        :param _Principal: The list of users allowed to access the topic. Default value: `User:*`, which means all users. The current user must be in the user list. Add the prefix `User:` before the user name (`User:A`, for example).
        :type Principal: str
        """
        self._Operation = None
        self._PermissionType = None
        self._Host = None
        self._Principal = None

    @property
    def Operation(self):
        """ACL operation types. Enumerated values: `All` (all operations), `Read` (read), `Write` (write).
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PermissionType(self):
        """Permission types: `Deny`, `Allow`.
        :rtype: str
        """
        return self._PermissionType

    @PermissionType.setter
    def PermissionType(self, PermissionType):
        self._PermissionType = PermissionType

    @property
    def Host(self):
        """The default value is `*`, which means that any host can access the topic. CKafka currently does not support specifying a host value of * or an IP range.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Principal(self):
        """The list of users allowed to access the topic. Default value: `User:*`, which means all users. The current user must be in the user list. Add the prefix `User:` before the user name (`User:A`, for example).
        :rtype: str
        """
        return self._Principal

    @Principal.setter
    def Principal(self, Principal):
        self._Principal = Principal


    def _deserialize(self, params):
        self._Operation = params.get("Operation")
        self._PermissionType = params.get("PermissionType")
        self._Host = params.get("Host")
        self._Principal = params.get("Principal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclRuleResp(AbstractModel):
    """Results returned by the `AclRuleList` API

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of data entries
        :type TotalCount: int
        :param _AclRuleList: ACL rule list
Note: This field may return null, indicating that no valid values can be obtained.
        :type AclRuleList: list of AclRule
        """
        self._TotalCount = None
        self._AclRuleList = None

    @property
    def TotalCount(self):
        """Total number of data entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AclRuleList(self):
        """ACL rule list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of AclRule
        """
        return self._AclRuleList

    @AclRuleList.setter
    def AclRuleList(self, AclRuleList):
        self._AclRuleList = AclRuleList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AclRuleList") is not None:
            self._AclRuleList = []
            for item in params.get("AclRuleList"):
                obj = AclRule()
                obj._deserialize(item)
                self._AclRuleList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppIdResponse(AbstractModel):
    """`AppId` query result

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible `AppId`
        :type TotalCount: int
        :param _AppIdList: List of eligible `AppId`
Note: this field may return null, indicating that no valid values can be obtained.
        :type AppIdList: list of int
        """
        self._TotalCount = None
        self._AppIdList = None

    @property
    def TotalCount(self):
        """Number of eligible `AppId`
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AppIdList(self):
        """List of eligible `AppId`
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._AppIdList = params.get("AppIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Assignment(AbstractModel):
    """Stores the information of partition assigned to this consumer

    """

    def __init__(self):
        r"""
        :param _Version: Assignment version information
        :type Version: int
        :param _Topics: Topic information list
Note: this field may return null, indicating that no valid values can be obtained.
        :type Topics: list of GroupInfoTopics
        """
        self._Version = None
        self._Topics = None

    @property
    def Version(self):
        """Assignment version information
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Topics(self):
        """Topic information list
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of GroupInfoTopics
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics


    def _deserialize(self, params):
        self._Version = params.get("Version")
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = GroupInfoTopics()
                obj._deserialize(item)
                self._Topics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchContent(AbstractModel):
    """Message content that can be sent in batches

    """

    def __init__(self):
        r"""
        :param _Body: Message body that is sent.
        :type Body: str
        :param _Key: Message sending key name.
        :type Key: str
        """
        self._Body = None
        self._Key = None

    @property
    def Body(self):
        """Message body that is sent.
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Key(self):
        """Message sending key name.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key


    def _deserialize(self, params):
        self._Body = params.get("Body")
        self._Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateAclRequest(AbstractModel):
    """BatchCreateAcl request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _ResourceType: ACL resource type. Default value: `2` (topic).
        :type ResourceType: int
        :param _ResourceNames: Resource list array.
        :type ResourceNames: list of str
        :param _RuleList: ACL rule list.
        :type RuleList: list of AclRuleInfo
        """
        self._InstanceId = None
        self._ResourceType = None
        self._ResourceNames = None
        self._RuleList = None

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
    def ResourceType(self):
        """ACL resource type. Default value: `2` (topic).
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceNames(self):
        """Resource list array.
        :rtype: list of str
        """
        return self._ResourceNames

    @ResourceNames.setter
    def ResourceNames(self, ResourceNames):
        self._ResourceNames = ResourceNames

    @property
    def RuleList(self):
        """ACL rule list.
        :rtype: list of AclRuleInfo
        """
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceNames = params.get("ResourceNames")
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = AclRuleInfo()
                obj._deserialize(item)
                self._RuleList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateAclResponse(AbstractModel):
    """BatchCreateAcl response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Status code.
        :type Result: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Status code.
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class BatchModifyGroupOffsetsRequest(AbstractModel):
    """BatchModifyGroupOffsets request structure.

    """

    def __init__(self):
        r"""
        :param _GroupName: Consumer group name.
        :type GroupName: str
        :param _InstanceId: Instance name.
        :type InstanceId: str
        :param _Partitions: Partition information.
        :type Partitions: list of Partitions
        :param _TopicName: Name of the specified topic. Default value: names of all topics.
        :type TopicName: list of str
        """
        self._GroupName = None
        self._InstanceId = None
        self._Partitions = None
        self._TopicName = None

    @property
    def GroupName(self):
        """Consumer group name.
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def InstanceId(self):
        """Instance name.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Partitions(self):
        """Partition information.
        :rtype: list of Partitions
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def TopicName(self):
        """Name of the specified topic. Default value: names of all topics.
        :rtype: list of str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._InstanceId = params.get("InstanceId")
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = Partitions()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyGroupOffsetsResponse(AbstractModel):
    """BatchModifyGroupOffsets response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class BatchModifyTopicAttributesRequest(AbstractModel):
    """BatchModifyTopicAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Topic: Topic attribute list
        :type Topic: list of BatchModifyTopicInfo
        """
        self._InstanceId = None
        self._Topic = None

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
    def Topic(self):
        """Topic attribute list
        :rtype: list of BatchModifyTopicInfo
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Topic") is not None:
            self._Topic = []
            for item in params.get("Topic"):
                obj = BatchModifyTopicInfo()
                obj._deserialize(item)
                self._Topic.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyTopicAttributesResponse(AbstractModel):
    """BatchModifyTopicAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: list of BatchModifyTopicResultDTO
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result.
        :rtype: list of BatchModifyTopicResultDTO
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = BatchModifyTopicResultDTO()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class BatchModifyTopicInfo(AbstractModel):
    """Topic parameters that can be modified in batches

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name.
        :type TopicName: str
        :param _PartitionNum: The number of partitions.
        :type PartitionNum: int
        :param _Note: Remarks.
        :type Note: str
        :param _ReplicaNum: Number of replicas.
        :type ReplicaNum: int
        :param _CleanUpPolicy: Message deletion policy. Valid values: `delete`, `compact`.
        :type CleanUpPolicy: str
        :param _MinInsyncReplicas: The minimum number of replicas specified by `min.insync.replicas` when the producer sets `request.required.acks` to `-1`.
        :type MinInsyncReplicas: int
        :param _UncleanLeaderElectionEnable: Whether to allow a non-ISR replica to be the leader.
        :type UncleanLeaderElectionEnable: bool
        :param _RetentionMs: Message retention period in topic dimension in milliseconds. Value range: 1 minute to 90 days.
        :type RetentionMs: int
        :param _RetentionBytes: Message retention size in topic dimension. Value range: 1 MB - 1024 GB.
        :type RetentionBytes: int
        :param _SegmentMs: Segment rolling duration in milliseconds. Value range: 1-90 days.
        :type SegmentMs: int
        :param _MaxMessageBytes: Message size per batch. Value range: 1 KB - 12 MB.
        :type MaxMessageBytes: int
        """
        self._TopicName = None
        self._PartitionNum = None
        self._Note = None
        self._ReplicaNum = None
        self._CleanUpPolicy = None
        self._MinInsyncReplicas = None
        self._UncleanLeaderElectionEnable = None
        self._RetentionMs = None
        self._RetentionBytes = None
        self._SegmentMs = None
        self._MaxMessageBytes = None

    @property
    def TopicName(self):
        """Topic name.
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionNum(self):
        """The number of partitions.
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def Note(self):
        """Remarks.
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def ReplicaNum(self):
        """Number of replicas.
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def CleanUpPolicy(self):
        """Message deletion policy. Valid values: `delete`, `compact`.
        :rtype: str
        """
        return self._CleanUpPolicy

    @CleanUpPolicy.setter
    def CleanUpPolicy(self, CleanUpPolicy):
        self._CleanUpPolicy = CleanUpPolicy

    @property
    def MinInsyncReplicas(self):
        """The minimum number of replicas specified by `min.insync.replicas` when the producer sets `request.required.acks` to `-1`.
        :rtype: int
        """
        return self._MinInsyncReplicas

    @MinInsyncReplicas.setter
    def MinInsyncReplicas(self, MinInsyncReplicas):
        self._MinInsyncReplicas = MinInsyncReplicas

    @property
    def UncleanLeaderElectionEnable(self):
        """Whether to allow a non-ISR replica to be the leader.
        :rtype: bool
        """
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def RetentionMs(self):
        """Message retention period in topic dimension in milliseconds. Value range: 1 minute to 90 days.
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def RetentionBytes(self):
        """Message retention size in topic dimension. Value range: 1 MB - 1024 GB.
        :rtype: int
        """
        return self._RetentionBytes

    @RetentionBytes.setter
    def RetentionBytes(self, RetentionBytes):
        self._RetentionBytes = RetentionBytes

    @property
    def SegmentMs(self):
        """Segment rolling duration in milliseconds. Value range: 1-90 days.
        :rtype: int
        """
        return self._SegmentMs

    @SegmentMs.setter
    def SegmentMs(self, SegmentMs):
        self._SegmentMs = SegmentMs

    @property
    def MaxMessageBytes(self):
        """Message size per batch. Value range: 1 KB - 12 MB.
        :rtype: int
        """
        return self._MaxMessageBytes

    @MaxMessageBytes.setter
    def MaxMessageBytes(self, MaxMessageBytes):
        self._MaxMessageBytes = MaxMessageBytes


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._PartitionNum = params.get("PartitionNum")
        self._Note = params.get("Note")
        self._ReplicaNum = params.get("ReplicaNum")
        self._CleanUpPolicy = params.get("CleanUpPolicy")
        self._MinInsyncReplicas = params.get("MinInsyncReplicas")
        self._UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self._RetentionMs = params.get("RetentionMs")
        self._RetentionBytes = params.get("RetentionBytes")
        self._SegmentMs = params.get("SegmentMs")
        self._MaxMessageBytes = params.get("MaxMessageBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyTopicResultDTO(AbstractModel):
    """Results of the batch modified topic attributes

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _TopicName: Topic name.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TopicName: str
        :param _ReturnCode: Status code.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ReturnCode: str
        :param _Message: Message status.
        :type Message: str
        """
        self._InstanceId = None
        self._TopicName = None
        self._ReturnCode = None
        self._Message = None

    @property
    def InstanceId(self):
        """Instance ID.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        """Topic name.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def ReturnCode(self):
        """Status code.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def Message(self):
        """Message status.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._ReturnCode = params.get("ReturnCode")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterInfo(AbstractModel):
    """Cluster information entity

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: int
        :param _ClusterName: Cluster name
        :type ClusterName: str
        :param _MaxDiskSize: The cluster’s maximum disk capacity in GB
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type MaxDiskSize: int
        :param _MaxBandWidth: The cluster’s maximum bandwidth in MB/s
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type MaxBandWidth: int
        :param _AvailableDiskSize: The cluster’s available disk capacity in GB
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type AvailableDiskSize: int
        :param _AvailableBandWidth: The cluster’s available bandwidth in MB/s
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type AvailableBandWidth: int
        :param _ZoneId: The AZ where the cluster resides
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ZoneId: int
        :param _ZoneIds: The AZ where the cluster nodes reside. If the cluster is a multi-AZ cluster, this field means multiple AZs where the cluster nodes reside.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ZoneIds: list of int
        """
        self._ClusterId = None
        self._ClusterName = None
        self._MaxDiskSize = None
        self._MaxBandWidth = None
        self._AvailableDiskSize = None
        self._AvailableBandWidth = None
        self._ZoneId = None
        self._ZoneIds = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: int
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        """Cluster name
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def MaxDiskSize(self):
        """The cluster’s maximum disk capacity in GB
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize

    @property
    def MaxBandWidth(self):
        """The cluster’s maximum bandwidth in MB/s
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def AvailableDiskSize(self):
        """The cluster’s available disk capacity in GB
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AvailableDiskSize

    @AvailableDiskSize.setter
    def AvailableDiskSize(self, AvailableDiskSize):
        self._AvailableDiskSize = AvailableDiskSize

    @property
    def AvailableBandWidth(self):
        """The cluster’s available bandwidth in MB/s
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AvailableBandWidth

    @AvailableBandWidth.setter
    def AvailableBandWidth(self, AvailableBandWidth):
        self._AvailableBandWidth = AvailableBandWidth

    @property
    def ZoneId(self):
        """The AZ where the cluster resides
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneIds(self):
        """The AZ where the cluster nodes reside. If the cluster is a multi-AZ cluster, this field means multiple AZs where the cluster nodes reside.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._MaxDiskSize = params.get("MaxDiskSize")
        self._MaxBandWidth = params.get("MaxBandWidth")
        self._AvailableDiskSize = params.get("AvailableDiskSize")
        self._AvailableBandWidth = params.get("AvailableBandWidth")
        self._ZoneId = params.get("ZoneId")
        self._ZoneIds = params.get("ZoneIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Config(AbstractModel):
    """Advanced configuration object

    """

    def __init__(self):
        r"""
        :param _Retention: Message retention period
Note: this field may return null, indicating that no valid values can be obtained.
        :type Retention: int
        :param _MinInsyncReplicas: Minimum number of sync replications
Note: this field may return null, indicating that no valid values can be obtained.
        :type MinInsyncReplicas: int
        :param _CleanUpPolicy: Log cleanup mode. Default value: delete.
delete: logs will be deleted by save time; compact: logs will be compressed by key; compact, delete: logs will be compressed by key and deleted by save time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CleanUpPolicy: str
        :param _SegmentMs: Segment rolling duration
Note: this field may return null, indicating that no valid values can be obtained.
        :type SegmentMs: int
        :param _UncleanLeaderElectionEnable: 0: false, 1: true.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UncleanLeaderElectionEnable: int
        :param _SegmentBytes: Number of bytes for segment rolling
Note: this field may return null, indicating that no valid values can be obtained.
        :type SegmentBytes: int
        :param _MaxMessageBytes: Maximum number of message bytes
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxMessageBytes: int
        :param _RetentionBytes: Message retention file size.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RetentionBytes: int
        """
        self._Retention = None
        self._MinInsyncReplicas = None
        self._CleanUpPolicy = None
        self._SegmentMs = None
        self._UncleanLeaderElectionEnable = None
        self._SegmentBytes = None
        self._MaxMessageBytes = None
        self._RetentionBytes = None

    @property
    def Retention(self):
        """Message retention period
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Retention

    @Retention.setter
    def Retention(self, Retention):
        self._Retention = Retention

    @property
    def MinInsyncReplicas(self):
        """Minimum number of sync replications
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MinInsyncReplicas

    @MinInsyncReplicas.setter
    def MinInsyncReplicas(self, MinInsyncReplicas):
        self._MinInsyncReplicas = MinInsyncReplicas

    @property
    def CleanUpPolicy(self):
        """Log cleanup mode. Default value: delete.
delete: logs will be deleted by save time; compact: logs will be compressed by key; compact, delete: logs will be compressed by key and deleted by save time.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CleanUpPolicy

    @CleanUpPolicy.setter
    def CleanUpPolicy(self, CleanUpPolicy):
        self._CleanUpPolicy = CleanUpPolicy

    @property
    def SegmentMs(self):
        """Segment rolling duration
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SegmentMs

    @SegmentMs.setter
    def SegmentMs(self, SegmentMs):
        self._SegmentMs = SegmentMs

    @property
    def UncleanLeaderElectionEnable(self):
        """0: false, 1: true.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def SegmentBytes(self):
        """Number of bytes for segment rolling
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SegmentBytes

    @SegmentBytes.setter
    def SegmentBytes(self, SegmentBytes):
        self._SegmentBytes = SegmentBytes

    @property
    def MaxMessageBytes(self):
        """Maximum number of message bytes
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxMessageBytes

    @MaxMessageBytes.setter
    def MaxMessageBytes(self, MaxMessageBytes):
        self._MaxMessageBytes = MaxMessageBytes

    @property
    def RetentionBytes(self):
        """Message retention file size.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RetentionBytes

    @RetentionBytes.setter
    def RetentionBytes(self, RetentionBytes):
        self._RetentionBytes = RetentionBytes


    def _deserialize(self, params):
        self._Retention = params.get("Retention")
        self._MinInsyncReplicas = params.get("MinInsyncReplicas")
        self._CleanUpPolicy = params.get("CleanUpPolicy")
        self._SegmentMs = params.get("SegmentMs")
        self._UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self._SegmentBytes = params.get("SegmentBytes")
        self._MaxMessageBytes = params.get("MaxMessageBytes")
        self._RetentionBytes = params.get("RetentionBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerGroup(AbstractModel):
    """User group entity

    """

    def __init__(self):
        r"""
        :param _ConsumerGroupName: User group name
        :type ConsumerGroupName: str
        :param _SubscribedInfo: Subscribed message entity
        :type SubscribedInfo: list of SubscribedInfo
        """
        self._ConsumerGroupName = None
        self._SubscribedInfo = None

    @property
    def ConsumerGroupName(self):
        """User group name
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def SubscribedInfo(self):
        """Subscribed message entity
        :rtype: list of SubscribedInfo
        """
        return self._SubscribedInfo

    @SubscribedInfo.setter
    def SubscribedInfo(self, SubscribedInfo):
        self._SubscribedInfo = SubscribedInfo


    def _deserialize(self, params):
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        if params.get("SubscribedInfo") is not None:
            self._SubscribedInfo = []
            for item in params.get("SubscribedInfo"):
                obj = SubscribedInfo()
                obj._deserialize(item)
                self._SubscribedInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerGroupResponse(AbstractModel):
    """Returned consumer group result entity

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible consumer groups
        :type TotalCount: int
        :param _TopicList: Topic list
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicList: list of ConsumerGroupTopic
        :param _GroupList: Consumer group list
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupList: list of ConsumerGroup
        :param _TotalPartition: Total number of partitions
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalPartition: int
        :param _PartitionListForMonitor: List of monitored partitions
Note: this field may return null, indicating that no valid values can be obtained.
        :type PartitionListForMonitor: list of Partition
        :param _TotalTopic: Total number of topics
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalTopic: int
        :param _TopicListForMonitor: List of monitored topics
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicListForMonitor: list of ConsumerGroupTopic
        :param _GroupListForMonitor: List of monitored groups
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupListForMonitor: list of Group
        """
        self._TotalCount = None
        self._TopicList = None
        self._GroupList = None
        self._TotalPartition = None
        self._PartitionListForMonitor = None
        self._TotalTopic = None
        self._TopicListForMonitor = None
        self._GroupListForMonitor = None

    @property
    def TotalCount(self):
        """Number of eligible consumer groups
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TopicList(self):
        """Topic list
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of ConsumerGroupTopic
        """
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList

    @property
    def GroupList(self):
        """Consumer group list
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of ConsumerGroup
        """
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList

    @property
    def TotalPartition(self):
        """Total number of partitions
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalPartition

    @TotalPartition.setter
    def TotalPartition(self, TotalPartition):
        self._TotalPartition = TotalPartition

    @property
    def PartitionListForMonitor(self):
        """List of monitored partitions
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Partition
        """
        return self._PartitionListForMonitor

    @PartitionListForMonitor.setter
    def PartitionListForMonitor(self, PartitionListForMonitor):
        self._PartitionListForMonitor = PartitionListForMonitor

    @property
    def TotalTopic(self):
        """Total number of topics
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalTopic

    @TotalTopic.setter
    def TotalTopic(self, TotalTopic):
        self._TotalTopic = TotalTopic

    @property
    def TopicListForMonitor(self):
        """List of monitored topics
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of ConsumerGroupTopic
        """
        return self._TopicListForMonitor

    @TopicListForMonitor.setter
    def TopicListForMonitor(self, TopicListForMonitor):
        self._TopicListForMonitor = TopicListForMonitor

    @property
    def GroupListForMonitor(self):
        """List of monitored groups
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Group
        """
        return self._GroupListForMonitor

    @GroupListForMonitor.setter
    def GroupListForMonitor(self, GroupListForMonitor):
        self._GroupListForMonitor = GroupListForMonitor


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TopicList") is not None:
            self._TopicList = []
            for item in params.get("TopicList"):
                obj = ConsumerGroupTopic()
                obj._deserialize(item)
                self._TopicList.append(obj)
        if params.get("GroupList") is not None:
            self._GroupList = []
            for item in params.get("GroupList"):
                obj = ConsumerGroup()
                obj._deserialize(item)
                self._GroupList.append(obj)
        self._TotalPartition = params.get("TotalPartition")
        if params.get("PartitionListForMonitor") is not None:
            self._PartitionListForMonitor = []
            for item in params.get("PartitionListForMonitor"):
                obj = Partition()
                obj._deserialize(item)
                self._PartitionListForMonitor.append(obj)
        self._TotalTopic = params.get("TotalTopic")
        if params.get("TopicListForMonitor") is not None:
            self._TopicListForMonitor = []
            for item in params.get("TopicListForMonitor"):
                obj = ConsumerGroupTopic()
                obj._deserialize(item)
                self._TopicListForMonitor.append(obj)
        if params.get("GroupListForMonitor") is not None:
            self._GroupListForMonitor = []
            for item in params.get("GroupListForMonitor"):
                obj = Group()
                obj._deserialize(item)
                self._GroupListForMonitor.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerGroupTopic(AbstractModel):
    """Consumer group topic object

    """

    def __init__(self):
        r"""
        :param _TopicId: Topic ID
        :type TopicId: str
        :param _TopicName: Topic name
        :type TopicName: str
        """
        self._TopicId = None
        self._TopicName = None

    @property
    def TopicId(self):
        """Topic ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        """Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerRecord(AbstractModel):
    """Message record

    """

    def __init__(self):
        r"""
        :param _Topic: Topic name
        :type Topic: str
        :param _Partition: Partition ID
        :type Partition: int
        :param _Offset: Offset
        :type Offset: int
        :param _Key: Message key
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Key: str
        :param _Value: Message value
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Value: str
        :param _Timestamp: Message timestamp
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Timestamp: int
        :param _Headers: Message headers
Note: This field may return null, indicating that no valid values can be obtained.
        :type Headers: str
        """
        self._Topic = None
        self._Partition = None
        self._Offset = None
        self._Key = None
        self._Value = None
        self._Timestamp = None
        self._Headers = None

    @property
    def Topic(self):
        """Topic name
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        """Partition ID
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        """Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Key(self):
        """Message key
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Message value
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Timestamp(self):
        """Message timestamp
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Headers(self):
        """Message headers
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._Partition = params.get("Partition")
        self._Offset = params.get("Offset")
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Timestamp = params.get("Timestamp")
        self._Headers = params.get("Headers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAclRequest(AbstractModel):
    """CreateAcl request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID information
        :type InstanceId: str
        :param _ResourceType: ACL resource type (`2`: TOPIC, `3`: GROUP, `4`: CLUSTER).
        :type ResourceType: int
        :param _Operation: ACL operation type (`2`: ALL, `3`: READ, `4`: WRITE, `5`: CREATE, `6`: DELETE, `7`: ALTER, `8`: DESCRIBE, `9`: CLUSTER_ACTION, `10`: DESCRIBE_CONFIGS, `11`: ALTER_CONFIGS, `12`: IDEMPOTENT_WRITE).
        :type Operation: int
        :param _PermissionType: Permission type (`2`: DENY, `3`: ALLOW). CKafka currently supports `ALLOW`, which is equivalent to allowlist. `DENY` will be supported for ACLs compatible with open-source Kafka.
        :type PermissionType: int
        :param _ResourceName: Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name; if `resourceType` is `CLUSTER`, this field can be left empty.
        :type ResourceName: str
        :param _Host: The default value is `*`, which means that any host can access. Currently, CKafka does not support the host as `*`, but the future product based on the open-source Kafka will directly support this
        :type Host: str
        :param _Principal: The list of users allowed to access the topic. Default: User:*, meaning all users. The current user must be in the user list. Add `User:` before the user name (`User:A` for example).
        :type Principal: str
        :param _ResourceNameList: The resource name list, which is in JSON string format. Either `ResourceName` or `resourceNameList` can be specified.
        :type ResourceNameList: str
        """
        self._InstanceId = None
        self._ResourceType = None
        self._Operation = None
        self._PermissionType = None
        self._ResourceName = None
        self._Host = None
        self._Principal = None
        self._ResourceNameList = None

    @property
    def InstanceId(self):
        """Instance ID information
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceType(self):
        """ACL resource type (`2`: TOPIC, `3`: GROUP, `4`: CLUSTER).
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Operation(self):
        """ACL operation type (`2`: ALL, `3`: READ, `4`: WRITE, `5`: CREATE, `6`: DELETE, `7`: ALTER, `8`: DESCRIBE, `9`: CLUSTER_ACTION, `10`: DESCRIBE_CONFIGS, `11`: ALTER_CONFIGS, `12`: IDEMPOTENT_WRITE).
        :rtype: int
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PermissionType(self):
        """Permission type (`2`: DENY, `3`: ALLOW). CKafka currently supports `ALLOW`, which is equivalent to allowlist. `DENY` will be supported for ACLs compatible with open-source Kafka.
        :rtype: int
        """
        return self._PermissionType

    @PermissionType.setter
    def PermissionType(self, PermissionType):
        self._PermissionType = PermissionType

    @property
    def ResourceName(self):
        """Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name; if `resourceType` is `CLUSTER`, this field can be left empty.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Host(self):
        """The default value is `*`, which means that any host can access. Currently, CKafka does not support the host as `*`, but the future product based on the open-source Kafka will directly support this
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Principal(self):
        """The list of users allowed to access the topic. Default: User:*, meaning all users. The current user must be in the user list. Add `User:` before the user name (`User:A` for example).
        :rtype: str
        """
        return self._Principal

    @Principal.setter
    def Principal(self, Principal):
        self._Principal = Principal

    @property
    def ResourceNameList(self):
        """The resource name list, which is in JSON string format. Either `ResourceName` or `resourceNameList` can be specified.
        :rtype: str
        """
        return self._ResourceNameList

    @ResourceNameList.setter
    def ResourceNameList(self, ResourceNameList):
        self._ResourceNameList = ResourceNameList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ResourceType = params.get("ResourceType")
        self._Operation = params.get("Operation")
        self._PermissionType = params.get("PermissionType")
        self._ResourceName = params.get("ResourceName")
        self._Host = params.get("Host")
        self._Principal = params.get("Principal")
        self._ResourceNameList = params.get("ResourceNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAclResponse(AbstractModel):
    """CreateAcl response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateAclRuleRequest(AbstractModel):
    """CreateAclRule request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ResourceType: ACL resource type. Currently, the only valid value is `Topic`.
        :type ResourceType: str
        :param _PatternType: Matching type. Valid values: `PREFIXED`(match by prefix), `PRESET` (match by preset policy).
        :type PatternType: str
        :param _RuleName: Rule name
        :type RuleName: str
        :param _RuleList: ACL rule list
        :type RuleList: list of AclRuleInfo
        :param _Pattern: Prefix value for prefix match
        :type Pattern: str
        :param _IsApplied: A parameter used to specify whether the preset ACL rule is applied to new topics
        :type IsApplied: int
        :param _Comment: Remarks for ACL rules
        :type Comment: str
        """
        self._InstanceId = None
        self._ResourceType = None
        self._PatternType = None
        self._RuleName = None
        self._RuleList = None
        self._Pattern = None
        self._IsApplied = None
        self._Comment = None

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
    def ResourceType(self):
        """ACL resource type. Currently, the only valid value is `Topic`.
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def PatternType(self):
        """Matching type. Valid values: `PREFIXED`(match by prefix), `PRESET` (match by preset policy).
        :rtype: str
        """
        return self._PatternType

    @PatternType.setter
    def PatternType(self, PatternType):
        self._PatternType = PatternType

    @property
    def RuleName(self):
        """Rule name
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleList(self):
        """ACL rule list
        :rtype: list of AclRuleInfo
        """
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def Pattern(self):
        """Prefix value for prefix match
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def IsApplied(self):
        """A parameter used to specify whether the preset ACL rule is applied to new topics
        :rtype: int
        """
        return self._IsApplied

    @IsApplied.setter
    def IsApplied(self, IsApplied):
        self._IsApplied = IsApplied

    @property
    def Comment(self):
        """Remarks for ACL rules
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ResourceType = params.get("ResourceType")
        self._PatternType = params.get("PatternType")
        self._RuleName = params.get("RuleName")
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = AclRuleInfo()
                obj._deserialize(item)
                self._RuleList.append(obj)
        self._Pattern = params.get("Pattern")
        self._IsApplied = params.get("IsApplied")
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAclRuleResponse(AbstractModel):
    """CreateAclRule response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Unique key of a rule
        :type Result: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Unique key of a rule
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateConsumerRequest(AbstractModel):
    """CreateConsumer request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _GroupName: Group name.
        :type GroupName: str
        :param _TopicName: Topic name. You must specify the name of an existing topic for either `TopicName` or `TopicNameList`.
        :type TopicName: str
        :param _TopicNameList: Topic name array.
        :type TopicNameList: list of str
        """
        self._InstanceId = None
        self._GroupName = None
        self._TopicName = None
        self._TopicNameList = None

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
    def GroupName(self):
        """Group name.
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TopicName(self):
        """Topic name. You must specify the name of an existing topic for either `TopicName` or `TopicNameList`.
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicNameList(self):
        """Topic name array.
        :rtype: list of str
        """
        return self._TopicNameList

    @TopicNameList.setter
    def TopicNameList(self, TopicNameList):
        self._TopicNameList = TopicNameList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GroupName = params.get("GroupName")
        self._TopicName = params.get("TopicName")
        self._TopicNameList = params.get("TopicNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsumerResponse(AbstractModel):
    """CreateConsumer response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Description of the created consumer group.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Description of the created consumer group.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateDatahubTopicRequest(AbstractModel):
    """CreateDatahubTopic request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Topic name, which is a string of up to 128 characters. It can contain letters, digits, and hyphens (-) and must start with a letter.
        :type Name: str
        :param _PartitionNum: Number of partitions, which should be greater than 0.
        :type PartitionNum: int
        :param _RetentionMs: Message retention period in milliseconds. The current minimum value is 60,000 ms.
        :type RetentionMs: int
        :param _Note: Topic remarks, which are a string of up to 128 characters. It can contain letters, digits, and hyphens (-) and must start with a letter.
        :type Note: str
        :param _Tags: Tag list
        :type Tags: list of Tag
        """
        self._Name = None
        self._PartitionNum = None
        self._RetentionMs = None
        self._Note = None
        self._Tags = None

    @property
    def Name(self):
        """Topic name, which is a string of up to 128 characters. It can contain letters, digits, and hyphens (-) and must start with a letter.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PartitionNum(self):
        """Number of partitions, which should be greater than 0.
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def RetentionMs(self):
        """Message retention period in milliseconds. The current minimum value is 60,000 ms.
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def Note(self):
        """Topic remarks, which are a string of up to 128 characters. It can contain letters, digits, and hyphens (-) and must start with a letter.
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Tags(self):
        """Tag list
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._PartitionNum = params.get("PartitionNum")
        self._RetentionMs = params.get("RetentionMs")
        self._Note = params.get("Note")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatahubTopicResponse(AbstractModel):
    """CreateDatahubTopic response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned creation result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DatahubTopicResp`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned creation result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DatahubTopicResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DatahubTopicResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateInstancePostData(AbstractModel):
    """Data structure returned by the pay-as-you-go instance creation API

    """

    def __init__(self):
        r"""
        :param _FlowId: This parameter has a fixed value of 0 returned by `CreateInstancePre`. It is only used for backend data alignment  and cannot be used as the query condition for `CheckTaskStatus`. 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type FlowId: int
        :param _DealNames: List of order IDs Note: This field may return null, indicating that no valid values can be obtained.
        :type DealNames: list of str
        :param _InstanceId: Instance ID. When multiple instances are purchased, the ID of the first one is returned by default . Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _DealNameInstanceIdMapping: Mapping between orders and the purchased instances.  Note: This field may return null, indicating that no valid values can be obtained.
        :type DealNameInstanceIdMapping: list of DealInstanceDTO
        """
        self._FlowId = None
        self._DealNames = None
        self._InstanceId = None
        self._DealNameInstanceIdMapping = None

    @property
    def FlowId(self):
        """This parameter has a fixed value of 0 returned by `CreateInstancePre`. It is only used for backend data alignment  and cannot be used as the query condition for `CheckTaskStatus`. 
Note:  This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DealNames(self):
        """List of order IDs Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def InstanceId(self):
        """Instance ID. When multiple instances are purchased, the ID of the first one is returned by default . Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealNameInstanceIdMapping(self):
        """Mapping between orders and the purchased instances.  Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DealInstanceDTO
        """
        return self._DealNameInstanceIdMapping

    @DealNameInstanceIdMapping.setter
    def DealNameInstanceIdMapping(self, DealNameInstanceIdMapping):
        self._DealNameInstanceIdMapping = DealNameInstanceIdMapping


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._DealNames = params.get("DealNames")
        self._InstanceId = params.get("InstanceId")
        if params.get("DealNameInstanceIdMapping") is not None:
            self._DealNameInstanceIdMapping = []
            for item in params.get("DealNameInstanceIdMapping"):
                obj = DealInstanceDTO()
                obj._deserialize(item)
                self._DealNameInstanceIdMapping.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancePostRequest(AbstractModel):
    """CreateInstancePost request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceName: Instance name, which is a string of up to 64 characters. It can contain letters, digits, and hyphens (-) and must start with a letter.
        :type InstanceName: str
        :param _BandWidth: Private network peak bandwidth of an instance  in MB/sec.  If you create a Standard Edition instance, pass in the corresponding peak bandwidth for the current instance specification.  If you create a Pro Edition instance, configure the peak bandwidth, partition count, and other parameters as required by Pro Edition.
        :type BandWidth: int
        :param _VpcId: ID of the VPC where the default access point of the created instance resides.  This parameter is required as instances cannot be created in the classic network currently.
        :type VpcId: str
        :param _SubnetId: ID of the subnet  where the default access point of the created instance resides. 
        :type SubnetId: str
        :param _InstanceType: Instance specification.  This parameter is required for a Standard Edition instance but not for a Pro Edition instance.  Valid values:  `1` (Small),  `2` (Standard),  `3` (Advanced),  `4` (Large),  `5` (Xlarge L1),  `6` (Xlarge L2),  `7` (Xlarge L3),  `8` (Xlarge L4),  
        :type InstanceType: int
        :param _MsgRetentionTime: The maximum instance log retention period in minutes by default.  If this parameter is left empty, the default retention period is 1,440 minutes (1 day) to 30 days.  If the message retention period of the topic is explicitly set, it will prevail.
        :type MsgRetentionTime: int
        :param _ClusterId: Cluster ID, which can be selected when you create an instance.  You don’t need to pass in this parameter if the cluster where the instance resides is not specified.
        :type ClusterId: int
        :param _KafkaVersion: Instance version.  Valid values: `0.10.2`, `1.1.1`, `2.4.2`, and `2.8.1`.
        :type KafkaVersion: str
        :param _SpecificationsType: Instance type. Valid values: `standard` (Standard Edition),  `profession`  (Pro Edition)
        :type SpecificationsType: str
        :param _DiskType: Instance disk type. Valid values:  `CLOUD_BASIC` (Premium Cloud Storage),  `CLOUD_SSD` (SSD).  If this parameter is left empty, the default value `CLOUD_BASIC` will be used.
        :type DiskType: str
        :param _DiskSize: Instance disk size, which must meet the requirement of the instance’s specification.
        :type DiskSize: int
        :param _Partition: The maximum number of partitions of the instance, which must meet the requirement of the instance’s specification.
        :type Partition: int
        :param _TopicNum: The maximum number of topics of the instance, which must meet the requirement of the instance’s specification.
        :type TopicNum: int
        :param _ZoneId: AZ of the instance.  When a multi-AZ instance is created, the value of this parameter is the AZ ID of the subnet where the instance’s default access point resides.
        :type ZoneId: int
        :param _MultiZoneFlag: Whether the current instance is a multi-AZ instance
        :type MultiZoneFlag: bool
        :param _ZoneIds: This parameter indicates the list of AZ IDs when the instance is deployed in multiple AZs.  Note that `ZoneId` must be included in the array of this parameter.
        :type ZoneIds: list of int
        :param _InstanceNum: The number of purchased instances.  Default value: `1`. This parameter is optional.  If it is passed in, multiple instances will be created, with their names being `instanceName` plus different suffixes.
        :type InstanceNum: int
        :param _PublicNetworkMonthly: Public network bandwidth in Mbps.  The 3 Mbps of free bandwidth is not included here by default.  For example, if you need 3 Mbps of public network bandwidth, pass in `0`; if you need 6 Mbps, pass in `3`. The value must be an integer multiple of 3.
        :type PublicNetworkMonthly: int
        """
        self._InstanceName = None
        self._BandWidth = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceType = None
        self._MsgRetentionTime = None
        self._ClusterId = None
        self._KafkaVersion = None
        self._SpecificationsType = None
        self._DiskType = None
        self._DiskSize = None
        self._Partition = None
        self._TopicNum = None
        self._ZoneId = None
        self._MultiZoneFlag = None
        self._ZoneIds = None
        self._InstanceNum = None
        self._PublicNetworkMonthly = None

    @property
    def InstanceName(self):
        """Instance name, which is a string of up to 64 characters. It can contain letters, digits, and hyphens (-) and must start with a letter.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def BandWidth(self):
        """Private network peak bandwidth of an instance  in MB/sec.  If you create a Standard Edition instance, pass in the corresponding peak bandwidth for the current instance specification.  If you create a Pro Edition instance, configure the peak bandwidth, partition count, and other parameters as required by Pro Edition.
        :rtype: int
        """
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def VpcId(self):
        """ID of the VPC where the default access point of the created instance resides.  This parameter is required as instances cannot be created in the classic network currently.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """ID of the subnet  where the default access point of the created instance resides. 
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceType(self):
        """Instance specification.  This parameter is required for a Standard Edition instance but not for a Pro Edition instance.  Valid values:  `1` (Small),  `2` (Standard),  `3` (Advanced),  `4` (Large),  `5` (Xlarge L1),  `6` (Xlarge L2),  `7` (Xlarge L3),  `8` (Xlarge L4),  
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MsgRetentionTime(self):
        """The maximum instance log retention period in minutes by default.  If this parameter is left empty, the default retention period is 1,440 minutes (1 day) to 30 days.  If the message retention period of the topic is explicitly set, it will prevail.
        :rtype: int
        """
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def ClusterId(self):
        """Cluster ID, which can be selected when you create an instance.  You don’t need to pass in this parameter if the cluster where the instance resides is not specified.
        :rtype: int
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def KafkaVersion(self):
        """Instance version.  Valid values: `0.10.2`, `1.1.1`, `2.4.2`, and `2.8.1`.
        :rtype: str
        """
        return self._KafkaVersion

    @KafkaVersion.setter
    def KafkaVersion(self, KafkaVersion):
        self._KafkaVersion = KafkaVersion

    @property
    def SpecificationsType(self):
        """Instance type. Valid values: `standard` (Standard Edition),  `profession`  (Pro Edition)
        :rtype: str
        """
        return self._SpecificationsType

    @SpecificationsType.setter
    def SpecificationsType(self, SpecificationsType):
        self._SpecificationsType = SpecificationsType

    @property
    def DiskType(self):
        """Instance disk type. Valid values:  `CLOUD_BASIC` (Premium Cloud Storage),  `CLOUD_SSD` (SSD).  If this parameter is left empty, the default value `CLOUD_BASIC` will be used.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """Instance disk size, which must meet the requirement of the instance’s specification.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Partition(self):
        """The maximum number of partitions of the instance, which must meet the requirement of the instance’s specification.
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def TopicNum(self):
        """The maximum number of topics of the instance, which must meet the requirement of the instance’s specification.
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def ZoneId(self):
        """AZ of the instance.  When a multi-AZ instance is created, the value of this parameter is the AZ ID of the subnet where the instance’s default access point resides.
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def MultiZoneFlag(self):
        """Whether the current instance is a multi-AZ instance
        :rtype: bool
        """
        return self._MultiZoneFlag

    @MultiZoneFlag.setter
    def MultiZoneFlag(self, MultiZoneFlag):
        self._MultiZoneFlag = MultiZoneFlag

    @property
    def ZoneIds(self):
        """This parameter indicates the list of AZ IDs when the instance is deployed in multiple AZs.  Note that `ZoneId` must be included in the array of this parameter.
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def InstanceNum(self):
        """The number of purchased instances.  Default value: `1`. This parameter is optional.  If it is passed in, multiple instances will be created, with their names being `instanceName` plus different suffixes.
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def PublicNetworkMonthly(self):
        """Public network bandwidth in Mbps.  The 3 Mbps of free bandwidth is not included here by default.  For example, if you need 3 Mbps of public network bandwidth, pass in `0`; if you need 6 Mbps, pass in `3`. The value must be an integer multiple of 3.
        :rtype: int
        """
        return self._PublicNetworkMonthly

    @PublicNetworkMonthly.setter
    def PublicNetworkMonthly(self, PublicNetworkMonthly):
        self._PublicNetworkMonthly = PublicNetworkMonthly


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._BandWidth = params.get("BandWidth")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceType = params.get("InstanceType")
        self._MsgRetentionTime = params.get("MsgRetentionTime")
        self._ClusterId = params.get("ClusterId")
        self._KafkaVersion = params.get("KafkaVersion")
        self._SpecificationsType = params.get("SpecificationsType")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._Partition = params.get("Partition")
        self._TopicNum = params.get("TopicNum")
        self._ZoneId = params.get("ZoneId")
        self._MultiZoneFlag = params.get("MultiZoneFlag")
        self._ZoneIds = params.get("ZoneIds")
        self._InstanceNum = params.get("InstanceNum")
        self._PublicNetworkMonthly = params.get("PublicNetworkMonthly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancePostResp(AbstractModel):
    """Data structure returned by pay-as-you-go instance APIs

    """

    def __init__(self):
        r"""
        :param _ReturnCode: Returned code. `0` indicates normal status while other codes indicate errors.
        :type ReturnCode: str
        :param _ReturnMessage: Message returned by the API. An error message will be returned if the API reports an error. 
        :type ReturnMessage: str
        :param _Data: Returned data.  Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePostData`
        """
        self._ReturnCode = None
        self._ReturnMessage = None
        self._Data = None

    @property
    def ReturnCode(self):
        """Returned code. `0` indicates normal status while other codes indicate errors.
        :rtype: str
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMessage(self):
        """Message returned by the API. An error message will be returned if the API reports an error. 
        :rtype: str
        """
        return self._ReturnMessage

    @ReturnMessage.setter
    def ReturnMessage(self, ReturnMessage):
        self._ReturnMessage = ReturnMessage

    @property
    def Data(self):
        """Returned data.  Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePostData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMessage = params.get("ReturnMessage")
        if params.get("Data") is not None:
            self._Data = CreateInstancePostData()
            self._Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancePostResponse(AbstractModel):
    """CreateInstancePost response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateInstancePreData(AbstractModel):
    """Data returned by the `CreateInstancePre` API.

    """

    def __init__(self):
        r"""
        :param _FlowId: The value returned by `CreateInstancePre` is 0, which is fixed and cannot be used as the query condition of `CheckTaskStatus`. It is only used to ensure the consistency with the backend data structure.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type FlowId: int
        :param _DealNames: Order number list.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DealNames: list of str
        :param _InstanceId: Instance ID. When multiple instances are purchased, the ID of the first one is returned by default . Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _DealNameInstanceIdMapping: Mapping between orders and the purchased instances.  Note: This field may return null, indicating that no valid values can be obtained.
        :type DealNameInstanceIdMapping: list of DealInstanceDTO
        """
        self._FlowId = None
        self._DealNames = None
        self._InstanceId = None
        self._DealNameInstanceIdMapping = None

    @property
    def FlowId(self):
        """The value returned by `CreateInstancePre` is 0, which is fixed and cannot be used as the query condition of `CheckTaskStatus`. It is only used to ensure the consistency with the backend data structure.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DealNames(self):
        """Order number list.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def InstanceId(self):
        """Instance ID. When multiple instances are purchased, the ID of the first one is returned by default . Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealNameInstanceIdMapping(self):
        """Mapping between orders and the purchased instances.  Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DealInstanceDTO
        """
        return self._DealNameInstanceIdMapping

    @DealNameInstanceIdMapping.setter
    def DealNameInstanceIdMapping(self, DealNameInstanceIdMapping):
        self._DealNameInstanceIdMapping = DealNameInstanceIdMapping


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._DealNames = params.get("DealNames")
        self._InstanceId = params.get("InstanceId")
        if params.get("DealNameInstanceIdMapping") is not None:
            self._DealNameInstanceIdMapping = []
            for item in params.get("DealNameInstanceIdMapping"):
                obj = DealInstanceDTO()
                obj._deserialize(item)
                self._DealNameInstanceIdMapping.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancePreResp(AbstractModel):
    """Data structure returned by monthly subscribed instance APIs

    """

    def __init__(self):
        r"""
        :param _ReturnCode: Returned code. 0: Normal; other values: Error.
        :type ReturnCode: str
        :param _ReturnMessage: The message indicating whether the operation is successful.
        :type ReturnMessage: str
        :param _Data: Data returned by the operation.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreData`
        :param _DeleteRouteTimestamp: Deletion time.  This parameter has been deprecated and will be deleted.  Note: This field may return null, indicating that no valid values can be obtained.
        :type DeleteRouteTimestamp: str
        """
        self._ReturnCode = None
        self._ReturnMessage = None
        self._Data = None
        self._DeleteRouteTimestamp = None

    @property
    def ReturnCode(self):
        """Returned code. 0: Normal; other values: Error.
        :rtype: str
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMessage(self):
        """The message indicating whether the operation is successful.
        :rtype: str
        """
        return self._ReturnMessage

    @ReturnMessage.setter
    def ReturnMessage(self, ReturnMessage):
        self._ReturnMessage = ReturnMessage

    @property
    def Data(self):
        """Data returned by the operation.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def DeleteRouteTimestamp(self):
        warnings.warn("parameter `DeleteRouteTimestamp` is deprecated", DeprecationWarning) 

        """Deletion time.  This parameter has been deprecated and will be deleted.  Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DeleteRouteTimestamp

    @DeleteRouteTimestamp.setter
    def DeleteRouteTimestamp(self, DeleteRouteTimestamp):
        warnings.warn("parameter `DeleteRouteTimestamp` is deprecated", DeprecationWarning) 

        self._DeleteRouteTimestamp = DeleteRouteTimestamp


    def _deserialize(self, params):
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMessage = params.get("ReturnMessage")
        if params.get("Data") is not None:
            self._Data = CreateInstancePreData()
            self._Data._deserialize(params.get("Data"))
        self._DeleteRouteTimestamp = params.get("DeleteRouteTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePartitionRequest(AbstractModel):
    """CreatePartition request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _TopicName: Topic name
        :type TopicName: str
        :param _PartitionNum: Number of topic partitions
        :type PartitionNum: int
        """
        self._InstanceId = None
        self._TopicName = None
        self._PartitionNum = None

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
    def TopicName(self):
        """Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionNum(self):
        """Number of topic partitions
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._PartitionNum = params.get("PartitionNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePartitionResponse(AbstractModel):
    """CreatePartition response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result set
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result set
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreatePostPaidInstanceRequest(AbstractModel):
    """CreatePostPaidInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceName: Instance name, which is a string of up to 64 letters, digits, and hyphens (-). It must start with a letter.
        :type InstanceName: str
        :param _VpcId: ID of the VPC where the default access point of the created instance resides.  This parameter is required as instances cannot be created in the classic network currently.
        :type VpcId: str
        :param _SubnetId: ID of the subnet  where the default access point of the created instance resides.
        :type SubnetId: str
        :param _InstanceType: Instance specification.  This parameter is required for a Standard Edition instance but not for a Pro Edition instance.  Valid values:  `1` (Small),  `2` (Standard),  `3` (Advanced),  `4` (Large),  `5` (Xlarge L1),  `6` (Xlarge L2),  `7` (Xlarge L3),  `8` (Xlarge L4),  
        :type InstanceType: int
        :param _MsgRetentionTime: The maximum instance log retention period in minutes by default.  If this parameter is left empty, the default retention period is 1,440 minutes (1 day) to 30 days.  If the message retention period of the topic is explicitly set, it will prevail.
        :type MsgRetentionTime: int
        :param _ClusterId: Cluster ID, which can be selected when you create an instance.  You don’t need to pass in this parameter if the cluster where the instance resides is not specified.
        :type ClusterId: int
        :param _KafkaVersion: Instance version.  Valid values: `0.10.2`, `1.1.1`, `2.4.2`, and `2.8.1`.
        :type KafkaVersion: str
        :param _SpecificationsType: Instance type. `standard` (Standard Edition),  `profession`  (Pro Edition)
        :type SpecificationsType: str
        :param _DiskType: Instance disk type.  `CLOUD_BASIC` (Premium Cloud Storage),  `CLOUD_SSD` (SSD).  If this parameter is left empty, the default value `CLOUD_BASIC` will be used.
        :type DiskType: str
        :param _BandWidth: Private network peak bandwidth of an instance  in MB/sec.  If you create a Standard Edition instance, pass in the corresponding peak bandwidth for the current instance specification.  If you create a Pro Edition instance, configure the peak bandwidth, partition count, and other parameters as required by Pro Edition.
        :type BandWidth: int
        :param _DiskSize: Instance disk size, which must meet the requirement of the instance’s specification.
        :type DiskSize: int
        :param _Partition: The maximum number of partitions of the instance, which must meet the requirement of the instance’s specification.
        :type Partition: int
        :param _TopicNum: The maximum number of topics of the instance, which must meet the requirement of the instance’s specification.
        :type TopicNum: int
        :param _ZoneId: AZ of the instance.  When a multi-AZ instance is created, the value of this parameter is the AZ ID of the subnet where the instance’s default access point resides.
        :type ZoneId: int
        :param _MultiZoneFlag: Whether the current instance is a multi-AZ instance
        :type MultiZoneFlag: bool
        :param _ZoneIds: This parameter indicates the list of AZ IDs when the instance is deployed in multiple AZs.  Note that `ZoneId` must be included in the array of this parameter.
        :type ZoneIds: list of int
        :param _InstanceNum: The number of purchased instances.  Default value: `1`. This parameter is optional.  If it is passed in, multiple instances will be created, with their names being `instanceName` plus different suffixes.
        :type InstanceNum: int
        :param _PublicNetworkMonthly: Public network bandwidth in Mbps.  The 3 Mbps of free bandwidth is not included here by default.  For example, if you need 3 Mbps of public network bandwidth, pass in `0`; if you need 6 Mbps, pass in `3`.  The value must be an integer multiple of 3.
        :type PublicNetworkMonthly: int
        """
        self._InstanceName = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceType = None
        self._MsgRetentionTime = None
        self._ClusterId = None
        self._KafkaVersion = None
        self._SpecificationsType = None
        self._DiskType = None
        self._BandWidth = None
        self._DiskSize = None
        self._Partition = None
        self._TopicNum = None
        self._ZoneId = None
        self._MultiZoneFlag = None
        self._ZoneIds = None
        self._InstanceNum = None
        self._PublicNetworkMonthly = None

    @property
    def InstanceName(self):
        """Instance name, which is a string of up to 64 letters, digits, and hyphens (-). It must start with a letter.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def VpcId(self):
        """ID of the VPC where the default access point of the created instance resides.  This parameter is required as instances cannot be created in the classic network currently.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """ID of the subnet  where the default access point of the created instance resides.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceType(self):
        """Instance specification.  This parameter is required for a Standard Edition instance but not for a Pro Edition instance.  Valid values:  `1` (Small),  `2` (Standard),  `3` (Advanced),  `4` (Large),  `5` (Xlarge L1),  `6` (Xlarge L2),  `7` (Xlarge L3),  `8` (Xlarge L4),  
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MsgRetentionTime(self):
        """The maximum instance log retention period in minutes by default.  If this parameter is left empty, the default retention period is 1,440 minutes (1 day) to 30 days.  If the message retention period of the topic is explicitly set, it will prevail.
        :rtype: int
        """
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def ClusterId(self):
        """Cluster ID, which can be selected when you create an instance.  You don’t need to pass in this parameter if the cluster where the instance resides is not specified.
        :rtype: int
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def KafkaVersion(self):
        """Instance version.  Valid values: `0.10.2`, `1.1.1`, `2.4.2`, and `2.8.1`.
        :rtype: str
        """
        return self._KafkaVersion

    @KafkaVersion.setter
    def KafkaVersion(self, KafkaVersion):
        self._KafkaVersion = KafkaVersion

    @property
    def SpecificationsType(self):
        """Instance type. `standard` (Standard Edition),  `profession`  (Pro Edition)
        :rtype: str
        """
        return self._SpecificationsType

    @SpecificationsType.setter
    def SpecificationsType(self, SpecificationsType):
        self._SpecificationsType = SpecificationsType

    @property
    def DiskType(self):
        """Instance disk type.  `CLOUD_BASIC` (Premium Cloud Storage),  `CLOUD_SSD` (SSD).  If this parameter is left empty, the default value `CLOUD_BASIC` will be used.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def BandWidth(self):
        """Private network peak bandwidth of an instance  in MB/sec.  If you create a Standard Edition instance, pass in the corresponding peak bandwidth for the current instance specification.  If you create a Pro Edition instance, configure the peak bandwidth, partition count, and other parameters as required by Pro Edition.
        :rtype: int
        """
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def DiskSize(self):
        """Instance disk size, which must meet the requirement of the instance’s specification.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Partition(self):
        """The maximum number of partitions of the instance, which must meet the requirement of the instance’s specification.
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def TopicNum(self):
        """The maximum number of topics of the instance, which must meet the requirement of the instance’s specification.
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def ZoneId(self):
        """AZ of the instance.  When a multi-AZ instance is created, the value of this parameter is the AZ ID of the subnet where the instance’s default access point resides.
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def MultiZoneFlag(self):
        """Whether the current instance is a multi-AZ instance
        :rtype: bool
        """
        return self._MultiZoneFlag

    @MultiZoneFlag.setter
    def MultiZoneFlag(self, MultiZoneFlag):
        self._MultiZoneFlag = MultiZoneFlag

    @property
    def ZoneIds(self):
        """This parameter indicates the list of AZ IDs when the instance is deployed in multiple AZs.  Note that `ZoneId` must be included in the array of this parameter.
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def InstanceNum(self):
        """The number of purchased instances.  Default value: `1`. This parameter is optional.  If it is passed in, multiple instances will be created, with their names being `instanceName` plus different suffixes.
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def PublicNetworkMonthly(self):
        """Public network bandwidth in Mbps.  The 3 Mbps of free bandwidth is not included here by default.  For example, if you need 3 Mbps of public network bandwidth, pass in `0`; if you need 6 Mbps, pass in `3`.  The value must be an integer multiple of 3.
        :rtype: int
        """
        return self._PublicNetworkMonthly

    @PublicNetworkMonthly.setter
    def PublicNetworkMonthly(self, PublicNetworkMonthly):
        self._PublicNetworkMonthly = PublicNetworkMonthly


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceType = params.get("InstanceType")
        self._MsgRetentionTime = params.get("MsgRetentionTime")
        self._ClusterId = params.get("ClusterId")
        self._KafkaVersion = params.get("KafkaVersion")
        self._SpecificationsType = params.get("SpecificationsType")
        self._DiskType = params.get("DiskType")
        self._BandWidth = params.get("BandWidth")
        self._DiskSize = params.get("DiskSize")
        self._Partition = params.get("Partition")
        self._TopicNum = params.get("TopicNum")
        self._ZoneId = params.get("ZoneId")
        self._MultiZoneFlag = params.get("MultiZoneFlag")
        self._ZoneIds = params.get("ZoneIds")
        self._InstanceNum = params.get("InstanceNum")
        self._PublicNetworkMonthly = params.get("PublicNetworkMonthly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePostPaidInstanceResponse(AbstractModel):
    """CreatePostPaidInstance response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePostResp`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePostResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CreateInstancePostResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateTopicIpWhiteListRequest(AbstractModel):
    """CreateTopicIpWhiteList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _TopicName: Topic name
        :type TopicName: str
        :param _IpWhiteList: IP allowlist list
        :type IpWhiteList: list of str
        """
        self._InstanceId = None
        self._TopicName = None
        self._IpWhiteList = None

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
    def TopicName(self):
        """Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def IpWhiteList(self):
        """IP allowlist list
        :rtype: list of str
        """
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._IpWhiteList = params.get("IpWhiteList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicIpWhiteListResponse(AbstractModel):
    """CreateTopicIpWhiteList response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Result of deleting topic IP allowlist
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Result of deleting topic IP allowlist
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _TopicName: Topic name, which is a string of up to 128 characters. It can contain letters, digits, and hyphens (-) and must start with a letter.
        :type TopicName: str
        :param _PartitionNum: Number of partitions, which should be greater than 0
        :type PartitionNum: int
        :param _ReplicaNum: Number of replicas, which cannot be higher than the number of brokers. Maximum value: 3
        :type ReplicaNum: int
        :param _EnableWhiteList: IP allowlist switch. 1: enabled, 0: disabled. Default value: 0
        :type EnableWhiteList: int
        :param _IpWhiteList: IP allowlist list for quota limit, which is required if `enableWhileList` is 1
        :type IpWhiteList: list of str
        :param _CleanUpPolicy: Log cleanup policy, which is `delete` by default. `delete`: logs will be deleted by save time; `compact`: logs will be compressed by key; `compact, delete`: logs will be compressed by key and deleted by save time.
        :type CleanUpPolicy: str
        :param _Note: Topic remarks string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)
        :type Note: str
        :param _MinInsyncReplicas: Default value: 1
        :type MinInsyncReplicas: int
        :param _UncleanLeaderElectionEnable: Whether to allow an unsynced replica to be elected as leader. false: no, true: yes. Default value: false
        :type UncleanLeaderElectionEnable: int
        :param _RetentionMs: Message retention period in milliseconds, which is optional. Min value: 60,000 ms.
        :type RetentionMs: int
        :param _SegmentMs: Segment rolling duration in ms. The current minimum value is 3,600,000 ms
        :type SegmentMs: int
        :param _MaxMessageBytes: Max message size in bytes. Value range: 1,024 bytes (1 KB) to 8,388,608 bytes (8 MB).
        :type MaxMessageBytes: int
        :param _EnableAclRule: Preset ACL rule. `1`: enable, `0`: disable. Default value: `0`.
        :type EnableAclRule: int
        :param _AclRuleName: Name of the preset ACL rule.
        :type AclRuleName: str
        :param _RetentionBytes: Message retention file size in bytes, which is an optional parameter. Default value: -1. Currently, the min value that can be entered is 1,048,576 B.
        :type RetentionBytes: int
        :param _Tags: Tag list.
        :type Tags: list of Tag
        """
        self._InstanceId = None
        self._TopicName = None
        self._PartitionNum = None
        self._ReplicaNum = None
        self._EnableWhiteList = None
        self._IpWhiteList = None
        self._CleanUpPolicy = None
        self._Note = None
        self._MinInsyncReplicas = None
        self._UncleanLeaderElectionEnable = None
        self._RetentionMs = None
        self._SegmentMs = None
        self._MaxMessageBytes = None
        self._EnableAclRule = None
        self._AclRuleName = None
        self._RetentionBytes = None
        self._Tags = None

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
    def TopicName(self):
        """Topic name, which is a string of up to 128 characters. It can contain letters, digits, and hyphens (-) and must start with a letter.
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionNum(self):
        """Number of partitions, which should be greater than 0
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def ReplicaNum(self):
        """Number of replicas, which cannot be higher than the number of brokers. Maximum value: 3
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def EnableWhiteList(self):
        """IP allowlist switch. 1: enabled, 0: disabled. Default value: 0
        :rtype: int
        """
        return self._EnableWhiteList

    @EnableWhiteList.setter
    def EnableWhiteList(self, EnableWhiteList):
        self._EnableWhiteList = EnableWhiteList

    @property
    def IpWhiteList(self):
        """IP allowlist list for quota limit, which is required if `enableWhileList` is 1
        :rtype: list of str
        """
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList

    @property
    def CleanUpPolicy(self):
        """Log cleanup policy, which is `delete` by default. `delete`: logs will be deleted by save time; `compact`: logs will be compressed by key; `compact, delete`: logs will be compressed by key and deleted by save time.
        :rtype: str
        """
        return self._CleanUpPolicy

    @CleanUpPolicy.setter
    def CleanUpPolicy(self, CleanUpPolicy):
        self._CleanUpPolicy = CleanUpPolicy

    @property
    def Note(self):
        """Topic remarks string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def MinInsyncReplicas(self):
        """Default value: 1
        :rtype: int
        """
        return self._MinInsyncReplicas

    @MinInsyncReplicas.setter
    def MinInsyncReplicas(self, MinInsyncReplicas):
        self._MinInsyncReplicas = MinInsyncReplicas

    @property
    def UncleanLeaderElectionEnable(self):
        """Whether to allow an unsynced replica to be elected as leader. false: no, true: yes. Default value: false
        :rtype: int
        """
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def RetentionMs(self):
        """Message retention period in milliseconds, which is optional. Min value: 60,000 ms.
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def SegmentMs(self):
        """Segment rolling duration in ms. The current minimum value is 3,600,000 ms
        :rtype: int
        """
        return self._SegmentMs

    @SegmentMs.setter
    def SegmentMs(self, SegmentMs):
        self._SegmentMs = SegmentMs

    @property
    def MaxMessageBytes(self):
        """Max message size in bytes. Value range: 1,024 bytes (1 KB) to 8,388,608 bytes (8 MB).
        :rtype: int
        """
        return self._MaxMessageBytes

    @MaxMessageBytes.setter
    def MaxMessageBytes(self, MaxMessageBytes):
        self._MaxMessageBytes = MaxMessageBytes

    @property
    def EnableAclRule(self):
        """Preset ACL rule. `1`: enable, `0`: disable. Default value: `0`.
        :rtype: int
        """
        return self._EnableAclRule

    @EnableAclRule.setter
    def EnableAclRule(self, EnableAclRule):
        self._EnableAclRule = EnableAclRule

    @property
    def AclRuleName(self):
        """Name of the preset ACL rule.
        :rtype: str
        """
        return self._AclRuleName

    @AclRuleName.setter
    def AclRuleName(self, AclRuleName):
        self._AclRuleName = AclRuleName

    @property
    def RetentionBytes(self):
        """Message retention file size in bytes, which is an optional parameter. Default value: -1. Currently, the min value that can be entered is 1,048,576 B.
        :rtype: int
        """
        return self._RetentionBytes

    @RetentionBytes.setter
    def RetentionBytes(self, RetentionBytes):
        self._RetentionBytes = RetentionBytes

    @property
    def Tags(self):
        """Tag list.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._PartitionNum = params.get("PartitionNum")
        self._ReplicaNum = params.get("ReplicaNum")
        self._EnableWhiteList = params.get("EnableWhiteList")
        self._IpWhiteList = params.get("IpWhiteList")
        self._CleanUpPolicy = params.get("CleanUpPolicy")
        self._Note = params.get("Note")
        self._MinInsyncReplicas = params.get("MinInsyncReplicas")
        self._UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self._RetentionMs = params.get("RetentionMs")
        self._SegmentMs = params.get("SegmentMs")
        self._MaxMessageBytes = params.get("MaxMessageBytes")
        self._EnableAclRule = params.get("EnableAclRule")
        self._AclRuleName = params.get("AclRuleName")
        self._RetentionBytes = params.get("RetentionBytes")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResp(AbstractModel):
    """Return for topic creation

    """

    def __init__(self):
        r"""
        :param _TopicId: Topic ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        """Topic ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned creation result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicResp`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned creation result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CreateTopicResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Name: Username
        :type Name: str
        :param _Password: User password
        :type Password: str
        """
        self._InstanceId = None
        self._Name = None
        self._Password = None

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
    def Name(self):
        """Username
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Password(self):
        """User password
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    """CreateUser response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DatahubTopicDTO(AbstractModel):
    """DataHub topic

    """

    def __init__(self):
        r"""
        :param _Name: Name
        :type Name: str
        :param _TopicName: Topic name
        :type TopicName: str
        :param _TopicId: Topic ID
        :type TopicId: str
        :param _PartitionNum: The number of partitions
        :type PartitionNum: int
        :param _RetentionMs: Expiration time
        :type RetentionMs: int
        :param _Note: Remarks
        :type Note: str
        :param _Status: Status (`1`: In use; `2`: Deleting)
        :type Status: int
        """
        self._Name = None
        self._TopicName = None
        self._TopicId = None
        self._PartitionNum = None
        self._RetentionMs = None
        self._Note = None
        self._Status = None

    @property
    def Name(self):
        """Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TopicName(self):
        """Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        """Topic ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionNum(self):
        """The number of partitions
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def RetentionMs(self):
        """Expiration time
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def Note(self):
        """Remarks
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Status(self):
        """Status (`1`: In use; `2`: Deleting)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TopicName = params.get("TopicName")
        self._TopicId = params.get("TopicId")
        self._PartitionNum = params.get("PartitionNum")
        self._RetentionMs = params.get("RetentionMs")
        self._Note = params.get("Note")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatahubTopicResp(AbstractModel):
    """DataHub topic response

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name
        :type TopicName: str
        :param _TopicId: TopicId
Note: This field may return null, indicating that no valid values can be obtained.
        :type TopicId: str
        """
        self._TopicName = None
        self._TopicId = None

    @property
    def TopicName(self):
        """Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        """TopicId
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DealInstanceDTO(AbstractModel):
    """Mapping between orders and CKafka instances for monthly subscribed and pay-as-you-go instance APIs.

    """

    def __init__(self):
        r"""
        :param _DealName: Order list.  Note: This field may return null, indicating that no valid values can be obtained.
        :type DealName: str
        :param _InstanceIdList: ID list of the purchased CKafka instances corresponding to the order list.  Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceIdList: list of str
        """
        self._DealName = None
        self._InstanceIdList = None

    @property
    def DealName(self):
        """Order list.  Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def InstanceIdList(self):
        """ID list of the purchased CKafka instances corresponding to the order list.  Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._InstanceIdList = params.get("InstanceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAclRequest(AbstractModel):
    """DeleteAcl request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID information
        :type InstanceId: str
        :param _ResourceType: ACL resource type (`2`: TOPIC, `3`: GROUP, `4`: CLUSTER).
        :type ResourceType: int
        :param _ResourceName: Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name; if `resourceType` is `CLUSTER`, this field can be left empty.
        :type ResourceName: str
        :param _Operation: ACL operation type (`2`: ALL, `3`: READ, `4`: WRITE, `5`: CREATE, `6`: DELETE, `7`: ALTER, `8`: DESCRIBE, `9`: CLUSTER_ACTION, `10`: DESCRIBE_CONFIGS, `11`: ALTER_CONFIGS, `12`: IDEMPOTENT_WRITE).
        :type Operation: int
        :param _PermissionType: Permission type (`2`: DENY, `3`: ALLOW). CKafka currently supports `ALLOW`, which is equivalent to allowlist. `DENY` will be supported for ACLs compatible with open-source Kafka.
        :type PermissionType: int
        :param _Host: The default value is `*`, which means that any host can access. Currently, CKafka does not support the host as `*`, but the future product based on the open-source Kafka will directly support this
        :type Host: str
        :param _Principal: User list. The default value is `*`, which means that any user can access. The current user can only be one included in the user list
        :type Principal: str
        """
        self._InstanceId = None
        self._ResourceType = None
        self._ResourceName = None
        self._Operation = None
        self._PermissionType = None
        self._Host = None
        self._Principal = None

    @property
    def InstanceId(self):
        """Instance ID information
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceType(self):
        """ACL resource type (`2`: TOPIC, `3`: GROUP, `4`: CLUSTER).
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        """Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name; if `resourceType` is `CLUSTER`, this field can be left empty.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Operation(self):
        """ACL operation type (`2`: ALL, `3`: READ, `4`: WRITE, `5`: CREATE, `6`: DELETE, `7`: ALTER, `8`: DESCRIBE, `9`: CLUSTER_ACTION, `10`: DESCRIBE_CONFIGS, `11`: ALTER_CONFIGS, `12`: IDEMPOTENT_WRITE).
        :rtype: int
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PermissionType(self):
        """Permission type (`2`: DENY, `3`: ALLOW). CKafka currently supports `ALLOW`, which is equivalent to allowlist. `DENY` will be supported for ACLs compatible with open-source Kafka.
        :rtype: int
        """
        return self._PermissionType

    @PermissionType.setter
    def PermissionType(self, PermissionType):
        self._PermissionType = PermissionType

    @property
    def Host(self):
        """The default value is `*`, which means that any host can access. Currently, CKafka does not support the host as `*`, but the future product based on the open-source Kafka will directly support this
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Principal(self):
        """User list. The default value is `*`, which means that any user can access. The current user can only be one included in the user list
        :rtype: str
        """
        return self._Principal

    @Principal.setter
    def Principal(self, Principal):
        self._Principal = Principal


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceName = params.get("ResourceName")
        self._Operation = params.get("Operation")
        self._PermissionType = params.get("PermissionType")
        self._Host = params.get("Host")
        self._Principal = params.get("Principal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAclResponse(AbstractModel):
    """DeleteAcl response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteInstancePreRequest(AbstractModel):
    """DeleteInstancePre request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstancePreResponse(AbstractModel):
    """DeleteInstancePre response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CreateInstancePreResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteRouteRequest(AbstractModel):
    """DeleteRoute request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Unique instance ID.
        :type InstanceId: str
        :param _RouteId: Route ID.
        :type RouteId: int
        :param _CallerAppid: AppId of the caller.
        :type CallerAppid: int
        :param _DeleteRouteTime: The time when a route was deleted.
        :type DeleteRouteTime: str
        """
        self._InstanceId = None
        self._RouteId = None
        self._CallerAppid = None
        self._DeleteRouteTime = None

    @property
    def InstanceId(self):
        """Unique instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RouteId(self):
        """Route ID.
        :rtype: int
        """
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId

    @property
    def CallerAppid(self):
        """AppId of the caller.
        :rtype: int
        """
        return self._CallerAppid

    @CallerAppid.setter
    def CallerAppid(self, CallerAppid):
        self._CallerAppid = CallerAppid

    @property
    def DeleteRouteTime(self):
        """The time when a route was deleted.
        :rtype: str
        """
        return self._DeleteRouteTime

    @DeleteRouteTime.setter
    def DeleteRouteTime(self, DeleteRouteTime):
        self._DeleteRouteTime = DeleteRouteTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RouteId = params.get("RouteId")
        self._CallerAppid = params.get("CallerAppid")
        self._DeleteRouteTime = params.get("DeleteRouteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRouteResponse(AbstractModel):
    """DeleteRoute response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteRouteTriggerTimeRequest(AbstractModel):
    """DeleteRouteTriggerTime request structure.

    """

    def __init__(self):
        r"""
        :param _DelayTime: Modification time.
        :type DelayTime: str
        """
        self._DelayTime = None

    @property
    def DelayTime(self):
        """Modification time.
        :rtype: str
        """
        return self._DelayTime

    @DelayTime.setter
    def DelayTime(self, DelayTime):
        self._DelayTime = DelayTime


    def _deserialize(self, params):
        self._DelayTime = params.get("DelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRouteTriggerTimeResponse(AbstractModel):
    """DeleteRouteTriggerTime response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTopicIpWhiteListRequest(AbstractModel):
    """DeleteTopicIpWhiteList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _TopicName: Topic name
        :type TopicName: str
        :param _IpWhiteList: IP allowlist list
        :type IpWhiteList: list of str
        """
        self._InstanceId = None
        self._TopicName = None
        self._IpWhiteList = None

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
    def TopicName(self):
        """Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def IpWhiteList(self):
        """IP allowlist list
        :rtype: list of str
        """
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._IpWhiteList = params.get("IpWhiteList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicIpWhiteListResponse(AbstractModel):
    """DeleteTopicIpWhiteList response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Result of deleting topic IP allowlist
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Result of deleting topic IP allowlist
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: CKafka instance ID
        :type InstanceId: str
        :param _TopicName: CKafka topic name
        :type TopicName: str
        """
        self._InstanceId = None
        self._TopicName = None

    @property
    def InstanceId(self):
        """CKafka instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        """CKafka topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result set
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result set
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    """DeleteUser request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Name: Username
        :type Name: str
        """
        self._InstanceId = None
        self._Name = None

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
    def Name(self):
        """Username
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    """DeleteUser response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeACLRequest(AbstractModel):
    """DescribeACL request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ResourceType: ACL resource type (`2`: TOPIC, `3`: GROUP, `4`: CLUSTER).
        :type ResourceType: int
        :param _ResourceName: Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name; if `resourceType` is `CLUSTER`, this field can be left empty.
        :type ResourceName: str
        :param _Offset: Offset position
        :type Offset: int
        :param _Limit: Quantity limit
        :type Limit: int
        :param _SearchWord: Keyword match
        :type SearchWord: str
        """
        self._InstanceId = None
        self._ResourceType = None
        self._ResourceName = None
        self._Offset = None
        self._Limit = None
        self._SearchWord = None

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
    def ResourceType(self):
        """ACL resource type (`2`: TOPIC, `3`: GROUP, `4`: CLUSTER).
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        """Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name; if `resourceType` is `CLUSTER`, this field can be left empty.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Offset(self):
        """Offset position
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Quantity limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchWord(self):
        """Keyword match
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceName = params.get("ResourceName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchWord = params.get("SearchWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeACLResponse(AbstractModel):
    """DescribeACL response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned ACL result set object
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AclResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned ACL result set object
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.AclResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = AclResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeAclRuleRequest(AbstractModel):
    """DescribeAclRule request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _RuleName: ACL rule name
        :type RuleName: str
        :param _PatternType: ACL rule matching type
        :type PatternType: str
        :param _IsSimplified: Whether to read simplified ACL rules
        :type IsSimplified: bool
        """
        self._InstanceId = None
        self._RuleName = None
        self._PatternType = None
        self._IsSimplified = None

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
    def RuleName(self):
        """ACL rule name
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def PatternType(self):
        """ACL rule matching type
        :rtype: str
        """
        return self._PatternType

    @PatternType.setter
    def PatternType(self, PatternType):
        self._PatternType = PatternType

    @property
    def IsSimplified(self):
        """Whether to read simplified ACL rules
        :rtype: bool
        """
        return self._IsSimplified

    @IsSimplified.setter
    def IsSimplified(self, IsSimplified):
        self._IsSimplified = IsSimplified


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RuleName = params.get("RuleName")
        self._PatternType = params.get("PatternType")
        self._IsSimplified = params.get("IsSimplified")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAclRuleResponse(AbstractModel):
    """DescribeAclRule response structure.

    """

    def __init__(self):
        r"""
        :param _Result: The set of returned ACL rules
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AclRuleResp`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """The set of returned ACL rules
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.AclRuleResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = AclRuleResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeAppInfoRequest(AbstractModel):
    """DescribeAppInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset position
        :type Offset: int
        :param _Limit: Maximum number of users to be queried in this request. Maximum value: 50. Default value: 50
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        """Offset position
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Maximum number of users to be queried in this request. Maximum value: 50. Default value: 50
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppInfoResponse(AbstractModel):
    """DescribeAppInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned list of eligible `AppId`
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AppIdResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned list of eligible `AppId`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.AppIdResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = AppIdResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCkafkaZoneRequest(AbstractModel):
    """DescribeCkafkaZone request structure.

    """

    def __init__(self):
        r"""
        :param _CdcId: Cloud Dedicated Cluster (CDC) business parameter.
        :type CdcId: str
        """
        self._CdcId = None

    @property
    def CdcId(self):
        """Cloud Dedicated Cluster (CDC) business parameter.
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId


    def _deserialize(self, params):
        self._CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCkafkaZoneResponse(AbstractModel):
    """DescribeCkafkaZone response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned results for the query
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ZoneResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned results for the query
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ZoneResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ZoneResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeConnectInfoResultDTO(AbstractModel):
    """Topic connection information

    """

    def __init__(self):
        r"""
        :param _IpAddr: IP address
Note: This field may return null, indicating that no valid values can be obtained.
        :type IpAddr: str
        :param _Time: Connection time
Note: This field may return null, indicating that no valid values can be obtained.
        :type Time: str
        :param _IsUnSupportVersion: Whether it is a supported version
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsUnSupportVersion: bool
        """
        self._IpAddr = None
        self._Time = None
        self._IsUnSupportVersion = None

    @property
    def IpAddr(self):
        """IP address
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IpAddr

    @IpAddr.setter
    def IpAddr(self, IpAddr):
        self._IpAddr = IpAddr

    @property
    def Time(self):
        """Connection time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def IsUnSupportVersion(self):
        """Whether it is a supported version
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsUnSupportVersion

    @IsUnSupportVersion.setter
    def IsUnSupportVersion(self, IsUnSupportVersion):
        self._IsUnSupportVersion = IsUnSupportVersion


    def _deserialize(self, params):
        self._IpAddr = params.get("IpAddr")
        self._Time = params.get("Time")
        self._IsUnSupportVersion = params.get("IsUnSupportVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumerGroupRequest(AbstractModel):
    """DescribeConsumerGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: CKafka instance ID.
        :type InstanceId: str
        :param _GroupName: Name of the group to be queried, which is optional.
        :type GroupName: str
        :param _TopicName: Name of the corresponding topic in the group to be queried, which is optional. If this parameter is specified but `group` is not specified, this parameter will be ignored.
        :type TopicName: str
        :param _Limit: Number of results to be returned in this request
        :type Limit: int
        :param _Offset: Offset position
        :type Offset: int
        """
        self._InstanceId = None
        self._GroupName = None
        self._TopicName = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        """CKafka instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupName(self):
        """Name of the group to be queried, which is optional.
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TopicName(self):
        """Name of the corresponding topic in the group to be queried, which is optional. If this parameter is specified but `group` is not specified, this parameter will be ignored.
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Limit(self):
        """Number of results to be returned in this request
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset position
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GroupName = params.get("GroupName")
        self._TopicName = params.get("TopicName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumerGroupResponse(AbstractModel):
    """DescribeConsumerGroup response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned consumer group information
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConsumerGroupResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned consumer group information
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ConsumerGroupResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ConsumerGroupResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDatahubTopicRequest(AbstractModel):
    """DescribeDatahubTopic request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Name
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        """Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatahubTopicResp(AbstractModel):
    """DataHub topic details

    """

    def __init__(self):
        r"""
        :param _Name: Name
        :type Name: str
        :param _TopicName: Topic name
        :type TopicName: str
        :param _TopicId: Topic ID
        :type TopicId: str
        :param _PartitionNum: The number of partitions
        :type PartitionNum: int
        :param _RetentionMs: Expiration time
        :type RetentionMs: int
        :param _Note: Remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :type Note: str
        :param _UserName: Username
        :type UserName: str
        :param _Password: Password
        :type Password: str
        :param _Status: Status (`1`: In use; `2`: Deleting)
        :type Status: int
        :param _Address: Service routing address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: str
        """
        self._Name = None
        self._TopicName = None
        self._TopicId = None
        self._PartitionNum = None
        self._RetentionMs = None
        self._Note = None
        self._UserName = None
        self._Password = None
        self._Status = None
        self._Address = None

    @property
    def Name(self):
        """Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TopicName(self):
        """Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        """Topic ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionNum(self):
        """The number of partitions
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def RetentionMs(self):
        """Expiration time
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def Note(self):
        """Remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def UserName(self):
        """Username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """Password
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Status(self):
        """Status (`1`: In use; `2`: Deleting)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Address(self):
        """Service routing address
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TopicName = params.get("TopicName")
        self._TopicId = params.get("TopicId")
        self._PartitionNum = params.get("PartitionNum")
        self._RetentionMs = params.get("RetentionMs")
        self._Note = params.get("Note")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Status = params.get("Status")
        self._Address = params.get("Address")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatahubTopicResponse(AbstractModel):
    """DescribeDatahubTopic response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result object
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicResp`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result object
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeDatahubTopicResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDatahubTopicsRequest(AbstractModel):
    """DescribeDatahubTopics request structure.

    """

    def __init__(self):
        r"""
        :param _SearchWord: Keyword for query
        :type SearchWord: str
        :param _Offset: Query offset, which defaults to `0`.
        :type Offset: int
        :param _Limit: Maximum number of results to be returned in this request. Default value: `50`. Maximum value: `50`.
        :type Limit: int
        """
        self._SearchWord = None
        self._Offset = None
        self._Limit = None

    @property
    def SearchWord(self):
        """Keyword for query
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        """Query offset, which defaults to `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Maximum number of results to be returned in this request. Default value: `50`. Maximum value: `50`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SearchWord = params.get("SearchWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatahubTopicsResp(AbstractModel):
    """DataHub topic list

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total count
        :type TotalCount: int
        :param _TopicList: Topic list
Note: This field may return null, indicating that no valid values can be obtained.
        :type TopicList: list of DatahubTopicDTO
        """
        self._TotalCount = None
        self._TopicList = None

    @property
    def TotalCount(self):
        """Total count
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TopicList(self):
        """Topic list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DatahubTopicDTO
        """
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TopicList") is not None:
            self._TopicList = []
            for item in params.get("TopicList"):
                obj = DatahubTopicDTO()
                obj._deserialize(item)
                self._TopicList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatahubTopicsResponse(AbstractModel):
    """DescribeDatahubTopics response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Topic list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicsResp`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Topic list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicsResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeDatahubTopicsResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeGroup(AbstractModel):
    """`DescribeGroup` response entity

    """

    def __init__(self):
        r"""
        :param _Group: groupId
        :type Group: str
        :param _Protocol: Protocol used by the group.
        :type Protocol: str
        """
        self._Group = None
        self._Protocol = None

    @property
    def Group(self):
        """groupId
        :rtype: str
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Protocol(self):
        """Protocol used by the group.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Group = params.get("Group")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupInfoRequest(AbstractModel):
    """DescribeGroupInfo request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: (Filter) filter by instance ID.
        :type InstanceId: str
        :param _GroupList: Kafka consumer group (`Consumer-group`), which is an array in the format of `GroupList.0=xxx&GroupList.1=yyy`.
        :type GroupList: list of str
        """
        self._InstanceId = None
        self._GroupList = None

    @property
    def InstanceId(self):
        """(Filter) filter by instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupList(self):
        """Kafka consumer group (`Consumer-group`), which is an array in the format of `GroupList.0=xxx&GroupList.1=yyy`.
        :rtype: list of str
        """
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GroupList = params.get("GroupList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupInfoResponse(AbstractModel):
    """DescribeGroupInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: list of GroupInfoResponse
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of GroupInfoResponse
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = GroupInfoResponse()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGroupOffsetsRequest(AbstractModel):
    """DescribeGroupOffsets request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: (Filter) filter by instance ID
        :type InstanceId: str
        :param _Group: Kafka consumer group
        :type Group: str
        :param _Topics: Array of the names of topics subscribed to by a group. If there is no such array, this parameter means the information of all topics in the specified group
        :type Topics: list of str
        :param _SearchWord: Fuzzy match by `topicName`
        :type SearchWord: str
        :param _Offset: Offset position of this query. Default value: 0
        :type Offset: int
        :param _Limit: Maximum number of results to be returned in this request. Default value: 50. Maximum value: 50
        :type Limit: int
        """
        self._InstanceId = None
        self._Group = None
        self._Topics = None
        self._SearchWord = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        """(Filter) filter by instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Group(self):
        """Kafka consumer group
        :rtype: str
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Topics(self):
        """Array of the names of topics subscribed to by a group. If there is no such array, this parameter means the information of all topics in the specified group
        :rtype: list of str
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def SearchWord(self):
        """Fuzzy match by `topicName`
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        """Offset position of this query. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Maximum number of results to be returned in this request. Default value: 50. Maximum value: 50
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Group = params.get("Group")
        self._Topics = params.get("Topics")
        self._SearchWord = params.get("SearchWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupOffsetsResponse(AbstractModel):
    """DescribeGroupOffsets response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result object
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupOffsetResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result object
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.GroupOffsetResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = GroupOffsetResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeGroupRequest(AbstractModel):
    """DescribeGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _SearchWord: Search keyword
        :type SearchWord: str
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Maximum number of results to be returned
        :type Limit: int
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Offset = None
        self._Limit = None

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
    def SearchWord(self):
        """Search keyword
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        """Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Maximum number of results to be returned
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchWord = params.get("SearchWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupResponse(AbstractModel):
    """DescribeGroup response structure.

    """

    def __init__(self):
        r"""
        :param _Result: List of returned results
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """List of returned results
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.GroupResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = GroupResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceAttributesRequest(AbstractModel):
    """DescribeInstanceAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceAttributesResponse(AbstractModel):
    """DescribeInstanceAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result object of instance attributes
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceAttributesResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result object of instance attributes
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceAttributesResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = InstanceAttributesResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeInstancesDetailRequest(AbstractModel):
    """DescribeInstancesDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: (Filter) filter by instance ID
        :type InstanceId: str
        :param _SearchWord: Filter by instance name, instance ID, AZ, VPC ID, or subnet ID. Fuzzy query is supported.
        :type SearchWord: str
        :param _Status: (Filter) instance status. 0: creating, 1: running, 2: deleting. If this parameter is left empty, all instances will be returned by default
        :type Status: list of int
        :param _Offset: Offset. If this parameter is left empty, `0` will be used by default.
        :type Offset: int
        :param _Limit: Number of returned results. If this parameter is left empty, `10` will be used by default. The maximum value is `20`.
        :type Limit: int
        :param _TagKey: Tag key match.
        :type TagKey: str
        :param _Filters: Filter. Valid values of `filter.Name` include `Ip`, `VpcId`, `SubNetId`, `InstanceType`, and `InstanceId`. Up to 10 values can be passed for `filter.Values`.
        :type Filters: list of Filter
        :param _InstanceIds: This parameter has been deprecated and replaced with `InstanceIdList`.
        :type InstanceIds: str
        :param _InstanceIdList: Filter by instance ID.
        :type InstanceIdList: list of str
        :param _TagList: Filter instances by a set of tags
        :type TagList: list of Tag
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Status = None
        self._Offset = None
        self._Limit = None
        self._TagKey = None
        self._Filters = None
        self._InstanceIds = None
        self._InstanceIdList = None
        self._TagList = None

    @property
    def InstanceId(self):
        """(Filter) filter by instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        """Filter by instance name, instance ID, AZ, VPC ID, or subnet ID. Fuzzy query is supported.
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Status(self):
        """(Filter) instance status. 0: creating, 1: running, 2: deleting. If this parameter is left empty, all instances will be returned by default
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        """Offset. If this parameter is left empty, `0` will be used by default.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned results. If this parameter is left empty, `10` will be used by default. The maximum value is `20`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TagKey(self):
        """Tag key match.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def Filters(self):
        """Filter. Valid values of `filter.Name` include `Ip`, `VpcId`, `SubNetId`, `InstanceType`, and `InstanceId`. Up to 10 values can be passed for `filter.Values`.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def InstanceIds(self):
        """This parameter has been deprecated and replaced with `InstanceIdList`.
        :rtype: str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceIdList(self):
        """Filter by instance ID.
        :rtype: list of str
        """
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

    @property
    def TagList(self):
        """Filter instances by a set of tags
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchWord = params.get("SearchWord")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TagKey = params.get("TagKey")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceIdList = params.get("InstanceIdList")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesDetailResponse(AbstractModel):
    """DescribeInstancesDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result object of instance details
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceDetailResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result object of instance details
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceDetailResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = InstanceDetailResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: (Filter) filter by instance ID
        :type InstanceId: str
        :param _SearchWord: (Filter) filter by instance name. Fuzzy search is supported
        :type SearchWord: str
        :param _Status: (Filter) instance status. 0: creating, 1: running, 2: deleting. If this parameter is left empty, all instances will be returned by default
        :type Status: list of int
        :param _Offset: Offset. If this parameter is left empty, 0 will be used by default
        :type Offset: int
        :param _Limit: Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 100.
        :type Limit: int
        :param _TagKey: Tag key value (this field has been deprecated).
        :type TagKey: str
        :param _VpcId: VPC ID.
        :type VpcId: str
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Status = None
        self._Offset = None
        self._Limit = None
        self._TagKey = None
        self._VpcId = None

    @property
    def InstanceId(self):
        """(Filter) filter by instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        """(Filter) filter by instance name. Fuzzy search is supported
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Status(self):
        """(Filter) instance status. 0: creating, 1: running, 2: deleting. If this parameter is left empty, all instances will be returned by default
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        """Offset. If this parameter is left empty, 0 will be used by default
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TagKey(self):
        """Tag key value (this field has been deprecated).
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def VpcId(self):
        """VPC ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchWord = params.get("SearchWord")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TagKey = params.get("TagKey")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = InstanceResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeRegionRequest(AbstractModel):
    """DescribeRegion request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: The offset value
        :type Offset: int
        :param _Limit: The maximum number of results returned
        :type Limit: int
        :param _Business: Business field, which can be ignored.
        :type Business: str
        :param _CdcId: CDC business field, which can be ignored.
        :type CdcId: str
        """
        self._Offset = None
        self._Limit = None
        self._Business = None
        self._CdcId = None

    @property
    def Offset(self):
        """The offset value
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """The maximum number of results returned
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Business(self):
        """Business field, which can be ignored.
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def CdcId(self):
        """CDC business field, which can be ignored.
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Business = params.get("Business")
        self._CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegionResponse(AbstractModel):
    """DescribeRegion response structure.

    """

    def __init__(self):
        r"""
        :param _Result: List of the returned results of enumerated regions
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Result: list of Region
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """List of the returned results of enumerated regions
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: list of Region
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = Region()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRouteRequest(AbstractModel):
    """DescribeRoute request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Unique instance ID
        :type InstanceId: str
        :param _RouteId: Route ID
        :type RouteId: int
        """
        self._InstanceId = None
        self._RouteId = None

    @property
    def InstanceId(self):
        """Unique instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RouteId(self):
        """Route ID
        :rtype: int
        """
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RouteId = params.get("RouteId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteResponse(AbstractModel):
    """DescribeRoute response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result set of route information
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.RouteResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result set of route information
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.RouteResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = RouteResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Unique task ID
        :type FlowId: int
        """
        self._FlowId = None

    @property
    def FlowId(self):
        """Unique task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TaskStatusResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TaskStatusResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = TaskStatusResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTopicAttributesRequest(AbstractModel):
    """DescribeTopicAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _TopicName: Topic name
        :type TopicName: str
        """
        self._InstanceId = None
        self._TopicName = None

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
    def TopicName(self):
        """Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicAttributesResponse(AbstractModel):
    """DescribeTopicAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result object
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicAttributesResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result object
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicAttributesResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = TopicAttributesResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTopicDetailRequest(AbstractModel):
    """DescribeTopicDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _SearchWord: (Filter) filter by `topicName`. Fuzzy search is supported
        :type SearchWord: str
        :param _Offset: Offset. If this parameter is left empty, 0 will be used by default
        :type Offset: int
        :param _Limit: Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 20. This value must be greater than 0
        :type Limit: int
        :param _AclRuleName: Name of the preset ACL rule.
        :type AclRuleName: str
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Offset = None
        self._Limit = None
        self._AclRuleName = None

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
    def SearchWord(self):
        """(Filter) filter by `topicName`. Fuzzy search is supported
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        """Offset. If this parameter is left empty, 0 will be used by default
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 20. This value must be greater than 0
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AclRuleName(self):
        """Name of the preset ACL rule.
        :rtype: str
        """
        return self._AclRuleName

    @AclRuleName.setter
    def AclRuleName(self, AclRuleName):
        self._AclRuleName = AclRuleName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchWord = params.get("SearchWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AclRuleName = params.get("AclRuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicDetailResponse(AbstractModel):
    """DescribeTopicDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned entity of topic details
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicDetailResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned entity of topic details
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicDetailResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = TopicDetailResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTopicProduceConnectionRequest(AbstractModel):
    """DescribeTopicProduceConnection request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _TopicName: Topic name
        :type TopicName: str
        """
        self._InstanceId = None
        self._TopicName = None

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
    def TopicName(self):
        """Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicProduceConnectionResponse(AbstractModel):
    """DescribeTopicProduceConnection response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Result set of returned connection information
        :type Result: list of DescribeConnectInfoResultDTO
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Result set of returned connection information
        :rtype: list of DescribeConnectInfoResultDTO
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = DescribeConnectInfoResultDTO()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopicRequest(AbstractModel):
    """DescribeTopic request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _SearchWord: Filter by `topicName`. Fuzzy search is supported
        :type SearchWord: str
        :param _Offset: Offset. If this parameter is left empty, 0 will be used by default
        :type Offset: int
        :param _Limit: The number of results to be returned, which defaults to 20 if left empty. The maximum value is 50.
        :type Limit: int
        :param _AclRuleName: Name of the preset ACL rule.
        :type AclRuleName: str
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Offset = None
        self._Limit = None
        self._AclRuleName = None

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
    def SearchWord(self):
        """Filter by `topicName`. Fuzzy search is supported
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        """Offset. If this parameter is left empty, 0 will be used by default
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """The number of results to be returned, which defaults to 20 if left empty. The maximum value is 50.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AclRuleName(self):
        """Name of the preset ACL rule.
        :rtype: str
        """
        return self._AclRuleName

    @AclRuleName.setter
    def AclRuleName(self, AclRuleName):
        self._AclRuleName = AclRuleName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchWord = params.get("SearchWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AclRuleName = params.get("AclRuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicResponse(AbstractModel):
    """DescribeTopic response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicResult`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = TopicResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTopicSubscribeGroupRequest(AbstractModel):
    """DescribeTopicSubscribeGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _TopicName: Topic name
        :type TopicName: str
        :param _Offset: Starting position of paging
        :type Offset: int
        :param _Limit: Number of results per page
        :type Limit: int
        """
        self._InstanceId = None
        self._TopicName = None
        self._Offset = None
        self._Limit = None

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
    def TopicName(self):
        """Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Offset(self):
        """Starting position of paging
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of results per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicSubscribeGroupResponse(AbstractModel):
    """DescribeTopicSubscribeGroup response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned results
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicSubscribeGroup`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned results
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicSubscribeGroup`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = TopicSubscribeGroup()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTopicSyncReplicaRequest(AbstractModel):
    """DescribeTopicSyncReplica request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _TopicName: Topic name
        :type TopicName: str
        :param _Offset: Offset. If this parameter is left empty, 0 will be used by default.
        :type Offset: int
        :param _Limit: Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 20.
        :type Limit: int
        :param _OutOfSyncReplicaOnly: Filters unsynced replicas only
        :type OutOfSyncReplicaOnly: bool
        """
        self._InstanceId = None
        self._TopicName = None
        self._Offset = None
        self._Limit = None
        self._OutOfSyncReplicaOnly = None

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
    def TopicName(self):
        """Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Offset(self):
        """Offset. If this parameter is left empty, 0 will be used by default.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OutOfSyncReplicaOnly(self):
        """Filters unsynced replicas only
        :rtype: bool
        """
        return self._OutOfSyncReplicaOnly

    @OutOfSyncReplicaOnly.setter
    def OutOfSyncReplicaOnly(self, OutOfSyncReplicaOnly):
        self._OutOfSyncReplicaOnly = OutOfSyncReplicaOnly


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OutOfSyncReplicaOnly = params.get("OutOfSyncReplicaOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicSyncReplicaResponse(AbstractModel):
    """DescribeTopicSyncReplica response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returns topic replica details
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicInSyncReplicaResult`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returns topic replica details
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicInSyncReplicaResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = TopicInSyncReplicaResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeUserRequest(AbstractModel):
    """DescribeUser request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _SearchWord: Filter by name
        :type SearchWord: str
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Number of results to be returned in this request
        :type Limit: int
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Offset = None
        self._Limit = None

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
    def SearchWord(self):
        """Filter by name
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        """Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of results to be returned in this request
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchWord = params.get("SearchWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserResponse(AbstractModel):
    """DescribeUser response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result list
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.UserResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result list
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.UserResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UserResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DynamicDiskConfig(AbstractModel):
    """Dynamic disk expansion configuration

    """

    def __init__(self):
        r"""
        :param _Enable: Whether to enable dynamic disk expansion configuration. `0`: disable, `1`: enable.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Enable: int
        :param _StepForwardPercentage: Percentage of dynamic disk expansion each time.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StepForwardPercentage: int
        :param _DiskQuotaPercentage: Disk quota threshold (in percentage) for triggering the automatic disk expansion event.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DiskQuotaPercentage: int
        :param _MaxDiskSpace: Max disk space in GB.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MaxDiskSpace: int
        """
        self._Enable = None
        self._StepForwardPercentage = None
        self._DiskQuotaPercentage = None
        self._MaxDiskSpace = None

    @property
    def Enable(self):
        """Whether to enable dynamic disk expansion configuration. `0`: disable, `1`: enable.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def StepForwardPercentage(self):
        """Percentage of dynamic disk expansion each time.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepForwardPercentage

    @StepForwardPercentage.setter
    def StepForwardPercentage(self, StepForwardPercentage):
        self._StepForwardPercentage = StepForwardPercentage

    @property
    def DiskQuotaPercentage(self):
        """Disk quota threshold (in percentage) for triggering the automatic disk expansion event.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskQuotaPercentage

    @DiskQuotaPercentage.setter
    def DiskQuotaPercentage(self, DiskQuotaPercentage):
        self._DiskQuotaPercentage = DiskQuotaPercentage

    @property
    def MaxDiskSpace(self):
        """Max disk space in GB.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxDiskSpace

    @MaxDiskSpace.setter
    def MaxDiskSpace(self, MaxDiskSpace):
        self._MaxDiskSpace = MaxDiskSpace


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._StepForwardPercentage = params.get("StepForwardPercentage")
        self._DiskQuotaPercentage = params.get("DiskQuotaPercentage")
        self._MaxDiskSpace = params.get("MaxDiskSpace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DynamicRetentionTime(AbstractModel):
    """Dynamic message retention time configuration

    """

    def __init__(self):
        r"""
        :param _Enable: Whether the dynamic message retention time configuration is enabled. 0: disabled; 1: enabled
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Enable: int
        :param _DiskQuotaPercentage: Disk quota threshold (in percentage) for triggering the message retention time change event
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type DiskQuotaPercentage: int
        :param _StepForwardPercentage: Percentage by which the message retention time is shortened each time
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type StepForwardPercentage: int
        :param _BottomRetention: Minimum retention time, in minutes
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type BottomRetention: int
        """
        self._Enable = None
        self._DiskQuotaPercentage = None
        self._StepForwardPercentage = None
        self._BottomRetention = None

    @property
    def Enable(self):
        """Whether the dynamic message retention time configuration is enabled. 0: disabled; 1: enabled
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def DiskQuotaPercentage(self):
        """Disk quota threshold (in percentage) for triggering the message retention time change event
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskQuotaPercentage

    @DiskQuotaPercentage.setter
    def DiskQuotaPercentage(self, DiskQuotaPercentage):
        self._DiskQuotaPercentage = DiskQuotaPercentage

    @property
    def StepForwardPercentage(self):
        """Percentage by which the message retention time is shortened each time
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepForwardPercentage

    @StepForwardPercentage.setter
    def StepForwardPercentage(self, StepForwardPercentage):
        self._StepForwardPercentage = StepForwardPercentage

    @property
    def BottomRetention(self):
        """Minimum retention time, in minutes
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BottomRetention

    @BottomRetention.setter
    def BottomRetention(self, BottomRetention):
        self._BottomRetention = BottomRetention


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._DiskQuotaPercentage = params.get("DiskQuotaPercentage")
        self._StepForwardPercentage = params.get("StepForwardPercentage")
        self._BottomRetention = params.get("BottomRetention")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchMessageByOffsetRequest(AbstractModel):
    """FetchMessageByOffset request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Topic: Topic name
        :type Topic: str
        :param _Partition: Partition ID
        :type Partition: int
        :param _Offset: Offset information, which is required.
        :type Offset: int
        """
        self._InstanceId = None
        self._Topic = None
        self._Partition = None
        self._Offset = None

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
    def Topic(self):
        """Topic name
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        """Partition ID
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        """Offset information, which is required.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._Partition = params.get("Partition")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchMessageByOffsetResponse(AbstractModel):
    """FetchMessageByOffset response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned results
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConsumerRecord`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned results
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ConsumerRecord`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ConsumerRecord()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class FetchMessageListByOffsetRequest(AbstractModel):
    """FetchMessageListByOffset request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Topic: Topic name
        :type Topic: str
        :param _Partition: Partition ID
        :type Partition: int
        :param _Offset: Offset information
        :type Offset: int
        :param _SinglePartitionRecordNumber: The maximum number of messages that can be queried. Default value: 20. Maximum value: 20.
        :type SinglePartitionRecordNumber: int
        """
        self._InstanceId = None
        self._Topic = None
        self._Partition = None
        self._Offset = None
        self._SinglePartitionRecordNumber = None

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
    def Topic(self):
        """Topic name
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        """Partition ID
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        """Offset information
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SinglePartitionRecordNumber(self):
        """The maximum number of messages that can be queried. Default value: 20. Maximum value: 20.
        :rtype: int
        """
        return self._SinglePartitionRecordNumber

    @SinglePartitionRecordNumber.setter
    def SinglePartitionRecordNumber(self, SinglePartitionRecordNumber):
        self._SinglePartitionRecordNumber = SinglePartitionRecordNumber


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._Partition = params.get("Partition")
        self._Offset = params.get("Offset")
        self._SinglePartitionRecordNumber = params.get("SinglePartitionRecordNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchMessageListByOffsetResponse(AbstractModel):
    """FetchMessageListByOffset response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result. Note: The returned list does not display the message content (key and value). To query the message content, call the `FetchMessageByOffset` API.
        :type Result: list of ConsumerRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result. Note: The returned list does not display the message content (key and value). To query the message content, call the `FetchMessageByOffset` API.
        :rtype: list of ConsumerRecord
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = ConsumerRecord()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Query filter
    >Key-value pair filters for conditional filtering queries, such as filter ID, name, and status
    > * If there are multiple `Filter`, the relationship among them is logical `AND`.
    > * If there are multiple `Values` in the same `Filter`, the relationship among them is logical `OR`.
    >

    """

    def __init__(self):
        r"""
        :param _Name: Field to be filtered.
        :type Name: str
        :param _Values: Filter value of field.
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
        """Filter value of field.
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
        


class Group(AbstractModel):
    """Group entity

    """

    def __init__(self):
        r"""
        :param _GroupName: Group name
        :type GroupName: str
        """
        self._GroupName = None

    @property
    def GroupName(self):
        """Group name
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfoMember(AbstractModel):
    """Consumer information

    """

    def __init__(self):
        r"""
        :param _MemberId: Unique ID generated for consumer in consumer group by coordinator
        :type MemberId: str
        :param _ClientId: `client.id` information by the client consumer SDK
        :type ClientId: str
        :param _ClientHost: Generally stores client IP address
        :type ClientHost: str
        :param _Assignment: Stores the information of partition assigned to this consumer
        :type Assignment: :class:`tencentcloud.ckafka.v20190819.models.Assignment`
        """
        self._MemberId = None
        self._ClientId = None
        self._ClientHost = None
        self._Assignment = None

    @property
    def MemberId(self):
        """Unique ID generated for consumer in consumer group by coordinator
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def ClientId(self):
        """`client.id` information by the client consumer SDK
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ClientHost(self):
        """Generally stores client IP address
        :rtype: str
        """
        return self._ClientHost

    @ClientHost.setter
    def ClientHost(self, ClientHost):
        self._ClientHost = ClientHost

    @property
    def Assignment(self):
        """Stores the information of partition assigned to this consumer
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.Assignment`
        """
        return self._Assignment

    @Assignment.setter
    def Assignment(self, Assignment):
        self._Assignment = Assignment


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._ClientId = params.get("ClientId")
        self._ClientHost = params.get("ClientHost")
        if params.get("Assignment") is not None:
            self._Assignment = Assignment()
            self._Assignment._deserialize(params.get("Assignment"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfoResponse(AbstractModel):
    """`GroupInfo` response data entity

    """

    def __init__(self):
        r"""
        :param _ErrorCode: Error code. 0: success
        :type ErrorCode: str
        :param _State: Group status description (common valid values: Empty, Stable, Dead):
Dead: the consumer group does not exist
Empty: there are currently no consumer subscriptions in the consumer group
PreparingRebalance: the consumer group is currently in `rebalance` state
CompletingRebalance: the consumer group is currently in `rebalance` state
Stable: each consumer in the consumer group has joined and is in stable state
        :type State: str
        :param _ProtocolType: The type of protocol selected by the consumer group, which is `consumer` for common consumers. However, some systems use their own protocols; for example, the protocol used by kafka-connect is `connect`. Only with the standard `consumer` protocol can this API get to know the specific assigning method and parse the specific partition assignment
        :type ProtocolType: str
        :param _Protocol: Consumer partition assignment algorithm, such as `range` (which is the default value for the Kafka consumer SDK), `roundrobin`, and `sticky`
        :type Protocol: str
        :param _Members: This array contains information only if `state` is `Stable` and `protocol_type` is `consumer`
        :type Members: list of GroupInfoMember
        :param _Group: Kafka consumer group
        :type Group: str
        """
        self._ErrorCode = None
        self._State = None
        self._ProtocolType = None
        self._Protocol = None
        self._Members = None
        self._Group = None

    @property
    def ErrorCode(self):
        """Error code. 0: success
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def State(self):
        """Group status description (common valid values: Empty, Stable, Dead):
Dead: the consumer group does not exist
Empty: there are currently no consumer subscriptions in the consumer group
PreparingRebalance: the consumer group is currently in `rebalance` state
CompletingRebalance: the consumer group is currently in `rebalance` state
Stable: each consumer in the consumer group has joined and is in stable state
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ProtocolType(self):
        """The type of protocol selected by the consumer group, which is `consumer` for common consumers. However, some systems use their own protocols; for example, the protocol used by kafka-connect is `connect`. Only with the standard `consumer` protocol can this API get to know the specific assigning method and parse the specific partition assignment
        :rtype: str
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def Protocol(self):
        """Consumer partition assignment algorithm, such as `range` (which is the default value for the Kafka consumer SDK), `roundrobin`, and `sticky`
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Members(self):
        """This array contains information only if `state` is `Stable` and `protocol_type` is `consumer`
        :rtype: list of GroupInfoMember
        """
        return self._Members

    @Members.setter
    def Members(self, Members):
        self._Members = Members

    @property
    def Group(self):
        """Kafka consumer group
        :rtype: str
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._State = params.get("State")
        self._ProtocolType = params.get("ProtocolType")
        self._Protocol = params.get("Protocol")
        if params.get("Members") is not None:
            self._Members = []
            for item in params.get("Members"):
                obj = GroupInfoMember()
                obj._deserialize(item)
                self._Members.append(obj)
        self._Group = params.get("Group")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfoTopics(AbstractModel):
    """Internal topic object of `GroupInfo`

    """

    def __init__(self):
        r"""
        :param _Topic: Name of assigned topics
        :type Topic: str
        :param _Partitions: Information of assigned partition
Note: this field may return null, indicating that no valid values can be obtained.
        :type Partitions: list of int
        """
        self._Topic = None
        self._Partitions = None

    @property
    def Topic(self):
        """Name of assigned topics
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partitions(self):
        """Information of assigned partition
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._Partitions = params.get("Partitions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupOffsetPartition(AbstractModel):
    """Group offset partition object

    """

    def __init__(self):
        r"""
        :param _Partition: Topic `partitionId`
        :type Partition: int
        :param _Offset: Offset position submitted by consumer
        :type Offset: int
        :param _Metadata: Metadata can be passed in for other purposes when the consumer submits messages. Currently, this parameter is usually an empty string
Note: this field may return null, indicating that no valid values can be obtained.
        :type Metadata: str
        :param _ErrorCode: Error code
        :type ErrorCode: int
        :param _LogEndOffset: Latest offset of current partition
        :type LogEndOffset: int
        :param _Lag: Number of unconsumed messages
        :type Lag: int
        """
        self._Partition = None
        self._Offset = None
        self._Metadata = None
        self._ErrorCode = None
        self._LogEndOffset = None
        self._Lag = None

    @property
    def Partition(self):
        """Topic `partitionId`
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        """Offset position submitted by consumer
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Metadata(self):
        """Metadata can be passed in for other purposes when the consumer submits messages. Currently, this parameter is usually an empty string
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def ErrorCode(self):
        """Error code
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def LogEndOffset(self):
        """Latest offset of current partition
        :rtype: int
        """
        return self._LogEndOffset

    @LogEndOffset.setter
    def LogEndOffset(self, LogEndOffset):
        self._LogEndOffset = LogEndOffset

    @property
    def Lag(self):
        """Number of unconsumed messages
        :rtype: int
        """
        return self._Lag

    @Lag.setter
    def Lag(self, Lag):
        self._Lag = Lag


    def _deserialize(self, params):
        self._Partition = params.get("Partition")
        self._Offset = params.get("Offset")
        self._Metadata = params.get("Metadata")
        self._ErrorCode = params.get("ErrorCode")
        self._LogEndOffset = params.get("LogEndOffset")
        self._Lag = params.get("Lag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupOffsetResponse(AbstractModel):
    """Returned result of consumer group offset

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of eligible results
        :type TotalCount: int
        :param _TopicList: Array of partitions in the topic, where each element is a JSON object
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicList: list of GroupOffsetTopic
        """
        self._TotalCount = None
        self._TopicList = None

    @property
    def TotalCount(self):
        """Total number of eligible results
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TopicList(self):
        """Array of partitions in the topic, where each element is a JSON object
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of GroupOffsetTopic
        """
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TopicList") is not None:
            self._TopicList = []
            for item in params.get("TopicList"):
                obj = GroupOffsetTopic()
                obj._deserialize(item)
                self._TopicList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupOffsetTopic(AbstractModel):
    """Consumer group topic object

    """

    def __init__(self):
        r"""
        :param _Topic: Topic name
        :type Topic: str
        :param _Partitions: Array of partitions in the topic, where each element is a JSON object
Note: this field may return null, indicating that no valid values can be obtained.
        :type Partitions: list of GroupOffsetPartition
        """
        self._Topic = None
        self._Partitions = None

    @property
    def Topic(self):
        """Topic name
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partitions(self):
        """Array of partitions in the topic, where each element is a JSON object
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of GroupOffsetPartition
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = GroupOffsetPartition()
                obj._deserialize(item)
                self._Partitions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupResponse(AbstractModel):
    """`DescribeGroup` response

    """

    def __init__(self):
        r"""
        :param _TotalCount: Count
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _GroupList: GroupList
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupList: list of DescribeGroup
        :param _GroupCountQuota: Consumer group quota
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupCountQuota: int
        """
        self._TotalCount = None
        self._GroupList = None
        self._GroupCountQuota = None

    @property
    def TotalCount(self):
        """Count
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def GroupList(self):
        """GroupList
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of DescribeGroup
        """
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList

    @property
    def GroupCountQuota(self):
        """Consumer group quota
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._GroupCountQuota

    @GroupCountQuota.setter
    def GroupCountQuota(self, GroupCountQuota):
        self._GroupCountQuota = GroupCountQuota


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("GroupList") is not None:
            self._GroupList = []
            for item in params.get("GroupList"):
                obj = DescribeGroup()
                obj._deserialize(item)
                self._GroupList.append(obj)
        self._GroupCountQuota = params.get("GroupCountQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquireCkafkaPriceRequest(AbstractModel):
    """InquireCkafkaPrice request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceType: `standard`: Standard Edition; `profession`: Pro Edition
        :type InstanceType: str
        :param _InstanceChargeParam: Billing mode for instance purchase/renewal. If this parameter is left empty when you purchase an instance, the fees for one month under the monthly subscription mode will be displayed by default.
        :type InstanceChargeParam: :class:`tencentcloud.ckafka.v20190819.models.InstanceChargeParam`
        :param _InstanceNum: The number of instances to be purchased or renewed. If this parameter is left empty, the default value is `1`.
        :type InstanceNum: int
        :param _Bandwidth: Private network bandwidth in MB/sec, which is required when you purchase an instance.
        :type Bandwidth: int
        :param _InquiryDiskParam: Disk type and size, which is required when you purchase an instance.
        :type InquiryDiskParam: :class:`tencentcloud.ckafka.v20190819.models.InquiryDiskParam`
        :param _MessageRetention: Message retention period in hours, which is required when you purchase an instance.
        :type MessageRetention: int
        :param _Topic: The number of instance topics to be purchased, which is required when you purchase an instance.
        :type Topic: int
        :param _Partition: The number of instance partitions to be purchased, which is required when you purchase an instance.
        :type Partition: int
        :param _ZoneIds: The region for instance purchase, which can be obtained via the `DescribeCkafkaZone` API.
        :type ZoneIds: list of int
        :param _CategoryAction: Operation type flag. `purchase`: Making new purchases; `renew`: Renewing an instance. The default value is `purchase` if this parameter is left empty.
        :type CategoryAction: str
        :param _BillType: This field is not required.
        :type BillType: str
        :param _PublicNetworkParam: Billing mode for public network bandwidth, which is required when you purchase public network bandwidth. Currently, public network bandwidth is only supported for Pro Edition.
        :type PublicNetworkParam: :class:`tencentcloud.ckafka.v20190819.models.InquiryPublicNetworkParam`
        :param _InstanceId: ID of the instance to be renewed, which is required when you renew an instance.
        :type InstanceId: str
        """
        self._InstanceType = None
        self._InstanceChargeParam = None
        self._InstanceNum = None
        self._Bandwidth = None
        self._InquiryDiskParam = None
        self._MessageRetention = None
        self._Topic = None
        self._Partition = None
        self._ZoneIds = None
        self._CategoryAction = None
        self._BillType = None
        self._PublicNetworkParam = None
        self._InstanceId = None

    @property
    def InstanceType(self):
        """`standard`: Standard Edition; `profession`: Pro Edition
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceChargeParam(self):
        """Billing mode for instance purchase/renewal. If this parameter is left empty when you purchase an instance, the fees for one month under the monthly subscription mode will be displayed by default.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceChargeParam`
        """
        return self._InstanceChargeParam

    @InstanceChargeParam.setter
    def InstanceChargeParam(self, InstanceChargeParam):
        self._InstanceChargeParam = InstanceChargeParam

    @property
    def InstanceNum(self):
        """The number of instances to be purchased or renewed. If this parameter is left empty, the default value is `1`.
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def Bandwidth(self):
        """Private network bandwidth in MB/sec, which is required when you purchase an instance.
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def InquiryDiskParam(self):
        """Disk type and size, which is required when you purchase an instance.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryDiskParam`
        """
        return self._InquiryDiskParam

    @InquiryDiskParam.setter
    def InquiryDiskParam(self, InquiryDiskParam):
        self._InquiryDiskParam = InquiryDiskParam

    @property
    def MessageRetention(self):
        """Message retention period in hours, which is required when you purchase an instance.
        :rtype: int
        """
        return self._MessageRetention

    @MessageRetention.setter
    def MessageRetention(self, MessageRetention):
        self._MessageRetention = MessageRetention

    @property
    def Topic(self):
        """The number of instance topics to be purchased, which is required when you purchase an instance.
        :rtype: int
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        """The number of instance partitions to be purchased, which is required when you purchase an instance.
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def ZoneIds(self):
        """The region for instance purchase, which can be obtained via the `DescribeCkafkaZone` API.
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def CategoryAction(self):
        """Operation type flag. `purchase`: Making new purchases; `renew`: Renewing an instance. The default value is `purchase` if this parameter is left empty.
        :rtype: str
        """
        return self._CategoryAction

    @CategoryAction.setter
    def CategoryAction(self, CategoryAction):
        self._CategoryAction = CategoryAction

    @property
    def BillType(self):
        """This field is not required.
        :rtype: str
        """
        return self._BillType

    @BillType.setter
    def BillType(self, BillType):
        self._BillType = BillType

    @property
    def PublicNetworkParam(self):
        """Billing mode for public network bandwidth, which is required when you purchase public network bandwidth. Currently, public network bandwidth is only supported for Pro Edition.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryPublicNetworkParam`
        """
        return self._PublicNetworkParam

    @PublicNetworkParam.setter
    def PublicNetworkParam(self, PublicNetworkParam):
        self._PublicNetworkParam = PublicNetworkParam

    @property
    def InstanceId(self):
        """ID of the instance to be renewed, which is required when you renew an instance.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        if params.get("InstanceChargeParam") is not None:
            self._InstanceChargeParam = InstanceChargeParam()
            self._InstanceChargeParam._deserialize(params.get("InstanceChargeParam"))
        self._InstanceNum = params.get("InstanceNum")
        self._Bandwidth = params.get("Bandwidth")
        if params.get("InquiryDiskParam") is not None:
            self._InquiryDiskParam = InquiryDiskParam()
            self._InquiryDiskParam._deserialize(params.get("InquiryDiskParam"))
        self._MessageRetention = params.get("MessageRetention")
        self._Topic = params.get("Topic")
        self._Partition = params.get("Partition")
        self._ZoneIds = params.get("ZoneIds")
        self._CategoryAction = params.get("CategoryAction")
        self._BillType = params.get("BillType")
        if params.get("PublicNetworkParam") is not None:
            self._PublicNetworkParam = InquiryPublicNetworkParam()
            self._PublicNetworkParam._deserialize(params.get("PublicNetworkParam"))
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquireCkafkaPriceResp(AbstractModel):
    """Values returned by the `InquireCkafkaPrice` API

    """

    def __init__(self):
        r"""
        :param _InstancePrice: Instance price
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstancePrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryPrice`
        :param _PublicNetworkBandwidthPrice: Public network bandwidth price
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicNetworkBandwidthPrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryPrice`
        """
        self._InstancePrice = None
        self._PublicNetworkBandwidthPrice = None

    @property
    def InstancePrice(self):
        """Instance price
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryPrice`
        """
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def PublicNetworkBandwidthPrice(self):
        """Public network bandwidth price
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryPrice`
        """
        return self._PublicNetworkBandwidthPrice

    @PublicNetworkBandwidthPrice.setter
    def PublicNetworkBandwidthPrice(self, PublicNetworkBandwidthPrice):
        self._PublicNetworkBandwidthPrice = PublicNetworkBandwidthPrice


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self._InstancePrice = InquiryPrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("PublicNetworkBandwidthPrice") is not None:
            self._PublicNetworkBandwidthPrice = InquiryPrice()
            self._PublicNetworkBandwidthPrice._deserialize(params.get("PublicNetworkBandwidthPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquireCkafkaPriceResponse(AbstractModel):
    """InquireCkafkaPrice response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Output parameters
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InquireCkafkaPriceResp`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Output parameters
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquireCkafkaPriceResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = InquireCkafkaPriceResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class InquiryBasePrice(AbstractModel):
    """Response parameters for instance price query

    """

    def __init__(self):
        r"""
        :param _UnitPrice: Original unit price
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnitPrice: float
        :param _UnitPriceDiscount: Discounted unit price
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnitPriceDiscount: float
        :param _OriginalPrice: Original price in total
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalPrice: float
        :param _DiscountPrice: Discounted price in total
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiscountPrice: float
        :param _Discount: Discount (%)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Discount: float
        :param _GoodsNum: Number of purchased items
Note: This field may return null, indicating that no valid values can be obtained.
        :type GoodsNum: int
        :param _Currency: Currency for payment
Note: This field may return null, indicating that no valid values can be obtained.
        :type Currency: str
        :param _DiskType: Dedicated disk response parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param _TimeSpan: Validity period
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeSpan: int
        :param _TimeUnit: Unit of the validity period (`m`: Month; `h`: Hour)
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeUnit: str
        :param _Value: Purchase quantity
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: int
        """
        self._UnitPrice = None
        self._UnitPriceDiscount = None
        self._OriginalPrice = None
        self._DiscountPrice = None
        self._Discount = None
        self._GoodsNum = None
        self._Currency = None
        self._DiskType = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._Value = None

    @property
    def UnitPrice(self):
        """Original unit price
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceDiscount(self):
        """Discounted unit price
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def OriginalPrice(self):
        """Original price in total
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        """Discounted price in total
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def Discount(self):
        """Discount (%)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def GoodsNum(self):
        """Number of purchased items
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Currency(self):
        """Currency for payment
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def DiskType(self):
        """Dedicated disk response parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def TimeSpan(self):
        """Validity period
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        """Unit of the validity period (`m`: Month; `h`: Hour)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def Value(self):
        """Purchase quantity
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._UnitPrice = params.get("UnitPrice")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        self._Discount = params.get("Discount")
        self._GoodsNum = params.get("GoodsNum")
        self._Currency = params.get("Currency")
        self._DiskType = params.get("DiskType")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryDetailPrice(AbstractModel):
    """Prices of different purchased items

    """

    def __init__(self):
        r"""
        :param _BandwidthPrice: Price of additional private network bandwidth
Note: This field may return null, indicating that no valid values can be obtained.
        :type BandwidthPrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        :param _DiskPrice: Disk price
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskPrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        :param _PartitionPrice: Price of additional partitions
Note: This field may return null, indicating that no valid values can be obtained.
        :type PartitionPrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        :param _TopicPrice: Price of additional topics
Note: This field may return null, indicating that no valid values can be obtained.
        :type TopicPrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        :param _InstanceTypePrice: Instance package price
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceTypePrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        self._BandwidthPrice = None
        self._DiskPrice = None
        self._PartitionPrice = None
        self._TopicPrice = None
        self._InstanceTypePrice = None

    @property
    def BandwidthPrice(self):
        """Price of additional private network bandwidth
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        return self._BandwidthPrice

    @BandwidthPrice.setter
    def BandwidthPrice(self, BandwidthPrice):
        self._BandwidthPrice = BandwidthPrice

    @property
    def DiskPrice(self):
        """Disk price
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def PartitionPrice(self):
        """Price of additional partitions
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        return self._PartitionPrice

    @PartitionPrice.setter
    def PartitionPrice(self, PartitionPrice):
        self._PartitionPrice = PartitionPrice

    @property
    def TopicPrice(self):
        """Price of additional topics
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        return self._TopicPrice

    @TopicPrice.setter
    def TopicPrice(self, TopicPrice):
        self._TopicPrice = TopicPrice

    @property
    def InstanceTypePrice(self):
        """Instance package price
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        return self._InstanceTypePrice

    @InstanceTypePrice.setter
    def InstanceTypePrice(self, InstanceTypePrice):
        self._InstanceTypePrice = InstanceTypePrice


    def _deserialize(self, params):
        if params.get("BandwidthPrice") is not None:
            self._BandwidthPrice = InquiryBasePrice()
            self._BandwidthPrice._deserialize(params.get("BandwidthPrice"))
        if params.get("DiskPrice") is not None:
            self._DiskPrice = InquiryBasePrice()
            self._DiskPrice._deserialize(params.get("DiskPrice"))
        if params.get("PartitionPrice") is not None:
            self._PartitionPrice = InquiryBasePrice()
            self._PartitionPrice._deserialize(params.get("PartitionPrice"))
        if params.get("TopicPrice") is not None:
            self._TopicPrice = InquiryBasePrice()
            self._TopicPrice._deserialize(params.get("TopicPrice"))
        if params.get("InstanceTypePrice") is not None:
            self._InstanceTypePrice = InquiryBasePrice()
            self._InstanceTypePrice._deserialize(params.get("InstanceTypePrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryDiskParam(AbstractModel):
    """Disk purchase parameters

    """

    def __init__(self):
        r"""
        :param _DiskType: Disk type. Valid values: `SSD` (SSD), `CLOUD_SSD` (SSD cloud disk), `CLOUD_PREMIUM` (Premium cloud disk), `CLOUD_BASIC` (Cloud disk).
        :type DiskType: str
        :param _DiskSize: Size of the purchased disk in GB
        :type DiskSize: int
        """
        self._DiskType = None
        self._DiskSize = None

    @property
    def DiskType(self):
        """Disk type. Valid values: `SSD` (SSD), `CLOUD_SSD` (SSD cloud disk), `CLOUD_PREMIUM` (Premium cloud disk), `CLOUD_BASIC` (Cloud disk).
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """Size of the purchased disk in GB
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
        


class InquiryPrice(AbstractModel):
    """Response parameters for instance price query

    """

    def __init__(self):
        r"""
        :param _UnitPrice: Original unit price
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnitPrice: float
        :param _UnitPriceDiscount: Discounted unit price
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnitPriceDiscount: float
        :param _OriginalPrice: Original price in total
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalPrice: float
        :param _DiscountPrice: Discounted price in total
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiscountPrice: float
        :param _Discount: Discount (%)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Discount: float
        :param _GoodsNum: Number of purchased items
Note: This field may return null, indicating that no valid values can be obtained.
        :type GoodsNum: int
        :param _Currency: Currency for payment
Note: This field may return null, indicating that no valid values can be obtained.
        :type Currency: str
        :param _DiskType: Dedicated disk response parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param _TimeSpan: Validity period
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeSpan: int
        :param _TimeUnit: Unit of the validity period (`m`: Month; `h`: Hour)
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeUnit: str
        :param _Value: Purchase quantity
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: int
        :param _DetailPrices: Prices of different purchased items
Note: This field may return null, indicating that no valid values can be obtained.
        :type DetailPrices: :class:`tencentcloud.ckafka.v20190819.models.InquiryDetailPrice`
        """
        self._UnitPrice = None
        self._UnitPriceDiscount = None
        self._OriginalPrice = None
        self._DiscountPrice = None
        self._Discount = None
        self._GoodsNum = None
        self._Currency = None
        self._DiskType = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._Value = None
        self._DetailPrices = None

    @property
    def UnitPrice(self):
        """Original unit price
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceDiscount(self):
        """Discounted unit price
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def OriginalPrice(self):
        """Original price in total
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        """Discounted price in total
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def Discount(self):
        """Discount (%)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def GoodsNum(self):
        """Number of purchased items
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Currency(self):
        """Currency for payment
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def DiskType(self):
        """Dedicated disk response parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def TimeSpan(self):
        """Validity period
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        """Unit of the validity period (`m`: Month; `h`: Hour)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def Value(self):
        """Purchase quantity
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def DetailPrices(self):
        """Prices of different purchased items
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryDetailPrice`
        """
        return self._DetailPrices

    @DetailPrices.setter
    def DetailPrices(self, DetailPrices):
        self._DetailPrices = DetailPrices


    def _deserialize(self, params):
        self._UnitPrice = params.get("UnitPrice")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        self._Discount = params.get("Discount")
        self._GoodsNum = params.get("GoodsNum")
        self._Currency = params.get("Currency")
        self._DiskType = params.get("DiskType")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._Value = params.get("Value")
        if params.get("DetailPrices") is not None:
            self._DetailPrices = InquiryDetailPrice()
            self._DetailPrices._deserialize(params.get("DetailPrices"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPublicNetworkParam(AbstractModel):
    """Public network bandwidth parameters

    """

    def __init__(self):
        r"""
        :param _PublicNetworkChargeType: Public network bandwidth billing mode (`BANDWIDTH_PREPAID`: Monthly subscription; `BANDWIDTH_POSTPAID_BY_HOUR`: Bill-by-hour)
        :type PublicNetworkChargeType: str
        :param _PublicNetworkMonthly: Public network bandwidth in MB
        :type PublicNetworkMonthly: int
        """
        self._PublicNetworkChargeType = None
        self._PublicNetworkMonthly = None

    @property
    def PublicNetworkChargeType(self):
        """Public network bandwidth billing mode (`BANDWIDTH_PREPAID`: Monthly subscription; `BANDWIDTH_POSTPAID_BY_HOUR`: Bill-by-hour)
        :rtype: str
        """
        return self._PublicNetworkChargeType

    @PublicNetworkChargeType.setter
    def PublicNetworkChargeType(self, PublicNetworkChargeType):
        self._PublicNetworkChargeType = PublicNetworkChargeType

    @property
    def PublicNetworkMonthly(self):
        """Public network bandwidth in MB
        :rtype: int
        """
        return self._PublicNetworkMonthly

    @PublicNetworkMonthly.setter
    def PublicNetworkMonthly(self, PublicNetworkMonthly):
        self._PublicNetworkMonthly = PublicNetworkMonthly


    def _deserialize(self, params):
        self._PublicNetworkChargeType = params.get("PublicNetworkChargeType")
        self._PublicNetworkMonthly = params.get("PublicNetworkMonthly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """Instance object

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _Status: Instance status. 0: creating, 1: running, 2: deleting, 5: isolated, -1: creation failed
        :type Status: int
        :param _IfCommunity: Whether it is an open-source instance. true: yes, false: no
Note: this field may return null, indicating that no valid values can be obtained.
        :type IfCommunity: bool
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Status = None
        self._IfCommunity = None

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
    def InstanceName(self):
        """Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Status(self):
        """Instance status. 0: creating, 1: running, 2: deleting, 5: isolated, -1: creation failed
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IfCommunity(self):
        """Whether it is an open-source instance. true: yes, false: no
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IfCommunity

    @IfCommunity.setter
    def IfCommunity(self, IfCommunity):
        self._IfCommunity = IfCommunity


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Status = params.get("Status")
        self._IfCommunity = params.get("IfCommunity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAttributesResponse(AbstractModel):
    """Returned result object of instance attributes

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _VipList: VIP list information of access point
        :type VipList: list of VipEntity
        :param _Vip: Virtual IP
        :type Vip: str
        :param _Vport: Virtual port
        :type Vport: str
        :param _Status: Instance status. 0: creating, 1: running, 2: deleting
        :type Status: int
        :param _Bandwidth: Instance bandwidth in Mbps
        :type Bandwidth: int
        :param _DiskSize: Instance storage capacity in GB
        :type DiskSize: int
        :param _ZoneId: AZ
        :type ZoneId: int
        :param _VpcId: VPC ID. If this parameter is empty, it means the basic network
        :type VpcId: str
        :param _SubnetId: Subnet ID. If this parameter is empty, it means the basic network
        :type SubnetId: str
        :param _Healthy: Instance health status. 1: healthy, 2: alarmed, 3: exceptional
        :type Healthy: int
        :param _HealthyMessage: Instance health information. Currently, the disk utilization is displayed with a maximum length of 256
        :type HealthyMessage: str
        :param _CreateTime: Creation time
        :type CreateTime: int
        :param _MsgRetentionTime: Message retention period in minutes
        :type MsgRetentionTime: int
        :param _Config: Configuration for automatic topic creation. If this field is empty, it means that automatic creation is not enabled
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.InstanceConfigDO`
        :param _RemainderPartitions: Number of remaining creatable partitions
        :type RemainderPartitions: int
        :param _RemainderTopics: Number of remaining creatable topics
        :type RemainderTopics: int
        :param _CreatedPartitions: Number of partitions already created
        :type CreatedPartitions: int
        :param _CreatedTopics: Number of topics already created
        :type CreatedTopics: int
        :param _Tags: Tag array
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _ExpireTime: Expiration time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: int
        :param _ZoneIds: Cross-AZ
Note: this field may return null, indicating that no valid values can be obtained.
        :type ZoneIds: list of int
        :param _Version: Kafka version information
Note: this field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param _MaxGroupNum: Maximum number of groups
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxGroupNum: int
        :param _Cvm: Offering type. `0`: Standard Edition; `1`: Professional Edition
Note: this field may return `null`, indicating that no valid value was found.
        :type Cvm: int
        :param _InstanceType: Type.
Note: this field may return `null`, indicating that no valid value was found.
        :type InstanceType: str
        :param _Features: Features supported by the instance. `FEATURE_SUBNET_ACL` indicates that the ACL policy supports setting subnets. 
Note: this field may return null, indicating that no valid values can be obtained.
        :type Features: list of str
        :param _RetentionTimeConfig: Dynamic message retention policy
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        :param _MaxConnection: Maximum number of connections
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxConnection: int
        :param _PublicNetwork: Public network bandwidth
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicNetwork: int
        :param _DeleteRouteTimestamp: Time
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeleteRouteTimestamp: str
        :param _RemainingPartitions: Number of remaining creatable partitions
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RemainingPartitions: int
        :param _RemainingTopics: Number of remaining creatable topics
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RemainingTopics: int
        :param _DynamicDiskConfig: Dynamic disk expansion policy.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DynamicDiskConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicDiskConfig`
        """
        self._InstanceId = None
        self._InstanceName = None
        self._VipList = None
        self._Vip = None
        self._Vport = None
        self._Status = None
        self._Bandwidth = None
        self._DiskSize = None
        self._ZoneId = None
        self._VpcId = None
        self._SubnetId = None
        self._Healthy = None
        self._HealthyMessage = None
        self._CreateTime = None
        self._MsgRetentionTime = None
        self._Config = None
        self._RemainderPartitions = None
        self._RemainderTopics = None
        self._CreatedPartitions = None
        self._CreatedTopics = None
        self._Tags = None
        self._ExpireTime = None
        self._ZoneIds = None
        self._Version = None
        self._MaxGroupNum = None
        self._Cvm = None
        self._InstanceType = None
        self._Features = None
        self._RetentionTimeConfig = None
        self._MaxConnection = None
        self._PublicNetwork = None
        self._DeleteRouteTimestamp = None
        self._RemainingPartitions = None
        self._RemainingTopics = None
        self._DynamicDiskConfig = None

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
    def InstanceName(self):
        """Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def VipList(self):
        """VIP list information of access point
        :rtype: list of VipEntity
        """
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList

    @property
    def Vip(self):
        """Virtual IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Virtual port
        :rtype: str
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Status(self):
        """Instance status. 0: creating, 1: running, 2: deleting
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Bandwidth(self):
        """Instance bandwidth in Mbps
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def DiskSize(self):
        """Instance storage capacity in GB
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def ZoneId(self):
        """AZ
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        """VPC ID. If this parameter is empty, it means the basic network
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet ID. If this parameter is empty, it means the basic network
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Healthy(self):
        """Instance health status. 1: healthy, 2: alarmed, 3: exceptional
        :rtype: int
        """
        return self._Healthy

    @Healthy.setter
    def Healthy(self, Healthy):
        self._Healthy = Healthy

    @property
    def HealthyMessage(self):
        """Instance health information. Currently, the disk utilization is displayed with a maximum length of 256
        :rtype: str
        """
        return self._HealthyMessage

    @HealthyMessage.setter
    def HealthyMessage(self, HealthyMessage):
        self._HealthyMessage = HealthyMessage

    @property
    def CreateTime(self):
        """Creation time
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MsgRetentionTime(self):
        """Message retention period in minutes
        :rtype: int
        """
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def Config(self):
        """Configuration for automatic topic creation. If this field is empty, it means that automatic creation is not enabled
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceConfigDO`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def RemainderPartitions(self):
        """Number of remaining creatable partitions
        :rtype: int
        """
        return self._RemainderPartitions

    @RemainderPartitions.setter
    def RemainderPartitions(self, RemainderPartitions):
        self._RemainderPartitions = RemainderPartitions

    @property
    def RemainderTopics(self):
        """Number of remaining creatable topics
        :rtype: int
        """
        return self._RemainderTopics

    @RemainderTopics.setter
    def RemainderTopics(self, RemainderTopics):
        self._RemainderTopics = RemainderTopics

    @property
    def CreatedPartitions(self):
        """Number of partitions already created
        :rtype: int
        """
        return self._CreatedPartitions

    @CreatedPartitions.setter
    def CreatedPartitions(self, CreatedPartitions):
        self._CreatedPartitions = CreatedPartitions

    @property
    def CreatedTopics(self):
        """Number of topics already created
        :rtype: int
        """
        return self._CreatedTopics

    @CreatedTopics.setter
    def CreatedTopics(self, CreatedTopics):
        self._CreatedTopics = CreatedTopics

    @property
    def Tags(self):
        """Tag array
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ExpireTime(self):
        """Expiration time
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ZoneIds(self):
        """Cross-AZ
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Version(self):
        """Kafka version information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def MaxGroupNum(self):
        """Maximum number of groups
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxGroupNum

    @MaxGroupNum.setter
    def MaxGroupNum(self, MaxGroupNum):
        self._MaxGroupNum = MaxGroupNum

    @property
    def Cvm(self):
        """Offering type. `0`: Standard Edition; `1`: Professional Edition
Note: this field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Cvm

    @Cvm.setter
    def Cvm(self, Cvm):
        self._Cvm = Cvm

    @property
    def InstanceType(self):
        """Type.
Note: this field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Features(self):
        """Features supported by the instance. `FEATURE_SUBNET_ACL` indicates that the ACL policy supports setting subnets. 
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Features

    @Features.setter
    def Features(self, Features):
        self._Features = Features

    @property
    def RetentionTimeConfig(self):
        """Dynamic message retention policy
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        """
        return self._RetentionTimeConfig

    @RetentionTimeConfig.setter
    def RetentionTimeConfig(self, RetentionTimeConfig):
        self._RetentionTimeConfig = RetentionTimeConfig

    @property
    def MaxConnection(self):
        """Maximum number of connections
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxConnection

    @MaxConnection.setter
    def MaxConnection(self, MaxConnection):
        self._MaxConnection = MaxConnection

    @property
    def PublicNetwork(self):
        """Public network bandwidth
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def DeleteRouteTimestamp(self):
        """Time
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DeleteRouteTimestamp

    @DeleteRouteTimestamp.setter
    def DeleteRouteTimestamp(self, DeleteRouteTimestamp):
        self._DeleteRouteTimestamp = DeleteRouteTimestamp

    @property
    def RemainingPartitions(self):
        """Number of remaining creatable partitions
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RemainingPartitions

    @RemainingPartitions.setter
    def RemainingPartitions(self, RemainingPartitions):
        self._RemainingPartitions = RemainingPartitions

    @property
    def RemainingTopics(self):
        """Number of remaining creatable topics
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RemainingTopics

    @RemainingTopics.setter
    def RemainingTopics(self, RemainingTopics):
        self._RemainingTopics = RemainingTopics

    @property
    def DynamicDiskConfig(self):
        """Dynamic disk expansion policy.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DynamicDiskConfig`
        """
        return self._DynamicDiskConfig

    @DynamicDiskConfig.setter
    def DynamicDiskConfig(self, DynamicDiskConfig):
        self._DynamicDiskConfig = DynamicDiskConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        if params.get("VipList") is not None:
            self._VipList = []
            for item in params.get("VipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self._VipList.append(obj)
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._Status = params.get("Status")
        self._Bandwidth = params.get("Bandwidth")
        self._DiskSize = params.get("DiskSize")
        self._ZoneId = params.get("ZoneId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Healthy = params.get("Healthy")
        self._HealthyMessage = params.get("HealthyMessage")
        self._CreateTime = params.get("CreateTime")
        self._MsgRetentionTime = params.get("MsgRetentionTime")
        if params.get("Config") is not None:
            self._Config = InstanceConfigDO()
            self._Config._deserialize(params.get("Config"))
        self._RemainderPartitions = params.get("RemainderPartitions")
        self._RemainderTopics = params.get("RemainderTopics")
        self._CreatedPartitions = params.get("CreatedPartitions")
        self._CreatedTopics = params.get("CreatedTopics")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ExpireTime = params.get("ExpireTime")
        self._ZoneIds = params.get("ZoneIds")
        self._Version = params.get("Version")
        self._MaxGroupNum = params.get("MaxGroupNum")
        self._Cvm = params.get("Cvm")
        self._InstanceType = params.get("InstanceType")
        self._Features = params.get("Features")
        if params.get("RetentionTimeConfig") is not None:
            self._RetentionTimeConfig = DynamicRetentionTime()
            self._RetentionTimeConfig._deserialize(params.get("RetentionTimeConfig"))
        self._MaxConnection = params.get("MaxConnection")
        self._PublicNetwork = params.get("PublicNetwork")
        self._DeleteRouteTimestamp = params.get("DeleteRouteTimestamp")
        self._RemainingPartitions = params.get("RemainingPartitions")
        self._RemainingTopics = params.get("RemainingTopics")
        if params.get("DynamicDiskConfig") is not None:
            self._DynamicDiskConfig = DynamicDiskConfig()
            self._DynamicDiskConfig._deserialize(params.get("DynamicDiskConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargeParam(AbstractModel):
    """Instance billing parameters

    """

    def __init__(self):
        r"""
        :param _InstanceChargeType: Instance billing mode (`PREPAID`: Monthly subscription; `POSTPAID_BY_HOUR`: Pay-as-you-go)
        :type InstanceChargeType: str
        :param _InstanceChargePeriod: Validity period, which is only required for the monthly subscription billing mode
        :type InstanceChargePeriod: int
        """
        self._InstanceChargeType = None
        self._InstanceChargePeriod = None

    @property
    def InstanceChargeType(self):
        """Instance billing mode (`PREPAID`: Monthly subscription; `POSTPAID_BY_HOUR`: Pay-as-you-go)
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePeriod(self):
        """Validity period, which is only required for the monthly subscription billing mode
        :rtype: int
        """
        return self._InstanceChargePeriod

    @InstanceChargePeriod.setter
    def InstanceChargePeriod(self, InstanceChargePeriod):
        self._InstanceChargePeriod = InstanceChargePeriod


    def _deserialize(self, params):
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._InstanceChargePeriod = params.get("InstanceChargePeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfigDO(AbstractModel):
    """Instance configuration entity

    """

    def __init__(self):
        r"""
        :param _AutoCreateTopicsEnable: Whether to create topics automatically
        :type AutoCreateTopicsEnable: bool
        :param _DefaultNumPartitions: Number of partitions
        :type DefaultNumPartitions: int
        :param _DefaultReplicationFactor: Default replication factor
        :type DefaultReplicationFactor: int
        """
        self._AutoCreateTopicsEnable = None
        self._DefaultNumPartitions = None
        self._DefaultReplicationFactor = None

    @property
    def AutoCreateTopicsEnable(self):
        """Whether to create topics automatically
        :rtype: bool
        """
        return self._AutoCreateTopicsEnable

    @AutoCreateTopicsEnable.setter
    def AutoCreateTopicsEnable(self, AutoCreateTopicsEnable):
        self._AutoCreateTopicsEnable = AutoCreateTopicsEnable

    @property
    def DefaultNumPartitions(self):
        """Number of partitions
        :rtype: int
        """
        return self._DefaultNumPartitions

    @DefaultNumPartitions.setter
    def DefaultNumPartitions(self, DefaultNumPartitions):
        self._DefaultNumPartitions = DefaultNumPartitions

    @property
    def DefaultReplicationFactor(self):
        """Default replication factor
        :rtype: int
        """
        return self._DefaultReplicationFactor

    @DefaultReplicationFactor.setter
    def DefaultReplicationFactor(self, DefaultReplicationFactor):
        self._DefaultReplicationFactor = DefaultReplicationFactor


    def _deserialize(self, params):
        self._AutoCreateTopicsEnable = params.get("AutoCreateTopicsEnable")
        self._DefaultNumPartitions = params.get("DefaultNumPartitions")
        self._DefaultReplicationFactor = params.get("DefaultReplicationFactor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetail(AbstractModel):
    """Instance details

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _Vip: Instance VIP information
        :type Vip: str
        :param _Vport: Instance port information
        :type Vport: str
        :param _VipList: Virtual IP list
        :type VipList: list of VipEntity
        :param _Status: Instance status. 0: creating, 1: running, 2: deleting, 5: isolated, -1: creation failed
        :type Status: int
        :param _Bandwidth: Instance bandwidth in Mbps
        :type Bandwidth: int
        :param _DiskSize: Instance storage capacity in GB
        :type DiskSize: int
        :param _ZoneId: AZ ID
        :type ZoneId: int
        :param _VpcId: vpcId. If this parameter is empty, it means the basic network
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _RenewFlag: Whether to renew the instance automatically, which is an int-type enumerated value. 1: yes, 2: no
        :type RenewFlag: int
        :param _Healthy: Instance status. An int-type value will be returned. `0`: Healthy, `1`: Alarmed, `2`: Exceptional
        :type Healthy: int
        :param _HealthyMessage: Instance status information
        :type HealthyMessage: str
        :param _CreateTime: Instance creation time
        :type CreateTime: int
        :param _ExpireTime: Instance expiration time
        :type ExpireTime: int
        :param _IsInternal: Whether it is an internal customer. 1: yes
        :type IsInternal: int
        :param _TopicNum: Number of topics
        :type TopicNum: int
        :param _Tags: Tag
        :type Tags: list of Tag
        :param _Version: Kafka version information
Note: this field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param _ZoneIds: Cross-AZ
Note: this field may return null, indicating that no valid values can be obtained.
        :type ZoneIds: list of int
        :param _Cvm: CKafka sale type
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cvm: int
        :param _InstanceType: CKafka instance type
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param _DiskType: Disk type
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type DiskType: str
        :param _MaxTopicNumber: Maximum number of topics for the current instance
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type MaxTopicNumber: int
        :param _MaxPartitionNumber: Maximum number of partitions for the current instance
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type MaxPartitionNumber: int
        :param _RebalanceTime: Time of scheduled upgrade
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type RebalanceTime: str
        :param _PartitionNumber: Number of partitions in the current instance.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PartitionNumber: int
        :param _PublicNetworkChargeType: Public network bandwidth type.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PublicNetworkChargeType: str
        :param _PublicNetwork: Public network bandwidth.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PublicNetwork: int
        :param _ClusterType: Instance type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterType: str
        :param _Features: Instance feature list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Features: list of str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Vip = None
        self._Vport = None
        self._VipList = None
        self._Status = None
        self._Bandwidth = None
        self._DiskSize = None
        self._ZoneId = None
        self._VpcId = None
        self._SubnetId = None
        self._RenewFlag = None
        self._Healthy = None
        self._HealthyMessage = None
        self._CreateTime = None
        self._ExpireTime = None
        self._IsInternal = None
        self._TopicNum = None
        self._Tags = None
        self._Version = None
        self._ZoneIds = None
        self._Cvm = None
        self._InstanceType = None
        self._DiskType = None
        self._MaxTopicNumber = None
        self._MaxPartitionNumber = None
        self._RebalanceTime = None
        self._PartitionNumber = None
        self._PublicNetworkChargeType = None
        self._PublicNetwork = None
        self._ClusterType = None
        self._Features = None

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
    def InstanceName(self):
        """Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Vip(self):
        """Instance VIP information
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Instance port information
        :rtype: str
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VipList(self):
        """Virtual IP list
        :rtype: list of VipEntity
        """
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList

    @property
    def Status(self):
        """Instance status. 0: creating, 1: running, 2: deleting, 5: isolated, -1: creation failed
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Bandwidth(self):
        """Instance bandwidth in Mbps
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def DiskSize(self):
        """Instance storage capacity in GB
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def ZoneId(self):
        """AZ ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        """vpcId. If this parameter is empty, it means the basic network
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

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
    def RenewFlag(self):
        """Whether to renew the instance automatically, which is an int-type enumerated value. 1: yes, 2: no
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Healthy(self):
        """Instance status. An int-type value will be returned. `0`: Healthy, `1`: Alarmed, `2`: Exceptional
        :rtype: int
        """
        return self._Healthy

    @Healthy.setter
    def Healthy(self, Healthy):
        self._Healthy = Healthy

    @property
    def HealthyMessage(self):
        """Instance status information
        :rtype: str
        """
        return self._HealthyMessage

    @HealthyMessage.setter
    def HealthyMessage(self, HealthyMessage):
        self._HealthyMessage = HealthyMessage

    @property
    def CreateTime(self):
        """Instance creation time
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        """Instance expiration time
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def IsInternal(self):
        """Whether it is an internal customer. 1: yes
        :rtype: int
        """
        return self._IsInternal

    @IsInternal.setter
    def IsInternal(self, IsInternal):
        self._IsInternal = IsInternal

    @property
    def TopicNum(self):
        """Number of topics
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

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
    def Version(self):
        """Kafka version information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ZoneIds(self):
        """Cross-AZ
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Cvm(self):
        """CKafka sale type
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Cvm

    @Cvm.setter
    def Cvm(self, Cvm):
        self._Cvm = Cvm

    @property
    def InstanceType(self):
        """CKafka instance type
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DiskType(self):
        """Disk type
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def MaxTopicNumber(self):
        """Maximum number of topics for the current instance
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxTopicNumber

    @MaxTopicNumber.setter
    def MaxTopicNumber(self, MaxTopicNumber):
        self._MaxTopicNumber = MaxTopicNumber

    @property
    def MaxPartitionNumber(self):
        """Maximum number of partitions for the current instance
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxPartitionNumber

    @MaxPartitionNumber.setter
    def MaxPartitionNumber(self, MaxPartitionNumber):
        self._MaxPartitionNumber = MaxPartitionNumber

    @property
    def RebalanceTime(self):
        """Time of scheduled upgrade
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RebalanceTime

    @RebalanceTime.setter
    def RebalanceTime(self, RebalanceTime):
        self._RebalanceTime = RebalanceTime

    @property
    def PartitionNumber(self):
        """Number of partitions in the current instance.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PartitionNumber

    @PartitionNumber.setter
    def PartitionNumber(self, PartitionNumber):
        self._PartitionNumber = PartitionNumber

    @property
    def PublicNetworkChargeType(self):
        """Public network bandwidth type.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PublicNetworkChargeType

    @PublicNetworkChargeType.setter
    def PublicNetworkChargeType(self, PublicNetworkChargeType):
        self._PublicNetworkChargeType = PublicNetworkChargeType

    @property
    def PublicNetwork(self):
        """Public network bandwidth.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def ClusterType(self):
        """Instance type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def Features(self):
        """Instance feature list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Features

    @Features.setter
    def Features(self, Features):
        self._Features = Features


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        if params.get("VipList") is not None:
            self._VipList = []
            for item in params.get("VipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self._VipList.append(obj)
        self._Status = params.get("Status")
        self._Bandwidth = params.get("Bandwidth")
        self._DiskSize = params.get("DiskSize")
        self._ZoneId = params.get("ZoneId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._RenewFlag = params.get("RenewFlag")
        self._Healthy = params.get("Healthy")
        self._HealthyMessage = params.get("HealthyMessage")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._IsInternal = params.get("IsInternal")
        self._TopicNum = params.get("TopicNum")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Version = params.get("Version")
        self._ZoneIds = params.get("ZoneIds")
        self._Cvm = params.get("Cvm")
        self._InstanceType = params.get("InstanceType")
        self._DiskType = params.get("DiskType")
        self._MaxTopicNumber = params.get("MaxTopicNumber")
        self._MaxPartitionNumber = params.get("MaxPartitionNumber")
        self._RebalanceTime = params.get("RebalanceTime")
        self._PartitionNumber = params.get("PartitionNumber")
        self._PublicNetworkChargeType = params.get("PublicNetworkChargeType")
        self._PublicNetwork = params.get("PublicNetwork")
        self._ClusterType = params.get("ClusterType")
        self._Features = params.get("Features")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetailResponse(AbstractModel):
    """Returned result of instance details

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of eligible instances
        :type TotalCount: int
        :param _InstanceList: List of eligible instance details
        :type InstanceList: list of InstanceDetail
        """
        self._TotalCount = None
        self._InstanceList = None

    @property
    def TotalCount(self):
        """Total number of eligible instances
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        """List of eligible instance details
        :rtype: list of InstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceQuotaConfigResp(AbstractModel):
    """Traffic throttling policy in instance/topic dimension

    """

    def __init__(self):
        r"""
        :param _QuotaProducerByteRate: Production throttling in MB/sec.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type QuotaProducerByteRate: int
        :param _QuotaConsumerByteRate: Consumption throttling in MB/sec.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type QuotaConsumerByteRate: int
        """
        self._QuotaProducerByteRate = None
        self._QuotaConsumerByteRate = None

    @property
    def QuotaProducerByteRate(self):
        """Production throttling in MB/sec.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._QuotaProducerByteRate

    @QuotaProducerByteRate.setter
    def QuotaProducerByteRate(self, QuotaProducerByteRate):
        self._QuotaProducerByteRate = QuotaProducerByteRate

    @property
    def QuotaConsumerByteRate(self):
        """Consumption throttling in MB/sec.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._QuotaConsumerByteRate

    @QuotaConsumerByteRate.setter
    def QuotaConsumerByteRate(self, QuotaConsumerByteRate):
        self._QuotaConsumerByteRate = QuotaConsumerByteRate


    def _deserialize(self, params):
        self._QuotaProducerByteRate = params.get("QuotaProducerByteRate")
        self._QuotaConsumerByteRate = params.get("QuotaConsumerByteRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceResponse(AbstractModel):
    """Aggregated returned result of instance status

    """

    def __init__(self):
        r"""
        :param _InstanceList: List of eligible instances
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceList: list of Instance
        :param _TotalCount: Total number of eligible results
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        """
        self._InstanceList = None
        self._TotalCount = None

    @property
    def InstanceList(self):
        """List of eligible instances
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Instance
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """Total number of eligible results
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = Instance()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JgwOperateResponse(AbstractModel):
    """Returned result value of operation

    """

    def __init__(self):
        r"""
        :param _ReturnCode: Returned code. 0: normal, other values: error
        :type ReturnCode: str
        :param _ReturnMessage: Success message
        :type ReturnMessage: str
        :param _Data: Data returned by an operation, which may contain `flowId`, etc.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.ckafka.v20190819.models.OperateResponseData`
        """
        self._ReturnCode = None
        self._ReturnMessage = None
        self._Data = None

    @property
    def ReturnCode(self):
        """Returned code. 0: normal, other values: error
        :rtype: str
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMessage(self):
        """Success message
        :rtype: str
        """
        return self._ReturnMessage

    @ReturnMessage.setter
    def ReturnMessage(self, ReturnMessage):
        self._ReturnMessage = ReturnMessage

    @property
    def Data(self):
        """Data returned by an operation, which may contain `flowId`, etc.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.OperateResponseData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMessage = params.get("ReturnMessage")
        if params.get("Data") is not None:
            self._Data = OperateResponseData()
            self._Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAclRuleRequest(AbstractModel):
    """ModifyAclRule request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _RuleName: ACL policy name
        :type RuleName: str
        :param _IsApplied: Whether to be applied to new topics
        :type IsApplied: int
        """
        self._InstanceId = None
        self._RuleName = None
        self._IsApplied = None

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
    def RuleName(self):
        """ACL policy name
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def IsApplied(self):
        """Whether to be applied to new topics
        :rtype: int
        """
        return self._IsApplied

    @IsApplied.setter
    def IsApplied(self, IsApplied):
        self._IsApplied = IsApplied


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RuleName = params.get("RuleName")
        self._IsApplied = params.get("IsApplied")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAclRuleResponse(AbstractModel):
    """ModifyAclRule response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Unique key of a rule
        :type Result: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Unique key of a rule
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyDatahubTopicRequest(AbstractModel):
    """ModifyDatahubTopic request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Name
        :type Name: str
        :param _RetentionMs: Message retention period in ms. The current minimum value is 60,000 ms.
        :type RetentionMs: int
        :param _Note: Topic remarks, which are a string of up to 64 characters. It can contain letters, digits, and hyphens (-) and must start with a letter.
        :type Note: str
        :param _Tags: Tag list
        :type Tags: list of Tag
        """
        self._Name = None
        self._RetentionMs = None
        self._Note = None
        self._Tags = None

    @property
    def Name(self):
        """Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RetentionMs(self):
        """Message retention period in ms. The current minimum value is 60,000 ms.
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def Note(self):
        """Topic remarks, which are a string of up to 64 characters. It can contain letters, digits, and hyphens (-) and must start with a letter.
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Tags(self):
        """Tag list
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._RetentionMs = params.get("RetentionMs")
        self._Note = params.get("Note")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatahubTopicResponse(AbstractModel):
    """ModifyDatahubTopic response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result set
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result set
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyGroupOffsetsRequest(AbstractModel):
    """ModifyGroupOffsets request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Kafka instance ID
        :type InstanceId: str
        :param _Group: Kafka consumer group
        :type Group: str
        :param _Strategy: Offset resetting policy. Meanings of the input parameters: 0: equivalent to the `shift-by` parameter, which indicates to shift the offset forward or backward by the value of the `shift`. 1: equivalent to `by-duration`, `to-datetime`, `to-earliest`, or `to-latest`, which indicates to move the offset to the specified timestamp. 2: equivalent to `to-offset`, which indicates to move the offset to the specified offset position
        :type Strategy: int
        :param _Topics: Indicates the topics to be reset. If this parameter is left empty, all topics will be reset
        :type Topics: list of str
        :param _Shift: When `strategy` is 0, this field is required. If it is above zero, the offset will be shifted backward by the value of the `shift`. If it is below zero, the offset will be shifted forward by the value of the `shift`. After a correct reset, the new offset should be (old_offset + shift). Note that if the new offset is smaller than the `earliest` parameter of the partition, it will be set to `earliest`, and if it is greater than the `latest` parameter of the partition, it will be set to `latest`
        :type Shift: int
        :param _ShiftTimestamp: Unit: ms. When `strategy` is 1, this field is required, where -2 indicates to reset the offset to the initial position, -1 indicates to reset to the latest position (equivalent to emptying), and other values represent the specified time, i.e., the offset of the topic at the specified time will be obtained and then reset. Note that if there is no message at the specified time, the last offset will be obtained
        :type ShiftTimestamp: int
        :param _Offset: Position of the offset that needs to be reset. When `strategy` is 2, this field is required
        :type Offset: int
        :param _Partitions: List of partitions that need to be reset. If the topics parameter is not specified, reset partitions in the corresponding partition list of all topics. If the topics parameter is specified, reset partitions of the corresponding partition list of the specified topic list.
        :type Partitions: list of int
        """
        self._InstanceId = None
        self._Group = None
        self._Strategy = None
        self._Topics = None
        self._Shift = None
        self._ShiftTimestamp = None
        self._Offset = None
        self._Partitions = None

    @property
    def InstanceId(self):
        """Kafka instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Group(self):
        """Kafka consumer group
        :rtype: str
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Strategy(self):
        """Offset resetting policy. Meanings of the input parameters: 0: equivalent to the `shift-by` parameter, which indicates to shift the offset forward or backward by the value of the `shift`. 1: equivalent to `by-duration`, `to-datetime`, `to-earliest`, or `to-latest`, which indicates to move the offset to the specified timestamp. 2: equivalent to `to-offset`, which indicates to move the offset to the specified offset position
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Topics(self):
        """Indicates the topics to be reset. If this parameter is left empty, all topics will be reset
        :rtype: list of str
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def Shift(self):
        """When `strategy` is 0, this field is required. If it is above zero, the offset will be shifted backward by the value of the `shift`. If it is below zero, the offset will be shifted forward by the value of the `shift`. After a correct reset, the new offset should be (old_offset + shift). Note that if the new offset is smaller than the `earliest` parameter of the partition, it will be set to `earliest`, and if it is greater than the `latest` parameter of the partition, it will be set to `latest`
        :rtype: int
        """
        return self._Shift

    @Shift.setter
    def Shift(self, Shift):
        self._Shift = Shift

    @property
    def ShiftTimestamp(self):
        """Unit: ms. When `strategy` is 1, this field is required, where -2 indicates to reset the offset to the initial position, -1 indicates to reset to the latest position (equivalent to emptying), and other values represent the specified time, i.e., the offset of the topic at the specified time will be obtained and then reset. Note that if there is no message at the specified time, the last offset will be obtained
        :rtype: int
        """
        return self._ShiftTimestamp

    @ShiftTimestamp.setter
    def ShiftTimestamp(self, ShiftTimestamp):
        self._ShiftTimestamp = ShiftTimestamp

    @property
    def Offset(self):
        """Position of the offset that needs to be reset. When `strategy` is 2, this field is required
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Partitions(self):
        """List of partitions that need to be reset. If the topics parameter is not specified, reset partitions in the corresponding partition list of all topics. If the topics parameter is specified, reset partitions of the corresponding partition list of the specified topic list.
        :rtype: list of int
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Group = params.get("Group")
        self._Strategy = params.get("Strategy")
        self._Topics = params.get("Topics")
        self._Shift = params.get("Shift")
        self._ShiftTimestamp = params.get("ShiftTimestamp")
        self._Offset = params.get("Offset")
        self._Partitions = params.get("Partitions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupOffsetsResponse(AbstractModel):
    """ModifyGroupOffsets response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyInstanceAttributesConfig(AbstractModel):
    """Configuration object for modifying instance attributes

    """

    def __init__(self):
        r"""
        :param _AutoCreateTopicEnable: Automatic creation. true: enabled, false: not enabled
        :type AutoCreateTopicEnable: bool
        :param _DefaultNumPartitions: Optional. If `auto.create.topic.enable` is set to `true` and this value is not set, 3 will be used by default
        :type DefaultNumPartitions: int
        :param _DefaultReplicationFactor: If `auto.create.topic.enable` is set to `true` but this value is not set, 2 will be used by default
        :type DefaultReplicationFactor: int
        """
        self._AutoCreateTopicEnable = None
        self._DefaultNumPartitions = None
        self._DefaultReplicationFactor = None

    @property
    def AutoCreateTopicEnable(self):
        """Automatic creation. true: enabled, false: not enabled
        :rtype: bool
        """
        return self._AutoCreateTopicEnable

    @AutoCreateTopicEnable.setter
    def AutoCreateTopicEnable(self, AutoCreateTopicEnable):
        self._AutoCreateTopicEnable = AutoCreateTopicEnable

    @property
    def DefaultNumPartitions(self):
        """Optional. If `auto.create.topic.enable` is set to `true` and this value is not set, 3 will be used by default
        :rtype: int
        """
        return self._DefaultNumPartitions

    @DefaultNumPartitions.setter
    def DefaultNumPartitions(self, DefaultNumPartitions):
        self._DefaultNumPartitions = DefaultNumPartitions

    @property
    def DefaultReplicationFactor(self):
        """If `auto.create.topic.enable` is set to `true` but this value is not set, 2 will be used by default
        :rtype: int
        """
        return self._DefaultReplicationFactor

    @DefaultReplicationFactor.setter
    def DefaultReplicationFactor(self, DefaultReplicationFactor):
        self._DefaultReplicationFactor = DefaultReplicationFactor


    def _deserialize(self, params):
        self._AutoCreateTopicEnable = params.get("AutoCreateTopicEnable")
        self._DefaultNumPartitions = params.get("DefaultNumPartitions")
        self._DefaultReplicationFactor = params.get("DefaultReplicationFactor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAttributesRequest(AbstractModel):
    """ModifyInstanceAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _MsgRetentionTime: Maximum retention period in minutes for instance log, which can be up to 30 days. 0 indicates not to enable the log retention period policy
        :type MsgRetentionTime: int
        :param _InstanceName: Instance name string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)
        :type InstanceName: str
        :param _Config: Instance configuration
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesConfig`
        :param _DynamicRetentionConfig: Dynamic message retention policy configuration
        :type DynamicRetentionConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        :param _RebalanceTime: Modification of the rebalancing time after upgrade
        :type RebalanceTime: int
        :param _PublicNetwork: Public network bandwidth
        :type PublicNetwork: int
        :param _DynamicDiskConfig: Dynamic disk expansion policy configuration.
        :type DynamicDiskConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicDiskConfig`
        :param _MaxMessageByte: The size of a single message in bytes at the instance level.
        :type MaxMessageByte: int
        """
        self._InstanceId = None
        self._MsgRetentionTime = None
        self._InstanceName = None
        self._Config = None
        self._DynamicRetentionConfig = None
        self._RebalanceTime = None
        self._PublicNetwork = None
        self._DynamicDiskConfig = None
        self._MaxMessageByte = None

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
    def MsgRetentionTime(self):
        """Maximum retention period in minutes for instance log, which can be up to 30 days. 0 indicates not to enable the log retention period policy
        :rtype: int
        """
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def InstanceName(self):
        """Instance name string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Config(self):
        """Instance configuration
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def DynamicRetentionConfig(self):
        """Dynamic message retention policy configuration
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        """
        return self._DynamicRetentionConfig

    @DynamicRetentionConfig.setter
    def DynamicRetentionConfig(self, DynamicRetentionConfig):
        self._DynamicRetentionConfig = DynamicRetentionConfig

    @property
    def RebalanceTime(self):
        """Modification of the rebalancing time after upgrade
        :rtype: int
        """
        return self._RebalanceTime

    @RebalanceTime.setter
    def RebalanceTime(self, RebalanceTime):
        self._RebalanceTime = RebalanceTime

    @property
    def PublicNetwork(self):
        """Public network bandwidth
        :rtype: int
        """
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def DynamicDiskConfig(self):
        """Dynamic disk expansion policy configuration.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DynamicDiskConfig`
        """
        return self._DynamicDiskConfig

    @DynamicDiskConfig.setter
    def DynamicDiskConfig(self, DynamicDiskConfig):
        self._DynamicDiskConfig = DynamicDiskConfig

    @property
    def MaxMessageByte(self):
        """The size of a single message in bytes at the instance level.
        :rtype: int
        """
        return self._MaxMessageByte

    @MaxMessageByte.setter
    def MaxMessageByte(self, MaxMessageByte):
        self._MaxMessageByte = MaxMessageByte


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MsgRetentionTime = params.get("MsgRetentionTime")
        self._InstanceName = params.get("InstanceName")
        if params.get("Config") is not None:
            self._Config = ModifyInstanceAttributesConfig()
            self._Config._deserialize(params.get("Config"))
        if params.get("DynamicRetentionConfig") is not None:
            self._DynamicRetentionConfig = DynamicRetentionTime()
            self._DynamicRetentionConfig._deserialize(params.get("DynamicRetentionConfig"))
        self._RebalanceTime = params.get("RebalanceTime")
        self._PublicNetwork = params.get("PublicNetwork")
        if params.get("DynamicDiskConfig") is not None:
            self._DynamicDiskConfig = DynamicDiskConfig()
            self._DynamicDiskConfig._deserialize(params.get("DynamicDiskConfig"))
        self._MaxMessageByte = params.get("MaxMessageByte")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAttributesResponse(AbstractModel):
    """ModifyInstanceAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyInstancePreRequest(AbstractModel):
    """ModifyInstancePre request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance name.
        :type InstanceId: str
        :param _DiskSize: Estimated disk capacity, which can be increased by increment.
        :type DiskSize: int
        :param _BandWidth: Estimated bandwidth, which can be increased by increment.
        :type BandWidth: int
        :param _Partition: Estimated partition count, which can be increased by increment.
        :type Partition: int
        """
        self._InstanceId = None
        self._DiskSize = None
        self._BandWidth = None
        self._Partition = None

    @property
    def InstanceId(self):
        """Instance name.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DiskSize(self):
        """Estimated disk capacity, which can be increased by increment.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def BandWidth(self):
        """Estimated bandwidth, which can be increased by increment.
        :rtype: int
        """
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def Partition(self):
        """Estimated partition count, which can be increased by increment.
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DiskSize = params.get("DiskSize")
        self._BandWidth = params.get("BandWidth")
        self._Partition = params.get("Partition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancePreResponse(AbstractModel):
    """ModifyInstancePre response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Response structure of modifying the configurations of a prepaid instance.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Response structure of modifying the configurations of a prepaid instance.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CreateInstancePreResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyPasswordRequest(AbstractModel):
    """ModifyPassword request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Name: Username
        :type Name: str
        :param _Password: Current user password
        :type Password: str
        :param _PasswordNew: New user password
        :type PasswordNew: str
        """
        self._InstanceId = None
        self._Name = None
        self._Password = None
        self._PasswordNew = None

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
    def Name(self):
        """Username
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Password(self):
        """Current user password
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def PasswordNew(self):
        """New user password
        :rtype: str
        """
        return self._PasswordNew

    @PasswordNew.setter
    def PasswordNew(self, PasswordNew):
        self._PasswordNew = PasswordNew


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Password = params.get("Password")
        self._PasswordNew = params.get("PasswordNew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPasswordResponse(AbstractModel):
    """ModifyPassword response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyTopicAttributesRequest(AbstractModel):
    """ModifyTopicAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _TopicName: Topic name.
        :type TopicName: str
        :param _Note: Topic remarks string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type Note: str
        :param _EnableWhiteList: IP allowlist switch. 1: enabled, 0: disabled.
        :type EnableWhiteList: int
        :param _MinInsyncReplicas: Default value: 1.
        :type MinInsyncReplicas: int
        :param _UncleanLeaderElectionEnable: 0: false, 1: true. Default value: 0.
        :type UncleanLeaderElectionEnable: int
        :param _RetentionMs: Message retention period in ms. The current minimum value is 60,000 ms.
        :type RetentionMs: int
        :param _SegmentMs: Segment rolling duration in ms. The current minimum value is 86,400,000 ms.
        :type SegmentMs: int
        :param _MaxMessageBytes: Max message size in bytes. Max value: 8,388,608 bytes (8 MB).
        :type MaxMessageBytes: int
        :param _CleanUpPolicy: Message deletion policy. Valid values: delete, compact
        :type CleanUpPolicy: str
        :param _IpWhiteList: IP allowlist, which is required if the value of `enableWhileList` is 1.
        :type IpWhiteList: list of str
        :param _EnableAclRule: Preset ACL rule. `1`: enable, `0`: disable. Default value: `0`.
        :type EnableAclRule: int
        :param _AclRuleName: Name of the preset ACL rule.
        :type AclRuleName: str
        :param _RetentionBytes: Message retention file size in bytes, which is an optional parameter. Default value: -1. Currently, the min value that can be entered is 1,048,576 B.
        :type RetentionBytes: int
        :param _Tags: Tag list.
        :type Tags: list of Tag
        :param _QuotaProducerByteRate: Production throttling in MB/sec.
        :type QuotaProducerByteRate: int
        :param _QuotaConsumerByteRate: Consumption throttling in MB/sec.
        :type QuotaConsumerByteRate: int
        :param _ReplicaNum: The number of topic replicas.
        :type ReplicaNum: int
        """
        self._InstanceId = None
        self._TopicName = None
        self._Note = None
        self._EnableWhiteList = None
        self._MinInsyncReplicas = None
        self._UncleanLeaderElectionEnable = None
        self._RetentionMs = None
        self._SegmentMs = None
        self._MaxMessageBytes = None
        self._CleanUpPolicy = None
        self._IpWhiteList = None
        self._EnableAclRule = None
        self._AclRuleName = None
        self._RetentionBytes = None
        self._Tags = None
        self._QuotaProducerByteRate = None
        self._QuotaConsumerByteRate = None
        self._ReplicaNum = None

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
    def TopicName(self):
        """Topic name.
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Note(self):
        """Topic remarks string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def EnableWhiteList(self):
        """IP allowlist switch. 1: enabled, 0: disabled.
        :rtype: int
        """
        return self._EnableWhiteList

    @EnableWhiteList.setter
    def EnableWhiteList(self, EnableWhiteList):
        self._EnableWhiteList = EnableWhiteList

    @property
    def MinInsyncReplicas(self):
        """Default value: 1.
        :rtype: int
        """
        return self._MinInsyncReplicas

    @MinInsyncReplicas.setter
    def MinInsyncReplicas(self, MinInsyncReplicas):
        self._MinInsyncReplicas = MinInsyncReplicas

    @property
    def UncleanLeaderElectionEnable(self):
        """0: false, 1: true. Default value: 0.
        :rtype: int
        """
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def RetentionMs(self):
        """Message retention period in ms. The current minimum value is 60,000 ms.
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def SegmentMs(self):
        """Segment rolling duration in ms. The current minimum value is 86,400,000 ms.
        :rtype: int
        """
        return self._SegmentMs

    @SegmentMs.setter
    def SegmentMs(self, SegmentMs):
        self._SegmentMs = SegmentMs

    @property
    def MaxMessageBytes(self):
        """Max message size in bytes. Max value: 8,388,608 bytes (8 MB).
        :rtype: int
        """
        return self._MaxMessageBytes

    @MaxMessageBytes.setter
    def MaxMessageBytes(self, MaxMessageBytes):
        self._MaxMessageBytes = MaxMessageBytes

    @property
    def CleanUpPolicy(self):
        """Message deletion policy. Valid values: delete, compact
        :rtype: str
        """
        return self._CleanUpPolicy

    @CleanUpPolicy.setter
    def CleanUpPolicy(self, CleanUpPolicy):
        self._CleanUpPolicy = CleanUpPolicy

    @property
    def IpWhiteList(self):
        """IP allowlist, which is required if the value of `enableWhileList` is 1.
        :rtype: list of str
        """
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList

    @property
    def EnableAclRule(self):
        """Preset ACL rule. `1`: enable, `0`: disable. Default value: `0`.
        :rtype: int
        """
        return self._EnableAclRule

    @EnableAclRule.setter
    def EnableAclRule(self, EnableAclRule):
        self._EnableAclRule = EnableAclRule

    @property
    def AclRuleName(self):
        """Name of the preset ACL rule.
        :rtype: str
        """
        return self._AclRuleName

    @AclRuleName.setter
    def AclRuleName(self, AclRuleName):
        self._AclRuleName = AclRuleName

    @property
    def RetentionBytes(self):
        """Message retention file size in bytes, which is an optional parameter. Default value: -1. Currently, the min value that can be entered is 1,048,576 B.
        :rtype: int
        """
        return self._RetentionBytes

    @RetentionBytes.setter
    def RetentionBytes(self, RetentionBytes):
        self._RetentionBytes = RetentionBytes

    @property
    def Tags(self):
        """Tag list.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def QuotaProducerByteRate(self):
        """Production throttling in MB/sec.
        :rtype: int
        """
        return self._QuotaProducerByteRate

    @QuotaProducerByteRate.setter
    def QuotaProducerByteRate(self, QuotaProducerByteRate):
        self._QuotaProducerByteRate = QuotaProducerByteRate

    @property
    def QuotaConsumerByteRate(self):
        """Consumption throttling in MB/sec.
        :rtype: int
        """
        return self._QuotaConsumerByteRate

    @QuotaConsumerByteRate.setter
    def QuotaConsumerByteRate(self, QuotaConsumerByteRate):
        self._QuotaConsumerByteRate = QuotaConsumerByteRate

    @property
    def ReplicaNum(self):
        """The number of topic replicas.
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._Note = params.get("Note")
        self._EnableWhiteList = params.get("EnableWhiteList")
        self._MinInsyncReplicas = params.get("MinInsyncReplicas")
        self._UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self._RetentionMs = params.get("RetentionMs")
        self._SegmentMs = params.get("SegmentMs")
        self._MaxMessageBytes = params.get("MaxMessageBytes")
        self._CleanUpPolicy = params.get("CleanUpPolicy")
        self._IpWhiteList = params.get("IpWhiteList")
        self._EnableAclRule = params.get("EnableAclRule")
        self._AclRuleName = params.get("AclRuleName")
        self._RetentionBytes = params.get("RetentionBytes")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._QuotaProducerByteRate = params.get("QuotaProducerByteRate")
        self._QuotaConsumerByteRate = params.get("QuotaConsumerByteRate")
        self._ReplicaNum = params.get("ReplicaNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicAttributesResponse(AbstractModel):
    """ModifyTopicAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result set
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result set
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class OperateResponseData(AbstractModel):
    """Data structure returned by operation

    """

    def __init__(self):
        r"""
        :param _FlowId: FlowId11
Note: this field may return null, indicating that no valid values can be obtained.
        :type FlowId: int
        :param _RouteDTO: RouteIdDto Note: This field may return null, indicating that no valid values can be obtained.
        :type RouteDTO: :class:`tencentcloud.ckafka.v20190819.models.RouteDTO`
        """
        self._FlowId = None
        self._RouteDTO = None

    @property
    def FlowId(self):
        """FlowId11
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RouteDTO(self):
        """RouteIdDto Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.RouteDTO`
        """
        return self._RouteDTO

    @RouteDTO.setter
    def RouteDTO(self, RouteDTO):
        self._RouteDTO = RouteDTO


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("RouteDTO") is not None:
            self._RouteDTO = RouteDTO()
            self._RouteDTO._deserialize(params.get("RouteDTO"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Partition(AbstractModel):
    """Partition entity

    """

    def __init__(self):
        r"""
        :param _PartitionId: Partition ID
        :type PartitionId: int
        """
        self._PartitionId = None

    @property
    def PartitionId(self):
        """Partition ID
        :rtype: int
        """
        return self._PartitionId

    @PartitionId.setter
    def PartitionId(self, PartitionId):
        self._PartitionId = PartitionId


    def _deserialize(self, params):
        self._PartitionId = params.get("PartitionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartitionOffset(AbstractModel):
    """Partition and offset

    """

    def __init__(self):
        r"""
        :param _Partition: Partition, such as "0" or "1"
Note: this field may return null, indicating that no valid values can be obtained.
        :type Partition: str
        :param _Offset: Offset, such as 100
Note: this field may return null, indicating that no valid values can be obtained.
        :type Offset: int
        """
        self._Partition = None
        self._Offset = None

    @property
    def Partition(self):
        """Partition, such as "0" or "1"
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        """Offset, such as 100
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Partition = params.get("Partition")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Partitions(AbstractModel):
    """Partition information

    """

    def __init__(self):
        r"""
        :param _Partition: Partition.
        :type Partition: int
        :param _Offset: Partition consumption offset.
        :type Offset: int
        """
        self._Partition = None
        self._Offset = None

    @property
    def Partition(self):
        """Partition.
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        """Partition consumption offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Partition = params.get("Partition")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """Message price entity

    """

    def __init__(self):
        r"""
        :param _RealTotalCost: Discounted price
        :type RealTotalCost: float
        :param _TotalCost: Original price
        :type TotalCost: float
        """
        self._RealTotalCost = None
        self._TotalCost = None

    @property
    def RealTotalCost(self):
        """Discounted price
        :rtype: float
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def TotalCost(self):
        """Original price
        :rtype: float
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._RealTotalCost = params.get("RealTotalCost")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Region(AbstractModel):
    """Region entity object

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID
        :type RegionId: int
        :param _RegionName: Region name
        :type RegionName: str
        :param _AreaName: Area name
        :type AreaName: str
        :param _RegionCode: Region code
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type RegionCode: str
        :param _RegionCodeV3: Region code (v3)
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type RegionCodeV3: str
        :param _Support: NONE: no special models are supported by default.\nCVM: the CVM type is supported.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Support: str
        :param _Ipv6: Whether IPv6 is supported. `0` indicates no, and `1` indicates yes.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Ipv6: int
        :param _MultiZone: Whether cross-AZ clusters are supported.`0` indicates no, and `1` indicates yes.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type MultiZone: int
        """
        self._RegionId = None
        self._RegionName = None
        self._AreaName = None
        self._RegionCode = None
        self._RegionCodeV3 = None
        self._Support = None
        self._Ipv6 = None
        self._MultiZone = None

    @property
    def RegionId(self):
        """Region ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """Region name
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def AreaName(self):
        """Area name
        :rtype: str
        """
        return self._AreaName

    @AreaName.setter
    def AreaName(self, AreaName):
        self._AreaName = AreaName

    @property
    def RegionCode(self):
        """Region code
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode

    @property
    def RegionCodeV3(self):
        """Region code (v3)
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RegionCodeV3

    @RegionCodeV3.setter
    def RegionCodeV3(self, RegionCodeV3):
        self._RegionCodeV3 = RegionCodeV3

    @property
    def Support(self):
        """NONE: no special models are supported by default.\nCVM: the CVM type is supported.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Support

    @Support.setter
    def Support(self, Support):
        self._Support = Support

    @property
    def Ipv6(self):
        """Whether IPv6 is supported. `0` indicates no, and `1` indicates yes.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def MultiZone(self):
        """Whether cross-AZ clusters are supported.`0` indicates no, and `1` indicates yes.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MultiZone

    @MultiZone.setter
    def MultiZone(self, MultiZone):
        self._MultiZone = MultiZone


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._AreaName = params.get("AreaName")
        self._RegionCode = params.get("RegionCode")
        self._RegionCodeV3 = params.get("RegionCodeV3")
        self._Support = params.get("Support")
        self._Ipv6 = params.get("Ipv6")
        self._MultiZone = params.get("MultiZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Route(AbstractModel):
    """Route entity object

    """

    def __init__(self):
        r"""
        :param _AccessType: Instance connection method
0: PLAINTEXT (plaintext method, which does not carry user information and is supported for legacy versions and Community Edition)
1: SASL_PLAINTEXT (plaintext method, which authenticates the login through SASL before data start and is supported only for Community Edition)
2: SSL (SSL-encrypted communication, which does not carry user information and is supported for legacy versions and Community Edition)
3: SASL_SSL (SSL-encrypted communication, which authenticates the login through SASL before data start and is supported only for Community Edition)
        :type AccessType: int
        :param _RouteId: Route ID
        :type RouteId: int
        :param _VipType: VIP network type (1: Public network TGW; 2: Classic network; 3: VPC; 4: Supporting network (IDC environment); 5: SSL public network access; 6: BM VPC; 7: Supporting network (CVM environment)).
        :type VipType: int
        :param _VipList: Virtual IP list
        :type VipList: list of VipEntity
        :param _Domain: Domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _DomainPort: Domain name port
Note: this field may return null, indicating that no valid values can be obtained.
        :type DomainPort: int
        :param _DeleteTimestamp: Timestamp
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeleteTimestamp: str
        """
        self._AccessType = None
        self._RouteId = None
        self._VipType = None
        self._VipList = None
        self._Domain = None
        self._DomainPort = None
        self._DeleteTimestamp = None

    @property
    def AccessType(self):
        """Instance connection method
0: PLAINTEXT (plaintext method, which does not carry user information and is supported for legacy versions and Community Edition)
1: SASL_PLAINTEXT (plaintext method, which authenticates the login through SASL before data start and is supported only for Community Edition)
2: SSL (SSL-encrypted communication, which does not carry user information and is supported for legacy versions and Community Edition)
3: SASL_SSL (SSL-encrypted communication, which authenticates the login through SASL before data start and is supported only for Community Edition)
        :rtype: int
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def RouteId(self):
        """Route ID
        :rtype: int
        """
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId

    @property
    def VipType(self):
        """VIP network type (1: Public network TGW; 2: Classic network; 3: VPC; 4: Supporting network (IDC environment); 5: SSL public network access; 6: BM VPC; 7: Supporting network (CVM environment)).
        :rtype: int
        """
        return self._VipType

    @VipType.setter
    def VipType(self, VipType):
        self._VipType = VipType

    @property
    def VipList(self):
        """Virtual IP list
        :rtype: list of VipEntity
        """
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList

    @property
    def Domain(self):
        """Domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainPort(self):
        """Domain name port
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DomainPort

    @DomainPort.setter
    def DomainPort(self, DomainPort):
        self._DomainPort = DomainPort

    @property
    def DeleteTimestamp(self):
        """Timestamp
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DeleteTimestamp

    @DeleteTimestamp.setter
    def DeleteTimestamp(self, DeleteTimestamp):
        self._DeleteTimestamp = DeleteTimestamp


    def _deserialize(self, params):
        self._AccessType = params.get("AccessType")
        self._RouteId = params.get("RouteId")
        self._VipType = params.get("VipType")
        if params.get("VipList") is not None:
            self._VipList = []
            for item in params.get("VipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self._VipList.append(obj)
        self._Domain = params.get("Domain")
        self._DomainPort = params.get("DomainPort")
        self._DeleteTimestamp = params.get("DeleteTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteDTO(AbstractModel):
    """RouteDTO

    """

    def __init__(self):
        r"""
        :param _RouteId: RouteId11 Note: This field may return null, indicating that no valid values can be obtained.
        :type RouteId: int
        """
        self._RouteId = None

    @property
    def RouteId(self):
        """RouteId11 Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId


    def _deserialize(self, params):
        self._RouteId = params.get("RouteId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteResponse(AbstractModel):
    """Returned object for route information

    """

    def __init__(self):
        r"""
        :param _Routers: Route information list
Note: this field may return null, indicating that no valid values can be obtained.
        :type Routers: list of Route
        """
        self._Routers = None

    @property
    def Routers(self):
        """Route information list
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Route
        """
        return self._Routers

    @Routers.setter
    def Routers(self, Routers):
        self._Routers = Routers


    def _deserialize(self, params):
        if params.get("Routers") is not None:
            self._Routers = []
            for item in params.get("Routers"):
                obj = Route()
                obj._deserialize(item)
                self._Routers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaleInfo(AbstractModel):
    """Sales information of Standard Edition

    """

    def __init__(self):
        r"""
        :param _Flag: Manually set flag.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Flag: bool
        :param _Version: CKafka version (v1.1.1/2.4.2/0.10.2）
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Version: str
        :param _Platform: Whether it is Pro Edition or Standard Edition.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Platform: str
        :param _SoldOut: Whether it has been sold out. `true`: sold out.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SoldOut: bool
        """
        self._Flag = None
        self._Version = None
        self._Platform = None
        self._SoldOut = None

    @property
    def Flag(self):
        """Manually set flag.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def Version(self):
        """CKafka version (v1.1.1/2.4.2/0.10.2）
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Platform(self):
        """Whether it is Pro Edition or Standard Edition.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def SoldOut(self):
        """Whether it has been sold out. `true`: sold out.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._SoldOut

    @SoldOut.setter
    def SoldOut(self, SoldOut):
        self._SoldOut = SoldOut


    def _deserialize(self, params):
        self._Flag = params.get("Flag")
        self._Version = params.get("Version")
        self._Platform = params.get("Platform")
        self._SoldOut = params.get("SoldOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessageRequest(AbstractModel):
    """SendMessage request structure.

    """

    def __init__(self):
        r"""
        :param _DataHubId: Datahub access ID.
        :type DataHubId: str
        :param _Message: Content of the message that has been sent. Up to 500 messages can be sent in a single request.
        :type Message: list of BatchContent
        """
        self._DataHubId = None
        self._Message = None

    @property
    def DataHubId(self):
        """Datahub access ID.
        :rtype: str
        """
        return self._DataHubId

    @DataHubId.setter
    def DataHubId(self, DataHubId):
        self._DataHubId = DataHubId

    @property
    def Message(self):
        """Content of the message that has been sent. Up to 500 messages can be sent in a single request.
        :rtype: list of BatchContent
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._DataHubId = params.get("DataHubId")
        if params.get("Message") is not None:
            self._Message = []
            for item in params.get("Message"):
                obj = BatchContent()
                obj._deserialize(item)
                self._Message.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessageResponse(AbstractModel):
    """SendMessage response structure.

    """

    def __init__(self):
        r"""
        :param _MessageId: Message ID list.
        :type MessageId: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MessageId = None
        self._RequestId = None

    @property
    def MessageId(self):
        """Message ID list.
        :rtype: list of str
        """
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MessageId = params.get("MessageId")
        self._RequestId = params.get("RequestId")


class SubscribedInfo(AbstractModel):
    """Subscribed message entity

    """

    def __init__(self):
        r"""
        :param _TopicName: Subscribed topic name
        :type TopicName: str
        :param _Partition: Subscribed partition
Note: this field may return null, indicating that no valid values can be obtained.
        :type Partition: list of int
        :param _PartitionOffset: Partition offset information
Note: this field may return null, indicating that no valid values can be obtained.
        :type PartitionOffset: list of PartitionOffset
        :param _TopicId: ID of the subscribed topic. 
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicId: str
        """
        self._TopicName = None
        self._Partition = None
        self._PartitionOffset = None
        self._TopicId = None

    @property
    def TopicName(self):
        """Subscribed topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Partition(self):
        """Subscribed partition
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def PartitionOffset(self):
        """Partition offset information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of PartitionOffset
        """
        return self._PartitionOffset

    @PartitionOffset.setter
    def PartitionOffset(self, PartitionOffset):
        self._PartitionOffset = PartitionOffset

    @property
    def TopicId(self):
        """ID of the subscribed topic. 
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._Partition = params.get("Partition")
        if params.get("PartitionOffset") is not None:
            self._PartitionOffset = []
            for item in params.get("PartitionOffset"):
                obj = PartitionOffset()
                obj._deserialize(item)
                self._PartitionOffset.append(obj)
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag object in instance details

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """Tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value
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
        


class TaskStatusResponse(AbstractModel):
    """Returned task status

    """

    def __init__(self):
        r"""
        :param _Status: Task status. `0` (Successful), `1` (Failed), `2` ( Running)
        :type Status: int
        :param _Output: Output information Note: This field may return null, indicating that no valid values can be obtained.
        :type Output: str
        """
        self._Status = None
        self._Output = None

    @property
    def Status(self):
        """Task status. `0` (Successful), `1` (Failed), `2` ( Running)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Output(self):
        """Output information Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Output = params.get("Output")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Topic(AbstractModel):
    """Returned topic object

    """

    def __init__(self):
        r"""
        :param _TopicId: Topic ID
        :type TopicId: str
        :param _TopicName: Topic name
        :type TopicName: str
        :param _Note: Remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Note: str
        """
        self._TopicId = None
        self._TopicName = None
        self._Note = None

    @property
    def TopicId(self):
        """Topic ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        """Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Note(self):
        """Remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicAttributesResponse(AbstractModel):
    """Returned topic attributes result entity

    """

    def __init__(self):
        r"""
        :param _TopicId: Topic ID
        :type TopicId: str
        :param _CreateTime: Creation time
        :type CreateTime: int
        :param _Note: Topic remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Note: str
        :param _PartitionNum: Number of partitions
        :type PartitionNum: int
        :param _EnableWhiteList: IP allowlist switch. 1: enabled, 0: disabled
        :type EnableWhiteList: int
        :param _IpWhiteList: IP allowlist list
        :type IpWhiteList: list of str
        :param _Config: Topic configuration array
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`
        :param _Partitions: Partition details
        :type Partitions: list of TopicPartitionDO
        :param _EnableAclRule: Switch of the preset ACL rule. `1`: enable, `0`: disable.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type EnableAclRule: int
        :param _AclRuleList: Preset ACL rule list.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type AclRuleList: list of AclRule
        :param _QuotaConfig: Traffic throttling policy in topic dimension.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type QuotaConfig: :class:`tencentcloud.ckafka.v20190819.models.InstanceQuotaConfigResp`
        :param _ReplicaNum: Number of replicas
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReplicaNum: int
        """
        self._TopicId = None
        self._CreateTime = None
        self._Note = None
        self._PartitionNum = None
        self._EnableWhiteList = None
        self._IpWhiteList = None
        self._Config = None
        self._Partitions = None
        self._EnableAclRule = None
        self._AclRuleList = None
        self._QuotaConfig = None
        self._ReplicaNum = None

    @property
    def TopicId(self):
        """Topic ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def CreateTime(self):
        """Creation time
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Note(self):
        """Topic remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def PartitionNum(self):
        """Number of partitions
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def EnableWhiteList(self):
        """IP allowlist switch. 1: enabled, 0: disabled
        :rtype: int
        """
        return self._EnableWhiteList

    @EnableWhiteList.setter
    def EnableWhiteList(self, EnableWhiteList):
        self._EnableWhiteList = EnableWhiteList

    @property
    def IpWhiteList(self):
        """IP allowlist list
        :rtype: list of str
        """
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList

    @property
    def Config(self):
        """Topic configuration array
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.Config`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Partitions(self):
        """Partition details
        :rtype: list of TopicPartitionDO
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def EnableAclRule(self):
        """Switch of the preset ACL rule. `1`: enable, `0`: disable.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EnableAclRule

    @EnableAclRule.setter
    def EnableAclRule(self, EnableAclRule):
        self._EnableAclRule = EnableAclRule

    @property
    def AclRuleList(self):
        """Preset ACL rule list.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: list of AclRule
        """
        return self._AclRuleList

    @AclRuleList.setter
    def AclRuleList(self, AclRuleList):
        self._AclRuleList = AclRuleList

    @property
    def QuotaConfig(self):
        """Traffic throttling policy in topic dimension.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceQuotaConfigResp`
        """
        return self._QuotaConfig

    @QuotaConfig.setter
    def QuotaConfig(self, QuotaConfig):
        self._QuotaConfig = QuotaConfig

    @property
    def ReplicaNum(self):
        """Number of replicas
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._CreateTime = params.get("CreateTime")
        self._Note = params.get("Note")
        self._PartitionNum = params.get("PartitionNum")
        self._EnableWhiteList = params.get("EnableWhiteList")
        self._IpWhiteList = params.get("IpWhiteList")
        if params.get("Config") is not None:
            self._Config = Config()
            self._Config._deserialize(params.get("Config"))
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = TopicPartitionDO()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._EnableAclRule = params.get("EnableAclRule")
        if params.get("AclRuleList") is not None:
            self._AclRuleList = []
            for item in params.get("AclRuleList"):
                obj = AclRule()
                obj._deserialize(item)
                self._AclRuleList.append(obj)
        if params.get("QuotaConfig") is not None:
            self._QuotaConfig = InstanceQuotaConfigResp()
            self._QuotaConfig._deserialize(params.get("QuotaConfig"))
        self._ReplicaNum = params.get("ReplicaNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicDetail(AbstractModel):
    """Topic details

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name
        :type TopicName: str
        :param _TopicId: Topic ID
        :type TopicId: str
        :param _PartitionNum: Number of partitions
        :type PartitionNum: int
        :param _ReplicaNum: Number of replicas
        :type ReplicaNum: int
        :param _Note: Remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Note: str
        :param _CreateTime: Creation time
        :type CreateTime: int
        :param _EnableWhiteList: Whether to enable IP authentication allowlist. true: yes, false: no
        :type EnableWhiteList: bool
        :param _IpWhiteListCount: Number of IPs in IP allowlist
        :type IpWhiteListCount: int
        :param _ForwardCosBucket: COS bucket for data backup: address of the destination COS bucket
Note: this field may return null, indicating that no valid values can be obtained.
        :type ForwardCosBucket: str
        :param _ForwardStatus: Status of data backup to COS. 1: not enabled, 0: enabled
        :type ForwardStatus: int
        :param _ForwardInterval: Frequency of data backup to COS
        :type ForwardInterval: int
        :param _Config: Advanced configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`
        :param _RetentionTimeConfig: Message retention time configuration (for recording the latest retention time)
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.TopicRetentionTimeConfigRsp`
        :param _Status: `0`: normal, `1`: deleted, `2`: deleting
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Status: int
        :param _Tags: Tag list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        """
        self._TopicName = None
        self._TopicId = None
        self._PartitionNum = None
        self._ReplicaNum = None
        self._Note = None
        self._CreateTime = None
        self._EnableWhiteList = None
        self._IpWhiteListCount = None
        self._ForwardCosBucket = None
        self._ForwardStatus = None
        self._ForwardInterval = None
        self._Config = None
        self._RetentionTimeConfig = None
        self._Status = None
        self._Tags = None

    @property
    def TopicName(self):
        """Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        """Topic ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionNum(self):
        """Number of partitions
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def ReplicaNum(self):
        """Number of replicas
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def Note(self):
        """Remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def CreateTime(self):
        """Creation time
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EnableWhiteList(self):
        """Whether to enable IP authentication allowlist. true: yes, false: no
        :rtype: bool
        """
        return self._EnableWhiteList

    @EnableWhiteList.setter
    def EnableWhiteList(self, EnableWhiteList):
        self._EnableWhiteList = EnableWhiteList

    @property
    def IpWhiteListCount(self):
        """Number of IPs in IP allowlist
        :rtype: int
        """
        return self._IpWhiteListCount

    @IpWhiteListCount.setter
    def IpWhiteListCount(self, IpWhiteListCount):
        self._IpWhiteListCount = IpWhiteListCount

    @property
    def ForwardCosBucket(self):
        """COS bucket for data backup: address of the destination COS bucket
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ForwardCosBucket

    @ForwardCosBucket.setter
    def ForwardCosBucket(self, ForwardCosBucket):
        self._ForwardCosBucket = ForwardCosBucket

    @property
    def ForwardStatus(self):
        """Status of data backup to COS. 1: not enabled, 0: enabled
        :rtype: int
        """
        return self._ForwardStatus

    @ForwardStatus.setter
    def ForwardStatus(self, ForwardStatus):
        self._ForwardStatus = ForwardStatus

    @property
    def ForwardInterval(self):
        """Frequency of data backup to COS
        :rtype: int
        """
        return self._ForwardInterval

    @ForwardInterval.setter
    def ForwardInterval(self, ForwardInterval):
        self._ForwardInterval = ForwardInterval

    @property
    def Config(self):
        """Advanced configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.Config`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def RetentionTimeConfig(self):
        """Message retention time configuration (for recording the latest retention time)
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicRetentionTimeConfigRsp`
        """
        return self._RetentionTimeConfig

    @RetentionTimeConfig.setter
    def RetentionTimeConfig(self, RetentionTimeConfig):
        self._RetentionTimeConfig = RetentionTimeConfig

    @property
    def Status(self):
        """`0`: normal, `1`: deleted, `2`: deleting
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        """Tag list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._TopicId = params.get("TopicId")
        self._PartitionNum = params.get("PartitionNum")
        self._ReplicaNum = params.get("ReplicaNum")
        self._Note = params.get("Note")
        self._CreateTime = params.get("CreateTime")
        self._EnableWhiteList = params.get("EnableWhiteList")
        self._IpWhiteListCount = params.get("IpWhiteListCount")
        self._ForwardCosBucket = params.get("ForwardCosBucket")
        self._ForwardStatus = params.get("ForwardStatus")
        self._ForwardInterval = params.get("ForwardInterval")
        if params.get("Config") is not None:
            self._Config = Config()
            self._Config._deserialize(params.get("Config"))
        if params.get("RetentionTimeConfig") is not None:
            self._RetentionTimeConfig = TopicRetentionTimeConfigRsp()
            self._RetentionTimeConfig._deserialize(params.get("RetentionTimeConfig"))
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicDetailResponse(AbstractModel):
    """Returned topic details entity

    """

    def __init__(self):
        r"""
        :param _TopicList: List of returned topic details
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicList: list of TopicDetail
        :param _TotalCount: Number of all eligible topic details
        :type TotalCount: int
        """
        self._TopicList = None
        self._TotalCount = None

    @property
    def TopicList(self):
        """List of returned topic details
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of TopicDetail
        """
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList

    @property
    def TotalCount(self):
        """Number of all eligible topic details
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("TopicList") is not None:
            self._TopicList = []
            for item in params.get("TopicList"):
                obj = TopicDetail()
                obj._deserialize(item)
                self._TopicList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicInSyncReplicaInfo(AbstractModel):
    """Topic replica and details

    """

    def __init__(self):
        r"""
        :param _Partition: Partition name
        :type Partition: str
        :param _Leader: Leader ID
        :type Leader: int
        :param _Replica: Replica set
        :type Replica: str
        :param _InSyncReplica: ISR
        :type InSyncReplica: str
        :param _BeginOffset: Starting offset
Note: this field may return null, indicating that no valid values can be obtained.
        :type BeginOffset: int
        :param _EndOffset: Ending offset
Note: this field may return null, indicating that no valid values can be obtained.
        :type EndOffset: int
        :param _MessageCount: Number of messages
Note: this field may return null, indicating that no valid values can be obtained.
        :type MessageCount: int
        :param _OutOfSyncReplica: Unsynced replica set
Note: this field may return null, indicating that no valid values can be obtained.
        :type OutOfSyncReplica: str
        """
        self._Partition = None
        self._Leader = None
        self._Replica = None
        self._InSyncReplica = None
        self._BeginOffset = None
        self._EndOffset = None
        self._MessageCount = None
        self._OutOfSyncReplica = None

    @property
    def Partition(self):
        """Partition name
        :rtype: str
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Leader(self):
        """Leader ID
        :rtype: int
        """
        return self._Leader

    @Leader.setter
    def Leader(self, Leader):
        self._Leader = Leader

    @property
    def Replica(self):
        """Replica set
        :rtype: str
        """
        return self._Replica

    @Replica.setter
    def Replica(self, Replica):
        self._Replica = Replica

    @property
    def InSyncReplica(self):
        """ISR
        :rtype: str
        """
        return self._InSyncReplica

    @InSyncReplica.setter
    def InSyncReplica(self, InSyncReplica):
        self._InSyncReplica = InSyncReplica

    @property
    def BeginOffset(self):
        """Starting offset
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def EndOffset(self):
        """Ending offset
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EndOffset

    @EndOffset.setter
    def EndOffset(self, EndOffset):
        self._EndOffset = EndOffset

    @property
    def MessageCount(self):
        """Number of messages
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MessageCount

    @MessageCount.setter
    def MessageCount(self, MessageCount):
        self._MessageCount = MessageCount

    @property
    def OutOfSyncReplica(self):
        """Unsynced replica set
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OutOfSyncReplica

    @OutOfSyncReplica.setter
    def OutOfSyncReplica(self, OutOfSyncReplica):
        self._OutOfSyncReplica = OutOfSyncReplica


    def _deserialize(self, params):
        self._Partition = params.get("Partition")
        self._Leader = params.get("Leader")
        self._Replica = params.get("Replica")
        self._InSyncReplica = params.get("InSyncReplica")
        self._BeginOffset = params.get("BeginOffset")
        self._EndOffset = params.get("EndOffset")
        self._MessageCount = params.get("MessageCount")
        self._OutOfSyncReplica = params.get("OutOfSyncReplica")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicInSyncReplicaResult(AbstractModel):
    """Set of topic replicas and details

    """

    def __init__(self):
        r"""
        :param _TopicInSyncReplicaList: Set of topic details and replicas
        :type TopicInSyncReplicaList: list of TopicInSyncReplicaInfo
        :param _TotalCount: Total number
        :type TotalCount: int
        """
        self._TopicInSyncReplicaList = None
        self._TotalCount = None

    @property
    def TopicInSyncReplicaList(self):
        """Set of topic details and replicas
        :rtype: list of TopicInSyncReplicaInfo
        """
        return self._TopicInSyncReplicaList

    @TopicInSyncReplicaList.setter
    def TopicInSyncReplicaList(self, TopicInSyncReplicaList):
        self._TopicInSyncReplicaList = TopicInSyncReplicaList

    @property
    def TotalCount(self):
        """Total number
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("TopicInSyncReplicaList") is not None:
            self._TopicInSyncReplicaList = []
            for item in params.get("TopicInSyncReplicaList"):
                obj = TopicInSyncReplicaInfo()
                obj._deserialize(item)
                self._TopicInSyncReplicaList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicPartitionDO(AbstractModel):
    """Partition details

    """

    def __init__(self):
        r"""
        :param _Partition: Partition ID
        :type Partition: int
        :param _LeaderStatus: Leader running status
        :type LeaderStatus: int
        :param _IsrNum: ISR quantity
        :type IsrNum: int
        :param _ReplicaNum: Number of replicas
        :type ReplicaNum: int
        """
        self._Partition = None
        self._LeaderStatus = None
        self._IsrNum = None
        self._ReplicaNum = None

    @property
    def Partition(self):
        """Partition ID
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def LeaderStatus(self):
        """Leader running status
        :rtype: int
        """
        return self._LeaderStatus

    @LeaderStatus.setter
    def LeaderStatus(self, LeaderStatus):
        self._LeaderStatus = LeaderStatus

    @property
    def IsrNum(self):
        """ISR quantity
        :rtype: int
        """
        return self._IsrNum

    @IsrNum.setter
    def IsrNum(self, IsrNum):
        self._IsrNum = IsrNum

    @property
    def ReplicaNum(self):
        """Number of replicas
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum


    def _deserialize(self, params):
        self._Partition = params.get("Partition")
        self._LeaderStatus = params.get("LeaderStatus")
        self._IsrNum = params.get("IsrNum")
        self._ReplicaNum = params.get("ReplicaNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicResult(AbstractModel):
    """`TopicResponse` returned uniformly

    """

    def __init__(self):
        r"""
        :param _TopicList: List of returned topic information
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicList: list of Topic
        :param _TotalCount: Number of eligible topics
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        """
        self._TopicList = None
        self._TotalCount = None

    @property
    def TopicList(self):
        """List of returned topic information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Topic
        """
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList

    @property
    def TotalCount(self):
        """Number of eligible topics
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("TopicList") is not None:
            self._TopicList = []
            for item in params.get("TopicList"):
                obj = Topic()
                obj._deserialize(item)
                self._TopicList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRetentionTimeConfigRsp(AbstractModel):
    """Information returned for topic message retention time configuration

    """

    def __init__(self):
        r"""
        :param _Expect: Expected value, i.e., the topic message retention time (min) configured
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Expect: int
        :param _Current: Current value (min), i.e., the retention time currently in effect, which may be dynamically adjusted
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Current: int
        :param _ModTimeStamp: Last modified time
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ModTimeStamp: int
        """
        self._Expect = None
        self._Current = None
        self._ModTimeStamp = None

    @property
    def Expect(self):
        """Expected value, i.e., the topic message retention time (min) configured
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Expect

    @Expect.setter
    def Expect(self, Expect):
        self._Expect = Expect

    @property
    def Current(self):
        """Current value (min), i.e., the retention time currently in effect, which may be dynamically adjusted
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Current

    @Current.setter
    def Current(self, Current):
        self._Current = Current

    @property
    def ModTimeStamp(self):
        """Last modified time
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ModTimeStamp

    @ModTimeStamp.setter
    def ModTimeStamp(self, ModTimeStamp):
        self._ModTimeStamp = ModTimeStamp


    def _deserialize(self, params):
        self._Expect = params.get("Expect")
        self._Current = params.get("Current")
        self._ModTimeStamp = params.get("ModTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicSubscribeGroup(AbstractModel):
    """`DescribeTopicSubscribeGroup` output parameters

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _StatusCountInfo: Number of consumer group status
        :type StatusCountInfo: str
        :param _GroupsInfo: Consumer group information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type GroupsInfo: list of GroupInfoResponse
        :param _Status: Whether a request is asynchronous. If there are fewer consumer groups in the instances, the result will be returned directly, and status code is 1. When there are many consumer groups in the instances, cache will be updated asynchronously. When status code is 0, grouping information will not be returned until cache update is completed and status code becomes 1.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Status: int
        """
        self._TotalCount = None
        self._StatusCountInfo = None
        self._GroupsInfo = None
        self._Status = None

    @property
    def TotalCount(self):
        """Total number
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def StatusCountInfo(self):
        """Number of consumer group status
        :rtype: str
        """
        return self._StatusCountInfo

    @StatusCountInfo.setter
    def StatusCountInfo(self, StatusCountInfo):
        self._StatusCountInfo = StatusCountInfo

    @property
    def GroupsInfo(self):
        """Consumer group information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of GroupInfoResponse
        """
        return self._GroupsInfo

    @GroupsInfo.setter
    def GroupsInfo(self, GroupsInfo):
        self._GroupsInfo = GroupsInfo

    @property
    def Status(self):
        """Whether a request is asynchronous. If there are fewer consumer groups in the instances, the result will be returned directly, and status code is 1. When there are many consumer groups in the instances, cache will be updated asynchronously. When status code is 0, grouping information will not be returned until cache update is completed and status code becomes 1.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._StatusCountInfo = params.get("StatusCountInfo")
        if params.get("GroupsInfo") is not None:
            self._GroupsInfo = []
            for item in params.get("GroupsInfo"):
                obj = GroupInfoResponse()
                obj._deserialize(item)
                self._GroupsInfo.append(obj)
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    """User entity

    """

    def __init__(self):
        r"""
        :param _UserId: User ID
        :type UserId: int
        :param _Name: Username
        :type Name: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _UpdateTime: Last updated time
        :type UpdateTime: str
        """
        self._UserId = None
        self._Name = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def UserId(self):
        """User ID
        :rtype: int
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Name(self):
        """Username
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreateTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Last updated time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Name = params.get("Name")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserResponse(AbstractModel):
    """Returned user entity

    """

    def __init__(self):
        r"""
        :param _Users: List of eligible users
Note: this field may return null, indicating that no valid values can be obtained.
        :type Users: list of User
        :param _TotalCount: Total number of eligible users
        :type TotalCount: int
        """
        self._Users = None
        self._TotalCount = None

    @property
    def Users(self):
        """List of eligible users
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of User
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def TotalCount(self):
        """Total number of eligible users
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = User()
                obj._deserialize(item)
                self._Users.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VipEntity(AbstractModel):
    """Virtual IP entity

    """

    def __init__(self):
        r"""
        :param _Vip: Virtual IP
        :type Vip: str
        :param _Vport: Virtual port
        :type Vport: str
        """
        self._Vip = None
        self._Vport = None

    @property
    def Vip(self):
        """Virtual IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Virtual port
        :rtype: str
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport


    def _deserialize(self, params):
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """Zone information entity

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID
        :type ZoneId: str
        :param _IsInternalApp: Whether it is an internal application.
        :type IsInternalApp: int
        :param _AppId: Application ID
        :type AppId: int
        :param _Flag: Flag
        :type Flag: bool
        :param _ZoneName: Zone name
        :type ZoneName: str
        :param _ZoneStatus: Zone status
        :type ZoneStatus: int
        :param _Exflag: Extra flag
        :type Exflag: str
        :param _SoldOut: JSON object. The key is the model. The value `true` means “sold out”, and `false` means “not sold out”.
        :type SoldOut: str
        :param _SalesInfo: Information on whether Standard Edition has been sold out.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SalesInfo: list of SaleInfo
        """
        self._ZoneId = None
        self._IsInternalApp = None
        self._AppId = None
        self._Flag = None
        self._ZoneName = None
        self._ZoneStatus = None
        self._Exflag = None
        self._SoldOut = None
        self._SalesInfo = None

    @property
    def ZoneId(self):
        """Zone ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IsInternalApp(self):
        """Whether it is an internal application.
        :rtype: int
        """
        return self._IsInternalApp

    @IsInternalApp.setter
    def IsInternalApp(self, IsInternalApp):
        self._IsInternalApp = IsInternalApp

    @property
    def AppId(self):
        """Application ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Flag(self):
        """Flag
        :rtype: bool
        """
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def ZoneName(self):
        """Zone name
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneStatus(self):
        """Zone status
        :rtype: int
        """
        return self._ZoneStatus

    @ZoneStatus.setter
    def ZoneStatus(self, ZoneStatus):
        self._ZoneStatus = ZoneStatus

    @property
    def Exflag(self):
        """Extra flag
        :rtype: str
        """
        return self._Exflag

    @Exflag.setter
    def Exflag(self, Exflag):
        self._Exflag = Exflag

    @property
    def SoldOut(self):
        """JSON object. The key is the model. The value `true` means “sold out”, and `false` means “not sold out”.
        :rtype: str
        """
        return self._SoldOut

    @SoldOut.setter
    def SoldOut(self, SoldOut):
        self._SoldOut = SoldOut

    @property
    def SalesInfo(self):
        """Information on whether Standard Edition has been sold out.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of SaleInfo
        """
        return self._SalesInfo

    @SalesInfo.setter
    def SalesInfo(self, SalesInfo):
        self._SalesInfo = SalesInfo


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._IsInternalApp = params.get("IsInternalApp")
        self._AppId = params.get("AppId")
        self._Flag = params.get("Flag")
        self._ZoneName = params.get("ZoneName")
        self._ZoneStatus = params.get("ZoneStatus")
        self._Exflag = params.get("Exflag")
        self._SoldOut = params.get("SoldOut")
        if params.get("SalesInfo") is not None:
            self._SalesInfo = []
            for item in params.get("SalesInfo"):
                obj = SaleInfo()
                obj._deserialize(item)
                self._SalesInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneResponse(AbstractModel):
    """The entity returned for the query of Kafka’s zone information

    """

    def __init__(self):
        r"""
        :param _ZoneList: Zone list
        :type ZoneList: list of ZoneInfo
        :param _MaxBuyInstanceNum: Maximum number of instances to be purchased
        :type MaxBuyInstanceNum: int
        :param _MaxBandwidth: Maximum bandwidth in MB/S
        :type MaxBandwidth: int
        :param _UnitPrice: Pay-as-you-go unit price
        :type UnitPrice: :class:`tencentcloud.ckafka.v20190819.models.Price`
        :param _MessagePrice: Pay-as-you-go unit message price
        :type MessagePrice: :class:`tencentcloud.ckafka.v20190819.models.Price`
        :param _ClusterInfo: Cluster information dedicated to a user
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ClusterInfo: list of ClusterInfo
        :param _Standard: Purchase of Standard Edition configurations
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Standard: str
        :param _StandardS2: Purchase of Standard S2 Edition configurations
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type StandardS2: str
        :param _Profession: Purchase of Pro Edition configurations
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Profession: str
        :param _Physical: Purchase of Physical Dedicated Edition configurations
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Physical: str
        :param _PublicNetwork: Public network bandwidth.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PublicNetwork: str
        :param _PublicNetworkLimit: Public network bandwidth configuration.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PublicNetworkLimit: str
        """
        self._ZoneList = None
        self._MaxBuyInstanceNum = None
        self._MaxBandwidth = None
        self._UnitPrice = None
        self._MessagePrice = None
        self._ClusterInfo = None
        self._Standard = None
        self._StandardS2 = None
        self._Profession = None
        self._Physical = None
        self._PublicNetwork = None
        self._PublicNetworkLimit = None

    @property
    def ZoneList(self):
        """Zone list
        :rtype: list of ZoneInfo
        """
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

    @property
    def MaxBuyInstanceNum(self):
        """Maximum number of instances to be purchased
        :rtype: int
        """
        return self._MaxBuyInstanceNum

    @MaxBuyInstanceNum.setter
    def MaxBuyInstanceNum(self, MaxBuyInstanceNum):
        self._MaxBuyInstanceNum = MaxBuyInstanceNum

    @property
    def MaxBandwidth(self):
        """Maximum bandwidth in MB/S
        :rtype: int
        """
        return self._MaxBandwidth

    @MaxBandwidth.setter
    def MaxBandwidth(self, MaxBandwidth):
        self._MaxBandwidth = MaxBandwidth

    @property
    def UnitPrice(self):
        """Pay-as-you-go unit price
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.Price`
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def MessagePrice(self):
        """Pay-as-you-go unit message price
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.Price`
        """
        return self._MessagePrice

    @MessagePrice.setter
    def MessagePrice(self, MessagePrice):
        self._MessagePrice = MessagePrice

    @property
    def ClusterInfo(self):
        """Cluster information dedicated to a user
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: list of ClusterInfo
        """
        return self._ClusterInfo

    @ClusterInfo.setter
    def ClusterInfo(self, ClusterInfo):
        self._ClusterInfo = ClusterInfo

    @property
    def Standard(self):
        """Purchase of Standard Edition configurations
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Standard

    @Standard.setter
    def Standard(self, Standard):
        self._Standard = Standard

    @property
    def StandardS2(self):
        """Purchase of Standard S2 Edition configurations
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StandardS2

    @StandardS2.setter
    def StandardS2(self, StandardS2):
        self._StandardS2 = StandardS2

    @property
    def Profession(self):
        """Purchase of Pro Edition configurations
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Profession

    @Profession.setter
    def Profession(self, Profession):
        self._Profession = Profession

    @property
    def Physical(self):
        """Purchase of Physical Dedicated Edition configurations
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Physical

    @Physical.setter
    def Physical(self, Physical):
        self._Physical = Physical

    @property
    def PublicNetwork(self):
        """Public network bandwidth.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def PublicNetworkLimit(self):
        """Public network bandwidth configuration.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PublicNetworkLimit

    @PublicNetworkLimit.setter
    def PublicNetworkLimit(self, PublicNetworkLimit):
        self._PublicNetworkLimit = PublicNetworkLimit


    def _deserialize(self, params):
        if params.get("ZoneList") is not None:
            self._ZoneList = []
            for item in params.get("ZoneList"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._ZoneList.append(obj)
        self._MaxBuyInstanceNum = params.get("MaxBuyInstanceNum")
        self._MaxBandwidth = params.get("MaxBandwidth")
        if params.get("UnitPrice") is not None:
            self._UnitPrice = Price()
            self._UnitPrice._deserialize(params.get("UnitPrice"))
        if params.get("MessagePrice") is not None:
            self._MessagePrice = Price()
            self._MessagePrice._deserialize(params.get("MessagePrice"))
        if params.get("ClusterInfo") is not None:
            self._ClusterInfo = []
            for item in params.get("ClusterInfo"):
                obj = ClusterInfo()
                obj._deserialize(item)
                self._ClusterInfo.append(obj)
        self._Standard = params.get("Standard")
        self._StandardS2 = params.get("StandardS2")
        self._Profession = params.get("Profession")
        self._Physical = params.get("Physical")
        self._PublicNetwork = params.get("PublicNetwork")
        self._PublicNetworkLimit = params.get("PublicNetworkLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        