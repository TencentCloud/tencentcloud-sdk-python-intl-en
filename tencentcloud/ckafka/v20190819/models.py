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


class Acl(AbstractModel):
    r"""ACL object entity

    """

    def __init__(self):
        r"""
        :param _ResourceType: ACL resource type. 0: UNKNOWN, 1: ANY, 2: TOPIC, 3: GROUP, 4: CLUSTER, 5: TRANSACTIONAL_ID. Currently, only `TOPIC` is available,
        :type ResourceType: int
        :param _ResourceName: Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name
        :type ResourceName: str
        :param _Principal: List of users, defaults to User:*, means any User is accessible in the entire region. the current User can only be the User in the list of users.
        :type Principal: str
        :param _Host: Defaults to *, indicating any host is accessible in the entire region. currently, ckafka does not support * as the host, however, the following open-source kafka productization will directly support it.
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
        r"""ACL resource type. 0: UNKNOWN, 1: ANY, 2: TOPIC, 3: GROUP, 4: CLUSTER, 5: TRANSACTIONAL_ID. Currently, only `TOPIC` is available,
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        r"""Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Principal(self):
        r"""List of users, defaults to User:*, means any User is accessible in the entire region. the current User can only be the User in the list of users.
        :rtype: str
        """
        return self._Principal

    @Principal.setter
    def Principal(self, Principal):
        self._Principal = Principal

    @property
    def Host(self):
        r"""Defaults to *, indicating any host is accessible in the entire region. currently, ckafka does not support * as the host, however, the following open-source kafka productization will directly support it.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Operation(self):
        r"""ACL operation mode. 0: UNKNOWN, 1: ANY, 2: ALL, 3: READ, 4: WRITE, 5: CREATE, 6: DELETE, 7: ALTER, 8: DESCRIBE, 9: CLUSTER_ACTION, 10: DESCRIBE_CONFIGS, 11: ALTER_CONFIGS, 12: IDEMPOTEN_WRITE
        :rtype: int
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PermissionType(self):
        r"""Permission type. 0: UNKNOWN, 1: ANY, 2: DENY, 3: ALLOW
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
    r"""Set of returned ACL results

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible data entries
        :type TotalCount: int
        :param _AclList: ACL list.
        :type AclList: list of Acl
        """
        self._TotalCount = None
        self._AclList = None

    @property
    def TotalCount(self):
        r"""Number of eligible data entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AclList(self):
        r"""ACL list.
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
    r"""Output parameters of ACL rule list APIs

    """

    def __init__(self):
        r"""
        :param _RuleName: ACL rule name.
        :type RuleName: str
        :param _InstanceId: The ckafka cluster instance Id.
        :type InstanceId: str
        :param _PatternType: ACL rule-based matching type. currently only supports prefix match. valid values: PREFIXED.
        :type PatternType: str
        :param _Pattern: Indicates the prefix value for prefix match.
        :type Pattern: str
        :param _ResourceType: Acl resource type, currently only support Topic. valid values: Topic.
        :type ResourceType: str
        :param _AclList: Specifies the ACL information contained in the rule.
        :type AclList: str
        :param _CreateTimeStamp: Specifies the time when the rule was created.
        :type CreateTimeStamp: str
        :param _IsApplied: Specifies whether to apply the preset ACL rule to newly-added topics.
        :type IsApplied: int
        :param _UpdateTimeStamp: Rule update time.
        :type UpdateTimeStamp: str
        :param _Comment: Specifies the remark of the rule.
        :type Comment: str
        :param _TopicName: One of the displayed corresponding TopicName.
        :type TopicName: str
        :param _TopicCount: Number of topics to which the ACL rule is applied.
        :type TopicCount: int
        :param _PatternTypeTitle: Specifies the pattern type.
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
        r"""ACL rule name.
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PatternType(self):
        r"""ACL rule-based matching type. currently only supports prefix match. valid values: PREFIXED.
        :rtype: str
        """
        return self._PatternType

    @PatternType.setter
    def PatternType(self, PatternType):
        self._PatternType = PatternType

    @property
    def Pattern(self):
        r"""Indicates the prefix value for prefix match.
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def ResourceType(self):
        r"""Acl resource type, currently only support Topic. valid values: Topic.
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def AclList(self):
        r"""Specifies the ACL information contained in the rule.
        :rtype: str
        """
        return self._AclList

    @AclList.setter
    def AclList(self, AclList):
        self._AclList = AclList

    @property
    def CreateTimeStamp(self):
        r"""Specifies the time when the rule was created.
        :rtype: str
        """
        return self._CreateTimeStamp

    @CreateTimeStamp.setter
    def CreateTimeStamp(self, CreateTimeStamp):
        self._CreateTimeStamp = CreateTimeStamp

    @property
    def IsApplied(self):
        r"""Specifies whether to apply the preset ACL rule to newly-added topics.
        :rtype: int
        """
        return self._IsApplied

    @IsApplied.setter
    def IsApplied(self, IsApplied):
        self._IsApplied = IsApplied

    @property
    def UpdateTimeStamp(self):
        r"""Rule update time.
        :rtype: str
        """
        return self._UpdateTimeStamp

    @UpdateTimeStamp.setter
    def UpdateTimeStamp(self, UpdateTimeStamp):
        self._UpdateTimeStamp = UpdateTimeStamp

    @property
    def Comment(self):
        r"""Specifies the remark of the rule.
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def TopicName(self):
        r"""One of the displayed corresponding TopicName.
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicCount(self):
        r"""Number of topics to which the ACL rule is applied.
        :rtype: int
        """
        return self._TopicCount

    @TopicCount.setter
    def TopicCount(self, TopicCount):
        self._TopicCount = TopicCount

    @property
    def PatternTypeTitle(self):
        r"""Specifies the pattern type.
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
    r"""Four pieces of information of ACL rules: source IP address, destination IP address, source port, and destination port

    """

    def __init__(self):
        r"""
        :param _Operation: ACL operation types. Enumerated values: `All` (all operations), `Read` (read), `Write` (write).
        :type Operation: str
        :param _PermissionType: Permission type. Deny: Deny. Allow: permission.
        :type PermissionType: str
        :param _Host: Indicates any host is accessible in the entire region.
        :type Host: str
        :param _Principal: The User. User:* means any User is accessible in the entire region. the current User can only be the User in the list of users. the input format requires the [User:] prefix. for example, for User A, input User:A.
        :type Principal: str
        """
        self._Operation = None
        self._PermissionType = None
        self._Host = None
        self._Principal = None

    @property
    def Operation(self):
        r"""ACL operation types. Enumerated values: `All` (all operations), `Read` (read), `Write` (write).
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PermissionType(self):
        r"""Permission type. Deny: Deny. Allow: permission.
        :rtype: str
        """
        return self._PermissionType

    @PermissionType.setter
    def PermissionType(self, PermissionType):
        self._PermissionType = PermissionType

    @property
    def Host(self):
        r"""Indicates any host is accessible in the entire region.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Principal(self):
        r"""The User. User:* means any User is accessible in the entire region. the current User can only be the User in the list of users. the input format requires the [User:] prefix. for example, for User A, input User:A.
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
    r"""Results returned by the `AclRuleList` API

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of data entries
        :type TotalCount: int
        :param _AclRuleList: AclRule list.
        :type AclRuleList: list of AclRule
        """
        self._TotalCount = None
        self._AclRuleList = None

    @property
    def TotalCount(self):
        r"""Total number of data entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AclRuleList(self):
        r"""AclRule list.
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
        


class Assignment(AbstractModel):
    r"""Stores the information of partition assigned to this consumer

    """

    def __init__(self):
        r"""
        :param _Version: Assignment version information
        :type Version: int
        :param _Topics: topic information list.
        :type Topics: list of GroupInfoTopics
        """
        self._Version = None
        self._Topics = None

    @property
    def Version(self):
        r"""Assignment version information
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Topics(self):
        r"""topic information list.
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
    r"""Message content that can be sent in batches

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
        r"""Message body that is sent.
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Key(self):
        r"""Message sending key name.
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
    r"""BatchCreateAcl request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _ResourceType: ACL resource type. Default value: `2` (topic).
        :type ResourceType: int
        :param _ResourceNames: Resource list array, obtainable through the DescribeTopic API (https://www.tencentcloud.comom/document/product/597/40847?from_cn_redirect=1).
        :type ResourceNames: list of str
        :param _RuleList: Specifies the set ACL rule list, which can be obtained through the DescribeAclRule API (https://www.tencentcloud.comom/document/product/597/89217?from_cn_redirect=1).
        :type RuleList: list of AclRuleInfo
        """
        self._InstanceId = None
        self._ResourceType = None
        self._ResourceNames = None
        self._RuleList = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceType(self):
        r"""ACL resource type. Default value: `2` (topic).
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceNames(self):
        r"""Resource list array, obtainable through the DescribeTopic API (https://www.tencentcloud.comom/document/product/597/40847?from_cn_redirect=1).
        :rtype: list of str
        """
        return self._ResourceNames

    @ResourceNames.setter
    def ResourceNames(self, ResourceNames):
        self._ResourceNames = ResourceNames

    @property
    def RuleList(self):
        r"""Specifies the set ACL rule list, which can be obtained through the DescribeAclRule API (https://www.tencentcloud.comom/document/product/597/89217?from_cn_redirect=1).
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
    r"""BatchCreateAcl response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Status code: 0 - modification succeeded, otherwise modification failed.
        :type Result: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Status code: 0 - modification succeeded, otherwise modification failed.
        :rtype: int
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


class BatchModifyGroupOffsetsRequest(AbstractModel):
    r"""BatchModifyGroupOffsets request structure.

    """

    def __init__(self):
        r"""
        :param _GroupName: Consumer group name.
        :type GroupName: str
        :param _InstanceId: The ckafka cluster instance Id.
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
        r"""Consumer group name.
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Partitions(self):
        r"""Partition information.
        :rtype: list of Partitions
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def TopicName(self):
        r"""Name of the specified topic. Default value: names of all topics.
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
    r"""BatchModifyGroupOffsets response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class BatchModifyTopicAttributesRequest(AbstractModel):
    r"""BatchModifyTopicAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _Topic: Specifies the topic attribute list (a maximum of 10 per batch), which can be obtained through the [DescribeTopic](https://www.tencentcloud.comom/document/product/597/40847?from_cn_redirect=1) api.
        :type Topic: list of BatchModifyTopicInfo
        """
        self._InstanceId = None
        self._Topic = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""Specifies the topic attribute list (a maximum of 10 per batch), which can be obtained through the [DescribeTopic](https://www.tencentcloud.comom/document/product/597/40847?from_cn_redirect=1) api.
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
    r"""BatchModifyTopicAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: list of BatchModifyTopicResultDTO
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result.
        :rtype: list of BatchModifyTopicResultDTO
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
            self._Result = []
            for item in params.get("Result"):
                obj = BatchModifyTopicResultDTO()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class BatchModifyTopicInfo(AbstractModel):
    r"""Topic parameters that can be modified in batches

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name
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
        :param _RetentionBytes: Specifies the message retention size in the topic dimension in bytes. value range: 1 GB to 1024 GB.
        :type RetentionBytes: int
        :param _SegmentMs: Duration of Segment shard scrolling in milliseconds. value range: 1 day to 90 days.
        :type SegmentMs: int
        :param _MaxMessageBytes: Message size per batch. Value range: 1 KB - 12 MB.
        :type MaxMessageBytes: int
        :param _LogMsgTimestampType: Specifies the time type for message storage: CreateTime/LogAppendTime.
        :type LogMsgTimestampType: str
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
        self._LogMsgTimestampType = None

    @property
    def TopicName(self):
        r"""Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionNum(self):
        r"""The number of partitions.
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def Note(self):
        r"""Remarks.
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def ReplicaNum(self):
        r"""Number of replicas.
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def CleanUpPolicy(self):
        r"""Message deletion policy. Valid values: `delete`, `compact`.
        :rtype: str
        """
        return self._CleanUpPolicy

    @CleanUpPolicy.setter
    def CleanUpPolicy(self, CleanUpPolicy):
        self._CleanUpPolicy = CleanUpPolicy

    @property
    def MinInsyncReplicas(self):
        r"""The minimum number of replicas specified by `min.insync.replicas` when the producer sets `request.required.acks` to `-1`.
        :rtype: int
        """
        return self._MinInsyncReplicas

    @MinInsyncReplicas.setter
    def MinInsyncReplicas(self, MinInsyncReplicas):
        self._MinInsyncReplicas = MinInsyncReplicas

    @property
    def UncleanLeaderElectionEnable(self):
        r"""Whether to allow a non-ISR replica to be the leader.
        :rtype: bool
        """
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def RetentionMs(self):
        r"""Message retention period in topic dimension in milliseconds. Value range: 1 minute to 90 days.
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def RetentionBytes(self):
        r"""Specifies the message retention size in the topic dimension in bytes. value range: 1 GB to 1024 GB.
        :rtype: int
        """
        return self._RetentionBytes

    @RetentionBytes.setter
    def RetentionBytes(self, RetentionBytes):
        self._RetentionBytes = RetentionBytes

    @property
    def SegmentMs(self):
        r"""Duration of Segment shard scrolling in milliseconds. value range: 1 day to 90 days.
        :rtype: int
        """
        return self._SegmentMs

    @SegmentMs.setter
    def SegmentMs(self, SegmentMs):
        self._SegmentMs = SegmentMs

    @property
    def MaxMessageBytes(self):
        r"""Message size per batch. Value range: 1 KB - 12 MB.
        :rtype: int
        """
        return self._MaxMessageBytes

    @MaxMessageBytes.setter
    def MaxMessageBytes(self, MaxMessageBytes):
        self._MaxMessageBytes = MaxMessageBytes

    @property
    def LogMsgTimestampType(self):
        r"""Specifies the time type for message storage: CreateTime/LogAppendTime.
        :rtype: str
        """
        return self._LogMsgTimestampType

    @LogMsgTimestampType.setter
    def LogMsgTimestampType(self, LogMsgTimestampType):
        self._LogMsgTimestampType = LogMsgTimestampType


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
        self._LogMsgTimestampType = params.get("LogMsgTimestampType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyTopicResultDTO(AbstractModel):
    r"""Results of the batch modified topic attributes

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id.
        :type InstanceId: str
        :param _TopicName: Topic name
        :type TopicName: str
        :param _ReturnCode: Operation return code.
        :type ReturnCode: str
        :param _Message: Returned information.
        :type Message: str
        """
        self._InstanceId = None
        self._TopicName = None
        self._ReturnCode = None
        self._Message = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        r"""Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def ReturnCode(self):
        r"""Operation return code.
        :rtype: str
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def Message(self):
        r"""Returned information.
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
    r"""Cluster information entity

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: int
        :param _ClusterName: Cluster name
        :type ClusterName: str
        :param _MaxDiskSize: Maximum disk of the cluster (unit: GB).
        :type MaxDiskSize: int
        :param _MaxBandWidth: Maximum bandwidth of the cluster. unit: MB/s.
        :type MaxBandWidth: int
        :param _AvailableDiskSize: Current availability of cluster disk (unit: GB).
        :type AvailableDiskSize: int
        :param _AvailableBandWidth: Available bandwidth of the cluster. unit: MB/s.
        :type AvailableBandWidth: int
        :param _ZoneId: Indicates the AZ to which the cluster belongs.
        :type ZoneId: int
        :param _ZoneIds: The AZ where the cluster nodes are located. If the cluster is a cross-AZ cluster, it includes multiple AZs where the cluster nodes are located.
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
        r"""Cluster ID
        :rtype: int
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""Cluster name
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def MaxDiskSize(self):
        r"""Maximum disk of the cluster (unit: GB).
        :rtype: int
        """
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize

    @property
    def MaxBandWidth(self):
        r"""Maximum bandwidth of the cluster. unit: MB/s.
        :rtype: int
        """
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def AvailableDiskSize(self):
        r"""Current availability of cluster disk (unit: GB).
        :rtype: int
        """
        return self._AvailableDiskSize

    @AvailableDiskSize.setter
    def AvailableDiskSize(self, AvailableDiskSize):
        self._AvailableDiskSize = AvailableDiskSize

    @property
    def AvailableBandWidth(self):
        r"""Available bandwidth of the cluster. unit: MB/s.
        :rtype: int
        """
        return self._AvailableBandWidth

    @AvailableBandWidth.setter
    def AvailableBandWidth(self, AvailableBandWidth):
        self._AvailableBandWidth = AvailableBandWidth

    @property
    def ZoneId(self):
        r"""Indicates the AZ to which the cluster belongs.
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneIds(self):
        r"""The AZ where the cluster nodes are located. If the cluster is a cross-AZ cluster, it includes multiple AZs where the cluster nodes are located.
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
    r"""Advanced configuration object

    """

    def __init__(self):
        r"""
        :param _Retention: Message retention period in milliseconds.
        :type Retention: int
        :param _MinInsyncReplicas: Minimum number of sync replications
Note: this field may return null, indicating that no valid values can be obtained.
        :type MinInsyncReplicas: int
        :param _CleanUpPolicy: Log cleanup mode. Default value: delete.
delete: logs will be deleted by save time; compact: logs will be compressed by key; compact, delete: logs will be compressed by key and deleted by save time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CleanUpPolicy: str
        :param _SegmentMs: Duration of Segment shard scrolling in milliseconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SegmentMs: int
        :param _UncleanLeaderElectionEnable: 0: false, 1: true.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UncleanLeaderElectionEnable: int
        :param _SegmentBytes: Segment specifies the number of bytes for sharding scroll. unit: bytes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SegmentBytes: int
        :param _MaxMessageBytes: Maximum message byte size. unit: bytes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxMessageBytes: int
        :param _RetentionBytes: Specifies the message retention file size in Bytes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RetentionBytes: int
        :param _LogMsgTimestampType: The time type for message saving. CreateTime means the time when the producer created this message. LogAppendTime means the time when the broker received the message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogMsgTimestampType: str
        """
        self._Retention = None
        self._MinInsyncReplicas = None
        self._CleanUpPolicy = None
        self._SegmentMs = None
        self._UncleanLeaderElectionEnable = None
        self._SegmentBytes = None
        self._MaxMessageBytes = None
        self._RetentionBytes = None
        self._LogMsgTimestampType = None

    @property
    def Retention(self):
        r"""Message retention period in milliseconds.
        :rtype: int
        """
        return self._Retention

    @Retention.setter
    def Retention(self, Retention):
        self._Retention = Retention

    @property
    def MinInsyncReplicas(self):
        r"""Minimum number of sync replications
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MinInsyncReplicas

    @MinInsyncReplicas.setter
    def MinInsyncReplicas(self, MinInsyncReplicas):
        self._MinInsyncReplicas = MinInsyncReplicas

    @property
    def CleanUpPolicy(self):
        r"""Log cleanup mode. Default value: delete.
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
        r"""Duration of Segment shard scrolling in milliseconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SegmentMs

    @SegmentMs.setter
    def SegmentMs(self, SegmentMs):
        self._SegmentMs = SegmentMs

    @property
    def UncleanLeaderElectionEnable(self):
        r"""0: false, 1: true.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def SegmentBytes(self):
        r"""Segment specifies the number of bytes for sharding scroll. unit: bytes.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SegmentBytes

    @SegmentBytes.setter
    def SegmentBytes(self, SegmentBytes):
        self._SegmentBytes = SegmentBytes

    @property
    def MaxMessageBytes(self):
        r"""Maximum message byte size. unit: bytes.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxMessageBytes

    @MaxMessageBytes.setter
    def MaxMessageBytes(self, MaxMessageBytes):
        self._MaxMessageBytes = MaxMessageBytes

    @property
    def RetentionBytes(self):
        r"""Specifies the message retention file size in Bytes.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RetentionBytes

    @RetentionBytes.setter
    def RetentionBytes(self, RetentionBytes):
        self._RetentionBytes = RetentionBytes

    @property
    def LogMsgTimestampType(self):
        r"""The time type for message saving. CreateTime means the time when the producer created this message. LogAppendTime means the time when the broker received the message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LogMsgTimestampType

    @LogMsgTimestampType.setter
    def LogMsgTimestampType(self, LogMsgTimestampType):
        self._LogMsgTimestampType = LogMsgTimestampType


    def _deserialize(self, params):
        self._Retention = params.get("Retention")
        self._MinInsyncReplicas = params.get("MinInsyncReplicas")
        self._CleanUpPolicy = params.get("CleanUpPolicy")
        self._SegmentMs = params.get("SegmentMs")
        self._UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self._SegmentBytes = params.get("SegmentBytes")
        self._MaxMessageBytes = params.get("MaxMessageBytes")
        self._RetentionBytes = params.get("RetentionBytes")
        self._LogMsgTimestampType = params.get("LogMsgTimestampType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerGroup(AbstractModel):
    r"""User group entity

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
        r"""User group name
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def SubscribedInfo(self):
        r"""Subscribed message entity
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
    r"""Returned consumer group result entity

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible consumer groups
        :type TotalCount: int
        :param _TopicList: Topic list.
        :type TopicList: list of ConsumerGroupTopic
        :param _GroupList: Specifies the consumption group List.
        :type GroupList: list of ConsumerGroup
        :param _TotalPartition: Total number of partitions.
        :type TotalPartition: int
        :param _PartitionListForMonitor: Monitored partition list.
        :type PartitionListForMonitor: list of Partition
        :param _TotalTopic: Total number of topics.
        :type TotalTopic: int
        :param _TopicListForMonitor: Monitored topic list.
        :type TopicListForMonitor: list of ConsumerGroupTopic
        :param _GroupListForMonitor: Monitored group list.
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
        r"""Number of eligible consumer groups
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TopicList(self):
        r"""Topic list.
        :rtype: list of ConsumerGroupTopic
        """
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList

    @property
    def GroupList(self):
        r"""Specifies the consumption group List.
        :rtype: list of ConsumerGroup
        """
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList

    @property
    def TotalPartition(self):
        r"""Total number of partitions.
        :rtype: int
        """
        return self._TotalPartition

    @TotalPartition.setter
    def TotalPartition(self, TotalPartition):
        self._TotalPartition = TotalPartition

    @property
    def PartitionListForMonitor(self):
        r"""Monitored partition list.
        :rtype: list of Partition
        """
        return self._PartitionListForMonitor

    @PartitionListForMonitor.setter
    def PartitionListForMonitor(self, PartitionListForMonitor):
        self._PartitionListForMonitor = PartitionListForMonitor

    @property
    def TotalTopic(self):
        r"""Total number of topics.
        :rtype: int
        """
        return self._TotalTopic

    @TotalTopic.setter
    def TotalTopic(self, TotalTopic):
        self._TotalTopic = TotalTopic

    @property
    def TopicListForMonitor(self):
        r"""Monitored topic list.
        :rtype: list of ConsumerGroupTopic
        """
        return self._TopicListForMonitor

    @TopicListForMonitor.setter
    def TopicListForMonitor(self, TopicListForMonitor):
        self._TopicListForMonitor = TopicListForMonitor

    @property
    def GroupListForMonitor(self):
        r"""Monitored group list.
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
    r"""Consumer group topic object

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
        r"""Topic ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        r"""Topic name
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
    r"""Message record

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
        :param _Timestamp: Message timestamp.
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
        r"""Topic name
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        r"""Partition ID
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        r"""Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Key(self):
        r"""Message key
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Message value
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Timestamp(self):
        r"""Message timestamp.
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Headers(self):
        r"""Message headers
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
    r"""CreateAcl request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _ResourceType: ACL resource type (`2`: TOPIC, `3`: GROUP, `4`: CLUSTER).
        :type ResourceType: int
        :param _Operation: ACL operation type (`2`: ALL, `3`: READ, `4`: WRITE, `5`: CREATE, `6`: DELETE, `7`: ALTER, `8`: DESCRIBE, `9`: CLUSTER_ACTION, `10`: DESCRIBE_CONFIGS, `11`: ALTER_CONFIGS, `12`: IDEMPOTENT_WRITE).
        :type Operation: int
        :param _PermissionType: Permission type (2:DENY, 3:ALLOW). currently ckafka supports ALLOW (equivalent to allowlist), others used when compatible with open-source kafka acl.
        :type PermissionType: int
        :param _ResourceName: Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name; if `resourceType` is `CLUSTER`, this field can be left empty.
        :type ResourceName: str
        :param _Host: Defaults to *, indicating any host is accessible in the entire region. supports filling in ips or ranges, and uses ";" for separation.
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
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceType(self):
        r"""ACL resource type (`2`: TOPIC, `3`: GROUP, `4`: CLUSTER).
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Operation(self):
        r"""ACL operation type (`2`: ALL, `3`: READ, `4`: WRITE, `5`: CREATE, `6`: DELETE, `7`: ALTER, `8`: DESCRIBE, `9`: CLUSTER_ACTION, `10`: DESCRIBE_CONFIGS, `11`: ALTER_CONFIGS, `12`: IDEMPOTENT_WRITE).
        :rtype: int
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PermissionType(self):
        r"""Permission type (2:DENY, 3:ALLOW). currently ckafka supports ALLOW (equivalent to allowlist), others used when compatible with open-source kafka acl.
        :rtype: int
        """
        return self._PermissionType

    @PermissionType.setter
    def PermissionType(self, PermissionType):
        self._PermissionType = PermissionType

    @property
    def ResourceName(self):
        r"""Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name; if `resourceType` is `CLUSTER`, this field can be left empty.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Host(self):
        r"""Defaults to *, indicating any host is accessible in the entire region. supports filling in ips or ranges, and uses ";" for separation.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Principal(self):
        r"""The list of users allowed to access the topic. Default: User:*, meaning all users. The current user must be in the user list. Add `User:` before the user name (`User:A` for example).
        :rtype: str
        """
        return self._Principal

    @Principal.setter
    def Principal(self, Principal):
        self._Principal = Principal

    @property
    def ResourceNameList(self):
        r"""The resource name list, which is in JSON string format. Either `ResourceName` or `resourceNameList` can be specified.
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
    r"""CreateAcl response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateAclRuleRequest(AbstractModel):
    r"""CreateAclRule request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _ResourceType: ACL resource type. Currently, the only valid value is `Topic`.
        :type ResourceType: str
        :param _PatternType: ACL rule-based matching type. currently supports prefix match and PRESET policy. valid values: PREFIXED/PRESET.
        :type PatternType: str
        :param _RuleName: Rule name
        :type RuleName: str
        :param _RuleList: ACL rule list
        :type RuleList: list of AclRuleInfo
        :param _Pattern: Indicates the prefix for prefix match. this parameter is required when PatternType value is PREFIXED.
        :type Pattern: str
        :param _IsApplied: Specifies whether to apply the preset ACL rule to newly-added topics. defaults to 0, which means no. a value of 1 means yes.
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
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceType(self):
        r"""ACL resource type. Currently, the only valid value is `Topic`.
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def PatternType(self):
        r"""ACL rule-based matching type. currently supports prefix match and PRESET policy. valid values: PREFIXED/PRESET.
        :rtype: str
        """
        return self._PatternType

    @PatternType.setter
    def PatternType(self, PatternType):
        self._PatternType = PatternType

    @property
    def RuleName(self):
        r"""Rule name
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleList(self):
        r"""ACL rule list
        :rtype: list of AclRuleInfo
        """
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def Pattern(self):
        r"""Indicates the prefix for prefix match. this parameter is required when PatternType value is PREFIXED.
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def IsApplied(self):
        r"""Specifies whether to apply the preset ACL rule to newly-added topics. defaults to 0, which means no. a value of 1 means yes.
        :rtype: int
        """
        return self._IsApplied

    @IsApplied.setter
    def IsApplied(self, IsApplied):
        self._IsApplied = IsApplied

    @property
    def Comment(self):
        r"""Remarks for ACL rules
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
    r"""CreateAclRule response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Unique key of a rule
        :type Result: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Unique key of a rule
        :rtype: int
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


class CreateConsumerRequest(AbstractModel):
    r"""CreateConsumer request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _GroupName: Consumer group name.
        :type GroupName: str
        :param _TopicName: Topic name. one of TopicName or TopicNameList must display a specified existing topic name.
        :type TopicName: str
        :param _TopicNameList: Topic name list.
        :type TopicNameList: list of str
        """
        self._InstanceId = None
        self._GroupName = None
        self._TopicName = None
        self._TopicNameList = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupName(self):
        r"""Consumer group name.
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TopicName(self):
        r"""Topic name. one of TopicName or TopicNameList must display a specified existing topic name.
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicNameList(self):
        r"""Topic name list.
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
    r"""CreateConsumer response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Create consumer group returned results.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Create consumer group returned results.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateDatahubTopicRequest(AbstractModel):
    r"""CreateDatahubTopic request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Name, a string of no more than 128 characters, must start with "AppId-" and can contain letters, digits, and hyphens (-).
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
        r"""Name, a string of no more than 128 characters, must start with "AppId-" and can contain letters, digits, and hyphens (-).
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PartitionNum(self):
        r"""Number of partitions, which should be greater than 0.
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def RetentionMs(self):
        r"""Message retention period in milliseconds. The current minimum value is 60,000 ms.
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def Note(self):
        r"""Topic remarks, which are a string of up to 128 characters. It can contain letters, digits, and hyphens (-) and must start with a letter.
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Tags(self):
        r"""Tag list
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
    r"""CreateDatahubTopic response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned creation result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DatahubTopicResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned creation result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DatahubTopicResp`
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
            self._Result = DatahubTopicResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateInstancePostData(AbstractModel):
    r"""Data structure returned by the pay-as-you-go instance creation API

    """

    def __init__(self):
        r"""
        :param _FlowId: CreateInstancePre returns fixed as 0. it cannot be used as a query condition for CheckTaskStatus. this is merely to ensure alignment with the backend data structure.
        :type FlowId: int
        :param _DealNames: Order ID list
        :type DealNames: list of str
        :param _InstanceId: The ckafka cluster instance Id. by default, returns the Id of the first purchased instance when purchasing multiple instances.
        :type InstanceId: str
        :param _DealNameInstanceIdMapping: Order and purchase mapping list corresponding to the instance.
        :type DealNameInstanceIdMapping: list of DealInstanceDTO
        """
        self._FlowId = None
        self._DealNames = None
        self._InstanceId = None
        self._DealNameInstanceIdMapping = None

    @property
    def FlowId(self):
        r"""CreateInstancePre returns fixed as 0. it cannot be used as a query condition for CheckTaskStatus. this is merely to ensure alignment with the backend data structure.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DealNames(self):
        r"""Order ID list
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id. by default, returns the Id of the first purchased instance when purchasing multiple instances.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealNameInstanceIdMapping(self):
        r"""Order and purchase mapping list corresponding to the instance.
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
        


class CreateInstancePostResp(AbstractModel):
    r"""Data structure returned by pay-as-you-go instance APIs

    """

    def __init__(self):
        r"""
        :param _ReturnCode: Returned code. `0` indicates normal status while other codes indicate errors.
        :type ReturnCode: str
        :param _ReturnMessage: Message returned by the API. An error message will be returned if the API reports an error. 
        :type ReturnMessage: str
        :param _Data: Specifies the Data returned.
        :type Data: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePostData`
        """
        self._ReturnCode = None
        self._ReturnMessage = None
        self._Data = None

    @property
    def ReturnCode(self):
        r"""Returned code. `0` indicates normal status while other codes indicate errors.
        :rtype: str
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMessage(self):
        r"""Message returned by the API. An error message will be returned if the API reports an error. 
        :rtype: str
        """
        return self._ReturnMessage

    @ReturnMessage.setter
    def ReturnMessage(self, ReturnMessage):
        self._ReturnMessage = ReturnMessage

    @property
    def Data(self):
        r"""Specifies the Data returned.
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
        


class CreateInstancePreData(AbstractModel):
    r"""Data returned by the `CreateInstancePre` API.

    """

    def __init__(self):
        r"""
        :param _FlowId: CreateInstancePre returns fixed as 0. it cannot be used as a query condition for CheckTaskStatus. this is merely to ensure alignment with the backend data structure.
        :type FlowId: int
        :param _DealNames: Order ID list
        :type DealNames: list of str
        :param _InstanceId: The ckafka cluster instance Id. by default, returns the Id of the first purchased instance when purchasing multiple instances.
        :type InstanceId: str
        :param _DealNameInstanceIdMapping: Order and purchase mapping list corresponding to the instance.
        :type DealNameInstanceIdMapping: list of DealInstanceDTO
        """
        self._FlowId = None
        self._DealNames = None
        self._InstanceId = None
        self._DealNameInstanceIdMapping = None

    @property
    def FlowId(self):
        r"""CreateInstancePre returns fixed as 0. it cannot be used as a query condition for CheckTaskStatus. this is merely to ensure alignment with the backend data structure.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DealNames(self):
        r"""Order ID list
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id. by default, returns the Id of the first purchased instance when purchasing multiple instances.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealNameInstanceIdMapping(self):
        r"""Order and purchase mapping list corresponding to the instance.
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
        


class CreateInstancePreRequest(AbstractModel):
    r"""CreateInstancePre request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceName: Specifies the ckafka cluster instance Name, an arbitrary string with length no more than 128 characters.
        :type InstanceName: str
        :param _ZoneId: Availability zone. when purchasing a multi-availability zone instance, this parameter specifies the primary az. [view availability zones](https://www.tencentcloud.comom/document/product/597/55246?from_cn_redirect=1).
        :type ZoneId: int
        :param _Period: Prepaid purchase duration, such as "1m", exactly one month. value ranges from 1m to 36m.
        :type Period: str
        :param _InstanceType: Specifies the standard edition instance specification for the international site. currently only the international site standard edition uses the current field to distinguish specifications, while the domestic site standard edition distinguishes specifications by peak bandwidth. fill in 1 for all instances except the international site standard edition. for international site standard edition instances: [entry-level (general)] fill 1; [standard type (standard)] fill 2; [advanced] fill 3; [capacity type (capacity)] fill 4; [advanced type 1 (specialized-1)] fill 5; [advanced type 2 (specialized-2)] fill 6; [advanced type 3 (specialized-3)] fill 7; [advanced type 4 (specialized-4)] fill 8.
        :type InstanceType: int
        :param _VpcId: VPC Id.
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _MsgRetentionTime: Optional. maximum retention time of instance logs, in minutes. default value: 1440 (1 day). value range: 1 minute to 90 days.
        :type MsgRetentionTime: int
        :param _ClusterId: Specifies the cluster Id when creating an instance.
        :type ClusterId: int
        :param _RenewFlag: Auto-Renewal tag for prepaid services. valid values: 0 (default state, not set by the user, initial status), 1 (auto-renew), 2 (explicitly no auto-renew, set by the user).
        :type RenewFlag: int
        :param _KafkaVersion: Specifies the CKafka version number. valid values: 2.4.1, 2.4.2, 2.8.1, 3.2.3. default value 2.4.1. 2.4.1 and 2.4.2 belong to the same version. any can be passed.
        :type KafkaVersion: str
        :param _SpecificationsType: Specifies the instance type. valid values: standard (default), profession, premium.
        :type SpecificationsType: str
        :param _DiskSize: Disk size. if it does not match the console specification ratio, the creation cannot succeed. default value is 500. step length is set to 100. can be accessed through the following link: https://www.tencentcloud.comom/document/product/597/122562.?from_cn_redirect=1
        :type DiskSize: int
        :param _BandWidth: Instance bandwidth. default value: 40 MB/s. minimum value: 20 MB/s. maximum value for advanced edition: 360 MB/s. maximum value for pro edition: 100000 MB/s. standard version fixed bandwidth specifications: 40 MB/s, 100 MB/s, 150 MB/s. view billing specifications through the following link: https://www.tencentcloud.comom/document/product/597/11745.?from_cn_redirect=1
        :type BandWidth: int
        :param _Partition: Partition size. if it does not match the console specification ratio, creation will fail. default value is 800, step length is 100. billing specifications can be viewed through the following link: https://www.tencentcloud.comom/document/product/597/122563.?from_cn_redirect=1
        :type Partition: int
        :param _Tags: Tag.
        :type Tags: list of Tag
        :param _DiskType: Specifies the disk type for a pro/advanced edition instance. you do not need to fill it in for a standard edition instance. valid values: "CLOUD_SSD" for SSD CLOUD disk; "CLOUD_BASIC" for high-performance CLOUD block storage. default value: "CLOUD_BASIC".
        :type DiskType: str
        :param _MultiZoneFlag: Specifies whether to create a cross-az instance. when the current parameter is true, zoneIds is required.
        :type MultiZoneFlag: bool
        :param _ZoneIds: Availability zone list. required item when purchasing a multi-availability zone instance.
        :type ZoneIds: list of int
        :param _PublicNetworkMonthly: Public network bandwidth size, in Mbps. the default is no free 3 Mbps bandwidth. for example, for a total of 3 Mbps public network bandwidth, pass 0 here; for a total of 6 Mbps public network bandwidth, pass 3 here. default value is 0. ensure the input parameter is a multiple of 3.
        :type PublicNetworkMonthly: int
        :param _InstanceNum: Number of instances to purchase. optional. default value is 1. when you input this parameter, it enables the creation of multiple instances with case-sensitive suffixes added to instanceName.
        :type InstanceNum: int
        :param _AutoVoucher: Whether to automatically select a voucher. valid values: 1 (yes), 0 (no). default is 0.
        :type AutoVoucher: int
        :param _ElasticBandwidthSwitch: Elastic bandwidth switch. specifies whether to enable elastic bandwidth. valid values: 0 (not enabled, default), 1 (enabled).
        :type ElasticBandwidthSwitch: int
        """
        self._InstanceName = None
        self._ZoneId = None
        self._Period = None
        self._InstanceType = None
        self._VpcId = None
        self._SubnetId = None
        self._MsgRetentionTime = None
        self._ClusterId = None
        self._RenewFlag = None
        self._KafkaVersion = None
        self._SpecificationsType = None
        self._DiskSize = None
        self._BandWidth = None
        self._Partition = None
        self._Tags = None
        self._DiskType = None
        self._MultiZoneFlag = None
        self._ZoneIds = None
        self._PublicNetworkMonthly = None
        self._InstanceNum = None
        self._AutoVoucher = None
        self._ElasticBandwidthSwitch = None

    @property
    def InstanceName(self):
        r"""Specifies the ckafka cluster instance Name, an arbitrary string with length no more than 128 characters.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ZoneId(self):
        r"""Availability zone. when purchasing a multi-availability zone instance, this parameter specifies the primary az. [view availability zones](https://www.tencentcloud.comom/document/product/597/55246?from_cn_redirect=1).
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Period(self):
        r"""Prepaid purchase duration, such as "1m", exactly one month. value ranges from 1m to 36m.
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def InstanceType(self):
        r"""Specifies the standard edition instance specification for the international site. currently only the international site standard edition uses the current field to distinguish specifications, while the domestic site standard edition distinguishes specifications by peak bandwidth. fill in 1 for all instances except the international site standard edition. for international site standard edition instances: [entry-level (general)] fill 1; [standard type (standard)] fill 2; [advanced] fill 3; [capacity type (capacity)] fill 4; [advanced type 1 (specialized-1)] fill 5; [advanced type 2 (specialized-2)] fill 6; [advanced type 3 (specialized-3)] fill 7; [advanced type 4 (specialized-4)] fill 8.
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def VpcId(self):
        r"""VPC Id.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

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
    def MsgRetentionTime(self):
        r"""Optional. maximum retention time of instance logs, in minutes. default value: 1440 (1 day). value range: 1 minute to 90 days.
        :rtype: int
        """
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def ClusterId(self):
        r"""Specifies the cluster Id when creating an instance.
        :rtype: int
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RenewFlag(self):
        r"""Auto-Renewal tag for prepaid services. valid values: 0 (default state, not set by the user, initial status), 1 (auto-renew), 2 (explicitly no auto-renew, set by the user).
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def KafkaVersion(self):
        r"""Specifies the CKafka version number. valid values: 2.4.1, 2.4.2, 2.8.1, 3.2.3. default value 2.4.1. 2.4.1 and 2.4.2 belong to the same version. any can be passed.
        :rtype: str
        """
        return self._KafkaVersion

    @KafkaVersion.setter
    def KafkaVersion(self, KafkaVersion):
        self._KafkaVersion = KafkaVersion

    @property
    def SpecificationsType(self):
        r"""Specifies the instance type. valid values: standard (default), profession, premium.
        :rtype: str
        """
        return self._SpecificationsType

    @SpecificationsType.setter
    def SpecificationsType(self, SpecificationsType):
        self._SpecificationsType = SpecificationsType

    @property
    def DiskSize(self):
        r"""Disk size. if it does not match the console specification ratio, the creation cannot succeed. default value is 500. step length is set to 100. can be accessed through the following link: https://www.tencentcloud.comom/document/product/597/122562.?from_cn_redirect=1
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def BandWidth(self):
        r"""Instance bandwidth. default value: 40 MB/s. minimum value: 20 MB/s. maximum value for advanced edition: 360 MB/s. maximum value for pro edition: 100000 MB/s. standard version fixed bandwidth specifications: 40 MB/s, 100 MB/s, 150 MB/s. view billing specifications through the following link: https://www.tencentcloud.comom/document/product/597/11745.?from_cn_redirect=1
        :rtype: int
        """
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def Partition(self):
        r"""Partition size. if it does not match the console specification ratio, creation will fail. default value is 800, step length is 100. billing specifications can be viewed through the following link: https://www.tencentcloud.comom/document/product/597/122563.?from_cn_redirect=1
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Tags(self):
        r"""Tag.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DiskType(self):
        r"""Specifies the disk type for a pro/advanced edition instance. you do not need to fill it in for a standard edition instance. valid values: "CLOUD_SSD" for SSD CLOUD disk; "CLOUD_BASIC" for high-performance CLOUD block storage. default value: "CLOUD_BASIC".
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def MultiZoneFlag(self):
        r"""Specifies whether to create a cross-az instance. when the current parameter is true, zoneIds is required.
        :rtype: bool
        """
        return self._MultiZoneFlag

    @MultiZoneFlag.setter
    def MultiZoneFlag(self, MultiZoneFlag):
        self._MultiZoneFlag = MultiZoneFlag

    @property
    def ZoneIds(self):
        r"""Availability zone list. required item when purchasing a multi-availability zone instance.
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def PublicNetworkMonthly(self):
        r"""Public network bandwidth size, in Mbps. the default is no free 3 Mbps bandwidth. for example, for a total of 3 Mbps public network bandwidth, pass 0 here; for a total of 6 Mbps public network bandwidth, pass 3 here. default value is 0. ensure the input parameter is a multiple of 3.
        :rtype: int
        """
        return self._PublicNetworkMonthly

    @PublicNetworkMonthly.setter
    def PublicNetworkMonthly(self, PublicNetworkMonthly):
        self._PublicNetworkMonthly = PublicNetworkMonthly

    @property
    def InstanceNum(self):
        r"""Number of instances to purchase. optional. default value is 1. when you input this parameter, it enables the creation of multiple instances with case-sensitive suffixes added to instanceName.
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def AutoVoucher(self):
        r"""Whether to automatically select a voucher. valid values: 1 (yes), 0 (no). default is 0.
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def ElasticBandwidthSwitch(self):
        r"""Elastic bandwidth switch. specifies whether to enable elastic bandwidth. valid values: 0 (not enabled, default), 1 (enabled).
        :rtype: int
        """
        return self._ElasticBandwidthSwitch

    @ElasticBandwidthSwitch.setter
    def ElasticBandwidthSwitch(self, ElasticBandwidthSwitch):
        self._ElasticBandwidthSwitch = ElasticBandwidthSwitch


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._ZoneId = params.get("ZoneId")
        self._Period = params.get("Period")
        self._InstanceType = params.get("InstanceType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._MsgRetentionTime = params.get("MsgRetentionTime")
        self._ClusterId = params.get("ClusterId")
        self._RenewFlag = params.get("RenewFlag")
        self._KafkaVersion = params.get("KafkaVersion")
        self._SpecificationsType = params.get("SpecificationsType")
        self._DiskSize = params.get("DiskSize")
        self._BandWidth = params.get("BandWidth")
        self._Partition = params.get("Partition")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DiskType = params.get("DiskType")
        self._MultiZoneFlag = params.get("MultiZoneFlag")
        self._ZoneIds = params.get("ZoneIds")
        self._PublicNetworkMonthly = params.get("PublicNetworkMonthly")
        self._InstanceNum = params.get("InstanceNum")
        self._AutoVoucher = params.get("AutoVoucher")
        self._ElasticBandwidthSwitch = params.get("ElasticBandwidthSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancePreResp(AbstractModel):
    r"""Data structure returned by monthly subscribed instance APIs

    """

    def __init__(self):
        r"""
        :param _ReturnCode: Returned code. 0: Normal; other values: Error.
        :type ReturnCode: str
        :param _ReturnMessage: The message indicating whether the operation is successful.
        :type ReturnMessage: str
        :param _Data: Specifies the Data returned by the operation.
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
        r"""Returned code. 0: Normal; other values: Error.
        :rtype: str
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMessage(self):
        r"""The message indicating whether the operation is successful.
        :rtype: str
        """
        return self._ReturnMessage

    @ReturnMessage.setter
    def ReturnMessage(self, ReturnMessage):
        self._ReturnMessage = ReturnMessage

    @property
    def Data(self):
        r"""Specifies the Data returned by the operation.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def DeleteRouteTimestamp(self):
        warnings.warn("parameter `DeleteRouteTimestamp` is deprecated", DeprecationWarning) 

        r"""Deletion time.  This parameter has been deprecated and will be deleted.  Note: This field may return null, indicating that no valid values can be obtained.
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
        


class CreateInstancePreResponse(AbstractModel):
    r"""CreateInstancePre response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
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
            self._Result = CreateInstancePreResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreatePartitionRequest(AbstractModel):
    r"""CreatePartition request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _TopicName: Specifies the topic name, which can be obtained through the [DescribeTopic](https://www.tencentcloud.comom/document/product/597/40847?from_cn_redirect=1) api.
        :type TopicName: str
        :param _PartitionNum: Topic partition count. the input parameter is the number of partitions after modification rather than adding partitions. therefore, the input parameter must exceed the current topic partition count.
        :type PartitionNum: int
        """
        self._InstanceId = None
        self._TopicName = None
        self._PartitionNum = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        r"""Specifies the topic name, which can be obtained through the [DescribeTopic](https://www.tencentcloud.comom/document/product/597/40847?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionNum(self):
        r"""Topic partition count. the input parameter is the number of partitions after modification rather than adding partitions. therefore, the input parameter must exceed the current topic partition count.
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
    r"""CreatePartition response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result set
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result set
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreatePostPaidInstanceRequest(AbstractModel):
    r"""CreatePostPaidInstance request structure.

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC Id, obtain through the API [DescribeVpcs](https://www.tencentcloud.comom/document/product/215/15778?from_cn_redirect=1).
        :type VpcId: str
        :param _SubnetId: Subnet Id. can be obtained through the [DescribeSubnets](https://www.tencentcloud.comom/document/product/215/15784?from_cn_redirect=1) api.
        :type SubnetId: str
        :param _InstanceName: Specifies the cluster instance name of ckafka, an arbitrary character with length not exceeding 128.
        :type InstanceName: str
        :param _InstanceType: Specifies the standard edition instance specification for the international site. currently only the international site standard edition uses the current field to distinguish specifications, while the domestic site standard edition distinguishes specifications by peak bandwidth. fill in 1 for all instances except the international site standard edition. for international site standard edition instances: [entry-level (general)] fill 1; [standard type (standard)] fill 2; [advanced] fill 3; [capacity type (capacity)] fill 4; [advanced type 1 (specialized-1)] fill 5; [advanced type 2 (specialized-2)] fill 6; [advanced type 3 (specialized-3)] fill 7; [advanced type 4 (specialized-4)] fill 8.
        :type InstanceType: int
        :param _MsgRetentionTime: The maximum instance log retention period in minutes by default.  If this parameter is left empty, the default retention period is 1,440 minutes (1 day) to 30 days.  If the message retention period of the topic is explicitly set, it will prevail.
        :type MsgRetentionTime: int
        :param _ClusterId: Cluster ID, which can be selected when you create an instance.  You don’t need to pass in this parameter if the cluster where the instance resides is not specified.
        :type ClusterId: int
        :param _KafkaVersion: Instance version. currently supports "2.4.1", "2.4.2", "2.8.1", "3.2.3". default value "2.4.1". "2.4.1" and "2.4.2" belong to the same version. any one can be passed.
        :type KafkaVersion: str
        :param _SpecificationsType: Instance type. "standard": standard version. "profession": pro edition. (standard version is only supported on the international site. currently, the chinese site supports pro edition.).
        :type SpecificationsType: str
        :param _DiskType: Specifies the disk type for a pro edition instance. you do not need to fill it in for a standard edition instance. valid values: "CLOUD_SSD" for SSD CLOUD disk; "CLOUD_BASIC" for high-performance CLOUD block storage. default value: "CLOUD_BASIC".
        :type DiskType: str
        :param _BandWidth: Specifies the peak bandwidth of the instance private network, with a default value of 40 MB/s. for standard version, input the peak bandwidth corresponding to the current instance specifications. note that if the instance created is a pro edition instance, parameter configuration such as peak bandwidth and number of partitions should meet the billing specification of the professional edition. view billing specifications through the following link: https://www.tencentcloud.comom/document/product/597/11745.?from_cn_redirect=1
        :type BandWidth: int
        :param _DiskSize: Instance disk size. default value is 500. step length is set to 100. should meet the billing specification of the current instance. can be accessed through the following link: https://www.tencentcloud.comom/document/product/597/122562.?from_cn_redirect=1
        :type DiskSize: int
        :param _Partition: Specifies the maximum number of partitions for the instance, which should meet the billing specification of the current instance. default value is 800 with a step length of 100. the billing specification can be viewed through the following link: https://www.tencentcloud.comom/document/product/597/122563.?from_cn_redirect=1
        :type Partition: int
        :param _TopicNum: Maximum number of topics for the instance should meet the billing specification of the current instance. default value is 800, step length is set to 100.
        :type TopicNum: int
        :param _ZoneId: Specifies the availability zone of the instance. when creating a multi-az instance, this parameter is the availability zone id of the subnet where the default access point is created. ZoneId and ZoneIds cannot be empty at the same time. obtain through the API [DescribeCkafkaZone](https://www.tencentcloud.comom/document/product/597/55246?from_cn_redirect=1).
        :type ZoneId: int
        :param _MultiZoneFlag: Whether the current instance is a multi-AZ instance
        :type MultiZoneFlag: bool
        :param _ZoneIds: Specifies the multi-az id list when the instance is a multi-az instance. note that the multi-az corresponding to parameter ZoneId must be included in this parameter array. ZoneId and ZoneIds cannot be empty at the same time. you can obtain this information through the [DescribeCkafkaZone](https://www.tencentcloud.comom/document/product/597/55246?from_cn_redirect=1) api.
        :type ZoneIds: list of int
        :param _InstanceNum: The number of purchased instances.  Default value: `1`. This parameter is optional.  If it is passed in, multiple instances will be created, with their names being `instanceName` plus different suffixes.
        :type InstanceNum: int
        :param _PublicNetworkMonthly: Public network bandwidth in Mbps.  The 3 Mbps of free bandwidth is not included here by default.  For example, if you need 3 Mbps of public network bandwidth, pass in `0`; if you need 6 Mbps, pass in `3`.  The value must be an integer multiple of 3.
        :type PublicNetworkMonthly: int
        :param _Tags: Tag.
        :type Tags: list of Tag
        :param _ElasticBandwidthSwitch: Elastic bandwidth switch. valid values: 0 (disable, default), 1 (enable).
        :type ElasticBandwidthSwitch: int
        """
        self._VpcId = None
        self._SubnetId = None
        self._InstanceName = None
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
        self._Tags = None
        self._ElasticBandwidthSwitch = None

    @property
    def VpcId(self):
        r"""VPC Id, obtain through the API [DescribeVpcs](https://www.tencentcloud.comom/document/product/215/15778?from_cn_redirect=1).
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet Id. can be obtained through the [DescribeSubnets](https://www.tencentcloud.comom/document/product/215/15784?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceName(self):
        r"""Specifies the cluster instance name of ckafka, an arbitrary character with length not exceeding 128.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceType(self):
        r"""Specifies the standard edition instance specification for the international site. currently only the international site standard edition uses the current field to distinguish specifications, while the domestic site standard edition distinguishes specifications by peak bandwidth. fill in 1 for all instances except the international site standard edition. for international site standard edition instances: [entry-level (general)] fill 1; [standard type (standard)] fill 2; [advanced] fill 3; [capacity type (capacity)] fill 4; [advanced type 1 (specialized-1)] fill 5; [advanced type 2 (specialized-2)] fill 6; [advanced type 3 (specialized-3)] fill 7; [advanced type 4 (specialized-4)] fill 8.
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MsgRetentionTime(self):
        r"""The maximum instance log retention period in minutes by default.  If this parameter is left empty, the default retention period is 1,440 minutes (1 day) to 30 days.  If the message retention period of the topic is explicitly set, it will prevail.
        :rtype: int
        """
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def ClusterId(self):
        r"""Cluster ID, which can be selected when you create an instance.  You don’t need to pass in this parameter if the cluster where the instance resides is not specified.
        :rtype: int
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def KafkaVersion(self):
        r"""Instance version. currently supports "2.4.1", "2.4.2", "2.8.1", "3.2.3". default value "2.4.1". "2.4.1" and "2.4.2" belong to the same version. any one can be passed.
        :rtype: str
        """
        return self._KafkaVersion

    @KafkaVersion.setter
    def KafkaVersion(self, KafkaVersion):
        self._KafkaVersion = KafkaVersion

    @property
    def SpecificationsType(self):
        r"""Instance type. "standard": standard version. "profession": pro edition. (standard version is only supported on the international site. currently, the chinese site supports pro edition.).
        :rtype: str
        """
        return self._SpecificationsType

    @SpecificationsType.setter
    def SpecificationsType(self, SpecificationsType):
        self._SpecificationsType = SpecificationsType

    @property
    def DiskType(self):
        r"""Specifies the disk type for a pro edition instance. you do not need to fill it in for a standard edition instance. valid values: "CLOUD_SSD" for SSD CLOUD disk; "CLOUD_BASIC" for high-performance CLOUD block storage. default value: "CLOUD_BASIC".
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def BandWidth(self):
        r"""Specifies the peak bandwidth of the instance private network, with a default value of 40 MB/s. for standard version, input the peak bandwidth corresponding to the current instance specifications. note that if the instance created is a pro edition instance, parameter configuration such as peak bandwidth and number of partitions should meet the billing specification of the professional edition. view billing specifications through the following link: https://www.tencentcloud.comom/document/product/597/11745.?from_cn_redirect=1
        :rtype: int
        """
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def DiskSize(self):
        r"""Instance disk size. default value is 500. step length is set to 100. should meet the billing specification of the current instance. can be accessed through the following link: https://www.tencentcloud.comom/document/product/597/122562.?from_cn_redirect=1
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Partition(self):
        r"""Specifies the maximum number of partitions for the instance, which should meet the billing specification of the current instance. default value is 800 with a step length of 100. the billing specification can be viewed through the following link: https://www.tencentcloud.comom/document/product/597/122563.?from_cn_redirect=1
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def TopicNum(self):
        r"""Maximum number of topics for the instance should meet the billing specification of the current instance. default value is 800, step length is set to 100.
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def ZoneId(self):
        r"""Specifies the availability zone of the instance. when creating a multi-az instance, this parameter is the availability zone id of the subnet where the default access point is created. ZoneId and ZoneIds cannot be empty at the same time. obtain through the API [DescribeCkafkaZone](https://www.tencentcloud.comom/document/product/597/55246?from_cn_redirect=1).
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def MultiZoneFlag(self):
        r"""Whether the current instance is a multi-AZ instance
        :rtype: bool
        """
        return self._MultiZoneFlag

    @MultiZoneFlag.setter
    def MultiZoneFlag(self, MultiZoneFlag):
        self._MultiZoneFlag = MultiZoneFlag

    @property
    def ZoneIds(self):
        r"""Specifies the multi-az id list when the instance is a multi-az instance. note that the multi-az corresponding to parameter ZoneId must be included in this parameter array. ZoneId and ZoneIds cannot be empty at the same time. you can obtain this information through the [DescribeCkafkaZone](https://www.tencentcloud.comom/document/product/597/55246?from_cn_redirect=1) api.
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def InstanceNum(self):
        r"""The number of purchased instances.  Default value: `1`. This parameter is optional.  If it is passed in, multiple instances will be created, with their names being `instanceName` plus different suffixes.
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def PublicNetworkMonthly(self):
        r"""Public network bandwidth in Mbps.  The 3 Mbps of free bandwidth is not included here by default.  For example, if you need 3 Mbps of public network bandwidth, pass in `0`; if you need 6 Mbps, pass in `3`.  The value must be an integer multiple of 3.
        :rtype: int
        """
        return self._PublicNetworkMonthly

    @PublicNetworkMonthly.setter
    def PublicNetworkMonthly(self, PublicNetworkMonthly):
        self._PublicNetworkMonthly = PublicNetworkMonthly

    @property
    def Tags(self):
        r"""Tag.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ElasticBandwidthSwitch(self):
        r"""Elastic bandwidth switch. valid values: 0 (disable, default), 1 (enable).
        :rtype: int
        """
        return self._ElasticBandwidthSwitch

    @ElasticBandwidthSwitch.setter
    def ElasticBandwidthSwitch(self, ElasticBandwidthSwitch):
        self._ElasticBandwidthSwitch = ElasticBandwidthSwitch


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceName = params.get("InstanceName")
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
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ElasticBandwidthSwitch = params.get("ElasticBandwidthSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePostPaidInstanceResponse(AbstractModel):
    r"""CreatePostPaidInstance response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePostResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePostResp`
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
            self._Result = CreateInstancePostResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateRouteRequest(AbstractModel):
    r"""CreateRoute request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Specifies the ckafka cluster instance id. obtain through the API <a href="https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1">DescribeInstances</a>.</p>.
        :type InstanceId: str
        :param _VipType: <P>Specifies the network type of the route (3: vpc routing; 7: internal support route; 1: public network route).</p>.
        :type VipType: int
        :param _VpcId: <p>vpc network Id. required when vipType is 3.</p>.
        :type VpcId: str
        :param _SubnetId: <p>Specifies the vpc subnet id. required when vipType is 3.</p>.
        :type SubnetId: str
        :param _AccessType: <p>Access type: 0-plaintext; 1-sasl_plaintext; 3-sasl_ssl; 4-sasl_scram_sha_256; 5-sasl_scram_sha_512. defaults to 0. when vipType=3, supports 0,1,3,4,5. when vipType=7, supports 0,1,3. when vipType=1, supports 1,3.</p>.
        :type AccessType: int
        :param _AuthFlag: <P>Specifies whether access management is required. this field has been deprecated.</p>.
        :type AuthFlag: int
        :param _CallerAppid: <p>Specifies the caller appId.</p>.
        :type CallerAppid: int
        :param _PublicNetwork: <P>Public network bandwidth. required for public network route. must be a multiple of 3. no default value.</p>.
        :type PublicNetwork: int
        :param _Ip: <p>vip address.</p>.
        :type Ip: str
        :param _Note: <P>Specifies the remark information.</p>.
        :type Note: str
        :param _SecurityGroupIds: <P>Specifies the ordered list of security group associations.</p>.
        :type SecurityGroupIds: list of str
        """
        self._InstanceId = None
        self._VipType = None
        self._VpcId = None
        self._SubnetId = None
        self._AccessType = None
        self._AuthFlag = None
        self._CallerAppid = None
        self._PublicNetwork = None
        self._Ip = None
        self._Note = None
        self._SecurityGroupIds = None

    @property
    def InstanceId(self):
        r"""<p>Specifies the ckafka cluster instance id. obtain through the API <a href="https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1">DescribeInstances</a>.</p>.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VipType(self):
        r"""<P>Specifies the network type of the route (3: vpc routing; 7: internal support route; 1: public network route).</p>.
        :rtype: int
        """
        return self._VipType

    @VipType.setter
    def VipType(self, VipType):
        self._VipType = VipType

    @property
    def VpcId(self):
        r"""<p>vpc network Id. required when vipType is 3.</p>.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""<p>Specifies the vpc subnet id. required when vipType is 3.</p>.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def AccessType(self):
        r"""<p>Access type: 0-plaintext; 1-sasl_plaintext; 3-sasl_ssl; 4-sasl_scram_sha_256; 5-sasl_scram_sha_512. defaults to 0. when vipType=3, supports 0,1,3,4,5. when vipType=7, supports 0,1,3. when vipType=1, supports 1,3.</p>.
        :rtype: int
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def AuthFlag(self):
        r"""<P>Specifies whether access management is required. this field has been deprecated.</p>.
        :rtype: int
        """
        return self._AuthFlag

    @AuthFlag.setter
    def AuthFlag(self, AuthFlag):
        self._AuthFlag = AuthFlag

    @property
    def CallerAppid(self):
        r"""<p>Specifies the caller appId.</p>.
        :rtype: int
        """
        return self._CallerAppid

    @CallerAppid.setter
    def CallerAppid(self, CallerAppid):
        self._CallerAppid = CallerAppid

    @property
    def PublicNetwork(self):
        r"""<P>Public network bandwidth. required for public network route. must be a multiple of 3. no default value.</p>.
        :rtype: int
        """
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def Ip(self):
        r"""<p>vip address.</p>.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Note(self):
        r"""<P>Specifies the remark information.</p>.
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def SecurityGroupIds(self):
        r"""<P>Specifies the ordered list of security group associations.</p>.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VipType = params.get("VipType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._AccessType = params.get("AccessType")
        self._AuthFlag = params.get("AuthFlag")
        self._CallerAppid = params.get("CallerAppid")
        self._PublicNetwork = params.get("PublicNetwork")
        self._Ip = params.get("Ip")
        self._Note = params.get("Note")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRouteResponse(AbstractModel):
    r"""CreateRoute response structure.

    """

    def __init__(self):
        r"""
        :param _Result: <P>Returned result.</p>.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<P>Returned result.</p>.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateTopicIpWhiteListRequest(AbstractModel):
    r"""CreateTopicIpWhiteList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _TopicName: Specifies the topic name, which can be obtained through the [DescribeTopic](https://www.tencentcloud.comom/document/product/597/40847?from_cn_redirect=1) api.
        :type TopicName: str
        :param _IpWhiteList: Allowlist list. maximum value is 512. upper limit for incoming ips is 512.
        :type IpWhiteList: list of str
        """
        self._InstanceId = None
        self._TopicName = None
        self._IpWhiteList = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        r"""Specifies the topic name, which can be obtained through the [DescribeTopic](https://www.tencentcloud.comom/document/product/597/40847?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def IpWhiteList(self):
        r"""Allowlist list. maximum value is 512. upper limit for incoming ips is 512.
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
    r"""CreateTopicIpWhiteList response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Result of deleting topic IP allowlist
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Result of deleting topic IP allowlist
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    r"""CreateTopic request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance Id. you can obtain it by calling the DescribeInstances api.
        :type InstanceId: str
        :param _TopicName: Can only contain letters, digits, underscores, "-", or ".".
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
        :param _Note: Topic remark is a string of no more than 64 characters. the first character can be a letter or digit, and the remaining part can contain letters, digits, and hyphens (-).
        :type Note: str
        :param _MinInsyncReplicas: Minimum number of synchronous replicas, defaults to 1.
        :type MinInsyncReplicas: int
        :param _UncleanLeaderElectionEnable: Whether to allow unsynchronized replicas to be elected as leader. valid values: 0 (not allowed), 1 (allowed). default: not allowed.
        :type UncleanLeaderElectionEnable: int
        :param _RetentionMs: Optional parameter. specifies the message retention period in milliseconds. current min value is 60000. default value is 7200000 ms (2 hours). maximum value is 7776000000 ms (90 days).
        :type RetentionMs: int
        :param _SegmentMs: Duration of Segment shard scrolling in milliseconds. minimum value is 86400000 ms (1 day).
        :type SegmentMs: int
        :param _MaxMessageBytes: Maximum topic messages in Bytes. value range: 1024 (1 KB) to 12582912 (12 MB).
        :type MaxMessageBytes: int
        :param _EnableAclRule: Preset ACL rule. `1`: enable, `0`: disable. Default value: `0`.
        :type EnableAclRule: int
        :param _AclRuleName: Name of the preset ACL rule.
        :type AclRuleName: str
        :param _RetentionBytes: Optional. retain file size. defaults to -1, unit Byte. current min value is 1073741824.
        :type RetentionBytes: int
        :param _Tags: Tag list.
        :type Tags: list of Tag
        :param _LogMsgTimestampType: Time type for message saving. valid values: CreateTime/LogAppendTime.
        :type LogMsgTimestampType: str
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
        self._LogMsgTimestampType = None

    @property
    def InstanceId(self):
        r"""Instance Id. you can obtain it by calling the DescribeInstances api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        r"""Can only contain letters, digits, underscores, "-", or ".".
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionNum(self):
        r"""Number of partitions, which should be greater than 0
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def ReplicaNum(self):
        r"""Number of replicas, which cannot be higher than the number of brokers. Maximum value: 3
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def EnableWhiteList(self):
        r"""IP allowlist switch. 1: enabled, 0: disabled. Default value: 0
        :rtype: int
        """
        return self._EnableWhiteList

    @EnableWhiteList.setter
    def EnableWhiteList(self, EnableWhiteList):
        self._EnableWhiteList = EnableWhiteList

    @property
    def IpWhiteList(self):
        r"""IP allowlist list for quota limit, which is required if `enableWhileList` is 1
        :rtype: list of str
        """
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList

    @property
    def CleanUpPolicy(self):
        r"""Log cleanup policy, which is `delete` by default. `delete`: logs will be deleted by save time; `compact`: logs will be compressed by key; `compact, delete`: logs will be compressed by key and deleted by save time.
        :rtype: str
        """
        return self._CleanUpPolicy

    @CleanUpPolicy.setter
    def CleanUpPolicy(self, CleanUpPolicy):
        self._CleanUpPolicy = CleanUpPolicy

    @property
    def Note(self):
        r"""Topic remark is a string of no more than 64 characters. the first character can be a letter or digit, and the remaining part can contain letters, digits, and hyphens (-).
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def MinInsyncReplicas(self):
        r"""Minimum number of synchronous replicas, defaults to 1.
        :rtype: int
        """
        return self._MinInsyncReplicas

    @MinInsyncReplicas.setter
    def MinInsyncReplicas(self, MinInsyncReplicas):
        self._MinInsyncReplicas = MinInsyncReplicas

    @property
    def UncleanLeaderElectionEnable(self):
        r"""Whether to allow unsynchronized replicas to be elected as leader. valid values: 0 (not allowed), 1 (allowed). default: not allowed.
        :rtype: int
        """
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def RetentionMs(self):
        r"""Optional parameter. specifies the message retention period in milliseconds. current min value is 60000. default value is 7200000 ms (2 hours). maximum value is 7776000000 ms (90 days).
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def SegmentMs(self):
        r"""Duration of Segment shard scrolling in milliseconds. minimum value is 86400000 ms (1 day).
        :rtype: int
        """
        return self._SegmentMs

    @SegmentMs.setter
    def SegmentMs(self, SegmentMs):
        self._SegmentMs = SegmentMs

    @property
    def MaxMessageBytes(self):
        r"""Maximum topic messages in Bytes. value range: 1024 (1 KB) to 12582912 (12 MB).
        :rtype: int
        """
        return self._MaxMessageBytes

    @MaxMessageBytes.setter
    def MaxMessageBytes(self, MaxMessageBytes):
        self._MaxMessageBytes = MaxMessageBytes

    @property
    def EnableAclRule(self):
        r"""Preset ACL rule. `1`: enable, `0`: disable. Default value: `0`.
        :rtype: int
        """
        return self._EnableAclRule

    @EnableAclRule.setter
    def EnableAclRule(self, EnableAclRule):
        self._EnableAclRule = EnableAclRule

    @property
    def AclRuleName(self):
        r"""Name of the preset ACL rule.
        :rtype: str
        """
        return self._AclRuleName

    @AclRuleName.setter
    def AclRuleName(self, AclRuleName):
        self._AclRuleName = AclRuleName

    @property
    def RetentionBytes(self):
        r"""Optional. retain file size. defaults to -1, unit Byte. current min value is 1073741824.
        :rtype: int
        """
        return self._RetentionBytes

    @RetentionBytes.setter
    def RetentionBytes(self, RetentionBytes):
        self._RetentionBytes = RetentionBytes

    @property
    def Tags(self):
        r"""Tag list.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def LogMsgTimestampType(self):
        r"""Time type for message saving. valid values: CreateTime/LogAppendTime.
        :rtype: str
        """
        return self._LogMsgTimestampType

    @LogMsgTimestampType.setter
    def LogMsgTimestampType(self, LogMsgTimestampType):
        self._LogMsgTimestampType = LogMsgTimestampType


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
        self._LogMsgTimestampType = params.get("LogMsgTimestampType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResp(AbstractModel):
    r"""Return for topic creation

    """

    def __init__(self):
        r"""
        :param _TopicId: Topic ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        r"""Topic ID
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
    r"""CreateTopic response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned creation result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned creation result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicResp`
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
            self._Result = CreateTopicResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    r"""CreateUser request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
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
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""Username
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Password(self):
        r"""User password
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
    r"""CreateUser response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CvmAndIpInfo(AbstractModel):
    r"""CVM and IP information.

    """

    def __init__(self):
        r"""
        :param _CkafkaInstanceId: The ckafka cluster instance Id.
        :type CkafkaInstanceId: str
        :param _InstanceId: CVM instance ID (ins-test) or POD IP (10.0.0.30).
        :type InstanceId: str
        :param _Ip: IP address.
        :type Ip: str
        """
        self._CkafkaInstanceId = None
        self._InstanceId = None
        self._Ip = None

    @property
    def CkafkaInstanceId(self):
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._CkafkaInstanceId

    @CkafkaInstanceId.setter
    def CkafkaInstanceId(self, CkafkaInstanceId):
        self._CkafkaInstanceId = CkafkaInstanceId

    @property
    def InstanceId(self):
        r"""CVM instance ID (ins-test) or POD IP (10.0.0.30).
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        r"""IP address.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip


    def _deserialize(self, params):
        self._CkafkaInstanceId = params.get("CkafkaInstanceId")
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatahubTopicDTO(AbstractModel):
    r"""DataHub topic

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
        :param _RetentionMs: Expiration time in milliseconds.
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
        r"""Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TopicName(self):
        r"""Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        r"""Topic ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionNum(self):
        r"""The number of partitions
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def RetentionMs(self):
        r"""Expiration time in milliseconds.
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def Note(self):
        r"""Remarks
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Status(self):
        r"""Status (`1`: In use; `2`: Deleting)
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
    r"""DataHub topic response

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name
        :type TopicName: str
        :param _TopicId: Topic Id.
        :type TopicId: str
        """
        self._TopicName = None
        self._TopicId = None

    @property
    def TopicName(self):
        r"""Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        r"""Topic Id.
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
    r"""Mapping between orders and CKafka instances for monthly subscribed and pay-as-you-go instance APIs.

    """

    def __init__(self):
        r"""
        :param _DealName: Order transaction.
        :type DealName: str
        :param _InstanceIdList: Order transaction corresponds to the list of purchased CKafka instance ids.
        :type InstanceIdList: list of str
        """
        self._DealName = None
        self._InstanceIdList = None

    @property
    def DealName(self):
        r"""Order transaction.
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def InstanceIdList(self):
        r"""Order transaction corresponds to the list of purchased CKafka instance ids.
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
    r"""DeleteAcl request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _ResourceType: ACL resource type (`2`: TOPIC, `3`: GROUP, `4`: CLUSTER).
        :type ResourceType: int
        :param _ResourceName: Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name; if `resourceType` is `CLUSTER`, this field can be left empty.
        :type ResourceName: str
        :param _Operation: ACL operation type (`2`: ALL, `3`: READ, `4`: WRITE, `5`: CREATE, `6`: DELETE, `7`: ALTER, `8`: DESCRIBE, `9`: CLUSTER_ACTION, `10`: DESCRIBE_CONFIGS, `11`: ALTER_CONFIGS, `12`: IDEMPOTENT_WRITE).
        :type Operation: int
        :param _PermissionType: Permission type (2:DENY, 3:ALLOW). currently ckafka supports ALLOW (equivalent to allowlist), others used when compatible with open-source kafka acl.
        :type PermissionType: int
        :param _Host: The default value is `*`, which means that any host can access. Currently, CKafka does not support the host as `*`, but the future product based on the open-source Kafka will directly support this
        :type Host: str
        :param _Principal: List of users, defaults to User:*, means any User is accessible in the entire region. the current User can only be the User in the list of users.
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
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceType(self):
        r"""ACL resource type (`2`: TOPIC, `3`: GROUP, `4`: CLUSTER).
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        r"""Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name; if `resourceType` is `CLUSTER`, this field can be left empty.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Operation(self):
        r"""ACL operation type (`2`: ALL, `3`: READ, `4`: WRITE, `5`: CREATE, `6`: DELETE, `7`: ALTER, `8`: DESCRIBE, `9`: CLUSTER_ACTION, `10`: DESCRIBE_CONFIGS, `11`: ALTER_CONFIGS, `12`: IDEMPOTENT_WRITE).
        :rtype: int
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PermissionType(self):
        r"""Permission type (2:DENY, 3:ALLOW). currently ckafka supports ALLOW (equivalent to allowlist), others used when compatible with open-source kafka acl.
        :rtype: int
        """
        return self._PermissionType

    @PermissionType.setter
    def PermissionType(self, PermissionType):
        self._PermissionType = PermissionType

    @property
    def Host(self):
        r"""The default value is `*`, which means that any host can access. Currently, CKafka does not support the host as `*`, but the future product based on the open-source Kafka will directly support this
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Principal(self):
        r"""List of users, defaults to User:*, means any User is accessible in the entire region. the current User can only be the User in the list of users.
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
    r"""DeleteAcl response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteAclRuleRequest(AbstractModel):
    r"""DeleteAclRule request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance id information. you can obtain it through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _RuleName: acl rule name, obtain through the API DescribeAclRule.
        :type RuleName: str
        """
        self._InstanceId = None
        self._RuleName = None

    @property
    def InstanceId(self):
        r"""Instance id information. you can obtain it through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleName(self):
        r"""acl rule name, obtain through the API DescribeAclRule.
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAclRuleResponse(AbstractModel):
    r"""DeleteAclRule response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returns the rule ID of the deleted rule.
        :type Result: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returns the rule ID of the deleted rule.
        :rtype: int
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


class DeleteGroupRequest(AbstractModel):
    r"""DeleteGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id. can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _Group: Consumer group name, which can be obtained through the DescribeConsumerGroup API (https://www.tencentcloud.comom/document/product/597/40841?from_cn_redirect=1).
        :type Group: str
        """
        self._InstanceId = None
        self._Group = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id. can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Group(self):
        r"""Consumer group name, which can be obtained through the DescribeConsumerGroup API (https://www.tencentcloud.comom/document/product/597/40841?from_cn_redirect=1).
        :rtype: str
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Group = params.get("Group")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupResponse(AbstractModel):
    r"""DeleteGroup response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned results.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned results.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteInstancePostRequest(AbstractModel):
    r"""DeleteInstancePost request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
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
        


class DeleteInstancePostResponse(AbstractModel):
    r"""DeleteInstancePost response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceDeleteResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceDeleteResponse`
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
            self._Result = InstanceDeleteResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteInstancePreRequest(AbstractModel):
    r"""DeleteInstancePre request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
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
    r"""DeleteInstancePre response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
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
            self._Result = CreateInstancePreResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteRouteRequest(AbstractModel):
    r"""DeleteRoute request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
        :type InstanceId: str
        :param _RouteId: Route id, obtain through the API [DescribeRoute](https://www.tencentcloud.comom/document/product/597/45484?from_cn_redirect=1).
        :type RouteId: int
        :param _CallerAppid: AppId of the caller.
        :type CallerAppid: int
        :param _DeleteRouteTime: Sets the scheduled deletion time for routes. only public network routes support scheduled deletion. available for any time within the next 24 hours.
        :type DeleteRouteTime: str
        """
        self._InstanceId = None
        self._RouteId = None
        self._CallerAppid = None
        self._DeleteRouteTime = None

    @property
    def InstanceId(self):
        r"""ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RouteId(self):
        r"""Route id, obtain through the API [DescribeRoute](https://www.tencentcloud.comom/document/product/597/45484?from_cn_redirect=1).
        :rtype: int
        """
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId

    @property
    def CallerAppid(self):
        r"""AppId of the caller.
        :rtype: int
        """
        return self._CallerAppid

    @CallerAppid.setter
    def CallerAppid(self, CallerAppid):
        self._CallerAppid = CallerAppid

    @property
    def DeleteRouteTime(self):
        r"""Sets the scheduled deletion time for routes. only public network routes support scheduled deletion. available for any time within the next 24 hours.
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
    r"""DeleteRoute response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteRouteTriggerTimeRequest(AbstractModel):
    r"""DeleteRouteTriggerTime request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
        :type InstanceId: str
        :param _DelayTime: Modifies the scheduled time for deleting routes.
        :type DelayTime: str
        """
        self._InstanceId = None
        self._DelayTime = None

    @property
    def InstanceId(self):
        r"""ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DelayTime(self):
        r"""Modifies the scheduled time for deleting routes.
        :rtype: str
        """
        return self._DelayTime

    @DelayTime.setter
    def DelayTime(self, DelayTime):
        self._DelayTime = DelayTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DelayTime = params.get("DelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRouteTriggerTimeResponse(AbstractModel):
    r"""DeleteRouteTriggerTime response structure.

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


class DeleteTopicIpWhiteListRequest(AbstractModel):
    r"""DeleteTopicIpWhiteList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _TopicName: Specifies the topic name, which can be obtained through the [DescribeTopic](https://www.tencentcloud.comom/document/product/597/40847?from_cn_redirect=1) api.
        :type TopicName: str
        :param _IpWhiteList: IP allowlist list
        :type IpWhiteList: list of str
        """
        self._InstanceId = None
        self._TopicName = None
        self._IpWhiteList = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        r"""Specifies the topic name, which can be obtained through the [DescribeTopic](https://www.tencentcloud.comom/document/product/597/40847?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def IpWhiteList(self):
        r"""IP allowlist list
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
    r"""DeleteTopicIpWhiteList response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Result of deleting topic IP allowlist
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Result of deleting topic IP allowlist
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    r"""DeleteTopic request structure.

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
        r"""CKafka instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        r"""CKafka topic name
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
    r"""DeleteTopic response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result set
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result set
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    r"""DeleteUser request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _Name: Specifies the username, which can be obtained through the [DescribeUser](https://www.tencentcloud.comom/document/product/597/40855?from_cn_redirect=1) api.
        :type Name: str
        """
        self._InstanceId = None
        self._Name = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""Specifies the username, which can be obtained through the [DescribeUser](https://www.tencentcloud.comom/document/product/597/40855?from_cn_redirect=1) api.
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
    r"""DeleteUser response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeACLRequest(AbstractModel):
    r"""DescribeACL request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _ResourceType: ACL resource type (`2`: TOPIC, `3`: GROUP, `4`: CLUSTER).
        :type ResourceType: int
        :param _ResourceName: Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name; if `resourceType` is `CLUSTER`, this field can be left empty.
        :type ResourceName: str
        :param _Offset: Offset position
        :type Offset: int
        :param _Limit: Number limit. default value is 50. maximum value is 50.
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
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceType(self):
        r"""ACL resource type (`2`: TOPIC, `3`: GROUP, `4`: CLUSTER).
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        r"""Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name; if `resourceType` is `CLUSTER`, this field can be left empty.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Offset(self):
        r"""Offset position
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number limit. default value is 50. maximum value is 50.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchWord(self):
        r"""Keyword match
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
    r"""DescribeACL response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned ACL result set object
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AclResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned ACL result set object
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.AclResponse`
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
            self._Result = AclResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeAclRuleRequest(AbstractModel):
    r"""DescribeAclRule request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _RuleName: ACL rule name
        :type RuleName: str
        :param _PatternType: ACL rule-based matching type (PREFIXED: prefix match, PRESET: PRESET policy).
        :type PatternType: str
        :param _IsSimplified: Specifies whether to read the simplified ACL rule. default value is false, which means not to read the simplified ACL rule.
        :type IsSimplified: bool
        """
        self._InstanceId = None
        self._RuleName = None
        self._PatternType = None
        self._IsSimplified = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleName(self):
        r"""ACL rule name
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def PatternType(self):
        r"""ACL rule-based matching type (PREFIXED: prefix match, PRESET: PRESET policy).
        :rtype: str
        """
        return self._PatternType

    @PatternType.setter
    def PatternType(self, PatternType):
        self._PatternType = PatternType

    @property
    def IsSimplified(self):
        r"""Specifies whether to read the simplified ACL rule. default value is false, which means not to read the simplified ACL rule.
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
    r"""DescribeAclRule response structure.

    """

    def __init__(self):
        r"""
        :param _Result: The set of returned ACL rules
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AclRuleResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""The set of returned ACL rules
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.AclRuleResp`
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
            self._Result = AclRuleResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCkafkaVersionRequest(AbstractModel):
    r"""DescribeCkafkaVersion request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id.
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
        


class DescribeCkafkaVersionResponse(AbstractModel):
    r"""DescribeCkafkaVersion response structure.

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


class DescribeCkafkaZoneRequest(AbstractModel):
    r"""DescribeCkafkaZone request structure.

    """

    def __init__(self):
        r"""
        :param _CdcId: cdc cluster Id.
        :type CdcId: str
        """
        self._CdcId = None

    @property
    def CdcId(self):
        r"""cdc cluster Id.
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
    r"""DescribeCkafkaZone response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned results for the query
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ZoneResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned results for the query
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ZoneResponse`
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
            self._Result = ZoneResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeConnectInfoResultDTO(AbstractModel):
    r"""Topic connection information

    """

    def __init__(self):
        r"""
        :param _IpAddr: IP address
Note: This field may return null, indicating that no valid values can be obtained.
        :type IpAddr: str
        :param _Time: Connection time
Note: This field may return null, indicating that no valid values can be obtained.
        :type Time: str
        :param _IsUnSupportVersion: Specifies whether supported versions are required or not.
        :type IsUnSupportVersion: bool
        """
        self._IpAddr = None
        self._Time = None
        self._IsUnSupportVersion = None

    @property
    def IpAddr(self):
        r"""IP address
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IpAddr

    @IpAddr.setter
    def IpAddr(self, IpAddr):
        self._IpAddr = IpAddr

    @property
    def Time(self):
        r"""Connection time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def IsUnSupportVersion(self):
        r"""Specifies whether supported versions are required or not.
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
    r"""DescribeConsumerGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
        :type InstanceId: str
        :param _GroupName: Specifies the group name you want to query.
        :type GroupName: str
        :param _TopicName: Specifies the corresponding topic name in the group to be queried by the user. if this parameter is specified while the group is unspecified, ignore this parameter.
        :type TopicName: str
        :param _Limit: Returns the limit quantity of the consumption group. supports a maximum of 50.
        :type Limit: int
        :param _Offset: Specifies the starting offset amount of the consumer group list.
        :type Offset: int
        """
        self._InstanceId = None
        self._GroupName = None
        self._TopicName = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupName(self):
        r"""Specifies the group name you want to query.
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TopicName(self):
        r"""Specifies the corresponding topic name in the group to be queried by the user. if this parameter is specified while the group is unspecified, ignore this parameter.
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Limit(self):
        r"""Returns the limit quantity of the consumption group. supports a maximum of 50.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Specifies the starting offset amount of the consumer group list.
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
    r"""DescribeConsumerGroup response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned consumer group information
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConsumerGroupResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned consumer group information
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ConsumerGroupResponse`
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
            self._Result = ConsumerGroupResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCvmInfoRequest(AbstractModel):
    r"""DescribeCvmInfo request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
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
        


class DescribeCvmInfoResponse(AbstractModel):
    r"""DescribeCvmInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ListCvmAndIpInfoRsp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ListCvmAndIpInfoRsp`
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
            self._Result = ListCvmAndIpInfoRsp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDatahubTopicRequest(AbstractModel):
    r"""DescribeDatahubTopic request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Elastic topic name.
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        r"""Elastic topic name.
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
    r"""DataHub topic details

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
        :param _RetentionMs: Expiration time in milliseconds.
        :type RetentionMs: int
        :param _Note: Remarks.
        :type Note: str
        :param _UserName: Username
        :type UserName: str
        :param _Password: Password
        :type Password: str
        :param _Status: Status (`1`: In use; `2`: Deleting)
        :type Status: int
        :param _Address: Specifies the service routing address.
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
        r"""Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TopicName(self):
        r"""Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        r"""Topic ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionNum(self):
        r"""The number of partitions
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def RetentionMs(self):
        r"""Expiration time in milliseconds.
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def Note(self):
        r"""Remarks.
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def UserName(self):
        r"""Username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""Password
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Status(self):
        r"""Status (`1`: In use; `2`: Deleting)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Address(self):
        r"""Specifies the service routing address.
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
    r"""DescribeDatahubTopic response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result object
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result object
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicResp`
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
            self._Result = DescribeDatahubTopicResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDatahubTopicsRequest(AbstractModel):
    r"""DescribeDatahubTopics request structure.

    """

    def __init__(self):
        r"""
        :param _SearchWord: Search term.
        :type SearchWord: str
        :param _Offset: Query offset, which defaults to `0`.
        :type Offset: int
        :param _Limit: Maximum number of results to be returned in this request. Default value: `50`. Maximum value: `50`.
        :type Limit: int
        :param _QueryFromConnectResource: Specifies whether to query the topic list from the connection.
        :type QueryFromConnectResource: bool
        :param _ConnectResourceId: Connection ID.
        :type ConnectResourceId: str
        :param _TopicRegularExpression: topic resource expression.
        :type TopicRegularExpression: str
        """
        self._SearchWord = None
        self._Offset = None
        self._Limit = None
        self._QueryFromConnectResource = None
        self._ConnectResourceId = None
        self._TopicRegularExpression = None

    @property
    def SearchWord(self):
        r"""Search term.
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        r"""Query offset, which defaults to `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Maximum number of results to be returned in this request. Default value: `50`. Maximum value: `50`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def QueryFromConnectResource(self):
        r"""Specifies whether to query the topic list from the connection.
        :rtype: bool
        """
        return self._QueryFromConnectResource

    @QueryFromConnectResource.setter
    def QueryFromConnectResource(self, QueryFromConnectResource):
        self._QueryFromConnectResource = QueryFromConnectResource

    @property
    def ConnectResourceId(self):
        r"""Connection ID.
        :rtype: str
        """
        return self._ConnectResourceId

    @ConnectResourceId.setter
    def ConnectResourceId(self, ConnectResourceId):
        self._ConnectResourceId = ConnectResourceId

    @property
    def TopicRegularExpression(self):
        r"""topic resource expression.
        :rtype: str
        """
        return self._TopicRegularExpression

    @TopicRegularExpression.setter
    def TopicRegularExpression(self, TopicRegularExpression):
        self._TopicRegularExpression = TopicRegularExpression


    def _deserialize(self, params):
        self._SearchWord = params.get("SearchWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._QueryFromConnectResource = params.get("QueryFromConnectResource")
        self._ConnectResourceId = params.get("ConnectResourceId")
        self._TopicRegularExpression = params.get("TopicRegularExpression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatahubTopicsResp(AbstractModel):
    r"""DataHub topic list

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total count
        :type TotalCount: int
        :param _TopicList: Topic list.
        :type TopicList: list of DatahubTopicDTO
        """
        self._TotalCount = None
        self._TopicList = None

    @property
    def TotalCount(self):
        r"""Total count
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TopicList(self):
        r"""Topic list.
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
    r"""DescribeDatahubTopics response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Topic list.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicsResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Topic list.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicsResp`
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
            self._Result = DescribeDatahubTopicsResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeGroup(AbstractModel):
    r"""`DescribeGroup` response entity

    """

    def __init__(self):
        r"""
        :param _Group: Consumer group name.
        :type Group: str
        :param _Protocol: Protocol used by the group.
        :type Protocol: str
        """
        self._Group = None
        self._Protocol = None

    @property
    def Group(self):
        r"""Consumer group name.
        :rtype: str
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Protocol(self):
        r"""Protocol used by the group.
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
    r"""DescribeGroupInfo request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
        :type InstanceId: str
        :param _GroupList: Kafka group list. obtain through the API [DescribeConsumerGroup](https://www.tencentcloud.comom/document/product/597/40841?from_cn_redirect=1).
        :type GroupList: list of str
        """
        self._InstanceId = None
        self._GroupList = None

    @property
    def InstanceId(self):
        r"""ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupList(self):
        r"""Kafka group list. obtain through the API [DescribeConsumerGroup](https://www.tencentcloud.comom/document/product/597/40841?from_cn_redirect=1).
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
    r"""DescribeGroupInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: list of GroupInfoResponse
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result.
        :rtype: list of GroupInfoResponse
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
            self._Result = []
            for item in params.get("Result"):
                obj = GroupInfoResponse()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGroupOffsetsRequest(AbstractModel):
    r"""DescribeGroupOffsets request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id.
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
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Group(self):
        r"""Kafka consumer group
        :rtype: str
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Topics(self):
        r"""Array of the names of topics subscribed to by a group. If there is no such array, this parameter means the information of all topics in the specified group
        :rtype: list of str
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def SearchWord(self):
        r"""Fuzzy match by `topicName`
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        r"""Offset position of this query. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Maximum number of results to be returned in this request. Default value: 50. Maximum value: 50
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
    r"""DescribeGroupOffsets response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupOffsetResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.GroupOffsetResponse`
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
            self._Result = GroupOffsetResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeGroupRequest(AbstractModel):
    r"""DescribeGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id.
        :type InstanceId: str
        :param _SearchWord: Search keyword
        :type SearchWord: str
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Maximum number of results to be returned
        :type Limit: int
        :param _Filters: Only supported for GroupState filter criteria. valid values: Empty, Stable. note: this parameter can only be accessed in versions 2.8/3.2.
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        r"""Search keyword
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        r"""Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Maximum number of results to be returned
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""Only supported for GroupState filter criteria. valid values: Empty, Stable. note: this parameter can only be accessed in versions 2.8/3.2.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchWord = params.get("SearchWord")
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
        


class DescribeGroupResponse(AbstractModel):
    r"""DescribeGroup response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.GroupResponse`
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
            self._Result = GroupResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceAttributesRequest(AbstractModel):
    r"""DescribeInstanceAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
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
    r"""DescribeInstanceAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result object of instance attributes
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceAttributesResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result object of instance attributes
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceAttributesResponse`
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
            self._Result = InstanceAttributesResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeInstancesDetailRequest(AbstractModel):
    r"""DescribeInstancesDetail request structure.

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
        r"""(Filter) filter by instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        r"""Filter by instance name, instance ID, AZ, VPC ID, or subnet ID. Fuzzy query is supported.
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Status(self):
        r"""(Filter) instance status. 0: creating, 1: running, 2: deleting. If this parameter is left empty, all instances will be returned by default
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        r"""Offset. If this parameter is left empty, `0` will be used by default.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of returned results. If this parameter is left empty, `10` will be used by default. The maximum value is `20`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TagKey(self):
        r"""Tag key match.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def Filters(self):
        r"""Filter. Valid values of `filter.Name` include `Ip`, `VpcId`, `SubNetId`, `InstanceType`, and `InstanceId`. Up to 10 values can be passed for `filter.Values`.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def InstanceIds(self):
        warnings.warn("parameter `InstanceIds` is deprecated", DeprecationWarning) 

        r"""This parameter has been deprecated and replaced with `InstanceIdList`.
        :rtype: str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        warnings.warn("parameter `InstanceIds` is deprecated", DeprecationWarning) 

        self._InstanceIds = InstanceIds

    @property
    def InstanceIdList(self):
        r"""Filter by instance ID.
        :rtype: list of str
        """
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

    @property
    def TagList(self):
        r"""Filter instances by a set of tags
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
    r"""DescribeInstancesDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result object of instance details
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceDetailResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result object of instance details
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceDetailResponse`
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
            self._Result = InstanceDetailResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    r"""DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: (Query condition) filter by the ckafka cluster instance Id.
        :type InstanceId: str
        :param _SearchWord: Search term. example: (query condition) filter by instance name. fuzzy query is supported.
        :type SearchWord: str
        :param _Status: Instance status (query condition). valid values: 0: creating, 1: running, 2: deleting, 5: isolated, 7: upgrading. default return: all.
        :type Status: list of int
        :param _Offset: Offset. If this parameter is left empty, 0 will be used by default
        :type Offset: int
        :param _Limit: Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 100.
        :type Limit: int
        :param _TagKey: Tag key value (this field has been deprecated).
        :type TagKey: str
        :param _VpcId: (Query condition) VPC Id.
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
        r"""(Query condition) filter by the ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        r"""Search term. example: (query condition) filter by instance name. fuzzy query is supported.
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Status(self):
        r"""Instance status (query condition). valid values: 0: creating, 1: running, 2: deleting, 5: isolated, 7: upgrading. default return: all.
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        r"""Offset. If this parameter is left empty, 0 will be used by default
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TagKey(self):
        warnings.warn("parameter `TagKey` is deprecated", DeprecationWarning) 

        r"""Tag key value (this field has been deprecated).
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        warnings.warn("parameter `TagKey` is deprecated", DeprecationWarning) 

        self._TagKey = TagKey

    @property
    def VpcId(self):
        r"""(Query condition) VPC Id.
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
    r"""DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceResponse`
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
            self._Result = InstanceResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeRegionRequest(AbstractModel):
    r"""DescribeRegion request structure.

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
        r"""The offset value
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""The maximum number of results returned
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Business(self):
        r"""Business field, which can be ignored.
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def CdcId(self):
        r"""CDC business field, which can be ignored.
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
    r"""DescribeRegion response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returns the region enumeration result list.
        :type Result: list of Region
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returns the region enumeration result list.
        :rtype: list of Region
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
            self._Result = []
            for item in params.get("Result"):
                obj = Region()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRouteRequest(AbstractModel):
    r"""DescribeRoute request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id.
        :type InstanceId: str
        :param _RouteId: Route ID
        :type RouteId: int
        :param _MainRouteFlag: Specifies whether to display the primary route. when true, the routing list will additionally display the primary route information during instance creation (not affected by InternalFlag or UsedFor parameter filtering).	
        :type MainRouteFlag: bool
        """
        self._InstanceId = None
        self._RouteId = None
        self._MainRouteFlag = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RouteId(self):
        r"""Route ID
        :rtype: int
        """
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId

    @property
    def MainRouteFlag(self):
        r"""Specifies whether to display the primary route. when true, the routing list will additionally display the primary route information during instance creation (not affected by InternalFlag or UsedFor parameter filtering).	
        :rtype: bool
        """
        return self._MainRouteFlag

    @MainRouteFlag.setter
    def MainRouteFlag(self, MainRouteFlag):
        self._MainRouteFlag = MainRouteFlag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RouteId = params.get("RouteId")
        self._MainRouteFlag = params.get("MainRouteFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteResponse(AbstractModel):
    r"""DescribeRoute response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result set of route information
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.RouteResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result set of route information
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.RouteResponse`
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
            self._Result = RouteResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeSecurityGroupRoutesRequest(AbstractModel):
    r"""DescribeSecurityGroupRoutes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceRoute: Specifies the routing information.
        :type InstanceRoute: :class:`tencentcloud.ckafka.v20190819.models.InstanceRoute`
        :param _Filters: Filter.
        :type Filters: list of RouteFilter
        :param _Offset: Specifies the pagination Offset. default is 0.
        :type Offset: int
        :param _Limit: Pagination Limit. default: 20.
        :type Limit: int
        :param _SearchWord: Keyword. specifies fuzzy search by instance id, instance name, or vip.
        :type SearchWord: str
        """
        self._InstanceRoute = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._SearchWord = None

    @property
    def InstanceRoute(self):
        r"""Specifies the routing information.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceRoute`
        """
        return self._InstanceRoute

    @InstanceRoute.setter
    def InstanceRoute(self, InstanceRoute):
        self._InstanceRoute = InstanceRoute

    @property
    def Filters(self):
        r"""Filter.
        :rtype: list of RouteFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""Specifies the pagination Offset. default is 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Pagination Limit. default: 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchWord(self):
        r"""Keyword. specifies fuzzy search by instance id, instance name, or vip.
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord


    def _deserialize(self, params):
        if params.get("InstanceRoute") is not None:
            self._InstanceRoute = InstanceRoute()
            self._InstanceRoute._deserialize(params.get("InstanceRoute"))
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = RouteFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
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
        


class DescribeSecurityGroupRoutesResponse(AbstractModel):
    r"""DescribeSecurityGroupRoutes response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returns the security group routing information result object.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.SecurityGroupRouteResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returns the security group routing information result object.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.SecurityGroupRouteResp`
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
            self._Result = SecurityGroupRouteResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    r"""DescribeTaskStatus request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID.
        :type FlowId: int
        """
        self._FlowId = None

    @property
    def FlowId(self):
        r"""Flow ID.
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
    r"""DescribeTaskStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TaskStatusResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TaskStatusResponse`
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
            self._Result = TaskStatusResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTopicAttributesRequest(AbstractModel):
    r"""DescribeTopicAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _TopicName: Specifies the topic name, which can be obtained through the [DescribeTopic](https://www.tencentcloud.comom/document/product/597/40847?from_cn_redirect=1) api.
        :type TopicName: str
        """
        self._InstanceId = None
        self._TopicName = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        r"""Specifies the topic name, which can be obtained through the [DescribeTopic](https://www.tencentcloud.comom/document/product/597/40847?from_cn_redirect=1) api.
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
    r"""DescribeTopicAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result object
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicAttributesResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result object
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicAttributesResponse`
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
            self._Result = TopicAttributesResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTopicDetailRequest(AbstractModel):
    r"""DescribeTopicDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _SearchWord: (Filter) filter by `topicName`. Fuzzy search is supported
        :type SearchWord: str
        :param _Offset: Offset. If this parameter is left empty, 0 will be used by default
        :type Offset: int
        :param _Limit: Number of returned results. default: 20. value must be above 0.
        :type Limit: int
        :param _AclRuleName: Name of the preset ACL rule.
        :type AclRuleName: str
        :param _OrderBy: Sorts based on specific attributes (currently supports PartitionNum/CreateTime). default value: CreateTime.
        :type OrderBy: str
        :param _OrderType: 0 - sequential, 1 - reverse order. default value: 0.
        :type OrderType: int
        :param _Filters: Currently supports ReplicaNum (number of replicas) filter criteria.
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Offset = None
        self._Limit = None
        self._AclRuleName = None
        self._OrderBy = None
        self._OrderType = None
        self._Filters = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        r"""(Filter) filter by `topicName`. Fuzzy search is supported
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        r"""Offset. If this parameter is left empty, 0 will be used by default
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of returned results. default: 20. value must be above 0.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AclRuleName(self):
        r"""Name of the preset ACL rule.
        :rtype: str
        """
        return self._AclRuleName

    @AclRuleName.setter
    def AclRuleName(self, AclRuleName):
        self._AclRuleName = AclRuleName

    @property
    def OrderBy(self):
        r"""Sorts based on specific attributes (currently supports PartitionNum/CreateTime). default value: CreateTime.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        r"""0 - sequential, 1 - reverse order. default value: 0.
        :rtype: int
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def Filters(self):
        r"""Currently supports ReplicaNum (number of replicas) filter criteria.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchWord = params.get("SearchWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AclRuleName = params.get("AclRuleName")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
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
        


class DescribeTopicDetailResponse(AbstractModel):
    r"""DescribeTopicDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned entity of topic details
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicDetailResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned entity of topic details
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicDetailResponse`
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
            self._Result = TopicDetailResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTopicProduceConnectionRequest(AbstractModel):
    r"""DescribeTopicProduceConnection request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _TopicName: Specifies the topic name, which can be obtained through the [DescribeTopic](https://www.tencentcloud.comom/document/product/597/40847?from_cn_redirect=1) api.
        :type TopicName: str
        """
        self._InstanceId = None
        self._TopicName = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        r"""Specifies the topic name, which can be obtained through the [DescribeTopic](https://www.tencentcloud.comom/document/product/597/40847?from_cn_redirect=1) api.
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
    r"""DescribeTopicProduceConnection response structure.

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
        r"""Result set of returned connection information
        :rtype: list of DescribeConnectInfoResultDTO
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
            self._Result = []
            for item in params.get("Result"):
                obj = DescribeConnectInfoResultDTO()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopicRequest(AbstractModel):
    r"""DescribeTopic request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id.
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
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        r"""Filter by `topicName`. Fuzzy search is supported
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        r"""Offset. If this parameter is left empty, 0 will be used by default
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""The number of results to be returned, which defaults to 20 if left empty. The maximum value is 50.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AclRuleName(self):
        r"""Name of the preset ACL rule.
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
    r"""DescribeTopic response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicResult`
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
            self._Result = TopicResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTopicSubscribeGroupRequest(AbstractModel):
    r"""DescribeTopicSubscribeGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id.
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
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        r"""Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Offset(self):
        r"""Starting position of paging
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of results per page
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
    r"""DescribeTopicSubscribeGroup response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned results
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicSubscribeGroup`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned results
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicSubscribeGroup`
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
            self._Result = TopicSubscribeGroup()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTopicSyncReplicaRequest(AbstractModel):
    r"""DescribeTopicSyncReplica request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _TopicName: Topic name
        :type TopicName: str
        :param _Offset: Offset. If this parameter is left empty, 0 will be used by default.
        :type Offset: int
        :param _Limit: Number of returned results. default value: 20. must be greater than 0.
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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        r"""Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Offset(self):
        r"""Offset. If this parameter is left empty, 0 will be used by default.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of returned results. default value: 20. must be greater than 0.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OutOfSyncReplicaOnly(self):
        r"""Filters unsynced replicas only
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
    r"""DescribeTopicSyncReplica response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returns topic replica details
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicInSyncReplicaResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returns topic replica details
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicInSyncReplicaResult`
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
            self._Result = TopicInSyncReplicaResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTypeInstancesRequest(AbstractModel):
    r"""DescribeTypeInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: (Filter condition) filter by instance ID.
        :type InstanceId: str
        :param _SearchWord: (Filter condition) filter by instance name. fuzzy query is supported.
        :type SearchWord: str
        :param _Status: Instance status (filter condition). valid values: 0: creating, 1: running, 2: deleting. default return: all.
        :type Status: list of int
        :param _Offset: Offset. default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. default: 10. maximum value: 100.
        :type Limit: int
        :param _TagKey: Matches the Tag key.
        :type TagKey: str
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Status = None
        self._Offset = None
        self._Limit = None
        self._TagKey = None

    @property
    def InstanceId(self):
        r"""(Filter condition) filter by instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        r"""(Filter condition) filter by instance name. fuzzy query is supported.
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Status(self):
        r"""Instance status (filter condition). valid values: 0: creating, 1: running, 2: deleting. default return: all.
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        r"""Offset. default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of returned results. default: 10. maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TagKey(self):
        r"""Matches the Tag key.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchWord = params.get("SearchWord")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TagKey = params.get("TagKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTypeInstancesResponse(AbstractModel):
    r"""DescribeTypeInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceResponse`
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
            self._Result = InstanceResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeUserRequest(AbstractModel):
    r"""DescribeUser request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id.
        :type InstanceId: str
        :param _SearchWord: Filter by name
        :type SearchWord: str
        :param _Offset: Offset.
        :type Offset: int
        :param _Limit: The number of returns.
        :type Limit: int
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        r"""Filter by name
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        r"""Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""The number of returns.
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
    r"""DescribeUser response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.UserResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.UserResponse`
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
            self._Result = UserResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DynamicDiskConfig(AbstractModel):
    r"""Dynamic disk expansion configuration

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
        r"""Whether to enable dynamic disk expansion configuration. `0`: disable, `1`: enable.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def StepForwardPercentage(self):
        r"""Percentage of dynamic disk expansion each time.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepForwardPercentage

    @StepForwardPercentage.setter
    def StepForwardPercentage(self, StepForwardPercentage):
        self._StepForwardPercentage = StepForwardPercentage

    @property
    def DiskQuotaPercentage(self):
        r"""Disk quota threshold (in percentage) for triggering the automatic disk expansion event.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskQuotaPercentage

    @DiskQuotaPercentage.setter
    def DiskQuotaPercentage(self, DiskQuotaPercentage):
        self._DiskQuotaPercentage = DiskQuotaPercentage

    @property
    def MaxDiskSpace(self):
        r"""Max disk space in GB.
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
    r"""Dynamic message retention time configuration

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
        r"""Whether the dynamic message retention time configuration is enabled. 0: disabled; 1: enabled
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def DiskQuotaPercentage(self):
        r"""Disk quota threshold (in percentage) for triggering the message retention time change event
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskQuotaPercentage

    @DiskQuotaPercentage.setter
    def DiskQuotaPercentage(self, DiskQuotaPercentage):
        self._DiskQuotaPercentage = DiskQuotaPercentage

    @property
    def StepForwardPercentage(self):
        r"""Percentage by which the message retention time is shortened each time
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepForwardPercentage

    @StepForwardPercentage.setter
    def StepForwardPercentage(self, StepForwardPercentage):
        self._StepForwardPercentage = StepForwardPercentage

    @property
    def BottomRetention(self):
        r"""Minimum retention time, in minutes
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
    r"""FetchMessageByOffset request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _Topic: Specifies the topic name, which can be obtained through the [DescribeTopic](https://www.tencentcloud.comom/document/product/597/40847?from_cn_redirect=1) api.
        :type Topic: str
        :param _Partition: Partition ID
        :type Partition: int
        :param _Offset: Specifies the position information.
        :type Offset: int
        """
        self._InstanceId = None
        self._Topic = None
        self._Partition = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id, which can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""Specifies the topic name, which can be obtained through the [DescribeTopic](https://www.tencentcloud.comom/document/product/597/40847?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        r"""Partition ID
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        r"""Specifies the position information.
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
    r"""FetchMessageByOffset response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned results
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConsumerRecord`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned results
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ConsumerRecord`
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
            self._Result = ConsumerRecord()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class FetchMessageListByOffsetRequest(AbstractModel):
    r"""FetchMessageListByOffset request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id.
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
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""Topic name
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        r"""Partition ID
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        r"""Offset information
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SinglePartitionRecordNumber(self):
        r"""The maximum number of messages that can be queried. Default value: 20. Maximum value: 20.
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
    r"""FetchMessageListByOffset response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result. Note: The returned list does not display the message content (key and value). To query the message content, call the `FetchMessageByOffset` API.
        :type Result: list of ConsumerRecord
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result. Note: The returned list does not display the message content (key and value). To query the message content, call the `FetchMessageByOffset` API.
        :rtype: list of ConsumerRecord
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
            self._Result = []
            for item in params.get("Result"):
                obj = ConsumerRecord()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class FetchMessageListByTimestampRequest(AbstractModel):
    r"""FetchMessageListByTimestamp request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id.
        :type InstanceId: str
        :param _Topic: Topic name
        :type Topic: str
        :param _Partition: Partition ID
        :type Partition: int
        :param _StartTime: Query start time, a timestamp.
        :type StartTime: int
        :param _SinglePartitionRecordNumber: Maximum number of query results. default: 20. value range: 1-20.
        :type SinglePartitionRecordNumber: int
        """
        self._InstanceId = None
        self._Topic = None
        self._Partition = None
        self._StartTime = None
        self._SinglePartitionRecordNumber = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""Topic name
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        r"""Partition ID
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def StartTime(self):
        r"""Query start time, a timestamp.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def SinglePartitionRecordNumber(self):
        r"""Maximum number of query results. default: 20. value range: 1-20.
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
        self._StartTime = params.get("StartTime")
        self._SinglePartitionRecordNumber = params.get("SinglePartitionRecordNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchMessageListByTimestampResponse(AbstractModel):
    r"""FetchMessageListByTimestamp response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned results. note that the list does not return specific message content (key, value). if necessary, please use the FetchMessageByOffset API to query specific message content.
        :type Result: list of ConsumerRecord
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned results. note that the list does not return specific message content (key, value). if necessary, please use the FetchMessageByOffset API to query specific message content.
        :rtype: list of ConsumerRecord
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
            self._Result = []
            for item in params.get("Result"):
                obj = ConsumerRecord()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    r"""Query filter.
    Describes the key-value pair filter, which is used for conditional filtering queries. for example, filter by ID, name, and status.
    If there are multiple filters, the logical relationship between them is AND.
    If the same Filter contains multiple Values, the relationship between Values under the same Filter is logical OR.
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
        r"""Field to be filtered.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""Filter value of field.
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
    r"""Group entity

    """

    def __init__(self):
        r"""
        :param _GroupName: Consumer group name.
        :type GroupName: str
        """
        self._GroupName = None

    @property
    def GroupName(self):
        r"""Consumer group name.
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
    r"""Consumer information

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
        r"""Unique ID generated for consumer in consumer group by coordinator
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def ClientId(self):
        r"""`client.id` information by the client consumer SDK
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ClientHost(self):
        r"""Generally stores client IP address
        :rtype: str
        """
        return self._ClientHost

    @ClientHost.setter
    def ClientHost(self, ClientHost):
        self._ClientHost = ClientHost

    @property
    def Assignment(self):
        r"""Stores the information of partition assigned to this consumer
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
    r"""`GroupInfo` response data entity

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
        :param _Group: Consumer group name.
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
        r"""Error code. 0: success
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def State(self):
        r"""Group status description (common valid values: Empty, Stable, Dead):
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
        r"""The type of protocol selected by the consumer group, which is `consumer` for common consumers. However, some systems use their own protocols; for example, the protocol used by kafka-connect is `connect`. Only with the standard `consumer` protocol can this API get to know the specific assigning method and parse the specific partition assignment
        :rtype: str
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def Protocol(self):
        r"""Consumer partition assignment algorithm, such as `range` (which is the default value for the Kafka consumer SDK), `roundrobin`, and `sticky`
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Members(self):
        r"""This array contains information only if `state` is `Stable` and `protocol_type` is `consumer`
        :rtype: list of GroupInfoMember
        """
        return self._Members

    @Members.setter
    def Members(self, Members):
        self._Members = Members

    @property
    def Group(self):
        r"""Consumer group name.
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
    r"""Internal topic object of `GroupInfo`

    """

    def __init__(self):
        r"""
        :param _Topic: Name of assigned topics
        :type Topic: str
        :param _Partitions: Allocates partition info.
        :type Partitions: list of int
        """
        self._Topic = None
        self._Partitions = None

    @property
    def Topic(self):
        r"""Name of assigned topics
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partitions(self):
        r"""Allocates partition info.
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
    r"""Group offset partition object

    """

    def __init__(self):
        r"""
        :param _Partition: Topic `partitionId`
        :type Partition: int
        :param _Offset: Offset position submitted by consumer
        :type Offset: int
        :param _Metadata: Supports consumers to submit messages with imported metadata for other purposes, currently an empty string.
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
        r"""Topic `partitionId`
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        r"""Offset position submitted by consumer
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Metadata(self):
        r"""Supports consumers to submit messages with imported metadata for other purposes, currently an empty string.
        :rtype: str
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def ErrorCode(self):
        r"""Error code
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def LogEndOffset(self):
        r"""Latest offset of current partition
        :rtype: int
        """
        return self._LogEndOffset

    @LogEndOffset.setter
    def LogEndOffset(self, LogEndOffset):
        self._LogEndOffset = LogEndOffset

    @property
    def Lag(self):
        r"""Number of unconsumed messages
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
    r"""Returned result of consumer group offset

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of eligible results
        :type TotalCount: int
        :param _TopicList: The topic partition array, where each element is a json object.
        :type TopicList: list of GroupOffsetTopic
        """
        self._TotalCount = None
        self._TopicList = None

    @property
    def TotalCount(self):
        r"""Total number of eligible results
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TopicList(self):
        r"""The topic partition array, where each element is a json object.
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
    r"""Consumer group topic object

    """

    def __init__(self):
        r"""
        :param _Topic: Topic name
        :type Topic: str
        :param _Partitions: The topic partition array, where each element is a json object.
        :type Partitions: list of GroupOffsetPartition
        """
        self._Topic = None
        self._Partitions = None

    @property
    def Topic(self):
        r"""Topic name
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partitions(self):
        r"""The topic partition array, where each element is a json object.
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
    r"""`DescribeGroup` response

    """

    def __init__(self):
        r"""
        :param _TotalCount: Counting.
        :type TotalCount: int
        :param _GroupList: GroupList
        :type GroupList: list of DescribeGroup
        :param _GroupCountQuota: Specifies the consumer group quota.
        :type GroupCountQuota: int
        """
        self._TotalCount = None
        self._GroupList = None
        self._GroupCountQuota = None

    @property
    def TotalCount(self):
        r"""Counting.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def GroupList(self):
        r"""GroupList
        :rtype: list of DescribeGroup
        """
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList

    @property
    def GroupCountQuota(self):
        r"""Specifies the consumer group quota.
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
    r"""InquireCkafkaPrice request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceType: Chinese site standard version fill in standards2 international site standard version fill in standard pro edition fill in profession advanced edition fill in premium.
        :type InstanceType: str
        :param _InstanceChargeParam: Billing mode for instance purchase/renewal. If this parameter is left empty when you purchase an instance, the fees for one month under the monthly subscription mode will be displayed by default.
        :type InstanceChargeParam: :class:`tencentcloud.ckafka.v20190819.models.InstanceChargeParam`
        :param _InstanceNum: The number of instances to be purchased or renewed. If this parameter is left empty, the default value is `1`.
        :type InstanceNum: int
        :param _Bandwidth: Specifies the internal network bandwidth size of the instance, in MB/s (required when purchased; bandwidth information is required for pro edition/advanced edition inquiries).
        :type Bandwidth: int
        :param _InquiryDiskParam: Specifies the purchase type and size of the hard disk of the instance. required when purchased. disk information is required for pro edition or advanced edition inquiries.

        :type InquiryDiskParam: :class:`tencentcloud.ckafka.v20190819.models.InquiryDiskParam`
        :param _MessageRetention: Message retention period in hours, which is required when you purchase an instance.
        :type MessageRetention: int
        :param _Topic: The number of instance topics to be purchased, which is required when you purchase an instance.
        :type Topic: int
        :param _Partition: Number of partitions for instance purchase, unit: unit (required when purchased; bandwidth information required for pro edition/advanced edition inquiry).
Partition upper limit. maximum value of 40000. step length of 100.
Specifies the specifications and limits that can be viewed through the following link: https://www.tencentcloud.comom/document/product/597/122563.?from_cn_redirect=1

        :type Partition: int
        :param _ZoneIds: The region for instance purchase, which can be obtained via the `DescribeCkafkaZone` API.
        :type ZoneIds: list of int
        :param _CategoryAction: Operation type flag. `purchase`: Making new purchases; `renew`: Renewing an instance. The default value is `purchase` if this parameter is left empty.
        :type CategoryAction: str
        :param _BillType: This field is not required.
        :type BillType: str
        :param _PublicNetworkParam: Public network bandwidth billing mode. currently only the pro edition supports public network bandwidth. required when purchasing public network bandwidth. value must be a multiple of 3.
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
        r"""Chinese site standard version fill in standards2 international site standard version fill in standard pro edition fill in profession advanced edition fill in premium.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceChargeParam(self):
        r"""Billing mode for instance purchase/renewal. If this parameter is left empty when you purchase an instance, the fees for one month under the monthly subscription mode will be displayed by default.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceChargeParam`
        """
        return self._InstanceChargeParam

    @InstanceChargeParam.setter
    def InstanceChargeParam(self, InstanceChargeParam):
        self._InstanceChargeParam = InstanceChargeParam

    @property
    def InstanceNum(self):
        r"""The number of instances to be purchased or renewed. If this parameter is left empty, the default value is `1`.
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def Bandwidth(self):
        r"""Specifies the internal network bandwidth size of the instance, in MB/s (required when purchased; bandwidth information is required for pro edition/advanced edition inquiries).
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def InquiryDiskParam(self):
        r"""Specifies the purchase type and size of the hard disk of the instance. required when purchased. disk information is required for pro edition or advanced edition inquiries.

        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryDiskParam`
        """
        return self._InquiryDiskParam

    @InquiryDiskParam.setter
    def InquiryDiskParam(self, InquiryDiskParam):
        self._InquiryDiskParam = InquiryDiskParam

    @property
    def MessageRetention(self):
        r"""Message retention period in hours, which is required when you purchase an instance.
        :rtype: int
        """
        return self._MessageRetention

    @MessageRetention.setter
    def MessageRetention(self, MessageRetention):
        self._MessageRetention = MessageRetention

    @property
    def Topic(self):
        r"""The number of instance topics to be purchased, which is required when you purchase an instance.
        :rtype: int
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        r"""Number of partitions for instance purchase, unit: unit (required when purchased; bandwidth information required for pro edition/advanced edition inquiry).
Partition upper limit. maximum value of 40000. step length of 100.
Specifies the specifications and limits that can be viewed through the following link: https://www.tencentcloud.comom/document/product/597/122563.?from_cn_redirect=1

        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def ZoneIds(self):
        r"""The region for instance purchase, which can be obtained via the `DescribeCkafkaZone` API.
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def CategoryAction(self):
        r"""Operation type flag. `purchase`: Making new purchases; `renew`: Renewing an instance. The default value is `purchase` if this parameter is left empty.
        :rtype: str
        """
        return self._CategoryAction

    @CategoryAction.setter
    def CategoryAction(self, CategoryAction):
        self._CategoryAction = CategoryAction

    @property
    def BillType(self):
        r"""This field is not required.
        :rtype: str
        """
        return self._BillType

    @BillType.setter
    def BillType(self, BillType):
        self._BillType = BillType

    @property
    def PublicNetworkParam(self):
        r"""Public network bandwidth billing mode. currently only the pro edition supports public network bandwidth. required when purchasing public network bandwidth. value must be a multiple of 3.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryPublicNetworkParam`
        """
        return self._PublicNetworkParam

    @PublicNetworkParam.setter
    def PublicNetworkParam(self, PublicNetworkParam):
        self._PublicNetworkParam = PublicNetworkParam

    @property
    def InstanceId(self):
        r"""ID of the instance to be renewed, which is required when you renew an instance.
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
    r"""Values returned by the `InquireCkafkaPrice` API

    """

    def __init__(self):
        r"""
        :param _InstancePrice: Specifies the instance price.
        :type InstancePrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryPrice`
        :param _PublicNetworkBandwidthPrice: Public network bandwidth price
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicNetworkBandwidthPrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryPrice`
        """
        self._InstancePrice = None
        self._PublicNetworkBandwidthPrice = None

    @property
    def InstancePrice(self):
        r"""Specifies the instance price.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryPrice`
        """
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def PublicNetworkBandwidthPrice(self):
        r"""Public network bandwidth price
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
    r"""InquireCkafkaPrice response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InquireCkafkaPriceResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquireCkafkaPriceResp`
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
            self._Result = InquireCkafkaPriceResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class InquiryBasePrice(AbstractModel):
    r"""Response parameters for instance price query

    """

    def __init__(self):
        r"""
        :param _UnitPrice: Original price unit.
        :type UnitPrice: float
        :param _UnitPriceDiscount: Discount unit price.
        :type UnitPriceDiscount: float
        :param _OriginalPrice: Total original price.
        :type OriginalPrice: float
        :param _DiscountPrice: Total discount price.
        :type DiscountPrice: float
        :param _Discount: Discount (unit: %).
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
        :param _Value: Purchase quantity.
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
        r"""Original price unit.
        :rtype: float
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceDiscount(self):
        r"""Discount unit price.
        :rtype: float
        """
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def OriginalPrice(self):
        r"""Total original price.
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        r"""Total discount price.
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def Discount(self):
        r"""Discount (unit: %).
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def GoodsNum(self):
        r"""Number of purchased items
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Currency(self):
        r"""Currency for payment
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def DiskType(self):
        r"""Dedicated disk response parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def TimeSpan(self):
        r"""Validity period
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        r"""Unit of the validity period (`m`: Month; `h`: Hour)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def Value(self):
        r"""Purchase quantity.
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
    r"""Prices of different purchased items

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
        :param _InstanceTypePrice: Instance package price.
        :type InstanceTypePrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        self._BandwidthPrice = None
        self._DiskPrice = None
        self._PartitionPrice = None
        self._TopicPrice = None
        self._InstanceTypePrice = None

    @property
    def BandwidthPrice(self):
        r"""Price of additional private network bandwidth
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        return self._BandwidthPrice

    @BandwidthPrice.setter
    def BandwidthPrice(self, BandwidthPrice):
        self._BandwidthPrice = BandwidthPrice

    @property
    def DiskPrice(self):
        r"""Disk price
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def PartitionPrice(self):
        r"""Price of additional partitions
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        return self._PartitionPrice

    @PartitionPrice.setter
    def PartitionPrice(self, PartitionPrice):
        self._PartitionPrice = PartitionPrice

    @property
    def TopicPrice(self):
        r"""Price of additional topics
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        return self._TopicPrice

    @TopicPrice.setter
    def TopicPrice(self, TopicPrice):
        self._TopicPrice = TopicPrice

    @property
    def InstanceTypePrice(self):
        r"""Instance package price.
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
    r"""Disk purchase parameters

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
        r"""Disk type. Valid values: `SSD` (SSD), `CLOUD_SSD` (SSD cloud disk), `CLOUD_PREMIUM` (Premium cloud disk), `CLOUD_BASIC` (Cloud disk).
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""Size of the purchased disk in GB
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
    r"""Response parameters for instance price query

    """

    def __init__(self):
        r"""
        :param _UnitPrice: Original price unit.
        :type UnitPrice: float
        :param _UnitPriceDiscount: Discount unit price.
        :type UnitPriceDiscount: float
        :param _OriginalPrice: Total original price.
        :type OriginalPrice: float
        :param _DiscountPrice: Total discount price.
        :type DiscountPrice: float
        :param _Discount: Discount (unit: %).
        :type Discount: float
        :param _GoodsNum: Number of products
        :type GoodsNum: int
        :param _Currency: Specifies the payment currency.
        :type Currency: str
        :param _DiskType: Dedicated disk response parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param _TimeSpan: Purchase duration.
        :type TimeSpan: int
        :param _TimeUnit: Specifies the purchase duration unit ("m" for monthly, "h" for hourly).
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
        r"""Original price unit.
        :rtype: float
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceDiscount(self):
        r"""Discount unit price.
        :rtype: float
        """
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def OriginalPrice(self):
        r"""Total original price.
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        r"""Total discount price.
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def Discount(self):
        r"""Discount (unit: %).
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def GoodsNum(self):
        r"""Number of products
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Currency(self):
        r"""Specifies the payment currency.
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def DiskType(self):
        r"""Dedicated disk response parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def TimeSpan(self):
        r"""Purchase duration.
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        r"""Specifies the purchase duration unit ("m" for monthly, "h" for hourly).
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def Value(self):
        r"""Purchase quantity
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def DetailPrices(self):
        r"""Prices of different purchased items
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
    r"""Public network bandwidth parameters

    """

    def __init__(self):
        r"""
        :param _PublicNetworkChargeType: Public network bandwidth billing mode (`BANDWIDTH_PREPAID`: Monthly subscription; `BANDWIDTH_POSTPAID_BY_HOUR`: Bill-by-hour)
        :type PublicNetworkChargeType: str
        :param _PublicNetworkMonthly: Public network bandwidth, in MB. value must be 0 or a multiple of 3.
        :type PublicNetworkMonthly: int
        """
        self._PublicNetworkChargeType = None
        self._PublicNetworkMonthly = None

    @property
    def PublicNetworkChargeType(self):
        r"""Public network bandwidth billing mode (`BANDWIDTH_PREPAID`: Monthly subscription; `BANDWIDTH_POSTPAID_BY_HOUR`: Bill-by-hour)
        :rtype: str
        """
        return self._PublicNetworkChargeType

    @PublicNetworkChargeType.setter
    def PublicNetworkChargeType(self, PublicNetworkChargeType):
        self._PublicNetworkChargeType = PublicNetworkChargeType

    @property
    def PublicNetworkMonthly(self):
        r"""Public network bandwidth, in MB. value must be 0 or a multiple of 3.
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
    r"""Instance object

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id.
        :type InstanceId: str
        :param _InstanceName: Specifies the Name of the ckafka cluster instance.
        :type InstanceName: str
        :param _Status: Instance status. 0: creating, 1: running, 2: deleting, 3: deleted, 5: isolated, 7: upgrading, -1: creation failed.
        :type Status: int
        :param _IfCommunity: Specifies whether the instance is open-source. valid values: true (open-source), false (not open-source).
        :type IfCommunity: bool
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Status = None
        self._IfCommunity = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Specifies the Name of the ckafka cluster instance.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Status(self):
        r"""Instance status. 0: creating, 1: running, 2: deleting, 3: deleted, 5: isolated, 7: upgrading, -1: creation failed.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IfCommunity(self):
        r"""Specifies whether the instance is open-source. valid values: true (open-source), false (not open-source).
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
    r"""Returned result object of instance attributes

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id.
        :type InstanceId: str
        :param _InstanceName: Specifies the Name of the ckafka cluster instance.
        :type InstanceName: str
        :param _VipList: VIP list information of access point
        :type VipList: list of VipEntity
        :param _Vip: Virtual IP
        :type Vip: str
        :param _Vport: Virtual port
        :type Vport: str
        :param _Status: Instance status. 0: creating, 1: running, 2: deleting, 3: deleted, 5: isolated, 7: upgrading, -1: creation failed.
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
        :type Tags: list of Tag
        :param _ExpireTime: Expiration time
        :type ExpireTime: int
        :param _ZoneIds: Availability Zone List
        :type ZoneIds: list of int
        :param _Version: Specifies the ckafka cluster instance version.
        :type Version: str
        :param _MaxGroupNum: Maximum number of groups.
        :type MaxGroupNum: int
        :param _Cvm: Sale type. valid values: 0 (standard version), 1 (pro edition).
        :type Cvm: int
        :param _InstanceType: Instance type. valid values:. 
Specifies the pro edition.    
Standard version.
premium. specifies the advanced edition.
Specifies the serverless version.
        :type InstanceType: str
        :param _Features: Indicates the characteristics supported by the instance. FEATURE_SUBNET_ACL means the policy support for configuring subnets.
        :type Features: list of str
        :param _RetentionTimeConfig: Dynamic message retention policy.
        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        :param _MaxConnection: Maximum number of connections.
        :type MaxConnection: int
        :param _PublicNetwork: Public network bandwidth
        :type PublicNetwork: int
        :param _DeleteRouteTimestamp: Specifies the deprecated field with no actual meaning.
        :type DeleteRouteTimestamp: str
        :param _RemainingPartitions: Number of remaining creatable partitions.
        :type RemainingPartitions: int
        :param _RemainingTopics: Number of remaining creatable topics.
        :type RemainingTopics: int
        :param _DynamicDiskConfig: Scaling policy for dynamic disk.
        :type DynamicDiskConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicDiskConfig`
        :param _SystemMaintenanceTime: Specifies the system maintenance time.
        :type SystemMaintenanceTime: str
        :param _MaxMessageByte: Specifies the maximum size of messages at the instance level.
        :type MaxMessageByte: int
        :param _InstanceChargeType: Specifies the instance billing type. POSTPAID_BY_HOUR: hourly billing; PREPAID: annual/monthly package.
        :type InstanceChargeType: str
        :param _ElasticBandwidthSwitch: Whether to enable the elastic bandwidth allowlist.   
Indicates the allowlist feature with elastic bandwidth enabled.
0: elastic bandwidth allowlist feature is disabled.
        :type ElasticBandwidthSwitch: int
        :param _ElasticBandwidthOpenStatus: Indicates the elastic bandwidth activation status.
1: indicates elastic bandwidth is disabled.
Enable elastic bandwidth.
Enable elastic bandwidth successfully.
33: disabling elastic bandwidth.
Indicates that the elastic bandwidth is successfully disabled.
Enable elastic bandwidth failed.
Bandwidth failure.
        :type ElasticBandwidthOpenStatus: int
        :param _ClusterType: Cluster type.  
CLOUD_IDC idc cluster.
CLOUD_CVM_SHARE shared cluster.
CLOUD_CVM_YUNTI yunti cvm cluster.
CLOUD_CVM. specifies the cvm cluster.
CLOUD_CDC cdc cluster.
CLOUD_EKS_TSE eks cluster.
        :type ClusterType: str
        :param _FreePartitionNumber: Number of free partitions.
        :type FreePartitionNumber: int
        :param _ElasticFloatBandwidth: Specifies the elastic bandwidth upper limit.
        :type ElasticFloatBandwidth: int
        :param _CustomCertId: ssl custom certificate id. only returned for instance clusters with custom certificates.
        :type CustomCertId: str
        :param _UncleanLeaderElectionEnable: Default unclean.leader.election.enable configuration for cluster topic: 1 enable 0 disable.
        :type UncleanLeaderElectionEnable: int
        :param _DeleteProtectionEnable: Instance deletion protection switch. 1: enabled; 0: disabled.
        :type DeleteProtectionEnable: int
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
        self._SystemMaintenanceTime = None
        self._MaxMessageByte = None
        self._InstanceChargeType = None
        self._ElasticBandwidthSwitch = None
        self._ElasticBandwidthOpenStatus = None
        self._ClusterType = None
        self._FreePartitionNumber = None
        self._ElasticFloatBandwidth = None
        self._CustomCertId = None
        self._UncleanLeaderElectionEnable = None
        self._DeleteProtectionEnable = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Specifies the Name of the ckafka cluster instance.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def VipList(self):
        r"""VIP list information of access point
        :rtype: list of VipEntity
        """
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList

    @property
    def Vip(self):
        r"""Virtual IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""Virtual port
        :rtype: str
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Status(self):
        r"""Instance status. 0: creating, 1: running, 2: deleting, 3: deleted, 5: isolated, 7: upgrading, -1: creation failed.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Bandwidth(self):
        r"""Instance bandwidth in Mbps
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def DiskSize(self):
        r"""Instance storage capacity in GB
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def ZoneId(self):
        r"""AZ
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        r"""VPC ID. If this parameter is empty, it means the basic network
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet ID. If this parameter is empty, it means the basic network
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Healthy(self):
        r"""Instance health status. 1: healthy, 2: alarmed, 3: exceptional
        :rtype: int
        """
        return self._Healthy

    @Healthy.setter
    def Healthy(self, Healthy):
        self._Healthy = Healthy

    @property
    def HealthyMessage(self):
        r"""Instance health information. Currently, the disk utilization is displayed with a maximum length of 256
        :rtype: str
        """
        return self._HealthyMessage

    @HealthyMessage.setter
    def HealthyMessage(self, HealthyMessage):
        self._HealthyMessage = HealthyMessage

    @property
    def CreateTime(self):
        r"""Creation time
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MsgRetentionTime(self):
        r"""Message retention period in minutes
        :rtype: int
        """
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def Config(self):
        r"""Configuration for automatic topic creation. If this field is empty, it means that automatic creation is not enabled
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceConfigDO`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def RemainderPartitions(self):
        r"""Number of remaining creatable partitions
        :rtype: int
        """
        return self._RemainderPartitions

    @RemainderPartitions.setter
    def RemainderPartitions(self, RemainderPartitions):
        self._RemainderPartitions = RemainderPartitions

    @property
    def RemainderTopics(self):
        r"""Number of remaining creatable topics
        :rtype: int
        """
        return self._RemainderTopics

    @RemainderTopics.setter
    def RemainderTopics(self, RemainderTopics):
        self._RemainderTopics = RemainderTopics

    @property
    def CreatedPartitions(self):
        r"""Number of partitions already created
        :rtype: int
        """
        return self._CreatedPartitions

    @CreatedPartitions.setter
    def CreatedPartitions(self, CreatedPartitions):
        self._CreatedPartitions = CreatedPartitions

    @property
    def CreatedTopics(self):
        r"""Number of topics already created
        :rtype: int
        """
        return self._CreatedTopics

    @CreatedTopics.setter
    def CreatedTopics(self, CreatedTopics):
        self._CreatedTopics = CreatedTopics

    @property
    def Tags(self):
        r"""Tag array
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ExpireTime(self):
        r"""Expiration time
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ZoneIds(self):
        r"""Availability Zone List
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Version(self):
        r"""Specifies the ckafka cluster instance version.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def MaxGroupNum(self):
        r"""Maximum number of groups.
        :rtype: int
        """
        return self._MaxGroupNum

    @MaxGroupNum.setter
    def MaxGroupNum(self, MaxGroupNum):
        self._MaxGroupNum = MaxGroupNum

    @property
    def Cvm(self):
        r"""Sale type. valid values: 0 (standard version), 1 (pro edition).
        :rtype: int
        """
        return self._Cvm

    @Cvm.setter
    def Cvm(self, Cvm):
        self._Cvm = Cvm

    @property
    def InstanceType(self):
        r"""Instance type. valid values:. 
Specifies the pro edition.    
Standard version.
premium. specifies the advanced edition.
Specifies the serverless version.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Features(self):
        r"""Indicates the characteristics supported by the instance. FEATURE_SUBNET_ACL means the policy support for configuring subnets.
        :rtype: list of str
        """
        return self._Features

    @Features.setter
    def Features(self, Features):
        self._Features = Features

    @property
    def RetentionTimeConfig(self):
        r"""Dynamic message retention policy.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        """
        return self._RetentionTimeConfig

    @RetentionTimeConfig.setter
    def RetentionTimeConfig(self, RetentionTimeConfig):
        self._RetentionTimeConfig = RetentionTimeConfig

    @property
    def MaxConnection(self):
        r"""Maximum number of connections.
        :rtype: int
        """
        return self._MaxConnection

    @MaxConnection.setter
    def MaxConnection(self, MaxConnection):
        self._MaxConnection = MaxConnection

    @property
    def PublicNetwork(self):
        r"""Public network bandwidth
        :rtype: int
        """
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def DeleteRouteTimestamp(self):
        r"""Specifies the deprecated field with no actual meaning.
        :rtype: str
        """
        return self._DeleteRouteTimestamp

    @DeleteRouteTimestamp.setter
    def DeleteRouteTimestamp(self, DeleteRouteTimestamp):
        self._DeleteRouteTimestamp = DeleteRouteTimestamp

    @property
    def RemainingPartitions(self):
        r"""Number of remaining creatable partitions.
        :rtype: int
        """
        return self._RemainingPartitions

    @RemainingPartitions.setter
    def RemainingPartitions(self, RemainingPartitions):
        self._RemainingPartitions = RemainingPartitions

    @property
    def RemainingTopics(self):
        r"""Number of remaining creatable topics.
        :rtype: int
        """
        return self._RemainingTopics

    @RemainingTopics.setter
    def RemainingTopics(self, RemainingTopics):
        self._RemainingTopics = RemainingTopics

    @property
    def DynamicDiskConfig(self):
        r"""Scaling policy for dynamic disk.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DynamicDiskConfig`
        """
        return self._DynamicDiskConfig

    @DynamicDiskConfig.setter
    def DynamicDiskConfig(self, DynamicDiskConfig):
        self._DynamicDiskConfig = DynamicDiskConfig

    @property
    def SystemMaintenanceTime(self):
        r"""Specifies the system maintenance time.
        :rtype: str
        """
        return self._SystemMaintenanceTime

    @SystemMaintenanceTime.setter
    def SystemMaintenanceTime(self, SystemMaintenanceTime):
        self._SystemMaintenanceTime = SystemMaintenanceTime

    @property
    def MaxMessageByte(self):
        r"""Specifies the maximum size of messages at the instance level.
        :rtype: int
        """
        return self._MaxMessageByte

    @MaxMessageByte.setter
    def MaxMessageByte(self, MaxMessageByte):
        self._MaxMessageByte = MaxMessageByte

    @property
    def InstanceChargeType(self):
        r"""Specifies the instance billing type. POSTPAID_BY_HOUR: hourly billing; PREPAID: annual/monthly package.
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def ElasticBandwidthSwitch(self):
        r"""Whether to enable the elastic bandwidth allowlist.   
Indicates the allowlist feature with elastic bandwidth enabled.
0: elastic bandwidth allowlist feature is disabled.
        :rtype: int
        """
        return self._ElasticBandwidthSwitch

    @ElasticBandwidthSwitch.setter
    def ElasticBandwidthSwitch(self, ElasticBandwidthSwitch):
        self._ElasticBandwidthSwitch = ElasticBandwidthSwitch

    @property
    def ElasticBandwidthOpenStatus(self):
        r"""Indicates the elastic bandwidth activation status.
1: indicates elastic bandwidth is disabled.
Enable elastic bandwidth.
Enable elastic bandwidth successfully.
33: disabling elastic bandwidth.
Indicates that the elastic bandwidth is successfully disabled.
Enable elastic bandwidth failed.
Bandwidth failure.
        :rtype: int
        """
        return self._ElasticBandwidthOpenStatus

    @ElasticBandwidthOpenStatus.setter
    def ElasticBandwidthOpenStatus(self, ElasticBandwidthOpenStatus):
        self._ElasticBandwidthOpenStatus = ElasticBandwidthOpenStatus

    @property
    def ClusterType(self):
        r"""Cluster type.  
CLOUD_IDC idc cluster.
CLOUD_CVM_SHARE shared cluster.
CLOUD_CVM_YUNTI yunti cvm cluster.
CLOUD_CVM. specifies the cvm cluster.
CLOUD_CDC cdc cluster.
CLOUD_EKS_TSE eks cluster.
        :rtype: str
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def FreePartitionNumber(self):
        r"""Number of free partitions.
        :rtype: int
        """
        return self._FreePartitionNumber

    @FreePartitionNumber.setter
    def FreePartitionNumber(self, FreePartitionNumber):
        self._FreePartitionNumber = FreePartitionNumber

    @property
    def ElasticFloatBandwidth(self):
        r"""Specifies the elastic bandwidth upper limit.
        :rtype: int
        """
        return self._ElasticFloatBandwidth

    @ElasticFloatBandwidth.setter
    def ElasticFloatBandwidth(self, ElasticFloatBandwidth):
        self._ElasticFloatBandwidth = ElasticFloatBandwidth

    @property
    def CustomCertId(self):
        r"""ssl custom certificate id. only returned for instance clusters with custom certificates.
        :rtype: str
        """
        return self._CustomCertId

    @CustomCertId.setter
    def CustomCertId(self, CustomCertId):
        self._CustomCertId = CustomCertId

    @property
    def UncleanLeaderElectionEnable(self):
        r"""Default unclean.leader.election.enable configuration for cluster topic: 1 enable 0 disable.
        :rtype: int
        """
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def DeleteProtectionEnable(self):
        r"""Instance deletion protection switch. 1: enabled; 0: disabled.
        :rtype: int
        """
        return self._DeleteProtectionEnable

    @DeleteProtectionEnable.setter
    def DeleteProtectionEnable(self, DeleteProtectionEnable):
        self._DeleteProtectionEnable = DeleteProtectionEnable


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
        self._SystemMaintenanceTime = params.get("SystemMaintenanceTime")
        self._MaxMessageByte = params.get("MaxMessageByte")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._ElasticBandwidthSwitch = params.get("ElasticBandwidthSwitch")
        self._ElasticBandwidthOpenStatus = params.get("ElasticBandwidthOpenStatus")
        self._ClusterType = params.get("ClusterType")
        self._FreePartitionNumber = params.get("FreePartitionNumber")
        self._ElasticFloatBandwidth = params.get("ElasticFloatBandwidth")
        self._CustomCertId = params.get("CustomCertId")
        self._UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self._DeleteProtectionEnable = params.get("DeleteProtectionEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargeParam(AbstractModel):
    r"""Instance billing parameters

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
        r"""Instance billing mode (`PREPAID`: Monthly subscription; `POSTPAID_BY_HOUR`: Pay-as-you-go)
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePeriod(self):
        r"""Validity period, which is only required for the monthly subscription billing mode
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
    r"""Instance configuration entity

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
        r"""Whether to create topics automatically
        :rtype: bool
        """
        return self._AutoCreateTopicsEnable

    @AutoCreateTopicsEnable.setter
    def AutoCreateTopicsEnable(self, AutoCreateTopicsEnable):
        self._AutoCreateTopicsEnable = AutoCreateTopicsEnable

    @property
    def DefaultNumPartitions(self):
        r"""Number of partitions
        :rtype: int
        """
        return self._DefaultNumPartitions

    @DefaultNumPartitions.setter
    def DefaultNumPartitions(self, DefaultNumPartitions):
        self._DefaultNumPartitions = DefaultNumPartitions

    @property
    def DefaultReplicationFactor(self):
        r"""Default replication factor
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
        


class InstanceDeleteResponse(AbstractModel):
    r"""Deletion of instances returns a task.

    """

    def __init__(self):
        r"""
        :param _FlowId: Specifies the task Id returned after deleting an instance.
        :type FlowId: int
        """
        self._FlowId = None

    @property
    def FlowId(self):
        r"""Specifies the task Id returned after deleting an instance.
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
        


class InstanceDetail(AbstractModel):
    r"""Instance details

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id.
        :type InstanceId: str
        :param _InstanceName: CKafka cluster instance name.
        :type InstanceName: str
        :param _Vip: Instance VIP information
        :type Vip: str
        :param _Vport: Instance port information
        :type Vport: str
        :param _VipList: Virtual IP list
        :type VipList: list of VipEntity
        :param _Status: Instance status. 0: creating, 1: running, 2: deleting, 3: deleted, 5: isolated, 7: upgrading, -1: creation failed.
        :type Status: int
        :param _Bandwidth: Instance bandwidth in Mbps
        :type Bandwidth: int
        :param _DiskSize: Specifies the ckafka cluster instance disk size in gb.
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
        :param _Version: kafka version information.
        :type Version: str
        :param _ZoneIds: Cross-Availability zone.
        :type ZoneIds: list of int
        :param _Cvm: ckafka sales type.
        :type Cvm: int
        :param _InstanceType: Specifies the cluster instance type of ckafka.
        :type InstanceType: str
        :param _DiskType: Specifies the ckafka cluster instance disk type.
        :type DiskType: str
        :param _MaxTopicNumber: Maximum number of topics for current specifications.
        :type MaxTopicNumber: int
        :param _MaxPartitionNumber: Maximum number of partitions for current specifications.
        :type MaxPartitionNumber: int
        :param _RebalanceTime: Scheduled configuration upgrade time.
        :type RebalanceTime: str
        :param _PartitionNumber: Specifies the number of partitions in the current instance.
        :type PartitionNumber: int
        :param _PublicNetworkChargeType: Specifies the public network bandwidth type of the ckafka cluster instance.
        :type PublicNetworkChargeType: str
        :param _PublicNetwork: Public network bandwidth. minimum 3 Mbps. maximum 999 Mbps. only the pro edition supports filling in.
        :type PublicNetwork: int
        :param _ClusterType: Specifies the underlying cluster type of the ckafka cluster instance.
        :type ClusterType: str
        :param _Features: Instance feature list.
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
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""CKafka cluster instance name.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Vip(self):
        r"""Instance VIP information
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""Instance port information
        :rtype: str
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VipList(self):
        r"""Virtual IP list
        :rtype: list of VipEntity
        """
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList

    @property
    def Status(self):
        r"""Instance status. 0: creating, 1: running, 2: deleting, 3: deleted, 5: isolated, 7: upgrading, -1: creation failed.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Bandwidth(self):
        r"""Instance bandwidth in Mbps
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def DiskSize(self):
        r"""Specifies the ckafka cluster instance disk size in gb.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def ZoneId(self):
        r"""AZ ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        r"""vpcId. If this parameter is empty, it means the basic network
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

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
    def RenewFlag(self):
        r"""Whether to renew the instance automatically, which is an int-type enumerated value. 1: yes, 2: no
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Healthy(self):
        r"""Instance status. An int-type value will be returned. `0`: Healthy, `1`: Alarmed, `2`: Exceptional
        :rtype: int
        """
        return self._Healthy

    @Healthy.setter
    def Healthy(self, Healthy):
        self._Healthy = Healthy

    @property
    def HealthyMessage(self):
        r"""Instance status information
        :rtype: str
        """
        return self._HealthyMessage

    @HealthyMessage.setter
    def HealthyMessage(self, HealthyMessage):
        self._HealthyMessage = HealthyMessage

    @property
    def CreateTime(self):
        r"""Instance creation time
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        r"""Instance expiration time
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def IsInternal(self):
        r"""Whether it is an internal customer. 1: yes
        :rtype: int
        """
        return self._IsInternal

    @IsInternal.setter
    def IsInternal(self, IsInternal):
        self._IsInternal = IsInternal

    @property
    def TopicNum(self):
        r"""Number of topics
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def Tags(self):
        r"""Tag
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Version(self):
        r"""kafka version information.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ZoneIds(self):
        r"""Cross-Availability zone.
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Cvm(self):
        r"""ckafka sales type.
        :rtype: int
        """
        return self._Cvm

    @Cvm.setter
    def Cvm(self, Cvm):
        self._Cvm = Cvm

    @property
    def InstanceType(self):
        r"""Specifies the cluster instance type of ckafka.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DiskType(self):
        r"""Specifies the ckafka cluster instance disk type.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def MaxTopicNumber(self):
        r"""Maximum number of topics for current specifications.
        :rtype: int
        """
        return self._MaxTopicNumber

    @MaxTopicNumber.setter
    def MaxTopicNumber(self, MaxTopicNumber):
        self._MaxTopicNumber = MaxTopicNumber

    @property
    def MaxPartitionNumber(self):
        r"""Maximum number of partitions for current specifications.
        :rtype: int
        """
        return self._MaxPartitionNumber

    @MaxPartitionNumber.setter
    def MaxPartitionNumber(self, MaxPartitionNumber):
        self._MaxPartitionNumber = MaxPartitionNumber

    @property
    def RebalanceTime(self):
        r"""Scheduled configuration upgrade time.
        :rtype: str
        """
        return self._RebalanceTime

    @RebalanceTime.setter
    def RebalanceTime(self, RebalanceTime):
        self._RebalanceTime = RebalanceTime

    @property
    def PartitionNumber(self):
        r"""Specifies the number of partitions in the current instance.
        :rtype: int
        """
        return self._PartitionNumber

    @PartitionNumber.setter
    def PartitionNumber(self, PartitionNumber):
        self._PartitionNumber = PartitionNumber

    @property
    def PublicNetworkChargeType(self):
        r"""Specifies the public network bandwidth type of the ckafka cluster instance.
        :rtype: str
        """
        return self._PublicNetworkChargeType

    @PublicNetworkChargeType.setter
    def PublicNetworkChargeType(self, PublicNetworkChargeType):
        self._PublicNetworkChargeType = PublicNetworkChargeType

    @property
    def PublicNetwork(self):
        r"""Public network bandwidth. minimum 3 Mbps. maximum 999 Mbps. only the pro edition supports filling in.
        :rtype: int
        """
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def ClusterType(self):
        r"""Specifies the underlying cluster type of the ckafka cluster instance.
        :rtype: str
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def Features(self):
        r"""Instance feature list.
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
    r"""Returned result of instance details

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
        r"""Total number of eligible instances
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        r"""List of eligible instance details
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
    r"""Traffic throttling policy in instance/topic dimension

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
        r"""Production throttling in MB/sec.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._QuotaProducerByteRate

    @QuotaProducerByteRate.setter
    def QuotaProducerByteRate(self, QuotaProducerByteRate):
        self._QuotaProducerByteRate = QuotaProducerByteRate

    @property
    def QuotaConsumerByteRate(self):
        r"""Consumption throttling in MB/sec.
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
    r"""Aggregated returned result of instance status

    """

    def __init__(self):
        r"""
        :param _InstanceList: Specifies the list of instances meeting the conditions.
        :type InstanceList: list of Instance
        :param _TotalCount: Total results that meet the conditions.
        :type TotalCount: int
        """
        self._InstanceList = None
        self._TotalCount = None

    @property
    def InstanceList(self):
        r"""Specifies the list of instances meeting the conditions.
        :rtype: list of Instance
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        r"""Total results that meet the conditions.
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
        


class InstanceRoute(AbstractModel):
    r"""Instance route.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id.
        :type InstanceId: str
        :param _RouteId: Route ID
        :type RouteId: int
        """
        self._InstanceId = None
        self._RouteId = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RouteId(self):
        r"""Route ID
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
        


class InstanceScalingDownRequest(AbstractModel):
    r"""InstanceScalingDown request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka cluster instance Id. can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _UpgradeStrategy: Shrink mode. 1: stable mode. 
2. specifies high-speed configuration change.
        :type UpgradeStrategy: int
        :param _DiskSize: Specifies the disk capacity in GB. value range: maximum value 500000, step length 100.
The specifications and limitations can be viewed through the following link: https://www.tencentcloud.comom/document/product/597/122562.?from_cn_redirect=1


        :type DiskSize: int
        :param _BandWidth: Peak bandwidth in MB/s.
Specifies the url (https://www.tencentcloud.comom/document/product/597/11745?from_cn_redirect=1) to view specification limits and corresponding step length.
        :type BandWidth: int
        :param _Partition: Partition upper limit maximum value of 40000, step length 100.
Specification limits can be viewed through the following link: https://www.tencentcloud.comom/document/product/597/122563.?from_cn_redirect=1

        :type Partition: int
        """
        self._InstanceId = None
        self._UpgradeStrategy = None
        self._DiskSize = None
        self._BandWidth = None
        self._Partition = None

    @property
    def InstanceId(self):
        r"""ckafka cluster instance Id. can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UpgradeStrategy(self):
        r"""Shrink mode. 1: stable mode. 
2. specifies high-speed configuration change.
        :rtype: int
        """
        return self._UpgradeStrategy

    @UpgradeStrategy.setter
    def UpgradeStrategy(self, UpgradeStrategy):
        self._UpgradeStrategy = UpgradeStrategy

    @property
    def DiskSize(self):
        r"""Specifies the disk capacity in GB. value range: maximum value 500000, step length 100.
The specifications and limitations can be viewed through the following link: https://www.tencentcloud.comom/document/product/597/122562.?from_cn_redirect=1


        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def BandWidth(self):
        r"""Peak bandwidth in MB/s.
Specifies the url (https://www.tencentcloud.comom/document/product/597/11745?from_cn_redirect=1) to view specification limits and corresponding step length.
        :rtype: int
        """
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def Partition(self):
        r"""Partition upper limit maximum value of 40000, step length 100.
Specification limits can be viewed through the following link: https://www.tencentcloud.comom/document/product/597/122563.?from_cn_redirect=1

        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UpgradeStrategy = params.get("UpgradeStrategy")
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
        


class InstanceScalingDownResponse(AbstractModel):
    r"""InstanceScalingDown response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned results.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ScalingDownResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned results.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ScalingDownResp`
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
            self._Result = ScalingDownResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class JgwOperateResponse(AbstractModel):
    r"""Returned result value of operation

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
        r"""Returned code. 0: normal, other values: error
        :rtype: str
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMessage(self):
        r"""Success message
        :rtype: str
        """
        return self._ReturnMessage

    @ReturnMessage.setter
    def ReturnMessage(self, ReturnMessage):
        self._ReturnMessage = ReturnMessage

    @property
    def Data(self):
        r"""Data returned by an operation, which may contain `flowId`, etc.
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
        


class ListCvmAndIpInfoRsp(AbstractModel):
    r"""CVM and IP information list.

    """

    def __init__(self):
        r"""
        :param _CvmList: cvm and IP list.
        :type CvmList: list of CvmAndIpInfo
        :param _TotalCount: Specifies the instance data volume.
        :type TotalCount: int
        """
        self._CvmList = None
        self._TotalCount = None

    @property
    def CvmList(self):
        r"""cvm and IP list.
        :rtype: list of CvmAndIpInfo
        """
        return self._CvmList

    @CvmList.setter
    def CvmList(self, CvmList):
        self._CvmList = CvmList

    @property
    def TotalCount(self):
        r"""Specifies the instance data volume.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("CvmList") is not None:
            self._CvmList = []
            for item in params.get("CvmList"):
                obj = CvmAndIpInfo()
                obj._deserialize(item)
                self._CvmList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAclRuleRequest(AbstractModel):
    r"""ModifyAclRule request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id.
        :type InstanceId: str
        :param _RuleName: ACL rule name.
        :type RuleName: str
        :param _IsApplied: Specifies whether to apply to newly-added topics when importing predefined rule modifications.
        :type IsApplied: int
        """
        self._InstanceId = None
        self._RuleName = None
        self._IsApplied = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleName(self):
        r"""ACL rule name.
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def IsApplied(self):
        r"""Specifies whether to apply to newly-added topics when importing predefined rule modifications.
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
    r"""ModifyAclRule response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Unique key of a rule
        :type Result: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Unique key of a rule
        :rtype: int
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


class ModifyDatahubTopicRequest(AbstractModel):
    r"""ModifyDatahubTopic request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Elastic topic name.
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
        r"""Elastic topic name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RetentionMs(self):
        r"""Message retention period in ms. The current minimum value is 60,000 ms.
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def Note(self):
        r"""Topic remarks, which are a string of up to 64 characters. It can contain letters, digits, and hyphens (-) and must start with a letter.
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Tags(self):
        r"""Tag list
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
    r"""ModifyDatahubTopic response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result set
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result set
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyGroupOffsetsRequest(AbstractModel):
    r"""ModifyGroupOffsets request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
        :type InstanceId: str
        :param _Group: Consumer group name. obtain through the API [DescribeConsumerGroup](https://www.tencentcloud.comom/document/product/597/40841?from_cn_redirect=1).
        :type Group: str
        :param _Strategy: Reset offset strategy. parameter meaning: 0. align with the shift-by parameter, move the offset forward or backward by shift entries. 1. alignment reference (by-duration, to-datetime, to-earliest, to-latest), move the offset to the specified timestamp position. 2. alignment reference (to-offset), move the offset to the specified offset position.
        :type Strategy: int
        :param _Topics: Specifies the topic name list that needs to reset.
        :type Topics: list of str
        :param _Shift: When `strategy` is 0, this field is required. If it is above zero, the offset will be shifted backward by the value of the `shift`. If it is below zero, the offset will be shifted forward by the value of the `shift`. After a correct reset, the new offset should be (old_offset + shift). Note that if the new offset is smaller than the `earliest` parameter of the partition, it will be set to `earliest`, and if it is greater than the `latest` parameter of the partition, it will be set to `latest`
        :type Shift: int
        :param _ShiftTimestamp: In milliseconds. when strategy is 1, must include this field. among them, -2 means reset offset to the start position, -1 means reset to the latest position (equivalent to clearing), other values represent the specified time. obtain the offset at the specified time in the topic and reset. notably, if no message exists at the specified time, get the last offset.
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
        r"""ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Group(self):
        r"""Consumer group name. obtain through the API [DescribeConsumerGroup](https://www.tencentcloud.comom/document/product/597/40841?from_cn_redirect=1).
        :rtype: str
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Strategy(self):
        r"""Reset offset strategy. parameter meaning: 0. align with the shift-by parameter, move the offset forward or backward by shift entries. 1. alignment reference (by-duration, to-datetime, to-earliest, to-latest), move the offset to the specified timestamp position. 2. alignment reference (to-offset), move the offset to the specified offset position.
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Topics(self):
        r"""Specifies the topic name list that needs to reset.
        :rtype: list of str
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def Shift(self):
        r"""When `strategy` is 0, this field is required. If it is above zero, the offset will be shifted backward by the value of the `shift`. If it is below zero, the offset will be shifted forward by the value of the `shift`. After a correct reset, the new offset should be (old_offset + shift). Note that if the new offset is smaller than the `earliest` parameter of the partition, it will be set to `earliest`, and if it is greater than the `latest` parameter of the partition, it will be set to `latest`
        :rtype: int
        """
        return self._Shift

    @Shift.setter
    def Shift(self, Shift):
        self._Shift = Shift

    @property
    def ShiftTimestamp(self):
        r"""In milliseconds. when strategy is 1, must include this field. among them, -2 means reset offset to the start position, -1 means reset to the latest position (equivalent to clearing), other values represent the specified time. obtain the offset at the specified time in the topic and reset. notably, if no message exists at the specified time, get the last offset.
        :rtype: int
        """
        return self._ShiftTimestamp

    @ShiftTimestamp.setter
    def ShiftTimestamp(self, ShiftTimestamp):
        self._ShiftTimestamp = ShiftTimestamp

    @property
    def Offset(self):
        r"""Position of the offset that needs to be reset. When `strategy` is 2, this field is required
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Partitions(self):
        r"""List of partitions that need to be reset. If the topics parameter is not specified, reset partitions in the corresponding partition list of all topics. If the topics parameter is specified, reset partitions of the corresponding partition list of the specified topic list.
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
    r"""ModifyGroupOffsets response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyInstanceAttributesConfig(AbstractModel):
    r"""Configuration object for modifying instance attributes

    """

    def __init__(self):
        r"""
        :param _AutoCreateTopicEnable: Automatic creation. true: enabled, false: not enabled
        :type AutoCreateTopicEnable: bool
        :param _DefaultNumPartitions: Default number of partitions for a newly created topic. if AutoCreateTopicEnable is set to true and no value is set, defaults to 3.
        :type DefaultNumPartitions: int
        :param _DefaultReplicationFactor: Default number of replicas for a newly created topic. if AutoCreateTopicEnable is set to true and not specified, defaults to 2.
        :type DefaultReplicationFactor: int
        """
        self._AutoCreateTopicEnable = None
        self._DefaultNumPartitions = None
        self._DefaultReplicationFactor = None

    @property
    def AutoCreateTopicEnable(self):
        r"""Automatic creation. true: enabled, false: not enabled
        :rtype: bool
        """
        return self._AutoCreateTopicEnable

    @AutoCreateTopicEnable.setter
    def AutoCreateTopicEnable(self, AutoCreateTopicEnable):
        self._AutoCreateTopicEnable = AutoCreateTopicEnable

    @property
    def DefaultNumPartitions(self):
        r"""Default number of partitions for a newly created topic. if AutoCreateTopicEnable is set to true and no value is set, defaults to 3.
        :rtype: int
        """
        return self._DefaultNumPartitions

    @DefaultNumPartitions.setter
    def DefaultNumPartitions(self, DefaultNumPartitions):
        self._DefaultNumPartitions = DefaultNumPartitions

    @property
    def DefaultReplicationFactor(self):
        r"""Default number of replicas for a newly created topic. if AutoCreateTopicEnable is set to true and not specified, defaults to 2.
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
    r"""ModifyInstanceAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
        :type InstanceId: str
        :param _MsgRetentionTime: Maximum retention time of instance logs, in minutes, with a value range of 1min to 90 days.
        :type MsgRetentionTime: int
        :param _InstanceName: Specifies the Name of the ckafka cluster instance.
        :type InstanceName: str
        :param _Config: Instance configuration
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesConfig`
        :param _DynamicRetentionConfig: Dynamic message retention policy configuration
        :type DynamicRetentionConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        :param _RebalanceTime: Specifies the execution time of a scheduled task for edition upgrade or configuration upgrade in Unix timestamp, accurate to the second.
        :type RebalanceTime: int
        :param _PublicNetwork: Public network bandwidth. minimum 3 Mbps. maximum 999 Mbps. only the pro edition supports filling in.
        :type PublicNetwork: int
        :param _DynamicDiskConfig: Dynamic disk expansion policy configuration.
        :type DynamicDiskConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicDiskConfig`
        :param _MaxMessageByte: Single message size at the instance level (unit: byte). value range: 1024 (excluding) to 12582912 (excluding).
        :type MaxMessageByte: int
        :param _UncleanLeaderElectionEnable: Whether to allow unsynchronized replicas to be elected as leader. valid values: 1 (enable), 0 (disable).
        :type UncleanLeaderElectionEnable: int
        :param _DeleteProtectionEnable: Instance deletion protection switch. 1: enabled; 0: disabled.
        :type DeleteProtectionEnable: int
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
        self._UncleanLeaderElectionEnable = None
        self._DeleteProtectionEnable = None

    @property
    def InstanceId(self):
        r"""ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MsgRetentionTime(self):
        r"""Maximum retention time of instance logs, in minutes, with a value range of 1min to 90 days.
        :rtype: int
        """
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def InstanceName(self):
        r"""Specifies the Name of the ckafka cluster instance.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Config(self):
        r"""Instance configuration
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def DynamicRetentionConfig(self):
        r"""Dynamic message retention policy configuration
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        """
        return self._DynamicRetentionConfig

    @DynamicRetentionConfig.setter
    def DynamicRetentionConfig(self, DynamicRetentionConfig):
        self._DynamicRetentionConfig = DynamicRetentionConfig

    @property
    def RebalanceTime(self):
        r"""Specifies the execution time of a scheduled task for edition upgrade or configuration upgrade in Unix timestamp, accurate to the second.
        :rtype: int
        """
        return self._RebalanceTime

    @RebalanceTime.setter
    def RebalanceTime(self, RebalanceTime):
        self._RebalanceTime = RebalanceTime

    @property
    def PublicNetwork(self):
        r"""Public network bandwidth. minimum 3 Mbps. maximum 999 Mbps. only the pro edition supports filling in.
        :rtype: int
        """
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def DynamicDiskConfig(self):
        warnings.warn("parameter `DynamicDiskConfig` is deprecated", DeprecationWarning) 

        r"""Dynamic disk expansion policy configuration.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DynamicDiskConfig`
        """
        return self._DynamicDiskConfig

    @DynamicDiskConfig.setter
    def DynamicDiskConfig(self, DynamicDiskConfig):
        warnings.warn("parameter `DynamicDiskConfig` is deprecated", DeprecationWarning) 

        self._DynamicDiskConfig = DynamicDiskConfig

    @property
    def MaxMessageByte(self):
        r"""Single message size at the instance level (unit: byte). value range: 1024 (excluding) to 12582912 (excluding).
        :rtype: int
        """
        return self._MaxMessageByte

    @MaxMessageByte.setter
    def MaxMessageByte(self, MaxMessageByte):
        self._MaxMessageByte = MaxMessageByte

    @property
    def UncleanLeaderElectionEnable(self):
        r"""Whether to allow unsynchronized replicas to be elected as leader. valid values: 1 (enable), 0 (disable).
        :rtype: int
        """
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def DeleteProtectionEnable(self):
        r"""Instance deletion protection switch. 1: enabled; 0: disabled.
        :rtype: int
        """
        return self._DeleteProtectionEnable

    @DeleteProtectionEnable.setter
    def DeleteProtectionEnable(self, DeleteProtectionEnable):
        self._DeleteProtectionEnable = DeleteProtectionEnable


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
        self._UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self._DeleteProtectionEnable = params.get("DeleteProtectionEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAttributesResponse(AbstractModel):
    r"""ModifyInstanceAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyInstancePreRequest(AbstractModel):
    r"""ModifyInstancePre request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
        :type InstanceId: str
        :param _DiskSize: Specifies the disk capacity in GB. value range: 100 to 500000 with a step length of 100.
Specification limits can be viewed through the following link: https://www.tencentcloud.comom/document/product/597/122562.?from_cn_redirect=1

        :type DiskSize: int
        :param _BandWidth: Peak bandwidth in MB/s.
Specifies the specification limits and corresponding step length through the following link: https://www.tencentcloud.comom/document/product/597/11745.?from_cn_redirect=1

        :type BandWidth: int
        :param _Partition: Partition upper bound. maximum value of 40000. step length of 100.
Specifies the specifications and limits that can be viewed through the following link: https://www.tencentcloud.comom/document/product/597/122563.?from_cn_redirect=1
        :type Partition: int
        """
        self._InstanceId = None
        self._DiskSize = None
        self._BandWidth = None
        self._Partition = None

    @property
    def InstanceId(self):
        r"""ckafka cluster instance Id. obtain through the API [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1).
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DiskSize(self):
        r"""Specifies the disk capacity in GB. value range: 100 to 500000 with a step length of 100.
Specification limits can be viewed through the following link: https://www.tencentcloud.comom/document/product/597/122562.?from_cn_redirect=1

        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def BandWidth(self):
        r"""Peak bandwidth in MB/s.
Specifies the specification limits and corresponding step length through the following link: https://www.tencentcloud.comom/document/product/597/11745.?from_cn_redirect=1

        :rtype: int
        """
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def Partition(self):
        r"""Partition upper bound. maximum value of 40000. step length of 100.
Specifies the specifications and limits that can be viewed through the following link: https://www.tencentcloud.comom/document/product/597/122563.?from_cn_redirect=1
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
    r"""ModifyInstancePre response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Response structure of modifying the configurations of a prepaid instance.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Response structure of modifying the configurations of a prepaid instance.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
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
            self._Result = CreateInstancePreResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyPasswordRequest(AbstractModel):
    r"""ModifyPassword request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance Id. you can obtain it by calling the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _Name: Specifies the username, which can be obtained through the [DescribeUser](https://www.tencentcloud.comom/document/product/597/40855?from_cn_redirect=1) api.
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
        r"""Instance Id. you can obtain it by calling the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""Specifies the username, which can be obtained through the [DescribeUser](https://www.tencentcloud.comom/document/product/597/40855?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Password(self):
        r"""Current user password
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def PasswordNew(self):
        r"""New user password
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
    r"""ModifyPassword response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyRoutineMaintenanceTaskRequest(AbstractModel):
    r"""ModifyRoutineMaintenanceTask request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Specifies the ckafka cluster instance id. can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :type InstanceId: str
        :param _MaintenanceType: Automated operation and maintenance category. valid values: QUOTA, ANALYSIS, RE_BALANCE, ELASTIC_BANDWIDTH.
        :type MaintenanceType: str
        :param _MaintenanceSubtype: INSTANCE_STORAGE_CAPACITY (automatic disk scale-out)/MESSAGE_RETENTION_PERIOD (dynamic MESSAGE RETENTION policy).
        :type MaintenanceSubtype: str
        :param _TopicName: Topic name
        :type TopicName: str
        :param _ConfigureThreshold: Task trigger threshold.
        :type ConfigureThreshold: int
        :param _ConfigureStepSize: Specifies the step length for task adjustment.
        :type ConfigureStepSize: int
        :param _ConfigureLimit: Task adjustment upper limit.
        :type ConfigureLimit: int
        :param _PlannedTime: Specifies the expected trigger time of the task, storing the offset in seconds from 0 AM of the current day.
        :type PlannedTime: int
        :param _ExtraConfig: Additional task information.
        :type ExtraConfig: str
        :param _Status: Task status. 0: enabled, 1: disabled.
        :type Status: int
        :param _Week: Specifies the day of the week.
        :type Week: str
        """
        self._InstanceId = None
        self._MaintenanceType = None
        self._MaintenanceSubtype = None
        self._TopicName = None
        self._ConfigureThreshold = None
        self._ConfigureStepSize = None
        self._ConfigureLimit = None
        self._PlannedTime = None
        self._ExtraConfig = None
        self._Status = None
        self._Week = None

    @property
    def InstanceId(self):
        r"""Specifies the ckafka cluster instance id. can be obtained through the [DescribeInstances](https://www.tencentcloud.comom/document/product/597/40835?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MaintenanceType(self):
        r"""Automated operation and maintenance category. valid values: QUOTA, ANALYSIS, RE_BALANCE, ELASTIC_BANDWIDTH.
        :rtype: str
        """
        return self._MaintenanceType

    @MaintenanceType.setter
    def MaintenanceType(self, MaintenanceType):
        self._MaintenanceType = MaintenanceType

    @property
    def MaintenanceSubtype(self):
        r"""INSTANCE_STORAGE_CAPACITY (automatic disk scale-out)/MESSAGE_RETENTION_PERIOD (dynamic MESSAGE RETENTION policy).
        :rtype: str
        """
        return self._MaintenanceSubtype

    @MaintenanceSubtype.setter
    def MaintenanceSubtype(self, MaintenanceSubtype):
        self._MaintenanceSubtype = MaintenanceSubtype

    @property
    def TopicName(self):
        r"""Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def ConfigureThreshold(self):
        r"""Task trigger threshold.
        :rtype: int
        """
        return self._ConfigureThreshold

    @ConfigureThreshold.setter
    def ConfigureThreshold(self, ConfigureThreshold):
        self._ConfigureThreshold = ConfigureThreshold

    @property
    def ConfigureStepSize(self):
        r"""Specifies the step length for task adjustment.
        :rtype: int
        """
        return self._ConfigureStepSize

    @ConfigureStepSize.setter
    def ConfigureStepSize(self, ConfigureStepSize):
        self._ConfigureStepSize = ConfigureStepSize

    @property
    def ConfigureLimit(self):
        r"""Task adjustment upper limit.
        :rtype: int
        """
        return self._ConfigureLimit

    @ConfigureLimit.setter
    def ConfigureLimit(self, ConfigureLimit):
        self._ConfigureLimit = ConfigureLimit

    @property
    def PlannedTime(self):
        r"""Specifies the expected trigger time of the task, storing the offset in seconds from 0 AM of the current day.
        :rtype: int
        """
        return self._PlannedTime

    @PlannedTime.setter
    def PlannedTime(self, PlannedTime):
        self._PlannedTime = PlannedTime

    @property
    def ExtraConfig(self):
        r"""Additional task information.
        :rtype: str
        """
        return self._ExtraConfig

    @ExtraConfig.setter
    def ExtraConfig(self, ExtraConfig):
        self._ExtraConfig = ExtraConfig

    @property
    def Status(self):
        r"""Task status. 0: enabled, 1: disabled.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Week(self):
        r"""Specifies the day of the week.
        :rtype: str
        """
        return self._Week

    @Week.setter
    def Week(self, Week):
        self._Week = Week


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MaintenanceType = params.get("MaintenanceType")
        self._MaintenanceSubtype = params.get("MaintenanceSubtype")
        self._TopicName = params.get("TopicName")
        self._ConfigureThreshold = params.get("ConfigureThreshold")
        self._ConfigureStepSize = params.get("ConfigureStepSize")
        self._ConfigureLimit = params.get("ConfigureLimit")
        self._PlannedTime = params.get("PlannedTime")
        self._ExtraConfig = params.get("ExtraConfig")
        self._Status = params.get("Status")
        self._Week = params.get("Week")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoutineMaintenanceTaskResponse(AbstractModel):
    r"""ModifyRoutineMaintenanceTask response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned results.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned results.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyTopicAttributesRequest(AbstractModel):
    r"""ModifyTopicAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id.
        :type InstanceId: str
        :param _TopicName: Topic name
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
        :param _MaxMessageBytes: Max message size in bytes. Max value: 8,388,608 bytes (8 MB).
        :type MaxMessageBytes: int
        :param _SegmentMs: Duration of Segment shard scrolling in milliseconds. current min value is 86400000 ms.
        :type SegmentMs: int
        :param _CleanUpPolicy: Message deletion policy. Valid values: delete, compact
        :type CleanUpPolicy: str
        :param _IpWhiteList: IP allowlist, which is required if the value of `enableWhileList` is 1.
        :type IpWhiteList: list of str
        :param _EnableAclRule: Preset ACL rule. `1`: enable, `0`: disable. Default value: `0`.
        :type EnableAclRule: int
        :param _AclRuleName: ACL rule name.
        :type AclRuleName: str
        :param _RetentionBytes: Message retention file size in bytes, which is an optional parameter. Default value: -1. Currently, the min value that can be entered is 1,048,576 B.
        :type RetentionBytes: int
        :param _Tags: Tag list.
        :type Tags: list of Tag
        :param _QuotaProducerByteRate: Production traffic throttling in MB/s. set to -1 to disable throttling.
        :type QuotaProducerByteRate: int
        :param _QuotaConsumerByteRate: Consumption traffic throttling in MB/s. set to -1 for unlimited consumption.
        :type QuotaConsumerByteRate: int
        :param _ReplicaNum: Number of topic replicas. valid values: 1, 3.
        :type ReplicaNum: int
        :param _LogMsgTimestampType: Specifies the time type for message saving: CreateTime/LogAppendTime.
        :type LogMsgTimestampType: str
        """
        self._InstanceId = None
        self._TopicName = None
        self._Note = None
        self._EnableWhiteList = None
        self._MinInsyncReplicas = None
        self._UncleanLeaderElectionEnable = None
        self._RetentionMs = None
        self._MaxMessageBytes = None
        self._SegmentMs = None
        self._CleanUpPolicy = None
        self._IpWhiteList = None
        self._EnableAclRule = None
        self._AclRuleName = None
        self._RetentionBytes = None
        self._Tags = None
        self._QuotaProducerByteRate = None
        self._QuotaConsumerByteRate = None
        self._ReplicaNum = None
        self._LogMsgTimestampType = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        r"""Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Note(self):
        r"""Topic remarks string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def EnableWhiteList(self):
        r"""IP allowlist switch. 1: enabled, 0: disabled.
        :rtype: int
        """
        return self._EnableWhiteList

    @EnableWhiteList.setter
    def EnableWhiteList(self, EnableWhiteList):
        self._EnableWhiteList = EnableWhiteList

    @property
    def MinInsyncReplicas(self):
        r"""Default value: 1.
        :rtype: int
        """
        return self._MinInsyncReplicas

    @MinInsyncReplicas.setter
    def MinInsyncReplicas(self, MinInsyncReplicas):
        self._MinInsyncReplicas = MinInsyncReplicas

    @property
    def UncleanLeaderElectionEnable(self):
        r"""0: false, 1: true. Default value: 0.
        :rtype: int
        """
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def RetentionMs(self):
        r"""Message retention period in ms. The current minimum value is 60,000 ms.
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def MaxMessageBytes(self):
        r"""Max message size in bytes. Max value: 8,388,608 bytes (8 MB).
        :rtype: int
        """
        return self._MaxMessageBytes

    @MaxMessageBytes.setter
    def MaxMessageBytes(self, MaxMessageBytes):
        self._MaxMessageBytes = MaxMessageBytes

    @property
    def SegmentMs(self):
        r"""Duration of Segment shard scrolling in milliseconds. current min value is 86400000 ms.
        :rtype: int
        """
        return self._SegmentMs

    @SegmentMs.setter
    def SegmentMs(self, SegmentMs):
        self._SegmentMs = SegmentMs

    @property
    def CleanUpPolicy(self):
        r"""Message deletion policy. Valid values: delete, compact
        :rtype: str
        """
        return self._CleanUpPolicy

    @CleanUpPolicy.setter
    def CleanUpPolicy(self, CleanUpPolicy):
        self._CleanUpPolicy = CleanUpPolicy

    @property
    def IpWhiteList(self):
        r"""IP allowlist, which is required if the value of `enableWhileList` is 1.
        :rtype: list of str
        """
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList

    @property
    def EnableAclRule(self):
        r"""Preset ACL rule. `1`: enable, `0`: disable. Default value: `0`.
        :rtype: int
        """
        return self._EnableAclRule

    @EnableAclRule.setter
    def EnableAclRule(self, EnableAclRule):
        self._EnableAclRule = EnableAclRule

    @property
    def AclRuleName(self):
        r"""ACL rule name.
        :rtype: str
        """
        return self._AclRuleName

    @AclRuleName.setter
    def AclRuleName(self, AclRuleName):
        self._AclRuleName = AclRuleName

    @property
    def RetentionBytes(self):
        r"""Message retention file size in bytes, which is an optional parameter. Default value: -1. Currently, the min value that can be entered is 1,048,576 B.
        :rtype: int
        """
        return self._RetentionBytes

    @RetentionBytes.setter
    def RetentionBytes(self, RetentionBytes):
        self._RetentionBytes = RetentionBytes

    @property
    def Tags(self):
        r"""Tag list.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def QuotaProducerByteRate(self):
        r"""Production traffic throttling in MB/s. set to -1 to disable throttling.
        :rtype: int
        """
        return self._QuotaProducerByteRate

    @QuotaProducerByteRate.setter
    def QuotaProducerByteRate(self, QuotaProducerByteRate):
        self._QuotaProducerByteRate = QuotaProducerByteRate

    @property
    def QuotaConsumerByteRate(self):
        r"""Consumption traffic throttling in MB/s. set to -1 for unlimited consumption.
        :rtype: int
        """
        return self._QuotaConsumerByteRate

    @QuotaConsumerByteRate.setter
    def QuotaConsumerByteRate(self, QuotaConsumerByteRate):
        self._QuotaConsumerByteRate = QuotaConsumerByteRate

    @property
    def ReplicaNum(self):
        r"""Number of topic replicas. valid values: 1, 3.
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def LogMsgTimestampType(self):
        r"""Specifies the time type for message saving: CreateTime/LogAppendTime.
        :rtype: str
        """
        return self._LogMsgTimestampType

    @LogMsgTimestampType.setter
    def LogMsgTimestampType(self, LogMsgTimestampType):
        self._LogMsgTimestampType = LogMsgTimestampType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._Note = params.get("Note")
        self._EnableWhiteList = params.get("EnableWhiteList")
        self._MinInsyncReplicas = params.get("MinInsyncReplicas")
        self._UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self._RetentionMs = params.get("RetentionMs")
        self._MaxMessageBytes = params.get("MaxMessageBytes")
        self._SegmentMs = params.get("SegmentMs")
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
        self._LogMsgTimestampType = params.get("LogMsgTimestampType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicAttributesResponse(AbstractModel):
    r"""ModifyTopicAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Returned result.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class OperateResponseData(AbstractModel):
    r"""Data structure returned by operation

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID.
        :type FlowId: int
        :param _RouteDTO: RouteIdDto
        :type RouteDTO: :class:`tencentcloud.ckafka.v20190819.models.RouteDTO`
        """
        self._FlowId = None
        self._RouteDTO = None

    @property
    def FlowId(self):
        r"""Flow ID.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RouteDTO(self):
        r"""RouteIdDto
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
    r"""Partition entity

    """

    def __init__(self):
        r"""
        :param _PartitionId: Partition ID
        :type PartitionId: int
        """
        self._PartitionId = None

    @property
    def PartitionId(self):
        r"""Partition ID
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
    r"""Partition and offset

    """

    def __init__(self):
        r"""
        :param _Partition: Partition
        :type Partition: str
        :param _Offset: Specifies the offset.
        :type Offset: int
        """
        self._Partition = None
        self._Offset = None

    @property
    def Partition(self):
        r"""Partition
        :rtype: str
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        r"""Specifies the offset.
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
    r"""Partition information

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
        r"""Partition.
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        r"""Partition consumption offset.
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
    r"""Message price entity

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
        r"""Discounted price
        :rtype: float
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def TotalCost(self):
        r"""Original price
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
    r"""Region entity object

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID
        :type RegionId: int
        :param _RegionName: Region name
        :type RegionName: str
        :param _AreaName: Area name
        :type AreaName: str
        :param _RegionCode: Region code.
        :type RegionCode: str
        :param _RegionCodeV3: Region code (V3 version).
        :type RegionCodeV3: str
        :param _Support: Specifies the default value does not support any special type instance type.
        :type Support: str
        :param _Ipv6: Whether ipv6 is supported. 0: indicates no support. 1: indicates support.
        :type Ipv6: int
        :param _MultiZone: Whether cross-az is supported. valid values: 0 (unsupported), 1 (supported).
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
        r"""Region ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        r"""Region name
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def AreaName(self):
        r"""Area name
        :rtype: str
        """
        return self._AreaName

    @AreaName.setter
    def AreaName(self, AreaName):
        self._AreaName = AreaName

    @property
    def RegionCode(self):
        r"""Region code.
        :rtype: str
        """
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode

    @property
    def RegionCodeV3(self):
        r"""Region code (V3 version).
        :rtype: str
        """
        return self._RegionCodeV3

    @RegionCodeV3.setter
    def RegionCodeV3(self, RegionCodeV3):
        self._RegionCodeV3 = RegionCodeV3

    @property
    def Support(self):
        r"""Specifies the default value does not support any special type instance type.
        :rtype: str
        """
        return self._Support

    @Support.setter
    def Support(self, Support):
        self._Support = Support

    @property
    def Ipv6(self):
        r"""Whether ipv6 is supported. 0: indicates no support. 1: indicates support.
        :rtype: int
        """
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def MultiZone(self):
        r"""Whether cross-az is supported. valid values: 0 (unsupported), 1 (supported).
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
    r"""Route entity object

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
        :param _VipType: Specifies the network type of the route (3: vpc routing; 7: internal support route; 1: public network route).
        :type VipType: int
        :param _VipList: Virtual IP list
        :type VipList: list of VipEntity
        :param _Domain: Domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _DomainPort: Domain name port
Note: this field may return null, indicating that no valid values can be obtained.
        :type DomainPort: int
        :param _DeleteTimestamp: Timestamp.
        :type DeleteTimestamp: str
        :param _Subnet: Specifies the subnet Id.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Subnet: str
        :param _BrokerVipList: Virtual IP list (1:1 broker node).
        :type BrokerVipList: list of VipEntity
        :param _VpcId: VPC Id. specifies the Id of the vpc.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _Note: Remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :type Note: str
        :param _Status: Route status. 1: creating, 2: creation succeeded, 3: creation failed, 4: deleting, 6: deletion failed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        """
        self._AccessType = None
        self._RouteId = None
        self._VipType = None
        self._VipList = None
        self._Domain = None
        self._DomainPort = None
        self._DeleteTimestamp = None
        self._Subnet = None
        self._BrokerVipList = None
        self._VpcId = None
        self._Note = None
        self._Status = None

    @property
    def AccessType(self):
        r"""Instance connection method
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
        r"""Route ID
        :rtype: int
        """
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId

    @property
    def VipType(self):
        r"""Specifies the network type of the route (3: vpc routing; 7: internal support route; 1: public network route).
        :rtype: int
        """
        return self._VipType

    @VipType.setter
    def VipType(self, VipType):
        self._VipType = VipType

    @property
    def VipList(self):
        r"""Virtual IP list
        :rtype: list of VipEntity
        """
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList

    @property
    def Domain(self):
        r"""Domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainPort(self):
        r"""Domain name port
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DomainPort

    @DomainPort.setter
    def DomainPort(self, DomainPort):
        self._DomainPort = DomainPort

    @property
    def DeleteTimestamp(self):
        r"""Timestamp.
        :rtype: str
        """
        return self._DeleteTimestamp

    @DeleteTimestamp.setter
    def DeleteTimestamp(self, DeleteTimestamp):
        self._DeleteTimestamp = DeleteTimestamp

    @property
    def Subnet(self):
        r"""Specifies the subnet Id.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Subnet

    @Subnet.setter
    def Subnet(self, Subnet):
        self._Subnet = Subnet

    @property
    def BrokerVipList(self):
        r"""Virtual IP list (1:1 broker node).
        :rtype: list of VipEntity
        """
        return self._BrokerVipList

    @BrokerVipList.setter
    def BrokerVipList(self, BrokerVipList):
        self._BrokerVipList = BrokerVipList

    @property
    def VpcId(self):
        r"""VPC Id. specifies the Id of the vpc.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Note(self):
        r"""Remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Status(self):
        r"""Route status. 1: creating, 2: creation succeeded, 3: creation failed, 4: deleting, 6: deletion failed.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


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
        self._Subnet = params.get("Subnet")
        if params.get("BrokerVipList") is not None:
            self._BrokerVipList = []
            for item in params.get("BrokerVipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self._BrokerVipList.append(obj)
        self._VpcId = params.get("VpcId")
        self._Note = params.get("Note")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteDTO(AbstractModel):
    r"""RouteDTO

    """

    def __init__(self):
        r"""
        :param _RouteId: Route ID
        :type RouteId: int
        """
        self._RouteId = None

    @property
    def RouteId(self):
        r"""Route ID
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
        


class RouteFilter(AbstractModel):
    r"""Routing list filter.

    """

    def __init__(self):
        r"""
        :param _Name: Filters by name. currently supports security-group-id. filters by security group association.
        :type Name: str
        :param _Values: Filter value. when the filter name is security-group-id, only supports transmission of one value.
        :type Values: list of str
        :param _Relation: Filter relationship. supports IN and NOT_IN. default is IN.
        :type Relation: str
        """
        self._Name = None
        self._Values = None
        self._Relation = None

    @property
    def Name(self):
        r"""Filters by name. currently supports security-group-id. filters by security group association.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""Filter value. when the filter name is security-group-id, only supports transmission of one value.
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Relation(self):
        r"""Filter relationship. supports IN and NOT_IN. default is IN.
        :rtype: str
        """
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._Relation = params.get("Relation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteResponse(AbstractModel):
    r"""Returned object for route information

    """

    def __init__(self):
        r"""
        :param _Routers: Route Information List
        :type Routers: list of Route
        """
        self._Routers = None

    @property
    def Routers(self):
        r"""Route Information List
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
    r"""Sales information of versions.

    """

    def __init__(self):
        r"""
        :param _Flag: The manually configured flag. valid values: true (sold-out), false (available).
        :type Flag: bool
        :param _Version: Specifies the ckafka version number (1.1.1/2.4.2/0.10.2).
        :type Version: str
        :param _Platform: Pro edition, standard version flag.
        :type Platform: str
        :param _SoldOut: Specifies whether the item is sold-out. valid values: true (sold-out).
        :type SoldOut: bool
        """
        self._Flag = None
        self._Version = None
        self._Platform = None
        self._SoldOut = None

    @property
    def Flag(self):
        r"""The manually configured flag. valid values: true (sold-out), false (available).
        :rtype: bool
        """
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def Version(self):
        r"""Specifies the ckafka version number (1.1.1/2.4.2/0.10.2).
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Platform(self):
        r"""Pro edition, standard version flag.
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def SoldOut(self):
        r"""Specifies whether the item is sold-out. valid values: true (sold-out).
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
        


class ScalingDownResp(AbstractModel):
    r"""Instance downsizing response.

    """

    def __init__(self):
        r"""
        :param _DealNames: Order ID list
        :type DealNames: list of str
        """
        self._DealNames = None

    @property
    def DealNames(self):
        r"""Order ID list
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames


    def _deserialize(self, params):
        self._DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupRoute(AbstractModel):
    r"""Security group routing information.

    """

    def __init__(self):
        r"""
        :param _InstanceRoute: Specifies the routing information.
        :type InstanceRoute: :class:`tencentcloud.ckafka.v20190819.models.InstanceRoute`
        :param _SecurityGroupIds: Specifies the security group list to associate.
        :type SecurityGroupIds: list of str
        :param _InstanceName: CKafka cluster instance name.
        :type InstanceName: str
        :param _VpcId: Specifies the route vpcId.
        :type VpcId: str
        :param _Vip: Route vip.
        :type Vip: str
        """
        self._InstanceRoute = None
        self._SecurityGroupIds = None
        self._InstanceName = None
        self._VpcId = None
        self._Vip = None

    @property
    def InstanceRoute(self):
        r"""Specifies the routing information.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceRoute`
        """
        return self._InstanceRoute

    @InstanceRoute.setter
    def InstanceRoute(self, InstanceRoute):
        self._InstanceRoute = InstanceRoute

    @property
    def SecurityGroupIds(self):
        r"""Specifies the security group list to associate.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InstanceName(self):
        r"""CKafka cluster instance name.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def VpcId(self):
        r"""Specifies the route vpcId.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Vip(self):
        r"""Route vip.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        if params.get("InstanceRoute") is not None:
            self._InstanceRoute = InstanceRoute()
            self._InstanceRoute._deserialize(params.get("InstanceRoute"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._InstanceName = params.get("InstanceName")
        self._VpcId = params.get("VpcId")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupRouteResp(AbstractModel):
    r"""Security group routing information returned results.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of eligible security group routes.
        :type TotalCount: int
        :param _SecurityGroupRoutes: Eligible security group route information list.
        :type SecurityGroupRoutes: list of SecurityGroupRoute
        """
        self._TotalCount = None
        self._SecurityGroupRoutes = None

    @property
    def TotalCount(self):
        r"""Total number of eligible security group routes.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SecurityGroupRoutes(self):
        r"""Eligible security group route information list.
        :rtype: list of SecurityGroupRoute
        """
        return self._SecurityGroupRoutes

    @SecurityGroupRoutes.setter
    def SecurityGroupRoutes(self, SecurityGroupRoutes):
        self._SecurityGroupRoutes = SecurityGroupRoutes


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SecurityGroupRoutes") is not None:
            self._SecurityGroupRoutes = []
            for item in params.get("SecurityGroupRoutes"):
                obj = SecurityGroupRoute()
                obj._deserialize(item)
                self._SecurityGroupRoutes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessageRequest(AbstractModel):
    r"""SendMessage request structure.

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
        r"""Datahub access ID.
        :rtype: str
        """
        return self._DataHubId

    @DataHubId.setter
    def DataHubId(self, DataHubId):
        self._DataHubId = DataHubId

    @property
    def Message(self):
        r"""Content of the message that has been sent. Up to 500 messages can be sent in a single request.
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
    r"""SendMessage response structure.

    """

    def __init__(self):
        r"""
        :param _MessageId: Message ID list.
        :type MessageId: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MessageId = None
        self._RequestId = None

    @property
    def MessageId(self):
        r"""Message ID list.
        :rtype: list of str
        """
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

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
        self._MessageId = params.get("MessageId")
        self._RequestId = params.get("RequestId")


class SubscribedInfo(AbstractModel):
    r"""Subscribed message entity

    """

    def __init__(self):
        r"""
        :param _TopicName: Subscribed topic name
        :type TopicName: str
        :param _Partition: Specifies the subscription partition.
        :type Partition: list of int
        :param _PartitionOffset: Specifies the partition offset information.
        :type PartitionOffset: list of PartitionOffset
        :param _TopicId: Subscribed topic ID.
        :type TopicId: str
        """
        self._TopicName = None
        self._Partition = None
        self._PartitionOffset = None
        self._TopicId = None

    @property
    def TopicName(self):
        r"""Subscribed topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Partition(self):
        r"""Specifies the subscription partition.
        :rtype: list of int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def PartitionOffset(self):
        r"""Specifies the partition offset information.
        :rtype: list of PartitionOffset
        """
        return self._PartitionOffset

    @PartitionOffset.setter
    def PartitionOffset(self, PartitionOffset):
        self._PartitionOffset = PartitionOffset

    @property
    def TopicId(self):
        r"""Subscribed topic ID.
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
    r"""Tag object in instance details

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
        r"""Tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Tag value
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
    r"""Returned task status

    """

    def __init__(self):
        r"""
        :param _Status: Task status. `0` (Successful), `1` (Failed), `2` ( Running)
        :type Status: int
        :param _Output: Output information.
        :type Output: str
        """
        self._Status = None
        self._Output = None

    @property
    def Status(self):
        r"""Task status. `0` (Successful), `1` (Failed), `2` ( Running)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Output(self):
        r"""Output information.
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
    r"""Returned topic object

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
        r"""Topic ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        r"""Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Note(self):
        r"""Remarks
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
    r"""Returned topic attributes result entity

    """

    def __init__(self):
        r"""
        :param _TopicId: Topic ID
        :type TopicId: str
        :param _CreateTime: Specifies the unix second-level timestamp of the creation time.
        :type CreateTime: int
        :param _Note: Describes the topic remark.
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
        :param _EnableAclRule: ACL preset policy switch. valid values: 1 (on); 0 (off).
        :type EnableAclRule: int
        :param _AclRuleList: Preset policy list.
        :type AclRuleList: list of AclRule
        :param _QuotaConfig: topic throttling policy.
        :type QuotaConfig: :class:`tencentcloud.ckafka.v20190819.models.InstanceQuotaConfigResp`
        :param _ReplicaNum: Number of replicas
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
        r"""Topic ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def CreateTime(self):
        r"""Specifies the unix second-level timestamp of the creation time.
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Note(self):
        r"""Describes the topic remark.
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def PartitionNum(self):
        r"""Number of partitions
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def EnableWhiteList(self):
        r"""IP allowlist switch. 1: enabled, 0: disabled
        :rtype: int
        """
        return self._EnableWhiteList

    @EnableWhiteList.setter
    def EnableWhiteList(self, EnableWhiteList):
        self._EnableWhiteList = EnableWhiteList

    @property
    def IpWhiteList(self):
        r"""IP allowlist list
        :rtype: list of str
        """
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList

    @property
    def Config(self):
        r"""Topic configuration array
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.Config`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Partitions(self):
        r"""Partition details
        :rtype: list of TopicPartitionDO
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def EnableAclRule(self):
        r"""ACL preset policy switch. valid values: 1 (on); 0 (off).
        :rtype: int
        """
        return self._EnableAclRule

    @EnableAclRule.setter
    def EnableAclRule(self, EnableAclRule):
        self._EnableAclRule = EnableAclRule

    @property
    def AclRuleList(self):
        r"""Preset policy list.
        :rtype: list of AclRule
        """
        return self._AclRuleList

    @AclRuleList.setter
    def AclRuleList(self, AclRuleList):
        self._AclRuleList = AclRuleList

    @property
    def QuotaConfig(self):
        r"""topic throttling policy.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceQuotaConfigResp`
        """
        return self._QuotaConfig

    @QuotaConfig.setter
    def QuotaConfig(self, QuotaConfig):
        self._QuotaConfig = QuotaConfig

    @property
    def ReplicaNum(self):
        r"""Number of replicas
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
    r"""Topic details

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name
        :type TopicName: str
        :param _TopicId: Topic Id.
        :type TopicId: str
        :param _PartitionNum: Number of partitions
        :type PartitionNum: int
        :param _ReplicaNum: Number of topic replicas. valid values: 1, 3.
        :type ReplicaNum: int
        :param _Note: Remarks.
        :type Note: str
        :param _CreateTime: Creation time
        :type CreateTime: int
        :param _EnableWhiteList: Whether to enable IP authentication allowlist. true: yes, false: no
        :type EnableWhiteList: bool
        :param _IpWhiteListCount: Number of IPs in IP allowlist
        :type IpWhiteListCount: int
        :param _ForwardCosBucket: Data backup cos bucket. specifies the bucket address for archiving to cos.
        :type ForwardCosBucket: str
        :param _ForwardStatus: Status of data backup to COS. 1: not enabled, 0: enabled
        :type ForwardStatus: int
        :param _ForwardInterval: Frequency of data backup to COS
        :type ForwardInterval: int
        :param _Config: Advanced configuration.
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`
        :param _RetentionTimeConfig: Message retention period configuration (used for dynamic configuration change records).
        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.TopicRetentionTimeConfigRsp`
        :param _Status: 0: normal. 1: deleted. 2: deleting.
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
        r"""Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        r"""Topic Id.
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionNum(self):
        r"""Number of partitions
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def ReplicaNum(self):
        r"""Number of topic replicas. valid values: 1, 3.
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def Note(self):
        r"""Remarks.
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def CreateTime(self):
        r"""Creation time
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EnableWhiteList(self):
        r"""Whether to enable IP authentication allowlist. true: yes, false: no
        :rtype: bool
        """
        return self._EnableWhiteList

    @EnableWhiteList.setter
    def EnableWhiteList(self, EnableWhiteList):
        self._EnableWhiteList = EnableWhiteList

    @property
    def IpWhiteListCount(self):
        r"""Number of IPs in IP allowlist
        :rtype: int
        """
        return self._IpWhiteListCount

    @IpWhiteListCount.setter
    def IpWhiteListCount(self, IpWhiteListCount):
        self._IpWhiteListCount = IpWhiteListCount

    @property
    def ForwardCosBucket(self):
        r"""Data backup cos bucket. specifies the bucket address for archiving to cos.
        :rtype: str
        """
        return self._ForwardCosBucket

    @ForwardCosBucket.setter
    def ForwardCosBucket(self, ForwardCosBucket):
        self._ForwardCosBucket = ForwardCosBucket

    @property
    def ForwardStatus(self):
        r"""Status of data backup to COS. 1: not enabled, 0: enabled
        :rtype: int
        """
        return self._ForwardStatus

    @ForwardStatus.setter
    def ForwardStatus(self, ForwardStatus):
        self._ForwardStatus = ForwardStatus

    @property
    def ForwardInterval(self):
        r"""Frequency of data backup to COS
        :rtype: int
        """
        return self._ForwardInterval

    @ForwardInterval.setter
    def ForwardInterval(self, ForwardInterval):
        self._ForwardInterval = ForwardInterval

    @property
    def Config(self):
        r"""Advanced configuration.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.Config`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def RetentionTimeConfig(self):
        r"""Message retention period configuration (used for dynamic configuration change records).
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicRetentionTimeConfigRsp`
        """
        return self._RetentionTimeConfig

    @RetentionTimeConfig.setter
    def RetentionTimeConfig(self, RetentionTimeConfig):
        self._RetentionTimeConfig = RetentionTimeConfig

    @property
    def Status(self):
        r"""0: normal. 1: deleted. 2: deleting.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        r"""Tag list
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
    r"""Returned topic details entity

    """

    def __init__(self):
        r"""
        :param _TopicList: List of returned topic details.
        :type TopicList: list of TopicDetail
        :param _TotalCount: Number of all eligible topic details
        :type TotalCount: int
        """
        self._TopicList = None
        self._TotalCount = None

    @property
    def TopicList(self):
        r"""List of returned topic details.
        :rtype: list of TopicDetail
        """
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList

    @property
    def TotalCount(self):
        r"""Number of all eligible topic details
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
    r"""Topic replica and details

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
        :param _BeginOffset: Start Offset.
        :type BeginOffset: int
        :param _EndOffset: End Offset.
        :type EndOffset: int
        :param _MessageCount: Message count.
        :type MessageCount: int
        :param _OutOfSyncReplica: Unsynced replica.
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
        r"""Partition name
        :rtype: str
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Leader(self):
        r"""Leader ID
        :rtype: int
        """
        return self._Leader

    @Leader.setter
    def Leader(self, Leader):
        self._Leader = Leader

    @property
    def Replica(self):
        r"""Replica set
        :rtype: str
        """
        return self._Replica

    @Replica.setter
    def Replica(self, Replica):
        self._Replica = Replica

    @property
    def InSyncReplica(self):
        r"""ISR
        :rtype: str
        """
        return self._InSyncReplica

    @InSyncReplica.setter
    def InSyncReplica(self, InSyncReplica):
        self._InSyncReplica = InSyncReplica

    @property
    def BeginOffset(self):
        r"""Start Offset.
        :rtype: int
        """
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def EndOffset(self):
        r"""End Offset.
        :rtype: int
        """
        return self._EndOffset

    @EndOffset.setter
    def EndOffset(self, EndOffset):
        self._EndOffset = EndOffset

    @property
    def MessageCount(self):
        r"""Message count.
        :rtype: int
        """
        return self._MessageCount

    @MessageCount.setter
    def MessageCount(self, MessageCount):
        self._MessageCount = MessageCount

    @property
    def OutOfSyncReplica(self):
        r"""Unsynced replica.
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
    r"""Set of topic replicas and details

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
        r"""Set of topic details and replicas
        :rtype: list of TopicInSyncReplicaInfo
        """
        return self._TopicInSyncReplicaList

    @TopicInSyncReplicaList.setter
    def TopicInSyncReplicaList(self, TopicInSyncReplicaList):
        self._TopicInSyncReplicaList = TopicInSyncReplicaList

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
    r"""Partition details

    """

    def __init__(self):
        r"""
        :param _Partition: Partition ID. specifies the Partition ID.
        :type Partition: int
        :param _LeaderStatus: Leader running status. 0 means running normally.
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
        r"""Partition ID. specifies the Partition ID.
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def LeaderStatus(self):
        r"""Leader running status. 0 means running normally.
        :rtype: int
        """
        return self._LeaderStatus

    @LeaderStatus.setter
    def LeaderStatus(self, LeaderStatus):
        self._LeaderStatus = LeaderStatus

    @property
    def IsrNum(self):
        r"""ISR quantity
        :rtype: int
        """
        return self._IsrNum

    @IsrNum.setter
    def IsrNum(self, IsrNum):
        self._IsrNum = IsrNum

    @property
    def ReplicaNum(self):
        r"""Number of replicas
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
    r"""`TopicResponse` returned uniformly

    """

    def __init__(self):
        r"""
        :param _TopicList: List of returned topic information.
        :type TopicList: list of Topic
        :param _TotalCount: Number of eligible topics.
        :type TotalCount: int
        """
        self._TopicList = None
        self._TotalCount = None

    @property
    def TopicList(self):
        r"""List of returned topic information.
        :rtype: list of Topic
        """
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList

    @property
    def TotalCount(self):
        r"""Number of eligible topics.
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
    r"""Information returned for topic message retention time configuration

    """

    def __init__(self):
        r"""
        :param _Expect: Expected value, the message retention period (in minutes) set by user configuration.
        :type Expect: int
        :param _Current: Current value, which is the current effective value (may contain dynamic adjustment in minutes).
        :type Current: int
        :param _ModTimeStamp: Last modified time.
        :type ModTimeStamp: int
        """
        self._Expect = None
        self._Current = None
        self._ModTimeStamp = None

    @property
    def Expect(self):
        r"""Expected value, the message retention period (in minutes) set by user configuration.
        :rtype: int
        """
        return self._Expect

    @Expect.setter
    def Expect(self, Expect):
        self._Expect = Expect

    @property
    def Current(self):
        r"""Current value, which is the current effective value (may contain dynamic adjustment in minutes).
        :rtype: int
        """
        return self._Current

    @Current.setter
    def Current(self, Current):
        self._Current = Current

    @property
    def ModTimeStamp(self):
        r"""Last modified time.
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
    r"""`DescribeTopicSubscribeGroup` output parameters

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _StatusCountInfo: Number of consumer group status
        :type StatusCountInfo: str
        :param _GroupsInfo: Consumer group information.
        :type GroupsInfo: list of GroupInfoResponse
        :param _Status: Indicates whether the request is asynchronous. instances with fewer groups will return results directly with Status as 1. when there are more groups, the cache will be updated asynchronously. no group information will be returned when Status is 0 until the update is complete and results are returned with Status as 1.
        :type Status: int
        """
        self._TotalCount = None
        self._StatusCountInfo = None
        self._GroupsInfo = None
        self._Status = None

    @property
    def TotalCount(self):
        r"""Total number
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def StatusCountInfo(self):
        r"""Number of consumer group status
        :rtype: str
        """
        return self._StatusCountInfo

    @StatusCountInfo.setter
    def StatusCountInfo(self, StatusCountInfo):
        self._StatusCountInfo = StatusCountInfo

    @property
    def GroupsInfo(self):
        r"""Consumer group information.
        :rtype: list of GroupInfoResponse
        """
        return self._GroupsInfo

    @GroupsInfo.setter
    def GroupsInfo(self, GroupsInfo):
        self._GroupsInfo = GroupsInfo

    @property
    def Status(self):
        r"""Indicates whether the request is asynchronous. instances with fewer groups will return results directly with Status as 1. when there are more groups, the cache will be updated asynchronously. no group information will be returned when Status is 0 until the update is complete and results are returned with Status as 1.
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
        


class UpgradeBrokerVersionRequest(AbstractModel):
    r"""UpgradeBrokerVersion request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ckafka cluster instance Id.
        :type InstanceId: str
        :param _Type: 1. smooth configuration upgrade 2. vertical configuration upgrade.
        :type Type: int
        :param _SourceVersion: Version number
        :type SourceVersion: str
        :param _TargetVersion: Version number
        :type TargetVersion: str
        :param _DelayTimeStamp: Delay time.
        :type DelayTimeStamp: str
        """
        self._InstanceId = None
        self._Type = None
        self._SourceVersion = None
        self._TargetVersion = None
        self._DelayTimeStamp = None

    @property
    def InstanceId(self):
        r"""The ckafka cluster instance Id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        r"""1. smooth configuration upgrade 2. vertical configuration upgrade.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SourceVersion(self):
        r"""Version number
        :rtype: str
        """
        return self._SourceVersion

    @SourceVersion.setter
    def SourceVersion(self, SourceVersion):
        self._SourceVersion = SourceVersion

    @property
    def TargetVersion(self):
        r"""Version number
        :rtype: str
        """
        return self._TargetVersion

    @TargetVersion.setter
    def TargetVersion(self, TargetVersion):
        self._TargetVersion = TargetVersion

    @property
    def DelayTimeStamp(self):
        r"""Delay time.
        :rtype: str
        """
        return self._DelayTimeStamp

    @DelayTimeStamp.setter
    def DelayTimeStamp(self, DelayTimeStamp):
        self._DelayTimeStamp = DelayTimeStamp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._SourceVersion = params.get("SourceVersion")
        self._TargetVersion = params.get("TargetVersion")
        self._DelayTimeStamp = params.get("DelayTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeBrokerVersionResponse(AbstractModel):
    r"""UpgradeBrokerVersion response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Upgrade result.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Upgrade result.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
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
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class User(AbstractModel):
    r"""User entity

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
        r"""User ID
        :rtype: int
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Name(self):
        r"""Username
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreateTime(self):
        r"""Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""Last updated time
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
    r"""Returned user entity

    """

    def __init__(self):
        r"""
        :param _Users: Specifies the eligible users list.
        :type Users: list of User
        :param _TotalCount: Total number of eligible users
        :type TotalCount: int
        """
        self._Users = None
        self._TotalCount = None

    @property
    def Users(self):
        r"""Specifies the eligible users list.
        :rtype: list of User
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def TotalCount(self):
        r"""Total number of eligible users
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
    r"""Virtual IP entity

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
        r"""Virtual IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""Virtual port
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
    r"""Zone information entity

    """

    def __init__(self):
        r"""
        :param _ZoneId: Availability zone
        :type ZoneId: str
        :param _IsInternalApp: Whether it is an internal application.
        :type IsInternalApp: int
        :param _AppId: Application identifier
        :type AppId: int
        :param _Flag: Indicates whether the AZ is sold out. true indicates sold out. false indicates not sold out.
        :type Flag: bool
        :param _ZoneName: Availability zone name.
        :type ZoneName: str
        :param _ZoneStatus: Availability zone status. enumerates example: 3: enable, 4: disable. availability zone status is subject to SoldOut.
        :type ZoneStatus: int
        :param _Exflag: Extra flag
        :type Exflag: str
        :param _SoldOut: Specifies whether the item is sold-out. valid values: true (sold-out), false (not sold out).
        :type SoldOut: str
        :param _SalesInfo: Specifies the sell-out information of the standard version.
        :type SalesInfo: list of SaleInfo
        :param _ExtraFlag: Additional flag.
        :type ExtraFlag: str
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
        self._ExtraFlag = None

    @property
    def ZoneId(self):
        r"""Availability zone
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IsInternalApp(self):
        r"""Whether it is an internal application.
        :rtype: int
        """
        return self._IsInternalApp

    @IsInternalApp.setter
    def IsInternalApp(self, IsInternalApp):
        self._IsInternalApp = IsInternalApp

    @property
    def AppId(self):
        r"""Application identifier
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Flag(self):
        r"""Indicates whether the AZ is sold out. true indicates sold out. false indicates not sold out.
        :rtype: bool
        """
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def ZoneName(self):
        r"""Availability zone name.
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneStatus(self):
        r"""Availability zone status. enumerates example: 3: enable, 4: disable. availability zone status is subject to SoldOut.
        :rtype: int
        """
        return self._ZoneStatus

    @ZoneStatus.setter
    def ZoneStatus(self, ZoneStatus):
        self._ZoneStatus = ZoneStatus

    @property
    def Exflag(self):
        warnings.warn("parameter `Exflag` is deprecated", DeprecationWarning) 

        r"""Extra flag
        :rtype: str
        """
        return self._Exflag

    @Exflag.setter
    def Exflag(self, Exflag):
        warnings.warn("parameter `Exflag` is deprecated", DeprecationWarning) 

        self._Exflag = Exflag

    @property
    def SoldOut(self):
        r"""Specifies whether the item is sold-out. valid values: true (sold-out), false (not sold out).
        :rtype: str
        """
        return self._SoldOut

    @SoldOut.setter
    def SoldOut(self, SoldOut):
        self._SoldOut = SoldOut

    @property
    def SalesInfo(self):
        r"""Specifies the sell-out information of the standard version.
        :rtype: list of SaleInfo
        """
        return self._SalesInfo

    @SalesInfo.setter
    def SalesInfo(self, SalesInfo):
        self._SalesInfo = SalesInfo

    @property
    def ExtraFlag(self):
        r"""Additional flag.
        :rtype: str
        """
        return self._ExtraFlag

    @ExtraFlag.setter
    def ExtraFlag(self, ExtraFlag):
        self._ExtraFlag = ExtraFlag


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
        self._ExtraFlag = params.get("ExtraFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneResponse(AbstractModel):
    r"""The entity returned for the query of Kafka’s zone information

    """

    def __init__(self):
        r"""
        :param _ZoneList: <P>Specifies the zone list.</p>.
        :type ZoneList: list of ZoneInfo
        :param _MaxBuyInstanceNum: <P>Maximum number of instances that can be purchased.</p>.
        :type MaxBuyInstanceNum: int
        :param _MaxBandwidth: <p>Maximum purchase bandwidth in Mb/s.</p>.
        :type MaxBandwidth: int
        :param _UnitPrice: <P>Unit price for postpayment.</p>.
        :type UnitPrice: :class:`tencentcloud.ckafka.v20190819.models.Price`
        :param _MessagePrice: <P>Message unit price for postpayment.</p>.
        :type MessagePrice: :class:`tencentcloud.ckafka.v20190819.models.Price`
        :param _ClusterInfo: <P>User-Exclusive cluster information.</p>.
        :type ClusterInfo: list of ClusterInfo
        :param _Standard: <P>Specifies the standard version configuration to purchase.</p>.
        :type Standard: str
        :param _StandardS2: <P>Specifies the purchase of standard version s2 configuration.</p>.
        :type StandardS2: str
        :param _Profession: <P>Specifies the configuration for purchasing professional edition.</p>.
        :type Profession: str
        :param _Physical: <P>Purchase physical dedicated edition configuration.</p>.
        :type Physical: str
        :param _PublicNetwork: <p>Specifies the public network bandwidth. valid values: 3Mbps to 999Mbps. only supported in pro edition. abandoned, meaningless.</p>.
        :type PublicNetwork: str
        :param _PublicNetworkLimit: <P>Public network bandwidth configuration.</p>.
        :type PublicNetworkLimit: str
        :param _RequestId: <p>Request Id.</p>.
        :type RequestId: str
        :param _Offset: <P>Specifies the pagination offset.</p>.
        :type Offset: int
        :param _Limit: <P>Specifies the pagination limit.</p>.
        :type Limit: int
        :param _ForceCheckTag: <P>Specifies whether the tag is mandatory.</p>.
        :type ForceCheckTag: bool
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
        self._RequestId = None
        self._Offset = None
        self._Limit = None
        self._ForceCheckTag = None

    @property
    def ZoneList(self):
        r"""<P>Specifies the zone list.</p>.
        :rtype: list of ZoneInfo
        """
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

    @property
    def MaxBuyInstanceNum(self):
        r"""<P>Maximum number of instances that can be purchased.</p>.
        :rtype: int
        """
        return self._MaxBuyInstanceNum

    @MaxBuyInstanceNum.setter
    def MaxBuyInstanceNum(self, MaxBuyInstanceNum):
        self._MaxBuyInstanceNum = MaxBuyInstanceNum

    @property
    def MaxBandwidth(self):
        r"""<p>Maximum purchase bandwidth in Mb/s.</p>.
        :rtype: int
        """
        return self._MaxBandwidth

    @MaxBandwidth.setter
    def MaxBandwidth(self, MaxBandwidth):
        self._MaxBandwidth = MaxBandwidth

    @property
    def UnitPrice(self):
        r"""<P>Unit price for postpayment.</p>.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.Price`
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def MessagePrice(self):
        r"""<P>Message unit price for postpayment.</p>.
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.Price`
        """
        return self._MessagePrice

    @MessagePrice.setter
    def MessagePrice(self, MessagePrice):
        self._MessagePrice = MessagePrice

    @property
    def ClusterInfo(self):
        r"""<P>User-Exclusive cluster information.</p>.
        :rtype: list of ClusterInfo
        """
        return self._ClusterInfo

    @ClusterInfo.setter
    def ClusterInfo(self, ClusterInfo):
        self._ClusterInfo = ClusterInfo

    @property
    def Standard(self):
        r"""<P>Specifies the standard version configuration to purchase.</p>.
        :rtype: str
        """
        return self._Standard

    @Standard.setter
    def Standard(self, Standard):
        self._Standard = Standard

    @property
    def StandardS2(self):
        r"""<P>Specifies the purchase of standard version s2 configuration.</p>.
        :rtype: str
        """
        return self._StandardS2

    @StandardS2.setter
    def StandardS2(self, StandardS2):
        self._StandardS2 = StandardS2

    @property
    def Profession(self):
        r"""<P>Specifies the configuration for purchasing professional edition.</p>.
        :rtype: str
        """
        return self._Profession

    @Profession.setter
    def Profession(self, Profession):
        self._Profession = Profession

    @property
    def Physical(self):
        r"""<P>Purchase physical dedicated edition configuration.</p>.
        :rtype: str
        """
        return self._Physical

    @Physical.setter
    def Physical(self, Physical):
        self._Physical = Physical

    @property
    def PublicNetwork(self):
        r"""<p>Specifies the public network bandwidth. valid values: 3Mbps to 999Mbps. only supported in pro edition. abandoned, meaningless.</p>.
        :rtype: str
        """
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def PublicNetworkLimit(self):
        r"""<P>Public network bandwidth configuration.</p>.
        :rtype: str
        """
        return self._PublicNetworkLimit

    @PublicNetworkLimit.setter
    def PublicNetworkLimit(self, PublicNetworkLimit):
        self._PublicNetworkLimit = PublicNetworkLimit

    @property
    def RequestId(self):
        r"""<p>Request Id.</p>.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def Offset(self):
        r"""<P>Specifies the pagination offset.</p>.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<P>Specifies the pagination limit.</p>.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ForceCheckTag(self):
        r"""<P>Specifies whether the tag is mandatory.</p>.
        :rtype: bool
        """
        return self._ForceCheckTag

    @ForceCheckTag.setter
    def ForceCheckTag(self, ForceCheckTag):
        self._ForceCheckTag = ForceCheckTag


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
        self._RequestId = params.get("RequestId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ForceCheckTag = params.get("ForceCheckTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        