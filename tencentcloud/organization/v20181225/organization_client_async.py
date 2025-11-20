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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.organization.v20181225 import models
from typing import Dict


class OrganizationClient(AbstractClient):
    _apiVersion = '2018-12-25'
    _endpoint = 'organization.intl.tencentcloudapi.com'
    _service = 'organization'

    async def AcceptOrganizationInvitation(
            self,
            request: models.AcceptOrganizationInvitationRequest,
            opts: Dict = None,
    ) -> models.AcceptOrganizationInvitationResponse:
        """
        This API is used to accept an invitation to an organization.
        """
        
        kwargs = {}
        kwargs["action"] = "AcceptOrganizationInvitation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcceptOrganizationInvitationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddOrganizationNode(
            self,
            request: models.AddOrganizationNodeRequest,
            opts: Dict = None,
    ) -> models.AddOrganizationNodeResponse:
        """
        This API is used to add an organizational unit.
        """
        
        kwargs = {}
        kwargs["action"] = "AddOrganizationNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddOrganizationNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelOrganizationInvitation(
            self,
            request: models.CancelOrganizationInvitationRequest,
            opts: Dict = None,
    ) -> models.CancelOrganizationInvitationResponse:
        """
        This API is used to cancel an invitation to an organization.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelOrganizationInvitation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelOrganizationInvitationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrganization(
            self,
            request: models.CreateOrganizationRequest,
            opts: Dict = None,
    ) -> models.CreateOrganizationResponse:
        """
        This API is used to create an organization.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganization(
            self,
            request: models.DeleteOrganizationRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationResponse:
        """
        This API is used to delete an organization.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganizationMemberFromNode(
            self,
            request: models.DeleteOrganizationMemberFromNodeRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationMemberFromNodeResponse:
        """
        This API is used to delete an organization member.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganizationMemberFromNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationMemberFromNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganizationMembers(
            self,
            request: models.DeleteOrganizationMembersRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationMembersResponse:
        """
        This API is used to delete multiple organization members in a single request.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganizationMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganizationNodes(
            self,
            request: models.DeleteOrganizationNodesRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationNodesResponse:
        """
        This API is used to delete multiple organizational units in a single request.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganizationNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DenyOrganizationInvitation(
            self,
            request: models.DenyOrganizationInvitationRequest,
            opts: Dict = None,
    ) -> models.DenyOrganizationInvitationResponse:
        """
        This API is used to decline an invitation to an organization.
        """
        
        kwargs = {}
        kwargs["action"] = "DenyOrganizationInvitation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DenyOrganizationInvitationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOrganization(
            self,
            request: models.GetOrganizationRequest,
            opts: Dict = None,
    ) -> models.GetOrganizationResponse:
        """
        This API is used to obtain information on organizations.
        """
        
        kwargs = {}
        kwargs["action"] = "GetOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOrganizationMember(
            self,
            request: models.GetOrganizationMemberRequest,
            opts: Dict = None,
    ) -> models.GetOrganizationMemberResponse:
        """
        This API is used to obtain information on organization members.
        """
        
        kwargs = {}
        kwargs["action"] = "GetOrganizationMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOrganizationMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOrganizationInvitations(
            self,
            request: models.ListOrganizationInvitationsRequest,
            opts: Dict = None,
    ) -> models.ListOrganizationInvitationsResponse:
        """
        This API is used to obtain an invitation list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListOrganizationInvitations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOrganizationInvitationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOrganizationMembers(
            self,
            request: models.ListOrganizationMembersRequest,
            opts: Dict = None,
    ) -> models.ListOrganizationMembersResponse:
        """
        This API is used to obtain a list of organization members.
        """
        
        kwargs = {}
        kwargs["action"] = "ListOrganizationMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOrganizationMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOrganizationNodeMembers(
            self,
            request: models.ListOrganizationNodeMembersRequest,
            opts: Dict = None,
    ) -> models.ListOrganizationNodeMembersResponse:
        """
        This API is used to obtain a list of organizational unit members.
        """
        
        kwargs = {}
        kwargs["action"] = "ListOrganizationNodeMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOrganizationNodeMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOrganizationNodes(
            self,
            request: models.ListOrganizationNodesRequest,
            opts: Dict = None,
    ) -> models.ListOrganizationNodesResponse:
        """
        This API is used to obtain a list of organizational units.
        """
        
        kwargs = {}
        kwargs["action"] = "ListOrganizationNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOrganizationNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MoveOrganizationMembersToNode(
            self,
            request: models.MoveOrganizationMembersToNodeRequest,
            opts: Dict = None,
    ) -> models.MoveOrganizationMembersToNodeResponse:
        """
        This API is used to move members to a specified organizational unit.
        """
        
        kwargs = {}
        kwargs["action"] = "MoveOrganizationMembersToNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MoveOrganizationMembersToNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QuitOrganization(
            self,
            request: models.QuitOrganizationRequest,
            opts: Dict = None,
    ) -> models.QuitOrganizationResponse:
        """
        This API is used to quit an organization.
        """
        
        kwargs = {}
        kwargs["action"] = "QuitOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QuitOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendOrganizationInvitation(
            self,
            request: models.SendOrganizationInvitationRequest,
            opts: Dict = None,
    ) -> models.SendOrganizationInvitationResponse:
        """
        This API is used to send an invitation to join an organization.
        """
        
        kwargs = {}
        kwargs["action"] = "SendOrganizationInvitation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendOrganizationInvitationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOrganizationMember(
            self,
            request: models.UpdateOrganizationMemberRequest,
            opts: Dict = None,
    ) -> models.UpdateOrganizationMemberResponse:
        """
        This API is used to update information on organization members.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOrganizationMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOrganizationMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOrganizationNode(
            self,
            request: models.UpdateOrganizationNodeRequest,
            opts: Dict = None,
    ) -> models.UpdateOrganizationNodeResponse:
        """
        This API is used to update organizational units.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOrganizationNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOrganizationNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)