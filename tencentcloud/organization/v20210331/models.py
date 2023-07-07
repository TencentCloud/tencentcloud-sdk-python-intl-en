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
        :param _ParentNodeId: Parent node ID, which can be obtained through the `DescribeOrganizationNodes` API.
        :type ParentNodeId: int
        :param _Name: Node name, which can contain up to 40 letters, digits, and symbols `+@&._[]-`.
        :type Name: str
        :param _Remark: Remarks.
        :type Remark: str
        """
        self._ParentNodeId = None
        self._Name = None
        self._Remark = None

    @property
    def ParentNodeId(self):
        return self._ParentNodeId

    @ParentNodeId.setter
    def ParentNodeId(self, ParentNodeId):
        self._ParentNodeId = ParentNodeId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ParentNodeId = params.get("ParentNodeId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddOrganizationNodeResponse(AbstractModel):
    """AddOrganizationNode response structure.

    """

    def __init__(self):
        r"""
        :param _NodeId: Node ID.
        :type NodeId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NodeId = None
        self._RequestId = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._RequestId = params.get("RequestId")


class BindOrganizationMemberAuthAccountRequest(AbstractModel):
    """BindOrganizationMemberAuthAccount request structure.

    """

    def __init__(self):
        r"""
        :param _MemberUin: Member UIN.
        :type MemberUin: int
        :param _PolicyId: Policy ID, which can be obtained through the `DescribeOrganizationMemberPolicies` API.
        :type PolicyId: int
        :param _OrgSubAccountUins: List of sub-account UINs of the organization admin, which can contain up to five UINs.
        :type OrgSubAccountUins: list of int
        """
        self._MemberUin = None
        self._PolicyId = None
        self._OrgSubAccountUins = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def OrgSubAccountUins(self):
        return self._OrgSubAccountUins

    @OrgSubAccountUins.setter
    def OrgSubAccountUins(self, OrgSubAccountUins):
        self._OrgSubAccountUins = OrgSubAccountUins


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._PolicyId = params.get("PolicyId")
        self._OrgSubAccountUins = params.get("OrgSubAccountUins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindOrganizationMemberAuthAccountResponse(AbstractModel):
    """BindOrganizationMemberAuthAccount response structure.

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


class CancelOrganizationMemberAuthAccountRequest(AbstractModel):
    """CancelOrganizationMemberAuthAccount request structure.

    """

    def __init__(self):
        r"""
        :param _MemberUin: Member UIN.
        :type MemberUin: int
        :param _PolicyId: Policy ID.
        :type PolicyId: int
        :param _OrgSubAccountUin: Organization sub-account UIN.
        :type OrgSubAccountUin: int
        """
        self._MemberUin = None
        self._PolicyId = None
        self._OrgSubAccountUin = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def OrgSubAccountUin(self):
        return self._OrgSubAccountUin

    @OrgSubAccountUin.setter
    def OrgSubAccountUin(self, OrgSubAccountUin):
        self._OrgSubAccountUin = OrgSubAccountUin


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._PolicyId = params.get("PolicyId")
        self._OrgSubAccountUin = params.get("OrgSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelOrganizationMemberAuthAccountResponse(AbstractModel):
    """CancelOrganizationMemberAuthAccount response structure.

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


class CreateOrganizationMemberPolicyRequest(AbstractModel):
    """CreateOrganizationMemberPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _MemberUin: Member UIN.
        :type MemberUin: int
        :param _PolicyName: Policy name, which can contain up to 128 letters, digits, and symbols `+=,.@_-`.
        :type PolicyName: str
        :param _IdentityId: Member access identity ID, which can be obtained through the `DescribeOrganizationMemberAuthIdentities` API.
        :type IdentityId: int
        :param _Description: Description.
        :type Description: str
        """
        self._MemberUin = None
        self._PolicyName = None
        self._IdentityId = None
        self._Description = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._PolicyName = params.get("PolicyName")
        self._IdentityId = params.get("IdentityId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationMemberPolicyResponse(AbstractModel):
    """CreateOrganizationMemberPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PolicyId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class CreateOrganizationMemberRequest(AbstractModel):
    """CreateOrganizationMember request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Member name, which can contain up to 25 letters, digits, and symbols `+@&._[]-:,`.
        :type Name: str
        :param _PolicyType: Relationship policy. Valid value: `Financial`.
        :type PolicyType: str
        :param _PermissionIds: List of member financial permission IDs. `7` indicates paying, which is the default value.
        :type PermissionIds: list of int non-negative
        :param _NodeId: ID of the node of the member's department, which can be obtained through the `DescribeOrganizationNodes` API.
        :type NodeId: int
        :param _AccountName: Account name, which can contain up to 25 letters, digits, and symbols `+@&._[]-:,`.
        :type AccountName: str
        :param _Remark: Remarks.
        :type Remark: str
        :param _RecordId: Member creation record ID, which is required during retry upon creation exception.
        :type RecordId: int
        :param _PayUin: Payer UIN, which is required during paying for a member.
        :type PayUin: str
        :param _IdentityRoleID: List of member access identity IDs, which can be obtained through the `ListOrganizationIdentity` API. `1` indicates supported, which is the default value.
        :type IdentityRoleID: list of int non-negative
        :param _AuthRelationId: Verified entity relationship ID, which is required during creating members for different entities.
        :type AuthRelationId: int
        """
        self._Name = None
        self._PolicyType = None
        self._PermissionIds = None
        self._NodeId = None
        self._AccountName = None
        self._Remark = None
        self._RecordId = None
        self._PayUin = None
        self._IdentityRoleID = None
        self._AuthRelationId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PermissionIds(self):
        return self._PermissionIds

    @PermissionIds.setter
    def PermissionIds(self, PermissionIds):
        self._PermissionIds = PermissionIds

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def PayUin(self):
        return self._PayUin

    @PayUin.setter
    def PayUin(self, PayUin):
        self._PayUin = PayUin

    @property
    def IdentityRoleID(self):
        return self._IdentityRoleID

    @IdentityRoleID.setter
    def IdentityRoleID(self, IdentityRoleID):
        self._IdentityRoleID = IdentityRoleID

    @property
    def AuthRelationId(self):
        return self._AuthRelationId

    @AuthRelationId.setter
    def AuthRelationId(self, AuthRelationId):
        self._AuthRelationId = AuthRelationId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._PolicyType = params.get("PolicyType")
        self._PermissionIds = params.get("PermissionIds")
        self._NodeId = params.get("NodeId")
        self._AccountName = params.get("AccountName")
        self._Remark = params.get("Remark")
        self._RecordId = params.get("RecordId")
        self._PayUin = params.get("PayUin")
        self._IdentityRoleID = params.get("IdentityRoleID")
        self._AuthRelationId = params.get("AuthRelationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationMemberResponse(AbstractModel):
    """CreateOrganizationMember response structure.

    """

    def __init__(self):
        r"""
        :param _Uin: Member UIN.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Uin: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Uin = None
        self._RequestId = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._RequestId = params.get("RequestId")


class DeleteOrganizationMembersRequest(AbstractModel):
    """DeleteOrganizationMembers request structure.

    """

    def __init__(self):
        r"""
        :param _MemberUin: List of UINs of the members to be deleted.
        :type MemberUin: list of int
        """
        self._MemberUin = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationMembersResponse(AbstractModel):
    """DeleteOrganizationMembers response structure.

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


class DeleteOrganizationNodesRequest(AbstractModel):
    """DeleteOrganizationNodes request structure.

    """

    def __init__(self):
        r"""
        :param _NodeId: List of node IDs.
        :type NodeId: list of int
        """
        self._NodeId = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationNodesResponse(AbstractModel):
    """DeleteOrganizationNodes response structure.

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


class DescribeOrganizationMemberAuthAccountsRequest(AbstractModel):
    """DescribeOrganizationMemberAuthAccounts request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset.
        :type Offset: int
        :param _Limit: Maximum number of returned results.
        :type Limit: int
        :param _MemberUin: Member UIN.
        :type MemberUin: int
        :param _PolicyId: Policy ID.
        :type PolicyId: int
        """
        self._Offset = None
        self._Limit = None
        self._MemberUin = None
        self._PolicyId = None

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

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MemberUin = params.get("MemberUin")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMemberAuthAccountsResponse(AbstractModel):
    """DescribeOrganizationMemberAuthAccounts response structure.

    """

    def __init__(self):
        r"""
        :param _Items: List
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of OrgMemberAuthAccount
        :param _Total: Total number
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._Total = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgMemberAuthAccount()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationMemberAuthIdentitiesRequest(AbstractModel):
    """DescribeOrganizationMemberAuthIdentities request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset, which is an integer multiple of the value of `Limit`. Default value: `0`.
        :type Offset: int
        :param _Limit: Limit, which defaults to `10`. Value range: 1-50.
        :type Limit: int
        :param _MemberUin: Organization member UIN.
        :type MemberUin: int
        """
        self._Offset = None
        self._Limit = None
        self._MemberUin = None

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

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMemberAuthIdentitiesResponse(AbstractModel):
    """DescribeOrganizationMemberAuthIdentities response structure.

    """

    def __init__(self):
        r"""
        :param _Items: List of authorizable identities
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of OrgMemberAuthIdentity
        :param _Total: Total number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._Total = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgMemberAuthIdentity()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationMemberPoliciesRequest(AbstractModel):
    """DescribeOrganizationMemberPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset.
        :type Offset: int
        :param _Limit: Maximum number of returned results. Maximum value: `50`.
        :type Limit: int
        :param _MemberUin: Member UIN.
        :type MemberUin: int
        :param _SearchKey: Search keyword, which can be the policy name or description.
        :type SearchKey: str
        """
        self._Offset = None
        self._Limit = None
        self._MemberUin = None
        self._SearchKey = None

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

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MemberUin = params.get("MemberUin")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMemberPoliciesResponse(AbstractModel):
    """DescribeOrganizationMemberPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _Items: List.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of OrgMemberPolicy
        :param _Total: Total number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._Total = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgMemberPolicy()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationMembersRequest(AbstractModel):
    """DescribeOrganizationMembers request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset, which is an integer multiple of the value of `Limit`. Default value: `0`.
        :type Offset: int
        :param _Limit: Limit, which defaults to `10`. Value range: 1-50.
        :type Limit: int
        :param _Lang: Valid values: `en` (Tencent Cloud International); `zh` (Tencent Cloud).
        :type Lang: str
        :param _SearchKey: Search by member name or ID.
        :type SearchKey: str
        :param _AuthName: Entity name.
        :type AuthName: str
        :param _Product: Abbreviation of the trusted service, which is required during querying the trusted service admin.
        :type Product: str
        """
        self._Offset = None
        self._Limit = None
        self._Lang = None
        self._SearchKey = None
        self._AuthName = None
        self._Product = None

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

    @property
    def Lang(self):
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def AuthName(self):
        return self._AuthName

    @AuthName.setter
    def AuthName(self, AuthName):
        self._AuthName = AuthName

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Lang = params.get("Lang")
        self._SearchKey = params.get("SearchKey")
        self._AuthName = params.get("AuthName")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMembersResponse(AbstractModel):
    """DescribeOrganizationMembers response structure.

    """

    def __init__(self):
        r"""
        :param _Items: Member list.
        :type Items: list of OrgMember
        :param _Total: Total number.
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._Total = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgMember()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationNodesRequest(AbstractModel):
    """DescribeOrganizationNodes request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Maximum number of returned results. Maximum value: `50`.
        :type Limit: int
        :param _Offset: Offset.
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

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
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationNodesResponse(AbstractModel):
    """DescribeOrganizationNodes response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _Items: List details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of OrgNode
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgNode()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrganizationRequest(AbstractModel):
    """DescribeOrganization request structure.

    """

    def __init__(self):
        r"""
        :param _Lang: Valid values: `en` (Tencent Cloud International); `zh` (Tencent Cloud).
        :type Lang: str
        :param _Product: Abbreviation of the trusted service, which is required during querying the trusted service admin.
        :type Product: str
        """
        self._Lang = None
        self._Product = None

    @property
    def Lang(self):
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Lang = params.get("Lang")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationResponse(AbstractModel):
    """DescribeOrganization response structure.

    """

    def __init__(self):
        r"""
        :param _OrgId: Organization ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgId: int
        :param _HostUin: Creator UIN.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HostUin: int
        :param _NickName: Creator name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NickName: str
        :param _OrgType: Organization type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgType: int
        :param _IsManager: Whether the member is the organization admin. Valid values: `true` (yes); `false` (no).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsManager: bool
        :param _OrgPolicyType: Policy type. Valid values: `Financial` (finance management).
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgPolicyType: str
        :param _OrgPolicyName: Policy name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgPolicyName: str
        :param _OrgPermission: List of member financial permissions.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgPermission: list of OrgPermission
        :param _RootNodeId: Organization root node ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RootNodeId: int
        :param _CreateTime: Organization creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _JoinTime: Member joining time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JoinTime: str
        :param _IsAllowQuit: Whether the member is allowed to leave. Valid values: `Allow`, `Denied`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsAllowQuit: str
        :param _PayUin: Payer UIN.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayUin: str
        :param _PayName: Payer name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayName: str
        :param _IsAssignManager: Whether the member is the trusted service admin. Valid values: `true` (yes); `false` (no).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsAssignManager: bool
        :param _IsAuthManager: Whether the member is the verified entity admin. Valid values: `true` (yes); `false` (no).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsAuthManager: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OrgId = None
        self._HostUin = None
        self._NickName = None
        self._OrgType = None
        self._IsManager = None
        self._OrgPolicyType = None
        self._OrgPolicyName = None
        self._OrgPermission = None
        self._RootNodeId = None
        self._CreateTime = None
        self._JoinTime = None
        self._IsAllowQuit = None
        self._PayUin = None
        self._PayName = None
        self._IsAssignManager = None
        self._IsAuthManager = None
        self._RequestId = None

    @property
    def OrgId(self):
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def HostUin(self):
        return self._HostUin

    @HostUin.setter
    def HostUin(self, HostUin):
        self._HostUin = HostUin

    @property
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def OrgType(self):
        return self._OrgType

    @OrgType.setter
    def OrgType(self, OrgType):
        self._OrgType = OrgType

    @property
    def IsManager(self):
        return self._IsManager

    @IsManager.setter
    def IsManager(self, IsManager):
        self._IsManager = IsManager

    @property
    def OrgPolicyType(self):
        return self._OrgPolicyType

    @OrgPolicyType.setter
    def OrgPolicyType(self, OrgPolicyType):
        self._OrgPolicyType = OrgPolicyType

    @property
    def OrgPolicyName(self):
        return self._OrgPolicyName

    @OrgPolicyName.setter
    def OrgPolicyName(self, OrgPolicyName):
        self._OrgPolicyName = OrgPolicyName

    @property
    def OrgPermission(self):
        return self._OrgPermission

    @OrgPermission.setter
    def OrgPermission(self, OrgPermission):
        self._OrgPermission = OrgPermission

    @property
    def RootNodeId(self):
        return self._RootNodeId

    @RootNodeId.setter
    def RootNodeId(self, RootNodeId):
        self._RootNodeId = RootNodeId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def JoinTime(self):
        return self._JoinTime

    @JoinTime.setter
    def JoinTime(self, JoinTime):
        self._JoinTime = JoinTime

    @property
    def IsAllowQuit(self):
        return self._IsAllowQuit

    @IsAllowQuit.setter
    def IsAllowQuit(self, IsAllowQuit):
        self._IsAllowQuit = IsAllowQuit

    @property
    def PayUin(self):
        return self._PayUin

    @PayUin.setter
    def PayUin(self, PayUin):
        self._PayUin = PayUin

    @property
    def PayName(self):
        return self._PayName

    @PayName.setter
    def PayName(self, PayName):
        self._PayName = PayName

    @property
    def IsAssignManager(self):
        return self._IsAssignManager

    @IsAssignManager.setter
    def IsAssignManager(self, IsAssignManager):
        self._IsAssignManager = IsAssignManager

    @property
    def IsAuthManager(self):
        return self._IsAuthManager

    @IsAuthManager.setter
    def IsAuthManager(self, IsAuthManager):
        self._IsAuthManager = IsAuthManager

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OrgId = params.get("OrgId")
        self._HostUin = params.get("HostUin")
        self._NickName = params.get("NickName")
        self._OrgType = params.get("OrgType")
        self._IsManager = params.get("IsManager")
        self._OrgPolicyType = params.get("OrgPolicyType")
        self._OrgPolicyName = params.get("OrgPolicyName")
        if params.get("OrgPermission") is not None:
            self._OrgPermission = []
            for item in params.get("OrgPermission"):
                obj = OrgPermission()
                obj._deserialize(item)
                self._OrgPermission.append(obj)
        self._RootNodeId = params.get("RootNodeId")
        self._CreateTime = params.get("CreateTime")
        self._JoinTime = params.get("JoinTime")
        self._IsAllowQuit = params.get("IsAllowQuit")
        self._PayUin = params.get("PayUin")
        self._PayName = params.get("PayName")
        self._IsAssignManager = params.get("IsAssignManager")
        self._IsAuthManager = params.get("IsAuthManager")
        self._RequestId = params.get("RequestId")


class IdentityPolicy(AbstractModel):
    """Organization identity policy

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: int
        :param _PolicyName: Policy name
        :type PolicyName: str
        """
        self._PolicyId = None
        self._PolicyName = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationIdentityRequest(AbstractModel):
    """ListOrganizationIdentity request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset.  It must be an integer multiple of the value of `Limit`.  Default value: `0`.
        :type Offset: int
        :param _Limit: The limit for the number of query results.  Value range:  1-50.  Default value:  `10`.
        :type Limit: int
        :param _SearchKey: Search by name.
        :type SearchKey: str
        :param _IdentityId: Search by identity ID.
        :type IdentityId: int
        :param _IdentityType: Identity type.  Valid values: `1` (Preset), `2` (Custom).
        :type IdentityType: int
        """
        self._Offset = None
        self._Limit = None
        self._SearchKey = None
        self._IdentityId = None
        self._IdentityType = None

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

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityType(self):
        return self._IdentityType

    @IdentityType.setter
    def IdentityType(self, IdentityType):
        self._IdentityType = IdentityType


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        self._IdentityId = params.get("IdentityId")
        self._IdentityType = params.get("IdentityType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationIdentityResponse(AbstractModel):
    """ListOrganizationIdentity response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _Items: Item details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of OrgIdentity
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgIdentity()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class MemberIdentity(AbstractModel):
    """Member management identity

    """

    def __init__(self):
        r"""
        :param _IdentityId: Identity ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityId: int
        :param _IdentityAliasName: Identity name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityAliasName: str
        """
        self._IdentityId = None
        self._IdentityAliasName = None

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityAliasName(self):
        return self._IdentityAliasName

    @IdentityAliasName.setter
    def IdentityAliasName(self, IdentityAliasName):
        self._IdentityAliasName = IdentityAliasName


    def _deserialize(self, params):
        self._IdentityId = params.get("IdentityId")
        self._IdentityAliasName = params.get("IdentityAliasName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoveOrganizationNodeMembersRequest(AbstractModel):
    """MoveOrganizationNodeMembers request structure.

    """

    def __init__(self):
        r"""
        :param _NodeId: Organization node ID.
        :type NodeId: int
        :param _MemberUin: Member UIN list.
        :type MemberUin: list of int
        """
        self._NodeId = None
        self._MemberUin = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoveOrganizationNodeMembersResponse(AbstractModel):
    """MoveOrganizationNodeMembers response structure.

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


class OrgIdentity(AbstractModel):
    """Organization identity

    """

    def __init__(self):
        r"""
        :param _IdentityId: Identity ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityId: int
        :param _IdentityAliasName: Identity name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityAliasName: str
        :param _Description: Description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _IdentityPolicy: Identity policy.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityPolicy: list of IdentityPolicy
        :param _IdentityType: Identity type. Valid values: `1` (preset); `2` (custom).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityType: int
        :param _UpdateTime: Update time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self._IdentityId = None
        self._IdentityAliasName = None
        self._Description = None
        self._IdentityPolicy = None
        self._IdentityType = None
        self._UpdateTime = None

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityAliasName(self):
        return self._IdentityAliasName

    @IdentityAliasName.setter
    def IdentityAliasName(self, IdentityAliasName):
        self._IdentityAliasName = IdentityAliasName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IdentityPolicy(self):
        return self._IdentityPolicy

    @IdentityPolicy.setter
    def IdentityPolicy(self, IdentityPolicy):
        self._IdentityPolicy = IdentityPolicy

    @property
    def IdentityType(self):
        return self._IdentityType

    @IdentityType.setter
    def IdentityType(self, IdentityType):
        self._IdentityType = IdentityType

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._IdentityId = params.get("IdentityId")
        self._IdentityAliasName = params.get("IdentityAliasName")
        self._Description = params.get("Description")
        if params.get("IdentityPolicy") is not None:
            self._IdentityPolicy = []
            for item in params.get("IdentityPolicy"):
                obj = IdentityPolicy()
                obj._deserialize(item)
                self._IdentityPolicy.append(obj)
        self._IdentityType = params.get("IdentityType")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMember(AbstractModel):
    """Organization member

    """

    def __init__(self):
        r"""
        :param _MemberUin: Member UIN
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemberUin: int
        :param _Name: Member name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _MemberType: Member type. Valid values: `Invite` (invited); `Create` (created).
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemberType: str
        :param _OrgPolicyType: Relationship policy type
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgPolicyType: str
        :param _OrgPolicyName: Relationship policy name
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgPolicyName: str
        :param _OrgPermission: Relationship policy permission
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgPermission: list of OrgPermission
        :param _NodeId: Node ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeId: int
        :param _NodeName: Node name
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeName: str
        :param _Remark: Remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _CreateTime: Creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Update time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _IsAllowQuit: Whether the member is allowed to leave. Valid values: `Allow`, `Denied`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsAllowQuit: str
        :param _PayUin: Payer UIN
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayUin: str
        :param _PayName: Payer name
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayName: str
        :param _OrgIdentity: Management identity
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgIdentity: list of MemberIdentity
        :param _BindStatus: Security information binding status. Valid values: `Unbound`, `Valid`, `Success`, `Failed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BindStatus: str
        :param _PermissionStatus: Member permission status. Valid values: `Confirmed`, `UnConfirmed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PermissionStatus: str
        """
        self._MemberUin = None
        self._Name = None
        self._MemberType = None
        self._OrgPolicyType = None
        self._OrgPolicyName = None
        self._OrgPermission = None
        self._NodeId = None
        self._NodeName = None
        self._Remark = None
        self._CreateTime = None
        self._UpdateTime = None
        self._IsAllowQuit = None
        self._PayUin = None
        self._PayName = None
        self._OrgIdentity = None
        self._BindStatus = None
        self._PermissionStatus = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MemberType(self):
        return self._MemberType

    @MemberType.setter
    def MemberType(self, MemberType):
        self._MemberType = MemberType

    @property
    def OrgPolicyType(self):
        return self._OrgPolicyType

    @OrgPolicyType.setter
    def OrgPolicyType(self, OrgPolicyType):
        self._OrgPolicyType = OrgPolicyType

    @property
    def OrgPolicyName(self):
        return self._OrgPolicyName

    @OrgPolicyName.setter
    def OrgPolicyName(self, OrgPolicyName):
        self._OrgPolicyName = OrgPolicyName

    @property
    def OrgPermission(self):
        return self._OrgPermission

    @OrgPermission.setter
    def OrgPermission(self, OrgPermission):
        self._OrgPermission = OrgPermission

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeName(self):
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def IsAllowQuit(self):
        return self._IsAllowQuit

    @IsAllowQuit.setter
    def IsAllowQuit(self, IsAllowQuit):
        self._IsAllowQuit = IsAllowQuit

    @property
    def PayUin(self):
        return self._PayUin

    @PayUin.setter
    def PayUin(self, PayUin):
        self._PayUin = PayUin

    @property
    def PayName(self):
        return self._PayName

    @PayName.setter
    def PayName(self, PayName):
        self._PayName = PayName

    @property
    def OrgIdentity(self):
        return self._OrgIdentity

    @OrgIdentity.setter
    def OrgIdentity(self, OrgIdentity):
        self._OrgIdentity = OrgIdentity

    @property
    def BindStatus(self):
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def PermissionStatus(self):
        return self._PermissionStatus

    @PermissionStatus.setter
    def PermissionStatus(self, PermissionStatus):
        self._PermissionStatus = PermissionStatus


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._Name = params.get("Name")
        self._MemberType = params.get("MemberType")
        self._OrgPolicyType = params.get("OrgPolicyType")
        self._OrgPolicyName = params.get("OrgPolicyName")
        if params.get("OrgPermission") is not None:
            self._OrgPermission = []
            for item in params.get("OrgPermission"):
                obj = OrgPermission()
                obj._deserialize(item)
                self._OrgPermission.append(obj)
        self._NodeId = params.get("NodeId")
        self._NodeName = params.get("NodeName")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._IsAllowQuit = params.get("IsAllowQuit")
        self._PayUin = params.get("PayUin")
        self._PayName = params.get("PayName")
        if params.get("OrgIdentity") is not None:
            self._OrgIdentity = []
            for item in params.get("OrgIdentity"):
                obj = MemberIdentity()
                obj._deserialize(item)
                self._OrgIdentity.append(obj)
        self._BindStatus = params.get("BindStatus")
        self._PermissionStatus = params.get("PermissionStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMemberAuthAccount(AbstractModel):
    """Authorization relationship between the member and sub-account

    """

    def __init__(self):
        r"""
        :param _OrgSubAccountUin: Organization sub-account UIN.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgSubAccountUin: int
        :param _PolicyId: Policy ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyId: int
        :param _PolicyName: Policy name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyName: str
        :param _IdentityId: Identity ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityId: int
        :param _IdentityRoleName: Identity role name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityRoleName: str
        :param _IdentityRoleAliasName: Identity role alias.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityRoleAliasName: str
        :param _CreateTime: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Update time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _OrgSubAccountName: Sub-account name
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgSubAccountName: str
        """
        self._OrgSubAccountUin = None
        self._PolicyId = None
        self._PolicyName = None
        self._IdentityId = None
        self._IdentityRoleName = None
        self._IdentityRoleAliasName = None
        self._CreateTime = None
        self._UpdateTime = None
        self._OrgSubAccountName = None

    @property
    def OrgSubAccountUin(self):
        return self._OrgSubAccountUin

    @OrgSubAccountUin.setter
    def OrgSubAccountUin(self, OrgSubAccountUin):
        self._OrgSubAccountUin = OrgSubAccountUin

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityRoleName(self):
        return self._IdentityRoleName

    @IdentityRoleName.setter
    def IdentityRoleName(self, IdentityRoleName):
        self._IdentityRoleName = IdentityRoleName

    @property
    def IdentityRoleAliasName(self):
        return self._IdentityRoleAliasName

    @IdentityRoleAliasName.setter
    def IdentityRoleAliasName(self, IdentityRoleAliasName):
        self._IdentityRoleAliasName = IdentityRoleAliasName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def OrgSubAccountName(self):
        return self._OrgSubAccountName

    @OrgSubAccountName.setter
    def OrgSubAccountName(self, OrgSubAccountName):
        self._OrgSubAccountName = OrgSubAccountName


    def _deserialize(self, params):
        self._OrgSubAccountUin = params.get("OrgSubAccountUin")
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._IdentityId = params.get("IdentityId")
        self._IdentityRoleName = params.get("IdentityRoleName")
        self._IdentityRoleAliasName = params.get("IdentityRoleAliasName")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._OrgSubAccountName = params.get("OrgSubAccountName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMemberAuthIdentity(AbstractModel):
    """Authorizable identity of the organization member

    """

    def __init__(self):
        r"""
        :param _IdentityId: Identity ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityId: int
        :param _IdentityRoleName: Role name of an identity
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityRoleName: str
        :param _IdentityRoleAliasName: Role alias of an identity
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityRoleAliasName: str
        :param _Description: Description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _CreateTime: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Update time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _IdentityType: Identity type (`1`: Preset; `2`: Custom)
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityType: int
        """
        self._IdentityId = None
        self._IdentityRoleName = None
        self._IdentityRoleAliasName = None
        self._Description = None
        self._CreateTime = None
        self._UpdateTime = None
        self._IdentityType = None

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityRoleName(self):
        return self._IdentityRoleName

    @IdentityRoleName.setter
    def IdentityRoleName(self, IdentityRoleName):
        self._IdentityRoleName = IdentityRoleName

    @property
    def IdentityRoleAliasName(self):
        return self._IdentityRoleAliasName

    @IdentityRoleAliasName.setter
    def IdentityRoleAliasName(self, IdentityRoleAliasName):
        self._IdentityRoleAliasName = IdentityRoleAliasName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def IdentityType(self):
        return self._IdentityType

    @IdentityType.setter
    def IdentityType(self, IdentityType):
        self._IdentityType = IdentityType


    def _deserialize(self, params):
        self._IdentityId = params.get("IdentityId")
        self._IdentityRoleName = params.get("IdentityRoleName")
        self._IdentityRoleAliasName = params.get("IdentityRoleAliasName")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._IdentityType = params.get("IdentityType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMemberPolicy(AbstractModel):
    """Authorized policy of the organization member

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyId: int
        :param _PolicyName: Policy name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyName: str
        :param _IdentityId: Identity ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityId: int
        :param _IdentityRoleName: Identity role name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityRoleName: str
        :param _IdentityRoleAliasName: Identity role alias.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityRoleAliasName: str
        :param _Description: Description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _CreateTime: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Update time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._IdentityId = None
        self._IdentityRoleName = None
        self._IdentityRoleAliasName = None
        self._Description = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityRoleName(self):
        return self._IdentityRoleName

    @IdentityRoleName.setter
    def IdentityRoleName(self, IdentityRoleName):
        self._IdentityRoleName = IdentityRoleName

    @property
    def IdentityRoleAliasName(self):
        return self._IdentityRoleAliasName

    @IdentityRoleAliasName.setter
    def IdentityRoleAliasName(self, IdentityRoleAliasName):
        self._IdentityRoleAliasName = IdentityRoleAliasName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._IdentityId = params.get("IdentityId")
        self._IdentityRoleName = params.get("IdentityRoleName")
        self._IdentityRoleAliasName = params.get("IdentityRoleAliasName")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgNode(AbstractModel):
    """Department

    """

    def __init__(self):
        r"""
        :param _NodeId: Organization node ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeId: int
        :param _Name: Name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _ParentNodeId: Parent node ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ParentNodeId: int
        :param _Remark: Remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _CreateTime: Creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Update time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self._NodeId = None
        self._Name = None
        self._ParentNodeId = None
        self._Remark = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParentNodeId(self):
        return self._ParentNodeId

    @ParentNodeId.setter
    def ParentNodeId(self, ParentNodeId):
        self._ParentNodeId = ParentNodeId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Name = params.get("Name")
        self._ParentNodeId = params.get("ParentNodeId")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgPermission(AbstractModel):
    """Relationship policy permission

    """

    def __init__(self):
        r"""
        :param _Id: Permission ID
        :type Id: int
        :param _Name: Permission name
        :type Name: str
        """
        self._Id = None
        self._Name = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationNodeRequest(AbstractModel):
    """UpdateOrganizationNode request structure.

    """

    def __init__(self):
        r"""
        :param _NodeId: Node ID.
        :type NodeId: int
        :param _Name: Node name, which can contain up to 40 letters, digits, and symbols `+@&._[]-`.
        :type Name: str
        :param _Remark: Remarks.
        :type Remark: str
        """
        self._NodeId = None
        self._Name = None
        self._Remark = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationNodeResponse(AbstractModel):
    """UpdateOrganizationNode response structure.

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