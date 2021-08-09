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
        """
        :param RegistryId: ID of the instance to be verified.\n        :type RegistryId: str\n        """
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
        """
        :param IsValidated: Verification result. true: valid, false: invalid\n        :type IsValidated: bool\n        :param RegionId: ID of the region where the instance is located.\n        :type RegionId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param RegistryId: Instance ID\n        :type RegistryId: str\n        :param NamespaceName: Namespace\n        :type NamespaceName: str\n        :param Rule: Rule\n        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ImmutableTagRule`\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateMultipleSecurityPolicyRequest(AbstractModel):
    """CreateMultipleSecurityPolicy request structure.

    """

    def __init__(self):
        """
        :param RegistryId: Instance ID\n        :type RegistryId: str\n        :param SecurityGroupPolicySet: Security group policy\n        :type SecurityGroupPolicySet: list of SecurityPolicy\n        """
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
        """
        :param RegistryId: Instance ID\n        :type RegistryId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class DeleteImmutableTagRulesRequest(AbstractModel):
    """DeleteImmutableTagRules request structure.

    """

    def __init__(self):
        """
        :param RegistryId: Instance ID\n        :type RegistryId: str\n        :param NamespaceName: Namespace\n        :type NamespaceName: str\n        :param RuleId: Rule ID\n        :type RuleId: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMultipleSecurityPolicyRequest(AbstractModel):
    """DeleteMultipleSecurityPolicy request structure.

    """

    def __init__(self):
        """
        :param RegistryId: Instance ID\n        :type RegistryId: str\n        :param SecurityGroupPolicySet: Security group policy\n        :type SecurityGroupPolicySet: list of SecurityPolicy\n        """
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
        """
        :param RegistryId: Instance ID\n        :type RegistryId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class DescribeImmutableTagRulesRequest(AbstractModel):
    """DescribeImmutableTagRules request structure.

    """

    def __init__(self):
        """
        :param RegistryId: Instance ID\n        :type RegistryId: str\n        """
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
        """
        :param Rules: Rule list
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type Rules: list of ImmutableTagRule\n        :param EmptyNs: Namespace with no rules created
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type EmptyNs: list of str\n        :param Total: Total rules\n        :type Total: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class ImmutableTagRule(AbstractModel):
    """Tag immutability rule

    """

    def __init__(self):
        """
        :param RepositoryPattern: Repository matching rule\n        :type RepositoryPattern: str\n        :param TagPattern: Tag matching rule\n        :type TagPattern: str\n        :param RepositoryDecoration: repoMatches or repoExcludes\n        :type RepositoryDecoration: str\n        :param TagDecoration: matches or excludes\n        :type TagDecoration: str\n        :param Disabled: Disabling rule\n        :type Disabled: bool\n        :param RuleId: Rule ID\n        :type RuleId: int\n        :param NsName: Namespace\n        :type NsName: str\n        """
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
        


class ModifyImmutableTagRulesRequest(AbstractModel):
    """ModifyImmutableTagRules request structure.

    """

    def __init__(self):
        """
        :param RegistryId: Instance ID\n        :type RegistryId: str\n        :param NamespaceName: Namespace\n        :type NamespaceName: str\n        :param RuleId: Rule ID\n        :type RuleId: int\n        :param Rule: Rule\n        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ImmutableTagRule`\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SecurityPolicy(AbstractModel):
    """Security policy

    """

    def __init__(self):
        """
        :param PolicyIndex: Policy index\n        :type PolicyIndex: int\n        :param Description: Remarks\n        :type Description: str\n        :param CidrBlock: The public network IP address of the access source\n        :type CidrBlock: str\n        :param PolicyVersion: The version of the security policy\n        :type PolicyVersion: str\n        """
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
        