# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AcceptOrganizationInvitationResponse(AbstractModel):
    """AcceptOrganizationInvitation response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddOrganizationNodeRequest(AbstractModel):
    """AddOrganizationNode request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddOrganizationNodeResponse(AbstractModel):
    """AddOrganizationNode response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CancelOrganizationInvitationRequest(AbstractModel):
    """CancelOrganizationInvitation request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CancelOrganizationInvitationResponse(AbstractModel):
    """CancelOrganizationInvitation response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateOrganizationRequest(AbstractModel):
    """CreateOrganization request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateOrganizationResponse(AbstractModel):
    """CreateOrganization response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteOrganizationMemberFromNodeRequest(AbstractModel):
    """DeleteOrganizationMemberFromNode request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteOrganizationMemberFromNodeResponse(AbstractModel):
    """DeleteOrganizationMemberFromNode response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteOrganizationMembersRequest(AbstractModel):
    """DeleteOrganizationMembers request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteOrganizationMembersResponse(AbstractModel):
    """DeleteOrganizationMembers response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteOrganizationNodesRequest(AbstractModel):
    """DeleteOrganizationNodes request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteOrganizationNodesResponse(AbstractModel):
    """DeleteOrganizationNodes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteOrganizationRequest(AbstractModel):
    """DeleteOrganization request structure.

    """


class DeleteOrganizationResponse(AbstractModel):
    """DeleteOrganization response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DenyOrganizationInvitationRequest(AbstractModel):
    """DenyOrganizationInvitation request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DenyOrganizationInvitationResponse(AbstractModel):
    """DenyOrganizationInvitation response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetOrganizationMemberRequest(AbstractModel):
    """GetOrganizationMember request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetOrganizationMemberResponse(AbstractModel):
    """GetOrganizationMember response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetOrganizationRequest(AbstractModel):
    """GetOrganization request structure.

    """


class GetOrganizationResponse(AbstractModel):
    """GetOrganization response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListOrganizationInvitationsRequest(AbstractModel):
    """ListOrganizationInvitations request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListOrganizationInvitationsResponse(AbstractModel):
    """ListOrganizationInvitations response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListOrganizationMembersRequest(AbstractModel):
    """ListOrganizationMembers request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListOrganizationMembersResponse(AbstractModel):
    """ListOrganizationMembers response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListOrganizationNodeMembersRequest(AbstractModel):
    """ListOrganizationNodeMembers request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListOrganizationNodeMembersResponse(AbstractModel):
    """ListOrganizationNodeMembers response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListOrganizationNodesRequest(AbstractModel):
    """ListOrganizationNodes request structure.

    """


class ListOrganizationNodesResponse(AbstractModel):
    """ListOrganizationNodes response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MoveOrganizationMembersToNodeRequest(AbstractModel):
    """MoveOrganizationMembersToNode request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MoveOrganizationMembersToNodeResponse(AbstractModel):
    """MoveOrganizationMembersToNode response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OrgInvitation(AbstractModel):
    """Information on an invitation to an organization.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OrgMember(AbstractModel):
    """Information on an organization member.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OrgNode(AbstractModel):
    """Information on an organizational unit.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class QuitOrganizationRequest(AbstractModel):
    """QuitOrganization request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class QuitOrganizationResponse(AbstractModel):
    """QuitOrganization response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SendOrganizationInvitationRequest(AbstractModel):
    """SendOrganizationInvitation request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SendOrganizationInvitationResponse(AbstractModel):
    """SendOrganizationInvitation response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateOrganizationMemberRequest(AbstractModel):
    """UpdateOrganizationMember request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateOrganizationMemberResponse(AbstractModel):
    """UpdateOrganizationMember response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateOrganizationNodeRequest(AbstractModel):
    """UpdateOrganizationNode request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateOrganizationNodeResponse(AbstractModel):
    """UpdateOrganizationNode response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        