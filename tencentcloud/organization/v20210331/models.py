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


class AddOrganizationNodeRequest(AbstractModel):
    """AddOrganizationNode request structure.

    """

    def __init__(self):
        r"""
        :param ParentNodeId: Parent node ID, which can be obtained through the `DescribeOrganizationNodes` API.
        :type ParentNodeId: int
        :param Name: Node name, which can contain up to 40 letters, digits, and symbols `+@&._[]-`.
        :type Name: str
        :param Remark: Remarks.
        :type Remark: str
        """
        self.ParentNodeId = None
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.ParentNodeId = params.get("ParentNodeId")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddOrganizationNodeResponse(AbstractModel):
    """AddOrganizationNode response structure.

    """

    def __init__(self):
        r"""
        :param NodeId: Node ID.
        :type NodeId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NodeId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.RequestId = params.get("RequestId")


class BindOrganizationMemberAuthAccountRequest(AbstractModel):
    """BindOrganizationMemberAuthAccount request structure.

    """

    def __init__(self):
        r"""
        :param MemberUin: Member UIN.
        :type MemberUin: int
        :param PolicyId: Policy ID, which can be obtained through the `DescribeOrganizationMemberPolicies` API.
        :type PolicyId: int
        :param OrgSubAccountUins: List of sub-account UINs of the organization admin, which can contain up to five UINs.
        :type OrgSubAccountUins: list of int
        """
        self.MemberUin = None
        self.PolicyId = None
        self.OrgSubAccountUins = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        self.PolicyId = params.get("PolicyId")
        self.OrgSubAccountUins = params.get("OrgSubAccountUins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindOrganizationMemberAuthAccountResponse(AbstractModel):
    """BindOrganizationMemberAuthAccount response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CancelOrganizationMemberAuthAccountRequest(AbstractModel):
    """CancelOrganizationMemberAuthAccount request structure.

    """

    def __init__(self):
        r"""
        :param MemberUin: Member UIN.
        :type MemberUin: int
        :param PolicyId: Policy ID.
        :type PolicyId: int
        :param OrgSubAccountUin: Organization sub-account UIN.
        :type OrgSubAccountUin: int
        """
        self.MemberUin = None
        self.PolicyId = None
        self.OrgSubAccountUin = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        self.PolicyId = params.get("PolicyId")
        self.OrgSubAccountUin = params.get("OrgSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelOrganizationMemberAuthAccountResponse(AbstractModel):
    """CancelOrganizationMemberAuthAccount response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateOrganizationMemberPolicyRequest(AbstractModel):
    """CreateOrganizationMemberPolicy request structure.

    """

    def __init__(self):
        r"""
        :param MemberUin: Member UIN.
        :type MemberUin: int
        :param PolicyName: Policy name, which can contain up to 128 letters, digits, and symbols `+=,.@_-`.
        :type PolicyName: str
        :param IdentityId: Member access identity ID, which can be obtained through the `DescribeOrganizationMemberAuthIdentities` API.
        :type IdentityId: int
        :param Description: Description.
        :type Description: str
        """
        self.MemberUin = None
        self.PolicyName = None
        self.IdentityId = None
        self.Description = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        self.PolicyName = params.get("PolicyName")
        self.IdentityId = params.get("IdentityId")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationMemberPolicyResponse(AbstractModel):
    """CreateOrganizationMemberPolicy response structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class CreateOrganizationMemberRequest(AbstractModel):
    """CreateOrganizationMember request structure.

    """

    def __init__(self):
        r"""
        :param Name: Member name, which can contain up to 25 letters, digits, and symbols `+@&._[]-:,`.
        :type Name: str
        :param PolicyType: Relationship policy. Valid value: `Financial`.
        :type PolicyType: str
        :param PermissionIds: List of member financial permission IDs. `7` indicates paying, which is the default value.
        :type PermissionIds: list of int non-negative
        :param NodeId: ID of the node of the member's department, which can be obtained through the `DescribeOrganizationNodes` API.
        :type NodeId: int
        :param AccountName: Account name, which can contain up to 25 letters, digits, and symbols `+@&._[]-:,`.
        :type AccountName: str
        :param Remark: Remarks.
        :type Remark: str
        :param RecordId: Member creation record ID, which is required during retry upon creation exception.
        :type RecordId: int
        :param PayUin: Payer UIN, which is required during paying for a member.
        :type PayUin: str
        :param IdentityRoleID: List of member access identity IDs, which can be obtained through the `ListOrganizationIdentity` API. `1` indicates supported, which is the default value.
        :type IdentityRoleID: list of int non-negative
        :param AuthRelationId: Verified entity relationship ID, which is required during creating members for different entities.
        :type AuthRelationId: int
        """
        self.Name = None
        self.PolicyType = None
        self.PermissionIds = None
        self.NodeId = None
        self.AccountName = None
        self.Remark = None
        self.RecordId = None
        self.PayUin = None
        self.IdentityRoleID = None
        self.AuthRelationId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.PolicyType = params.get("PolicyType")
        self.PermissionIds = params.get("PermissionIds")
        self.NodeId = params.get("NodeId")
        self.AccountName = params.get("AccountName")
        self.Remark = params.get("Remark")
        self.RecordId = params.get("RecordId")
        self.PayUin = params.get("PayUin")
        self.IdentityRoleID = params.get("IdentityRoleID")
        self.AuthRelationId = params.get("AuthRelationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationMemberResponse(AbstractModel):
    """CreateOrganizationMember response structure.

    """

    def __init__(self):
        r"""
        :param Uin: Member UIN.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Uin: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Uin = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.RequestId = params.get("RequestId")


class DeleteOrganizationMembersRequest(AbstractModel):
    """DeleteOrganizationMembers request structure.

    """

    def __init__(self):
        r"""
        :param MemberUin: List of UINs of the members to be deleted.
        :type MemberUin: list of int
        """
        self.MemberUin = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationMembersResponse(AbstractModel):
    """DeleteOrganizationMembers response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteOrganizationNodesRequest(AbstractModel):
    """DeleteOrganizationNodes request structure.

    """

    def __init__(self):
        r"""
        :param NodeId: List of node IDs.
        :type NodeId: list of int
        """
        self.NodeId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationNodesResponse(AbstractModel):
    """DeleteOrganizationNodes response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeOrganizationMemberAuthAccountsRequest(AbstractModel):
    """DescribeOrganizationMemberAuthAccounts request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset.
        :type Offset: int
        :param Limit: Maximum number of returned results.
        :type Limit: int
        :param MemberUin: Member UIN.
        :type MemberUin: int
        :param PolicyId: Policy ID.
        :type PolicyId: int
        """
        self.Offset = None
        self.Limit = None
        self.MemberUin = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.MemberUin = params.get("MemberUin")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMemberAuthAccountsResponse(AbstractModel):
    """DescribeOrganizationMemberAuthAccounts response structure.

    """

    def __init__(self):
        r"""
        :param Items: List
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of OrgMemberAuthAccount
        :param Total: Total number
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Items = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = OrgMemberAuthAccount()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeOrganizationMemberAuthIdentitiesRequest(AbstractModel):
    """DescribeOrganizationMemberAuthIdentities request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset.
        :type Offset: int
        :param Limit: Maximum number of returned results. Maximum value: `50`.
        :type Limit: int
        :param MemberUin: Organization member UIN.
        :type MemberUin: int
        """
        self.Offset = None
        self.Limit = None
        self.MemberUin = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMemberAuthIdentitiesResponse(AbstractModel):
    """DescribeOrganizationMemberAuthIdentities response structure.

    """

    def __init__(self):
        r"""
        :param Items: List.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of OrgMemberAuthIdentity
        :param Total: Total number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Items = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = OrgMemberAuthIdentity()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeOrganizationMemberPoliciesRequest(AbstractModel):
    """DescribeOrganizationMemberPolicies request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset.
        :type Offset: int
        :param Limit: Maximum number of returned results. Maximum value: `50`.
        :type Limit: int
        :param MemberUin: Member UIN.
        :type MemberUin: int
        :param SearchKey: Search keyword, which can be the policy name or description.
        :type SearchKey: str
        """
        self.Offset = None
        self.Limit = None
        self.MemberUin = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.MemberUin = params.get("MemberUin")
        self.SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMemberPoliciesResponse(AbstractModel):
    """DescribeOrganizationMemberPolicies response structure.

    """

    def __init__(self):
        r"""
        :param Items: List.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of OrgMemberPolicy
        :param Total: Total number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Items = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = OrgMemberPolicy()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeOrganizationMembersRequest(AbstractModel):
    """DescribeOrganizationMembers request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset.
        :type Offset: int
        :param Limit: Maximum number of returned results. Maximum value: `50`.
        :type Limit: int
        :param Lang: Valid values: `en` (Tencent Cloud International); `zh` (Tencent Cloud).
        :type Lang: str
        :param SearchKey: Search by member name or ID.
        :type SearchKey: str
        :param AuthName: Entity name.
        :type AuthName: str
        :param Product: Abbreviation of the trusted service, which is required during querying the trusted service admin.
        :type Product: str
        """
        self.Offset = None
        self.Limit = None
        self.Lang = None
        self.SearchKey = None
        self.AuthName = None
        self.Product = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Lang = params.get("Lang")
        self.SearchKey = params.get("SearchKey")
        self.AuthName = params.get("AuthName")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMembersResponse(AbstractModel):
    """DescribeOrganizationMembers response structure.

    """

    def __init__(self):
        r"""
        :param Items: Member list.
        :type Items: list of OrgMember
        :param Total: Total number.
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Items = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = OrgMember()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeOrganizationNodesRequest(AbstractModel):
    """DescribeOrganizationNodes request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Maximum number of returned results. Maximum value: `50`.
        :type Limit: int
        :param Offset: Offset.
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationNodesResponse(AbstractModel):
    """DescribeOrganizationNodes response structure.

    """

    def __init__(self):
        r"""
        :param Total: Total number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param Items: List details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of OrgNode
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = OrgNode()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOrganizationRequest(AbstractModel):
    """DescribeOrganization request structure.

    """

    def __init__(self):
        r"""
        :param Lang: Valid values: `en` (Tencent Cloud International); `zh` (Tencent Cloud).
        :type Lang: str
        :param Product: Abbreviation of the trusted service, which is required during querying the trusted service admin.
        :type Product: str
        """
        self.Lang = None
        self.Product = None


    def _deserialize(self, params):
        self.Lang = params.get("Lang")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationResponse(AbstractModel):
    """DescribeOrganization response structure.

    """

    def __init__(self):
        r"""
        :param OrgId: Organization ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgId: int
        :param HostUin: Creator UIN.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HostUin: int
        :param NickName: Creator name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NickName: str
        :param OrgType: Organization type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgType: int
        :param IsManager: Whether the member is the organization admin. Valid values: `true` (yes); `false` (no).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsManager: bool
        :param OrgPolicyType: Policy type. Valid values: `Financial` (finance management).
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgPolicyType: str
        :param OrgPolicyName: Policy name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgPolicyName: str
        :param OrgPermission: List of member financial permissions.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgPermission: list of OrgPermission
        :param RootNodeId: Organization root node ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RootNodeId: int
        :param CreateTime: Organization creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param JoinTime: Member joining time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JoinTime: str
        :param IsAllowQuit: Whether the member is allowed to leave. Valid values: `Allow`, `Denied`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsAllowQuit: str
        :param PayUin: Payer UIN.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayUin: str
        :param PayName: Payer name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayName: str
        :param IsAssignManager: Whether the member is the trusted service admin. Valid values: `true` (yes); `false` (no).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsAssignManager: bool
        :param IsAuthManager: Whether the member is the verified entity admin. Valid values: `true` (yes); `false` (no).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsAuthManager: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OrgId = None
        self.HostUin = None
        self.NickName = None
        self.OrgType = None
        self.IsManager = None
        self.OrgPolicyType = None
        self.OrgPolicyName = None
        self.OrgPermission = None
        self.RootNodeId = None
        self.CreateTime = None
        self.JoinTime = None
        self.IsAllowQuit = None
        self.PayUin = None
        self.PayName = None
        self.IsAssignManager = None
        self.IsAuthManager = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrgId = params.get("OrgId")
        self.HostUin = params.get("HostUin")
        self.NickName = params.get("NickName")
        self.OrgType = params.get("OrgType")
        self.IsManager = params.get("IsManager")
        self.OrgPolicyType = params.get("OrgPolicyType")
        self.OrgPolicyName = params.get("OrgPolicyName")
        if params.get("OrgPermission") is not None:
            self.OrgPermission = []
            for item in params.get("OrgPermission"):
                obj = OrgPermission()
                obj._deserialize(item)
                self.OrgPermission.append(obj)
        self.RootNodeId = params.get("RootNodeId")
        self.CreateTime = params.get("CreateTime")
        self.JoinTime = params.get("JoinTime")
        self.IsAllowQuit = params.get("IsAllowQuit")
        self.PayUin = params.get("PayUin")
        self.PayName = params.get("PayName")
        self.IsAssignManager = params.get("IsAssignManager")
        self.IsAuthManager = params.get("IsAuthManager")
        self.RequestId = params.get("RequestId")


class IdentityPolicy(AbstractModel):
    """Organization identity policy

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID
        :type PolicyId: int
        :param PolicyName: Policy name
        :type PolicyName: str
        """
        self.PolicyId = None
        self.PolicyName = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationIdentityRequest(AbstractModel):
    """ListOrganizationIdentity request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset.
        :type Offset: int
        :param Limit: Maximum number of returned results. Maximum value: `50`.
        :type Limit: int
        :param SearchKey: Search by name.
        :type SearchKey: str
        :param IdentityId: Search by identity ID.
        :type IdentityId: int
        """
        self.Offset = None
        self.Limit = None
        self.SearchKey = None
        self.IdentityId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        self.IdentityId = params.get("IdentityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationIdentityResponse(AbstractModel):
    """ListOrganizationIdentity response structure.

    """

    def __init__(self):
        r"""
        :param Total: Total number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param Items: Item details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of OrgIdentity
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = OrgIdentity()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class MemberIdentity(AbstractModel):
    """Member management identity

    """

    def __init__(self):
        r"""
        :param IdentityId: Identity ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityId: int
        :param IdentityAliasName: Identity name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityAliasName: str
        """
        self.IdentityId = None
        self.IdentityAliasName = None


    def _deserialize(self, params):
        self.IdentityId = params.get("IdentityId")
        self.IdentityAliasName = params.get("IdentityAliasName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoveOrganizationNodeMembersRequest(AbstractModel):
    """MoveOrganizationNodeMembers request structure.

    """

    def __init__(self):
        r"""
        :param NodeId: Organization node ID.
        :type NodeId: int
        :param MemberUin: Member UIN list.
        :type MemberUin: list of int
        """
        self.NodeId = None
        self.MemberUin = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoveOrganizationNodeMembersResponse(AbstractModel):
    """MoveOrganizationNodeMembers response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OrgIdentity(AbstractModel):
    """Organization identity

    """

    def __init__(self):
        r"""
        :param IdentityId: Identity ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityId: int
        :param IdentityAliasName: Identity name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityAliasName: str
        :param Description: Description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param IdentityPolicy: Identity policy.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityPolicy: list of IdentityPolicy
        :param IdentityType: Identity type. Valid values: `1` (preset); `2` (custom).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityType: int
        :param UpdateTime: Update time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self.IdentityId = None
        self.IdentityAliasName = None
        self.Description = None
        self.IdentityPolicy = None
        self.IdentityType = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.IdentityId = params.get("IdentityId")
        self.IdentityAliasName = params.get("IdentityAliasName")
        self.Description = params.get("Description")
        if params.get("IdentityPolicy") is not None:
            self.IdentityPolicy = []
            for item in params.get("IdentityPolicy"):
                obj = IdentityPolicy()
                obj._deserialize(item)
                self.IdentityPolicy.append(obj)
        self.IdentityType = params.get("IdentityType")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMember(AbstractModel):
    """Organization member

    """

    def __init__(self):
        r"""
        :param MemberUin: Member UIN
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemberUin: int
        :param Name: Member name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param MemberType: Member type. Valid values: `Invite` (invited); `Create` (created).
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemberType: str
        :param OrgPolicyType: Relationship policy type
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgPolicyType: str
        :param OrgPolicyName: Relationship policy name
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgPolicyName: str
        :param OrgPermission: Relationship policy permission
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgPermission: list of OrgPermission
        :param NodeId: Node ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeId: int
        :param NodeName: Node name
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeName: str
        :param Remark: Remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param CreateTime: Creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param UpdateTime: Update time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param IsAllowQuit: Whether the member is allowed to leave. Valid values: `Allow`, `Denied`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsAllowQuit: str
        :param PayUin: Payer UIN
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayUin: str
        :param PayName: Payer name
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayName: str
        :param OrgIdentity: Management identity
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgIdentity: list of MemberIdentity
        :param BindStatus: Security information binding status. Valid values: `Unbound`, `Valid`, `Success`, `Failed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BindStatus: str
        :param PermissionStatus: Member permission status. Valid values: `Confirmed`, `UnConfirmed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PermissionStatus: str
        """
        self.MemberUin = None
        self.Name = None
        self.MemberType = None
        self.OrgPolicyType = None
        self.OrgPolicyName = None
        self.OrgPermission = None
        self.NodeId = None
        self.NodeName = None
        self.Remark = None
        self.CreateTime = None
        self.UpdateTime = None
        self.IsAllowQuit = None
        self.PayUin = None
        self.PayName = None
        self.OrgIdentity = None
        self.BindStatus = None
        self.PermissionStatus = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        self.Name = params.get("Name")
        self.MemberType = params.get("MemberType")
        self.OrgPolicyType = params.get("OrgPolicyType")
        self.OrgPolicyName = params.get("OrgPolicyName")
        if params.get("OrgPermission") is not None:
            self.OrgPermission = []
            for item in params.get("OrgPermission"):
                obj = OrgPermission()
                obj._deserialize(item)
                self.OrgPermission.append(obj)
        self.NodeId = params.get("NodeId")
        self.NodeName = params.get("NodeName")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.IsAllowQuit = params.get("IsAllowQuit")
        self.PayUin = params.get("PayUin")
        self.PayName = params.get("PayName")
        if params.get("OrgIdentity") is not None:
            self.OrgIdentity = []
            for item in params.get("OrgIdentity"):
                obj = MemberIdentity()
                obj._deserialize(item)
                self.OrgIdentity.append(obj)
        self.BindStatus = params.get("BindStatus")
        self.PermissionStatus = params.get("PermissionStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMemberAuthAccount(AbstractModel):
    """Authorization relationship between the member and sub-account

    """

    def __init__(self):
        r"""
        :param OrgSubAccountUin: Organization sub-account UIN.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgSubAccountUin: int
        :param PolicyId: Policy ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyId: int
        :param PolicyName: Policy name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyName: str
        :param IdentityId: Identity ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityId: int
        :param IdentityRoleName: Identity role name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityRoleName: str
        :param IdentityRoleAliasName: Identity role alias.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityRoleAliasName: str
        :param CreateTime: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param UpdateTime: Update time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param OrgSubAccountName: Sub-account name
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgSubAccountName: str
        """
        self.OrgSubAccountUin = None
        self.PolicyId = None
        self.PolicyName = None
        self.IdentityId = None
        self.IdentityRoleName = None
        self.IdentityRoleAliasName = None
        self.CreateTime = None
        self.UpdateTime = None
        self.OrgSubAccountName = None


    def _deserialize(self, params):
        self.OrgSubAccountUin = params.get("OrgSubAccountUin")
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.IdentityId = params.get("IdentityId")
        self.IdentityRoleName = params.get("IdentityRoleName")
        self.IdentityRoleAliasName = params.get("IdentityRoleAliasName")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.OrgSubAccountName = params.get("OrgSubAccountName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMemberAuthIdentity(AbstractModel):
    """Authorizable identity of the organization member

    """

    def __init__(self):
        r"""
        :param IdentityId: Identity ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityId: int
        :param IdentityRoleName: Identity role name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityRoleName: str
        :param IdentityRoleAliasName: Identity role alias.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityRoleAliasName: str
        :param Description: Description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param CreateTime: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param UpdateTime: Update time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self.IdentityId = None
        self.IdentityRoleName = None
        self.IdentityRoleAliasName = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.IdentityId = params.get("IdentityId")
        self.IdentityRoleName = params.get("IdentityRoleName")
        self.IdentityRoleAliasName = params.get("IdentityRoleAliasName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMemberPolicy(AbstractModel):
    """Authorized policy of the organization member

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyId: int
        :param PolicyName: Policy name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyName: str
        :param IdentityId: Identity ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityId: int
        :param IdentityRoleName: Identity role name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityRoleName: str
        :param IdentityRoleAliasName: Identity role alias.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityRoleAliasName: str
        :param Description: Description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param CreateTime: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param UpdateTime: Update time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.IdentityId = None
        self.IdentityRoleName = None
        self.IdentityRoleAliasName = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.IdentityId = params.get("IdentityId")
        self.IdentityRoleName = params.get("IdentityRoleName")
        self.IdentityRoleAliasName = params.get("IdentityRoleAliasName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgNode(AbstractModel):
    """Department

    """

    def __init__(self):
        r"""
        :param NodeId: Organization node ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeId: int
        :param Name: Name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param ParentNodeId: Parent node ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ParentNodeId: int
        :param Remark: Remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param CreateTime: Creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param UpdateTime: Update time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self.NodeId = None
        self.Name = None
        self.ParentNodeId = None
        self.Remark = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Name = params.get("Name")
        self.ParentNodeId = params.get("ParentNodeId")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgPermission(AbstractModel):
    """Relationship policy permission

    """

    def __init__(self):
        r"""
        :param Id: Permission ID
        :type Id: int
        :param Name: Permission name
        :type Name: str
        """
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationNodeRequest(AbstractModel):
    """UpdateOrganizationNode request structure.

    """

    def __init__(self):
        r"""
        :param NodeId: Node ID.
        :type NodeId: int
        :param Name: Node name, which can contain up to 40 letters, digits, and symbols `+@&._[]-`.
        :type Name: str
        :param Remark: Remarks.
        :type Remark: str
        """
        self.NodeId = None
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationNodeResponse(AbstractModel):
    """UpdateOrganizationNode response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")