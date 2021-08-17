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


class AcceptOrganizationInvitationRequest(AbstractModel):
    """AcceptOrganizationInvitation request structure.

    """

    def __init__(self):
        r"""
        :param Id: Invitation ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcceptOrganizationInvitationResponse(AbstractModel):
    """AcceptOrganizationInvitation response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddOrganizationNodeRequest(AbstractModel):
    """AddOrganizationNode request structure.

    """

    def __init__(self):
        r"""
        :param ParentNodeId: Parent organizational unit ID
        :type ParentNodeId: int
        :param Name: Organizational unit name
        :type Name: str
        """
        self.ParentNodeId = None
        self.Name = None


    def _deserialize(self, params):
        self.ParentNodeId = params.get("ParentNodeId")
        self.Name = params.get("Name")
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
        :param NodeId: Organizational unit ID
        :type NodeId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NodeId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.RequestId = params.get("RequestId")


class CancelOrganizationInvitationRequest(AbstractModel):
    """CancelOrganizationInvitation request structure.

    """

    def __init__(self):
        r"""
        :param Id: Invitation ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelOrganizationInvitationResponse(AbstractModel):
    """CancelOrganizationInvitation response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateOrganizationRequest(AbstractModel):
    """CreateOrganization request structure.

    """

    def __init__(self):
        r"""
        :param OrgType: Organization type; currently its value is fixed as `1`
        :type OrgType: int
        """
        self.OrgType = None


    def _deserialize(self, params):
        self.OrgType = params.get("OrgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationResponse(AbstractModel):
    """CreateOrganization response structure.

    """

    def __init__(self):
        r"""
        :param OrgId: Organization ID
        :type OrgId: int
        :param Nickname: Creator's name
        :type Nickname: str
        :param Mail: Creator's email address
        :type Mail: str
        :param OrgType: Organization type
        :type OrgType: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OrgId = None
        self.Nickname = None
        self.Mail = None
        self.OrgType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrgId = params.get("OrgId")
        self.Nickname = params.get("Nickname")
        self.Mail = params.get("Mail")
        self.OrgType = params.get("OrgType")
        self.RequestId = params.get("RequestId")


class DeleteOrganizationMemberFromNodeRequest(AbstractModel):
    """DeleteOrganizationMemberFromNode request structure.

    """

    def __init__(self):
        r"""
        :param MemberUin: UIN of the member to be deleted
        :type MemberUin: int
        :param NodeId: Organizational unit ID
        :type NodeId: int
        """
        self.MemberUin = None
        self.NodeId = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        self.NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationMemberFromNodeResponse(AbstractModel):
    """DeleteOrganizationMemberFromNode response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteOrganizationMembersRequest(AbstractModel):
    """DeleteOrganizationMembers request structure.

    """

    def __init__(self):
        r"""
        :param Uins: List of UINs of members to be deleted
        :type Uins: list of int non-negative
        """
        self.Uins = None


    def _deserialize(self, params):
        self.Uins = params.get("Uins")
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
        :param NodeIds: Organizational unit ID list
        :type NodeIds: list of int non-negative
        """
        self.NodeIds = None


    def _deserialize(self, params):
        self.NodeIds = params.get("NodeIds")
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


class DeleteOrganizationRequest(AbstractModel):
    """DeleteOrganization request structure.

    """


class DeleteOrganizationResponse(AbstractModel):
    """DeleteOrganization response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DenyOrganizationInvitationRequest(AbstractModel):
    """DenyOrganizationInvitation request structure.

    """

    def __init__(self):
        r"""
        :param Id: Invitation ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DenyOrganizationInvitationResponse(AbstractModel):
    """DenyOrganizationInvitation response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class GetOrganizationMemberRequest(AbstractModel):
    """GetOrganizationMember request structure.

    """

    def __init__(self):
        r"""
        :param MemberUin: Organization member UIN
        :type MemberUin: int
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
        


class GetOrganizationMemberResponse(AbstractModel):
    """GetOrganizationMember response structure.

    """

    def __init__(self):
        r"""
        :param Uin: Organization member UIN
        :type Uin: int
        :param Name: Organization member name
        :type Name: str
        :param Remark: Notes
        :type Remark: str
        :param JoinTime: Joining time 
        :type JoinTime: str
        :param NodeId: Organizational unit ID
        :type NodeId: int
        :param NodeName: Organizational unit name
        :type NodeName: str
        :param ParentNodeId: Parent organizational unit ID
        :type ParentNodeId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Uin = None
        self.Name = None
        self.Remark = None
        self.JoinTime = None
        self.NodeId = None
        self.NodeName = None
        self.ParentNodeId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.JoinTime = params.get("JoinTime")
        self.NodeId = params.get("NodeId")
        self.NodeName = params.get("NodeName")
        self.ParentNodeId = params.get("ParentNodeId")
        self.RequestId = params.get("RequestId")


class GetOrganizationRequest(AbstractModel):
    """GetOrganization request structure.

    """


class GetOrganizationResponse(AbstractModel):
    """GetOrganization response structure.

    """

    def __init__(self):
        r"""
        :param OrgId: Organization ID
        :type OrgId: int
        :param HostUin: Creator UIN
        :type HostUin: int
        :param Nickname: Creator's name
        :type Nickname: str
        :param Mail: Creator's email address
        :type Mail: str
        :param OrgType: Organization type
        :type OrgType: int
        :param IsEmpty: Whether the organization is empty or not 
        :type IsEmpty: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OrgId = None
        self.HostUin = None
        self.Nickname = None
        self.Mail = None
        self.OrgType = None
        self.IsEmpty = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrgId = params.get("OrgId")
        self.HostUin = params.get("HostUin")
        self.Nickname = params.get("Nickname")
        self.Mail = params.get("Mail")
        self.OrgType = params.get("OrgType")
        self.IsEmpty = params.get("IsEmpty")
        self.RequestId = params.get("RequestId")


class ListOrganizationInvitationsRequest(AbstractModel):
    """ListOrganizationInvitations request structure.

    """

    def __init__(self):
        r"""
        :param Invited: Whether to list the invitations you received or the invitations you sent. `1`: list the invitations you received; `0`: list the invitations you sent.
        :type Invited: int
        :param Offset: Offset
        :type Offset: int
        :param Limit: Limit
        :type Limit: int
        """
        self.Invited = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Invited = params.get("Invited")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationInvitationsResponse(AbstractModel):
    """ListOrganizationInvitations response structure.

    """

    def __init__(self):
        r"""
        :param Invitations: List of invitations
        :type Invitations: list of OrgInvitation
        :param TotalCount: Total number of results
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Invitations = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Invitations") is not None:
            self.Invitations = []
            for item in params.get("Invitations"):
                obj = OrgInvitation()
                obj._deserialize(item)
                self.Invitations.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListOrganizationMembersRequest(AbstractModel):
    """ListOrganizationMembers request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset
        :type Offset: int
        :param Limit: Limit
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationMembersResponse(AbstractModel):
    """ListOrganizationMembers response structure.

    """

    def __init__(self):
        r"""
        :param Members: Member list
        :type Members: list of OrgMember
        :param TotalCount: Total number of results
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Members = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Members") is not None:
            self.Members = []
            for item in params.get("Members"):
                obj = OrgMember()
                obj._deserialize(item)
                self.Members.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListOrganizationNodeMembersRequest(AbstractModel):
    """ListOrganizationNodeMembers request structure.

    """

    def __init__(self):
        r"""
        :param NodeId: Organizational unit ID
        :type NodeId: int
        :param Offset: Offset
        :type Offset: int
        :param Limit: Limit
        :type Limit: int
        """
        self.NodeId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationNodeMembersResponse(AbstractModel):
    """ListOrganizationNodeMembers response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of results
        :type TotalCount: int
        :param Members: Member list
        :type Members: list of OrgMember
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Members = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Members") is not None:
            self.Members = []
            for item in params.get("Members"):
                obj = OrgMember()
                obj._deserialize(item)
                self.Members.append(obj)
        self.RequestId = params.get("RequestId")


class ListOrganizationNodesRequest(AbstractModel):
    """ListOrganizationNodes request structure.

    """


class ListOrganizationNodesResponse(AbstractModel):
    """ListOrganizationNodes response structure.

    """

    def __init__(self):
        r"""
        :param Nodes: Organizational unit list
        :type Nodes: list of OrgNode
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Nodes = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Nodes") is not None:
            self.Nodes = []
            for item in params.get("Nodes"):
                obj = OrgNode()
                obj._deserialize(item)
                self.Nodes.append(obj)
        self.RequestId = params.get("RequestId")


class MoveOrganizationMembersToNodeRequest(AbstractModel):
    """MoveOrganizationMembersToNode request structure.

    """

    def __init__(self):
        r"""
        :param NodeId: Organizational unit ID
        :type NodeId: int
        :param Uins: Member UIN list
        :type Uins: list of int non-negative
        """
        self.NodeId = None
        self.Uins = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Uins = params.get("Uins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoveOrganizationMembersToNodeResponse(AbstractModel):
    """MoveOrganizationMembersToNode response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OrgInvitation(AbstractModel):
    """Information on an invitation to an organization.

    """

    def __init__(self):
        r"""
        :param Id: Invitation ID
        :type Id: int
        :param Uin: UIN of the invitee
        :type Uin: int
        :param HostUin: Creator UIN
        :type HostUin: int
        :param HostName: Creator's name
        :type HostName: str
        :param HostMail: Creator's email address
        :type HostMail: str
        :param Status: Invitation status. `-1`: expired; `0`: normal; `1`: accepted; `2`: invalid; `3`: cancelled
        :type Status: int
        :param Name: Name
        :type Name: str
        :param Remark: Notes
        :type Remark: str
        :param OrgType: Organization type
        :type OrgType: int
        :param InviteTime: Time of invitation
        :type InviteTime: str
        :param ExpireTime: Expiration time
        :type ExpireTime: str
        """
        self.Id = None
        self.Uin = None
        self.HostUin = None
        self.HostName = None
        self.HostMail = None
        self.Status = None
        self.Name = None
        self.Remark = None
        self.OrgType = None
        self.InviteTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uin = params.get("Uin")
        self.HostUin = params.get("HostUin")
        self.HostName = params.get("HostName")
        self.HostMail = params.get("HostMail")
        self.Status = params.get("Status")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.OrgType = params.get("OrgType")
        self.InviteTime = params.get("InviteTime")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMember(AbstractModel):
    """Information on an organization member.

    """

    def __init__(self):
        r"""
        :param Uin: UIN
        :type Uin: int
        :param Name: Name
        :type Name: str
        :param Remark: Notes
        :type Remark: str
        :param JoinTime: Joining time
        :type JoinTime: str
        """
        self.Uin = None
        self.Name = None
        self.Remark = None
        self.JoinTime = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.JoinTime = params.get("JoinTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgNode(AbstractModel):
    """Information on an organizational unit.

    """

    def __init__(self):
        r"""
        :param NodeId: Organizational unit ID
        :type NodeId: int
        :param Name: Name
        :type Name: str
        :param ParentNodeId: Parent organizational unit ID
        :type ParentNodeId: int
        :param MemberCount: Number of members
        :type MemberCount: int
        """
        self.NodeId = None
        self.Name = None
        self.ParentNodeId = None
        self.MemberCount = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Name = params.get("Name")
        self.ParentNodeId = params.get("ParentNodeId")
        self.MemberCount = params.get("MemberCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuitOrganizationRequest(AbstractModel):
    """QuitOrganization request structure.

    """

    def __init__(self):
        r"""
        :param OrgId: Organization ID
        :type OrgId: int
        """
        self.OrgId = None


    def _deserialize(self, params):
        self.OrgId = params.get("OrgId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuitOrganizationResponse(AbstractModel):
    """QuitOrganization response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SendOrganizationInvitationRequest(AbstractModel):
    """SendOrganizationInvitation request structure.

    """

    def __init__(self):
        r"""
        :param InviteUin: UIN of the invitee
        :type InviteUin: int
        :param Name: Name
        :type Name: str
        :param Remark: Notes
        :type Remark: str
        """
        self.InviteUin = None
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.InviteUin = params.get("InviteUin")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendOrganizationInvitationResponse(AbstractModel):
    """SendOrganizationInvitation response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateOrganizationMemberRequest(AbstractModel):
    """UpdateOrganizationMember request structure.

    """

    def __init__(self):
        r"""
        :param MemberUin: Member UIN
        :type MemberUin: int
        :param Name: Name
        :type Name: str
        :param Remark: Notes
        :type Remark: str
        """
        self.MemberUin = None
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationMemberResponse(AbstractModel):
    """UpdateOrganizationMember response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateOrganizationNodeRequest(AbstractModel):
    """UpdateOrganizationNode request structure.

    """

    def __init__(self):
        r"""
        :param NodeId: Organizational unit ID
        :type NodeId: int
        :param Name: Name
        :type Name: str
        :param ParentNodeId: Parent organizational unit ID
        :type ParentNodeId: int
        """
        self.NodeId = None
        self.Name = None
        self.ParentNodeId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Name = params.get("Name")
        self.ParentNodeId = params.get("ParentNodeId")
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