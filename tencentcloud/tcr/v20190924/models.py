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


class CheckInstanceRequest(AbstractModel):
    """CheckInstance request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: ID of the instance to be verified.
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstanceResponse(AbstractModel):
    """CheckInstance response structure.

    """

    def __init__(self):
        r"""
        :param IsValidated: Verification result. true: valid, false: invalid
        :type IsValidated: bool
        :param RegionId: ID of the region where the instance is located.
        :type RegionId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IsValidated = None
        self.RegionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsValidated = params.get("IsValidated")
        self.RegionId = params.get("RegionId")
        self.RequestId = params.get("RequestId")


class CreateImmutableTagRulesRequest(AbstractModel):
    """CreateImmutableTagRules request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace
        :type NamespaceName: str
        :param Rule: Rule
        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ImmutableTagRule`
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.Rule = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        if params.get("Rule") is not None:
            self.Rule = ImmutableTagRule()
            self.Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImmutableTagRulesResponse(AbstractModel):
    """CreateImmutableTagRules response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateMultipleSecurityPolicyRequest(AbstractModel):
    """CreateMultipleSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param SecurityGroupPolicySet: Security group policy
        :type SecurityGroupPolicySet: list of SecurityPolicy
        """
        self.RegistryId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = []
            for item in params.get("SecurityGroupPolicySet"):
                obj = SecurityPolicy()
                obj._deserialize(item)
                self.SecurityGroupPolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMultipleSecurityPolicyResponse(AbstractModel):
    """CreateMultipleSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class CreateReplicationInstanceRequest(AbstractModel):
    """CreateReplicationInstance request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Master instance ID
        :type RegistryId: str
        :param ReplicationRegionId: Region ID of the replication instance
        :type ReplicationRegionId: int
        :param ReplicationRegionName: Region name of the replication instance
        :type ReplicationRegionName: str
        """
        self.RegistryId = None
        self.ReplicationRegionId = None
        self.ReplicationRegionName = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.ReplicationRegionId = params.get("ReplicationRegionId")
        self.ReplicationRegionName = params.get("ReplicationRegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReplicationInstanceResponse(AbstractModel):
    """CreateReplicationInstance response structure.

    """

    def __init__(self):
        r"""
        :param ReplicationRegistryId: Enterprise Registry Instance ID
        :type ReplicationRegistryId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ReplicationRegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReplicationRegistryId = params.get("ReplicationRegistryId")
        self.RequestId = params.get("RequestId")


class DeleteImmutableTagRulesRequest(AbstractModel):
    """DeleteImmutableTagRules request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace
        :type NamespaceName: str
        :param RuleId: Rule ID
        :type RuleId: int
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RuleId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImmutableTagRulesResponse(AbstractModel):
    """DeleteImmutableTagRules response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMultipleSecurityPolicyRequest(AbstractModel):
    """DeleteMultipleSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param SecurityGroupPolicySet: Security group policy
        :type SecurityGroupPolicySet: list of SecurityPolicy
        """
        self.RegistryId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = []
            for item in params.get("SecurityGroupPolicySet"):
                obj = SecurityPolicy()
                obj._deserialize(item)
                self.SecurityGroupPolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMultipleSecurityPolicyResponse(AbstractModel):
    """DeleteMultipleSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class DescribeImmutableTagRulesRequest(AbstractModel):
    """DescribeImmutableTagRules request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImmutableTagRulesResponse(AbstractModel):
    """DescribeImmutableTagRules response structure.

    """

    def __init__(self):
        r"""
        :param Rules: Rule list
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Rules: list of ImmutableTagRule
        :param EmptyNs: Namespace with no rules created
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type EmptyNs: list of str
        :param Total: Total rules
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Rules = None
        self.EmptyNs = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = ImmutableTagRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.EmptyNs = params.get("EmptyNs")
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeReplicationInstanceCreateTasksRequest(AbstractModel):
    """DescribeReplicationInstanceCreateTasks request structure.

    """

    def __init__(self):
        r"""
        :param ReplicationRegistryId: Replication instance ID
        :type ReplicationRegistryId: str
        :param ReplicationRegionId: Region ID of the replication instance
        :type ReplicationRegionId: int
        """
        self.ReplicationRegistryId = None
        self.ReplicationRegionId = None


    def _deserialize(self, params):
        self.ReplicationRegistryId = params.get("ReplicationRegistryId")
        self.ReplicationRegionId = params.get("ReplicationRegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationInstanceCreateTasksResponse(AbstractModel):
    """DescribeReplicationInstanceCreateTasks response structure.

    """

    def __init__(self):
        r"""
        :param TaskDetail: Task details
        :type TaskDetail: list of TaskDetail
        :param Status: Overall task status
        :type Status: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskDetail = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskDetail") is not None:
            self.TaskDetail = []
            for item in params.get("TaskDetail"):
                obj = TaskDetail()
                obj._deserialize(item)
                self.TaskDetail.append(obj)
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeReplicationInstanceSyncStatusRequest(AbstractModel):
    """DescribeReplicationInstanceSyncStatus request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Master instance ID
        :type RegistryId: str
        :param ReplicationRegistryId: Replication instance ID
        :type ReplicationRegistryId: str
        :param ReplicationRegionId: Region ID of the replication instance
        :type ReplicationRegionId: int
        :param ShowReplicationLog: Whether to show the synchronization log
        :type ShowReplicationLog: bool
        :param Offset: Page offset for log display. Default value: 0
        :type Offset: int
        :param Limit: Maximum number of output entries. Default value: 5, maximum value: 20.
        :type Limit: int
        """
        self.RegistryId = None
        self.ReplicationRegistryId = None
        self.ReplicationRegionId = None
        self.ShowReplicationLog = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.ReplicationRegistryId = params.get("ReplicationRegistryId")
        self.ReplicationRegionId = params.get("ReplicationRegionId")
        self.ShowReplicationLog = params.get("ShowReplicationLog")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationInstanceSyncStatusResponse(AbstractModel):
    """DescribeReplicationInstanceSyncStatus response structure.

    """

    def __init__(self):
        r"""
        :param ReplicationStatus: Synchronization status
        :type ReplicationStatus: str
        :param ReplicationTime: Synchronization completion time
        :type ReplicationTime: str
        :param ReplicationLog: Synchronization log
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ReplicationLog: :class:`tencentcloud.tcr.v20190924.models.ReplicationLog`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ReplicationStatus = None
        self.ReplicationTime = None
        self.ReplicationLog = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReplicationStatus = params.get("ReplicationStatus")
        self.ReplicationTime = params.get("ReplicationTime")
        if params.get("ReplicationLog") is not None:
            self.ReplicationLog = ReplicationLog()
            self.ReplicationLog._deserialize(params.get("ReplicationLog"))
        self.RequestId = params.get("RequestId")


class DescribeReplicationInstancesRequest(AbstractModel):
    """DescribeReplicationInstances request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param Offset: Offset. Default value: 0
        :type Offset: int
        :param Limit: Maximum number of output entries. Default value: 20, maximum value: 100.
        :type Limit: int
        """
        self.RegistryId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationInstancesResponse(AbstractModel):
    """DescribeReplicationInstances response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of instances
        :type TotalCount: int
        :param ReplicationRegistries: Replication instance list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ReplicationRegistries: list of ReplicationRegistry
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ReplicationRegistries = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ReplicationRegistries") is not None:
            self.ReplicationRegistries = []
            for item in params.get("ReplicationRegistries"):
                obj = ReplicationRegistry()
                obj._deserialize(item)
                self.ReplicationRegistries.append(obj)
        self.RequestId = params.get("RequestId")


class ImmutableTagRule(AbstractModel):
    """Tag immutability rule

    """

    def __init__(self):
        r"""
        :param RepositoryPattern: Repository matching rule
        :type RepositoryPattern: str
        :param TagPattern: Tag matching rule
        :type TagPattern: str
        :param RepositoryDecoration: repoMatches or repoExcludes
        :type RepositoryDecoration: str
        :param TagDecoration: matches or excludes
        :type TagDecoration: str
        :param Disabled: Disabling rule
        :type Disabled: bool
        :param RuleId: Rule ID
        :type RuleId: int
        :param NsName: Namespace
        :type NsName: str
        """
        self.RepositoryPattern = None
        self.TagPattern = None
        self.RepositoryDecoration = None
        self.TagDecoration = None
        self.Disabled = None
        self.RuleId = None
        self.NsName = None


    def _deserialize(self, params):
        self.RepositoryPattern = params.get("RepositoryPattern")
        self.TagPattern = params.get("TagPattern")
        self.RepositoryDecoration = params.get("RepositoryDecoration")
        self.TagDecoration = params.get("TagDecoration")
        self.Disabled = params.get("Disabled")
        self.RuleId = params.get("RuleId")
        self.NsName = params.get("NsName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageReplicationRequest(AbstractModel):
    """ManageReplication request structure.

    """

    def __init__(self):
        r"""
        :param SourceRegistryId: Source instance ID
        :type SourceRegistryId: str
        :param DestinationRegistryId: Destination instance ID
        :type DestinationRegistryId: str
        :param Rule: Synchronization rule
        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ReplicationRule`
        :param Description: Rule description
        :type Description: str
        :param DestinationRegionId: Region ID of the destination instance. For example, `1` represents Guangzhou
        :type DestinationRegionId: int
        :param PeerReplicationOption: Configuration of the synchronization rule
        :type PeerReplicationOption: :class:`tencentcloud.tcr.v20190924.models.PeerReplicationOption`
        """
        self.SourceRegistryId = None
        self.DestinationRegistryId = None
        self.Rule = None
        self.Description = None
        self.DestinationRegionId = None
        self.PeerReplicationOption = None


    def _deserialize(self, params):
        self.SourceRegistryId = params.get("SourceRegistryId")
        self.DestinationRegistryId = params.get("DestinationRegistryId")
        if params.get("Rule") is not None:
            self.Rule = ReplicationRule()
            self.Rule._deserialize(params.get("Rule"))
        self.Description = params.get("Description")
        self.DestinationRegionId = params.get("DestinationRegionId")
        if params.get("PeerReplicationOption") is not None:
            self.PeerReplicationOption = PeerReplicationOption()
            self.PeerReplicationOption._deserialize(params.get("PeerReplicationOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageReplicationResponse(AbstractModel):
    """ManageReplication response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImmutableTagRulesRequest(AbstractModel):
    """ModifyImmutableTagRules request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace
        :type NamespaceName: str
        :param RuleId: Rule ID
        :type RuleId: int
        :param Rule: Rule
        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ImmutableTagRule`
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RuleId = None
        self.Rule = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RuleId = params.get("RuleId")
        if params.get("Rule") is not None:
            self.Rule = ImmutableTagRule()
            self.Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImmutableTagRulesResponse(AbstractModel):
    """ModifyImmutableTagRules response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param RegistryType: Instance specification
        :type RegistryType: str
        """
        self.RegistryId = None
        self.RegistryType = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RegistryType = params.get("RegistryType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PeerReplicationOption(AbstractModel):
    """Parameters for cross-account synchronization

    """

    def __init__(self):
        r"""
        :param PeerRegistryUin: UIN of the destination instance
        :type PeerRegistryUin: str
        :param PeerRegistryToken: Permanent access Token for the destination instance
        :type PeerRegistryToken: str
        :param EnablePeerReplication: Whether to enable cross-account synchronization
        :type EnablePeerReplication: bool
        """
        self.PeerRegistryUin = None
        self.PeerRegistryToken = None
        self.EnablePeerReplication = None


    def _deserialize(self, params):
        self.PeerRegistryUin = params.get("PeerRegistryUin")
        self.PeerRegistryToken = params.get("PeerRegistryToken")
        self.EnablePeerReplication = params.get("EnablePeerReplication")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicationFilter(AbstractModel):
    """Synchronization rule filter

    """

    def __init__(self):
        r"""
        :param Type: Type (`name`, `tag` and `resource`)
        :type Type: str
        :param Value: It is left blank by default
        :type Value: str
        """
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicationLog(AbstractModel):
    """Synchronization log

    """

    def __init__(self):
        r"""
        :param ResourceType: Resource type
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ResourceType: str
        :param Source: Path of the source resource
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Source: str
        :param Destination: Path of the destination resource
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Destination: str
        :param Status: Synchronization status
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Status: str
        :param StartTime: Start time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StartTime: str
        :param EndTime: End time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type EndTime: str
        """
        self.ResourceType = None
        self.Source = None
        self.Destination = None
        self.Status = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.Source = params.get("Source")
        self.Destination = params.get("Destination")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicationRegistry(AbstractModel):
    """ID of Enterprise Registry replication instance

    """

    def __init__(self):
        r"""
        :param RegistryId: Master instance ID
        :type RegistryId: str
        :param ReplicationRegistryId: Replication instance ID
        :type ReplicationRegistryId: str
        :param ReplicationRegionId: Region ID of the replication instance
        :type ReplicationRegionId: int
        :param ReplicationRegionName: Region name of the replication instance
        :type ReplicationRegionName: str
        :param Status: Status of the replication instance
        :type Status: str
        :param CreatedAt: Creation time
        :type CreatedAt: str
        """
        self.RegistryId = None
        self.ReplicationRegistryId = None
        self.ReplicationRegionId = None
        self.ReplicationRegionName = None
        self.Status = None
        self.CreatedAt = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.ReplicationRegistryId = params.get("ReplicationRegistryId")
        self.ReplicationRegionId = params.get("ReplicationRegionId")
        self.ReplicationRegionName = params.get("ReplicationRegionName")
        self.Status = params.get("Status")
        self.CreatedAt = params.get("CreatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicationRule(AbstractModel):
    """Synchronization rule

    """

    def __init__(self):
        r"""
        :param Name: Name of synchronization rule
        :type Name: str
        :param DestNamespace: Destination namespace
        :type DestNamespace: str
        :param Override: Whether to override
        :type Override: bool
        :param Filters: Synchronization filters
        :type Filters: list of ReplicationFilter
        """
        self.Name = None
        self.DestNamespace = None
        self.Override = None
        self.Filters = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DestNamespace = params.get("DestNamespace")
        self.Override = params.get("Override")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = ReplicationFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicy(AbstractModel):
    """Security policy

    """

    def __init__(self):
        r"""
        :param PolicyIndex: Policy index
        :type PolicyIndex: int
        :param Description: Remarks
        :type Description: str
        :param CidrBlock: The public network IP address of the access source
        :type CidrBlock: str
        :param PolicyVersion: The version of the security policy
        :type PolicyVersion: str
        """
        self.PolicyIndex = None
        self.Description = None
        self.CidrBlock = None
        self.PolicyVersion = None


    def _deserialize(self, params):
        self.PolicyIndex = params.get("PolicyIndex")
        self.Description = params.get("Description")
        self.CidrBlock = params.get("CidrBlock")
        self.PolicyVersion = params.get("PolicyVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskDetail(AbstractModel):
    """Task details

    """

    def __init__(self):
        r"""
        :param TaskName: Task
        :type TaskName: str
        :param TaskUUID: Task UUID
        :type TaskUUID: str
        :param TaskStatus: Task status
        :type TaskStatus: str
        :param TaskMessage: Task details
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TaskMessage: str
        :param CreatedTime: Start time of the task
        :type CreatedTime: str
        :param FinishedTime: End time of the task
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FinishedTime: str
        """
        self.TaskName = None
        self.TaskUUID = None
        self.TaskStatus = None
        self.TaskMessage = None
        self.CreatedTime = None
        self.FinishedTime = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.TaskUUID = params.get("TaskUUID")
        self.TaskStatus = params.get("TaskStatus")
        self.TaskMessage = params.get("TaskMessage")
        self.CreatedTime = params.get("CreatedTime")
        self.FinishedTime = params.get("FinishedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        